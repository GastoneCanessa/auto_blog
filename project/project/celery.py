import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'generate-daily-post-every-day': {
        'task': 'app.views.generate_post',  # il percorso al tuo task
        'schedule': crontab(hour=10, minute=10), 
    },
}