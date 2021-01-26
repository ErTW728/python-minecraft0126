# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:44:00 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z+1,30)
mc.setBlock(x,y,z-1,30)
mc.setBlock(x+1,y,z+1,30)
mc.setBlock(x-1,y,z+1,30)
mc.setBlock(x+1,y,z-1,30)
mc.setBlock(x-1,y,z-1,30)
mc.setBlock(x+1,y,z,30)
mc.setBlock(x-1,y,z+1,30)