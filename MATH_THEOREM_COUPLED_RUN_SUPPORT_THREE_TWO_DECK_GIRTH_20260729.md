# Coupled run-boundary trades, the exact support-three atlas, and the event-potential gate

Date: 2026-07-29

Status: unconditional boundary/event normal form; exact complete
support-at-most-three census on the audited resident `k=15` middle/q1-perfect
seed; seed-specific perfect-face girth at least four; exact short-zero
potential criterion.  No bounded Markov basis and no compiler-Hall descent are
claimed.

## 1. Result

Let `k=15`, `N=429`, `W=6435`, and let `c` be the coordinate-zero trace of
the exact resident carrier in

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
SHA-256 4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10
```

Its middle-necklace and lower-`q1`-necklace maps are both permutations.
Write its `N` scalar one-runs in cyclic order as

\[
 [S_i,E_i],\qquad
 \ell_i=E_i-S_i+1,\qquad
 g_i=S_{i+1}-E_i-1.
 \tag{1.1}
\]

For a same-run-order displacement

\[
 S'_i=S_i+u_i,\qquad E'_i=E_i+v_i,
 \tag{1.2}
\]

define its run-boundary support by

\[
 B(u,v)=\{i:(u_i,v_i)\ne(0,0)\}.
 \tag{1.3}
\]

### Theorem 1.1 (exact `k=15` support-three closure)

Among all nonzero same-run-order displacements with `|B(u,v)|<=3` that

1. preserve the start-residue and end-residue transversals modulo `N`;
2. preserve total one-mass;
3. keep every one-run of length at least four and every zero-gap nonempty;

there are exactly **46,928** distinct legal trace states.  None preserves the
middle-necklace permutation.  In particular none preserves both the middle
and lower-`q1` decks.

Consequently every same-run-order resident trade from this seed that stays
on the middle/q1-perfect face has

\[
 |B(u,v)|\ge4.
 \tag{1.4}
\]

This is a seed-specific perfect-face girth theorem.  It is not a universal
support bound and does not imply that a support-four trade exists.

## 2. Complete finite normal form

The census is finite for a structural reason, not because boundary positions
were scanned.

### Theorem 2.1 (support-restricted residue/lift normal form)

Let `R=B(u,v)` for any anchored legal run-transversal word.  Since endpoints
outside `R` are fixed and already use all outside endpoint residues, there
are unique permutations `a,b in Sym(R)` such that

\[
 u_i\equiv S_{a(i)}-S_i\pmod N,
 \qquad
 v_i\equiv E_{b(i)}-E_i\pmod N.
 \tag{2.1}
\]

Using residue representatives `pi_i=S_i mod N` and
`rho_i=E_i mod N`, write

\[
 u_i=\pi_{a(i)}-\pi_i+NA_i,
 \qquad
 v_i=\rho_{b(i)}-\rho_i+NB_i.
 \tag{2.2}
\]

Then mass balance is exactly

\[
 \sum_{i\in R}A_i=\sum_{i\in R}B_i,
 \tag{2.3}
\]

and literal legality is exactly

\[
 \ell_i+v_i-u_i\ge4,
 \qquad
 g_i+u_{i+1}-v_i\ge1.
 \tag{2.4}
\]

Together with the two localized signed necklace equations, (2.1)--(2.4)
are necessary and sufficient for a resident simultaneous middle/q1 trade.

#### Proof

Endpoint transversality and the fixed outside endpoints force the two
permutations.  Congruence gives (2.2).  Permutations preserve the ordinary
sum of their residue sets, so `sum(v-u)=0` reduces to (2.3).  Equations
(2.4) are respectively the new run and following-gap lengths.  Finally,
only changed middle columns and their adjacent `q1` halo can alter either
perfect deck; equality of the old and new localized necklace multisets is
therefore necessary and sufficient.  \(\square\)

### Lemma 2.2 (unique lifts at the resident seed)

Let `C=[a,b]` be a cyclically consecutive component of `R`.  Fixed exterior
boundaries force every new start and end in `C` into

\[
 I_C=[E_{a-1}+2,S_{b+1}-2].
 \tag{2.5}
\]

On the resident `k=15` trace, the maximum cardinalities of `I_C` for
`|C|=1,2,3` are respectively

\[
 63,\qquad 88,\qquad 111,
 \tag{2.6}
\]

all strictly below `N=429`.  Hence every target endpoint residue has at most
one chronological lift in its component.  There are no hidden same-residue
`N`-slides at support at most three.

This proves completeness of the generator: for each two-run support it tests
the three nonidentity pairs in `Sym(2)^2`; for each three-run support it tests
the 26 pairs in `Sym(3)^2` whose combined support is all three runs.  Thus it
examines the exact finite template set

\[
 3\binom{429}{2}+26\binom{429}{3}=340,018,822
 \tag{2.7}
\]

by deterministic fixed-dimensional enumeration, retaining only the 46,928
legal states.  These retained descriptions are injective: maximal-run
decomposition together with any fixed outside anchor recovers the moved
support, chronological lifts, and endpoint-residue permutations uniquely.

## 3. Exact census

The orientation below is the coordinate-zero trace of the authoritative
explicit fixture.  It is the reflection

\[
 c^{\rm fixture}_p=c^{\rm pinned}_{-p\bmod W}
 \tag{3.1}
\]

of the retained annealer seed.  Reflection swaps the start/end labels.  This
explains why the pinned-seed one-neighbor audit reports `907` end and `898`
start moves, while the fixture-oriented table reports the reverse.  It does
not change any pass/fail conclusion.  The literal bitwise identity (3.1) is
independently asserted at line 176 of
`scratch/audit_k15_cspace_weighted_hole_mmm_cube_20260729.py`; the two atlas
summaries visibly exchange start/end and `2+3`/`3+2` categories.

| boundary type | legal states | middle-perfect | q1-perfect | joint-perfect |
|---|---:|---:|---:|---:|
| start-only transposition | 907 | 0 | 1 | 0 |
| end-only transposition | 898 | 0 | 1 | 0 |
| coupled two-run rectangle | 1,045 | 0 | 0 | 0 |
| start-only 3-cycle | 4,078 | 0 | 0 | 0 |
| end-only 3-cycle | 4,037 | 0 | 0 | 0 |
| distinct start/end transpositions (`2+2`) | 9,370 | 0 | 0 | 0 |
| start 2-cycle, end 3-cycle (`2+3`) | 9,700 | 0 | 0 | 0 |
| start 3-cycle, end 2-cycle (`3+2`) | 9,821 | 0 | 0 | 0 |
| paired start/end 3-cycles (`3+3`) | 7,072 | 0 | 0 | 0 |
| **total** | **46,928** | **0** | **2** | **0** |

The new `4,037` END-only negative is therefore one slice of a stronger
closure.  Enlarging end-only arity blindly is not justified: the first
still-open same-order family begins at support four and may be pure
start-only, pure end-only, or coupled.

## 4. Why this is not a universal rectangle obstruction

At `k=7` there are exactly 35 minimum-boundary-support unordered pairs of
joint-perfect traces.  One aligned pair has

```text
c  =11111110011110001110000111011100000
c' =11111110000011101110000111000111100
```

and

\[
 u=(0,3,0,0,2),\qquad v=(0,2,0,0,3).
 \tag{4.1}
\]

Thus both shores move on the same two run slots and the coupled rectangle is
genuinely joint-perfect.  It changes all five quotient columns even though
its boundary support is two.  The `k=15` no-go is therefore a property of
the audited seed's two-deck fibre, not of run-transversal geometry alone.

## 5. Exact event-stream translation

Write the physical Johnson event stream as

\[
 T_{t+1}=T_t-\{\alpha_t\}+\{\beta_t\}.
 \tag{5.1}
\]

For scalar run `j` and coordinate `x`, the translated membership run is
`[S_j+xN,E_j+xN]`, so exactly

\[
 \beta_{S_j+xN-1}=x,
 \qquad
 \alpha_{E_j+xN}=x.
 \tag{5.2}
\]

Its one-lifetime and following zero-lifetime are `ell_j` and `g_j`.
Consequently a boundary displacement performs the literal lifetime surgery

\[
 \boxed{\ell'_j=\ell_j+v_j-u_j,\qquad
        g'_j=g_j+u_{j+1}-v_j.}
 \tag{5.3}
\]

Equivalently, one-residence through `d` is

\[
 \beta_i\notin\{\alpha_{i+1},\ldots,\alpha_{i+d}\},
 \tag{5.4}
\]

and dual residence is

\[
 \alpha_i\notin\{\beta_{i+1},\ldots,\beta_{i+d}\}.
 \tag{5.5}
\]

These are respectively `ell_j>=d+1` and `g_j>=d+1`.  The first controls the
lower ranks; the second controls the upper ranks.

Put

\[
 \psi_q(t)=(q-t)^+,
 \qquad
 \Phi_H(t)=\sum_{q=1}^H\psi_q(t)
           =\binom{(H-t+1)^+}{2}.
 \tag{5.6}
\]

The event-stream run-deficit theorem gives, for every legal strict-spiral
displacement and `1<=q<=W`,

\[
 \frac{\Delta E_q^-}{k}
 =\sum_j[\psi_q(\ell_j+v_j-u_j)-\psi_q(\ell_j)],
 \tag{5.7}
\]

\[
 \frac{\Delta E_q^+}{k}
 =\sum_j[\psi_q(g_j+u_{j+1}-v_j)-\psi_q(g_j)],
 \tag{5.8}
\]

and the exact short-zero potential change is

\[
 \boxed{
 \Delta\mathcal Z_H
 =\sum_j[\Phi_H(g_j+u_{j+1}-v_j)-\Phi_H(g_j)].}
 \tag{5.9}
\]

This is not an entropy proxy.  It is the coefficient-exact aggregate upper
rank deficit.

### Theorem 5.1 (coupled kernel-potential criterion)

A displacement produces another resident middle/q1-perfect carrier with
strictly smaller `Z_H` if and only if all of the following hold:

1. the legal circulation conditions (2.3)--(2.4) and the two endpoint
   residue permutations hold;
2. the localized signed middle-necklace vector vanishes;
3. the localized signed q1-necklace vector vanishes;
4. the right side of (5.9) is negative.

The first three items are the exact structural/two-deck kernel.  Equation
(5.9) makes the fourth equivalent to strict potential decrease.  If also
every `g'_j>=H`, all upper windows through depth `H` have the expected rank;
for the strict Johnson dilation tower through depth `H`, the safe condition
is `g'_j>=H+1`.

