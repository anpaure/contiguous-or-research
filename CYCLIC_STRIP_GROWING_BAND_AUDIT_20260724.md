# Audit of the quantitative cyclic-strip central-band cover

## Verdict

The cyclic-strip theorem is valid.  It gives an unconditional literal
contiguous-OR word of length `(1+o(1))W` covering a two-sided central band of
explicit depth

\[
J=(\log m)^{1/2-o(1)}.
\]

Here the displayed exponent uses a slowly growing choice
`g=(log m)^{o(1)}` (for example a power of `log log m`).  The theorem's
broader allowed range `g->infinity`, `g=o(sqrt(log m))` also includes choices
giving smaller powers of `log m`.

The argument is a cover argument, not a matching argument, and its use of a
growing-uniformity theorem is legitimate.  It does not prove coefficient
one because the depths between this polylogarithmic band and the
`Theta(sqrt(m log log m))` outer-reservoir threshold remain open.

## 1. Atom and parameter audit

For `n=2m+1`, choose disjoint cores

\[
|C|=m-\ell,\qquad |D|=m+1-\ell,
\]

leaving a `2ell`-set `R` with an undirected cyclic order.  The strip

\[
\{C\cup I(t,\ell+d):-J\le d\le J+1, t\in\mathbb Z_{2\ell}\}
\]

has exactly

\[
K=4\ell(J+1)
\]

distinct vertices.  The word of the `2ell` intervals of length `ell-J`,
followed by the first `2J+1` of them, has length

\[
P=2\ell+2J+1
\]

and exposes the whole strip by literal consecutive unions.  The assumptions
`2<=ell-J` and `J+1<ell` prevent degenerate interval families and full-cycle
wraparound.

The edge parametrization is injective.  The lowest-rank members recover
`C` by intersection and `C union R` by union.  After deleting `C`, two
coordinates are adjacent in the underlying cycle exactly when they occur
together in `ell-J-1` of the shortest intervals; a nonadjacent pair occurs
together at most `ell-J-2` times.

## 2. Degree and codegree audit

The number of strip edges is

\[
|E|=\frac{n!}{4\ell(m-\ell)!(m+1-\ell)!}.
\]

A rank-`m+d` vertex has degree

\[
D_d=\frac{(m+d)!(m+1-d)!}
 {2(m-\ell)!(m+1-\ell)!}.
\]

The minimum is `D_0=D_1`; the maximum is
`D_(-J)=D_(J+1)=D`, and

\[
D_{\min}/D=1-O(J^2/m).
\]

For distinct band vertices `X,Y`, the stabilizer of `X` has orbit size

\[
\binom{|X|}{|X\cap Y|}
\binom{n-|X|}{|Y\setminus X|}.
\]

Every nontrivial co-occurring pair has orbit size at least `m-J`: the only
orbit-one alternatives are `emptyset,X,X^c,[n]`, and `X^c` cannot share a
strip with `X` because every strip member contains the nonempty core `C`.
Since one strip has only `2ell` vertices in the rank of `Y`, the maximum
codegree `Gamma` satisfies

\[
\Gamma/D\le 2\ell/(m-J).
\]

Conversely, a middle vertex has exactly two immediate rank-`m+1`
supersets in every containing strip, giving

\[
\Gamma\ge 2D_{\min}/(m+1).
\]

The lower bound is used only to verify that the allowed degree defect in the
near-regular cover theorem dominates `D-D_min`.

## 3. Economical-cover theorem audit

The applicable result is the near-regular form of the
Alon--Bollobas--Kim--Vu economical-cover theorem.  For edge size `K>4`,
maximum degree `D`, maximum codegree `Gamma`, and minimum degree at least

\[
D-20(D^2\Gamma\log D)^{1/3},
\]

the condition

\[
e^{2K}\Gamma\log D=o(D)
\]

gives a cover of size

\[
\frac{|V|}{K}
\left(1+O\left[
(\Gamma\log(1+\Gamma)/D)^{1/(K-1)}
\right]\right).
\]

