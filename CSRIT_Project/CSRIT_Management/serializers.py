from rest_framework import  serializers
from .models import Teams


# serializer for creating new team
class CreateTeamSerializers(serializers.Serializer):
    team= serializers.CharField()
    location = serializers.CharField()
    contacts = serializers.CharField()
    country_flag = serializers.CharField()
    official_team_name = serializers.CharField()
    member_since = serializers.DateField()
    #method of creating new team
    def Create_team(self):
        newteam = Teams()
        newteam.team =self.validated_data.get("team")
        newteam.location = self.validated_data.get("location")
        newteam.contacts = self.validated_data.get("contacts")
        newteam.country_flag = self.validated_data.get("country_flag")
        newteam.official_team_name = self.validated_data.get("official_team_name")
        newteam.member_since = self.validated_data.get("member_since")
        newteam.save()
        return newteam
class TeamSerializer(serializers.Serializer):
    # uuid = serializers.UUIDField()
    team= serializers.CharField()
    location = serializers.CharField()
    contacts = serializers.CharField()
    country_flag = serializers.CharField()
    official_team_name = serializers.CharField()
    member_since = serializers.DateField()
class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
      model = Teams
      fields ='__all__'
# serializer for uppdating one of the team using uuid
class UpdateTeamSerializer(serializers.Serializer):
    team= serializers.CharField()
    location = serializers.CharField()
    contacts = serializers.CharField()
    country_flag = serializers.CharField()
    official_team_name = serializers.CharField()
    member_since = serializers.DateField()
    def update_team(self,team):
        
        team.team = self.validated_data.get("team")
        team.location = self.validated_data.get("location")
        team.contacts = self.validated_data.get("contacts")
        team.country_flag = self.validated_data.get("country_flag")
        team.official_team_name = self.validated_data.get("official_team_name")
        team.member_since = self.validated_data.get("member_since")
        team.save()
        return team
