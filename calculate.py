import pyxel  # Pyxelをインポート


def distance(x1, y1, x2, y2, hw=False):
    w = x1 - x2
    h = y1 - y2
    d = pyxel.sqrt((w * w) + (h * h))
    if hw == True:
        return d, h, w
    else:
        return d
