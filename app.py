import subprocess
import sys

def http_to_hls(http_stream_url, output_folder):
    # Constructing the FFmpeg command to convert the HTTP stream to HLS
    command = [
        'ffmpeg',
        '-i', http_stream_url,  # Input stream URL
        '-profile:v', 'baseline',  # Baseline profile (for compatibility with most devices)
        '-level', '3.0', 
        '-s', '640x360',  # Output resolution
        '-start_number', '0',  # Start the HLS list at zero
        '-hls_time', '3',  # Segment duration
        '-hls_list_size', '360',  # Number of playlist entries, allowing 1 hour of past content
        '-hls_flags', 'append_list',  # Append to the list rather than starting a new one
        '-f', 'hls',  # HLS format
        output_folder + '/index.m3u8'  # Output path for the playlist
    ]

    
    # Running the FFmpeg command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    
    if process.returncode != 0:
        print("Error:", err.decode())
    else:
        print("Conversion completed successfully. HLS files are saved in:", output_folder)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python http_to_hls.py [HTTP_STREAM_URL] [OUTPUT_FOLDER]")
    else:
        http_to_hls(sys.argv[1], sys.argv[2])
