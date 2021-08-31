# GUI Application automation and testing library
# Copyright (C) 2006-2018 Mark Mc Mahon and Contributors
# https://github.com/pywinauto/pywinauto/graphs/contributors
# http://pywinauto.readthedocs.io/en/latest/credits.html
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of pywinauto nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -*- coding: UTF-8 -*-
"""Run some automations to test things"""
from __future__ import unicode_literals
from __future__ import print_function

from pywinauto import application

#from pywinauto import tests
#from pywinauto.findbestmatch import MatchError

#
# # application.set_timing(3, .5, 10, .5, .4, .2, .2, .1, .2, .5)
# app = application.Application()
# app.connect("SciTEWindow")
# # app["WindowsForms10.Window.8.app.0.378734a"]["WindowsForms10.EDIT.app.0.378734a4"].set_edit_text("fasfsf")
# # app["WindowsForms10.Window.8.app.0.378734a"]["WindowsForms10.BUTTON.app.0.378734a11"].click()
# app['SciTEWindow'][''].click()
#
# exit(1)

# application.set_timing(3, .5, 10, .5, .4, .2, .2, .1, .2, .5)
app = application.Application(backend="uia")
app.connect(path=r"K:\develop\KlST\SPA\HC32L136_SDK\编程工具\(EXE)HDSC Programmer Config Tool_v2.4.4\(EXE)HDSC Programmer Config Tool_v2.4.4")
# app["WindowsForms10.Window.8.app.0.378734a"]["WindowsForms10.BUTTON.app.0.378734a2"].set_edit_text("fasfsf")
# app["WindowsForms10.Window.8.app.0.378734a"]["WindowsForms10.BUTTON.app.0.378734a11"].click()
# app['WindowsForms10.Window.8.app.0.378734a'].wait('ready')
# app['HDSC Programmer Config Tool']['Edit4'].set_text("sdad")
app['HDSC Programmer Config Tool']['Edit4'].set_text("sdad")
app['HDSC Programmer Config Tool']['Edit6'].set_text("HC32L136x8/HC32L130x8")

# pywinauto.findbestmatch.MatchError: Could not find 'asdf' in 'dict_keys(['statusStrip1', 'statusStrip1StatusBar', 'StatusBar', 'Static', '请检查您的PGM是否为带屏版,带屏版才可配置此选项!', '请检查您的PGM是否为带屏版,带屏版才可配置此选项!Static', 'Static0', 'Static1', 'Static2', '2.4', '2.4Static', 'Static3', 'www.hdsc.com.cnStatic', 'www.hdsc.com.cn', 'www.hdsc.com.cn0', 'www.hdsc.com.cn1', 'www.hdsc.com.cn2', 'Hyperlink', 'www.hdsc.com.cnHyperlink', 'GroupBox', 'MCU信息GroupBox', 'FlashEdit', 'Edit', '滚码功能', 'CheckBox', '滚码功能CheckBox', 'Static4', 'FlashStatic', 'Flash', 'Static5', 'SRAM', 'SRAMStatic', 'Static6', 'XTAL', 'XTALStatic', 'Static7', '系列', '系列Static', 'Static8', '芯片名称Static', '芯片名称', 'Static9', 'MCU信息', 'MCU信息Static', 'Pane', 'MCU信息Pane', 'GroupBox0', 'GroupBox1', 'GroupBox2', '芯片名称GroupBox', 'Pane0', 'Pane1', 'Pane2', '芯片名称Pane', '选项字节设置', 'Button', '选项字节设置Button', '页擦除', 'CheckBox0', 'CheckBox1', 'CheckBox2', '页擦除CheckBox', '片擦除', 'CheckBox3', '片擦除CheckBox', 'XTAL(MHz)Edit', 'Edit0', 'Edit1', 'Edit2', 'CheckBox4', '计数(Dec)', '计数(Dec)CheckBox', '目标Hex文件Pane', 'Pane3', 'CheckBox5', '芯片加密CheckBox', '芯片加密', '复  位', 'CheckBox6', '复  位CheckBox', '供    电', 'CheckBox7', '供    电CheckBox', '文件加密', '文件加密CheckBox', 'CheckBox8', 'ComboBox256000', 'ComboBox115200', 'ComboBox76800', 'ComboBox', 'ComboBox19200', 'ComboBox128000', 'ComboBox38400', '波特率(bps)ComboBox', '打开Button', '打开', 'Button0', 'Button1', 'Button2', 'XTAL(MHz)Edit0', 'XTAL(MHz)Edit1', 'XTAL(MHz)Edit2', 'Edit3', '目标Hex文件Edit', 'Edit4', '密钥Edit', 'Edit5', '芯片名称Edit', 'Edit6', 'Static10', 'XTAL(MHz)', 'XTAL(MHz)Static', 'Static11', '目标Hex文件', '目标Hex文件Static', 'Static12', '密钥', '密钥Static', 'Static13', '波特率(bps)', '波特率(bps)Static', 'Static14', '芯片名称Static0', '芯片名称Static1', '芯片名称Static2', '芯片名称0', '芯片名称1', '芯片名称2', 'CheckBox9', '编程时写选项字节CheckBox', '编程时写选项字节', 'Static15', '版本：Static', '版本：', 'Pane4', 'FlashPane', '配置文件名Edit', 'Edit7', '确定Button', '确定', 'Button3', 'www.hdsc.com.cn3', 'GroupBox3', 'www.hdsc.com.cnGroupBox', '带屏版', 'CheckBox10', '带屏版CheckBox', 'Static16', '配置文件名Static', '配置文件名', 'TitleBar', '关闭', '关闭Button', 'Button4'])'



