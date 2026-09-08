# Complete odd-composition normal form for the `k=15` NAND/Euler face

Date: 2026-07-29

Status: exact parameterization, fail-closed general mixed-step search, and
independently verified finite certificates.  This note does **not** claim a
`k=15` coefficient-one word and does not turn search failure into an
infeasibility statement.

## 1. Complete parameterization

Put

\[
 k=15,\qquad C=429,\qquad W=kC=6435.
\]

In a class-balanced complement-coherent NAND word, list the `C` special
zeros (the departures followed by a zero at distance three) in increasing
lifted order,

\[
 L_0<L_1<\cdots<L_{C-1}<L_C=L_0+W,
 \qquad \Delta_a=L_{a+1}-L_a.
\]

### Theorem 1 (odd-composition normal form)

Up to cyclic origin, the class-balanced complement-coherent NAND/Euler
words having physical residence at least four are in bijection with vectors

\[
 \boxed{\Delta_a=7+2y_a,\quad y_a\in\mathbb Z_{\ge0},\quad
        \sum_{a=0}^{428}y_a=1716}                  \tag{1.1}
\]

such that the `429` prefix residues

\[
 \boxed{0,\Delta_0,\Delta_0+\Delta_1,\ldots,
   \Delta_0+\cdots+\Delta_{427}\pmod {429}}        \tag{1.2}
\]

are all distinct.  Given the vector, the word is reconstructed uniquely by
placing zeros in block `a` at

\[
 L_a,\ L_a+3,\ L_a+5,\ldots,L_{a+1}-2             \tag{1.3}
\]

and ones everywhere else, then setting `c_p=d_(2p)`.

#### Proof

Between consecutive special zeros, the first zero gap is three and every
remaining zero gap is two.  Therefore every `Delta_a` is odd.  The physical
one-run paired with the block has length `(Delta_a+1)/2`; residence four is
equivalent to `Delta_a>=7`.  The gaps sum to `W`, so writing
`Delta_a=7+2y_a` gives

\[
 \sum y_a={15C-7C\over2}=4C=1716.
\]

Class balance is equivalent to having one special departure in every
residue modulo `C`.  These residues are exactly the prefix sums (1.2), so
this is equivalent to their being a permutation.

Conversely, (1.1)--(1.2) and (1.3) give exactly one gap-three departure in
each residue and only gap-two departures otherwise.  If `b_v` denotes the
number of gap-two departures from residue `v`, flow balance gives
`b_v=b_(v-2)`.  Since `C` is odd, all `b_v` are equal, and their total is
`6C`; hence every residue has six gap-two departures.  Thus the projected
zero walk is exactly an Euler circuit of the multigraph with six arcs
`v->v+2` and one arc `v->v+3` at every vertex.  The NAND law, all class
sums, every Johnson seam, and residence four follow.  Block reconstruction
is forced.  This proves both directions.  \(\square\)

This is strictly larger than the old affine step-seven portfolio.  That
portfolio put almost all `1716` units into at most four entries.  The parity
rotor disperses them over all `429` entries.  The new search ranges over the
whole normal form (1.1)--(1.2).

## 2. Exact objectives

For a reconstructed word, let `H_v` be its seven zero heights in residue
`v`, and let `lambda_v` be the marked special-zero height.  Rotation
canonicalization gives

\[
 \Phi=|\{[H_v]:v\in\mathbb Z_C\}|,
 \qquad
 \Psi=|\{[H_v\setminus\{\lambda_v\}]:v\in\mathbb Z_C\}|. \tag{2.1}
\]

The exact targets are

\[
 \boxed{\Phi=429,\qquad \Psi=335.}                 \tag{2.2}
\]

`Phi` is simultaneously middle and lower-`q1` necklace coverage.  `Psi` is
lower-`q2` coverage and, by complement coherence, dual upper-`q1` coverage.
The two short rank-six orbits are weighted by their actual orbit sizes in
the physical counter; `Psi=335` is equivalent to all `5005` physical
rank-six targets being present.

Let `P_phi` and `P_psi` be the sums of `binom(load,2)` over the two orbit
palettes.  There are 429 samples on 429 middle targets and 429 samples on
335 punctured targets.  Consequently

\[
 P_\Phi\ge429-\Phi,
 \qquad
 P_\Psi\ge94+(335-\Psi)
\]

in the live deficit range, and

\[
 \boxed{\Xi=P_\Phi+P_\Psi-94\ge
 (429-\Phi)+(335-\Psi),}                           \tag{2.3}
\]

Thus `Xi=0` is a smooth sufficient certificate for both complete palettes.
The converse needs the punctured load profile to be floor-balanced: a
complete `Psi=335` deck may still contain a triple load, in which case
`P_Psi>94` and `Xi>0`.  The second portfolio deliberately optimizes this
stronger potential because it supplies a multiplicity gradient; it does not
identify `Xi` with the logical coverage condition.

## 3. Search implementation and soundness boundary

The implementation is

```text
scratch/k15_nand_euler_mixed_step_search.cpp
```

It uses two complete coordinate systems:

1. balanced transfers and rearrangements of the `y_a` in (1.1), followed by
   an exact prefix-permutation test;
