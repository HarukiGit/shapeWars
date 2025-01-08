import pyxel  # Pyxelをインポート


# プレイヤークラス
class Player:
    def __init__(self, x, y, radius, hp):
        self.x = x  # プレイヤーの初期X座標
        self.y = y  # プレイヤーの初期Y座標
        self.radius = radius
        self.hp = hp

    def update(self):
        if self.hp < 0:
            print("GAME ORVER")

    def draw(self):
        # プレイヤーの描画（円）
        pyxel.circ(self.x, self.y, self.radius, 11)
