import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
from PyQt4.QtGui import QApplication, QWidget, QLabel, QGroupBox, QVBoxLayout, QImage, QPixmap
from PyQt4.QtCore import QSize, QTimer
import cv2



                               #UI Files Connector

QLogin = uic.loadUiType("Login.ui")[0]

qtCom_setFile = "input.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCom_setFile)

QConfig = uic.loadUiType("config_dailog.ui")[0]

QInterfaceType = uic.loadUiType("InterfaceType.ui")[0]

QAdvice = uic.loadUiType("Advice.ui")[0]

QVisualization = uic.loadUiType("Visualization.ui")[0]

QTrend = uic.loadUiType("Trend.ui")[0]

QRegistration = uic.loadUiType("registration.ui")[0]

QEdit_Profile = uic.loadUiType("edit_profile.ui")[0]

QResults = uic.loadUiType("results.ui")[0]

QCamera = uic.loadUiType("Camera.ui")[0]

QData = uic.loadUiType("data.ui")[0]

QParameters = uic.loadUiType("Parameters.ui")[0]

QStatistics = uic.loadUiType("Statistics.ui")[0]

QLAN = uic.loadUiType("lan_settings.ui")[0]

QWifi = uic.loadUiType("wifi_settings.ui")[0]

QOFC = uic.loadUiType("ofc_settings.ui")[0]

QSerial = uic.loadUiType("serial_settings.ui")[0]

QMobile = uic.loadUiType("mobile_settings.ui")[0]

QZigbee = uic.loadUiType("zigbee_settings.ui")[0]

QAbout = uic.loadUiType("About.ui")[0]

                                      #Login Class

class QLoginClass(QtGui.QDialog, QLogin):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_Login.clicked.connect(self.loginCheck)
        self.pushButton_Signup.clicked.connect(self.signup)
        


    def loginCheck(self):
        username = self.lineEdit_Username.text()
        password = self.lineEdit_Password.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if(len(result.fetchall()) > 0):
            print("User Found ! ")
            self.accept()
        else:
            print("User Not Found !")
            self.showMessageBox('Warning','Invalid Username And Password')
        connection.close()

    def signup(self):
        signup = QRegistrationClass()
        signup.exec_()


    





                                      #Function Classes 

class QConfigClass(QtGui.QDialog, QConfig):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_LAN.clicked.connect(self.lan)
        self.pushButton_WIFI.clicked.connect(self.wifi)
        self.pushButton_OFC.clicked.connect(self.ofc)
        self.pushButton_Serial.clicked.connect(self.serial)
        self.pushButton_Mobile.clicked.connect(self.mobile)
        self.pushButton_Zigbee.clicked.connect(self.zigbee)

    def mobile(self):
        mobile = QMobileClass()
        mobile.exec_()


    def zigbee(self):
        zigbee = QZigbeeClass()
        zigbee.exec_()
        


    def serial(self):
        serial = QSerialClass()
        serial.exec_()


    def lan(self):
        lan = QLANClass()
        lan.exec_()

    def wifi(self):
        wifi = QWifiClass()
        wifi.exec_()

    def ofc(self):
        ofc = QOFCClass()
        ofc.exec_()


class QInterface_TypeClass(QtGui.QDialog, QInterfaceType):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QLANClass(QtGui.QDialog, QLAN):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QWifiClass(QtGui.QDialog, QWifi):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QOFCClass(QtGui.QDialog, QOFC):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QSerialClass(QtGui.QDialog, QSerial):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QMobileClass(QtGui.QDialog, QMobile):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

class QZigbeeClass(QtGui.QDialog, QZigbee):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        
class QAdviceClass(QtGui.QDialog, QAdvice):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QVisualizationClass(QtGui.QDialog, QVisualization):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_Stats.clicked.connect(self.stats)
        self.pushButton_Load.clicked.connect(self.loadData)
        self.pushButton_Exit.clicked.connect(self.closeIt)


    def closeIt(self): 
        self.close()
        

    def loadData(self):
        conn = sqlite3.connect('tutorial.db')

          
        query = "SELECT * FROM stuffToPlot"
        result = conn.execute(query)
        self.tableWidget_Visualization.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_Visualization.insertRow(row_number)
            for coloumn_number, data in enumerate(row_data):
                self.tableWidget_Visualization.setItem(row_number, coloumn_number, QtGui.QTableWidgetItem(str(data)))

        conn.close()       


    def stats(self):
        stats = QStatisticsClass()
        stats.exec_()

class QTrendClass(QtGui.QDialog, QTrend):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)



