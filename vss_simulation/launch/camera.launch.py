from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():

    pkg_share = get_package_share_directory('vss_simulation')
    xacro_file = PathJoinSubstitution([pkg_share, 'urdf', 'camera.urdf.xacro'])
    rviz_config = PathJoinSubstitution([pkg_share, 'rviz', 'display_vss.rviz'])
    robot_desc = Command(['xacro ', xacro_file])

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {'robot_description': ParameterValue(robot_desc, value_type=str)}
            ]
        )
    ])