import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify, render_template
import cv2

app = Flask(__name__)

emotions_list = ['Molesto','Feliz','Relajado','Triste']
model = tf.keras.models.load_model('my_model.h5')

@app.route('/predict_image', methods=['POST'])
def predict_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No se envió ninguna imagen.'})

    user_image = request.files['image'].read()
    nparr = np.frombuffer(user_image, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Preprocesado a la imagen del usuario
    img_size = (192, 192)
    image_resized = cv2.resize(image, img_size)

    # Reordenar los canales de color 
    image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)


    prediction = model.predict(np.expand_dims(image_rgb, axis=0))

    emotions_probabilities = prediction[0]
    emotions_dict = {emotion: round(probability * 100, 2) for emotion, probability in zip(emotions_list, emotions_probabilities)}

    sorted_emotions = sorted(emotions_dict.items(), key=lambda x: x[1], reverse=True)

    return render_template('result.html', emotions=sorted_emotions)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)