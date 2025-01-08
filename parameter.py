import json

# JSONファイルを読み込む
with open("config.json", "r") as f:
    config = json.load(f)

# ゲームの初期設定
SCREEN_WIDTH = config["screen"]["width"]["value"]
SCREEN_HEIGHT = config["screen"]["height"]["value"]
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
