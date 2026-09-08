# Long physical arcs: a favorable q=1 profile and an all-depth retirement gate

**Date:** 2026-08-21  
**Method:** pure mathematics; the finite checker is an audit only  
**Status:** exact arc degrees, multiplicity, and pair profile; naive
all-depth matching is ruled out, while the q=1 long-fragment route remains
open

## 0. Outcome

Put

\[
 b=2r+1,\qquad
 \mathcal M=\binom{[b]}r,\qquad
 \mathcal L=\binom{[b]}{r-1},\qquad
 A=|\mathcal M|,
 \tag{0.1}
\]

and fix \(1\le\ell\le r\).  An **oriented \(\ell\)-arc word** is a word

\[
                  w=(w_0,\ldots,w_{r+\ell-2})       \tag{0.2}
\]

of distinct labels from \([b]\).  At starts \(0\le i<\ell\), put

\[
 M_i=\{w_i,\ldots,w_{i+r-1}\},\qquad
L_i=\{w_i,\ldots,w_{i+r-2}\}.                       \tag{0.3}
\]

Throughout, \((x)_j=x(x-1)\cdots(x-j+1)\) is a falling factorial, with
\((x)_0=1\).

The q=1 arc hypergraph has vertex set \(\mathcal M\sqcup\mathcal L\)
and one indexed edge \(\{M_i,L_i:0\le i<\ell\}\) for every word (0.2).
Its exact degrees are

\[
 \boxed{
 D_M=\ell r!(r+1)_{\ell-1},\qquad
 D_L=\ell(r-1)!(r+2)_\ell,
 \qquad {D_L\over D_M}={r+2\over r}.}                \tag{0.4}
\]

Every underlying target-set edge has parameter multiplicity exactly
\((r-\ell)!\), so quotienting to the simple hypergraph divides all degrees
and codegrees by the same number.

The maximum pair codegree has scale \(D_M/r\).  In fact, for
\(S\in\mathcal L\), \(M\in\mathcal M\), and \(S\subset M\),

\[
 d(M,S)={2\ell-1\over\ell r}D_M,                     \tag{0.5}
\]

while every same-layer pair has codegree \(O(D_M/r^2)\), uniformly for
\(\ell=o(r)\).  The complete formulas are in Section 2.  Consequently

\[
 {\Delta_2\over D_M}={2-1/\ell\over r}\le {2\over r},
 \qquad
 {2\ell\Delta_2\over D_M}=O(\ell/r)=o(1)             \tag{0.6}
\]

when \(\ell=o(r)\); the first ratio is \((2+o(1))/r\) if also
\(\ell\to\infty\).  Thus the q=1 long-arc catalogue has the favorable
growing-rank pair signature sought for a near matching.  Such a matching
would directly supply physical fragments of length \(\ell\), and an
H-collar at their ends would cost \(O(HA/\ell)=o(A)\) when
\(H\ll\ell\).

There is, however, an exact boundary on what may be put into the same
ordinary matching edge.  If every arc start also carries all same-start
targets of ranks \(r-q\), \(1\le q\le H\), then:

1. the degree of a fixed rank-\((r-q)\) target is

   \[
    D_q=\ell(r-q)!(r+q+1)_{\ell+q-1}
       ={A\over A_q}D_M,
    \qquad A_q=\binom b{r-q};                         \tag{0.7}
   \]

2. target-disjointness at depth H bounds any matching by \(A_H/\ell\)
   arcs, so it covers at most \(A_H\) middle targets; and
3. the edge rank is \((H+1)\ell\), while the attached q=1 pair floor
   (0.5) remains.  Hence

   \[
    {(H+1)\ell\Delta_2\over D_M}
       \ge { (H+1)(2\ell-1)\over r}.                 \tag{0.8}
   \]

For \(H=\alpha\sqrt{r\log r}\),

\[
                  {A_H\over A}=r^{-\alpha^2+o(1)}.   \tag{0.9}
\]

Thus, at this \(H=\alpha\sqrt{r\log r}\) scale, the naive all-depth arc
hypergraph loses almost every middle target and also fails the natural
rank-scaled codegree test whenever \(H\ll\ell\).  Long arcs remain a
positive q=1 fragment route only if
deeper targets are handled by a declining retirement schedule or a
cluster-aware coupon theorem, not by placing every depth in one ordinary
hyperedge.

## 1. Exact degrees and simple-edge multiplicity

