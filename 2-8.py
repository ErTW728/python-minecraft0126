# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:22:09 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input("你的名子?")
message = input('要說什麼?')
mc.postToChat('<'+username +">" +message)