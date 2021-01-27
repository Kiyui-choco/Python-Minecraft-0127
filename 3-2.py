from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()

while True:
    hits = BergOnlyLoveElla.events.pollBlockHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        block = BergOnlyLoveElla.getBlock(x,y,z)
        print(type(block))
        BergOnlyLoveElla.postToChat('你打到了'+str(block)) 
        if block == 1:
            BergOnlyLoveElla.setBlock(x,y,z,46)