# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append("../")
from Figuras import Figuras

@step(u'Given I have the square (\d+)')
def given_i_have_the_number_5(step,number):
    world.number = int(number)
    world.escenario = 0
@step(u'Given I have the circle (\d+)')
def given_i_have_the_number_6(step,number):
    world.number = int(number)
    world.escenario = 1

@step(u'Given I have the diamond (\d+) (\d+)')
def given_i_have_the_number_7(step,number,base):
    world.number = int(number)
    world.escenario = 2
    world.base = int(base)	

@step(u'Given I have the triangle (\d+) (\d+)')
def given_i_have_the_number_7(step,number,base):
    world.number = int(number)
    world.escenario = 3
    world.base = int(base)	

@step(u'Given I have the rectangle (\d+) (\d+)')
def given_i_have_the_number_7(step,number,base):
    world.number = int(number)
    world.escenario = 4
    world.base = int(base)	



@step(u'When I compute its figure')
def when_i_compute_its_figure(step):
    f=Figuras()
   
    if(world.escenario==0):
		world.number = f.cuadrado(world.number)
    elif(world.escenario==1):
		world.number = f.circulo(world.number)
    elif(world.escenario==2):
		world.number = f.rombo(world.number,world.base)
    elif(world.escenario==3):
		world.number = f.triangulo(world.number,world.base)
    else:	
        	world.number = f.rectangulo(world.number,world.base)
@step(u'Then I see the number (\d+)')
def then_i_see_the_number_25(step,x):
    if(world.escenario==0):
    	assert world.number == int(x)
    else:	
	assert world.number == int(x)
	