2. swaps/cycles/block swaps in the long-residue permutation, followed by
   the unique minimum odd lift and all legal remaining `2C` lift units.

Every scored state is rebuilt into its literal height fibres.  Every emitted
word then undergoes a separate eager bit audit checking:

* `00` and `111` are absent;
* exactly 429 long gaps occur, one in each residue;
* all 429 class sums equal eight;
* every seam is Johnson;
* physical minimum one-run is at least four;
* fast height scores equal literal middle and triple-intersection scores.

The independent retained verifier is

```text
scratch/verify_k15_nand_gap_candidate.py
```

It reads only the emitted `c` word.  Therefore every reported positive
certificate is sound.  The moves are heuristic and not known to connect the
whole feasible-state graph, so no `UNSAT` or optimality conclusion can be
drawn from any finite run.

## 4. Calibration and retained certificates

The self-test reproduces both earlier constructions:

| seed | `Phi` | `Psi` | minimum run |
|---|---:|---:|---:|
| two-adjacent-defect carry fan | 42 | 42 | 4 |
| parity rotor | 82 | 80 | 4 |

One local one-core calibration of one million attempts took under one
second and reached `(Phi,Psi)=(366,302)`.  The first remote balanced
portfolio reached `(396,326)`.  Diversified exact portfolios retained:

| objective | `Phi` | `Psi` | status |
|---|---:|---:|---|
| middle first | 409 | 303 | independent `PASS` |
| balanced | 400 | 322 | independent `PASS` |
| alternating | 396 | 326 | independent `PASS` |
| punctured deck first | 367 | **335** | independent `PASS` |
| `Xi` first, phase two | **404** | **328** | independent `PASS`, `Xi=32` |
| punctured deck fixed | **378** | **335** | independent `PASS`, `Xi=53` |

The last row is the first construction in this face covering all 335
rank-six necklace classes and all 5005 physical rank-six targets; by duality
it also covers the complete first upper shadow.  It is **not** a middle
Hamilton carrier because `Phi=367<429`.

The exact retained files are:

```text
scratch/k15_nand_euler_mixed_phi.cw
scratch/k15_nand_euler_mixed_phi.audit.json
scratch/k15_nand_euler_mixed_balanced.cw
scratch/k15_nand_euler_mixed_balanced.audit.json
scratch/k15_nand_euler_mixed_alternating.cw
scratch/k15_nand_euler_mixed_alternating.audit.json
scratch/k15_nand_euler_mixed_psi.cw
scratch/k15_nand_euler_mixed_psi.audit.json
```

The `Psi=335` word has SHA-256

```text
de3786f9b6b3f3b211e991fbf9f38a2f0a5026b6d63eee07810439c2746d3936
```

and its audit JSON has SHA-256

```text
8901f728b5f2ec2f756b535bec0c241915bb90d875af4d327f1c31d6f97ccb5c
```

The best joint `Xi` point currently retained is

```text
scratch/k15_nand_euler_mixed_pairs_xi32.cw
```

with `(Phi,Psi)=(404,328)`, `(P_phi,P_psi)=(25,101)`, and therefore
`Xi=32`.  Its two load profiles already attain their integrality floors:
`Xi=(429-Phi)+(335-Psi)`.  Its SHA-256 is

```text
f6bcb3a50771f92157cb429b60a20310bf053b688462d91b36fd8ef8afbed543
```

The full-`Psi` point with the largest retained middle support is

```text
scratch/k15_nand_euler_mixed_q2full_phi378.cw
```

with `(Phi,Psi)=(378,335)` and all 5005 physical first-shadow targets.

## 4.1 Two global moves omitted by the old search

If one interval has `Delta>=7+2C`, moving one full `2C` lift unit from it
to any other interval preserves every prefix residue modulo `C`.  Hence

\[
 (\Delta_i,\Delta_j)\longmapsto
 (\Delta_i-2C,\Delta_j+2C)                         \tag{4.1}
\]

is always prefix-valid.  The implementation now includes this exact
`LiftTransfer` move.  The current best certificates lie on the no-extra-lift
face, so it does not alter those particular neighborhoods; it is needed for
complete exploration above other residue orders.

There is also a global two-parent representation.  A candidate is one
marked lifted point

\[
 P_v=v+C\lambda_v
\]

for every residue `v`.  Given two retained parents, select either parental
height independently for each residue, sort the 429 selected points, and
accept precisely when every cyclic consecutive gap is odd and at least
seven.  This is an exact `2^429` hybrid cube, not a relaxation.  For the
retained middle-first and punctured-first parents, 193 heights differ;
236 single-coordinate switches and 27,777 two-coordinate switches are
already feasible.  A dedicated fail-closed crossover mode is present in the
C++ search.  Its ability to improve `Xi` is empirical and not assumed.

## 5. What remains

The complete finite coverage gate inside this symmetry face is
`(Phi,Psi)=(429,335)`; `Xi=0` is a stronger floor-balanced sufficient
target.  Even `Xi=0` would supply only the middle, lower-`q1`, lower-`q2`,
and dual upper-`q1` gates.  The wider shadow tower and exact lower compiler
must still be audited before a length-6438 contiguous-OR word can be
claimed.  Conversely, failure to reach `Xi=0` would not refute either this
symmetry face or the original conjecture.
