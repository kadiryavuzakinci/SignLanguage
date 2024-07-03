import supervision as sv

class FrameProcessor:
    def __init__(self, model, box_annotator, confidence_threshold=0.5):
        self.model = model
        self.box_annotator = box_annotator
        self.confidence_threshold = confidence_threshold
        self.detected_classes = set()
        self.last_detected_class = None

    def process_frame(self, frame):
        try:
            result = self.model(frame, agnostic_nms=True)[0]
            detections = sv.Detections.from_ultralytics(result)

            # Filter detections based on confidence threshold
            filtered_detections = detections[detections.confidence >= self.confidence_threshold]

            labels = [
                f"{class_name} {confidence:.2f}"
                for class_name, confidence
                in zip(filtered_detections['class_name'], filtered_detections.confidence)
            ]

            annotated_frame = self.box_annotator.annotate(
                scene=frame,
                detections=filtered_detections,
                labels=labels
            )

            new_detected_classes = set(label.split()[0] for label in labels)

            # Update the detected classes set with new detections
            self.detected_classes.update(new_detected_classes)

            return annotated_frame, list(self.detected_classes), labels[-1].split()[0] if labels else None
        
        except Exception as e:
            print(f"An error occurred while processing the frame: {e}")
            return frame, list(self.detected_classes), self.last_detected_class
