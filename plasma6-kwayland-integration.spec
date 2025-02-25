%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f2`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary: 	KDE Library for integration with the Wayland display server
Name: 		plasma6-kwayland-integration
Version:	6.3.2
Release: 	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kwayland-integration/-/archive/%{gitbranch}/kwayland-integration-%{gitbranchd}.tar.bz2#/kwayland-integration-%{git}.tar.bz2
%else
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/kwayland-integration-%{version}.tar.xz
%endif
Url: 		https://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6IdleTime)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KWayland) >= 5.90.0
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WaylandClient)

BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	qt5-qtwayland
BuildRequires:	qt5-qtwayland-private-devel

BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	plasma-wayland-protocols
BuildRequires:	wayland-tools
Requires:	plasma6-kwayland

%description
KDE Library for integration  Wayland display server.

%prep
%autosetup -p1 -n kwayland-integration-%{?git:%{gitbranchd}}%{!?git:%{version}}
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
%{_qtdir}/plugins/kf5/kwindowsystem/KF5WindowSystemKWaylandPlugin.so
%{_datadir}/qlogging-categories6/kwindowsystem.kwayland.categories
