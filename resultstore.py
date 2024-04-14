import const, logging

class ResultStore():
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self._easyResultFile = "easyBestScores.log"
        self._normalResultFile = "normalBestScores.log"
        self._hardResultFile = "hardBestScores.log"
    
    def readEasyResultFile(self):
        try:
            f = open(self._easyResultFile, 'r', encoding='UTF-8')
            datalist = f.readlines()
            f.close()
            return datalist
        except Exception as e:
            logging.error(f"{self._easyResultFile}の読み込みでエラー発生")
            logging.error(f"{e}")
            return []
    
    def readNormalResultFile(self):
        try:
            f = open(self._normalResultFile, 'r', encoding='UTF-8')
            datalist = f.readlines()
            f.close()
            return datalist
        except Exception as e:
            logging.error(f"{self._normalResultFile}の読み込みでエラー発生")
            logging.error(f"{e}")
            return []
    
    def readHardResultFile(self):
        try:
            f = open(self._hardResultFile, 'r', encoding='UTF-8')
            datalist = f.readlines()
            f.close()
            return datalist
        except Exception as e:
            logging.error(f"{self._hardResultFile}の読み込みでエラー発生")
            logging.error(f"{e}")
            return []
    
    def readResultFile(self, level):
        if level == const.Constants.get_instance().EASY:
            return self.readEasyResultFile()
        if level == const.Constants.get_instance().NORMAL:
            return self.readNormalResultFile()
        if level == const.Constants.get_instance().HARD:
            return self.readHardResultFile()

    def appendToEasyResultFile(self, distance):
        datalist = self.readEasyResultFile()
        datalist_int = []
        for data in datalist:
            datalist_int.append(int(data))
        datalist_int.append(distance)
        sorteddatalist = sorted(datalist_int)
        sliceddatalist = sorteddatalist
        if len(sorteddatalist) > 5:
            sliceddatalist = sorteddatalist[:5]

        try:
            f = open(self._easyResultFile, 'w', encoding='UTF-8')
            for data in sliceddatalist:
                f.write(str(data))
                f.write("\n")
            f.close()
        except Exception as e:
            logging.error(f"{self._easyResultFile}への書き込みでエラー発生")
            logging.error(f"{e}")
    
    def appendToNoramlResultFile(self, distance):
        datalist = self.readNormalResultFile()
        datalist_int = []
        for data in datalist:
            datalist_int.append(int(data))
        datalist_int.append(distance)
        sorteddatalist = sorted(datalist_int)
        sliceddatalist = sorteddatalist
        if len(sorteddatalist) > 5:
            sliceddatalist = sorteddatalist[:5]

        try:
            f = open(self._normalResultFile, 'w', encoding='UTF-8')
            for data in sliceddatalist:
                f.write(str(data))
                f.write("\n")
            f.close()
        except Exception as e:
            logging.error(f"{self._normalResultFile}への書き込みでエラー発生")
            logging.error(f"{e}")
    
    def appendToHardResultFile(self, distance):
        datalist = self.readHardResultFile()
        datalist_int = []
        for data in datalist:
            datalist_int.append(int(data))
        datalist_int.append(distance)
        sorteddatalist = sorted(datalist_int)
        sliceddatalist = sorteddatalist
        if len(sorteddatalist) > 5:
            sliceddatalist = sorteddatalist[:5]

        try:
            f = open(self._hardResultFile, 'w', encoding='UTF-8')
            for data in sliceddatalist:
                f.write(str(data))
                f.write("\n")
            f.close()
        except Exception as e:
            logging.error(f"{self._hardResultFile}への書き込みでエラー発生")
            logging.error(f"{e}")
    
    def appendToResultFile(self, level, distance):
        if level == const.Constants.get_instance().EASY:
            self.appendToEasyResultFile(distance)
            return
        if level == const.Constants.get_instance().NORMAL:
            self.appendToNoramlResultFile(distance)
            return
        if level == const.Constants.get_instance().HARD:
            self.appendToHardResultFile(distance)
            return