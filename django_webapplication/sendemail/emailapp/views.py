from django.shortcuts import render
from . import models
import smtplib

# Create your views here.
def send_an_email(request):
    print ("Request is ",request)
    if request.method == 'POST':
        if request.POST ['emailid'] and request.POST['emailsubject'] and request.POST['emailbody']:
            post = models.EmailModel()
            post.emailid = request.POST['emailid']
            post.emailsubject = request.POST['emailsubject']
            post.emailbody = request.POST['emailbody']
            post.save()
            message = 'Subject: {}\n\n{}'.format(post.emailsubject, post.emailbody)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('email', 'pwd')
            mail.sendmail('test@test.com', post.emailid, message )
            mail.close()
            return render(request, 'emailapp/sendemailpage.html', {'msg': 'Success!'})
        else:
            return render(request, 'emailapp/sendemailpage.html', {'msg': 'Error!'})
    else:
        return render(request, 'emailapp/sendemailpage.html', {'msg': 'Invalid request!'})
