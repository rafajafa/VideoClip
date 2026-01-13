# from moviepy.editor import VideoFileClip
import moviepy.editor
import selenium.webdriver.edge.options
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import cv2
import os
from PIL import Image
from PIL import ImageSequence
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.lanauge = 'English'
        
        # self.retranslateUi(self)
        self.retranslateUiEnglish(self)
        
        self.init_slots()
        self.video_path = ''   #视频路径
        self.init_timer()
        self.cap = cv2.VideoCapture()
        self.start_time = 0
        self.finish_time = 0
        self.video_fps = 0

    def setupUi(self, MainWindow):
        font = QtGui.QFont()
        font.setPointSize(9)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 474)
        MainWindow.setMinimumSize(QtCore.QSize(505, 474))
        MainWindow.setMaximumSize(QtCore.QSize(505, 474))       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(57, 17, 389, 227))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 270, 481, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(90, 30))

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 30))
        
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.toolButtonInput = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonInput.sizePolicy().hasHeightForWidth())
        self.toolButtonInput.setSizePolicy(sizePolicy)
        self.toolButtonInput.setMinimumSize(QtCore.QSize(40, 30))
        self.toolButtonInput.setMaximumSize(QtCore.QSize(16777215, 30))
        self.toolButtonInput.setObjectName("toolButtonInput")
        self.horizontalLayout.addWidget(self.toolButtonInput)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(310, 350, 181, 32))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.label_template = QtWidgets.QLabel(self.centralwidget)
        self.label_template.setGeometry(QtCore.QRect(50, 10, 403, 241))
        self.label_template.setText("")
        self.label_template.setObjectName("label_template")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 310, 481, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(160, 30))
        self.label_6.setMaximumSize(QtCore.QSize(160, 30))

        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.time_start = QtWidgets.QTextEdit(self.layoutWidget1)
        self.time_start.setMinimumSize(QtCore.QSize(35, 0))
        self.time_start.setMaximumSize(QtCore.QSize(35, 30))
        self.time_start.setObjectName("time_start")
        self.horizontalLayout_3.addWidget(self.time_start)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(5, 30))
        self.label_11.setMaximumSize(QtCore.QSize(5, 30))

        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.time_start_2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.time_start_2.setMinimumSize(QtCore.QSize(35, 0))
        self.time_start_2.setMaximumSize(QtCore.QSize(35, 30))
        self.time_start_2.setObjectName("time_start_2")
        self.horizontalLayout_3.addWidget(self.time_start_2)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(30, 30))
        self.label_7.setMaximumSize(QtCore.QSize(30, 30))

        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.time_finish = QtWidgets.QTextEdit(self.layoutWidget1)
        self.time_finish.setMinimumSize(QtCore.QSize(35, 0))
        self.time_finish.setMaximumSize(QtCore.QSize(35, 30))
        self.time_finish.setObjectName("time_finish")
        self.horizontalLayout_3.addWidget(self.time_finish)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(5, 30))
        self.label_12.setMaximumSize(QtCore.QSize(5, 30))

        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.time_finish_2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.time_finish_2.setMinimumSize(QtCore.QSize(35, 0))
        self.time_finish_2.setMaximumSize(QtCore.QSize(35, 30))
        self.time_finish_2.setObjectName("time_finish_2")
        self.horizontalLayout_3.addWidget(self.time_finish_2)
        spacerItem = QtWidgets.QSpacerItem(50, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox.setMinimumSize(QtCore.QSize(100, 30))
        self.checkBox.setMaximumSize(QtCore.QSize(100, 30))
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 350, 281, 32))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(130, 30))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))

        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.output_name = QtWidgets.QTextEdit(self.layoutWidget2)
        self.output_name.setMinimumSize(QtCore.QSize(0, 30))
        self.output_name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.output_name.setObjectName("output_name")
        self.horizontalLayout_4.addWidget(self.output_name)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 390, 481, 32))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(70, 30))
        self.label_9.setMaximumSize(QtCore.QSize(70, 30))

        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox.setMinimumSize(QtCore.QSize(80, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(80, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(100, 30))
        self.label_10.setMaximumSize(QtCore.QSize(125, 30))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.workshop_name = QtWidgets.QTextEdit(self.layoutWidget3)
        self.workshop_name.setMinimumSize(QtCore.QSize(0, 30))
        self.workshop_name.setMaximumSize(QtCore.QSize(100, 30))
        self.workshop_name.setObjectName("workshop_name")
        self.horizontalLayout_5.addWidget(self.workshop_name)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        
        self.languageButton = QtWidgets.QPushButton(self.centralwidget)
        self.languageButton.setGeometry(QtCore.QRect(420, 10, 75, 30))
        self.languageButton.setObjectName("languageButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(MainWindow)
        self.retranslateUiEnglish(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SteamVideoCut"))
        self.label_5.setText(_translate("MainWindow", "视频路径："))
        self.toolButtonInput.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "切片"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.label_6.setText(_translate("MainWindow", "选择视频时长：从"))
        self.label_11.setText(_translate("MainWindow", "："))
        self.label_7.setText(_translate("MainWindow", " 到"))
        self.label_12.setText(_translate("MainWindow", "："))
        self.checkBox.setText(_translate("MainWindow", "播放视频"))
        self.label_8.setText(_translate("MainWindow", "输出的切片名称："))
        self.label_9.setText(_translate("MainWindow", "浏览器："))
        self.comboBox.setItemText(0, _translate("MainWindow", "Edge"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Chorme"))
        self.label_10.setText(_translate("MainWindow", "创意工坊名称："))
        self.pushButton_3.setText(_translate("MainWindow", "上传"))
        self.languageButton.setText(_translate("MainWindow", "English"))
        self.languageButton.setText(_translate("MainWindow", "English"))
        
    def retranslateUiEnglish(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SteamVideoCut"))
        self.label_5.setText(_translate("MainWindow", "Video Path:"))
        self.toolButtonInput.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Split"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_6.setText(_translate("MainWindow", "Select Video Duration:"))
        self.label_11.setText(_translate("MainWindow", ":"))
        self.label_7.setText(_translate("MainWindow", " To"))
        self.label_12.setText(_translate("MainWindow", ":"))
        self.checkBox.setText(_translate("MainWindow", "Play Video"))
        self.label_8.setText(_translate("MainWindow", "Output Split Name:"))
        self.label_9.setText(_translate("MainWindow", "Browser:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Edge"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Chorme"))
        self.label_10.setText(_translate("MainWindow", "Name on workshop:"))
        self.pushButton_3.setText(_translate("MainWindow", "Upload"))
        self.languageButton.setText(_translate("MainWindow", "中文"))
        
    def switch_language(self):
        """Switch between English and Chinese languages"""
        if self.lanauge == 'English':
            self.lanauge = 'Chinese'
            self.retranslateUi(self)
        else:
            self.lanauge = 'English'
            self.retranslateUiEnglish(self)
        

    def init_slots(self):
        self.pushButton.clicked.connect(self.split_video_to_gifs)  # 连接切片函数
        self.time_start.textChanged.connect(self.read_time_start)
        self.time_start_2.textChanged.connect(self.read_time_start)
        self.time_finish.textChanged.connect(self.read_time_finish)
        self.time_finish_2.textChanged.connect(self.read_time_finish)
        self.toolButtonInput.clicked.connect(self.InpurDir)           # 连接视频路径选择函数
        self.pushButton_3.clicked.connect(self.upload_gif)
        # self.toolButtonOutput.clicked.connect(self.SaveResults)
        self.pushButton_2.clicked.connect(self.close)
        self.languageButton.clicked.connect(self.switch_language)

        pix = QPixmap('template_1.png')        #设置label图片
        self.label_template.setPixmap(pix)
        self.label_template.setScaledContents(True)  # 自适应QLabel大小
        self.output_name.setPlainText("output_gif")
        self.workshop_name.setText('gif') #设置上传名称

        self.checkBox.setChecked(True)
        self.checkBox.clicked.connect(self.check_video_play)

    def InpurDir(self):
        video_type = [".mp4", ".mkv", ".MOV", ".avi","m4v"]
        self.video_path = QtWidgets.QFileDialog.getOpenFileName()[0]

        #判断是否为视频文件
        if self.video_path:
            for vdi in video_type:
                if vdi in self.video_path:
                    print("right")
                    break
                else:
                    if vdi == "m4v":
                        error_msg = "不支持该格式" if self.lanauge == 'Chinese' else "Unsupported format"
                        QtWidgets.QMessageBox.information(self, "Error", error_msg, QtWidgets.QMessageBox.Yes,
                                                          QtWidgets.QMessageBox.Yes)
                        return

        if self.video_path:
            print("选择输入视频路径：", self.video_path)
            self.textEdit.setPlainText(self.video_path)
            print("videoIsOpen")

            # 获取视频时长,并设置文本框中时间
            duration = self.get_video_duration()
            self.time_start.setText("00")
            self.time_start_2.setText("00")
            if duration < 15:
                self.finish_time = duration
                self.time_finish.setText("00")
                self.time_finish_2.setText(str(duration))
            else:
                self.finish_time = 10
                self.time_finish.setText("00")
                self.time_finish_2.setText("10")

            self.cap.open(self.video_path) #打开视频
            self.timer.start(30)   #设置视频播放计时器

    def get_video_duration(self):
        video = cv2.VideoCapture(self.video_path)
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_rate = video.get(cv2.CAP_PROP_FPS)
        self.video_fps = int(frame_rate)               #更新视频帧率
        print("fps:", self.video_fps)
        duration = int(frame_count / frame_rate)
        video.release()
        return duration

    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.play_video)

    def check_video_play(self):
        if self.checkBox.isChecked():
            self.timer.start(30)
            print("play video")
        else:
            self.timer.stop()
            print("pause video")

    def play_video(self):
        ret, img = self.cap.read()
        if ret:
            #cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # 视频流的长和宽
            height, width = img.shape[:2]
            # 对视频进行缩放，适应label大小
            #cur_frame = cv2.resize(img,(0, 0), fx= width / self.label.width(),fy= height / self.label.height())
            cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            pixmap = QImage(cur_frame, width, height, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
            self.label.setScaledContents(True)
            # ratio = max(width / self.label.width(), height / self.label.height())
            # pixmap.setDevicePixelRatio(ratio)
            # 视频流置于label中间部分播放
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setPixmap(pixmap)

    def read_time_start(self):
        if ":" in self.time_start.toPlainText():
            print("minite")
        else:

            print("start time:", self.time_start.toPlainText(),":", self.time_start_2.toPlainText())

    def read_time_finish(self):
        if ":" in self.time_finish.toPlainText():
            print("minite")
        else:

            print("finish time:", self.time_finish.toPlainText(), ":", self.time_finish_2.toPlainText())

    def split_video_to_gifs(self):
        #计算时间
        self.start_time = int(self.time_start.toPlainText()) * 60 + int(self.time_start_2.toPlainText())  # 转化为秒
        self.finish_time = int(self.time_finish.toPlainText()) * 60 + int(self.time_finish_2.toPlainText())  # 转化为秒
        # 读取视频文件
        video = moviepy.editor.VideoFileClip(self.video_path).subclip(self.start_time, self.finish_time)  # 取前10秒
        # video = VideoFileClip(input_video)

        #缩放视频到模板大小
        video = video.resize((770,449))

        # 获取视频的宽和高
        width, height = video.size

        # 计算每个部分的宽度
        segment_width = (width - 20) / 5

        for i in range(5):
            # 计算每个 GIF 的起始和结束位置
            start_x = i * segment_width + i * 5
            end_x = start_x + segment_width

            # 裁剪视频
            gif_segment = video.crop(x1=start_x, x2=end_x, y1=0, y2=height)

            # 生成 GIF 文件
            gif_segment.write_gif(f"{self.output_name.toPlainText()}_part{i + 1}.gif", fps=6)

        # 关闭视频文件
        video.close()
        #print("ok")

        max_size = 5 * 1024 * 1024  # 5MB in bytes

        # 检查文件大小,如果过大则进行缩小
        for i in range(1, 6):
            file_size = os.path.getsize(f"{self.output_name.toPlainText()}_part{i}.gif")
            if file_size <= max_size:
                if i == 5:
                    flag = 0
                    print("文件大小小于 5MB，不需要调整")
            else:
                flag = 1
                print("文件大小大于 5MB，需要调整")
                break

        if flag == 1:
            # 修改文件大小
            for i in range(1, 6):
                im = Image.open(f"{self.output_name.toPlainText()}_part{i}.gif")
                # 计算缩放比例
                original_width, original_height = im.size
                scale_factor = (max_size / file_size) ** 0.5
                new_width = int(original_width * scale_factor * 0.85)  # 0.9为缩放调节因子
                new_height = int(original_height * scale_factor * 0.85)

                resize_frames = [frame.resize((new_width, new_height)) for frame in ImageSequence.Iterator(im)]
                resize_frames[0].save(f"{self.output_name.toPlainText()}_part{i}.gif", save_all=True, append_images=resize_frames[1:])
                print("resize Done!")

        # 更改最后一个字节为21
        for i in range(1,6):
            path = f"{self.output_name.toPlainText()}_part{i}.gif"
            with open(path, 'rb') as f:
                gif_data = bytearray(f.read())

            # 修改最后一个字节为 21
            if len(gif_data) >= 2:
                gif_data[-1] = 0x21

            # 保存修改后的 GIF 文件
            with open(path, 'wb') as f:
                f.write(gif_data)

        success_msg = "切片成功" if self.lanauge == 'Chinese' else "Split successful"
        QtWidgets.QMessageBox.information(self, "Result", success_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)

    def upload_gif(self):
        try:
            #判断使用的浏览器
            if self.comboBox.currentText() == 'Edge':
                op = selenium.webdriver.edge.options.Options()
                op.page_load_strategy = "eager"
                driver = webdriver.Edge(options=op)
            elif self.comboBox.currentText() == 'Chorme':
                op = selenium.webdriver.chrome.options.Options()
                driver = webdriver.Chrome(options=op)

            #打开网页
            driver.get("https://steamcommunity.com/sharedfiles/edititem/767/3/")
            #time.sleep(5)

            #等待网页加载
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input' )) #.find_element_by_id("someId"))

            if os.path.exists("user.txt"):
                # 从文本文件逐行读取,输入到用户名和密码，并点击登录
                with open("user.txt", "r", encoding="utf-8") as file:
                    line1 = file.readline().strip()
                    line2 = file.readline().strip()
                    print("ID:", line1)
                    print("PASSWORD:", line2)
                    input_element = driver.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')  # 获取该输入框的Xpath
                    input_element.clear()  # 清除该输入框中的原本内容
                    input_element.send_keys(line1)  # 向该输入框中添加搜索词
                    input_element = driver.find_element(By.XPATH,'//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input')  # 获取该输入框的Xpath
                    input_element.clear()  # 清除该输入框中的原本内容
                    input_element.send_keys(line2)  # 向该输入框中添加搜索词
                    driver.find_element(By.CLASS_NAME, "LBS7IDpob52Sb4ZoKobh0").click()
                    driver.find_element(By.CLASS_NAME, "DjSvCZoKKfoNSmarsEcTS").click()
            else:
                print("手动输入账号密码")

            # 判断是否登录成功
            while True:
                if driver.current_url == "https://steamcommunity.com/sharedfiles/edititem/767/3/":
                    print("login sussessfully")
                    break
            # time.sleep(1)

            # #把密码和用户名保存到txt文件中
            # # 获取用户输入
            # string1 = input("请输入第一条字符串: ")
            # string2 = input("请输入第二条字符串: ")
            #
            # # 保存到文本文件
            # with open("strings.txt", "w", encoding="utf-8") as file:
            #     file.write(string1 + "\n")
            #     file.write(string2 + "\n")
            for i in range(1, 6):
                #从第二次循环开始，每次再打开一次创意工坊界面
                if i > 1:
                    driver.get("https://steamcommunity.com/sharedfiles/edititem/767/3/")
                    # 等待网页加载
                    WebDriverWait(driver, 15).until(lambda driver: driver.find_element(By.CLASS_NAME, 'titleField'))

                # 输入标题
                input_element = driver.find_element(By.CLASS_NAME, 'titleField')
                input_element.clear()  # 清除该输入框中的原本内容
                input_element.send_keys(f"{self.workshop_name.toPlainText()}_{i}")   # 向该输入框中添加
                # time.sleep(0.5)

                # 上传gif文件
                dir_path = os.path.abspath(f"{self.output_name.toPlainText()}_part{i}.gif")
                driver.find_element(By.ID, 'file').send_keys(dir_path)
                #time.sleep(0.5)

                # 点击选择框

                driver.find_element(By.ID, "agree_terms").click()

                # 控制台输入命令
                driver.execute_script('''
                    $J('[name=consumer_app_id]').val(480);
                    $J('[name=file_type]').val(0);
                    $J('[name=visibility]').val(0);
                ''')
                #time.sleep(0.5)
                #print("script input finish")

                # 点击提交
                try:
                    driver.find_element(By.XPATH, '//*[@id="SubmitItemForm"]/div[6]/a[2]').click()
                    driver.implicitly_wait(5)
                except Exception:
                    print("timeout")

                # 保存创意工坊的url
                # while True:
                #     if driver.current_url != "https://steamcommunity.com/sharedfiles/edititem/767/3/":
                #         url = driver.current_url
                #         if i == 1 :
                #             with open("url.txt", "w", encoding="utf-8") as file:
                #                 file.write(url + "\n")
                #         else:
                #             with open("url.txt", "a", encoding="utf-8") as file: #追加内容
                #                 file.write(url + "\n")
                #         break

            print("upload finish")
            success_msg = "上传成功" if self.lanauge == 'Chinese' else "Upload successful"
            QtWidgets.QMessageBox.information(self, "Result", success_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)
            time.sleep(1)

        except:
            error_msg = "上传失败" if self.lanauge == 'Chinese' else "Upload failed"
            QtWidgets.QMessageBox.information(self, "Result", error_msg, QtWidgets.QMessageBox.Yes,
                                              QtWidgets.QMessageBox.Yes)

#output_gif_prefix = "output_gif"  # 输出 GIF 文件的前缀
# split_video_to_gifs(input_video, output_gif_prefix)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setWindowTitle('SteamVideoCut')

    # style_file = './style.qss'
    # style_sheet = QSSLoader.read_qss_file(style_file)
    # ui.setStyleSheet(style_sheet)

    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    #apply_stylesheet(app, theme='dark_teal.xml')

    ui.show()
    sys.exit(app.exec_())