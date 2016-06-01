Name:           ros-indigo-jackal-tutorials
Version:        0.5.3
Release:        0%{?dist}
Summary:        ROS jackal_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/jackal_msgs
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rosdoc-lite

%description
Jackal's tutorials.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Wed Jun 01 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.5.3-0
- Autogenerated by Bloom

* Thu Mar 24 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.5.2-1
- Autogenerated by Bloom