The potential has a Robin--Hood marginal law.  With

\[
 \lambda_H(t)=\Phi_H(t)-\Phi_H(t+1)=(H-t)^+,
 \tag{5.10}
\]

moving one zero-letter from a donor gap `a` to a recipient gap `b` changes
the potential by

\[
 (H-g_a+1)^+-(H-g_b)^+.
 \tag{5.11}
\]

Thus a legal circulation improves the capacity precisely when the total
marginal cost of shortening gaps is smaller than the total credit from
lengthening gaps.  Middle/q1 balance remains the hard coupling.

## 6. MMM shear: positive capacity motion, not compiler descent

The verified MMM switch

\[
 (1807,7,12)\longrightarrow(1807,11,12)
 \tag{6.1}
\]

is an extensive coupled event move.  It preserves the middle and lower-q1
decks, one-residence, and the 47 lower-q2 holes.  For `H=7`,

\[
 \mathcal Z_7:2973\longrightarrow2961,
 \qquad \Delta\mathcal Z_7=-12
 \tag{6.2}
\]

in quotient units, equivalently `-180` physical rank-deficit units.  Exact
upper holes improve `95 -> 94`.

It is not a simultaneous protected-compiler descent.  The terminal lower-q3
positive-degree missing set changes from 11 to 12 quotient orbits, creating
representative `1159`; equivalently, the rank-five protected-envelope
zero-degree targets worsen `165 -> 180`, exactly its 15 rotations.  Ranks
one through four retain zero zero-degree targets.  Moreover the audited
five-menu parallel family has only two residence-clean unit-voltage
assignments, namely this pair.  Hence that finite family contains no state
that improves both (6.2) and this mandatory terminal compiler prerequisite.

