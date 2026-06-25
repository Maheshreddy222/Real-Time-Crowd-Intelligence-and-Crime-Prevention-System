from django.db import models

# 📷 Camera
class Camera(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# 👥 People Count / Detection
class Detection(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    people_count = models.IntegerField(default=0)
    object_type = models.CharField(max_length=100, blank=True)
    confidence = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)


# 🚨 Alerts
class Alert(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    severity = models.CharField(max_length=20)  # Low / Medium / High
    timestamp = models.DateTimeField(auto_now_add=True)


# 🛡 Zones
class Zone(models.Model):
    name = models.CharField(max_length=100)
    is_secured = models.BooleanField(default=True)


# ⚠ Safety Violations
class Violation(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)