# Folded C8: a conditional antidiagonal address template and a nonresident minimum halo

Date: 2026-08-01  
Lane: Thread D, four-block C8 host/compiler interface  
Status: exact finite **conditional address template** for `2<=d<=12`; exact
six-label minimum-halo theorem; dimension-uniform flat-residence obstruction.
The authenticated endpoint forest supplies only one suffix ray and does not
realize the two cross banks simultaneously.

## 0. Verdict

On the formal canonical screened aligned-source/opposite-ray words, the
global width--OR--cap address bijection sends the native ray cells to
explicit source cells and conversely.  If both blocks survived in one
owner-legal endpoint state, these addresses would provide the candidate
cross tickets

\[
 P_0(j)\longleftrightarrow S_1(j+1),\qquad
 P_1(j)\longleftrightarrow S_0(j+1)       \tag{0.1}
\]

as `2(d-1)` paired tickets, each ticket consisting of two distinct formal
interval cells.  Altogether the four target banks use `4(d-1)` distinct
candidate addresses.  The address identity holds with the active screen
`{a1,a3}`, with the host screen
`{z,a1,a3}`, and with either screen recycled in an already present common
immediate-left letter.  The recycled formal screen has packet source charge
zero.

This is **not** a combined physical-bank theorem.  On the unmodified
common-endpoint cuts, the independent exact census has
`exact_one_ray_comparators=0` for every `2<=d<=12`; the best cuts have upper
support 15.  The three-edge seam restores support 16 but may move the prefix
coordinate to the other component.  The authenticated forest therefore
supplies one literal suffix-ray rethread only.  Simultaneous realization of
both cross matchings in one owner/cap/guard state remains open.

If a future host embeds all candidate cells in one physical endpoint,
pulling them back through the address bijection reduces matching completion
to forced-edge Hall in one fixed complete cap state.  That implication is
conditional on the missing topology/occurrence embedding.  Owner legality,
both `q1` sidecars, complete address guards, and regeneration are not
consequences of the address identity.

The smallest direct phase-dependent lower-palette halo does not supply that
closure.  In omitted-pair notation it is

\[
\begin{array}{c|cc}
 &0&1\\ \hline
 L&ah-ax-bx-hx&bh-bx-ax-hx,\\
 R&yt-ay-by-bt&yt-by-ay-at.
\end{array}                                             \tag{0.2}
\]

Its lower counters agree shore by shore and its two upper mismatches cancel.
But `h` on the left and `t` on the right have owner-presence trace `0110`.
Thus no flat depth-`d` source can realize it for `d>=2`.  In the literal
full chronology, maximal erosion loses `h` at zero-based owner rows `1,2`
and `t` at rows `d+4,d+5` for every audited `4<=d<=64` and in both phases.

Consequently the seven planted-host menu does not by itself make the
four-block macro resident/common-cap at zero accumulated length.  It gives
the correct ray values and the two useful typed endpoint caps, while a
simultaneous two-ray topology, nonlocal equal-length resident host, and then
forced-edge Hall remain necessary.

## 1. Canonical endpoint words and target banks

Let `S0,S1` be the aligned folded source pair and `G1,G0` the opposite ray
pair.  After the unique cancelling cyclic cut, prepend either common screen

\[
 E=\{a_1,a_3\}\quad\hbox{or}\quad E=\{z,a_1,a_3\}.       \tag{1.1}
\]

Write the resulting endpoint words as `W^-` and `W^+`.  If the actual
immediate-left ambient letter already contains `E`, it replaces the fresh
screen; since that letter occupies the same address in both phases, this is
the zero-charge recycled form.

For `1<=j<d`, put

\[
\begin{aligned}
 P_0(j)&=\{z,a_3\}\cup\{f_1,\ldots,f_j\},&
 P_1(j)&=\{z,a_1\}\cup\{f_1,\ldots,f_j\},\\
 S_0(j+1)&=\{z,a_1\}\cup\{f_{j+1},\ldots,f_d\},&
 S_1(j+1)&=\{z,a_3\}\cup\{f_{j+1},\ldots,f_d\}.
                                                               \tag{1.2}
\end{aligned}
\]

These `4(d-1)` target values are pairwise distinct.

Let `m=|S_epsilon|` and define zero-based addresses

\[
\begin{array}{ll}
 N_P(j)=[m+1,m+j],&N_S(j)=[m+j+1,m+d],\\
 A_P(j)=[p_L,p_L+j-1],&A_S(j)=[p_L+j+1,p_R],             \tag{1.3}
\end{array}
\]

