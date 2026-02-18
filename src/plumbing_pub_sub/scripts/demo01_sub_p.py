#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

"""
1. 导包
2. 初始化节点
3. 创建订阅者对象
4. 回调函数
5. spin()

"""

def pub_callback(msg):

    rospy.loginfo("订阅的消息为：%s",msg.data)


if __name__ == "__main__":
    rospy.init_node("HaiDai")

    sub = rospy.Subscriber("che",String,pub_callback,queue_size=1)

    rospy.spin()