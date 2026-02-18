#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"

void doPerson(const plumbing_pub_sub::Person::ConstPtr& person)
{
    ROS_INFO("订阅到的数据：%d, %s, %.2f", person->age, person->name.c_str(), person->height);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ROS_INFO("订阅方p节点启动");
    ros::init(argc, argv, "sub_person_p");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe<plumbing_pub_sub::Person>("chatter", 10, doPerson);
    ros::spin();
    return 0;
}


