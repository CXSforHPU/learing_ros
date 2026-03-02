#include "ros/ros.h"
#include "plumbing_server_client/AddInts.h"

/*
    客户端：请求服务
    1. 包含头文件
    2. 初始化 ros 节点
    3. 创建 ros 句柄
    4. 创建 请求的 服
    5. 发送请求并 获取响应
    6. 处理响应

*/


int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"xiaoMing");
    ros::NodeHandle nh;

    ros::ServiceClient client = nh.serviceClient<plumbing_server_client::AddInts>("addInts");

    plumbing_server_client::AddInts ai;
    ai.request.num1 = 10;
    ai.request.num2 = 20;

    bool flag = client.call(ai);
    if (flag)
    {
        ROS_INFO("执行结果：%d",ai.response.sum);
    }
    else
    {
        ROS_INFO("调用服务失败");
    }
    

    return 0; 
}
