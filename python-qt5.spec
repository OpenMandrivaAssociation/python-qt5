%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Set of Python bindings for Trolltech's Qt application framework
Name:		python-qt5
Version:	5.4.2
Release:	1
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		http://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0:	http://downloads.sourceforge.net/pyqt/PyQt-gpl-%{version}.tar.gz
BuildRequires:	python-sip
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
BuildRequires:	pkgconfig(Qt5Designer)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5MultimediaWidgets)
BuildRequires:	pkgconfig(Qt5Network)
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
Requires:	%{name}-gui = %{EVRD}
Requires:	%{name}-multimedia = %{EVRD}
Requires:	%{name}-multimediawidgets = %{EVRD}
Requires:	%{name}-network = %{EVRD}
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
Requires:	%{name}-webkit = %{EVRD}
Requires:	%{name}-webkitwidgets = %{EVRD}
Requires:	%{name}-websockets = %{EVRD}
Requires:	%{name}-widgets = %{EVRD}
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
%{_datadir}/sip/PyQt5/Qt
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
%{_datadir}/sip/PyQt5/QtBluetooth

#------------------------------------------------------------

%package gui
Summary:	PyQt 5 gui
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description gui
PyQt 5 gui.

%files gui
%{py_platsitedir}/PyQt5/QtGui.so
%ifarch %{ix86} x86_64
%{py_platsitedir}/PyQt5/_QOpenGLFunctions_2_0.so
%{_datadir}/sip/PyQt5/_QOpenGLFunctions_2_0
%endif
%ifarch %{armx}
%{py_platsitedir}/PyQt5/_QOpenGLFunctions_ES2.so
%{_datadir}/sip/PyQt5/_QOpenGLFunctions_ES2
%endif
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
%{_datadir}/sip/PyQt5/QtNetwork

#------------------------------------------------------------

%package help
Summary:	PyQt 5 help
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description help
PyQt 5 help.

%files help
%{py_platsitedir}/PyQt5/QtHelp.so
%{_datadir}/sip/PyQt5/QtHelp

#------------------------------------------------------------

%package multimedia
Summary:	PyQt 5 multimedia
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description multimedia
PyQt 5 multimedia.

%files multimedia
%{py_platsitedir}/PyQt5/QtMultimedia.so
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
%{_datadir}/sip/PyQt5/QtTest

#------------------------------------------------------------

%package webkit
Summary:	PyQt 5 Webkit
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description webkit
PyQt 5 webkit.

%files webkit
%{py_platsitedir}/PyQt5/QtWebKit.so
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
%{_datadir}/sip/PyQt5/QtWidgets

#------------------------------------------------------------

%package xmlpatterns
Summary:	PyQt 5 xmlpatterns
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description xmlpatterns
PyQt 5 xmlpatterns.

%files xmlpatterns
%{py_platsitedir}/PyQt5/QtXmlPatterns.so
%{py_platsitedir}/PyQt5/QtXml.so
%{_datadir}/sip/PyQt5/QtXmlPatterns
%{_datadir}/sip/PyQt5/QtXml/QtXmlmod.sip
%{_datadir}/sip/PyQt5/QtXml/qdom.sip
%{_datadir}/sip/PyQt5/QtXml/qxml.sip

#------------------------------------------------------------

%package x11extras
Summary:	PyQt 5 x11extras
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description x11extras
PyQt 5 x11extras.

%files x11extras
%{py_platsitedir}/PyQt5/QtX11Extras.so
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

#------------------------------------------------------------

%package doc
Summary:	PyQt 5 documentation
Group:		Development/KDE and Qt
Buildarch:	noarch

%description doc
PyQt 5 documentation.

%files doc
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/examples
#------------------------------------------------------------

%package examples
Summary:	PyQt 5 examples
Group:		Development/KDE and Qt
BuildArch:	noarch

%description examples
PyQt 5 examples.

%files examples
%doc %{_docdir}/%{name}/examples

#------------------------------------------------------------

%prep
%setup -q -n PyQt-gpl-%{version}

%build
export PATH=%{_qt5_bindir}:$PATH

python ./configure.py \
	--qsci-api \
	--confirm-license

sed -i -e "s,-fstack-protector,-fno-stack-protector,g" _Q*/Makefile
sed -i -e "s,^LIBS .*= ,LIBS = $(python-config --libs) ,g" */Makefile
sed -i -e "s#^LFLAGS .*= #LFLAGS = %{ldflags} #g" */Makefile

%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
rm -fr %{buildroot}%{py_platsitedir}/PyQt5/uic/port_v3

mkdir -p %{buildroot}%{_docdir}/%{name}
    cp -fr doc/html/* %{buildroot}%{_docdir}/%{name}/

mkdir %{buildroot}%{_docdir}/%{name}/examples
    cp -fr examples/* %{buildroot}%{_docdir}/%{name}/examples/

