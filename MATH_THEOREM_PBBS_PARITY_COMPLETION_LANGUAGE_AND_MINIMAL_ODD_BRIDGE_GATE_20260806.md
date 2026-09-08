# Parity-complete hook language and the minimal odd-bridge gate

**Date:** 2026-08-06  
**Method:** exact cyclic run decomposition and the enlarged hook arc
language; no computation or search  
**Status:** unconditional sufficiency theorem for one explicit local
packet.  The native hook sector supplies every even bridge.  Adding the
single missing odd-bridge transition constructs every target whose maximal
runs have length at least two, within the original length and mass budgets.
The physical PBBS realization, regeneration, and component packing of the
odd bridge remain the exact gate.

## 1. The missing arc

For a source root `q`, terminal mass `z>=0`, and parity bit
`epsilon in {0,1}`, define

\[
 \begin{aligned}
 y&=q-(2z+\varepsilon),\\
 q'&=y-1=q-(2z+\varepsilon+1),\\
 F&=\{q,y\}.
 \end{aligned}
\tag{1.1}
\]

Call this a parity-`epsilon` hook arc of native cost `z`.  We will also use
the conservative charged cost `z+epsilon`, pricing one extra mass unit for
every parity-changing chip.

The native height-`d+1` hook component supplies exactly the
`epsilon=0` arcs:

\[
 q'=q-(2z+1),\qquad F=\{q,q-2z\}.
\tag{1.2}
\]

The sole missing local generator is therefore

\[
 \boxed{
 q'=q-(2z+2),\qquad
 F=\{q,q-(2z+1)\}.}
\tag{OB}
\]

It bridges an odd coordinate distance while exporting the next root one
coordinate below the bridge endpoint.

## 2. The parity-complete path graph

Let `K_b^pm` be the directed graph on `Z_n` containing every arc `(1.1)`
with `0<=z<=b` and `epsilon in {0,1}`.  Give it cost `z` and emitted core
`F`.

For a path

\[
 q_0\to q_1\to\cdots\to q_\ell
\tag{2.1}
\]

write `z_i,epsilon_i` for its arc data.  Its source interval consists of
the `ell` cells rooted at `q_0,...,q_(ell-1)` and emits

\[
 \bigcup_{i=0}^{\ell-1}
 \{q_i,q_{i+1}+1\}.
\tag{2.2}
\]

The native hook core-language theorem realizes `(2.1)` whenever every
`epsilon_i=0` and `sum z_i<=b`.  A protected realization of `(OB)` which
composes with those native cells would realize the full graph.

## 3. Every nontrivial-run target has a parity-complete path

Let `S subset Z_n` be a union of `r` maximal cyclic runs

\[
 R_1,\ldots,R_r,
 \qquad |R_j|\ge2,
 \qquad A:=|S|\le d.
\tag{3.1}
\]

Orient every run in decreasing cyclic order.  Let `D_j` be the distance
from the last coordinate of `R_j` to the first coordinate of `R_(j+1)`.
Then

\[
 \sum_{j=1}^rD_j=n-A+r.
\tag{3.2}
\]

Choose a largest gap `D_*` as the linear cut.  Starting after that cut:

1. traverse each run with zero-cost native cells;
2. at the last coordinate before a nonterminal gap `D_j`, use
   
   \[
   z_j=\lfloor D_j/2\rfloor,
   \qquad
   \varepsilon_j=D_j\pmod2;
   \tag{3.3}
   \]
3. the secondary core is exactly the first coordinate of the next run,
   and the exported root is its second coordinate.

Thus the emitted core union is exactly `S`.  The number of source cells is

\[
 \boxed{\ell=A-r+1\le d,}
\tag{3.4}
\]

and the native mass cost is

\[
 \begin{aligned}
 Z
 &=\sum_{j\ne *}\left\lfloor{D_j\over2}\right\rfloor\\
 &\le {n-A+r-D_*\over2}.
 \end{aligned}
\tag{3.5}
\]

Even after charging one additional unit for every odd bridge,

\[
 \begin{aligned}
 Z^+
 &=\sum_{j\ne *}\left\lceil{D_j\over2}\right\rceil\\
 &\le {n-A+2r-1-D_*\over2}.
 \end{aligned}
\tag{3.5+}
\]

As in the audited largest-gap calculation,

\[
 D_*\ge{n-A+r\over r}
       \ge{2(n-d)\over d}
       =(16/\pi+o(1))d.
\tag{3.6}
\]

Since `A>=2r`, the right side below is at most `2d+2`; hence `(3.6)` gives,
eventually,

\[
 D_*\ge2d+2-A+2r.
\tag{3.7}
\]

