# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:52:17 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z-1,407)
    time.sleep(0.1)