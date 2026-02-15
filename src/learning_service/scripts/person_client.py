#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
from learning_service.srv import Person, PersonRequest

def person_client() :
    rospy.init_node("person_client")

    rospy.wait_for_service("person_server")

    try:
        person_client = rospy.ServiceProxy("person_server", Person)
        response = person_client("Tom", 18, PersonRequest.male)
        rospy.loginfo(response.result)
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s" % e)

if __name__ == "__main__":
    person_client()