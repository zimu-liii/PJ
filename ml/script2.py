
import matplotlib.pyplot as plt

from ml.image import predict_pollute_img, test_images

tag = {0: 'all prediction passed', 1: 'only polluted prediction failed', 2: 'only origin prediction failed',
       3: 'all prediction failed and origin == polluted', 4: 'all prediction failed but origin != polluted'}

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                   'Ankle boot']

for i in range(len(test_images)):
    try:
        img, img1, label, prediction, prediction1 = predict_pollute_img(i,0.15)
    except:
        print(i)

        '''if label == prediction and prediction == prediction1:

            plt.imshow(img, cmap='gray')
            plt.show()
            plt.imshow(img1, cmap='gray')
            plt.show()

            print(class_names[label], class_names[prediction], class_names[prediction1], tag[0])
            break'''

        if label == prediction and label != prediction1:

            plt.imshow(img, cmap='gray')
            plt.show()
            plt.imshow(img1, cmap='gray')
            plt.show()

            print(class_names[label], class_names[prediction], class_names[prediction1], tag[1])
            break

        '''if label != prediction and label == prediction1:

            plt.imshow(img, cmap='gray')
            plt.show()
            plt.imshow(img1, cmap='gray')
            plt.show()

            print(class_names[label], class_names[prediction], class_names[prediction1], tag[2])
            break'''

        '''if label != prediction and label != prediction1 and prediction == prediction1:

            plt.imshow(img, cmap='gray')
            plt.show()
            plt.imshow(img1, cmap='gray')
            plt.show()

            print(class_names[label], class_names[prediction], class_names[prediction1], tag[3])
            break'''

        '''if label != prediction and label != prediction1 and prediction != prediction1:
        
            plt.imshow(img, cmap='gray')
            plt.show()
            plt.imshow(img1, cmap='gray')
            plt.show()

            print(class_names[label], class_names[prediction], class_names[prediction1], tag[4])
            break'''
