from pyleap import *
Snowman = Sprite("https://cdn.leaplearner.education/ud/dev//78601/162952612518413.png",300,300)
Snowman.Scale=0.01
bg = Sprite("https://cdn.leaplearner.education/ud/dev//78601/162952637986619.jpg",300,250)
bg.Scale=0.01


def draw(dt):
    bg.draw()
    Snowman.draw()

       
    





repeat(draw)
run()