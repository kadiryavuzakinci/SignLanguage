import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None

    def initialize_camera(self):
        try:
            self.cap = cv2.VideoCapture(self.camera_index)
            if not self.cap.isOpened():
                raise Exception(f"Failed to open camera with index {self.camera_index}")
        except Exception as e:
            print(f"An error occurred while initializing the camera: {e}")
            self.cap = None

        return self.cap
