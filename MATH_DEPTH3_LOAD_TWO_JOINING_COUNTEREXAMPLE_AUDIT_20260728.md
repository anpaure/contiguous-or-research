# Depth-three joining: multiplicity two is not enough

Date: 2026-07-28

Status: theorem audit, sharp local obstruction, and independently verified
Johnson counterexample.

## 0. Verdict

Theorem 3.1 of
`MATH_DEPTH_THREE_TRANSITION_SYSTEM_AND_COMMON_ORDER_GATE_20260728.md`
is correct: disconnected transition components can always be joined by
`c-1` local switches, pair--pair switches preserve the complete
depth-three point-degree vector, and at most the two end-stub switches can
change the boundary marginals.

The proposed support upgrade is false:

> Initial load at least two on every depth-three target does **not** imply
> that the transition components can be joined while retaining complete
> depth-three support.

There are two versions of the obstruction below.

1. The smallest abstract obstruction has rank `s=4` and three transition
   components.  Rank at most three and two components can never obstruct.
2. A machine-checkable `k=12, s=4` Johnson multigraph has complete
   rank-two support with minimum load two, but no connected local
   transition system in its fixed-end pairing fibre retains that support.

Thus the remaining theorem needs a **label-congestion/cut condition**, not
only a pointwise multiplicity floor.

## 1. Audit of the component-joining theorem

Let two transition components meet at an owner `A`.  Suppose the selected
transition pairs omit the unordered coordinate pairs

\[
 P=\{x,y\},\qquad Q=\{u,v\}\subseteq A,
\]

and hence carry depth-three labels

\[
 S=A\setminus P,\qquad T=A\setminus Q.
\]

Deleting the two transition edges and using either cross-pairing merges the
two components.  One of the two cross-pairings is safe.  If two cycles are
joined, the result is a cycle; if the unique path and a cycle are joined,
the result is a path.  This proves the `c-1` assertion exactly as in
Theorem 3.1.

The point-degree assertion is also exact.  The sum of the two old label
incidence vectors is

\[
 2\mathbf 1_A-\mathbf 1_P-\mathbf 1_Q.
\]

Every cross-pairing has the same multiset of four omitted coordinates, so
the sum of the two new incidence vectors is identical.

For a stub--pair switch, the unpaired copy and one member of the pair are
paired and the other member becomes the new stub.  It joins the unique path
to a cycle and keeps the stub at the same owner type.  Once this has been
done at an endpoint owner, the enlarged path has a genuine transition pair
there, so that endpoint never forces a second stub--pair operation.  This
also remains true when the two global endpoints have the same owner type.

Two wording qualifications are useful.

* A pair--pair switch always replaces two **pair occurrences**, but its
  label multiset need not change.  Thus “two others” should not be read as
  “two distinct new labels.”
* Point-degree preservation applies to pair--pair switches.  The at most
  two stub--pair switches are precisely the stated exceptions.

No counterexample to Theorem 3.1 itself was found.

## 2. Exact local support rule

### Lemma 2.1 (free and destructive joins)

For two safe pairs at one owner `A`:

1. if `P=Q` or `P\cap Q\ne\varnothing`, there is a cross-pairing which
   preserves the old label multiset `\{S,T\}` exactly;
2. if `P\cap Q=\varnothing`, both cross-pairings delete one occurrence of
   each of `S,T`, and neither new label equals `S` or `T`.

Consequently a disjoint-pair join is support-preserving at the moment it is
made if and only if the current loads of both deleted labels are at least
two.

#### Proof

If, for example, `P=\{x,y\}` and `Q=\{x,v\}`, cross-pair the copy of `x`
from the first pair with `v`, and `y` with the copy of `x` from the second.
The two new omitted-coordinate types are `Q` and `P`.  The same copy-level
crossing works when `P=Q`.

If `P,Q` are disjoint, every cross-pair contains one coordinate of `P` and
one of `Q`; it is therefore neither `P` nor `Q`.  Since a label at the fixed
owner `A` determines its omitted pair uniquely, neither old label is
recreated. \(\square\)

