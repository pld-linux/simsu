Summary:	A basic Sudoku game
Summary(pl.UTF-8):	Zwykła gra Sudoku
Name:		simsu
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://gottcode.org/simsu/%{name}-%{version}.tar.gz
# Source0-md5:	bc021b15443165153143c81689da5be6
Patch0:		%{name}-desktop.patch
URL:		http://gottcode.org/simsu/
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A basic Sudoku game.

%description -l pl.UTF-8
Zwykła gra Sudoku.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install simsu $RPM_BUILD_ROOT%{_bindir}
install simsu.desktop $RPM_BUILD_ROOT%{_desktopdir}
install simsu.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/simsu
%{_desktopdir}/simsu.desktop
%{_pixmapsdir}/simsu.png
