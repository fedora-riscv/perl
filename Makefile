# Makefile for source rpm: perl
# $Id$
NAME := perl
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
