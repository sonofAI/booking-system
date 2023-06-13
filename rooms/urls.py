from django.urls import path
from .views import RoomViewSet, RoomAvailabilityView, BookingCreateView, RoomBookingList

urlpatterns = [
    path('', RoomViewSet.as_view({'get': 'list'}), name='rooms'),
    path('<int:pk>/', RoomViewSet.as_view({'get': 'retrieve'}), name='room-info'),
    path('<int:room_id>/bookings', RoomBookingList.as_view(), name='room-bookings'),
    path('<int:room_id>/availability/', RoomAvailabilityView.as_view(), name='room-availability'),
    path('<int:room_id>/book/', BookingCreateView.as_view(), name='book-room'),
]