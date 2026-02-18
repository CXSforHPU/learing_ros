#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"

/*
    发布方：发布person数据
        1.包含头文件；
        2.初始化 ros 节点；
        3.创建 ros 句柄；
        4.创建发布者对象；
        5.组织被发布的数据，并编写发布逻辑；
        6.spin().
*/

int main(int argc, char **argv)
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "banzhuren");

    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<plumbing_pub_sub::Person>("chatter", 10);

    plumbing_pub_sub::Person person;
    person.name = "张三";
    person.age = 18;
    person.height = 1.68;

    ros::Rate rate(1);

    while (ros::ok())
    {
        person.age++;
        pub.publish(person);
        ROS_INFO("发布的数据：%s, %d, %.2f", person.name.c_str(), person.age, person.height);
        rate.sleep();
        ros::spinOnce();
    }

}

