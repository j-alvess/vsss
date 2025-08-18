import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
     pkg_dir = get_package_share_directory('vss_simulation')

     robot_path = os.path.join(pkg_dir, 'urdf', 'vss.xacro')
     camera_file = PathJoinSubstitution([pkg_dir, 'urdf', 'camera.urdf.xacro'])

     # Propriedades gerais dos robos
     robots_z = 0.1
     robots_Y = -1.57

     # Propriedades especificas dos robos
     robots = [ # ['nome', [x, y]]
          [
               'robot_team1_center',
               [0.375, 0]
          ], 
          [
               'robot_team1_north',
               [0.375, 0.4]
          ], 
          [
               'robot_team1_south',
               [0.375, -0.4]
          ],
          [
               'robot_team2_center',
               [-0.375, 0]
          ], 
          [
               'robot_team2_north',
               [-0.375, 0.4]
          ], 
          [
               'robot_team2_south',
               [-0.375, -0.4]
          ]]

     # Criacao de um LaunchDescription base com a arena
     ld = LaunchDescription([IncludeLaunchDescription(
          PythonLaunchDescriptionSource([
               pkg_dir, '/launch/arena_vss.launch.py'
          ])
     )])

     # Criacao dos robos
     for name, pos in robots:
          robot_description = Command([
               'xacro ',
               robot_path,
               f' prefix:={name}_'
          ])

          robot_state_publisher = Node(
               package='robot_state_publisher', 
               executable='robot_state_publisher',
               namespace=name, 
               parameters=[{'robot_description': robot_description}])
          
          spawn_entity = Node(
               package='gazebo_ros', 
               executable='spawn_entity.py',
               arguments=['-entity', name, '-topic', f'/{name}/robot_description', 
                    '-x', str(pos[0]), '-y', str(pos[1]), '-z', str(robots_z), '-Y', str(robots_Y)])

          ld.add_action(GroupAction([
               robot_state_publisher,
               spawn_entity
          ]))

     # Criacao da Camera
     robot_state_publisher_camera = Node(
          package='robot_state_publisher',
          executable='robot_state_publisher',
          name='robot_state_publisher',
          namespace='camera',
          output='screen',
          parameters=[
               {'robot_description': ParameterValue(Command(['xacro ', camera_file]), value_type=str)}
          ])
     spawn_entity_camera = Node(
          package='gazebo_ros',
          executable='spawn_entity.py',
          arguments=['-entity', 'up_camera', '-topic', '/camera/robot_description', '-x', '0', '-y', '0', '-z', '2', '-P', '1.57'],
          output='screen'
     )
     ld.add_action(GroupAction([
          robot_state_publisher_camera,
          spawn_entity_camera
     ]))


     return ld