# Closed-set Hall normal form for a random Catalan omission bank

**Date:** 2026-08-07  
**Method:** Hall complementation and exact biregular incidence counting  
**Status:** unconditional reduction for the first perfect matching.  It
identifies the precise random lower-tail event and the missing near-equality
cut-counting theorem.  It does not prove that a random omission bank passes
all cuts or that two edge-disjoint perfect matchings exist.

## 1. Setup

Let `|Omega|=2m` and

\[
 \mathcal B={\Omega\choose m-1},\qquad
 \mathcal U={\Omega\choose m},
\]

\[
 W=|\mathcal U|,qquad C={W\over m+1},qquad
 V=|\mathcal B|=W-C=mC.
\]

Let `O subset U` have order `C`, put `R=U\O`, and let `G_O` be the
balanced containment graph `B <-> R`.

For `T subseteq B`, define its closed upper interior

\[
 Z(T)=\{U\in\mathcal U:\partial^-U\subseteq T\},     \tag{1.1}
\]

and its defect demand

\[
 d(T)=|Z(T)|-|T|.                                    \tag{1.2}
\]

## 2. Exact Hall equivalence

### Theorem 2.1

`G_O` has a perfect matching if and only if

\[
 \boxed{
 |\mathcal O\cap Z(T)|\ge d(T)
 \quad\text{for every }T\subseteq\mathcal B.}        \tag{2.1}
\]

Cuts with `d(T)<=0` are automatic.

#### Proof

For `A subseteq B`, put `T=B\A`.  A retained upper set has no neighbour in
`A` exactly when all its facets lie in `T`.  Hence

\[
 R\setminus N_{G_O}(A)=R\cap Z(T).
\]

Since `|R|=|B|=V`, Hall's inequality `|N(A)|>=|A|` is equivalent to

\[
 |R\cap Z(T)|\le|T|.
\]

Using `R=U\O` gives (2.1). \(\square\)

Thus the omission bank is a base of the dual transversal matroid exactly
when it pays every closed-set defect (1.2).

## 3. The threshold is never above its sampling mean

Put `z=|Z(T)|` and `t=|T|`.  Every member of `Z(T)` has all `m` facets in
`T`, while a facet lies below at most `m+1` rank-`m` sets.  Therefore

\[
                         mz\le(m+1)t.                \tag{3.1}
\]

Equivalently,

\[
 \boxed{
 d(T)=z-t\le {z\over m+1}.}                          \tag{3.2}
\]

If `O` is a uniformly random `C`-subset of `U`, then

\[
 \mathbb E|O\cap Z(T)|={Cz\over W}={z\over m+1}.     \tag{3.3}
\]

So every Hall failure is a lower deviation below a threshold no larger
than the exact mean.

The equality case in (3.1) is rigid.  Equality says that every facet in
`T` uses all its `m+1` upper neighbours inside `Z(T)`.  Since by definition
every member of `Z(T)` uses all its facets in `T`, the pair `(T,Z(T))` is
a union of connected components of the full incidence graph
`B <-> U`.  That graph is connected.  Hence equality occurs only at the
empty pair or at

\[
                         T=B,\qquad Z(T)=U.           \tag{3.4}
\]

At the full pair, `d(T)=C` and `|O cap Z(T)|=C`
deterministically, so it is not a strict Hall failure.

For every nontrivial positive cut the integer slack

\[
 s(T)=z-(m+1)d(T)=(m+1)t-mz                         \tag{3.5}
\]

is therefore at least one.  Its mean-minus-threshold gap is exactly
`s(T)/(m+1)`.

## 4. Exact random event and missing counting lemma

For fixed `T`, under uniform `C`-subset sampling,

\[
 |O\cap Z(T)|\sim\operatorname {Hypergeom}(W,z,C),  \tag{4.1}
\]

and its Hall-failure probability is exactly

\[
 \Pr\left[
  \operatorname {Hypergeom}(W,z,C)<z-t
 \right].                                           \tag{4.2}

The first-matching problem for a random omission bank is consequently
reduced to the following pure Boolean cut statement.

> **Near-equality closed-set counting lemma.**  The number of distinct
> closed pairs `(T,Z(T))` with a given small slack `s(T)` is sufficiently
> small that the hypergeometric lower tails (4.2) are summable.

This is the exact analogue of a Karger near-minimum-cut enumeration.  Raw
union bound over all `2^V` facet families cannot work, and local maximum
omission degree does not encode the slack (3.5).

## 5. Relation to the hinge bank and scope

The private-hinge theorem constructs an omission bank with two-sided
exposure `o(m)`, but its hypergeometric sampling occurs inside one private
catalogue matching, not uniformly over all `C`-subsets of `U`.  Therefore
(4.1) cannot be applied to that bank without an additional domination or
prospective coupling theorem.

Conversely, forcing `O` to be a common/dual transversal basis makes (2.1)
automatic, but the existing uniform common-basis marginal theorem does not
give negative dependence or star-load concentration; the abstract
parallel-`C6` no-go theorem rules out that inference in general.

Even after (2.1) is proved, an integral coloured two-factor needs a second
edge-disjoint perfect matching with intersection-colour surjection, and a
Hamilton cycle needs connectedness.  This note closes none of those later
rows.  It isolates the first exact all-cut lemma for the random balanced
host route.

