from train import model
#Test
results = model.predict(model='your_model.pt', conf=0.5, source='test/images', save=True)
