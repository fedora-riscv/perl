%define threading  1
%define largefiles 1
%define suidperl   1

%define perlver 5.8.0
%define perlrel 55
%define perlepoch 2
%define cpanver 1.61
%define dbfilever 1.804
%define cgiver 2.81

Provides: perl(:WITH_PERLIO)

%if %{threading}
%define thread_arch -thread-multi
Provides: perl(:WITH_ITHREADS)
Provides: perl(:WITH_THREADS)
%else
%define thread_arch %{nil}
Provides: perl(:WITHOUT_ITHREADS)
Provides: perl(:WITHOUT_THREADS)
%endif

%if %{largefiles}
Provides: perl(:WITH_LARGEFILES)
%else
Provides: perl(:WITHOUT_LARGEFILES)
%endif

Summary: The Perl programming language.
Name: perl
Version: %{perlver}
Release: %{perlrel}
Epoch: %{perlepoch}
License: Artistic
Group: Development/Languages

Vendor       : Red Hat, Inc.
Distribution : Red Hat Linux

# temporary til 64bit issues are resolved
#ExcludeArch: ia64
#ExcludeArch: alpha

Source0: ftp://ftp.perl.org/pub/perl/CPAN/src/perl-%{perlver}.tar.bz2
Source1: clean-manifest.pl
Source5: MANIFEST.CPAN
Source6: MANIFEST.CGI
Source7: MANIFEST.DB_File
Source9: MANIFEST.suidperl
Source10: system-owned-directories
Source11: filter-depends.sh
Source12: perl-5.8.0-libnet.cfg

# Patch1: perl-5.6.0-installman.patch
# Patch2: perl5.005_03-db1.patch
# Patch3: perl-5.6.0-nodb.patch
Patch4: perl-5.6.1-prereq.patch
Patch5: perl-5.6.0-root.patch
Patch6: perl-5.8.0-fhs.patch
Patch7: perl-5.6.0-buildroot.patch
Patch8: perl-5.8.0-errno.patch
Patch9: perl-5.7.3-syslog.patch

%define __find_requires %{SOURCE11}

Obsoletes: perl-NDBM_File
Obsoletes: perl-Digest-MD5
Obsoletes: perl-MIME-Base64
Obsoletes: perl-libnet

# for some reason, sys/types.h and sys/socket.h need to be included
# BEFORE perl.h when the types are used.  TODO: clean this.
# Patch10: perl-5.6.1-socketinc.patch

# ia64 doesn't include the kernel's define for ia64 page size.
# according to notting@redhat.com, the RH kernel is usually compiled
# with 16kb size, so...
# Patch12: perl-5.6.1-ia64pagesize.patch

# Configure doesn't listen well when we say no ndbm.  When it links in, it then conflicts with berkeley db.  oops.
Patch16: perl-5.8.0-nondbm.patch

# make sure we get the proper ldflags on libperl.so
Patch17: perl-5.8.0-sharedlinker.patch

# perl 5.8.0 likes to use man3ext for BOTH directories AND files.  not kosher.
Patch18: perl-5.8.0-manext.patch

# lynx is depracated, use links instead
Patch19: perl-5.8.0-links.patch
Patch20: perl-5.8.0-pager.patch

Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gawk, grep, tcsh

# By definition of 'do' (see 'man perlfunc') this package provides all
# versions of perl previous to it.
Provides: perl <= %{epoch}:%{version}

# These provides are needed by the perl pkg itself with auto-generated perl.req
Provides: perl(VMS::Filespec)
Provides: perl(VMS::Stdio)

# XXX needed by perl-libnet
Provides: perl(Mac::Files)

# XXX needed by perl-CGI
Provides: perl(FCGI)

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

# These modules appear to be missing or break assumptions made by the
# dependency analysis tools.  Typical problems include refering to
# CGI::Apache as Apache and having no package line in CPAN::Nox.pm. I
# hope that the perl people fix these to work with our dependency
# engine or give us better dependency tools.
#
# Provides: perl(Apache)
# Provides: perl(ExtUtils::MM_Mac)
# Provides: perl(ExtUtils::XSSymSet)
# Provides: perl(LWP::UserAgent)
# Provides: perl(URI::URL)

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

%package CPAN
Version: %{cpanver}
Release: %{perlrel}
Summary: CPAN module for Perl
Group: Development/Languages
Requires: perl >= %{perlepoch}:%{perlver}-%{perlrel}

%description CPAN
CPAN modules for Perl

%package CGI
Version: %{cgiver}
Release: %{perlrel}
Summary: CGI modules for Perl
Group: Development/Languages
Requires: perl >= %{perlepoch}:%{perlver}-%{perlrel}

