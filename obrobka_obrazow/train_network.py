#!/usr/bin/python3

# Following script trains CNN model for satellite images classification and saves it for later use without retraining.
# In order to do this, we used Tensorfow (keras).

###########################################
###  Script by @gmikx (Mikołaj Giza)    ###
###  CatSat Team in CanSat Competition  ###
###########################################


# Import Needed Libraries
import os
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, save_model
from keras import layers
from keras.callbacks import EarlyStopping


# Find Localisation of This File in Filesystem
path_to_this_file = os.path.dirname(os.path.realpath(__file__))


# Data Preprocessing

# Preprocessing Training Set Data
train_datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True)
training_set = train_datagen.flow_from_directory(f'{path_to_this_file}/dataset/train',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='categorical')

# Preprocessing Test Set Data
test_datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True)
test_set = test_datagen.flow_from_directory(f'{path_to_this_file}/dataset/test',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='categorical')

# Store the Number of Classes Found and the Classes Themselves in Variables.
classes = training_set.class_indices
no_of_classes = len(classes)


# Building the C(onvolutional)N(eural)N(etwork)

# Initialise CNN
cnn = Sequential()

# Add convolution layer #1
cnn.add(layers.Conv2D(filters=34, kernel_size=3, activation='relu',
        padding='same', input_shape=[64, 64, 3]))

# Pooling
cnn.add(layers.MaxPooling2D((2, 2)))

# Add convolution layer #2
cnn.add(layers.Conv2D(filters=64, kernel_size=3,
        activation='relu', padding='valid'))

# Pooling
cnn.add(layers.MaxPooling2D((2, 2)))

# Flattening
cnn.add(layers.Flatten())

# Full connection
cnn.add(layers.Dense(units=200, activation='relu'))

# Output Layer
cnn.add(layers.Dense(units=no_of_classes, activation='softmax'))


# Train the Model

# Early Stop - stop the training if there's no more improvement in model performance.
# This operation saves time and prevents overfitting
early_stop = EarlyStopping(
    patience=5, min_delta=0.001, restore_best_weights=True)

# Compile the Network
cnn.compile(optimizer='adam', loss='categorical_crossentropy',
            metrics=['accuracy'])

# Fit the Network
cnn.fit(x=training_set, validation_data=test_set,
        epochs=25, callbacks=[early_stop])


# Evaluating the model
result = cnn.evaluate(test_set)
print(f'Test loss: {result[0]}')
print(f'Test accuracy: {result[1]}')

# Save the Trained Model
path_to_save = f'{path_to_this_file}/best_model'
cnn.save(path_to_save)
print(f'Model saved in {path_to_save}!')
