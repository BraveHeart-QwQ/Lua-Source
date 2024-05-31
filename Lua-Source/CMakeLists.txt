cmake_minimum_required(VERSION 3.10)
project(lua53)

set(CMAKE_C_STANDARD 90)
option(STUDY_USE "Build for learning the source codes(Add head files in the projects)." ON)

file(GLOB LUA_EXE "lua.c")
# file(GLOB LUAC_EXE "luac.c")

if(STUDY_USE)
    file(GLOB LUALIB_SRC "*.h" "*.c")
    file(GLOB LUAC_SRC "*.h" "*.c")
    list(REMOVE_ITEM LUALIB_SRC ${LUA_EXE} ${LUAC_EXE})
    list(REMOVE_ITEM LUAC_SRC ${LUAC_EXE})
else()
    aux_source_directory(src LUALIB_SRC)
    aux_source_directory(src LUAC_SRC)
    list(REMOVE_ITEM LUALIB_SRC ${LUA_EXE} ${LUAC_EXE})
    list(REMOVE_ITEM LUAC_SRC ${LUAC_EXE})
endif()

if(WIN32)
    add_definitions(-DLUA_BUILD_AS_DLL)
else()
    add_compile_options(-fdeclspec)
endif()

add_library(lua53 SHARED ${LUALIB_SRC})

add_executable(lua ${LUA_EXE})
target_link_libraries(lua lua53)

# add_executable(luac ${LUAC_EXE})
