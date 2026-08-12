# Master audit of the three attached exploratory reports

## Verdict

The three attachments were read in full and checked against the current
constant-one frontier.  They contain no proof of

\[
\nu(k)\le (1+o(1))W(k).
\]

They are exploratory and, in two places, truncated or duplicated.  Their
useful residue consists of four exact facts:

1. the singleton external-touch model is a FIFO subset-Ucycle model;
2. in an odd wreath factor, complementary window ranks are exactly paired;
3. lower windows are consecutive intersections of middle windows;
4. full translation equivariance is arithmetically impossible for an
   infinite prime subfamily.

None of these removes the current positive integral packet-selection gate.

## 1. The singleton/Ucycle report

The ordered-partition/MTF dictionary and the following restricted statement
are correct: if every useful state is a permutation and every middle-changing
update touches an element outside the current middle prefix, then the middle
sets are FIFO windows of a symbol stream.  Selecting one ordering per middle
set and joining the corresponding directed tuple-edges into few Eulerian
components would therefore give a restricted sufficient construction.

It is **not** valid to make permutation states or singleton entries without
loss of generality.  The calibrated top-fibre promotion construction uses
genuine nonsingleton states and already evades the Ucycle reset barrier.
Consequently, coefficient one is not equivalent to a central near-Ucycle.

Other unsupported claims in that report include:

- a forced SCD-radius distribution for arbitrary near-optimal words;
- an assertion that a non-middle endpoint can raise the next middle depth by
  at most one;
- a static partial-sum closure argument applied to dynamic MTF blocks;
- heuristic FIFO-path codegrees used as if they were proved estimates.

The divisibility assertion that \(2m\nmid\binom{2m}{m}\) is also false in
general; for example \(12\mid\binom{12}{6}=924\).

## 2. Exact complementary-window identities

Let \(n=2m+1\), and let \(I_\pi(j,r)\) denote the cyclic interval of length
\(r\) in an order \(\pi\).  Then

\[
[n]\setminus I_\pi(j,r)=I_\pi(j+r,n-r).
\]

Hence, for every family of cyclic orders,

\[
\mu_r(S)=\mu_{n-r}(S^c).
\]

In the usual odd central indexing this pairs upper depth \(q\) with lower
depth \(q-1\): rank \(m+q\) is complementary to rank
\(m-(q-1)\).  In particular, an exact middle wreath factor automatically
covers rank \(m+1\) exactly.

Also,

\[
I_\pi(j,m-q)=\bigcap_{t=0}^{q} I_\pi(j-t,m).
\]

Thus a lower target occurs precisely when the middle cycle contains the
corresponding \((q+1)\)-vertex consecutive run in its up-set.  These are clean
reformulations, not constructions.

The attachments' proposed repair principle saying that arbitrary holes at
different ranks can be chained at cost equal to the maximum single-rank
defect is false without a nested-chain and literal-factorability theorem.
Endpoint throughput gives a lower capacity bound, not such an upper bound.

## 3. Exact nested codegrees

For an \(r\)-set \(S\) and an adjacent containing \((r+1)\)-set \(T\), the
fraction of cyclic orders containing \(S\) as a window, conditional on
containing \(T\), is

\[
\frac{2}{r+1}.
\]

Equivalently, conditional in the other direction the ratio is
\(2/(n-r)\).  This is the exact vertical clustering responsible for the
failure of black boxes that encode all ranks as unrelated vertices.  It is
already built into the calibrated packet analysis.

One incidence count in the second attachment omitted a factorial: a fixed
\(r\)-set lies in

\[
r!(n-r)!
\]

oriented cyclic orders modulo rotation.  For \(r=m-q\) this is
\((m-q)!(m+q+1)!\), not \((m-q)!(m+q)!\).

## 4. Translation-fixed wreaths

### Theorem 4.1

Let \(p=2m+1\) be prime and identify the ground set with \(\mathbb Z_p\).
A wreath fixed setwise by a nonzero translation is an arithmetic-progression
wreath.  Up to reversal there are exactly \(m\) such wreaths.

#### Proof

Write the middle windows of a cyclic order as

\[
A_j=I_\pi(j,m),\qquad j\in\mathbb Z_p.
\]

Their graph under intersection size \(m-1\) is the cycle
\(A_0A_1\cdots A_{p-1}A_0\).  A nonzero translation preserving the wreath
induces an order-\(p\) automorphism of this cycle.  It must therefore be a
nontrivial rotation: for some \(c\ne0\),

\[
A_{j+c}=A_j+1.
\]

Let \(x_j\) be the coordinate leaving when \(A_j\) is shifted to
\(A_{j+1}\).  The preceding identity gives

\[
x_{j+c}=x_j+1.
\]

As \(c\) is invertible modulo \(p\), this forces

\[
x_j=x_0+c^{-1}j,
\]

so the cyclic order is an arithmetic progression.  Conversely every
arithmetic-progression order is translation-fixed.  Nonzero differences are
identified in pairs under reversal, leaving \((p-1)/2=m\) unoriented
wreaths.  \(\square\)

### Corollary 4.2

If a translation-invariant exact middle factor contains \(a\) fixed wreaths
and the rest in free translation orbits, then

\[
\operatorname{Cat}_m=a+p b,\qquad 0\le a\le m.
\]

Moreover

\[
\operatorname{Cat}_m\equiv 2(-1)^m\pmod p.
\]

Indeed,

\[
\binom{p-1}{m}\equiv(-1)^m\pmod p,
\qquad (m+1)^{-1}\equiv2\pmod p.
\]

If \(p\equiv3\pmod4\), then \(m\) is odd and the required residue is
\(p-2>m\).  Therefore:

\[
\boxed{\text{For prime }p=2m+1\equiv3\pmod4,
\text{ no translation-invariant exact middle wreath factor exists.}}
\]

This rules out a natural algebraic symmetry ansatz.  It does not obstruct
non-equivariant factors or the calibrated top-packet route.

## 5. Relation to the current constructive frontier

The reports do not engage the strongest present reduction:

- choose the first crossing height \(H\sim\sqrt{m\log m}\);
- use one promotion packet on every \((m+H)\)-top;
- obtain \(W-o(W)\) physical middle-owner slots with total reset cost
  \(o(W)\);
- use a sparse reservoir to make all depths beyond
  \(Q\sim\sqrt{m\log\log m}\) negligible;
- use complementary-segment rectangles as exact rank-isolating signed
  repairs in the hard band.

The exact remaining work is positive and integral:

1. construct an owner-near-transversal of cyclic top packets whose shallow
   nested-column defect is small enough;
2. prove that sufficiently many required rectangle directions are
   support-feasible with bounded top congestion, preferably by packing many
   rectangles into each top.

The attachments neither prove nor refute either statement.
