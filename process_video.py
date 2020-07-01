import ffmpeg
import os
from glob import glob

base = '/your/base/path/here'
date = '<date_folder>'
hour = '<hour_folder>'
path_to_hour = os.path.join(base,date,hour)

def write_video():
    print('writing to %s' % os.path.join(path_to_hour,hour+'.mp4'))
    (
        ffmpeg
        .input(os.path.join(path_to_hour,'*.jpg'), pattern_type='glob', framerate=10)
        .output(os.path.join(path_to_hour,hour+'.mp4'))
        .overwrite_output()
        .run()
    )

if __name__=='__main__':
    write_video()
