import os
import cv2

def resize_image(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    resized_image = cv2.resize(image, (50, 50))

    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)

def iterate_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(file_path)
            resize_image(file_path,file_path)

for i in range(10):
    folder_path = f"dataset/test/{i}"
    iterate_files(folder_path)
