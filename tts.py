from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    if not text.strip():
        print("Error: No text provided for TTS")
        return

    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    
    # ✅ Play the audio (Works for Windows)
    os.system(f"start {filename}")

    # ✅ If using macOS/Linux, use:
    # os.system(f"afplay {filename}")  # macOS
    # os.system(f"mpg321 {filename}")  # Linux

# Test TTS
if __name__ == "__main__":
    text_to_speech("यह टेस्ला के समाचारों का विश्लेषण है।")
