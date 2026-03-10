# ⚡ QUICK START GUIDE - Professional Airline Booking System

## 🚀 Get Started in 2 Minutes

### Step 1: Activate Environment
```powershell
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Step 2: Run Server
```bash
python manage.py runserver
```

### Step 3: Open Browser
```
http://127.0.0.1:8000/
```

---

## 🔐 Login Credentials

### Admin Panel (Full Control)
- **URL:** http://127.0.0.1:8000/admin/
- **Username:** admin
- **Password:** Admin@12345

### Demo User Account
- **Username:** demo_user
- **Password:** Demo@12345

### Other Test Accounts
- **john_doe** / John@12345
- **jane_smith** / Jane@12345

---

## 📍 Main Features

### 🏠 Homepage
```
http://127.0.0.1:8000/
```
View featured flights and start searching

### 🔍 Search Flights
```
http://127.0.0.1:8000/search/
```
Find flights by source, destination, and date

### 🎫 Book Flights
```
Click "Book Now" on any flight
Fill in passenger details
Confirm booking
```

### 📋 My Bookings
```
Login → My Bookings
View all your confirmed bookings
```

### 👤 Profile
```
Login → Profile
Update personal information
Manage preferences
```

---

## 🛠️ Admin Panel Features

### Manage Flights
```
/admin/flights/flight/
- Add/Edit/Delete flights
- Set prices and seats
- Choose aircraft type
- Toggle active status
```

### Manage Bookings
```
/admin/flights/booking/
- View all bookings
- Filter by status
- Track payments
- See passenger details
```

### View Reviews
```
/admin/flights/review/
- See flight reviews
- Manage ratings
- Read comments
```

### Send Notifications
```
/admin/flights/notification/
- Create notifications
- Send to users
- Track engagement
```

---

## 📊 Test Workflow

### 1. Register New Account
```
/register/
Fill in username, email, password
Click Register
```

### 2. Login
```
/login/
Enter credentials
Click Login
```

### 3. Search Flights
```
Go to /search/
Select source (e.g., "New York")
Select destination (e.g., "Los Angeles")
Choose date
Click Search
```

### 4. Book Flight
```
Click "Book Flight" button
Fill passenger details
Enter seat number
Click "Confirm Booking"
```

### 5. View Booking
```
Go to /booking-history/
See your confirmed booking
Check booking ID
```

### 6. Update Profile
```
Go to /profile/
Update information
Save changes
```

---

## 📝 Sample Data Included

### Flights
- 6 real airlines (American, United, Delta, Southwest, British Airways, Air France)
- Multiple routes with different prices
- Different aircraft types
- Various capacities

### Users
- 4 pre-created accounts
- Different user types
- Sample profiles

### Bookings
- Sample bookings for testing
- Different seat assignments
- Various statuses

---

## 🔧 Common Commands

```bash
# Start server
python manage.py runserver

# Create new admin user
python manage.py createsuperuser

# Load sample data
python manage.py shell < setup_sample_data.py

# Check system
python manage.py check

# View database data
python manage.py shell

# Run tests
python manage.py test
```

---

## 🐛 If Something Goes Wrong

### Issue: Can't login?
```
Solution: Create superuser
python manage.py createsuperuser
```

### Issue: Database error?
```
Solution: Apply migrations
python manage.py migrate
```

### Issue: Static files not loading?
```
Solution: Collect static
python manage.py collectstatic
```

### Issue: Virtual env not activating?
```
Solution: Recreate it
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📈 Project Structure

```
airline_project/
├── flights/              → Django app with all models
├── templates/            → HTML pages (9 files)
├── static/              → CSS and JavaScript
├── db.sqlite3           → Database
├── manage.py            → Django CLI
├── setup_sample_data.py → Sample data
├── requirements.txt     → Dependencies
└── README_PROFESSIONAL.md → Full docs
```

---

## 🎯 What You Can Do

✅ **Search Flights** - Find flights by route and date  
✅ **Book Flights** - Reserve your seat  
✅ **Manage Profile** - Update personal info  
✅ **View History** - See past bookings  
✅ **Admin Dashboard** - Manage all flights and bookings  
✅ **User Management** - Create accounts  
✅ **Notifications** - Send alerts to users  
✅ **Reviews** - Rate and review flights  

---

## 📞 Quick Help

| Problem | Solution |
|---------|----------|
| Server won't start | Check if port 8000 is available |
| Database error | Run `python manage.py migrate` |
| Can't login | Use admin/Admin@12345 |
| Lost password | Create new user |
| Missing flights | Run `python manage.py shell < setup_sample_data.py` |

---

## 🌟 Pro Tips

1. **Test with Sample Data**
   - Load sample data to see demo flights
   - Makes testing easier

2. **Use Admin for Management**
   - Add flights in admin panel
   - Update prices easily
   - Monitor bookings

3. **Mobile Responsive**
   - Works on smartphones
   - Try responsive design
   - Test mobile booking

4. **Backup Your Data**
   - Export database regularly
   - Save backups to cloud
   - Maintain data integrity

---

## 🚀 Ready to Deploy?

When you're ready for production:

1. Change `DEBUG = False` in settings
2. Use PostgreSQL instead of SQLite
3. Set up NGINX + Gunicorn
4. Enable HTTPS
5. Configure email service
6. Set up monitoring

See `DOCUMENTATION.md` for deployment details.

---

## 📡 Server is Running!

```
✅ Development Server Active
🌐 http://127.0.0.1:8000/
👨‍💼 Admin: http://127.0.0.1:8000/admin/
⏹️  Stop: Press Ctrl+C
📝 Logs: Will appear below
```

---

**🎉 You're all set! Start booking flights now! ✈️**

For full documentation, see: `DOCUMENTATION.md` or `README_PROFESSIONAL.md`

