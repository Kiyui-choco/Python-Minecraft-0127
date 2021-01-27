from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()

x,y,z = BergOnlyLoveElla.player.getPos()

number = 1

for i in range(8):
    for j in range(number):
        BergOnlyLoveElla.spawnEntity(x,y,z,60)
        
    number = number*2
    
    BergOnlyLoveElla.postToChat('這次生成了'+str(number)+'隻蠹魚')