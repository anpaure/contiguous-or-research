# Quantitative reserve absorbers and endpoint-template capacity

Date: 2026-07-31  
Status: exact schedule counts, an exact rare-boundary no-go for the
fixed-filler family, a two-filler repair, an independent-boundary absorber,
and a linear-capacity packing lemma; no robust reserve-packing theorem

## 0. Verdict

The first Boolean absorber has much more schedule entropy than a naive
count suggests, but that entropy is clustered behind one rare boundary
event.  For a fixed outer pair at distance `s`, it has

```text
s! (s+2)!
```

distinct oriented support paths, yet under independent middle-resource
reserves of density `q=C/m` the probability that even one is available is
at most `(s+2)q^2`.  Thus the apparent constant-threshold first moment for
one prescribed pair is false.

There are two exact repairs.

1. A one-switch/two-filler family has

   ```text
   s! (s+2)! binom(s-1,2)
   ```

   distinct schedules and no shared boundary coordinate.  Its boundary
   gate has a nonzero limit at density `C/m`.
2. More strongly, at distance `s>=3`, *any* prescribed first diamond above
   the lower endpoint and *any* prescribed last diamond below the upper
   endpoint extend to a valid two-state absorber.  The two boundary ports
   are therefore completely independent.

Raw capacity is also sufficient: for `m>=4`, the full ordered-diamond
system contains at least `Cat_m` pairwise resource-disjoint direct
absorbers.  What remains open is not the existence or number of local
gadgets, but an integral correlation theorem selecting a robust family
inside the sparse resources left by the main matching.

## 1. Fixed-filler schedules: exact count and clustered failure

Let

```text
L in C([2m],m-1),       U in C([2m],m+1),
s=|L-U|.
```

Write

```text
L-U={a_1,...,a_s},      U-L={b_1,...,b_s,c,d}.
```

The fixed-filler absorber uses

```text
L_i=L-{a_1,...,a_i}+{b_1,...,b_i},
U_i=L_i union L_(i+1) union {c}.
```

For `s>=1`, ordering the `a`-coordinates and all `s+2` upper-difference
coordinates gives exactly

```text
F_s=s!(s+2)!                                               (1.1)
```

distinct oriented support paths.  Indeed the lower path recovers the two
swap orders, and the repeated filler recovers `c`; the remaining coordinate
is `d`.  Conversely every pair of orders gives the displayed path.

Orient the physical middle resources so that the transition unions and the
final `d`-extension are tail resources, while the `c`-extensions are head
resources.  Across both absorber states there are `s+1` resources of each
role, hence `2s+2` in total.  In particular every schedule using filler `c`
requires both boundary resources

```text
L+c in H_reserve,                 U-c in T_reserve.        (1.2)
```

### Proposition 1.1 (rare-boundary bound)

If the tail and head reserves contain each rank-`m` resource independently
with probability `q`, then for a fixed pair `(L,U)`

```text
P(some fixed-filler schedule is wholly available) <= (s+2)q^2.   (1.3)
```

### Proof

There are only `s+2` possible fillers `c`.  For each one, the two resources
in (1.2) lie in different role pools and occur together with probability
`q^2`.  A union bound proves (1.3).  `square`

For `s=alpha m+o(m)` and `q=C/m`, (1.3) is `O(C^2/m)`, although the raw
first moment is

```text
E(number of available descriptions)=s!(s+2)!q^(2s+2).
```

The discrepancy is genuine clustering: whenever (1.2) occurs, factorially
many internal schedules may become available together.  Schedule count
alone therefore cannot certify the reserve.

For comparison, the number of upper endpoints at distance `s` from a fixed
lower endpoint is

```text
D_s=binom(m-1,s) binom(m+1,s+2).
```

For fixed `s`, summing the description first moment over all such endpoints
gives the exact expression

```text
D_s F_s (C/m)^(2s+2)
 = (m-1)_s (m+1)_(s+2) (C/m)^(2s+2)
 -> C^(2s+2).                                             (1.4)
```

Thus bounded-distance endpoint degree can remain constant even though one
prescribed far pair has a rare boundary gate.

## 2. A one-switch/two-filler family

The shared-boundary defect can already be removed while retaining a closed
schedule count.

### Theorem 2.1 (two-filler absorber)

Assume `s>=3`.  Order the coordinates as above.  Choose

```text
1<=j<=s-2,             j+2<=t<=s,             f=b_t.
```

Use filler `f` for transitions `i<j` and filler `c` for transitions
`i>=j`:

```text
U_i=L_i union L_(i+1) union { f  if i<j,  c if i>=j }.
```

The same alternating odd/even edge sets as in the fixed-filler construction
are valid absorber states, and in each state every physical middle resource
is distinct.

### Proof

