# Exact owner incidence for moving-bank carousels, a local coset packing, and the separated-core boundary

**Date:** 2026-08-07  
**Status:** theorem.  This note settles the exact degree and pair-codegree
ledger for the owner-copy hypergraph and gives an explicit owner-disjoint
packing on one fixed support.  It also proves that the tempting strategy of
separating the permanent cores can never yield a positive-density owner
packing.  It does not prove the remaining overlapping-core global packing.

## 1. The abstract owner configuration

Use the parameters of the moving-bank carousel

\[
 n=2m+1,\qquad D=d+1,\qquad s=m-2d,
 \qquad p=s-1=m-2d-1,
\tag{1.1}
\]

and choose

\[
 R\ge d+2,\qquad L=Rd,
 \qquad p+L\le n.
\tag{1.2}
\]

Put

\[
                         t=m-p=2d+1.                 \tag{1.3}
\]

On an abstract coordinate set, let \(P_0\) be the permanent core of size
\(p\), and let \(F_0=B\mathbin{\dot\cup}Z\) be the labelled carousel bank of
size \(L\).  Write the \(L\) rank-\(m\) owners from the moving-bank theorem as

\[
                         O_e=P_0\cup Q_e,
 \qquad Q_e\in{F_0\choose t},\qquad e\in\mathbb Z_L.
\tag{1.4}
\]

The moving-bank theorem says that the \(O_e\)'s are distinct.  It will be
useful that every two of them have the common \(p\)-set \(P_0\); hence

\[
 1\le |O_e\setminus O_f|=|Q_e\setminus Q_f|\le t
 \quad(e\ne f).                                      \tag{1.5}
\]

For \(1\le q\le t\), define the exact ordered distance inventory

\[
 a_q:=\bigl|\{(e,f):e\ne f, |Q_e\setminus Q_f|=q\}\bigr|.
\tag{1.6}
\]

Thus

\[
                         \sum_{q=1}^{t}a_q=L(L-1).   \tag{1.7}
\]

## 2. The parameterized owner-copy hypergraph

Let 

\[
                         \mathcal V={ [n]\choose m},
 \qquad W=|\mathcal V|.                              \tag{2.1}
\]

Form a parameterized \(L\)-uniform multihypergraph \(\mathcal H_{\rm car}\)
on \(\mathcal V\) as follows.  For every injection

\[
                         \phi:P_0\dot\cup F_0\hookrightarrow[n],
\tag{2.2}
\]

insert the hyperedge

\[
                         E_\phi=\{\phi(O_e):e\in\mathbb Z_L\}.
\tag{2.3}
\]

Parallel copies are retained only to make the incidence identities exact.
They are harmless for matching: a matching in the multihypergraph projects
to a matching of literal carousel owner sets.

### Theorem 2.1 (exact degree and pair codegree)

The hypergraph \(\mathcal H_{\rm car}\) is regular, of degree

\[
 \boxed{
 \Delta=L\,m!\,(n-m)_{p+L-m}.
 }
\tag{2.4}
\]

If \(X,Y\in\mathcal V\) have Johnson distance

\[
                         q=|X\setminus Y|,
\tag{2.5}
\]

then their codegree is zero for \(q>t\), while for \(1\le q\le t\),

\[
 \boxed{
 \Delta(X,Y)
 =a_q(m-q)!(q!)^2(n-m-q)_{p+L-m-q}.
 }
\tag{2.6}
\]

Equivalently,

\[
 \boxed{
 {\Delta(X,Y)\over\Delta}
 ={a_q/L\over {m\choose q}{n-m\choose q}}.
 }
\tag{2.7}
\]

#### Proof

Fix \(X\in\mathcal V\).  Choose the unique abstract owner position \(e\)
which maps to \(X\), biject its \(m\) labels with \(X\), and inject the
remaining \(p+L-m\) labels into \([n]\setminus X\).  This gives

\[
                         Lm!(n-m)_{p+L-m}
\]

injections.  Since the abstract owners are distinct, an injection is not
counted twice.  This proves (2.4).

Now fix distinct \(X,Y\) at distance \(q\).  An ordered abstract pair
\((O_e,O_f)\) can map to \((X,Y)\) only if its distance is \(q\), giving
\(a_q\) choices.  Its intersection, first difference and second difference
have sizes \(m-q,q,q\), respectively.  Their bijections contribute

\[
                         (m-q)!(q!)^2.
\]

The remaining \(p+L-m-q\) abstract labels are injected outside
\(X\cup Y\), giving the last factor of (2.6).  If \(q>t\), (1.5) makes the
codegree zero.

