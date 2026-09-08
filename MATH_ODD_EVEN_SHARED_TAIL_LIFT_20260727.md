# Odd-to-even shared-tail lift: exact theorem and obstruction audit

Date: 2026-07-27

## 1. The arithmetic is exact only at equal depth

Let the old dimension be `k=2m+1`, put

\[
r=m+1,qquad W=\binom{2m+1}{m+1},
\]

and suppose its exact word has length `W+d_o`.  The next even dimension has
central width `2W` and target length `2W+d_e`.

In a strict two-sector template, take a `z`-free first block of length
`W+d_o` and a `z`-bearing suffix of length

\[
L=2W+d_e-(W+d_o)=W+d_e-d_o.
\]

The depth-`d_e` central row has `2W` cells.  Exactly

\[
2W-(W+d_o-d_e)=W+d_e-d_o=L
\tag{1.1}
\]

of them meet the `z`-bearing suffix.  But exactly half of the even central
layer, namely `W` masks, contain `z`.  Therefore

\[
\boxed{\text{a rank-exact two-block sector lift requires }d_e=d_o.}
\tag{1.2}
\]

This validates the arithmetic for

\[
15\to16,\qquad17\to18,\qquad19\to20,
\]

where both depths are three.  It **rules out** this strict template for
`11 -> 12` and `13 -> 14`, where the depth drops from three to two.  In the
`11 -> 12` case (1.1) gives 461 central cells containing the new coordinate,
whereas the rank-six layer requires 462.

Thus the earlier statement that `13 -> 14` merely needs “one extra
compression” was too optimistic: the two-block support itself has the wrong
central incidence count.

## 2. Exact shared-tail theorem at common depth

Let `X` be the old coordinate set and let `z` be new.  Let

\[
A=(A_0,\ldots,A_{W+d-1})
\]

be an exact old word.  Let

\[
B=(B_0,\ldots,B_{W+d-1}),\qquad B_i\subseteq X,
\]

where zero masks are allowed in `B`.  Define

\[
T_i=\bigcup_{j=0}^{d}A_{i+j},\qquad
R_i=\bigcup_{j=0}^{d}B_{i+j}qquad(0\le i<W).
\]

Assume:

1. **shared tail**

   \[
   (B_0,\ldots,B_{d-1})=(A_W,\ldots,A_{W+d-1});
   \tag{2.1}
   \]

2. `(T_i)` enumerates every rank-`r` mask on `X` exactly once;
3. `(R_i)` enumerates every rank-`r-1` mask on `X` exactly once.

Construct

\[
U=
(A_0,\ldots,A_{W+d-1},
 \{z\}\cup B_d,\ldots,\{z\}\cup B_{W+d-1}).
\tag{2.2}
\]

It has length

\[
(W+d)+W=2W+d=B(2m+2).
\]

### Central-row theorem

The first `W` depth-`d` cells of `U` are the `T_i` and avoid `z`.  By
(2.1), the next `W` projected depth-`d` cells are the `R_i`, and every one
contains `z` in `U`.  Hence the depth-`d` row of `U` enumerates the complete
even central layer exactly once.

### Necessary and sufficient seam condition

Let `M(A,B)` be the following family of projected masks:

\[
\begin{aligned}
\mathcal M(A,B)=
&\left\{\bigcup_{j=s}^{t}B_j: d\le s\le t<W+d\right\}\\
&\cup
\left\{
\left(\bigcup_{i=s}^{W+d-1}A_i\right)
\cup
\left(\bigcup_{j=d}^{t}B_j\right):
0\le s<W+d,\ d\le t<W+d
\right\}.
\end{aligned}
\tag{2.3}
\]

These are exactly the old-coordinate projections of intervals in `U` that
meet the appended `z`-bearing sector.  Intervals avoiding that sector lie in
`A` and cover every nonempty mask on `X`.  Therefore:

> **Shared-tail lift theorem.** Under (2.1)--(2.3), the word `U` is universal
> on `X union {z}` if and only if
>
> \[
> \boxed{\mathcal M(A,B)=2^X.}
> \tag{2.4}
> \]

The empty target in (2.4) is not cosmetic: it is the target `{z}`.  It
forces at least one nonempty interval of the appended part of `B` to consist
entirely of zero masks.  In particular `B` cannot simply be a relabelled
copy of the nonzero old word.

