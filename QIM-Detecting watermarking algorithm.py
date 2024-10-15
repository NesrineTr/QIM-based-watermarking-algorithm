import numpy as np
import cv2



def extract_watermark(quantized_image,watermarked_image , delta, watermark_binary_length):
    rows, cols = watermarked_image.shape
    extracted_bits = []


    for i in range(rows):
        for j in range(cols):
            if len(extracted_bits) < watermark_binary_length:
                if watermarked_image[i+100, j+100] == quantized_image[i+100, j+100]+delta: 
                    extracted_bits.append('1')
                else:
                    extracted_bits.append('0') 

    watermark = ''
    for i in range(0, len(extracted_bits), 8):  
        byte = ''.join(extracted_bits[i:i+8]) 
        if len(byte) == 8: 
            watermark += chr(int(byte, 2))

    return watermark

delta = 5
original_image = cv2.imread('quantized_image.png', cv2.IMREAD_GRAYSCALE)
watermarked_image = cv2.imread('watermarked_image.png', cv2.IMREAD_GRAYSCALE)
watermark_binary_length = 56

extracted_watermark = extract_watermark( original_image, watermarked_image, delta, watermark_binary_length)
print("Watermark extrait :", extracted_watermark)
