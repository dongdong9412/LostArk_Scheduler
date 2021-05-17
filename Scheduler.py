import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QFont
import pandas as pd
from datetime import datetime, timedelta
import atexit
import pickle


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.userInfo = dict()
        self.days = ['Day6', 'Day7', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5']
        self.date = self.days[datetime.today().weekday()]
        self.loadData()
        self.initUI()
        atexit.register(self.saveData)
    
    def loadData(self):
        try:
            with open('UserData', 'rb') as savedData:
                self.userInfo = pickle.load(savedData)
            print('Load Data')
            print(self.userInfo)

        except:
            print('No DataBase')

    def saveData(self):
        try:
            with open('UserData','wb') as saveFile:
                pickle.dump(self.userInfo, saveFile)
                saveFile.close()
            print('Save Data')
        except:
            print('No DataBase')
        

    def initUI(self):
        # Daily Contents Label #
        self.dailyHeader = QLabel('일일 컨텐츠', self)
        self.dailyHeader.move(10, 70)
        font_dailyHeader = self.dailyHeader.font()
        font_dailyHeader.setPointSize(10)
        font_dailyHeader.setBold(True)
        font_dailyHeader.setFamily('맑은 고딕')
        self.dailyHeader.setFont(font_dailyHeader)

        # Daily Check List #
        self.DailycheckBox_1 = QCheckBox('길드 출석', self)
        self.DailycheckBox_1.move(10, 90)
        self.DailycheckBox_1.stateChanged.connect(self.DailycheckBox1_Contents)

        self.DailycheckBox_2 = QCheckBox('카오스 던전', self)
        self.DailycheckBox_2.move(10, 110)
        self.DailycheckBox_2.stateChanged.connect(self.DailycheckBox2_Contents)
        self.DailyspinBox_1 = QSpinBox()
        self.DailyspinBox_1.setMinimum(0)
        self.DailyspinBox_1.setMaximum(2)
        self.DailyspinBox_1.setSingleStep(1)
        self.DailyspinBox_1.setGeometry(10, 110, 100, 20)

        self.DailycheckBox_3 = QCheckBox('가디언 토벌', self)
        self.DailycheckBox_3.move(10, 130)
        self.DailycheckBox_3.stateChanged.connect(self.DailycheckBox3_Contents)

        self.DailycheckBox_4 = QCheckBox('에포나', self)
        self.DailycheckBox_4.move(10, 150)
        self.DailycheckBox_4.stateChanged.connect(self.DailycheckBox4_Contents)

        # Weekly Check List #
        self.WeeklycheckBox_1 = QCheckBox('오레하/카슈', self)
        self.WeeklycheckBox_1.move(210, 90)
        self.WeeklycheckBox_1.stateChanged.connect(self.WeeklycheckBox1_Contents)

        self.WeeklycheckBox_2 = QCheckBox('아르고스', self)
        self.WeeklycheckBox_2.move(210, 110)
        self.WeeklycheckBox_2.stateChanged.connect(self.WeeklycheckBox2_Contents)

        self.WeeklycheckBox_3 = QCheckBox('주간 에포나', self)
        self.WeeklycheckBox_3.move(210, 130)
        self.WeeklycheckBox_3.stateChanged.connect(self.WeeklycheckBox3_Contents)

        self.WeeklycheckBox_4 = QCheckBox('군단장', self)
        self.WeeklycheckBox_4.move(210, 150)
        self.WeeklycheckBox_4.stateChanged.connect(self.WeeklycheckBox4_Contents)

        self.WeeklycheckBox_5 = QCheckBox('길드 의뢰', self)
        self.WeeklycheckBox_5.move(210, 170)
        self.WeeklycheckBox_5.stateChanged.connect(self.WeeklycheckBox5_Contents)

        self.WeeklycheckBox_6 = QCheckBox('도전 토벌', self)
        self.WeeklycheckBox_6.move(210, 190)
        self.WeeklycheckBox_6.stateChanged.connect(self.WeeklycheckBox6_Contents)

        # Weekly Contents Label #
        self.weeklyHeader = QLabel('주간 컨텐츠', self)
        self.weeklyHeader.move(210, 70)
        font_weeklyHeader = self.weeklyHeader.font()
        font_weeklyHeader.setPointSize(10)
        font_weeklyHeader.setBold(True)
        font_weeklyHeader.setFamily('맑은 고딕')
        self.weeklyHeader.setFont(font_weeklyHeader)
        
        # User Info Add Button #
        self.addInfo = QPushButton(self)
        self.addInfo.setText('Add')
        self.addInfo.clicked.connect(self.add_Info)
        self.addInfo.move(165, 9)

        # User Info Edit #
        self.editInfo = QLineEdit(self)
        self.editInfo.move(10, 10)

        # User List #
        self.CharacterList = QComboBox(self)
        self.CharacterList.setGeometry(10,40, 200, 20)
        self.CharacterList.activated[str].connect(self.select_Character)
        self.CharacterList.currentTextChanged.connect(self.switch_Character)

        # 카오스 던전 휴식 게이지 #
        self.gauge1_Label = QLabel('카오스 던전', self)
        self.gauge1_Label.move(10, 220)
        font_gauge1_Label = self.gauge1_Label.font()
        font_gauge1_Label.setPointSize(10)
        font_gauge1_Label.setBold(True)
        font_gauge1_Label.setFamily('맑은 고딕')
        self.gauge1_Label.setFont(font_gauge1_Label)
        self.gauge_1 = QProgressBar(self)
        self.gauge_1.setGeometry(90, 219, 200, 20)

        # 에포나 휴식 게이지 #
        self.gauge1_Label = QLabel('에포나', self)
        self.gauge1_Label.move(10, 250)
        font_gauge1_Label = self.gauge1_Label.font()
        font_gauge1_Label.setPointSize(10)
        font_gauge1_Label.setBold(True)
        font_gauge1_Label.setFamily('맑은 고딕')
        self.gauge1_Label.setFont(font_gauge1_Label)
        self.gauge_1 = QProgressBar(self)
        self.gauge_1.setGeometry(90, 249, 200, 20)
        self.gauge_1.setValue(10)

        # 가디언 토벌 휴식 게이지 #
        self.gauge1_Label = QLabel('가디언 토벌', self)
        self.gauge1_Label.move(10, 280)
        font_gauge1_Label = self.gauge1_Label.font()
        font_gauge1_Label.setPointSize(10)
        font_gauge1_Label.setBold(True)
        font_gauge1_Label.setFamily('맑은 고딕')
        self.gauge1_Label.setFont(font_gauge1_Label)
        self.gauge_1 = QProgressBar(self)
        self.gauge_1.setGeometry(90, 279, 200, 20)

        self.update_SavedData()

        self.setWindowTitle('Lost Ark Scheduler_v1')
        self.resize(400,350)
        self.show()

    def update_SavedData(self):
        print(bool(self.userInfo))
        if bool(self.userInfo) == True:
            self.CharacterList.addItems(self.userInfo.keys())
            if self.DailycheckBox_1.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['길드 출석']:
                self.DailycheckBox_1.toggle()
            if self.DailycheckBox_2.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['카오스 던전']:
                self.DailycheckBox_2.toggle()
            if self.DailycheckBox_3.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['가디언 토벌']:
                self.DailycheckBox_3.toggle()
            if self.DailycheckBox_4.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['에포나']:
                self.DailycheckBox_4.toggle()
            if self.WeeklycheckBox_1.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['오레하/카슈']:
                self.WeeklycheckBox_1.toggle()
            if self.WeeklycheckBox_2.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['아르고스']:
                self.WeeklycheckBox_2.toggle()
            if self.WeeklycheckBox_3.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['주간 에포나']:
                self.WeeklycheckBox_3.toggle()
            if self.WeeklycheckBox_4.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['군단장']:
                self.WeeklycheckBox_4.toggle()
            if self.WeeklycheckBox_5.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['길드 의뢰']:
                self.WeeklycheckBox_5.toggle()
            if self.WeeklycheckBox_6.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['도전 토벌']:
                self.WeeklycheckBox_6.toggle()

    def select_Character(self, text):
        # Load Character Data #
        print('select_Character')
        if self.DailycheckBox_1.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['길드 출석']:
            self.DailycheckBox_1.toggle()
        if self.DailycheckBox_2.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['카오스 던전']:
            self.DailycheckBox_2.toggle()
        if self.DailycheckBox_3.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['가디언 토벌']:
            self.DailycheckBox_3.toggle()
        if self.DailycheckBox_4.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['에포나']:
            self.DailycheckBox_4.toggle()
        if self.WeeklycheckBox_1.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['오레하/카슈']:
            self.WeeklycheckBox_1.toggle()
        if self.WeeklycheckBox_2.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['아르고스']:
            self.WeeklycheckBox_2.toggle()
        if self.WeeklycheckBox_3.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['주간 에포나']:
            self.WeeklycheckBox_3.toggle()
        if self.WeeklycheckBox_4.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['군단장']:
            self.WeeklycheckBox_4.toggle()
        if self.WeeklycheckBox_5.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['길드 의뢰']:
            self.WeeklycheckBox_5.toggle()
        if self.WeeklycheckBox_6.isChecked() != self.userInfo[self.CharacterList.currentText()][self.date]['도전 토벌']:
            self.WeeklycheckBox_6.toggle()

    def switch_Character(self):
        print('switch_Character')

    def add_Info(self):
        characterName = self.editInfo.text()
        if not characterName in self.userInfo.keys():
            self.userInfo[characterName] = {
                self.date:{
                    '길드 출석':False,
                    '카오스 던전':False,
                    '가디언 토벌':False,
                    '에포나':False,
                    '오레하/카슈':False,
                    '아르고스':False,
                    '주간 에포나':False,
                    '군단장':False,
                    '길드 의뢰':False,
                    '도전 토벌':False
                }
            }
            self.CharacterList.addItem(characterName)
            self.CharacterList.setCurrentText(characterName)
            self.editInfo.clear()
            print(self.userInfo)

    def DailycheckBox1_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.DailycheckBox_1.text()] = self.DailycheckBox_1.isChecked()
    def DailycheckBox2_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.DailycheckBox_2.text()] = self.DailycheckBox_2.isChecked()
    def DailycheckBox3_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.DailycheckBox_3.text()] = self.DailycheckBox_3.isChecked()
    def DailycheckBox4_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.DailycheckBox_4.text()] = self.DailycheckBox_4.isChecked()

    def WeeklycheckBox1_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.WeeklycheckBox_1.text()] = self.WeeklycheckBox_1.isChecked()
    def WeeklycheckBox2_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.WeeklycheckBox_2.text()] = self.WeeklycheckBox_2.isChecked()
    def WeeklycheckBox3_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.WeeklycheckBox_3.text()] = self.WeeklycheckBox_3.isChecked()
    def WeeklycheckBox4_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.WeeklycheckBox_4.text()] = self.WeeklycheckBox_4.isChecked()
    def WeeklycheckBox5_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.WeeklycheckBox_5.text()] = self.WeeklycheckBox_5.isChecked()
    def WeeklycheckBox6_Contents(self):
        if bool(self.userInfo):
            self.userInfo[self.CharacterList.currentText()][self.date][self.WeeklycheckBox_6.text()] = self.WeeklycheckBox_6.isChecked()
if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = MyApp()
    sys.exit(app.exec_())