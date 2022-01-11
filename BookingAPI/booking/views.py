from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Bookings
from .serializers import BookingSerializer

# Create your views here.
class BookingAPIView(APIView):
    def post(self,request):
        name = request.data['name']
        slot = request.data['slot']
        bookings = Bookings.objects.all()
        bookings.filter(slot=slot)
        no_of_bookings = bookings.count()
        if no_of_bookings<=2 and (slot>=0 and slot<=23):
            serializer=BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context={'status':'confirmed'}
                return Response(context)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            context={"status": "slot full, unable to save booking for "+str(name)+" in slot " + str(slot)}
            return Response(context)

    def get(self,request):
        bookings=Bookings.objects.all()
        serializer=BookingSerializer(bookings,many=True)
        return Response(serializer.data)

class BookingsCancelAPIView(APIView):
    def post(self,request):
        name=request.data['name']
        slot=request.data['slot']
        del_booking=Bookings.objects.filter(name=name)
        print(del_booking)
        if del_booking:
            del_booking.delete()
            context={"status": "canceled booking for "+str(name)+" in slot "+str(slot)}
            return Response(context)
        else:
            context = {"status": "no booking for " + str(name) + " in slot " + str(slot)}
            return Response(context)





