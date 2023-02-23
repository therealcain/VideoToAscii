# VideoToAscii
Converting a video or webcam to ASCII in Python.

# How to use
Just add a file called "videoplayback.mp4" (You can edit it in code) next to the python code, and run the code :)

Also make sure you have 'opencv2', 'curses', 'numpy' installed.

# How it works?
1. Loading the video with OpenCV (or any other library).
2. Resize the video to a low resolution scale (In my case it was 50x25), because when working with high resolution videos/images the iterations takes longer,
hence it will make the video with very low framerate per second.
3. Convert the entire video to grayscale, because we don't need colors. We actually need only black and white, but black and white is boring because
it means it will only have 2 ascii codes to be represented by. So we can convert it entirely to grayscale, just so we can have a veriety of ascii codes. 
Instead of this we can also use some luminance algrotihms like [Relative Luminance](https://en.wikipedia.org/wiki/Relative_luminance).
4. Now we need to choose our luminance characters, I picked: " .,-~:;=!*#$@", I organized them by size of the characters.
5. We need to filter now the pixel value to see which pixel it fits, the more bright it is the larger the character is.
6. Lastly, we position all of the characters in terminal and show it :)
