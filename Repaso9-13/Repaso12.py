# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Repaso12.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(738, 663)
        self.actAbrir = QAction(MainWindow)
        self.actAbrir.setObjectName(u"actAbrir")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actAbrir.setIcon(icon)
        self.actGuardar = QAction(MainWindow)
        self.actGuardar.setObjectName(u"actGuardar")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actGuardar.setIcon(icon1)
        self.actSalir = QAction(MainWindow)
        self.actSalir.setObjectName(u"actSalir")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.actSalir.setIcon(icon2)
        self.actionMostrar = QAction(MainWindow)
        self.actionMostrar.setObjectName(u"actionMostrar")
        self.actionOcultar = QAction(MainWindow)
        self.actionOcultar.setObjectName(u"actionOcultar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 738, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)
        self.dockPlaylist = QDockWidget(MainWindow)
        self.dockPlaylist.setObjectName(u"dockPlaylist")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.lstPlaylist = QListWidget(self.dockWidgetContents)
        QListWidgetItem(self.lstPlaylist)
        QListWidgetItem(self.lstPlaylist)
        QListWidgetItem(self.lstPlaylist)
        self.lstPlaylist.setObjectName(u"lstPlaylist")
        self.lstPlaylist.setGeometry(QRect(100, 60, 256, 201))
        self.dockPlaylist.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.dockPlaylist)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menuArchivo.addAction(self.actAbrir)
        self.menuArchivo.addAction(self.actGuardar)
        self.menuArchivo.addAction(self.actSalir)
        self.menuVer.addAction(self.actionMostrar)
        self.menuVer.addAction(self.actionOcultar)
        self.toolBar_2.addAction(self.actAbrir)
        self.toolBar_2.addAction(self.actGuardar)
        self.toolBar_2.addAction(self.actSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir...", None))
#if QT_CONFIG(statustip)
        self.actAbrir.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir un archivo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(statustip)
        self.actGuardar.setStatusTip(QCoreApplication.translate("MainWindow", u"Guardar el archivo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(statustip)
        self.actSalir.setStatusTip(QCoreApplication.translate("MainWindow", u"Cerrrar la aplicaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.actionOcultar.setText(QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.dockPlaylist.setWindowTitle(QCoreApplication.translate("MainWindow", u"Playlist", None))

        __sortingEnabled = self.lstPlaylist.isSortingEnabled()
        self.lstPlaylist.setSortingEnabled(False)
        ___qlistwidgetitem = self.lstPlaylist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"cancion_1.wav", None));
        ___qlistwidgetitem1 = self.lstPlaylist.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"cancion_2.wav", None));
        ___qlistwidgetitem2 = self.lstPlaylist.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"cancion_3.wav", None));
        self.lstPlaylist.setSortingEnabled(__sortingEnabled)

    # retranslateUi

