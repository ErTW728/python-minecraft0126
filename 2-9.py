# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:38:12 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z-1,63,0,"我愛Minecraft","也愛Python")