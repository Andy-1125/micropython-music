from yinfuku2 import yin
from time import sleep as s
# 音符序列
note_sequence = [1,1,5,5,6,6,5,4,4,3,3,2,2,1,5,5,4,4,3,3,2,5,5,4,4,3,3,2]
# 每个音符的播放时间，单位为秒
time_per_note = 0.2

for note in note_sequence:
    yin(note, time_per_note)
    # 音符之间的短暂停顿，可根据需要调整
    s(0.05)
    yin(0, 0)