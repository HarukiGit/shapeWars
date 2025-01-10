import pyxel  # Pyxelをインポート
import time
import calculate
import PyxelUniversalFont as puf


class Enemy:
    def __init__(self, x, y, radius, speed, hp, damage):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.hp = hp
        self.active = True
        self.damage = damage

    def update(self, players, screen_x, screen_y):
        self.screen_x = screen_x
        self.screen_y = screen_y
        players_distance = []
        for index, player in enumerate(players):
            distance = calculate.distance(self.x, self.y, player.x, player.y)
            players_distance.append(distance)
        self.min_distance_index = players_distance.index(min(players_distance))

        EtoP_distance, h, w = calculate.distance(
            self.x,
            self.y,
            players[self.min_distance_index].x,
            players[self.min_distance_index].y,
            hw=True,
        )
        self.x -= self.speed * (w / EtoP_distance)
        self.y -= self.speed * (h / EtoP_distance)
        if EtoP_distance < players[self.min_distance_index].radius:
            players[self.min_distance_index].hp -= self.damage
            self.active = False

        # 非アクティブ処理
        if self.hp <= 0:
            self.active = False

    def draw(self, players):
        # 弾の描画（円）
        pyxel.circ(self.x - self.screen_x, self.y - self.screen_y, self.radius, 7)
        # フォントを指定
        writer = puf.Writer("misaki_gothic.ttf")
        # draw(x座標, y座標, テキスト, フォントサイズ, 文字の色(16:モザイク))
        # 背景色はデフォルト値(-1:透明)
        writer.draw(
            self.x - self.screen_x - 20 / 2,
            self.y - self.screen_y + 20,
            f"{self.hp}",
            20,
            7,
        )

        """pyxel.line(
            players[self.min_distance_index].x,
            players[self.min_distance_index].y,
            self.x,
            self.y,
            4,
        )"""
