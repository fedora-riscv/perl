Summary: The Perl programming language.
Name: perl
%define perlver 5.6.0
Version: %{perlver}
Release: 17
License: GPL or Artistic
Group: Development/Languages
Source0: ftp://ftp.perl.org/pub/perl/CPAN/src/perl-%{perlver}.tar.bz2
Source2: find-provides
Source3: find-requires
Source4: find-requires.64
Patch0: perl5.005_02-buildsys.patch
Patch1: perl-5.6.0-installman.patch
Patch2: perl5.005_03-db1.patch
Patch3: perl-5.6.0-nodb.patch
Patch4: perl-5.6.0-prereq.patch
Patch5: perl-5.6.0-root.patch
Patch6: perl-5.6.0-fhs.patch
Patch7: perl-5.6.0-buildroot.patch
Patch8: perl-5.6.0-errno.patch
Patch9: perl-5.6.0-syslog.patch
Buildroot: %{_tmppath}/%{name}-root
BuildPreReq: gawk, grep, tcsh
BuildRequires: gdbm-devel, db1-devel
Requires: gdbm, db1
Epoch: 1

# ----- Perl module provides.
Provides: perl(autouse)  
Provides: perl(blib)  
Provides: perl(diagnostics)  
Provides: perl(integer)  
Provides: perl(less)  
Provides: perl(lib)  
Provides: perl(locale)  
Provides: perl(ops)  
Provides: perl(overload)  
Provides: perl(re)  
Provides: perl(sigtrap)  
Provides: perl(strict)  
Provides: perl(subs)  
Provides: perl(vmsish)  
Provides: perl(vars)  
Provides: perl(AnyDBM_File)  
Provides: perl(AutoLoader) = 5.57
Provides: perl(AutoSplit) = 1.0305
Provides: perl(Benchmark) = 1.00
Provides: perl(Carp)  
Provides: perl(CGI)  
Provides: perl(CGI::Carp)  
Provides: perl(CGI::Cookie)  
Provides: perl(CGI::Fast)  
Provides: perl(CGI::Pretty)  
Provides: perl(CGI::Push)  
Provides: perl(Class::Struct) = 0.58
Provides: perl(Class::Struct::Tie_ISA)  
Provides: perl(CPAN)  
Provides: perl(CPAN::Author)  
Provides: perl(CPAN::Bundle)  
Provides: perl(CPAN::CacheMgr)  
Provides: perl(CPAN::Complete)  
Provides: perl(CPAN::Config)  
Provides: perl(CPAN::Debug)  
Provides: perl(CPAN::Distribution)  
Provides: perl(CPAN::Eval)  
Provides: perl(CPAN::FirstTime) = 1.38
Provides: perl(CPAN::FTP)  
Provides: perl(CPAN::FTP::netrc)  
Provides: perl(CPAN::Index)  
Provides: perl(CPAN::InfoObj)  
Provides: perl(CPAN::Mirrored::By)  
Provides: perl(CPAN::Module)  
Provides: perl(CPAN::Nox) = 1.00
Provides: perl(CPAN::Queue)  
Provides: perl(CPAN::Shell)  
Provides: perl(CPAN::Tarzip)  
Provides: perl(Cwd) = 2.02
Provides: perl(DB)  
Provides: perl(Devel::SelfStubber) = 1.01
Provides: perl(DirHandle)  
Provides: perl(Dumpvalue)  
Provides: perl(DynaLoader)  
Provides: perl(English)  
Provides: perl(Env)  
Provides: perl(Env::Array)  
Provides: perl(Env::Array::VMS)  
Provides: perl(Exporter)  
Provides: perl(ExtUtils::Command) = 1.01
Provides: perl(ExtUtils::Embed) = 1.2505
Provides: perl(ExtUtils::Install) = 1.28
Provides: perl(ExtUtils::Installed)  
Provides: perl(ExtUtils::Install::Warn)  
Provides: perl(ExtUtils::Liblist)  
Provides: perl(ExtUtils::MakeMaker)  
Provides: perl(ExtUtils::Manifest) = 1.33
Provides: perl(ExtUtils::Miniperl)  
Provides: perl(ExtUtils::Mkbootstrap) = 1.14
Provides: perl(ExtUtils::Mksymlists) = 1.17
Provides: perl(ExtUtils::MM_Cygwin)  
Provides: perl(ExtUtils::MM_OS2)  
Provides: perl(ExtUtils::MM_Unix)  
Provides: perl(ExtUtils::MM_VMS)  
Provides: perl(ExtUtils::MM_Win32)  
Provides: perl(ExtUtils::MM_Win95)  
Provides: perl(ExtUtils::Packlist)  
Provides: perl(ExtUtils::testlib) = 1.11
Provides: perl(Fatal) = 1.02
Provides: perl(Fh)  
Provides: perl(File::Basename) = 2.6
Provides: perl(FileCache)  
Provides: perl(File::CheckTree)  
Provides: perl(File::Compare) = 1.1002
Provides: perl(File::Copy) = 2.03
Provides: perl(File::DosGlob)  
Provides: perl(File::Find)  
Provides: perl(FileHandle) = 2.00
Provides: perl(File::Path)  
Provides: perl(File::Spec) = 0.8
Provides: perl(File::Spec::Functions)  
Provides: perl(File::Spec::Mac)  
Provides: perl(File::Spec::OS2)  
Provides: perl(File::Spec::Unix)  
Provides: perl(File::Spec::VMS)  
Provides: perl(File::Spec::Win32)  
Provides: perl(File::stat)  
Provides: perl(FindBin) = 1.42
Provides: perl(Getopt::Long) = 2.23
Provides: perl(Getopt::Std) = 1.02
Provides: perl(I18N::Collate)  
Provides: perl(IO::Socket::INET) = 1.25
Provides: perl(IO::Socket::UNIX) = 1.20
Provides: perl(IPC::Open2) = 1.01
Provides: perl(IPC::Open3) = 1.0103
Provides: perl(main)  
Provides: perl(Math::BigFloat)  
Provides: perl(Math::BigInt)  
Provides: perl(Math::Complex) = 1.26
Provides: perl(Math::Trig) = 1.00
Provides: perl(MM)  
Provides: perl(MultipartBuffer)  
Provides: perl(MY)  
Provides: perl(Net::hostent)  
Provides: perl(Net::netent)  
Provides: perl(Net::Ping) = 2.02
Provides: perl(Net::protoent)  
Provides: perl(Net::servent)  
Provides: perl(Pod::Checker) = 1.098
Provides: perl(TempFile)  
Provides: perl(xsubpp::counter)  

