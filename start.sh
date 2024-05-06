#!/bin/bash

# 1. start your http camera server, then

# 2. Run ffmpeg to create the HLS files

ffmpeg -i http://127.0.0.1:8000 -y \
-c:v libx264 \
-b:v 800000 \
-preset veryfast \
-profile:v baseline \
-level 3.0 \
-hls_time 3 \
-hls_list_size 3 \
-hls_flags delete_segments \
-hls_start_number_source datetime \
-hls_segment_filename "./hls" \
-f hls ./hls/index.m3u8

# 3. serve the HLS content on a web server

# view the hls content


