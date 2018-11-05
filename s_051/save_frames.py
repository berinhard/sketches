def save_video_frames(frame_rate, seconds, stop_run=True, extension="png", log_frame=True):
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
        frame_name ="#" * (len(str(num_frames)))
        saveFrame("{}.{}".format(frame_name, extension))
    elif stop_run:
        noLoop()
