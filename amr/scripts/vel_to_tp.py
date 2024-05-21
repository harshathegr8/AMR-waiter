#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from time import sleep

pub = rospy.Publisher("Time_period", String, queue_size=0)
lin, ang = 0, 0

def callback(data):
    lin = data.linear.x
    ang = data.angular.z
    if ang == 0 and lin != 0:  # Straight movement
        t = 0.22 / (abs(lin) * 200) * 1000
        if lin < 0:  # forward
            yoff, xoff = -t, t
        elif lin > 0:  # reverse
            xoff, yoff = -t, t
    elif ang != 0 and lin != 0:  # Angular linear combined
        t = 0.22 / (abs(lin) * 200) * 1000
        t2 = 0.22 / ((abs(lin) + 0.28 * abs(ang)) * 200) * 1000
        if ang < 0:  # rightwards
            if lin > 0:  # forward right
                xoff = t - 1
                yoff = -(t2 - 1)
            elif lin < 0:  # backward right
                xoff = -(t - 1)
                yoff = t2 - 1
        elif ang > 0:  # leftwards
            if lin > 0:  # forward left
                yoff = -(t - 1)
                xoff = t2 - 1
            elif lin < 0:  # backward left
                yoff = t - 1
                xoff = -(t2 - 1)
    elif ang != 0 and lin == 0:  # Only angular
        t = 0.22 / (0.28 * abs(ang) * 200) * 1000
        if ang < 0:  # rightwards
            xoff, yoff = -t/2,-t/2
        if ang > 0:  # leftwards
            xoff, yoff = t/2, t/2
    else:
        xoff, yoff = 0, 0
    a = String()
    a.data = str(xoff) + "," + str(yoff)
    pub.publish(a)

rospy.init_node('tp_gen')
rospy.Subscriber("cmd_vel", Twist, callback)
rospy.spin()
