from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
app = Celery('main')

# Using a string here means that the worker doesn’t have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-fund': {
        'task': 'fund_manager.tasks.update_portfolios_and_navs',
        'schedule': 60.0
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
