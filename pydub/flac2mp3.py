from pydub import AudioSegment
import glob,os

taget_audios = glob.glob('input/*.flac')

for taget_audio in taget_audios:
  filename = os.path.splitext(os.path.basename(taget_audio))[0]
  export_audio = AudioSegment.from_file(taget_audio, "flac")
  export_audio.export(os.path.join ("output/", filename + ".mp3"), format="mp3", bitrate="320k")