Summary:	XShipWars data
Summary(pl):	Dane do XShipWars
Name:		xsw-data
Version:	1.33d
Release:	1
License:	Modified GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://fox.mit.edu/pub/%{name}/xswdata%{version}.tgz
URL:		http://wolfpack.tfu.net/ShipWars/XShipWars/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description 
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet.
This package contains some data needed for the game client.

%description -l pl
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
