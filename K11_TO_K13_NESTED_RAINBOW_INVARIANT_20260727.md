# What the exact `k=11` words actually transfer to `k=13`

Date: 2026-07-27

## 1. The lower-colour sequence is itself a Hamilton cycle

Let `k=2r-1`, and let

\[
T_0,T_1,\ldots,T_{W-1},\qquad W=\binom{k}{r}=\binom{k}{r-1},
\]

be a cyclic ordering of all rank-`r` sets whose consecutive intersections
are all distinct.  Put

\[
X_i=T_{i-1}\cap T_i.
\]

Then the `X_i` enumerate the complete rank-`r-1` layer.  Moreover,
`X_i` and `X_{i+1}` are two distinct facets of `T_i`, and consequently

\[
X_i\cup X_{i+1}=T_i,
\qquad |X_i\cap X_{i+1}|=r-2.
\]

Thus `(X_i)` is a Hamilton cycle of `J(k,r-1)`, its consecutive unions
enumerate the complete rank-`r` layer, and

\[
\boxed{
  T_{i-1}\cap T_i\cap T_{i+1}=X_i\cap X_{i+1}.}
\]

Complete lower-`q=2` coverage is therefore a second, nested rainbow
condition: the edge intersections of the `X`-cycle must cover the complete
rank-`r-2` layer.

This transition design is not determined by the one-coordinate run
histogram or by the upper excess histogram.

## 2. Residence is the local part; nested rainbowness is the global part

A coordinate run of length `ell` in `(T_i)` becomes a run of length
`ell-1` in `(X_i)`.  Hence depth-three residence is exactly the assertion
that every cyclic coordinate run in `(X_i)` has length at least three.

The exact `k=11` certificates and the residence-perfect `k=13`
certificates all satisfy this local condition.  Their difference is the
global adjacency colouring of the `X`-cycle.

For three genuine exact `k=11` rotors, the lower-`q=2` shadow contains all
`330` rank-four sets.  For the current residence-perfect `k=13` rotors:

| certificate | lower-`q=2` covered | holes |
|---|---:|---:|
| `sigma_sat_k13_benders597_c756_f60` | 1118/1287 | 169 |
| `sigma_sat_k13_res0_swap455` | 1131/1287 | 156 |

The latter cycles already have zero residence defects and a perfect simple
upper-excess design, but their rank-five compiler is UNSAT.

## 3. The two marginal histograms are already optimal at `k=13`

For `sigma_sat_k11_allcentral_cap2` the `X`-run histogram is

```
3:143, 4:132, 5:55, 6:44, 7:22, 8:11,
9:22, 10:11, 11:11, 13:11
```

with mean `5` and minimum `3`.  Its upper load profile is exactly

```
load 1: 198 targets; load 2: 132 targets.
```

For `sigma_sat_k13_res0_swap455` the `X`-run histogram is

```
3:364, 4:312, 5:234, 6:247, 7:195, 8:130,
9:26, 10:39, 11:39, 12:26, 13:13, 14:39,
15:26, 16:13, 17:13
```

with mean `6` and minimum `3`.  Its upper profile is also at the exact
integrality floor:

```
load 1: 858 targets; load 2: 429 targets.
```

The fraction of minimum-length runs is smaller at this `k=13` seed than at
the exact `k=11` seed, yet compilation fails.  Therefore neither marginal
is the missing invariant.  The missing datum is their alignment with the
edge-intersection colours of the `X`-cycle.

## 4. Exact compiler localization

Before the seed-specific obstruction, there is a general flatness theorem
for an exact depth-three compiler.

Let the cyclic compiler entries be `A_i` and put

\[
D^j_i=A_i\cup A_{i-1}\cup\cdots\cup A_{i-j}.
\]

Exact reconstruction says `D^3_i=T_i`.  Every coordinate occurrence in an
entry persists through four consecutive middle cells, so every coordinate
one-run in `(T_i)` has length at least four.  Consequently the coordinates
deleted in any three consecutive Johnson steps are distinct.  It follows
that

