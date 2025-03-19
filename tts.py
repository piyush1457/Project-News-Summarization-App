from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    if not text.strip():
        print("Error: No text provided for TTS")
        return

    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    os.system(f"start {filename}")

if __name__ == "__main__":
    text_to_speech("यह टेस्ला के समाचारों का विश्लेषण है।")
