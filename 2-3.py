# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:18:53 2021

@author: user
"""
import random,time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    color = random.randrange(0,16)
    mc.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,95,color)
    time.sleep(0.01)
    
    
    
    
    
    
    