This is the exact seam statement.  There is no probabilistic or asymptotic
loss in it.

## 3. Exact additional input: dual residence

An exact old arrival-clock tableau gives an erosion of the rank-`r`
chronology `(T_i)`.  The second sector needs an erosion of a rank-`r-1`
chronology, naturally the complements of another ordering of the old middle
layer.

For a cyclic binary support word, it is a depth-`d` dilation of some support
if and only if every maximal one-run has length at least `d+1`.  Necessity is
immediate because one selected occurrence creates `d+1` consecutive output
ones.  For sufficiency, place occurrences in each run beginning `d` cells
after its left endpoint, ending at its right endpoint, with gaps at most
`d+1`.

Consequently:

- existence of `A` requires every coordinate's one-runs in `T` to have
  length at least `d+1`;
- existence of a dual erosion `B` for the complement chronology requires
  every coordinate's **zero-runs** in that chronology to have length at
  least `d+1`.

Thus an odd-to-even lift is not a theorem from an arbitrary exact odd word.
It needs a **bi-resident central chronology**, plus the boundary match (2.1)
and marked coverage (2.4).

This is already decisive on the known `k=11` rotors.  For each of the bulk,
multirow, and PBBS-derived exact certificates, every coordinate has:

\[
\min(\text{one-run})=4,qquad
\min(\text{zero-run})=1,qquad
42\text{ runs}.
\]

Relabelling, reversal, and changing the cyclic cut preserve these run
lengths.  Therefore no generic relabel/reversal of any known `k=11`
chronology has a depth-three dual erosion.  The proposed lift requires a new
co-resident rotor, not a seam adjustment to the present one.

## 4. Why a relabelled second copy can never work

There is a second, independent obstruction.  Away from the one projected
zero needed for `{z}`, the depth-`d` row of a relabelled/reversed copy of
`A` has rank `r`.  A zero replacement can affect at most `d+1` consecutive
central cells.  But the `z`-containing even central sector needs projected
rank `r-1` in all `W` cells.  For `W>d+1`, a relabel/reversal of the same
base word is therefore impossible even if its boundary cells match.

The correct second sector is a **dual erosion**, not a coordinate relabel of
the first sector.

An exhaustive restricted audit confirms the obstruction numerically at
`k=11 -> 12`.  For every oriented cyclic cut and every coordinate
permutation whose four-cell prefix matches the required overlap, and for
every location of the projected zero, the best residuals are:

| exact `k=11` input | compatible transformed seams | best missing `k=12` masks |
|---|---:|---:|
| original SAT word | 15,600 | 11 |
| bulk-compiler word | 1,080 | 5 |
| depth-three multirow word | 19,920 | 4 |
| PBBS-derived multirow word | 3,480 | 5 |

These are exhaustive results inside the relabel/reversal shared-overlap
family, not global lower bounds for `k=12`.

The actual exact `k=12` certificate is also visibly outside this template.
The strict lift would give the new coordinate one zero block of length 465
and one one block of length 461.  In the known 926-word, each coordinate is
present only 251--285 times and has 225--267 linear runs.  Its success uses a
distributed new-coordinate support, not a shared-tail sector block.

## 5. Verifier and seam CSP

The exact verifier is

```sh
python3 scratch/verify_odd_even_shared_tail.py \
  --k OLD_ODD_K --depth 3 --old OLD.word --dual DUAL.word \
  --output LIFTED.word --require-universal
```

It independently checks (2.1), both central layers, the marked condition
(2.4), and all contiguous unions in the final word.

The restricted relabel/reversal CSP used for the finite audit is

```sh
c++ -O3 -std=c++20 scratch/audit_odd_even_shared_tail_lift.cpp \
  -o scratch/audit_odd_even_shared_tail_lift

scratch/audit_odd_even_shared_tail_lift \
  11 3 2 scratch/sigma_calibration_bulk_k11_465.word \
  scratch/shared_tail_k12_best_near.word
```

For the general dual seam, a fixed candidate lower-middle chronology
`(R_i)` has a direct SAT formulation.  Use Boolean variables `b[j,x]` for
`x in B_j`.

1. Fix `b[0..d-1,x]` by (2.1).
2. Encode `D^dB=R` coordinatewise:
   - if `x notin R_i`, set every `b[i..i+d,x]=0`;
   - if `x in R_i`, add the clause
     `b[i,x] or ... or b[i+d,x]`.
