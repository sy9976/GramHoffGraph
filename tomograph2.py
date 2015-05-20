#!/usr/bin/env python
import math as math
import Image
import numpy as np
from cv2 import *

def drawRay(x1, y1, x2, y2, matrix, sinValue, imgSize): # x1,y1 - detektor
  beginX, endX, beginY, endY = imgSize
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
  if dx >= dy:
    e = dx/2
    for i in range(dx):
      x1 = x1 + kx
      e = e - dy
      if e < 0:
        y1 = y1 + ky
        e = e + dx
      if ((x1>=beginX) and (x1<endX) and (y1>=beginY) and (y1<endY)):
        matrix[x1][y1] += sinValue
  else:
    e = dy/2
    for i in range(dy):
      y1 = y1 + ky
      e = e - dx
      if e < 0:
        x1 = x1 + kx
        e = e + dy
      if ((x1>=beginX) and (x1<endX) and (y1>=beginY) and (y1<endY)):
        matrix[x1][y1] += sinValue
  #matrix[x1][y1] -= sinValue
  return result

def drawRayRGB(x1, y1, x2, y2, matrix):
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
  if dx >= dy:
    e = dx/2
    for i in range(dx):
      x1 = x1 + kx
      e = e - dy
      if e < 0:
        y1 = y1 + ky
        e = e + dx
      result += (matrix[x1][y1][0] + matrix[x1][y1][1] + matrix[x1][y1][2])/3
  else:
    e = dy/2
    for i in range(dy):
      y1 = y1 + ky
      e = e - dx
      if e < 0:
        x1 = x1 + kx
        e = e + dy
      result += (matrix[x1][y1][0] + matrix[x1][y1][1] + matrix[x1][y1][2])/3
  result -= matrix[x1][y1][0] + matrix[x1][y1][1] + matrix[x1][y1][2]
  result = result
  return result

def drawRayGray(x1, y1, x2, y2, matrix):
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
  dy = abs(y2 - y1)#brak sumowania pierwszego piksela -emiter
  if dx >= dy:
    e = dx/2
    for i in range(dx):
      x1 = x1 + kx
      e = e - dy
      if e < 0:
        y1 = y1 + ky
        e = e + dx
      result += matrix[x1][y1]
  else:
    e = dy/2
    for i in range(dy):
      y1 = y1 + ky
      e = e - dx
      if e < 0:
        x1 = x1 + kx
        e = e + dy
      result += matrix[x1][y1]
  result -= matrix[x1][y1]#ostatni - detektor
  return result

def repaintCircle(matrix, circle):
  for i in range (len(circle)):
    if (len(matrix.shape) == 3):
      matrix[circle[i][0]][circle[i][1]] = [250, 0, 0]
    else:
      matrix[circle[i][0]][circle[i][1]] = 250

def drawCircle(x0, y0, r, matrix):
  step = math.atan(1.0/r)
  alpha = 0
  circle = []
  while alpha <= 2*np.pi:
    x = x0 + int(np.cos(alpha)*r)
    y = y0 + int(np.sin(alpha)*r)
    if (len(matrix.shape) == 3):
      matrix[x][y] = [250, 0, 0]
    else:
      matrix[x][y] = 250
    alpha += step
    if circle:
      if circle[len(circle)-1] != (x, y):
        circle.append((x,y))
    else:
      circle.append((x,y))
  return circle

