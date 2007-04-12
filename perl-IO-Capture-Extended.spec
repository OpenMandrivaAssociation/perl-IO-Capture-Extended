%define real_name IO-Capture-Extended

Summary:	IO::Capture::Extended - Extend functionality of IO::Capture
Name:		perl-%{real_name}
Version:	0.09
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-IO-Capture
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
IO::Capture::Extended is a distribution consisting of two
classes, each of which is a collection of subroutines which are
useful in extending the functionality of CPAN modules 
IO::Capture::Stdout and IO::Capture::Stderr, particularly when
used in a testing context such as that provided by Test::Simple,
Test::More or other modules built on Test::Builder.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/IO/Capture/Stdout
%dir %{perl_vendorlib}/IO/Capture/Extended
%dir %{perl_vendorlib}/IO/Capture/Stderr
%{perl_vendorlib}/IO/Capture/Extended.pm
%{perl_vendorlib}/IO/Capture/Stdout/*pm
%{perl_vendorlib}/IO/Capture/Extended/*pm
%{perl_vendorlib}/IO/Capture/Stderr/*pm
%{_mandir}/*/*

