# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z+2,30)
mc.setBlock(x,y,z-2,30)
mc.setBlock(x-1,y,z+1,30)
mc.setBlock(x+1,y,z+1,30)
mc.setBlock(x+1,y,z-1,30)
mc.setBlock(x-1,y,z-1,30)
mc.setBlock(x+2,y,z,30)
mc.setBlock(x-2,y,z,30)