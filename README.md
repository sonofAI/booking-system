# Room Booking API

The Room Booking System is a web application that allows users to book rooms for various purposes, such as meetings, conferences, or team collaborations. It provides an API for managing rooms and bookings, allowing seamless integration with other systems.

## Features

- View a list of available rooms.
- Create a new booking for a specific room.
- Retrieve a list of bookings for a room.
- Validate bookings to avoid conflicts with existing bookings.
- Check room availability.

## Technologies Used

- Django
- Django REST Framework
- SQLite

# API Endpoints
- `GET /api/rooms/`: Get a list of all rooms.
- `GET /api/rooms/{room_id}/`: Get information about specific room by id.
- `GET /api/rooms/{room_id}/bookings/`: Get a list of created bookings for a specific room.
- `GET /api/rooms/{room_id}/availability/`: Get a list of available times for a specific room.
- `POST /api/rooms/{room_id}/book/`: Book a room by id.