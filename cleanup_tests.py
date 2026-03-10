import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_project.settings')
django.setup()

from django.contrib.auth.models import User

def cleanup_users():
    protected = ['admin', 'demo_user']
    users = User.objects.exclude(username__in=protected)
    count = users.count()
    if count > 0:
        print(f"Deleting {count} test users...")
        users.delete()
        print("Cleanup successful.")
    else:
        print("No test users found to clean up.")

if __name__ == "__main__":
    cleanup_users()
