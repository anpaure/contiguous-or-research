# Exact topology-changing overlay descent at `k=16`

Date: 2026-07-29  
Status: proved finite certificate; scoped to one six-component overlay.

## 1. Inputs and scope

Let `A` be the edge set in
`scratch/k16_connected_q1_lower2_hamilton_20260729.json`, SHA-256

`16fc3739b8b4df5bed71c44b2f2e148f4839753cab6b9ea308e78d17ee9c32d8`,

and let `B` be the canonical q1-perfect, top-biresident Hamilton factor in
`scratch/k16_qfactor_q1_topresident_hamilton_20260729.json`, SHA-256

`f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5`.

The first artifact is `PARTIAL_Q1_PHYSICAL_HAMILTON` and is compiler-UNSAT;
it is used here only as a source of alternating quotient edges.  The second
artifact is the only valid base for the residence CEGAR.

Both are 2-factors in the same 858-vertex, 27,456-edge `C_15` quotient.
They share 783 edge orbits and have 75 exclusive edge orbits each.

## 2. Component-toggle lemma

Colour `A\B` red and `B\A` blue.  For a quotient vertex `v`, let
`d_R(v)` and `d_B(v)` count incidences, with a quotient loop counted twice.

### Lemma 2.1

Every connected component `C` of the red-blue support satisfies

\[
d_{R\cap C}(v)=d_{B\cap C}(v)
\quad\text{for every }v.
\]

Consequently, replacing all red edges of any union of components by all its
blue edges preserves quotient degree two at every vertex.

### Proof

Deleting the common edges from the two degree-two factors gives
`d_R(v)=d_B(v)` at every vertex.  All red and blue incidences at a fixed
vertex belong to the same connected component of the symmetric-difference
support.  Thus the equality holds componentwise.  The degree change under a
component toggle is `d_B(v)-d_R(v)=0`.  The same argument counts a loop by
its two incidences. ∎

This lemma preserves only degree.  Shadow coverage, voltage, connectedness,
and residence must still be checked after every toggle.

## 3. Exact overlay census

The overlay has six components.  In the deterministic ordering used by
`scratch/search_k16_hamilton_overlay_component_descent_20260729.py`, their
red/blue sizes are

\[
(2,2),(2,2),(2,2),(2,2),(3,3),(64,64).
\]

All `2^6=64` component unions were reconstructed literally.  Exactly three
are simultaneously

1. lower-q1 complete;
2. upper-q1 complete;
3. one quotient cycle of unit voltage; and
4. one physical Hamilton cycle.

Their exact ledgers are:

| mask | toggled components | voltage | old short positive runs | all-coordinate short positive runs | top biresident | q2 holes | deeper upper holes |
|---:|---|---:|---:|---:|:---:|---:|---:|
| 34 | 1,5 | 7 | 3330 | 3345 | no | 88 | 125 |
| 51 | 0,1,4,5 | 13 | 3360 | 3375 | no | 88 | 122 |
| 63 | all | 11 | 3390 | 3390 | yes | 88 | 122 |

For mask 34 the old-coordinate histogram is

\[
1:345,\qquad 2:1590,\qquad 3:1395.
\]

Its extra fifteen all-coordinate defects are top-coordinate singleton
positive runs.  It also has thirty top-coordinate singleton zero-runs and
fifteen top-coordinate zero-runs of length two.  Thus its apparent old-run
improvement is paid for by a failure of the protected top collar.

Mask 63 is exactly the canonical factor `B`.  Hence:

### Theorem 3.1 (scoped overlay no-go)

Among all unions of connected components of this particular `A`-versus-`B`
symmetric difference, `B` is the unique factor which is q1-perfect, a
physical Hamilton cycle, and top-biresident.  No such component toggle
strictly decreases its 3390 old-coordinate short-run defects.

The theorem does not cover alternating circuits using edges outside this
overlay, or partial interacting switches inside its non-simple 64-edge
component.  Those genuine topology changes remain available to the global
CEGAR.

## 4. Reproduction

The solver-free command is

```text
python3 scratch/search_k16_hamilton_overlay_component_descent_20260729.py
```

It writes
`scratch/k16_hamilton_overlay_component_descent_20260729.json`.  The current
artifact records internal payload SHA-256

`b9866c92ffda8ddd349e85b46d5442f3e57b0d3b2a2b353f465fad3ae892d4dc`.

An independent implementation found the same six components, the same three
q1-perfect physical Hamilton toggles, and the corrected separation between
old-coordinate and top-coordinate short runs.
