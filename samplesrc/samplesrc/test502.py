#ステートパターン
class State: # 【状態の基本形】
    def say(self, text):
        pass

class GirlState(State): # 【少女役の状態】
    def say(self, text):
        print(f"「わぁ、{text}だね！」")
        
class WitchState(State): # 【魔女役の状態】
    def say(self, text):
        print(f"「ふふふ。{text}じゃないか。」")

class GrandmotherState(State): # 【老婆役の状態】
    def say(self, text):
        print(f"「ほんに、{text}じゃのぉ。」")

class VoiceActress(): #【声優】
    def __init__(self):
        self._state = GirlState()

    def roleplaying(self, chara):
        print(f"Stateの変更: あなたの役は{chara}です。")
        if chara == "少女":
            self._state = GirlState()
        if chara == "魔女":
            self._state = WitchState()
        if chara == "老婆":
            self._state = GrandmotherState()

    def say(self, text):
        self._state.say(text)

mirai = VoiceActress() # 声優を作る

mirai.roleplaying("少女")
mirai.say("今日はいい天気")
mirai.roleplaying("魔女")
mirai.say("今日はいい天気")
mirai.roleplaying("老婆")
mirai.say("今日はいい天気")