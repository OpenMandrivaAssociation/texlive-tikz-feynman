Name:		texlive-tikz-feynman
Version:	56615
Release:	1
Summary:	Feynman diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-feynman
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-feynman.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-feynman.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package allowing Feynman diagrams to be easily
generated within LaTeX with minimal user instructions and
without the need of external programs. It builds upon the TikZ
package and leverages the graph placement algorithms from TikZ
in order to automate the placement of many vertices.
tikz-feynman allows fine-tuned placement of vertices so that
even complex diagrams can still be generated with ease.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-feynman
%doc %{_texmfdistdir}/doc/latex/tikz-feynman

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
