import cv2
cap = cv2.Videocapture("Dance.mp4")
if(cap.isopened() == False):
    print("error opening video")

while(cap.isopned()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow("frame",frame)

        if cv2.waitKey(25) == ord("q"):
            break
    else:
            break

cap.release()
cv2.destroyAllWindows()
    