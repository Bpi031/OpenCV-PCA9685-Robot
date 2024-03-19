import cv2

def detect_qr_codes(camera_id=0, delay=1, window_name='OpenCV QR Code'):
    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(camera_id)

    try:
        for _ in iter(lambda: cap.isOpened(), False):
            ret, frame = cap.read()

            if ret:
                ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
                if ret_qr:
                    for s, p in zip(decoded_info, points):
                        if s:
                            print(s)
                            color = (0, 255, 0)
                        else:
                            color = (0, 0, 255)
                        frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
                cv2.imshow(window_name, frame)

            cv2.waitKey(delay)
    except KeyboardInterrupt:
        pass

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Call the function
    detect_qr_codes()