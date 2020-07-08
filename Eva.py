import rospy
from std_msgs.msg import String

def callback_str(data):
    rospy.loginfo(data.data)

def Eva_listener():
    rospy.init_node('Eva', annoymous=False)
    rospy.subscriber('hello', String, callback_str)
    rospy.spin()

if __name__== '__main__':

    Eva_listener()
