from mcpi.minecraft import Minecraft
BergOnlyLoveElla = Minecraft.create()

while True:
    hits = BergOnlyLoveElla.events.pollProjectileHits()
    if len(hits) > 0 :
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        BergOnlyLoveElla.createExplosion(x,y,z,power=100)