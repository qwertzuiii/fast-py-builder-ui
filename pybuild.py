import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import json
import threading
import pybuild_ui as pui

buildfile = "build.json"

def load_json(jsonfile):
    """Returns a json file as a Dictionary"""
    return json.loads(open(jsonfile, 'r').read())


class MainApp(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uifile = pui.get_ui()
        uic.loadUi(uifile, self)  # ui file load
        pui.rem_ui()
        self.setWindowIcon(QIcon())  # Icon Loading

        self.valid_command = None

        if os.path.exists(buildfile):
            self.line_BuildJson.setText(os.path.abspath(buildfile))
            self.buildfile_load()


        #self.line_Command.setEnabled(False)
        self.btn_Build.clicked.connect(self.start)
        self.btn_Apply.clicked.connect(self.buildfile_load_cstm)
        self.combo_FileType.currentTextChanged.connect(self.onefile_changed)
    
    def buildfile_load(self):
        j = load_json(buildfile)
        self.line_File.setText(j['$file'])
        self.generating_command(j)
    
    def buildfile_load_cstm(self):
        try:
            j = load_json(self.line_BuildJson.text())
        except FileNotFoundError:
            i = 'Build.json file not found!'
            print(i)
            self.line_Command.setPlainText(i)
            self.valid_command = False
            return
        except json.decoder.JSONDecodeError:
            i = 'Build.json file is not a valid json file!'
            print(i)
            self.line_Command.setPlainText(i)
            self.valid_command = False
            return
        self.generating_command(j)

    def generating_command(self, js):
        add_data = ""
        for file in js['$add-data']:
            add_data += ' --add-data "{}"'.format(file)
        
        if not js['$icon']:
            icon = ''
        else:
            icon = ' --icon "{}"'.format(js['$icon'])
        
        if not js['$name']:
            name = ''
        else:
            name = ' --name "{}"'.format(js['$name'])
        
        if js['$seeconsole']:
            console = 'console'
        else:
            console = 'windowed'
        
        file = '  ' + js['$file']

        onefile_index = self.combo_FileType.currentIndex()
        #print(onefile_index)

        if onefile_index == 0:
            onefile = "onefile"
        elif onefile_index == 1:
            onefile = "onedir"

        command = f'pyinstaller --noconfirm --{onefile} --{console}{icon}{name}{add_data}{file}'

        #self.line_Command.setText(command)  # FOR QLINEEDIT
        self.line_Command.setPlainText(command)  # FOR QPLAINTEXTEDIT
        self.valid_command = True
    
    def onefile_changed(self, value):
        self.buildfile_load()
    
    def start(self):
        if self.valid_command == None:
            print('Cannot start building! (valid_command == None)')
            return
        elif not self.valid_command:
            print('Cannot start building! (valid_command == False)')
            return

        x = threading.Thread(target=self.start_th)
        x.start()
    
    def start_th(self):
        command = self.line_Command.toPlainText()
        os.system(command)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appMain = MainApp()
    appMain.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Exiting...')