import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_project.settings')
django.setup()

from django.contrib.auth.models import User
from apps.users.models import UserProfile

def check_users():
    print("Checking Database Users...")
    users = User.objects.all()
    print(f"Total Users: {users.count()}")
    for user in users:
        print(f" - {user.username} (Email: {user.email}, Is Superuser: {user.is_superuser})")
        profile = UserProfile.objects.filter(user=user).first()
        if profile:
            print(f"   Profile exists: Nationality: {profile.nationality}")
        else:
            print(f"   Profile MISSING")

if __name__ == "__main__":
    check_users()
