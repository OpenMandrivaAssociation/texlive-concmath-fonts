# revision 17218
# category Package
# catalog-ctan /fonts/concmath
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-concmath-fonts
Version:	20060827
Release:	1
Summary:	Concrete mathematics fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/concmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath-fonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath-fonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The fonts are derived from the computer modern mathematics
fonts and from Knuth's Concrete Roman fonts. LaTeX support is
offered by the concmath package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccam10.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccam5.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccam6.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccam7.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccam8.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccam9.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccbm10.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccbm5.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccbm6.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccbm7.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccbm8.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccbm9.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccex10.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccex7.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccex8.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccex9.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccmi10.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccmi5.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccmi6.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccmi7.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccmi8.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccmi9.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccsy10.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccsy5.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccsy6.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccsy7.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccsy8.mf
%{_texmfdistdir}/fonts/source/public/concmath-fonts/xccsy9.mf
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccam10.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccam5.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccam6.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccam7.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccam8.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccam9.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccbm10.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccbm5.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccbm6.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccbm7.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccbm8.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccbm9.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccex10.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccex7.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccex8.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccex9.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccsy6.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/concmath-fonts/xccsy9.tfm
%doc %{_texmfdistdir}/doc/fonts/concmath-fonts/CATALOGUE
%doc %{_texmfdistdir}/doc/fonts/concmath-fonts/Makefile
%doc %{_texmfdistdir}/doc/fonts/concmath-fonts/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
