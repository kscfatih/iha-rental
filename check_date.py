import os
import django

# Django projenizin ana dizinini belrtin
django_project_dir = '/home/iha'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iha.settings")  # Django projenizin adını buraya ekleyin
django.setup()

from management.tasks import delete_expired_ihas

import time

while True:
    delete_expired_ihas()
    time.sleep(10)  # Her saatte bir çalıştır
