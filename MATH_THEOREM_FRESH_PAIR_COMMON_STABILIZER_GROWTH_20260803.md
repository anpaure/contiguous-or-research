# Fresh-pair common stabilizer and central-band orbit growth

**Date:** 2026-08-03  
**Status:** unconditional arithmetic theorem and conditional interface for
same-parity quotient induction.  No finite computation is used.

## 0. Outcome

The same-parity transition from an odd ground set of size `k=2m-1` to one
of size `k+2` has a natural common symmetry: rotate the `k` old coordinates
and fix the fresh pair.  Unlike using unrelated rotations on the parent and
child, this is one literal group action on the complete transition.

Every old-coordinate subset whose rank lies within `a` of `m` has orbit
order at least

\[
                         \frac{k}{|2a+1|}.             \tag{0.1}
\]

Consequently, throughout any central band of width `O(sqrt(k))`, every
orbit order is `Omega(sqrt(k))`.  In particular:

* the two parent Middle-Levels shores are free;
* the three fresh-pair sectors of the child central layer have orbit order
  at least `k/3`; and
* every addressed object retaining a central-band old-subset label also has
  growing orbit order.

Therefore a uniform `O(1)` defect in a stabilizer-pure central-band gate
vanishes for all sufficiently large dimensions, stratum by stratum.  The
result supplies the growing **common** modulus requested by the
tap-decorated same-parity induction theorem.  It does not construct the
finite quotient state, the upper-complete carrier, the protected signature,
or the literal suffix router.

## 1. Orbit order of a cyclic subset

Let `C_k=<rho>` rotate `[k]`, and let `S` be a subset of rank `s`.  If its
stabilizer has order `h`, then every stabilizer orbit on coordinates has
size `h`: no nonidentity coordinate rotation fixes a coordinate, so the
stabilizer acts freely on `[k]`.  The invariant set `S` is a union of these
coordinate orbits.  Hence

\[
                         h\mid k,\qquad h\mid s.      \tag{1.1}
\]

The orbit order of `S` is

\[
                         q(S)=\frac{k}{h}.            \tag{1.2}
\]

### Lemma 1.1

For every `s`-subset,

\[
                         q(S)\ge\frac{k}{\gcd(k,s)}.  \tag{1.3}
\]

For a fixed subset `S`, equality holds exactly when its stabilizer has order
`gcd(k,s)`.

### Proof

Equation (1.1) gives `h<=gcd(k,s)`.  Substitute in (1.2).  Equality has
the stated meaning. \(\square\)

## 2. Odd central-band arithmetic

Put

\[
                         k=2m-1,\qquad s=m+a,         \tag{2.1}
\]

where `a` is any integer for which `0<=s<=k`.  Euclid's algorithm gives

\[
 \gcd(2m-1,m+a)\mid 2(m+a)-(2m-1)=2a+1.            \tag{2.2}
\]

Since `2a+1` is a nonzero odd integer,

\[
                         \gcd(k,s)\le |2a+1|.         \tag{2.3}
\]

### Theorem 2.1 (central-band orbit lower bound)

Every rank-`m+a` subset of `[2m-1]` has orbit order at least

\[
                         q\ge\frac{2m-1}{|2a+1|}.     \tag{2.4}
\]

In particular, if `|a|<=D`, then

\[
                         q\ge\frac{k}{2D+1}.          \tag{2.5}
\]

### Proof

Combine Lemma 1.1 with (2.3). \(\square\)

### Corollary 2.2 (the parent middle shores are free)

The ranks `m-1` and `m` have `a=-1` and `a=0`.  In both cases
`|2a+1|=1`, so every orbit has order `k`.

This recovers the freeness of both shores of `ML_m` without a separate
case argument.

### Corollary 2.3 (deadline-scale bands have growing modulus)

Let `D(k)=O(sqrt(k))`.  Every subset in the old-coordinate rank band

\[
                         |s-m|\le D(k)                \tag{2.6}
\]

has orbit order

\[
                         q=\Omega(\sqrt{k}).           \tag{2.7}
\]

For the OR-word deadline `d(k)=Theta(sqrt(k))`, every target, port, or
capacity object retaining such an old-subset label therefore has a modulus
tending to infinity.

### Corollary 2.4 (residual-subgroup version)

Let `H<=C_k` have order `h`.  A rank-`m+a` subset has `H`-orbit order at
least

\[
                         \frac{h}{|2a+1|}.             \tag{2.8}
\]

### Proof

If an `H`-stabilizer has order `t`, then its coordinate cycles all have
length `t`, so `t` divides both `h` and the subset rank `m+a`.  Since
`h|k`,

\[
 t\le\gcd(h,m+a)\le\gcd(k,m+a)\le |2a+1|.
\]

The `H`-orbit has order `h/t`, proving (2.8). \(\square\)

## 3. The common fresh-pair action

