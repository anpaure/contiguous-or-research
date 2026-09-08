# Exact two-rail topology after the rigid PBBS split

**Date:** 2026-08-05  
**Method:** cut-edge permutation calculus; no computation or search  
**Status:** unconditional.  The rigid q2-neutral C6 followed by one
three-component connector on each two-soliton arc produces exactly two
hybrid cycles.  Further C6s using no external component cannot join those
two cycles.  This identifies the correct dynamic object as a two-rail
forest, not a one-cycle merger.

## 1. Cut-permutation convention

Remove a collection of directed factor edges.  Label each removed edge by
`e`, with tail `P_e` and head `Q_e`.  Let `sigma(e)` be the label of the
next removed edge encountered after starting at `Q_e` and following the old
factor.  The cycles of `sigma` are exactly the old factor components met by
the cuts.

A clean C6 reconnects its three tails to the three heads by a 3-cycle
`tau`.  After all reconnections, the new factor components are the cycles
of

\[
                         F=\tau\circ\sigma.
\tag{1.1}
\]

For disjoint C6s, `tau` is the product of their disjoint 3-cycles.

## 2. Rigid split plus two opposite-arc connectors

Let the rigid C6 have cut labels

\[
                         s,r_1,r_2,
\]

where `s` lies on `C_ss` and `r_1,r_2` lie on `C_ts`.  Let two disjoint
rotated copies of one three-component connector have labels

\[
 \alpha,a_\alpha,b_\alpha,
 \qquad
 \beta,a_\beta,b_\beta.
\]

Here `alpha,beta` are T-edges, `a_*` lie on one donor component `A`, and
`b_*` on another donor component `B`.  Choose `alpha,beta` in the interiors
of the two open T-arcs cut by `r_1,r_2`.  Up to reversing all cyclic
orders, the old path permutation is

\[
 \sigma=(s)(r_1\ \alpha\ r_2\ \beta)
        (a_\alpha\ a_\beta)(b_\alpha\ b_\beta).
\tag{2.1}
\]

The three clean reconnections have

\[
 \tau=(s\ r_1\ r_2)
       (\alpha\ a_\alpha\ b_\alpha)
       (\beta\ a_\beta\ b_\beta),
\tag{2.2}

up to simultaneously reversing the last two triples.  Direct composition
gives

\[
\begin{aligned}
 F={}&(s\ r_1\ a_\alpha\ b_\beta\ \alpha)\\
    &\quad(r_2\ a_\beta\ b_\alpha\ \beta).
\end{aligned}
\tag{2.3}

Thus:

### Theorem 2.1

The rigid switch plus two opposite-arc copies of the same three-sector C6
turn the four original components `C_ss,C_ts,A,B` into exactly two hybrid
cycles.  Every original component has material in the resulting two-rail
system, and the two donor cycles are split across the rails.

The conclusion is independent of the metric positions of the cuts; only
the assertion that `alpha,beta` lie on opposite T-arcs enters (2.1).

## 3. Parity obstruction to joining the rails by C6s alone

For permutations on the cut labels,

\[
 \operatorname {sgn}(\pi)=(-1)^{N-c(\pi)},
\tag{3.1}
\]

where `N` is the number of labels and `c(pi)` its cycle count.  A C6
reconnection is a 3-cycle and hence even.  Therefore composing with any
number of clean C6 reconnections preserves the parity of the factor
component count on the affected union.

### Corollary 3.1

No sequence of clean C6s supported only on the two cycles in (2.3) can
join them into one.  More generally, a C6 with cut distribution `2+1`
over two cycles always leaves two cycles.

To obtain one factor cycle, one must introduce an additional component and
use a genuine `1+1+1` straddling connector, or use a parity-changing
higher circuit such as a suitable C8.

For the graphic q1 gate, joining the two rails is not necessary: it is
enough that each rail eventually contains an omitted q1 occurrence.  This
leads to a weaker and more natural target.

## 4. Two-rail propagation principle

Suppose `R_0,R_1` are the current hybrid rails.  For each `epsilon=0,1`,
take a genuine q2-neutral C6 using one edge of `R_epsilon` and one edge on
each of two fresh donor cycles.  If the two connector triples are
component-disjoint outside their designated rails, each switch merges
three components into one.  The result is again exactly two rails, with
the donors absorbed railwise.

Iterating this operation never accumulates extra components.  If at some
terminal stage each rail absorbs a donor cycle containing an omitted q1
occurrence, then the selected subgraph on both rails is a path forest and
the graphic gate is closed, even though the ambient factor still has two
components.

Hence the exact dynamic target is:

> produce two angle-disjoint lifts of each required action-profile
> connector, propagate the two rigid output rails, and terminate both in
> omission-bearing sectors.

The all-hook connector chain supplies the action-profile skeleton for such
propagation.  It does not yet supply the two angle-disjoint physical lifts
or the terminal omission-bearing boundary connectors.
