%define major 5
%define libname %mklibname milou %{major}
%define devname %mklibname milou -d
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: milou
Version: 5.1.1
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: A search client for Baloo
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KdepimLibs)
BuildRequires: cmake(Qt5Script)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5Runner)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Declarative)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
A search client for Baloo

%package -n %{libname}
Summary: KDE Frameworks 5 Milou search framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 Milou search framework

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Milou search library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Milou search library

%prep
%setup -qn %{name}-%{plasmaver}
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang milou
%find_lang plasma_applet_org.kde.milou

%files -f milou.lang,plasma_applet_org.kde.milou.lang
%{_libdir}/qt5/qml/org/kde/milou
%{_datadir}/kservicetypes5/*
%{_datadir}/kservices5/*
%{_datadir}/plasma/plasmoids/org.kde.milou
%{_libdir}/qt5/plugins/miloutextplugin.so

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{plasmaver}