The transition unions are distinct along the monotone lower path.  The
`f`-extensions and `c`-extensions are separately distinct.  They cannot
meet each other because `f=b_t` has not entered the lower path at the switch
and `c` never enters it.  The separation `t>=j+2` also prevents the last
`f`-extension from equalling the next transition union; `t=j+1` is exactly
the forbidden equality.  Before the switch the `f` signature separates the
auxiliary resources from the `c` family, and after the switch the `c`
signature does the converse.  The final two resources have the same
separation as in the fixed-filler proof.  These exhaust the possible
collisions.  `square`

### Proposition 2.2 (exact count)

The number of distinct oriented two-filler support paths is

```text
G_s=s!(s+2)! binom(s-1,2).                                (2.1)
```

### Proof

There are `s!` removal orders, `(s+2)!` upper-coordinate orders, and

```text
sum_(j=1)^(s-2) (s-j-1)=binom(s-1,2)
```

choices of `(j,t)`.  The lower path recovers both swap orders; the two
constant filler segments recover `j,f,c`, and the known addition order then
recovers `t`.  Hence distinct descriptions give distinct support paths.
`square`

Across both states the family uses `s+1` tail-role and `s+2` head-role
resources, `2s+3` total.  Consequently

```text
E(number of available descriptions)=G_s q^(2s+3).         (2.2)
```

If `s=alpha m+o(m)` and `q=C/m`, Stirling's formula gives

```text
G_s q^(2s+3)
 =(1+o(1)) pi alpha^5 C^3 m^2 (alpha C/e)^(2 alpha m).     (2.3)
```

Thus its description first moment has threshold `C=e/alpha`.

Unlike the fixed-filler family, its two endpoint requirements are distinct
stars.  For `r` coordinates with independent tail/head membership of
density `q`, the exact probability of an ordered distinct tail/head pair is

```text
p_star(r,q)
 =1-2(1-q)^r+(1-q)^(2r)-r q^2(1-q)^(2r-2).               (2.4)
```

Indeed the first three terms assert that both role sets are nonempty, and
the last term subtracts the only bad nonempty case: both are supported on
the same singleton coordinate.  Here `r=s+2`, so the two endpoint gates
have limiting probability

```text
(1-exp(-alpha C))^4.                                     (2.5)
```

This removes the rare `O(1/m)` boundary event.  Equations (2.2)--(2.5) do
not by themselves prove that an internal corridor survives; correlations
among its resources are still the unresolved issue.

## 3. Arbitrary prescribed boundary ports

The exact local theorem is stronger still.

### Theorem 3.1 (independent-boundary absorber)

For every pair `(L,U)` with `|L-U|>=3`, every prescribed upper neighbour

```text
U_0=L+{p,q}
```

and every prescribed lower neighbour

```text
L_*=U-{r,t}
```

are the first and last boundary edges of a two-state alternating absorber
whose physical middle resources are pairwise distinct in each state.  Its
support has at most `2m+1` edges.

The closed construction and proof are in

```text
MATH_THEOREM_CATALAN_INDEPENDENT_BOUNDARY_ABSORBER_20260731.md.
```

For independent role reserves of density `q`, the probability that a fixed
lower endpoint has at least one usable prescribed boundary diamond is
`p_star(m+1,q)`, and the same holds at the upper endpoint.  At distance at
least three the two boundary resource families are disjoint, so the joint
probability is

```text
p_star(m+1,q)^2 -> (1-exp(-C))^4              (q=C/m).     (3.1)
```

Thus boundary compatibility is now a constant-probability event with no
shared-coordinate tax.  The unsolved task is to find internally available,
mutually disjoint corridors joining many such independently chosen ports.

## 4. A simple endpoint template of Catalan size always embeds

Distance-zero absorbers are single ordered diamonds: the off state is empty
and the on state is that atom.  They already prove that raw reserve capacity
is not the issue.

Put

```text
N=binom(2m,m-1)=m Cat_m.
```

There are

```text
E=N m(m+1)                                               (4.1)
```

ordered diamonds.  A fixed lower or upper outer resource lies in
`m(m+1)` ordered diamonds, while a fixed tail or head middle resource lies
in `m^2`.

### Theorem 4.1 (linear direct-absorber packing)

For `m>=4`, the ordered-diamond system contains at least `Cat_m` atoms
pairwise disjoint in all four resource classes.

### Proof

Greedily select an atom and delete every atom sharing any of its four
resources.  One choice deletes at most

```text
2m(m+1)+2m^2=4m^2+2m
```

atoms.  Hence the greedy matching has size at least

```text
E/(4m^2+2m)=N(m+1)/(4m+2).
```

For `m>=4`, this is at least `N/m=Cat_m`.  `square`

This embeds a simple matching template of the exact Catalan order.  It does
not embed a robustly matchable bounded-degree endpoint graph: alternatives
for different template edges must share endpoint resources but avoid all
internal role conflicts, an integral correlation condition absent from the
greedy argument.

