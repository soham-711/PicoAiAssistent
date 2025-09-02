import psutil

def get_dynamic_info():
    cpu_usage = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    battery = psutil.sensors_battery()

    return {
        "cpu_usage_percent": cpu_usage,
        "ram_used_gb": round(ram.used / (1024**3), 2),
        "ram_available_gb": round(ram.available / (1024**3), 2),
        "ram_usage_percent": ram.percent,
        "disk_used_gb": round(disk.used / (1024**3), 2),
        "disk_free_gb": round(disk.free / (1024**3), 2),
        "disk_usage_percent": disk.percent,
        "battery_percent": battery.percent if battery else "N/A",
        "battery_plugged": battery.power_plugged if battery else "N/A",
    }
