from ultralytics import YOLO


# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8l.pt")  # load a pretrained model

# # Use the model
# model.train(data="coco8.yaml", epochs=3)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format


# Use the model
# results = model.train(data=os.path.join(ROOT_DIR, "config.yaml"), epochs=20, imgsz=640)  # train the model
results = model.train(data='your_data.yaml',epochs=20, batch=32, imgsz=640)