## 5. The weakest clean multi-demand condition currently proved

Let demand `i` have a nonempty family `S_i` of candidate schedules, each
schedule carrying its complete set of outer and middle resources.  Two
schedules conflict when these resource sets meet.

### Lemma 5.1 (collision-density greedy criterion)

Suppose the demands are ordered so that, for every `i` and every schedule
`A in S_j` with `j<i`, at most `eta_(j,i)|S_i|` schedules in `S_i` conflict
with `A`.  If

```text
sum_(j<i) eta_(j,i) < 1                    for every i,    (5.1)
```

then one can choose one schedule from each `S_i`, all resource-disjoint.

### Proof

After schedules have been selected for demands before `i`, the union bound
shows that they forbid fewer than

```text
|S_i| sum_(j<i) eta_(j,i) < |S_i|
```

candidates.  At least one remains.  Choose it and continue.  `square`

In the symmetric case, it suffices that every selected schedule conflicts
with at most an `eta` fraction of every other family and
`(h-1)eta<1` for `h` demands.  This is a genuine deterministic
pseudorandom-pool condition, but it is not yet verified for the critical
Boolean reserve.

The exact many-demand object is the hypergraph whose vertices are resources
and whose hyperedges are candidate schedules, with an additional demand
colour on each hyperedge.  The missing theorem asks for a rainbow matching
covering all reserve demands.  This is a set-packing problem, not an
ordinary network flow in general; integrality cannot be assumed for free.

## 6. A more favourable intermediate stopping scale

The preceding calculations suggest that absorption need not be postponed
until only `Cat_m=N/m` outer vertices remain.  Suppose a pseudorandom nibble
is stopped when a fraction

```text
p=m^(-1/3)
```

of every resource class survives.  Conditional on a fixed surviving
resource, an ordered diamond survives when its other three resources do, so
the residual degree scale is

```text
D_res=m^2 p^3=Theta(m)=Theta(log N).                       (6.1)
```

The largest original pair codegree is `m`; after its other two resources
are thinned it becomes

```text
Delta_2,res=m p^2=Theta(m^(1/3))=Theta(D_res^(1/3)).        (6.2)
```

There are `Np` residual outer vertices on each shore.  Each middle shore
has `Np+Cat_m` unused vertices, and

```text
Cat_m/(Np)=m^(-2/3),                                      (6.3)
```

so the required final middle slack is lower order but still explicit.

At this density the local absorber is far above its entropy threshold.  If
`s=alpha m`, substituting `q=p=m^(-1/3)` into (2.2) gives

```text
log E(number of two-filler schedules)
  =(4 alpha/3+o(1)) m log m,
```

and the boundary-star probability tends to one.  Thus the local corridor
has enormous schedule room rather than the constant-order room at `q=C/m`.

This identifies a potentially easier exact endgame:

> stop the main nibble at survival `m^(-1/3)` and prove a pseudorandom
> perfect-matching theorem for the resulting logarithmic-degree Boolean
> residual, using independent-boundary absorbers for the final defects.

Equations (6.1)--(6.3) verify the scale but do not prove that theorem.  In
particular generic almost-perfect matching results still do not supply the
required exact integral correlation or physical-forest condition.

## 7. What is now left

The local picture is complete enough to isolate one global statement.

> **Critical corridor-packing theorem.**  After an almost-perfect ordered
> diamond matching leaves pseudorandom outer and middle reserves at the
> critical scale, choose a robust endpoint template of order
> `Theta(Cat_m)` and realize every selected template edge by a mutually
> resource-disjoint independent-boundary corridor.

Theorem 3.1 removes endpoint compatibility from this statement.  Theorem
4.1 proves that its raw resource count has Catalan-scale room.  Lemma 5.1
gives one sufficient collision condition.  What is not proved is that the
actual Boolean reserve produced by a nibble, or a deterministic analogue,
satisfies such a condition while also retaining the outer matching and
physical-forest constraints.

## 8. Audits

The two-filler construction was checked for every endpoint-pair orbit
through `m=6`, including 194,832 pairs at `m=6`, and the exact count (2.1)
was exhaustively verified at `s=3,4`:

```text
scratch/audit_boolean_two_filler_absorber_20260731.py
scratch/boolean_two_filler_absorber_m4_m6_20260731.audit.json
```

The independent-boundary closed formula was checked for every prescribed
boundary in every endpoint-pair orbit through `m=8`:

```text
scratch/audit_boolean_prescribed_boundary_absorber_20260731.py
scratch/boolean_prescribed_boundary_absorber_m4_m8_20260731.audit.json
```

An independently written constructive audit through `m=7` is retained as

```text
scratch/audit_independent_boundary_absorber_constructive_20260731.py
scratch/independent_boundary_absorber_constructive_m4_m7_20260731.audit.json.
```
