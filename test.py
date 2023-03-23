import time
import cv2
import numpy as np
camera_path = r'D:\FPT\ky5\AIP391\My Project\yolov5_potholes_detection\test_video\video_duong_ban_dem.mp4'
cap = cv2.VideoCapture(camera_path)

while cap.isOpened():
    
    start_time = time.perf_counter()
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 640))
    if not ret:
        break
    end_time = time.perf_counter()
    fps = 1 / np.round(end_time - start_time, 3)
    cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
    cv2.imshow("img", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break