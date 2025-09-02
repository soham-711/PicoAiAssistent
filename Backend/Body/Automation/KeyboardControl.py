# import keyboard
# import pyperclip
# import time
# from typing import List, Union, Optional
# import logging
# import subprocess
# import os

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# class KeyboardControl:
#     @staticmethod
#     def type_text(text: str, delay: float = 0.01):
#         """
#         Type text character by character with optional delay
        
#         Args:
#             text (str): Text to type
#             delay (float): Delay between each character in seconds
#         """
#         try:
#             for char in text:
#                 keyboard.write(char)
#                 time.sleep(delay)
#             logging.info(f"Typed text: {text[:50]}{'...' if len(text) > 50 else ''}")
#         except Exception as e:
#             logging.error(f"Error typing text: {e}")

#     @staticmethod
#     def type_text_instant(text: str):
#         """
#         Type text instantly (all at once)
        
#         Args:
#             text (str): Text to type
#         """
#         try:
#             keyboard.write(text)
#             logging.info(f"Typed text instantly: {text[:50]}{'...' if len(text) > 50 else ''}")
#         except Exception as e:
#             logging.error(f"Error typing text instantly: {e}")

#     @staticmethod
#     def press_hotkey(*keys: str, delay: float = 0.1):
#         """
#         Press a hotkey combination
        
#         Args:
#             *keys: Key names (e.g., 'ctrl', 'alt', 's')
#             delay (float): Delay between key presses
#         """
#         try:
#             keyboard.send('+'.join(keys))
#             time.sleep(delay)
#             logging.info(f"Pressed hotkey: {'+'.join(keys)}")
#         except Exception as e:
#             logging.error(f"Error pressing hotkey {'+'.join(keys)}: {e}")

#     @staticmethod
#     def press_key(key: str, times: int = 1, delay: float = 0.1):
#         """
#         Press a single key multiple times
        
#         Args:
#             key (str): Key to press
#             times (int): Number of times to press
#             delay (float): Delay between presses
#         """
#         try:
#             for _ in range(times):
#                 keyboard.press_and_release(key)
#                 time.sleep(delay)
#             logging.info(f"Pressed key '{key}' {times} times")
#         except Exception as e:
#             logging.error(f"Error pressing key '{key}': {e}")

#     @staticmethod
#     def hold_key(key: str, duration: float = 1.0):
#         """
#         Hold a key down for specified duration
        
#         Args:
#             key (str): Key to hold
#             duration (float): Duration to hold in seconds
#         """
#         try:
#             keyboard.press(key)
#             time.sleep(duration)
#             keyboard.release(key)
#             logging.info(f"Held key '{key}' for {duration} seconds")
#         except Exception as e:
#             logging.error(f"Error holding key '{key}': {e}")

#     @staticmethod
#     def press_and_hold(*keys: str, hold_duration: float = 1.0):
#         """
#         Press and hold multiple keys simultaneously
        
#         Args:
#             *keys: Keys to press and hold
#             hold_duration (float): Duration to hold in seconds
#         """
#         try:
#             # Press all keys
#             for key in keys:
#                 keyboard.press(key)
            
#             # Hold for duration
#             time.sleep(hold_duration)
            
#             # Release all keys
#             for key in keys:
#                 keyboard.release(key)
            
#             logging.info(f"Pressed and held keys: {', '.join(keys)} for {hold_duration} seconds")
#         except Exception as e:
#             logging.error(f"Error pressing and holding keys: {e}")

#     # WINDOWS KEY FUNCTIONS
#     @staticmethod
#     def press_windows_key():
#         """Press Windows key alone"""
#         try:
#             keyboard.press_and_release('windows')
#             time.sleep(0.1)
#             logging.info("Pressed Windows key")
#         except Exception as e:
#             logging.error(f"Error pressing Windows key: {e}")

#     @staticmethod
#     def press_windows_combination(*keys: str):
#         """
#         Press Windows key combination (Windows + key)
        
