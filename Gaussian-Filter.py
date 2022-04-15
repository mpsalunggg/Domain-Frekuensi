import cv2

img_path = r"spongebob.jpg"

img = cv2.imread(img_path)

blur_img = cv2.GaussianBlur(img, (9, 9), sigmaX=34, sigmaY=36)

cv2.imwrite("hasil_gaussian2jpg", blur_img)