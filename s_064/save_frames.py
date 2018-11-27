#####
# The save_video_frames function saves sketches' frames to be used by `ffmpeg` command to generate videos.
# For example, if we call the method with the following parameters:
#
# save_video_frames(25, 60 * 10)
#
# The ffmpeg commands to generate the video would be:
#
# $ ffmpeg -framerate 25 -pattern_type glob -i '*.png' -c:v libx264 -r 25 -pix_fmt yuv420p out_youtube.mp4
#
# The single loose coupling between the Python code and the ffmpeg is the frame rate.
#
# You can also cut it to extract a smaller sample (ideal for Instagram or Twitter)
# $ ffmpeg -ss 00:00:00 -t 00:00:20 -i out_youtube.mp4 out.mp4
#####


def save_video_frames(frame_rate, seconds, stop_run=True, extension="png", log_frame=True, pg_graphics=None):
    """
    GIST: https://gist.github.com/berinhard/d2ef20f361f70b7c0a216957d993efb2
    Save the required number of frames given for `seconds` with the given `frame_rate`.

    stop_run: calls noLoop() after saving all frames
    extension: file extension
    log_frame: enables logging in the terminal
    """
    num_frames = frame_rate * seconds

    if log_frame:
        print("{} /  {} - {}%".format(
            frameCount, int(num_frames), int(frameCount * 100 / num_frames)
        ))
    if frameCount <= num_frames:
        frame_name = "#" * (len(str(num_frames)))
        if not pg_graphics:
            saveFrame("{}.{}".format(frame_name, extension))
        else:
            frame_name = frameCount
            pg_graphics.save("{}.{}".format(frame_name, extension))
    elif stop_run:
        noLoop()
