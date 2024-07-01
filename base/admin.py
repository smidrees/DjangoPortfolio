from django.contrib import admin

from  .models import Work, Education, Projects, Contact, Certification, Language, Profile, Social
# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    list_display=("position", "start_date", "end_date", "company")

class EduAdmin(admin.ModelAdmin):
    list_display=("title", "start_date", "end_date", "institute")

class ProjAdmin(admin.ModelAdmin):
    list_display=("date", "title", "picture")

class ContactAdmin(admin.ModelAdmin):
    list_display=("email", "subject", "message")

admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EduAdmin)
admin.site.register(Projects, ProjAdmin)
admin.site.register(Contact, ContactAdmin)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title','institute')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language','proficiency')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','title',)

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("platform", "url", "username")
    
