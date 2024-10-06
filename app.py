from flask import Flask, request, jsonify, render_template
import smtplib
from datetime import datetime
from threading import Timer

app = Flask(__name__)

# In-memory storage for notifications (for demonstration)
notifications = []

def send_email(email):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("bogyt09@gmail.com", "Bogy2018!") 
        message = f"Subject: Landsat Data Notification\n\nIt's time for the Landsat data update!"
        server.sendmail("bogyt09@gmail.com", email, message)
        server.quit()
        print(f"Notification sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")



def schedule_notification(email, notification_time):
    if notification_time.tzinfo is not None:
        notification_time = notification_time.replace(tzinfo=None)

    now = datetime.now()

    delay = (notification_time - now).total_seconds()
    if delay > 0:
        Timer(delay, send_email, args=[email]).start()
    print(f"Notification scheduled for {email} at {notification_time}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_notification', methods=['POST'])
def set_notification():
    data = request.get_json()
    email = data['email']
    notification_time = datetime.fromisoformat(data['time'])
    if notification_time.tzinfo is not None:
        notification_time = notification_time.replace(tzinfo=None)

    notifications.append({'email': email, 'time': notification_time})

    schedule_notification(email, notification_time)

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
