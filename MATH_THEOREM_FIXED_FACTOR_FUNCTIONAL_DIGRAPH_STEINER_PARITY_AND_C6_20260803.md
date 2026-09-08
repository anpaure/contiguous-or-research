# Fixed-factor functional upper digraphs, the Steiner parity barrier, and Boolean `C6` exchanges

**Date:** 2026-08-03  
**Status:** unconditional exact reduction and scoped obstruction.  This note
does **not** prove the existence of a cap-two second perfect matching.

## 0. Statement

Let `m>=3`, put `n=2m-1`, and write

\[
 \mathcal L={ [n]\choose m-1},\qquad
 \mathcal M={ [n]\choose m},\qquad
 \mathcal U={ [n]\choose m+1}.
\]

Let `G` be the containment graph between `mathcal L` and `mathcal M`, fix a
perfect matching `F_0`, and put `H=G-F_0`.  For every `S in mathcal M`,
define its **root** `a(S) in S` by

\[
                         F_0^{-1}(S)=S-\{a(S)\}.             \tag{0.1}
\]

Contracting every edge of `F_0` turns `H` into an `(m-1)`-in-regular and
`(m-1)`-out-regular digraph `D_(F_0)` on `mathcal M`.  Its arcs are

\[
                 S\longrightarrow S-\{a(S)\}+\{b\},
                 \qquad b\notin S,                           \tag{0.2}
\]

and the upper colour of this arc is `R=S+{b}`.

For a fixed `R in mathcal U`, index its facets by

\[
                         S_b=R-\{b\}\qquad(b\in R).
\]

Then the complete upper-colour class is the loopless functional digraph

\[
                         p_R:b\longmapsto a(S_b)             \tag{0.3}
\]

on the `m+1` points of `R`.  In particular, every colour has one arc out
of every facet, but its head multiplicities can be arbitrary.

This gives two useful conclusions.

1.  The colour--tail and colour--head marginal SDRs always exist, by Hall,
    but they can use different occurrences.  The cap-two second-factor
    problem is precisely their occurrence-level correlation with a full
    cycle cover.
2.  The tempting strengthening that every `p_R` be a permutation is not a
    viable all-parameter route.  It forces, for every coordinate `x`, a
    Steiner system

    \[
                       S(m-2,m-1,2m-2),                      \tag{0.4}
    \]

    and is therefore impossible whenever `m` is even.  Under equal root
    loads the parity failure is quantitative: it forces a positive-density
    family of local head collisions.

Finally, the minimal literal exchanges left after fixing `F_0` are genuine
three-edge Boolean `C6` switches.  For every rank-`m-2` core there are at
least

\[
               {m+1\choose3}-(m+1)(m-1)
               ={(m+1)(m-1)(m-6)\over6}                     \tag{0.5}
\]

full `C6` supports when `m>=7`, and their exact upper-colour action is a
cubic cyclic reassignment recorded in Theorem 4.2 below.  This proves that
the three-colour gate has cubic local supply; it does not prove that one of
those switches decreases the global selector energy.

## 1. Contraction and the functional upper classes

### Theorem 1.1 (exact contracted digraph)

After identifying each `q in mathcal L` with `S=F_0(q)`, every edge of
`H` is uniquely the arc (0.2).  The resulting digraph has indegree and
outdegree `m-1` at every middle set.  Its upper-colour-`R` arcs are exactly

\[
             S_b\longrightarrow S_{p_R(b)},\qquad b\in R,   \tag{1.1}
\]

where `p_R` is (0.3); in particular `p_R(b) != b`.

#### Proof

Put `q=F_0^{-1}(S)=S-{a(S)}`.  The `m` neighbours of `q` are
`q+{x}`, `x notin q`.  The choice `x=a(S)` is the deleted matching edge
`qS`; the remaining choices have `x=b notin S` and give (0.2).

Deleting one perfect matching from the `m`-regular balanced bipartite graph
`G` leaves an `(m-1)`-regular graph, which proves both degree assertions
after contraction.

