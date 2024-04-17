Name:           warp
Version:        0.7.0
Release:        1
Summary:        App to securely send files via the internet or local network
License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/en-GB/app/app.drey.Warp/
Source0:        https://gitlab.gnome.org/World/warp/-/archive/v%{version}/warp-v%{version}.tar.bz2
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  cargo
BuildRequires:  gettext
BuildRequires:  rust
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(zbar)


%description
Warp allows you to securely send files to each other via the internet or local
network by exchanging a word-based code.

The best transfer method will be determined using the "Magic Wormhole" protocol
which includes local network transfer if possible.

%lang_package

%prep
%autosetup -n %{name}-v%{version} -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/warp
%{_datadir}/applications/*.desktop
%{_datadir}/help/*/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.metainfo.xml
