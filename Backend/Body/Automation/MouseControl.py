# import pyautogui
# import time
# import math
# import random
# from typing import Tuple, List, Optional, Union
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Safety feature - fail safe
# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.1  # Default pause between actions

# class MouseControl:
#     # Screen information
#     screen_width, screen_height = pyautogui.size()
    
#     @staticmethod
#     def get_screen_size() -> Tuple[int, int]:
#         """Get screen width and height"""
#         return pyautogui.size()
    
#     @staticmethod
#     def get_current_position() -> Tuple[int, int]:
#         """Get current mouse position"""
#         return pyautogui.position()
    
#     @staticmethod
#     def move(x: int, y: int, duration: float = 0.5, tween: str = 'linear'):
#         """
#         Move mouse to specific coordinates
        
#         Args:
#             x (int): X coordinate
#             y (int): Y coordinate
#             duration (float): Movement duration in seconds
#             tween (str): Tweening function for movement
#         """
#         try:
#             pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.__dict__.get(tween, pyautogui.linear))
#             logging.info(f"Moved to coordinates: ({x}, {y})")
#         except Exception as e:
#             logging.error(f"Error moving mouse: {e}")
    
#     @staticmethod
#     def move_relative(dx: int, dy: int, duration: float = 0.5):
#         """
#         Move mouse relative to current position
        
#         Args:
#             dx (int): X distance to move
#             dy (int): Y distance to move
#             duration (float): Movement duration in seconds
#         """
#         try:
#             pyautogui.moveRel(dx, dy, duration=duration)
#             logging.info(f"Moved relative: ({dx}, {dy})")
#         except Exception as e:
#             logging.error(f"Error moving mouse relatively: {e}")
    
#     @staticmethod
#     def move_to_center(duration: float = 0.5):
#         """Move mouse to screen center"""
#         try:
#             center_x = MouseControl.screen_width // 2
#             center_y = MouseControl.screen_height // 2
#             MouseControl.move(center_x, center_y, duration)
#             logging.info("Moved to screen center")
#         except Exception as e:
#             logging.error(f"Error moving to center: {e}")
    
#     @staticmethod
#     def move_to_corner(corner: str = 'center', duration: float = 0.5):
#         """
#         Move mouse to screen corner
        
#         Args:
#             corner (str): 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'center'
#             duration (float): Movement duration in seconds
#         """
#         try:
#             corners = {
#                 'top-left': (0, 0),
#                 'top-right': (MouseControl.screen_width, 0),
#                 'bottom-left': (0, MouseControl.screen_height),
#                 'bottom-right': (MouseControl.screen_width, MouseControl.screen_height),
#                 'center': (MouseControl.screen_width // 2, MouseControl.screen_height // 2)
#             }
            
#             if corner not in corners:
#                 raise ValueError(f"Corner must be one of {list(corners.keys())}")
            
#             x, y = corners[corner]
#             MouseControl.move(x, y, duration)
#             logging.info(f"Moved to {corner} corner")
#         except Exception as e:
#             logging.error(f"Error moving to corner: {e}")
    
#     @staticmethod
#     def click(x: Optional[int] = None, y: Optional[int] = None, 
#               button: str = 'left', clicks: int = 1, interval: float = 0.1):
#         """
#         Perform mouse click
        
#         Args:
#             x (int): X coordinate (optional)
#             y (int): Y coordinate (optional)
#             button (str): 'left', 'right', 'middle'
#             clicks (int): Number of clicks
#             interval (float): Time between clicks
#         """
#         try:
#             if x is not None and y is not None:
#                 pyautogui.click(x=x, y=y, button=button, clicks=clicks, interval=interval)
#                 logging.info(f"Clicked at ({x}, {y}) with {button} button {clicks} times")
#             else:
#                 pyautogui.click(button=button, clicks=clicks, interval=interval)
#                 logging.info(f"Clicked at current position with {button} button {clicks} times")
#         except Exception as e:
#             logging.error(f"Error clicking: {e}")
    
#     @staticmethod
#     def double_click(x: Optional[int] = None, y: Optional[int] = None, button: str = 'left'):
#         """Double click at specified or current position"""
#         try:
#             MouseControl.click(x, y, button, clicks=2, interval=0.1)
#             logging.info("Double clicked")
#         except Exception as e:
#             logging.error(f"Error double clicking: {e}")
    
