# Compact two-`AllDifferent` Markov moves and the `k=15` perfect-face atlas

Date: 2026-07-29

Status: independently audited exact move normal form; exact distinction between the formal toric
lattice, chronological applicability, and perfect-deck connectivity;
complete support-four permutation skeleton; explicit unbounded nonnegative
Markov-degree example; five new solver-free `k=15` finite audits run on the
H100 CPU; and a sharp statement of the unclosed move classes.  No complete
support-four atlas and no q2 improvement are claimed.

## 1. Main conclusions

Let a strict cyclic run schedule have `N` inclusive one-runs

\[
 [S_i,E_i],\qquad
 \ell_i=E_i-S_i+1,\qquad
 g_i=S_{i+1}-E_i-1,                                \tag{1.1}
\]

where

\[
 \ell_i\ge h,\quad g_i\ge1,\quad
 \sum_i\ell_i=rN,\quad \sum_i g_i=(k-r)N,        \tag{1.2}
\]

and both endpoint-residue lists

\[
 \pi_i=S_i\pmod N,\qquad \rho_i=E_i\pmod N       \tag{1.3}
\]

are permutations of `Z_N`.

The exact conclusions are as follows.

1. Every same-run-order move is uniquely a pair of endpoint permutations
   decorated by integer lift vectors.  Rank preservation is equality of the
   total start and end cycle windings; positivity is one sharp interval
   inequality per run.
2. The expanded integer lattice has generators of boundary support at most
   two.  Therefore the proved `k=15` support-at-most-three obstruction is
   not toric torsion: it comes from nonnegative chronology and the
   middle/q1 perfect-deck face.
3. Inside a fixed endpoint-permutation chamber, the known `N`-block life and
   gap transfers are a complete Markov basis.  The resident `k=15` chamber
   is a singleton, so none applies there.
4. Cross-chamber nonnegative Markov degree is not uniformly bounded.  An
   explicit interval-domain face has two `N`-state lift chambers, and every
   bridge between them has support `N`; at `N=4` one such bridge is a literal
   support-four dual-gap descent.
5. A no-slide boundary-support-four move has exactly `453` endpoint-
   permutation skeletons on a fixed four-set.  At the resident `k=15` seed
   every four-run component collar is shorter than `429`, so these skeletons
   are exhaustive.
6. Three new finite `k=15` classes are closed exactly:

   * a four-consecutive-run boundary block has no structurally legal
     nonidentity state;
   * the `46,928` legal support-at-most-three states have `46,928` distinct
     nonzero middle/q1 signatures and no opposite pair;
   * there is no legal single life transfer and no legal single gap transfer
     in the compact composition.
7. The first nonlinear fixed-cut two-gap-pulse audit finds `157`
   structurally legal schedules, of which `72` strictly improve the exact
   dual-gap potential.  None preserves the middle deck or q1.  The closest
   has only two middle holes and one q1 hole while improving the potential by
   twelve.  The bank contains one genuine resident seam-support-four move;
   it instead has score `(Delta Z_7,middle holes,q1 holes)=(+15,16,11)`.
8. All `12,246` unordered pairs of those `157` states were then combined as
   direct larger compact edits.  There are `12,056` structurally legal
   distinct terminals and `5,196` dual-gap improvements, but no middle/q1-
   perfect terminal.
9. Among the move families audited here, the known extensive MMM selector
   remains the only proved connection from the resident seed to a better
   middle/q1-perfect state:

   \[
   \mathcal Z_7:2973\to2961,
   \qquad \operatorname{miss}_U:95\to94,
   \qquad \operatorname{miss}_{q2}:47\to47.         \tag{1.4}
   \]

   It preserves middle/q1 but worsens lower q3 from `11` to `12`.  No
   middle/q1-preserving move proved here improves q2.

Thus support four is the first open class only in the **boundary-seam
support** metric.  In the direct `(life,gap)` metric, support-two long-block
shears and support-four two-pulse shears are different, generally seam-dense
objects.

## 2. Exact lifted two-permutation normal form

Let another aligned schedule have

\[
 S_i'=S_i+u_i,\qquad E_i'=E_i+v_i,\qquad u_N=u_0. \tag{2.1}
\]

Put

\[
 a_i=\ell_i-h,\qquad b_i=g_i-1.                   \tag{2.2}
\]

