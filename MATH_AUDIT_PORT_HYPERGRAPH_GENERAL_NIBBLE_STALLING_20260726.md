# General nibble theorems stall on the port-sparsified annulus hypergraph

Date: 2026-07-26

## Verdict

The integrally port-sparsified fine-strip hypergraph is a clean exact gate,
but even the recent higher-codegree Rödl-nibble theorem does not prove its
near-perfect matching statement.  The obstruction is the full-edge
codegree, equivalently the ratio between logarithmic degree and edge rank.

Use the intended parameters

\[
 H=\lceil\sqrt{m\log m}\rceil,
 \qquad h=m^{3/4+o(1)}.
\]

Let \(K\) be the rank of one port edge and \(D=D_1\) its nonmiddle
vertex degree.  The exact port theorem gives

\[
 K=\Theta(h\sqrt m),
\]

while

\[
 D={ (m+1)!(m-1)!\over2(m-h)!^2},
 \qquad
 \log D=(2+o(1))h\log m.
\]

Consequently

\[
 \boxed{
 {\log D\over K}=\Theta\!\left({\log m\over\sqrt m}\right)=o(1),
 \qquad D^{1/(K-1)}=1+o(1).}
\tag{1}
\]

## Higher-codegree theorem audit

Theorem 1.4 of Gould--Kelly, *Advancing the Rödl Nibble: New bounds on
matchings and the list chromatic index of hypergraphs* (arXiv:2511.11375),
allows a matching parameter

\[
 B_0\le
 \min_{4\le j\le K}
 \left({D\over D_j}\right)^{1/(j-1)}.
\]

Our port hypergraph is simple, so its full-edge codegree is \(D_K=1\).
The \(j=K\) constraint alone therefore gives

\[
 B_0\le D^{1/(K-1)}=1+o(1).
\]

The theorem's leftover bound is of order

\[
 |V|B_0^{-1+o(1)}\operatorname {polylog}D,
\]

which is not \(o(|V|)\) when \(B_0=1+o(1)\).  Better estimates for pair
or intermediate codegrees cannot remove the full-edge bottleneck inside
that theorem.

The older Pippenger--Frankl--Rödl and Vu bounds are also nonuniform in the
growing rank and halt no later.  Their fixed-rank forms remain valid for
the separate fixed-parameter theorem, where \(H,h\) are held constant
before \(m\to\infty\).

## Consequence

The annulus matching criterion cannot be closed by citing a general
high-uniformity nibble, even one using the entire codegree sequence.  A
successful theorem must exploit the special decomposition of a port edge
into \(2h\) nested Boolean flags, rather than regard it as one arbitrary
\(K\)-set.

This recovers the same quantitative stalling ratio found in the earlier
hard-resource audit:

\[
 {\text{entropy per strip}\over\text{hard ports per strip}}
 \asymp {\log m\over\sqrt m}\to0.
\]
