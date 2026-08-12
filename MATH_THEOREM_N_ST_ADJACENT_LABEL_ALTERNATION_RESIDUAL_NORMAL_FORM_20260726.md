# PBBS predecessor passages: strict adjacent-label alternation and the residual-phase normal form

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Theorem and boundary

Let \(\mathcal O\) be one augmented rank-\(d\) reduced PBBS orbit, put

\[
                         p=2d+1,\qquad L=|\mathcal O|,
\]

and let \(\kappa_s\in\mathbb Z_p\) be the persistent equality-particle
identity selected at time \(s\).  Coordinate homomesy gives exactly
\(q=L/p\) visits to each identity.

Fix adjacent identities \(b,a=b+1\).  Write \(t_{b,i}\) for the cyclic
\(b\)-visits and

\[
                         g_{b,i}=t_{b,i+1}-t_{b,i}.
\]

Then the \(a\)- and \(b\)-visits strictly alternate.  In particular there
is a unique \(a\)-visit

\[
                         t_{b,i-1}<s_{b,i}<t_{b,i}.
\]

Define its residual phase by

\[
                         r_{b,i}=t_{b,i}-s_{b,i}.
\]

The exact normal form is

\[
 \boxed{
  1\le r_{b,i}\le g_{b,i-1}-1,
  \qquad
  B_2(s_{b,i})-s_{b,i}=r_{b,i}+g_{b,i}.}          \tag{0.1}
\]

Hence the complete predecessor-active count through horizon \(G\) is

\[
 \boxed{
  A_G(\mathcal O)=
  \sum_{b\in\mathbb Z_p}\sum_{i=1}^{q}
  \mathbf1_{\{r_{b,i}+g_{b,i}\le G\}}.}          \tag{0.2}
\]

If

\[
                         h_{b,i}=s_{b,i+1}-s_{b,i}
\]

is the corresponding ordered successor-gap sequence, then

\[
 \boxed{
                         h_{b,i}=g_{b,i}+r_{b,i}-r_{b,i+1}.}    \tag{0.3}
\]

Thus even the complete ordered marginal renewal cycles of \(a\) and
\(b\) determine only the coboundary of \(r\), not its absolute integral
phase.  The active indicator (0.2) depends on that phase.

This is sharp under strict alternation.  There are balanced cyclic words
having the same ordered cyclic gap sequences for \(a\) and \(b\), with
strict \(a,b\) alternation and the no-overtaking order at every \(a\)-visit,
but with active counts zero and one, respectively, on the even
\(\tau\)-phase subdeck.  The example is a renewal-data obstruction, not a
claim that the completed words satisfy every simultaneous PBBS constraint
for the other adjacent label pairs.

Consequently the exact Kac identities and all one-particle killed-operator
Jordan data cannot prove a critical lower or upper packing bound.  A
decision requires a PBBS-specific law for the residuals \(r_{b,i}\), and
then their common alignment across labels and even phases.

## 1. Strict alternation

The audited no-overtaking inequality says that at every phase selecting
\(a\), the next selection of \(a\) occurs before the second future
selection of its immediate predecessor \(b\).  Therefore an open interval
between two consecutive \(a\)-visits contains at most one \(b\)-visit.

There are exactly \(q\) such cyclic intervals and, by componentwise
homomesy, exactly \(q\) visits of \(b\).  Every interval must therefore
contain exactly one \(b\)-visit.  It follows equivalently that every open
interval between consecutive \(b\)-visits contains exactly one \(a\)-visit.
This proves strict cyclic alternation and the existence and uniqueness of
\(s_{b,i}\).

## 2. Residual formula and coboundary

The unique visit \(s_{b,i}\) lies strictly inside the preceding
\(b\)-block, so

\[
 1\le t_{b,i}-s_{b,i}
 \le t_{b,i}-t_{b,i-1}-1=g_{b,i-1}-1.            \tag{2.1}
\]

The first two future \(b\)-visits after \(s_{b,i}\) occur at
\(t_{b,i}\) and \(t_{b,i+1}\).  Therefore

\[
 t_{b,i+1}-s_{b,i}
 =(t_{b,i}-s_{b,i})+(t_{b,i+1}-t_{b,i})
 =r_{b,i}+g_{b,i}.                               \tag{2.2}
\]

This proves (0.1), and summing its horizon indicator proves (0.2).

Finally,

\[
\begin{aligned}
 h_{b,i}
 &=s_{b,i+1}-s_{b,i}\\
 &=(t_{b,i+1}-r_{b,i+1})-(t_{b,i}-r_{b,i})\\
 &=g_{b,i}+r_{b,i}-r_{b,i+1},
\end{aligned}
\]

