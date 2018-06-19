'''
Created on Jun 19, 2018

@author: xiongan2
'''
import sys
import random
from PySide2.QtWidgets import QApplication, QLabel, QMessageBox, QPushButton, QDialog, QLineEdit, QVBoxLayout
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWebEngineWidgets import QWebEngineView

def hello_label():
    app = QApplication([])
    label = QLabel("Hello World")
    label.show()
    sys.exit(app.exec_())                 
    
def hello_label2():
    app = QApplication(sys.argv)
    #label = QLabel("Hello World!")
    label = QLabel("<font color=red size=40>Hello World!</font>")
    label.show()
    app.exec_()  

def hello_QML():
    app = QApplication([])
    view = QQuickView()
    url = QUrl("view.qml")
    
    view.setSource(url)
    view.show()
    app.exec_()  
############################################################################################    
def test_msg_box():
    app = QApplication(sys.argv)

    # Create a simple dialog box
    msg_box = QMessageBox()
    msg_box.setText("Hello World!")
    msg_box.show()
    
    sys.exit(msg_box.exec_())
############################################################################################    
def say_hello():                                                                                     
    print("Button clicked, Hello!") 
    
def test_push_button():                                                                                            
    # Create the Qt Application                                                                         
    app = QApplication(sys.argv)                                                                        
    # Create a button, connect it and show it                                                           
    button = QPushButton("Click me")                                                                    
    button.clicked.connect(say_hello)                                                                    
    button.show()                                                                                       
    # Run the main Qt loop                                                                              
    app.exec_()
    
def test_push_button_exit():
        # Create a QApplication
    app = QApplication([])

    # Create a button
    button = QPushButton('Exit')

    # Connect the button "clicked" signal to the exit() method
    # that finishes the QApplication
    button.clicked.connect(app.exit)

    button.show()
    app.exec_()
############################################################################################        
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = ['Hallo Welt', 'Hello World']

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))
    
def test_widget():
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
############################################################################################    
class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print("Hello %s" % self.edit.text())

def test_form():
    app = QtWidgets.QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
    

                                
if __name__ == "__main__":
    #hello_label2()
    #hello_QML()
    #test_msg_box()
    #test_push_button()
    #test_push_button_exit()
    #test_widget()
    test_form()
