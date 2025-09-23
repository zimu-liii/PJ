import tensorflow as tf
import numpy as np


def model_preparation():
    # import Fashion MNIST dataset
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    '''
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                   'Ankle boot']
    '''

    # preprocess of dataset
    train_images_norm = train_images / 255.0
    test_images_norm = test_images / 255.0

    # build model
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    # compile model
    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    # train model
    model.fit(train_images_norm, train_labels, epochs=10)

    test_loss, test_acc = model.evaluate(test_images_norm, test_labels, verbose=2)
    print('\nTest accuracy:', test_acc)

    # test model
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    predictions = probability_model.predict(test_images_norm)
    predictions_stats = []
    for i in range(len(predictions)):
        if np.argmax(predictions[i]) == test_labels[i]:
            predictions_stats.append(True)
        else:
            predictions_stats.append(False)
    predictions_accuracy = predictions_stats.count(True) / len(predictions_stats)
    print('\nPrediction accuracy:', predictions_accuracy)

    return probability_model


if __name__ == '__main__':
    probability_model = model_preparation()
    probability_model.save('model.h5')