#     @staticmethod
#     def triple_click(x: Optional[int] = None, y: Optional[int] = None, button: str = 'left'):
#         """Triple click at specified or current position"""
#         try:
#             MouseControl.click(x, y, button, clicks=3, interval=0.1)
#             logging.info("Triple clicked")
#         except Exception as e:
#             logging.error(f"Error triple clicking: {e}")
    
#     @staticmethod
#     def right_click(x: Optional[int] = None, y: Optional[int] = None):
#         """Right click at specified or current position"""
#         try:
#             MouseControl.click(x, y, button='right')
#             logging.info("Right clicked")
#         except Exception as e:
#             logging.error(f"Error right clicking: {e}")
    
#     @staticmethod
#     def middle_click(x: Optional[int] = None, y: Optional[int] = None):
#         """Middle click at specified or current position"""
#         try:
#             MouseControl.click(x, y, button='middle')
#             logging.info("Middle clicked")
#         except Exception as e:
#             logging.error(f"Error middle clicking: {e}")
    
#     @staticmethod
#     def drag(x1: int, y1: int, x2: int, y2: int, duration: float = 1.0, button: str = 'left'):
#         """
#         Drag mouse from one point to another
        
#         Args:
#             x1 (int): Start X coordinate
#             y1 (int): Start Y coordinate
#             x2 (int): End X coordinate
#             y2 (int): End Y coordinate
#             duration (float): Drag duration in seconds
#             button (str): Mouse button to use for dragging
#         """
#         try:
#             pyautogui.moveTo(x1, y1, duration=0.1)
#             pyautogui.dragTo(x2, y2, duration=duration, button=button)
#             logging.info(f"Dragged from ({x1}, {y1}) to ({x2}, {y2})")
#         except Exception as e:
#             logging.error(f"Error dragging: {e}")
    
#     @staticmethod
#     def drag_relative(dx: int, dy: int, duration: float = 1.0, button: str = 'left'):
#         """
#         Drag mouse relative to current position
        
#         Args:
#             dx (int): X distance to drag
#             dy (int): Y distance to drag
#             duration (float): Drag duration in seconds
#             button (str): Mouse button to use for dragging
#         """
#         try:
#             pyautogui.dragRel(dx, dy, duration=duration, button=button)
#             logging.info(f"Dragged relatively: ({dx}, {dy})")
#         except Exception as e:
#             logging.error(f"Error dragging relatively: {e}")
    
#     @staticmethod
#     def scroll(amount: int, x: Optional[int] = None, y: Optional[int] = None):
#         """
#         Scroll mouse wheel
        
#         Args:
#             amount (int): Positive to scroll up, negative to scroll down
#             x (int): X coordinate to scroll at (optional)
#             y (int): Y coordinate to scroll at (optional)
#         """
#         try:
#             if x is not None and y is not None:
#                 pyautogui.scroll(amount, x=x, y=y)
#                 logging.info(f"Scrolled {amount} at ({x}, {y})")
#             else:
#                 pyautogui.scroll(amount)
#                 logging.info(f"Scrolled {amount} at current position")
#         except Exception as e:
#             logging.error(f"Error scrolling: {e}")
    
#     @staticmethod
#     def hscroll(amount: int, x: Optional[int] = None, y: Optional[int] = None):
#         """
#         Horizontal scroll (if supported)
        
#         Args:
#             amount (int): Positive to scroll right, negative to scroll left
#             x (int): X coordinate to scroll at (optional)
#             y (int): Y coordinate to scroll at (optional)
#         """
#         try:
#             if x is not None and y is not None:
#                 pyautogui.hscroll(amount, x=x, y=y)
#                 logging.info(f"Horizontal scrolled {amount} at ({x}, {y})")
#             else:
#                 pyautogui.hscroll(amount)
#                 logging.info(f"Horizontal scrolled {amount} at current position")
#         except Exception as e:
#             logging.error(f"Error horizontal scrolling: {e}")
    
#     @staticmethod
#     def scroll_up(amount: int = 100, x: Optional[int] = None, y: Optional[int] = None):
#         """Scroll up"""
#         try:
#             MouseControl.scroll(amount, x, y)
#             logging.info(f"Scrolled up: {amount}")
#         except Exception as e:
#             logging.error(f"Error scrolling up: {e}")
    
