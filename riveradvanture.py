import time

def print_slow(text):
    """讓文字慢慢顯示出來，增加沉浸感"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def start_adventure():
    print_slow("你是一名勇敢的海上冒險家，航行在神秘的急流之中，尋找傳說中的海龍王寶藏！")
    print_slow("但在這片危險的海域，你需要選擇你的航道……")
    choose_path()

def choose_path():
    print_slow("\n前方有三條河道可選：")
    print_slow("1. 左側河道，霧氣瀰漫，傳說有魔法生物在此守護。")
    print_slow("2. 中央河道，海水洶湧，水底似乎藏有巨大陰影……")
    print_slow("3. 右側河道，海盜旗幟隱約可見，可能會有敵人攔截。")
    
    choice = input("選擇你的航道 (1/2/3): ")
    if choice == "1":
        enchanted_path()
    elif choice == "2":
        sea_monster_encounter()
    elif choice == "3":
        pirate_attack()
    else:
        print_slow("無效的選擇，請再試一次！")
        choose_path()

def enchanted_path():
    print_slow("\n你進入了被魔法籠罩的河道，周圍的霧氣中隱約可見閃爍的光點……")
    print_slow("突然，一條發光的銀色美人魚出現在你面前！")
    print_slow("美人魚微笑著對你說：‘回答我的謎語，否則你將無法前行。’")
    solve_riddle()

def solve_riddle():
    riddle = "什麼東西越用越多，但從不減少？"
    print_slow(f"美人魚的謎語：{riddle}")
    answer = input("你的答案是：")
    
    if answer in ["知識", "智慧", "信息"]:
        print_slow("美人魚微笑著點頭：‘聰明的冒險家，你可以通過！’")
        print_slow("你繼續前行，終於來到了海龍王的宮殿……")
        meet_sea_dragon()
    else:
        print_slow("美人魚搖了搖頭，施展魔法讓你的船回到了起點！")
        choose_path()

def sea_monster_encounter():
    print_slow("\n你選擇了中央河道，突然水面劇烈翻滾，一隻巨大的觸手從水中探出！")
    print_slow("這是一隻傳說中的深海巨怪！你該怎麼辦？")
    print_slow("1. 與巨怪戰鬥！")
    print_slow("2. 用魚餌引開它。")
    print_slow("3. 全速後退，換一條路！")
    
    choice = input("選擇你的行動 (1/2/3): ")
    if choice == "1":
        print_slow("你奮力與巨怪戰鬥，但它的力量太強大了……你的船被捲入深海！")
        game_over()
    elif choice == "2":
        print_slow("你迅速拋出魚餌，巨怪被美味的魚群吸引，讓你有機會安全通過！")
        meet_sea_dragon()
    elif choice == "3":
        print_slow("你選擇撤退，回到了起點。")
        choose_path()
    else:
        print_slow("無效選擇，請再試一次！")
        sea_monster_encounter()

def pirate_attack():
    print_slow("\n你選擇了右側河道，卻發現一艘滿是骷髏標誌的海盜船擋在前方！")
    print_slow("海盜首領站在甲板上，揮舞著他的彎刀大笑：‘交出財寶，否則我們就讓你沉入海底！’")
    print_slow("你該怎麼辦？")
    print_slow("1. 與海盜決戰！")
    print_slow("2. 用謊言欺騙他們，說你已經有了更大的寶藏線索。")
    print_slow("3. 直接跳海，試圖逃跑！")
    
    choice = input("選擇你的行動 (1/2/3): ")
    if choice == "1":
        print_slow("你奮力戰鬥，但海盜人數眾多，最終被俘虜！")
        game_over()
    elif choice == "2":
        print_slow("海盜對你的故事深信不疑，他們讓你通過，希望之後能找到更大的寶藏！")
        meet_sea_dragon()
    elif choice == "3":
        print_slow("你勇敢地跳入海中，但很快被洶湧的海浪吞沒……")
        game_over()
    else:
        print_slow("無效選擇，請再試一次！")
        pirate_attack()

def meet_sea_dragon():
    print_slow("\n你來到了海龍王的宮殿，他的雙眼閃爍著神秘的光芒。")
    print_slow("‘勇敢的冒險者，你已經通過了重重考驗。現在回答我的最後一個問題。’")
    print_slow("海龍王問道：‘什麼比金子更珍貴，卻無法用錢買到？’")
    answer = input("你的答案是：")
    if answer in ["時間", "友誼", "生命"]:
        print_slow("海龍王點頭微笑：‘你是個智慧的探險家，這份寶藏屬於你了！’")
        print_slow("你成功獲得傳說中的寶藏，成為史上最偉大的冒險家！")
        print_slow("\n🎉 恭喜你完成冒險！🎉")
    else:
        print_slow("海龍王搖頭：‘你還不夠智慧，請再來挑戰！’")
        game_over()

def game_over():
    print_slow("\n💀 你的冒險結束了……💀")
    replay = input("想再試一次嗎？(y/n): ")
    if replay.lower() == "y":
        start_adventure()
    else:
        print_slow("謝謝遊玩，再見！")

start_adventure()