from logging.config import listen
from random import choice, choices, random
import turtle as turtle

t = turtle.Turtle()
t.width(15)    # Dit gaat de dikte van u pen wijzigen waarmee u tekent

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'black'] 

def up():
    t.setheading(90)   # Wat dit gaat doen is dat de turtle 90 graden upwards gaat dus noorden
    t.forward(100)      
def down():
    t.setheading(270)  # Dus in dit geval het tegenovergestelde dus 270 graden
    t.forward(100)
def left():
    t.setheading(180)  # 180 graden
    t.forward(100)
def right():
    t.setheading(0)    # 0 graden
    t.forward(100)
def clickleft(x, y):             # Deze functie is als je op je linkermuisknop drukt dat kleuren random veranderen naar de opgegeven kleuren in colors.
    t.color(choices(colors))     # Zoals je hier ziet colors = de opgegeven kleuren in colors en choices = gaat die random choices maken dus in dit gevalen een random kleur kiezen.



turtle.listen()   # listens for overall the entire turtle module's inputs , dus hij gaat luisteren naar de events. events = alles wat je doet met je muis of keyboard.

turtle.onscreenclick(clickleft, 1)   # 1 = linkerknop muis , 2# middenknop en 3# is u rechterknop
turtle.onkey(up, 'Up')   # Onkey enables the binding of a keypress with a function. Zo dit gaat de functie up activeren als we de key 'Up' pressen , in dit geval 0 graden + 100 forward.
turtle.onkey(down, 'Down')  # De 'Up' , 'Down' , 'Left' en 'Right' key representen u pijltjes op u toetsenbord key
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()
