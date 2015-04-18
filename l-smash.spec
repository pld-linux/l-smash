Summary:	Loyal to Spec of MPEG4, and Ad-hock Simple Hackwork library
Summary(pl.UTF-8):	Biblioteka L-SMASH (Loyal to Spec of MPEG4, and Ad-hock Simple Hackwork)
Name:		l-smash
Version:	2.3.0
Release:	1
License:	ISC
Group:		Libraries
Source0:	https://github.com/l-smash/l-smash/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	72e68a32e6a671afebbfbbab3b5dd47c
URL:		http://l-smash.github.io/l-smash/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Loyal to Spec of MPEG4, and Ad-hock Simple Hackwork library.

%description -l pl.UTF-8
Biblioteka L-SMASH (Loyal to Spec of MPEG4, and Ad-hock Simple
Hackwork).

%package devel
Summary:	Header files for L-SMASH library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki L-SMASH
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for L-SMASH library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki L-SMASH.

%package static
Summary:	Static L-SMASH library
Summary(pl.UTF-8):	Statyczna biblioteka L-SMASH
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static L-SMASH library.

%description static -l pl.UTF-8
Statyczna biblioteka L-SMASH.

%prep
%setup -q

%build
# not autoconf script
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--cc="%{__cc}" \
	--extra-cflags="%{rpmcflags}" \
	--extra-ldflags="%{rpmldflags}" \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/boxdumper
%attr(755,root,root) %{_bindir}/muxer
%attr(755,root,root) %{_bindir}/remuxer
%attr(755,root,root) %{_bindir}/timelineeditor
%attr(755,root,root) %{_libdir}/liblsmash.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblsmash.so
%{_includedir}/lsmash.h
%{_pkgconfigdir}/liblsmash.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblsmash.a
