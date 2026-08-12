# Protected simple Catalan targets and row-fixed Ryser transport

**Date:** 2026-08-03  
**Status:** unconditional abstract palette theorem and exact reduction to an
occurrence-addressed selector.  No finite search, asymptotic matching theorem,
or literal `C6/C8` lift is used.

## 0. Result and scope

Put

\[
 v=2m-1,\qquad k=m+1,\qquad
 W={v\choose m},\qquad U={v\choose k},\qquad
 C=W-U=\operatorname {Cat}_m .                       \tag{0.1}
\]

For every `m>=3` there is a **simple** family

\[
 {\cal D}\subseteq { [v]\choose k},\qquad |{\cal D}|=C,       \tag{0.2}
\]

in which every coordinate occurs exactly

\[
                    \lambda=2\operatorname {Cat}_{m-1}       \tag{0.3}
\]

times.  Consequently `1+1_D` is an upper-surjective Catalan
palette with multiplicity exactly one or two and with the exact coordinate
current of every union of two edge-disjoint perfect middle-levels matchings.

More strongly, if `F` is any protected upper-colour bank satisfying

\[
                         |F|<{m-1\over2},                     \tag{0.4}
\]

then `D` can be chosen disjoint from `F`.  Thus every protected colour is
unique in the target palette.

If an initial two-matching factor has occurrence-labelled protected rows
whose distinct colours are `F`, abstract Ryser switching carries its labelled
palette to `1+1_D` while fixing every protected row throughout.  The switches
act only on unprotected row labels.  The terminal target contains no duplicate
protected colour; intermediate unprotected rows are not asserted to avoid
the same colour values.

This removes three abstract obstructions at once: existence of a balanced
duplicate target, multiplicity congestion, and preservation of a fixed
`O(sqrt(m))` protected palette bank.  It does **not** choose literal
tail/head occurrences, produce a Hamilton component, or construct the
capacity-faithful common-cap port map.  Section 5 states that remaining lift
exactly.

## 1. An elementary regular-simple-uniform lemma

### Lemma 1.1 (degree-balancing switch)

Let `0<=b<=binom(v,k)`.  There is a simple `k`-uniform hypergraph with `b`
edges whose vertex degrees differ by at most one.  If `v` divides `bk`, it
may be chosen regular of degree `bk/v`.

### Proof

Among all simple `k`-uniform `b`-edge families `H`, choose one minimizing

\[
                             \sum_{x=1}^v d_H(x)^2.             \tag{1.1}
\]

Suppose `d_H(x)>=d_H(y)+2`.  Put

\[
 \begin{aligned}
 A&=\{E\in H:x\in E,\ y\notin E\},\\
 B&=\{E\in H:y\in E,\ x\notin E\}.
 \end{aligned}                                                 \tag{1.2}
\]

Then

\[
                         |A|-|B|=d_H(x)-d_H(y)>0.               \tag{1.3}
\]

The map

\[
                         E\longmapsto E-x+y                     \tag{1.4}
\]

is injective from `A` into the complete family corresponding to `B`.  If
`E-x+y` belonged to `H` for every `E in A`, (1.4) would inject `A` into
`B`, contradicting (1.3).  Hence some `E in A` has `E-x+y notin H`.
Replace `E` by `E-x+y`.  Simplicity and edge count are preserved, while
the change in (1.1) is

\[
 (d_H(x)-1)^2+(d_H(y)+1)^2-d_H(x)^2-d_H(y)^2
 =2(d_H(y)-d_H(x)+1)<0,                                  \tag{1.5}
\]

a contradiction.  Thus all degrees differ by at most one.  If their average
`bk/v` is integral, they are all equal to it.  \(\square\)

This proof is worth retaining: it needs neither a cyclic-orbit divisibility
hypothesis nor a design-existence theorem.

## 2. A simple Catalan duplicate one-design in every parameter

### Theorem 2.1 (simple Catalan target)

For every `m>=3`, a family `D` satisfying (0.2)--(0.3) exists.

### Proof

First,

\[
 {U\over W}={m-1\over m+1},\qquad
 {C\over W}={2\over m+1},\qquad
 {C\over U}={2\over m-1}.                                \tag{2.1}
\]

The Catalan identity

\[
 {Ck\over v}
 ={\operatorname {Cat}_m(m+1)\over2m-1}
 =2\operatorname {Cat}_{m-1}=\lambda                  \tag{2.2}
\]

