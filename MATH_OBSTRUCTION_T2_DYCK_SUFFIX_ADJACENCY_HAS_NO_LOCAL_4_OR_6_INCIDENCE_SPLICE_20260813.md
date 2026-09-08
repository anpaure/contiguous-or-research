# Adjacent Dyck suffixes do not give a local four- or six-incidence splice

**Date:** 2026-08-13  
**Status:** unconditional local obstruction and exact hexagon-current
formula.  The result excludes the direct adjacent-suffix Gray-edge splice
inside the constant-suffix part of the `T2` tensor.  It does not exclude a
longer alternating circuit using two or more prefix phases.

## 0. Outcome

Split the coordinate ground into a prefix ground and a suffix ground.  In
the constant-suffix part of a tensor path, an internal prefix owner has the
form

\[
                         A=P\sqcup U,                 \tag{0.1}
\]

and its two selected immediate-upper neighbours have the form

\[
                         Q^-\sqcup U,
 \qquad                  Q^+\sqcup U,                \tag{0.2}
\]

where `P` has prefix rank `p`, `Q^\pm` have prefix rank `p+1`, and
`U` has suffix rank `s`.  Thus the owner rank is `R=p+s`.

Let

\[
 U=K\sqcup\{x\},\qquad U'=K\sqcup\{y\},\qquad x\ne y, \tag{0.3}
\]

and put `B=P\sqcup U'`.  Although `A` and `B` are Johnson adjacent, their
unique common immediate-upper colour

\[
                         X=A\cup B
                          =P\sqcup K\sqcup\{x,y\}     \tag{0.4}
\]

is unselected at **both** `A` and `B` in the tensor factor.  Consequently:

* there is no four-incidence switch joining `A` and `B`;
* there is no alternating incidence hexagon containing both `A` and `B`;
* a Gray edge `U\leftrightarrow U'` cannot by itself cross-rethread the two
  corresponding internal prefix arcs while preserving the exact owner and
  immediate-upper ledgers.

The obstruction is local and independent of how the Dyck suffixes are
ordered.  A successful suffix coupling must use a longer alternating
circuit, necessarily involving at least four owners and some additional
prefix or suffix phase.

## 1. There is no incidence four-cycle

Let `\mathcal I_R` be the containment graph between rank `R` owners and
rank `R+1` immediate-upper colours.

### Lemma 1.1

Two distinct rank-`R` owners have at most one common neighbour in
`\mathcal I_R`.  Hence `\mathcal I_R` has no four-cycle.

#### Proof

If `S,T` have a common rank-`R+1` superset, then `|S\cup T|\le R+1`.
Since `S\ne T` and both have rank `R`, equality holds and the only common
rank-`R+1` superset is `S\cup T`.  Thus no two owners have two common
neighbours. \(\square\)

In particular, the usual two-by-two continuation swap cannot be performed
on `A,B`: the required `K_(2,2)` is absent.

## 2. Exact normal form and selection test for a hexagon

Every simple six-cycle in `\mathcal I_R` has, after adjoining a common
rank-`R-1` set `H`, the form

\[
\begin{array}{c|ccc}
\text{owners}&H+a&H+b&H+c\\
\text{colours}&H+ab&H+bc&H+ca,
\end{array}                                           \tag{2.1}
\]

with the evident cyclic containments.  Indeed, consecutive owners on the
six-cycle are Johnson adjacent; writing the first two as `H+a,H+b`, the
third common-neighbour conditions force the third to be `H+c`.

Let `F` be an exact incidence factor and write `\chi_F(e)` for its
incidence indicator.  The hexagon `(2.1)` is alternating if and only if,
at each of its three colour vertices, the two cycle incidences have
opposite indicators.  In particular, if two owners `S,T` occur
consecutively on an alternating hexagon, then

\[
 \boxed{
 \chi_F(S,S\cup T)+\chi_F(T,S\cup T)=1.}             \tag{2.2}
\]

