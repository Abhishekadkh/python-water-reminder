import time
from plyer import notification

# Function to send a desktop notification
def send_reminder():
    notification.notify(
        title="Time to Drink Water 💧",
        message="Take a short break and drink a glass of water!",
        timeout=10  # Notification stays for 10 seconds
    )

# Function to run the reminder loop every hour
def start_reminder():
    # Set the reminder interval to 1 hour (3600 seconds)
    interval_seconds = 3600  

    while True:
        print("Waiting for 1 hour before next reminder...")
        time.sleep(interval_seconds)  # Wait for 1 hour
        send_reminder()  # Send the water drinking reminder

# Main entry point
if __name__ == "__main__":
    print("💧 Water Reminder Started! You'll be notified every hour.")
    start_reminder()
    