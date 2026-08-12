# Independent audit: hinge-rectangle coloured flow and the exact one-copy obstruction hierarchy

Date: 2026-08-02  
Status: independent proof audit.  The literal hinge rectangle and its
root-conditioned network rounding are valid after requiring one fixed unit
on every owner arc.  The audit also separates generic one-copy obstructions
from statements proved for the canonical central Boolean profile.  It does
not prove the missing root-conditioned flow or topology hypotheses.

## 0. Verdict

The hinge-rectangle theorem is a genuine integral face of the coloured
trace problem.

* For every strict chain of at most `d` named lower targets below one owner,
  there is a Cartesian tail/head sub-menu with fixed owner and fixed declared
  target payload.
* Once an exact owner-chain table and an integral rooted boundary are fixed,
  any fractional balance point supported on those rectangles rounds by an
  ordinary lower-bounded network flow.  The rounded point uses one trace per
  owner and preserves the complete declared target vector.
* This conclusion does **not** follow from the stationary pull clock and the
  SCD selector separately.  They solve two projections; neither proves that
  one exact chain table supports a root-conditioned fractional hinge flow.
* Connected Euler chronology remains a separate labelled-spine problem.
  Tail-fixed crossed-head switches are possible exactly within a common
  internal spine and subject to mutual terminal-payload admissibility.

The generic implication

\[
 \text{stationary fractional coloured circulation}
 \Longrightarrow
 \text{one-copy integral circulation with }O(1)\text{ sidecar}
\]

is false.  None of the known generic counterexamples, however, proves that
the full large-`k` canonical central Boolean instance is impossible.

## 1. Literal rectangle audit

Let

\[
 \varnothing\ne S_1\subsetneq\cdots\subsetneq S_\ell\subsetneq T,
 \qquad 1\le\ell\le d-1,
\]

put `S_0=emptyset`, and choose `x in S_1`.  For arbitrary

\[
 A\subseteq S_\ell,
 \qquad
 \varnothing\ne B\subseteq S_1,
\]

define

\[
 B_0=(T\setminus S_\ell)\cup A,
 \qquad B_d=B,
\]

and the common middle word by

\[
\begin{aligned}
 B_i&=\{x\} &&(1\le i\le d-\ell-1),\\
 B_{d-j}&=S_j\setminus S_{j-1} &&(2\le j\le\ell),\\
 B_{d-1}&=S_1.
\end{aligned}
\tag{1.1}
\]

The index ranges in (1.1) are disjoint and exhaust `1,...,d-1`.
Strictness makes every difference letter nonempty, `x` makes every filler
nonempty, `B` is nonempty by assumption, and `B_0` contains the nonempty set
\(T\setminus S_\ell\).  Thus all source letters are legal.

For `1<=j<=ell`, the suffix of length `j+1` starts at `B_(d-j)` and has
union

\[
 (S_j\setminus S_{j-1})\cup\cdots\cup
 (S_2\setminus S_1)\cup S_1\cup B=S_j.              \tag{1.2}
\]

The fixed middle letters cover `S_ell`, and `B_0` supplies
\(T\setminus S_\ell\), so
the full owner is exactly `T`.  The tail

\[
 ((T\setminus S_\ell)\cup A,B_1,\ldots,B_{d-1})
\]

depends only on `A`, while the head

\[
 (B_1,\ldots,B_{d-1},B)
\]

depends only on `B`.  Every cross-pair is therefore a literal de Bruijn
trace with the same owner and marked chain.  The rectangle sizes are

\[
 2^{|S_\ell|}
 \quad\text{and}\quad
 2^{|S_1|}-1.                                           \tag{1.3}
\]

When `ell=d`, put

\[
 B_{d-j+1}=S_j\setminus S_{j-1}\quad(1\le j\le d),
 \qquad B_0=(T\setminus S_d)\cup A,\quad A\subseteq S_d.
\tag{1.4}
\]

Then the suffix of length `j` is `S_j`; the head is fixed and only the tail
varies.  This is the degenerate rectangle of size
\(2^{|S_d|}\times1\).

