# One-or-two-rail propagation through the named PBBS hook chain

**Date:** 2026-08-05  
**Method:** voltage-one rotation grids, near-hook orbit dichotomy, and
cut-permutation calculus; no computation or search  
**Status:** unconditional for all sufficiently large `m`.  If two
connectors use the same physical near-hook component, they propagate two
rails; if they use different near-hook components, they collapse the two
rails to one.  One connector per later hook then propagates that single
rail.  Thus the named hook block ends with at most two cycles while q1 and
q2 remain exact.  This does not absorb the other action-angle components.

## 1. Named connectors and their common rotation order

Put `n=2m+1`.  For `1<=b<=m-4`, let `G_b` be the selected common-pivot
q2-neutral clean `C6` with component profiles

\[
 H_b=(m-b,1^b),\qquad H_{b+1},\qquad
 J_b=(m-1-b,2,1^{b-1}).
\tag{1.1}
\]

The case `b=m-4` is the separately audited `h=3` endpoint.  Consecutive
gadgets use the same physical `H_b` component.  Its rooted shape cycle has
odd period `p_b` and voltage one.  Hence ground rotation `rho` acts as

\[
                         \rho=g^{p_b(m+1)}
\tag{1.2}
\]

and has order `n`.  After quotienting physical distance by `p_b`, every
fixed edge occurrence has rotation order

\[
 0,m+1,2(m+1),\ldots,(n-1)(m+1)\pmod n.
\tag{1.3}
\]

The multiplier is independent of `b`; the old-edge rotation orbits of
`G_(b-1)` and `G_b` therefore induce the same cyclic order on their common
hook component, up to a fixed offset.

Let `B=12`, a uniform bound on the protected rank-`m` support of one clean
connector including its unchanged q2 companion endpoints, and fix

\[
                         M>10B^2+10.
\tag{1.4}
\]

For the near-hook edge of `G_b`, let

\[
 a_b=|\{\rho^xJ_b^{(0)}:x\in\mathbb Z_n\}|
\tag{1.5}
\]

be the orbit size of its displayed physical component.  The rotation group
is cyclic of odd order, so `a_b` is an odd divisor of `n`, and

\[
 \rho^xJ_b^{(0)}=\rho^yJ_b^{(0)}
 \quad\Longleftrightarrow\quad x\equiv y\pmod {a_b}.
\tag{1.6}
\]

## 2. Paired placement with the near-hook orbit priced

### Lemma 2.1

Suppose two old cuts split a named hook component into arcs each containing
at least `M` placements of the next connector's hook edge.  For all
sufficiently large `n`, choose one placement `x,y` in each arc such that
their protected supports avoid each other and any fixed collection of at
most two neighboring protected supports.  In addition:

1. if `a_b=1`, both cyclic separations of `x,y` are at least `4M`;
2. if `a_b>1`, one may require `x not congruent y (mod a_b)`, so the two
   near-hook edges lie on distinct physical components.

#### Proof

Use the common cyclic order (1.3).  In each old arc take a centered interval
of `M` admissible indices.  The midpoints of complementary arcs are
antipodal, so every pair in these centered intervals is within `2M` of
antipodal.  For `n>=12M`, both cyclic separations are at least `4M`.

No rank-`m` set has a nontrivial rotational stabilizer because
`gcd(m,2m+1)=1`.  Hence two protected supports `U,V` forbid at most
`|U||V|<=B^2` relative rotations.  Choose `x` avoiding at most `2B^2`
absolute exclusions.  With `x` fixed, self-intersection and the two
neighboring supports exclude at most `3B^2` values of `y`.

If `a_b=1`, (1.4) leaves a valid `y`.  If `a_b>1`, then `a_b>=3`, and at
most `ceil(M/a_b)<=M/3+1` of the `M` indices are congruent to `x` modulo
`a_b`.  After removing those and the support exclusions, (1.4) still leaves
a valid `y`.  `square`

## 3. Exact topology of a paired stage

Suppose the current named subsystem has exactly two rails `R_0,R_1`, and
the named `H_b` component is split between them.  Apply protected-disjoint
rotations `G^0,G^1` of `G_b`, with their `H_b` edges on `R_0,R_1`.
Their `H_(b+1)` edges lie on the same fresh named hook component `A`.
Let `D_i` be the physical `J_b` component used by `G^i`.

