import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("landingpage.ui", self)
        self.patientbutton.clicked.connect(self.gotopatient)
        self.doctorbutton.clicked.connect(self.gotodoctor)

    def gotodoctor(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
        widget.setFixedWidth(400)   

    def gotopatient(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(400)

class PatientScreen(QDialog):
    def __init__(self):
        super(PatientScreen, self).__init__()
        loadUi("patient.ui", self)
        self.goback.clicked.connect(self.gobackfunction)
        self.patientsubmitbutton.clicked.connect(self.patientinformation)
        

    def patientinformation(self):
        patient_name = self.patientname.text()
        if self.radioButton.isChecked():
            patient_gender = self.radioButton.text()
        else:
            patient_gender = self.radioButton_2.text()
        patient_blood_group = self.BG.currentText()
        date_of_birth = self.dob.text()
        phone_number = self.phonenumber.text()
        address = self.address.toPlainText()

        print(patient_name)

        return {
            'patient_name' : patient_name,
            'patient_gender': patient_gender,
            'patient_blood_group': patient_blood_group,
            'date_of_birth': date_of_birth,
            'phone_number': patient_gender,
            'address': address

        }


    def gobackfunction(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.setFixedWidth(650)

class DoctorScreen(QDialog):
    def __init__(self):
        super(DoctorScreen, self).__init__()
        loadUi("doctor.ui", self)
        self.doctorsubmitbutton.clicked.connect(self.doctorinformation)
        self.gobackdoctor.clicked.connect(self.gobackfunction)

    def doctorinformation(self):
        doctor_name = self.doctorname.text()
        designation = self.designation.text()
        license = self.license.text()
        phone_number = self.phone_number.text()
        address = self.address.toPlainText()

        print(doctor_name)

        return {
            'doctor_name' : doctor_name,
            'designation': designation,
            'license': license,
            'phone_number': phone_number,
            'address': address

        }


    def gobackfunction(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
        widget.setFixedWidth(650)
        


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
patientscreen = PatientScreen()
doctorscreen = DoctorScreen()
widget.addWidget(mainwindow)
widget.addWidget(patientscreen)
widget.addWidget(doctorscreen)
widget.setFixedHeight(600)
widget.setFixedWidth(650)
widget.show()





try:
    sys.exit(app.exec_())
except:
    print("Exiting")