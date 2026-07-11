%global tl_name tikz-feynman
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	Feynman diagrams with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-feynman
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-feynman.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-feynman.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(iftex)
Requires:	texlive(pgfopts)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX package allowing Feynman diagrams to be easily generated
within LaTeX with minimal user instructions and without the need of
external programs. It builds upon the TikZ package and leverages the
graph placement algorithms from TikZ in order to automate the placement
of many vertices. tikz-feynman allows fine-tuned placement of vertices
so that even complex diagrams can still be generated with ease.

