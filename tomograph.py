#!/usr/bin/env python
import math as math
import Image
#from PIL import Image
#from pylab import cm
import numpy as np
#from numpy import *
from cv2 import *
#import matplotlib.pyplot as plt
#import msvcrt 

def drawRay(x1, y1, x2, y2, matrix):
  result = 0
  if x1 <= x2:
    kx = 1
  else:
    kx = -1
  if y1 <= y2:
    ky = 1
  else:
    ky = -1
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  #print matrix[x1][y1]
  #result += matrix[x1][y1][1]
  #print x1, y1
  if dx >= dy:
    e = dx/2
    for i in range(dx):
      x1 = x1 + kx
      e = e - dy
      if e < 0:
        y1 = y1 + ky
        e = e + dx
      #print x1, y1
      result += matrix[x1][y1][1]
      #print matrix[x1][y1]
  else:
    e = dy/2
    for i in range(dy):
      y1 = y1 + ky
      e = e - dx
      if e < 0:
        x1 = x1 + kx
        e = e + dy
      #print x1, y1
      #print matrix[x1][y1]
      result += matrix[x1][y1][1]
  result -= matrix[x1][y1][1]
  return result

def drawRay2(x1, y1, x2, y2, matrix):
  result = 0
  xEnd, yEnd, zEnd = matrix.shape
  x = x1;
  y = y1;
  print "start"
  print x1, y1, x2, y2
  #ustalenie kierunku rysowania
  if x1 < x2:
    xi = 1
    dx = x2 - x1
  else:
    x1 = -1
    dx = x1 - x2
  if y1 < y2:
    yi = 1
    dy = y2 - y1
  else:
    yi = -1
    dy = y1 - y2
  #pierwszy piksel
  #if ((x > 0) and (y > 0)):
  result += matrix[x][y][1]
    #print "dodaje"
  print matrix[x][y]
  #matrix[x][y] = 1
  #wybor osi wiodacej
  if dx > dy: #os OX
    ai = (dy - dx) * 2
    bi = dy * 2
    d = bi - dx
    while x != x2:
      if d >= 0:
        x += xi
        y += yi
        d += ai
      else:
        d += bi
        x += xi
      #matrix[x][y] = [0, 250, 0]
      #if ((x > 0) and (y > 0)):
        #print "dodaje"
      print matrix[x][y]
      result += matrix[x][y][1]
  else:#os OY
    ai = (dx - dy) * 2
    bi = dx * 2
    d = bi - dy
    while y != y2:
      if d >= 0:
        x += xi
        y += yi
        d += ai
      else:
        d += bi
        y += yi
      #matrix[x][y] = [0, 250, 0]
      #if ((x > 0) and (y > 0)):
        #print "dodaje"
      print matrix[x][y]
      result += matrix[x][y][1]
  return result
def drawCircle(x0, y0, r, matrix):
  circle = [[] for i in range(8)]
  x = r;
  y = 0;
  error = 1 - x;
  while x >= y:
    matrix[x+x0][y+y0] = [250, 0, 0]
    matrix[y+x0][x+y0] = [250, 0, 0]
    matrix[-y+x0][x+y0] = [250, 0, 0]
    matrix[-x+x0][y+y0] = [250, 0, 0]
    matrix[-x+x0][-y+y0] = [250, 0, 0]
    matrix[-y+x0][-x+y0] = [250, 0, 0]
    matrix[y+x0][-x+y0] = [250, 0, 0]
    matrix[x+x0][-y+y0] = [250, 0, 0]
    circle[0].append((x+x0,y+y0)) 
    circle[1].append((y+x0, x+y0))
    circle[2].append((-y+x0, x+y0))
    circle[3].append((-x+x0, y+y0))
    circle[4].append((-x+x0, -y+y0))
    circle[5].append((-y+x0, -x+y0))
    circle[6].append((y+x0, -x+y0))
    circle[7].append((x+x0, -y+y0))
    y += 1
    if error < 0:
      error += 2 * y + 1
    else:
      x -= 1
      error += 2 * (y - x) + 1

  result = []
  for i in range(8):
    result += circle[i]
  return result

def repaintCircle(matrix, circle):
  for i in range (len(circle)):
    matrix[circle[i][0]][circle[i][1]] = [250, 0, 0]

def drawCircle2(x0, y0, r, matrix):
  step = math.atan(1.0/r)
  alpha = 0
  circle = []
  while alpha <= 2*np.pi:
    x = x0 + round(np.cos(alpha)*r)
    y = y0 + round(np.sin(alpha)*r)
    matrix[x][y] = [250, 0, 0]
    alpha += step
    circle.append((x,y))
  return circle