### Theorem 2.1 (complete compact structural move theorem)

The new schedule lies in the same rank-`r`, residence-`h` structural fibre
if and only if there are unique permutations `sigma,tau in S_N` and unique
integer lift vectors `A,B` such that

\[
 u_i=\bar\pi_{\sigma(i)}-\bar\pi_i+NA_i,           \tag{2.3}
\]

\[
 v_i=\bar\rho_{\tau(i)}-\bar\rho_i+NB_i,           \tag{2.4}
\]

\[
 \boxed{\sum_iA_i=\sum_iB_i,}                      \tag{2.5}
\]

and

\[
 \boxed{u_i-a_i\le v_i\le u_{i+1}+b_i
        \quad(i\in\mathbb Z_N).}                   \tag{2.6}
\]

Here the barred residues are their representatives in `{0,...,N-1}`.  The
composition changes are exactly

\[
 \boxed{
 \Delta\ell_i=v_i-u_i,
 \qquad
 \Delta g_i=u_{i+1}-v_i.}                          \tag{2.7}
\]

#### Proof

The two modular `AllDifferent` constraints say that the new start and end
residue lists are permutations of the old lists.  This uniquely gives
`sigma,tau` and the integer quotient lifts in (2.3)--(2.4).  Permutations
preserve ordinary residue sums, so

\[
 \sum_i u_i=N\sum_iA_i,\qquad
 \sum_i v_i=N\sum_iB_i.                             \tag{2.8}
\]

Preservation of total one-mass is `sum(v-u)=0`, exactly (2.5).  The two
inequalities in (2.6) are respectively

\[
 \ell_i+v_i-u_i\ge h,\qquad
 g_i+u_{i+1}-v_i\ge1.                               \tag{2.9}
\]

Conversely, (2.7) and (2.6) give a positive chronological decomposition,
and

\[
 S_i'+\ell_i'+g_i'=S_{i+1}+u_{i+1}=S_{i+1}'.       \tag{2.10}
\]

Endpoint transversality plus (2.5) then gives every class sum and every
Johnson seam.  ∎

This is a groupoid normal form: the allowed residue permutation changes
with the source state.  It is not one translation-invariant lattice in raw
`(life,gap)` coordinates.

### Corollary 2.2 (cycle windings and phase)

For a cycle `C` of `sigma`, define

\[
 \omega_S(C)={1\over N}\sum_{i\in C}u_i
             =\sum_{i\in C}A_i,                    \tag{2.11}
\]

and define `omega_E(D)` for cycles of `tau`.  Nonzero lift fixed points are
one-cycles.  Then rank preservation is precisely

\[
 \boxed{
 \sum_C\omega_S(C)=\sum_D\omega_E(D).}             \tag{2.12}
\]

The endpoint barycentres

\[
 \Phi_S={\sum_iS_i-\binom N2\over N}\pmod k,
 \qquad
 \Phi_E={\sum_iE_i-\binom N2\over N}\pmod k       \tag{2.13}
\]

satisfy

\[
 \Phi_E-\Phi_S=r-1\pmod k,                         \tag{2.14}
\]

and a move changes both by the common winding in (2.12).  For any restricted
move catalogue, the subgroup generated by

\[
 (\Omega,\operatorname{sgn}\sigma,
          \operatorname{sgn}\tau)
 \in\mathbb Z_k\times\mathbb Z_2^2                 \tag{2.15}
\]

is therefore an exact reachability obstruction.  The unrestricted formal
lattice generates the full phase/parity group, so (2.15) is catalogue-
specific, not a universal obstruction.

## 3. Formal lattice versus a legal Markov basis

Introduce start- and end-assignment permutation matrices `X,Y` and lift
coordinates `z,w` by

\[
 S_i=\sum_a aX_{ia}+Nz_i,\qquad
 E_i=\sum_a aY_{ia}+Nw_i.                           \tag{3.1}
\]

After deleting (2.6), the integer kernel is generated by:

1. `2 x 2` Birkhoff rectangles in `X`;
2. `2 x 2` Birkhoff rectangles in `Y`;
3. within-start lift transfers `N(e_i-e_j)`;
4. within-end lift transfers; and
5. one paired start/end phase lift and its inverse.

