# The graph singleton absorber has no owner-preserving long-pure-rail dilation

**Date:** 2026-08-13  
**Status:** unconditional actual-column obstruction for `q >= 3`  
**Scope:** legal pure rails with a fixed `(R-q)`-core and a cyclic order of
pairwise distinct toggle labels

## 1. Setup

Let

\[
 q\ge3,\qquad |D|=R-2q,\qquad |V|=2q+2,
\]

where `D` and `V` are disjoint.  For an edge
`e in binom(V,2)`, put

\[
 \Omega(e)=D\cup(V\setminus e).                    \tag{1.1}
\]

Thus `Omega(e)` is an `R`-set, and the map `e mapsto Omega(e)` is
injective.

A legal pure rail of period `m` has the form

\[
 \rho=(C,T,\sigma),\qquad |C|=R-q,\quad |T|=m,
 \quad C\cap T=\varnothing,                         \tag{1.2}
\]

where `sigma` is a cyclic order of the pairwise distinct points of `T`,
and its owner deck is

\[
 \mathcal D(\rho)
 =\{C\cup I_t^q(\sigma):t\in\mathbb Z_m\}.         \tag{1.3}
\]

The obstruction below applies in particular to the minimal biresident
periods `m=2q+1` and `m=2q+3`.

## 2. A core-capacity lemma

### Lemma 2.1

If `m >= 2q+1`, then a legal pure rail contains at most `q` owners from
the graph family

\[
 \Omega\binom V2
 =\{\Omega(e):e\in\tbinom V2\}.                    \tag{2.1}
\]

### Proof

There is nothing to prove if the rail contains no graph owner.  Otherwise
its core `C` is contained in one such owner, and hence

\[
 C\subseteq D\cup V.                               \tag{2.2}
\]

Put

\[
 s=|D\setminus C|,\qquad
 Z=D\setminus C,\qquad
 W=V\setminus(C\cap V).                            \tag{2.3}
\]

Since `|C|=R-q` and `|D|=R-2q`,

\[
 |C\cap V|=q+s,qquad |W|=q+2-s.                  \tag{2.4}
\]

If `Omega(e)` belongs to the rail, then `C subseteq Omega(e)`.  Therefore
`e` is disjoint from `C cap V`, so `e subseteq W`, and its active
`q`-window is exactly

\[
 \Omega(e)\setminus C
 =Z\cup(W\setminus e).                             \tag{2.5}
\]

In particular `s <= q` whenever such an edge exists.

Suppose first that `s >= 1`.  Every graph-owner window in the rail
contains the same `s` distinct toggle labels `Z`.  In a cyclic order of
length at least `2q+1`, at most

\[
 q-s+1\le q                                        \tag{2.6}
\]

cyclic `q`-windows contain a prescribed `s`-set.  Indeed, after unrolling
one `q`-window which contains `Z`, the first and last points of `Z` have
span at least `s-1`; the possible starts form an interval of length at
most `q-(s-1)`.

Now suppose that `s=0`.  By (2.5), every graph-owner window is a cyclic
`q`-window contained in the fixed set `W`, where

\[
 |W|=q+2.                                          \tag{2.7}
\]

Mark in the cyclic toggle order the positions occupied by points of `W`.
There are at most `q+2` marked positions.  Since `m>=2q+1` and `q>=3`,
there are at least `q-1>=2` unmarked positions, and fewer than `2q`
marked positions.  Hence at most one marked run has length at least `q`.
A marked run of length `r` contains `max(r-q+1,0)` all-marked
`q`-windows.  Their total number is therefore at most

\[
 (q+2)-q+1=3\le q.                                 \tag{2.8}
\]

Both cases prove the lemma. \(\square\)

## 3. No balanced rooted dilation of the graph absorber

Let `S` be the graph used in the star--cycle singleton absorber.  Its
edges are partitioned into `q+1` stars of size `q+1`, and hence

\[
 |E(S)|=(q+1)^2.                                   \tag{3.1}
\]

The distinguished edge is `uv`, and `G=S-uv` is partitioned into `q`
cycles of length `q+2`.

Call a proposed dilation **owner-preserving** if its plus owner shore
contains every original owner

\[
 \{\Omega(e):e\in E(S)\},                          \tag{3.2}
\]

and its minus shore contains every original owner over `E(G)`.  Arbitrary
additional owners may be shared between the two shores, and original
owners may be reassigned to entirely different component cores and cyclic
orders.

### Theorem 3.1 (actual-column no-go)

For `q >= 3`, there is no owner-preserving dilation in which the plus
shore is an owner-disjoint union of `q+1` legal pure rails of periods at
least `2q+1`.  Consequently, the minimal period-ledger proposal

\[
 (q+1)C_{2q+1}\quad\text{versus}\quad qC_{2q+3}   \tag{3.3}
\]

cannot be a correlated cross-core or shared-auxiliary dilation of the
original graph absorber.

### Proof

By Lemma 2.1, each of the `q+1` plus rails contains at most `q` of the
original graph owners.  Owner-disjointness therefore gives the upper bound

\[
 q(q+1)                                             \tag{3.4}
\]

on the number of owners from (3.2) which the plus shore can contain.  But
injectivity of `Omega` and (3.1) require it to contain

\[
 (q+1)^2>q(q+1).                                   \tag{3.5}
\]

This is a contradiction. \(\square\)

The proof uses neither the minus shore nor any palette, trace, socket,
history, cap, or residence row beyond the legal pure-rail column form.
It therefore remains valid after all of those constraints are imposed.

## 4. Why this is stronger than the fixed-core insertion no-go

The earlier fixed-core calculation ruled out lengthening each short graph
component merely by inserting fresh active labels while retaining its old
core.  Theorem 3.1 allows all of the apparent escape routes inside an
owner-preserving dilation:

* every original graph owner may change component;
* every long component may use a new core;
* auxiliary owners may be chosen jointly across the two shores; and
* no edgewise or componentwise functoriality is assumed.

The obstruction is instead intrinsic to an actual long pure-rail column.
Once its core omits `s` points of `D`, all graph-owner windows in that rail
must contain the same set `Z` of those `s` points.  If `s=0`, they must all
be supported on only `q+2` toggle labels.  Either way the rail has capacity
at most `q`, one short of the average `q+1` demanded on the plus shore.

## 5. Exact surviving routes

The theorem does **not** rule out a completely new one-owner trade whose
common owner reserve is unrelated to the graph owner families.  Such an
object would not be a dilation of the star--cycle absorber and would need
a new construction from scratch.

For the proved graph absorber, the surviving routes are therefore:

1. use the short periods `q+1,q+2`, which already have positive residence
   and simple aggregate immediate-lower palettes, and solve their run-safe
   occurrence fusion plus upper backups;
2. use the complementary-fibre lift and accept one whole legal rail as the
   structured leave; or
3. enlarge the legal column class beyond fixed-core distinct-toggle pure
   rails and prove the compiler for that enlarged class.

In particular, searching further within the owner-preserving asymmetric
period pair `(2q+1,2q+3)` cannot close the graph absorber: that entire
branch is now excluded before immediate-lower or all-width tickets are
examined.
