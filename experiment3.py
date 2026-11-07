# ==============================================================================
# Developed By: Mithik jain G
# Register No: 212224240087
# Experiment 3: Histogram Equalization Using OpenCV (Grayscale & Color Images)
# ==============================================================================

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    image_name = 'n14.jpg' if os.path.exists('n14.jpg') else 'parrot.jpg'
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)

    # --------------------------------------------------------------------------
    # Part A: Grayscale Histogram Equalization
    # --------------------------------------------------------------------------
    print("[INFO] Processing Grayscale Histogram Equalization...")
    gray = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        print(f"[ERROR] Could not load image from '{image_name}'.")
        return

    # Step 3: Grayscale Image & Histogram
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title('Grayscale Histogram')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "step3_grayscale_histogram.png"))
    plt.close()

    # Step 4: Equalization
    equalized = cv2.equalizeHist(gray)

    # Step 5: 2x2 Grid for Grayscale
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plt.imshow(gray, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title('Original Histogram')

    plt.subplot(2, 2, 3)
    plt.imshow(equalized, cmap='gray')
    plt.title('Equalized Grayscale Image')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.hist(equalized.ravel(), 256, [0, 256])
    plt.title('Equalized Histogram')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "step5_grayscale_2x2_grid.png"))
    plt.close()
    print("[SUCCESS] Grayscale equalization outputs saved.")

    # --------------------------------------------------------------------------
    # Part B: Color Image Histogram Equalization
    # --------------------------------------------------------------------------
    print("[INFO] Processing Color Image Histogram Equalization...")
    img = cv2.imread(image_name)

    # Step 6: Original Color Image
    plt.figure(figsize=(6, 5))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Color Image')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "step6_original_color_image.png"))
    plt.close()

    # Step 7: BGR Histogram
    b, g, r = cv2.split(img)
    plt.figure(figsize=(8, 5))
    plt.hist(b.ravel(), 256, [0, 256], color='blue', label='Blue')
    plt.hist(g.ravel(), 256, [0, 256], color='green', label='Green')
    plt.hist(r.ravel(), 256, [0, 256], color='red', label='Red')
    plt.title('BGR Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "step7_bgr_histogram.png"))
    plt.close()

    # Step 8, 9, 10: HSV Equalization on V Channel
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v_equalized = cv2.equalizeHist(v)
    hsv_equalized = cv2.merge((h, s, v_equalized))
    enhanced = cv2.cvtColor(hsv_equalized, cv2.COLOR_HSV2BGR)

    # Step 11: 2x2 Grid for Color
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Color Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    for channel, color, name in zip(cv2.split(img),
                                     ['blue', 'green', 'red'],
                                     ['Blue', 'Green', 'Red']):
        hist = cv2.calcHist([img], [['Blue', 'Green', 'Red'].index(name)],
                            None, [256], [0, 256])
        plt.plot(hist, color=color, label=name)
    plt.title('Original Color Histogram')
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB))
    plt.title('Enhanced Color Image')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    for i, color in enumerate(['blue', 'green', 'red']):
        hist = cv2.calcHist([enhanced], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=color.capitalize())
    plt.title('Enhanced Color Histogram')
    plt.legend()

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "step11_color_2x2_grid.png"))
    plt.close()
    print("[SUCCESS] Color equalization outputs saved.")

if __name__ == "__main__":
    main()