#     @staticmethod
#     def scroll_down(amount: int = 100, x: Optional[int] = None, y: Optional[int] = None):
#         """Scroll down"""
#         try:
#             MouseControl.scroll(-amount, x, y)
#             logging.info(f"Scrolled down: {amount}")
#         except Exception as e:
#             logging.error(f"Error scrolling down: {e}")
    
#     @staticmethod
#     def scroll_to_top(x: Optional[int] = None, y: Optional[int] = None):
#         """Scroll to top of page"""
#         try:
#             MouseControl.scroll(-10000, x, y)  # Large negative scroll
#             logging.info("Scrolled to top")
#         except Exception as e:
#             logging.error(f"Error scrolling to top: {e}")
    
#     @staticmethod
#     def scroll_to_bottom(x: Optional[int] = None, y: Optional[int] = None):
#         """Scroll to bottom of page"""
#         try:
#             MouseControl.scroll(10000, x, y)  # Large positive scroll
#             logging.info("Scrolled to bottom")
#         except Exception as e:
#             logging.error(f"Error scrolling to bottom: {e}")
    
#     @staticmethod
#     def mouse_down(x: Optional[int] = None, y: Optional[int] = None, button: str = 'left'):
#         """
#         Press and hold mouse button
        
#         Args:
#             x (int): X coordinate (optional)
#             y (int): Y coordinate (optional)
#             button (str): 'left', 'right', 'middle'
#         """
#         try:
#             if x is not None and y is not None:
#                 pyautogui.mouseDown(x=x, y=y, button=button)
#                 logging.info(f"Mouse down at ({x}, {y}) with {button} button")
#             else:
#                 pyautogui.mouseDown(button=button)
#                 logging.info(f"Mouse down at current position with {button} button")
#         except Exception as e:
#             logging.error(f"Error pressing mouse down: {e}")
    
#     @staticmethod
#     def mouse_up(x: Optional[int] = None, y: Optional[int] = None, button: str = 'left'):
#         """
#         Release mouse button
        
#         Args:
#             x (int): X coordinate (optional)
#             y (int): Y coordinate (optional)
#             button (str): 'left', 'right', 'middle'
#         """
#         try:
#             if x is not None and y is not None:
#                 pyautogui.mouseUp(x=x, y=y, button=button)
#                 logging.info(f"Mouse up at ({x}, {y}) with {button} button")
#             else:
#                 pyautogui.mouseUp(button=button)
#                 logging.info(f"Mouse up at current position with {button} button")
#         except Exception as e:
#             logging.error(f"Error releasing mouse: {e}")
    
#     @staticmethod
#     def drag_and_drop(start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 1.0):
#         """
#         Drag and drop operation
        
#         Args:
#             start_x (int): Start X coordinate
#             start_y (int): Start Y coordinate
#             end_x (int): End X coordinate
#             end_y (int): End Y coordinate
#             duration (float): Duration of drag in seconds
#         """
#         try:
#             MouseControl.move(start_x, start_y, duration=0.1)
#             MouseControl.mouse_down(button='left')
#             MouseControl.move(end_x, end_y, duration=duration)
#             MouseControl.mouse_up(button='left')
#             logging.info(f"Drag and drop from ({start_x}, {start_y}) to ({end_x}, {end_y})")
#         except Exception as e:
#             logging.error(f"Error in drag and drop: {e}")
    
#     @staticmethod
#     def smooth_move(x: int, y: int, duration: float = 1.0, steps: int = 100):
#         """
#         Smooth movement with custom steps
        
#         Args:
#             x (int): Target X coordinate
#             y (int): Target Y coordinate
#             duration (float): Movement duration in seconds
#             steps (int): Number of steps for smooth movement
#         """
#         try:
#             current_x, current_y = MouseControl.get_current_position()
#             step_duration = duration / steps
            
#             for i in range(steps + 1):
#                 progress = i / steps
#                 ease = progress * progress  # Quadratic easing
#                 move_x = current_x + (x - current_x) * ease
#                 move_y = current_y + (y - current_y) * ease
#                 pyautogui.moveTo(move_x, move_y, duration=0)
#                 time.sleep(step_duration)
            
#             logging.info(f"Smooth moved to ({x}, {y})")
#         except Exception as e:
#             logging.error(f"Error in smooth movement: {e}")
    
