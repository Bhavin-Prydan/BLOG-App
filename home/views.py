from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Post


from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# Create your views here.
def home(request):
	return render(request,'home/home.html')


def about(request):
	return render(request,'home/about.html')
	

def contact(request):
	if request.method == 'POST':
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		content=request.POST['content']
		print(name,email,phone,content)

		if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<5 :
			messages.error(request,'Please fill the form corectlly')
		else:	
			contact=Contact(name=name,email=email,phone=phone,content=content)
			contact.save()
			messages.success(request,'Your message has been successfully sent')	
	return render(request,'home/contact.html')
			
def search(request):
	query = request.GET['query']
	if len(query)>50:
		allposts=Post.objects.none()
	else:	
		allpostTitle = Post.objects.filter(title__icontains=query)
		allpostContent = Post.objects.filter(content__icontains=query)
		allposts = allpostTitle.union(allpostContent)

	if allposts.count() == 0:
		messages.warning(request,'No search result found. please refine your query.')	
	
	param={'allposts':allposts,'query':query}
	return render(request,'home/search.html',param)			

def handlesignup(request):
	if request.method == 'POST':
		username = request.POST['username']
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		if len(username)>10:
			messages.error(request,"username must be under 10 characters")
			return redirect('home')

		if not username.isalnum():
			messages.error(request,"username should only contain letters and numbers")
			return redirect('home')
				
		if pass1 != pass2:
			messages.error(request,"passwords do not match")
			return redirect('home')	


		myuser = User.objects.create_user(username,email,pass1)
		myuser.first_name=fname
		myuser.last_name=lname
		myuser.save()
		messages.success(request,"Your iCoder account has been successfully created")
		return redirect('home')
	else:
		return HttpResponse('404 - Not Found')	

def handlelogin(request):
	if request.method == 'POST':
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']
		
		user = 	authenticate(username=loginusername,password=loginpassword)

		if user is not None:
			login(request,user)
			messages.success(request,"Successfully Logged In")
			return redirect('home')
		else:
			messages.error(request,"Invalid Credentials , Please Try Again")
			return redirect('home')
				
	return HttpResponse('404 - Not Found')		


def handlelogout(request):
	logout(request)
	messages.success(request,"Successfully Logged Out")
	return redirect('home')




def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'iCoder',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'bhavinasodariya2911@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')	
					return redirect ("/password_reset/done/")
			messages.error(request, 'An invalid email has been entered.')		
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset/password_reset.html", context={"password_reset_form":password_reset_form})

	