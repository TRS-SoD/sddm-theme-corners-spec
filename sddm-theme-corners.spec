# this file was auto genrated by sddm2rpm
Name: sddm-theme-corners
Summary: Auto genrated specfile for sddm-theme-corners sddm theme
License: GPLv3
Version: 1.0.0
Release: 0%{?dist}
Source0: sddm-theme-corners.tar.gz
BuildArch:  noarch
# QML imports:
# org.kde.plasma.workspace.components
# org.kde.plasma.workspace.keyboardlayout
Requires:       sddm

%if 0%{?fedora}
BuildRequires:  kf5-rpm-macros
Requires:       kf5-plasma >= %{_kf5_version}
# Background.qml:import QtQuick
Requires:       qt5-qtquickcontrols
# on-screen keyboard
Recommends:     qt5-qtvirtualkeyboard
%endif

%if 0%{?suse_version}
Requires:      libKF5Plasma5
# Background.qml:import QtQuick
Requires:       libqt5-qtquickcontrols
# on-screen keyboard
Recommends:     libqt5-qtvirtualkeyboards
%endif

%description
auto genrated spec file for sddm theme sddm-theme-corners

%prep
%autosetup -n %{name}
 
%build
# we don't need one

%install
mkdir -p %{buildroot}/%{_datadir}/sddm/themes/sddm-theme-corners
cp -r * %{buildroot}/%{_datadir}/sddm/themes/sddm-theme-corners

%files
%{_datadir}/sddm/themes/sddm-theme-corners

%changelog
# please add one before compiling