shows that `v` divides `Ck`.  Also `C<=U` for `m>=3`, with equality only at
`m=3`.  Apply Lemma 1.1 with `b=C`.  Its integral average is (2.2), so the
resulting simple family is regular of degree `lambda`.  \(\square\)

The target multiplicity vector

\[
                         \mu_R^*=1+\mathbf1_{R\in D}           \tag{2.3}
\]

therefore lies in `{1,2}` and has total mass

\[
                             U+C=W.                            \tag{2.4}
\]

For a coordinate `x`, the complete base layer contributes
`binom(2m-2,m)` rows and `D` contributes `lambda`.  If
`A=binom(2m-2,m-1)`, then

\[
 {2\operatorname {Cat}_{m-1}}={2A\over m},\qquad
 {2m-2\choose m}={m-1\over m}A,                         \tag{2.5}
\]

and hence

\[
 {2m-2\choose m}+2\operatorname {Cat}_{m-1}
 =2A-{2m-2\choose m-2}.                               \tag{2.6}
\]

The right side is exactly the coordinate current of two edge-disjoint
perfect middle-levels matchings.  Indeed, write the matchings as incidence
bijections `t,s:L->M`, where `L` and `M` are the rank-`(m-1)` and rank-`m`
shores.  Each coordinate occurs in

\[
                         A={2m-2\choose m-1}
\]

members of each image matching.  Edge-disjointness gives `t(q) ne s(q)`;
since both are rank-`m` supersets of the same `q in L`,

\[
                         t(q)\cap s(q)=q.
\]

The number of intersections containing a fixed coordinate is therefore
`binom(2m-2,m-2)`.  Inclusion--exclusion gives exactly the right side of
(2.6).  Thus (2.3) has the required full labelled matrix margins, not merely
the correct total number of rows.

## 3. Avoiding a protected colour bank

### Theorem 3.1 (exact protected-bank avoidance)

For every `F subseteq binom([v],k)` with `|F|<(m-1)/2`, the family `D` in
Theorem 2.1 may be chosen with

\[
                              D\cap F=\varnothing.              \tag{3.1}
\]

### Proof

Start with any simple regular `D_0` from Theorem 2.1 and choose a uniformly
random coordinate permutation `pi in S_v`.  For a fixed `E in D_0`, the
image `pi(E)` is uniform on the `U` upper colours.  Since a permutation maps
distinct blocks to distinct blocks,

\[
 \begin{aligned}
 \mathbb E|\pi(D_0)\cap F|
 &=\sum_{E\in D_0}\Pr(\pi(E)\in F)\\
 &={C|F|\over U}={2|F|\over m-1}<1,                    \tag{3.2}
 \end{aligned}
\]

where (2.1) was used in the last equality.  The random variable in (3.2) is
a nonnegative integer, so some permutation makes it zero.  Coordinate
permutation preserves simplicity and every degree.  Take
`D=pi(D_0)`.  \(\square\)

In particular, every protected bank of `O(sqrt(m))` distinct upper colours
is avoidable for all sufficiently large `m`.  Unlike the repeated cyclic
multidesign, this target never asks for more than two literal occurrences of
one colour; every colour fibre, which has `m+1` rooted occurrences, retains
raw multiplicity slack at least `m-1`.

## 4. Row-fixed abstract Ryser transport

Let the `W` turn occurrences of a union of two edge-disjoint perfect
middle-levels matchings be labelled.  Write its palette matrix as `A`: every
row is the zero-one incidence vector of its rank-`(m+1)` upper colour.

Let `I` be a set of protected row labels.  Assume their colours are pairwise
distinct and call their colour set `F`.  Let `D` be given by Theorem 3.1.
Form a target matrix `B` with row multiset `1+1_D`, assigning the unique copy
of each `R in F` to the same protected row label on which it occurs in `A`.
Assign all remaining target rows arbitrarily to the remaining labels.

### Theorem 4.1 (protected-row Ryser theorem)

The matrix `A` can be transformed to `B` by ordinary `2x2` row-coordinate
switches none of which uses a row in `I`.

### Proof

The matrices have the same row sums.  Equations (2.5)--(2.6) say that they
have the same column sums.  By construction,

\[
                              A_i=B_i\qquad(i\in I).             \tag{4.1}
\]

