# Unsaturated one-copy hinges: exact predecessor Hall, Boolean expansion, and the first forbidden cut

**Date:** 2026-08-02  
**Lane:** A, integral coloured rotors  
**Status:** exact protected-completion reduction, a deterministic positive
expansion criterion, and a sharp raw-menu obstruction.  This note does not
construct the canonical all-`k` table.

## 0. Outcome

The one-sided rectangles of
`MATH_THEOREM_A_UNSATURATED_ONECOPY_HINGE_AND_PROTECTED_COMPLETION_GATE_20260802.md`
have a useful feature which is stronger than it first appears: after literal
residence histories and named upper witnesses are imposed, **any surviving
tail subfamily is still Cartesian**, because the head is fixed.  Hence the
protected-completion problem has no residual tail--head correlation.  It is
exactly a capacitated predecessor matching.

This note proves four facts.

1. The matching is feasible exactly when one Hall family holds.  The family
   splits into independent order-`d` de Bruijn spine fibres, and inside a
   fibre the unfiltered unsaturated menus are Boolean intervals.
2. A weighted bounded-overlap inequality gives a genuine deterministic
   positive expansion theorem for these menus.
3. A connected Euler completion is exact after reserving a distinct-role
   forest and applying the same Hall test with the consumed tail capacities
   removed.
4. The raw Boolean menus do **not** satisfy Hall automatically.  At depth one
   there is a four-role example with pairwise distinct owners and heads in
   which every role has a legal predecessor but two roles have the same sole
   predecessor.  Four roles are minimal under those hypotheses.  Disjoint
   copies force an arbitrarily large boundary-only sidecar when the role
   table, head multiplicities, and menus are held fixed.

Thus the live all-`k` assertion is not “unsaturation implies expansion”.  It
is the concrete task of choosing the owner/chain table so that its accepted
Boolean intervals obey the cuts below, and then reserving a connected
skeleton without destroying them.

## 1. Accepted one-sided menus

Let `V` be the finite set of **complete interface states**.  A state includes
the literal order-`d` source tuple, clipped signed run ages, endpoint type,
and every other boundary datum on which concatenation depends.  Let `I` be
the free roles.  Role `i` has

* a fixed owner and fixed named lower payload;
* a fixed completed head state `h_i in V`; and
* a nonempty accepted tail menu `M_i subseteq V`.

For every `a in M_i`, the physical packet `a -> h_i` is assumed to have the
same fixed resource payload and to pass its literal internal residence audit,
named upper-witness tickets, and exterior boundary-signature audit.  Its
private interior meets other packets only at declared interface states.

This is exactly how one must filter an unsaturated hinge.  If its raw tail
menu is

\[
 \mathcal A_i=\{(U_i\cup A,\sigma_i):A\subseteq F_i\},
 \qquad F_i=S_{i,1}-\{y_i\},                         \tag{1.1}
\]

then `M_i` is the subfamily whose physical histories and upper guards pass.
Since the head remains the singleton `{h_i}`, every `M_i x {h_i}` is still
a literal Cartesian completed hinge.  Filtering cannot create the
non-Cartesian projection error from a genuinely two-sided packet.

Let `P` be the fixed protected packet bank and put

\[
 \eta=\partial P,\qquad
 m(v)=|\{i:h_i=v\}|,\qquad b(v)=m(v)+\eta(v).         \tag{1.2}
\]

The sign convention is `partial(a -> h)=1_h-1_a`.  Necessarily
`b(v)>=0` for every state and `b(V)=|I|`.  The number `b(v)` is the exact
number of selected free tails which must equal `v`.

## 2. Exact fixed-head predecessor theorem

For `J subseteq I`, write

\[
 N(J)=\bigcup_{i\in J}M_i.                           \tag{2.1}
\]

For `X subseteq V`, put

\[
 \ell_M(X)=|\{i:M_i\subseteq X\}|.                  \tag{2.2}
\]

### Theorem 2.1 (protected predecessor min--max)

There is a choice `a_i in M_i` for every role such that

\[
 \sum_i({\bf1}_{h_i}-{\bf1}_{a_i})=-\eta            \tag{2.3}
\]

if and only if `b>=0` and either, equivalently both, of the following Hall
families holds:

\[
 \boxed{|J|\le b(N(J))\quad(J\subseteq I),}          \tag{2.4}
\]

\[
 \boxed{\ell_M(X)\le b(X)\quad(X\subseteq V).}       \tag{2.5}
\]

It suffices in (2.5) to test sets which are unions of accepted menus.

