from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class User(AbstractUser):
  user_uuid = models.UUIDField(
         default = uuid.uuid4,
         editable = False)
  username = models.CharField(max_length=200,unique=True)
  email = models.EmailField(
      verbose_name='Email',
      max_length=255
  )
  password = models.CharField(max_length=200)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  phoneNumber = models.CharField(max_length=200)


  USERNAME_FIELD = 'username'
 
  class Meta:
     db_table = 'Users'