cmake_minimum_required(VERSION 3.10)
project(lua53)

add_subdirectory(Lua-Source)

install(TARGETS lua
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
)
