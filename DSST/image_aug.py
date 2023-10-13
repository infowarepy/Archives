import cv2
import imgaug as ia
from imgaug import augmenters as iaa
import os

input_dir = 'dataset/[5]input_images/'
output_dir = 'dataset/test/5/'
os.makedirs(output_dir, exist_ok=True)

augmentation = iaa.Sequential([
    iaa.Affine(rotate=(-15, 15), scale=(0.8, 1.2)),
    iaa.GaussianBlur(sigma=(0, 1.0)),
    iaa.AdditiveGaussianNoise(scale=(0, 0.05*255)),
    iaa.Multiply((0.8, 1.2))
])
input_images = os.listdir(input_dir)


for image_name in input_images:
    image_path = os.path.join(input_dir, image_name)
    image = cv2.imread(image_path)

    augmented_images = augmentation(images=[image] * 20)  # Generate 100 augmented images

    for i, augmented_image in enumerate(augmented_images):
        output_image_name = f"augmented_{i}_{image_name}"
        output_image_path = os.path.join(output_dir, output_image_name)
        cv2.imwrite(output_image_path, augmented_image)
