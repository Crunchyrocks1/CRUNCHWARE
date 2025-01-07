import time
import winsound
from plyer import notification

# Function to display a notification and play a beep
def notify():
    # Display the notification
    notification.notify(
        title='Notification Title',
        message='This is your notification message!',
        timeout=5  # Time in seconds for the notification to stay on screen
    )

    # Play a beep sound
    winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms

if __name__ == "__main__":
    # Trigger the notification and beep
    notify()
    time.sleep(2)  # Wait for 2 seconds before exiting
