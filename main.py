import PicoOled13
import utime

# Initialize the display
display = PicoOled13.get()
display.clear()

# Get OLED display dimensions
oled_width = display.get_width()
oled_height = display.get_height()

# Initial previous time
previous_time = utime.localtime()

def draw_initial_watch_face():
    current_time = utime.localtime()
    
    # Format the time as HH:MM:SS
    time_str = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
    
    # Calculate the position to center the text
    x_pos = (oled_width - len(time_str) * 8) // 2
    y_pos = oled_height // 2
    
    # Display the entire time in the center of the screen
    display.text(time_str, x_pos, y_pos, 0xffff)
    display.show()
    
    return current_time

def update_time(previous_time):
    current_time = utime.localtime()
    
    if current_time[3] != previous_time[3] or current_time[4] != previous_time[4] or current_time[5] != previous_time[5]:
        # Clear the old time
        old_time_str = "{:02d}:{:02d}:{:02d}".format(previous_time[3], previous_time[4], previous_time[5])
        x_pos = (oled_width - len(old_time_str) * 8) // 2
        y_pos = oled_height // 2
        display.text(old_time_str, x_pos, y_pos, 0x0000)  # Clear old time by writing black
        
        # Draw the new time
        new_time_str = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
        display.text(new_time_str, x_pos, y_pos, 0xffff)  # Write new time in white
        display.show()
    
    return current_time

# Draw the initial time
previous_time = draw_initial_watch_face()

while True:
    # Update the time
    previous_time = update_time(previous_time)
    utime.sleep(1)
