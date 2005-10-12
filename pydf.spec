Summary:	Fully colourised df clone written in Python
Summary(pl):	Kolorowy klon df napisany w Pythonie
Name:		pydf
Version:	0.9.8.5
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	http://melkor.dnp.fmph.uniba.sk/~garabik/pydf/%{name}_%{version}.tar.gz
# Source0-md5:	81af7f7f86bd8e18b192953dc19b4a38
URL:		http://melkor.dnp.fmph.uniba.sk/~garabik/pydf/
BuildRequires:	rpm-pythonprov
Requires:	python >= 1.5.2
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

install pydf	$RPM_BUILD_ROOT%{_bindir}
install pydfrc	$RPM_BUILD_ROOT%{_sysconfdir}
install pydf.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pydf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pydfrc
%{_mandir}/man1/pydf.1*
