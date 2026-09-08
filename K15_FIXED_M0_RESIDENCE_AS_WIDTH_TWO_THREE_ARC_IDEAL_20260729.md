# `k=15`: residence in a fixed matching is an exact width-two/three arc ideal

Date: 2026-07-29

Status: proved finite reduction, independently replayed clause audit, and a
positive resident exact-double-shadow factor in the step-19 fixed-`M0` fibre.
This replaces the previous width-at-most-four CEGAR description by an exact,
eager, much smaller residence theory.  It still does **not** prove
`nu(15)=6438`: the retained factor has thirteen physical components and a few
deeper-shadow holes.

## 1. Matching-permutation normal form

Let

\[
 {cal L}=\binom{[15]}7,\qquad {cal V}=\binom{[15]}8,
\]

and fix an equivariant perfect matching

\[
 M_0:{\cal L}\longrightarrow {\cal V},\qquad L\subset M_0(L).
\]

Let `P` be a second perfect matching in the same incidence graph.  On the
searched face `P` and `M0` have no common edge.  Put

\[
 \tau=M_0^{-1}P:{\cal L}\longrightarrow {\cal L}.
\]

Thus `tau` is a permutation.  If `L_(i+1)=tau(L_i)` along one of its cycles,
put

\[
 T_i=M_0(L_i).
\]

Then

\[
 P(L_i)=M_0(L_{i+1})=T_{i+1},\qquad
 L_i=T_i\cap T_{i+1}.                         \tag{1}
\]

Because the two incident middle sets at `L_i` are distinct, (1) is a Johnson
transition.  On the lower-`q2` rank-exact face, consecutive lower states also
satisfy

\[
 |L_i\cap L_{i+1}|=6.                          \tag{2}
\]

For the directed lower arc `e_i=(L_i,L_(i+1))`, define its two labels

\[
 \iota(e_i)=L_{i+1}\setminus L_i,qquad
 \delta(e_i)=L_i\setminus L_{i+1}.             \tag{3}
\]

Both labels are single coordinates by (2).

## 2. Exact run correspondence

### Lemma 2.1 (a one-zero lower gap is a forbidden matching loop)

The incidence trace of a coordinate in `(L_i)` cannot contain `101`.

**Proof.**  Suppose the trace at `L_i,L_(i+1),L_(i+2)` is `101` for a
coordinate `x`.  The first arc deletes `x`, so the fixed middle set at the
gap is

\[
 M_0(L_{i+1})=L_{i+1}\cup\{x\}.
\]

The second arc immediately reinserts `x`, so

\[
 P(L_{i+1})=L_{i+1}\cup\{x\}=M_0(L_{i+1}),
\]

contrary to the non-loop condition.  \(\square\)

### Lemma 2.2 (dilation without coalescence)

For every coordinate, maximal positive runs in `(L_i)` and `(T_i)` are in
bijection, and a lower run of length `a` corresponds to a middle run of
length `a+1`.

**Proof.**  Equation (1) gives the coordinatewise Boolean identity

\[
 1_{x\in T_{i+1}}=1_{x\in L_i}\vee1_{x\in L_{i+1}}. \tag{4}
\]

Thus the middle trace is the radius-one forward dilation of the lower trace.
Every lower positive run grows by one.  Distinct lower runs could coalesce
under this dilation only across a one-zero gap, excluded by Lemma 2.1.
There is no isolated middle `1`: it would force the two adjacent rank-seven
intersections to be the same set `T_i-{x}`, hence a fixed point of `tau` and
again a common `P=M0` edge.  \(\square\)

### Theorem 2.3 (residence as two arc exclusions)

The middle carrier has depth-three residence -- every positive coordinate
run has length at least four -- if and only if every lower coordinate run has
length at least three.  Equivalently, along every directed `tau`-cycle,

\[
 \boxed{
 \iota(e_i)\ne\delta(e_{i+1})
 \quad\hbox{and}\quad
 \iota(e_i)\ne\delta(e_{i+2})
 }
                                                        \tag{5}
\]

for every `i`.

**Proof.**  Lemma 2.2 converts middle run lengths `2,3` into lower run
lengths `1,2`.  A lower run of length one begins with an insertion on `e_i`
and ends with the same deletion on `e_(i+1)`.  A lower run of length two does
the same on `e_i,e_(i+2)`.  Conversely either equality in (5) produces the
corresponding short lower run.  \(\square\)

This is the exact local/global characterization requested by the fixed
matching lane.  It uses the complete global permutation `tau`, but its
forbidden witnesses have radii only one and two.

## 3. Exact quotient CNF

One quotient Boolean variable selects an entire rotation orbit of physical
directed arcs.  Expand every live variable to its fifteen physical arcs.
For every physically consecutive pair `(e,f)` with

\[
 \iota(e)=\delta(f),
\]

add

\[
 \neg z_e\vee\neg z_f.                           \tag{6}
\]

For every physically consecutive triple `(e,f,g)` with

\[
 \iota(e)=\delta(g),
\]

add

\[
 \neg z_e\vee\neg z_f\vee\neg z_g.             \tag{7}
\]

Repeated quotient variables in one physical motif are collapsed, rotation
duplicates are removed, and a clause in (7) containing one of (6) is
discarded.  Perfect-matching constraints make (6)--(7) exact: selecting the
variables selects the indicated consecutive physical path.  Conversely any
short run supplies one of these paths by Theorem 2.3.

