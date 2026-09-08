# Johnson event streams, exact run-deficit identities, and the MMM shear potential

Date: 2026-07-29

Status: unconditional theorem for every cyclic Johnson walk, with an exact
`k=15` audit on the resident strict spiral and its verified MMM parallel-edge
shear.  This does not change the bound on `nu(15)`.

## 1. Event-stream normal form

Let

\[
T_0,T_1,\ldots,T_{L-1}\in\binom{[k]}r
\]

be a cyclic Johnson walk.  At transition `i`, write

\[
T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.              \tag{1.1}
\]

The two event streams contain all interval-shadow information.  For every
`q>=1`, indices being cyclic,

\[
\boxed{
\bigcap_{a=0}^{q}T_{i+a}
=T_i\setminus\{\alpha_i,\ldots,\alpha_{i+q-1}\},}
                                                               \tag{1.2}
\]

and

\[
\boxed{
\bigcup_{a=0}^{q}T_{i+a}
=T_i\cup\{\beta_i,\ldots,\beta_{i+q-1}\}.}         \tag{1.3}
\]

These are set identities; repeated or nonfresh events are simply absorbed by
the set operations.  Thus Claude's useful `gap algebra` is valid without a
residence hypothesis.  Residence controls the *ranks* of these sets, not the
identities themselves.

### Proof

An element of `T_i` survives the intersection precisely when it is not
deleted in the next `q` transitions, which proves (1.2).  An element outside
`T_i` enters the union precisely when it is inserted in one of those
transitions, which proves (1.3).  \(\square\)

## 2. Exact run-deficit theorem

For a coordinate `x`, read its cyclic binary trace

\[
\mathbf 1_{x\in T_0},\ldots,\mathbf 1_{x\in T_{L-1}}.
\]

Let `R_x^+(s)` and `R_x^-(s)` be the numbers of cyclic one-runs and zero-runs
of length `s`.  Define

\[
L_i^{(q)}=\bigcap_{a=0}^{q}T_{i+a},\qquad
U_i^{(q)}=\bigcup_{a=0}^{q}T_{i+a}.
\]

### Theorem 2.1 (coefficient-exact lower and upper rank error)

For every `1<=q<=L`,

\[
\boxed{
\sum_{i=0}^{L-1}\left(\lvert L_i^{(q)}\rvert-(r-q)\right)
=\sum_{x\in[k]}\sum_{s\ge1}(q-s)^+R_x^+(s),}       \tag{2.1}
\]

and

\[
\boxed{
\sum_{i=0}^{L-1}\left((r+q)-\lvert U_i^{(q)}\rvert\right)
=\sum_{x\in[k]}\sum_{s\ge1}(q-s)^+R_x^-(s).}       \tag{2.2}
\]

Here the formulas remain true when `r-q<0` or `r+q>k`; the left sides then
count the forced repeated events as well as the Boolean-rank cap.
The range `q<=L` is essential for this single-wrap cyclic run count.  The set
identities (1.2)--(1.3) remain valid for arbitrary `q`, but for `q>L` a
coordinate trace can wrap more than once and the coefficient `(q-s)^+` no
longer counts its contribution without an additional winding term.

### Proof

Begin with the lower side.  Without repetitions, each of the `q` deletions
would remove a new member of `T_i`, leaving rank `r-q`.  A deletion fails to
lower the running intersection exactly when it closes a one-run that began
strictly inside the same window.  A one-run of length `s` is wholly internal
to exactly `q-s` windows of `q` transitions when `s<q`, and to none otherwise.
Each such internal run contributes one unit of rank excess.  Summing over
coordinates and runs gives (2.1).

The upper argument is dual.  Without repetitions, the `q` insertions add
`q` new elements.  An insertion fails to enlarge the running union exactly
when it closes a zero-run that began strictly inside the window.  A zero-run
of length `s` is internal to exactly `(q-s)^+` such windows, proving (2.2).
\(\square\)

### Corollary 2.2 (residence and dual residence)

If every one-run has length at least `h`, then every lower window with
`q<=h` has the exact rank `r-q`.  If every zero-run has length at least `h`,
then every upper window with `q<=h` has exact rank `r+q`.

At `q=h`, consecutive shadow states need not be Johnson-adjacent: a
length-`h` run can make the nominal deletion and insertion coincide.  The
usual exact Johnson erosion/dilation tower is therefore stated safely for
`q<h`.

