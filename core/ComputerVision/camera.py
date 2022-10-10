import cv2
from djitellopy import tello
drone = tello.Tello()


def set_camera():
    if True:
        drone.stream_on()
    while True:
        image = drone.get_frame_read().frame
        image = cv2.resize(image,(300, 300))
        cv2.imshow('display', image)
        cv2.waitKey(1)


if __name__ == '__main__':
    set_camera()
