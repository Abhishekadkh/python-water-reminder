import time
import winsound
from plyer import notification

# Function to play a beep sound
def play_beep():
    winsound.Beep(1000, 500)  # 1000 Hz frequency for 500 ms

# Function to send a desktop notification
def send_reminder():
    play_beep()  # Play beep before notification
    notification.notify(
        title="Time to Drink Water 💧",
        message="Take a short break and drink a glass of water!",
        timeout=10  # Notification stays for 10 seconds
    )

# Function to run the reminder loop every hour
def start_reminder():
    interval_seconds = 3600  # 1 hour

    while True:
        print("Waiting for 1 hour before next reminder...")
        time.sleep(interval_seconds)
        send_reminder()

# Main entry point
if __name__ == "__main__":
    print("💧 Water Reminder Started! You'll be notified every hour.")
    start_reminder()