If the upper colour is `R`, then necessarily `S=S_b=R-{b}`.  Formula
(0.2) gives the head

\[
 S_b-\{a(S_b)\}+\{b\}=R-\{a(S_b)\}=S_{p_R(b)}.
\]

Since `a(S_b) in S_b`, it differs from `b`; hence there are no loops.
\(\square\)

### Corollary 1.2 (cycle-cover formulation)

A second perfect matching `F_1 subset H` is exactly a directed cycle cover
of `D_(F_0)`.  Its multiplicity at `R` is the number of selected arcs of
the functional digraph `p_R`.  Therefore `F_1` is upper-surjective and
cap-two exactly when that cycle cover selects one or two arcs from every
`p_R`.

This is an exact restatement, not a relaxation.  Connectedness of the
compressed owner chronology is the further requirement that the cycle
cover have one component.

## 2. The two marginal SDRs are automatic but do not couple

Let `B_tail` be the bipartite occurrence graph between `mathcal U` and a
tail copy of `mathcal M`, containing one edge `R--S` for each facet
`S subset R`.  Let `B_head` contain the same arc occurrences, but join
`R` to their heads `R-{a(S)}` instead.

### Proposition 2.1 (separate saturation)

Both `B_tail` and `B_head` have a matching saturating every vertex of
`mathcal U`.

#### Proof

In either occurrence multigraph every `R` has degree `m+1`.  Every middle
set has degree `m-1`: this is obvious for tails, and for heads it is the
indegree assertion of Theorem 1.1.  Thus for any `X subseteq mathcal U`,

\[
               (m+1)|X|\le (m-1)|N(X)|,
\]

where degrees count parallel occurrences.  Hence `|N(X)|>=|X|`, and Hall's
theorem applies.  Parallel occurrences do not affect the conclusion,
because a matching uses distinct vertices. \(\square\)

The proposition deliberately gives two possibly different occurrence
choices.  Requiring the same occurrence in the two matchings is exactly a
three-partite rainbow-matching correlation and is not implied by Hall on
the two projections.

## 3. Why the permutation shortcut forces Steiner systems

Call `F_0` **upper-permutational** when every map `p_R` is a permutation.

### Theorem 3.1 (Steiner reduction)

If `F_0` is upper-permutational, then for every coordinate `x in [n]` the
family

\[
 \mathcal B_x=\{[n]\setminus S:S\in\mathcal M,\ a(S)=x\}  \tag{3.1}
\]

is a Steiner system `S(m-2,m-1,2m-2)` on `[n]-{x}`.

Consequently no upper-permutational `F_0` exists when `m` is even.

#### Proof

The map `p_R` is injective exactly when the roots of the `m+1` facets of
`R` are pairwise distinct.  Every two adjacent vertices of the Johnson
graph `J(n,m)` are facets of their unique union `R`; hence
upper-permutationality is equivalent to

\[
        S\sim T\text{ in }J(n,m)\quad\Longrightarrow\quad
        a(S)\ne a(T).                                      \tag{3.2}
\]

Fix `x`.  Because `a(S)=x` implies `x in S`, every member of
`mathcal B_x` is an `(m-1)`-subset of the `(2m-2)`-set `[n]-{x}`.
Condition (3.2) says that two such blocks cannot share `m-2` points.

Count pairs `(R,S)` with `x in R`, `S subset R`, and `a(S)=x`.  Every
`R` containing `x` contributes exactly one pair because its facet roots
are a permutation of `R`.  Every fixed `S` rooted at `x` lies in exactly
`n-m=m-1` upper sets.  Therefore

\[
 |\mathcal B_x|
 ={ {2m-2\choose m}\over m-1}
 ={1\over m}{2m-2\choose m-1}
 =\operatorname {Cat}_{m-1}.                              \tag{3.3}
\]

Each block contains `m-1` subsets of size `m-2`, and

\[
 (m-1)|\mathcal B_x|={2m-2\choose m-2}.                   \tag{3.4}
\]