#### Proof

Equation (2.3) says exactly that state `v` is chosen as a tail `b(v)`
times.  Replace `v` by `b(v)` distinguishable capacity copies and join role
`i` to all copies of the states in `M_i`.  An assignment is therefore a
perfect matching of all roles, and (2.4) is Hall's theorem.

If (2.4) holds and `J_X={i:M_i subseteq X}`, then
`N(J_X) subseteq X`, so

\[
 \ell_M(X)=|J_X|\le b(N(J_X))\le b(X).
\]

Conversely, for `X=N(J)`, every role in `J` is counted by `ell_M(X)`, and
(2.5) gives (2.4).  Finally, if (2.5) fails at `X`, take
`J_X={i:M_i subseteq X}` and `Y=N(J_X)`.  Then `Y subseteq X`,
`ell_M(Y)>=ell_M(X)`, and `b(Y)<=b(X)`, so the union of menus `Y` also
fails.  \(\square\)

This theorem is the fixed-head specialization of the protected Hoffman
theorem.  It is an ordinary integral max-flow problem; the corrected
fractional pull clock is neither needed nor sufficient to produce its input
table.

## 3. Spine decomposition and Boolean form

Write the underlying literal order-`d` tuple of a complete state as
`(Q,sigma)`, where `Q` is its first letter and `sigma` is the remaining
`(d-1)`-tuple.  Auxiliary run-age and guard labels are suppressed in this
notation.  Let `V_sigma` contain **all complete-state refinements** whose
underlying tuple has that suffix.  Every accepted refinement of one raw
unsaturated menu in (1.1) lies in one fibre

\[
 \mathcal V_\sigma=\{(Q,\sigma;\xi):Q\ne\varnothing,
                         \ \xi\text{ is an allowed auxiliary label}\}. \tag{3.1}
\]

Let `I_sigma={i:M_i subseteq V_sigma}`.  Since the fibres are disjoint, the
predecessor matching is the direct sum of its fibre matchings.  In
particular, feasibility forces

\[
 b(\mathcal V_\sigma)=|I_\sigma|                     \tag{3.2}
\]

for every used fibre, and, subject to (3.2), it is equivalent to (2.4)
inside every fibre separately.

At the literal-tuple projection, before residence/upper filtering, the
possible first letters of role `i` form the Boolean interval

\[
 [U_i,U_i\cup F_i]
   =\{U_i\cup A:A\subseteq F_i\},
 \qquad U_i\cap F_i=\varnothing.                    \tag{3.3}
\]

The actual accepted menu is a labelled subfamily over this interval; two
different auxiliary histories over the same first letter remain distinct
states.  Thus an exact forbidden cut is a deficient union of accepted
labelled subfamilies of these intervals.  This is a finite and proof-safe separator: a max-flow
minimum cut returns the roles `J`, their literal neighbourhood `N(J)`, and
the integer deficit

\[
 \delta(J)=|J|-b(N(J))>0.                            \tag{3.4}
\]

No mask-degree or marginal shortcut is involved.

## 4. A positive Boolean expansion criterion

For a state `v`, define its accepted menu load

\[
 \Delta(v)=|\{i:v\in M_i\}|.                         \tag{4.1}
\]

### Theorem 4.1 (weighted overlap expansion)

If

\[
 \boxed{\sum_{v\in M_i}{b(v)\over\Delta(v)}\ge1
        \quad\hbox{for every role }i,}               \tag{4.2}
\]

then all predecessor Hall cuts hold and there is an integral protected
completion.

#### Proof

For every `J subseteq I`, sum (4.2) over `i in J` and interchange the sums:

\[
 |J|
 \le\sum_{v\in N(J)}b(v)
       {|\{i\in J:v\in M_i\}|\over\Delta(v)}
 \le\sum_{v\in N(J)}b(v)=b(N(J)).
\]

Now apply Theorem 2.1.  \(\square\)

### Corollary 4.2 (bounded-load raw cubes)

Suppose all raw choices survive, every offered state has `b(v)>=1`, and
`Delta(v)<=Delta` throughout a spine fibre.  If

\[
                         2^{|F_i|}\ge\Delta          \tag{4.3}
\]

for every role in that fibre, then its predecessor matching exists.  The
same conclusion holds with a role-dependent bound
`sum_(v in M_i)b(v)/Delta(v)>=1` after arbitrary protected filtering.

This is an actual expansion statement supplied by the Boolean menus.  Its
load hypothesis is essential: Boolean cardinality alone gives no Hall
surplus.

