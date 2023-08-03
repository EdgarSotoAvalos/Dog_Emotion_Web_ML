# Dog Emotion Classification Web App

This project is a web application that uses a trained deep learning model to classify emotions in dog images. The app is built with Flask as the web framework and TensorFlow/Keras for the deep learning model.

## Requirements

Before running the web app, make sure you have the following installed:

- Python (>= 3.6)
- Flask (>= 1.1.2)
- NumPy (>= 1.19.5)
- OpenCV (cv2)
- TensorFlow (>= 2.0)
- Keras (>= 2.4.3)
- Matplotlib (>= 3.3.4)

You can install the required dependencies using `pip` with the following command:

```bash
pip install Flask numpy opencv-python tensorflow keras matplotlib
```

## Getting Started

1. Clone this repository to your local machine.
  
2. Make sure you have the model file `my_model.h5` in the root directory.

3. Run the Flask web app using the following command:
```bash
python app.py
```

4. Open your web browser and go to `http://127.0.0.1:5000/` to access the web app.

## How to Use

The web app provides a user-friendly interface to classify emotions in dog images. Follow these steps:

1. Click the "Seleccionar archivo" button to choose an image of your dog from your computer or mobile device.

2. Press the "Analizar" button to get the classification of emotions for your adorable furry companion.

## Dataset

The model was trained using the [Dog Emotion Dataset](https://www.kaggle.com/datasets/danielshanbalico/dog-emotion). This dataset consists of images of dogs labeled with different emotions, making it suitable for emotion classification tasks.

## Important Note

This project is for educational and demonstration purposes only. The accuracy of emotion classification depends on the quality and diversity of the dataset used to train the model. Emotion classification in animals is a challenging task and might not be as accurate as human emotion classification. The creators and contributors of this project are not responsible for any reliance on the predictions made by the model.

## Authors

- [Edgar Soto Avalos](https://github.com/EdgarSotoAvalos)

## License

This project is licensed under the [MIT License](LICENSE).