The transparency is deliberately limited.  In the nonfull case, varying
`B_d` changes the unmarked length-one suffix.  Varying `B_0` can change
prefix, exterior-window, upper, residence, guard, and compiler data.  The
proved rectangle is transparent for the owner and the **declared marked
chain**.  Additional payload must be imposed by restricting to a smaller
subrectangle and rechecking fractional feasibility.

## 2. Root-conditioned network audit

Fix a rooted trace path `P` whose owner and declared target resources are
distinct, remove those resources from the owner-chain table, and put

\[
                         \eta=\partial P.
\]

For each remaining owner `T`, let
\(E_T=\mathcal A_T\times\mathcal H_T\) be a nonempty hinge rectangle.  Assume
there is a rational point

\[
 x(E_T)=1\quad(T\text{ free}),
 \qquad
 \partial x=-\eta.                                      \tag{2.1}
\]

Introduce nodes `T^-`,`T^+` and an arc `T^- -> T^+` whose **lower and upper
capacities are both one**.  Join each literal tail state in
\(\mathcal A_T\) to `T^-`, and join `T^+` to each literal head state in
\(\mathcal H_T\).
The tail/head marginals of (2.1) give a feasible flow with integral state
boundary.  Lower-bounded network-flow matrices are totally unimodular, so
there is an integral flow.  The fixed unit on the owner arc forces exactly
one integral tail and one integral head for every owner.  Cartesianity
turns that pair back into one literal trace.

This proves integral owner and target preservation because the target
payload is constant on each owner rectangle and the owner-chain table
partitions the residual named targets.

The fixed-unit qualification is essential.  Merely declaring
`T^- -> T^+` to have capacity at most one would permit zero flow through an
owner and would not prove the owner equations.  The corrected theorem uses
lower capacity equal to upper capacity equal to one.

The theorem is conditional on (2.1).  The pull-clock circulation may split
one owner among several chain payloads, and an SCD table need not support
the pull-clock tails and heads.  Hence neither known marginal theorem
supplies (2.1) for one common table.

## 3. Exact topology row after rounding

Write a selected trace as

\[
                       e=(A_0,M,A_d),
 \qquad M=(A_1,\ldots,A_{d-1}).                       \tag{3.1}
\]

For two traces `e=(A_0,M,A_d)` and `f=(B_0,N,B_d)`, keep their tails fixed
and transpose their old heads.  Both crossed traces are literal order-`d`
de Bruijn arcs if and only if

\[
                              M=N.                    \tag{3.2}
\]

Indeed, the suffix of the first old tail and the prefix of the second old
head are respectively `M` and `N`; the other crossed arc gives the same
equality.  Payload preservation additionally requires `B_d` to be an
allowed terminal for the first labelled menu and `A_d` to be allowed for
the second.

Consequently, a tail-fixed rerouting factors into one bipartite
head-assignment problem per spine.  This fibre is integral, but
connectedness couples the spine factors.

An exact sufficient fusion certificate is a connected head permutation.
Choose one unprotected selected arc from every current Euler component,
all with the same spine, and cyclically permute their head tokens so that
every received terminal remains in the receiver's labelled menu.  The
tail and head multisets are unchanged; every owner and target payload is
unchanged; deleting one arc from an Eulerian component does not disconnect
it; and the cyclic cross-arcs join all components.  More generally, complete
exchange pools whose component--pool incidence graph is connected give a
sequence of pairwise component mergers.

For this move class, a disconnected component--pool incidence graph is an
exact invariant obstruction.  Larger alternating circuits, tail changes,
or source-changing packets may escape it.

Thus the exact post-rounding topology lemma still needed is:

> choose the integral hinge flow and one protected root so that its
> payload-transparent spine pools admit a connected head permutation (or a
> protected fusion tree); alternatively leave only components whose exact
> suffix--prefix reset tour has total cost `O(1)`.

A bounded number of components alone yields only `O(d)` in general.

On the rigid full-depth face there is an equivalent graphic--flow
criterion.  Each role `i` has a fixed head state `h_i`; let

