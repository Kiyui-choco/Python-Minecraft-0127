def plantTree(x,y,z):
    BergOnlyLoveElla.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    BergOnlyLoveElla.setBlocks(x,y,z,x,y+4,z,17)

from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()
x,y,z = BergOnlyLoveElla.player.getTilePos()
for i in range(1000):
    for j in range(8):
        for k in range(1000):
            plantTree(x+i*5,y+j*8,z+k*5)
