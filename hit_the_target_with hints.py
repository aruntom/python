#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:49:30 2017

@author: aruntom
"""

#Arun Tom

import turtle
import math

SCREEN_WIDTH=600
SCREEN_HEIGHT= 600
TARGET_LLEFT_X=100
TARGET_LLEFT_Y=250
TARGET_WIDTH=25
FORCE_FACTOR=30
PROJECTILE_SPEED=1
NORTH=90
SOUTH=270
EAST=0
WEST=180

turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)



turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

angle=float(input("Enter the projectile's angle: "))
force=float(input("Enter the launch force (1-10): "))

distance=force * FORCE_FACTOR

turtle.setheading(angle)

turtle.pendown()
turtle.forward(distance)



if (turtle.xcor()>= TARGET_LLEFT_X and turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH)) and (turtle.ycor()>= TARGET_LLEFT_Y and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("Target hit")
   
   
    
else:
    print("You missed the target.")
   
    x4angle=math.degrees(math.atan((TARGET_LLEFT_Y+TARGET_WIDTH)/(TARGET_LLEFT_X)))
    x2angle=math.degrees(math.atan((TARGET_LLEFT_Y)/(TARGET_LLEFT_X+TARGET_WIDTH)))
    x1angle=math.degrees(math.atan((TARGET_LLEFT_Y)/(TARGET_LLEFT_X)))
    tur_dist = math.sqrt( (turtle.xcor() - 0)**2 + (turtle.ycor() - 0)**2 )
    x3_dist=math.sqrt((TARGET_LLEFT_X+TARGET_WIDTH)**2+(TARGET_LLEFT_Y+TARGET_WIDTH)**2)
    x1_dist=math.sqrt((TARGET_LLEFT_X)**2+(TARGET_LLEFT_Y)**2)
    tur_angle=turtle.heading()
    x4_dist=math.sqrt((TARGET_LLEFT_X)**2+(TARGET_LLEFT_Y+TARGET_WIDTH)**2)
    x2_dist=math.sqrt((TARGET_LLEFT_X+TARGET_WIDTH)**2+(TARGET_LLEFT_Y)**2)
    
# =============================================================================
#     print("\n\n",'*'*50,"\nSummary:")
#     print("farrest dist to hit: ",x3_dist)
#     print("closeset dist to hit: ",x1_dist)
#     print("turtle dist: ",tur_dist)
#     print('\n')
#     print("largest angle to hit: ",x4angle)
#     print("Smallest angle to hit: ",x2angle)
#     print("turtle angle: ",tur_angle)
#     print("\n",'*'*50)
#     
# =============================================================================
    in_for1=0
    de_for1=0
    
    in_ang1=0
    de_ang1=0
    
    
    
    
    if tur_dist<x1_dist:
        in_for1=1
    elif tur_dist>x3_dist:
        de_for1=1
    if tur_angle<x2angle:
        in_ang1=1
    elif tur_angle>x4angle:
        de_ang1=1
    
    if tur_angle<x2angle:
        in_ang1=1
    elif tur_angle>x4angle:
        de_ang1=1
        
    if tur_angle<=x4angle and tur_angle>= x2angle and tur_dist>x4_dist:
        de_for1=1
        
    elif tur_angle<=x4angle and tur_angle>= x2angle and tur_dist<x1_dist:
        in_for1=1
        
    elif tur_angle<=x1angle and tur_angle>= x2angle and tur_dist<x4_dist:
        in_for1=1
        
    print("Hint: ",end=" ")   
    if in_for1 :
        print("Increase launch force")
    if de_for1 :
        print("Decrease launch force")
    if in_ang1 :
        print("Try larger Angle")
    if de_ang1 :
        print("Try lower Angle")




# =============================================================================
#     if turtle.xcor()<TARGET_LLEFT_X and turtle.ycor()>TARGET_LLEFT_Y+TARGET_WIDTH:
#         print("Try lower angle")
#     if turtle.xcor()>TARGET_LLEFT_X+TARGET_WIDTH and turtle.ycor()<TARGET_LLEFT_Y:
#         print("Try Higher angle")
#         
#         
#         
#     if ((turtle.xcor()<TARGET_LLEFT_X) and (turtle.ycor()<TARGET_LLEFT_Y)):
#         print("Raise launch force")
#     if ((turtle.xcor()>TARGET_LLEFT_X + TARGET_WIDTH) and (turtle.ycor()>TARGET_LLEFT_Y + TARGET_WIDTH)):
#         print("Lower launch force")
# 
# =============================================================================

