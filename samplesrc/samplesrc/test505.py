#シングルトンパターン
class HotelFront: # ホテルのフロント係
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def checkin(self):
        print("「いらっしゃいませ。デザインパターンホテルへようこそ。」")

    def roomservice(self):
        print("「はい、フロントです。ルームサービスのご注文でしょうか？」")

    def forgotten(self):
        print("「ご連絡ありがとうございます。お名前とお部屋番号をお教えいただけますか？」")

print("フロントでチェックイン")
HotelFront.get_instance().checkin()
print("302号室から内線")
HotelFront.get_instance().roomservice()
print("808号室から内線")
HotelFront.get_instance().roomservice()
print("忘れ物をしたので、外から電話")
HotelFront.get_instance().forgotten()
