import ffmpeg


def convert_to_mp4(file_name,name):
    input_name = file_name
    stream = ffmpeg.input(input_name)
    stream = ffmpeg.hflip(stream)
    changed_file_name=file_name.replace('.webm','.mp4')
    stream = ffmpeg.output(stream, changed_file_name)
    ffmpeg.run(stream)

def convert_to_wav(file_name,name):
    input_name = file_name
    stream = ffmpeg.input(input_name)
    stream = ffmpeg.hflip(stream)
    changed_file_name = file_name.replace('.webm', '.wav')
    stream = ffmpeg.output(stream, changed_file_name)
    ffmpeg.run(stream)

