# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       Conversor_ui_to_py
# Autor:        Ing. Guillermo G. Guzmán
# Creado:       26 de Junio 2023
# Modificado:   27 de Julio 2023
# Copyright:    (c) 2023 by Ing. Guillermo G. Guzmán, 2023
# License:      a definir
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
Aplicación que convierte archivos ui en archivos py
"""

# Versión Python: 3.8.8
# Versión PyQt5: 5.15.2

import locale
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog
from PyQt5.QtCore import QProcess

from ui_conversor_ui_to_py import *


class UiConversor(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.archivo = ""
        self.nombre_archivo = ""
        self.direccion = ""
        self.ruta = ""

        self.setupUi(self)

        # ================Centrar Ventana =======================
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        self.move(qt_rectangle.topLeft())
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        # Configuramos el locale para Argentina
        locale.setlocale(locale.LC_ALL, '')

        self.lbl_mensaje.setHidden(True)
        self.bt_convertir.setEnabled(False)
        self.bt_abrir.clicked.connect(self.abrir_archivo)
        self.bt_convertir.clicked.connect(self.convertir_archivo)

    def abrir_archivo(self) -> None:
        """
        Abre un QFileDialog para seleccionar el archivo a convertir
        """
        self.lbl_mensaje.setHidden(True)
        self.txt_direccion.setText("")
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, "Abrir archivo", filter="*.ui")
        # print(len(file_path[0]))
        if len(file_path[0]):
            try:
                directorios = file_path[0].split("/")
                self.archivo = directorios[-1].split(".")
                directorios.pop()
                self.nombre_archivo = self.archivo[0]
                self.ruta = "/".join(directorios) + "/"
                # print(self.ruta)
                # print(self.nombre_archivo)
                self.txt_direccion.setText(file_path[0])
                self.bt_convertir.setEnabled(True)

            except Exception as error:
                print(error)

    def convertir_archivo(self):
        # print(len(self.ruta))
        if len(self.ruta):
            aplicacion = 'pyuic5 "' + self.ruta + self.nombre_archivo + '.ui" -o "' \
                         + self.ruta + 'ui_' + self.nombre_archivo + '.py"'
            try:
                process = QProcess(self)
                # print(aplicacion)
                process.startDetached(aplicacion)
                self.bt_convertir.setEnabled(False)
                self.lbl_mensaje.setHidden(False)
            except Exception as error:
                print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = UiConversor()
    ui.show()
    app.exec_()
