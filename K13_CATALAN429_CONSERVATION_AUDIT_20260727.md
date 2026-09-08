# The `429 = C_7` audit for the joint `k=13` compiler

## Verdict

The `429` missing masks in

`scratch/sigma_jointcompiler_k13_d2descent_b7_r2.certificate.json`

are **not** a conservation law.  In quotient units the best cut misses

\[
1+1+7+17+7=33=C_7/13,
\]

but the five summands have different sources, and only one related signed
quantity is forced to equal `33`.

Two direct counterexamples are already in the workspace.

* `sigma_jointcompiler_k13_d2descent_b7_r3.certificate.json` has the same
  compiler target ranks `4,5,6` and the same actual D2 defect `7`, but its best
  cut misses `507 = 39*13` masks, with quotient histogram
  `rank 2:1, rank 3:5, rank 6:7, rank 8:17, rank 9:9`.
* Keeping the **same central cycle** as the 429 seed and re-solving only the
  compiler with ranks `2,3` included gives
  `sigma_jointcompiler_k13_b7_fixed_lower23.certificate.json`.  Its best cut
  misses `403 = 31*13` masks, with quotient histogram
  `rank 6:7, rank 8:17, rank 9:7`.

Thus the number of missing orbits can be both larger and smaller than `33`
inside essentially the same normal form.

## What the Catalan `33` really counts

For the translation quotient at `k=13`, the central cycle has

\[
Q=W/13=C_6=132
\]

edges and there are

\[
U=\binom{13}{8}/13=99
\]

rank-8 target orbits.  If `l_A` is the load of a rank-8 orbit, put

\[
H^+_1=\#\{A:l_A=0\},\qquad
P^+_1=\sum_A(l_A-1)^+.
\]

Then the exact identity is

\[
\boxed{P^+_1-H^+_1=Q-U=33=C_7/13.}
\]

For the B7/r2 seed the quotient load histogram is

\[
0^{17}1^{43}2^{30}3^7 4^2,
\]

so `H^+_1=17`, `P^+_1=50`, and `50-17=33`.  The number `33` is
the **net surplus of occurrences over targets**, not the number of holes.

There is an identical signed identity for the central lower-q2 rank-5 load.
Residence makes all 132 triple intersections have rank 5, hence

\[
\boxed{P^-_2-H^-_2=132-99=33.}
\]

For B7/r2 its quotient histogram is

\[
0^7 1^{55}2^{34}3^3,
\]

so `H^-_2=7`, `P^-_2=40`, and again `40-7=33`.

This is the genuine appearance of `C_7/13`: it is a signed overload-minus-hole
identity in two complementary load systems.

The exact `k=11` certificate is the decisive calibration.  There the analogous
surplus is `C_6/11=12`, while both load systems have zero holes and absorb all
12 units as duplicates.  The final word has zero missing masks.  Therefore a
Catalan surplus does not force a Catalan deficit.

## The useful coupling: central lower-q2 holes charge bad D2 cells

Let a cyclic depth-3 compiler have entries `A_i`, write `T_i` for the
compiler-oriented middle cycle, and define

\[
D_i^j=A_i\cup A_{i-1}\cup\cdots\cup A_{i-j},\qquad T_i=D_i^3.
\]

Put

\[
X_i=T_i\cap T_{i+1},\qquad Y_i=X_i\cap X_{i+1}.
\]

Exact reconstruction and depth-3 residence give

\[
|A_i|\le r-3,\quad |D_i^1|\le r-2,\quad D_i^2\subseteq X_i,
\quad |D_i^2|\le r-1.
\]

Call `i` bad when `D_i^2 != X_i`.  A bad D2 cell has rank at most `r-2`.

### Charging lemma

Assume the compiler covers every rank-`(r-2)` mask.  If `b` is the number of
bad D2 cells and `H^-_2` is the number of rank-`(r-2)` masks absent from the
central triple intersections `{Y_i}`, then

\[
\boxed{H^-_2\le b.}
\]

The same statement holds orbitwise in the translation quotient.

### Proof

`D_i^0=A_i` has rank at most `r-3`, so it cannot cover a rank-`(r-2)` target.
Also

\[
D_i^1\subseteq D_i^2\cap D_{i+1}^2.
\]

