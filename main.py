from time import sleep
import psutil
from win10toast import ToastNotifier

script_name = "Power Level Notify"

def main(low_warning=20, high_warning=80, interval=20, toast_duration=60):
    toaster = ToastNotifier()
    last_level = (low_warning + high_warning) * 0.5
    while True:
        battery = psutil.sensors_battery()

        try:
            new_level = battery.percent
        except AttributeError:
            toaster.show_toast(script_name, "Could not find the computer's battery!")
            exit(1)

        if new_level <= low_warning and last_level > low_warning:
            toaster.show_toast(script_name, f"Power level is below {new_level}%",
                                duration=toast_duration, threaded=True)
        elif new_level >= high_warning and last_level < high_warning:
            toaster.show_toast(script_name, f"Power level is above {new_level}%",
                                duration=toast_duration, threaded=True)

        last_level = new_level

        sleep(interval)

if __name__ == "__main__":
    main()