## 5. Connected Euler skeleton and bounded sidecars

Let `R` choose tails `a_i in M_i` from pairwise distinct roles.  Put

\[
 t_R(v)=|\{i\in R:a_i=v\}|,
 \qquad b_R(v)=b(v)-t_R(v).                          \tag{5.1}
\]

### Theorem 5.1 (fixed-head connected criterion)

Fix an exact intended state support `V_*`.  A protected completion on
`V_*` with at most `c` weak Euler components exists if and only if there is
a reserved set `R` such that

1. `P union {a_i -> h_i:i in R}` spans `V_*` with at most `c` weak
   components;
2. `b_R>=0`, every residual menu is nonempty after restriction to `V_*`,
   and
3. for all residual role sets `J`,

   \[
       |J|\le b_R\left(\bigcup_{i\in J}M_i\right).   \tag{5.2}
   \]

For `c=1` this is an exact connected Euler certificate.

#### Proof

After reserving a role `i`, both its fixed head contribution to `m` and its
arc boundary are transferred to the protected bank.  They cancel at the
head and consume exactly one tail unit at `a_i`; hence the residual demand
is precisely `b_R=b-t_R`.  Theorem 2.1 completes the residual roles.  The
reserved support already supplies the required spanning forest.

Conversely, take a spanning forest with at most `c` components from any
completed support and let `R` be its distinct free-role arcs outside `P`.
The remaining selected tails certify (5.2).  \(\square\)

Now hold `I`, the fixed heads, and all menus unchanged, and let an extra
boundary-only sidecar consist of `q` directed paths or arcs, hence have
boundary whose total positive mass is at most `q`.  If `J_1,...,J_s` are
Hall-deficient role sets with pairwise disjoint neighbourhoods, then every
repairing sidecar obeys

\[
 q\ge\sum_{t=1}^s\delta(J_t).                        \tag{5.3}
\]

Indeed the sidecar must add at least `delta(J_t)` units of boundary capacity
to each disjoint neighbourhood, while one directed path contributes at most
one unit to their total positive boundary.  Thus an `O(1)` boundary-only
sidecar on this fixed table is possible only when the total disjoint-cut
deficit is `O(1)`.  A repair which replaces owner roles, changes head
multiplicities, or changes the chain table is outside (5.3).

## 6. The first raw-menu forbidden cut

The following example uses no residence or upper filtering.  Take depth
`d=1`, owner rank `r=3`, ground set `{0,1,2,3,4}`, and four strict chains
`emptyset < S_i < T_i`.  The guard `y_i`, the sets
`U_i=T_i-S_i`, `F_i=S_i-{y_i}`, and the raw tail menus are:

| `i` | `T_i` | fixed head `S_i` | `y_i` | `U_i` | `F_i` | raw tails |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `034` | `03` | `3` | `4` | `0` | `{4,04}` |
| 1 | `013` | `1`  | `1` | `03`| empty | `{03}` |
| 2 | `023` | `2`  | `2` | `03`| empty | `{03}` |
| 3 | `014` | `04` | `0` | `1` | `4` | `{1,14}` |

All owners and all heads are pairwise distinct, and both endpoint unions of
every trace are proper in its owner.  Relative to the four available heads,
the predecessor neighbourhoods are exactly

\[
 N(0)=\{3\},\qquad N(1)=\{0\},\qquad
 N(2)=\{0\},\qquad N(3)=\{1\}.                      \tag{6.1}
\]

Thus every role has a legal predecessor, but

\[
 J=\{1,2\},\qquad N(J)=\{0\},\qquad\delta(J)=1.     \tag{6.2}
\]

The predecessor matching is impossible.

### Proposition 6.1 (minimality at depth one)

Among depth-one raw unsaturated tables with pairwise distinct owners and
heads, and with every role having a predecessor in the head bank, four
roles are the minimum size of a Hall obstruction.

#### Proof

At depth one a compatibility edge `i -> j` means

\[
 S_j=(T_i-S_i)\cup A,qquad A\subseteq S_i-\{y_i\}.
                                                               \tag{6.3}
\]

Consequently

\[
                         T_i=S_i\cup S_j.             \tag{6.4}
\]

There is no loop because every allowed tail contains the nonempty set
`T_i-S_i`, disjoint from `S_i`.  If both `i -> j` and `j -> i` existed,
(6.4) would give `T_i=S_i union S_j=T_j`, contradicting distinct owners.
Hence the compatibility digraph has neither loops nor directed two-cycles.

