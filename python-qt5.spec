%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define _disable_lto 1
%define _disable_ld_no_undefined 1
%define major %(echo %{version} |cut -d. -f1-2)

Summary:	Set of Python bindings for Trolltech's Qt application framework
Name:		python-qt5
Version:	5.10.1
Release:	1
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		http://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0:	https://downloads.sourceforge.net/project/pyqt/PyQt5/PyQt-%{major}/PyQt5_gpl-%{version}.tar.gz
#Patch1:		PyQt5_gpl-5.6-dbus_ftbfs.patch
BuildRequires:	python-sip >= 4.19
BuildRequires:	qmake5
%if %mdvver >= 201500
BuildRequires:	qt5-qtbase-macros
%else
BuildRequires:	qt5-macros
%endif
BuildRequires:	sed
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(Qt5Bluetooth)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Location)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5MultimediaWidgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5NetworkAuth)
BuildRequires:	pkgconfig(Qt5Nfc)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Positioning)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Sensors)
BuildRequires:	pkgconfig(Qt5SerialPort)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5WebChannel)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineCore)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5WebSockets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5XmlPatterns)
BuildRequires:	pkgconfig(Qt5X11Extras)
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-dbus = %{EVRD}
Requires:	%{name}-bluetooth = %{EVRD}
Requires:	%{name}-designer = %{EVRD}
Requires:	%{name}-enginio = %{EVRD}
Requires:	%{name}-gui = %{EVRD}
Requires:	%{name}-location = %{EVRD}
Requires:	%{name}-multimedia = %{EVRD}
Requires:	%{name}-multimediawidgets = %{EVRD}
Requires:	%{name}-network = %{EVRD}
Requires:	%{name}-nfc = %{EVRD}
Requires:	%{name}-opengl = %{EVRD}
Requires:	%{name}-positioning = %{EVRD}
Requires:	%{name}-printsupport = %{EVRD}
Requires:	%{name}-qml = %{EVRD}
Requires:	%{name}-quick = %{EVRD}
Requires:	%{name}-quickwidgets = %{EVRD}
Requires:	%{name}-sensors = %{EVRD}
Requires:	%{name}-serialport = %{EVRD}
Requires:	%{name}-sql = %{EVRD}
Requires:	%{name}-svg = %{EVRD}
Requires:	%{name}-test = %{EVRD}
Requires:	%{name}-webchannel = %{version}
Requires:	%{name}-webenginecore = %{EVRD}
Requires:	%{name}-webenginewidgets = %{EVRD}
Requires:	%{name}-webkit = %{EVRD}
Requires:	%{name}-webkitwidgets = %{EVRD}
Requires:	%{name}-websockets = %{EVRD}
Requires:	%{name}-widgets = %{EVRD}
Requires:	%{name}-xml = %{EVRD}
Requires:	%{name}-xmlpatterns = %{EVRD}
Requires:	%{name}-x11extras = %{EVRD}
Provides:	PyQt5 = %{EVRD}

%description
PyQt is a set of Python bindings for Trolltech's Qt application framework.

%files

#------------------------------------------------------------

%package core
Summary:	PyQt 5 core
Group:		Development/KDE and Qt

%description core
PyQt 5 core.

%files core
%dir %{py_platsitedir}/PyQt5
%{py_platsitedir}/PyQt5/uic
%{py_platsitedir}/PyQt5/__init__.py*
%{py_platsitedir}/PyQt5/Qt.so
%{py_platsitedir}/PyQt5/QtCore.so
%{py_platsitedir}/PyQt5/QtCore.pyi
%{_datadir}/sip/PyQt5/QtCore
%{_qt5_datadir}/qsci/api/python/PyQt5.api

#------------------------------------------------------------

%package dbus
Summary:	PyQt 5 dbus
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description dbus
PyQt 5 dbus.

%files dbus
%{py_platsitedir}/PyQt5/QtDBus.so
%{py_platsitedir}/PyQt5/QtDBus.pyi
%{py_sitedir}/dbus/mainloop/pyqt5.so
%{_datadir}/sip/PyQt5/QtDBus

#------------------------------------------------------------

%package designer
Summary:	PyQt 5 designer
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description designer
PyQt 5 designer.

%files designer
%{py_platsitedir}/PyQt5/QtDesigner.so
%{py_platsitedir}/PyQt5/QtDesigner.pyi
%{_datadir}/sip/PyQt5/QtDesigner

#------------------------------------------------------------

%package bluetooth
Summary:	PyQt 5 bluetooth
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description bluetooth
PyQt 5 bluetooth.

