from pyleap import *

b1=Rectangle(157,100,400,120,"orange")
b2=Rectangle(215,217,339,100,"green")
w1=Rectangle(230,220,50,90,"black")
w2=Rectangle(285,220,50,90,"black")
w3=Rectangle(340,220,50,90,"black")
w4=Rectangle(395,220,50,90,"black")
w5=Rectangle(450,220,50,90,"black")
w6=Rectangle(505,220,50,90,"black")
we1=Circle(230,100,40,"black")
we2=Circle(230,100,20,"white")
we3=Circle(480,100,40,"black")
we4=Circle(480,100,20,"white")
door=Rectangle(282,105,55,210,"black")
title=Text("School bus",370,165,20,"red")





def loop(dt):
    Rectangle(0,0,window.w,window.h,"pink").draw()
    b1.draw()
    b2.draw()
    w1.draw()
    w2.draw()
    w3.draw()
    w4.draw()
    w5.draw()
    w6.draw()
    we1.draw()
    we2.draw()
    we3.draw()
    we4.draw()
    door.stroke()
    title.draw()




repeat(loop)
run()