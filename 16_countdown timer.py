# sample by AI
import time
import sys

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def countdown_timer(total_seconds):
    try:
        while total_seconds > 0:
            sys.stdout.write("\r⏳ Countdown: " + format_time(total_seconds))
            sys.stdout.flush()
            time.sleep(1)
            total_seconds -= 1

        sys.stdout.write("\r⏰ Countdown: 00:00:00\n")
        print("✅ Timer completed successfully!")

    except KeyboardInterrupt:
        print("\n❌ Timer stopped manually.")

def main():
    print("=== Countdown Timer (HH:MM:SS) ===")

    hours = int(input("Enter hours   : "))
    minutes = int(input("Enter minutes : "))
    seconds = int(input("Enter seconds : "))

    if minutes >= 60 or seconds >= 60 or hours < 0:
        print("❌ Invalid time format")
        return

    total_seconds = hours * 3600 + minutes * 60 + seconds

    if total_seconds <= 0:
        print("❌ Time must be greater than zero")
        return

    countdown_timer(total_seconds)

if __name__ == "__main__":
    main()

# ex 1
import time 
my_time = int(input(f"Enter the time in seconds : "))
for x in range (0, my_time):
    print(x)
    time.sleep(1)
print("TIME'S UP!")

my_time = int(input(f"Enter the time in seconds : "))
for x in reversed(range (0, my_time)):
    print(x)
    time.sleep(1)
print("TIME'S UP!")



for x in range(my_time , 0 , -1):
    seconds = x % 60
    minute = int(x /60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minute:02}:{seconds:02}")
    time.sleep(1)

time.sleep(3)
print(f"times up")