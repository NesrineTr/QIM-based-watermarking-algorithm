import numpy as np
import cv2
import matplotlib.pyplot as plt

def display_image(image, title='', filename=None):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    if filename:
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
    else:
        plt.show()

def quantize_image(image, delta):
    return np.round(image / delta) * delta

def insert_watermark(image, watermark_bits, delta):
    watermarked_image = np.copy(image)
    modified_mask = np.zeros_like(image) 
    rows, cols = image.shape
    bit_index = 0 

    for i in range(rows):
        for j in range(cols):
            if bit_index < len(watermark_bits):
                if watermark_bits[bit_index] == '1':
                    watermarked_image[i+100, j+100] += delta
                    modified_mask[i+100, j+100] = 255 
                bit_index += 1
           

    return watermarked_image, modified_mask

def string_to_bits(s):
    return ''.join(format(ord(char), '08b') for char in s)



original_image = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('original_image.png', original_image)

delta = 5

quantized_image = quantize_image(original_image, delta)
cv2.imwrite('quantized_image.png', quantized_image)


phrase = "Nesrine"
watermark_bits = string_to_bits(phrase)

max_bits = original_image.size
if len(watermark_bits) > max_bits:
    raise ValueError("La phrase est trop longue pour être insérée dans l'image.")

watermarked_image, modified_mask = insert_watermark(quantized_image, watermark_bits, delta)
cv2.imwrite('watermarked_image.png', watermarked_image)

display_image(modified_mask, title='Modified Pixels Mask', filename='modified_mask.png')




