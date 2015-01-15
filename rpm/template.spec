Name:           ros-indigo-jackal-msgs
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS jackal_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/jackal_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
Messages exclusive to Jackal, especially for representing low-level motor
commands and sensors.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jan 14 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.4.2-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.4.1-0
- Autogenerated by Bloom

* Fri Dec 12 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.4.0-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.3.0-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.2.1-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.2.0-0
- Autogenerated by Bloom

* Sat Sep 06 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.1-0
- Autogenerated by Bloom

* Fri Sep 05 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.0-0
- Autogenerated by Bloom

