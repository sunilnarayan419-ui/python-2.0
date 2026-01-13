# Python Alarm Clock

import time
import datetime
import pygame   


def set_alarm(alarm_time):
    print(f"⏰ Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"

    # Initialize pygame mixer ONCE
    pygame.mixer.init()

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")

        if current_time == alarm_time:
            print("🔔 WAKE UP!!! 🔔")

            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Keep program alive while music is playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break  # Stop alarm after playing once

        time.sleep(1)


# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