Let the parent coordinates be `[k]`, and add a fresh ordered pair
`{u,v}`.  Let `C_k` rotate `[k]` and fix `u,v`.  This is one action on:

* every parent subset;
* every child subset of `[k] union {u,v}`;
* every transition incidence which remembers its old-coordinate part; and
* every addressed physical object whose schedule, port, cap, and capacity
  labels are transported equivariantly.

If a child set has total rank `r'` and contains exactly `b in {0,1,2}`
fresh coordinates, its orbit order is the orbit order of its old part,
whose rank is `r'-b`.

For the child central rank `r'=m+1`, the three old ranks are

\[
                         m+1,\qquad m,\qquad m-1.    \tag{3.1}
\]

### Theorem 3.1 (child central-sector modulus)

Under the common old-coordinate action, every child central owner has orbit
order at least

\[
                         k/3.                         \tag{3.2}
\]

The one-fresh and two-fresh sectors are in fact free; only the zero-fresh
sector can have a shorter orbit, and then its order is still at least
`k/3`.

### Proof

The ranks `m` and `m-1` are free by Corollary 2.2.  For rank `m+1`, put
`a=1` in Theorem 2.1, giving order at least `k/3`. \(\square\)

The same argument applies to any child central band whose old ranks remain
within `D` of `m`: every orbit order is at least `k/(2D+1)`.

## 4. Addressed objects inherit the lower bound

Let an addressed object `omega` carry an old-subset label `S(omega)` and
suppose the action preserves the projection

\[
                         \omega\longmapsto S(\omega). \tag{4.1}
\]

Then

\[
 \operatorname{Stab}(\omega)
       \subseteq \operatorname{Stab}(S(\omega)),      \tag{4.2}
\]

so

\[
                         |C_k\omega|\ge |C_kS(\omega)|. \tag{4.3}
\]

### Corollary 4.1

Every addressed port, cell, sink, node-split capacity, or transition arc
which retains a central-band old-subset label has orbit order at least the
bound in Theorem 2.1.

The qualification “retains” is load-bearing.  Quotienting away the old
label, identifying several physical addresses, or routing through a
fresh-only fixed bottleneck may create a short orbit and destroys the
conclusion.

## 5. Bounded defects become exact in the common action

Fix a constant `C`.  Decompose an addressed invariant matching or flow gate
by exact orbit order, with capacity-faithful period strata as in the
stabilizer-stratified defect theorem.  Suppose every period stratum has
defect or corank at most `C`.

### Theorem 5.1 (central-band exactness from bounded quotient defect)

For every old-rank band `|s-m|<=D(k)` satisfying

\[
                         \frac{k}{2D(k)+1}>C,          \tag{5.1}
\]

every stabilizer-pure matching and suffix-flow gate in that band saturates
exactly.

In particular, (5.1) holds eventually whenever `D(k)=O(sqrt(k))`.

### Proof

Every exact orbit order in the band is greater than `C` by Theorem 2.1 and
Corollary 4.1.  On an order-`q` stratum, matching deficiency and suffix
corank are nonnegative multiples of `q`.  A number at most `C<q` is zero.
Apply this separately to every stratum. \(\square\)

### Corollary 5.2 (fully pinned residual subgroup)

Let `H_k<=C_k` have order `h_k`.  Suppose every finite-capacity object of
one complete `H_k`-invariant matching or flow gate retains an equivariant
old-subset label in the band `|s-m|<=D(k)`, and suppose its exact-period
strata are capacity-faithful and have defect at most `C`.  If

\[
                         \frac{h_k}{2D(k)+1}>C,        \tag{5.2}
\]

then every stratum of that gate is exact.

### Proof

Corollary 2.4 and addressed-label inheritance give orbit order at least
`h_k/(2D(k)+1)` on every finite physical object.  This exceeds `C`; apply
periodwise matching or suffix-corank divisibility. \(\square\)

This avoids two false requirements:

1. the parent and child do not need independent full coordinate rotations;
   the one old-coordinate `C_k` action is common to both;
2. the action need not be globally free; growing exact-period strata are
   enough.

## 6. Interface with same-parity induction

The tap-decorated quotient induction requires one common residual
stabilizer on a transition arrow, not unrelated symmetries at its two
levels.  The fresh-pair action supplies a canonical candidate:

\[
 C_k\curvearrowright
 \bigl(\text{parent on }[k]\bigr)
 \longrightarrow
 \bigl(\text{child on }[k]\cup\{u,v\}\bigr).         \tag{6.1}
\]

If the complete materialized arrow is equivariant under this action, its
packing transport is flat, and every finite physical capacity retains a
central-band old-subset address or belongs to a bounded exceptional bank,
then the residual modulus tends to infinity by Theorem 2.1.  A uniform
per-stratum defect estimate consequently promotes to exact saturation by
Theorem 5.1.

The parent/child orbit schemas may differ; only the group and the literal
transition action are common.  An integral quotient flow may break
symmetry, but its authenticated output type must still be exported by the
transition state.

