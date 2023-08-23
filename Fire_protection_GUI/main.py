# This Python file uses the following encoding: utf-8
import sys
import serial, time
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_Widget


class SerialFrame:
    def __init__(self, start, id, payload):
        self.start = start
        self.id = id
        self.payload = payload
        self.crc = self.calculate_crc()

    def to_bytes(self):
        return bytes([self.start >> 8, self.start & 0xFF, self.id, self.payload, self.crc])


    def calculate_crc(self):
        data = [self.start >> 8, self.start & 0xFF, self.id, self.payload]
        crc = 0
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ 0x07
                else:
                    crc <<= 1
        return crc & 0xFF

def send_frame(serial_port, frame):
    serial_port.write(frame.to_bytes())
    print(f"Sent: {frame.to_bytes().hex()}")


class MainWindow(QMainWindow):
    mcu_connected = 0
    Serial_Obj = serial.Serial()  # serial handler
    Serial_Obj.baudrate = 115200
    Serial_Obj.bytesize = 8
    Serial_Obj.parity = 'N'
    Serial_Obj.stopbits = 1

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        for i in range(19):
            self.ui.port_box.addItem("COM" + str(i))

        self.ui.connect_button.clicked.connect(self.connect_mcu)

        self.ui.pushButton_ping.clicked.connect(self.test_ping)
        self.ui.pushButton_rel_on.clicked.connect(self.test_rel_on)
        self.ui.pushButton_rel_off.clicked.connect(self.test_rel_off)
        self.ui.pushButton_alm_on.clicked.connect(self.test_alm_on)
        self.ui.pushButton_alm_off.clicked.connect(self.test_alm_off)
        self.ui.pushButton_wifi_conn.clicked.connect(self.test_wifi_conn)
    def connect_mcu(self):
        if self.mcu_connected == 0:
            self.Serial_Obj.port = self.ui.port_box.currentText()
            self.Serial_Obj.close()
            try:
                self.Serial_Obj.open()
            except:
                self.ui.status_label.setText("Nieudana próba połączenia z portem: " + self.Serial_Obj.port)
                self.mcu_connected = 0
            else:
                self.ui.status_label.setText("Połączono z portem: " + self.Serial_Obj.port)
                self.mcu_connected = 1

        else:
            self.Serial_Obj.close()
            self.mcu_connected = 0
            self.ui.status_label.setText("Rozłączono z portem: " + self.Serial_Obj.port)

    def closeEvent(self, event):
        self.Serial_Obj.close()

    def test_ping(self):
        ping_frame = SerialFrame(0x1D1E, 0x00, 0x00)
        send_frame(self.Serial_Obj, ping_frame)

    def test_rel_on(self):
        rel_on_frame = SerialFrame(0x1D1E, 0x01, 0x00)
        send_frame(self.Serial_Obj, rel_on_frame)

    def test_rel_off(self):
        rel_off_frame = SerialFrame(0x1D1E, 0x02, 0x00)
        send_frame(self.Serial_Obj, rel_off_frame)

    def test_alm_on(self):
        alm_on_frame = SerialFrame(0x1D1E, 0x03, 0x00)
        send_frame(self.Serial_Obj, alm_on_frame)

    def test_alm_off(self):
        alm_off_frame = SerialFrame(0x1D1E, 0x04, 0x00)
        send_frame(self.Serial_Obj, alm_off_frame)

    def test_wifi_conn(self):
        wifi_conn_frame = SerialFrame(0x1D1E, 0x05, 0x00)
        send_frame(self.Serial_Obj, wifi_conn_frame)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