\[
\begin{aligned}
A_i&\subseteq T_i\cap T_{i+1}\cap T_{i+2}\cap T_{i+3}, &&|A_i|\le r-3,\\
D^1_i&\subseteq T_i\cap T_{i+1}\cap T_{i+2}, &&|D^1_i|\le r-2,\\
D^2_i&\subseteq T_i\cap T_{i+1}, &&|D^2_i|\le r-1.
\end{aligned}
\]

There are exactly `W` cyclic `D^2` cells and exactly `W` rank-`r-1`
targets.  No lower row can reach rank `r-1`.  Thus full lower coverage forces

\[
\boxed{D^2_i=T_i\cap T_{i+1}\quad\text{for every }i.}
\]

Likewise every rank-`r-2` target must occur in `D^1`, and whenever `D^1_i`
has that rank it equals

\[
T_i\cap T_{i+1}\cap T_{i+2}.
\]

Therefore

\[
\boxed{
\text{a full depth-three lower compiler necessarily forces complete
central lower-}q=2\text{ coverage}.}
\]

This is exactly the nested-rainbow feature shared by all genuine exact
`k=11` rotors.  In SAT it supplies two strong redundant propagators:
pointwise `D^2=outgoing lower colour`, and explicit lower-`q=2` coverage.

Equivalently, put `B_i=D^2_i` and `C_i=D^1_i`.  In the full lower normal
form,

\[
|B_i|=r-1,\qquad T_i=B_{i-1}\cup B_i,
\qquad C_i\subseteq B_i\cap B_{i+1}.
\]

The `B_i` consequently form a Hamilton cycle on the rank-`r-1` layer whose
edge unions enumerate the rank-`r` layer perfectly and whose edge
intersections cover the rank-`r-2` layer.  The residence condition is exactly
that every coordinate run in this `B`-cycle has length at least three.
Thus the core inherited from `k=11` is a **resident doubly-rainbow Johnson
cycle**, followed by the compatible `C/A` labelling of its lower shadows.

For the first residence-perfect `k=13` rotor, the rank-five target

\[
\{2,6,8,10,12\}
\]

has eight possible three-entry envelopes.  Every envelope is the target
plus one outsider, and exact middle reconstruction forces that outsider to
remain inside the same three-entry window.  Hence this single target is
compiler-impossible.  Its thirteen translates form the orbit represented
by mask `597`.

After forcing that orbit into the central lower-`q=2` shadow, new
residence-perfect cycles have no individually impossible target and have a
perfect target-to-locally-feasible-cell matching, but the full compiler is
still UNSAT.  This proves that ordinary Hall capacity is exhausted: the
remaining condition is simultaneous compatibility of overlapping entry
bits.

## 5. Symmetry audit

All three exact sigma-based `k=11` rotors are invariant under the chosen
translation group `Z_11`, as built.  Exhaustive testing of the ten
multipliers shows no additional affine multiplier stabilizer: only
multiplier `1` preserves each selected family.  The analogous tested
`k=13` rotor likewise has only its translation stabilizer.

Thus extra `AGL(1,k)` symmetry is not the mechanism to transfer.  The
transferable normal form is instead

\[
\boxed{
\text{nested rainbow Hamilton cycle}
+\text{minimum run length}
+\text{simple upper excess}
+\text{compatible lower entry labelling}.}
\]

## 6. Computational consequence

Weak Benders cuts can repair individually impossible shadow orbits, but
they do not express overlap compatibility.  The correct next encoding is a
joint quotient SAT model containing both the central sigma choices and the
depth-three compiler entry bits.  That model has now been calibrated:

* fixed exact `k=11`: SAT and independently verifies a new length-465 word;
* fixed incompatible `k=13`: UNSAT, agreeing with the independent compiler.

Unconstrained `k=13` instances of this joint model are the first direct
searches whose SAT output is itself an exact length-1719 construction.
