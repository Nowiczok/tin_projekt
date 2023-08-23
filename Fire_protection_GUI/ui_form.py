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
        Widget.resize(800, 600)
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
        self.status_label.setGeometry(QRect(40, 520, 241, 16))

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
    # retranslateUi

