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


def scene1():
	on(p1)
	off(p2)
	off(p3)


def scene2():
	off(p1)
	on(p2)
	off(p3)


def scene3():
	off(p1)
	off(p2)
	on(p3)


def play():
	scene1()
	time.sleep(t)
	scene2()
	time.sleep(t)
	scene3()
	time.sleep(t)


init()

for i in range(60):
	play()

off(p3)
