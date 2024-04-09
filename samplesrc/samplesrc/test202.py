class Robot: #【お手伝いロボ】
    def __init__(self, name, battery):
        # どんなデータを持つのか？
        self.job = "お手伝い"
        self.name = name
        self.battery = battery

    # メソッド：どんな処理をするのか？
    def show_info(self):
        print(f"私は「{self.name}」です。仕事は{self.job}で、充電残量は{self.battery}です。")

robot1 = Robot("ココア", 100) # Robot1を作る
robot2 = Robot("ラテ", 80)    # Robot2を作る
robot1.show_info()
robot2.show_info()