### Lemma 3.1 (same/different-donor dichotomy)

After both switches:

1. if `D_0=D_1`, the subsystem again has exactly two rails, and material
   from `A,D_0` occurs on both;
2. if `D_0 ne D_1`, the subsystem is exactly one cycle.

#### Proof

The first switch has old edges on the three distinct cycles `R_0,A,D_0`,
so it merges them into one cycle `M`; `R_1` remains.

If `D_1=D_0`, the second switch has one old edge on `R_1` and two on `M`.
Cutting gives three paths.  The clean reconnection multiplies the successor
permutation by an even 3-cycle, so the parity of the number of cycles is
unchanged.  It is positive, even, and at most three, hence exactly two.
The explicit cut permutation from the rigid-split theorem puts one `A` arc
and one `D_0` arc on each output rail.

If `D_1 ne D_0`, the second switch instead has old edges on the three
distinct cycles `R_1,M,D_1`; a clean three-way switch merges them into one.
`square`

Both cases preserve q1 and q2 exactly because each connector is neutral and
the protected supports are disjoint.

### Lemma 3.2 (single-rail propagation)

If the current named subsystem is one cycle containing the named `H_b`
component, one protected rotation of `G_b` merges into it fresh components
`H_(b+1)` and `J_b` and leaves one cycle.

#### Proof

The full named `H_b` component lies in the current cycle, so every rotated
placement of the displayed `H_b` edge lies on it.  The other two action
profiles are new at stage `b` and hence their physical components are
fresh.  A bounded number of previous supports excludes only a bounded
number of rotations; choose another.  The old edges then lie on three
distinct cycles, which the clean switch merges into one.  `square`

## 4. Induction through the named chain

### Theorem 4.1

For all sufficiently large `m`, apply the rigid single-soliton split, then
two rotations of `G_1`, one on each rigid arc.  At every later stage use
two copies while two rails remain, and one copy after the first collapse.
The supports can be chosen pairwise disjoint whenever their triples are
nonconsecutive and literally disjoint for neighboring stages.  Every switch
is selected and q2-neutral, and the final named subsystem has one or two
cycles.

The union of those cycles contains every named hook component and every
near-hook component selected by the construction.  If two rails survive,
both contain material from every selected named component.

#### Proof

The rigid arcs contain linearly many placements of `G_1`.  Here
`J_1=(m-2,2)` is the `B` component of the explicit rotation-rigid connector;
its displayed voltage is `2`, a unit modulo odd `n`, so `a_1=1`.  Choose
two protected-disjoint placements on opposite rigid arcs with separation in
`[4M,n-4M]`.  Lemma 3.1 gives two rails containing `H_2,J_1`.

Suppose the two cuts inherited on `H_b` have separation in
`[4M,n-4M]`.  By the common order (1.3), each hook arc contains at least
`4M-1` placements of `G_b`.

If `a_b=1`, Lemma 2.1 selects a protected-disjoint pair.  Lemma 3.1 keeps
two rails, and the induced cuts on `H_(b+1)` again have separation in
`[4M,n-4M]`.

If `a_b>1`, Lemma 2.1 selects rotations on distinct `J_b` components.
Lemma 3.1 collapses the subsystem to one cycle.  Lemma 3.2 then propagates
that one cycle through every remaining stage.

Nonconsecutive connector types have disjoint action profiles, so only the
bounded neighboring supports enter the exclusions.  Induction reaches
`b=m-4`.  The disjoint local q1/q2 identities compose exactly.  `square`

## 5. Consequence and remaining gap

The complete named block has at most two cycles.  The bounded-graphic-
defect q2 Pascal theorem can puncture one selected turn per cycle, at cost
at most two q2/owner sidecar occurrences per puncture.  Hence the named
block has q2 graphic sidecar at most

\[
                         2\cdot2=4.
\tag{5.1}
\]

If any stage has `a_b>1`, the block has one final cycle and this charge is
at most two.

The theorem does not absorb the exponentially many other action-angle
components in the hook and non-hook sectors.  The remaining global theorem
is an angle-level leaf-plucking/attachment theorem giving a physically
disjoint q2-neutral attachment of every outside selected PBBS component to
this bounded-rail spine.  No q3, residence, arbitrary-upper, or common-cap
claim is included.
