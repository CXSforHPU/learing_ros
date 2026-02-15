#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from learning_topic.msg import Person


def person_publisher():
    rospy.init_node('person_publisher', anonymous=True)

    pub = rospy.Publisher('person_info', Person, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        person = Person()
        person.name = 'Tom'
        person.age = 18
        person.sex = Person.male


        rospy.loginfo("Publish person info: %s, %d, %d", person.name, person.age, person.sex)

        pub.publish(person)

        rate.sleep()

if __name__ == '__main__':
    try:
        person_publisher()
    except rospy.ROSInterruptException:
        pass