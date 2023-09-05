import cv2
cap = cv2.VideoCapture('sample2.mp4')
cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

c = 0
while(1):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # This condition prevents from infinite looping
    # incase video ends.
    if ret == False:
        break

    # Operation on the frame came here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    HUMANS = cascade.detectMultiScale(gray, 1.9, 1)

    # Display the resulting frame 
    for (x, y, w, h) in HUMANS:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("FRAME", frame)
    print(len(HUMANS))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release video object
cap.release()

# Destroy all windows
cv2.destroyAllWindows()

