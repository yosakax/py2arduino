#coding: utf-8
"""
Lチカのテスト
"""
import time
from pyfirmata2 import Arduino
from py2arduino import set_pin

def main():
    # 操作するArduinoを決定
    board = Arduino(Arduino.AUTODETECT)
    # digital_8をデジタルピンのoutputに設定
    digital_8 = set_pin(board, pin=8, mode="output", data="digital")
    # time.sleep(2)
    while True:
        # LEDを点灯
        digital_8.high()
        time.sleep(0.5)
        # LEDを消灯
        digital_8.low()
        time.sleep(0.5)

if __name__ == "__main__":
    main()