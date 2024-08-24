
from PyQt5.QtWidgets import QApplication

App = QApplication([])

App.setStyleSheet("""
    QPushButton {
        background-color: green;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        font-family: tahoma;
    }
                  
    QPushButton:hover {
      background-color: lightgreen;
      color: black;                  
    }
    
    QSpinBox, QListWidget {
        padding: 5px;
        font-family: tahoma;
        border: 1px solid black;
        font-size: 14px;
                  }
    QRadioButton {
        font-size: 14px;
        padding: 5px;
        font-family: tahoma;
    }
    QRadioButton:hover {
        color:darkblue;
    }
    
    QListWidget{
        padding: 5px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 10px;
        border: 2px solid #4CAF50;
        color:black;
    }
    QGroupBox {
        font-size: 18px;
        border: 2px solid #4CAF50; /* Green border */
        border-radius: 10px;
    }
    QFormLayout {
        text-size: 16px;
        text-weight: bold;
    }
                               
  """)