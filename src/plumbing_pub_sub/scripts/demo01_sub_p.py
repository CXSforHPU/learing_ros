#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from plumbing_pub_sub.msg import Person

"""
1. 导包
2. 初始化节点
3. 创建订阅者对象
4. 回调函数
5. spin()

"""

def pub_callback(msg):

    rospy.loginfo("订阅的数据：%d %s %.2f",msg.age,msg.name,msg.height)


if __name__ == "__main__":
    rospy.init_node("HaiDai")

    sub = rospy.Subscriber("che",Person,pub_callback,queue_size=1)

    rospy.spin()