The failure of the load-two heuristic is therefore cumulative: a label
with load two can pay for one destructive join, but not for two.

## 3. Smallest abstract obstruction

Let `p,q,r` be pairwise disjoint two-sets and put

\[
 A=p\cup q,\qquad B=p\cup r.
\]

Take three transition components `C_1,C_2,C_3` whose only intercomponent
contacts are

\[
 C_1\;--A--\;C_2\;--B--\;C_3.
\]

At `A`, let the pair in `C_1` omit `p` and the pair in `C_2` omit `q`.
Their labels are respectively `q` and `p`.  At `B`, let the pair in `C_2`
omit `r` and the pair in `C_3` omit `p`; their labels are `p` and `r`.
Give `q` one additional private occurrence in `C_1` and `r` one additional
private occurrence in `C_3`.  Pad any other required labels privately.
Initially every required label has multiplicity at least two, and `p` has
multiplicity exactly two.

Any connected final transition system must cross-pair at both `A` and `B`,
because those contacts are bridges of the component-contact graph.  The
omitted pairs are disjoint at both contacts.  Lemma 2.1 therefore deletes
both occurrences of `p`; the cross labels at `A` and `B` cannot equal `p`.
Hence complete support is impossible.

This is minimal in the two relevant parameters.

* For `s\le3`, two two-subsets of an owner cannot be disjoint.  Every join
  has a label-preserving cross-pairing.
* With only two transition components, one join is enough.  A destructive
  join removes at most one occurrence of either old label, so initial load
  two leaves both labels present.

Thus `s=4` and three components are the smallest abstract failure.  This
statement is about the local transition/contact system.  It does not claim
that the smallest full-layer Johnson certificate has `k=6` or three core
components.

## 4. Full Johnson certificate

The proof object is

* `scratch/depth3_load2_joining_counterexample.json`, SHA-256
  `fa3679b3aebc44a0c62c2da9a91b0cbe613ee6bf3427baab09862e69bdd20128`;
* `scratch/verify_depth3_load2_joining_counterexample.py`, SHA-256
  `6c75ce7373a04d03e7f44b759c0dd98990b352193f968b260664a6df165bf4fa`.

It has `k=12`, owner rank `s=4`, four core transition cycles, and thirty
auxiliary cycles.  The verifier checks all of the following directly.

1. Every displayed cycle is a safe closed walk in `J(12,4)`: consecutive
   owners intersect in rank three and every consecutive triple intersects
   in rank two.
2. The core components meet in exactly the path

   \[
   K_0\;--0123--\;K_1\;--0145--\;K_2\;--2345--\;K_3.
   \]

3. Every auxiliary cycle is disjoint from the last three macro components,
   contains the common hub `0138`, and has the same hub label `13`.
   Equal-type pair--pair switches therefore merge all auxiliary cycles into
   `K_0` without changing a label.  Opening one remaining hub pair creates
   the two global end stubs.
4. After that opening, every one of the `\binom{12}{2}=66` rank-two labels
   has load at least two.  The labels

   \[
   p=01,\qquad q=23,\qquad r=45
   \]

   have load exactly two.
5. Rebuilding the owner-to-pair-type incidence independently gives 217
   owner types.  Exactly three owners have more than one omitted-pair type:

   \[
   0123:\{01,23\},\qquad
   0145:\{01,45\},\qquad
   2345:\{23,45\}.
   \]

   At every other owner, all distinguishable pair copies have one common
   omitted-coordinate type.  Any safe re-pairing there therefore preserves
   its label multiset.

At each of the three flexible owners there are four stubs and exactly three
perfect matchings: the original within-component matching and the two
cross-matchings.  Thus the `3^3` enumeration is exhaustive for the entire
fixed-end local-pairing fibre, not merely for the greedy `c-1` joining
sequence.  A connected transition graph must use a cross state at all
three contact owners.  Doing so deletes both occurrences of each of
`01,23,45`; none is recreated.  There are eight connected bridge states
and zero support-preserving connected states.