### Corollary 2.3 (pointwise event form)

For every integer `d>=1`, minimum one-run length at least `d+1` is equivalent
to

\[
 \beta_i\notin\{\alpha_{i+1},\ldots,\alpha_{i+d}\}
 \qquad(i\in\mathbb Z_L).
 \tag{2.3}
\]

Minimum zero-run length at least `d+1` is equivalently

\[
 \alpha_i\notin\{\beta_{i+1},\ldots,\beta_{i+d}\}
 \qquad(i\in\mathbb Z_L).
 \tag{2.4}
\]

Indeed, `beta_i=x` starts the next one-run of coordinate `x`, whose first
subsequent deletion is the first `alpha_(i+s)=x`; dually, `alpha_i=x` starts
the next zero-run, whose first subsequent insertion is the first
`beta_(i+s)=x`.

## 3. Strict-spiral scalarization

For a unit-voltage strict `Z_k` spiral of length `W=kN`, every coordinate
trace is a translate of the scalar trace `c`.  If `R_c^+(s),R_c^-(s)` are
the one- and zero-run histograms of `c`, Theorem 2.1 becomes

\[
E_q^-=k\sum_s(q-s)^+R_c^+(s),\qquad
E_q^+=k\sum_s(q-s)^+R_c^-(s).                       \tag{3.1}
\]

Thus the exact upper native-rank capacity is controlled by the short
**zero** runs.  This is independent of necklace collisions: it is the rank
budget that exists before distinct target coverage is considered.

Equation (3.1) supplies a proof-safe inexpensive search potential:

\[
\mathcal Z_H(c)=\sum_{q=1}^{H}\sum_s(q-s)^+R_c^-(s). \tag{3.2}
\]

Minimizing `Z_H` cannot replace the exact upper-hole audit, but it increases
the number and rank quality of available upper windows.  Unlike raw Hamming
distance, it is a mathematically forced relaxation of the actual objective.

## 4. The verified `k=15` MMM shear

Use the residence-perfect strict spiral

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
```

and the verified parallel-edge switch

\[
(1807,7,12)\longrightarrow(1807,11,12).
\]

The switch preserves all middle owners, the exact lower first shadow,
residence, and the set of 47 missing lower-`q2` orbits.  It improves the
exact all-width upper holes from `95` to `94`.

Its scalar zero-run histogram changes by

```text
1:-1, 4:+1, 5:+1, 7:-1, 9:+1, 11:-1,
15:-1, 16:+1, 19:+1, 24:-1, 25:-1, 30:+1.
```

Consequently the exact physical upper-rank deficit changes by

| transition depth `q` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `Delta E_q^+` | 0 | -15 | -30 | -45 | -45 | -30 | -15 |

Across the depths needed to reach the full rank at `k=15`, the shear removes
exactly `180` physical units, or `12` quotient units, of upper rank deficit.
It simultaneously fills one upper necklace hole and creates none.

This is not a full carrier/compiler descent.  The terminal lower-`q3`
positive-degree missing set worsens from 11 to 12 quotient orbits, creating
representative `1159`; the corresponding protected rank-five zero-degree
targets worsen `165 -> 180`.  Full compiler Hall is not defined for this
comparison because both states already fail lower `q2` with 47 holes, so the
fail-closed compiler is not invoked.

This does not prove monotonicity of holes under `Z_H`, but it is the first
nonlocal switch for which the exact capacity potential and the exact shadow
objective improve together on the upper side.  Future MMM/overlay searches
should therefore use the lexicographic objective

1. middle and lower-`q1` exactness;
2. required one-residence and lower shadows;
3. the short-zero-run potential (3.2);
4. exact upper orbit holes;
5. exact compiler Hall/cut feasibility.

## 5. Reproduction

```sh
python3 scratch/audit_k15_event_stream_rank_deficit_20260729.py
```

Artifacts:

```text
scratch/audit_k15_event_stream_rank_deficit_20260729.py
scratch/k15_event_stream_rank_deficit_20260729.audit.json
```

At creation their SHA-256 hashes were

```text
8f592dc49682bcb6d896e9a79df0ac6dc8bd8b0e5b13990a62053719fb844c80
4580f1df6c5316ae39216496c766e50e54c28ffa4b0b4932b20a60f3971f1270
```
