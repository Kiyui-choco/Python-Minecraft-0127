def plantTree(x,y,z):
    BergOnlyLoveElla.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    BergOnlyLoveElla.setBlocks(x,y,z,x,y+4,z,17)

from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()
x,y,z = BergOnlyLoveElla.player.getTilePos()
for i in range(0,10000,5):
    plantTree(x+i,y,z)
