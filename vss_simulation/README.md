<h1> VSS-Field_Simulation <h1>

<h2> Spawn world </h2>
<p> To spawn VSS Field:
<pre>
ros2 launch vss_simulation start_world.launch.py
</pre>

<h2> Spawn Rviz Simulation </h2>
<p> To spawn VSS Rviz:
<pre>
ros2 launch vss_simulation rviz.launch.py
</pre>

<h2> Gazebo Simulation </h2>
<p> To spawn Gazebo simulation:
<pre>
ros2 launch vss_simulation robot.launch.py
</pre>

<h3> Debug </h3>
<p> To spawn controller through terminal: 
<pre>
ros2 run controller_manager spawner -c /robot_team1_center/controller_manager diff_cont
</pre>
<p> To use controller: 
<pre>
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/robot_team1_center/diff_cont/cmd_vel_unstamped
</pre>