import cv2
import matplotlib.pyplot as plt

cascade_path = '/home/kawai/opencv/data/haarcascades/haarcascade_frontalface_default.xml'

def face_detection(img_src):
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(img_gray)
    if len(facerect) == 0:
        print('No face detected')
        return None

    rect = facerect[0]
    cv2.rectangle(
        img_src,
        tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]),
        (255, 255, 255),
        thickness=2)
    return img_src

if __name__ == "__main__":
    lena_path = './lena.png'
    lena_src = cv2.imread(lena_path)
    lena_face_detected = face_detection(lena_src)
    if lena_face_detected is None:
        img_show = lena_src
    else:
        img_show = cv2.cvtColor(lena_face_detected, cv2.COLOR_BGR2RGB)
    plt.imshow(img_show)
    plt.show()
