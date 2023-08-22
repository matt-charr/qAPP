#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "qa::factory" for configuration "Release"
set_property(TARGET qa::factory APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(qa::factory PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libfactory.a"
  )

list(APPEND _cmake_import_check_targets qa::factory )
list(APPEND _cmake_import_check_files_for_qa::factory "${_IMPORT_PREFIX}/lib/libfactory.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
