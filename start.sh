#!/bin/bash

# 1. start your http camera server, then

# 2. Run ffmpeg to create the HLS files

ffmpeg -i http://127.0.0.1:8000 \
-c:v libx264 \
-preset veryfast \
-profile:v baseline \
-level 3.0 \
-hls_time 60 \
-hls_list_size 90000 \
-hls_flags delete_segments \
-hls_start_number_source datetime \
-hls_segment_filename "./hls/file%d.ts" \
-f hls ./hls/index.m3u8

# 3. serve the HLS content on a web server

# view the hls content