which proves (0.3).  Summing (0.3) around the cycle recovers only the
tautology \(\sum_i h_{b,i}=\sum_i g_{b,i}=L\); it supplies no absolute
normalization of \(r\).

## 3. Exact Kac sums and their limitation

For every actual orbit,

\[
 \sum_{i=1}^q g_{b,i}=L,
 \qquad q=L/p.
\]

Summing over \(b\) gives

\[
 \sum_{b,i}1=L,
 \qquad
 \sum_{b,i}g_{b,i}=pL.                           \tag{3.1}
\]

Fix a reduced rank/peak cell and let \(\mathsf M_m(d,k)\) be its total
inverse-Pascal mass.  Multiplying (3.1) by the orbit-constant weight

\[
                         P_m(F)=\binom{m+d-k}{2d}
\]

and using the standard \(1/p\) augmented-to-root normalization gives

\[
 \boxed{
 \sum_{\mathcal O}{P_m\over p}\sum_{b,i}1
 =\mathsf M_m(d,k),
 \qquad
 \sum_{\mathcal O}{P_m\over p}\sum_{b,i}g_{b,i}
 =p\,\mathsf M_m(d,k).}                          \tag{3.2}
\]

Thus the mean predecessor gap is exactly \(p\).  On the inverse-Pascal
saddle,

\[
                         p=m+O(\sqrt{m\log m}),
\]

whereas \(G=2A\sqrt m+O(1)\).  But (3.2) does not control the lower tail
of the coupled sums \(r_{b,i}+g_{b,i}\): a mean constraint permits many
small gaps compensated by a few long gaps, and it contains no information
about their residual phases.

## 4. Alternation-respecting same-marginal obstruction

Let \(p\ge5\), put

\[
                         P=2p,\qquad \ell=2p-3,
\]

and place the two \(b\)-visits at \(0,\ell\).  Compare the two placements

\[
 a_{\rm early}=\{1,\ell+1\},
 \qquad
 a_{\rm late}=\{\ell-1,\ell+2\}.                 \tag{4.1}
\]

Both cyclic systems strictly alternate \(b,a,b,a\).  In both, the
ordered cyclic \(b\)-gap sequence is \((\ell,3)\).  The ordered cyclic
\(a\)-gap sequences are \((\ell,3)\) and \((3,\ell)\), respectively,
which are the same cyclic sequence with different starting index.

In the early coupling, the second future \(b\)-visit after either
\(a\)-visit has delay \(\ell+2\).  In the late coupling, the corresponding
delays are

\[
                         4,\qquad\ell+1.          \tag{4.2}
\]

Indeed the first late visit at \(\ell-1\) sees \(b\) at \(\ell\) and
\(P\), while the second at \(\ell+2=P-1\) sees \(b\) at \(P\) and
\(P+\ell\).

Therefore, for every

\[
                         4\le G<\ell+1,           \tag{4.3}
\]

the early coupling has no active \(a\)-visit and the late coupling has
exactly one.  The active late visit \(\ell-1\) is even, so the discrepancy
survives restriction to the \(\tau={\cal U}_d^2\) phases.

To make full balanced words, place every remaining label twice in the
unused early positions, and define the late word by reflecting all labels
through

\[
                         t\longmapsto\ell-t\pmod P.             \tag{4.4}
\]

The reflection fixes the \(b\)-position set, sends the early \(a\)-set to
the late one, and preserves every remaining label's cyclic gap multiset.
Thus all one-particle visit counts, gap multisets, and killed-shift Jordan
spectra agree.  The stronger ordered-cycle statement for the tested pair
was checked above.

This proves exactly what scalar renewal information omits.  It does not
purport to realize the completed words as PBBS orbits; simultaneous
alternation and Dyck chronology for all other adjacent label pairs are
precisely the additional structure a successful PBBS theorem must use.

## 5. Packing and deck boundary

The residual normal form does not establish either

\[
 \overline\nu_H=\Omega_A(B_m/H)
 \qquad\hbox{or}\qquad
 \overline\nu_H=o_A(B_m/H).
\]

If a future PBBS-specific residual theorem supplies a quotient packing
of size \(c_AB_m/H\), the exact deck lift gives

\[
 \boxed{
 \nu_H(P_m)\ge c_A{NB_m\over H}
 =\left({2c_A\over A}+o(1)\right)B_m\sqrt m.}     \tag{5.1}
\]

There is no factor two in this lower deck direction.  Conversely, the
upper packing/transversal comparison can lose the familiar factor two.

The precise unresolved quantity is now the Pascal-weighted joint law of

\[
                         (g_{b,i},r_{b,i})
\]

on the genuine long-period saddle orbits, together with the alignment of
the indicators in (0.2) at even phase separations \(1,\ldots,H+1\).
