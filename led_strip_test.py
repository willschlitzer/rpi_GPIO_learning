import board
import neopixel
from datetime import datetime, date
from time import sleep
pixel_num = 150
pixels = neopixel.NeoPixel(board.D10, pixel_num)
end = datetime(2020, 6, 18, 18, 30, 0, 0)
start = datetime(2020, 1, 11, 11, 43, 0, 0)
total_time = end - start
right_now = datetime.today()
completed_time = right_now - start
per_comp = completed_time/total_time
#print(per_comp)
lit_pix = int(per_comp * pixel_num)
#print(lit_pix)

for i in range(pixel_num):
    pixels[i] = (255, 0, 0)

for i in range(lit_pix):
    pixels[i] = (0, 255, 0)
