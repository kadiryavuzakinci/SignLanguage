from ultralytics import YOLO

class ModelLoader:
    def __init__(self, model_path="best.pt"):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        try:
            self.model = YOLO(self.model_path)
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            self.model = None

        return self.model