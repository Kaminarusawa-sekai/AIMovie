# Import everything needed to edit video clips
from moviepy.editor import *
import moviepy


def pic_to_video(pic_path,timestep):
    clip=ImageClip(pic_path)
    clip.set_position(0,0)
    clip=clip.set_duration(timestep)
    clip.fps=24
    return clip


def pics_to_video(pics,timestep):
    clips=[]
    for p in pics:
        clip=pic_to_video(p,timestep)
        clips.append(clip)

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("my_concatenation.mp4")
