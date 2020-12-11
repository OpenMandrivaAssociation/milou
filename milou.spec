%define major 5
%define libname %mklibname milou %{major}
%define devname %mklibname milou -d
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: milou
Version:	5.20.4
Release:	2
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: A search client for Baloo
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KF5Runner)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5ItemModels)
Requires: %{libname} = %{EVRD}

%description
A search client for Baloo.

%package -n %{libname}
Summary: KDE Frameworks 5 Milou search framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 Milou search framework.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Milou search library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Milou search library.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang milou
%find_lang plasma_applet_org.kde.milou

%files -f milou.lang -f plasma_applet_org.kde.milou.lang
%{_libdir}/qt5/qml/org/kde/milou
%{_datadir}/kservicetypes5/*
%{_datadir}/kservices5/*
%{_datadir}/plasma/plasmoids/org.kde.milou
%{_libdir}/qt5/plugins/miloutextplugin.so
%{_datadir}/metainfo/org.kde.milou.appdata.xml

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{plasmaver}
