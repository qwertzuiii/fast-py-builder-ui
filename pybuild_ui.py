xml = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>541</width>
    <height>312</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>541</width>
    <height>312</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>541</width>
    <height>312</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Py-Build</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QGroupBox" name="group_File">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>521</width>
      <height>51</height>
     </rect>
    </property>
    <property name="title">
     <string>File</string>
    </property>
    <widget class="QLineEdit" name="line_File">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>501</width>
       <height>21</height>
      </rect>
     </property>
     <property name="placeholderText">
      <string notr="true">File Path</string>
     </property>
    </widget>
   </widget>
   <widget class="QGroupBox" name="group_BuildJson">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>521</width>
      <height>51</height>
     </rect>
    </property>
    <property name="title">
     <string>Build.json</string>
    </property>
    <widget class="QLineEdit" name="line_BuildJson">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>421</width>
       <height>21</height>
      </rect>
     </property>
     <property name="placeholderText">
      <string notr="true">build.json</string>
     </property>
    </widget>
    <widget class="QPushButton" name="btn_Apply">
     <property name="geometry">
      <rect>
       <x>440</x>
       <y>20</y>
       <width>75</width>
       <height>21</height>
      </rect>
     </property>
     <property name="text">
      <string>Apply</string>
     </property>
    </widget>
   </widget>
   <widget class="QGroupBox" name="group_OneFileOrDirectory">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>130</y>
      <width>521</width>
      <height>51</height>
     </rect>
    </property>
    <property name="title">
     <string>One File / Directory</string>
    </property>
    <widget class="QComboBox" name="combo_FileType">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>501</width>
       <height>22</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>One File</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Directory</string>
      </property>
     </item>
    </widget>
   </widget>
   <widget class="QPushButton" name="btn_Build">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>280</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Build</string>
    </property>
   </widget>
   <widget class="QGroupBox" name="group_Command">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>190</y>
      <width>521</width>
      <height>81</height>
     </rect>
    </property>
    <property name="title">
     <string>Command</string>
    </property>
    <widget class="QPlainTextEdit" name="line_Command">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>501</width>
       <height>51</height>
      </rect>
     </property>
     <property name="readOnly">
      <bool>true</bool>
     </property>
     <property name="plainText">
      <string notr="true"/>
     </property>
     <property name="placeholderText">
      <string>Command</string>
     </property>
    </widget>
   </widget>
   <widget class="QPushButton" name="btn_batch">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>280</y>
      <width>111</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Create Batch File</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

import tempfile, os

temp_path = tempfile.gettempdir() + "\\"

p = temp_path + '.pybuild.xml'

def get_ui():
    with open(p, 'wb') as uif:
        uif.write(xml.encode())
    return p

def rem_ui():
    os.remove(p)