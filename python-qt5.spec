%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define _disable_lto 1
%define _disable_ld_no_undefined 1
%define major %(echo %{version} |cut -d. -f1-2)

Summary:	Set of Python bindings for Trolltech's Qt application framework
Name:		python-qt5
Version:	5.15.0
Release:	1
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		http://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0:	http://pypi.io/packages/source/p/pyqt/PyQt5-%{version}.tar.gz
#Patch1:		PyQt5_gpl-5.6-dbus_ftbfs.patch
# support newer Qt5 releases than 5.9.3/5.10.0
#Patch1:		PyQt5-Timeline.patch

BuildRequires:	python-sip >= 5.1.0
BuildRequires:	python-sip-qt5
BuildRequires:	python-qt-builder
BuildRequires:	qmake5
BuildRequires:	qt5-qtbase-macros
BuildRequires:	glibc-devel
BuildRequires:	sed
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(Qt5Bluetooth)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5Enginio)
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
BuildRequires:	pkgconfig(Qt5RemoteObjects)
BuildRequires:	pkgconfig(Qt5WebChannel)
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
Requires:	%{name}-remoteobjects = %{EVRD}
Requires:	%{name}-qml = %{EVRD}
Requires:	%{name}-quick = %{EVRD}
Requires:	%{name}-quickwidgets = %{EVRD}
Requires:	%{name}-sensors = %{EVRD}
Requires:	%{name}-serialport = %{EVRD}
Requires:	%{name}-sql = %{EVRD}
Requires:	%{name}-svg = %{EVRD}
Requires:	%{name}-test = %{EVRD}
Requires:	%{name}-webchannel = %{version}
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
%{py_platsitedir}/PyQt5/__init__.py
%dir %{py_platsitedir}/PyQt5/__pycache__
%{py_platsitedir}/PyQt5/__pycache__/__init__.cpython-38.opt-1.pyc
%{py_platsitedir}/PyQt5/__pycache__/__init__.cpython-38.pyc

#------------------------------------------------------------

%package dbus
Summary:	PyQt 5 dbus
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description dbus
PyQt 5 dbus.

%files dbus
#%{py_platsitedir}/PyQt5/QtDBus.abi3.so

#------------------------------------------------------------

%package designer
Summary:	PyQt 5 designer
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description designer
PyQt 5 designer.

%files designer
%{py_platsitedir}/PyQt5/QtDesigner.abi3.so

#------------------------------------------------------------

%package bluetooth
Summary:	PyQt 5 bluetooth
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description bluetooth
PyQt 5 bluetooth.

%files bluetooth
%{py_platsitedir}/PyQt5/QtBluetooth.abi3.so

#------------------------------------------------------------

%package enginio
Summary:	PyQt 5 enginio
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description enginio
PyQt 5 enginio (cloud storage).

%files enginio
%{py_platsitedir}/PyQt5/Enginio.abi3.so

#------------------------------------------------------------

%package gui
Summary:	PyQt 5 gui
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description gui
PyQt 5 gui.

%files gui
%{py_platsitedir}/PyQt5/QtGui.abi3.so

#------------------------------------------------------------

%package network
Summary:	PyQt 5 network
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description network
PyQt 5 network.

%files network
%{py_platsitedir}/PyQt5/QtNetwork.abi3.so

#------------------------------------------------------------

%package networkauth
Summary:	PyQt 5 network authentication
Group:		Development/KDE and Qt
Requires:	%{name}-network = %{EVRD}

%description networkauth
PyQt 5 network authentication.

%files networkauth
%{py_platsitedir}/PyQt5/QtNetworkAuth.abi3.so

#------------------------------------------------------------

%package nfc
Summary:	PyQt 5 nfc
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description nfc
PyQt 5 nfc.

%files nfc
%{py_platsitedir}/PyQt5/QtNfc.abi3.so

#------------------------------------------------------------

%package help
Summary:	PyQt 5 help
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description help
PyQt 5 help.

%files help
%{py_platsitedir}/PyQt5/QtHelp.abi3.so

#------------------------------------------------------------

%package location
Summary:	PyQt 5 location
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description location
PyQt 5 location.

%files location
%{py_platsitedir}/PyQt5/QtLocation.abi3.so

#------------------------------------------------------------

%package multimedia
Summary:	PyQt 5 multimedia
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description multimedia
PyQt 5 multimedia.

%files multimedia
%{py_platsitedir}/PyQt5/QtMultimedia.abi3.so

#------------------------------------------------------------

%package multimediawidgets
Summary:	PyQt 5 multimediawidgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description multimediawidgets
PyQt 5 multimediawidgets.

%files multimediawidgets
%{py_platsitedir}/PyQt5/QtMultimediaWidgets.abi3.so

#------------------------------------------------------------

%package opengl
Summary:	PyQt 5 opengl
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description opengl
PyQt 5 opengl.

