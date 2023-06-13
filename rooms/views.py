from datetime import datetime

from rest_framework.viewsets import ModelViewSet

from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomBookingList(generics.ListAPIView):
    serializer_class = BookingSerializer

    def list(self, request, *args, **kwargs):
        room_id = self.kwargs['room_id']
        room = Room.objects.filter(id=room_id)

        self.queryset = room
        bookings = Booking.objects.filter(room=room[0]).order_by('start')

        times = []
        for booking in bookings:
            times.append({
                'start': booking.start.strftime('%Y-%m-%d %H:%M:%S'),
                'end': booking.end.strftime('%Y-%m-%d %H:%M:%S')
            })

        return Response(times)


class BookingCreateView(APIView):
    def valid_time(self, room_id, start, end):
        time_format = '%Y-%m-%d %H:%M:%S'

        current_time = str(datetime.now())[:-7]
        current_time = datetime.strptime(current_time, time_format)

        start = datetime.strptime(start, time_format)
        end = datetime.strptime(end, time_format)

        conflicting_bookings = Booking.objects.filter(
            room_id=room_id,
            start__lt=end,
            end__gt=start,
        )
        if conflicting_bookings.exists():
            return False

        upcoming_bookings = Booking.objects.filter(
            room_id=room_id,
            start__gt=current_time
        ).order_by('start')

        if upcoming_bookings.exists():
            next_booking = upcoming_bookings.first()

            if next_booking.start < end:
                return False
        else:
            next_booking = None

        if start >= end or start < current_time:
            return False

        return True


    def post(self, request, room_id):
        resident = request.data.get('resident')
        start = request.data.get('start')
        end = request.data.get('end')

        if self.valid_time(room_id, start, end):
            booking = Booking(room_id=room_id, resident=resident, start=start, end=end)
            booking.save()

            return Response(
                {'message': 'xona muvaffaqiyatli band qilindi'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'error': 'uzr, siz tanlagan vaqtda xona band'},
                status=status.HTTP_400_BAD_REQUEST
            )


class RoomAvailabilityView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def list(self, request, *args, **kwargs):
        room_id = self.kwargs['room_id']
        room = Room.objects.filter(id=room_id)

        self.queryset = room
        bookings = Booking.objects.filter(room=room[0]).order_by('start')

        booked_times = []
        for booking in bookings:
            booked_times.append({
                'start': booking.start.strftime('%Y-%m-%d %H:%M:%S'),
                'end': booking.end.strftime('%Y-%m-%d %H:%M:%S')
            })
        
        free_times = []
        length = len(booked_times)
        for i in range(length):
            if i != length - 1:
                free_times.append({
                    'start': booked_times[i]['end'],
                    'end': booked_times[i+1]['start']
                })
            else:
                free_times.append({
                    'start': booked_times[i]['end'],
                    'end': booked_times[i]['end'][:-9] + ' 23:59:59'
                })
        
        return Response(free_times)