The nonintersection condition says that no `(m-2)`-set occurs twice;
(3.4) says that all of them occur.  This is precisely (0.4).

In an `S(m-2,m-1,2m-2)`, the number of blocks containing a fixed
`(m-3)`-set would be

\[
 { \binom{\,2m-2-(m-3)\,}{1}
    \over \binom{\,m-1-(m-3)\,}{1}}
 ={m+1\over2}.                                            \tag{3.5}
\]

This is not an integer for even `m`, proving the final assertion.
\(\square\)

Thus replacing each functional colour class by a local permutation is not
a harmless regularization.  It imports a high-strength Steiner-design
requirement before the second matching is even selected.  The obstruction
is scoped: the desired cap-two cycle cover does **not** require the maps
`p_R` to be permutations.

### Theorem 3.2 (quantitative even-`m` collision bound)

Let `m` be even, fix `x`, and suppose merely that the root load has the
balanced value

\[
             |\{S:a(S)=x\}|=\operatorname {Cat}_{m-1}.      \tag{3.6}
\]

For `Q in {[n]-{x}\choose m-2}`, put

\[
 d_Q=|\{B\in\mathcal B_x:Q\subset B\}|.
\]

Then the number of adjacent pairs of middle sets rooted at `x` is

\[
 \mathcal E_x:=\sum_Q {d_Q\choose2}
 \ge {1\over2(m+1)}{2m-2\choose m-2}.                     \tag{3.7}

Equivalently, summed over upper sets, the functional digraphs have at least
that many pairs of arcs whose two tails both have root label `x` and whose
common head is `R-{x}`.

#### Proof

Put `N={2m-2 choose m-2}`.  Equation (3.6) gives
`sum_Q d_Q=N`.  For every `(m-3)`-set `P`,

\[
       \sum_{Q\supset P}d_Q
       =2|\{B\in\mathcal B_x:P\subset B\}|                 \tag{3.8}
\]

is even.  But there are `m+1` sets `Q` containing `P`, an odd number.
Thus at least one such `Q` has `d_Q !=1`.

Let `Z` be the number of `Q` with `d_Q=0`, and `P_+` the number with
`d_Q>=2`.  Double-counting pairs `P subset Q` shows

\[
        (m-2)(Z+P_+)\ge {2m-2\choose m-3},
        \qquad Z+P_+\ge {N\over m+1}.                       \tag{3.9}
\]

Since `sum_Q(d_Q-1)=0`,

\[
              Z=\sum_{d_Q\ge2}(d_Q-1)\ge P_+.
\]

Therefore `Z>=N/(2(m+1))`, and

\[
 \mathcal E_x
 =\sum_{d_Q\ge2}{d_Q\choose2}
 \ge\sum_{d_Q\ge2}(d_Q-1)=Z,
\]

which is (3.7).  Two blocks counted at `Q` correspond to two adjacent
middle sets with unique union `R`; both roots equal `x`, so their arcs in
`p_R` have the same head. \(\square\)

In particular, an `x`-transitive or coordinate-transitive proposed first
factor cannot make the functional classes asymptotically permutation-like
at even `m` without paying the collision mass (3.7).

### Corollary 3.3 (global positive-density collision mass)

If `m` is even and every coordinate has the balanced root load (3.6), then

\[
                  \sum_{x\in[n]}\mathcal E_x
                  \ge {1\over2}|\mathcal U|.               \tag{3.10}
\]

Thus the phrase “positive-density collision family” is literal after
summing the root-labelled collision pairs.

#### Proof

Apply (3.7) for all `2m-1` coordinates and use

\[
 {2m-2\choose m-2}
 ={m+1\over2m-1}{2m-1\choose m-2}
 ={m+1\over2m-1}|\mathcal U|.
\]

The factors cancel to give (3.10). Each colliding arc pair has one common
root label, so the sum is the intended root-labelled collision
multiplicity. \(\square\)

## 4. The literal Boolean `C6` supply

Fix a core `C in {[n] choose m-2}` and put `A=[n]-C`, so `|A|=m+1`.
For `a in A`, define the fixed-point-free pointer `f_C(a) in A-{a}` by

\[
                   F_0(C+\{a\})=C+\{a,f_C(a)\}.             \tag{4.1}
\]

For distinct `a,b,c in A`, the associated Boolean hexagon is

\[
 C+a, C+ab, C+b, C+bc, C+c, C+ca, C+a.               \tag{4.2}
\]

### Theorem 4.1 (full-hexagon abundance)

The six edges in (4.2) all belong to `H=G-F_0` exactly when the triple
`{a,b,c}` contains no directed pointer edge of `f_C`, i.e.

\[
 f_C(a)\notin\{b,c\},\quad
 f_C(b)\notin\{a,c\},\quad
 f_C(c)\notin\{a,b\}.                                    \tag{4.3}
\]

For every core `C`, the number of such triples is at least the quantity in
(0.5).  In particular it is positive for every `m>=7`.

#### Proof

At the lower vertex `C+a`, the unique deleted `F_0` edge goes to
`C+a+f_C(a)`.  The two hexagon edges go to `C+a+b` and `C+a+c`; hence both
survive exactly under the first condition in (4.3), and similarly at the
other two lower vertices.

There are `binom(m+1,3)` triples.  Each of the `m+1` directed pointer
edges `a -> f_C(a)` belongs to exactly `m-1` triples.  A union bound on the
bad triples proves (0.5). \(\square\)

### Theorem 4.2 (exact cubic reassignment)

Assume (4.3), and abbreviate `x_a=f_C(a)`, etc.  If a second perfect
matching contains the alternating phase

\[
       (C+a,C+ab),\quad(C+b,C+bc),\quad(C+c,C+ca),           \tag{4.4}
\]

then switching around the hexagon replaces it by

\[
       (C+a,C+ac),\quad(C+b,C+ab),\quad(C+c,C+bc).           \tag{4.5}
\]

The old upper-colour multiset is

\[
 \{C+ab+x_a, C+bc+x_b, C+ac+x_c\},                       \tag{4.6}
\]

and the new upper-colour multiset is

\[
 \{C+ac+x_a, C+ab+x_b, C+bc+x_c\}.                       \tag{4.7}
\]

Thus the minimal matching exchange is exactly a cubic cyclic reassignment
of three active labels among three fixed pointer contexts.

#### Proof

The matching switch is the usual exchange between the two alternating
perfect matchings of a `C6`.  For example, the upper colour of
`(C+a,C+ab)` is

\[
 F_0(C+a)\cup(C+ab)=(C+a+x_a)\cup(C+ab)=C+ab+x_a.
\]

The other five identities are identical. \(\square\)

Theorem 4.1 supplies cubically many **potential** local moves per core.
A move is applicable only when the incumbent second matching contains one
of its alternating phases, and (4.6)--(4.7) need not decrease the convex
upper-collision energy.  Accordingly these theorems prove the correct move
scale and its exact action, not a descent theorem.

## 5. Sharpened remaining statement

The fixed-factor selector is now separated into three exact layers.

1.  **Marginals:** colour--tail and colour--head SDRs are automatic
    (Proposition 2.1).
2.  **Correlation:** choose the same arc occurrences so that the selected
    arcs form a full cycle cover and use every functional class `p_R` once
    or twice.
3.  **Topology:** join that cycle cover to one component if required.

Neither making all `p_R` permutations nor applying the two marginal Hall
theorems closes layer 2.  At even `m`, the former shortcut is ruled out by
Theorem 3.1; the genuine local generators that can change layer 2 are the
three-edge reassignments of Theorem 4.2.

The remaining positive theorem can therefore be stated cleanly as follows.

> **Functional-colour cycle-cover theorem.**  For some perfect matching
> `F_0` (or, more strongly, for every `F_0`), the regular digraph
> `D_(F_0)` has a directed cycle cover containing one or two arcs from every
> functional colour class `p_R`.

This theorem is exactly equivalent to the cap-two second-perfect-matching
gate.  Nothing in this note asserts it.
