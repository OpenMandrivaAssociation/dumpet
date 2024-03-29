Summary:	A tool to dump and debug bootable CD images
Name:		dumpet
Version:	2.1
Release:	8
License:	GPLv2+
Group:		System/Base
Url:		https://fedorahosted.org/dumpet/
Source0:	https://fedorahosted.org/releases/d/u/dumpet/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(libxml-2.0)

%description
DumpET is a utility to aid in the debugging of bootable CD-ROM images.

%prep
%setup -q

%build
%make CFLAGS="%{optflags} $(pkg-config --cflags libxml-2.0)"

%install
mkdir -p %{buildroot}/%{_bindir}
%makeinstall_std 

%files
%doc README TODO COPYING
%{_bindir}/dumpet
%{_mandir}/man1/dumpet.1*
