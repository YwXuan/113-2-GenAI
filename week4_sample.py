# -*- coding: utf-8 -*-
"""week4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ybK6Uo3VgClehBIywq78LsDZGi8c6TtQ
"""

import time

def start_game():
    print("你身處一個黑暗的森林中，周圍寂靜無聲。")
    print("你看到前方有兩條路：左邊和右邊。")
    choose_path()

def choose_path():
    choice = input("你要選擇哪條路？（左/右）")
    if choice == "左":
        left_path()
    elif choice == "右":
        right_path()
    else:
        print("請輸入「左」或「右」。")
        choose_path()

def left_path():
    print("你沿著左邊的路走，突然聽到一陣奇怪的聲音。")
    print("你發現一個破舊的小屋，裡面傳來微弱的光。")
    choice = input("你要進去小屋嗎？（是/否）")
    if choice == "是":
        enter_house()
    elif choice == "否":
        print("你決定繼續往前走，但很快就迷失了方向。")
        time.sleep(2)
        print("遊戲結束，你失敗了。")
    else:
        print("請輸入「是」或「否」。")
        left_path()

def right_path():
    print("你沿著右邊的路走，遇到一條湍急的河流。")
    print("你看到一座搖搖晃晃的橋，似乎隨時都會斷裂。")
    choice = input("你要過橋嗎？（是/否）")
    if choice == "是":
        cross_bridge()
    elif choice == "否":
        print("你決定繞道而行，但天色漸漸暗了下來。")
        time.sleep(2)
        print("遊戲結束，你失敗了。")
    else:
        print("請輸入「是」或「否」。")
        right_path()

def enter_house():
    print("你走進小屋，發現裡面住著一位老巫婆。")
    print("她告訴你，森林深處藏著寶藏，但必須通過重重考驗。")
    print("老巫婆給你一個謎語：『什麼東西越大，反而越輕？』")
    answer = input("你的答案是什麼？")
    if answer in ["泡泡", "氣球", "羽毛", "雲", "影子", "夢想", "希望", "笑容", "空氣"]:
       print ("老巫婆點點頭，並給你一把鑰匙")
       time.sleep(1)
       print ("你打開了寶箱，裡面裝滿了金幣，你贏得了勝利！")
    else :
      print ("老巫婆搖搖頭，並把你變成一隻青蛙")
      time.sleep(2)
      print("遊戲結束，你失敗了。")

def cross_bridge():
    print("你小心翼翼地走過搖晃的橋，終於到達對岸。")
    print("前方出現一個洞穴，裡面似乎有光芒閃爍。")
    print("你走進洞穴，發現一堆閃閃發光的寶石，你贏得了勝利！")

start_game()