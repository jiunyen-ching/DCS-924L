# DCS-924L
The script fetches frames from the DLINK DCS-942L IP camera and saves them into folders separated by day and hour. Dates arranged in Year-Month-Day order for easy sorting.\
In case of a power disruption, DCS-924L does not have an internal battery to keep it running. Hence, when the camera is able to resume operation, the clock resets to factory settings and the timestamp will be out of sync. To account for this, the code fetches timestamps from the computer and writes it on the image.

## Requirement
1. OpenCV
2. ffmpeg

## Usage
1. Ensure that you are able to view the camera stream from an Internet browser via `http://<ip_address>/video.mjpg.cgi`
2. In `get_frames.py`, edit the code to your camera's IP address, username, and password.
3. Run `get_frames.py` to start recording.
4. To convert the frames into video, edit the code in `process_video.py` and change `base`, `date`, and `hour` to where the frames are stored.
5. Output video is in .mp4 format and is stored in the same folder as the source frames.