Finally,

\[
 { (m-q)!(q!)^2\over m!}
 { (n-m-q)_{p+L-m-q}\over(n-m)_{p+L-m}}
 ={1\over {m\choose q}{n-m\choose q}},
\]

which proves (2.7). \(\square\)

### Corollary 2.2 (coarse uniform pair-codegree bound)

If \(t<m/2\), then

\[
 \boxed{
 {\Delta_2(\mathcal H_{\rm car})\over\Delta}
 \le {L-1\over m(m+1)}.
 }
\tag{2.8}
\]

In the triangular regime this is \(O(1/m)=O(1/L)\).  For the minimal
choice \(R=d+2\),

\[
 L\,{\Delta_2\over\Delta}
 \le {L(L-1)\over m(m+1)}
 \longrightarrow {\pi^2\over16}.                   \tag{2.9}
\]

#### Proof

For \(1\le q\le t<m/2\), the numbers

\[
                         {m\choose q}{m+1\choose q}
\]

are minimized at \(q=1\).  Also \(a_q/L\le L-1\).  Apply (2.7), use
\(n-m=m+1\), and then \(d^2/m\to\pi/4\). \(\square\)

The coarse bound discards nearly all of the literal cycle geometry.  The
actual maximum codegree is one power of \(L\) smaller.

### Theorem 2.3 (the only Johnson-distance-one pairs are cycle edges)

Assume \(d\ge3\).  Then

\[
                         a_1=2L.                    \tag{2.10}
\]

Consequently, for all sufficiently large triangular parameters,

\[
 \boxed{
 {\Delta_2(\mathcal H_{\rm car})\over\Delta}
 ={2\over m(m+1)}=\Theta(L^{-2}).
 }
\tag{2.11}
\]

The same conclusion holds for \(d=2,R\ge5\).  The isolated template
\((d,R)=(2,4)\) has additional high--high chords and is irrelevant to the
asymptotic statement.

#### Proof

Write

\[
 C_j=\{b_j,\ldots,b_{j+d}\},\qquad
 D_j=\{b_{j-1},\ldots,b_{j+d}\}.                   \tag{2.12}
\]

The noncore parts of the owners are

\[
 \begin{aligned}
 Q_{j,0}&=D_j\cup\{z_{j-1,a}:1\le a<d\},\\
 Q_{j,r}&=C_j
   \cup\{z_{j-1,a}:r\le a<d\}
   \cup\{z_{j,a}:1\le a\le r\},
       &&1\le r<d.                                  \tag{2.13}
 \end{aligned}
\]

For two low owners in the same period, direct cancellation in (2.13)
gives

\[
                         d_J(Q_{j,r},Q_{j,u})=|r-u|. \tag{2.14}
\]

For a high owner and a low owner in the same period,

\[
                         d_J(Q_{j,0},Q_{j,r})=r.     \tag{2.15}
\]

For a low owner and the next high owner,

\[
                         d_J(Q_{j,r},Q_{j+1,0})=d-r.\tag{2.16}
\]

Thus distance one occurs in these cases exactly at consecutive positions
of the carousel.

It remains to exclude chords between different periods.  The \(Z\)-part
of an owner in period \(j\) is supported on period blocks \((j-1,j)\), and
a high owner uses only block \(j-1\).  Nonadjacent period supports are
disjoint, giving distance at least \(d-1\ge2\).  For low owners in
consecutive periods, say \((j,r)\) and \((j+1,u)\), their \(B\)-parts have
Johnson distance one and their \(Z\)-parts have intersection of size

\[
                         \max(0,r-u+1).
\]

Their total Johnson distance is therefore

\[
                         1+d-\max(0,r-u+1)\ge2.     \tag{2.17}
\]

Two consecutive-period high owners have disjoint \(Z\)-parts of size
\(d-1\), and hence distance at least \(d-1\).  The remaining orientations
are the same cases with indices reversed.  This proves that the \(L\)
unordered cycle edges are the only distance-one pairs, yielding (2.10).

At \(q=1\), equation (2.7) now gives \(2/[m(m+1)]\).  For \(q\ge2\),

\[
 {\Delta(X,Y)\over\Delta}
 \le {L-1\over {m\choose2}{m+1\choose2}}
 =O(m^{-3}),                                        \tag{2.18}
\]

because the binomial product is increasing throughout
\(2\le q\le t=o(m)\).  The \(q=1\) value is therefore maximal for large
\(m\), proving (2.11). \(\square\)

