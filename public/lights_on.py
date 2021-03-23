import RPi.GPIO as g
import time

p1=40
p2=38
p3=36
t=0.05

g.setmode(g.BOARD)
g.setwarnings(False)

def init():
	g.setup(p1,g.OUT)
	g.setup(p2,g.OUT)
	g.setup(p3,g.OUT)


def on(pin):
	g.output(pin,g.LOW)


def off(pin):
	g.output(pin,g.HIGH) 


def scene_on():
	on(p1)
	on(p2)
	on(p3)


init()
scene_on()
