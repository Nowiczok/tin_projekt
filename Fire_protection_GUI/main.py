# This Python file uses the following encoding: utf-8
import sys
import serial
import threading
import time
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

    def receive_frame(self, serial_port, timeout=10):
        start_bytes = bytes([self.start >> 8, self.start & 0xFF])
        received_bytes = bytearray()

        def read_serial():
            nonlocal received_bytes
            while True:
                received_byte = serial_port.read(1)
                if received_byte:
                    received_bytes += received_byte

        serial_thread = threading.Thread(target=read_serial)
        serial_thread.start()

        start_time = time.time()
        while time.time() - start_time < timeout:
            if start_bytes in received_bytes:
                start_index = received_bytes.index(start_bytes)
                if len(received_bytes) >= start_index + 5:  # Minimalna długość ramki
                    received_frame = SerialFrame(
                        (received_bytes[start_index] << 8) | received_bytes[start_index + 1],
                        received_bytes[start_index + 2],
                        received_bytes[start_index + 3]
                    )
                    if received_frame.to_bytes() == received_bytes[start_index:start_index + 5]:
                        serial_thread.join()  # Zakończenie wątku
                        return True  # Ramka odczytana poprawnie

        serial_thread.join()  # Zakończenie wątku
        return False  # Przekroczono czas oczekiwania
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
        def ping_task():
            nonlocal test_result
            test_result = ping_frame.receive_frame(self.Serial_Obj, timeout=1)

        test_result = False
        ping_frame = SerialFrame(0x1D1E, 0x00, 0x00)
        send_frame(self.Serial_Obj, ping_frame)

        ping_thread = threading.Thread(target=ping_task)
        ping_thread.start()
        ping_thread.join(timeout=1)  #wait for thread for 1 sec
        if test_result == True:
            self.ui.ping_status_label.setText("<font color=green>PASS")
        else:
            self.ui.ping_status_label.setText("<font color=red>FAIL")

    def test_rel_on(self):
        rel_on_frame = SerialFrame(0x1D1E, 0x01, 0x00)
        def rel_on_task():
            nonlocal test_result
            test_result = rel_on_frame.receive_frame(self.Serial_Obj, timeout=1)

        test_result = False
        send_frame(self.Serial_Obj, rel_on_frame)

        ping_thread = threading.Thread(target=rel_on_task)
        ping_thread.start()
        ping_thread.join(timeout=1)  #wait for thread for 1 sec
        if test_result == True:
            self.ui.rel_on_status_label.setText("<font color=green>PASS")
        else:
            self.ui.rel_on_status_label.setText("<font color=red>FAIL")


    def test_rel_off(self):
        rel_off_frame = SerialFrame(0x1D1E, 0x02, 0x00)

        def rel_off_task():
            nonlocal test_result
            test_result = rel_off_frame.receive_frame(self.Serial_Obj, timeout=1)

        test_result = False
        send_frame(self.Serial_Obj, rel_off_frame)

        ping_thread = threading.Thread(target=rel_off_task)
        ping_thread.start()
        ping_thread.join(timeout=1)  #wait for thread for 1 sec
        if test_result == True:
            self.ui.rel_off_status_label.setText("<font color=green>PASS")
        else:
            self.ui.rel_off_status_label.setText("<font color=red>FAIL")


    def test_alm_on(self):
        alm_on_frame = SerialFrame(0x1D1E, 0x03, 0x00)


        def alm_on_task():
            nonlocal test_result
            test_result = alm_on_frame.receive_frame(self.Serial_Obj, timeout=1)

        test_result = False
        send_frame(self.Serial_Obj, alm_on_frame)

        ping_thread = threading.Thread(target=alm_on_task)
        ping_thread.start()
        ping_thread.join(timeout=1)  #wait for thread for 1 sec
        if test_result == True:
            self.ui.alm_on_status_label.setText("<font color=green>PASS")
        else:
            self.ui.alm_on_status_label.setText("<font color=red>FAIL")

    def test_alm_off(self):
        alm_off_frame = SerialFrame(0x1D1E, 0x04, 0x00)


        def alm_off_task():
            nonlocal test_result
            test_result = alm_off_frame.receive_frame(self.Serial_Obj, timeout=1)

        test_result = False
        send_frame(self.Serial_Obj, alm_off_frame)

        ping_thread = threading.Thread(target=alm_off_task)
        ping_thread.start()
        ping_thread.join(timeout=1)  #wait for thread for 1 sec
        if test_result == True:
            self.ui.alm_off_status_label.setText("<font color=green>PASS")
        else:
            self.ui.alm_off_status_label.setText("<font color=red>FAIL")


    def test_wifi_conn(self):
        wifi_conn_frame = SerialFrame(0x1D1E, 0x05, 0x00)
        def wifi_conn_task():
            nonlocal test_result
            test_result = wifi_conn_frame.receive_frame(self.Serial_Obj, timeout=1)

        test_result = False
        send_frame(self.Serial_Obj, wifi_conn_frame)

        ping_thread = threading.Thread(target=wifi_conn_task)
        ping_thread.start()
        ping_thread.join(timeout=1)  # wait for thread for 1 sec
        if test_result:
            self.ui.wifi_conn_status_label.setText("<font color=green>PASS")
        else:
            self.ui.wifi_conn_status_label.setText("<font color=red>FAIL")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