%files bluetooth
%{py_platsitedir}/PyQt5/QtBluetooth.so
%{py_platsitedir}/PyQt5/QtBluetooth.pyi
%{_datadir}/sip/PyQt5/QtBluetooth

#------------------------------------------------------------


%package enginio
Summary:        PyQt 5 enginio
Group:          Development/KDE and Qt
Requires:       %{name}-core = %{EVRD}

%description enginio
PyQt 5 enginio (cloud storage)

%files enginio
%{py_platsitedir}/PyQt5/Enginio.so
%{py_platsitedir}/PyQt5/Enginio.pyi
%{_datadir}/sip/PyQt5/Enginio

#------------------------------------------------------------

%package gui
Summary:	PyQt 5 gui
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description gui
PyQt 5 gui.

%files gui
%{py_platsitedir}/PyQt5/QtGui.so
%{py_platsitedir}/PyQt5/QtGui.pyi
%{py_platsitedir}/PyQt5/_QOpenGLFunctions_*.so
%{_datadir}/sip/PyQt5/QtGui

#------------------------------------------------------------

%package network
Summary:	PyQt 5 network
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description network
PyQt 5 network.

%files network
%{py_platsitedir}/PyQt5/QtNetwork.so
%{py_platsitedir}/PyQt5/QtNetwork.pyi
%{_datadir}/sip/PyQt5/QtNetwork

#------------------------------------------------------------

%package networkauth
Summary:	PyQt 5 network authentication
Group:		Development/KDE and Qt
Requires:	%{name}-network = %{EVRD}

%description networkauth
PyQt 5 network authentication.

%files networkauth
%{py_platsitedir}/PyQt5/QtNetworkAuth.so
%{py_platsitedir}/PyQt5/QtNetworkAuth.pyi
%{_datadir}/sip/PyQt5/QtNetworkAuth

#------------------------------------------------------------

%package nfc
Summary:        PyQt 5 nfc
Group:          Development/KDE and Qt
Requires:       %{name}-core = %{EVRD}

%description nfc
PyQt 5 nfc.

%files nfc
%{py_platsitedir}/PyQt5/QtNfc.so
%{py_platsitedir}/PyQt5/QtNfc.pyi
%{_datadir}/sip/PyQt5/QtNfc

#------------------------------------------------------------

%package help
Summary:	PyQt 5 help
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description help
PyQt 5 help.

%files help
%{py_platsitedir}/PyQt5/QtHelp.so
%{py_platsitedir}/PyQt5/QtHelp.pyi
%{_datadir}/sip/PyQt5/QtHelp

#------------------------------------------------------------

%package location
Summary:        PyQt 5 location
Group:          Development/KDE and Qt
Requires:       %{name}-core = %{EVRD}

%description location
PyQt 5 location.

%files location
%{py_platsitedir}/PyQt5/QtLocation.so
%{py_platsitedir}/PyQt5/QtLocation.pyi
%{_datadir}/sip/PyQt5/QtLocation

#------------------------------------------------------------

%package multimedia
Summary:	PyQt 5 multimedia
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description multimedia
PyQt 5 multimedia.

%files multimedia
%{py_platsitedir}/PyQt5/QtMultimedia.so
%{py_platsitedir}/PyQt5/QtMultimedia.pyi
%{_datadir}/sip/PyQt5/QtMultimedia

#------------------------------------------------------------

%package multimediawidgets
Summary:	PyQt 5 multimediawidgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description multimediawidgets
PyQt 5 multimediawidgets.

%files multimediawidgets
%{py_platsitedir}/PyQt5/QtMultimediaWidgets.so
%{py_platsitedir}/PyQt5/QtMultimediaWidgets.pyi
%{_datadir}/sip/PyQt5/QtMultimediaWidgets

#------------------------------------------------------------

%package opengl
Summary:	PyQt 5 opengl
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description opengl
PyQt 5 opengl.

%files opengl
%{py_platsitedir}/PyQt5/QtOpenGL.so
%{py_platsitedir}/PyQt5/QtOpenGL.pyi
%{_datadir}/sip/PyQt5/QtOpenGL

#------------------------------------------------------------

%package positioning
Summary:	PyQt 5 positioning
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description positioning
PyQt 5 positioning.

%files positioning
%{py_platsitedir}/PyQt5/QtPositioning.so
%{py_platsitedir}/PyQt5/QtPositioning.pyi
%{_datadir}/sip/PyQt5/QtPositioning

#------------------------------------------------------------

