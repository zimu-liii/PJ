

from ml.image import predict_pollute, test_images

result = []

tag = {0: 'all prediction passed', 1: 'only polluted prediction failed', 2: 'only origin prediction failed',
       3: 'all prediction failed and origin == polluted', 4: 'all prediction failed but origin != polluted'}

for i in range(len(test_images)):
    try:
        label, prediction, prediction1 = predict_pollute(i,0.001)
    except:
        print(i)

    if 'label' in dir():
        if label == prediction and prediction == prediction1:
            result.append(0)
        if label == prediction and label != prediction1:
            result.append(1)
        if label != prediction and label == prediction1:
            result.append(2)
        if label != prediction and label != prediction1 and prediction == prediction1:
            result.append(3)
        if label != prediction and label != prediction1 and prediction != prediction1:
            result.append(4)

print('Total test_images number: %d \n' % len(result),
      '%s : %d \n' % (tag[0], result.count(0)),
      '%s : %d \n' % (tag[1], result.count(1)),
      '%s : %d \n' % (tag[2], result.count(2)),
      '%s : %d \n' % (tag[3], result.count(3)),
      '%s : %d \n' % (tag[4], result.count(4))
      )
