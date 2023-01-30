import os
import h5py
import numpy as np
import librosa
import wave

# --查看h5py文件--
fileName = 'MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.h5'
filePath = '/data/xyth/piano_transcription/hdf5s/maestro/2004/'
h5f = h5py.File(filePath + fileName, 'r')

# --查看h5py文件里里所有的键--
# print([key for key in h5f.keys()]) 
# midi的h5是三个key：midi_event, midi_event_time, waveform

# --查看midi_event--
midi_event = np.array(h5f['midi_event'])
for e in midi_event:
    print(e.decode())

# --查看midi_event_time--
# 单位：秒
#midi_event_time = np.array(h5f['midi_event_time'])

'''
enumerate：有序号
for time in enumerate(midi_event_time):
    print(time)

结果：
(28507, 943.4167)
(28508, 943.4167)
(28509, 943.43335)
(28510, 943.4354)
(28511, 943.4552)
(28512, 943.4552)
(28513, 943.46356)

用两个接收
for idx, time in enumerate(midi_event_time
idx 接受的是序号，time接收的是时间
'''

#for idx, time in enumerate(midi_event_time):
#    print(idx)
#    print(time)
    

# --查看waveform--
# sample_rate = 16000  # 重采样率
#waveform = np.array(h5f['waveform'])
#print(waveform)
#print(type(waveform)) # 从hdf5里读出来的是ndarray

# --查看waveform的采样率--
# 直接从获得
#fileDir = "/data/xyth/maestro-v3.0.0/2004"
#fileName = "MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.wav"
#filePath = os.path.join(fileDir, fileName)

#f = wave.open(filePath)
#params = f.getparams()
#Channels = f.getnchannels()
#SampleRate = f.getframerate()   # 采样频率
#frames = f.getnframes()   # 采样点数
#Duration = frames / float(SampleRate)  # 计算时长，秒
#DurationMinute = Duration / 60
#print(SampleRate)
#print(DurationMinute)

## --音频处理工具--
#
# import os
# import librosa
# import numpy as np
# from scipy.io import wavfile
#
# sample_rate = 16000  # 重采样率
#
# # ---转格式小工具---
# def float32_to_int16(x):
#     assert np.max(np.abs(x)) <= 1.
#     return (x * 32767.).astype(np.int16) # astype：强制转化数据类型
#
# def int16_to_float32(x):
#     return (x / 32767.).astype(np.float32)
#
# audio_dir = "/Users/logickino/Documents/音乐学习/Andrew Gordon - 60 Of The Funkiest Keyboard Riffs/mp3"
# audio_name = "FUNKRI01.mp3"
# audio_path = os.path.join(audio_dir, audio_name)
#
# (audio, _) = librosa.core.load(audio_path, sr=sample_rate, mono=True)  # 读音频文件，重新按照采样率采样
#
# # 音频长度计算
# # 计算
# print(len(audio))              # 音频时间，一共有多少帧
# print(len(audio)/sample_rate)  # 音频时间长短（单位：s）
#
# # 转格式的话是float32_to_int16，不转格式的话，就是float32
# # data = float32_to_int16(audio)
# print(audio)
#
# # 转调功能测试，一般用于数据增广, n_steps是转调
# wave = librosa.effects.pitch_shift(audio, sr=sample_rate, n_steps = -5, bins_per_octave=12)
# print(wave)
#
# # 数据的保存
# # 设定名称，保存路径
# save_name = "test2.wav"
# save_path = os.path.join(audio_dir, save_name)
#
# # 保存wav文件
# # wavfile.write(save_path, rate=sample_rate, data=wave)
# wave = float32_to_int16(wave)
#
# wavfile.write(save_path, rate=sample_rate, data=wave)