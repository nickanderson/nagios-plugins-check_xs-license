# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
# Preamble 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
%define name        nagios-plugins-check_xs-license
%define version     1.2
%define release     1
%define buildroot %{_builddir}/%{name}-%{version}-%{release}-ROOT


Name:         %{name}
Summary:      Citrix XenServer License Check Expiration
Version:      %{version}
Release:      %{release}
License:      BSD
URL:          http://github.com/nickanderson/nagios-plugins-check_xs-license
Group:        NagiosPlugins
Autoreqprov:  no
Source:       %{name}-%{version}.tar.gz
Vendor:       Nick Anderson
Distribution: Centos
Packager:     Nick Anderson <nick@cmdln.org> 
BuildArch:    noarch

BuildRoot: %{buildroot}

%description 
Nagios check plugin to check the status of a Citrix XenServer License for expiration.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
# Prep-Section 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
%prep 
%setup -cn %{name}-%{version}-%{release}

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
# Build-Section 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
%build 
exit 0


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
# Install-Section 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
%install 
echo "BUILDROOT" %{buildroot}
echo "BUILDDIR" %{_builddir}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/nagios/plugins
install -m 0755 check_xs-license %{buildroot}/usr/lib/nagios/plugins


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
/usr/lib/nagios/plugins/check_xs-license


%changelog
* Thu Jun 07 2010 Nick Anderson <nick@cmdln.org> - 1.1-1
Initial RPM build. Do not need 64bit version for now