Indeed, decompose the two permutation differences into even alternating
cycles and then into transpositions.  What remains is divisible
coordinatewise by `N`; within-shore transfers reduce each residual vector
to one coordinate, and (2.5) pairs the two remaining totals.  Thus the
formal lattice is generated in boundary support at most two.

These formal generators are not automatically an applicable cross-chamber
Markov basis.  A formal rectangle can leave the nonnegative assignment face;
an applicable assignment move can violate chronology (2.6); and a
structurally legal move can violate the middle/q1 deck equations.  Properly
applicable assignment rectangles preserve the two modular `AllDifferent`
constraints.

Inside a fixed endpoint-permutation chamber, write

\[
 \ell_i=L_i+Np_i,\qquad g_i=G_i+Nq_i.              \tag{3.2}
\]

The two nonnegative weak-composition factors are connected by

\[
 p\mapsto p+e_i-e_j,\qquad q\mapsto q+e_i-e_j,     \tag{3.3}
\]

whenever the donor is positive.  This is the complete chamber Markov basis
already proved in
`MATH_THEOREM_RUN_TRANSVERSAL_CSPACE_MARKOV_BASIS_AND_TWO_DECK_TRADES_20260729.md`.

At the resident seed,

\[
 4\le\ell_i\le32<429,\qquad1\le g_i\le44<429.     \tag{3.4}
\]

Every length is its least legal congruence representative.  Hence

\[
 P=Q=0,                                             \tag{3.5}
\]

and its chamber is a singleton.  Every nontrivial move must change at least
one endpoint permutation.

## 4. The complete boundary-support-four skeleton

Assume a boundary move has exact support `R`, `|R|=4`, and there is no
nonzero `N`-slide.  Its endpoint assignments are a pair

\[
 (\sigma,\tau)\in\operatorname{Sym}(R)^2
\]

with no point fixed by both.  Inclusion-exclusion gives

\[
 \boxed{
 D_4=\sum_{j=0}^4(-1)^j\binom4j((4-j)!)^2=453.}    \tag{4.1}
\]

Writing `2,3,22,4` for a transposition, a 3-cycle, two disjoint
transpositions, and a 4-cycle, the complete list up to exchanging the two
shores is:

| unordered shore cycle types | ordered count |
|---|---:|
| `1 / 22` | 6 |
| `1 / 4` | 12 |
| `2 / 2` with disjoint supports | 6 |
| `2 / 3` | 48 |
| `2 / 22` | 36 |
| `2 / 4` | 72 |
| `3 / 3` | 48 |
| `3 / 22` | 48 |
| `3 / 4` | 96 |
| `22 / 22` | 9 |
| `22 / 4` | 36 |
| `4 / 4` | 36 |

The counts sum to `453`.  Under simultaneous conjugacy by `S_4`, there are
`32` templates: `26` connected permutation graphs and `6` consisting of two
two-vertex components.

Here is an exact Burnside proof of the latter assertion.  If `g in S_4`, a
pair fixed by simultaneous conjugation lies in `C(g)^2`.  Inclusion-exclusion
over the vertices fixed by both permutations gives

\[
 F(g)=\sum_{J\subseteq[4]}(-1)^{|J|}
 \left|\{\gamma\in C(g):\gamma|_J=\operatorname{id}_J\}\right|^2. \tag{4.2}
\]

Checking the five centralizers gives the following table; `F_conn(g)` counts
the pairs for which the undirected two-colour permutation graph is connected,
equivalently \(\langle\sigma,\tau\rangle\) is transitive.

| cycle type of `g` | class size | `|C(g)|` | `F(g)` | disconnected | `F_conn(g)` |
|---|---:|---:|---:|---:|---:|
| `1^4` | 1 | 24 | 453 | 27 | 426 |
| `2 1^2` | 6 | 4 | 9 | 9 | 0 |
| `2^2` | 3 | 8 | 57 | 15 | 42 |
| `3 1` | 8 | 3 | 0 | 0 | 0 |
| `4` | 6 | 4 | 15 | 3 | 12 |

For completeness, the nonidentity centralizer counts are immediate.  The
centralizer of a transposition is
`{1,(12),(34),(12)(34)}`, giving `4^2-3^2+2=9`; the order-eight centralizer of
`(12)(34)` contains two complementary single transpositions and five
fixed-point-free elements, giving `8^2-3^2+2=57`; every element centralizing
a 3-cycle fixes the remaining vertex; and the cyclic order-four centralizer
of a 4-cycle gives `4^2-1=15`.