Equations `(3.5+)--(3.7)` give the stronger charged bound

\[
 \boxed{Z\le Z^+\le {n-2d-3\over2}=b.}
\tag{3.8}
\]

We have proved:

### Theorem 3.1 (parity-complete run covering)

Every target of rank at most `d` whose maximal runs all have length at
least two has a path of length at most `d` and cost at most `b` in
`K_b^pm`, with emitted core set exactly equal to the target.

No envelope assistance is needed.

## 4. The rank-six witness is repaired by two odd arcs

For

\[
 S=\{0,-1,-4,-5,-8,-9\},
\]

cut the largest gap `n-9`.  The four source cells are

\[
 \begin{array}{c|c|c|c}
 q&z&\varepsilon&F\\ \hline
 0&0&0&\{0\}\\
 -1&1&1&\{-1,-4\}\\
 -5&1&1&\{-5,-8\}\\
 -9&0&0&\{-9\}.
 \end{array}
\tag{4.1}
\]

Their union is `S`, their native cost is two, their parity-charged cost is
four, and their length is four.  Both costs are at most `b` eventually.
Thus `(OB)` repairs precisely the parity defect isolated by the
three-dimer obstruction.

## 5. Why a two-hook reset is not the general repair

If one is allowed to concatenate independently rooted native hook
segments, every odd outgoing run gap can be made a segment boundary.
For `t` odd gaps this uses `t` segments: one odd gap is the global linear
cut and the other `t-1` require physical seams.

The number `t` can be `Theta(d)`.  Moreover the largest gap must normally
be the global cut to retain the mass bound.  In the rank-six witness the
largest gap is even, so both odd gaps would require seams; three hook
segments, not two, are needed.  Hence one protected two-hook seam repairs
the witness only if it also implements a parity-changing bridge.  Plain
component reset does not give a bounded-state all-rank theorem.

This is why `(OB)`, rather than an unrestricted number of component cuts,
is the minimal useful repair.

## 6. Exact physical PBBS lemma

The remaining local theorem can now be stated without reference to a
global compiler.

> **Protected odd-bridge lemma.**  For every eventual height `d+1`, every
> `0<=z<=b`, and every choice of labels `q,y` with
> `q-y=2z+1`, the PBBS factor has a same-length protected local packet
> whose source interface is `(OB)`.  The packet:
>
> 1. has mandatory source core `{q,y}` and exports next root `y-1`;
> 2. preserves the complete owner multiset and immediate lower/upper
>    palettes;
> 3. preserves the exterior depth-`d` antecedent and all inherited upper
>    interval witnesses;
> 4. exports the same packet state, so any finite sequence of odd bridges
>    can be planted serially; and
> 5. has an occurrence-labelled component bank satisfying Hall for the
>    parity words selected by Theorem 3.1.

Under this lemma, Theorem 3.1 and the native hook realization give a
literal, component-disjoint atlas for every nontrivial-run target through
rank `d` without changing the owner or `q1` rows.

The likely action-profile donor is a multi-near-hook sector

\[
 \boxed{(h,2^t,1^{b-2t})},
\]

where `t` is the number of odd bridges.  It has the same total soliton mass
as `(h,1^b)`, and the extra charge in `(3.5+)` is exactly one unit for each
unit-leaf pair promoted to a length-two soliton.  The existing all-hook
`q2`-neutral connector chain already supplies the one-chip near-hook
profile `(h,2,1^{b-2})` after the corresponding parameter shift.  What is
not yet proved is the literal depth-`d` formula:

> a terminal length-two soliton changes the hook root step from
> `2z+1` to `2z+2` and changes the exit span from `2z` to `2z+1`, while
> preserving the protected exterior.

Proving this formula, and then proving that `t` chips can be scheduled at
the prescribed bridge positions, would realize `(OB)` at exactly the
already-paid cost `(3.5+)`.  Existing connector theorems establish useful
owner/`q1`/`q2` exchanges involving the near-hook profile, but do not yet
establish this source-envelope calculation or its regenerative packing.

## 7. Remaining singleton-run interface

Theorem 3.1 covers all pure-dimer targets and all multi-run targets with no
singleton run.  Singleton runs are independent and can often be retained
in the initial survivor envelope, but the terminal support corridor of a
bridge may collide with them.  A complete all-low theorem additionally
needs one of:

* an odd-bridge packet whose protected envelope carries an arbitrary
  prescribed independent singleton bank of size at most `d`; or
* a separate singleton-bypass interface.

This is now distinct from the parity problem.  The native one-cell theorem
already proves every singleton target individually; what remains is their
simultaneous presence inside a higher-rank target interval.
