#!/usr/bin/env python
##########################################
##########################################
### Deskside Tool Kit (DsTk) v0.9 beta ##
###       By Forrester Terry            ##
###         Team Crypto 2014            ##
##########################################
            
from PyQt4 import QtCore, QtGui
from functionsfile import *
from submission import *
from PyQt4.QtCore import SIGNAL, SLOT
from sigoutput import *


    

             

class Dialog(QtGui.QDialog):
    NumGridRows = 3
    NumButtons = 4




    # Here is where the modules get intialized    
    def SubmissionForm(self, text):
         # Loaner Selection
        global loaneryesno
        if loaneroptionradioyes.isChecked():
            loaneryesno = "Yes"
        else:
            loaneryesno = "No"
        # Ac Adapter Selection
        global acyesno
        if ACradioyes.isChecked():
            acyesno = "Yes"
        else:
            acyesno = "No"

        # Notes Input Conversion
        NotesEdit = notessmallEditor 
        NotesEdit.setObjectName("NotesInput")

        # Let's convert some of these variables into usable strings...
        ClientName = str(clientnameEdit.text())
        SUNet = str(clientsunetEdit.text())
        Phone = str(clientphoneEdit.text())
        Department = str(clientdepartmentEdit.text())
        NotesInput = str(NotesEdit.toPlainText())
        OSversion = str(osresult)
        

        
             

        #Executes the Script to Create Excel File; Each varible must be passed manually...
        outputform(ClientName, SUNet, Phone, Department, Duedateresponse, cryptform, datedueyo, loaneryesno, acyesno, NotesInput)

        
        # Exectute Print SIG
        printsig(ClientName, Department, OSversion, modelresult, serialresult, freespaceresult, smartresult, NotesInput)
        
    def __init__(self):
        super(Dialog, self).__init__()
        self.LOGO()
        self.SystemInformation()
        self.UserForm2()
        self.TechForm()
        self.Notes()
        self.setWindowTitle("Encryption Submission Form - DsTK")

        
        # A work around to ensuring if no value is clicked for Encrpytion Path, that Ready Win is printed as default.
        # As it is the default selection... duh.

        #UPDATE TO HAVE PROPER TIME
        global cryptform
        cryptform = 'Ready Win'
        global datedueyo
        dateconvertdue = strftime('%b %d, %Y')
        datedueyo = dateconvertdue

        
        buttonRED = QtGui.QPushButton("Submit Form/WorkOrder", None)   
        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
     
        buttonRED.clicked.connect(self.SubmissionForm)
        
           
                                               
    

                   
        
       # Here is where the modules get Added                 
        mainLayout = QtGui.QVBoxLayout()        
        mainLayout.addWidget(self.LOGOBOX)
        mainLayout.addWidget(self.verticalGroupBox)
        mainLayout.addWidget(self.userform)
        mainLayout.addWidget(self.Techform)
        mainLayout.addWidget(self.notes)
        mainLayout.addWidget(buttonRED)
       
             
        # Setup dat Main Layout!
        self.setLayout(mainLayout)
        
        
   
    def LOGO(self):

        def resource_path(relative_path):
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)


        self.LOGOBOX = QtGui.QGroupBox("")
        grid = QtGui.QGridLayout()
        grid.setSpacing(0)
        grid.setHorizontalSpacing(0)

        #Process for the Picture:
        label = QtGui.QLabel() 
        logo = resource_path("YO.png")
        
 
        label.setPixmap(QtGui.QPixmap(logo))
        label.show()
        
        
        



        
        grid.addWidget(label, 0, 1)
        
        self.LOGOBOX.setLayout(grid)
    def SystemInformation(self):
        
        self.verticalGroupBox = QtGui.QGroupBox("System Information")
        grid = QtGui.QVBoxLayout()
        
        
        # Left Column Items
        hostnameresult = hostname
        hostnametext =QtGui.QLabel("Hostname: {}".format(hostnameresult))
        global osresult
        osresult = osversion
        ostextt = QtGui.QLabel("OS: {}".format(osresult))

        global modelresult
        modelresult = model()
        modeltext = QtGui.QLabel("Model Number: {}".format(modelresult))

        global serialresult
        serialresult = getserialnumber
        serialtext = QtGui.QLabel("Serial Number: {}".format(serialresult))
        global freespaceresult
        freespaceresult = str(freespace())
        freespacetext = QtGui.QLabel("Free Space: {}".format(freespaceresult))
        global smartresult
        smartresult = smart()
        smarttext = QtGui.QLabel("S.M.A.R.T: {}".format(smartresult))

        # Right Column Items   
        
        

        grid.addWidget(hostnametext)   
       
        grid.addWidget(ostextt)     

        grid.addWidget(modeltext)
        
        grid.addWidget(serialtext)
        
        grid.addWidget(freespacetext)   
              
        grid.addWidget(smarttext)
      

        self.verticalGroupBox.setLayout(grid)

        
    def UserForm2(self):

        self.userform = QtGui.QGroupBox("User Form")
        #====> Define UserForm Text
        clientname = QtGui.QLabel('Name:')
        clientsunet = QtGui.QLabel("SUNetID:")
        clientphone = QtGui.QLabel("Phone Number:")
        clientdepartment = QtGui.QLabel("Department:")
        loaneroption = QtGui.QLabel("Loaner?")
        
        
        #====> Import Results 
        #Client Name Input 
        global clientnameEdit
        clientnameEdit = QtGui.QLineEdit()
        clientnameEdit.setObjectName("clientnameinput")
        #Client SUNet
        global clientsunetEdit
        clientsunetEdit = QtGui.QLineEdit()
        clientsunetEdit.setFixedWidth(80)
        clientsunetEdit.setObjectName("clientsunetinput")

        #Client Phone Number
        global clientphoneEdit
        clientphoneEdit = QtGui.QLineEdit()
        clientphoneEdit.setObjectName("clientphoneinput")

        #Client Department
        global clientdepartmentEdit
        clientdepartmentEdit = QtGui.QLineEdit()
        clientdepartmentEdit.setObjectName("clientdepartmentinput")

        #Loaner Yes or No?
        
        global loaneroptionradioyes
        loaneroptionradioyes = QtGui.QRadioButton("Yes")
        loaneroptionradioyes.setCheckable(True)
        
        global loaneroptionradiono
        loaneroptionradiono = QtGui.QRadioButton("No")
  
            
        
        # Grid Layout for User Submission Portition
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        

        grid.addWidget(clientname, 1, 0)
        grid.addWidget(clientnameEdit, 1, 1)

        grid.addWidget(clientsunet, 1, 2)
        grid.addWidget(clientsunetEdit, 1, 3)

        grid.addWidget(clientphone, 2, 0)
        grid.addWidget(clientphoneEdit, 2, 1)

        grid.addWidget(clientdepartment, 3, 0)
        grid.addWidget(clientdepartmentEdit, 3, 1)

        grid.addWidget(loaneroption, 2, 2)
        grid.addWidget(loaneroptionradioyes, 2, 3)
        grid.addWidget(loaneroptionradiono, 3, 3)
        self.userform.setLayout(grid)


    def TechForm(self):

        self.Techform = QtGui.QGroupBox("Technician Form")
        

        encryptionpathtext = QtGui.QLabel('Encryption Path:')
        estimatedreturntext = QtGui.QLabel("Estimated Return:")
        ACadapter = QtGui.QLabel('AC Adapter?:')
      
     
        encryptionpathDropdown = QtGui.QComboBox()
       
        dateBox = QtGui.QDateEdit()
        dateBox.setCalendarPopup(True)
        
        #get current date and time
        now = QtCore.QDate.currentDate()
        
        

        #set current date and time to the object
        dateBox.setDate(now)
        dateBox.dateChanged.connect(self.onReturnDate)
        
        
        # AC Adapter Yes or No
        global ACradioyes
        ACradioyes = QtGui.QRadioButton("Yes")
        ACradiono = QtGui.QRadioButton("No")

        ####QtGui.QLabel("{}{}".format(ACradioyes, ACradiono))     
        

        #== ComboBox Options and other nonsense...
        encryptionpathDropdown = QtGui.QComboBox(self)
        encryptionpathDropdown.addItem('Ready Win'),           
        encryptionpathDropdown.addItem('New Win'),           
        encryptionpathDropdown.addItem('Upgrade Win'),            
        encryptionpathDropdown.addItem('Encrypted Win'),

        
 
        #== Creates interaction for Encryption Options and Selection
        encryptionpathDropdown.currentIndexChanged[str].connect(self.onActivated) 

                
        #Layout for TechForm
        grid = QtGui.QGridLayout()
        vertical = QtGui.QVBoxLayout()       
        

        grid.addWidget(encryptionpathtext, 0, 0)
        grid.addWidget(encryptionpathDropdown, 0, 1)

        grid.addWidget(estimatedreturntext, 1, 0)
        grid.addWidget(dateBox, 1, 1)

        grid.addWidget(ACadapter, 2, 0)
        grid.addWidget(ACradioyes, 2, 1)
        grid.addWidget(ACradiono, 2, 2)

        


        #Due Date Response Variable
        global Duedateresponse
        Duedateresponse = dateBox

        self.Techform.setLayout(grid)
        
    def Notes(self):
        
        self.notes = QtGui.QGroupBox("Notes")
        layout = QtGui.QHBoxLayout()
        global notessmallEditor
        notessmallEditor = QtGui.QTextEdit()
        notessmallEditor.setPlainText("")
  
        layout.addWidget(notessmallEditor)

        
        self.notes.setLayout(layout)
        

###############################################################################
######## Conversion and Variable Scripts to do Stuff, yeah  ###################
###############################################################################
        
    # This Converts Combobox into a string, so we can see what the user choose. Yay! 
    def onActivated(self, text):
        global cryptform
         
        if text == 'Ready Win':
            cryptform = 'Ready Win'
        elif text == 'New Win':
            cryptform = 'New Win'
        elif text == 'Upgrade Win':
            cryptform = 'Upgrade Win'
        elif text == 'Encrypted Win':
            cryptform = 'Encrypted Win'
        else:
            cryptform = 'Ready Win'
        
    def onReturnDate(self, date):
        
        global datedueyo
        
        datetimez = date.toPyDate()        

        dateconvertdue = datetimez.strftime('%b %d, %Y')
        
        datedueyo = str(dateconvertdue)            
   
    def button(self, name):
        buttonRED = QtGui.QPushButton(self, name)
        buttonRED.clicked.connect(self.button_click(shost))
        
    def button_click(self):
        # shost is a QString object
        shost = clientnameEdit.text()
        print shost
        
##################################################################
########## End of all that good stuff. ###########################
##################################################################

        

#  End of Program -- Below Line Executes Program
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