# statusStrip1
# 2.4
# www.hdsc.com.cn
# 滚码功能
# Flash
# SRAM
# XTAL
# 系列
# 芯片名称
# MCU信息
# 选项字节设置
# 页擦除
# 片擦除
# 计数(Dec)
# 芯片加密
# 复  位
# 供    电
# 文件加密
# 115200
# XTAL(MHz)
# 目标Hex文件
# 密钥
# 波特率(bps)
# 芯片名称
# 编程时写选项字节
# 版本：
# 确定
# 带屏版
# 配置文件名

exit(1)


app = application.Application()
app.start(r"notepad.exe")

app['Notepad'].wait('ready')
# app['Notepad'].print_control_identifiers
# app.Properties.print_control_identifiers()
# app['Notepad'].click("文件->页面设置")
# exit(1)
app['Notepad'].menu_select("文件->页面设置")
app['页面设置']['Button6'].click()
exit(1)



# ----- Page Setup Dialog ----
# Select the 4th combobox item
app['文本编辑器']['ExpandByDef'].check()

# Select the 'Letter' combobox item
app['页面设置']['ComboBox1'].select("信封")

# ----- Next Page Setup Dialog ----
# app['页面设置']['确定'].click()

# app['页面设置']['Network'].click()

# ----- Connect To Printer Dialog ----
# Select a checkbox
app['ConnectToPrinter']['ExpandByDef'].check()
# Uncheck it again - but use click this time!
app['ConnectToPrinter']['ExpandByDef'].click()

app['ConnectToPrinter']['OK'].close_click()

# ----- 2nd Page Setup Dialog again ----
app['PageSetupDlg2']['Properties'].click()

# ----- Document Properties Dialog ----
doc_props = app.window(name_re = ".*Document Properties")

# Two ways of selecting tabs
doc_props['TabCtrl'].select(2)
doc_props['TabCtrl'].select("Layout")

# click a Radio button
doc_props['RotatedLandscape'].click()
doc_props['Portrait'].click()

# open the Advanced options dialog in two steps
advbutton = doc_props['Advanced']
advbutton.click()

# ----- Advanced Options Dialog ----
# close the 4 windows
app.window(name_re = ".* Advanced Options")['Ok'].click()

# ----- Document Properties Dialog again ----
doc_props['Cancel'].close_click()
# ----- 2nd Page Setup Dialog again ----
app['PageSetup2']['OK'].close_click()
# ----- Page Setup Dialog ----
app['PageSetup']['Ok'].close_click()

# type some text
app['Notepad']['Edit'].set_edit_text("I am typing s\xe4me text to Notepad"
    "\r\n\r\nAnd then I am going to quit")

# exit notepad
app['NotepadDialog'].menu_select("File->Exit")
app['Notepad']['No'].close_click()

