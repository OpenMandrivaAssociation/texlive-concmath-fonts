%global tl_name concmath-fonts
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Concrete mathematics fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/concmath
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath-fonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath-fonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are derived from the computer modern mathematics fonts and
from Knuth's Concrete Roman fonts; they are distributed as Metafont
source. LaTeX support is offered by the concmath package.

