from pyleap import *
window.set_size(420,600)
window.set_caption("sunset")
water=Rectangle(0,0,420,200,"blue")
sky=Rectangle(0,200,420,400,"#00008B")
cloud=Sprite("https://cdn.leaplearner.education/i/ef60ae.png",200,550)
cloud.scale=0.5
sun=Circle(50,550,40,"yellow")




def draw(dt):
    
    sky.draw()
    cloud.draw()
    sun.draw()
    water.draw()
    sun.y=sun.y-1




repeat(draw)
run()