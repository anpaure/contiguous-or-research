# q2 representative exchanges: exact local damage and cycle-augmenting flow

**Date:** 2026-08-05  
**Method:** pure occurrence calculus on a disjoint union of cyclic turn
words; no computation or search  
**Status:** unconditional exchange theorem and conditional augmentation
mechanism.  A one-label representative switch loses at most two selected
q2 adjacencies and gains at most two.  For a packet of switches, factor-cycle
omissions obey an exact flow-divergence law.  Any q2-safe augmenting path to
a cycle with a spare omission reduces the number of unhit factor cycles by
one.  Existence of enough such paths for PBBS is not proved.

## 1. Setup

Let the turn positions be the vertices of a disjoint union `C` of cyclic
position graphs, one for each factor cycle.  Position `p` carries q1 label
`Y_p`.  An unequal adjacent pair `e=p(p+1)` has q2 colour

\[
 D(e)=Y_p\cap Y_{p+1}.                               \tag{1.1}
\]

Let `S` be a one-occurrence section: exactly one occurrence of every q1
label belongs to `S`.  Put

\[
 E(S)=\{p(p+1):p,p+1\in S\},                        \tag{1.2}
\]

and for each q2 colour define its selected witness load

\[
 c_D(S)=|\{e\in E(S):D(e)=D\}|.                     \tag{1.3}
\]

The section is q2-complete exactly when `c_D(S)>=1` for every `D`.

For a factor cycle `C`, let

\[
 o_C(S)=|C\setminus S|                               \tag{1.4}
\]

be its number of omissions.  The graphic condition is `o_C(S)>=1` for
every cycle.

## 2. Exact one-label exchange formula

Let `Y` be repeated, let `p in S` be its current representative, and let
`q notin S` be another occurrence of `Y`.  Switch the representative:

\[
 S'=S-\{p\}+\{q\}.                                  \tag{2.1}
\]

Define