def drawArc(x0, y0, r, matrix, circle, alpha, beta):
  alpha = alpha%360
  beta = beta%360
  xAlpha = x0 + round(np.cos(np.radians(alpha))*r)
  yAlpha = y0 + round(np.sin(np.radians(alpha))*r)
  xBeta = x0 + round(np.cos(np.radians(beta))*r)
  yBeta = y0 + round(np.sin(np.radians(beta))*r)
  err = 0
  if ((matrix[xAlpha][yAlpha] == [250, 0, 0]).all()):
    err = 0
  elif ((matrix[xAlpha-1][yAlpha] == [250, 0, 0]).all()):
    xAlpha -= 1
  elif ((matrix[xAlpha+1][yAlpha] == [250, 0, 0]).all()):
    xAlpha += 1
  elif ((matrix[xAlpha-1][yAlpha-1] == [250, 0, 0]).all()):
    xAlpha -= 1
    yAlpha -= 1
  elif ((matrix[xAlpha-1][yAlpha+1] == [250, 0, 0]).all()):
    xAlpha -= 1
    yAlpha += 1
  elif ((matrix[xAlpha][yAlpha-1] == [250, 0, 0]).all()):
    yAlpha -= 1
  elif ((matrix[xAlpha][yAlpha+1] == [250, 0, 0]).all()):
    yAlpha += 1
  elif ((matrix[xAlpha+1][yAlpha-1] == [250, 0, 0]).all()):
    xAlpha += 1
    yAlpha -= 1
  elif ((matrix[xAlpha+1][yAlpha+1] == [250, 0, 0]).all()):
    xAlpha += 1
    yAlpha += 1
  else:
    err = 1
  
  err = 0
  if ((matrix[xBeta][yBeta] == [250, 0, 0]).all()):
    err = 0
  elif ((matrix[xBeta-1][yBeta] == [250, 0, 0]).all()):
    xBeta -= 1
  elif ((matrix[xBeta+1][yBeta] == [250, 0, 0]).all()):
    xBeta += 1
  elif ((matrix[xBeta-1][yBeta-1] == [250, 0, 0]).all()):
    xBeta -= 1
    yBeta -= 1
  elif ((matrix[xBeta-1][yBeta+1] == [250, 0, 0]).all()):
    xBeta -= 1
    yBeta += 1
  elif ((matrix[xBeta][yBeta-1] == [250, 0, 0]).all()):
    yBeta -= 1
  elif ((matrix[xBeta][yBeta+1] == [250, 0, 0]).all()):
    yBeta += 1
  elif ((matrix[xBeta+1][yBeta-1] == [250, 0, 0]).all()):
    xBeta += 1
    yBeta -= 1
  elif ((matrix[xBeta+1][yBeta+1] == [250, 0, 0]).all()):
    xBeta += 1
    yBeta += 1
  else:
    err = 1
  if not err:
    matrix[xAlpha][yAlpha] = [0, 0, 250]
    matrix[xBeta][yBeta] = [0, 0, 250]
  if beta > alpha:
    for i in range (len(circle)):
      if circle[i] == (xAlpha, yAlpha):
        for j in range(i, len(circle)):
          if circle[j] == (xBeta, yBeta):
            #print "BREAK" 
            break
          matrix[circle[j][0]][circle[j][1]] = [0, 0, 250]
  else:
    for i in range (len(circle)):
      if circle[i] == (xAlpha, yAlpha):
        for j in range (i, len(circle)):
          matrix[circle[j][0]][circle[j][1]] = [0, 0, 250]
    for i in range (len(circle)):
      if circle[i] == (xBeta, yBeta):
        break
      matrix[circle[i][0]][circle[i][1]] = [0, 0, 250]

def createDetectors(width, circle):
  count = 0
  result = []
  while circle:
    tmp = []
    while ((count < width) and circle):
      count += 1
      tmp.append(circle.pop())
    result.append(tmp)
    count = 0
  return result

def calculateEmiterDistance(x, y, distance):
  distance += round(math.sqrt(x**2 + y**2)/2 + 1)
  return distance

