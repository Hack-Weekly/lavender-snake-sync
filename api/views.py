import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse,Http404
from api.serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.views.generic import TemplateView
from api.models import Event,Availability

User=get_user_model()
# project imports

from api.serializers import EventSerializer,AvailabilitySerializer,CreateEventSerializer,CreateAvailabilitySerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/',
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
          

    ]
   
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            body = request.body.decode('utf-8')
            data = json.loads(body)
            if 'text' not in data:
                return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)
            text = data.get('text')
            data = f'Congratulation your API just responded to POST request with text: {text}'
            return Response({'response': data}, status=status.HTTP_200_OK)
        except json.JSONDecodeError:
            return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)
    return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)

class EventView(generics.ListAPIView):
    #shows all events
    queryset = Event.objects.all()
    serializer_class = EventSerializer



class CrudEventView(APIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self,request,format=None):
        '''
        Create new event and check that inputs are valid
        '''
        serializer = CreateEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk=None,format=None):
        '''Retrieve an event using unique id:pk
           If user did not create the event, then note cannot be viewed
           If the event is anonymous then name and notes cannot be viewed
        '''
        if pk is None:
            return Response({"message":"Please enter an event id"}, status=status.HTTP_200_OK)
        event=Event.objects.get(pk=pk)
        if event.creator != request.user and event.is_public == False:
            return Response({"message":"You can not view this event"}, status=status.HTTP_200_OK)
        serializer = self.serializer_class(event)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def patch(self,request,pk,format=None):
        '''Update an existing event created by the user'''
        event = Event.objects.get(pk=pk)
        if event.creator != request.user:
            return Response({"message":"You can not edit this event"}, status=status.HTTP_200_OK)
        serializer = self.serializer_class(event,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        '''Delete an existing event created by the user'''
        event = Event.objects.get(pk=pk)
        if event.creator != request.user:
            return Response({"message":"You can not delete this event"}, status=status.HTTP_200_OK)
        event.delete()
        return Response({"message":"Event deleted"},status=status.HTTP_200_OK)


class AvailabilityView(APIView):
    #shows all availabilities
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        availabilities = Availability.objects.all()
        serializer = self.serializer_class(availabilities,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        '''Create new availability and check that inputs are valid'''
        serializer = CreateAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)