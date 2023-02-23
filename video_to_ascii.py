import cv2
import numpy as np
import curses

# Luminance characters
LUMINANCE = " .,-~:;=!*#$@"

# Values to know when to use the luminance. (between 0 to 255)
LUMINANCE_PRECISION = [int((255 / len(LUMINANCE)) * (len(LUMINANCE) - x)) for x in range(0, len(LUMINANCE))]

# Dimensions of the luminance.
# This can't be any number, depending on your terminal size.
RESIZED_DIMENSIONS = (50, 25)

def main():
    # Use a playback
    cap = cv2.VideoCapture("videoplayback.mp4")
    
    # Use webcam
    # cap = cv2.VideoCapture(0)
    
    # Terminal screen - Curses
    stdscr = curses.initscr()
    curses.curs_set(0)

    if not cap.isOpened():
        print("Failed to open video capture.")

    while cap.isOpened():
        # read frames
        ret, frame = cap.read()

        # Frame still on
        if ret:
            # Resize the frame to the desired dimensions
            resized = cv2.resize(frame, RESIZED_DIMENSIONS)

            # Convert the frame to Gray Scale
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

            # Clear the terminal screen
            # To allow characters to be repositioned
            stdscr.clear()

            # Loop over the (x,y) of the frame
            for i in range(gray.shape[0]):
                for j in range(gray.shape[1]):
                    
                    # Luminance index
                    luminance = 0
                    
                    # Check if the value of the grayscale is between the
                    # luminance precision
                    for idx, dist in enumerate(LUMINANCE_PRECISION):
                        distance = abs(gray[i, j] - dist)
                        if distance <= (255 / len(LUMINANCE)):
                            luminance = idx
                            break
                    
                    # Position the character
                    stdscr.addstr(i, j, LUMINANCE[luminance])
            
            # Allow to view the new terminal window
            stdscr.refresh()
        else:
            break

    # Free memory
    cap.release()
    curses.endwin()

if __name__ == '__main__':
    main()