%package printsupport
Summary:	PyQt 5 printsupport
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description printsupport
PyQt 5 printsupport

%files printsupport
%{py_platsitedir}/PyQt5/QtPrintSupport.so
%{py_platsitedir}/PyQt5/QtPrintSupport.pyi
%{_datadir}/sip/PyQt5/QtPrintSupport

#------------------------------------------------------------

%package qml
Summary:	PyQt 5 qml
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description qml
PyQt 5 qml.

%files qml
%{py_platsitedir}/PyQt5/QtQml.so
%{py_platsitedir}/PyQt5/QtQml.pyi
%{_qt5_plugindir}/PyQt5/libpyqt5qmlplugin.so
%{_datadir}/sip/PyQt5/QtQml

#------------------------------------------------------------

%package quick
Summary:	PyQt 5 quick
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description quick
PyQt 5 quick.

%files quick
%{py_platsitedir}/PyQt5/QtQuick.so
%{py_platsitedir}/PyQt5/QtQuick.pyi
%{_datadir}/sip/PyQt5/QtQuick

#------------------------------------------------------------

%package quickwidgets
Summary:	PyQt 5 quickwidgets
Group:		Development/KDE and Qt
Requires:	%{name}-quick = %{EVRD}

%description quickwidgets
PyQt 5 quickwidgets.

%files quickwidgets
%{py_platsitedir}/PyQt5/QtQuickWidgets.so
%{py_platsitedir}/PyQt5/QtQuickWidgets.pyi
%{_datadir}/sip/PyQt5/QtQuickWidgets


#------------------------------------------------------------

%package sensors
Summary:	PyQt 5 sensors
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description sensors
PyQt 5 sensors.

%files sensors
%{py_platsitedir}/PyQt5/QtSensors.so
%{py_platsitedir}/PyQt5/QtSensors.pyi
%{_datadir}/sip/PyQt5/QtSensors

#------------------------------------------------------------

%package serialport
Summary:	PyQt 5 serialport
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description serialport
PyQt 5 serialport.

%files serialport
%{py_platsitedir}/PyQt5/QtSerialPort.so
%{py_platsitedir}/PyQt5/QtSerialPort.pyi
%{_datadir}/sip/PyQt5/QtSerialPort

#------------------------------------------------------------

%package sql
Summary:	PyQt 5 sql
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description sql
PyQt 5 sql.

%files sql
%{py_platsitedir}/PyQt5/QtSql.so
%{py_platsitedir}/PyQt5/QtSql.pyi
%{_datadir}/sip/PyQt5/QtSql

#------------------------------------------------------------

%package svg
Summary:	PyQt 5 svg
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description svg
PyQt 5 svg.

%files svg
%{py_platsitedir}/PyQt5/QtSvg.so
%{py_platsitedir}/PyQt5/QtSvg.pyi
%{_datadir}/sip/PyQt5/QtSvg

#------------------------------------------------------------

%package test
Summary:	PyQt 5 test
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description test
PyQt 5 test.

%files test
%{py_platsitedir}/PyQt5/QtTest.so
%{py_platsitedir}/PyQt5/QtTest.pyi
%{_datadir}/sip/PyQt5/QtTest

#------------------------------------------------------------

%package       webchannel
Summary:       PyQt 5 webchannel
Group:         Development/KDE and Qt
Requires:      %{name}-core = %{EVRD}

%description   webchannel
PyQt 5 webchannel.

%files webchannel
%{python_sitearch}/PyQt5/QtWebChannel.so
%{py_platsitedir}/PyQt5/QtWebChannel.pyi
%{_datadir}/sip/PyQt5/QtWebChannel

#------------------------------------------------------------

%package webenginecore
Summary:        PyQt 5 webenginecore
Group:          Development/KDE and Qt
Requires:       %{name}-core = %{EVRD}
Requires:       %{name}-webchannel = %{EVRD}

%description webenginecore
PyQt 5 webenginecore.

