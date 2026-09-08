# Audit: canonical ternary fibres give literal queue rings and one-third owner coverage

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_RANK2_QUEUE_CANONICAL_TRIPLE_FIBRES_AND_ONE_THIRD_OWNER_PACKING_20260807.md`  
**Verdict:** PASS.  The fibre partition, linear quotient, kernel-translate
packing, and conversion back to literal rank-two queue source words are exact.

## 1. Canonical fibres

Let \(Y\in\binom{[n]}{m+1}\) be eligible, let
\(B(Y)=(T_{i_1},\ldots,T_{i_p})\) be its first \(p\) singleton triples,
and let

\[
                         A(Y)=Y\setminus\bigcup_{j=1}^pT_{i_j}.
\]

Changing the unique chosen point inside any selected triple preserves its
singleton status.  It changes no intersection with any other global triple.
Consequently the first \(p\) singleton triples and the outside set \(A(Y)\)
remain fixed.  Thus the eligible complements partition into exact fibres

\[
                         A+\prod_{j=1}^pT_{i_j}
                         \cong\mathbb F_3^p.
\]

For a uniform \((m+1)\)-set,

\[
 \Pr(|Y\cap T_i|=1)
 =3\frac{\binom{n-3}m}{\binom n{m+1}}
 =\frac38+O(m^{-1}).
\]

There are \(2m/3+O(1)\) global triples, so the expected number of singleton
triples is \(m/4+O(1)\).  A selected--unselected transposition changes this
count in at most two triples.  Slice bounded differences therefore gives
an \(e^{-\Omega(m)}\) lower tail below \(p=o(m)\).  Hence eligible fibres
contain \((1-e^{-\Omega(m)})W\) owner complements.

## 2. Linear quotient

Put

\[
 \mathcal A=\{q\mathbf1+P_j:q\in\mathbb F_3,\ 0\le j<p\},
 \qquad
 P_j=e_1+\cdots+e_j.
\]

For \(h=1+\lceil\log_3p\rceil\), choose nonzero
\(s\in\mathbb F_3^h\) and choose \(R_0=0,R_1,\ldots,R_{p-1}\) in distinct
cosets of \(\langle s\rangle\).  The assignments

\[
 F(e_j)=R_j-R_{j-1}\quad(j<p),
 \qquad
 F(e_p)=s-R_{p-1}
\]

give

\[
                         F(P_j)=R_j,
 \qquad F(\mathbf1)=s.
\]

Therefore the \(3p\) points \(q s+R_j\) are distinct, so
\(F|_{\mathcal A}\) is injective.

## 3. Kernel translates

If

\[
                         c+a=c'+a',
 \qquad c,c'\in\ker F,quad a,a'\in\mathcal A,
\]

then applying \(F\) gives \(F(a)=F(a')\), hence \(a=a'\) and \(c=c'\).
Thus the translates \(c+\mathcal A\), \(c\in\ker F\), are pairwise
disjoint.

Their covered fraction is exactly

\[
                         \frac{3p}{|\operatorname{im}F|}.
\]

Injectivity on \(\mathcal A\) gives
\(|\operatorname{im}F|\ge3p\), while

\[
                         |\operatorname{im}F|
 \le3^h\le9p.
\]

Hence the covered fraction lies in \([1/3,1]\).

## 4. Literal queue-ring check

The coordinate of a point of \(\mathbb F_3^p\) records the omitted member
of the corresponding phase triple.  In cyclic order, \(\mathcal A\)
increments phases \(1,2,\ldots,p\) in each of three rounds.  This is exactly
the complement-state chronology of the rank-two block queue.

Adding \(c=(c_1,\ldots,c_p)\) replaces the omission label in phase \(i\) by
its translate modulo three.  Equivalently, it rotates the cyclic naming of
the three elements of that phase support by \(c_i\).  It does not change
the source-word rule.  Therefore every \(c+\mathcal A\) is a literal queue
ring, not merely an abstract set of owner states.

The original local theorem consequently supplies, for every selected
translate:

- a simple flat rank-\(m\) Johnson owner cycle of length \(3p\);
- simple immediate lower and upper owner palettes;
- owner gap \(p\) and positive run \(2p\) for each phase coordinate; and
- exact regeneration after \(3p\) source positions.

## 5. Global assembly and scope

Different kernel translates are owner-disjoint inside one fibre.  Different
canonical fibres are disjoint sets of complements, hence yield disjoint
rank-\(m\) owners after complementation.  The construction therefore covers

\[
                         \left(\frac13-o(1)\right)W
\]

owners by literal queue rings.

This closes the queue-owner matching row.  It does not establish disjointness
of the proper suffix targets carried by different rings, nor does it fuse the
rings into one physical chronology or construct the residual PBBS chart.
