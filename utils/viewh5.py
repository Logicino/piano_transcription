import h5py
import numpy as np

fileName = 'MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.h5'
filePath = '/data/xyth/piano_transcription/hdf5s/maestro/2004/'
h5f = h5py.File(filePath + fileName, 'r')

# 查看所有的键
# print([key for key in h5f.keys()]) 
# midi的h5是三个key：midi_event, midi_event_time, waveform

midi_event = np.array(h5f['midi_event'])
for e in midi_event:
    print(e.decode())
# print(e.decode() for e in midi_event)

# midi_events = [e.decode() for e in hf['midi_event'][:]]  # .decode() 字符串编码转换

# midi_event_time = np.array(h5f['midi_event_time'])
# print(midi_event_time)

# waveform = np.array(h5f['waveform'])
# print(waveform)
# print(waveform.shape[0])