%description CGI
CGI modules for Perl

%package DB_File
Version: %{dbfilever}
Release: %{perlrel}
Summary: DB_File module for Perl
Group: Development/Languages
Requires: perl >= %{perlepoch}:%{perlver}-%{perlrel}

%description DB_File
DB_File modules for Perl

%if %{suidperl}
%package suidperl
Version: %{perlver}
Release: %{perlrel}
Summary: suidperl, for use with setuid perl scripts
Group: Development/Languages
Requires: perl = %{perlepoch}:%{perlver}-%{perlrel}

%description suidperl
suidperl is a setuid binary copy of perl that allows for (hopefully)
more secure running of setuid perl scripts.
%endif

%prep
%setup -q
# %patch1 -p1 -b .instman
# Perl does not have a single entry point to define what db library to use
# so the patch below is mostly broken...
#%patch2 -p1
# %patch3 -p1 -b .nodb
#%patch4 -p1 -b .prereq
%patch5 -p1 -b .root
%patch6 -p1 -b .fhs
#%xpatch7 -p1 -b .buildroot
%patch8 -p1 -b .errno
%patch9 -p1 -b .syslog
#%%patch10 -p1 -b .incs

# %xpatch16 -p1 -b .nondbm

%patch17 -p1 -b .sharedlinker

%patch18 -p1 -b .manext
%patch19 -p1 -b .links
%patch20 -p1 -b .pager

find . -name \*.orig -exec rm -fv {} \;

%build

echo "RPM Build arch: %{_arch}"

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
sh Configure -des -Doptimize="$RPM_OPT_FLAGS" \
	-Dmyhostname=localhost \
	-Dperladmin=root@localhost \
	-Dcc='%{__cc}' \
        -Dcf_by='Red Hat, Inc.' \
	-Dinstallprefix=$RPM_BUILD_ROOT%{_prefix} \
	-Dprefix=%{_prefix} \
	-Darchname=%{_arch}-%{_os} \
%ifarch sparc
	-Ud_longdbl \
%endif
	-Dvendorprefix=%{_prefix} \
	-Dsiteprefix=%{_prefix} \
	-Duseshrplib \
%if %threading
	-Dusethreads \
        -Duseithreads \
%else
	-Uusethreads \
        -Uuseithreads \
%endif
%if %largefiles
        -Duselargefiles \
%else
        -Uuselargefiles \
%endif
	-Dd_dosuid \
	-Dd_semctl_semun \
	-Di_db \
	-Ui_ndbm \
	-Di_gdbm \
	-Di_shadow \
	-Di_syslog \
	-Dman3ext=3pm \
	-Duseperlio \
	-Dinstallusrbinperl \
	-Ubincompat5005 \
	-Uversiononly \
	-Dpager='/usr/bin/less -isr' \
#        -Dotherlibdirs=/usr/lib/perl5/5.6.0/%{_arch}-linux:/usr/lib/perl5/5.6.0:/usr/lib/perl5/vendor_perl/5.6.0/%{_arch}-linux:/usr/lib/perl5/vendor_perl/5.6.0

make -f Makefile

make -f Makefile test || /bin/true

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make install -f Makefile

mkdir -p ${RPM_BUILD_ROOT}/usr/lib/perl5/vendor_perl/%{perlver}/%{_arch}-%{_os}

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 utils/pl2pm ${RPM_BUILD_ROOT}%{_bindir}/pl2pm

# Generate *.ph files with a trick. Is this sick or what ?
make all -f - <<EOF
PKGS	= glibc-devel gdbm-devel gpm-devel libgr-devel libjpeg-devel \
	  libpng-devel libtiff-devel ncurses-devel popt \
	  zlib-devel binutils libelf e2fsprogs-devel pam pwdb \
	  rpm-devel
