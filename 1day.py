#01 day - one line
import psutil, time
while True:
    print(f"CPU {psutil.cpu_percent()}%")
    time.sleep(5)

