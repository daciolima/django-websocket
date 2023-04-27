import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')

app = Celery('admin')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_joke_5s': {
        'task': 'core.tasks.get_joke',
        'schedule': 5.0
    }
}

app.autodiscover_tasks()