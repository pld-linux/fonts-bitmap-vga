Summary:	vga bitmap font
Summary(pl.UTF-8):	Font bitmapowy vga
Name:		fonts-bitmap-vga
Version:	0
Release:	1
License:	unknown
Group:		Fonts
Source0:	vga.pcf
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_miscfontsdir	%{_fontsdir}/misc

%description
This package contains vga bitmap font (PCF).

%description -l pl.UTF-8
Pakiet ten zawiera bitmapowy (PCF) font vga.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_miscfontsdir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_miscfontsdir}
gzip -9nf $RPM_BUILD_ROOT%{_miscfontsdir}/vga.pcf

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%{_miscfontsdir}/vga.pcf.gz
