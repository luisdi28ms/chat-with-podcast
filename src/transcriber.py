import whisper

model = whisper.load_model("base.en")
result = model.transcribe("VMP7679265734.mp3")
print(result["text"])
