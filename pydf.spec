Summary:	Fully colourised df clone written in python
Summary(pl):	Kolorowy klon df napisany w pythonie
Name:		pydf
Version:	0.9.6
Release:	1
License:	Public Domain
Group:		Applications/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(pl):	Aplikacje/System
Group(pt_BR):	Aplicações/Sistema
Source0:	http://melkor.dnp.fmph.uniba.sk/~garabik/pydf/%{name}_%{version}.tar.gz
URL:		http://melkor.dnp.fmph.uniba.sk/~garabik/pydf/
Requires:	python >= 1.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
pydf displays the amount of used and available space on your
filesystems, just like df, but in colours. The output format is
completely customizable.

%description -l pl
pydf wy¶wietla ilo¶æ wykorzystanego i dostêpnego miejsca na systemach
plików, tak jak df, ale w kolorach. Format wyj¶ciowy jest w pe³ni
konfigurowalny.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

install pydf   $RPM_BUILD_ROOT%{_bindir}
install pydfrc $RPM_BUILD_ROOT%{_sysconfdir}
install pydf.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/pydf
%config %{_sysconfdir}/pydfrc

%{_mandir}/man1/pydf.1*