STDH	= \$(filter %{_includedir}/include/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' \$(PKGS)))
STDH	+=\$(wildcard %{_includedir}/linux/*.h) \
	  \$(wildcard %{_includedir}/bits/*.h)  \
	  \$(wildcard %{_includedir}/sys/*.h)  \
	  \$(wildcard %{_includedir}/scsi/*.h) 
# \$(wildcard %{_includedir}/asm/*.h)
GCCDIR	= \$(shell gcc --print-file-name include)
GCCH	= \$(filter \$(GCCDIR)/%%, \$(shell rpm -q --queryformat '[%%{FILEMODES} %%{FILENAMES}\n]' gcc | grep -v ^4 | awk '{print $NF}'))

PERLLIB = \$(RPM_BUILD_ROOT)%{_libdir}/perl5/%{perlver}
ARCHLIB = \$(RPM_BUILD_ROOT)%{_libdir}/perl5/%{perlver}/%{_arch}-%{_os}%{thread_arch}
PERL	= LD_LIBRARY_PATH=\$(ARCHLIB)/CORE PERL5LIB=\$(PERLLIB) \$(RPM_BUILD_ROOT)%{_bindir}/perl
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

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

# build MANIFEST.all

%define new_perl_lib $RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}
%define new_arch_lib $RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}/%{_arch}-%{_os}%{thread_arch}
%define new_perl_flags LD_LIBRARY_PATH=%{new_arch_lib}/CORE PERL5LIB=%{new_perl_lib}
%define new_perl %{new_perl_flags} $RPM_BUILD_ROOT/%{_bindir}/perl

find $RPM_BUILD_ROOT -type f -or -type l | grep -v Filter > MANIFEST.all
find $RPM_BUILD_ROOT -type d -printf "%%%%dir %p\n" | grep -v Filter >> MANIFEST.all

%{new_perl} -i -p -e "s|$RPM_BUILD_ROOT||g;" MANIFEST.all
cp MANIFEST.all /tmp

for i in  %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE10} 
do
  %{new_perl} %{SOURCE1} %{_arch} $i MANIFEST.all MANIFEST.all.tmp %{thread_arch}
  mv MANIFEST.all.tmp MANIFEST.all
done

%if %{suidperl}
  %{new_perl} %{SOURCE1} %{_arch} %{SOURCE9} MANIFEST.all MANIFEST.all.tmp %{thread_arch}
  mv MANIFEST.all.tmp MANIFEST.all
%endif

install -m 0644 %{SOURCE12} $RPM_BUILD_ROOT/usr/lib/perl5/5.8.0/Net/libnet.cfg

# fix the rest of the stuff
find $RPM_BUILD_ROOT%{_libdir}/perl* -name .packlist -o -name perllocal.pod | \
%{new_perl_flags} xargs $RPM_BUILD_ROOT/%{_bindir}/perl -I lib/ -i -p -e "s|$RPM_BUILD_ROOT||g;" MANIFEST.all

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files -f MANIFEST.all
%defattr(-,root,root)

%files -f %{SOURCE5} CPAN
%defattr(-,root,root)

%files -f %{SOURCE6} CGI
%defattr(-,root,root)

%files -f %{SOURCE7} DB_File
%defattr(-,root,root)

%if %{suidperl}
%files -f %{SOURCE9} suidperl
%defattr(-,root,root)
%endif

%changelog
* Sun Sep  1 2002 Chip Turner <cturner@redhat.com>
- fix pager issues; default to /usr/bin/less -isr
- more work on pager bug (72125)

* Thu Aug 29 2002 Chip Turner <cturner@redhat.com>
- add a few new directories to h2ph to produce better .ph files

* Thu Aug 15 2002 Chip Turner <cturner@redhat.com>
- change from lynx to links in CPAN.pm

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build
- remove Filter packages and use CPAN ones

* Fri Jul 19 2002 Chip Turner <cturner@redhat.com>
- move to final perl 5.8.0, huzzah!

* Tue Jul 16 2002 Chip Turner <cturner@redhat.com>
- update CPAN, CGI, and DB_File versions; obsolete perl-libnet
- libnet.cfg supplied, default to passive ftp in all cases

* Tue Jun 18 2002 Chip Turner <cturner@redhat.com>
- add patch to ensire libperl.so is linked properly

* Mon May 20 2002 Nalin Dahyabhai <nalin@redhat.com>
- always build with -fPIC

* Thu May  9 2002 Jeff Johnson <jbj@redhat.com>
- rebuild in rawhide

* Sun Mar 31 2002 Chip Turner <cturner@redhat.com>
- split suidperl back out (bug #62215)

* Tue Mar 26 2002 Chip Turner <cturner@redhat.com>
- restructuring of some directories, alteration of @INC

* Thu Dec 20 2001 Chip Turner <cturner@redhat.com>
- remove ndbm completely

* Sun Dec 16 2001 Chip Turner <cturner@redhat.com>
- make rpmlint happy, split out NDBM_File, clean up other spots
- stopped doing grep -v etc in favor of custom script

* Wed Dec 12 2001 Chip Turner <cturner@redhat.com>
- cleaning up of ia64 issues, as well as compatibility with gcc 3.1
  and glibc 2.2.4

* Mon Sep 24 2001 Chip Turner <cturner@redhat.com>
- changing building of extra modules out of the core perl rpm

* Mon Sep 17 2001 Chip Turner <cturner@redhat.com>
- upgrade to 5.6.1, added old INC dirs to maintain compat

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
