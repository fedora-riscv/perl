%define multilib_64_archs x86_64 s390x ppc64 sparc64
%define perl_archname %{_arch}-%{_os}-thread-multi
%define new_perl_lib  $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}:$RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{version}
%define comp_perl_lib $RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{version}:$RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{version}
%define new_arch_lib  $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{perl_archname}
%define comp_arch_lib $RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{version}/%{perl_archname}
%define new_perl_flags LD_PRELOAD=/%{new_arch_lib}/CORE/libperl.so LD_LIBRARY_PATH=%{new_arch_lib}/CORE PERL5LIB=%{new_perl_lib}:%{comp_perl_lib}
%define new_perl %{new_perl_flags} $RPM_BUILD_ROOT/%{_bindir}/perl

%define db4_major %(grep "DB_VERSION_MAJOR" /usr/include/db.h | cut -f3)
%define db4_minor %(grep "DB_VERSION_MINOR" /usr/include/db.h | cut -f3)
%define db4_patch %(grep "DB_VERSION_PATCH" /usr/include/db.h | cut -f3)

%define perl_version    5.10.0
%define perl_epoch      4

Name:           perl
Version:        %{perl_version}
Release:        31%{?dist}
Epoch:          %{perl_epoch}
Summary:        The Perl programming language
Group:          Development/Languages
# Modules Tie::File and Getopt::Long are licenced under "GPLv2+ or Artistic,"
# we have to reflect that in the sub-package containing them.
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic)
Url:            http://www.perl.org/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RG/RGARCIA/perl-%{perl_version}.tar.gz
Source11:       filter-requires.sh
Source12:       perl-5.8.0-libnet.cfg
# Specific to Fedora/RHEL
Patch1:         perl-5.8.0-root.patch

# Removes date check, Fedora/RHEL specific
Patch2:         perl-5.10.0-perlbug-tag.patch

# Fedora/RHEL use links instead of lynx
Patch3:         perl-5.10.0-links.patch

# work around annoying rpath issue
# This is only relevant for Fedora, as it is unlikely
# that upstream will assume the existence of a libperl.so
Patch4:         perl-5.8.8-rpath-make.patch

# Fedora/RHEL only (64bit only)
Patch5:         perl-5.8.0-libdir64.patch

# Fedora/RHEL specific (use libresolv instead of libbind)
Patch6:         perl-5.10.0-libresolv.patch

# FIXME: May need the "Fedora" references removed before upstreaming
Patch7:         perl-5.10.0-USE_MM_LD_RUN_PATH.patch

# Skip hostname tests, since hostname lookup isn't available in Fedora
# buildroots by design.
Patch8:         perl-5.10.0-disable_test_hosts.patch

# Bump Sys::Syslog to 0.24 to fix test failure case
Patch9:         perl-5.10.0-SysSyslog-0.24.patch

# The Fedora builders started randomly failing this futime test
# only on x86_64, so we just don't run it. Works fine on normal
# systems.
Patch10:        perl-5.10.0-x86_64-io-test-failure.patch

# http://public.activestate.com/cgi-bin/perlbrowse/p/32891
Patch11:        32891.patch

# Update Module::Load::Conditional to 0.24 for clean upgrade
Patch12:	perl-5.10.0-Module-Load-Conditional-0.24.patch

# Upgrade Module::CoreList to 2.14
Patch13:	perl-5.10.0-Module-CoreList2.14.patch

# Upgrade CGI to 3.38
Patch14:	perl-5.10.0-CGI-3.38.patch

# Problem with assertion - add upstream patch
Patch15:	perl-5.10.0-bz448392.patch

# Wrong access test
Patch16:	perl-5.10.0-accessXOK.patch

# CVE-2008-2827 perl: insecure use of chmod in rmtree
Patch17:	perl-5.10.0-CVE-2008-2827.patch

# pos function handle unicode ok
Patch18:	perl-5.10.0-pos.patch

BuildRoot:      %{_tmppath}/%{name}-%{perl_version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  tcsh, dos2unix, man, groff
BuildRequires:  gdbm-devel, db4-devel, zlib-devel
# For tests
BuildRequires:  procps, rsyslog

# The long line of Perl provides.

# These provides are needed by the perl pkg itself with auto-generated perl.req
Provides: perl(VMS::Filespec)
Provides: perl(VMS::Stdio)

# Compat provides
Provides: perl(:MODULE_COMPAT_5.10.0)

# Threading provides
Provides: perl(:WITH_ITHREADS)
Provides: perl(:WITH_THREADS)
# Largefile provides
Provides: perl(:WITH_LARGEFILES)
# PerlIO provides
Provides: perl(:WITH_PERLIO)
# File provides
Provides: perl(abbrev.pl)
Provides: perl(assert.pl)
Provides: perl(bigfloat.pl)
Provides: perl(bigint.pl)
Provides: perl(bigrat.pl)
Provides: perl(bytes_heavy.pl)
Provides: perl(cacheout.pl)
Provides: perl(complete.pl)
Provides: perl(ctime.pl)
Provides: perl(dotsh.pl)
Provides: perl(dumpvar.pl)
Provides: perl(exceptions.pl)
Provides: perl(fastcwd.pl)
Provides: perl(find.pl)
Provides: perl(finddepth.pl)
Provides: perl(flush.pl)
Provides: perl(ftp.pl)
Provides: perl(getcwd.pl)
Provides: perl(getopt.pl)
Provides: perl(getopts.pl)
Provides: perl(hostname.pl)
Provides: perl(importenv.pl)
Provides: perl(look.pl)
Provides: perl(newgetopt.pl)
Provides: perl(open2.pl)
Provides: perl(open3.pl)
Provides: perl(perl5db.pl)
Provides: perl(pwd.pl)
Provides: perl(shellwords.pl)
Provides: perl(stat.pl)
Provides: perl(syslog.pl)
Provides: perl(tainted.pl)
Provides: perl(termcap.pl)
Provides: perl(timelocal.pl)
Provides: perl(utf8_heavy.pl)
Provides: perl(validate.pl)
Provides: perl(Carp::Heavy)

# Long history in 3rd-party repositories:
Provides: perl-File-Temp = 0.18
Obsoletes: perl-File-Temp < 0.18


Requires: perl-libs = %{perl_epoch}:%{perl_version}-%{release}
Requires: db4 = %{db4_major}.%{db4_minor}.%{db4_patch}

# We need this to break the dependency loop, and ensure that perl-libs 
# gets installed before perl.
Requires(post): perl-libs

# Filter the automatically generated dependencies.
#
# The original script might be /usr/lib/rpm/perl.req or
# /usr/lib/rpm/redhat/perl.req, better use the original value of the macro:
%{expand:%%define prev__perl_requires %{__perl_requires}} 
%define __perl_requires %{SOURCE11} %{prev__perl_requires}

# When _use_internal_dependency_generator is 0, the perl.req script is
# called from /usr/lib/rpm{,/redhat}/find-requires.sh
# Likewise:
%{expand:%%define prev__find_requires %{__find_requires}} 
%define __find_requires %{SOURCE11} %{prev__find_requires}


%description
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications are system
administration utilities and web programming.  A large proportion of
the CGI scripts on the web are written in Perl.  You need the perl
package installed on your system so that your system can handle Perl
scripts.

Install this package if you want to program in Perl or enable your
system to handle Perl scripts.

%package libs
Summary:        The libraries for the perl runtime
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description libs
The libraries for the perl runtime


%package devel
Summary:        Header files for use in perl development
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description devel
This package contains header files and development modules.
Most perl packages will need to install perl-devel to build.


%package suidperl
Summary:        Suidperl, for use with setuid perl scripts
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description suidperl
Suidperl is a setuid binary copy of perl that allows for (hopefully)
more secure running of setuid perl scripts.


%package Archive-Extract
Summary:        Generic archive extracting mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.24
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Archive-Extract
Archive::Extract is a generic archive extraction mechanism.


%package Archive-Tar
Summary:        A module for Perl manipulation of .tar files
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
# It's really 1.37_01, but we drop the _01.
Version:        1.37
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Compress::Zlib), perl(IO::Zlib)

