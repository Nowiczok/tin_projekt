# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(793, 517)
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(600, 20, 151, 211))
        self.label_8.setPixmap(QPixmap(u"agh_znk_wbr_rgb_150ppi_V2.png"))
        self.label_8.setScaledContents(True)
        self.connect_button = QPushButton(Widget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setGeometry(QRect(590, 400, 141, 51))
        self.port_box = QComboBox(Widget)
        self.port_box.setObjectName(u"port_box")
        self.port_box.setGeometry(QRect(664, 470, 81, 31))
        self.port_box.setEditable(True)
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(580, 470, 81, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.pushButton_ping = QPushButton(Widget)
        self.pushButton_ping.setObjectName(u"pushButton_ping")
        self.pushButton_ping.setGeometry(QRect(20, 270, 141, 51))
        self.pushButton_rel_on = QPushButton(Widget)
        self.pushButton_rel_on.setObjectName(u"pushButton_rel_on")
        self.pushButton_rel_on.setGeometry(QRect(190, 270, 141, 51))
        self.pushButton_rel_off = QPushButton(Widget)
        self.pushButton_rel_off.setObjectName(u"pushButton_rel_off")
        self.pushButton_rel_off.setGeometry(QRect(360, 270, 141, 51))
        self.pushButton_alm_on = QPushButton(Widget)
        self.pushButton_alm_on.setObjectName(u"pushButton_alm_on")
        self.pushButton_alm_on.setGeometry(QRect(530, 270, 141, 51))
        self.pushButton_alm_off = QPushButton(Widget)
        self.pushButton_alm_off.setObjectName(u"pushButton_alm_off")
        self.pushButton_alm_off.setGeometry(QRect(20, 430, 141, 51))
        self.pushButton_wifi_conn = QPushButton(Widget)
        self.pushButton_wifi_conn.setObjectName(u"pushButton_wifi_conn")
        self.pushButton_wifi_conn.setGeometry(QRect(190, 430, 141, 51))
        self.status_label = QLabel(Widget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(290, 490, 241, 20))
        self.ping_status_label = QLabel(Widget)
        self.ping_status_label.setObjectName(u"ping_status_label")
        self.ping_status_label.setEnabled(True)
        self.ping_status_label.setGeometry(QRect(40, 240, 101, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.ping_status_label.setFont(font1)
        self.ping_status_label.setAutoFillBackground(False)
        self.ping_status_label.setAlignment(Qt.AlignCenter)
        self.rel_off_status_label = QLabel(Widget)
        self.rel_off_status_label.setObjectName(u"rel_off_status_label")
        self.rel_off_status_label.setEnabled(True)
        self.rel_off_status_label.setGeometry(QRect(380, 229, 101, 31))
        self.rel_off_status_label.setFont(font1)
        self.rel_off_status_label.setAutoFillBackground(False)
        self.rel_off_status_label.setAlignment(Qt.AlignCenter)
        self.alm_on_status_label = QLabel(Widget)
        self.alm_on_status_label.setObjectName(u"alm_on_status_label")
        self.alm_on_status_label.setEnabled(True)
        self.alm_on_status_label.setGeometry(QRect(550, 229, 91, 31))
        self.alm_on_status_label.setFont(font1)
        self.alm_on_status_label.setAutoFillBackground(False)
        self.alm_on_status_label.setAlignment(Qt.AlignCenter)
        self.alm_off_status_label = QLabel(Widget)
        self.alm_off_status_label.setObjectName(u"alm_off_status_label")
        self.alm_off_status_label.setEnabled(True)
        self.alm_off_status_label.setGeometry(QRect(30, 389, 111, 31))
        self.alm_off_status_label.setFont(font1)
        self.alm_off_status_label.setAutoFillBackground(False)
        self.alm_off_status_label.setAlignment(Qt.AlignCenter)
        self.wifi_conn_status_label = QLabel(Widget)
        self.wifi_conn_status_label.setObjectName(u"wifi_conn_status_label")
        self.wifi_conn_status_label.setEnabled(True)
        self.wifi_conn_status_label.setGeometry(QRect(200, 389, 111, 31))
        self.wifi_conn_status_label.setFont(font1)
        self.wifi_conn_status_label.setAutoFillBackground(False)
        self.wifi_conn_status_label.setAlignment(Qt.AlignCenter)
        self.rel_on_status_label = QLabel(Widget)
        self.rel_on_status_label.setObjectName(u"rel_on_status_label")
        self.rel_on_status_label.setEnabled(True)
        self.rel_on_status_label.setGeometry(QRect(210, 230, 101, 31))
        self.rel_on_status_label.setFont(font1)
        self.rel_on_status_label.setAutoFillBackground(False)
        self.rel_on_status_label.setAlignment(Qt.AlignCenter)
        self.label_8.raise_()
        self.connect_button.raise_()
        self.port_box.raise_()
        self.label_9.raise_()
        self.pushButton_ping.raise_()
        self.pushButton_rel_on.raise_()
        self.pushButton_rel_off.raise_()
        self.pushButton_alm_on.raise_()
        self.pushButton_alm_off.raise_()
        self.pushButton_wifi_conn.raise_()
        self.ping_status_label.raise_()
        self.rel_off_status_label.raise_()
        self.alm_on_status_label.raise_()
        self.alm_off_status_label.raise_()
        self.wifi_conn_status_label.raise_()
        self.rel_on_status_label.raise_()
        self.status_label.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_8.setText("")
        self.connect_button.setText(QCoreApplication.translate("Widget", u"Po\u0142\u0105cz", None))
        self.port_box.setCurrentText(QCoreApplication.translate("Widget", u"COM1", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Port:", None))
        self.pushButton_ping.setText(QCoreApplication.translate("Widget", u"Ping", None))
        self.pushButton_rel_on.setText(QCoreApplication.translate("Widget", u"Relay on", None))
        self.pushButton_rel_off.setText(QCoreApplication.translate("Widget", u"Relay off", None))
        self.pushButton_alm_on.setText(QCoreApplication.translate("Widget", u"Alarm on", None))
        self.pushButton_alm_off.setText(QCoreApplication.translate("Widget", u"Alarm off", None))
        self.pushButton_wifi_conn.setText(QCoreApplication.translate("Widget", u"Wifi connection", None))
        self.status_label.setText("")
        self.ping_status_label.setText("")
        self.rel_off_status_label.setText("")
        self.alm_on_status_label.setText("")
        self.alm_off_status_label.setText("")
        self.wifi_conn_status_label.setText("")
        self.rel_on_status_label.setText("")
    # retranslateUi

