import sys
import rospy
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton, QLabel, QHBoxLayout, QProxyStyle, QStyle
from PyQt5.QtCore import Qt, QCoreApplication
from std_msgs.msg import Float64

global sld_value
sld_value = 0

class SliderProxyStyle(QProxyStyle):
    def pixelMetric(self, metric, option, widget):
        if metric == QStyle.PM_SliderThickness:
            return 40
        elif metric == QStyle.PM_SliderLength:
            return 15
        return super(QProxyStyle,self).pixelMetric(metric, option, widget)

class MyApp(QWidget):

    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        self.slider = QSlider(Qt.Horizontal, self)
        style = SliderProxyStyle(self.slider.style())
        self.slider.setStyle(style)
        self.slider.move(125, 20)
        self.slider.setRange(0, 20)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setSingleStep(1)
        # self.slider.setTickPosition(1)

        self.slider.valueChanged.connect(self.updateLabel)
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label.setMinimumWidth(80)
        self.label.move(130, 5)

        hbox.addWidget(self.slider)
        hbox.addSpacing(15)
        hbox.addWidget(self.label)

        btn = QPushButton('Default', self)
        btn.move(75, 60)
        btn.clicked.connect(self.button_clicked)

        quit = QPushButton('Quit', self)
        quit.move(185, 60)
        quit.clicked.connect(self.quit_button)

        plus = QPushButton('+', self)
        plus.move(225, 25)
        plus.clicked.connect(self.plus_clicked)
        plus.resize(25,25)

        minus = QPushButton('-', self)
        minus.move(85, 25)
        minus.clicked.connect(self.minus_clicked)
        minus.resize(25,25)

        self.setWindowTitle('Amplitude')
        self.setGeometry(300, 300, 350, 100)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)

    def plus_clicked(self):
        global sld_value
        if sld_value <= 20:
            self.slider.setValue(sld_value+1)

    def minus_clicked(self):
        global sld_value
        if sld_value > 0:
            self.slider.setValue(sld_value-1)

    def quit_button(self):
        QCoreApplication.instance().quit()
        rospy.signal_shutdown("Quit the slider")

    def updateLabel(self, value):
        global sld_value
        sld_value = value
        self.label.setText(str(value))

def talker():
    global sld_value
    pub = rospy.Publisher('amp', Float64, queue_size=10)
    while not rospy.is_shutdown():
        global sld_value
        pub.publish(float(sld_value))
        rospy.sleep(0.1)

def talker_thread():
    print('Start to publish Amplitude to ROS core...')
    t_thread = threading.Thread(target = talker)
    t_thread.start()

if __name__ == '__main__':
    rospy.init_node('amp_talker')
    talker_thread()
    sld_value = 0
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    rospy.signal_shutdown("Quit the slider")