There are \((b)_{r+\ell-1}\) parameter words.

### Lemma 1.1 (target degrees)

Equations (0.4) and (0.7) hold.

#### Proof

Fix a middle target M and its start i.  Order its r labels in \(r!\) ways
and fill the \(\ell-1\) word positions outside that window by an ordered
selection from the \(r+1\) complementary labels.  There are \(\ell\)
choices for i, proving the first formula in (0.4).

For a fixed lower target L, order its \(r-1\) labels and fill the remaining
\(\ell\) positions from its \(r+2\) complementary labels.  This proves the
second formula.  Taking the ratio of the falling factorials gives
\((r+2)/r\).

At depth q, a fixed \((r-q)\)-target occupies one of \(\ell\) starts.  Its
labels have \((r-q)!\) orders, and the remaining \(\ell+q-1\) positions
are filled from \(r+q+1\) labels.  This gives the first formula in (0.7).
Finally

\[
 {D_q\over D_M}
 ={(r-q)!(r+q+1)!\over r!(r+1)!}
 ={\binom b r\over\binom b{r-q}},
\]

proving the second. \(\square\)

### Lemma 1.2 (uniform parameter multiplicity)

Every underlying q=1 target-set edge is represented by exactly
\((r-\ell)!\) words.

#### Proof

Inside one edge, containment between its lower and middle targets forms the
path

\[
 L_0-M_0-L_1-M_1-\cdots-L_{\ell-1}-M_{\ell-1}.       \tag{1.1}
\]

Indeed, \(L_i\subset M_j\) exactly for \(j=i\), and also for \(j=i-1\)
when \(i\ge1\).  The two shores distinguish the endpoints, so the target
set recovers the displayed direction.

The transitions recover the outgoing word labels
\(w_0,\ldots,w_{\ell-2}\), and the flags recover the incoming labels
\(w_{r-1},\ldots,w_{r+\ell-2}\).  The remaining positions
\(w_{\ell-1},\ldots,w_{r-2}\) form a common core of size \(r-\ell\);
their set is recovered, but their order is invisible to every target in
the edge.  Its arbitrary ordering gives exactly \((r-\ell)!\)
representations. \(\square\)

## 2. Exact pair codegrees

All formulas below count parameter words; Lemma 1.2 shows that the simple
quotient has the same relative values.

For two middle targets at Johnson distance d, \(1\le d<\ell\),

\[
 \lambda^{MM}_d
  =2(\ell-d)(d!)^2(r-d)!(r+1-d)_{\ell-1-d},          \tag{2.1}
\]

and the codegree is zero for \(d\ge\ell\).

For two lower targets at Johnson distance d, \(1\le d<\ell\),

\[
 \lambda^{LL}_d
  =2(\ell-d)(d!)^2(r-1-d)!(r+2-d)_{\ell-d},          \tag{2.2}
\]

and again it is zero for \(d\ge\ell\).

For a mixed pair \(M,S\), put \(d=|M\setminus S|\).  It has zero
codegree unless \(1\le d\le\ell\), and

\[
 \lambda^{ML}_1
  =(2\ell-1)(r-1)!(r+1)_{\ell-1},                    \tag{2.3}
\]

while, for \(2\le d\le\ell\),

\[
 \lambda^{ML}_d
  =(2\ell-2d+1)d!(d-1)!(r-d)!(r-d+2)_{\ell-d}.       \tag{2.4}
\]

### Proposition 2.1 (complete pair profile)

Equations (2.1)--(2.4) are exact.  Uniformly for \(\ell=o(r)\), their
maximum is (2.3), and hence (0.5)--(0.6) hold.

#### Proof

Suppose first that two rank-r windows occur with positive start gap d.
There are \(2(\ell-d)\) choices of their left-right order and positions.
Their outgoing d labels, common \(r-d\) labels, and incoming d labels may
be ordered in \(d!,(r-d)!,d!\) ways.  The remaining \(\ell-1-d\) word
positions are filled from the \(r+1-d\) labels outside their union.  This
is (2.1).  The same cut with window length \(r-1\) leaves \(\ell-d\)
outside positions and proves (2.2).

For a mixed pair, its two possible relative placements have the lower
window start d positions to the right of the middle start, or d-1
positions to its left.  When d=1 these are the two boundary facets of M.
They contribute \(\ell\) and \(\ell-1\) placements, respectively, and
give (2.3).  For d>=2 the two placement counts are \(\ell-d\) and
\(\ell-d+1\); the common order factor is

