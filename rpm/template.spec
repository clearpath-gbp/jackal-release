Name:           ros-melodic-jackal-control
Version:        0.6.3
Release:        1%{?dist}
Summary:        ROS jackal_control package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/jackal_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-controller-manager
Requires:       ros-melodic-diff-drive-controller
Requires:       ros-melodic-interactive-marker-twist-server
Requires:       ros-melodic-joint-state-controller
Requires:       ros-melodic-joy
Requires:       ros-melodic-robot-localization
Requires:       ros-melodic-teleop-twist-joy
Requires:       ros-melodic-topic-tools
Requires:       ros-melodic-twist-mux
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roslaunch

%description
Controllers for Jackal

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Jul 18 2019 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.6.3-1
- Autogenerated by Bloom

