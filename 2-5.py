# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:44:35 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    block1 = mc.getBlock(x,y-1,z)
    block2 = mc.getBlock(x,y-1,z+1)
    block3 = mc.getBlock(x,y-1,z-1)
    block4 = mc.getBlock(x+1,y-1,z)
    block5 = mc.getBlock(x-1,y-1,z)
    if block1 == 8 or block1 == 9 or block2 == 8 or block2 == 9 or block3 == 8 or block3 ==9 or block4 == 8 or block4 == 9 or block5 ==8 or block5 == 9:
    
        mc.setBlock(x,y-1,z,79)
        mc.setBlock(x,y-1,z+1,79)
        mc.setBlock(x,y-1,z-1,79)
        mc.setBlock(x+1,y-1,z,79)
        mc.setBlock(x-1,y-1,z,79)