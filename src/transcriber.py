import whisper

model = whisper.load_model("base.en")
result = model.transcribe("VMP7679265734.mp3")
with open("files/output/VMP7679265734.txt", "w") as file:
    file.write(result["text"])
