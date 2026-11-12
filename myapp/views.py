from django.shortcuts import redirect, render, get_object_or_404
from myapp.models import *
# from .models import Contact

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Save the contact form data to the database
        mycontact = Contact(name=name, email=email, subject=subject, message=message)
        mycontact.save()

        # Optionally, you can redirect to a success page or show a success message
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def error(request):
    return render(request, '404.html')

def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter.html')

def show(request):
    all = Contact.objects.all()
    return render(request, 'show.html', {'all': all})

def delete(request, id):
    contactinfo = Contact.objects.get(id=id)
    contactinfo.delete()
    return redirect('/show')

def edit(request, id):
    editappointment = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.subject = request.POST.get('subject')
        editappointment.message = request.POST.get('message')

        editappointment.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')
