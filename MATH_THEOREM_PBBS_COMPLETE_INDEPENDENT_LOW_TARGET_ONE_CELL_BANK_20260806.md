# Every independent low target has one native hook cell

**Date:** 2026-08-06  
**Method:** full hook-envelope formula and step-two path decomposition; no
computation or search  
**Status:** unconditional local theorem for every nonempty independent
target of rank at most `d`.  It closes all targets whose cyclic runs are
singletons.  Simultaneous component Hall and mixed singleton/nontrivial-run
targets remain separate.

## 1. Setup

Use

\[
 n=2m+1,\qquad p=2d+1,\qquad b=m-d-1.
\tag{1.1}
\]

The full hook-envelope theorem says that an envelope rooted at `q` is

\[
 P=\{q\}\cup(q+J),
\tag{1.2}
\]

where `J` is a nonconsecutive `b`-subset of the oriented path

\[
 \{3,4,\ldots,n-2\}.
\tag{1.3}
\]

If its terminal occupancy is `z`, its mandatory core is

\[
 F=\{q,q-2z\},
\tag{1.4}
\]

and its terminal free-leaf suffix is

\[
 q-2z,q-2z+2,\ldots,q-2.
\tag{1.5}
\]

## 2. Endpoint choice in the step-two graph

Let `S subset Z_n` be nonempty, independent in the ordinary cycle graph,
and `|S|<=d`.

Because `n` is odd, addition by two is one cycle on `Z_n`.  The proper
subset `S` induces a disjoint union of paths in that cycle.  Choose an
endpoint `q in S` oriented so that

\[
 q+2\notin S.
\tag{2.1}
\]

Let `z>=0` be maximal with

\[
 q-2,q-4,\ldots,q-2z\in S.
\tag{2.2}
\]

Thus

\[
 q-2(z+1)\notin S.
\tag{2.3}
\]

The set in `(2.2)` is empty when `z=0`.

## 3. Completing the envelope

Force the terminal suffix

\[
 K=\{q-2z,q-2z+2,\ldots,q-2\}.
\tag{3.1}
\]

It has size `z` and lies in `S`.  Every remaining member of
`S-{q}-K` lies in the prefix path

\[
 I'=\{q+3,q+4,\ldots,q-2z-2\}.
\tag{3.2}
\]

Indeed `(2.1)` removes the two forward boundary positions, ordinary
independence removes the neighbours of `q` and of `q-2z`, and maximality
`(2.3)` removes the next step-two position.

The path `(3.2)` has length

\[
 2m-2z-3
\]

and independence number `m-z-1`.  Put

\[
 Q=S-\{q\}-K,
 \qquad |Q|\le d-z-1.
\]

The standard path-extension argument extends `Q` to an independent set of
size at least

\[
 (m-z-1)-|Q|\ge m-d=b+1.
\tag{3.3}
\]

In particular choose an independent `J' subset I'` of the required size

\[
 |J'|=b-z,
 \qquad Q\subseteq J'.
\tag{3.4}
\]

Then

\[
 J=J'\mathbin{\dot\cup}K
\tag{3.5}
\]

is a nonconsecutive `b`-set in `(1.3)`.  Its terminal occupancy is exactly
`z`, and the corresponding envelope contains `S`.

## 4. Complete independent-set ticket

The mandatory core `(1.4)` is contained in `S`: for `z=0` it is `{q}`;
for `z>0`, both endpoints occur in `(2.2)`.  Therefore

\[
 F\subseteq S\subseteq P.
\]

The exact one-cell ticket theorem permits thinning this source cell to
`S` while retaining the full depth-`d` owner row.

### Theorem 4.1

Every nonempty independent `S subset Z_n` with `|S|<=d` has a literal
one-cell occurrence on a native height-`d+1` hook component.

Thus all-singleton-run targets are closed locally.  Together with the
parity-complete run theorem, the only local all-low interface left is the
coexistence of isolated coordinates with one or more nontrivial runs and
their bridge support corridors.