#         Args:
#             *keys: Additional keys to press with Windows key
#         """
#         try:
#             combination = ['windows'] + list(keys)
#             keyboard.send('+'.join(combination))
#             time.sleep(0.2)
#             logging.info(f"Pressed Windows combination: Win+{'+'.join(keys)}")
#         except Exception as e:
#             logging.error(f"Error pressing Windows combination: {e}")

#     @staticmethod
#     def open_run_dialog():
#         """Open Windows Run dialog (Win + R)"""
#         try:
#             keyboard.send('windows+r')
#             time.sleep(0.5)
#             logging.info("Opened Run dialog")
#         except Exception as e:
#             logging.error(f"Error opening Run dialog: {e}")

#     @staticmethod
#     def open_file_explorer():
#         """Open File Explorer (Win + E)"""
#         try:
#             keyboard.send('windows+e')
#             time.sleep(1)
#             logging.info("Opened File Explorer")
#         except Exception as e:
#             logging.error(f"Error opening File Explorer: {e}")

#     @staticmethod
#     def open_settings():
#         """Open Windows Settings (Win + I)"""
#         try:
#             keyboard.send('windows+i')
#             time.sleep(1)
#             logging.info("Opened Windows Settings")
#         except Exception as e:
#             logging.error(f"Error opening Settings: {e}")

#     @staticmethod
#     def open_action_center():
#         """Open Action Center/Notifications (Win + A)"""
#         try:
#             keyboard.send('windows+a')
#             time.sleep(0.5)
#             logging.info("Opened Action Center")
#         except Exception as e:
#             logging.error(f"Error opening Action Center: {e}")

#     @staticmethod
#     def open_search():
#         """Open Windows Search (Win + S)"""
#         try:
#             keyboard.send('windows+s')
#             time.sleep(0.5)
#             logging.info("Opened Windows Search")
#         except Exception as e:
#             logging.error(f"Error opening Search: {e}")

#     @staticmethod
#     def lock_windows():
#         """Lock Windows (Win + L)"""
#         try:
#             keyboard.send('windows+l')
#             time.sleep(1)
#             logging.info("Locked Windows")
#         except Exception as e:
#             logging.error(f"Error locking Windows: {e}")

#     @staticmethod
#     def minimize_all_windows():
#         """Minimize all windows (Win + D)"""
#         try:
#             keyboard.send('windows+d')
#             time.sleep(0.5)
#             logging.info("Minimized all windows")
#         except Exception as e:
#             logging.error(f"Error minimizing windows: {e}")

#     @staticmethod
#     def show_desktop():
#         """Show desktop (Win + D) - same as minimize all"""
#         try:
#             KeyboardControl.minimize_all_windows()
#         except Exception as e:
#             logging.error(f"Error showing desktop: {e}")

#     @staticmethod
#     def open_task_view():
#         """Open Task View (Win + Tab)"""
#         try:
#             keyboard.send('windows+tab')
#             time.sleep(0.5)
#             logging.info("Opened Task View")
#         except Exception as e:
#             logging.error(f"Error opening Task View: {e}")

#     @staticmethod
#     def open_emoji_panel():
#         """Open Emoji Panel (Win + .) or (Win + ;)"""
#         try:
#             keyboard.send('windows+.')
#             time.sleep(0.5)
#             logging.info("Opened Emoji Panel")
#         except Exception as e:
#             logging.error(f"Error opening Emoji Panel: {e}")

#     @staticmethod
#     def take_screenshot():
#         """Take screenshot (Win + Shift + S)"""
#         try:
#             keyboard.send('windows+shift+s')
#             time.sleep(1)
#             logging.info("Took screenshot with Snipping Tool")
#         except Exception as e:
#             logging.error(f"Error taking screenshot: {e}")

