%global tl_name simplewick
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	Simple Wick contractions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simplewick
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple means of drawing Wick contractions above
and below expressions.

