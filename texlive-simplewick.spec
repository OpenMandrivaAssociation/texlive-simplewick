# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/simplewick
# catalog-date 2008-08-23 15:48:35 +0200
# catalog-license gpl
# catalog-version 1.2a
Name:		texlive-simplewick
Version:	1.2a
Release:	6
Summary:	Simple Wick contractions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simplewick
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplewick.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-2
+ Revision: 756028
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-1
+ Revision: 719538
- texlive-simplewick
- texlive-simplewick
- texlive-simplewick
- texlive-simplewick