#     @staticmethod
#     def open_game_bar():
#         """Open Xbox Game Bar (Win + G)"""
#         try:
#             keyboard.send('windows+g')
#             time.sleep(1)
#             logging.info("Opened Game Bar")
#         except Exception as e:
#             logging.error(f"Error opening Game Bar: {e}")

#     @staticmethod
#     def open_share_menu():
#         """Open Share menu (Win + H)"""
#         try:
#             keyboard.send('windows+h')
#             time.sleep(0.5)
#             logging.info("Opened Share menu")
#         except Exception as e:
#             logging.error(f"Error opening Share menu: {e}")

#     @staticmethod
#     def open_project_menu():
#         """Open Project menu (Win + P)"""
#         try:
#             keyboard.send('windows+p')
#             time.sleep(0.5)
#             logging.info("Opened Project menu")
#         except Exception as e:
#             logging.error(f"Error opening Project menu: {e}")

#     @staticmethod
#     def open_mobility_center():
#         """Open Windows Mobility Center (Win + X)"""
#         try:
#             keyboard.send('windows+x')
#             time.sleep(0.5)
#             logging.info("Opened Mobility Center")
#         except Exception as e:
#             logging.error(f"Error opening Mobility Center: {e}")

#     @staticmethod
#     def virtual_desktop_next():
#         """Switch to next virtual desktop (Win + Ctrl + Right)"""
#         try:
#             keyboard.send('windows+ctrl+right')
#             time.sleep(0.5)
#             logging.info("Switched to next virtual desktop")
#         except Exception as e:
#             logging.error(f"Error switching virtual desktop: {e}")

#     @staticmethod
#     def virtual_desktop_previous():
#         """Switch to previous virtual desktop (Win + Ctrl + Left)"""
#         try:
#             keyboard.send('windows+ctrl+left')
#             time.sleep(0.5)
#             logging.info("Switched to previous virtual desktop")
#         except Exception as e:
#             logging.error(f"Error switching virtual desktop: {e}")

#     @staticmethod
#     def new_virtual_desktop():
#         """Create new virtual desktop (Win + Ctrl + D)"""
#         try:
#             keyboard.send('windows+ctrl+d')
#             time.sleep(0.5)
#             logging.info("Created new virtual desktop")
#         except Exception as e:
#             logging.error(f"Error creating virtual desktop: {e}")

#     @staticmethod
#     def close_virtual_desktop():
#         """Close current virtual desktop (Win + Ctrl + F4)"""
#         try:
#             keyboard.send('windows+ctrl+f4')
#             time.sleep(0.5)
#             logging.info("Closed current virtual desktop")
#         except Exception as e:
#             logging.error(f"Error closing virtual desktop: {e}")

#     # STANDARD KEYBOARD FUNCTIONS (continued)
#     @staticmethod
#     def copy():
#         """Copy selected text to clipboard"""
#         try:
#             keyboard.send('ctrl+c')
#             time.sleep(0.1)
#             logging.info("Copied to clipboard")
#         except Exception as e:
#             logging.error(f"Error copying: {e}")

#     @staticmethod
#     def paste():
#         """Paste from clipboard"""
#         try:
#             keyboard.send('ctrl+v')
#             time.sleep(0.1)
#             logging.info("Pasted from clipboard")
#         except Exception as e:
#             logging.error(f"Error pasting: {e}")

#     @staticmethod
#     def cut():
#         """Cut selected text"""
#         try:
#             keyboard.send('ctrl+x')
#             time.sleep(0.1)
#             logging.info("Cut selected text")
#         except Exception as e:
#             logging.error(f"Error cutting: {e}")

#     @staticmethod
#     def save():
#         """Save current document"""
#         try:
#             keyboard.send('ctrl+s')
#             time.sleep(0.1)
#             logging.info("Saved document")
#         except Exception as e:
#             logging.error(f"Error saving: {e}")

#     @staticmethod
#     def select_all():
#         """Select all content"""
#         try:
#             keyboard.send('ctrl+a')
#             time.sleep(0.1)
#             logging.info("Selected all content")
#         except Exception as e:
#             logging.error(f"Error selecting all: {e}")

