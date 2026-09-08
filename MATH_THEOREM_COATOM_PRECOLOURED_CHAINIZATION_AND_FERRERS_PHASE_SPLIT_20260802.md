# Coatom-precoloured chainization and the exact Ferrers phase split

**Date:** 2026-08-02  
**Status:** unconditional exact reductions, an unconditional depth-two
positive theorem on the zero-boundary face, and a sharp arithmetic separation
of the zero-boundary and active-boundary cases.  This note does **not** prove a
`d+O(1)` coatom-rooted chain partition for general odd dimension.

## 0. Setup and result

Put

\[
        k=2r-1,\qquad
        W={k\choose r-1}={k\choose r},\qquad
        \Lambda=\sum_{s=1}^{r-1}{k\choose s}=2^{k-1}-1,
\]

and

\[
 d=\min\left\{q:qW+{q+1\choose2}\ge\Lambda\right\},
 \qquad h=(\Lambda-dW)_+ .                              \tag{0.1}
\]

Let `B` be a chosen Ferrers boundary bank of `h` strict-lower targets and
let

\[
 \mathcal R=\{S\subseteq[k]:1\le |S|\le r-1\}\setminus\mathcal B.
                                                               \tag{0.2}
\]

In the canonical triangular construction `B` lies in ranks at most `d`.
In the nontrivial range `d<r-1`, the complete coatom layer

\[
                         \mathcal Q={ [k]\choose r-1}          \tag{0.3}
\]

therefore remains in `R`.

This note proves four facts.

1. Coatom-rooted chainization is exactly a **bounded proper-colouring
   extension** of the incomparability graph, with the coatom clique
   precoloured bijectively.
2. The triangular boundary is active precisely when one explicit remainder
   is positive and at most a triangular number.  A gcd test rules this out;
   in particular it is never active in an odd prime dimension.
3. On the zero-boundary face, depth two always chainizes integrally by one
   ordinary containment flow.  At active depth two, the whole problem is
   exactly one Hall/min-cut test.  The only odd active depth-two parameter is
   `k=9`.
4. If the boundary is active, every exact depth-`d` solution is saturated:
   every coatom chain has length exactly `d`.  It consequently gives `W`
   chains of length exactly `2d` covering all but `2h+2` vertices of the
   full Boolean lattice.  Thus the active boundary is an equal-chain
   critical face, not an automatic absorber.

The result sharply distinguishes the two cases requested by the one-copy
normal form.  It also explains why perfect-graph colouring or a generic
max-flow argument cannot close the general `d>=3` row: bounded colouring is
NP-hard on co-comparability graphs for every fixed capacity at least three.
The complete Boolean instance may still have extra structure, but that
structure must be used explicitly.

## 1. Exact precoloured bounded-colouring equivalence

Let `G_R` be the incomparability graph of `R`: two targets are adjacent
exactly when neither contains the other.  The coatom layer `Q` is a clique
of size `W` in `G_R`.

### Theorem 1.1 (coatom-precoloured colouring normal form)

For an integer `q>=1`, the following are equivalent.

1. `R` has a partition

   \[
                    \mathcal R=\mathop{\dot\bigcup}_{Q\in\mathcal Q}C_Q
                                                               \tag{1.1}
   \]

   in which every `C_Q` is an inclusion chain of size at most `q` and has
   maximum `Q`.
2. `G_R` has a proper colouring

   \[
                         \phi:\mathcal R\longrightarrow\mathcal Q
                                                               \tag{1.2}
   \]

   satisfying

   \[
                  \phi(Q)=Q,\qquad |\phi^{-1}(Q)|\le q
                         \quad(Q\in\mathcal Q).                \tag{1.3}
   \]

#### Proof

Given (1.1), colour every member of `C_Q` by `Q`.  A colour class is a
chain, hence an independent set in the incomparability graph; (1.3) is
immediate.

