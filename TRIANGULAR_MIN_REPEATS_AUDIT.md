# Independent audit of `TRIANGULAR_MIN_REPEATS.md`

## Verdict

The main theorems are correct.

* The complete-graph edge encoding is an exact reformulation of triangular
  bounding boxes.
* The three-provider support works in the ordinary and both boundary cases
  `u=0,1`.
* The short-window count, quadratic root, ceiling, and
  `(2/3+o(1))R` asymptotic are correct.
* The peak-run and portal arguments give the displayed linear repetition
  bound with the stated rounding.
* The original audit established exact values through `R=3`.  A later,
  independently audited proof-producing SAT computation now also establishes
  `rho(4)=2`; see `TRIANGULAR_SAT_AUDIT.md`.

The new file `scratch/triangular_r6_plus5.txt` is also a valid certificate:
it contains all `22` letters, has length `27`, and covers all `91` targets.
It proves

\[
                         1\le\rho(6)\le5,
\]

not equality or minimality.

This certificate changes the status of the observed quadratic pattern.  At
`R=6`,

\[
                  \left\lfloor\frac{(R-1)^2}{4}\right\rfloor=6,
\]

while a word with five repeats exists.  Therefore that expression is not a
valid all-`R` lower bound and cannot be the exact all-`R` formula.  The
source only records its agreement with `R=3,4,5` and does not claim a
theorem, but future handoffs should explicitly record the `R=6`
counterexample to extrapolating it.

No source theorem requires correction.  One scope point deserves emphasis:
the repetition lower bounds concern spanning words over the triangular
alphabet.  They do not apply unchanged when arbitrary outside-alphabet
entries are permitted.

## 1. Complete-graph reformulation

For every ordinary triangular cell

\[
                         E_{s,y}=(s,y),\qquad0\le y<s,
\]

map the cell to the unordered edge `{y,s}` of `K_(R+1)`.  This is a
bijection between

\[
 \mathcal T_R\setminus\{P_0\}
\]

and the `binom(R+1,2)` ordinary graph edges.  The cells `P_s=E_(s,0)` for
`s>=1` become the edges `{0,s}`, while the exceptional `P_0` becomes one
extra loop at zero.  Hence

\[
                    |\mathcal T_R|=1+\binom{R+1}{2}.
\]

For an ordinary edge `e={a,b}`, `a<b`, its triangular coordinates are

\[
                         (h(e),\ell(e))=(b,a).
\]

Giving the loop both values zero preserves the same statement.  Therefore a
word interval has bounding box `[u,r] times [0,x]` if and only if

\[
 \min h=u,\qquad\max h=r,
 \qquad\min\ell=0,\qquad\max\ell=x.
\]

Equivalently all its edges lie in

\[
 \{e:u\le h(e)\le r,\ 0\le\ell(e)\le x\}
\]

and the interval attains every one of the four extrema.  This is an exact
Ferrers-rectangle formulation, not just a mnemonic.

When `u=0`, attaining the lower `h`-side requires the loop `P_0`; no ordinary
edge has high endpoint zero.  This agrees with the original cell geometry.

## 2. Three-provider support

Fix `u<r` and `1<=x<r`.

### Interior case `u>=2`

The cells

\[
                         E_{u,1},\quad P_r,\quad E_{r,x}
\]

have first coordinates `u,r,r` and second coordinates `1,0,x`.  Their
extrema are exactly `u,r,0,x`.  All three cells are legal because `1<u` and
`x<r`.

### Boundary case `u=1`

The formal cell `E_(1,1)` is illegal.  Replacing it by `P_1=(1,0)` gives
first-coordinate minimum one; `P_r` still supplies height zero and
`E_(r,x)` supplies height `x`.  The bounding box remains exact.

### Boundary case `u=0`

Using the loop/cell `P_0=(0,0)` supplies both the required first-coordinate
minimum and height minimum.  Together with `P_r,E_(r,x)`, it gives the
desired box.

No provider claim is made at `x=0`; those are the separate peak-only
targets.  Lemma 1 is exact.

## 3. Fixed-upper-row literal grid

For one fixed `r`, the word

\[
 E_{r,r-1},E_{r,r-2},\ldots,E_{r,1},P_r,
 E_{r-1,1},\ldots,E_{2,1},P_1,P_0
\]

covers all positive-height targets with upper row `r`.

For target `(u,r,x)`, start at `E_(r,x)`.  Moving right first visits only
row-`r` cells of heights at most `x`, then `P_r`, and then height-one cells
with first coordinates decreasing.

* For `u>=2`, stop at `E_(u,1)`.
* For `u=1`, stop at `P_1`.
* For `u=0`, stop at `P_0`.

Every intermediate first coordinate lies in `[u,r]`, every intermediate
height lies in `[0,x]`, and the four extrema are attained.  Thus the literal
grid assertion has no endpoint gap.  Its inefficiency is exactly the
repetition of the column-one suffix for each different `r`.

## 4. Target count and short-window inequality

For each upper row `r`, there are `r` choices of lower endpoint and `r`
choices of height.  Hence the number of targets is

