# breach_checker.py

def check_email(email: str):
    email = email.lower().strip()

    mock_breaches = {
        "test@example.com": [
            {
                "date": "2022-01-15",
                "data": "Emails, Passwords"
            },
            {
                "date": "2023-07-03",
                "data": "Emails"
            }
        ],
        "john.doe@gmail.com": [
            {
                "date": "2021-08-19",
                "data": "Emails, Usernames"
            }
        ]
    }

    breaches = mock_breaches.get(email, [])

    return {
        "found": len(breaches) > 0,
        "breaches": breaches
    }
