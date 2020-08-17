from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')
    else:
            first_name = request.POST["first_name"]
            dropdown = request.POST["dropdown"]
            students = request.POST["students"]
            tel = request.POST["tel"]
            country = request.POST["country"]
            #The Email of the Person williing to register
            from_email = request.POST['from_email']
            try:
                send_mail("Student Registration","This is a registration request by " + first_name +". Their email-id is " + from_email + ". The age of the the student is:  " + students +  ". Contact information: " + tel +  ". They wish to apply for " + dropdown + " package from " + country , from_email, ['hatechz14@gmail.com','mrssohaib@hotmail.com'] )
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            try:
                send_mail("Registration Request Received", "Your registration request was received! Our team will contact you shortly.", from_email, [from_email])
            except BadHeaderError:
                return("Invalid Header Found")
            return redirect('success')

    return render(request, 'contact.html')

def success(request):
    return render(request, 'success_email_send.html')