Consequently

\[
 {453+6\cdot9+3\cdot57+8\cdot0+6\cdot15\over24}=32,              \tag{4.3}
\]

whereas

\[
 {426+6\cdot0+3\cdot42+8\cdot0+6\cdot12\over24}=26.             \tag{4.4}
\]

Validity excludes isolated vertices.  Hence a disconnected two-colour graph
has component sizes `2+2`.  On either component its nonzero restriction is
one of

\[
 S=(\text{swap},1),\qquad
 E=(1,\text{swap}),\qquad
 B=(\text{swap},\text{swap}).
\]

Up to simultaneous conjugacy a disconnected template is an unordered
two-multiset from `{S,E,B}`, giving exactly
\(\binom{3+2-1}{2}=6\) templates.  This independently matches `32-26=6` and
completes the classification.

### Lemma 4.1 (unique support-four lifts at the seed)

For a consecutive moved component of size `s`, every new endpoint lies in

\[
 I_{a,s}=[E_{a-1}+2,S_{a+s}-2].                     \tag{4.5}
\]

The exact resident collar ledger is

| `s` | minimum size | maximum size | sum over `a` |
|---:|---:|---:|---:|
| 1 | 4 | 63 | 8,580 |
| 2 | 12 | 88 | 15,015 |
| 3 | 19 | 111 | 21,450 |
| 4 | 33 | 143 | 27,885 |

In particular every component collar has size below `N=429`.  Each requested
endpoint residue therefore has at most one chronological lift.  There are no
hidden `429`-slides, and every triple `(R,sigma,tau)` determines at most one
literal candidate.

### Corollary 4.2 (balanced cycle packets)

Decorate every start/end cycle by its winding (2.11).  A packet is
cycle-indecomposable precisely when no nonempty proper choice of its start
and end cycles has equal winding sum.  This is the correct primitive notion
at the permutation/lift level.  It does not assert that a zero-winding
4-cycle is primitive in the unrestricted formal lattice, where transpositions
still generate.

## 5. The canonical seam quartet and its resident pruning

Choose start slots `a,b`, end slots `c,d`, and integers `x,y,omega`.  Put

\[
 u_a=x,\qquad u_b=N\omega-x,                       \tag{5.1}
\]

\[
 v_c=y,\qquad v_d=N\omega-y,                       \tag{5.2}
\]

where the residue congruences make `(a b)` a start transposition and `(c d)`
an end transposition.  All other entries vanish.  This is the canonical
balanced seam square.  It is legal exactly when (2.6) holds.

If the four slots are distinct, its composition effects are

\[
\begin{aligned}
 \Delta\ell_a&=-x,&
 \Delta\ell_b&=-(N\omega-x),&
 \Delta\ell_c&=y,&
 \Delta\ell_d&=N\omega-y,\\
 \Delta g_{a-1}&=x,&
 \Delta g_{b-1}&=N\omega-x,&
 \Delta g_c&=-y,&
 \Delta g_d&=-(N\omega-y).
\end{aligned}                                      \tag{5.3}
\]

Coincident indices add their contributions.

### Lemma 5.1 (the resident disjoint quartet has zero winding)

Assume the start and end pairs are disjoint.  If `omega>0`, then at the two
start slots `v=0`, and the run inequalities give

\[
 429\omega=\sum_{\{a,b\}}u_i
 \le\sum_{\{a,b\}}(\ell_i-4)\le56,                 \tag{5.4}
\]

impossible.  If `omega<0`, use the two end slots to obtain

\[
 429|\omega|\le56,                                  \tag{5.5}
\]

again impossible.  Hence

\[
 \boxed{\omega=0.}                                  \tag{5.6}
\]

The tempting rank-seven intermediate excursion is therefore unavailable in
this disjoint resident quartet.  If no end-supported slot immediately
precedes a start-supported slot, gap legality also separates into legality
of the two zero-winding partial swaps.  Only adjacent gap cancellation can
make a new structural portal; otherwise the only possible benefit is exact
middle/q1 signature cancellation.

## 6. Direct compact moves and the support-metric correction

