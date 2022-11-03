from django.contrib import admin

# Register your models here.
from .models import Candidate
from .models import User


class AdminUser(admin.ModelAdmin):
    list_display=['name','phone','email']

class AdminCandidate(admin.ModelAdmin):
    list_display=['name','party','votes']



# Register your models here.
admin.site.register(User,AdminUser)
admin.site.register(Candidate,AdminCandidate)
