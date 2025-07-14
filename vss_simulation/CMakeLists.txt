cmake_minimum_required(VERSION 3.8)
project(vss_simulation)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# A única dependência necessária para um pacote sem código C++
find_package(ament_cmake REQUIRED)

# Instala o manifest do pacote
install(
  FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)

# Instala todos os diretórios de recursos para que o launch file os encontre
install(
  DIRECTORY launch models worlds urdf rviz
  DESTINATION share/${PROJECT_NAME}
)

# Configurações de teste padrão
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()