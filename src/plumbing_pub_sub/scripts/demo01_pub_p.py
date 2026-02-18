#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system('source ../../../devel/setup.bash')


import rospy
from std_msgs.msg import String
from plumbing_pub_sub.msg import Person
import random

"""
1 导包
2 初始化节点
3 创建发布者对象
4 创建消息对象
5 发布消息

"""

if __name__ == "__main__":
    # 初始化节点
    rospy.init_node("sanDai")
    # 创建发布者对象
    pub = rospy.Publisher("che",Person,queue_size=10)
    # 创建消息对象
    msg = Person()

    rate = rospy.Rate(1)
    #设置计数器
    count = 0
    while not rospy.is_shutdown():
        count += 1
        msg.name = "小张" + str(count)
        msg.age = random.randint(10,30)
        msg.height = random.uniform(1.5,2.0)
        # 发布消息
        pub.publish(msg)
        rospy.loginfo("发布的消息为：%s,%d,%.2f",msg.name,msg.age,msg.height)
        rate.sleep()
