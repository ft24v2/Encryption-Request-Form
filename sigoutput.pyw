from dtk import *
from functionsfile import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os, time, sys
import win32com.client

def printmessagebox(self):
    QMessageBox.information(self, "Something")


def printsig(ClientName, Department, OSversion, modelresult, serialresult, freespaceresult, smartresult, NotesInput):
    
    

    if not os.path.exists('..\\WorkOrders\\{}-{}-{}'.format(ClientName, Department, str(hostname))):
        os.makedirs('..\\WorkOrders\\{}-{}-{}'.format(ClientName, Department, str(hostname)))
       
    def mappeddrives():
        
        print "Processing Mapped Drives"
        strComputer = "." 
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
        colItems = objSWbemServices.ExecQuery("Select * from Win32_MappedLogicalDisk")
        
        for objItem in colItems:     
            my_file.write("=== Share: {}{} ===".format(objItem.Caption,objItem.ProviderName))
            my_file.write("<P>Mount&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=  {}<BR>".format(objItem.Caption ))
            my_file.write(" Path&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(objItem.ProviderName))
            my_file.write(" Share Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(objItem.VolumeName))
            my_file.write("  <BR>")
            
    def printerslist():
        
        print "Processing Printers"
          
        
        strComputer = "."
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_PrinterConfiguration")
        
        for objItem in colItems:

            
            my_file.write("=== Printer: {} ===".format(objItem.DeviceName))
            my_file.write("<P>Name &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=  {}<BR>".format(objItem.Caption))
            my_file.write(" Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(objItem.Description))
            my_file.write(" Driver Version&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(objItem.DriverVersion))
            my_file.write(" Name    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}".format(objItem.Name))
            my_file.write("<br>")
            
    def programslistyo():

        print "Processing Programs (May take a bit)"
       

        
        strComputer = "." 
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Product")

        for objItem in colItems:
            productname = objItem.Caption.encode("utf-8")
            description = objItem.Description.encode("utf-8")
            installdate = objItem.InstallDate.encode("utf-8")
            productsname = objItem.Name.encode("utf-8")
            vendor = objItem.Vendor.encode("utf-8")
            productversion = objItem.Version.encode("utf-8")

            my_file.write("<p>")
            my_file.write("&nbsp;&nbsp;&nbsp;==== {} ===== <br>".format(productname))
            my_file.write("Description:  {} <br>".format(description))
            my_file.write("Install Date: {} <br>".format(installdate))
            my_file.write("Name:         {} <br>".format(productsname))
            my_file.write("Vendor:       {} <br>".format(vendor))
            my_file.write("Version:      {} <br>".format(productversion))
           
        print "Making Log"
        
    with open('..\\WorkOrders\\{}-{}-{}\\Output.htm'.format(ClientName, Department, str(hostname)), "w") as my_file:
        my_file.write("<html>")
        my_file.write("<head>")
        my_file.write("<title>{} Summary</title>".format(str(hostname)))
        my_file.write("<STYLE type=""text/css"">")
        my_file.write("")
        my_file.write("")
        my_file.write("   H1 { border-style:solid; border-width:1px 2px 2px 1px; font-size: large}")
        my_file.write("   H2 { font-size: medium; margin-top: 6 px; margin-bottom: 2 px; border-bottom-style:solid; border-bottom-width: 1 px}")  
        my_file.write("  P {font-family: Lucida Console; font-size:medium; margin-top: 2 px; margin-bottom: 6 px}")
        my_file.write("textarea {font-family: Lucida Console; font-size:medium}")
        my_file.write("#pFooter {text-align:right; font-size:small}")
        my_file.write("    TABLE.tableDetail {border-collapse: collapse; border-style: solid; border-width: 1px; border-color: Black; width: 100%; font-family: Lucida Console; font-size:xx-small}")
        my_file.write("    THEAD.theadDetail {border-color: White; border-width: 1px; font-weight:bold; text-align:center; background-color:Black; color: White}") 
        my_file.write("    TH.thDetail {border-color: White; border-width: 1px; border-style: solid} ")
        my_file.write("    TD.tdDetail {border-color: Black; border-width: 1px; border-style: solid; text-align:left}")
        my_file.write("    TD.tdDetailCenter {border-color: Black; border-width: 1px; border-style: solid; text-align:center}")
        my_file.write("   ")
        my_file.write("    @media print ")
        my_file.write("    {")
        my_file.write("        #tblToolBar, #hrToolBar {display: none}")
        my_file.write("        THEAD.theadDetail {display: table-header-group; border-color: Black; background-color:White; color: Black}")
        my_file.write("        TH.thDetail {border-color: Black}")
        my_file.write("    }")
        my_file.write("  ")
        my_file.write("</STYLE>")
        my_file.write("</head>")
        my_file.write("<body>")
        my_file.write("<H1 id=""h1Header"">{}</H1>".format(str(hostname)))
        my_file.write("<H2 id=""h2General"">General Information</H2>")
        my_file.write("<P id=""pGeneral"">")

        my_file.write("Hostname &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(str(hostname)))
        my_file.write("OS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(OSversion))
        my_file.write("Model Number &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(modelresult))
        my_file.write("Serial Number&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(str(serialresult)))
        my_file.write("Free Space&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(str(freespaceresult)))
        my_file.write("S.M.A.R.T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {}<BR>".format(str(smartresult)))
        my_file.write("<H2 id=""NOTESSS"">Notes</H2>")
        my_file.write("{}".format(NotesInput))
        my_file.write("<br>")


        
        my_file.write("<H2 id=""h2Hardware"">Mapped Drives</H2>")
# Here we define the mapped drives part
        mappeddrives()
    
        my_file.write("</P>")
        my_file.write("<H2 id=""h2Storage"">Installed Printers</H2>")
# Here we enter the Printers 
        my_file.write("<P id=""pStorage"">")
        my_file.write("")
        printerslist()
        
        my_file.write("</P>")
        my_file.write("<H2 id=""h2Network"">Installed Programs</H2>")
# Here we put da Programs 
        my_file.write("<P id=""pNetwork"">&nbsp;</P>")
        programslistyo()
        my_file.write("</body>")
        my_file.write("</html>")

                       
        print "DONE!"

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()
        
