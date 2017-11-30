# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:16:22 2017

@author: GANGZ
"""

from PIL import Image,ImageDraw,ImageFont


def draw_text(img, font, pos,fg_color, text):
    
    drawBrush = ImageDraw.Draw(img)
    drawBrush.text(pos, text, fg_color, font)
    
if __name__ == '__main__':
    img = Image.open('qq_header.png')
    width,height = img.size
    font = ImageFont.truetype("arial.ttf", 17)
    pos = (width-20, 20)
    fg_color=(255,0,0)
    text = '2'
    draw_text(img, font, pos, fg_color,text)
    img.save('qq_header2.png','png')
    img.show()
        
