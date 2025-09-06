import pyautogui
import time
# for future use

print("You have 5 seconds to hover your mouse over the button (audio or video call)...")
time.sleep(5)

# Show current mouse position every second for 5 seconds
for _ in range(5):
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")
    time.sleep(1)
