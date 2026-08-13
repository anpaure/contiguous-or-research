# A global singleton-provider bank with linear owner cost and exact owner/q1 extension

**Date:** 2026-08-13  
**Method:** far-core packing, central period-`2q+1` resident rails, and
protected Ore--Ryser completion  
**Status:** proved at the owner/immediate-lower incidence level.  Every
singleton target has a literal provider in one protected bank, and that bank
extends to an exact spanning owner/q1 two-factor.  The arbitrary residual
two-factor is not yet proved to carry the full-aperture resident antecedents;
that compatibility is stated explicitly as the remaining chronology gate.

## 1. Setting

Put

\[
 n=2M-1,\qquad \mathcal L=\binom{[n]}{M-1},\qquad
 \mathcal U=\binom{[n]}M.
\tag{1.1}
\]

Fix `q>=4`, put

\[
 r=2q+1,\qquad c=M-q,
\tag{1.2}
\]

and assume

\[
 c\ge4.
\tag{1.3}
\]

as holds in the intended diagonal regime `q=Theta(sqrt M)` (with the
constant in the present application).  A **minimal central rail** consists
of a core `C`, `|C|=c`, a disjoint cyclically ordered toggle set
`T=(z_0,...,z_(r-1))`, and source letters

\[
 P_i=C\cup\{z_i\}.
\tag{1.4}
\]

Its owner and immediate-lower rows are

\[
 O_i=C\cup\{z_i,\ldots,z_{i+q-1}\}\in\mathcal U,
 \qquad
 L_i=C\cup\{z_i,\ldots,z_{i+q-2}\}\in\mathcal L.
\tag{1.5}
\]

The alternating sequence

\[
 O_0,L_1,O_1,L_2,\ldots,O_{r-1},L_0,O_0
\tag{1.6}
\]

is a simple incidence cycle.  The toggle trace is `1^q0^(q+1)`, so both
positive and zero runs have length at least `q`.

## 2. Guarded caps supply many toggle singletons simultaneously

### Lemma 2.1 (guarded literal singleton caps)

Let `A` be a set of active source positions such that every cyclic interval
of `q-1` positions contains a guard in `[r] setminus A`.  Simultaneously
cap every active source position `i` to the literal letter `{z_i}` and
leave every guard position maximal.  Then every active one-position cell
has OR exactly `{z_i}`, and every window union of length at least `q-1`
is unchanged.  In particular, the immediate-lower, owner, and
immediate-upper rows are all preserved.

#### Proof

At an active position `i`, the emitted letter is literally `{z_i}`.  Every
`(q-1)`-window contains a maximal guard letter and therefore still contains
the whole core `C`.  Its toggle incidence is unchanged, because both a
capped and a maximal letter at position `i` contain `z_i`.  Hence its union
remains `L_j`.  Every longer window contains a `(q-1)`-subwindow and
therefore also contains a guard; the same argument preserves its maximal
union.  \(\square\)

This is precisely why the singleton obstruction of a full-aperture rail is
not an obstruction inside a guarded minimal-aperture reserve rail.  The
guard hypothesis is essential: capping all positions would erase the core.

## 3. Far-core packing

Put

\[
 h=r-3=2q-2,
 \qquad G=\left\lceil {n\over h}\right\rceil.
\tag{3.1}
\]

Partition `[n]` into active label blocks `A_1,...,A_G` of size at most `h`.
For each `j`, enlarge `A_j` with distinct filler labels to an `r`-set
`T_j`.  Order `T_j` cyclically so that the active positions have no run
longer than `q-2`.  This is possible because there are at least three
guards and

\[
 h=2q-2\le3(q-2)\qquad(q\ge4).
\tag{3.2}
\]

Thus every cyclic `(q-1)`-window contains a guard.

For equal-size sets, write

