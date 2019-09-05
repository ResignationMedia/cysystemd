%global srcname cysystemd 
%global pkgname systemd
%global sum SystemD wrapper on Cython

# Hack %{?dist} on CentOS build hosts
%if 0%{?rhel} == 6
  %define dist .el6
%endif
%if 0%{?rhel} == 7
  %define dist .el7
%endif

Summary: %{sum}
Name: python%{python3_pkgversion}-%{srcname}
Version: 1.1.0 
Release: 1%{?dist}
Source0: %{srcname}-%{version}.tar.gz
Group: System Environment/Base
License: Apache-2.0
URL: https://github.com/mosquito/cysystemd 
Vendor: mosquito
BuildArch: x86_64
BuildRequires: python%{python3_pkgversion}-devel gcc systemd-devel python%{python3_pkgversion}-Cython
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
# Hopefully, we can use this in the future
%{?python_disable_dependency_generator}

%description
%{sum}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%clean
rm -rf %{buildroot}

%files
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}*.egg-info/

%changelog
* Wed Sep 4 2019 Chris Brundage <chris.brundage@atmosphere.tv> 1.1.0-1 
- First rpm build

