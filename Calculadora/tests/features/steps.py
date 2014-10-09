# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append("../")
from Calculator import Calculator


@step(u'Given I have the addition (\d+) (\d+)')
def given_i_have_the_number_7(step,number,numero2):
    world.number = int(number)
    world.escenario = 0
    world.numero2 = int(numero2)	

@step(u'Given I have the subtraction (\d+) (\d+)')
def given_i_have_the_number_8(step,number,numero2):
    world.number = int(number)
    world.escenario = 1
    world.numero2 = int(numero2)	

@step(u'Given I have the multiplication (\d+) (\d+)')
def given_i_have_the_number_9(step,number,numero2):
    world.number = int(number)
    world.escenario = 2
    world.numero2 = int(numero2)	

@step(u'Given I have the division (\d+) (\d+)')
def given_i_have_the_number_6(step,number,numero2):
    world.number = int(number)
    world.escenario = 3
    world.numero2 = int(numero2)	


@step(u'When I compute its operation')
def when_i_compute_its_operation(step):
    c=Calculator()
   
    if(world.escenario==0):
		world.number = c.suma(world.number,world.numero2)
    elif(world.escenario==1):
		world.number = c.resta(world.number,world.numero2)
    elif(world.escenario==2):
		world.number = c.multi(world.number,world.numero2)
    else:
		world.number = c.division(world.number,world.numero2)
   
@step(u'Then I see the number (\d+)')
def then_i_see_the_number(step,x):
    
    	assert world.number == int(x)
    
	
