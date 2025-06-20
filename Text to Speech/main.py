import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

L=["Arun", "Faisal", "Sunny"]

for i in L:
    x=(f"Hey {i} drink water")
    speaker.Speak(x)