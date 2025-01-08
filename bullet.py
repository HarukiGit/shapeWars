import pyxel  # Pyxelをインポート
import calculate


# 弾クラス
class Bullet:
    def __init__(
        self, x, y, radius, speed, fire_diffusion, fire_range, damage, enemies
    ):
        self.x = x
        self.y = y
        self.x_init = x
        self.y_init = y
        self.radius = radius
        self.speed = speed
        self.damage = damage
        self.fire_diffusion = pyxel.rndf(-fire_diffusion, fire_diffusion)
        self.fire_range = fire_range
        self.active = True

        enemies_distance = []
        for index, enemy in enumerate(enemies):
            distance = calculate.distance(self.x, self.y, enemy.x, enemy.y)
            enemies_distance.append(distance)
        min_distance_index = enemies_distance.index(min(enemies_distance))
        w = self.x - enemies[min_distance_index].x
        h = self.y - enemies[min_distance_index].y
        self.angle = pyxel.atan2(h, w) + self.fire_diffusion

    def update(self, enemies):
        # 弾の移動
        self.x += self.speed * pyxel.cos(self.angle) * -1
        self.y += self.speed * pyxel.sin(self.angle) * -1

        # 被弾処理
        # 敵と弾の距離よりそれぞれの当たり判定円の半径の和が大きければ被弾
        for enemy in enemies:
            d = calculate.distance(self.x, self.y, enemy.x, enemy.y)
            if d < self.radius + enemy.radius:
                enemy.hp -= self.damage
                self.active = False

        # 画面外に出たら非アクティブに
        if (
            calculate.distance(self.x, self.y, self.x_init, self.y_init)
            > self.fire_range
        ):
            self.active = False

    def draw(self):
        # 弾の描画（円）
        pyxel.circ(self.x, self.y, self.radius, 7)
