from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	sno = models.AutoField(primary_key=True)
	title =models.CharField(max_length=20)
	content =models.TextField(max_length=10000)
	author=models.CharField(max_length=25)
	views = models.IntegerField(default=0)
	slug=models.CharField(max_length=133)
	timeStemp = models.DateTimeField(blank=True)

	def __str__(self):
		return self.title + ' by ' + self.author

	def get_absolute_url(self):
		return reverse('blogPost',args=[self.slug])			


class BlogComment(models.Model):
	sno = models.AutoField(primary_key=True)
	comment = models.TextField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)		
	post = models.ForeignKey(Post,on_delete=models.CASCADE)		
	parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
	timestemp = models.DateTimeField(default=now)				

	def __str__(self):
		return self.comment[0:13] + "..." + "by " + self.user.username