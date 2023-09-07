import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse,Http404
from api.serializers import MyTokenObtainPairSerializer, RegisterSerializer, EventSerializer, CreateEventSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import Event

User=get_user_model()
# project imports

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


#@permission_classes([IsAuthenticated])
class CrudEventView(APIView):
    serializer_class = EventSerializer
    def post(self,request,format=None):
        '''
        Create new event and check that inputs are valid
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            is_public = serializer.data.get("is_public")
            event_start = serializer.data.get("event_start")
            event_end = serializer.data.get("event_end") 
            user = User.objects.get(user_name=self.request.user.username)
            event_note = serializer.data.get("event_note")
            anonymous = serializer.data.get("anonymous")
            event = Event(creator=user,is_public=is_public,event_start=event_start,event_end=event_end,event_note=event_note,anonymous=anonymous)
            event.save()
            return Response({"event_id":event.id},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk=None,format=None):
        '''Retrieve an event using unique id:pk
           If user did not create the event, then note cannot be viewed
           If the event is anonymous then name and notes cannot be viewed
        '''
        if not pk:
            return Response({"message":"Welcome, create a new event",},status=status.HTTP_200_OK)
        event = Event.objects.get(pk=pk)
        if event.creator == request.user:
            event = Event.objects.get(pk=pk)
        if event.anonymous and event.creator != request.user:
            event = Event.objects.filter(pk=pk).defer("event_note","name")[0]
        if event.creator != request.user and not event.anonymous:
            event = Event.objects.filter(pk=pk).defer("event_note")[0]
        serializer = self.serializer_class(event)
        return Response(serializer.data)
    
    def patch(self,request,pk,format=None):
        '''Update an existing event created by the user'''
        query_set = Event.objects.filter(pk=pk)
        serializer = self.serializer_class(data=request.data)
        if query_set.exists():
            event = query_set[0]
            print(event.creator,self.request.user)
            if event.creator != self.request.user:
                return Response({"message":"You did not create this event"},status=status.HTTP_401_UNAUTHORIZED)
            if serializer.is_valid():
                event.is_public = serializer.data.get("is_public")
                event.event_start = serializer.data.get("event_start")
                event.event_end = serializer.data.get("event_end")
                event.event_note = serializer.data.get("event_note")
                event.anonymous = serializer.data.get("anonymous")
                event.save(update_fields=["is_public","event_start","event_end","event_note","anonymous"])
                return Response({"message":"Successfully updated"},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Event Error"},status=status.HTTP_400_BAD_REQUEST)