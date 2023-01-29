import h5py
import numpy as np

fileName = 'MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.h5'
filePath = '/data/xyth/piano_transcription/hdf5s/maestro/2004/'
h5f = h5py.File(filePath + fileName, 'r')

# 查看所有的键
print([key for key in h5f.keys()]) 
# midi的h5是三个key：midi_event, midi_event_time, waveform

#rgb = np.array(h5f['rgb'])  # 创建以h5中rgb这一group数据为内容的numpy类型array矩阵；
#rgb = np.transpose(rgb, (1, 2, 0))
#print('np.array type:', type(rgb))
#print('np.array dtype:', rgb.dtype)
#rgb = np.asfarray(rgb)
#print('np.asfarray type:', type(rgb))
#print('np.asfarray dtype:', rgb.dtype)

midi_event = np.array(h5f['midi_event'])
# print("midi_event", midi_event)

midi_event_time = np.array(h5f['midi_event_time'])
# print(midi_event_time)

waveform = np.array(h5f['waveform'])
print(waveform)
print(waveform.shape[0])
