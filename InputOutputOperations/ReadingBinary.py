'''Demo Strating raeding binary data'''

from struct import unpack

avi = open('large.avi', mode='br')
avi.seek(64)
binary = avi.read(8)
width_height = unpack('<hhhh', binary) # unpack 4 little-endian short integers
width = width_height[0]
heigth = width_height[2]
print('The video has a pixel width of %i and height of %i.' % (width, height))