With at most three roles, choosing one available outgoing edge at every
vertex produces a directed cycle.  The preceding exclusions force that
cycle to use all three vertices, and those three edges are a perfect
predecessor matching.  Therefore a locally nonempty obstruction needs at
least four roles, and (6.1) attains the bound.  \(\square\)

The example persists at every owner rank `r>=3`: adjoin one common
`(r-3)`-set to every `S_i` and `T_i` and retain the displayed guards.  A
menu state can equal a head only when it contains the whole common set, so
the compatibility graph (6.1) is unchanged.

### Proposition 6.2 (the obstruction exists at every depth)

For every `d>=1` and `r>=d+1` there is a raw depth-`d`, rank-`r`
unsaturated table with pairwise distinct owners and heads in which every
role has a predecessor in the head bank but predecessor Hall fails by one.

#### Construction and proof

Choose positive integers `p_0,...,p_d` summing to `r`.  On a cyclic index
set of length `L=2(d+1)`, take pairwise disjoint coordinate blocks `C_t`
with

\[
                         |C_t|=p_{t\bmod(d+1)}.       \tag{6.5}
\]

For each `i modulo L`, let the ordered head blocks be

\[
 H_i=(C_i,C_{i+1},\ldots,C_{i+d-1}),                 \tag{6.6}
\]

let `U_i=C_(i-1)`, and recover the strict chain by declaring the last `q`
blocks of `H_i` to have union `S_(i,q)`.  Then

\[
 T_i=C_{i-1}\cup C_i\cup\cdots\cup C_{i+d-1}         \tag{6.7}
\]

has rank `r`.  These cyclic interval owners are pairwise distinct.  Choose
any guard in the last block of `H_i`.  The empty subset choice in the first
letter gives the literal tail state

\[
 (C_{i-1},C_i,\ldots,C_{i+d-2})=H_{i-1}.             \tag{6.8}
\]

Every nonempty subset choice adds a point of `C_(i+d-1)` to the first
letter.  Since all head first letters are whole, pairwise disjoint blocks,
no such enriched first letter is a head first letter.  Thus among the head
bank role `i` has the unique predecessor option `H_(i-1)`.  The `L` cycle
roles alone have their cyclic perfect matching.

Now take a fresh block `Z`, disjoint from all `C_t`, with `|Z|=|C_d|`, and
add one extra role with

\[
 H_e=(C_1,C_2,\ldots,C_{d-1},Z),\qquad U_e=C_0.      \tag{6.9}
\]

For `d=1`, (6.9) means simply `H_e=(Z)`.  Its owner has rank
`|C_0|+...+|C_(d-1)|+|Z|=r` and is distinct because it contains `Z`.
Exactly as above, its unique head-bank predecessor is `H_0`.  Hence the
cycle role `1` and the extra role `e` both have neighbourhood `{H_0}`.
This is a Hall cut of deficit one, while every role has a predecessor.
All owner traces have nonempty letters and both endpoint `d`-state unions
are proper, exactly as in the unsaturated theorem.  \(\square\)

Finally, take `p` copies of either construction on disjoint coordinate
blocks (using the depth-one common-core lift when desired).  Equality of
literal states cannot cross copies, so their deficient neighbourhoods are
disjoint.  By (5.3), every boundary-only repair which leaves this
role/head/menu table fixed needs at least `p` sidecar paths.  Hence the raw
unsaturated-menu theorem alone cannot imply a dimension-uniform `O(1)`
boundary-only sidecar on a fixed table at any depth, even before residence
and upper constraints are imposed.  A coupled role or chain-table
replacement is the precise escape not covered by this lower bound.

## 7. Exact remaining all-`k` gate

A positive protected-completion theorem now has a precise target.

1. Choose an exact owner/chain table and literal guards so its accepted
   one-sided menus satisfy either the exact fibre Hall cuts (2.4), or the
   sufficient weighted expansion condition (4.2).
2. Reserve a distinct-role connected skeleton and verify the residual cuts
   (5.2).  Matching feasibility alone does not imply connectedness.
3. Prove that the selected menu states carry the required literal histories
   and an occurrence-level upper witness bank.  These conditions may delete
   Boolean choices but introduce no new tail--head correlation because the
   head is fixed.
4. Bound the total disjoint-cut deficit by `O(1)` if a sidecar is allowed.

The four-role obstruction shows that none of these rows follows merely from
the cardinality `|M_i|=2^(|S_(i,1)|-1)`.  The missing structural assertion is
an overlap/load theorem for the **chosen global chain table**, not another
fractional-clock argument.