### Corollary 2.4 (exact fractional owner factor)

Giving every parameterized carousel weight \(1/\Delta\) is a fractional
perfect matching of \(\mathcal H_{\rm car}\).  Its total weight is

\[
                         {W\over L}.                 \tag{2.19}
\]

This is the correct scalar count for a complete owner factor.

## 3. The quantitative growing-uniformity boundary

The coarse estimate (2.8) by itself cannot be fed formally into a
fixed-uniformity Pippenger--Spencer theorem, because \(L\to\infty\).
Indeed, regularity, a perfect fractional matching, and only the weaker
information

\[
                         \Delta_2/\Delta=\Theta(1/L)
\tag{3.1}
\]

do not imply a positive-density integral matching for growing \(L\).

Indeed, take the line hypergraph of a projective plane of order \(q\).  It
is \((q+1)\)-uniform and \((q+1)\)-regular, every pair of vertices has
codegree one, and the uniform edge weighting is a fractional perfect
matching.  But every two lines meet, so its maximum matching has one edge
and covers only

\[
                         {q+1\over q^2+q+1}=o(1)
\]

of the vertices.  Here \(\Delta_2/\Delta=1/(q+1)=1/L\).

This shows why the literal sharpening in Theorem 2.3 matters: the actual
carousel has \(\Delta_2/\Delta=\Theta(L^{-2})\), so the projective-plane
obstruction does not model it.

This stronger estimate is still not, by itself, a cited all-parameter
matching theorem.  Classical Pippenger--Spencer statements fix the
uniformity before taking the asymptotic limit.  The available effective
error estimates have exponents and implicit thresholds depending on that
uniformity; substituting \(L=\Theta(m)=\Theta(\log W)\) into a
fixed-\(L\) conclusion is therefore not a valid diagonal argument.

Thus a positive-density conclusion still needs either a quantitative
large-uniformity nibble specialized to fixed target density, or further
higher-intersection structure of this copy hypergraph.  What is now ruled
out is the former projective-plane-scale obstruction: the actual carousel
has an extra factor \(L^{-1}\) of pairwise pseudorandomness.

## 4. A deterministic owner packing on one fixed core and support

There is nevertheless a large exact local packing hidden in the carousel.
Partition the bank as

\[
 F_0=B\mathbin{\dot\cup}Z_1\mathbin{\dot\cup}\cdots
          \mathbin{\dot\cup}Z_{d-1},
 \qquad |B|=|Z_i|=R,                                 \tag{4.1}
\]

using the period index \(j\in\mathbb Z_R\) on every part.  Let

\[
                         G=(\mathbb Z_R)^d            \tag{4.2}
\]

act by independent cyclic translation on the \(d\) parts.  Translating all
parts by the same amount is the diagonal subgroup

\[
                         \Delta_G=\{(c,c,\ldots,c):c\in\mathbb Z_R\}.
\tag{4.3}
\]

For \(R\ge d+3\), every age profile has a proper cyclic interval on \(B\),
and equality between one translated owner and another forces the
translation difference to lie in \(\Delta_G\).

For \(R=d+2\), the high owner uses all of \(B\).  Its stabilizer is the
larger subgroup

\[
 K_0=\{(c_B,c,c,\ldots,c):c_B,c\in\mathbb Z_R\},
 \qquad |K_0|=R^2.                                  \tag{4.4}
\]

Every low-owner stabilizer is still \(\Delta_G\subset K_0\).

### Theorem 4.1 (translation-coset packing)

On one fixed labelled pair \((P_0,F_0)\), there are pairwise
owner-disjoint translated carousels numbering

\[
 \boxed{
 M_{R,d}=\begin{cases}
 R^{d-1},&R\ge d+3,\\
 R^{d-2},&R=d+2.
 \end{cases}}
\tag{4.5}
\]

They cover respectively \(LR^{d-1}\) and \(LR^{d-2}\) distinct
rank-\(m\) owners.

#### Proof

Choose one representative from every coset of \(\Delta_G\) when
\(R\ge d+3\), or from every coset of \(K_0\) when \(R=d+2\), and translate
the whole labelled carousel by that representative.

The age of an owner is recovered from its part-size profile: age zero has
\(d+2\) elements of \(B\), while age \(r\ge1\) has \(d+1\) elements of
\(B\) and two elements of the distinguished part \(Z_r\).  Hence equal
owners have equal age.

