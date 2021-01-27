from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()

x,y,z = BergOnlyLoveElla.player.getTilePos()
for i in range(0,10000):
    BergOnlyLoveElla.setBlock(x+i,y-1,z+i,46)
    BergOnlyLoveElla.setBlock(x+1+i,y-1,z+i,46)
    BergOnlyLoveElla.setBlock(x+2+i,y-1,z+i,46)
    BergOnlyLoveElla.setBlock(x+3+i,y-1,z+i,46)
    BergOnlyLoveElla.setBlock(x+4+i,y-1,z+i,46)