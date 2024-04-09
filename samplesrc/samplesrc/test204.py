class Robot: #【お手伝いロボ】
    def __init__(self, name, battery):
        # どんなデータを持つのか？
        self._job = "お手伝い"
        self._name = name
        self._battery = battery

    # プロパティ：値を返すのみ
    @property
    def job(self):
        return self._job
    @property
    def name(self):
        return self._name
    @property
    def battery(self):
        return self._battery

    # メソッド：どんな処理をするのか？
    def show_info(self):
        print(f"私は「{self._name}」です。仕事は{self._job}で、充電残量は{self._battery}です。")

robot1 = Robot("ココア", 100) # Robot1を作る
robot2 = Robot("ラテ", 80)    # Robot2を作る
robot1.battery = 10000 # おなかを開けて危険に変更!
robot1.show_info()
robot2.show_info()