Let

\[
 A_i=\Delta\ell_i,\qquad B_i=\Delta g_i,\qquad
 \sum_iA_i=\sum_iB_i=0.                             \tag{6.1}
\]

Anchor `u_0=0` and define

\[
 u_i=\sum_{j<i}(A_j+B_j),
 \qquad v_i=u_i+A_i.                                \tag{6.2}
\]

### Theorem 6.1 (complete direct-composition criterion)

The edit `(A,B)` is a legal compact schedule move if and only if

\[
 \ell_i+A_i\ge h,\qquad g_i+B_i\ge1,               \tag{6.3}
\]

and both lists

\[
 (S_i+u_i\pmod N)_i,\qquad(E_i+v_i\pmod N)_i      \tag{6.4}
\]

are permutations.  Equations (6.2) invert (2.7), proving necessity and
sufficiency.

A compact four-cell edit makes `u` piecewise constant on as many as four
macroscopic arcs and can therefore have large seam support.  Conversely, a
seam move supported on `R` satisfies

\[
 \operatorname{supp}\Delta\ell\subseteq R,
 \qquad
 \operatorname{supp}\Delta g\subseteq R\cup(R-1). \tag{6.5}
\]

Thus the union of affected run indices has size at most `2|R|`, although the
number of nonzero scalar cells across the two arrays can be as large as
`3|R|`.  Statements about “support four” must specify which metric is meant.

### Corollary 6.2 (single compact transfers)

A single gap transfer

\[
 B=t(e_a-e_b),\qquad A=0                            \tag{6.6}
\]

translates the run-index interval `I=(a,b]` rigidly by `t`.  It preserves
both modular `AllDifferent` constraints exactly when

\[
 \boxed{\pi(I)+t=\pi(I),\qquad \rho(I)+t=\rho(I).} \tag{6.7}
\]

A single life transfer translates start indices `(a,b]` and end indices
`[a,b)`; its exact criterion is

\[
 \boxed{
 \pi((a,b])+t=\pi((a,b]),
 \qquad
 \rho([a,b))+t=\rho([a,b)).}                        \tag{6.8}
\]

For `N=429`, a nonempty `+t`-invariant subset is a union of translation
cycles of length

\[
 {429\over\gcd(429,t)}.                             \tag{6.9}
\]

The donor bounds are `|t|<=28` for life and `|t|<=43` for gaps.  Thus a
nonzero life-transfer interval has length at least `33`, while a nonzero gap
interval has length at least `11`.  The smallest arithmetic gap portals are
`t=39`, length `11`, and `t=33`, length `13`.  The exact seed audit below
shows that even these do not occur simultaneously on both endpoint shores.

## 7. The nonlinear gap two-pulse family

Let

\[
 B=t(e_a-e_b)+s(e_c-e_d),\qquad A=0.                \tag{7.1}
\]

Then

\[
 u=v=t\mathbf1_I+s\mathbf1_J,
 \qquad I=(a,b],\quad J=(c,d].                      \tag{7.2}
\]

Let `A_(epsilon,delta)` be the four run-index atoms cut out by `I,J`.  The
move is structurally legal exactly when the four translated start-residue
sets

\[
 \pi(A_{\epsilon\delta})+\epsilon t+\delta s       \tag{7.3}
\]

partition `Z_N`, the analogous four end-residue sets partition `Z_N`, and
the edited gaps remain positive.  This is an exact atom-partition theorem.

Equivalently, for every nontrivial character `chi` of `Z_N`,

\[
 (\chi(t)-1)F_I^\pi+(\chi(s)-1)F_J^\pi
 +(\chi(t)-1)(\chi(s)-1)F_{I\cap J}^\pi=0,          \tag{7.4}
\]

with the same equation for `rho`.  This is a finite nonlinear four-cut
system, not a moment relaxation.

For disjoint fixed-cut intervals, the cross term vanishes.  If

\[
 \Delta_\pi(I,t)=\mathbf1_{\pi(I)+t}-\mathbf1_{\pi(I)},
\]

and similarly for `rho`, two pulses are legal precisely when their pair of
signed defects are opposites.  This is the exact inverse-defect join used in
the finite audit.

The exact dual-gap potential is

