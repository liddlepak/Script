import os
import time

import pyautogui as pg

PAUSE: int = 2
DELETE_DIGIT: int = 2
CONF_DIGIT: float = 0.9
FILEPATH: str = "/System/Applications/Calculator.app"

os.system('open '+FILEPATH)
time.sleep(PAUSE)

one = pg.locateCenterOnScreen("template/one.png", confidence=CONF_DIGIT)
two = pg.locateCenterOnScreen("template/two.png", confidence=CONF_DIGIT)
plus = pg.locateCenterOnScreen("template/plus.png", confidence=CONF_DIGIT)
seven = pg.locateCenterOnScreen("template/seven.png", confidence=CONF_DIGIT)
equal = pg.locateCenterOnScreen("template/equal.png", confidence=CONF_DIGIT)

values = (one, two, plus, seven, equal)

for value in values:
    x, y = value
    pg.click(x/DELETE_DIGIT, y/DELETE_DIGIT)
