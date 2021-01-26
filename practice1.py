# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:40:30 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random,time
while True:
    x,y,z = mc.player.getTilePos()
    color = random.randrange(0,9)
    mc.setBlock(x,y,z-1,38,color)
    time.sleep(0.01)