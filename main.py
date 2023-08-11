import cupy as cp
from PIL import Image
import os

def expand_images(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_folder, filename))
            img = cp.array(img)  # Chuyển đổi ảnh sang CuPy array

            image_width, image_height = img.shape[1], img.shape[0]

            new_image_width = image_width * width
            new_image_height = image_height * height

            new_image = cp.zeros((new_image_height, new_image_width, 3), dtype=cp.uint8)

            for i in range(height):
                for j in range(width):
                    new_image[i * image_height: (i + 1) * image_height, j * image_width: (j + 1) * image_width] = img

            new_image_pil = Image.fromarray(cp.asnumpy(new_image))  # Chuyển đổi CuPy array sang PIL image
            new_image_pil.save(os.path.join(output_folder, f"{filename.split('.')[0]}_expanded.jpg"))  # Thay đổi file format nếu cần

if __name__ == "__main__":
    input_folder = "images"  # Thay đổi đường dẫn tới thư mục ảnh đầu vào của bạn
    output_folder = "output"  # Thay đổi đường dẫn tới thư mục output mong muốn

    width = int(input("Nhập chiều ngang: "))
    height = int(input("Nhập chiều cao: "))

    expand_images(input_folder, output_folder, width, height)
