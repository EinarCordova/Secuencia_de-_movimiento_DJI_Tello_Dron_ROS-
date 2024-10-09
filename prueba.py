#!/usr/bin/env python3
import rospy
from djitellopy import Tello

if __name__ == '__main__':
    rospy.init_node("test_node")
    rospy.loginfo("Test node has been started.")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        tello = Tello()

        tello.connect()
        print (tello.get_battery)
        rospy.sleep(1)

        tello.takeoff()
        tello.rotate_counter_clockwise(360)
        tello.land()

        rospy.is_shutdown
        
        
        