\[
                         a_v=|\{i:h_i=v\}|.
\]

Its variable leading letter gives a literal list of legal tail states.
Balance is exactly an exact-demand bipartite matching from roles to tail
states, with demand `a_v` at state `v`.  A connected selection exists if
and only if there is a legal weak spanning-tree skeleton using distinct
roles `R`, with tail-use vector `b_R<=a`, such that after deleting `R` the
residual role--tail graph has an exact capacitated matching with demands
`a-b_R`.  Necessity follows by extracting a spanning tree from a connected
selector; sufficiency follows by adjoining the residual matching to the
tree.  A protected root is handled by preassigning its role.  Retain the
original all-role head-demand vector `a`, subtract the pinned literal
tail-use vector `b_P`, and require `0<=b_P<=a`; the free roles have exact
tail demand `a-b_P`.  Include the fixed rooted block in the graphic
certificate and contract it before applying the spanning-tree criterion.

## 4. Proof-safe obstruction hierarchy

The earlier obstruction notes establish different, noninterchangeable
facts.

### 4.1 Minimal owner/state torsion

One owner with the two reverse traces `u->v` and `v->u` has a stationary
half-half point, but neither integral owner choice is balanced.  The owner
row together with one state row has determinant two.  This is the smallest
literal warning against generic total unimodularity; it is not a complete
all-owner Boolean instance.

### 4.2 Complete Boolean calibration

At `(k,r,d)=(4,2,1)`, the six pair owners have the two orientations of the
six edges of `K_4`.  The half-half law has exact owner mass, exact state
balance, and exact fractional singleton-target loads.  Every one-copy
choice orients `K_4`, so every state has odd divergence.  No balanced
circuit or unbridged open trail exists.

For every even `k`, the same `r=2,d=1` family requires at least
`k/2-1` sidecar arcs for an open trail and `k/2` for a circuit.  It therefore
refutes a generic `O(1)` sidecar theorem even when exact named-singleton
loads are included fractionally.  For `k>4`, this family is not the
canonical central-rank/deadline slice.

### 4.3 Saturated marked-age hole

At `(r,d,W)=(7,3,2)`, a four-state literal rotation cycle weighted by one
half gives a connected rational stationary circulation and the integer
marked-rank histogram with one copy of every rank `1,...,6`.  No integral
circulation of mass two has that histogram.  This is a genuine saturated
marked-age semigroup hole and is minimal only for the stated
single-rotation saturated mechanism.  It is not a canonical Boolean-profile
counterexample.

### 4.4 Canonical fixed-histogram obstruction

For the displayed symmetric pull decomposition at `k=10`,

\[
 W x_{1,1}=605/29
\]

is nonintegral.  Therefore that exact block-start histogram cannot be
retained on a one-copy owner period.  This does not rule out another
integral decomposition: a verified optimal `k=10` word exists, and the
large-`k` aggregate conductor theorem proves the canonical role vector is
integral after permitted trades.

### 4.5 Physical odd-cycle minor

The physical tail/head/owner hypergraph first has a clean strong odd-cycle
minor at `C_5`, not `C_3`.  This proves that the unrestricted common master
is not a balanced/network matrix.  The authenticated pentagon has a portal,
so it is not by itself a fractional-but-integral impossibility certificate.

## 5. Minimal canonical lemma after this audit

For the canonical central Boolean problem, the weakest current sufficient
statement is the following correlated existence theorem.

> Choose simultaneously an exact residual named-target chain table, one
> admissible rooted path, and guarded hinge subrectangles such that the
> root-conditioned rational balance equations (2.1) hold.  Then choose the
> resulting integral network-flow point so that its transparent
> component--spine pools admit a connected head permutation or protected
> fusion tree; otherwise certify an exact `O(1)` overlap-reset tour.

The first sentence is the unresolved owner/target/root correlation.  Once
it holds, integral one-copy rounding is automatic.  The second sentence is
the unresolved topology row.  Fractional pull-clock stationarity alone
certifies neither one.

Residence, arbitrary-width upper decks, exterior chronology, and the
terminal common-cap compiler remain outside this audit.