%files webenginecore
%{py_platsitedir}/PyQt5/QtWebEngineCore.so
%{py_platsitedir}/PyQt5/QtWebEngineCore.pyi
%{py_platsitedir}/PyQt5/QtWebEngine.so
%{py_platsitedir}/PyQt5/QtWebEngine.pyi
%{_datadir}/sip/PyQt5/QtWebEngineCore
%dir %{_datadir}/sip/PyQt5/QtWebEngine
%{_datadir}/sip/PyQt5/QtWebEngine/*.sip

#------------------------------------------------------------

%package webenginewidgets
Summary:        PyQt 5 webenginewidgets
Group:          Development/KDE and Qt
Requires:       %{name}-core = %{EVRD}
Requires:	%{name}-webchannel = %{EVRD}

%description webenginewidgets
PyQt 5 webenginewidgets.

%files webenginewidgets
%{py_platsitedir}/PyQt5/QtWebEngineWidgets.so
%{py_platsitedir}/PyQt5/QtWebEngineWidgets.pyi
%{_datadir}/sip/PyQt5/QtWebEngineWidgets

#------------------------------------------------------------

%package webkit
Summary:	PyQt 5 Webkit
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description webkit
PyQt 5 webkit.

%files webkit
%{py_platsitedir}/PyQt5/QtWebKit.so
%{py_platsitedir}/PyQt5/QtWebKit.pyi
%{_datadir}/sip/PyQt5/QtWebKit

#------------------------------------------------------------

%package webkitwidgets
Summary:	PyQt 5 webkitwidgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description webkitwidgets
PyQt 5 webkitwidgets.

%files webkitwidgets
%{py_platsitedir}/PyQt5/QtWebKitWidgets.so
%{py_platsitedir}/PyQt5/QtWebKitWidgets.pyi
%{_datadir}/sip/PyQt5/QtWebKitWidgets

#------------------------------------------------------------

%package websockets
Summary:	PyQt 5 WebSockets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description websockets
PyQt 5 websockets.

%files websockets
%{py_platsitedir}/PyQt5/QtWebSockets.so
%{py_platsitedir}/PyQt5/QtWebSockets.pyi
%{_datadir}/sip/PyQt5/QtWebSockets


#------------------------------------------------------------

%package widgets
Summary:	PyQt 5 widgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description widgets
PyQt 5 widgets.

%files widgets
%{py_platsitedir}/PyQt5/QtWidgets.so
%{py_platsitedir}/PyQt5/QtWidgets.pyi
%{_datadir}/sip/PyQt5/QtWidgets

#------------------------------------------------------------

%package xml
Summary:	PyQt 5 xml
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description xml
PyQt 5 xml.

%files xml
%{py_platsitedir}/PyQt5/QtXml.so
%{py_platsitedir}/PyQt5/QtXml.pyi
%dir %{_datadir}/sip/PyQt5/QtXml
%{_datadir}/sip/PyQt5/QtXml/QtXmlmod.sip
%{_datadir}/sip/PyQt5/QtXml/qdom.sip
%{_datadir}/sip/PyQt5/QtXml/qxml.sip


#------------------------------------------------------------

%package xmlpatterns
Summary:	PyQt 5 xmlpatterns
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-xml = %{EVRD}

%description xmlpatterns
PyQt 5 xmlpatterns.

%files xmlpatterns
%{py_platsitedir}/PyQt5/QtXmlPatterns.so
%{py_platsitedir}/PyQt5/QtXmlPatterns.pyi
%{_datadir}/sip/PyQt5/QtXmlPatterns

#------------------------------------------------------------

%package x11extras
Summary:	PyQt 5 x11extras
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description x11extras
PyQt 5 x11extras.

%files x11extras
%{py_platsitedir}/PyQt5/QtX11Extras.so
%{py_platsitedir}/PyQt5/QtX11Extras.pyi
%{_datadir}/sip/PyQt5/QtX11Extras

#------------------------------------------------------------

%package devel
Summary:	PyQt 5 devel
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires:	qt5-designer

%description devel
PyQt 5 devel utilities.

%files devel
%{_bindir}/pyuic5
%{_bindir}/pyrcc5
%{_bindir}/pylupdate5
%{_qt5_plugindir}/designer/*
%{python_sitearch}/PyQt5/pylupdate*
%{python_sitearch}/PyQt5/pyrcc*

#------------------------------------------------------------

### python2-qt5

%define py2_name python2-qt5

%package -n    python2-qt5
Summary:       Set of Python 2 bindings for Trolltech's Qt application framework
Group:         Development/KDE and Qt
BuildRequires: pkgconfig(python2)
BuildRequires: python2-sip
BuildRequires: python2-dbus

Provides:      python2-PyQt5 = %{version}-%{release}

Requires:      %{py2_name}-core = %{version}
Requires:      %{py2_name}-dbus = %{version}
Requires:      %{py2_name}-bluetooth = %{version}
Requires:      %{py2_name}-designer = %{version}
Requires:      %{py2_name}-gui = %{version}
Requires:      %{py2_name}-location = %{version}
Requires:      %{py2_name}-multimedia = %{version}
Requires:      %{py2_name}-multimediawidgets = %{version}
Requires:      %{py2_name}-nfc = %{version}
Requires:      %{py2_name}-network = %{version}
Requires:      %{py2_name}-opengl = %{version}
Requires:      %{py2_name}-positioning = %{version}
Requires:      %{py2_name}-printsupport = %{version}
Requires:      %{py2_name}-qml = %{version}
Requires:      %{py2_name}-quick = %{version}
Requires:      %{py2_name}-serialport = %{version}
Requires:      %{py2_name}-sql = %{version}
Requires:      %{py2_name}-svg = %{version}
Requires:      %{py2_name}-test = %{version}
Requires:      %{py2_name}-webchannel = %{version}
Requires:      %{py2_name}-webenginecore = %{version}
Requires:      %{py2_name}-webenginewidgets = %{version}
Requires:      %{py2_name}-webkit = %{version}
Requires:      %{py2_name}-webkitwidgets = %{version}
Requires:      %{py2_name}-websockets = %{version}
Requires:      %{py2_name}-widgets = %{version}
Requires:      %{py2_name}-xmlpatterns = %{version}
Requires:      %{py2_name}-x11extras = %{version}

%description -n python2-qt5
PyQt is a set of Python 2 bindings for Trolltech's Qt application framework.

%files -n python2-qt5
%doc NEWS README



#------------------------------------------------------------

%package -n python2-qt5-core
Summary:	PyQt 5 core
Group:		Development/KDE and Qt

%description -n python2-qt5-core
PyQt 5 core.

%files -n python2-qt5-core
%dir %{py2_platsitedir}/PyQt5
%{py2_platsitedir}/PyQt5/uic
%{py2_platsitedir}/PyQt5/__init__.py*
%{py2_platsitedir}/PyQt5/Qt.so
%{py2_platsitedir}/PyQt5/QtCore.so
%{_datadir}/python2-sip/PyQt5/QtCore

#------------------------------------------------------------

%package -n python2-qt5-dbus
Summary:	PyQt 5 dbus
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-dbus
PyQt 5 dbus.

%files -n python2-qt5-dbus
%{py2_platsitedir}/PyQt5/QtDBus.so
%{py2_puresitedir}/dbus/mainloop/pyqt5.so
%{_datadir}/python2-sip/PyQt5/QtDBus

#------------------------------------------------------------

%package -n python2-qt5-designer
Summary:	PyQt 5 designer
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-designer
PyQt 5 designer.

%files -n python2-qt5-designer
%{py2_platsitedir}/PyQt5/QtDesigner.so
%{_datadir}/python2-sip/PyQt5/QtDesigner

#------------------------------------------------------------

%package -n python2-qt5-bluetooth
Summary:	PyQt 5 bluetooth
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-bluetooth
PyQt 5 bluetooth.

%files -n python2-qt5-bluetooth
%{py2_platsitedir}/PyQt5/QtBluetooth.so
%{_datadir}/python2-sip/PyQt5/QtBluetooth

#------------------------------------------------------------


%package -n python2-qt5-enginio
Summary:        PyQt 5 enginio
Group:          Development/KDE and Qt
Requires:       python2-qt5-core = %{EVRD}

%description -n python2-qt5-enginio
PyQt 5 enginio (cloud storage)

%files -n python2-qt5-enginio
%{py2_platsitedir}/PyQt5/Enginio.so
%{_datadir}/python2-sip/PyQt5/Enginio

#------------------------------------------------------------

%package -n python2-qt5-gui
Summary:	PyQt 5 gui
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-gui
PyQt 5 gui.

%files -n python2-qt5-gui
%{py2_platsitedir}/PyQt5/QtGui.so
%{py2_platsitedir}/PyQt5/_QOpenGLFunctions_*.so
%{_datadir}/python2-sip/PyQt5/QtGui

#------------------------------------------------------------

%package -n python2-qt5-network
Summary:	PyQt 5 network
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-network
PyQt 5 network.

%files -n python2-qt5-network
%{py2_platsitedir}/PyQt5/QtNetwork.so
%{_datadir}/python2-sip/PyQt5/QtNetwork

#------------------------------------------------------------

%package -n python2-qt5-networkauth
Summary:	PyQt 5 network authentication
Group:		Development/KDE and Qt
Requires:	python2-qt5-network = %{EVRD}

%description -n python2-qt5-networkauth
PyQt 5 network authentication.

%files -n python2-qt5-networkauth
%{py2_platsitedir}/PyQt5/QtNetworkAuth.so
%{_datadir}/python2-sip/PyQt5/QtNetworkAuth

#------------------------------------------------------------

%package -n python2-qt5-nfc
Summary:        PyQt 5 nfc
Group:          Development/KDE and Qt
Requires:       python2-qt5-core = %{EVRD}

%description -n python2-qt5-nfc
PyQt 5 nfc.

%files -n python2-qt5-nfc
%{py2_platsitedir}/PyQt5/QtNfc.so
%{_datadir}/python2-sip/PyQt5/QtNfc

#------------------------------------------------------------

%package -n python2-qt5-help
Summary:	PyQt 5 help
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-help
PyQt 5 help.

%files -n python2-qt5-help
%{py2_platsitedir}/PyQt5/QtHelp.so
%{_datadir}/python2-sip/PyQt5/QtHelp

#------------------------------------------------------------

%package -n python2-qt5-location
Summary:        PyQt 5 location
Group:          Development/KDE and Qt
Requires:       python2-qt5-core = %{EVRD}

%description -n python2-qt5-location
PyQt 5 location.

%files -n python2-qt5-location
%{py2_platsitedir}/PyQt5/QtLocation.so
%{_datadir}/python2-sip/PyQt5/QtLocation

#------------------------------------------------------------

%package -n python2-qt5-multimedia
Summary:	PyQt 5 multimedia
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-multimedia
PyQt 5 multimedia.

%files -n python2-qt5-multimedia
%{py2_platsitedir}/PyQt5/QtMultimedia.so
%{_datadir}/python2-sip/PyQt5/QtMultimedia

#------------------------------------------------------------

%package -n python2-qt5-multimediawidgets
Summary:	PyQt 5 multimediawidgets
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-multimediawidgets
PyQt 5 multimediawidgets.

%files -n python2-qt5-multimediawidgets
%{py2_platsitedir}/PyQt5/QtMultimediaWidgets.so
%{_datadir}/python2-sip/PyQt5/QtMultimediaWidgets

#------------------------------------------------------------

%package -n python2-qt5-opengl
Summary:	PyQt 5 opengl
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-opengl
PyQt 5 opengl.

%files -n python2-qt5-opengl
%{py2_platsitedir}/PyQt5/QtOpenGL.so
%{_datadir}/python2-sip/PyQt5/QtOpenGL

#------------------------------------------------------------

%package -n python2-qt5-positioning
Summary:	PyQt 5 positioning
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-positioning
PyQt 5 positioning.

%files -n python2-qt5-positioning
%{py2_platsitedir}/PyQt5/QtPositioning.so
%{_datadir}/python2-sip/PyQt5/QtPositioning

#------------------------------------------------------------

%package -n python2-qt5-printsupport
Summary:	PyQt 5 printsupport
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-printsupport
PyQt 5 printsupport

%files -n python2-qt5-printsupport
%{py2_platsitedir}/PyQt5/QtPrintSupport.so
%{_datadir}/python2-sip/PyQt5/QtPrintSupport

#------------------------------------------------------------

%package -n python2-qt5-qml
Summary:	PyQt 5 qml
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-qml
PyQt 5 qml.

%files -n python2-qt5-qml
%{py2_platsitedir}/PyQt5/QtQml.so
#{_qt5_plugindir}/PyQt5/libpyqt5qmlplugin.so
%{_datadir}/python2-sip/PyQt5/QtQml

#------------------------------------------------------------

%package -n python2-qt5-quick
Summary:	PyQt 5 quick
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-quick
PyQt 5 quick.

%files -n python2-qt5-quick
%{py2_platsitedir}/PyQt5/QtQuick.so
%{_datadir}/python2-sip/PyQt5/QtQuick

#------------------------------------------------------------

%package -n python2-qt5-quickwidgets
Summary:	PyQt 5 quickwidgets
Group:		Development/KDE and Qt
Requires:	%{name}-quick = %{EVRD}

%description -n python2-qt5-quickwidgets
PyQt 5 quickwidgets.

%files -n python2-qt5-quickwidgets
%{py2_platsitedir}/PyQt5/QtQuickWidgets.so
%{_datadir}/python2-sip/PyQt5/QtQuickWidgets


#------------------------------------------------------------

%package -n python2-qt5-sensors
Summary:	PyQt 5 sensors
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-sensors
PyQt 5 sensors.

%files -n python2-qt5-sensors
%{py2_platsitedir}/PyQt5/QtSensors.so
%{_datadir}/python2-sip/PyQt5/QtSensors

#------------------------------------------------------------

%package -n python2-qt5-serialport
Summary:	PyQt 5 serialport
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-serialport
PyQt 5 serialport.

%files -n python2-qt5-serialport
%{py2_platsitedir}/PyQt5/QtSerialPort.so
%{_datadir}/python2-sip/PyQt5/QtSerialPort

#------------------------------------------------------------

%package -n python2-qt5-sql
Summary:	PyQt 5 sql
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-sql
PyQt 5 sql.

%files -n python2-qt5-sql
%{py2_platsitedir}/PyQt5/QtSql.so
%{_datadir}/python2-sip/PyQt5/QtSql

#------------------------------------------------------------

%package -n python2-qt5-svg
Summary:	PyQt 5 svg
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-svg
PyQt 5 svg.

%files -n python2-qt5-svg
%{py2_platsitedir}/PyQt5/QtSvg.so
%{_datadir}/python2-sip/PyQt5/QtSvg

#------------------------------------------------------------

%package -n python2-qt5-test
Summary:	PyQt 5 test
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-test
PyQt 5 test.

%files -n python2-qt5-test
%{py2_platsitedir}/PyQt5/QtTest.so
%{_datadir}/python2-sip/PyQt5/QtTest

#------------------------------------------------------------

%package -n python2-qt5-webchannel
Summary:       PyQt 5 webchannel
Group:         Development/KDE and Qt
Requires:      python2-qt5-core = %{EVRD}

%description -n python2-qt5-webchannel
PyQt 5 webchannel.

%files -n python2-qt5-webchannel
%{python2_sitearch}/PyQt5/QtWebChannel.so
%{_datadir}/python2-sip/PyQt5/QtWebChannel

#------------------------------------------------------------

%package -n python2-qt5-webenginecore
Summary:        PyQt 5 webenginecore
Group:          Development/KDE and Qt
Requires:       python2-qt5-core = %{EVRD}
Requires:       python2-qt5-webchannel = %{EVRD}

%description -n python2-qt5-webenginecore
PyQt 5 webenginecore.

%files -n python2-qt5-webenginecore
%{py2_platsitedir}/PyQt5/QtWebEngineCore.so
%{py2_platsitedir}/PyQt5/QtWebEngine.so
%{_datadir}/python2-sip/PyQt5/QtWebEngineCore
%dir %{_datadir}/python2-sip/PyQt5/QtWebEngine
%{_datadir}/python2-sip/PyQt5/QtWebEngine/*.sip

#------------------------------------------------------------

%package -n python2-qt5-webenginewidgets
Summary:        PyQt 5 webenginewidgets
Group:          Development/KDE and Qt
Requires:       python2-qt5-core = %{EVRD}
Requires:	python2-qt5-webchannel = %{EVRD}

%description -n python2-qt5-webenginewidgets
PyQt 5 webenginewidgets.

%files -n python2-qt5-webenginewidgets
%{py2_platsitedir}/PyQt5/QtWebEngineWidgets.so
%{_datadir}/python2-sip/PyQt5/QtWebEngineWidgets

#------------------------------------------------------------

%package -n python2-qt5-webkit
Summary:	PyQt 5 Webkit
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-webkit
PyQt 5 webkit.

%files -n python2-qt5-webkit
%{py2_platsitedir}/PyQt5/QtWebKit.so
%{_datadir}/python2-sip/PyQt5/QtWebKit

#------------------------------------------------------------

%package -n python2-qt5-webkitwidgets
Summary:	PyQt 5 webkitwidgets
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-webkitwidgets
PyQt 5 webkitwidgets.

%files -n python2-qt5-webkitwidgets
%{py2_platsitedir}/PyQt5/QtWebKitWidgets.so
%{_datadir}/python2-sip/PyQt5/QtWebKitWidgets

#------------------------------------------------------------

%package -n python2-qt5-websockets
Summary:	PyQt 5 WebSockets
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-websockets
PyQt 5 websockets.

%files -n python2-qt5-websockets
%{py2_platsitedir}/PyQt5/QtWebSockets.so
%{_datadir}/python2-sip/PyQt5/QtWebSockets


#------------------------------------------------------------

%package -n python2-qt5-widgets
Summary:	PyQt 5 widgets
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-widgets
PyQt 5 widgets.

%files -n python2-qt5-widgets
%{py2_platsitedir}/PyQt5/QtWidgets.so
%{_datadir}/python2-sip/PyQt5/QtWidgets

#------------------------------------------------------------

%package -n python2-qt5-xml
Summary:	PyQt 5 xml
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-xml
PyQt 5 xml.

%files -n python2-qt5-xml
%{py2_platsitedir}/PyQt5/QtXml.so
%dir %{_datadir}/python2-sip/PyQt5/QtXml
%{_datadir}/python2-sip/PyQt5/QtXml/QtXmlmod.sip
%{_datadir}/python2-sip/PyQt5/QtXml/qdom.sip
%{_datadir}/python2-sip/PyQt5/QtXml/qxml.sip


#------------------------------------------------------------

%package -n python2-qt5-xmlpatterns
Summary:	PyQt 5 xmlpatterns
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}
Requires:	python2-qt5-xml = %{EVRD}

%description -n python2-qt5-xmlpatterns
PyQt 5 xmlpatterns.

%files -n python2-qt5-xmlpatterns
%{py2_platsitedir}/PyQt5/QtXmlPatterns.so
%{_datadir}/python2-sip/PyQt5/QtXmlPatterns

#------------------------------------------------------------

%package -n python2-qt5-x11extras
Summary:	PyQt 5 x11extras
Group:		Development/KDE and Qt
Requires:	python2-qt5-core = %{EVRD}

%description -n python2-qt5-x11extras
PyQt 5 x11extras.

%files -n python2-qt5-x11extras
%{py2_platsitedir}/PyQt5/QtX11Extras.so
%{_datadir}/python2-sip/PyQt5/QtX11Extras

#------------------------------------------------------------

%package -n python2-qt5-devel
Summary:	PyQt 5 devel
Group:		Development/KDE and Qt
Requires:	python2-qt5 = %{EVRD}
Requires:	qt5-designer

%description -n python2-qt5-devel
PyQt 5 devel utilities.

%files -n python2-qt5-devel
%{python2_sitearch}/PyQt5/pylupdate*
%{python2_sitearch}/PyQt5/pyrcc*


#------------------------------------------------------------


%prep
%setup -q -n PyQt5_gpl-%{version}
%apply_patches
cp -a . %{py2dir}

%build
export PATH=%{_qt5_bindir}:$PATH

python ./configure.py \
	--qsci-api \
	--confirm-license

#sed -i -e "s,-fstack-protector-strong,,g" _Q*/Makefile
sed -i -e "s,^LIBS .*= ,LIBS = $(python-config --libs) ,g" */Makefile
sed -i -e "s#^LFLAGS .*= #LFLAGS = %{ldflags} #g" */Makefile
sed -i -e "s#-flto##g" */Makefile
%make