The action on the child in (6.1) is **not** the child's full coordinate
rotation `C_(k+2)`: it fixes the fresh pair.  Therefore this theorem supplies
a growing common modulus for one arrow, but does not by itself concatenate
successive arrows.  A regenerative spine must additionally authenticate a
change-of-group (or common groupoid/biset) interface from the output
`C_k`-state to the next arrow's `C_(k+2)`-state.  Flatness inside each arrow
does not imply that inter-arrow re-gauging.

### Corollary 6.1 (conditional regenerative promotion)

Suppose a same-parity construction has, at every sufficiently large odd
`k`, one tap-decorated transition and an actual residual cyclic subgroup
`H_k<=C_k` of order `h_k` satisfying:

1. the `H_k` action survives the fully pinned compensation, sidecar, and
   every reservation, and

   \[
                    \frac{h_k}{2D(k)+1}>C             \tag{6.2}
   \]

   for all sufficiently large `k`;
2. every persistent addressed matching/flow shore, port, sink, internal
   vertex, and finite-capacity arc retains an old-subset label in a band
   `|s-m|<=D(k)=O(sqrt(k))`; fixed bookkeeping supernodes are allowed, but
   their incident finite-capacity arc orbits still satisfy this condition;
   the label projection is equivariant:
   `S(g omega)=g S(omega)` for every `g in H_k`;
3. every complete addressed matching/flow gate restricted to one exact
   period stratum is invariant under the residual `H_k` action;
   distinct exact-period strata are pairwise disjoint in finite physical
   capacity; within one fixed period `q`, distinct residual gates are either
   capacity-disjoint or represented together in one exact joint
   **q-pure**, invariant, capacity-faithful matching/flow gate to which
   Corollary 5.2 applies (or a separate exact `q`-divisibility theorem is
   supplied);
4. every stratum has defect at most one absolute `C`;
5. chronology/packing continuation is flat and the output state is
   authenticated;
6. every persistent fresh-only, seam, pivot, compensation, boundary, or
   continuation obligation outside the growing strata is either saturated
   exactly or exported in a uniformly bounded sidecar which is literally
   replaced in the authenticated child state; that sidecar is
   capacity-disjoint from the invariant bulk, or is fixed first and its
   capacities are deleted before forming a residual bulk which still
   satisfies items 1--5 and 7; only terminal-only omissions (which are not
   inherited by the next arrow) may use a bounded literal repair/
   target-bypass charge; and
7. every suffix-flow gate used to service claims is coupled to its
   capacity-faithful claim-to-port router in the same period stratum; and
8. the sidecar and all period-stratum witnesses coinstantiate in this one
   materialized child, and their union is one authenticated successor lift,
   not merely a collection of marginally exact gates; after the certified
   change-of-group/reframing interface, that same child is admissible as the
   fully pinned `C_(k+2)` candidate for the next arrow.

Then every persistent central-band gate is exact for all sufficiently
large `k`; the bounded persistent exterior bank is regenerated, and only
the uniformly bounded terminal-only charge is paid.

#### Proof

Items 1--4, 6, and 7 put every persistent bulk gate on the exact residual
face of Corollary 5.2, so every matching deficiency and suffix corank is
zero.  Item 7 converts suffix exactness into claim service.  Item 6 closes
every persistent exterior obligation inside the regenerated output and
pays only genuinely terminal omissions once.  Item 8 makes those exact
witnesses one authenticated child rather than incompatible marginals.
\(\square\)

The `q`-purity in item 3 is essential.  A joint program containing orbit
orders `q_1` and `q_2` has, in general, only their common divisor as an
arithmetic modulus; that divisor can be one even when both orders tend to
infinity.  Cross-period shared capacities must therefore be removed into
the exceptional bank or handled by a separate joint theorem with its own
growing modulus.

This promotes only the inner matching/flow gates.  Combined with a closed
recurrent **outer** quotient core, both parity taps, literal replacement of
the bounded persistent sidecar, and the remaining central-ownership,
upper-coverage, residence and terminal-repair hypotheses of the
regenerative-spine theorem, it is sufficient for `nu(k)<=B(k)+O(1)`.

## 7. What remains open

The arithmetic common stabilizer is no longer the obstacle.  The missing
construction must still provide:

* one upper-complete one-copy parent/child carrier;
* a flat capacity-faithful physical lift of the fresh-pair action;
* protected occurrence signatures or nested-shell lower compilation;
* private literal claim-to-port prefixes and quotient-expanding suffix
  networks;
* a bounded odd actuator/opening bank; and
* a recurrent finite transition state whose output is again admissible.

The last item includes the authenticated change-of-group interface between
successive fresh-pair actions.

The theorem proves that any uniform bounded defect on the central-band
period strata would then disappear automatically.  It does not prove that
bounded defect estimate or construct the state.
