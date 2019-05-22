import cv2


im = cv2.imread('image.jpg')


ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()


ss.setBaseImage(im)


ss.switchToSelectiveSearchFast()




rects = ss.process()




numShowRects = 100


increment = 50

while True:
 
  imOut = im.copy()

 
  for i, rect in enumerate(rects):
    
      if (i < numShowRects):
          x, y, w, h = rect
          cv2.rectangle(imOut, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
      else:
          break


  cv2.imshow("Output", imOut)

 
  k = cv2.waitKey(0) & 0xFF

  
  if k == 109:
      numShowRects += increment
  
  elif k == 108 and numShowRects > increment:
      numShowRects -= increment
 
  elif k == 113:
      break


cv2.destroyAllWindows()