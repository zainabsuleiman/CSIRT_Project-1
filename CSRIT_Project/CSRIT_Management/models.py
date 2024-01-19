from django.db import models
import uuid
# Create your models here.

class Teams(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, blank=False, null=False)
    team= models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contacts = models.CharField(max_length=255, blank=True)
    country_flag = models.CharField(max_length=20, blank=False)
    official_team_name = models.CharField(max_length=200 , blank=False)
    member_since = models.DateField()
     
    def __str__(self):
        return self.team
    class Meta:
     db_table = 'Teams'