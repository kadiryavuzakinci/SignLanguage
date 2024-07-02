import cv2

class ClassStripDrawer:
    def __init__(self, strip_height=50, strip_color=(255, 0, 0)):
        self.strip_height = strip_height
        self.strip_color = strip_color

    def draw_class_strip(self, frame, detected_classes):
        try:
            cv2.rectangle(frame, (0, 0), (frame.shape[1], self.strip_height), self.strip_color, -1)
            
            # Concatenate all detected classes, starting from the most recent ones
            text = ''
            remaining_width = frame.shape[1] - 20
            for label in reversed(detected_classes):
                if cv2.getTextSize(text + label, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0][0] <= remaining_width:
                    text = f"{label.split()[0]}, {text}"  # Exclude guess rate from displayed text
                else:
                    break
            
            cv2.putText(frame, text, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
        except Exception as e:
            print(f"An error occurred while drawing the class strip: {e}")
