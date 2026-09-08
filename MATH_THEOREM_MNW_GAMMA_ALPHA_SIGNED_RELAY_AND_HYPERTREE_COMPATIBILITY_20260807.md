# A signed MNW gamma-alpha relay inside one spanning hypertree

**Date:** 2026-08-07  
**Method:** exact q2 currents, inverse multiplicities, and a one-connector
modification of the published MNW recursion; no computation or search  
**Status:** unconditional.  A Catalan cylinder of mirror-gamma holes can be
transported without collateral support loss inside one conflict-free
spanning hypertree.  The relay moves, rather than annihilates, one unit hole.

## 1. The two currents telescope

The mirror-gamma current is

\[
\begin{aligned}
 \partial_2(1\operatorname{revcomp}(\gamma)0)
={}&+[1110101101]+[1011011101]\\
   &-[1110011101]-[1011101101].                      \tag{1.1}
\end{aligned}
\]

The ordinary alpha pattern with internal Dyck word `1100` has current

\[
 \partial_2\alpha(1100)
   =[1110011101]-[1110011110].                        \tag{1.2}
\]

Indeed, the general alpha current is

\[
                  [1w11101]-[1w11110],               \tag{1.3}
\]

and substitution of `w=1100` gives (1.2).  Adding (1.1) and (1.2) cancels
the intermediate target exactly:

\[
 \boxed{
 +[1110101101]+[1011011101]
 -[1011101101]-[1110011110].}                        \tag{1.4}
\]

## 2. Exact canonical multiplicities

Write

\[
\begin{array}{c|c|c}
\text{name}&\text{target}&\text{canonical multiplicity}\\ \hline
H&1110101101&0,\\
G&1011011101&1,\\
C&1110011101&1,\\
D&1011101101&1,\\
L&1110011110&2.
\end{array}                                                   \tag{2.1}
\]

These values follow from the exact height/corridor/ordinal inverse test.
For transparency, the witnesses are:

* `G`: `(p,q)=(6,7)`, and no other pair;
* `C`: `(6,8)`, and no other pair;
* `D`: `(4,5)`, and no other pair;
* `L`: exactly `(2,3)` and `(6,7)`.

The candidate-pair exhaustion for `H` is the mirror-gamma absence proof.

Applying the two tuples in order changes the five loads as

\[
\begin{array}{c|ccccc}
 &H&G&C&D&L\\ \hline
\text{canonical}&0&1&1&1&2\\
\text{after mirror gamma}&1&2&0&0&2\\
\text{after alpha(1100)}&1&2&1&0&1.
\end{array}                                                   \tag{2.2}
\]

Thus the pair transports the unique hole from `H` to `D`; every other old
target remains represented.  It is an exact signed relay, not a defect
reduction.

Every word in (2.1) ends at height four.  Appending a Dyck suffix `v`
preserves all five multiplicities and appends `v` to (1.4).

## 3. The two tuples are locally compatible

The mirror-gamma tuple and `alpha(1100)` share exactly one Dyck root,

\[
                         A=1110011000.                \tag{3.1}
\]

At this root, gamma's marked edge has position two before wrapping and
therefore position three after wrapping.  The first-root alpha edge in the
published path display has position five, independently of its internal
Dyck word.  Hence the selected edge positions are three and five.  They are
not consecutive and produce no compound correction.

Their other roots are distinct.  The two tuple nodes and their five support
roots therefore form an incidence tree.  In particular the pair is a
conflict-free hyperforest and its signed current is exactly the sum (1.4).

## 4. A connector substitution in the published recursion

The standard construction of `F_(m,5)` partitions each suffix fibre into

\[
 F_{m,4},
 \qquad
 1\operatorname{revcomp}(E_4)0v,
 \qquad
 1\operatorname{revcomp}(F_4)0v,                     \tag{4.1}
\]

and joins these three already-spanned blocks with `alpha(1010)v`.

The three roots of `alpha(1100)` are

\[
\begin{aligned}
A&=1110011000,\\
B&=1110010100,\\
C_0&=1110010010.                                     \tag{4.2}
\end{aligned}
\]

They lie one per block of (4.1):

1. deleting the outer wrapper from `A` gives `11001100 in F_4`;
2. deleting it from `B` gives `10101100 in E_4=10D_3`;
3. `C_0` has first-return decomposition
   `1 revcomp(101100) 0 10`, so `C_0 in F_(5,4)`.

Suffixing by `v` preserves these memberships.  Therefore
`alpha(1100)v` may replace `alpha(1010)v` as the connector of the same
three blocks.  The recursive spanning-tree proof is unchanged.

The standard tree on `F_4` contains `gamma`.  Consequently the third block
in (4.1) contains

\[
                  (1\operatorname{revcomp}(\gamma)0)v. \tag{4.3}
\]

The connector substitution therefore places both relay tuples in one
spanning tree.

### Theorem 4.1 (hypertree-compatible relay cylinder)

For every `m>=5`, there is a conflict-free MNW spanning tree `T_m^relay`
which, for every `v in D_(m-5)`, contains both tuples

\[
(1\operatorname{revcomp}(\gamma)0)v,
\qquad
\alpha(1100)v.                                       \tag{4.4}
\]

Their supports for different `v` are disjoint.  Simultaneously over the
whole suffix bank, the canonical holes

\[
                         1110101101v                 \tag{4.5}

are filled and exactly the targets

\[
                         1011101101v                 \tag{4.6}

become uncovered; no other canonical target is lost by these relay pairs.

#### Proof

Use `alpha(1100)v` instead of the original connector independently in every
suffix fibre of `F_(m,5)`, and retain the standard spanning trees in the
three blocks.  The membership calculation above proves that each connector
still joins precisely those three components, hence the result is a
spanning tree.  MNW conflict-freeness applies to every selected tree.

The wrapped standard `F_4` block supplies (4.3).  Section 3 rules out an
interaction correction within each relay pair, while suffix projection
separates distinct fibres.  Equations (1.4) and (2.2) prove the support
statement. \(\square\)

## 5. Exact remaining relay target

The entire first relay problem has therefore collapsed to one cylinder:

\[
                         \boxed{1011101101v}.         \tag{5.1}

The prefix is `10` followed by the classical semilength-four hole
`11101101`, but it has canonical multiplicity one rather than zero.  A
second relay must restore this occurrence while terminating at a
multiplicity-at-least-two provider.

Neither the base mirror currents nor `alpha(w)` at semilength five has
positive term (5.1).  Thus the next step must use a different nontrivial
context, a compound rectangle, or a longer signed macro.  The important
gain is that topology and simultaneous suffix compatibility no longer form
part of this first-stage gate.