#     @staticmethod
#     def undo():
#         """Undo last action"""
#         try:
#             keyboard.send('ctrl+z')
#             time.sleep(0.1)
#             logging.info("Undid last action")
#         except Exception as e:
#             logging.error(f"Error undoing: {e}")

#     @staticmethod
#     def redo():
#         """Redo last undone action"""
#         try:
#             keyboard.send('ctrl+y')
#             time.sleep(0.1)
#             logging.info("Redid action")
#         except Exception as e:
#             logging.error(f"Error redoing: {e}")

#     @staticmethod
#     def new_tab():
#         """Open new tab"""
#         try:
#             keyboard.send('ctrl+t')
#             time.sleep(0.1)
#             logging.info("Opened new tab")
#         except Exception as e:
#             logging.error(f"Error opening new tab: {e}")

#     @staticmethod
#     def close_tab():
#         """Close current tab"""
#         try:
#             keyboard.send('ctrl+w')
#             time.sleep(0.1)
#             logging.info("Closed tab")
#         except Exception as e:
#             logging.error(f"Error closing tab: {e}")

#     @staticmethod
#     def refresh():
#         """Refresh page"""
#         try:
#             keyboard.send('f5')
#             time.sleep(0.1)
#             logging.info("Refreshed page")
#         except Exception as e:
#             logging.error(f"Error refreshing: {e}")

#     @staticmethod
#     def enter():
#         """Press Enter key"""
#         try:
#             keyboard.send('enter')
#             time.sleep(0.1)
#             logging.info("Pressed Enter")
#         except Exception as e:
#             logging.error(f"Error pressing Enter: {e}")

#     @staticmethod
#     def escape():
#         """Press Escape key"""
#         try:
#             keyboard.send('esc')
#             time.sleep(0.1)
#             logging.info("Pressed Escape")
#         except Exception as e:
#             logging.error(f"Error pressing Escape: {e}")

#     @staticmethod
#     def tab():
#         """Press Tab key"""
#         try:
#             keyboard.send('tab')
#             time.sleep(0.1)
#             logging.info("Pressed Tab")
#         except Exception as e:
#             logging.error(f"Error pressing Tab: {e}")

#     @staticmethod
#     def backspace(times: int = 1):
#         """Press Backspace key"""
#         try:
#             for _ in range(times):
#                 keyboard.send('backspace')
#                 time.sleep(0.05)
#             logging.info(f"Pressed Backspace {times} times")
#         except Exception as e:
#             logging.error(f"Error pressing Backspace: {e}")

#     @staticmethod
#     def delete(times: int = 1):
#         """Press Delete key"""
#         try:
#             for _ in range(times):
#                 keyboard.send('delete')
#                 time.sleep(0.05)
#             logging.info(f"Pressed Delete {times} times")
#         except Exception as e:
#             logging.error(f"Error pressing Delete: {e}")

#     @staticmethod
#     def arrow_key(direction: str, times: int = 1):
#         """
#         Press arrow keys
        
#         Args:
#             direction (str): 'up', 'down', 'left', 'right'
#             times (int): Number of times to press
#         """
#         try:
#             valid_directions = ['up', 'down', 'left', 'right']
#             if direction.lower() not in valid_directions:
#                 raise ValueError(f"Direction must be one of {valid_directions}")
            
#             for _ in range(times):
#                 keyboard.send(direction.lower())
#                 time.sleep(0.1)
#             logging.info(f"Pressed {direction} arrow {times} times")
#         except Exception as e:
#             logging.error(f"Error pressing arrow key: {e}")

#     @staticmethod
#     def function_key(key_number: int):
#         """
#         Press function key
        
#         Args:
#             key_number (int): F1 through F12 (1-12)
#         """
#         try:
#             if not 1 <= key_number <= 12:
#                 raise ValueError("Function key number must be between 1 and 12")
            
