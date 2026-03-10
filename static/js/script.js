// Script.js - Airline Booking System

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Registration form validation
    const registerForm = document.querySelector('form[method="POST"]');
    if (registerForm && document.querySelector('input[name="password_confirm"]')) {
        registerForm.addEventListener('submit', function(e) {
            const usernameInput = document.querySelector('input[name="username"]');
            const emailInput = document.querySelector('input[name="email"]');
            const passwordInput = document.querySelector('input[name="password"]');
            const passwordConfirmInput = document.querySelector('input[name="password_confirm"]');
            
            if (!usernameInput) return; // Not the registration form
            
            const username = usernameInput.value.trim();
            const email = emailInput.value.trim();
            const password = passwordInput.value;
            const passwordConfirm = passwordConfirmInput.value;

            if (!username || !email || !password || !passwordConfirm) {
                e.preventDefault();
                alert('Please fill in all fields');
                return false;
            }

            if (username.length < 3) {
                e.preventDefault();
                alert('Username must be at least 3 characters long');
                return false;
            }

            if (password.length < 6) {
                e.preventDefault();
                alert('Password must be at least 6 characters long');
                return false;
            }

            if (password !== passwordConfirm) {
                e.preventDefault();
                alert('Passwords do not match');
                return false;
            }

            if (!isValidEmail(email)) {
                e.preventDefault();
                alert('Please enter a valid email address');
                return false;
            }
        });
    }

    // Form validation
    const forms = document.querySelectorAll('form[novalidate]');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Real-time password match check
    const password = document.querySelector('input[name="password"]');
    const passwordConfirm = document.querySelector('input[name="password_confirm"]');
    if (password && passwordConfirm) {
        passwordConfirm.addEventListener('input', function() {
            if (this.value && password.value !== this.value) {
                this.classList.add('is-invalid');
                this.classList.remove('is-valid');
            } else if (this.value === password.value && this.value) {
                this.classList.remove('is-invalid');
                this.classList.add('is-valid');
            } else {
                this.classList.remove('is-invalid', 'is-valid');
            }
        });
    }
});

// Utility function to check valid email
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Utility function to format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

// Utility function to format date
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// Smooth scroll to elements
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
