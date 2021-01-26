# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:19:44 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
long = 10
big =8
high = 7
mc.setBlocks(x,y,z,x+long,y+high,z+big,95)
mc.setBlocks(x+1,y+1,z+1,x+long-1,y+high-1,z+big-1,0)