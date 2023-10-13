import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten, Conv2D, AveragePooling2D, BatchNormalization, Dropout, MaxPooling2D
from tensorflow.keras.regularizers import l2
from tensorflow.keras.layers import Activation

# generators
train_ds = keras.utils.image_dataset_from_directory(
    directory = 'dataset/train',
    labels='inferred',
    label_mode = 'int',
    batch_size=32,
    image_size=(50,50),
    shuffle=True
)

validation_ds = keras.utils.image_dataset_from_directory(
    directory = 'dataset/test',
    labels='inferred',
    label_mode = 'int',
    batch_size=32,
    image_size=(50,50),
    shuffle=True
)

def preprocessing(image, label):
    image = tf.image.rgb_to_grayscale(image)
    image = tf.cast(image / 255., tf.float32)
    return image, label

train_ds = train_ds.map(preprocessing)
validation_ds = validation_ds.map(preprocessing)

# LENET CNN architecture with batch normalization and dropout layer to reduce overfitting
model = Sequential()

model.add(Conv2D(6,kernel_size=(5,5),padding='same',activation='tanh',input_shape=(50,50,1)))
model.add(BatchNormalization())
model.add(AveragePooling2D(pool_size=(2,2),strides=2,padding='valid'))

model.add(Conv2D(16,kernel_size=(5,5),padding='valid',activation='tanh'))
model.add(BatchNormalization())
model.add(AveragePooling2D(pool_size=(2,2),strides=2,padding='valid'))

model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(32,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(10,activation='softmax'))

model.summary()

model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

history=model.fit(train_ds,epochs=20,validation_data=validation_ds)

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'],color='red',label='train')
plt.plot(history.history['val_accuracy'],color='blue',label='validation')
plt.legend()
plt.show()

plt.plot(history.history['loss'],color='red',label='train')
plt.plot(history.history['val_loss'],color='blue',label='validation')
plt.legend()
plt.show()

from tensorflow.keras.models import load_model
model.save('/content/drive/MyDrive/Infoware/symbol_recognition.h5')

import cv2
img_list=[]
for i in range(10):
  img=cv2.imread(f'drawn{i}.png')
  img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img = cv2.resize(img, (50, 50))
  img = img.reshape((1,50,50,1))
  img_list.append(img)

for i in range(10):
  print(f'drawn{i}= ',model.predict(img_list[i]).argmax(axis=1))

len(img_list[4][0])

