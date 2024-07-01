from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, request
from django.db.models import Q

from .models import Work, Education, Projects, Contact, Certification, Language, Profile, Social #to present the data dynamically from this table 
from .forms import ContactForm

def index(request):
    # profile = get_object_or_404(Profile, user=request.user)
    profile = Profile.objects.first()
    project = Projects.objects.all()    
    work = Work.objects.all()
    education = Education.objects.all()
    certification = Certification.objects.all()
    language = Language.objects.all()
    social = Social.objects.all()


    # getting data from user and storing in DB
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("index")
        else:
            form = ContactForm()
    
    context = {"work": work, "education": education, "project": project, "form":form, 'certification':certification, 'profile':profile, 'language':language, "social":social}


    # for a in profile:
    #     print(a.profile_title)

    return render(request, 'index.html', context)



def messages(request):
    contact = Contact.objects.all()
    
    #search filter by email
    q = request.GET.get("q", default="")
    contact = Contact.objects.filter(Q(email__icontains=q))
    
    
    return render(request, "messages.html", {"contact_data":contact})


# Create your views here.
