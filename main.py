import numpy as np
import cv2
import supervision as sv
import time
from initialize_camera import Camera
from load_model import ModelLoader
from draw_class import ClassStripDrawer
from frame_process import FrameProcessor
from voice import SpeechConverter
from generate_sentences import SentenceGenerator

def run_cycle(cap):
    model_loader = ModelLoader(model_path="yolov8l.pt")
    model = model_loader.load_model()
    
    box_annotator = sv.BoxAnnotator(thickness=1, text_thickness=1, text_scale=1)
    
    frame_processor = FrameProcessor(model, box_annotator)
    class_strip_drawer = ClassStripDrawer()
    speech_converter = SpeechConverter()
    sentence_generator = SentenceGenerator()

    detected_classes = set()
    previous_class = None

    start_time = time.time()
    while time.time() - start_time < 10:
        ret, frame = cap.read()
        fps_start_time = time.time()
        frame_time = time.time()

        if not ret:
            print("Failed to capture frame")
            break

        annotated_frame, new_detected_classes, last_detected_class = frame_processor.process_frame(frame)
        new_classes = [label.split()[0] for label in new_detected_classes]
        
        # Check for new classes that are different from the previous detected class
        for class_name in new_classes:
            if class_name != previous_class:
                detected_classes.add(class_name)
                previous_class = class_name

        class_strip_drawer.draw_class_strip(annotated_frame, list(detected_classes))

        # Write detected class names to file instantly
        with open("words.txt", "w") as f:
            f.write(', '.join(detected_classes) + '\n')

        fps_end_time = time.time() #
        fps = 1 / np.round(fps_end_time - fps_start_time, 2) #
        cv2.putText(annotated_frame, f'FPS: {int(fps)}', (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

        cv2.imshow('YOLOv8 Detection', annotated_frame)

        if cv2.waitKey(10) & 0XFF == ord('q'):
            cv2.destroyAllWindows()
            return False

    # Generate meaningful sentence from words and save to file
    sentence_generator.process_words_file("words.txt", "meaningful.txt")
    
    # Convert last word to speech
    speech_converter.convert_words_to_speech("meaningful.txt")

    # Display frames with the blue strip without processing for 5 seconds
    end_time = time.time() + 5
    while time.time() < end_time:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        
        # Draw the blue strip on the frame
        class_strip_drawer.draw_class_strip(frame, list(detected_classes))
        
        cv2.imshow('Detection', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            return False

    return True

def main():
    camera = Camera(camera_index=0)
    cap = camera.initialize_camera()
    
    while True:
        if not run_cycle(cap):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
