import os
import edge_tts
import asyncio
from utils import timeit
from playsound import playsound

voice = "pt-BR-AntonioNeural"
output_file = "fala.mp3"

@timeit
async def create_tts(text):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print("nova fala")

@timeit
def speak(text):
    asyncio.run(create_tts(text))

    playsound(output_file)
    
    os.remove(output_file)


if __name__ == "__main__":
    speak("Rodando Teste 1")
    speak("Rodando Teste 2")
    speak("Todos os testes foram concluidos")
