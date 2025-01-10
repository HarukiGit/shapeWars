import pyxel  # Pyxelをインポート
import time
from bullet import Bullet
import calculate


# プレイヤークラス
class Player:
    def __init__(
        self,
        x,
        y,
        radius,
        hp,
        b_fire_rate,
        b_radius,
        b_speed,
        b_fire_diffusion,
        b_fire_range,
        b_fire_damage,
    ):
        self.x = x  # プレイヤーの初期X座標
        self.y = y  # プレイヤーの初期Y座標
        self.radius = radius
        self.hp = hp
        self.hp_init = hp
        self.rate_start_time = time.time()

        self.b_fire_rate = b_fire_rate
        self.b_radius = b_radius
        self.b_speed = b_speed
        self.b_fire_diffusion = b_fire_diffusion
        self.b_fire_range = b_fire_range
        self.b_fire_damage = b_fire_damage

        self.active = True

    def update(self, bullets, enemies):
        self.rate_end_time = time.time()
        self.rate_time = self.rate_end_time - self.rate_start_time
        # 弾を発射
        if len(enemies) != 0:
            if self.rate_time > self.b_fire_rate:
                bullets.append(
                    Bullet(
                        self.x,
                        self.y,
                        self.b_radius,
                        self.b_speed,
                        self.b_fire_diffusion,
                        self.b_fire_range,
                        self.b_fire_damage,
                        enemies,
                    )
                )
                self.rate_start_time = time.time()
        if self.hp <= 0:
            # print("GAME ORVER")
            self.active = False

    def draw(self, enemies):
        # プレイヤーの描画（円）
        pyxel.circ(self.x, self.y, self.radius, 11)
        pyxel.rect(
            self.x - self.radius,
            self.y + self.radius + 10,
            self.radius * 2 * (self.hp / self.hp_init),
            5,
            8,
        )

        enemies_distance = []
        for index, enemy in enumerate(enemies):
            distance = calculate.distance(self.x, self.y, enemy.x, enemy.y)
            enemies_distance.append(distance)
        self.min_distance_index = enemies_distance.index(min(enemies_distance))
        pyxel.line(
            enemies[self.min_distance_index].x,
            enemies[self.min_distance_index].y,
            self.x,
            self.y,
            4,
        )