#             keyboard.send(f'f{key_number}')
#             time.sleep(0.1)
#             logging.info(f"Pressed F{key_number}")
#         except Exception as e:
#             logging.error(f"Error pressing function key: {e}")

#     @staticmethod
#     def write_to_clipboard(text: str):
#         """
#         Write text directly to clipboard
        
#         Args:
#             text (str): Text to write to clipboard
#         """
#         try:
#             pyperclip.copy(text)
#             time.sleep(0.1)
#             logging.info(f"Written to clipboard: {text[:50]}{'...' if len(text) > 50 else ''}")
#         except Exception as e:
#             logging.error(f"Error writing to clipboard: {e}")

#     @staticmethod
#     def read_from_clipboard() -> str:
#         """
#         Read text from clipboard
        
#         Returns:
#             str: Text from clipboard
#         """
#         try:
#             text = pyperclip.paste()
#             logging.info(f"Read from clipboard: {text[:50]}{'...' if len(text) > 50 else ''}")
#             return text
#         except Exception as e:
#             logging.error(f"Error reading from clipboard: {e}")
#             return ""

#     @staticmethod
#     def clear_clipboard():
#         """Clear clipboard contents"""
#         try:
#             pyperclip.copy('')
#             time.sleep(0.1)
#             logging.info("Cleared clipboard")
#         except Exception as e:
#             logging.error(f"Error clearing clipboard: {e}")

#     @staticmethod
#     def type_with_clipboard(text: str):
#         """
#         Type text using clipboard (useful for special characters)
        
#         Args:
#             text (str): Text to type via clipboard
#         """
#         try:
#             original_clipboard = pyperclip.paste()
#             pyperclip.copy(text)
#             time.sleep(0.1)
#             keyboard.send('ctrl+v')
#             time.sleep(0.1)
#             pyperclip.copy(original_clipboard)  # Restore original clipboard
#             logging.info(f"Typed via clipboard: {text[:50]}{'...' if len(text) > 50 else ''}")
#         except Exception as e:
#             logging.error(f"Error typing via clipboard: {e}")

#     @staticmethod
#     def wait_for_keypress(key: str, timeout: float = 10.0) -> bool:
#         """
#         Wait for a specific key to be pressed
        
#         Args:
#             key (str): Key to wait for
#             timeout (float): Maximum time to wait in seconds
            
#         Returns:
#             bool: True if key was pressed, False if timeout
#         """
#         try:
#             logging.info(f"Waiting for key '{key}' to be pressed...")
#             return keyboard.wait(key, timeout=timeout)
#         except Exception as e:
#             logging.error(f"Error waiting for key '{key}': {e}")
#             return False

#     @staticmethod
#     def record_keystrokes(duration: float = 5.0) -> List[str]:
#         """
#         Record keystrokes for specified duration
        
#         Args:
#             duration (float): Recording duration in seconds
            
#         Returns:
#             List[str]: List of recorded keystrokes
#         """
#         try:
#             recorded_keys = []
            
#             def on_key(event):
#                 if event.event_type == keyboard.KEY_DOWN:
#                     recorded_keys.append(event.name)
            
#             # Start recording
#             keyboard.hook(on_key)
#             time.sleep(duration)
#             keyboard.unhook_all()
            
#             logging.info(f"Recorded {len(recorded_keys)} keystrokes")
#             return recorded_keys
#         except Exception as e:
#             logging.error(f"Error recording keystrokes: {e}")
#             return []

#     @staticmethod
#     def simulate_typing_speed(text: str, wpm: int = 60):
#         """
#         Type text at a specific words-per-minute speed
        
#         Args:
#             text (str): Text to type
#             wpm (int): Words per minute speed
#         """
#         try:
#             # Calculate delay per character (average word = 5 characters + space)
#             delay_per_char = 60.0 / (wpm * 6)
            
