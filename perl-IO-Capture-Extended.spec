%define upstream_name    IO-Capture-Extended
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	IO::Capture::Extended - Extend functionality of IO::Capture
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Capture)
BuildArch:	noarch

%description
IO::Capture::Extended is a distribution consisting of two
classes, each of which is a collection of subroutines which are
useful in extending the functionality of CPAN modules 
IO::Capture::Stdout and IO::Capture::Stderr, particularly when
used in a testing context such as that provided by Test::Simple,
Test::More or other modules built on Test::Builder.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/IO/Capture/Stdout
%dir %{perl_vendorlib}/IO/Capture/Extended
%dir %{perl_vendorlib}/IO/Capture/Stderr
%{perl_vendorlib}/IO/Capture/Extended.pm
%{perl_vendorlib}/IO/Capture/Stdout/*pm
%{perl_vendorlib}/IO/Capture/Extended/*pm
%{perl_vendorlib}/IO/Capture/Stderr/*pm
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 402547
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.11-3mdv2009.0
+ Revision: 257310
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.11-1mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.11-1mdv2008.0
+ Revision: 20198
- 0.11


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.09-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.09-1mdk
- initial Mandriva package

