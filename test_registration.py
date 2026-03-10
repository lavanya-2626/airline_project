import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_project.settings')
django.setup()

from apps.auth_app.services import AuthService
from django.contrib.auth.models import User

def test_registration():
    username = "testuser_" + str(os.getpid())
    email = f"{username}@example.com"
    password = "TestPassword@123"
    
    print(f"Attempting to register user: {username}...")
    try:
        user = AuthService.register_user(username, email, password)
        print(f"SUCCESS: User {user.username} (ID: {user.id}) created.")
        
        # Verify it's in the DB
        exists = User.objects.filter(username=username).exists()
        print(f"Database verification: {'FOUND' if exists else 'NOT FOUND'}")
        
    except Exception as e:
        print(f"FAILURE: {str(e)}")

if __name__ == "__main__":
    test_registration()
