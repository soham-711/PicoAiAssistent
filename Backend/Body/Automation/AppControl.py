import os
import subprocess
import time
import psutil
import pygetwindow as gw
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AppControl:
    @staticmethod
    def open_app(app_path):
        """
        Open an application with robust error handling
        
        Args:
            app_path (str): Path or name of the application to open
        """
        try:
            # Check if app is already running
            app_name = os.path.basename(app_path)
            if AppControl._is_process_running(app_name):
                logging.info(f"{app_name} is already running")
                return True
            
            # Open the application
            subprocess.Popen(app_path, shell=True)
            logging.info(f"Opened {app_path}")
            
            # Wait for application to start
            time.sleep(2)
            return True
            
        except FileNotFoundError:
            logging.error(f"Application not found: {app_path}")
            return False
        except PermissionError:
            logging.error(f"Permission denied to open: {app_path}")
            return False
        except Exception as e:
            logging.error(f"Error opening {app_path}: {e}")
            return False

    @staticmethod
    def close_app(app_name):
        """
        Close an application with multiple fallback methods
        
        Args:
            app_name (str): Name of the application process to close
        """
        try:
            # Normalize app name (remove .exe if present, then add .exe for consistency)
            if app_name.lower().endswith('.exe'):
                process_name = app_name.lower()
            else:
                process_name = f"{app_name.lower()}.exe"
            
            # Method 1: Using psutil (more reliable)
            closed = False
            for proc in psutil.process_iter(['name', 'pid']):
                try:
                    if proc.info['name'].lower() == process_name:
                        proc.terminate()
                        proc.wait(timeout=3)  # Wait for process to terminate
                        logging.info(f"Closed {app_name} (PID: {proc.info['pid']})")
                        closed = True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                    continue
            
            # Method 2: Fallback to taskkill if psutil fails
            if not closed:
                result = subprocess.run(['taskkill', '/f', '/im', app_name], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0 or "not found" not in result.stderr:
                    logging.info(f"Closed {app_name} using taskkill")
                    closed = True
                else:
                    logging.warning(f"{app_name} was not running or could not be closed")
            
            return closed
            
        except Exception as e:
            logging.error(f"Error closing {app_name}: {e}")
            return False

    @staticmethod
    def switch_window(title, partial_match=True, wait_time=5):
        """
        Switch to a window with the given title
        
        Args:
            title (str): Window title to search for
            partial_match (bool): Whether to allow partial title matches
            wait_time (int): Maximum time to wait for window to appear (seconds)
        """
        try:
            start_time = time.time()
            window = None
            
            # Wait for window to appear
            while time.time() - start_time < wait_time and window is None:
                try:
                    if partial_match:
                        # Get all windows and check for partial title match
                        all_windows = gw.getAllTitles()
                        for win_title in all_windows:
                            if title.lower() in win_title.lower():
                                windows = gw.getWindowsWithTitle(win_title)
                                if windows:
                                    window = windows[0]
                                    break
                    else:
                        # Exact title match
                        windows = gw.getWindowsWithTitle(title)
                        if windows:
                            window = windows[0]
                    
                    if window:
                        window.activate()
                        # Bring to front and maximize for better focus
                        window.restore()
                        window.maximize()
                        logging.info(f"Switched to window: {title}")
                        return True
                    
                    time.sleep(0.5)  # Wait before retrying
                    
                except IndexError:
                    continue
                except Exception:
                    continue
            
            logging.warning(f"Window not found: {title}")
            return False
            
        except Exception as e:
            logging.error(f"Error switching to {title}: {e}")
            return False

    @staticmethod
    def _is_process_running(process_name):
        """
        Check if a process is currently running
        
        Args:
            process_name (str): Name of the process to check
            
        Returns:
            bool: True if process is running, False otherwise
        """
        try:
            if not process_name.lower().endswith('.exe'):
                process_name += '.exe'
            
            for proc in psutil.process_iter(['name']):
                if proc.info['name'].lower() == process_name.lower():
                    return True
            return False
        except:
            return False

    @staticmethod
    def get_running_apps():
        """
        Get list of currently running applications
        
        Returns:
            list: List of running application names
        """
        try:
            apps = []
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] and proc.info['name'].endswith('.exe'):
                    apps.append(proc.info['name'])
            return sorted(set(apps))
        except Exception as e:
            logging.error(f"Error getting running apps: {e}")
            return []

    @staticmethod
    def wait_for_window(title, timeout=10):
        """
        Wait for a specific window to appear
        
        Args:
            title (str): Window title to wait for
            timeout (int): Maximum time to wait (seconds)
            
        Returns:
            bool: True if window appeared, False otherwise
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if AppControl.switch_window(title, partial_match=True, wait_time=1):
                return True
            time.sleep(0.5)
        return False


# Example usage and testing
if __name__ == "__main__":
    # Test the AppControl class
    app = AppControl()
    
    # Example 1: Open Notepad
    print("Opening Notepad...")
    app.open_app("notepad.exe")
    
    # Wait for Notepad to open
    time.sleep(2)
    
    # Example 2: Switch to Notepad window (with partial matching)
    print("Switching to Notepad...")
    app.switch_window("Notepad", partial_match=True)
    
    # Example 3: Wait a bit then close Notepad
    time.sleep(3)
    print("Closing Notepad...")
    app.close_app("notepad.exe")
    
    # Example 4: Get running applications
    print("Running applications:", app.get_running_apps()[:5])  # Show first 5




# import os, psutil, subprocess, time
# import pygetwindow as gw
# from Config.Settings import APP_ALIASES

# class AppControl:
#     @staticmethod
#     def open_app(name_or_path: str) -> bool:
#         cmd = APP_ALIASES.get(name_or_path.lower(), name_or_path)
#         try:
#             # os.startfile handles files/shortcuts; subprocess handles plain exe/commands
#             try:
#                 os.startfile(cmd)  # works for files and registered apps
#             except OSError:
#                 subprocess.Popen(cmd, shell=True)  # works for exe/commands on PATH
#             return True
#         except Exception:
#             return False

#     @staticmethod
#     def close_app(process_name: str) -> bool:
#         ok = False
#         pn = process_name.lower()
#         for p in psutil.process_iter(["pid", "name"]):
#             try:
#                 if pn in (p.info["name"] or "").lower():
#                     psutil.Process(p.info["pid"]).kill()
#                     ok = True
#             except Exception:
#                 pass
#         return ok

#     @staticmethod
#     def get_window_titles():
#         return [t for t in gw.getAllTitles() if t.strip()]

#     @staticmethod
#     def bring_to_front(title_substr: str) -> bool:
#         for t in AppControl.get_window_titles():
#             if title_substr.lower() in t.lower():
#                 win = gw.getWindowsWithTitle(t)[0]
#                 try:
#                     win.activate()
#                 except Exception:
#                     win.minimize(); time.sleep(0.1); win.restore()
#                 return True
#         return False

#     @staticmethod
#     def minimize(title_substr: str) -> bool:
#         for t in AppControl.get_window_titles():
#             if title_substr.lower() in t.lower():
#                 gw.getWindowsWithTitle(t)[0].minimize()
#                 return True
#         return False

#     @staticmethod
#     def maximize(title_substr: str) -> bool:
#         for t in AppControl.get_window_titles():
#             if title_substr.lower() in t.lower():
#                 gw.getWindowsWithTitle(t)[0].maximize()
#                 return True
#         return False

#     @staticmethod
#     def open_file(path: str) -> bool:
#         try:
#             os.startfile(path)
#             return True
#         except Exception:
#             return False
