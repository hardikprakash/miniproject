import model, cv2, mtcnn, methods


def main(isHeadless, doRefresh):
    required_shape = (160, 160)
    face_encoder = model.InceptionResNetV2()
    path_m = "facenet_keras_weights.h5"
    face_encoder.load_weights(path_m)
    encodings_path = 'encodings/encodings.pkl'
    face_detector = mtcnn.MTCNN()
    encoding_dict = methods.load_pickle(encodings_path)
    detected_names = set()
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("VidSrc Error")
            break

        frame = methods.detect(frame, face_detector, face_encoder, encoding_dict, doRefresh, detected_names)

        if not isHeadless:
            cv2.imshow('camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
