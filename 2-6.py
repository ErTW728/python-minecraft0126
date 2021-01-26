# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:47:24 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos(1)
answer = int(input('請問你右邊要放甚麼方塊:'))
mc.setBlock(x+1,y,z,answer)