\[
 L(p,q)=E(S)\setminus E(S'),\qquad
 G(p,q)=E(S')\setminus E(S).                        \tag{2.2}
\]

Every lost edge is incident with `p`, and every gained edge is incident
with `q`.  Therefore

\[
 |L(p,q)|\le2,\qquad |G(p,q)|\le2.                  \tag{2.3}
\]

For a q2 colour `D`, put

\[
 \ell_D=|\{e\in L(p,q):D(e)=D\}|,
 \qquad
 g_D=|\{e\in G(p,q):D(e)=D\}|.                     \tag{2.4}
\]

### Theorem 2.1 (sharp exchange criterion)

For every q2 colour,

\[
 \boxed{c_D(S')=c_D(S)-\ell_D+g_D.}                 \tag{2.5}
\]

Consequently the switch is q2-safe if and only if

\[
 c_D(S)-\ell_D+g_D\ge1\qquad\text{for every }D.     \tag{2.6}
\]

Only the at most four adjacency occurrences in (2.3) need be inspected.
In particular, the number of q2 colours which can lose coverage is at most
two, not four; four is the bound on total changed adjacency occurrences.

#### Proof

All position statuses except `p,q` are unchanged.  Removing `p` can delete
only its two incident selected-selected edges, and adding `q` can create
only its two incident edges.  Summing the colour indicators over the
symmetric difference gives (2.5), and (2.6) is the definition of q2
completeness. `square`

A convenient sufficient condition is that every colour on a lost edge has
an untouched second witness, unless the same colour is restored on a gained
edge.  Formula (2.6), rather than that sufficient relaxation, is the exact
test.

## 3. Exact cycle-flow law for a packet

Let `mathcal P` be a finite packet of switches

\[
 p_Y\longrightarrow q_Y,                            \tag{3.1}
\]

using distinct q1 labels `Y`.  Thus all old representatives `p_Y` are
distinct, all new representatives `q_Y` are distinct, and the final set

\[
 S_{\mathcal P}=
 S-\{p_Y:Y\in\mathcal P\}+\{q_Y:Y\in\mathcal P\}   \tag{3.2}
\]

is again a one-occurrence section.

Make a directed multigraph on the factor cycles: a switch contributes one
arc from the cycle containing `p_Y` to the cycle containing `q_Y`.  Define
its divergence with the sign convention

\[
 \operatorname{div}_{\mathcal P}(C)
 =\#\{Y:p_Y\in C\}-\#\{Y:q_Y\in C\}.               \tag{3.3}
\]

### Theorem 3.1 (omission-flow identity)

For every factor cycle,

\[
 \boxed{
 o_C(S_{\mathcal P})=o_C(S)+
             \operatorname{div}_{\mathcal P}(C).}  \tag{3.4}
\]

Thus representative exchanges transport omission tokens opposite the
directed arcs: the old representative cycle gains an omission and the new
representative cycle spends one.

#### Proof

Each old representative removed from `C` raises `o_C` by one; each new
representative inserted in `C` lowers it by one.  Sum over the packet.
`square`

The q2 effect of a packet is also local.  If `T` is the set of all old and
new occurrence positions in (3.1), only adjacency edges incident with `T`
can change.  Hence at most `4|mathcal P|` adjacency occurrences enter its
exact analogue of (2.5).  Overlaps can only reduce this bound.

## 4. Cycle augmenting paths

Call an exchange **currently q2-safe** when it satisfies (2.6) in the
current section.  Let

\[
 C_0,C_1,\ldots,C_t                                \tag{4.1}
\]

be distinct factor cycles.  For `0<=j<t`, suppose there is a repeated
label `Y_j` whose current representative `p_j` lies on `C_j` and which has
an unselected occurrence `q_j` on `C_(j+1)`.  Assume:

1. the labels `Y_j` are distinct and `p_j!=q_(j-1)` on every internal
   cycle;
2. switching `p_j -> q_j` in order `j=0,1,...,t-1` is currently q2-safe at
   every step;
3. `o_(C_0)(S)=0`; and
4. `o_(C_t)(S)>=2`.

### Theorem 4.1 (q2-safe cycle augmentation)

After the switches along (4.1), the section remains q2-complete, every
cycle which was hit remains hit, and `C_0` becomes hit.  Thus the number of
unhit factor cycles falls by one.

#### Proof

Sequential safety preserves q2 completeness.  By (3.4), `C_0` gains one
omission.  Every internal `C_j` loses the occurrence `q_(j-1)` and gains
the omission `p_j`, so its final omission count equals its initial count.
The terminal cycle loses one omission and retains at least one.  Every other
cycle is unchanged. `square`

The same conclusion holds for any q2-safe packet whose divergence is `+1`
at one unhit cycle, `-1` at one cycle with at least two omissions, and zero
elsewhere.  The packet need not literally be a path.

## 5. Exact alternate-witness restoration interface

If a desired cycle arc `p->q` is not q2-safe, Theorem 2.1 identifies at
most two uncovered colours.  To repair one such colour `D`, choose an
alternate witness edge `uv` of colour `D`.  Activating `uv` requires moving
the representatives of at most its two repeated endpoint labels to `u`
and `v`.  Those switches create their own exact loss sets by (2.5).

Thus q2 restoration is a binary branching process, not an uncontrolled
global recomputation:

\[
 \text{one cycle switch}
 \longrightarrow\text{at most two lost colours}
 \longrightarrow\text{at most two endpoint switches per colour}. \tag{5.1}
\]

A finite restoration tree closes successfully exactly when the union of
its distinct-label switches passes the packet form of (2.5).  Its cycle
effect is then given independently by the divergence law (3.4).  This is
the precise augmenting object required after the canonical PBBS section:

> a q2-safe occurrence packet with positive divergence at an unhit PBBS
> cycle and negative divergence only at a cycle with spare omission.

## 6. Scope

The theorem proves the local exchange calculus and the augmentation
implication.  It does not prove that the PBBS occurrence graph always
contains the required safe paths or finite restoration trees.  Load bounds
`1<=mu_1<=3` and `1<=mu_2<=10` alone do not imply this: a lost q2 colour
may have load one, and its unique witness may use occurrence fibres already
fixed elsewhere.  The remaining theorem is an expansion/reachability
statement for these exact exchange packets, not a scalar multiplicity
estimate.

