%global srcname ndjson

%global pypi_name ndjson

Name:           python3-ndjson
Version:        0.3.0
Release:        1%{?dist}
Summary:        ndjson parser

License:        GPL3
URL:            https://github.com/rhgrant10/ndjson
Source0:        https://github.com/rhgrant10/ndjson/archive/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Support for ndjson. Plain and simple.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -Rf *requirements-dev.txt *.egg-info

%build
CFLAGS="" %{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python3_sitelib}/*

%changelog
* Tue Oct 06 2020 Daniel Pawlik <dpawlik@redhat.com> - 0.3.0-1
- Initial packaging
