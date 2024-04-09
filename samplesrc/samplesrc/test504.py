#オブザーバーパターン
class Subject: # 配信者の基本形
    def __init__(self):
        self._observers = []
        
    def attach(self, observer): # 登録する
        self._observers.append(observer)

    def notify(self, data): # 通知する
        for observer in self._observers:
            observer.update(data)

class Publisher(Subject): # 配信するクラス
    def publish(self, data, text):
        print(f"配信者:{text}")
        self.notify(data)

class Observer: # 受信者の基本系
    def update(self, data):
        pass

class Follower(Observer): #受信するクラス
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print(f"{self._name}:通知が来た。{data}を見よう！")

p1 = Publisher() # 送信者を作る
f1 = Follower("受信者1") # 受信者を作って登録
p1.attach(f1)
f2 = Follower("受信者2") # 受信者を作って登録
p1.attach(f2)
p1.publish("動画001", "配信したよ〜。") # メッセージ送信