\[
 d_J(C,C')=|C\setminus C'|=|C'\setminus C|
\tag{3.3}
\]

for Johnson distance.  The number of `c`-sets at distance at most `q+1` from
one fixed `c`-set is at most

\[
 B_{q+1}(n,c)=\sum_{s=0}^{q+1}\binom cs\binom{n-c}s.
\tag{3.4}
\]

### Lemma 3.1 (far cores)

If

\[
 (G-1)B_{q+1}(n,c)<\binom{n-r}{c},
\tag{3.5}
\]

then there are cores `C_1,...,C_G` such that

\[
 |C_j|=c,\qquad C_j\cap T_j=\varnothing,
 \qquad d_J(C_i,C_j)>q+1\quad(i\ne j).
\tag{3.6}
\]

Condition `(3.5)` holds for all sufficiently large parameters whenever

\[
 q=o\!\left({c\over\log n}\right).
\tag{3.7}
\]

In particular it holds in the intended regime `q=Theta(sqrt M)`.

#### Proof

Choose the cores greedily.  At step `j`, there are exactly
`binom(n-r,c)` candidates disjoint from `T_j`.  Each earlier core excludes
at most the full Johnson ball `(3.4)`, so `(3.5)` leaves a candidate.

For the asymptotic statement,

\[
 \log B_{q+1}(n,c)=O\!\left(q\log{n\over q}\right)=o(c),
\tag{3.8}
\]

whereas `n-r=2c-2` and hence

\[
 \log\binom{n-r}{c}=\Theta(c).
\tag{3.9}
\]

Also `log G=O(log n)`.  Thus `(3.5)` eventually holds.  \(\square\)

Take the `G` minimal rails `(C_j,T_j)`.

### Lemma 3.2 (global disjoint singleton bank)

Assume `(3.5)`.  These `G` rails are pairwise owner-disjoint, pairwise
immediate-lower-palette-disjoint, and pairwise immediate-upper-palette-
disjoint.  Their guarded simultaneous caps provide every singleton `{x}`,
while preserving all three protected rows.  The bank uses

\[
 Gr<{nr\over r-3}+r
    =n+{3n\over r-3}+r
\tag{3.11}

owners and the same number of immediate-lower vertices.

#### Proof

If an owner belonged to rails `i` and `j`, that rank-`M=c+q` set would
contain both `C_i` and `C_j`.  Hence

\[
 |C_i\cup C_j|=c+d_J(C_i,C_j)\le c+q=M,
\tag{3.10}
\]

contrary to `(3.6)`.  If an immediate-lower vertex belonged to both rails,
the same argument would give `c+d_J(C_i,C_j)<=M-1`, an even stronger
contradiction.  A shared immediate-upper vertex would give
`c+d_J(C_i,C_j)<=M+1=c+q+1`, again contradicting `(3.6)`.  Thus all three
palettes are disjoint.

The active blocks partition `[n]`, so Lemma 2.1 supplies every singleton
exactly once as a designated active cap.  The owner count follows from
`G=ceil(n/(r-3))`.  \(\square\)

The important scale is therefore

\[
 \#\text{cycles}=O(n/q),\qquad
 \#\text{protected owners}=n+O(n/q+q),\qquad
 \#\text{unprovided singletons}=0.
\tag{3.12}

## 4. Exact owner/q1 completion

Let `P` be the union of the alternating incidence cycles of Lemma 3.2 and
put `e=|E(P)|=2rG`.

### Lemma 4.1 (exposure bounds)

For every lower vertex `x` and every owner `A`,

\[
 \ell_P(x)\le2G,
 \qquad
 z_A:=|N(A)\cap Z|\le2G,
\tag{4.1}
\]

where `Z` is the protected lower palette.

#### Proof

In one rail, two owner windows at cyclic starting distance `s` have Johnson
distance `min(s,r-s)` for distances at most `q`.  Hence a rank-`M-1` set,
whose rank-`M` supersets form a clique in the Johnson graph, lies below at
most two rail owners.  This gives the first bound after summing over the
`G` rails.

Likewise, the protected lower vertices are the cyclic `(q-1)`-windows on
the toggle set, with the common core adjoined.  The members contained in a
fixed rank-`M` owner form a clique, while the cyclic interval family has
clique number at most two.  Thus one owner contains at most two protected
lower vertices from each rail, proving the second bound.  \(\square\)

### Theorem 4.2 (exact spanning incidence extension)

Assume, in addition, that

\[
 Q:={M(M-1)\over2M-1}\,e<\binom{M+3}{3},
\tag{4.2}
\]

and

\[
 2G<{M-2\over M-1}\left({M\over4}-1\right).
\tag{4.3}

\]

Then `P` extends to a spanning two-factor of the middle-levels incidence
graph on `mathcal L union mathcal U`.

In particular, `(4.2)--(4.3)` hold eventually when `q=Theta(sqrt M)`.

#### Proof

Use the exact protected Ore criterion

\[
 \lambda_P(A)\le\sigma(A)\qquad(A\subseteq\mathcal L).
\tag{4.4}

\]

The protected small/co-small localization theorem says that a failed shore
satisfies

\[
 \min\{|A|,W-|A|\}<Q.
\tag{4.5}

\]

On the small side, there are no protected path endpoints, so the exact
loss identity and Lemma 4.1 give

\[
 \lambda_P(A)\le\sum_{x\in A}\ell_P(x)\le2G|A|.
\tag{4.6}

\]

Write `a=|A|=binom{x}{M}` in the real-binomial convention.  Equations
`(4.2)` and `(4.5)` imply `x<M+3`.  Kruskal--Katona and the exact
shadow-slack inequality give

\[
 \sigma(A)
 \ge {M-2\over M-1}\bigl(|N(A)|-|A|\bigr)
 >{M-2\over M-1}\left({M\over4}-1\right)|A|.
\tag{4.7}

\]

By `(4.3)`, this is larger than `(4.6)`.

For the co-small side, complement inside the residual lower shore and take
an inclusion-minimal positive optional core `B^-`.  Its positive owner
family has size larger than `|B^-|`.  By `(4.1)`, every owner has optional
gap at least `M-2G`; residual capacity is at most two.  The partial-shadow
core theorem therefore forces each positive owner to contain at least

\[
 D=M-2G-1
\tag{4.8}

\]

members of `B^-`, and consequently

\[
 |B^-|\ge\binom{2D-1}{D-1}+1.
\tag{4.9}

\]

Here `G=O(M/q)=o(M)`, so `(4.9)` is exponential in `M`, whereas `(4.5)`
and `(4.2)` make the co-small core smaller than `Q=O(M^2)`.  This is a
contradiction.  No protected Ore cut fails, and bipartite `b`-matching
integrality supplies the spanning two-factor.  \(\square\)

## 5. What this does and does not close

Combining Lemma 3.2 and Theorem 4.2 proves, on one simultaneous object:

1. every owner and every immediate-lower target is used exactly once;
2. `n+O(n/q+q)=O(n)` owners lie in the singleton reserve;
3. every singleton target has a literal one-cell provider;
4. every reserve rail is a legal two-sided resident period-`2q+1` rail,
   with simple protected lower and upper palettes.

Thus singleton supply itself no longer requires `Theta(n)` separate owner
cycles or any terminal charge.  It costs `O(n/q)` cycles and `O(n)`
protected owners, with zero singleton defect.  The sparse guards ensure
that these claims hold simultaneously on one literal source word, rather
than only as incompatible one-at-a-time caps.

The theorem deliberately does **not** claim that the arbitrary residual
two-factor from protected Ore completion has a literal depth-`q` resident
source chronology.  In particular, it is not yet a switch theorem inserting
this bank into the exact full-aperture MSW factor while preserving the
full-aperture antecedents outside the bank.  The exact remaining gate is:

> trade the `O(n)` protected owner/lower incidences into the full-aperture
> MSW carrier, or construct a resident antecedent for the Ore-completed
> background, without changing the protected singleton rails.

This is a chronology/positive-semigroup compatibility problem, not an
owner-demand, immediate-lower-demand, singleton-capacity, or reserve-size
obstruction.
