import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


def build_model(num_classes, input_shape=(300, 300, 3)):
    base_model = EfficientNetB3(
        weights="imagenet",
        include_top=False,
        input_shape=input_shape
    )

    # 🔥 Deeper fine-tuning
    for layer in base_model.layers[:-120]:
        layer.trainable = False
    for layer in base_model.layers[-120:]:
        layer.trainable = True

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(512, activation="relu")(x)
    x = Dropout(0.5)(x)
    output = Dense(num_classes, activation="softmax")(x)

    model = Model(inputs=base_model.input, outputs=output)

    model.compile(
        optimizer=Adam(learning_rate=3e-5),  # 🔥 slightly higher
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model