This is both necessary and, together with the corresponding conditions at
the other two colours, sufficient.

### Lemma 2.1 (exact q2 current of a legal hexagon)

Orient `(2.1)` so that the removed incidences are

\[
 (H+a,H+ab),\quad(H+b,H+bc),\quad(H+c,H+ca),          \tag{2.3}
\]

and the inserted incidences are the other three cycle edges.  Let
`M_a,M_b,M_c` be the unchanged other selected immediate-upper mate at the
three owners.  The switch preserves every owner degree and every
immediate-upper degree, and its complete internal q2 current is

\[
\begin{aligned}
\Delta_2={}&
 [M_a\cup(H+ca)]-[M_a\cup(H+ab)]\\
 &+[M_b\cup(H+ab)]-[M_b\cup(H+bc)]\\
 &+[M_c\cup(H+bc)]-[M_c\cup(H+ca)].                 \tag{2.4}
\end{aligned}
\]

#### Proof

The alternating toggle removes and inserts one incidence at every cycle
vertex, proving owner and immediate-upper exactness.  At owner `H+a`, the
only changed q1 mate is `H+ab -> H+ca`, while `M_a` stays fixed, giving
the first difference in `(2.4)`.  The other two terms are identical.
\(\square\)

Thus even when a suffix hexagon exists, q1 exactness alone does not imply
q2 support preservation; equation `(2.4)` is the exact additional ledger.

## 3. The tensor obstruction

### Theorem 3.1 (no local adjacent-suffix hexagon at an internal prefix state)

Assume `(0.1)--(0.3)` and that `A,B` lie at the same internal prefix phase
of two constant-suffix tensor paths.  Then no alternating incidence
hexagon contains both `A` and `B`.

#### Proof

The selected neighbours at `A` are exactly the two colours in `(0.2)`.
Their prefix projection has rank `p+1` and their suffix projection is
exactly `U`.  By contrast, `X` from `(0.4)` has prefix projection `P` of
rank `p` and suffix projection `U\cup U'` of rank `s+1`.  Therefore
`X` is neither selected neighbour of `A`, and

\[
                         \chi_F(A,X)=0.              \tag{3.1}
\]

The same argument with `U'` gives

\[
                         \chi_F(B,X)=0.              \tag{3.2}
\]

By the three-owner normal form `(2.1)`, every pair of owner vertices on a
simple six-cycle is consecutive around that cycle.  Hence any six-cycle
containing `A,B` must use their unique common colour `X` between them.
Equations `(3.1)--(3.2)` contradict the alternating condition `(2.2)`.
\(\square\)

There is a dual failure at a literal selected suffix transition: if the
factor uses the complete incidence edge `A-X-B`, then both indicators in
`(2.2)` equal one instead of zero.  A local hexagon is possible only in a
**split** state in which exactly one of `A-X,B-X` is selected.  Neither the
constant-suffix internal prefix phase nor an untouched suffix edge has
that property.

## 4. Consequence for the `T2V` residence proposal

The six changed `T2` owners occur at internal positions of the five fixed
prefix paths.  After tensoring by a Dyck suffix `V`, every selected q1
neighbour at those positions retains the suffix projection `U(V)`.
Therefore Theorem 3.1 applies literally to corresponding changed owners
for every adjacent pair `U(V),U(V')`.

It follows that arranging the Dyck roots in a Johnson Gray cycle and
placing one independent four- or six-incidence splice on every Gray edge
cannot concatenate the short prefix-coordinate runs.  The first possible
escape is a longer alternating circuit which visits at least four owners
and changes an additional phase.  The natural candidate is the
octahedral `1100 <-> 1010` two-row rectangle, but its exterior q2 current
must still be checked by `(2.4)` or its longer-circuit analogue.

This note does not obstruct such a rectangle, a coordinated pair of
rectangles, or a non-fixed-phase Chung--Feller rewire.
