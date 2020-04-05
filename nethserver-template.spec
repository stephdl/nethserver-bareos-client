Summary: nethserver-bareos  is a module to install bareos
%define name nethserver-bareos-client
Name: %{name}
%define version 0.0.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: bareos-fd

BuildRequires: nethserver-devtools
BuildArch: noarch

%description
Bareos (Backup Archiving Recovery Open Sourced) is a reliable, cross-network 
open source software for backup, archiving and recovery of data for all 
well-established operating systems. This is a wrapper to install quickly e client on NethServer

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Sat Apr 04 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- initial
