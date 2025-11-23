from fastapi import FastAPI, UploadFile
from moviepy.editor import VideoFileClip
import os
import uuid

app = FastAPI()

@app.post("/upload")
async def upload_video(file: UploadFile):
    temp_name = f"input_{uuid.uuid4()}.mp4"
    with open(temp_name, "wb") as buffer:
        buffer.write(await file.read())

    clip = VideoFileClip(temp_name)
    duration = clip.duration

    max_clips = 8
    clip_duration = 30

    num_clips = min(max_clips, int(duration // clip_duration))
    output_files = []

    for i in range(num_clips):
        start = i * clip_duration
        end = start + clip_duration

        subclip = clip.subclip(start, min(end, duration))
        out_name = f"clip_{i+1}_{uuid.uuid4()}.mp4"
        subclip.write_videofile(out_name)

        output_files.append(out_name)

    clip.close()
    os.remove(temp_name)

    return {"clips": output_files}
