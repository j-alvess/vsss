import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    pkg_dir = get_package_share_directory('vss_simulation')


    robot_path = os.path.join(pkg_dir, 'urdf', 'vss.xacro')
    

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                pkg_dir, '/launch/arena_vss.launch.py'
            ]),
        ),

        Node(package='robot_state_publisher', 
             executable='robot_state_publisher',
             namespace='robot_team1_center', parameters=[{'robot_description': Command(['xacro ', robot_path])}]),
        Node(package='gazebo_ros', 
             executable='spawn_entity.py',
             arguments=['-entity', 'robot_team1_center', '-topic', '/robot_team1_center/robot_description', '-x', '0.375', '-y', '0', '-z', '0.1', '-Y', '-1.57']),

        Node(package='robot_state_publisher', 
             executable='robot_state_publisher',
             namespace='robot_team1_north', parameters=[{'robot_description': Command(['xacro ', robot_path])}]),
        Node(package='gazebo_ros', 
             executable='spawn_entity.py',
             arguments=['-entity', 'robot_team1_north', '-topic', '/robot_team1_north/robot_description', '-x', '0.375', '-y', '0.4', '-z', '0.1', '-Y', '-1.57']),

        Node(package='robot_state_publisher', 
             executable='robot_state_publisher',
             namespace='robot_team1_south', parameters=[{'robot_description': Command(['xacro ', robot_path])}]),
        Node(package='gazebo_ros', 
             executable='spawn_entity.py',
             arguments=['-entity', 'robot_team1_south', '-topic', '/robot_team1_south/robot_description', '-x', '0.375', '-y', '-0.4', '-z', '0.1', '-Y', '-1.57']),

        Node(package='robot_state_publisher', 
             executable='robot_state_publisher',
             namespace='robot_team2_center', parameters=[{'robot_description': Command(['xacro ', robot_path])}]),
        Node(package='gazebo_ros', 
             executable='spawn_entity.py',
             arguments=['-entity', 'robot_team2_center', '-topic', '/robot_team2_center/robot_description', '-x', '-0.375', '-y', '0', '-z', '0.1', '-Y', '1.57']),

        Node(package='robot_state_publisher', 
             executable='robot_state_publisher',
             namespace='robot_team2_north', parameters=[{'robot_description': Command(['xacro ', robot_path])}]),
        Node(package='gazebo_ros', 
             executable='spawn_entity.py',
             arguments=['-entity', 'robot_team2_north', '-topic', '/robot_team2_north/robot_description', '-x', '-0.375', '-y', '0.4', '-z', '0.1', '-Y', '1.57']),

        Node(package='robot_state_publisher', 
             executable='robot_state_publisher',
             namespace='robot_team2_south', parameters=[{'robot_description': Command(['xacro ', robot_path])}]),
        Node(package='gazebo_ros', 
             executable='spawn_entity.py',
             arguments=['-entity', 'robot_team2_south', '-topic', '/robot_team2_south/robot_description', '-x', '-0.375', '-y', '-0.4', '-z', '0.1', '-Y', '1.57']),
        
    ])