\[
 \mathcal Z_7(g)=\sum_i\Phi_7(g_i),
 \qquad
 \Phi_7(q)=\binom{(8-q)^+}{2}.                      \tag{7.5}
\]

All potential changes in this family are supported on the four edited gap
cells.  Potential descent is only a capacity prefilter; it says nothing by
itself about the orbit decks.

## 8. Exact new `k=15` finite audits

All nontrivial finite enumeration was run CPU-only on the approved H100
host.  Each script is deterministic and solver-free.

### 8.1 Four consecutive seam slots

For each of the `429` cyclic blocks

\[
 R=\{a,a+1,a+2,a+3\},
\]

all `453` joint endpoint-permutation skeletons were checked.  Thus

\[
 429\cdot453=194,337                               \tag{8.1}
\]

raw assignments were examined.  The exact maximum collar size is `143`.
There are

\[
 \boxed{0\text{ structurally legal nonidentity assignments}.}       \tag{8.2}
\]

There is also a short analytic proof.  The common sub-`N` collar contains
one unique lift of each of the four old start residues.  A new start
permutation therefore has the same four literal points; chronological order
forces them pointwise fixed.  The same holds for ends.  Exact support four
is impossible.

This closes only the geometric shape of one block of four consecutive run
slots, not all connected permutation templates on nonconsecutive slots.

### 8.2 Commuting pairs from the support-three atlas

Every one of the `46,928` structurally legal support-at-most-three states
was reconstructed in the TSV's reflected gauge.  Its exact signed middle/q1
orbit vector was computed without hashing.  The result is

\[
 \boxed{
 46,928\text{ distinct nonzero signatures},
 \qquad0\text{ opposite pairs}.}                    \tag{8.3}
\]

Hence no two atlas moves with disjoint q1 halos and commuting boundary
effects can form a perfect-deck composite.  This does not exclude
overlapping-halo nonlinear composites, adjacent boundary interactions, or a
primitive quartet whose halves are illegal separately.

### 8.3 Single direct life/gap transfers

All unordered edit-position pairs and every donor-feasible signed transfer
were tested by the exact invariant-set criteria (6.7)--(6.8).  There are

\[
 \boxed{0\text{ structurally legal nonzero life transfers},}
\]

and

\[
 \boxed{0\text{ structurally legal nonzero gap transfers}.}          \tag{8.4}
\]

Both transfer directions and the complementary wrapping interval are
included.  This closes compact support two only when the other composition
is held fixed; simultaneous life/gap transfers remain open.

### 8.4 Fixed-cut separated gap two-pulses

The exact pulse census is

\[
 1,101,672\text{ nonzero feasible single pulse descriptions}.        \tag{8.5}
\]

Their signed two-shore defects are all nonzero and all distinct.  The exact
inverse join finds

\[
 157\text{ fixed-cut, strictly separated structural pairs}.          \tag{8.6}
\]

Their interval-length types are

\[
 (1,1)^{155},\qquad(1,2)^1,\qquad(2,2)^1.           \tag{8.7}
\]

Of these, `72` have `Delta Z_7<0`; the best potential change is `-30`.
Nevertheless,

\[
 \boxed{
 \text{middle-perfect}=0,
 \qquad q1\text{-perfect}=0.}                       \tag{8.8}
\]

The closest state is

\[
 (48,49,+1),\qquad(224,225,-1),                    \tag{8.9}
\]

meaning the two indicated gap pulses.  It has

\[
 \Delta\mathcal Z_7=-12,\qquad
 \operatorname{miss}_M=2,\qquad
 \operatorname{miss}_{q1}=1.                       \tag{8.10}
\]

Its normalized trace digest is

```text
4573a878ef9896f896f6b4d826e3b1253fa6d7534c7f51a161c04da7bb203b83
```

The fixed-cut qualifier is essential.  The audit omits adjacent pulses
sharing a gap cell and the other cyclic noncrossing pairing whose wrapping
arc becomes nested at the fixed cut.

Moreover, `156` of the `157` states have seam support at most three and are
already corroborated by the old seam atlas.  Only the single type `(2,2)`
state is genuinely seam-support four.  Explicitly, its two gap pulses are

\[
 (101,103,+22),\qquad(374,376,-22).                \tag{8.11}
\]

It is a literal structurally legal resident move of compact gap support four
and seam support four.  Its score is

