import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QVBoxLayout,QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import  QDateTime
from Streaming import Streaming 




from System import Check_Access,Get_Code,Preprocess,Registre,generate_qr_code,generate_random_data,Add_New_User


class Window0(QDialog):
    def __init__(self):
        super(Window0,self).__init__()
        loadUi('Window0.ui',self)
    
        self.addImage()
        self.Registere_Button.clicked.connect(self.Registere)
        self.Join_Button.clicked.connect(self.Join)
        
        
        self.Home_Button.clicked.connect(self.Home)
        self.AboutUs_Button.clicked.connect(self.AboutUs)
        self.Contact_Button.clicked.connect(self.Contact)
        
        

    def addImage(self):
        Image_pxmap = QPixmap('Window0_Image.png')
        self.Background_Label.setPixmap(Image_pxmap)
               
    def Registere(self):
        widget.setCurrentIndex(1)
    
    def Join(self):
        widget.setCurrentIndex(5)
    
    def Home(self):
        self.showFullScreen()
        widget.setCurrentIndex(0)   
    def AboutUs(self):
        pass
    def Contact(self):
        widget.setCurrentIndex(4)
        
        
#######################################################################################       
#######################################################################################  
class Window1(QDialog):
    def __init__(self):
        super(Window1,self).__init__()
        loadUi('Window1.ui',self)
        self.addImage()
        
        self.Start_Streaming()
 
        self.Capture_Button.clicked.connect(self.Capture)
        self.Continue_Button.clicked.connect(self.Continue)
        self.Restart_Button.clicked.connect(self.Restart)
        self.Home_Button.clicked.connect(self.Home)
        self.AboutUs_Button.clicked.connect(self.AboutUs)
        self.Contact_Button.clicked.connect(self.Contact)
        
    def addImage(self):
        Image_pxmap = QPixmap('Window1_Image.png')
        self.Background_Label.setPixmap(Image_pxmap)
    
    def Start_Streaming(self):
            self.streaming_widget = Streaming()
            self.streaming_layout = QVBoxLayout(self.Camera_widget)
            self.streaming_layout.setContentsMargins(0, 0, 0, 0)
            self.streaming_layout.addWidget(self.streaming_widget)
           
    def Capture(self):
        # Capture the current frame from the streaming widget
        self.frame = self.streaming_widget.viewfinder.grab()
        print('The farme has been saved')
        # Stop the streaming
        self.streaming_widget.camera.stop()
     
    def Continue(self):
        Image = Preprocess(self.frame)
        Code = Get_Code(Image)
        Result = Check_Access(Code)
        print(Result)
        widget.setFixedWidth(600)
        widget.setFixedHeight(350)
        
        if Result :
            current_datetime = QDateTime.currentDateTime()
            # Registre the User in the Database 
            Registre(Result)
            
            
            # Edit Dialog-window
            Window22.User_Message.setText('Known')
            Window22.Name_Message.setText(Result[1])
            current_datetime = QDateTime.currentDateTime()
            formatted_datetime = current_datetime.toString("yyyy-MM-dd hh:mm:ss")
            Window22.DateTime_Message.setText(formatted_datetime)
            widget.setCurrentIndex(3)
        else :
            Window21.User_Message.setText('Uknown')
            Window21.Name_Message.setText('**********')
            Window21.DateTime_Message.setText('**************')
            widget.setCurrentIndex(2)
        

    
    def Restart(self):
        # Restart the streaming by hiding and showing the Streaming widget
        self.streaming_widget.camera.stop()
        self.streaming_widget.viewfinder.setVisible(False)
        self.streaming_widget.camera.start()
        self.streaming_widget.viewfinder.setVisible(True)
        
    def Home(self):
        widget.setCurrentIndex(0)  
         
    def AboutUs(self):
        pass
    def Contact(self):
        widget.setCurrentIndex(4)
        
#######################################################################################  
#######################################################################################  
class Window21(QDialog):
    def __init__(self):
        super(Window21,self).__init__()
        loadUi('Window21.ui',self)
        self.addImage()
        self.Home_Button.clicked.connect(self.Home)
        self.Contact_Button.clicked.connect(self.Contact)
       
        
      
        
    def addImage(self):
        Image_pxmap = QPixmap('Window21_Image.png')
        self.Background_Label.setPixmap(Image_pxmap)
    
    def Home(self):
        widget.setFixedWidth(1600)
        widget.setFixedHeight(800)
        widget.setCurrentIndex(0)   
    
    def Contact(self):
        widget.setFixedWidth(1600)
        widget.setFixedHeight(800)
        widget.setCurrentIndex(4)
        
#######################################################################################  
####################################################################################### 
class Window22(QDialog):
    def __init__(self):
        super(Window22,self).__init__()
        loadUi('Window22.ui',self)
        self.addImage()
        self.Home_Button.clicked.connect(self.Home)
        self.Contact_Button.clicked.connect(self.Contact)
      
        
      
        
    def addImage(self):
        Image_pxmap = QPixmap('Window22_Image.png')
        self.Background_Label.setPixmap(Image_pxmap)
    
    def Home(self):
        widget.setFixedWidth(1600)
        widget.setFixedHeight(800)
        widget.setCurrentIndex(0)   
    
    def Contact(self):
        widget.setFixedWidth(1600)
        widget.setFixedHeight(800)
        widget.setCurrentIndex(4)


