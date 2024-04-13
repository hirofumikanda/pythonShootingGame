class Constants:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    @property
    def EASY(self):
        return 0
    
    @property
    def NORMAL(self):
        return 1
    
    @property
    def HARD(self):
        return 2