\[
 \Delta\mathcal Z_7=+15,
 \qquad \operatorname{miss}_M=16,
 \qquad \operatorname{miss}_{q1}=11,              \tag{8.12}
\]

and its normalized trace digest is

```text
fa8b62cb4466088f9f57d5b47bb01e3e286ec9761b350d00ae6389719ca59b72
```

Thus legal support four exists in the resident structural fibre, but this
first exact portal moves away from both the potential and the two protected
decks.

### 8.5 Pairs of the 157 structural states

Every unordered pair was added as a direct terminal compact edit:

\[
 \binom{157}{2}=12,246.                              \tag{8.13}
\]

All terminal edit vectors are distinct; `12,056` pass the two modular
`AllDifferent` constraints and positivity.  Of these, `5,196` strictly
improve `Z_7`, with minimum delta `-58`.  Yet

\[
 \boxed{0\text{ terminals preserve both middle and q1}.}             \tag{8.14}
\]

In fact the minimum middle-hole count and minimum q1-hole count are both
three, and there is one terminal with hole pair `(3,3)`.  This is a direct
compact-support-at-most-eight terminal audit generated by this bank.  It is
not a complete support-eight atlas, and its nonperfect first intermediate
states do not give a path staying inside the perfect face.

## 9. An explicit unbounded nonnegative Markov-degree face

For every `N>=2`, take the abstract compact parameters

\[
 k=N+2,\qquad r=N,\qquad h=N-1.                    \tag{9.1}
\]

Use half-open deletion seams `D_i=S_i+ell_i`.  State `A` has

\[
 \ell_i=N\quad(0\le i<N),                           \tag{9.2}
\]

and all gaps one except

\[
 g_{N-2}=N+1.                                       \tag{9.3}
\]

Its start residues are `i` and its deletion residues are also `i`.  Put

\[
 u_i=1\quad(0\le i\le N-2),\qquad
 u_{N-1}=-(N-1),\qquad v=0.                        \tag{9.4}
\]

The terminal state `B` has

\[
 \ell_i'=N-1\quad(i<N-1),\qquad
 \ell_{N-1}'=2N-1,                                 \tag{9.5}
\]

and every gap equals two.  It is legal, cyclically shifts all start
residues, fixes every deletion residue, and has support `N`.

Restrict the assignment face so row `i` may use only start residue `i` or
`i+1`, while deletion residues stay fixed.  `AllDifferent` forces all binary
choices equal, but the lift surplus can still move.  The face consists of
exactly `2N` schedules:

* in the first chamber the start residues are `i`, every life is `N`, and
  the unique `N`-unit gap surplus may occupy any one of the `N` gaps;
* in the second chamber the start residues are `i+1`, every gap is `2`, and
  the unique `N`-unit life surplus may occupy any one of the `N` runs.

Every move between these two chambers changes the start residue in every
row, hence has seam support at least `N`.  The displayed `A -> B` move is one
legal support-`N` bridge.  Moreover every state in the first chamber and
every state in the second chamber respectively satisfy

\[
 \mathcal Z_2=N-1,
 \qquad \mathcal Z_2=0.                            \tag{9.6}
\]

For `N=4`, this is the concrete support-four move

\[
 (\ell,g)=((4,4,4,4),(1,1,5,1))
\]

to

\[
 (\ell',g')=((3,3,3,7),(2,2,2,2)).                 \tag{9.7}
\]

Thus every move bank connecting this nonnegative face contains a move of
support at least `N`.  This proves unbounded nonnegative Markov degree on
cyclic interval-domain faces.  It is not a middle-level or unrestricted
`k=15` obstruction.

## 10. Exact `k=15` connectivity boundary

The unrestricted graph whose edges are *all* legal displacements is
trivially connected after aligning run order: the difference of any two
states is one legal displacement.  A Markov-basis claim is stronger: it asks
for a prescribed local move bank whose legal intermediate states connect the
whole fibre.

What is proved at the resident seed is:

* support at most three is not a Markov basis for the middle/q1-perfect
  fibre;
* the seed is not globally isolated in the middle/q1-perfect fibre, because
  the extensive MMM selector gives another such state;
* the new bounded classes in Section 8 do not connect the seed to any other
  middle/q1-perfect state;