A full compiler Hall number is not available for either state: both fail the
earlier lower-q2 gate with 47 holes, so the fail-closed compiler was not
invoked and no core/cut was selected.  It would therefore be incorrect to
report a Hall-deficiency change.  What is rigorously proved is potential
descent together with deterioration of a necessary protected-port gate.

This is the sharp proved boundary.  A true next move must be either

- a support-at-least-four pure or coupled circulation satisfying Theorem 5.1
  and the exact compiler-Hall audit; or
- a composition of wider MMM/gluing switches whose event-potential gains
  cancel their lower-terminal damage.

No theorem here says that short-zero potential controls necklace holes or
compiler Hall.  They are separate fail-closed filters.

## 7. Frozen artifacts

```text
scratch/audit_k15_coupled_run_support3_atlas_20260729.cpp
d4ed720fc3171e336c0de2b63df1d3260362dbc44ad94773b0ea9a60ae08bc78

scratch/k15_coupled_run_support3_atlas_20260729.tsv
c19b9085487bc22d49623d89a651d040b4e198828b70d7a68dba6694a683a9cc

scratch/k15_coupled_run_support3_atlas_20260729.summary.txt
e5b89413798880c4ab365a3b3c7d0126e57fc710f554eb0b3cc26653c06e2ed7

scratch/k15_runtrans_seed_3eac_20260729.cw
7dd31950ffd69eea819d5ea413feb66f1d32bc1d88fe206a2b11faf26c1fd332

scratch/audit_strict_spiral_three_run_cycles_20260729.py
3a490101dc0d79d6ed504d954e4604150d2df1af7ea5f4f6f1c44a5ee2400165

scratch/strict_spiral_three_run_cycle_audit_20260729.json
bbeadffb2669c95f09924a941959c80ad51e3a5c76c30a541252da325aad4e31

scratch/audit_k15_event_stream_rank_deficit_20260729.py
8f592dc49682bcb6d896e9a79df0ac6dc8bd8b0e5b13990a62053719fb844c80

scratch/k15_event_stream_rank_deficit_20260729.audit.json
4580f1df6c5316ae39216496c766e50e54c28ffa4b0b4932b20a60f3971f1270
```

The TSV stores every structurally legal candidate, not merely survivors.
Its `run_local_toggles` field counts pre-XOR run-local membership toggles and
is not asserted to equal final trace Hamming distance.  The authoritative
mathematical conclusion is the exact category census and zero middle-perfect
count above.
