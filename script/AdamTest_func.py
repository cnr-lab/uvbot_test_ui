from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import time

from AdamTest import Ui_MainWindow_TestforAdam
from can_interface import UvbotCanInterface,UvbotDebugUI

class TestAtestWindow(Ui_MainWindow_TestforAdam):
    finished = Signal()
    def __init__(self):
        self.can0 = UvbotCanInterface("can0")
        self.func = UvbotDebugUI(self.can0) 
        self.timer = QTimer()
        self.timer.timeout.connect(self.can)
        
    def can(self):
        self.func.parse()
        self.Receive_data()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.UV_ON.clicked.connect(self.Uv_ON)
        self.UV_OFF.clicked.connect(self.Uv_OFF)

        self.AIR_ON.clicked.connect(self.Air_ON)
        self.AIR_OFF.clicked.connect(self.Air_OFF)

        self.LED_B.clicked.connect(self.Led_B)
        self.LED_R.clicked.connect(self.Led_R)
        self.LED_G.clicked.connect(self.Led_G)
        self.LED_X.clicked.connect(self.Led_X)

        self.Speaker_send.clicked.connect(self.Speaker_SEND)
        self.motor_send.clicked.connect(self.Motor_SEND)
        self.Unlock_send.clicked.connect(self.unlock_send)

        self.up.clicked.connect(self.UP)
        self.left.clicked.connect(self.LEFT)
        self.down.clicked.connect(self.DOWN)
        self.right.clicked.connect(self.RIGHT)
        self.suspend.clicked.connect(self.Suspend)
        self.Receive_data()
        self.timer.start(1)
        


    def Receive_data(self):
        self.ultra_data1.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.ultrasound[0]), None))
        self.ultra_data2.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.ultrasound[1]), None))
        self.ultra_data4.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.ultrasound[2]), None))
        self.ultra_data3.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.ultrasound[3]), None))
        self.ultra_data5.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.ultrasound[4]), None))
        self.ultra_data6.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.ultrasound[5]), None))
        
        self.floor_data1.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.floor[0]), None))
        self.floor_data2.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.floor[1]), None))
        self.floor_data3.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.floor[2]), None))
        self.floor_data4.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.floor[3]), None))

        self.PIR_data_1.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.pir[0]), None))
        self.PIR_data_2.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p align=\"center\"><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.pir[1]), None))
        self.PIR_data_3.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.pir[2]), None))
        self.PIR_data_4.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.pir[3]), None))
        self.PIR_data_5.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.pir[4]), None))
        self.PIR_data_6.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.pir[5]), None))

        self.touch_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.touch), None))

        self.battery_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"{}".format(self.func.battery), None))

        self.charge_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"{}".format(self.func.charge), None))

        self.IMU_Roll_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.imu[0]), None))
        self.IMU_Yaw_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.imu[1]), None))
        self.IMU_Pitch_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.imu[2]), None))
        self.IMU_Z_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.imu[3]), None))

        self.Encoder_Left_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.enc[1]), None))
        self.Encoder_Right_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.enc[0]), None))

        self.Current_Left_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.current[1]), None))
        self.Current_Right_data.setText(QCoreApplication.translate("MainWindow_TestforAdam", u"<html><head/><body><p><span style=\" color:#2e3436;\">{}</span></p></body></html>".format(self.func.current[0]), None))

    #UV BUTTON
    def Uv_ON(self):
        self.func.sendUV(1)
        print("UV_ON")

    def Uv_OFF(self):
        self.func.sendUV(0)
        print("UV_OFF")

    #AIR BUTTON
    def Air_ON(self):
        self.func.sendAir(1)
        print("AIR_ON")
    def Air_OFF(self):
        self.func.sendAir(0)
        print("AIR_OFF")

    #LED BUTTON
    def Led_B(self):
        self.func.sendLED("blue")
        print("LED_BLUE")
    def Led_R(self):
        self.func.sendLED("red")
        print("LED_RED")
    def Led_G(self):
        self.func.sendLED("green")
        print("LED_GREEN")
    def Led_X(self):
        self.func.sendLED("off")
        print("LED_X")

    #SPEAKER BUTTON
    def Speaker_SEND(self):
        self.func.sendTTS()
        print("SPEAKER DATA SEND")

    #MOTOR BUTTON
    def Motor_SEND(self):
        self.func.setMotorDriver()
        print("MOTOR DATA SEND")

    #UNLOCK BUTTON
    def unlock_send(self):
        self.func.startRobot()
        print("UNLOCK DATA SEND")

    #JOYSTICK BUTTON
    def UP(self):
        self.func.sendJoy("front")
        print("JOY UP")

    def LEFT(self):
        self.func.sendJoy("left")
        print("JOY LEFT")

    def DOWN(self):
        self.func.sendJoy("back")
        print("JOY DOWN")

    def RIGHT(self):
        self.func.sendJoy("right")
        print("JOY RIGHT")
        
    def Suspend(self):
        self.func.sendJoy("stop")
        print("JOY STOP")