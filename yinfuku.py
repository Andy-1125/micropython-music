from machine import Pin, PWM
from time import sleep as s

'''
【音符频率对应表 】

音符  频率 占空比

--------------------------------

低1DO 262 1908 #-1    DO# 277 1805

低2RE 294 1700 #-2    RE# 311 1608

低3MI 330 1516 #-3    MI# 340 1470\

低4FA 349 1433 #-4    FA# 370 1350

低5SO 392 1276 #-5    SO# 415 1205

低6LA 440 1136 #-6    LA# 466 1072

低7SI 494 1012 #-7    SI# 524 0954\

中1DO 523 0956 #1    DO# 554 0903

中2RE 578 0842 #2    RE# 622 0804

中3MI 659 0759 #3    MI# 682 0733\

中4FA 698 0716 #4    FA# 740 0676

中5SO 784 0638 #5    SO# 831 0602

中6LA 880 0568 #6    LA# 932 0536

中7SI 988 0506 #7    SI# 1046 478\

高1DO 1046 478 #11    DO# 1109 451

高2RE 1175 426 #22    RE# 1245 402

高3MI 1318 372 #33    MI# 1356 368\

高4FA 1397 358 #44    FA# 1480 338

高5SO 1568 319 #55    S0# 1661 292

高6LA 1760 284 #66    LA# 1865 268

高7SI 1976 253 #77    SI# 2066 242\

(#表示半音,用于上升半个音  \表示不存在的半音)
'''


def yin(fu, time):
    # 创建PWM对象
    pwm = PWM(Pin(2))
    # 音符频率与占空比的映射表
    notes = {
        1: (523, 956),
        2: (578, 842),
        3: (659, 759),
        4: (698, 716),
        5: (784, 638),
        6: (880, 568),
        7: (988, 506),
        -1: (262, 1908),
        -2: (294, 1700),
        -3: (330, 1516),
        -4: (349, 1433),
        -5: (392, 1276),
        -6: (440, 1136),
        -7: (494, 1012),
        11: (1046, 478),
        22: (1175, 426),
        33: (1318, 372),
        44: (1397, 358),
        55: (1568, 319),
        66: (1760, 284),
        77: (1976, 253),
    }
    # 查找音符对应的频率和占空比
    if fu in notes:
        freq, duty = notes[fu]
        # PWM频率
        pwm.freq(freq)
        # PWM占空比（1024=100%）
        pwm.duty(duty)
        # 音符时间
        s(time)
        # 休止
        pwm.duty(0)
        s(time)
    else:
        # 休止符
        pwm.duty(0)
        # 音符时间
        s(time)