The independent audit command is

```bash
python3 scratch/verify_depth3_load2_joining_counterexample.py
```

and returns

```text
{"connected_bridge_states": 8, "core_components": 4,
 "critical_initial_loads": {"01": 2, "23": 2, "45": 2},
 "hub_gadgets": 30, "k": 12,
 "minimum_initial_load_after_opening": 2,
 "multi_pair_type_owners": 3, "owner_types": 217, "rank": 4,
 "support_preserving_connected_states": 0, "verified": true}
```

Repeated Johnson edge *types* cause no issue: the object is explicitly a
multigraph, so every occurrence is a distinguishable edge copy.  The safe
cycles pair those copies locally and the hub switches operate on copies.

## 5. The correct replacement condition

For a depth-three label `S`, define its disposable budget

\[
                         b_S=m_S-1.
\]

A disjoint-pair join consumes one unit from each of its two old labels; an
intersecting-pair join can be chosen with zero label cost.  The certificate
fails because the mandatory bridge demand of each critical label is two,
while its disposable budget is one.

### Proposition 5.1 (budgeted spanning-tree sufficient condition)

Let the initial transition components have one distinguished path and the
rest cycles.  Suppose there is a spanning tree of their contact graph such
that every tree edge is assigned

* an owner shared by its endpoint components;
* one transition-pair occurrence in each endpoint component;
* a safe cross-pairing;

and the assigned pair occurrences are distinct.  Charge zero when the two
omitted pairs intersect and charge one to each deleted old label when they
are disjoint.  If, for every label `S`, the total charge is at most `b_S`,
then the components can be joined into one path without creating a
depth-three hole.

#### Proof

Root the tree at the unique path component and contract its edges from the
leaves inward.  A subtree not containing the root is a cycle; the root
subtree is a path.  The assigned pair occurrences are distinct, so the pair
needed at a later contraction has not been removed earlier.  The topology
argument of Theorem 3.1 shows that every contraction produces the required
cycle or path.  Lemma 2.1 gives zero loss on intersecting joins.  On
disjoint joins, the assumed charge inequality leaves every old label with
at least one occurrence.  New labels only add slack. \(\square\)

This condition is sufficient, not necessary: a more general sequence may
use labels created by earlier switches.  It is nevertheless the first
noncircular condition that distinguishes the positive cases from the
load-two counterexample.

For a rigid contact tree in which each contact owner has exactly one pair
on each side and no other owner permits label-changing re-pairing, there is
an exact finite criterion.  Every contact must be crossed.  Choose one of
the two cross-pairings at each contact; let `d_S` count the old occurrences
of `S` thereby deleted and `a_S` the new occurrences of `S` thereby added.
Then the resulting system is support-preserving if and only if

\[
                         m_S-d_S+a_S\ge1
                         \qquad\text{for every }S.
\tag{5.1}
\]

The simpler budget inequality `d_S\le m_S-1` is sufficient in general and
is exact when no mandatory cross-pairing can recreate a charged label.
That non-recreation hypothesis holds for the three critical labels in the
verified certificate: `d_p=d_q=d_r=2`, `a_p=a_q=a_r=0`, and
`m_p=m_q=m_r=2`.

## 6. Consequence for the common-order gate

The histogram `2^2577 3^426` at `k=15` is useful redundancy, but it does
not by itself close transition connectivity.  A proof must additionally
produce one of the following.

1. a component-contact spanning tree whose destructive label congestion is
   at most one on every load-two target and at most two on every load-three
   target;
2. a stronger exchange theorem showing that labels created by earlier
   switches can be routed to pay later bridge demands; or
3. a connected transition system from the outset.

Point-degree preservation cannot substitute for this condition: every
bridge switch in the counterexample preserves the complete point-degree
vector while destroying support.
