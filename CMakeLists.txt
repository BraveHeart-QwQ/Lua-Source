cmake_minimum_required(VERSION 3.10)
project(lua53)

add_subdirectory(Lua-Source)

install(TARGETS lua lua53
    RUNTIME DESTINATION ${CMAKE_SOURCE_DIR}/out/bin
    LIBRARY DESTINATION ${CMAKE_SOURCE_DIR}/out/lib
)
