import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

dataset_path = "dataset"

img_size = (224, 224)
batch_size = 32

# Load dataset
train_ds = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=img_size,
    batch_size=batch_size
)

class_names = train_ds.class_names
print("Classes:", class_names)

<<<<<<< HEAD
# Normalize
normalization_layer = layers.Rescaling(1./255)

# Data Augmentation 
=======
# ✅ Normalize
normalization_layer = layers.Rescaling(1./255)

# ✅ Data Augmentation (NEW 🔥)
>>>>>>> a1c44a7b169c8d13f2e681654854b7fb82e1c176
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.2),
    layers.RandomBrightness(0.2)
])

# Apply preprocessing
train_ds = train_ds.map(lambda x, y: (data_augmentation(normalization_layer(x)), y))
val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))

<<<<<<< HEAD
# performance optimization
=======
# ✅ Performance optimization
>>>>>>> a1c44a7b169c8d13f2e681654854b7fb82e1c176
train_ds = train_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=tf.data.AUTOTUNE)

# Base model
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224,224,3),
    include_top=False,
    weights='imagenet'
)

<<<<<<< HEAD
=======
# ✅ Freeze some layers (IMPORTANT FIX)
>>>>>>> a1c44a7b169c8d13f2e681654854b7fb82e1c176
for layer in base_model.layers[:-20]:
    layer.trainable = False

# Model
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
<<<<<<< HEAD
    layers.BatchNormalization(),   
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.4),           
=======
    layers.BatchNormalization(),   # NEW
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.4),           # Increased
>>>>>>> a1c44a7b169c8d13f2e681654854b7fb82e1c176
    layers.Dense(len(class_names), activation='softmax')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

<<<<<<< HEAD
# Early stopping 
=======
# ✅ Early stopping (NEW 🔥)
>>>>>>> a1c44a7b169c8d13f2e681654854b7fb82e1c176
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

history = model.fit(
    train_ds,
    validation_data=val_ds,
<<<<<<< HEAD
    epochs=30,   
=======
    epochs=30,   # increased but controlled by early stopping
>>>>>>> a1c44a7b169c8d13f2e681654854b7fb82e1c176
    callbacks=[early_stop]
)

model.save("sugarcane_model.h5")

print("Training complete and model saved.")