%files opengl
%{py_platsitedir}/PyQt5/QtOpenGL.abi3.so
%{py_platsitedir}/PyQt5/_QOpenGLFunctions_2_0.abi3.so
%{py_platsitedir}/PyQt5/_QOpenGLFunctions_2_1.abi3.so
%{py_platsitedir}/PyQt5/_QOpenGLFunctions_4_1_Core.abi3.so
%{py_platsitedir}/PyQt5/bindings/QtOpenGL

#------------------------------------------------------------

%package positioning
Summary:	PyQt 5 positioning
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description positioning
PyQt 5 positioning.

%files positioning
%{py_platsitedir}/PyQt5/QtPositioning.abi3.so

#------------------------------------------------------------

%package printsupport
Summary:	PyQt 5 printsupport
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description printsupport
PyQt 5 printsupport

%files printsupport
%{py_platsitedir}/PyQt5/QtPrintSupport.abi3.so

#------------------------------------------------------------

%package qml
Summary:	PyQt 5 qml
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description qml
PyQt 5 qml.

%files qml
%{py_platsitedir}/PyQt5/QtQml.abi3.so

#------------------------------------------------------------

%package quick
Summary:	PyQt 5 quick
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description quick
PyQt 5 quick.

%files quick
%{py_platsitedir}/PyQt5/QtQuick.abi3.so

#------------------------------------------------------------

%package quickwidgets
Summary:	PyQt 5 quickwidgets
Group:		Development/KDE and Qt
Requires:	%{name}-quick = %{EVRD}

%description quickwidgets
PyQt 5 quickwidgets.

%files quickwidgets
%{py_platsitedir}/PyQt5/QtQuickWidgets.abi3.so


#------------------------------------------------------------

%package sensors
Summary:	PyQt 5 sensors
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description sensors
PyQt 5 sensors.

%files sensors
%{py_platsitedir}/PyQt5/QtSensors.abi3.so

#------------------------------------------------------------

%package serialport
Summary:	PyQt 5 serialport
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description serialport
PyQt 5 serialport.

%files serialport
%{py_platsitedir}/PyQt5/QtSerialPort.abi3.so

#------------------------------------------------------------

%package sql
Summary:	PyQt 5 sql
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description sql
PyQt 5 sql.

%files sql
%{py_platsitedir}/PyQt5/QtSql.abi3.so

#------------------------------------------------------------

%package svg
Summary:	PyQt 5 svg
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description svg
PyQt 5 svg.

%files svg
%{py_platsitedir}/PyQt5/QtSvg.abi3.so

#------------------------------------------------------------

%package test
Summary:	PyQt 5 test
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description test
PyQt 5 test.

%files test
%{py_platsitedir}/PyQt5/QtTest.abi3.so

#------------------------------------------------------------

%package webchannel
Summary:	PyQt 5 webchannel
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description   webchannel
PyQt 5 webchannel.

%files webchannel
%{py_platsitedir}/PyQt5/QtWebChannel.abi3.so

#------------------------------------------------------------

%package remoteobjects
Summary:	PyQt 5 remoteobjects
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description remoteobjects
PyQt 5 remoteobjects.

%files remoteobjects
%{py_platsitedir}/PyQt5/QtRemoteObjects.abi3.so

#------------------------------------------------------------

%package webkit
Summary:	PyQt 5 Webkit
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description webkit
PyQt 5 webkit.

%files webkit
%{py_platsitedir}/PyQt5/QtWebKit.abi3.so

#------------------------------------------------------------

%package webkitwidgets
Summary:	PyQt 5 webkitwidgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description webkitwidgets
PyQt 5 webkitwidgets.

%files webkitwidgets
%{py_platsitedir}/PyQt5/QtWebKitWidgets.abi3.so

#------------------------------------------------------------

%package websockets
Summary:	PyQt 5 WebSockets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description websockets
PyQt 5 websockets.

%files websockets
%{py_platsitedir}/PyQt5/QtWebSockets.abi3.so


#------------------------------------------------------------

%package widgets
Summary:	PyQt 5 widgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description widgets
PyQt 5 widgets.

%files widgets
%{py_platsitedir}/PyQt5/QtWidgets.abi3.so

#------------------------------------------------------------

%package xml
Summary:	PyQt 5 xml
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description xml
PyQt 5 xml.

%files xml
%{py_platsitedir}/PyQt5/QtXml.abi3.so


#------------------------------------------------------------

%package xmlpatterns
Summary:	PyQt 5 xmlpatterns
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-xml = %{EVRD}

%description xmlpatterns
PyQt 5 xmlpatterns.

%files xmlpatterns
%{py_platsitedir}/PyQt5/QtXmlPatterns.abi3.so

#------------------------------------------------------------

%package x11extras
Summary:	PyQt 5 x11extras
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description x11extras
PyQt 5 x11extras.

%files x11extras
%{py_platsitedir}/PyQt5/QtX11Extras.abi3.so

#------------------------------------------------------------

%package devel
Summary:	PyQt 5 devel
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires:	qt5-designer

%description devel
PyQt 5 devel utilities.

