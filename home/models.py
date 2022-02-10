from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
	sno = models.AutoField(primary_key=True)
	name =models.CharField(max_length=200)
	phone =models.CharField(max_length=13)
	email =models.EmailField()
	content =models.TextField(max_length=1000)
	timeStemp = models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return 'Message From ' + self.name + ' - ' + self.email

# extend User Model with use of (OneToOne field)
class extenduser(models.Model):
	city = models.CharField(max_length=20)
	district = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	user = models.OneToOneField(User,on_delete=models.CASCADE)

