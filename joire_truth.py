from robottools import RobotTools
import PySimpleGUI as sg

rt = RobotTools('192.168.11.46', 22222)

# GUI設定
sg.theme()
# ウインドウのレイアウトの作成
# レイアウトはグリッド（2次元リスト）で表現される
layout = []

# モーションボタンのレイアウト
layout.append(
    [
        sg.Button('アイドルモーション開始', key='idle'),
        sg.Button('アイドルモーション停止', key='stop'),
        sg.Button('ポーズリセット', key='reset')    
    ]
)

# 発話ボタンのレイアウト
text_1 = '今から10エックスに乗たす21エックスひく54は0という方程式をたすき掛けという方法を用いて解く手順を説明します。'
layout.append(
    [
        sg.Text(text_1, size=(50, 1)),
        sg.Button('発話', key='speak_1')
    ]
)

text_2 = 'まずエックスに乗の係数が10であるため、積が10となる数字の組み合わせを見つけます。'
layout.append(
    [
        sg.Text(text_2, size=(50, 1)),
        sg.Button('発話', key='speak_2')
    ]
)

text_3 = '次に、定数項がマイナス54であるため、積がマイナス54となる数字の組み合わせを見つけます。'
layout.append(
    [
        sg.Text(text_3, size=(50, 1)),
        sg.Button('発話', key='speak_3')
    ]
)


text_4 = 'ここまでに見つけた数字の組み合わせをこのように置き'
layout.append(
    [
        sg.Text(text_4, size=(50, 1)),
        sg.Button('発話', key='speak_4')
    ]
)

text_5 = '斜めにかけて、それらを足したものがエックスの係数である21となるような組み合わせを見つけます。'
layout.append(
    [
        sg.Text(text_5, size=(50, 1)),
        sg.Button('発話', key='speak_5')
    ]
)
text_6 = 'よってこの数式では一列目が2と5、にれつめがマイナス3と18になります。'
layout.append(
    [
        sg.Text(text_6, size=(50, 1)),
        sg.Button('発話', key='speak_6')
    ]
)
text_7 = 'たすき掛けをしたものにかっこをつけると因数分解の解になるので、かっこ2エックスひく3かっことじ、かっこ5エックスたす18かっことじは0となり、'
layout.append(
    [
        sg.Text(text_7, size=(50, 1)),
        sg.Button('発話', key='speak_7')
    ]
)
text_8 = 'エックスについての方程式を解くとエックスは3/2 とマイナス18/5となります。'
layout.append(
    [
        sg.Text(text_8, size=(50, 1)),
        sg.Button('発話', key='speak_8')
    ]
)
text_9 = '解説は以上となります。QRコードを読み込んで、ご回答お願いします。終わりましたら、右側のベルを鳴らしてください。'
layout.append(
    [
        sg.Text(text_9, size=(50, 1)),
        sg.Button('発話', key='speak_9')
    ]
)

# テキストの自由入力
layout.append(
    [
        sg.InputText(key='free_speech_field', size=(50, 1)),
        sg.Button('発話', key='speak_free')
    ]
)


# ウインドウにレイアウトを設定
window = sg.Window('Sota controller', layout)

# Event loop
while True:
    event, values = window.read(timeout=1)
    if event is None:
        print('Window event is None. exit')
        break
    
    elif event == 'speak_1':
        d = rt.say_text(text_1)
        servo_map = dict(HEAD_R=0,BODY_Y=0,R_SHOU=90,HEAD_P=0,R_ELBO=0,L_ELBO=0,HEAD_Y=0,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    elif event == 'speak_2':
        d = rt.say_text(text_2)
        servo_map = dict(HEAD_R=0,BODY_Y=-50,R_SHOU=90,HEAD_P=-27,R_ELBO=0,L_ELBO=0,HEAD_Y=-37,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    elif event == 'speak_3':
        d = rt.say_text(text_3)
        servo_map = dict(HEAD_R=0,BODY_Y=0,R_SHOU=90,HEAD_P=0,R_ELBO=0,L_ELBO=0,HEAD_Y=0,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    elif event == 'speak_4':
        d = rt.say_text(text_4)
        servo_map = dict(HEAD_R=0,BODY_Y=-50,R_SHOU=-67,HEAD_P=-27,R_ELBO=0,L_ELBO=0,HEAD_Y=-37,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    elif event == 'speak_5':
        d = rt.say_text(text_5)
        servo_map = dict(HEAD_R=0,BODY_Y=0,R_SHOU=-67,HEAD_P=0,R_ELBO=0,L_ELBO=0,HEAD_Y=0,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    elif event == 'speak_6':
        d = rt.say_text(text_6)
        servo_map = dict(HEAD_R=0,BODY_Y=0,R_SHOU=90,HEAD_P=0,R_ELBO=0,L_ELBO=0,HEAD_Y=0,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    elif event == 'speak_7':
        d = rt.say_text(text_7)
        servo_map = dict(HEAD_R=0,BODY_Y=-50,R_SHOU=90,HEAD_P=-27,R_ELBO=0,L_ELBO=0,HEAD_Y=-37,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    elif event == 'speak_8':
        d = rt.say_text(text_8)
        servo_map = dict(HEAD_R=0,BODY_Y=0,R_SHOU=90,HEAD_P=0,R_ELBO=0,L_ELBO=0,HEAD_Y=0,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    elif event == 'speak_9':
        d = rt.say_text(text_9)
        servo_map = dict(HEAD_R=0,BODY_Y=0,R_SHOU=90,HEAD_P=0,R_ELBO=0,L_ELBO=0,HEAD_Y=0,L_SHOU=-90)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)
    

    elif event == 'speak_free':
        d = rt.say_text(values['free_speech_field'])
        rt.play_motion(m)
    elif event == 'idle':
        rt.play_idle_motion()
    elif event == 'stop':
        rt.stop_idle_motion()
    elif event == 'reset':
        servo_map = dict(HEAD_R=0, HEAD_P=-5, HEAD_Y=0, BODY_Y=0, 
                         L_SHOU=-90, L_ELBO=0, R_SHOU=90, R_ELBO=0)
        pose = dict(Msec=500, ServoMap=servo_map)
        rt.play_pose(pose)
    else:
        pass

window.close()