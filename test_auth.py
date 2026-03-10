import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_project.settings')
django.setup()

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def test_auth():
    username = "uitester_auth"
    email = "ui@example.com"
    password = "SecretPassword@456"
    
    print(f"1. Registering user: {username}")
    if User.objects.filter(username=username).exists():
        User.objects.filter(username=username).delete()
        print("   Deleted existing user for clean test.")
        
    User.objects.create_user(username=username, email=email, password=password)
    print("   Created successfully.")
    
    print(f"2. Testing authentication for {username}...")
    user = authenticate(username=username, password=password)
    
    if user:
        print(f"   SUCCESS: Authenticated as {user.username}")
    else:
        print("   FAILURE: Authentication returned None")

if __name__ == "__main__":
    test_auth()
