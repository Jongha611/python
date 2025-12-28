import time
from turtle import Turtle

john = Turtle()

john.shape("turtle")
john.color("yellow", "blue")

while True:
    john.forward(5)
    john.left(5)
    time.sleep(2)