Summary:	Internals for the KDE Telepathy IM suite
Name:		ktp-approver
Version:	21.12.0
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(TelepathyQt5)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	dbus-tools
Requires:	dbus-tools

%description
Internals for the KDE Telepathy IM suite

%files -f kded_ktp_approver.lang
%{_sysconfdir}/xdg/ktp_approverrc
%{_libdir}/qt5/plugins/kded_ktp_approver.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.Approver.service
%{_datadir}/kservices5/kded/ktp_approver.desktop
%{_datadir}/kservicetypes5/ktp-approver.desktop

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kded_ktp_approver
