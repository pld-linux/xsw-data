Summary:	XShipWars data
Summary(pl.UTF-8):   Dane do XShipWars
Name:		xsw-data
Version:	1.33d
Release:	2
License:	GPL-like
Group:		Applications/Games
Source0:	ftp://gd.tuwien.ac.at/games/wolfpack/xswdata-%{version}.tar.bz2
# Source0-md5:	065d7b1b3a526382578c7c5a12d62d80
URL:		http://wolfpack.twu.net/ShipWars/XShipWars/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet. This
package contains some data needed for the game client.

%description -l pl.UTF-8
XShipWars to wysoko konfigurowalny system gry w przestrzeni kosmicznej
dla wielu graczy, zaprojektowany do grania przez Internet. Ten pakiet
zawiera dane potrzebne dla klienta gry.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xshipwars,%{_sysconfdir}}

cd $RPM_BUILD_ROOT%{_datadir}/xshipwars
tar xzf %{SOURCE0}
rm -f etc/xshipwarsrc # comes with client
mv -f etc $RPM_BUILD_ROOT%{_sysconfdir}/xshipwars

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xshipwars/*
%{_sysconfdir}/xshipwars/*