def drawEdge(matrix, emiterDistance):
  x, y, z = matrix.shape
  if x > y:
    tmpmat = np.zeros((x, (x-y)/2, 3), np.uint8)
    matrix = np.hstack((tmpmat, matrix))
    matrix = np.hstack((matrix, tmpmat))
  elif y > x:
    tmpmat = np.zeros(((y-x)/2, y, 3), np.uint8)
    matrix = np.concatenate((tmpmat, matrix))
    matrix = np.concatenate((matrix, tmpmat))
  x, y, z = matrix.shape
  print 'x, y: ', x, y, 'emiterDistance: ', emiterDistance
  tmpmat = np.zeros((20+emiterDistance-x/2, y, 3), np.uint8)
  matrix = np.concatenate((tmpmat, matrix))
  matrix = np.concatenate((matrix, tmpmat))
  x, y, z = matrix.shape
  print 'x, y: ', x, y, 'emiterDistance: ', emiterDistance
  tmpmat = np.zeros((x, 20+emiterDistance-y/2, 3), np.uint8)
  print tmpmat.shape
  matrix = np.hstack((tmpmat, matrix))
  matrix = np.hstack((matrix, tmpmat))
  x, y, z = matrix.shape
  print 'x, y: ', x, y, 'emiterDistance: ', emiterDistance
  return matrix

def middleDetectors(detectors):
  result = []
  for i in range(len(detectors)):
    result.append(detectors[i][len(detectors[i])//2])
  return result
    #print "Detector"
    #print detectors[i]
    #print "Middle"
    #print detectors[i][len(detectors[i])//2]

def acquisition(matrix, middleDetectors, alpha, emiterDistance, maxPixels):
  angle = 0
  x, y, z = matrix.shape
  result = []
  while angle <= 360:
    tmp = []
    emiterPositionX = x/2 + round(np.cos(np.radians(angle))*emiterDistance)
    emiterPositionY = y/2 + round(np.sin(np.radians(angle))*emiterDistance)
    for i in range(len(middleDetectors)):
      middleX, middleY = middleDetectors[i]
      #print emiterPositionX, emiterPositionY, middleX, middleY
      absorption = drawRay(int(emiterPositionX), int(emiterPositionY), int(middleX), int(middleY), matrix)
      normalAbsorption = int(round(255.0*(absorption/(255.0*maxPixels))))
      #print normalAbsorption
      tmp.append(normalAbsorption)
      #print absorption
    angle += alpha
    result.append(tmp)
  return result

#matrix = np.zeros((200,200, 3), np.uint8)
img = imread('data/kwadraty.png')
#imgGray = imread('data/image3.jpg', 0)
#imshow('imgae', img2)
#img2 = Image.fromarray(np.uint8(cm.gist_earth(img)))
#img = img.resize((100, 100), Image.BILINEAR)
print img.shape
x, y, z = img.shape
if x > y:
  maxPixels = x
else:
  maxPixels = y
print maxPixels
emiterDistance = 50
detectorWidth = 4
alpha = 1
beta = 30
emiterDistance = calculateEmiterDistance(x, y, emiterDistance)
img = drawEdge(img, emiterDistance)
x, y, z = img.shape
print 'XYZ: ', x, y, z
circle = drawCircle2(x/2, y/2, emiterDistance, img)
circletmp = circle[:]
detectors = createDetectors(detectorWidth, circletmp)
middlePoints = middleDetectors(detectors)
a = acquisition(img, middlePoints, alpha, emiterDistance, maxPixels)
#imshow('D', a)
img3 = np.asmatrix(np.array(a, dtype=np.uint8))
#im = Image.fromarray(np.array(a))
#im.show()
namedWindow('X', WINDOW_NORMAL)
resizeWindow('X', 400, 400)
imshow('X', img)
imshow('A', img3)
#namedWindow('TEST', WINDOW_NORMAL)
#resizeWindow('TEST', 400, 400)
#plt.imshow(matrix, cmap='gray')
while(1):
  #plt.imshow(matrix)
  #plt.show()
  begin = alpha + 180 - beta
  end = alpha + 180 + beta
  repaintCircle(img, circle)
  drawArc(x/2, y/2, emiterDistance, img, circle, begin, end)
  imshow('X', img)
  #imshow('TEST', matrix)
  #c = msvcrt.getch()
  #print 'wcisnales', c 
  key = waitKey(0)
  if key == 27: #ESC
    break
  elif key == ord('a'):
    alpha += 1
  elif key == ord('s'):
    if alpha > 1:
      alpha -= 1
  elif key == ord('q'):
    beta += 1
  elif key == ord('w'):
    if beta > 1:
      beta -= 1
#f = open('plik', 'w')
#lista = ["bla ", "bla ", "yyy "]
#f.writelines(lista)
#f.close()
