from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use sim time if true'
    )

    pkg_share = get_package_share_directory('vss_simulation')
    xacro_file = PathJoinSubstitution([pkg_share, 'urdf', 'vss.xacro'])
    rviz_config = PathJoinSubstitution([pkg_share, 'rviz', 'display_vss.rviz'])
    robot_desc = Command(['xacro ', xacro_file])

    return LaunchDescription([
        use_sim_time_arg,
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {'use_sim_time': LaunchConfiguration('use_sim_time')},
                {'robot_description': ParameterValue(robot_desc, value_type=str)}
            ]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config],
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
        ),
    ])
