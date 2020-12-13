%define debug_package %{nil}
Name:           signal-composer-plugins-demo-n2k
#Hexsha: 26f518c962b01d00c472a4507c7f5b6074b6bf8d
Version: 1.0.0
Release:        1%{?dist}
Summary:        A signal composer plugin meant to collect, process and push NMEA200 data coming from the low-can binding, to a redis TSDB
Group:          Development/Libraries/C and C++
License:        APL2.0
URL:            http://git.ovh.iot/redpesk/redpesk-common/canbus-plugins-redpesk.git
Source:         %{name}-%{version}.tar.gz
Patch:          0001-Fix-pkgconfig-issues.patch

BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  afb-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kernel-headers
BuildRequires:  pkgconfig(json-c)
BuildRequires:  afb-libhelpers-devel
BuildRequires:  afb-libcontroller-devel
BuildRequires:  signal-composer-binding-devel
Requires:       canbus-binding
Requires:       canbus-plugins-n2k-basic
Requires:       redis-tsdb-binding
Requires:       signal-composer-binding

%description
%summary

%prep
%autosetup -p 1

%build
%afm_configure_cmake
%make_build -C %{_builddirpkg} %{name}

%install
make DESTDIR=%{?buildroot} -C %{_builddirpkg} install_%{name}

%check

%clean

%files
%{_afmdatadir}/signal-composer-binding/lib/plugins/%{name}.ctlso
%{_afmdatadir}/signal-composer-binding/etc/%{name}.json

%post
# Dirty workaround, waiting for a real config file management
cp %{_afmdatadir}/signal-composer-binding/etc/%{name}.json %{_afmdatadir}/signal-composer-binding/etc/control-signal-composer-config.json

%changelog
* Fri Dec 11 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: 26f518c962b01d00c472a4507c7f5b6074b6bf8d
- Commit message:
- 	demo-n2k plugin basics development.
- 	
- 	This commit introduce the first developments within the demo-n2k plugin
- 	- json configuration file (link with redis & low-can)
- 	- source file (storing & pushing function)
- 	- cmake (installation of the plugin within signal-composer environment)
- 	
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