#     @staticmethod
#     def circle_movement(center_x: int, center_y: int, radius: int = 100, 
#                        duration: float = 2.0, clockwise: bool = True):
#         """
#         Move mouse in a circular pattern
        
#         Args:
#             center_x (int): Center X coordinate
#             center_y (int): Center Y coordinate
#             radius (int): Circle radius
#             duration (float): Duration for full circle
#             clockwise (bool): Direction of movement
#         """
#         try:
#             steps = 360
#             step_duration = duration / steps
#             direction = 1 if clockwise else -1
            
#             for angle in range(0, 361, 1):
#                 rad = math.radians(angle * direction)
#                 x = center_x + radius * math.cos(rad)
#                 y = center_y + radius * math.sin(rad)
#                 pyautogui.moveTo(x, y, duration=0)
#                 time.sleep(step_duration)
            
#             logging.info(f"Circular movement around ({center_x}, {center_y})")
#         except Exception as e:
#             logging.error(f"Error in circular movement: {e}")
    
#     @staticmethod
#     def shake_mouse(duration: float = 0.5, intensity: int = 10):
#         """
#         Shake mouse (useful for getting attention or testing)
        
#         Args:
#             duration (float): Shake duration in seconds
#             intensity (int): Shake intensity
#         """
#         try:
#             start_time = time.time()
#             current_x, current_y = MouseControl.get_current_position()
            
#             while time.time() - start_time < duration:
#                 dx = random.randint(-intensity, intensity)
#                 dy = random.randint(-intensity, intensity)
#                 pyautogui.moveRel(dx, dy, duration=0)
#                 time.sleep(0.01)
            
#             # Return to original position
#             pyautogui.moveTo(current_x, current_y, duration=0.1)
#             logging.info("Mouse shake completed")
#         except Exception as e:
#             logging.error(f"Error shaking mouse: {e}")
    
#     @staticmethod
#     def draw_square(start_x: int, start_y: int, size: int = 100, duration: float = 2.0):
#         """
#         Draw a square with mouse movement
        
#         Args:
#             start_x (int): Starting X coordinate
#             start_y (int): Starting Y coordinate
#             size (int): Square size
#             duration (float): Duration for drawing
#         """
#         try:
#             points = [
#                 (start_x, start_y),
#                 (start_x + size, start_y),
#                 (start_x + size, start_y + size),
#                 (start_x, start_y + size),
#                 (start_x, start_y)
#             ]
            
#             point_duration = duration / len(points)
            
#             for point in points:
#                 MouseControl.move(point[0], point[1], duration=point_duration)
            
#             logging.info(f"Drew square starting at ({start_x}, {start_y})")
#         except Exception as e:
#             logging.error(f"Error drawing square: {e}")
    
#     @staticmethod
#     def get_pixel_color(x: int, y: int) -> Tuple[int, int, int]:
#         """
#         Get RGB color of pixel at specified coordinates
        
#         Args:
#             x (int): X coordinate
#             y (int): Y coordinate
            
#         Returns:
#             Tuple[int, int, int]: RGB color values
#         """
#         try:
#             color = pyautogui.pixel(x, y)
#             logging.info(f"Pixel color at ({x}, {y}): {color}")
#             return color
#         except Exception as e:
#             logging.error(f"Error getting pixel color: {e}")
#             return (0, 0, 0)
    
#     @staticmethod
#     def wait_until_color(x: int, y: int, expected_color: Tuple[int, int, int], 
#                         timeout: float = 10.0, check_interval: float = 0.1) -> bool:
#         """
#         Wait until pixel at coordinates matches expected color
        
#         Args:
#             x (int): X coordinate
#             y (int): Y coordinate
#             expected_color (Tuple[int, int, int]): Expected RGB color
#             timeout (float): Maximum time to wait
#             check_interval (float): Time between checks
            
#         Returns:
#             bool: True if color matched, False if timeout
#         """
#         try:
#             start_time = time.time()
            
#             while time.time() - start_time < timeout:
#                 current_color = MouseControl.get_pixel_color(x, y)
#                 if current_color == expected_color:
#                     logging.info(f"Color matched at ({x}, {y}): {expected_color}")
#                     return True
#                 time.sleep(check_interval)
            
