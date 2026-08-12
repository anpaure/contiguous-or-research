# Two regular incidence factors give a private typed router

**Date:** 2026-08-04  
**Status:** unconditional fixed-state network theorem; conditional application
to the Boolean carrier.  No finite computation is used.

## 0. Outcome

The full-port strict-gammoid certificate used in the current common-cap
interface is sufficient but need not be verified by an opaque all-cut
argument.  It follows from a second bounded-degree incidence factor with a
literal private occurrence lift.

Fix one materialized cap/guard/occurrence state and delete one fixed
compensation linkage.  Suppose

\[
 B=(G,P;E_B),\qquad H=(P,S;E_H)
\]

are bipartite graphs satisfying

\[
 \deg_B(g)=h,\quad \deg_B(p)\le h,
 \qquad
 \deg_H(p)=q,\quad \deg_H(s)\le q.                 \tag{0.1}
\]

Assume every incidence of `B` has a private literal claim-to-port prefix,
every incidence of `H` has a private literal port-to-sink suffix, the two
families are mutually private away from their displayed endpoints, and
all terminal types are legal for every claim which can reach the displayed
port.  Then every gain claim in `G` has a vertex-disjoint route to a
distinct typed sink.

The proof sends `1/(hq)` units along every displayed two-stage incidence
chain and invokes integral max flow.  Thus the hard physical premise may be
replaced by the concrete occurrence statement

> expose a left-regular/right-bounded private suffix factor on the active
> physical ports.

For `h=q=2`, two occurrence-lifted protected two-factors suffice.  An
abstract Middle Levels factor still does not prove the result: the private
literal lifts, coexistence after compensation deletion, and type legality
remain essential.

## 1. Fixed residual network

Let `D` be a finite directed node-capacitated network.  Split every unit
physical capacity into an in/out vertex joined by a capacity-one arc.  Fix
one compensation linkage `L`, delete all capacities and sink slots used by
`L`, and denote the residual network by

\[
 D'=D-\operatorname{cap}(L).
\]

Every object below belongs to one fixed materialized state.  Equal Boolean
values at different physical addresses remain different occurrences, and
aliases of one physical cell pass through one shared capacity-one vertex.

For every `g in G`, let `a_g` be a distinct claim start.  For every
`gp in E_B`, fix a directed prefix

\[
 Q_{gp}:a_g\leadsto p.
\]

For every `ps in E_H`, fix a directed suffix

\[
 R_{ps}:p\leadsto s,
\]

where the vertices of `S` are distinct residual typed sink occurrences.
Assume:

1. different prefix interiors are disjoint; prefixes belonging to one
   claim may share their claim start, and prefixes ending at one physical
   port may share only that port;
2. different suffix interiors are disjoint; suffixes incident with one
   port may share only that port, and suffixes incident with one sink may
   share only that sink;
3. a prefix and a suffix meet only when the prefix ends at the suffix's
   displayed port, and then only at that port;
4. all displayed paths avoid the capacities and sinks deleted by `L`;
5. for every `gp in E_B`, every sink adjacent to `p` in `H` is a legal
   terminal occurrence for `g`.

The privacy hypotheses may be weakened to the corresponding congestion
bounds, but the private form is the clean reusable certificate.

## 2. Two-factor composition theorem

### Theorem 2.1

Under Section 1 and the degree conditions (0.1), there are pairwise
vertex-disjoint directed paths in `D'`, one from every `a_g`, ending at
distinct legal sinks in `S`.

### Proof

Add a super-source `alpha` with a capacity-one arc to each `a_g`, and a
super-sink `omega` with a capacity-one arc from each `s in S`.

For every two-stage incidence

\[
             g p\in E_B,\qquad p s\in E_H,
\]

send `1/(hq)` units along

\[
        \alpha,a_g,Q_{gp},p,R_{ps},s,\omega .        \tag{2.1}
\]

The resulting loads are as follows.

* A source arc at `g` has load

  \[
  {1\over hq}\sum_{p:gp\in E_B}\deg_H(p)
       ={hq\over hq}=1,
  \]
  because the `h` ports adjacent to `g` each have `q` suffix incidences.
* A private prefix interior for `gp` is used with all `q` suffixes at `p`,
  hence has load `q/(hq)=1/h`.
* A physical port `p` has load

  \[
                \deg_B(p)q/(hq)=\deg_B(p)/h\le1.    \tag{2.2}
  \]
* A private suffix interior for `ps` has load

  \[
                \deg_B(p)/(hq)\le1/q.               \tag{2.3}
  \]
* A sink `s` has load

  \[
   {1\over hq}\sum_{p:ps\in E_H}\deg_B(p)
      \le {h\deg_H(s)\over hq}\le1.                 \tag{2.4}
  \]

Privacy accounts for every possible shared unit capacity.  Thus (2.1) is
a feasible flow of value `|G|`.  All capacities in the augmented
node-split network are integral, so max-flow integrality supplies an
integral flow of the same value.  Every claim arc is saturated and every
sink arc has capacity one.  Flow decomposition gives one vertex-disjoint
path per claim, ending at distinct sinks.  Condition 5 makes every chosen
terminal legal.  Adjoining the fixed linkage `L` gives the corresponding
simultaneous linkage in the original network.  \(\square\)

### Corollary 2.2 (the suffix factor already certifies full port rank)

Under the hypotheses on `H`, every subset `Y subseteq P` satisfies

\[
 q|Y|=|E_H(Y,N_H(Y))|\le q|N_H(Y)|,
\]

and hence `|N_H(Y)|>=|Y|`.  Therefore `H` has a matching saturating all
active ports.  With the private suffix lift, the active port set has full
rank in the residual typed suffix gammoid.

The fractional proof of Theorem 2.1 is nevertheless useful because it
keeps both incidence ledgers visible and extends immediately to rational
edge weights satisfying the analogous source, port, and sink congestion
inequalities.

## 3. Exact scope at `h=q=2`

Suppose the small protected-factor theorem provides an abstract spanning
two-factor on a Middle Levels incidence graph.  If logical gain claims are
injected into its left shore and its right shore is lifted to distinct
physical ports, it supplies a graph `B` with the first half of (0.1).

A second protected two-factor can certify the suffix stage only after all
of the following are proved in one state:

1. the active physical ports inject into its left shore;
2. every selected factor incidence has a literal occurrence-labelled
   port-to-sink realization after deleting the compensation linkage;
3. the realizations have private interiors and distinct physical endpoint
   capacities as required in Section 1;
4. the right shore consists of unused typed sink occurrences; and
5. both factors coexist with the pivot, upper witness bank, and background
   compiler.

The abstract existence of two graph factors alone does not prove any of
these physical rows.  Conversely, once these rows hold, no separate
all-subset gammoid audit is needed: the degree count and Theorem 2.1 prove
all cuts simultaneously.

## 4. Relation to the current all-dimensional frontier

The current common-cap synthesis asks for either full residual active-port
rank or another capacity-faithful direct-flow certificate.  Theorem 2.1
gives such a certificate with a very small local description:

\[
 \boxed{\text{private gain--port factor}
        +\text{private port--sink factor}.}
\]

It does not solve the protected pivot coinstantiation theorem.  Its value
is the quantifier reduction: instead of proving every residual suffix cut
directly, it is enough to co-instantiate one bounded-degree typed suffix
factor.  The remaining obstruction is therefore occurrence-level
coexistence, not max-flow integrality or an unidentified Hall inequality.