%files devel
/usr/bin/pylupdate5
/usr/bin/pyrcc5
/usr/bin/pyuic5
%dir %{_datadir}/qt5/qsci
%dir %{_datadir}/qt5/qsci/api
%dir %{_datadir}/qt5/qsci/api/python
%{_datadir}/qt5/qsci/api/python/PyQt5.api
%{py_platsitedir}/PyQt5/pylupdate.abi3.so
%{py_platsitedir}/PyQt5/pyrcc.abi3.so
%{py_platsitedir}/PyQt5/uic
# Contains only the cache files for pyrcc, pylupdate
%{py_platsitedir}/PyQt5/__pycache__/pyrcc_main.cpython-38.pyc
%{py_platsitedir}/PyQt5/__pycache__/pyrcc_main.cpython-38.opt-1.pyc
%{py_platsitedir}/PyQt5/__pycache__/pylupdate_main.cpython-38.opt-1.pyc
%{py_platsitedir}/PyQt5/__pycache__/pylupdate_main.cpython-38.pyc
%{py_platsitedir}/PyQt5/pylupdate_main.py
%{py_platsitedir}/PyQt5/bindings/QtPositioning
%{py_platsitedir}/PyQt5/bindings/QtLocation
%{py_platsitedir}/PyQt5/bindings/QtSvg
%{py_platsitedir}/PyQt5/bindings/QtPrintSupport
%{py_platsitedir}/PyQt5/bindings/QtSql
%{py_platsitedir}/PyQt5/bindings/QtQuickWidgets
%{py_platsitedir}/PyQt5/bindings/QtWebKitWidgets
%{py_platsitedir}/PyQt5/bindings/QtNetworkAuth
%{py_platsitedir}/PyQt5/bindings/QtDBus
%{py_platsitedir}/PyQt5/bindings/QtXmlPatterns
%{py_platsitedir}/PyQt5/bindings/QtCore
%{py_platsitedir}/PyQt5/bindings/QtXml
%{py_platsitedir}/PyQt5/bindings/QtTest
%{py_platsitedir}/PyQt5/bindings/QtRemoteObjects
%{py_platsitedir}/PyQt5/bindings/QtQuick
%{py_platsitedir}/PyQt5/bindings/QtMultimedia
%{py_platsitedir}/PyQt5/bindings/QtGui
%{py_platsitedir}/PyQt5/bindings/Enginio
%{py_platsitedir}/PyQt5/bindings/QtNetwork
%{py_platsitedir}/PyQt5/bindings/QtSensors
%{py_platsitedir}/PyQt5/bindings/QtWebKit
%{py_platsitedir}/PyQt5/bindings/QtWebSockets
%{py_platsitedir}/PyQt5/bindings/QtQml
%{py_platsitedir}/PyQt5/bindings/QtWebChannel
%{py_platsitedir}/PyQt5/bindings/QtWidgets
%{py_platsitedir}/PyQt5/bindings/QtMultimediaWidgets
%{py_platsitedir}/PyQt5/bindings/QtDesigner
%{py_platsitedir}/PyQt5/bindings/QtHelp
%{py_platsitedir}/PyQt5/bindings/QtNfc
%{py_platsitedir}/PyQt5/bindings/QtX11Extras
%{py_platsitedir}/PyQt5/bindings/QtBluetooth
%{py_platsitedir}/PyQt5/bindings/QtSerialPort
%{py_platsitedir}/PyQt5/pyrcc_main.py
%{py_platsitedir}/PyQt5-*.dist-info
%{_libdir}/qt5/plugins/PyQt5/libpyqt5qmlplugin.so
%{_libdir}/qt5/plugins/designer/libpyqt5.so


#------------------------------------------------------------

%prep
%autosetup -n PyQt5-%{version} -p1

%build
python configure.py \
	--qmake="%{_qt5_bindir}/qmake" \
	--sipdir=%{_datadir}/sip/PyQt5 \
	--qsci-api \
	--assume-shared \
	--confirm-license \
	--debug \
	--verbose

sed -i -e "s,-fstack-protector,-fno-stack-protector,g" _Q*/Makefile
sed -i -e "s,^LIBS .*= ,LIBS = $(python3-config --libs) ,g" Qt*/Makefile _Q*/Makefile dbus/Makefile
sed -i -e "s#^LFLAGS .*= #LFLAGS = %{ldflags} #g" Qt*/Makefile _Q*/Makefile pyrcc/Makefile designer/Makefile dbus/Makefile qmlscene/Makefile

%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

rm -rf %{buildroot}%{python_sitearch}/PyQt5/uic/port_v2

# ensure .so modules are executable for proper -debuginfo extraction
for i in %{buildroot}%{python_sitearch}/PyQt5/*.so ; do
    chmod a+rx $i
done

# Get rid of bits and pieces that aren't useful on Linux
rm -rf	\
	 %{buildroot}%{_datadir}/sip/PyQt5/QAxContainer \
	 %{buildroot}%{_datadir}/sip/PyQt5/QtAndroidExtras \
	 %{buildroot}%{_datadir}/sip/PyQt5/QtMacExtras \
	 %{buildroot}%{_datadir}/sip/PyQt5/QtWinExtras