#             logging.warning(f"Timeout waiting for color at ({x}, {y})")
#             return False
#         except Exception as e:
#             logging.error(f"Error waiting for color: {e}")
#             return False
    
#     @staticmethod
#     def is_on_screen(x: int, y: int) -> bool:
#         """
#         Check if coordinates are on screen
        
#         Args:
#             x (int): X coordinate
#             y (int): Y coordinate
            
#         Returns:
#             bool: True if coordinates are on screen
#         """
#         try:
#             on_screen = (0 <= x <= MouseControl.screen_width and 
#                         0 <= y <= MouseControl.screen_height)
#             logging.info(f"Coordinates ({x}, {y}) are {'on' if on_screen else 'off'} screen")
#             return on_screen
#         except Exception as e:
#             logging.error(f"Error checking screen bounds: {e}")
#             return False
    
#     @staticmethod
#     def set_mouse_speed(delay: float = 0.1):
#         """
#         Set pause between mouse actions
        
#         Args:
#             delay (float): Pause duration in seconds
#         """
#         try:
#             pyautogui.PAUSE = delay
#             logging.info(f"Set mouse speed delay to {delay} seconds")
#         except Exception as e:
#             logging.error(f"Error setting mouse speed: {e}")
    
#     @staticmethod
#     def disable_failsafe():
#         """Disable fail-safe feature (use with caution)"""
#         try:
#             pyautogui.FAILSAFE = False
#             logging.warning("Fail-safe feature disabled")
#         except Exception as e:
#             logging.error(f"Error disabling fail-safe: {e}")
    
#     @staticmethod
#     def enable_failsafe():
#         """Enable fail-safe feature"""
#         try:
#             pyautogui.FAILSAFE = True
#             logging.info("Fail-safe feature enabled")
#         except Exception as e:
#             logging.error(f"Error enabling fail-safe: {e}")


# # Example usage and demonstration
# if __name__ == "__main__":
#     mc = MouseControl()
    
#     print(f"Screen size: {mc.get_screen_size()}")
#     print(f"Current position: {mc.get_current_position()}")
    
#     # Test basic movements
#     mc.move_to_center()
#     time.sleep(1)
    
#     mc.move_to_corner('top-right')
#     time.sleep(1)
    
#     # Test clicks
#     mc.click(button='left')
#     mc.double_click()
#     mc.right_click()
    
#     # Test scrolling
#     mc.scroll_up(200)
#     time.sleep(1)
#     mc.scroll_down(200)
    
#     # Test drag and drop
#     center_x, center_y = mc.screen_width // 2, mc.screen_height // 2
#     mc.drag_and_drop(center_x - 100, center_y, center_x + 100, center_y)
    
#     # Test smooth movement
#     mc.smooth_move(center_x, center_y - 100, duration=2.0)
    
#     # Test circular movement
#     mc.circle_movement(center_x, center_y, radius=50, duration=1.0)
    
#     # Test pixel color detection
#     color = mc.get_pixel_color(center_x, center_y)
#     print(f"Center pixel color: {color}")
    
#     print("Mouse automation test completed!")



import pyautogui, time

class MouseControl:
    @staticmethod
    def move_to(x: int, y: int, duration: float = 0.2):
        pyautogui.moveTo(x, y, duration=duration)

    @staticmethod
    def click(button="left"):
        pyautogui.click(button=button)

    @staticmethod
    def double_click():
        pyautogui.doubleClick()

    @staticmethod
    def right_click():
        pyautogui.click(button="right")

    @staticmethod
    def drag_to(x: int, y: int, duration: float = 0.2):
        pyautogui.dragTo(x, y, duration=duration)

    @staticmethod
    def scroll(amount: int):
        pyautogui.scroll(amount)

    @staticmethod
    def hover(x: int, y: int, duration: float = 0.2):
        MouseControl.move_to(x, y, duration=duration)

    @staticmethod
    def draw_circle(center_x: int, center_y: int, radius: int = 100, steps: int = 60):
        for i in range(steps):
            angle = (i / steps) * 6.28318
            x = center_x + int(radius * __import__("math").cos(angle))
            y = center_y + int(radius * __import__("math").sin(angle))
            pyautogui.moveTo(x, y)
            if i == 0: pyautogui.mouseDown()
        pyautogui.mouseUp()
