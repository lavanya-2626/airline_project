import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_project.settings')
django.setup()

from django.contrib.auth.models import User
from apps.users.models import UserProfile

def full_check():
    print("Full Database Audit...")
    users = User.objects.all()
    print(f"Total Users Found: {users.count()}")
    for user in users:
        p_exists = UserProfile.objects.filter(user=user).exists()
        print(f"User: {user.username: <15} | Email: {user.email: <25} | Profile: {'[OK]' if p_exists else '[MISSING]'}")

if __name__ == "__main__":
    full_check()