# ----- Perl module dependencies.
#
# Provide perl-specific find-{provides,requires} until rpm-3.0.4 catches up.
%define	__find_provides	%{SOURCE2}
%ifnarch ia64 sparc64 s390x
%define	__find_requires	%{SOURCE3}
%else
%define	__find_requires	%{SOURCE4}
%endif
# By definition of 'do' (see 'man perlfunc') this package provides all
# versions of perl previous to it.
Provides: perl <= %{version}

# These modules appear to be missing or break assumptions made by the
# dependency analysis tools.  Typical problems include refering to
# CGI::Apache as Apache and having no package line in CPAN::Nox.pm. I
# hope that the perl people fix these to work with our dependency
# engine or give us better dependency tools.
#
# Provides: perl(Apache)
# Provides: perl(ExtUtils::MM_Mac)
# Provides: perl(ExtUtils::XSSymSet)
# Provides: perl(FCGI)
# Provides: perl(LWP::UserAgent)
# Provides: perl(Mac::Files)
# Provides: perl(URI::URL)
# Provides: perl(VMS::Filespec)

%description
Perl is a high-level programming language with roots in C, sed, awk,
and shell scripting. Perl is good at handling processes and files,
and is especially good at handling text. Perl's hallmarks are
practicality and efficiency. While it is used to do a lot of
different things, Perl's most common applications are system
administration utilities and Web programming. A large portion of the
CGI scripts on the Web are written in Perl. You need the perl package
installed on your system so that your system can handle Perl scripts.

Install this package if you want to program in Perl or enable your
system to handle Perl scripts.

%prep
%setup -q
mkdir modules
%patch0 -p1 -b .buildsys
%patch1 -p1 -b .instman
# Perl does not have a single entry point to define what db library to use
# so the patch below is mostly broken...
#%patch2 -p1
%patch3 -p1 -b .nodb
%patch4 -p1 -b .prereq
%patch5 -p1 -b .root
%patch6 -p1 -b .fhs
%patch7 -p1 -b .buildroot
%patch8 -p1 -b .errno
%patch9 -p1 -b .syslog

