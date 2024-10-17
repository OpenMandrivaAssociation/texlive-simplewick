Name:		texlive-simplewick
Version:	15878
Release:	2
Summary:	Simple Wick contractions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simplewick
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple means of drawing Wick
contractions above and below expressions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/simplewick/simplewick.sty
%doc %{_texmfdistdir}/doc/latex/simplewick/README
%doc %{_texmfdistdir}/doc/latex/simplewick/simplewick.pdf
#- source
%doc %{_texmfdistdir}/source/latex/simplewick/simplewick.dtx
%doc %{_texmfdistdir}/source/latex/simplewick/simplewick.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