where

\[
                        p_L=4d+12,\qquad p_R=p_L+d.       \tag{1.4}
\]

The `N` cells are native opposite-ray cells and the `A` cells lie in the
aligned source block.  Notice that the source address `p_L+j` is strictly
between `A_P(j)` and `A_S(j)`; it belongs to neither cell.

## 2. Exact address formulas

Let `hat W_p=W^-_p union W^+_p` and label an interval address `I` by

\[
 (|I|,\operatorname{OR}_{W^\epsilon}(I),
       \operatorname{OR}_{\widehat W}(I)).                \tag{2.1}
\]

The frozen canonical bijection `Phi` pairs lexicographically equal-rank
addresses inside each label fibre.

### Theorem 2.1 (conditional canonical-word address identity)

For both screens in (1.1), in fresh and recycled form, and every audited
`2<=d<=12`, `Phi` satisfies

\[
\begin{array}{llll}
 \Phi(N_P(j))=A_P(j),&&
 \Phi(N_S(j))=A_S(j),\\
 \Phi^{-1}(N_P(j))=A_P(j),&&
 \Phi^{-1}(N_S(j))=A_S(j).                              \tag{2.2}
\end{array}
\]

The literal OR table is

\[
\begin{array}{c|cc}
 &N_P(j)&N_S(j)\\ \hline
 W^-&P_1(j)&S_1(j+1)\\
 W^+&P_0(j)&S_0(j+1)
\end{array},
\qquad
\begin{array}{c|cc}
 &A_P(j)&A_S(j)\\ \hline
 W^-&P_0(j)&S_0(j+1)\\
 W^+&P_1(j)&S_1(j+1).
\end{array}                                               \tag{2.3}
\]

Moreover every pair in (2.2) has the same interval cap in (2.1).

#### Proof

The explicit formal source and ray words give (2.3) by direct union.  Enumerating
all interval addresses and sorting the complete fibres (2.1) gives (2.2).
The audit checks the formula, not merely fibre cardinality.  It also checks
that the old and new address projections are bijective and that the cap
unions agree.  Screen recycling changes only the common address immediately
to the left and hence leaves all four displayed cells and their images
unchanged.  This proves the finite statement. \(\square\)

### Corollary 2.2 (candidate two-cross address template)

In the formal word `W^+`, the candidate address assignment for the first
ticket in (0.1) is

\[
                  N_P(j)\text{ for }P_0(j),\qquad
                  A_S(j)\text{ for }S_1(j+1),            \tag{2.4}
\]

and for the second it is

\[
                  A_P(j)\text{ for }P_1(j),\qquad
                  N_S(j)\text{ for }S_0(j+1).            \tag{2.5}
\]

All addresses in (2.4)--(2.5), over every `j`, are distinct in the formal
canonical word.  Hence they form a cell-disjoint **candidate** bank on that
word.  A ticket has two cells; it is not a license to collapse a prefix and
suffix into one compiler cell.

The corollary does not say that these four banks survive the owner-legal
cut/seam/forest operation in one component.  They do not in the current
authenticated endpoint: its exact comparator count is zero.  This missing
simultaneous occurrence condition precedes every compiler Hall calculation.

## 3. Conditional compiler completion gate

Assume first that a physical endpoint contains all four candidate banks in
one owner-legal state.  Fix one legal complete cap/guard state.  Let `F^+` be the forced new edges
in (2.4)--(2.5) and pull them back through `Phi` to `F^-`.  Let `G^-` be the
old target--occurrence compiler graph.

### Theorem 3.1 (forced-bank completion)

Under the preceding physical-embedding hypothesis, the cross bank extends
to a complete new compiler matching iff:

1. every edge of `F^-` is legal in `G^-`; and
2. after deleting the targets and cells saturated by `F^-`, the residual
   graph satisfies Hall:

\[
              |N_{G^- - V(F^-)}(X)|\ge |X|              \tag{3.1}
\]

for every residual target set `X`.

#### Proof

Necessity is immediate.  Hall supplies a residual matching, whose union with
`F^-` is complete.  Applying the address isomorphism gives the desired new
matching.  Conversely every complete new matching containing `F^+` pulls
back to such an old matching. \(\square\)

For a named old matching, (3.1) is equivalently a vertex-disjoint
alternating-linkage condition.  If the packet is a genuine private
full-block refinement, the forced packet cells are outside the transported
background image and residual Hall is automatic.  Otherwise (3.1) is the
exact remaining matching row.

