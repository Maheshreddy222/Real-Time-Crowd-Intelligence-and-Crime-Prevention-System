from django.shortcuts import render

def dashboard(request):
    return render(request, 'monitor/dashboard.html')
def cameras(request):
    return render(request, 'monitor/cameras.html')

def alerts(request):
    return render(request, 'monitor/alerts.html')

def analytics(request):
    return render(request, 'monitor/analytics.html')

def profile(request):
    return render(request, 'monitor/profile.html')

def notifications(request):
    return render(request, 'monitor/notifications.html')
def detection(request):
    return render(request, 'monitor/detection.html')
def users(request):
    return render(request, 'monitor/users.html')

def security(request):
    return render(request, 'monitor/security.html')

def settings(request):
    return render(request, 'monitor/settings.html')

def search(request):
    return render(request, 'monitor/search.html')

def logout_view(request):
    return render(request, 'monitor/logout.html')
from django.shortcuts import render
from .models import Camera, Detection, Alert, Zone, Violation

def dashboard(request):
    cameras = Camera.objects.all()
    
    # 👥 People Detected (sum of all detections)
    total_people = sum([d.people_count for d in Detection.objects.all()])
    
    # 🚨 Active Alerts
    alerts = Alert.objects.all().order_by('-timestamp')
    active_alerts = alerts.count()
    
    # 🛡 Zones Secured
    zones_secured = Zone.objects.filter(is_secured=True).count()
    
    # ⚠ Safety Violations
    violations = Violation.objects.count()

    # Recent Alerts (for right panel)
    recent_alerts = alerts[:5]

    return render(request, 'monitor/dashboard.html', {
        'total_people': total_people,
        'active_alerts': active_alerts,
        'zones_secured': zones_secured,
        'violations': violations,
        'cameras': cameras,
        'recent_alerts': recent_alerts,
    })


import json
from .models import Detection, Alert, Camera

def load_kaggle_data(request):
    camera = Camera.objects.first()

    # Load detections
    with open('monitor/data/output.json') as f:
        data = json.load(f)

    for item in data:
        Detection.objects.create(
            camera=camera,
            object_type=item['object'],
            confidence=item['confidence'],
            people_count=1
        )

    # Load alerts
    with open('monitor/data/alerts.json') as f:
        alerts = json.load(f)

    for a in alerts:
        Alert.objects.create(
            camera=camera,
            title="AI Alert",
            message=a['alert'],
            severity="High"
        )

    