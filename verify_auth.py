import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_project.settings')
django.setup()

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def auth_check():
    print("Verifying Core Authentication...")
    
    users_to_test = [
        ('demo_user', 'Demo@12345'),
        ('admin', 'Admin@12345'),
    ]
    
    for username, password in users_to_test:
        print(f"Auth Attempt: {username: <15} / {password: <12}...", end='')
        user = authenticate(username=username, password=password)
        if user:
            print(" [SUCCESS]")
        else:
            u_obj = User.objects.filter(username=username).first()
            if not u_obj:
                print(" [FAILED: User NOT FOUND]")
            else:
                print(f" [FAILED: Incorrect Password/Backend? User exists with ID {u_obj.id}]")

if __name__ == "__main__":
    auth_check()
