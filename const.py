class Constants:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    '''
    難易度コード
    '''
    @property
    def EASY(self):
        return 0
    @property
    def NORMAL(self):
        return 1
    @property
    def HARD(self):
        return 2

    '''
    敵キャラ出現間隔
    '''
    @property
    def ENEMYINTERVAL_EASY(self):
        return 30
    @property
    def ENEMYINTERVAL_NORMAL(self):
        return 15
    @property
    def ENEMYINTERVAL_HARD(self):
        return 5
    def ENEMYINTERVAl(self, level):
        if level == self.EASY:
            return self.ENEMYINTERVAL_EASY
        if level == self.NORMAL:
            return self.ENEMYINTERVAL_NORMAL
        if level == self.HARD:
            return self.ENEMYINTERVAL_HARD
    
    '''
    敵キャラ出現比率
    '''
    @property
    def ENEMYTYPE_EASY(self):
        return {'normal': 4, 'flame': 1, 'ice': 1}
    @property
    def ENEMYTYPE_NORMAL(self):
        return {'flame': 2, 'ice': 2, 'strongflame': 1}
    @property
    def ENEMYTYPE_HARD(self):
        return {'flame': 1, 'ice': 1, 'strongflame': 2, 'dragon': 2}
    def ENEMYTYPE(self, level):
        if level == self.EASY:
            return self.ENEMYTYPE_EASY
        if level == self.NORMAL:
            return self.ENEMYTYPE_NORMAL
        if level == self.HARD:
            return self.ENEMYTYPE_HARD
    
    '''
    アイテム出現間隔
    '''
    @property
    def ITEMINTERVAL_EASY(self):
        return 150
    @property
    def ITEMINTERVAL_NORMAL(self):
        return 200
    @property
    def ITEMINTERVAL_HARD(self):
        return 300
    def ITEMINTERVAL(self, level):
        if level == self.EASY:
            return self.ITEMINTERVAL_EASY
        if level == self.NORMAL:
            return self.ITEMINTERVAL_NORMAL
        if level == self.HARD:
            return self.ITEMINTERVAL_HARD
    
    '''
    クリア条件（撃墜数）
    '''
    @property
    def CLEARNUMBER_EASY(self):
        return 30
    @property
    def CLEARNUMBER_NORMAL(self):
        return 30
    @property
    def CLEARNUMBER_HARD(self):
        return 30
    def CLEARNUMBER(self, level):
        if level == self.EASY:
            return self.CLEARNUMBER_EASY
        if level == self.NORMAL:
            return self.CLEARNUMBER_NORMAL
        if level == self.HARD:
            return self.CLEARNUMBER_HARD