from django.contrib import admin
from .models import Camera, Detection, Alert, Zone, Violation

admin.site.register(Camera)
admin.site.register(Detection)
admin.site.register(Alert)
admin.site.register(Zone)
admin.site.register(Violation)