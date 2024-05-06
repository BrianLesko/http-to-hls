#!/bin/bash

docker run -d -p 8080:80 -v $(pwd)/hls:/hls -v $(pwd):/etc/nginx -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf --name hls hls