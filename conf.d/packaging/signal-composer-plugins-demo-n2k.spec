%define debug_package %{nil}
Name:           signal-composer-plugins-demo-n2k
Version:        1.0.0
Release:        0%{?dist}
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
%{_afmdatadir}/signal-composer-binding/var/WS310.log
%post
# Dirty workaround, waiting for a real config file management
cp %{_afmdatadir}/signal-composer-binding/etc/%{name}.json %{_afmdatadir}/signal-composer-binding/etc/control-signal-composer-config.json

%changelog
* Wed Dec 16 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20201216+183119+0+gdffd0eab
- Upgrade version from source commit sha: dffd0eabeb707e83087b0a4417974a3493b3f84f
- Commit message:
- 	[docs] Fix broken links
- 	
- 	- Remove ® signs
- 	
- 	- Fix broken links
- 	
- 	- Add description for cloud-publication-binding
- 	
- 	Signed-off-by: Emilie Argouarch <emilie.argouarch@iot.bzh>


* Tue Dec 15 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20201215+150813+0+g569e61e0
- Upgrade version from source commit sha: 569e61e0f53476e11abf41bbfdf931a66ef71f8c
- Commit message:
- 	[sensor log] Add the sensor log to the repository
- 	
- 	If the user do not have the sensor for the demo,
- 	it can be do by using canplayer on the log files
- 	
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Tue Dec 15 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20201215+135435+0+g810d721f
- Upgrade version from source commit sha: 810d721f1a1c5b07c0d0a1388dc11202d40a84f3
- Commit message:
- 	[docs] First layout of documentation
- 	
- 	- demo-n2k documentation: not yet finished
- 	- plugin's documentation: nearly done
- 	
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


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


