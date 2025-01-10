import pyxel
import time
import json
from player import Player
from enemy import Enemy
from bullet import Bullet

# JSONファイルを読み込む
with open("config.json", "r") as f:
    config = json.load(f)

# ゲームの初期設定
SCREEN_WIDTH = config["screen"]["width"]["value"]
SCREEN_HEIGHT = config["screen"]["height"]["value"]
SCREEN_DIDPLAYSCALE = config["screen"]["display_scale"]["value"]
SCREEN_FPS = config["screen"]["fps"]["value"]

MAP_WIDTH = config["map"]["width"]["value"]
MAP_HEIGHT = config["map"]["height"]["value"]

PLAYER_RADIUS = config["player"]["radius"]["value"]
PLAYER_HP = config["player"]["hp"]["value"]

ENEMY_RADIUS = config["enemy"]["radius"]["value"]
ENEMY_SPEED = config["enemy"]["speed"]["value"]
ENEMY_DAMAGE = config["enemy"]["damage"]["value"]
ENEMY_HP = config["enemy"]["hp"]["value"]
ENEMY_SPAWN_INTERVAL_RANGE = config["enemy"]["spawn_interval_range"]["value"]  # [s]

BULLET_RADIUS = config["bullet"]["radius"]["value"]
BULLET_SPEED = config["bullet"]["speed"]["value"]
BULLET_DAMAGE = config["bullet"]["damage"]["value"]
BULLET_FIRE_RATE = config["bullet"]["fire_rate"]["value"]  # [s]
BULLET_FIRE_DIFFUSION = config["bullet"]["fire_diffusion"]["value"]  # [°]
BULLET_FIRE_RANGE = config["bullet"]["fire_range"]["value"]

MACHINE_GUN_RADIUS = config["machine_gun"]["radius"]["value"]
MACHINE_GUN_SPEED = config["machine_gun"]["speed"]["value"]
MACHINE_GUN_DAMAGE = config["machine_gun"]["damage"]["value"]
MACHINE_GUN_FIRE_RATE = config["machine_gun"]["fire_rate"]["value"]  # [s]
MACHINE_GUN_FIRE_DIFFUSION = config["machine_gun"]["fire_diffusion"]["value"]  # [°]
MACHINE_GUN_FIRE_RANGE = config["machine_gun"]["fire_range"]["value"]

CANNON_RADIUS = config["cannon"]["radius"]["value"]
CANNON_SPEED = config["cannon"]["speed"]["value"]
CANNON_DAMAGE = config["cannon"]["damage"]["value"]
CANNON_FIRE_RATE = config["cannon"]["fire_rate"]["value"]  # [s]
CANNON_FIRE_DIFFUSION = config["cannon"]["fire_diffusion"]["value"]  # [°]
CANNON_FIRE_RANGE = config["cannon"]["fire_range"]["value"]


# メインゲームクラス
class App:
    def __init__(self):
        pyxel.init(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            display_scale=SCREEN_DIDPLAYSCALE,
            fps=SCREEN_FPS,
        )
        self.screen_x = MAP_WIDTH // 2
        self.screen_y = MAP_HEIGHT // 2
        self.random_create = 0
        self.players = []
        self.players.append(
            Player(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 - 100,
                PLAYER_RADIUS,
                PLAYER_HP,
                BULLET_FIRE_RATE,
                BULLET_RADIUS,
                BULLET_SPEED,
                BULLET_FIRE_DIFFUSION,
                BULLET_FIRE_RANGE,
                BULLET_DAMAGE,
            )
        )
        self.players.append(
            Player(
                SCREEN_WIDTH // 2 + PLAYER_RADIUS * 2 - 200,
                SCREEN_HEIGHT // 2 + 200,
                PLAYER_RADIUS,
                PLAYER_HP,
                MACHINE_GUN_FIRE_RATE,
                MACHINE_GUN_RADIUS,
                MACHINE_GUN_SPEED,
                MACHINE_GUN_FIRE_DIFFUSION,
                MACHINE_GUN_FIRE_RANGE,
                MACHINE_GUN_DAMAGE,
            )
        )
        self.players.append(
            Player(
                SCREEN_WIDTH // 2 - PLAYER_RADIUS * 2 + 200,
                SCREEN_HEIGHT // 2 + 200,
                PLAYER_RADIUS,
                PLAYER_HP,
                CANNON_FIRE_RATE,
                CANNON_RADIUS,
                CANNON_SPEED,
                CANNON_FIRE_DIFFUSION,
                CANNON_FIRE_RANGE,
                CANNON_DAMAGE,
            )
        )

        self.bullets = []
        self.enemies = []
        self.start_time = time.time()

        pyxel.run(self.update, self.draw)

    def update(self):

        for player in self.players:
            # プレイヤーの更新
            player.update(self.bullets, self.enemies)
        # 非アクティブなプレイヤーを削除
        self.players = [player for player in self.players if player.active]

        # 敵の発生
        end_time = time.time()  # 現在時刻（処理完了後）を取得
        etime = end_time - self.start_time

        if (etime >= self.random_create) or (len(self.enemies) <= 1):
            spawn_frame = pyxel.rndi(0, 3)
            if spawn_frame == 0:
                spawan_x = 0
                spawan_y = pyxel.rndi(0, SCREEN_HEIGHT)
            elif spawn_frame == 1:
                spawan_x = pyxel.rndi(0, SCREEN_WIDTH)
                spawan_y = 0
            elif spawn_frame == 2:
                spawan_x = SCREEN_WIDTH
                spawan_y = pyxel.rndi(0, SCREEN_HEIGHT)
            elif spawn_frame == 3:
                spawan_x = pyxel.rndi(0, SCREEN_WIDTH)
                spawan_y = SCREEN_HEIGHT

            randomy = pyxel.rndi(0, SCREEN_HEIGHT)
            self.enemies.append(
                Enemy(
                    spawan_x,
                    spawan_y,
                    ENEMY_RADIUS,
                    ENEMY_SPEED,
                    ENEMY_HP,
                    ENEMY_DAMAGE,
                )
            )
            self.random_create = pyxel.rndi(0, ENEMY_SPAWN_INTERVAL_RANGE)
            self.start_time = time.time()
        # 敵の更新
        for enemy in self.enemies:
            enemy.update(self.players)

        # 非アクティブな敵を削除
        self.enemies = [enemy for enemy in self.enemies if enemy.active]

        # 弾の更新
        for bullet in self.bullets:
            bullet.update(self.enemies)

        # 非アクティブな弾を削除
        self.bullets = [bullet for bullet in self.bullets if bullet.active]

    def draw(self):
        # 画面のクリア
        pyxel.cls(0)
        for player in self.players:
            pyxel.rectb(
                player.x - player.radius,
                player.y - player.radius,
                player.radius * 2,
                player.radius * 2,
                7,
            )
            # プレイヤーの描画
            player.draw(self.enemies)

        # 弾の描画
        for enemy in self.enemies:
            enemy.draw(self.players)

        # 弾の描画
        for bullet in self.bullets:
            bullet.draw()


# ゲームの実行
App()