3. Add a selector for an all-zero appended cell or interval, to cover `{z}`.
4. For each `S subseteq X`, introduce witness variables for the intervals
   in (2.3).  A selected witness forbids every coordinate outside `S` and
   requires every coordinate of `S` to occur in its fixed/variable cells.
   Require at least one witness for each `S`.

Those clauses are exactly (2.1) and (2.4); no sufficiency gap remains.  The
large part is the marked-cover witness catalogue, not the erosion equations.

## 6. Verdict for `15 -> 16`

The length arithmetic is genuinely perfect, but the claimed unconditional
lift is false.  A valid theorem must assume or construct all three items:

\[
\boxed{
\text{bi-resident dual chronology}
+\text{shared erosion boundary}
+\text{marked seam cover}.}
\]

No known certificate supplies the first item under relabel/reversal.  The
highest-value finite target for `k=15` is therefore stronger than the one in
the symmetry sweep: construct the complement-coherent `C_30` rotor so that
both coordinate runs and gaps have length at least four.  Only then is the
`15 -> 16` shared-tail CSP the correct next step.

## 7. Superseding no-go: the strict shared-tail template cannot realize `{z}`

The preceding verdict is still too optimistic.  The obstruction is not the
choice of dual chronology; it follows from rank-exactness itself.

### Theorem 7.1 (nonzero-source theorem)

Let

\[
 R_i=\bigcup_{j=0}^{d}B_{i+j}
 \qquad(0\le i<W)
\tag{7.1}
\]

where the `R_i` are consecutive distinct sets of the same cardinality and
`W>=d+2`.  Then every source letter

\[
 B_0,B_1,\ldots,B_{W+d-1}
\]

is nonempty.

#### Proof

For `0<=p<W-1`, choose

\[
 x\in R_p\setminus R_{p+1},
\]

which exists because the two sets are distinct and equicardinal.  To cover
`x` in (7.1) at index `p`, it must occur in one of
`B_p,...,B_(p+d)`.  Every one of `B_(p+1),...,B_(p+d)` also belongs to the
next window defining `R_(p+1)`, where `x` is forbidden.  Hence

\[
 x\in B_p,
\]

so `B_p` is nonempty.

It remains to cover `p=W-1,...,W+d-1`.  Put `i=p-d`; the assumption
`W>=d+2` gives `1<=i<W`.  Choose

\[
 y\in R_i\setminus R_{i-1}.
\]

The window defining `R_i` uses `B_i,...,B_(i+d)`, while every source letter
through `B_(i+d-1)` also belongs to the previous window defining
`R_(i-1)`, where `y` is forbidden.  Therefore the only possible source is

\[
 y\in B_{i+d}=B_p.
\]

Thus every source position is nonempty.  \(\square\)

### Corollary 7.2 (strict shared-tail impossibility)

Under the central-row hypotheses of Section 2, the `R_i` enumerate one
uniform layer and are therefore consecutive distinct equicardinal sets.
Assume in addition `W>=d+2` (as holds for every advertised nontrivial
rank-slack instance `k>=3`, and in particular throughout the `15 -> 16`
application).  Then
Theorem 7.1 makes every appended projection `B_d,...,B_(W+d-1)` nonempty.
Consequently every interval of the lifted word (2.2) which contains the new
coordinate `z` also contains at least one old coordinate.  The singleton
`{z}` never occurs.

Hence the marked condition (2.4) is impossible:

\[
 \boxed{\text{no nontrivial strict two-block shared-tail lift is universal}.}
\tag{7.2}
\]

This supersedes the proposed SAT target in Section 5 and the conditional
route in Section 6.  A successful odd-to-even lift must distribute the new
coordinate across at least two separated sectors (as the exact `k=14`
six-piece braid does), or leave the strict shared-tail central-row template
in another essential way.

The size hypothesis cannot simply be omitted: for example `W=2,d=1` and
`(B_0,B_1,B_2)=({a},emptyset,{b})` give distinct equicardinal windows
`R_0={a},R_1={b}`.  The genuinely tiny lift `k=1 -> 2` is likewise an
exception (`W=1,d=0`); it is excluded by the explicit `W>=d+2` condition,
not by the word “nontrivial.”
