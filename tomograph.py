#!/usr/bin/env python
from PIL import Image
from numpy import *
from cv2 import *
import matplotlib.pyplot as plt
#import msvcrt 

def drawRay(x1, y1, x2, y2, matrix):
  x = x1;
  y = y1;
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
  matrix[x][y] = 1
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
      matrix[x][y] = [0, 250, 0]
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
      matrix[x][y] = [0, 250, 0]

def drawCircle(x0, y0, r, matrix):
  circle = [[] for i in range(8)]
  print circle
  #for i in range(8):
  #  tmp = a[]
  #  circle.append(tmp)
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
  print result
  for i in range(8):
    result += circle[i]
  return result

def drawCircle2(x0, y0, r, matrix):
  for i in range(360):
    x = x0 + cos(radians(i))*r
    y = y0 + sin(radians(i))*r
    matrix[x][y] = 255

def drawArc(x0, y0, r, matrix, circle, alpha, beta):
  xAlpha = x0 + sin(radians(alpha))*r
  yAlpha = y0 + cos(radians(alpha))*r
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

  xBeta = x0 + sin(radians(alpha))*r
  yBeta = y0 + cos(radians(alpha))*r
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
  #for i in range(beta-alpha):
    #x = x0 + sin(radians(alpha+i))*r
    #y = y0 + cos(radians(alpha+i))*r
    #print 'x,y ', x, y
    #matrix[x][y] = [0, 0, 250]

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

matrix = zeros((200,200, 3), uint8)
#matrix = Image.new("L", (200,200))
#drawRay(0, 1, 7, 14, matrix)
circle = drawCircle(100, 100, 75, matrix)
detectors = createDetectors(10, circle)
#print detectors
#matrixRGB = cvtColor(matrix, COLOR_GRAY2RGB)
#drawArc(100, 100, 75, matrix, 0, 45)
#img = imread('data/image.jpg', IMREAD_GRAYSCALE)
#print split(img).shape
namedWindow('TEST', WINDOW_NORMAL)
resizeWindow('TEST', 400, 400)
alpha = 0;
#plt.imshow(matrix, cmap='gray')
while(1):
  #plt.imshow(matrix)
  #plt.show()
  begin = 20 + alpha
  end = 45 + alpha
  print begin, end
  drawArc(100, 100, 75, matrix, circle, begin, end)
  print alpha
  imshow('TEST', matrix)
#imshow('TEST', matrix)
#print sin (pi/4)
#c = msvcrt.getch()
#print 'wcisnales', c 
  key = waitKey(0)
  if key == 27: #ESC
    break
  if key == ord('a'):
    alpha += 1
#f = open('plik', 'w')
#lista = ["bla ", "bla ", "yyy "]
#f.writelines(lista)
#f.close()
