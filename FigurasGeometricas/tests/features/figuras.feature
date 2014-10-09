Feature: Compute figure
	 to play with Lettuce 

Scenario: Figure of 0
	Given I have the square 5
	When I compute its figure 
	Then I see the number 25



Scenario: Figure of 1
	Given I have the circle 1
	When I compute its figure 
	Then I see the number 3

Scenario: Figure of 1
	Given I have the diamond 5 2
	When I compute its figure 
	Then I see the number 5

Scenario: Figure of 1
	Given I have the rectangle 5 2
	When I compute its figure 
	Then I see the number 10


Scenario: Figure of 1
	Given I have the triangle 5 2
	When I compute its figure 
	Then I see the number 5
