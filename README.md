# Screen recording using python

This code captures the screen along with the webcam feed and saves it as a video file. Here's how it works:

    The code imports necessary modules:
        ImageGrab from PIL (Python Imaging Library) is used to capture the screen.
        numpy (imported as np) is used to process the captured image.
        cv2 is OpenCV, a library used for image and video processing.
        GetSystemMetrics from win32api is used to get the screen resolution.

    The webcam capture is initialized using cv2.VideoCapture(0). This assumes the default webcam is connected.

    The code retrieves the width and height of the screen using GetSystemMetrics(0) and GetSystemMetrics(1).

    The user is prompted to enter a file name for the captured video.

    The four character code ("mp4v") is used to define the video codec for the captured video.

    A VideoWriter object named captured_video is created with the specified file name, video codec, frame rate (20.0), and screen dimensions (width and height). This object is used to save the captured video.

    Inside the while loop, the screen is captured using ImageGrab.grab() with the specified bounding box (0, 0, width, height). The captured image is converted to a NumPy array.

    The color format of the image is converted from BGR to RGB using `cv2.cvtColor
