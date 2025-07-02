cmake_minimum_required(VERSION 3.8)
project(vss_simulation)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# Adicione outros pacotes que seu código C++ possa precisar, como rclcpp, etc.
# find_package(rclcpp REQUIRED)

# Instala o package.xml
install(
  FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)

# Instala os diretorios com recursos
install(
  DIRECTORY launch models worlds
  DESTINATION share/${PROJECT_NAME}
)

# Se as pastas rviz e urdf tiverem arquivos, adicione-as também
# install(
#   DIRECTORY rviz urdf
#   DESTINATION share/${PROJECT_NAME}
# )

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
