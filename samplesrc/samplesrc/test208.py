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

    #プロパティ：値を入れる
    @battery.setter 
    def battery(self, value):
        if 0 <= value <= 100:
            self._battery = value
        else:
            print("注意: batteryの値は、0〜100にしてください。")
            
    # メソッド：どんな処理をするのか？
    def show_info(self):
        print(f"私は「{self._name}」です。仕事は{self._job}で、充電残量は{self._battery}です。")

    def do_work(self):
        self._battery -= 10
        print(f"{self._name}は、お手伝いをしました。充電残量は{self._battery}です。")

class CookingRobot(Robot): #【お料理ロボ：お手伝いロボを継承】
    def __init__(self, name, battery):
        super().__init__(name, battery)
        self._job = "お料理"
        
    def do_work(self): # 仕事をする
        self._battery -= 20
        print(f"{self._name}は、昼食を作りました。充電残量は{self._battery}です。")

class CleaningRobot(Robot): #【お掃除ロボ：お手伝いロボを継承】
    def __init__(self, name, battery):
        super().__init__(name, battery)
        self._job = "お掃除"

    def do_work(self): # 仕事をする
        self._battery -= 30
        print(f"{self._name}は、庭の掃除をしました。充電残量は{self._battery}です。")

robots = []
robots.append(Robot("ココア", 100))
robots.append(Robot("ラテ", 80))
robots.append(CookingRobot("シェフィ", 100))
robots.append(CleaningRobot("スウィーピー", 100))

for robot in robots:
    robot.show_info()
print("【仕事を命令】")
for robot in robots:
    robot.do_work()