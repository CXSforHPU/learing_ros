#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from learning_service.srv import Person, PersonResponse

def person_Callback(req):
    rospy.loginfo("Person Info: name:%s age:%d height:%f", req.name, req.age, req.sex)
    return PersonResponse("OK")

def person_server() :
    rospy.init_node("person_server")
    service = rospy.Service("person_server", Person, person_Callback)
    rospy.loginfo("Waiting for client to connect")
    rospy.spin()

if __name__ == "__main__":
    person_server()