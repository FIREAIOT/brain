    i = 0
    scores = np.squeeze(scores)
    boxes = np.squeeze(boxes)

    for box in boxes:
      if(scores[i] > 0.6):
        print "box number {} has a score of {}".format(i, scores[i])
        (h, w, l) = image.shape
        ymin, xmin, ymax, xmax = box
        startY = int(ymin * h)
        startX = int(xmin * w)
        endY = int(ymax * h)
        endX = int(xmax * w)

        cv2.rectangle(image, (startY, startX), (endX, endY), (0,255,0), 3)
      i += 1