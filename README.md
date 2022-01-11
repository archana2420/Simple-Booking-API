# Simple-Booking-API
A web application (only API, no UI) in Python 3 that can be used as a scheduler. The server will maintain fixed slots of 1 hour starting from 12 AM (so, slots would be 0, 1, 2, .. 23 where each number represents the starting hour of the slot) and would accept bookings. Each slot can have maximum 2 bookings. Subsequent requests for the same slot would fail unless a booking is canceled. Implement two endpoints:

POST /booking - Given a name and slot number, save the details if space is available in the slot, else return error.
POST /cancel - Given a name and slot number, delete the booking if available else return error.
GET /booking - Show all bookings
