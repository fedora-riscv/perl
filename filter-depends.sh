#!/bin/sh

/usr/lib/rpm/find-requires $* | grep -v NDBM | grep -v 'perl(v5.6.0)' | grep -v 'perl(Mac::'

