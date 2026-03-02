#include "ros/ros.h"
#include "plumbing_server_client/AddInts.h"

/*
    服务端 解析客户端数据并运算产生响应
    1. 包含头文件
    2. 初始化 ros 节点
    3. 创建 ros 句柄
    4. 创建 服务对象
    5. 处理请求并产生响应
    6.spin()
*/

bool donums(plumbing_server_client::AddInts::Request &req, plumbing_server_client::AddInts::Response &res)
{
    //处理请求
    int num1 = req.num1;
    int num2 = req.num2;

    //产生响应
    res.sum = num1 + num2;

    ROS_INFO("请求数据: %d, %d, 服务响应: %d", num1, num2, res.sum);
    return true;
}


int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "heiShui"); //初始化 ros 节点 名称唯一

    ros::NodeHandle nh; //创建 ros 句柄

    ros::ServiceServer server = nh.advertiseService<plumbing_server_client::AddInts::Request, plumbing_server_client::AddInts::Response>("addInts", donums);
    
    ROS_INFO("服务端启动");
    ros::spin();
    return 0;
}