Conversely, every colour class of a proper colouring is pairwise comparable
and hence is a chain.  It contains its precoloured coatom `Q`.  Every other
member has rank below `r-1`, so comparability with `Q` forces it to be a
subset of `Q`.  Therefore `Q` is the maximum of the class, and (1.3) gives
the length bound.  The colour classes partition `R`.  \(\square\)

This differs slightly from the earlier owner-list-colouring formulation.
Here the complete coatom layer is part of the target bank and is a
precoloured maximum clique.  Consequently anchoring and use of every colour
are automatic.

The graph `G_R` is a co-comparability graph and hence perfect.  Perfection
solves uncapacitated colouring, but not (1.2)--(1.3).  Bonomo, Mattia and
Oriolo prove that bounded colouring remains NP-hard on co-comparability
graphs for every fixed bound `q>=3` when the number of colours is part of
the input.  Thus there is no generic perfect-graph or ordinary-network
rounding of Theorem 1.1.  This is a route obstruction, not a hardness result
for the single highly symmetric Boolean instance.

## 2. Exact arithmetic phase split

Write

\[
                a=\left\lfloor{\Lambda\over W}\right\rfloor,
                \qquad \rho=\Lambda-aW,
                \qquad 0\le\rho<W .                          \tag{2.1}
\]

### Theorem 2.1 (remainder criterion)

For every odd `k>=3`,

\[
 d=
 \begin{cases}
 a,&0\le\rho\le {a+1\choose2},\\
 a+1,&\rho>{a+1\choose2},
 \end{cases}                                                \tag{2.2}
\]

and

\[
 h=
 \begin{cases}
 \rho,&0<\rho\le {a+1\choose2},\\
 0,&\rho=0\text{ or }\rho>{a+1\choose2}.
 \end{cases}                                                \tag{2.3}
\]

Thus the true triangular boundary is active if and only if

\[
                    0<\Lambda\bmod W\le {a+1\choose2}.        \tag{2.4}
\]

#### Proof

Since every strict-lower rank has size at most `W`, we have `a<=r-1`.
Also

\[
                         {a\choose2}<W.                       \tag{2.5}
\]

For `r>=3`, this follows already from
`W=binom(2r-1,r-1)>binom(r-1,2)`; the remaining case is immediate.
Consequently

\[
 (a-1)W+{a\choose2}<aW\le\Lambda,                            \tag{2.6}
\]

so `d>=a`.  The value `a` is admissible exactly when

\[
 aW+{a+1\choose2}\ge aW+\rho,
\]

which is the first line of (2.2).  If it is not admissible, `a+1` is
admissible even without its triangular term.  Formula (2.3) follows from
the definition of `h`.  \(\square\)

### Corollary 2.2 (gcd exclusion)

Let

\[
                         g=\gcd(\Lambda,W).
\]

If

\[
                         g>{a+1\choose2},                     \tag{2.7}
\]

then `h=0`.

#### Proof

The remainder `rho=Lambda-aW` is a multiple of `g`.  It cannot be both
positive and smaller than `g`.  Apply (2.3).  \(\square\)

### Corollary 2.3 (odd prime dimensions are zero-boundary)

If `k` is an odd prime, then `h=0`.

#### Proof

Write `k=2m+1`.  Fermat's theorem gives

\[
                         k\mid 2^{k-1}-1=\Lambda,
\]

and every nontrivial binomial coefficient in row `k` is divisible by `k`,
so `k|W`.  Hence `g>=k` in Corollary 2.2.

It remains to bound the triangular term.  The standard Wallis estimate

\[
                         {2m\choose m}\ge {4^m\over2\sqrt m}
\]

and

\[
 W={2m+1\over m+1}{2m\choose m}
       \ge {3\over2}{2m\choose m}
\]

give

\[
                         a<{4\sqrt m\over3}.                  \tag{2.8}
\]

Therefore

\[
 {a+1\choose2}
 <{8m\over9}+{2\sqrt m\over3}<2m+1=k.                       \tag{2.9}
\]

