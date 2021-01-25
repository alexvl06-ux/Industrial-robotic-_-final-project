#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
#from functool import partial
def callback(data):
	global pub
	print data.axes
	msg = Twist()
	msg.linear.x = data.axes[1]
	msg.angular.z = data.axes[0]
	pub.publish(msg)
def function():
	global pub
	rospy.init_node('Joy', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rospy.Subscriber('joy', Joy, callback)
	rospy.spin()
if __name__ =="__main__":
	try:
		function()
	except rospy.ROSInterruptException:
		pass