\[
 T_R=\sum_{r=1}^{R}r^2
    =\frac{R(R+1)(2R+1)}6.
\]

One physical interval has one bounding box, so selected witnesses for
different targets are different physical intervals.

If every target has a shortest witness of length at most `Lambda`, then the
number of available physical intervals is

\[
 \sum_{j=1}^{\Lambda}(n-j+1)
 =\Lambda n-\frac{\Lambda(\Lambda-1)}2.
\]

The largest shortest-witness length always satisfies `Lambda<=n`, so no
truncation of this sum is missing.  Therefore

\[
 T_R\le\Lambda n-\frac{\Lambda(\Lambda-1)}2.
\]

Rearranging gives

\[
 \Lambda^2-(2n+1)\Lambda+2T_R\le0.
\]

A universal word has at least `T_R` total intervals, so the discriminant is
nonnegative.  The quadratic is nonpositive only between its roots; hence

\[
 \Lambda\ge
 \left\lceil
  \frac{2n+1-\sqrt{(2n+1)^2-8T_R}}2
 \right\rceil.
\]

The ceiling is in the correct direction.

## 5. Long-witness asymptotic

For a near-once word,

\[
 n=1+\frac{R(R+1)}2+O(R)
   =\left(\frac12+o(1)\right)R^2,
\]

while

\[
 T_R=\left(\frac13+o(1)\right)R^3.
\]

Let `A=2n+1`.  Expanding the smaller root gives

\[
 \frac{A-\sqrt{A^2-8T_R}}2
 =\frac{2T_R}{A}+O\left(\frac{T_R^2}{A^3}\right)
 =\frac{T_R}{n}+O(1).
\]

Since

\[
                         \frac{T_R}{n}
                         =\left(\frac23+o(1)\right)R,
\]

one obtains

\[
                         \Lambda\ge(2/3+o(1))R.
\]

The source's expression `T_R/n+O(T_R^2/n^3)` is valid at the required
precision; the omitted replacement of `2n+1` by `2n` contributes only
`O(1/R)`.  The second error term is `O(1)`, hence negligible relative to
`R`.

This proves only that at least one target has a long shortest witness.  It
does not identify that target or say that a positive fraction of targets
need long witnesses.

## 6. Peak runs and zero-height targets

Let `p` be the number of peak occurrences, `b` the number of maximal peak
runs, and `q_p` the number of extra peak occurrences.  A spanning word has

\[
                         p=R+1+q_p,
 \qquad q_p\le q.
\]

A peak run of length `s` has exactly `s-1` peak--peak adjacencies.  Summing
over all runs gives exactly `p-b` such adjacencies.

For every `i=0,...,R-1`, a zero-height witness for

\[
                         [i,i+1]\times\{0\}
\]

uses only `P_i,P_(i+1)`, contains both, and therefore contains a physical
transition between those two distinct labels.  Different `i` need different
physical transitions.  Hence

\[
                         p-b\ge R
\]

and

\[
                         q_p=p-(R+1)\ge b-1.
\]

This count includes peak runs at either word endpoint without any special
rounding.

## 7. Portal count and peak-run rounding

For `i=1,...,R-1`, the top-adjacent target

\[
                         [i,i+1]\times[0,i]
\]

contains a peak and the unique possible height-`i` cell inside that first-
coordinate range, namely `E_(i+1,i)`.  Its witness crosses a peak/nonpeak
portal.

Every letter of a witness has first coordinate in `{i,i+1}`.  A fixed
portal with first-coordinate pair `{a,b}` can be contained in at most two
consecutive sets `{i,i+1}`:

* if `a!=b`, it is usable for at most the unique adjacent pair `{a,b}`;
* if `a=b`, it is usable only when the common value is the lower or upper
  endpoint, giving at most two values of `i`.

Thus at least

\[
                         \left\lceil\frac{R-1}{2}\right\rceil
\]

physical portals are needed.  Each peak run has at most two portal
boundaries, so

\[
 b\ge
 \left\lceil
  \frac{\lceil(R-1)/2\rceil}{2}
 \right\rceil
 =\left\lceil\frac{R-1}{4}\right\rceil.
\]

Combining with `q>=q_p>=b-1` gives

\[
 q\ge\left\lceil\frac{R-1}{4}\right\rceil-1.
\]

Checking the four residue classes of `R` modulo four gives the exact identity

\[
 \left\lceil\frac{R-1}{4}\right\rceil-1
 =\left\lceil
   \frac{\lfloor R/2\rfloor-2}{2}
  \right\rceil.
\]

This is the same bound as the direct peak-incidence derivation in the
companion note.  It is `R/4-O(1)` and requires no canonical provider
assumption.

The proof uses the triangular alphabet and the requirement that every peak
label occur.  Outside-alphabet entries can create additional zero-height or
portal behavior and require a different excess parameter.

## 8. Exact and certified small ledger

The exact values are

\[
                         \rho(1)=0,\qquad
                         \rho(2)=0,\qquad
                         \rho(3)=1.
\]

At `R=1`, the two-peak spine is universal.  At `R=2`, the displayed
permutation

