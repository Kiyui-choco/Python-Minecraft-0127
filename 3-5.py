from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()

x,y,z = BergOnlyLoveElla.player.getTilePos()
for i in range(0,20):
    BergOnlyLoveElla.setBlock(x,y-1,z+i,46)