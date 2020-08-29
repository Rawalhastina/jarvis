import os
import sys
import subprocess
import datetime
import time
import pyglet
from datetime import datetime
from time import sleep
from time import strftime

from time import sleep
image = pyglet.resource.image('bg3.png')


animation = pyglet.image.load_animation('bg.gif')
animSprite = pyglet.sprite.Sprite(animation, x=470, y=250)
 
 
w = 1280
h = 800

 
window = pyglet.window.Window(width=w, height=h)







subprocess.Popen([sys.executable, 'jarvisWork.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

@window.event
def on_draw():
    window.clear()

    image.blit(0,0)
    animSprite.draw()
    
    
 

pyglet.app.run()