# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:51:33 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
try: 
    answer = int(input('請問你右邊要放甚麼方塊:'))
    mc.setBlock(x+1,y,z,answer)
except:
    print ('你打錯了')