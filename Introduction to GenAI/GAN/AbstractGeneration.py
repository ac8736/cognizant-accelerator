import tensorflow as tf
from keras._tf_keras.keras.preprocessing import image_dataset_from_directory
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import layers

IMG_SIZE = 64  
BATCH_SIZE = 32

dataset = image_dataset_from_directory(
    "dataset",
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    label_mode=None 
)

def normalize(image):
    image = tf.cast(image, tf.float32) / 255.0
    return image

dataset = dataset.map(lambda x: normalize(x))

generator = keras.Sequential([
    layers.Dense(8*8*256, use_bias=False, input_shape=(100,)),
    layers.BatchNormalization(),
    layers.LeakyReLU(),
    layers.Reshape((8, 8, 256)),
    layers.Conv2DTranspose(128, (5, 5), strides=(2, 2), padding="same", use_bias=False),
    layers.BatchNormalization(),
    layers.LeakyReLU(),
    layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding="same", use_bias=False),
    layers.BatchNormalization(),
    layers.LeakyReLU(),
    layers.Conv2DTranspose(3, (5, 5), strides=(2, 2), padding="same", activation="tanh")
])

discriminator = keras.Sequential([
    layers.Conv2D(64, (5, 5), strides=(2, 2), padding="same", input_shape=(64, 64, 3)),
    layers.LeakyReLU(),
    layers.Dropout(0.3),
    layers.Conv2D(128, (5, 5), strides=(2, 2), padding="same"),
    layers.LeakyReLU(),
    layers.Dropout(0.3),
    layers.Flatten(),
    layers.Dense(1, activation="sigmoid")
])

cross_entropy = keras.losses.BinaryCrossentropy()

def generator_loss(fake_output):
    return cross_entropy(tf.ones_like(fake_output), fake_output)

def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    return real_loss + fake_loss

generator_optimizer = keras.optimizers.Adam(1e-4)
discriminator_optimizer = keras.optimizers.Adam(1e-4)

LATENT_DIM = 100

def train_step(real_images):
    noise = tf.random.normal([BATCH_SIZE, LATENT_DIM])  # Random noise

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_output = discriminator(real_images, training=True)
        fake_output = discriminator(generated_images, training=True)

        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    gradients_gen = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_disc = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

    generator_optimizer.apply_gradients(zip(gradients_gen, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_disc, discriminator.trainable_variables))

    return gen_loss, disc_loss

def generate_and_save_images(epoch, noise_dim=LATENT_DIM):
    noise = tf.random.normal([1, noise_dim])
    generated_image = generator(noise, training=False)[0]

    plt.imshow(generated_image)
    plt.axis("off")
    plt.title(f"Epoch {epoch}")
    plt.show()

def train(dataset, epochs):
    for epoch in range(epochs):
        print(f"Epoch {epoch+1}/{epochs}")
        for image_batch in dataset:
            gen_loss, disc_loss = train_step(image_batch)

        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch+1}, Gen Loss: {gen_loss.numpy():.4f}, Disc Loss: {disc_loss.numpy():.4f}")
            generate_and_save_images(epoch + 1)

train(dataset, 500)
