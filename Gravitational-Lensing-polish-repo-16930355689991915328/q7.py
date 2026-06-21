import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("hubble-lrg3757.bmp")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
crop = gray[325:650, 600:950]

plt.figure(figsize=(10,10))
plt.imshow(crop, cmap='gray')
plt.title("Cropped ring")
plt.axis('off')
plt.show()

_, thresh = cv2.threshold(crop, 90, 255, cv2.THRESH_BINARY)

# Estimate center and theta_E from the crop
# The ring is roughly centered in the crop
h, w = crop.shape
center = (w//2, h//2)
# By looking at the image, we can estimate theta_E in pixels.
# Let's say theta_E is around 80 pixels.
theta_e = 85

# Create de-lensed image
reconstructed = np.zeros_like(crop)

for i in range(h):
    for j in range(w):
        # move origin to center
        y = i - center[1]
        x = j - center[0]

        theta = np.sqrt(x**2 + y**2)
        if theta == 0: continue

        # Lens equation: beta = theta * (1 - theta_e^2 / theta^2)
        beta = theta * (1 - (theta_e**2 / theta**2))

        # map back to pixel coords
        ix = int(beta * (x/theta) + center[0])
        iy = int(beta * (y/theta) + center[1])

        if 0 <= ix < w and 0 <= iy < h:
            # simple additive mapping to handle multiple pixels mapping to same source
            # using max to keep brightness
            reconstructed[iy, ix] = max(reconstructed[iy, ix], crop[i, j])

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(crop, cmap='gray')
plt.title("Lensed (Cropped)")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(thresh, cmap='gray')
plt.title("Thresholded")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(reconstructed, cmap='gray')
plt.title("Reconstructed Source")
plt.axis('off')

plt.tight_layout()
plt.show()









    