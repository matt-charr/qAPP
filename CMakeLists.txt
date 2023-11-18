CMAKE_MINIMUM_REQUIRED(VERSION 3.27)
PROJECT("qa-demo")

# find qalgebra lib.
# WARNING: please set CMAKE_PREFIX_PATH at qalgebra location.
# ex: I installed qalgebra at C:\Program Files\qa\qalgebra,
# I need to configure with the command 'cmake -DCMAKE_PREFIX_PATH="C:\Program Files\qa\qalgebra"
FIND_PACKAGE(qalgebra REQUIRED)

# create lib.
# WARNING: If you add subdirectories, you have to provide the source files inside.
# ex: I create a subdirectory 'babar/', I need to relpace with:
# FILE(GLOB SRC *.cpp babar/*.cpp)
FILE(GLOB SRC *.cpp)
ADD_LIBRARY(${LIB_NAME} STATIC ${SRC})
TARGET_LINK_LIBRARIES(${LIB_NAME} PUBLIC QA::qalgebra)

# install.
# WARNING: You need to provide a name for the library with the option -DLIB_NAME.
# WARNING: You need to provide the installation directory with the option -DCMAKE_INSTALL_PREFIX.
# ex: I want to install my library at C:\Program Files\qa\my_library,
# I need to configure with the command 'cmake -DCMAKE_INSTALL_PREFIX="C:\Program Files\qa\my_library"
INCLUDE(GNUInstallDirs)
TARGET_INCLUDE_DIRECTORIES(${LIB_NAME} PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}>
    $<INSTALL_INTERFACE:${LIB_NAME}/include>
)
INSTALL(TARGETS ${LIB_NAME}
    EXPORT ${LIB_NAME}_Exports
    LIBRARY DESTINATION 
        ${LIB_NAME}/lib
        NAMELINK_SKIP
    RUNTIME DESTINATION 
        ${CMAKE_INSTALL_BINDIR}
    ARCHIVE DESTINATION 
        ${LIB_NAME}/lib
)
INSTALL(
    EXPORT ${LIB_NAME}_Exports
    DESTINATION 
        ${LIB_NAME}/lib/cmake/${LIB_NAME}
    NAMESPACE QA::
)
INSTALL(TARGETS ${LIB_NAME}
    LIBRARY DESTINATION 
        ${LIB_NAME}/lib
        NAMELINK_ONLY
    RUNTIME DESTINATION 
        ${CMAKE_INSTALL_BINDIR}
    ARCHIVE DESTINATION 
        ${LIB_NAME}/lib
)
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/${LIB_NAME}Config.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/${LIB_NAME}Config.cmake"
    INSTALL_DESTINATION 
        ${LIB_NAME}/lib/cmake/${LIB_NAME}
)
write_basic_package_version_file(
    "${LIB_NAME}ConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)
INSTALL(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/${LIB_NAME}Config.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/${LIB_NAME}ConfigVersion.cmake
    DESTINATION
        ${LIB_NAME}/lib/cmake/${LIB_NAME}
)