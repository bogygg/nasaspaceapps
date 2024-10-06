import smtplib

def test_email():
    try:
        server = smtplib.SMTP('smtp.your-email-provider.com', 587)
        server.starttls()
        server.login("your_email@example.com", "your_password")
        message = "Subject: Test Email\n\nThis is a test email."
        server.sendmail("your_email@example.com", "recipient@example.com", message)
        server.quit()
        print("Test email sent successfully")
    except Exception as e:
        print(f"Failed to send test email: {e}")

test_email()