%description Archive-Tar
Archive::Tar provides an object oriented mechanism for handling tar
files.  It provides class methods for quick and easy files handling
while also allowing for the creation of tar file objects for custom
manipulation.  If you have the IO::Zlib module installed, Archive::Tar
will also support compressed or gzipped tar files.


%package Compress-Raw-Zlib
Summary:        Low-Level Interface to the zlib compression library
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        2.008
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Compress-Raw-Zlib
This module provides a Perl interface to the zlib compression library.
It is used by IO::Compress::Zlib.


%package Compress-Zlib
Summary:        A module providing Perl interfaces to the zlib compression library
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        2.008
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Compress-Zlib
The Compress::Zlib module provides a Perl interface to the zlib
compression library. Most of the functionality provided by zlib is
available in Compress::Zlib.

The module can be split into two general areas of functionality,
namely in-memory compression/decompression and read/write access to
gzip files.


%package CPAN
Summary:        Query, download and build perl modules from CPAN sites
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        1.9205
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Provides:       cpan = %{version}

%description CPAN
Query, download and build perl modules from CPAN sites.


%package CPANPLUS
Summary:        API & CLI access to the CPAN mirrors
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        0.84
Requires:       perl(IPC::Run) >= 0.79
Requires:       perl(Module::Pluggable) >= 2.4
Requires:       perl(Module::CoreList)
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Provides:       perl-CPANPLUS-Dist-Build = 0.06
Obsoletes:	perl-CPANPLUS-Dist-Build <= 0.05

%description CPANPLUS
The CPANPLUS library is an API to the CPAN mirrors and a collection of
interactive shells, commandline programs, etc, that use this API.


%package Digest-SHA
Summary:        Perl extension for SHA-1/224/256/384/512
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        5.45
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Digest-SHA
Digest::SHA is a complete implementation of the NIST Secure Hash
Standard.  It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests.  The
module can handle all types of input, including partial-byte data.


%package ExtUtils-CBuilder
Summary:        Compile and link C code for Perl modules
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.21
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-CBuilder
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was
motivated by the Module::Build project, but may be useful for other
purposes as well.


%package ExtUtils-Embed
Summary:        Utilities for embedding Perl in C/C++ applications
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        1.27
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-Embed
Utilities for embedding Perl in C/C++ applications.


%package ExtUtils-MakeMaker
Summary:        Create a module Makefile
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
# It's really 6.36_01, but we drop the _01.
Version:        6.36
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Test::Harness)

%description ExtUtils-MakeMaker
Create a module Makefile.


%package ExtUtils-ParseXS
Summary:        Module and a script for converting Perl XS code into C code
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
# It's really 2.18_02, but we drop the _02.
Version:        2.18
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-ParseXS
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and
creates the glue necessary to let Perl access those functions.


%package File-Fetch
Summary:        Generic file fetching mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        0.14
Requires:       perl(IPC::Cmd) >= 0.36
Requires:       perl(Module::Load::Conditional) >= 0.04
Requires:       perl(Params::Check) >= 0.07
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description File-Fetch
File::Fetch is a generic file fetching mechanism.


%package IO-Compress-Base
Summary:        Base Class for IO::Compress modules
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        2.008
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Compress-Base
This module is the base class for all IO::Compress and IO::Uncompress
modules. This module is not intended for direct use in application
code. Its sole purpose is to to be sub-classed by IO::Compress
modules.


%package IO-Compress-Zlib
Summary:        Perl interface to allow reading and writing of gzip and zip data
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
# Really 1.23_01, but we drop the _01.
Version:        2.008
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Compress-Zlib
This module provides an "IO::"-style Perl interface to "Compress::Zlib"


%package IO-Zlib
Summary:        Perl IO:: style interface to Compress::Zlib
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        1.07
Requires:       perl(Compress::Zlib)
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Zlib
This modules provides an IO:: style interface to the Compress::Zlib
package. The main advantage is that you can use an IO::Zlib object in
much the same way as an IO::File object so you can have common code
that doesn't know which sort of file it is using.


%package IPC-Cmd
Summary:        Finding and running system commands made easy
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
# Really 0.40_1, but we drop the _1.
Version:        0.40
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IPC-Cmd
IPC::Cmd allows you to run commands, interactively if desired, in a
platform independent way, but have them still work.


%package Locale-Maketext-Simple
Summary:        Simple interface to Locale::Maketext::Lexicon
Group:          Development/Libraries
License:        MIT
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.18
Requires:	perl = %{perl_epoch}:%{perl_version}-%{release}

%description Locale-Maketext-Simple
This module is a simple wrapper around Locale::Maketext::Lexicon, designed
to alleviate the need of creating Language Classes for module authors.


%package Log-Message
Summary:        Generic message storage mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.01
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
# Add a versioned provides, since we pull the unversioned one out.
Provides:       perl(Log::Message::Handlers) = %{version}

%description Log-Message
Log::Message is a generic message storage mechanism. It allows you to 
store messages on a stack -- either shared or private -- and assign meta-data 
to it. Some meta-data will automatically be added for you, like a timestamp
and a stack trace, but some can be filled in by the user, like a tag by
which to identify it or group it, and a level at which to handle the
message (for example, log it, or die with it).


%package Log-Message-Simple
Summary:        Simplified frontend to Log::Message
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        0.04
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Log-Message-Simple
This module provides standardized logging facilities using the
Log::Message module.


%package Module-Build
Summary:        Perl module for building and installing Perl modules
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
# Really 0.2808_01, but we drop the _01.
Version:        0.2808
Requires:       perl(Archive::Tar) >= 1.08
Requires:       perl(ExtUtils::CBuilder) >= 0.15
Requires:       perl(ExtUtils::ParseXS) >= 1.02
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Build
Module::Build is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to ExtUtils::MakeMaker.
Developers may alter the behavior of the module through subclassing in a
much more straightforward way than with MakeMaker. It also does not 
require a make on your system - most of the Module::Build code is pure-perl and
written in a very cross-platform way. In fact, you don't even need a 
shell, so even platforms like MacOS (traditional) can use it fairly easily. Its
only prerequisites are modules that are included with perl 5.6.0, and it
works fine on perl 5.005 if you can install a few additional modules.


