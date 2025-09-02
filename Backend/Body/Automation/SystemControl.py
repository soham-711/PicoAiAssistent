# import os
# import psutil
# import pyautogui
# from datetime import datetime
# import ctypes

# class SystemControl:

#     @staticmethod
#     def shutdown(delay=0):
#         """Shutdown the system immediately or after a delay"""
#         try:
#             if delay > 0:
#                 print(f"Shutdown in {delay} seconds...")
#             os.system(f"shutdown /s /t {delay}")
#         except Exception as e:
#             print(f"Error shutting down: {e}")

#     @staticmethod
#     def restart(delay=0):
#         """Restart the system immediately or after a delay"""
#         try:
#             if delay > 0:
#                 print(f"Restart in {delay} seconds...")
#             os.system(f"shutdown /r /t {delay}")
#         except Exception as e:
#             print(f"Error restarting: {e}")

#     @staticmethod
#     def lock():
#         """Lock the system immediately"""
#         try:
#             os.system("rundll32.exe user32.dll,LockWorkStation")
#         except Exception as e:
#             print(f"Error locking system: {e}")

#     @staticmethod
#     def sleep():
#         """Put the system to sleep immediately"""
#         try:
#             print("Putting system to sleep...")
#             ctypes.windll.PowrProf.SetSuspendState(False, True, True)
#         except Exception as e:
#             print(f"Error putting system to sleep: {e}")

#     @staticmethod
#     def system_info():
#         """Display system info like CPU, RAM, Disk, Battery"""
#         try:
#             print(f"CPU Usage: {psutil.cpu_percent()}%")
#             print(f"RAM Usage: {psutil.virtual_memory().percent}%")
#             print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
#             if hasattr(psutil, "sensors_battery") and psutil.sensors_battery():
#                 battery = psutil.sensors_battery()
#                 print(f"Battery: {battery.percent}% {'Charging' if battery.power_plugged else 'Not Charging'}")
#         except Exception as e:
#             print(f"Error getting system info: {e}")

#     @staticmethod
#     def screenshot(file_name=None):
#         """Take a screenshot and save it with timestamp"""
#         try:
#             if not file_name:
#                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#                 file_name = f"screenshot_{timestamp}.png"
#             pyautogui.screenshot(file_name)
#             print(f"Screenshot saved as {file_name}")
#         except Exception as e:
#             print(f"Error taking screenshot: {e}")


# # Example usage:
# SystemControl.sleep()
# # SystemControl.shutdown(10)
# # SystemControl.restart()
# # SystemControl.lock()
# # SystemControl.system_info()
# # SystemControl.screenshot()



import os, psutil, pyautogui
from datetime import datetime
import ctypes

class SystemControl:
    @staticmethod
    def shutdown(delay=0):
        os.system(f"shutdown /s /t {delay}")

    @staticmethod
    def restart(delay=0):
        os.system(f"shutdown /r /t {delay}")

    @staticmethod
    def lock():
        os.system("rundll32.exe user32.dll,LockWorkStation")

    @staticmethod
    def sleep():
        ctypes.windll.PowrProf.SetSuspendState(False, True, True)

    @staticmethod
    def system_info():
        print(f"CPU: {psutil.cpu_percent()}%")
        print(f"RAM: {psutil.virtual_memory().percent}%")
        print(f"Disk: {psutil.disk_usage('/').percent}%")
        b = getattr(psutil, "sensors_battery", lambda: None)()
        if b: print(f"Battery: {b.percent}% {'Charging' if b.power_plugged else 'Not Charging'}")

    @staticmethod
    def screenshot(file_name=None, region=None):
        if not file_name:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"screenshot_{ts}.png"
        shot = pyautogui.screenshot(region=region) if region else pyautogui.screenshot()
        shot.save(file_name)
        print(f"Saved: {file_name}")

    # Optional: volume & brightness (works on Windows)
    @staticmethod
    def set_volume(percent: int):
        try:
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            from comtypes import CLSCTX_ALL
            from ctypes import POINTER, cast
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            vol_range = volume.GetVolumeRange()  # (min, max, step)
            new = vol_range[0] + (vol_range[1] - vol_range[0]) * (percent/100.0)
            volume.SetMasterVolumeLevel(new, None)
        except Exception as e:
            print(f"Volume set failed: {e}")

    @staticmethod
    def set_brightness(percent: int):
        try:
            import screen_brightness_control as sbc
            sbc.set_brightness(percent)
        except Exception as e:
            print(f"Brightness set failed: {e}")
