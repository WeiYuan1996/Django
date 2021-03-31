from django.contrib import admin
from social_app_2021.models import UserProfile
from social_app_2021.models import Group
from social_app_2021.models import Event
from social_app_2021.models import Feed

admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Feed)

# Register your models here.