%package Module-CoreList
Summary:        Perl core modules indexed by perl versions
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        2.14
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(version)

%description Module-CoreList
Module::CoreList contains the hash of hashes %Module::CoreList::version,
this is keyed on perl version as indicated in $].  The second level hash
is module => version pairs.


%package Module-Load
Summary:        Runtime require of both modules and files
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.12
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Load
Module::Load eliminates the need to know whether you are trying to
require either a file or a module.


%package Module-Load-Conditional
Summary:        Looking up module information / loading at runtime
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        0.24
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Load-Conditional
Module::Load::Conditional provides simple ways to query and possibly 
load
any of the modules you have installed on your system during runtime.


%package Module-Loaded
Summary:        Mark modules as loaded or unloaded
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.01
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Loaded
When testing applications, often you find yourself needing to provide
functionality in your test environment that would usually be provided by
external modules. Rather than munging the %INC by hand to mark these
external modules as loaded, so they are not attempted to be loaded by
perl, this module offers you a very simple way to mark modules as loaded
and/or unloaded.


%package Module-Pluggable
Summary:        Automatically give your module the ability to have plugins
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        3.60
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Pluggable
Provides a simple but, hopefully, extensible way of having 'plugins' for
your module.


%package Object-Accessor
Summary:        Perl module that allows per object accessors
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.32
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Object-Accessor
Object::Accessor provides an interface to create per object accessors 
(as opposed to per Class accessors, as, for example, Class::Accessor 
provides).


%package Package-Constants
Summary:        List all constants declared in a package
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.01
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Package-Constants
Package::Constants lists all the constants defined in a certain package.
This can be useful for, among others, setting up an autogenerated
@EXPORT/@EXPORT_OK for a Constants.pm file.


%package Params-Check
Summary:        Generic input parsing/checking mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        0.26
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Params-Check
Params::Check is a generic input parsing/checking mechanism.


%package Pod-Escapes
Summary:        Perl module for resolving POD escape sequences
Group:   	Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        1.04
Requires:	perl = %{perl_epoch}:%{perl_version}-%{release}

%description Pod-Escapes
This module provides things that are useful in decoding Pod E<...>
sequences. Presumably, it should be used only by Pod parsers and/or
formatters.


%package Pod-Simple
Summary:        Framework for parsing POD documentation
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        3.05
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Pod-Simple
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules.


%package Term-UI
Summary:        Term::ReadLine UI made easy
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        0.18
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Log::Message::Simple)

%description Term-UI
Term::UI is a transparent way of eliminating the overhead of having to
format a question and then validate the reply, informing the user if the
answer was not proper and re-issuing the question.


%package Test-Harness
Summary:        Run Perl standard test scripts with statistics
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        2.64
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Test-Harness
Run Perl standard test scripts with statistics.


%package Test-Simple
Summary:        Basic utilities for writing tests
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        0.72
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Test-Simple
Basic utilities for writing tests.


%package Time-Piece
Summary:        Time objects from localtime and gmtime
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        1.12
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Time-Piece
The Time::Piece module replaces the standard localtime and gmtime functions
with implementations that return objects.  It does so in a backwards
compatible manner, so that using localtime or gmtime as documented in
perlfunc still behave as expected.


%package version
Summary:        Perl extension for Version Objects
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          3
Version:        0.74
Requires:	perl = %{perl_epoch}:%{perl_version}-%{release}

%description version
Perl extension for Version Objects


