# 🔐 Email Breach Checker

A simple Flask-based web application that checks whether an email address has appeared in known data breaches.

This project is built as a **learning-focused clone** inspired by *Have I Been Pwned (HIBP)*, using **mock breach data** instead of real breach records.

---

## ✨ Features
- Web interface to submit an email address
- Displays whether the email was found in any breaches
- Shows breach date and type of exposed data
- Clean UI with clear safe / breached indicators
- Mock data implementation for ethical and cost-free testing

---

## 🛠 Tech Stack
- **Python**
- **Flask**
- **HTML (Jinja2 templates)**
- **CSS**
- **Git & GitHub**

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yashmita-sudhir/email-breach-checker.git
cd email-breach-checker
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
pip install flask
python3 app.py
http://127.0.0.1:5000
Test Emails
Use these sample emails to test the application:

| Email                | Result   |
| -------------------- | -------- |
| `test@example.com`   | Breached |
| `john.doe@gmail.com` | Breached |
| `safe@domain.com`    | Safe     |

About the Data Source
This project does NOT use real breach data.
Why mock data?
The official Have I Been Pwned API requires a paid subscription
As a student project, the goal was to:
Learn Flask routing & templating
Understand backend logic
Practice ethical handling of breach-related data
Using mock data avoids:
Exposing real user information
API rate limits and costs
Misuse of sensitive datasets
This design choice keeps the project ethical, legal, and accessible while still demonstrating real-world logic.

🙏 Credits
Inspired by Have I Been Pwned by Troy Hunt
https://haveibeenpwned.com
This project is not affiliated with or endorsed by HIBP.
##This project is for educational purposes only.##
