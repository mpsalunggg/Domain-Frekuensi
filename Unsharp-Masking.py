import cv2

image = cv2.imread("spongebob.jpg")
gaussian_3 = cv2.GaussianBlur(image, (0, 0), 2.0)
unsharp_image = cv2.addWeighted(image, 2.5, gaussian_3, -1.0, 0)
cv2.imwrite("hasil_unsharp.jpg", unsharp_image)