```text
(2,1) (2,0) (1,0) (0,0)
```

is spanning and universal.  At `R=3`, the independent exact-once
obstruction gives the lower bound one and the displayed length-eight word
attains it.

The current certified ledger, including the later SAT and `R=7` artifacts,
is:

\[
 \begin{array}{c|c|c|c}
 R&|\mathcal T_R|&\text{certified word length}&\text{rigorous status}\\ \hline
 4&11&13&\rho(4)=2\\
 5&16&20&1\le\rho(5)\le4\\
 6&22&27&1\le\rho(6)\le5\\
 7&29&38&1\le\rho(7)\le9.
 \end{array}
\]

The `R=6` word in `scratch/triangular_r6_plus5.txt` is

```text
(5,4) (5,3) (4,2) (5,1) (4,0) (3,1) (2,1) (1,0)
(4,3) (4,1) (3,2) (3,0) (2,1) (1,0) (0,0) (1,0)
(2,0) (3,0) (4,0) (5,0) (6,0) (6,1) (6,2) (6,3)
(5,2) (6,4) (6,5)
```

It was independently checked by exhaustive interval enumeration on the
remote Linux worker.  The decisive output was

```text
R=6 n=27 alphabet=22 excess=5 distinct=22 span=1 targets=91 missing=0
```

This is an upper-bound certificate only.  Failed searches with fewer repeats
are not lower bounds.

The earlier successful excesses at `R=3,4,5` were `1,2,4`, matching

\[
                         \left\lfloor\frac{(R-1)^2}{4}\right\rfloor.
\]

At `R=6` that expression equals six, but a five-repeat word exists.  Thus it
cannot be promoted to an all-`R` lower bound or exact formula.  The
strict-interior antichain cardinality remains correct; what fails is the
unproved charging of one distinct repeat to each antichain member.

The recorded heuristic failures establish no additional lower bounds.  The
`R=4,n=12` lower bound is instead certified by a checked DRAT refutation.
For `R=5,6,7`, the generic exact-once obstruction remains the only proved
lower bound recorded here.

## 9. Scope ledger

| Statement | Audit status | Qualification |
|---|---|---|
| `T_R minus {P_0}=E(K_(R+1))` | proved exactly | `P_0` is one extra loop. |
| Ferrers rectangle reformulation | proved exactly | Includes `u=0` via the loop. |
| Three-provider support | proved | Boundary replacements at `u=0,1` are necessary and sufficient. |
| Fixed-`r` literal grid | proved | Covers positive heights; recopying column one is the cost. |
| Short-window inequality | proved exactly | Selected witnesses are distinct intervals. |
| Quadratic smaller root | proved exactly | Ceiling and discriminant direction correct. |
| `Lambda>=(2/3+o(1))R` | proved | One long shortest witness, not a density statement. |
| Peak-run inequality `p-b>=R` | proved exactly | Spanning triangular word hypothesis. |
| Portal lower bound | proved | Capacity at most two, including boundary values. |
| Linear repetition theorem | proved | Rounding identity checked modulo four. |
| `rho(1),rho(2),rho(3),rho(4)` | exact | `0,0,1,2`; `R=4` has a checked DRAT lower certificate. |
| `R=4` certificate | exact upper witness | Together with the DRAT refutation, proves `rho(4)=2`. |
| `R=5` certificate | verified upper bound | `rho(5)<=4`; minimality unknown. |
| `R=6,+5` certificate | independently verified upper bound | `rho(6)<=5`; minimality unknown. |
| `R=7,+9` certificate | independently verified upper bound | `rho(7)<=9`; minimality unknown. |
| Quadratic excess pattern | disproved as an all-`R` formula/lower bound | `R=6` has `5<floor(25/4)=6`. |
| Linear-overhead construction | open | Lower bound proves it would be order-optimal. |

## 10. Safe handoff statement

The following summary keeps proof, certificate, and heuristic evidence
separate.

> A spanning triangular word is equivalently an ordering with repetitions of
> the edges of `K_(R+1)` plus one loop.  Its universal intervals must realize
> every Ferrers bounding rectangle.  Peak-run and portal incidence gives
> \[
> \rho(R)\ge
> \left\lceil\frac{\lfloor R/2\rfloor-2}{2}\right\rceil
> =R/4-O(1),
> \]
> together with `rho(R)>=1` for `R>=3`.  A near-once word necessarily has a
> target whose shortest witness has length at least `(2/3+o(1))R`.

> Exact values are known through `R=4`:
> `rho(1),rho(2),rho(3),rho(4)=0,0,1,2`.  Certified upper bounds give
> `rho(5)<=4`, `rho(6)<=5`, and `rho(7)<=9`; none of these three upper values
> is proved minimal.  The `R=6` certificate refutes extrapolating
> `floor((R-1)^2/4)` as a universal lower bound or exact formula.

> The remaining problem is either to construct a global `O(R)`-repeat portal
> braid with linearly long clean witnesses, or to prove a stronger
> portal-congestion lower bound.  Small heuristic nonfindings do not decide
> between those alternatives.
