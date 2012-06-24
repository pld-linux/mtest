Summary:	Multicast testing tools
Name:		mtest
Version:	1
Release:	0
License:	Custom
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	http://catarina.usc.edu/pim/pimd/%{name}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'msend' and 'mrcv' are respectively multicast sender and multicast
receiver tools for multicast routing debugging. They don't have any
"user friendly" interface, but give you a simple and sufficient
control for debugging.

%prep
%setup -q -n %{name}

%build
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install msend mrcv $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