This theorem deliberately begins **after** a legal common cap state has
been fixed.  Pointwise union caps and the finite fibre identity do not prove
owner erosion, `q1` sidecars, deadline guards, or source regeneration.

## 4. The minimum direct halo and its obstruction

Use the common owner universe `D` and encode an owner by its omitted pair.
Set

\[
 a=a_1,\quad b=a_3,\quad h=f_{d+1},\quad
 x=f_2,\quad y=f_{d-1},\quad t=f_0.                     \tag{4.1}
\]

For a Johnson edge between omitted pairs `E,E'`, its lower colour is
`E union E'` and its upper omitted label is `E intersect E'`.  The circuit
(0.2) therefore has phase-equal lower counters separately on each halo;
its only upper discrepancy is the transposition of `D\a,D\b`, which cancels
between the two halos.

### Theorem 4.1 (natural-alphabet minimum)

Among simple phase-dependent left/right paths on the alphabet
`{a,b,h,t,x,y}`, with at most three edges per halo, exact phase equality of
the combined lower and upper counters and owner-disjoint shores requires at
least four extra owner positions per phase.  There are five labelled
minimum solutions.  Exactly one is obtained by applying `a<->b` to the
entire phase-zero circuit, namely (0.2).

Every one of the five minimum solutions has left `h` trace `0110` and right
`t` trace `0110`.

#### Proof

Enumerate the 15 omitted-pair vertices and all simple endpoint paths of one,
two, or three edges.  Hash each phase-zero pair of disjoint paths by its
two exact counters and join phase-one paths only on equal hashes.  The counts
by number of extra owner positions are

\[
                           0,0,0,0,5.                    \tag{4.2}
\]

The five retained rows are then checked directly for their two coordinate
traces.  This is complete only in the stated natural alphabet and edge
range. \(\square\)

The finite scope is not used to infer the all-label residence lower bound.
For the involutive separated left halo, if every omitted pair contained
`h`, deleting `h` would give an `a`-to-`x` label walk whose edge multiset is
`a<->b` invariant.  Its odd-degree endpoint set `{a,x}` is not invariant, a
contradiction.  Hence an internal positive `h` run is forced.  A flat
depth-`d` source can create an internal positive owner run only with length
at least `d+1`, so a resident separated left halo has at least `d+2` edges.
The right `t` argument is identical.  This is the dimension-uniform growing
halo obstruction.

For the literal minimum (0.2), the independent full replay is sharper:
maximal erosion is nonempty but reconstructs every owner except rows `1,2`
and `d+4,d+5`, losing `h,h,t,t` respectively, for both phases and every
`4<=d<=64`.  This agrees exactly with the two `0110` traces.

## 5. Consequence for the seven-host menu

The seven planted rays remain a correct partition of the directed source
deck differences.  Two members supply the typed endpoint caps

\[
 X_L=K\cup\{z,a_1,a_3,f_1\},\qquad
 X_R=K\cup\{z,a_1,a_3,f_d\}.                            \tag{5.1}
\]

The common coatom rail between them is owner-simple, Johnson, internally
resident, and has a nonzero maximal inverse.  The address theorem above
settles only the conditional address algebra.  It does not settle the
simultaneous physical antidiagonal occurrence question.

These facts do **not** combine into a zero-length regenerative four-block
macro.  The seven hosts are not letters of the current sharp sources; their
one-sided ray identities do not give the cross-host internal/prefix/suffix
deck; the current forest has only one suffix ray; and the minimum direct
palette circuit fails maximal reconstruction.
The literal next theorem must provide one of:

1. a simultaneous prefix/suffix two-cross host plus a prospectively planted,
   nonlocal equal-length resident halo/rethread, together with its owner and
   `q1` rows; or
2. a nonflat facet/compiler host in which the missing prefix occurrence and
   the two `0110` traces are not
   depth-`d` source runs.

In either case it must fix one complete cap/guard state and pass the
forced-edge Hall condition (3.1).  Signed counter cancellation and the
seven formal ray identities are insufficient substitutes.

## 6. Audit

Run

```text
python3 scratch/audit_threadD_folded_c8_antidiagonal_halo_gate_20260801.py --write
```

The replay checks both screens and both fresh/recycled formal words for every
`2<=d<=12`; all canonical address formulas, literal ORs, cap unions,
distinctness, and the natural-alphabet halo census.  It also imports the
independent common-endpoint audit and asserts
`exact_one_ray_comparators=0` at every depth.  The independent literal
maximal-erosion replay through `d=64` is in
`scratch/audit_threadD_c8_phase_halo_circuit_20260801.py`.