pushd %{py2dir}
%{__python2} configure.py \
  --sipdir=%{_datadir}/python2-sip/PyQt5 \
  --no-qsci-api \
  --assume-shared \
  --confirm-license \
  --debug \
  --verbose

sed -i -e "s,^LIBS .*= ,LIBS = $(python2-config --libs) ,g" Qt*/Makefile _Q*/Makefile dbus/Makefile
sed -i -e "s#^LFLAGS .*= #LFLAGS = %{ldflags} #g" Qt*/Makefile _Q*/Makefile pyrcc/Makefile designer/Makefile dbus/Makefile qmlscene/Makefile
sed -i -e "s#-flto##g" */Makefile
%make

%install

### python2-qt5 install
pushd %{py2dir}
%make_install INSTALL_ROOT=%{buildroot} -C %{py2dir}
rm -fr %{buildroot}%{python3_sitearch}/PyQt5/uic/port_v2
# Get rid of bits and pieces that aren't useful on Linux
rm -rf	\
	 %{buildroot}%{_datadir}/python2-sip/PyQt5/QAxContainer \
	 %{buildroot}%{_datadir}/python2-sip/PyQt5/QtAndroidExtras \
	 %{buildroot}%{_datadir}/python2-sip/PyQt5/QtMacExtras \
	 %{buildroot}%{_datadir}/python2-sip/PyQt5/QtWinExtras
popd

%makeinstall_std INSTALL_ROOT=%{buildroot}
rm -fr %{buildroot}%{py_platsitedir}/PyQt5/uic/port_v2
# Get rid of bits and pieces that aren't useful on Linux
rm -rf	\
	 %{buildroot}%{_datadir}/sip/PyQt5/QAxContainer \
	 %{buildroot}%{_datadir}/sip/PyQt5/QtAndroidExtras \
	 %{buildroot}%{_datadir}/sip/PyQt5/QtMacExtras \
	 %{buildroot}%{_datadir}/sip/PyQt5/QtWinExtras