%package core
Summary:        Base perl metapackage
Group:          Development/Languages
# This rpm doesn't contain any copyrightable material.
# Nevertheless, it needs a License tag, so we'll use the generic
# "perl" license.
License:        GPL+ or Artistic
Epoch:          0
Version:        %{perl_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-libs = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-devel = %{perl_epoch}:%{perl_version}-%{release}

Requires:       perl-Archive-Extract, perl-Archive-Tar, perl-Compress-Raw-Zlib, perl-Compress-Zlib, perl-CPAN,
Requires:       perl-CPANPLUS, perl-Digest-SHA, perl-ExtUtils-CBuilder,
Requires:       perl-ExtUtils-Embed, perl-ExtUtils-MakeMaker, perl-ExtUtils-ParseXS,
Requires:       perl-File-Fetch, perl-IO-Compress-Base, perl-IO-Compress-Zlib, perl-IO-Zlib,
Requires:       perl-IPC-Cmd, perl-Locale-Maketext-Simple, perl-Log-Message, perl-Log-Message-Simple,
Requires:       perl-Module-Build, perl-Module-CoreList, perl-Module-Load,
Requires:       perl-Module-Load-Conditional, perl-Module-Loaded,
Requires:       perl-Module-Pluggable, perl-Object-Accessor, perl-Package-Constants,
Requires:       perl-Params-Check, perl-Pod-Escapes, perl-Pod-Simple, perl-Term-UI, 
Requires:       perl-Test-Harness, perl-Test-Simple, perl-Time-Piece, perl-version
# Note: perl-suidperl has always been an independent subpackage
# We don't want perl-core to drag it in.

%description core
A metapackage which requires all of the perl bits and modules in the
upstream tarball from perl.org.


%prep
%setup -q 
%patch1 -p1
%patch2 -p1
%patch3 -p1
# This patch breaks sparc64 compilation
# We should probably consider removing it for all arches.
%ifnarch sparc64
%patch4 -p1
%endif
%ifarch %{multilib_64_archs}
%patch5 -p1
%endif
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

#
# Candidates for doc recoding (need case by case review):
# find . -name "*.pod" -o -name "README*" -o -name "*.pm" | xargs file -i | grep charset= | grep -v '\(us-ascii\|utf-8\)'
recode()
{
        iconv -f "$2" -t utf-8 < "$1" > "${1}_"
        mv -f "${1}_" "$1"
}
recode README.cn euc-cn
recode README.jp euc-jp
recode README.ko euc-kr
recode README.tw big5
recode pod/perlebcdic.pod iso-8859-1
recode pod/perlhack.pod iso-8859-1
recode pod/perlhist.pod iso-8859-1
recode pod/perlothrtut.pod iso-8859-1
recode pod/perlthrtut.pod iso-8859-1
recode lib/Unicode/Collate.pm iso-8859-1
for i in Changes*; do
    recode $i iso-8859-1
done
recode AUTHORS iso-8859-1


find . -name \*.orig -exec rm -fv {} \;

# Oh, the irony. Perl generates some non-versioned provides we don't need.
# Each of these has a versioned provide, which we keep.
cat << EOF > perl-prov
#!/bin/sh
%{__perl_provides} $* |\
    sed -e '/^perl(Carp)$/d' |\
    sed -e '/^perl(DynaLoader)$/d' |\
    sed -e '/^perl(Locale::Maketext)$/d' |\
    sed -e '/^perl(Log::Message::Handlers)$/d' |\
    sed -e '/^perl(Math::BigInt)$/d' |\
    sed -e '/^perl(Net::Config)$/d' |\
    sed -e '/^perl(Tie::Hash)$/d' |\
    sed -e '/^perl(bigint)$/d' |\
    sed -e '/^perl(bigrat)$/d' |\
    sed -e '/^perl(bytes)$/d' |\
    sed -e '/^perl(utf8)$/d' |\
    sed -e '/^perl(DB)$/d'
EOF
%define __perl_provides %{_builddir}/%{name}-%{perl_version}/perl-prov
chmod +x %{__perl_provides}

# Configure Compress::Zlib to use system zlib
sed -i "s|BUILD_ZLIB      = True|BUILD_ZLIB      = False|" ext/Compress/Raw/Zlib/config.in
sed -i "s|INCLUDE         = ./zlib-src|INCLUDE         = %{_includedir}|" ext/Compress/Raw/Zlib/config.in
sed -i "s|LIB             = ./zlib-src|LIB             = %{_libdir}|" ext/Compress/Raw/Zlib/config.in

%build
echo "RPM Build arch: %{_arch}"

# use "lib", not %{_lib}, for privlib, sitelib, and vendorlib

# Because of the typo in the first F-9 release, we have to support the default
# sitedir as well for 32bit archs, via -Dotherlibdirs.  No need to mention the
# arch-specific subdir though, perl will add it, if it exists.

/bin/sh Configure -des -Doptimize="$RPM_OPT_FLAGS -DPERL_USE_SAFE_PUTENV" \
        -Dversion=%{perl_version} \
        -Dmyhostname=localhost \
        -Dperladmin=root@localhost \
        -Dcc='%{__cc}' \
        -Dcf_by='Red Hat, Inc.' \
        -Dinstallprefix=%{_prefix} \
        -Dprefix=%{_prefix} \
        -Dprivlib="%{_prefix}/lib/perl5/%{perl_version}" \
        -Dsitelib="%{_prefix}/local/lib/perl5/site_perl/%{perl_version}" \
        -Dvendorlib="%{_prefix}/lib/perl5/vendor_perl/%{perl_version}" \
        -Darchlib="%{_libdir}/perl5/%{perl_version}/%{perl_archname}" \
        -Dsitearch="%{_prefix}/local/%{_lib}/perl5/site_perl/%{perl_version}/%{perl_archname}" \
        -Dvendorarch="%{_libdir}/perl5/vendor_perl/%{perl_version}/%{perl_archname}" \
        -Darchname=%{perl_archname} \
%ifarch %{multilib_64_archs}
        -Dlibpth="/usr/local/lib64 /lib64 %{_prefix}/lib64" \
%else
	-Dotherlibdirs="%{_prefix}/lib/perl5/site_perl/%{perl_version}" \
%endif
%ifarch sparc sparcv9
        -Ud_longdbl \
%endif
        -Dvendorprefix=%{_prefix} \
        -Dsiteprefix=%{_prefix}/local \
        -Duseshrplib \
        -Dusethreads \
        -Duseithreads \
        -Duselargefiles \
        -Dd_dosuid \
        -Dd_semctl_semun \
        -Di_db \
        -Ui_ndbm \
        -Di_gdbm \
        -Di_shadow \
        -Di_syslog \
        -Dman3ext=3pm \
        -Duseperlio \
        -Dinstallusrbinperl=n \
        -Ubincompat5005 \
        -Uversiononly \
        -Dpager='/usr/bin/less -isr' \
        -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
        -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
        -Ud_endservent_r_proto -Ud_setservent_r_proto \
        -Dscriptdir='%{_bindir}'

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%ifarch %{multilib_64_archs}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/%{perl_version}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/vendor_perl/%{perl_version}/auto
%ifarch x86_64
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/vendor_perl/%{perl_version}/i386-linux-thread-multi/auto
%endif
%ifarch s390x
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/vendor_perl/%{perl_version}/s390-linux-thread-multi/auto
%endif
%ifarch ppc64
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/vendor_perl/%{perl_version}/ppc-linux-thread-multi/auto
%endif
%ifarch sparc64
mkdir -p -m 755 $RPM_BUILD_ROOT%{_prefix}/lib/perl5/vendor_perl/%{perl_version}/sparc-linux-thread-multi/auto
%endif
%endif

# perl doesn't create this module, but modules put things in it, so we need to own it.
mkdir -p -m 755 ${RPM_BUILD_ROOT}%{_libdir}/perl5/vendor_perl/%{perl_version}/%{perl_archname}/auto

install -p -m 755 utils/pl2pm ${RPM_BUILD_ROOT}%{_bindir}/pl2pm

for i in asm/termios.h syscall.h syslimits.h syslog.h sys/ioctl.h sys/socket.h sys/time.h wait.h
do
  %{new_perl} $RPM_BUILD_ROOT/%{_bindir}/h2ph -a \
              -d $RPM_BUILD_ROOT%{_libdir}/perl5/%{perl_version}/%{perl_archname} $i || /bin/true
done


for dir in $(%{new_perl} -le 'print join("\n", @INC)' | grep '^%{_prefix}/lib')
do
  mkdir -p $RPM_BUILD_ROOT/$dir
done

for dir in $(%{new_perl} -le 'print join("\n", @INC)' | grep '^%{_libdir}')
do
  mkdir -p $RPM_BUILD_ROOT/$dir
done

#
# libnet configuration file
#
mkdir -p -m 755 $RPM_BUILD_ROOT/%{_libdir}/perl5/%{perl_version}/Net
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT/%{_libdir}/perl5/%{perl_version}/Net/libnet.cfg

#
# Core modules removal
#
find $RPM_BUILD_ROOT -name '*NDBM*' | xargs rm -rfv

find $RPM_BUILD_ROOT -type f -name '*.bs' -a -empty -exec rm -f {} ';'

# Install sample cgi scripts (this used to happen automatically?)
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/%{perl_version}/CGI/eg/
cp -a lib/CGI/eg/* $RPM_BUILD_ROOT/usr/lib/perl5/%{perl_version}/CGI/eg/

# Cleanup binary paths and make cgi files executable
pushd $RPM_BUILD_ROOT/usr/lib/perl5/%{perl_version}/CGI/eg/
  for i in *.cgi make_links.pl RunMeFirst ; do
    sed -i 's|/usr/local/bin/perl|%{_bindir}/perl|g' $i
    chmod +x $i
  done
popd

# miniperl? As an interpreter? How odd.
sed -i 's|./miniperl|%{_bindir}/perl|' $RPM_BUILD_ROOT/usr/lib/perl5/%{perl_version}/ExtUtils/xsubpp
chmod +x $RPM_BUILD_ROOT/usr/lib/perl5/%{perl_version}/ExtUtils/xsubpp

# Don't need the .packlist
rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{perl_version}/%{perl_archname}/.packlist

# Fix some manpages to be UTF-8
pushd $RPM_BUILD_ROOT%{_mandir}/man1/
  for i in perl588delta.1 perldelta.1 ; do
    iconv -f MS-ANSI -t UTF-8 $i --output new-$i
    rm -rf $i
    mv new-$i $i
  done
popd

chmod -R u+w $RPM_BUILD_ROOT/*

# Compress Changes* to save space
%{__gzip} Changes*

# Local patch tracking
cd $RPM_BUILD_ROOT%{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/
perl -x patchlevel.h 'Fedora Patch1: Permit suidperl to install as nonroot'
perl -x patchlevel.h 'Fedora Patch2: Removes date check, Fedora/RHEL specific'
perl -x patchlevel.h 'Fedora Patch3: Fedora/RHEL use links instead of lynx'
%ifnarch sparc64
perl -x patchlevel.h 'Fedora Patch4: Work around annoying rpath issue'
%endif
%ifarch %{multilib_64_archs}
perl -x patchlevel.h 'Fedora Patch5: support for libdir64'
%endif
perl -x patchlevel.h 'Fedora Patch6: use libresolv instead of libbind'
perl -x patchlevel.h 'Fedora Patch7: USE_MM_LD_RUN_PATH'
perl -x patchlevel.h 'Fedora Patch8: Skip hostname tests, due to builders not being network capable'
perl -x patchlevel.h 'Fedora Patch9: Update Sys::Syslog to 0.24'
perl -x patchlevel.h 'Fedora Patch10: Dont run one io test due to random builder failures'
perl -x patchlevel.h '32891 fix big slowdown in 5.10 @_ parameter passing'
perl -x patchlevel.h 'Fedora Patch12: Update Module::Load::Conditional to 0.24'
perl -x patchlevel.h 'Fedora Patch13: Upgrade Module::CoreList to 2.14'
perl -x patchlevel.h 'Fedora Patch14: Upgrade CGI to 3.38'
perl -x patchlevel.h 'Fedora Patch15: Adopt upstream commit for assertion'
perl -x patchlevel.h 'Fedora Patch16: Access permission - rt49003'
perl -x patchlevel.h 'Fedora Patch17: CVE-2008-2827 perl: insecure use of chmod in rmtree'
perl -x patchlevel.h 'Fedora Patch18: pos function handle unicode correct'

%clean
rm -rf $RPM_BUILD_ROOT

%check
%ifnarch sparc64
make test
%endif

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc Artistic AUTHORS Changes* Copying README
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_bindir}/*
%{_libdir}/perl5/
%ifarch %{multilib_64_archs}
%{_prefix}/lib/perl5/
%endif

# libs
%exclude %{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/libperl.so

# devel
%exclude %{_bindir}/enc2xs
%exclude %{_mandir}/man1/enc2xs*
%exclude %{_bindir}/h2xs
%exclude %{_mandir}/man1/h2xs*
%exclude %{_bindir}/libnetcfg
%exclude %{_mandir}/man1/libnetcfg*
%exclude %{_bindir}/perlivp
%exclude %{_mandir}/man1/perlivp*
%exclude %{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/*.h
%exclude %{_bindir}/xsubpp
%exclude %{_mandir}/man1/xsubpp*

# suidperl
%exclude %{_bindir}/suidperl
%exclude %{_bindir}/sperl%{perl_version}

# Archive-Extract
%exclude %{_prefix}/lib/perl5/%{perl_version}/Archive/Extract.pm
%exclude %{_mandir}/man3/Archive::Extract.3*

# Archive-Tar
%exclude %{_bindir}/ptar
%exclude %{_bindir}/ptardiff
%exclude %{_prefix}/lib/perl5/%{perl_version}/Archive/Tar/
%exclude %{_prefix}/lib/perl5/%{perl_version}/Archive/Tar.pm
%exclude %{_mandir}/man1/ptar.1*
%exclude %{_mandir}/man1/ptardiff.1*
%exclude %{_mandir}/man3/Archive::Tar*

# CPAN
%exclude %{_bindir}/cpan
%exclude %{_prefix}/lib/perl5/%{perl_version}/CPAN/
%exclude %{_prefix}/lib/perl5/%{perl_version}/CPAN.pm
%exclude %{_mandir}/man1/cpan.1*
%exclude %{_mandir}/man3/CPAN.*
%exclude %{_mandir}/man3/CPAN:*

# CPANPLUS
%exclude %{_bindir}/cpan2dist
%exclude %{_bindir}/cpanp
%exclude %{_bindir}/cpanp-run-perl
%exclude %{_prefix}/lib/perl5/%{perl_version}/CPANPLUS/
%exclude %{_prefix}/lib/perl5/%{perl_version}/CPANPLUS.pm
%exclude %{_mandir}/man1/cpan2dist.1*
%exclude %{_mandir}/man1/cpanp.1*
%exclude %{_mandir}/man3/CPANPLUS*

# Compress::Raw::Zlib
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/Compress
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/Compress/Raw/
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/auto/Compress
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/auto/Compress/Raw/
%exclude %{_mandir}/man3/Compress::Raw::Zlib*

# Compress::Zlib
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/Compress/Zlib.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/auto/Compress/Zlib/
%exclude %{_mandir}/man3/Compress::Zlib*

# Digest::SHA
%exclude %{_bindir}/shasum
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/Digest/SHA.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/auto/Digest/SHA/
%exclude %{_mandir}/man1/shasum.1*
%exclude %{_mandir}/man3/Digest::SHA.3*

# ExtUtils::CBuilder
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/CBuilder/
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/CBuilder.pm
%exclude %{_mandir}/man3/ExtUtils::CBuilder*

# ExtUtils::Embed
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Embed.pm
%exclude %{_mandir}/man3/ExtUtils::Embed*

# ExtUtils::MakeMaker
%exclude %{_bindir}/instmodsh
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Command/
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Install.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Installed.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Liblist/
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Liblist.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MakeMaker/
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MakeMaker.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MANIFEST.SKIP
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MM*.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MY.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Manifest.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Mkbootstrap.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Mksymlists.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Packlist.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/testlib.pm
%exclude %{_mandir}/man1/instmodsh.1*
%exclude %{_mandir}/man3/ExtUtils::Command::MM*
%exclude %{_mandir}/man3/ExtUtils::Install.3*
%exclude %{_mandir}/man3/ExtUtils::Installed.3*
%exclude %{_mandir}/man3/ExtUtils::Liblist.3*
%exclude %{_mandir}/man3/ExtUtils::MM*
%exclude %{_mandir}/man3/ExtUtils::MY.3*
%exclude %{_mandir}/man3/ExtUtils::MakeMaker*
%exclude %{_mandir}/man3/ExtUtils::Manifest.3*
%exclude %{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%exclude %{_mandir}/man3/ExtUtils::Mksymlists.3*
%exclude %{_mandir}/man3/ExtUtils::Packlist.3*
%exclude %{_mandir}/man3/ExtUtils::testlib.3*

# ExtUtils::ParseXS
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/ParseXS.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/ExtUtils/xsubpp
%exclude %{_mandir}/man3/ExtUtils::ParseXS.3*

# File::Fetch
%exclude %{_prefix}/lib/perl5/%{perl_version}/File/Fetch.pm
%exclude %{_mandir}/man3/File::Fetch.3*

# IO::Compress::Base
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/File/GlobMapper.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Base/
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Base.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/AnyUncompress.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Base.pm
%exclude %{_mandir}/man3/File::GlobMapper.*
%exclude %{_mandir}/man3/IO::Compress::Base.*
%exclude %{_mandir}/man3/IO::Uncompress::AnyUncompress.*
%exclude %{_mandir}/man3/IO::Uncompress::Base.*

# IO::Compress::Zlib
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Adapter/
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Deflate.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Gzip/
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Gzip.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/RawDeflate.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Zip/
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Zip.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Zlib/
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Adapter/
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/AnyInflate.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Gunzip.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Inflate.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/RawInflate.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Unzip.pm
%exclude %{_mandir}/man3/IO::Compress::Deflate*
%exclude %{_mandir}/man3/IO::Compress::Gzip*
%exclude %{_mandir}/man3/IO::Compress::RawDeflate*
%exclude %{_mandir}/man3/IO::Compress::Zip*
%exclude %{_mandir}/man3/IO::Uncompress::AnyInflate*
%exclude %{_mandir}/man3/IO::Uncompress::Gunzip*
%exclude %{_mandir}/man3/IO::Uncompress::Inflate*
%exclude %{_mandir}/man3/IO::Uncompress::RawInflate*
%exclude %{_mandir}/man3/IO::Uncompress::Unzip*

# IO::Zlib
%exclude %{_prefix}/lib/perl5/%{perl_version}/IO/Zlib.pm
%exclude %{_mandir}/man3/IO::Zlib.*

# IPC::Cmd
%exclude %{_prefix}/lib/perl5/%{perl_version}/IPC/Cmd.pm
%exclude %{_mandir}/man3/IPC::Cmd.3*

# Locale::Maketext::Simple
%exclude %{_prefix}/lib/perl5/%{perl_version}/Locale/Maketext/Simple.pm
%exclude %{_mandir}/man3/Locale::Maketext::Simple.*

# Log::Message
%exclude %{_prefix}/lib/perl5/%{perl_version}/Log/Message.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/Log/Message/Config.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/Log/Message/Handlers.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/Log/Message/Item.pm
%exclude %{_mandir}/man3/Log::Message.3*
%exclude %{_mandir}/man3/Log::Message::Config.3*
%exclude %{_mandir}/man3/Log::Message::Handlers.3*
%exclude %{_mandir}/man3/Log::Message::Item.3*

# Log::Message::Simple
%exclude %{_prefix}/lib/perl5/%{perl_version}/Log/Message/Simple.pm
%exclude %{_mandir}/man3/Log::Message::Simple.3*

# Module::Build
%exclude %{_bindir}/config_data
%exclude %{_prefix}/lib/perl5/%{perl_version}/Module/Build/
%exclude %{_prefix}/lib/perl5/%{perl_version}/Module/Build.pm
%exclude %{_mandir}/man1/config_data.1*
%exclude %{_mandir}/man3/Module::Build*

# Module-CoreList
%exclude %{_bindir}/corelist
%exclude %{_prefix}/lib/perl5/%{perl_version}/Module/CoreList.pm
%exclude %{_mandir}/man1/corelist*
%exclude %{_mandir}/man3/Module::CoreList*

# Module-Load
%exclude %{_prefix}/lib/perl5/%{perl_version}/Module/Load.pm
%exclude %{_mandir}/man3/Module::Load.*

# Module-Load-Conditional
%exclude %{_prefix}/lib/perl5/%{perl_version}/Module/Load/
%exclude %{_mandir}/man3/Module::Load::Conditional*

# Module-Loaded
%exclude %{_prefix}/lib/perl5/%{perl_version}/Module/Loaded.pm
%exclude %{_mandir}/man3/Module::Loaded*

# Module-Pluggable
%exclude %{_prefix}/lib/perl5/%{perl_version}/Devel/InnerPackage.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/Module/Pluggable/
%exclude %{_prefix}/lib/perl5/%{perl_version}/Module/Pluggable.pm
%exclude %{_mandir}/man3/Devel::InnerPackage*
%exclude %{_mandir}/man3/Module::Pluggable*

# Object-Accessor
%exclude %{_prefix}/lib/perl5/%{perl_version}/Object/
%exclude %{_mandir}/man3/Object::Accessor*

# Package-Constants
%exclude %{_prefix}/lib/perl5/%{perl_version}/Package/
%exclude %{_mandir}/man3/Package::Constants*

# Params-Check
%exclude %{_prefix}/lib/perl5/%{perl_version}/Params/
%exclude %{_mandir}/man3/Params::Check*

# Pod-Escapes
%exclude %{_prefix}/lib/perl5/%{perl_version}/Pod/Escapes.pm
%exclude %{_mandir}/man3/Pod::Escapes.*

# Pod-Simple
%exclude %{_prefix}/lib/perl5/%{perl_version}/Pod/Simple/
%exclude %{_prefix}/lib/perl5/%{perl_version}/Pod/Simple.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/Pod/Simple.pod
%exclude %{_mandir}/man3/Pod::Simple*

# Term-UI
%exclude %{_prefix}/lib/perl5/%{perl_version}/Term/UI.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/Term/UI/
%exclude %{_mandir}/man3/Term::UI*

# Test::Harness
%exclude %{_bindir}/prove
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/Harness*
%exclude %{_mandir}/man1/prove.1*
%exclude %{_mandir}/man3/Test::Harness*

# Test::Simple
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/More*
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/Builder*
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/Simple*
%exclude %{_prefix}/lib/perl5/%{perl_version}/Test/Tutorial*
%exclude %{_mandir}/man3/Test::More*
%exclude %{_mandir}/man3/Test::Builder*
%exclude %{_mandir}/man3/Test::Simple*
%exclude %{_mandir}/man3/Test::Tutorial*

# Time::Piece
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/Time/Piece.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/Time/Seconds.pm
%exclude %{_libdir}/perl5/%{version}/%{perl_archname}/auto/Time/Piece/
%exclude %{_mandir}/man3/Time::Piece.3*
%exclude %{_mandir}/man3/Time::Seconds.3*

# version
%exclude %{_prefix}/lib/perl5/%{perl_version}/version.pm
%exclude %{_prefix}/lib/perl5/%{perl_version}/version.pod
%exclude %{_mandir}/man3/version.*

%files libs
%defattr(-,root,root)
%{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/libperl.so

%files devel
%defattr(-,root,root,-)
%{_bindir}/enc2xs
%{_mandir}/man1/enc2xs*
%{_bindir}/h2xs
%{_mandir}/man1/h2xs*
%{_bindir}/libnetcfg
%{_mandir}/man1/libnetcfg*
%{_bindir}/perlivp
%{_mandir}/man1/perlivp*
%{_libdir}/perl5/%{perl_version}/%{perl_archname}/CORE/*.h
%{_bindir}/xsubpp
%{_mandir}/man1/xsubpp*

%files suidperl
%defattr(-,root,root,-)
%{_bindir}/suidperl
%{_bindir}/sperl%{perl_version}

%files Archive-Extract
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Archive/
%{_mandir}/man3/Archive::Extract.3*

%files Archive-Tar
%defattr(-,root,root,-)
%{_bindir}/ptar
%{_bindir}/ptardiff
%{_prefix}/lib/perl5/%{perl_version}/Archive/Tar/ 
%{_prefix}/lib/perl5/%{perl_version}/Archive/Tar.pm
%{_mandir}/man1/ptar.1*
%{_mandir}/man1/ptardiff.1*
%{_mandir}/man3/Archive::Tar* 

%files Compress-Raw-Zlib
%defattr(-,root,root,-)
%dir %{_libdir}/perl5/%{version}/%{perl_archname}/Compress
%{_libdir}/perl5/%{version}/%{perl_archname}/Compress/Raw/
%dir %{_libdir}/perl5/%{version}/%{perl_archname}/auto/Compress/
%{_libdir}/perl5/%{version}/%{perl_archname}/auto/Compress/Raw/
%{_mandir}/man3/Compress::Raw::Zlib*

%files Compress-Zlib
%defattr(-,root,root,-)
%{_libdir}/perl5/%{version}/%{perl_archname}/Compress/Zlib.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/auto/Compress/Zlib/
%{_mandir}/man3/Compress::Zlib*

%files CPAN
%defattr(-,root,root,-)
%{_bindir}/cpan
%{_prefix}/lib/perl5/%{perl_version}/CPAN/
%{_prefix}/lib/perl5/%{perl_version}/CPAN.pm
%{_mandir}/man1/cpan.1*
%{_mandir}/man3/CPAN.*
%{_mandir}/man3/CPAN:*

%files CPANPLUS
%defattr(-,root,root,-)
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%{_prefix}/lib/perl5/%{perl_version}/CPANPLUS/
%{_prefix}/lib/perl5/%{perl_version}/CPANPLUS.pm
%{_mandir}/man1/cpan2dist.1*
%{_mandir}/man1/cpanp.1*
%{_mandir}/man3/CPANPLUS*

%files Digest-SHA
%defattr(-,root,root,-)
%{_bindir}/shasum
%dir %{_libdir}/perl5/%{version}/%{perl_archname}/Digest/
%{_libdir}/perl5/%{version}/%{perl_archname}/Digest/SHA.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/auto/Digest/SHA/
%{_mandir}/man1/shasum.1*
%{_mandir}/man3/Digest::SHA.3*

%files ExtUtils-CBuilder
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/CBuilder/
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/CBuilder.pm
%{_mandir}/man3/ExtUtils::CBuilder*

%files ExtUtils-Embed
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Embed.pm
%{_mandir}/man3/ExtUtils::Embed*

%files ExtUtils-MakeMaker
%defattr(-,root,root,-)
%{_bindir}/instmodsh
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Command/
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Install.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Installed.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Liblist/
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Liblist.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MakeMaker/
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MakeMaker.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MANIFEST.SKIP
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MM*.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/MY.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Manifest.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Mkbootstrap.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Mksymlists.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/Packlist.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/testlib.pm
%{_mandir}/man1/instmodsh.1*
%{_mandir}/man3/ExtUtils::Command::MM*
%{_mandir}/man3/ExtUtils::Install.3*
%{_mandir}/man3/ExtUtils::Installed.3*
%{_mandir}/man3/ExtUtils::Liblist.3*
%{_mandir}/man3/ExtUtils::MM*
%{_mandir}/man3/ExtUtils::MY.3*
%{_mandir}/man3/ExtUtils::MakeMaker*
%{_mandir}/man3/ExtUtils::Manifest.3*
%{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%{_mandir}/man3/ExtUtils::Mksymlists.3*
%{_mandir}/man3/ExtUtils::Packlist.3*
%{_mandir}/man3/ExtUtils::testlib.3*

%files ExtUtils-ParseXS
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/ParseXS.pm
%{_prefix}/lib/perl5/%{perl_version}/ExtUtils/xsubpp
%{_mandir}/man3/ExtUtils::ParseXS.3*

%files File-Fetch
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/File/Fetch.pm
%{_mandir}/man3/File::Fetch.3*

%files IO-Compress-Base
%defattr(-,root,root,-)
%{_libdir}/perl5/%{version}/%{perl_archname}/File/GlobMapper.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Base/
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Base.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/AnyUncompress.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Base.pm
%{_mandir}/man3/File::GlobMapper.*
%{_mandir}/man3/IO::Compress::Base.*
%{_mandir}/man3/IO::Uncompress::AnyUncompress.*
%{_mandir}/man3/IO::Uncompress::Base.*

%files IO-Compress-Zlib
%defattr(-,root,root,-)
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Adapter/
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Deflate.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Gzip/
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Gzip.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/RawDeflate.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Zip/
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Zip.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Compress/Zlib/
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Adapter/
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/AnyInflate.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Gunzip.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Inflate.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/RawInflate.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/IO/Uncompress/Unzip.pm
%{_mandir}/man3/IO::Compress::Deflate*
%{_mandir}/man3/IO::Compress::Gzip*
%{_mandir}/man3/IO::Compress::RawDeflate*
%{_mandir}/man3/IO::Compress::Zip*
%{_mandir}/man3/IO::Uncompress::AnyInflate*
%{_mandir}/man3/IO::Uncompress::Gunzip*
%{_mandir}/man3/IO::Uncompress::Inflate*
%{_mandir}/man3/IO::Uncompress::RawInflate*
%{_mandir}/man3/IO::Uncompress::Unzip*

%files IO-Zlib
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/IO/Zlib.pm
%{_mandir}/man3/IO::Zlib.*

%files IPC-Cmd
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/IPC/Cmd.pm
%{_mandir}/man3/IPC::Cmd.3*

%files Locale-Maketext-Simple
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Locale/Maketext/Simple.pm
%{_mandir}/man3/Locale::Maketext::Simple.*

%files Log-Message
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Log/Message.pm
%{_prefix}/lib/perl5/%{perl_version}/Log/Message/Config.pm
%{_prefix}/lib/perl5/%{perl_version}/Log/Message/Handlers.pm
%{_prefix}/lib/perl5/%{perl_version}/Log/Message/Item.pm
%{_mandir}/man3/Log::Message.3*
%{_mandir}/man3/Log::Message::Config.3*
%{_mandir}/man3/Log::Message::Handlers.3*
%{_mandir}/man3/Log::Message::Item.3*

%files Log-Message-Simple
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Log/Message/Simple.pm
%{_mandir}/man3/Log::Message::Simple.3*

%files Module-Build
%defattr(-,root,root,-)
%{_bindir}/config_data
%{_prefix}/lib/perl5/%{perl_version}/Module/Build/
%{_prefix}/lib/perl5/%{perl_version}/Module/Build.pm
%{_mandir}/man1/config_data.1*
%{_mandir}/man3/Module::Build*

%files Module-CoreList
%defattr(-,root,root,-)
%{_bindir}/corelist
%{_prefix}/lib/perl5/%{perl_version}/Module/CoreList.pm
%{_mandir}/man1/corelist*
%{_mandir}/man3/Module::CoreList*

%files Module-Load
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Module/Load.pm
%{_mandir}/man3/Module::Load.*

%files Module-Load-Conditional
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Module/Load/
%{_mandir}/man3/Module::Load::Conditional* 

%files Module-Loaded
%defattr(-,root,root,-)
%dir %{_prefix}/lib/perl5/%{perl_version}/Module/
%{_prefix}/lib/perl5/%{perl_version}/Module/Loaded.pm
%{_mandir}/man3/Module::Loaded*

%files Module-Pluggable
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Devel/InnerPackage.pm
%{_prefix}/lib/perl5/%{perl_version}/Module/Pluggable/
%{_prefix}/lib/perl5/%{perl_version}/Module/Pluggable.pm
%{_mandir}/man3/Devel::InnerPackage*
%{_mandir}/man3/Module::Pluggable*

%files Object-Accessor
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Object/
%{_mandir}/man3/Object::Accessor*

%files Package-Constants
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Package/
%{_mandir}/man3/Package::Constants*

%files Params-Check
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Params/
%{_mandir}/man3/Params::Check*

%files Pod-Escapes
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Pod/Escapes.pm
%{_mandir}/man3/Pod::Escapes.*

%files Pod-Simple
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Pod/Simple/ 
%{_prefix}/lib/perl5/%{perl_version}/Pod/Simple.pm
%{_prefix}/lib/perl5/%{perl_version}/Pod/Simple.pod
%{_mandir}/man3/Pod::Simple*

%files Term-UI
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Term/UI/
%{_prefix}/lib/perl5/%{perl_version}/Term/UI.pm
%{_mandir}/man3/Term::UI*

%files Test-Harness
%defattr(-,root,root,-)
%{_bindir}/prove
%{_prefix}/lib/perl5/%{perl_version}/Test/Harness*
%{_mandir}/man1/prove.1*
%{_mandir}/man3/Test::Harness*

%files Test-Simple
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/Test/More*
%{_prefix}/lib/perl5/%{perl_version}/Test/Builder*
%{_prefix}/lib/perl5/%{perl_version}/Test/Simple*
%{_prefix}/lib/perl5/%{perl_version}/Test/Tutorial*
%{_mandir}/man3/Test::More*
%{_mandir}/man3/Test::Builder*
%{_mandir}/man3/Test::Simple*
%{_mandir}/man3/Test::Tutorial*

%files Time-Piece
%defattr(-,root,root,-)
%{_libdir}/perl5/%{version}/%{perl_archname}/Time/Piece.pm 
%{_libdir}/perl5/%{version}/%{perl_archname}/Time/Seconds.pm
%{_libdir}/perl5/%{version}/%{perl_archname}/auto/Time/Piece/        
%{_mandir}/man3/Time::Piece.3*
%{_mandir}/man3/Time::Seconds.3*

%files version
%defattr(-,root,root,-)
%{_prefix}/lib/perl5/%{perl_version}/version.pm
%{_prefix}/lib/perl5/%{perl_version}/version.pod
%{_mandir}/man3/version.*

%files core
# Nothing. Nada. Zilch. Zarro. Uh uh. Nope. Sorry.

# Old changelog entries are preserved in CVS.
%changelog
* Mon Jul 21 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-31.fc9
- 455933 update to CGI-3.38
- fix fuzz problems (patch6)
- 217833 pos() function handle unicode characters correct

* Wed Jul  2 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-30.fc9
- 453646 use -DPERL_USE_SAFE_PUTENV. Without fail some modules f.e. readline.

* Fri Jun 27 2008 Stepan Kasal <skasal@redhat.com> 4:5.10.0-29.fc9
- add compatibility paths to @INC on 32bit archs (#452898), but do
  not explicitly mention the arch-specific subdir of it, perl adds it
  automatically

* Thu Jun 26 2008 Stepan Kasal <skasal@redhat.com> 4:5.10.0-28
- add compatibility paths to @INC on 32bit archs

* Tue Jun 24 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-27
- CVE-2008-2827 perl: insecure use of chmod in rmtree

* Thu Jun 12 2008 Stepan Kasal <skasal@redhat.com> 4:5.10.0-26
- make config parameter list consistent for 32bit and 64bit platforms,
  add config option -Dinc_version_list=none (#448735)
- use perl_archname consistently
- set siteprefix to prefix/local

* Wed Jun 11 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-25
- 447371 wrong access permission rt49003

* Mon May 26 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-24
- 448392 upstream fix for assertion

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-23
- sparc64 breaks with the rpath hack patch applied

* Mon May 19 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-22
- 447142 upgrade CGI to 3.37

* Sat May 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-21
- sparc64 fails two tests under mysterious circumstances. we need to get the
  rest of the tree moving, so we temporarily disable the tests on that arch.

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-20
- create the vendor_perl/%%{perl_version}/%%{perl_archname}/auto directory 
  in %%{_libdir} so we own it properly

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-19
- fix CPANPLUS-Dist-Build Provides/Obsoletes (bz 437615)
- bump version on Module-CoreList subpackage

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-18
- forgot to create the auto directory for multilib vendor_perl dirs

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-17
- own multilib vendor_perl directories
- mark Module::CoreList patch in patchlevel.h

* Tue Mar 18 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-16
- 437817: RFE: Upgrade Module::CoreList to 2.14

* Wed Mar 12 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-15
- xsubpp now lives in perl-devel instead of perl.

* Sat Mar  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-14
- back out Archive::Extract patch, causing odd test failure

* Sat Mar  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-13
- add missing lzma test file

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-12
- conditionalize multilib patch report in patchlevel.h
- Update Archive::Extract to 0.26
- Update Module::Load::Conditional to 0.24

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-11
- only do it once, and do it for all our patches

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-10
- note 32891 in patchlevel.h

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-9
- get rid of bad conflicts on perl-File-Temp

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-8
- use /usr/local for sitelib/sitearch dirs
- patch 32891 for significant performance improvement

* Fri Feb 22 2008 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-7
- Add perl-File-Temp provides/obsoletes/conflicts (#433836),
  reported by Bill McGonigle <bill@bfccomputing.com>
- escape the macros in Jan 30 entry

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4:5.10.0-6
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-5
- disable some futime tests in t/io/fs.t because they started failing on x86_64
  in the Fedora builders, and no one can figure out why. :/

* Wed Jan 30 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-4
- create %%{_prefix}/lib/perl5/vendor_perl/%%{perl_version}/auto and own it
  in base perl (resolves bugzilla 214580)

* Thu Jan 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-3
- Update Sys::Syslog to 0.24, to fix test failures

* Wed Jan 9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-2
- add some BR for tests

* Tue Jan 8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-1
- 5.10.0 final
- clear out all the unnecessary patches (down to 8 patches!)
- get rid of super perl debugging mode
- add new subpackages

* Thu Nov 29 2007 Robin Norwood <rnorwood@redhat.com> - 4:5.10.0_RC2-0.1
- first attempt at building 5.10.0


