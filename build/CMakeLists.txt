cmake_minimum_required (VERSION 3.6)
project(WilsonDiscordBot)

add_executable(WilsonDiscordBot source.cpp)

add_subdirectory(deps/sleepy-discord)
target_link_libraries(WilsonDiscordBot sleepy-discord)