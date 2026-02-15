#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from learning_topic.msg import Person

def person_Info_Callback(person_msg):
    rospy.loginfo("I receive person info: %s, %d, %d", person_msg.name, person_msg.sex, person_msg.age)


def person_subscriber():
    # ROS节点初始化
    rospy.init_node('person_subscriber', anonymous=True)

    # 创建一个Subscriber，订阅名为/person_info的Topic，注册回调函数person_Info_Callback
    rospy.Subscriber("person_info", Person, person_Info_Callback)

    # 循环等待回调函数
    rospy.spin()


if __name__ == '__main__':
    try:
        person_subscriber()
    except rospy.ROSInterruptException:
        pass