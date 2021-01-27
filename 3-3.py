from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()
import random
while True:
    x,y,z = BergOnlyLoveElla.player.getPos()
    a = random.uniform(-20,20)
    b = random.uniform(-20,20)
    y = y+30
    BergOnlyLoveElla.spawnEntity(x+a,y,z+b,20)
    