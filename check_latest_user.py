import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_project.settings')
django.setup()

from django.contrib.auth.models import User

def check_one_user():
    user = User.objects.last()
    if user:
        print(f"Latest User: {user.username}")
        print(f"ID:   {user.id} (Type: {type(user.id)})")
        print(f"Pass: {user.password[:15]}...")
        print(f"Reg:  {user.date_joined}")
    else:
        print("No users found.")

if __name__ == "__main__":
    check_one_user()
