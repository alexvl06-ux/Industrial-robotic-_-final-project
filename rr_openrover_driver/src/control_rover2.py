#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry 
import time
from random import randint

class Joystick(object):

    def __init__(self):
        self.axes = 6*[0.,]
        self.buttons = 6*[0.,]    
	rospy.Subscriber("/joy", Joy, self.callback)
	

    def callback(self, msg):
        self.axes = msg.axes
        self.buttons = msg.buttons
	
class Ubicacion(object):

    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.posz = 0

        self.orientationx = 0    
	self.orientationy = 0    
	self.orientationz = 0    
	rospy.Subscriber('/odom', Odometry, self.callback)
	

    def callback(self, msg):
	self.posx=round(msg.pose.pose.position.x,2)
	self.posy=round(msg.pose.pose.position.y,2)
	self.posz=round(msg.pose.pose.position.z,2)
	
	self.orientationx=round(msg.pose.pose.orientation.x,5)
	self.orientationy=round(msg.pose.pose.orientation.y,5)
	self.orientationz=round(msg.pose.pose.orientation.z,5)
	#print(round(msg.pose.pose.orientation.x,3))

velocity_publisher = rospy.Publisher('/cmd_vel/managed',Twist, queue_size=10)   
                                                                                         
vel_msg = Twist()         #Definimos una variable de tipo Twist

#vel_msg.linear.x = 0.5    #Asignamos una velocidad lineal de 0.5 m/s
#vel_msg.angular.z = 0.1   #Asignamos una velocidad angular de 0.1 rad/seg


rospy.init_node("testJoystick")
joystick = Joystick()
ubicacion= Ubicacion()
# Loop rate (in Hz)
aux=0 
tempx=0
tempy=0
tempz=0
modo=0
aux_2=0
ori=1
pos_ori=True
temp_modo=0
rate = rospy.Rate(100)
revision=0
# Continuous execution loop
while not rospy.is_shutdown():
    #scan_sub = rospy.Subscriber('/odom', Odometry, callback)
    # Show the axes and buttons
    #print '\naxis:', joystick.axes
    #print 'buttons:', joystick.buttons
    #print(ubicacion.orientation) 
    #print("X_OR:"+str(ubicacion.orientationx)+" Y_OR:"+str(ubicacion.orientationy))
    #vel_msg.linear.x = -0.2
        

    #Direccion adelante atras    
    if joystick.buttons[2]==1:
	#print("adelante")	
	
	vel_msg.linear.x = -0.6 
    elif joystick.buttons[3]==1:
	#print("atras")
	vel_msg.linear.x = 0.6 
    elif joystick.buttons[1]==1:
	vel_msg.linear.x = 0.0
 	#vel_msg.angular.z = 0.0 
    
 	#vel_msg.angular.z = 0.0 
    else:
	vel_msg.linear.x = -0.4
	#vel_msg.linear.x = 0.0 
	
	#direccion izq derecha
    if joystick.axes[4]==1:
	#print("Izquierda")
	vel_msg.angular.z = 0.5 
    elif joystick.axes[4]==-1:
	#print("Derecha")
	vel_msg.angular.z = -0.5 
    else:
	vel_msg.angular.z = 0.0 

    #manejo automatico
    
    if aux>300 and modo==0:
	print("Revision")
	print("X:"+str(ubicacion.posx)+" Y:"+str(ubicacion.posy))
	
	if(ubicacion.posx==tempx and ubicacion.posy==tempy and ubicacion.posz == tempz):
		
		vel_msg.angular.z=0.5
		vel_msg.linear.x = 0.05
		velocity_publisher.publish(vel_msg)
		delay=randint(4,7)
		print(delay)
		time.sleep(delay)
		vel_msg.linear.z=0.0
		print("Se movio estaba quieto")

	tempx=ubicacion.posx
	tempy=ubicacion.posy
	tempz=ubicacion.posz

	aux=0
    aux+=1

   
    
    # Wait for the next iteration&
    velocity_publisher.publish(vel_msg)
    rate.sleep()
    