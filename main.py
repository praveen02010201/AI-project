import whisper
model = whisper.load_model("base")
result = model.transcribe("audiofile.mp3")

with open("textline.txt", "w") as f:
    f.write(result["text"])