\[
              d!(d-1)!(r-d)!(r-d+2)_{\ell-d},
\]

which proves (2.4).

Divide by D_M.  At d=1, the three ratios are

\[
 {\lambda^{MM}_1\over D_M}
  ={2(\ell-1)\over\ell r(r+1)},\quad
 {\lambda^{LL}_1\over D_M}
  ={2(\ell-1)\over\ell r(r-1)},\quad
 {\lambda^{ML}_1\over D_M}
  ={2\ell-1\over\ell r}.                            \tag{2.5}
\]

For \(\ell=o(r)\), consecutive ratios in each of (2.1), (2.2), and
(2.4), after division by D_M, are O(\ell^2/r^2).  Thus all d>=2 terms are
smaller than their d=1 terms for large r.  The mixed d=1 term is the
largest in (2.5), proving the proposition. \(\square\)

## 3. The all-depth cardinality and codegree obstructions

Let the lower all-depth arc hypergraph add, at each start i, the targets
\(I_w(i,r-q)\) for every \(1\le q\le H\).  It has edge rank
\((H+1)\ell\), and Lemma 1.1 gives every layer degree.

### Theorem 3.1 (full-depth arcs cannot near-saturate the middle)

Every matching in this hypergraph has at most \(A_H/\ell\) edges and hence
covers at most \(A_H\) middle targets.  Moreover (0.8) holds.

#### Proof

Every hyperedge contains \(\ell\) distinct rank-\((r-H)\) targets, and a
matching cannot reuse any such target.  There are A_H targets in that
layer.  This proves the cardinality bound.

The hypergraph still contains the same-start q=1 attached pairs counted by
the first \(\ell\) placements in (2.3), of codegree \(D_M/r\).  Using the
full mixed-pair value gives the stronger lower bound (0.8). \(\square\)

The exact ratio

\[
 {A_H\over A}=\prod_{j=0}^{H-1}{r-j\over r+2+j}      \tag{3.1}
\]

has logarithm \(-H(H+1)/r+o(\log r)\) at
\(H=\alpha\sqrt{r\log r}\), proving (0.9).

The same conclusion is stronger if upper as well as lower nested targets
are inserted: the rank becomes \((2H+1)\ell\), while the final lower-layer
cardinality obstruction is unchanged.

## 4. What remains positive

At q=1, the uniform fractional weight \(1/D_L\) saturates every lower
target and loads every middle target by \(r/(r+2)\).  Its total mass is
\(|\mathcal L|/\ell\), the target-capacity optimum.  At lower depth q it
would induce mean target load

\[
                       {D_q\over D_L}={A_1\over A_q}. \tag{4.1}
\]

Thus the q=1 arc catalogue has the correct scalar capacity and long
physical geometry.  What (4.1) does not control is the integral coupon
gap: at shallow q the mean is only \(1+O(q^2/r)\), so independent or
Poisson-like rounding leaves a positive fraction of that layer uncovered.

The precise positive target is therefore:

> Find a near-optimal matching in the q=1 arc hypergraph whose interior
> depth-q windows, after an H-collar is removed at arc boundaries, have
> aggregate hole count o(A).

The present theorem proves that ordinary q=1 pair geometry and boundary
cost do not obstruct this target.  It also proves why one cannot obtain it
by adding all deeper targets to the same unretired matching hypergraph.
A successful proof needs correlated coupon control, an explicit declining
retirement schedule, or a cluster-aware theorem treating one nested start
profile as an atom.

## 5. Scope

The proved content is:

1. exact degrees at q=1 and every lower depth;
2. exact uniform parameter multiplicity and the complete q=1 pair profile;
3. the favorable q=1 normalized pair parameter O(1/r);
4. the exact all-depth cardinality obstruction; and
5. the all-depth rank-scaled pair-codegree floor.

The note does not invoke an unaudited growing-rank nibble theorem and does
not prove a q=1 arc matching, correlated deeper coupon coverage, a retired
arc schedule, endpoint-order coinstantiation, or a universal word.

## 6. Checker

The finite audit is

```text
scratch/audit_long_arc_q1_profile_and_all_depth_gate_20260821.py
```

It enumerates all parameter words for small \((r,\ell)\), checks every
degree, edge multiplicity, and pair-codegree formula, and checks the
all-depth degree formula.  The computation is an audit only; all asymptotic
claims above are analytic.