def drawArc(x0, y0, r, matrix, circle, middlePoints, alpha, beta):
  alpha = alpha%360
  beta = beta%360
  xAlpha = x0 + int(np.cos(np.radians(alpha))*r)
  yAlpha = y0 + int(np.sin(np.radians(alpha))*r)
  xBeta = x0 + int(np.cos(np.radians(beta))*r)
  yBeta = y0 + int(np.sin(np.radians(beta))*r)
  a = matrix.shape
  if (len(a) == 3):
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
  else:
    
    err = 0
    if (matrix[xAlpha][yAlpha] == 250):
      err = 0
    elif (matrix[xAlpha-1][yAlpha] == 250):
      xAlpha -= 1
    elif (matrix[xAlpha+1][yAlpha] == 250):
      xAlpha += 1
    elif (matrix[xAlpha-1][yAlpha-1] == 250):
      xAlpha -= 1
      yAlpha -= 1
    elif (matrix[xAlpha-1][yAlpha+1] == 250):
      xAlpha -= 1
      yAlpha += 1
    elif (matrix[xAlpha][yAlpha-1] == 250):
      yAlpha -= 1
    elif (matrix[xAlpha][yAlpha+1] == 250):
      yAlpha += 1
    elif (matrix[xAlpha+1][yAlpha-1] == 250):
      xAlpha += 1
      yAlpha -= 1
    elif (matrix[xAlpha+1][yAlpha+1] == 250):
      xAlpha += 1
      yAlpha += 1
    else:
      err = 1
  
    if (matrix[xBeta][yBeta] == 250):
      err = 0
    elif (matrix[xBeta-1][yBeta] == 250):
      xBeta -= 1
    elif (matrix[xBeta+1][yBeta] == 250):
      xBeta += 1
    elif (matrix[xBeta-1][yBeta-1] == 250):
      xBeta -= 1
      yBeta -= 1
    elif (matrix[xBeta-1][yBeta+1] == 250):
      xBeta -= 1
      yBeta += 1
    elif (matrix[xBeta][yBeta-1] == 250):
      yBeta -= 1
    elif (matrix[xBeta][yBeta+1] == 250):
      yBeta += 1
    elif (matrix[xBeta+1][yBeta-1] == 250):
      xBeta += 1
      yBeta -= 1
    elif (matrix[xBeta+1][yBeta+1] == 250):
      xBeta += 1
      yBeta += 1
    else:
      err = 1
    if not err:
      matrix[xAlpha][yAlpha] = 120
      matrix[xBeta][yBeta] = 120
  result = []
  if beta > alpha:
    for i in range (len(circle)):
      if circle[i] == (xAlpha, yAlpha):
        for j in range(i, len(circle)):
          if circle[j] == (xBeta, yBeta):
            break
          if (len(a) == 3):
            matrix[circle[j][0]][circle[j][1]] = [0, 0, 250]
            if ((circle[j][0], circle[j][1]) in middlePoints):
              result.append((circle[j][0], circle[j][1]))
          else: 
            matrix[circle[j][0]][circle[j][1]] = 120
            if ((circle[j][0], circle[j][1]) in middlePoints):
              result.append((circle[j][0], circle[j][1]))
  else:
    for i in range (len(circle)):
      if circle[i] == (xAlpha, yAlpha):
        for j in range (i, len(circle)):
          if (len(a) == 3):
            matrix[circle[j][0]][circle[j][1]] = [0, 0, 250]
            if ((circle[j][0], circle[j][1]) in middlePoints):
              result.append((circle[j][0], circle[j][1]))
          else:
            matrix[circle[j][0]][circle[j][1]] = 120
            if ((circle[j][0], circle[j][1]) in middlePoints):
              result.append((circle[j][0], circle[j][1]))
    for i in range (len(circle)):
      if circle[i] == (xBeta, yBeta):
        break
      if (len(a) == 3):
        matrix[circle[i][0]][circle[i][1]] = [0, 0, 250]
        if ((circle[i][0], circle[i][1]) in middlePoints):
          result.append((circle[i][0], circle[i][1]))
      else: 
        matrix[circle[i][0]][circle[i][1]] = 120
        if ((circle[i][0], circle[i][1]) in middlePoints):
          result.append((circle[i][0], circle[i][1]))
    
  return result

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
  a = matrix.shape
  imageSize = (0, 0, 0, 0)
  if (len(a) == 3):
    oldX, oldY, oldZ = matrix.shape
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
    tmpmat = np.zeros((20+emiterDistance-x/2, y, 3), np.uint8)
    matrix = np.concatenate((tmpmat, matrix))
    matrix = np.concatenate((matrix, tmpmat))
    x, y, z = matrix.shape
    tmpmat = np.zeros((x, 20+emiterDistance-y/2, 3), np.uint8)
    matrix = np.hstack((tmpmat, matrix))
    matrix = np.hstack((matrix, tmpmat))
    x, y, z = matrix.shape
    imageSize = ((x/2)-(oldX/2), (x/2)+(oldX/2), (y/2)-(oldY/2), (y/2)+(oldY/2))
    #print 'x, y: ', x, y, 'emiterDistance: ', emiterDistance
  elif (len(a) == 2): 
    x, y = matrix.shape
    oldX, oldY = matrix.shape
    if x > y:
      tmpmat = np.zeros((x, (x-y)/2), np.uint8)
      matrix = np.hstack((tmpmat, matrix))
      matrix = np.hstack((matrix, tmpmat))
    elif y > x:
      tmpmat = np.zeros(((y-x)/2, y), np.uint8)
      matrix = np.concatenate((tmpmat, matrix))
      matrix = np.concatenate((matrix, tmpmat))
    x, y = matrix.shape
    tmpmat = np.zeros((20+emiterDistance-x/2, y), np.uint8)
    matrix = np.concatenate((tmpmat, matrix))
    matrix = np.concatenate((matrix, tmpmat))
    x, y = matrix.shape
    tmpmat = np.zeros((x, 20+emiterDistance-y/2), np.uint8)
    matrix = np.hstack((tmpmat, matrix))
    matrix = np.hstack((matrix, tmpmat))
    x, y = matrix.shape
    imageSize = ((x/2)-(oldX/2), (x/2)+(oldX/2), (y/2)-(oldY/2), (y/2)+(oldY/2))
    #print 'x, y: ', x, y, 'emiterDistance: ', emiterDistance
  return (imageSize, matrix)

