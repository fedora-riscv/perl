#!/bin/sh

/usr/lib/rpm/perl.req $* | grep -v NDBM | grep -v 'perl(v5.6.0)' | grep -v 'perl(Mac::' | grep -v 'perl(Tk'

