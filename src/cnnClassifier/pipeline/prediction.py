import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        
    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        test_image = image.load_img(self.filename, target_size=(128, 128))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)  # ✅ correct

        prob = model.predict(test_image)[0][0]

        if prob >= 0.5:
            prediction = "Normal"
        else:
            prediction = "Tumor"

        return [
         {"prediction": prediction, "probability": float(prob)},
          {"image": self.filename}
         ]