The last inequality follows because
`10m/9-2sqrt(m)/3+1>0`.  Thus (2.7) holds.  The case `k=3` is also
immediate directly.  \(\square\)

There are infinitely many odd primes, so the Ferrers correction disappears
on an infinite subsequence.  In particular, the general static problem
cannot be reduced to absorbing the small boundary bank: on that subsequence
there is no boundary bank at all.

## 3. The complete depth-two face

Assume first that `d=2` and `h=0`.  Put

\[
 \mathcal P=\{S\subseteq[k]:1\le |S|\le r-2\}.
\]

Then `|P|=Lambda-W<=W`.

### Theorem 3.1 (zero-boundary depth-two chainization)

There is an injection

\[
                         f:\mathcal P\hookrightarrow\mathcal Q,
                         \qquad S\subset f(S).                 \tag{3.1}
\]

Consequently the complete lower ideal has a coatom-rooted chain partition
of depth at most two.

#### Proof

In the containment bipartite graph from `P` to `Q`, let every rank-`s`
target send one unit uniformly to its coatom supersets.  A target of rank
`s` has

\[
                         {k-s\choose r-1-s}
\]

such supersets.  A fixed coatom contains `binom(r-1,s)` rank-`s` targets,
so its incoming rank-`s` load is

\[
 { {r-1\choose s}\over {k-s\choose r-1-s}}
 ={ {k\choose s}\over {k\choose r-1}}
 ={ {k\choose s}\over W}.                                  \tag{3.2}
\]

The total load at a coatom is therefore `|P|/W<=1`.  This is a fractional
matching saturating `P`; bipartite matching integrality gives (3.1).

For every matched pair use the chain `{S,f(S)}`.  Every unmatched coatom is
a singleton chain.  These chains partition the lower ideal and have the
required distinct coatom maxima.  \(\square\)

The same proof handles every residual subfamily of `P`: simply restrict
the integral matching supplied for the complete `P`.

When `d=2` and `h>0`, the residual noncoatom bank has exactly `W` members,
so Theorem 1.1 reduces exactly to a perfect matching.

### Theorem 3.2 (active depth-two min-cut)

Let

\[
                 \mathcal P_{\mathcal B}=\mathcal P\setminus\mathcal B.
\]

An exact depth-two coatom-rooted partition exists if and only if

\[
 |N_{\mathcal Q}(X)|\ge |X|
             \qquad(X\subseteq\mathcal P_{\mathcal B}).       \tag{3.3}
\]

Equivalently, the unit-capacity network

\[
 s\longrightarrow\mathcal P_{\mathcal B}
   \longrightarrow\mathcal Q\longrightarrow t               \tag{3.4}
\]

has value `W`.

#### Proof

Every colour already contains its coatom and has room for exactly one
further target.  Thus a partition is precisely a perfect containment
matching from `P_B` to `Q`.  Hall's theorem and max-flow/min-cut give
(3.3)--(3.4).  \(\square\)

The quotient `Lambda/W` is strictly increasing with odd `k`: if
`k=2m+1`, then

\[
 {4^{m+1}-1\over {2m+3\choose m+1}}
 >{4^m-1\over {2m+1\choose m}}.                              \tag{3.5}
\]

Indeed,

\[
 {{2m+3\choose m+1}\over {2m+1\choose m}}
 =4-{2\over m+2}<4
 <{4^{m+1}-1\over4^m-1}.
\]

Direct evaluation at `k=3,5,7,9,11` therefore shows that the only odd
active-boundary depth-two case is

\[
                         k=9,\qquad d=2,\qquad h=3.            \tag{3.6}
\]

For the canonical left-filled Ferrers prefix one may take, after relabelling,

\[
                         \mathcal B=\{\{0\},\{1\},\{0,1\}\}.
                                                               \tag{3.7}
\]

A bounded independent Hopcroft--Karp audit of (3.4) finds a perfect
matching of all `126` residual targets.  This finite audit is not used in
any all-dimensional claim; Theorem 3.2 is the proof-level reduction.

