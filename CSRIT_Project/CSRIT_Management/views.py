from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import TeamSerializer , CreateTeamSerializers , TeamModelSerializer , UpdateTeamSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Teams

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
class TeamAPIView(GenericAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    """
    a view for creating team 
    """
    #create new team
    @swagger_auto_schema(operation_summary="Create Team",operation_description="this is a function for creating a team")
    def post(self,*args, **kwargs):
        serializer = CreateTeamSerializers(
            data=self.request.data)
        if serializer.is_valid():
            team = serializer.Create_team()
            team_serializer = None
            team_serializer = TeamSerializer(team)
            return Response(team_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(operation_summary="List Teams",operation_description="this is a function for getting all teams")   
    def get(self, *args, **kwargs):
        team = Teams.objects.all()
        team_serializer = TeamModelSerializer(team, many=True)
        return Response(team_serializer.data,  status=status.HTTP_200_OK)
class team_details(GenericAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]
    #function for getting team by uuid
    @swagger_auto_schema(operation_summary="Get team by uuid",operation_description="this is a function for returning a team using uuid")
    def get(self, *args, **kwargs):
         one_team = get_object_or_404(
            Teams, uuid=self.kwargs['uuid'])
         one_team_serializer = TeamModelSerializer(one_team,many=False)
         return Response(one_team_serializer.data, status=status.HTTP_200_OK)
    
     #function for updating team by uuid
    @swagger_auto_schema(operation_summary="Update team by uuid",operation_description="this is a function for updating a team using uuid")
    def put(self, *args, **kwargs):
        update_one_team = get_object_or_404(
            Teams, uuid=self.kwargs['uuid'])
        team_serializer = None
        serializer =UpdateTeamSerializer(data=self.request.data)
        if serializer.is_valid():
           team = serializer.update_team(update_one_team)
           team_serializer = TeamSerializer(team)
           return Response(team_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(team_serializer.errors,status=status.HTTP_404_NOT_FOUND)
    # function for deleting one team by uuid
    @swagger_auto_schema(operation_summary="Update team by uuid",operation_description="this is a function for updating a team using uuid")
    def delete(self,*args, **kwargs):
         delete_one_team = get_object_or_404(
            Teams, uuid=self.kwargs['uuid'])
         delete_one_team.delete()
         return Response("Team deleted successfully",status=status.HTTP_200_OK)