Therefore the resident double-shadow problem in a fixed `M0` fiber is
exactly:

1. a perfect matching `P`;
2. upper-`q1` and lower-`q2` colour-cover clauses; and
3. the negative conflict graph (6) plus the negative 3-uniform conflict
   hypergraph (7).

This is not an ordinary Hall/flow problem: after the matching equations, the
length-two lower runs leave genuine ternary conflicts.  It is nevertheless a
finite exact local reduction, rather than a chronology search or an
unbounded CEGAR hierarchy.

## 4. Audited `k=15` sizes

The compiler is

```text
scratch/k15_fixed_matching_minimal_residence_motifs_20260729.py
```

For the phase-two fixed matching it gives:

```text
live rank-exact variables       2999
physical bad pair paths        44865
physical bad triple paths     269505
distinct raw pair clauses       2989
distinct raw triple clauses    17967
subsumed triples                    3
minimal width-2 clauses          2990
minimal width-3 clauses         17963
total residence clauses         20953
```

Appending these to the 19,498-clause exact double-shadow CNF gives 40,451
clauses in total.  The retained SAT endpoint violates 74 minimal clauses:
21 of width two and 53 of width three.  The independent physical expansion
finds 1,110 bad runs; the zero/nonzero verdicts agree exactly.

For the collision-401 fixed matching the independently rebuilt counts are:

```text
minimal residence clauses       20971
width histogram          2:2999, 3:17972
violated clauses                    80
physical bad runs                 1200
zero/nonzero equivalence          PASS
```

The two compact replay reports are

* `scratch/k15_fixed_matching_minimal_residence_phase2_20260729.audit.json`
  (SHA-256
  `63628f0a61090cbc6ac47dac270c48f1aaf7b32fc545376975c470a9ff946aad`);
* `scratch/k15_fixed_matching_minimal_residence_c401_20260729.audit.json`
  (SHA-256
  `f59f62f9fae37c6f8ccae32509ff3ba51534947e5b37cd72370ee3421136bbd8`).

The multiplicative factor fifteen between many physical bad-run counts and
quotient clauses is rotation symmetry, not a discrepancy.

## 5. Exact alternating-cycle switch form

If `P` and `P'` are two perfect matchings against the same `M0`, then
`P` symmetric-difference `P'` is a disjoint union of alternating cycles.  Choosing a subset
of those cycles gives a Boolean switch vector `s`.  In that cube:

* the matching equations are automatic;
* a shadow colour `c` is preserved exactly when

\[
 w_P(c)-r_s(c)+a_s(c)\ge1;                       \tag{8}
\]

* residence is preserved exactly when none of (6)--(7) is fully selected
  after the switch.

Thus every fixed pair of endpoints has an exact Boolean feasibility problem
with only colour inequalities (8) and width-two/three residence clauses.
The exhaustive ten- and five-component cubes already retained in the repo
show that two particular exact-shadow endpoints have no resident hybrid
other than their non-shadow-complete parent.  That is a certified obstruction
for those two finite cubes only; it is not an obstruction to the entire
fixed-`M0` fiber.

## 6. Positive fixed-fibre intersection

Using the step-19 PBBS matching as `M0`, the complete eager model is SAT in
all four tested matching orientations.  Seed zero solved at round zero; the
base-plus-residence CNF had 40,441 clauses and Kissat needed 0.12 seconds
after the 12.3-second solver-free motif compilation.

Independent expansion gives

```text
physical middle vertices       6435
physical components              13
minimum coordinate run            4
residence violations               0
upper-q1 coverage          5005/5005
lower-q2 coverage          5005/5005
upper-q2 holes             108 physical / 8 quotient
lower-q3 holes                            6 quotient
upper-q3 holes                            3 quotient
```

The frozen evidence is

* `scratch/k15_fixed_m0_step19_seed0_resident_20260729.json`
  (SHA-256
  `b88d2b56d8647ec4e099b8f08e3a1e7d46cf463d9c0961df71e6a94eb8479971`);
* `scratch/k15_fixed_m0_step19_seed0_resident_20260729.independent.audit.json`
  (SHA-256
  `30696e7d2c68074ad6b47f6e8c8c84837ba8e458821321236e23ed6d0ee05fa7`).

A fresh local replay of the independent auditor reproduced the retained JSON
byte for byte.  Therefore the previously open intersection

\[
 \boxed{\text{residence}\ \cap\ \text{complete upper-}q1
        \ \cap\ \text{complete lower-}q2}
\]

is nonempty in a fixed-`M0` fibre.

That certificate left eight upper-`q2`, six lower-`q3`, and three upper-`q3`
quotient holes.  The next section records their subsequent simultaneous
closure.

## 7. Superseding all-shadow factor

Adding exact geodesic path-witness rows for upper `q2`, lower `q3`, and upper
`q3` produced the retained seed-801 factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    u2u3l3_s801.engine.json.
```

Independent audit proves residence, complete lower `q2`/`q3`, and complete
upper coverage at every rank.  It has nine physical components.  Therefore
the fixed-factor search gates are closed; the remaining problem is the exact
opening/seam/compiler problem in

```text
K15_NINE_CYCLE_ALL_SHADOW_FACTOR_OPENING_SEAM_THEOREM_20260729.md.
```

No length-6438 word is claimed yet.
