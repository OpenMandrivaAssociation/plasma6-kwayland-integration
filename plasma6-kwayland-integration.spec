%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230901

Summary: 	KDE Library for integration with the Wayland display server
Name: 		plasma6-kwayland-integration
Version:	5.240.0
Release: 	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kwayland-integration/-/archive/master/kwayland-integration-master.tar.bz2#/kwayland-integration-%{git}.tar.bz2
%else
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Url: 		http://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6IdleTime)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Wayland)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	plasma-wayland-protocols
BuildRequires:	wayland-tools
# In reality, "not the KF5 version"
BuildRequires:	plasma6-xdg-desktop-portal-kde
Requires:	kf6-kwayland

%description
KDE Library for integration  Wayland display server.

%prep
%autosetup -p1 -n kwayland-integration-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_qtdir}/plugins/kf6/kwindowsystem/KF6WindowSystemKWaylandPlugin.so
%{_datadir}/qlogging-categories6/kwindowsystem.kwayland.categories
