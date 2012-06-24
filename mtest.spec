Summary:	Multicast testing tools
Summary(pl.UTF-8):	Narzędzia testujące multicasty
Name:		mtest
Version:	1
Release:	3
License:	custom
Group:		Networking/Daemons
Source0:	http://catarina.usc.edu/pim/pimd/%{name}.tar.gz
# Source0-md5:	79e617d34d4b19a7f9f1c2ee19e455a7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'msend' and 'mrcv' are respectively multicast sender and multicast
receiver tools for multicast routing debugging. They don't have any
"user friendly" interface, but give you a simple and sufficient
control for debugging.

%description -l pl.UTF-8
msend i mrcv to narzędzia do odpowiednio wysyłania i odbierania
multicastów, służące do debuggowania routingu multicastowego. Nie mają
żadnego "przyjaznego użytkownikowi" interfejsu, ale dają prostą i
wystarczającą kontrolę do potrzeb testowania.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install msend mrcv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