## 4. The active boundary is an equal-chain critical face

Assume now `h>0` and an exact depth-`d` coatom-rooted partition
`(C_Q:Q in Q)` of `R` exists.

### Theorem 4.1 (saturation and full-lattice near-tiling)

Every `C_Q` has size exactly `d`.  Moreover, the full Boolean lattice has
`W` pairwise disjoint chains of size exactly `2d` which cover every set
except

\[
                  \mathcal B\ \dot\cup\
                  \{[k]\setminus S:S\in\mathcal B\}\ \dot\cup\
                  \{\varnothing,[k]\}.                       \tag{4.1}
\]

Thus precisely `2h+2` vertices are left outside the equal-chain family.

#### Proof

Since `h=Lambda-dW>0`,

\[
                         |\mathcal R|=\Lambda-h=dW.            \tag{4.2}
\]

There are `W` chains, each of size at most `d`, and together they cover
`dW` targets.  Hence every chain has size exactly `d`.

Make the bipartite graph between two copies of `Q`, joining `Q` to `Q'`
when `Q\cap Q'=\varnothing`.  It is `r`-regular: the complement of an
`(r-1)`-set has size `r`, and `Q'` is obtained by deleting one of its
elements.  It therefore has a perfect matching; write its bijection as
`f`.

For every `Q`, concatenate

\[
              C_Q\quad\text{with}\quad
              \{[k]\setminus S:S\in C_{f(Q)}\}               \tag{4.3}
\]

in reverse order on the second half.  The greatest member of `C_Q` is `Q`.
The least member of the complemented half is `[k]\setminus f(Q)`, which
contains `Q` because `Q\cap f(Q)=\varnothing`.  Thus (4.3) is a chain of size
`2d`.

The lower halves partition `R`, and the complemented halves partition
the complements of `R`.  These shores are disjoint in odd dimension.
Their complement in the full Boolean lattice is exactly (4.1).  \(\square\)

On the zero-boundary face, the same argument with chains of size at most
`q` gives a minimum `W`-chain decomposition of the full lattice with maximum
at most `2q+2` after the two extrema are attached.  Thus a uniform
`q=d+C` theorem would imply maximum chain length less than the average plus
`2C+4`, on an infinite prime subsequence by Corollary 2.3.  This is a strong
one-sided form of the uniform-chain programme, not a routine consequence
of normalized matching.

## 5. Exact frontier

The static odd one-copy row is now separated as follows.

\[
\boxed{
\begin{array}{c}
\text{zero-boundary depth }2:\ \text{proved by one matching},\\
\text{active depth }2:\ \text{one exact min-cut (only }k=9\text{)},\\
\text{general }d\ge3:\ \text{precoloured bounded colouring of a}\
\text{specific Boolean co-comparability graph},\\
\text{literal moving-core spelling and upper rows}:\ \text{still separate}.
\end{array}}
\]

The arithmetic split matters conceptually.

* When `h=0`, there is unused owner capacity but no boundary absorber.
  This is the generic phase and includes every odd prime dimension.
* When `h>0`, deleting the boundary targets leaves no owner slack at all;
  every colour class must be saturated.  An exact factor would already
  create the critical equal-chain near-tiling of Theorem 4.1.

Accordingly, future sharp work should not treat the Ferrers bank as the
source of the static integrality difficulty.  The remaining theorem is a
Boolean-specific capacitated precolouring extension (or an equivalent
global cross-SCD exchange theorem) at `d>=3`.

## References

* F. Bonomo, S. Mattia and G. Oriolo, *Bounded coloring of
  co-comparability graphs and the pickup and delivery tour combination
  problem*, Theoretical Computer Science **412** (2011), 6261--6268,
  doi:10.1016/j.tcs.2011.07.012.
* B. Sudakov, I. Tomon and A. Z. Wagner, *Uniform chain decompositions and
  applications*, Random Structures & Algorithms **60** (2022), 261--286.