If both adjacent D2 cells are good, a rank-`(r-2)` value of `D_i^1` is
contained in `X_i \cap X_{i+1}=Y_i`, and equal ranks force equality.  If an
adjacent D2 cell is bad, it has rank at most `r-2`; hence a rank-`(r-2)` D1
value contained in it must equal that bad D2 value.  A rank-`(r-2)` D2 value
is itself a bad-D2 value.  Consequently every compiler rank-`(r-2)` value
outside `{Y_i}` is the value of some bad D2 cell.  Covering the `H^-_2`
distinct central holes therefore needs at least `H^-_2` distinct bad cells.

For B7/r2 equality holds with no waste.  The seven central lower-q2 holes are

```
61, 79, 115, 217, 659, 665, 713
```

and these are exactly the seven rank-5 bad-D2 values.  The B7/r3 seed has the
same equality with a different seven-element set.  Other seeds satisfy the
strict version, e.g. B10/r2 has 8 central holes and 9 bad D2 cells.

As a consistency audit, the set containment asserted by the proof was checked
on every one of the 18 decoded `k=13` joint-compiler certificates in `scratch/`
that targets rank 5.  It holds in all 18; the observed `(H^-_2,b)` pairs include
`(7,7)`, `(8,8)`, `(8,9)`, `(11,12)`, `(11,15)`, `(11,19)`, and `(12,25)`.

This explains why the D2 descent stopped at 7: it had reached the lower bound
imposed by the chosen central cycle.  A B6 solve must change the central
lower-q2 image; changing compiler entries alone cannot work.

## The upper-q2 `7` is independent

For rank-9 targets, let `G^+_2` be the number of quotient length-three central
windows whose union really has rank 9.  With `U_2=715/13=55`,

\[
P^+_2-H^+_2=G^+_2-U_2.
\]

For B7/r2, `G^+_2=110`, `H^+_2=7`, and `P^+_2=62`.  This has no fixed relation
to the compiler D2 defect.  The B7/r3 seed retains D2 defect 7 and central
lower-q2 defect 7, but has `H^+_2=9`.  The equality of the extracted rank-6
and rank-9 deficits in the 429 word is therefore coincidental.

Two parts of the residual are nevertheless unavoidable, not merely artifacts
of the chosen cut.  A rank-6 OR can occur only in a three-entry D2 cell:
shorter cells have rank at most 5 and every cell of length at least 4 contains
a rank-7 middle cell.  Hence the word has exactly `b` missing rank-6 orbits.
Likewise every five-entry cell is the union of two adjacent middle sets and
has rank 8.  If any longer cell has rank 8, each five-entry subcell in it has
the same union.  Therefore no longer interval can repair a missing central
upper-q1 colour.  Exactness forces both `b=0` and `H^+_1=0`.

## Exact decomposition of the 429

For the best cut at start 2, the missing-orbit count is

\[
\underbrace{1+1}_{\text{untargeted ranks 2,3}}
+\underbrace{7}_{\text{bad compiler D2 / rank 6}}
+\underbrace{17}_{\text{central upper q1 / rank 8}}
+\underbrace{7}_{\text{central upper q2 / rank 9}}
=33.
\]

The fixed-lower23 solve removes the first two terms without changing the
central cycle or the other three terms, giving `31` missing orbits.

## SAT consequences

1. **Tie the compiler D2 budget to a central lower-q2 hole budget.**  A solve
   with D2 budget `B` must impose `H^-_2 <= B`.  In particular B6 around the
   current B7 central cycle is impossible until at least one of its seven
   missing central rank-5 orbits is supplied.
2. Add one hole variable `z_R` for each central lower-q2 target orbit, with
   `z_R OR (all lower-q2 witnesses for R)`, and an at-most-`B` constraint on
   the `z_R`.  This is a cheap necessary propagator even when full
   `--lower-q2` is too expensive.
3. Add analogous selectable hole budgets for upper q1 and upper q2.  Once
   compiler ranks 2 and 3 are forced, the directly relevant objective is
   `b + H^+_1 + H^+_2`, not `b` alone.  For the fixed-lower23 B7 seed it is
   `7+17+7=31`.
4. A stronger redundant implication is available per rank-5 target: a
   compiler witness not already realized as a central `Y_i` must be charged
   to an adjacent bad-D2 variable.  Encoding this charging lemma explicitly
   should improve propagation in the next D2 descent.