At a positive age, equality of the singleton entries in all other
\(Z\)-parts, the adjacent pair in \(Z_r\), and the proper cyclic interval
in \(B\) forces all part translations to differ by one common diagonal
shift.  At age zero the same conclusion holds when \(R\ge d+3\).  For
\(R=d+2\), the \(B\)-part is all of \(B\), so equality forces only the
\(Z\)-translations to have one common difference; this is exactly (4.4).

Two chosen representatives have difference in neither relevant
stabilizer.  Their translated owner inventories are therefore disjoint.
The coset counts are \(|G|/R=R^{d-1}\) and
\(|G|/R^2=R^{d-2}\). \(\square\)

This theorem is an exact nontrivial integral owner packing, but its size is
subexponential in \(n\), whereas \(W\) is exponential.  It is a local
building block, not yet the required theta-density packing.

## 5. A sharp no-go for separating the permanent cores

A very tempting global strategy is to choose permanent cores so far apart
that owner collisions become impossible without inspecting the moving
banks.  This strategy cannot have positive density.

For \(P,P'\in{[n]\choose p}\), every owner over \(P\) contains \(P\).
Therefore the sufficient automatic-separation condition is

\[
                         |P\cup P'|>m.               \tag{5.1}
\]

Since \(m-p=t\), this is equivalent to

\[
                         d_J(P,P')>t=2d+1.           \tag{5.2}
\]

### Theorem 5.1 (separated-core sphere bound)

Let \(\mathcal C\subseteq{[n]\choose p}\) satisfy (5.2).  Even if, for
each \(P\in\mathcal C\), one could use **every** rank-\(m\) superset of
\(P\) exactly once, the total fraction of the owner layer covered would be
at most

\[
 \boxed{
 { {m\choose 2d+1}\over
    \displaystyle\sum_{i=0}^{d}{p\choose i}{n-p\choose i}}
 =\exp\bigl(-(2\log2+o(1))d\bigr)=o(1).
 }
\tag{5.3}
\]

In particular, separated permanent cores cannot produce a fixed positive
owner density, and hence cannot produce the theta bank.

#### Proof

The Johnson balls of radius \(d\) around the members of \(\mathcal C\)
are disjoint by (5.2).  If

\[
 B_d(p,n):=\sum_{i=0}^{d}{p\choose i}{n-p\choose i},
\]

then the sphere-packing bound gives

\[
                         |\mathcal C|
 \le {{n\choose p}\over B_d(p,n)}.                  \tag{5.4}
\]

One core is contained in exactly \({n-p\choose m-p}\) owners.  Double
counting incidences \(P\subset X\), with \(|P|=p,|X|=m\), gives

\[
 {n\choose p}{n-p\choose m-p}
 ={n\choose m}{m\choose p}
 =W{m\choose 2d+1}.                                 \tag{5.5}
\]

Multiplying (5.4) by the number of owners over one core and using (5.5)
proves the first expression in (5.3).

For the asymptotic estimate, retain only the \(i=d\) term in the
denominator.  Since \(p=m-2d-1\), \(n-p=m+2d+2\), and \(d=o(m)\), Stirling's
formula gives

\[
 \begin{aligned}
 \log {m\choose 2d+1}
  &= (2d+1)\log {m\over2d+1}+(2d+1)+O(\log d+d^2/m),\\
 \log\left({p\choose d}{n-p\choose d}\right)
  &=2d\log {m\over d}+2d+O(\log d+d^2/m).
 \end{aligned}
\]

Their difference is

\[
                         -2d\log2+O(\log d+d^2/m),
\]

which proves (5.3). \(\square\)

## 6. Exact owner-row frontier

Three facts are now rigorous.

1. The complete carousel-copy hypergraph has an exact fractional perfect
   matching and pair-codegree \(\Theta(\Delta/L^2)\).
2. One fixed core and support admit an explicit large translation-coset
   owner packing.
3. Making different cores automatically noninteracting throws away an
   exponentially vanishing fraction of the owner layer, even under the
   impossible generosity of using every owner above each chosen core.

Thus the remaining owner theorem cannot be proved by either a black-box
fixed-uniformity nibble or a code of separated permanent cores.  It must
use correlated **overlapping** cores and the detailed multi-distance
structure of the carousel configuration.  A sufficient statement is:

> **Overlapping-core carousel packing lemma.**  The actual copy
> hypergraph \(\mathcal H_{\rm car}\) has a matching covering at least
> \((\theta+o(1))W\) owner vertices.

Theorem 2.1 supplies its exact incidence ledger, while Theorem 5.1 locates
the first strategy that provably cannot establish it.