This is exactly the growing-`K` regime treated in the paper, not an
illicit fixed-uniformity substitution.  See
[Alon--Bollobas--Kim--Vu, *Economical covers with geometric applications*]
(https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf), especially the
conditions preceding Corollary 3.6 and Theorem 3.7.

With `L=log m`,

\[
J\sim \frac{\sqrt L}{g},\qquad
\ell\sim\frac{\sqrt L}{\sqrt g},\qquad
K\sim\frac{4L}{g^{3/2}},
\]

where `g->infinity` and `g=o(sqrt L)`.  Then

\[
\log D=(2+o(1))\ell L,
\]

and

\[
e^{2K}\Gamma\log D/D
 \le \exp\{-L+O(L/g^{3/2})+O(\log L)\}=o(1).
\]

The relative degree spread `O(J^2/m)` is smaller than
`(Gamma log D/D)^(1/3)`, and the cover error is

\[
\exp\{-(1/4+o(1))g^{3/2}\}.
\]

All hypotheses therefore hold uniformly.

## 4. Exact word accounting

The two ranks at each depth `0<=q<=J` have equal size
`N_q=C(2m+1,m-q)`, so

\[
|V|=2\sum_{q=0}^{J}N_q
 =2(J+1)W(1+O(J^2/m)).
\]

The economical cover uses at most

\[
\frac{W}{2\ell}
\left(1+O(J^2/m)+e^{-\Omega(g^{3/2})}\right)
\]

strips.  Replacing every strip by its length-`P` literal word yields

\[
W\left(1+\frac{2J+1}{2\ell}\right)
\left(1+O(J^2/m)+e^{-\Omega(g^{3/2})}\right).
\]

Since `J/ell~g^(-1/2)`, this is `(1+o(1))W`.  The even-dimensional
analogue follows from symmetric cores of size `m-ell`, interval offsets
`-J,...,J`, uniformity `2ell(2J+1)`, and word length `2ell+2J`.

## 5. Exact scope and optimization barrier

The convenient parameters in the submitted proof are not rate-optimal.
Write `L=log m`, take any

\[
J=o(\sqrt L),\qquad c=L/J^2\to\infty,
\]

and let `W_0` denote the principal Lambert-W function.  The balanced choice

\[
\ell=\frac{L}{4J\,W_0(c/4)}
\tag{5.1}
\]

(rounded to a nearby integer) equates the seam loss `J/ell` with the ABKV
cover error.  Indeed,

\[
\frac{J}{\ell}=\frac{4W_0(c/4)}c,
\qquad
\exp\!\left(-\frac{L}{4\ell J}\right)
=\exp(-W_0(c/4))
=\frac{4W_0(c/4)}c.
\]

Thus the same proof yields the sharper relative error

\[
O\!\left(
 \frac{W_0(c)}c
 \frac{J^2}{m}
\right)
=O\!\left(
 \frac{J^2}{\log m}\log\frac{\log m}{J^2}
\right).
\tag{5.2}
\]

For `J=sqrt(L)/g`, this is `O((log g)/g^2)`, improving the convenient
`O(g^(-1/2))` rate while leaving the depth range unchanged.

The proof needs both

\[
J/\ell=o(1)
\quad\text{and}\quad
\ell J=o(\log m)
\]

for vanishing word overhead and for the economical-cover codegree
condition.  Consequently this architecture intrinsically gives

\[
J=o(\sqrt{\log m}).
\]

It resolves a quantitative growing band that the fixed-parameter Kahn
argument did not specify, but it cannot by itself reach the outer-reservoir
threshold `Theta(sqrt(m log log m))`.  The remaining rank interval is

\[
(\log m)^{1/2-o(1)}
 < |r-m| <
 \Theta(\sqrt{m\log\log m}).
\]

Ordinary layering does not evade this ceiling at coefficient one.  Any
separately emitted strip layer covering a full near-central rank costs
`(1-o(1))W`; several such layers spend several baselines.  In a fractional
mixture of total cost `W+o(W)`, almost all capacity must already span the
largest requested depth because every rank at `q=o(sqrt m)` has
`N_q=(1-o(1))W`.  Beating the ceiling requires a different shared-baseline
geometry, such as a rotor, queue, or wreath construction.
