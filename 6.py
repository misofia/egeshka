# из досрока
# по дефолту хвост опущен

from turtle import *
left(90) # надо повернуть на ось У
k = 20
speed(30)

for i in range(2):
    forward(13 * k)
    right(90)
    forward(18 * k)
    right(90)
up()
forward(5 * k)
right(90)
forward(9 * k)
left(90)
down()
for i in range(2):
    forward(11 * k)
    right(90)
    forward(7 * k)
    right(90)
up()

for x in range(-1 * k, 20 * k, k):
    for y in range(-5 * k, 20 * k, k):
        goto(x, y)
        dot(3, 'red')
done()