* the MMM state improves dual-gap and exact upper coverage but leaves q2 at
  `47` holes and creates one q3 hole.

Thus there is currently no proved path of bounded local perfect-face moves
from the resident state, and no proved middle/q1-perfect q2-improving
terminal.

The complete next seam-support-four audit is finite and proof-safe.  The
`453` skeletons reduce under simultaneous conjugacy to `32` templates.  As
an abstract search organization, partitioning four labelled moved vertices
into `1,2,3,4` unordered linearly ordered consecutive blocks gives the Lah
numbers

\[
 24,36,12,1                                         \tag{10.1}
\]

for one, two, three, and four blocks.  Their sum `73` does **not** count
actual four-subsets or cyclic embeddings in `Z_429`; those retain cyclic
placement and inter-block gap-length data.  Component collars give sparse
exact endpoint-relation tables.  Triangle/four-cycle joins for the connected
templates and opposite winding/signature joins for the six disconnected
templates are a proposed enumeration architecture, not an audited exhaustive
reduction.  Every output still requires direct middle/q1 replay because
overlapping q1 halos have a quadratic cross term.

For compact-variable support, the first unclosed deterministic classes are:

1. adjacent and wrap-separated two-gap pulses;
2. overlapping two-pulse atoms governed by (7.3)--(7.4);
3. simultaneous life-and-gap transfers;
4. larger pulse banks designed to repair the explicit `(2,1)` near defect.

Only after the exact middle/q1 equations vanish should q2 and arbitrary-
width upper scores be evaluated.

## 11. Artifacts and audit boundary

Permanent sources:

```text
scratch/audit_k15_compact_connected_support4_20260729.py
scratch/audit_k15_compact_commuting_atlas_pairs_20260729.py
scratch/audit_k15_compact_single_transfer_portals_20260729.py
scratch/audit_k15_compact_disjoint_gap_two_pulse_20260729.py
scratch/audit_k15_compact_two_pulse_pair_composites_20260729.py
```

Frozen outputs:

```text
scratch/connected_support4.audit.json
scratch/commuting_pairs.audit.json
scratch/single_transfer_portals.audit.json
scratch/disjoint_gap_two_pulse.audit.json
scratch/two_pulse_pair_composites.audit.json
scratch/connected_support4.time.txt
scratch/commuting_pairs.time.txt
scratch/single_transfer.time.txt
scratch/disjoint_gap_two_pulse.time.txt
scratch/two_pulse_pair_composites.time.txt
```

Current SHA-256 values are:

```text
0b645fa0659f15dfcc76453dd4ec9b1dc9ea38188541c8fb0ebed34678c19dbb  connected-four source
b2f798d512b1d97c6829c956d28ab78533a16aa212690b13841e01ea872ed905  commuting-pair source
05b24b8df38a297f7a636ee764306a231fc58fc76a5e3524a1122c39c13b9b75  single-transfer source
370a6b42112aaec8c366db639f1d74e26c23e321193bcf81346742c260445226  two-pulse source
946d0be63923c6781fbea4f066cdc145056a638521a8e649bd15fbb482d8d3c1  pair-composite source
6dc2e16b75bb79561546d9932aa17b5bf9b023b05cefe81c7337d69dab9bc37  connected-four result
3a9925cf2949a1d0e2aafcd0aef7f287fb3e441f99dba99b2a1810c6995b43d8  commuting-pair result
2e5b713ec13ad534f01dbae201890f2ccbfd1beb0b87a6e3455a0c889577ebdf  single-transfer result
8c198e350b08ab89ef7dc24315c52621e040d425ac788c02add56280d66a030c  two-pulse result
6301d4a125e72f4e4e994390ba49ce00aa3c7f3d33ee547a578bc2d0145e2d3c  pair-composite result
```

The source/result hashes above are audit identifiers, not mathematical
arguments.  The theorem scopes are:

* the `194,337` audit covers one four-consecutive-run geometric shape;
* the inverse-pair audit covers commuting pairs of individually legal old
  atlas moves;
* the single-transfer audit is cyclically complete for one compact transfer;
* the `157` two-pulse theorem is fixed-cut and strictly separated;
* the `12,246` composite audit ranges only over pairs generated by those
  `157` records.

No finite result in this note closes all boundary-support-four moves, all
compact support-four moves, or perfect-face connectivity.
