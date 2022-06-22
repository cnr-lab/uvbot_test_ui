import can
import os
import time

class UvbotCanInterface:
    def __init__(self,can_device):
        self.can_device = can_device
        self.can_bus = can.interface.Bus(self.can_device, bustype="socketcan")

    def sendCan(self,id,data):
        message = can.Message(arbitration_id=id, data=data)
        self.can_bus.send(message)
        
    def recvCan(self):
        data = self.can_bus.recv()
        return data.arbitration_id, data.data

    def flush(self):
        self.can_bus.flush_tx_buffer()

class UvbotDebugUI:
    def __init__(self,can_interface,significant_figures=100):
        self.can_interface = can_interface
        self.ultrasound = [0,0,0,0,0,0]
        self.floor = [0,0,0,0]
        self.pir = [0,0,0,0,0,0]
        self.touch = 0
        self.battery = 0
        self.charge = "알수없음"
        self.imu = [0,0,0,0] # Roll Pitch Yaw angularZ
        self.enc = [0,0] # Right Left
        self.current = [0,0]
        self.significant_figures = 100
        
        self.uv = 0
        self.air = 0
        self.rgb = 0
        
        self.count = 0

        self.jetson_state  = "OFF"  # ON, OFF
        self.camera_state  = "OFF"  # ON, OFF
        self.lidar_state  = "OFF"  # ON, OFF
        self.ir_state  = "알수없음"  # 0 : Robot_Standby, 1 : Finish_docking
    
    def parse(self): 
        if self.count >= 1000:
            id,data = self.can_interface.recvCan()
        else: 
            self.count = self.count+1
            return False   
        if id == 2002:
            for i in range(6):
                self.ultrasound[i] = data[i]
            self.floor[3] = (data[7]&128) >> 7
            self.floor[2] = (data[7]&64) >> 6
            self.floor[1] = (data[7]&32) >> 5
            self.floor[0] = (data[7]&16) >> 4
            return True 
            
        elif id == 2003:
            self.imu[0] = (data[0]|data[1]<<8)/self.significant_figures
            self.imu[1] = (data[2]|data[3]<<8)/self.significant_figures
            self.imu[2] = (data[4]|data[5]<<8)/self.significant_figures
            self.imu[3] = (data[6]|data[7]<<8)/self.significant_figures
            return True 

        elif id == 12105473:
            if data[0]  == 216:
                self.enc[0] = (data[5] | (data[6]<<8))
                self.enc[1] = (data[2] | (data[3]<<8))
                for i in range(2):
                    if not self.enc[i]&0b1000000 == 0:
                        self.enc[i] =self.enc[i] - 65534
                self.enc[0] = -1 * self.enc[0]    
            elif data[0] == 193:
                self.current[0] == (data[4] | (data[5]<<8))
            elif data[0] == 200:
                self.current[1] == (data[4] | (data[5]<<8))
            return True 
            
        elif id == 3001:
            self.pir[5] = (data[7]&128) >> 7
            self.pir[4] = (data[7]&64) >> 6
            self.pir[3] = (data[7]&32) >> 5
            self.pir[2] = (data[7]&16) >> 4
            self.pir[1] = (data[7]&8) >> 3
            self.pir[0] = (data[7]&4) >> 2
            self.touch = (data[6]&128) >> 7
            return True 
            
        elif id == 4001:
            self.battery = data[7]
            charge_can_msg = data[5]
            if charge_can_msg == 128:
                self.charge = "충전완료"
            elif charge_can_msg == 64:
                self.charge = "충전중"
            elif charge_can_msg== 32:
                self.charge = "충전기분리"

        elif id == 6003:
            if data[7] == 1:
                self.jetson_state  = "ON"  # ON, OFF
            elif data[7] == 0:
                self.jetson_state = "OFF"
            if data[6] == 1:
                self.lidar_state = "ON"
            elif data[6] == 0:
                self.lidar_state = "OFF"
            if data[5] == 1:
                self.camera_state = "ON"
            elif data[5] == 0:
                self.camera_state = "OFF"
            if data[4] == 1:
                self.ir_state = "Finish_docking"
            elif data[4] == 0:
                self.ir_state = "Robot_Standby"

        else:
            return False
                
    def sendJoy(self,direction="stop"):
        ID = 1001
        if direction == "stop":
            packit = [0,0,0,0,1,0,0,1]
        elif direction == "front":
            packit = [10,0,0,0,1,0,0,0]
        elif direction == "back":
            packit = [246,255,0,0,1,0,0,0]
        elif direction == "right":
            packit = [0,0,226,255,1,0,0,0]
        elif direction == "left":
            packit = [0,0,30,0,1,0,0,0]
        else:
            packit = [0,0,0,0,1,0,0,1]
        self.can_interface.sendCan(ID,packit)
        
    def sendLED(self,rgb="off"):
        packit5 = (0|(self.air<<7)|(self.uv<<6))
        if rgb == "red":
            self.rgb = 11
            packit = [0,0,0,40,0,packit5,0,self.rgb]
        elif rgb == "blue":
            self.rgb = 10
            packit = [0,0,0,40,0,packit5,0,self.rgb]
        elif rgb == "green":
            self.rgb = 12
            packit = [0,0,0,40,0,packit5,0,self.rgb]
        else:
            self.rgb = 0
            packit = [0,0,0,40,0,packit5,0,self.rgb]
        self.can_interface.sendCan(1002,packit)
        
    def sendUV(self,state):
        self.uv = state
        packit5 = (0|(self.air<<7)|(self.uv<<6))
        packit = [0,0,0,40,0,packit5,0,self.rgb]
        self.can_interface.sendCan(1002,packit)
        
    def sendAir(self,state):
        self.air = state
        packit5 = (0|(self.air<<7)|(self.uv<<6))
        packit = [0,0,0,40,0,packit5,0,self.rgb]
        self.can_interface.sendCan(1002,packit)
    
    def sendTTS(self):
        packit5 = (0|(self.air<<7)|(self.uv<<6))
        packit = [0,0,0,40,0,packit5,1,self.rgb]
        self.can_interface.sendCan(1002,packit)
        
    def startRobot(self):
        packit = [0,0,0,0,0,0,0,1]
        self.can_interface.sendCan(6001,packit)

    def sendRockJetson(self):
        self.can_interface.flush()
        packit = [0,0,0,0,0,0,0,0]
        self.can_interface.sendCan(6002,packit)
        
    def setMotorDriver(self):
        os.system("./script/md_motor_setting.sh")



if __name__ == "__main__":
    can0 = UvbotCanInterface("can0")
    ui = UvbotDebugUI(can0)
    
    ui.can_interface.recvCan()