#             for char in text:
#                 keyboard.write(char)
#                 time.sleep(delay_per_char)
            
#             logging.info(f"Typed at {wpm} WPM: {text[:50]}{'...' if len(text) > 50 else ''}")
#         except Exception as e:
#             logging.error(f"Error simulating typing speed: {e}")

#     @staticmethod
#     def press_media_key(key: str):
#         """
#         Press media control keys
        
#         Args:
#             key (str): Media key ('play/pause', 'next', 'previous', 'volume up', 'volume down', 'mute')
#         """
#         try:
#             media_keys = {
#                 'play/pause': 'play pause',
#                 'next': 'next track',
#                 'previous': 'previous track',
#                 'volume up': 'volume up',
#                 'volume down': 'volume down',
#                 'mute': 'volume mute'
#             }
            
#             if key.lower() not in media_keys:
#                 raise ValueError(f"Media key must be one of {list(media_keys.keys())}")
            
#             keyboard.send(media_keys[key.lower()])
#             time.sleep(0.1)
#             logging.info(f"Pressed media key: {key}")
#         except Exception as e:
#             logging.error(f"Error pressing media key: {e}")

#     @staticmethod
#     def press_special_key(key: str):
#         """
#         Press special keys
        
#         Args:
#             key (str): Special key ('home', 'end', 'page up', 'page down', 'insert', 'print screen')
#         """
#         try:
#             special_keys = ['home', 'end', 'page up', 'page down', 'insert', 'print screen']
            
#             if key.lower() not in special_keys:
#                 raise ValueError(f"Special key must be one of {special_keys}")
            
#             keyboard.send(key.lower())
#             time.sleep(0.1)
#             logging.info(f"Pressed special key: {key}")
#         except Exception as e:
#             logging.error(f"Error pressing special key: {e}")


# # Example usage and demonstration
# if __name__ == "__main__":
#     kc = KeyboardControl()
    
#     # Test various keyboard functions
#     print("Testing keyboard automation with Windows key...")
    
#     # Test Windows key functions
#     kc.press_windows_key()  # Press Windows key alone
#     time.sleep(1)
    
#     kc.open_search()  # Win + S
#     time.sleep(1)
#     kc.escape()  # Close search
    
#     kc.open_file_explorer()  # Win + E
#     time.sleep(2)
#     kc.press_hotkey('alt', 'f4')  # Close File Explorer
    
#     kc.open_run_dialog()  # Win + R
#     time.sleep(1)
#     kc.type_text("notepad")
#     kc.enter()
#     time.sleep(1)
    
#     # Type some text in Notepad
#     kc.type_text("Hello from Windows automation!")
#     kc.press_hotkey('ctrl', 's')  # Save
#     time.sleep(1)
#     kc.type_text("test_file.txt")
#     kc.enter()
#     time.sleep(1)
    
#     # Close Notepad
#     kc.press_hotkey('alt', 'f4')
    
#     print("Windows key automation test completed!")



import pyautogui, time, keyboard

class KeyboardControl:
    @staticmethod
    def type_text(text: str, interval: float = 0.02):
        pyautogui.typewrite(text, interval=interval)

    @staticmethod
    def press(*keys):
        # e.g. press("enter") or press("ctrl", "s")
        pyautogui.hotkey(*keys)

    @staticmethod
    def copy(): KeyboardControl.press("ctrl", "c")
    @staticmethod
    def cut():  KeyboardControl.press("ctrl", "x")
    @staticmethod
    def paste(): KeyboardControl.press("ctrl", "v")
    @staticmethod
    def save(): KeyboardControl.press("ctrl", "s")
    @staticmethod
    def undo(): KeyboardControl.press("ctrl", "z")
    @staticmethod
    def redo(): KeyboardControl.press("ctrl", "y")

    @staticmethod
    def register_hotkey(hotkey: str, callback):
        # hotkey e.g. "ctrl+shift+t"
        keyboard.add_hotkey(hotkey, callback)
