import pyautogui
import time
import pyperclip

# Function to click on the icon and drag to select text
def select_and_copy_text():
    # Give yourself a short delay before starting to position the mouse
    time.sleep(2)

    # Click on the icon at (1172, 1051)
    pyautogui.click(1172, 1051)
    time.sleep(0.5)  # Short delay to ensure the click is registered

    # Drag from (620, 273) to (1617, 853) to select the text
    pyautogui.moveTo(539, 269)
    pyautogui.dragTo(1617, 853, duration=1)  # Adjust duration if needed
    time.sleep(0.5)  # Short delay after dragging

    # Use the hotkey to copy the selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Short delay to ensure the text is copied
    pyautogui.click(1617, 853)

    # Get the text from the clipboard
    copied_text = pyperclip.paste()

    return copied_text

# Run the function and store the result in a variable
text_variable = select_and_copy_text()

# Print the copied text to verify
print("Copied Text:", text_variable)