Delete the rows `I` from both matrices.  Subtracting the identical vectors
in (4.1) leaves equal residual column sums, and all residual row sums are
still `m+1`.  Apply the self-contained zero-one matrix interchange theorem,
Theorem 1.1 of
`MATH_THEOREM_CATALAN_DUPLICATE_CURRENT_RYSER_AND_PREPARED_C6_RADO_20260803.md`:
two zero-one matrices with equal labelled row and column sums are connected
by ordinary `2x2` switches.  Applied to the residual matrices, it produces a
switch sequence using only residual row labels.  Restore the untouched rows
`I`.  \(\square\)

### Corollary 4.2 (safe abstract opening interface)

At the terminal target, every protected colour has multiplicity one and
every duplicate colour lies outside `F`.  Hence, **at the projected
immediate-upper owner-edge level**, if a literal connected two-factor
realizing `B` and fixing the protected occurrences is supplied, deleting
any nonprotected occurrence of a duplicated colour opens its owner cycle
without losing immediate-upper coverage.

This is only an upper-safe opening statement; it does not price lower-q,
higher-width, residence, source, or literal-cut effects.  The qualifier
“literal connected two-factor” is essential.  Theorem 4.1 is
a labelled palette-matrix path.  A general `2x2` switch need not be a Boolean
`C6`; even after catalytic distance-two factorization, literal common turns,
owner addresses, and reserve occurrences must coexist.

## 5. The exact remaining occurrence-and-port lift

The theorem reduces the positive owner/q1 row to the following strictly
smaller object.

Fix `D` as above and make one actual token for every upper colour plus one
duplicate token for every colour in `D`.  A **protected cap-two addressed
selector** is a literal rooted occurrence set `Q` satisfying

\[
 \begin{aligned}
 d_Q(t)&=d_Q(h)=1 &&\text{for every tail/head copy},\\
 |Q\cap E_R|&=1+\mathbf1_{R\in D}&&\text{for every upper colour }R,\\
 P&\subseteq Q,&&
 \end{aligned}                                                  \tag{5.1}
\]

together with the required terminal omission/opening convention.  Every
member of `Q` retains its full physical record

\[
 (R,t,h,\text{owner/lower occurrence},\text{phase},
   \text{physical port address},\text{capacity identity}).       \tag{5.2}
\]

For the common-cap interface, the selected active port set `P_Q` must be a
capacity-faithful image of these occurrence records in one materialized cap
state and must satisfy, after deleting the fixed compensation linkage and
all prefix interiors,

\[
             r_{\Gamma_{\rm suf}^{\rm type}}(P_Q)=|P_Q|.         \tag{5.3}
\]

Alternatively one may supply the stronger private literal factor-router of
`MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`.
Equal mask values at different physical addresses remain different ports;
aliases of one physical cell share one capacity-one gate.

Finally the endpoint permutation of `Q` must be joined by a support-disjoint
neutral `C8` tree, or otherwise proved to have the required single-component
topology.  Thus the remaining theorem is exactly

\[
 \boxed{\text{cap-two occurrence selector}
       +\text{ capacity-faithful typed router}
       +\text{ neutral }C8\text{ tree}.}              \tag{5.4}
\]

It is not another palette/current theorem.  The present result proves that
the terminal palette in (5.4) may always be simple, balanced, protected-bank
avoiding, and reachable without changing any protected occurrence row.

## 6. What is and is not proved

Proved unconditionally:

1. a simple regular Catalan duplicate design for every `m>=3`;
2. avoidance of every protected colour bank of size `<(m-1)/2`;
3. an upper-surjective cap-two target with the exact two-matching current;
4. abstract labelled Ryser transport fixing all protected occurrence rows;
5. a duplicate edge outside the protected palette for a safe opening once a
   literal connected realization exists.

Not proved:

1. a perfect matching of the colour--tail--head occurrence hypergraph with
   the target multiplicities (5.1);
2. a literal factorization of the row-fixed Ryser path by simultaneously
   available Boolean `C6` hosts;
3. a capacity-faithful occurrence-to-port map or the rank condition (5.3);
4. a compatible neutral `C8` spanning tree; or
5. any all-width/residence/lower-compiler conclusion.

Accordingly this is a strict positive reduction of the owner/q1 gate, not a
claim that the owner/q1 selector or the full universal-word theorem is
complete.
