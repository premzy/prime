import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
  reg, frame = cap.read()
  cv2.imshow("webcam window", frame)
  k = cv2.waitKey(25)
  if k == 27:
    break
  else:
    print "press the 'esc' key"
    
cap.release()
cv2.destroyAllWindow()