#######################################################################################  
####################################################################################### 
class Contact(QDialog):
    def __init__(self):
        super(Contact,self).__init__()
        loadUi('Contact.ui',self)
    
        self.addImage()
        self.Submit_Button.clicked.connect(self.Submit)
        
        self.Home_Button.clicked.connect(self.Home)
        self.AboutUs_Button.clicked.connect(self.AboutUs)
        self.Contact_Button.clicked.connect(self.Contact)
        
        self.Email_Edit.textChanged.connect(self.on_text_changed)
        self.Message_Edit.textChanged.connect(self.on_text_changed)
        
        
        

    def addImage(self):
        Image_pxmap = QPixmap('Contact_Image.png')
        self.Background_Label.setPixmap(Image_pxmap)
        
    def on_text_changed(self):
        sender = self.sender()  # Get the sender of the signal

        if sender.text():
            sender.setStyleSheet("background-color:  rgb(174, 233, 255); border : 3px solid rgb(53, 218, 255);border-radius:10px;")
        else:
            sender.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0)); border : 3px solid rgb(255, 255, 255);border-radius:10px;")
               
    def Submit(self):
        pass
    
    def Home(self):
        widget.setCurrentIndex(0)   
    def AboutUs(self):
        pass
    def Contact(self):
        widget.setCurrentIndex(4)
   
        
#######################################################################################  
####################################################################################### 
#class AboutUs

#######################################################################################  
####################################################################################### 
class Join(QDialog):
    def __init__(self):
        super(Join,self).__init__()
        loadUi('Join.ui',self)
        self.addImage()
        self.QR_Image = None
        self.Home_Button.clicked.connect(self.Home)
        self.AboutUs_Button.clicked.connect(self.AboutUs)
        self.Contact_Button.clicked.connect(self.Contact)
        
        self.Name_Edit.textChanged.connect(self.on_text_changed)
        self.Generate_Button.clicked.connect(self.Generate)
        self.Download_Button.clicked.connect(self.Download)
       
        
      
        
    def addImage(self):
        Image_pxmap = QPixmap('Join_Image.png')
        self.Background_Label.setPixmap(Image_pxmap)
        
    def on_text_changed(self):
        sender = self.sender()  # Get the sender of the signal

        if sender.text():
            sender.setStyleSheet("background-color:  rgb(174, 233, 255); border : 3px solid rgb(53, 218, 255);border-radius:10px;")
        else:
            sender.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0)); border : 3px solid rgb(255, 255, 255);border-radius:10px;")
    
    def Generate(self):
        Code = generate_random_data(8)
        self.QR_Image = generate_qr_code(Code)
        
        
        # Add The New User to Database:
        Name = self.Name_Edit.text()
        Add_New_User(Name,Code)
        
        # Save the Pillow Image to a file (e.g., PNG format)
        self.QR_Image.save(Name+".png")
        
        
        # Display The QR_Code:
        Image_pxmap = QPixmap(Name+".png")
        self.QrCode_Label.setPixmap(Image_pxmap)
        self.QrCode_Label.setScaledContents(True)  # This line ensures aspect ratio is preserved
        
        # Delete the file from storage after displaying it
        os.remove(Name+".png")
    
    def Download(self):

        # Get the user's name
        Name = self.Name_Edit.text()

        # Prompt the user to select the save location and filename
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Allow the user to select a location
        save_path, _ = QFileDialog.getSaveFileName(self, "Save QR Code Image", f"{Name}.png", "PNG Files (*.png);;All Files (*)", options=options)

        if save_path:
            # Save the Pillow Image to the specified location
            self.QR_Image.save(save_path)
 

        
    
    def Home(self):
        # Cleare the Name_Edit
        self.Name_Edit.clear()
        # Clear the QrCode_Label
        self.QrCode_Label.setPixmap(QPixmap())  # Set an empty pixmap
        
        widget.setCurrentIndex(0)   
        
    def AboutUs(self):
        pass
    def Contact(self):
        widget.setCurrentIndex(4)
        



#######################################################################################  
####################################################################################### 














     
app = QApplication(sys.argv)

Window0  = Window0()
Window1  = Window1() 
Window21 = Window21()
Window22 = Window22()
Contact  = Contact()
Join     = Join()

widget = QtWidgets.QStackedWidget()

widget.addWidget(Window0)
widget.addWidget(Window1)
widget.addWidget(Window21)
widget.addWidget(Window22)
widget.addWidget(Contact)
widget.addWidget(Join)

widget.setFixedWidth(1600)
widget.setFixedHeight(800)
widget.show()

app.exec()
        
    
            
        
    
   
        
        
        
        
        


        
        
        



































