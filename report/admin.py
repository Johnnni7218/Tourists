from django.contrib import admin
from .models import User, Coords, Mount, Photo

admin.site.register(User)
admin.site.register(Coords)
admin.site.register(Mount)
admin.site.register(Photo)
