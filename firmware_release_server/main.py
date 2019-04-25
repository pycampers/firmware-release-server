import os
import sys

import django

# setup django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firmware_release_server.settings")
django.setup()

from django.core.management import call_command

try:
    production = sys.argv[1] == "production"
except IndexError:
    production = False

if production:
    import gunicorn.app.wsgiapp as wsgi

    call_command("migrate")
    call_command("collectstatic", "--noinput")

    # This is just a simple way to supply args to gunicorn
    sys.argv = [".", "firmware_release_server.wsgi", "--bind=0.0.0.0:80"]

    wsgi.run()
else:
    call_command("runserver")
