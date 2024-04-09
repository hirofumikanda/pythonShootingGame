#ファクトリーパターン
class Coffee:
    def drink(self):
        print("コーヒーを飲む。")

class Latte:
    def drink(self):
        print("ラテを飲む。")

class Cappuccino:
    def drink(self):
        print("カプチーノを飲む。")

class Barista: #カフェ店員クラス（ファクトリークラス）
    def order(self, type):
        print(f"order: {type}を注文")
        if type == "ラテ":
            print("「ほんのり甘くてまろやかなラテです。どうぞ。」")
            return Latte()
        elif type == "カプチーノ":
            print("「エスプレッソにミルクの絶妙な泡立ちが特徴のカプチーノです。どうぞ。」")
            return Cappuccino()
        else:
            print("「豆の風味が引き立つ、バランスの取れたコーヒーです。どうぞ。」")
            return Coffee()

mirai = Barista() # ファクトリークラスを作る

cup = mirai.order("コーヒー")
cup.drink()
cup = mirai.order("カプチーノ")
cup.drink()
cup = mirai.order("ラテ")
cup.drink()