find . -name \*.orig -exec rm -fv {} \;

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
sh Configure -des -Doptimize="$RPM_OPT_FLAGS" \
	-Dcc='%{__cc}' \
	-Dcccdlflags='-fPIC' \
	-Dinstallprefix=$RPM_BUILD_ROOT%{_prefix} \
	-Dprefix=%{_prefix} \
	-Darchname=%{_arch}-%{_os} \
%ifarch sparc
	-Ud_longdbl \
%endif
	-Dd_dosuid \
	-Dd_semctl_semun \
	-Di_db \
	-Di_ndbm \
	-Di_gdbm \
	-Di_shadow \
	-Di_syslog \
	-Dman3ext=3pm \
	-Uuselargefiles
make -f Makefile

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make install -f Makefile
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 utils/pl2pm ${RPM_BUILD_ROOT}%{_bindir}/pl2pm

# Generate *.ph files with a trick. Is this sick or what ?
make all -f - <<EOF
PKGS	= glibc-devel gdbm-devel gpm-devel libgr-devel libjpeg-devel \
	  libpng-devel libtiff-devel ncurses-devel popt \
	  zlib-devel binutils libelf e2fsprogs-devel pam pwdb \
	  rpm-devel
STDH	= \$(filter %{_includedir}/include/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' \$(PKGS)))
STDH	+=\$(wildcard %{_includedir}/linux/*.h) \$(wildcard %{_includedir}/asm/*.h) \
	  \$(wildcard %{_includedir}/scsi/*.h)
GCCDIR	= \$(shell gcc --print-file-name include)
GCCH	= \$(filter \$(GCCDIR)/%%, \$(shell rpm -q --queryformat '[%%{FILEMODES} %%{FILENAMES}\n]' gcc | grep -v ^4 | awk '{print $NF}'))

PERLLIB = \$(RPM_BUILD_ROOT)%{_libdir}/perl5/%{perlver}
PERL	= PERL5LIB=\$(PERLLIB) \$(RPM_BUILD_ROOT)%{_bindir}/perl
PHDIR	= \$(PERLLIB)/\${RPM_ARCH}-linux*
H2PH	= \$(PERL) \$(RPM_BUILD_ROOT)%{_bindir}/h2ph -d \$(PHDIR)/

all: std-headers gcc-headers fix-config

std-headers: \$(STDH)
	cd %{_includedir} && \$(H2PH) \$(STDH:%{_includedir}/%%=%%)

gcc-headers: \$(GCCH)
	cd \$(GCCDIR) && \$(H2PH) \$(GCCH:\$(GCCDIR)/%%=%%) || true

fix-config: \$(PHDIR)/Config.pm
	\$(PERL) -i -p -e "s|\$(RPM_BUILD_ROOT)||g;" \$<

EOF

# fix the rest of the stuff
find $RPM_BUILD_ROOT%{_libdir}/perl* -name .packlist -o -name perllocal.pod | \
xargs ./perl -i -p -e "s|$RPM_BUILD_ROOT||g;" $packlist

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Artistic AUTHORS Changes* Copying README
%{_bindir}/*
%{_libdir}/*
%{_mandir}/*/*

%changelog
* Thu Aug  9 2001 Crutcher Dunnavant <crutcher@redhat.com> 5.6.0-17
- add deps on gdbm and db1, build deps on gdbm-devel and db1-devel; #49553

* Mon Jun 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- unbundle the Digest-MD5 module (noted by Charlie Brady) -- perl
  dependency checking RPM will do most of the heavy lifting
- mark License as GPL or Artistic

* Thu Jun 14 2001 Nalin Dahyabhai <nalin@redhat.com>
- use /usr/lib/rpm/findprovides.perl to complete the list of perl provides
- change Copyright: GPL to License: GPL
- include some of the text documentation files

* Wed Jun 13 2001 Crutcher Dunnavant <crutcher@redhat.com>
- added provides to close bug #43081

* Fri Jun 08 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add s390x change to specfile from Oliver Paukstadt
  <oliver.paukstadt@millenux.com>

* Fri Mar 23 2001 Preston Brown <pbrown@redhat.com>
- bzip2 source, save some space.

* Thu Dec  7 2000 Crutcher Dunnavant <crutcher@redhat.com>
- initial rebuild for 7.1

* Tue Sep 12 2000 Bill Nottingham <notting@redhat.com>
- fix dependencies on ia64/sparc64

* Mon Aug  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- replace the deprecated MD5 with Digest::MD5 (has to be here for cleanfeed)
- obsolete: perl-Digest-MD5
- use syslog instead of mail to report possible attempts to break into suidperl
- force syslog on at build-time

* Mon Jul 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- add Owen's fix for #14779/#14863
- specify cc=%{__cc}; continue to let cpp sort itself out
- switch shadow support on (#8646)
- release 7

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- strip buildroot from perl pods (#14040)
- release 6

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild (release 5)

* Wed Jun 21 2000 Preston Brown <pbrown@redhat.com>
- don't require tcsh to install, only to build
- release 4

* Mon Jun 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild against new db3 package
- release 3

* Sat Jun 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- disable 64-bit file support
- change name of package that Perl expects gcc to be in from "egcs" to "gcc"
- move man pages to /usr/share via hints/linux.sh and MM_Unix.pm
- fix problems prefixifying with empty prefixes
- disable long doubles on sparc (they're the same as doubles anyway)
- add an Epoch to make sure we can upgrade from perl-5.00503
- release 2

* Thu Mar 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.6.0

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Fri Jan 14 2000 Jeff Johnson <jbj@redhat.com>
- add provides for perl modules (from kestes@staff.mail.com).

* Mon Oct 04 1999 Cristian Gafton <gafton@redhat.com>
- fix the %install so that the MD5 module gets actually installed correctly

* Mon Aug 30 1999 Cristian Gafton <gafton@redhat.com>
- make sure the package builds even when we don't have perl installed on the
  system

* Fri Aug 06 1999 Cristian Gafton <gafton@redhat.com>
- merged with perl-MD5
- get rid of the annoying $RPM_BUILD_ROOT paths in the installed tree

* Mon Jul 26 1999 Cristian Gafton <gafton@redhat.com>
- do not link anymore against the system db library (and make each module
  link against it separately, so that we can have Berkeley db1 and db2 mixed
  up)

* Wed Jun 16 1999 Cristian Gafton <gafton@redhat.com>
- use wildcards for files in /usr/bin and /usr/man

* Tue Apr 06 1999 Cristian Gafton <gafton@redhat.com>
- version 5.00503
- make the default man3 install dir be release independent
- try to link against db1 to preserve compatibility with older databases;
  abandoned idea because perl is too broken to allow such an easy change
  (hardcoded names *everywhere* !!!)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- guilty of the inlined Makefile in the spec file
- adapted for the arm build

* Wed Sep 09 1998 Preston Brown <pbrown@redhat.com>
- added newer CGI.pm to the build
- changed the version naming scheme around to work with RPM

* Sun Jul 19 1998 Jeff Johnson <jbj@redhat.com>
- attempt to generate *.ph files reproducibly

* Mon Jun 15 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.004_04-m4 (pre-5.005 maintenance release)

* Tue Jun 12 1998 Christopher McCrory <chrismcc@netus.com
- need stdarg.h from gcc shadow to fix "use Sys::Syslog" (problem #635)

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to correct the .ph constructs unless defined (foo) to read
  unless(defined(foo))

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- fixed strftime problem

* Sun Mar 08 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to fix a security race
- do not use setres[ug]id - those are not implemented on 2.0.3x kernels

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 5.004_04 - 5.004_01 had some nasty memory leaks.
- fixed the spec file to be version-independent

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- Config.pm wasn't right do to the builtrooting

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- fixed arch-specfic part of spec file

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to perl 5.004_01
- users a build root

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Erik Troan <ewt@redhat.com>
- Incorporated security patch from Chip Salzenberg <salzench@nielsenmedia.com>

* Fri Feb 07 1997 Erik Troan <ewt@redhat.com>
- Use -Darchname=i386-linux 
- Require csh (for glob)
- Use RPM_ARCH during configuration and installation for arch independence