def middleDetectors(detectors):
  result = []
  for i in range(len(detectors)):
    result.append(detectors[i][len(detectors[i])//2])
  return result

def acquisition(matrix, circle, alpha, beta, mDetectors, emiterDistance, maxPixels, width):
  angle = 0
  a = matrix.shape
  begin = alpha + 180 - beta
  end = alpha + 180 + beta
  result = []
  width = 99999999
  if (len(a) == 3):
    x, y, z = matrix.shape
    while angle <= 360:
      tmp = []
      emiterPositionX = x/2 + int(np.cos(np.radians(angle))*emiterDistance)
      emiterPositionY = y/2 + int(np.sin(np.radians(angle))*emiterDistance)
      repaintCircle(matrix, circle)
      tmpList = drawArc(x/2, y/2, emiterDistance, matrix, circle, mDetectors, begin+angle, end+angle)
      for i in range(len(tmpList)):
        middleX, middleY = tmpList[i]
        absorption = drawRayRGB(int(emiterPositionX), int(emiterPositionY), int(middleX), int(middleY), matrix)
        normalAbsorption = int(255.0*(absorption/(255.0*maxPixels)))
        tmp.append(normalAbsorption)
      angle += alpha
      result.append(tmp)
      if (len(tmpList) < width):
        width = len(tmpList)
  elif (len(a) == 2):
    x, y = matrix.shape
    while (angle <= 360):
      tmp = []
      emiterPositionX = x/2 + round(np.cos(np.radians(angle))*emiterDistance)
      emiterPositionY = y/2 + round(np.sin(np.radians(angle))*emiterDistance)
      repaintCircle(matrix, circle)
      tmpList = drawArc(x/2, y/2, emiterDistance, matrix, circle, mDetectors, begin+angle, end+angle)
      for i in range(len(tmpList)):
        middleX, middleY = tmpList[i]
        absorption = drawRayGray(int(emiterPositionX), int(emiterPositionY), int(middleX), int(middleY), matrix)
        normalAbsorption = int(255.0*(absorption/(255.0*maxPixels)))
        tmp.append(normalAbsorption)
      angle += alpha
      result.append(tmp)
      if (len(tmpList) < width):
        width = len(tmpList)
  for i in range(len(result)):
    while (len(result[i])>width):
      a = result[i].pop()
  return result

def reconstruction(matrix, circle, alpha, beta, mDetectors, emiterDistance, maxPixels, width, sinogram, imgSize):
  x, y = matrix.shape
  recImage = np.zeros((x, y), dtype=np.uint32)
  angle = 0
  a = matrix.shape
  begin = alpha + 180 - beta
  end = alpha + 180 + beta
  result = []
  for i in range(len(sinogram)):
    emiterPositionX = x/2 + int(np.cos(np.radians(angle))*emiterDistance)
    emiterPositionY = y/2 + int(np.sin(np.radians(angle))*emiterDistance)
    repaintCircle(matrix, circle)
    tmpList = drawArc(x/2, y/2, emiterDistance, matrix, circle, mDetectors, begin+angle, end+angle)
    for j in range(len(sinogram[i])):
      middleX, middleY = tmpList[j]
      drawRay(middleX, middleY, emiterPositionX, emiterPositionY, recImage, sinogram[i][j], imgSize)
    angle += alpha
  recMax = recImage.max()
  for i in range(len(recImage)):
    for j in range(len(recImage[0])):
      recImage[i][j] = (255.0*recImage[i][j])/recMax
  return recImage

img = imread('data/triangle.jpeg', 0)
x, y  = img.shape
if x > y:
  maxPixels = x
else:
  maxPixels = y
emiterDistance = 20
detectorWidth = 3
alpha = 1
beta = 60


emiterDistance = calculateEmiterDistance(x, y, emiterDistance)
imgSize, img = drawEdge(img, emiterDistance)
x, y = img.shape
circle = drawCircle(x/2, y/2, emiterDistance, img)
circletmp = circle[:]
detectors = createDetectors(detectorWidth, circletmp)
middlePoints = middleDetectors(detectors)
a = acquisition(img, circle, alpha, beta, middlePoints, emiterDistance, maxPixels, detectorWidth)
img4 = reconstruction(img, circle, alpha, beta, middlePoints, emiterDistance, maxPixels, detectorWidth, a, imgSize)
img3 = np.asmatrix(np.array(a, dtype=np.uint8))
namedWindow('Original image', WINDOW_NORMAL)
resizeWindow('Original image', 400, 400)
namedWindow('Sinogram', WINDOW_NORMAL)
resizeWindow('Sinogram', 400, 400)
namedWindow('Reconstruction', WINDOW_NORMAL)
resizeWindow('Reconstruction', 400, 400)
while(1):
  imshow('Original image', img)
  imshow('Sinogram', img3)
  imshow('Reconstruction', img4.astype(np.uint8))
  key = waitKey(0)
  if key == 27: #ESC
    break
  #elif key == ord('a'):
  #  alpha += 1
  #elif key == ord('s'):
  #  if alpha > 1:
  #    alpha -= 1
  #elif key == ord('q'):
  #  beta += 1
  #elif key == ord('w'):
  #  if beta > 1:
  #    beta -= 1
