#!/usr/bin/env python

from numpy import *
from cv2 import *
import matplotlib.pyplot as plt

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
      matrix[x][y] = 1
  else:
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
      matrix[x][y] = 1

def drawCircle(x0, y0, r, matrix):
  x = r;
  y = 0;
  error = 1 - x;
  while x >= y:
    matrix[x+x0][y+y0] = 1
    matrix[y+x0][x+y0] = 1
    matrix[-x+x0][y+y0] = 1
    matrix[-y+x0][x+y0] = 1
    matrix[-x+x0][-y+y0] = 1
    matrix[-y+x0][-x+y0] = 1
    matrix[x+x0][-y+y0] = 1
    matrix[y+x0][-x+y0] = 1
    y += 1
    if error < 0:
      error += 2 * y + 1
    else:
      x -= 1
      error += 2 * (y - x) + 1


matrix = zeros((14,16), float)
#drawRay(0, 1, 7, 14, matrix)
drawCircle(5, 5, 4, matrix)
print matrix
img = imread('samolot00.jpg', IMREAD_GRAYSCALE)
namedWindow('TEST', WINDOW_NORMAL)
resizeWindow('TEST', 400, 400)
imshow('TEST', img)
waitKey(0)
m,n = img.shape
print m, n
#f = open('plik', 'w')
#lista = ["bla ", "bla ", "yyy "]
#f.writelines(lista)
#f.close()
