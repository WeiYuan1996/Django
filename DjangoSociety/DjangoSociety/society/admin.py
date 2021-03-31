from django.contrib import admin
from society.models import Group
from society.models import Event
from society.models import People
from society.models import User
from society.models import Image

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(People)
admin.site.register(User)
admin.site.register(Image)