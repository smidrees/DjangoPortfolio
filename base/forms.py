from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        #fields = ("","","",) # to include fields manually
        exclude = ()
        

