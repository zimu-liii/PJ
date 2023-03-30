# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:59:32 2023

@author: muzi
"""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from simulation.main import SIMU
from ml.model import model_preparation

# import model and dataset
#probability_model = tf.keras.models.load_model('ml/model.h5')
probability_model = model_preparation()
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# prediction of an original img from dataset
def predict(num):
    img = test_images[num]
    label = test_labels[num]

    img_norm = (np.expand_dims(img / 255.0, 0))
    predictions_single = probability_model.predict(img_norm)
    prediction = np.argmax(predictions_single[0])

    return img, label, prediction


# prediction of the polluted img and only return prediction results
def predict_pollute(num, rate):
    img, label, prediction = predict(num)

    ss = SIMU(img=img)
    img1 = np.array(ss.error_miss(rate))

    img1_norm = (np.expand_dims(img1 / 255.0, 0))
    predictions_single1 = probability_model.predict(img1_norm)
    prediction1 = np.argmax(predictions_single1[0])

    return label, prediction, prediction1


# prediction of the polluted img and also return images
def predict_pollute_img(num, rate):
    img, label, prediction = predict(num)

    ss = SIMU(img=img)
    img1 = np.array(ss.error_miss(rate))

    img1_norm = (np.expand_dims(img1 / 255.0, 0))
    predictions_single1 = probability_model.predict(img1_norm)
    prediction1 = np.argmax(predictions_single1[0])

    return img, img1, label, prediction, prediction1


# prediction of one img and the polluted, but to show and print
def predict_show(num, rate):
    img = test_images[num]

    img_norm = (np.expand_dims(img / 255.0, 0))
    predictions_single = probability_model.predict(img_norm)
    prediction = np.argmax(predictions_single[0])

    ss = SIMU(img=img)
    img1 = np.array(ss.error_miss(rate))

    img1_norm = (np.expand_dims(img1 / 255.0, 0))
    predictions_single1 = probability_model.predict(img1_norm)
    prediction1 = np.argmax(predictions_single1[0])

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                   'Ankle boot']

    print('test_image_number: %d \n' % num,
          'test_label: %s \n' % class_names[test_labels[num]],
          'prediction result: %s \n' % class_names[prediction],
          'prediction result after polluted: %s \n' % class_names[prediction1]
          )

    plt.imshow(img, cmap='gray')
    plt.show()

    plt.imshow(img1, cmap='gray')
    plt.show()

    return img, img1


if __name__ == '__main__':
    img, img1 = predict_show(1800, 0.25)
