# import pvporcupine
# import pyaudio
# import struct

# # Replace this with your actual access key from https://console.picovoice.ai/
# ACCESS_KEY = "tw/z5sRsBuOXg/xFOpsIaNzmDICqmrMj4t8zWEdCoYEtQIjfBxgDrw=="

# porcupine = pvporcupine.create(
#     access_key=ACCESS_KEY,
#     keywords=["jarvis"]
# )

# pa = pyaudio.PyAudio()
# stream = pa.open(
#     rate=porcupine.sample_rate,
#     channels=1,
#     format=pyaudio.paInt16,
#     input=True,
#     frames_per_buffer=porcupine.frame_length,
# )

# print("Listening for hotword...")

# try:
#     while True:
#         pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
#         pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

#         result = porcupine.process(pcm)
#         if result >= 0:
#             print("Hotword detected!")
#             break

# except KeyboardInterrupt:
#     print("Interrupted.")

# finally:
#     stream.stop_stream()
#     stream.close()
#     pa.terminate()
#     porcupine.delete()