class QRegistrationClass(QtGui.QDialog, QRegistration):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.saveRegisteration_btn.clicked.connect(self.insertData)

    def insertData(self):
        name = self.lineEdit_Name.text()
        username = self.lineEdit_Username.text()
        email = self.lineEdit_Email.text()
        password = self.lineEdit_Password.text()
        dob = self.lineEdit_DOB.text()
        address = self.lineEdit_Address.text()
        designation = self.lineEdit_Designation.text()
        phone = self.lineEdit_PhoneNo.text()
        qualification = self.lineEdit_Qualification.text()
        userid = self.lineEdit_UserId.text()

        connection  = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)",(name,username,email,password,dob,address,designation,phone,qualification,userid))
        connection.commit()
        connection.close()

  


class QEdit_ProfileClass(QtGui.QDialog, QEdit_Profile):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QResultsClass(QtGui.QDialog, QResults):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QCameraClass(QtGui.QDialog, QCamera):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        

class QDataClass(QtGui.QDialog, QData):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


        self.comboBox_Parameters.activated[str].connect(self.parameter)


    

    def parameter(self, text):
        cur_txt = text
        self.groupBox.hide()
        self.groupBox_2.hide()
        self.groupBox_3.hide()
        self.groupBox_4.hide()
        self.groupBox_5.hide()
        self.groupBox_6.hide()
        self.groupBox_7.hide()
        self.groupBox_8.hide()

        if  cur_txt == '1':
            self.groupBox.show()
            
        elif cur_txt == '2':
            self.groupBox.show()
            self.groupBox_2.show()
        elif cur_txt == '3':
            self.groupBox.show()
            self.groupBox_2.show()
            self.groupBox_3.show()
        elif cur_txt == '4':
            self.groupBox.show()
            self.groupBox_2.show()
            self.groupBox_3.show()
            self.groupBox_4.show()
        elif cur_txt == '5':
            self.groupBox.show()
            self.groupBox_2.show()
            self.groupBox_3.show()
            self.groupBox_4.show()
            self.groupBox_5.show()
        elif cur_txt == '6':
            self.groupBox.show()
            self.groupBox_2.show()
            self.groupBox_3.show()
            self.groupBox_4.show()
            self.groupBox_5.show()
            self.groupBox_6.show()
        elif cur_txt == '7':
            self.groupBox.show()
            self.groupBox_2.show()
            self.groupBox_3.show()
            self.groupBox_4.show()
            self.groupBox_5.show()
            self.groupBox_6.show()
            self.groupBox_7.show()   
        else:
            self.groupBox.show()
            self.groupBox_2.show()
            self.groupBox_3.show()
            self.groupBox_4.show()
            self.groupBox_5.show()
            self.groupBox_6.show()
            self.groupBox_7.show()
            self.groupBox_8.show()
        

    def parameters(self):
        para = QParametersClass()
        para.exec_()


class QParametersClass(QtGui.QDialog, QParameters):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QStatisticsClass(QtGui.QDialog, QStatistics):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class QAboutClass(QtGui.QDialog, QAbout):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)



                    #Main Menu Class

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        self.actionReports.triggered.connect(self.reports)
        self.actionInterface_Type.triggered.connect(self.interface_type)
        self.actionCom_Settings.triggered.connect(self.com_Settings)
        self.actionAdvice.triggered.connect(self.advice)
        self.actionVisualization.triggered.connect(self.visualization)
        self.actionTrend.triggered.connect(self.trend)
        self.actionRegister.triggered.connect(self.registration)
        self.actionResults.triggered.connect(self.results)
        self.actionCamera.triggered.connect(self.camera)
        self.actionData_Settings.triggered.connect(self.data)
        self.actionEdit_Profile.triggered.connect(self.edit_profile)
        self.actionExit.triggered.connect(self.exit)
        self.actionAbout.triggered.connect(self.about)
        self.pushButton_Camera.clicked.connect(self.camera)




                 #Main Menu Fucntions


    def about(self):
        about = QAboutClass()
        about.exec_()


        
    def exit(self):
        choice = QtGui.QMessageBox.question(self, "Exit", "Do you want to quit",
                                           QtGui.QMessageBox.Yes  | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print("App Exit")
            sys.exit()

        else:
            pass


    def data(self):
        data = QDataClass()
        data.exec_()


    def camera(self):
        cam = QCameraClass()
        cam.exec_()

    def results(self):
        results = QResultsClass()
        results.exec_()

    def edit_profile(self):
        editProfile = QEdit_ProfileClass()
        editProfile.exec_()


    def registration(self):
        register = QRegistrationClass()
        register.exec_()
        


    def trend(self):
        trend = QTrendClass()
        trend.exec_()



    def visualization(self):
        visual = QVisualizationClass()
        visual.exec_()
        


    def advice(self):
        alert = QAdviceClass()
        alert.exec_()


    def reports(self):
         pass
        
    def com_Settings(self):
        com = QConfigClass()
        com.exec_()

    def interface_type(self):
        interface = QInterface_TypeClass()
        interface.exec_()





         
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    login = QLoginClass()

    if login.exec_() == QtGui.QDialog.Accepted:
        window = MyApp()
        window.show()
        sys.exit(app.exec_())




