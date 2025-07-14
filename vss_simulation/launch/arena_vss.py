import os

from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_prefix
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_share = FindPackageShare(package='vss_simulation').find('vss_simulation')
    world_gazebo_path = os.path.join(pkg_share, 'worlds/campo_vss/campo_vss.world')
    
    install_share_dir = os.path.join(get_package_prefix('vss_simulation'), 'share')
    pkg_models_path = os.path.join(pkg_share, 'models')

    if 'GAZEBO_MODEL_PATH' in os.environ:
        os.environ['GAZEBO_MODEL_PATH'] = os.environ['GAZEBO_MODEL_PATH'] + ':' + install_share_dir + ':' + pkg_models_path
    else:
        os.environ['GAZEBO_MODEL_PATH'] = install_share_dir + ':' + pkg_models_path

    if 'GAZEBO_PLUGIN_PATH' in os.environ:
        os.environ['GAZEBO_PLUGIN_PATH'] = os.environ['GAZEBO_PLUGIN_PATH'] + ':' + os.path.join(get_package_prefix('vss_simulation'), 'lib')
    else:
        os.environ['GAZEBO_PLUGIN_PATH'] = os.path.join(get_package_prefix('vss_simulation'), 'lib')


    print("GAZEBO MODELS PATH=="+str(os.environ["GAZEBO_MODEL_PATH"]))
    print("GAZEBO PLUGINS PATH=="+str(os.environ["GAZEBO_PLUGIN_PATH"]))
    
    world_gazebo_arg = DeclareLaunchArgument(name="world", default_value=str(world_gazebo_path), description="starts world for simulation")
    
    gazebo_launch = ExecuteProcess(
        # Adicionado '--ros-args --log-level=debug' para mais detalhes nos logs dos nós ROS do Gazebo
        cmd=['gazebo', '--verbose', '--ros-args --log-level=debug', '-s', 'libgazebo_ros_factory.so', '-s', 'libgazebo_ros_init.so', LaunchConfiguration('world')],
        output='screen'
    )

    return LaunchDescription([
        world_gazebo_arg,
        gazebo_launch,
    ])
