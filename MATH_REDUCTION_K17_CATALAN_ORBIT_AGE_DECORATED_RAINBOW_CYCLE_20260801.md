# `k=17`: Catalan-orbit age decoration as a one-copy optimal-word reduction

Date: 2026-08-01

Status: unconditional reduction.  It converts the exact 1430-denominator
age-composition certificate into a finite one-copy problem on the
`Z_17` quotient.  The required decorated quotient cycle has not yet been
constructed, so this note does not prove `nu(17)=24313`.

## 1. Why the denominator 1430 is structural

For `k=17`, `r=9`, `d=3`,

\[
 W={17\choose9}=24310=17\cdot1430,
 \qquad 1430=\operatorname{Cat}_8.
\]

The cyclic rotation action of `Z_17` is free on every nonempty proper rank:
`17` is prime, so a subset fixed by a nonidentity rotation is either empty
or all of `[17]`.  Hence there are exactly

\[
                         {1\over17}{17\choose s}
\]

target orbits at rank `s`, and exactly 1430 owner orbits at rank 9.

The certificate in
`MATH_THEOREM_K17_EXACT_AGE_COMPOSITION_FRACTIONAL_ST_CERTIFICATE_20260801.md`
has denominator 1430.  Its rank capacities are

| rank | target orbits | certified slots |
|---:|---:|---:|
| 1 | 1 | 436 |
| 2 | 8 | 8 |
| 3 | 40 | 40 |
| 4 | 140 | 140 |
| 5 | 364 | 364 |
| 6 | 728 | 728 |
| 7 | 1144 | 1144 |
| 8 | 1430 | 1430 |

Thus its rational normalization is already the natural **one age type per
owner orbit** scale.  Only the singleton rank has slack.

## 2. Changing-owner age transition

The fixed-owner age lift has an exact Johnson analogue.

### Lemma 2.1

Let `T,T'` be rank-`r` sets with

\[
                         T'=T-\{\alpha\}+\{\beta\}.
\]

Let

\[
                         T=C_0\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_d
\]

be an age partition of type `c`, assume `C_d={alpha}`, and let `c'` satisfy

\[
                         c'_{i+1}\le c_i
                         \qquad(0\le i<d).
\]

Choose `S_i subseteq C_i` with `|S_i|=c'_(i+1)` and put

\[
 C'_{i+1}=S_i,\qquad
 C'_0=\{\beta\}\cup\bigcup_{i=0}^{d-1}(C_i-S_i).     \tag{2.1}
\]

Then `C'_0,...,C'_d` partition `T'`, have type `c'`, and appending the
nonempty source letter `C'_0` updates the literal last-occurrence ages
exactly.

### Proof

All sets in (2.1) are disjoint and lie in `T'`.  Since `|C_d|=1`,

\[
 |C'_0|
 =1+\sum_{i<d}(c_i-c'_{i+1})
 =1+(r-1)-(r-c'_0)=c'_0.
\]

The survivors move from age `i` to age `i+1`; every other retained old
coordinate and the new coordinate `beta` have age zero.  The unique oldest
coordinate `alpha` leaves the owner.  `square`

For `r=9,d=3`, every certified type has `c_3=1`, so the lemma applies to
every certified transition.

## 3. Consequences for residence and the rank-8 rainbow

At each Johnson step, delete exactly the unique age-three coordinate and
insert the new coordinate into age zero.  Therefore a coordinate cannot
leave less than four owner positions after it enters; an early refresh only
restarts its age.  The owner chronology has cyclic residence at least four.

Moreover, the deepest proper suffix is

\[
 C_0\cup C_1\cup C_2=T-C_3=T-\{\alpha\}=T\cap T'.   \tag{3.1}
\]

Thus the certified rank-8 suffix slot is literally the lower q1 colour of
the Johnson edge.  Requiring the 1430 quotient edges to have distinct
rank-8 colour orbits is simultaneously:

* exact rank-8 short-cell coverage; and
* a quotient lower-q1 rainbow.

## 4. The finite decorated quotient object

Let `QJ` be the quotient of the rank-9 Johnson graph by `Z_17`.  A
**certificate-decorated quotient cycle** consists of:

1. a cyclic ordering of all 1430 owner orbits, with a chosen voltage/shift
   on each Johnson edge;
2. one of the nine certified age types on each owner orbit, with the exact
   type multiplicities in the certificate;
3. the exact 16 directed type-transition multiplicities of the connected
   certificate;
4. a representative age partition of each owner, such that Lemma 2.1 holds
   on every selected edge and its oldest singleton is the deleted label;
5. distinct target orbits at every certified suffix rank `2,...,8`;
6. at least one age-zero singleton slot (all singleton values lie in the one
   `Z_17` singleton orbit);
7. coprime total voltage, equivalently nonzero voltage modulo 17; and
8. a chosen physical opening of the lifted cycle which is **upper-safe**:
   after discarding all cyclic owner intervals crossing that cut, the
   remaining linear owner intervals still cover every target of ranks
   `10,...,17`.

The type-transition multigraph is balanced and weakly connected on its
positive support: one unit in each direction between types `(4,3,1,1)` and
`(6,1,1,1)` joins the former isolated self-loop bank to the main component.
It therefore admits an Euler circuit on all 1430 arc occurrences.  Hence
item 3 may equivalently be imposed by fixing one cyclic type word obtained
from that Euler circuit and decorating the owner positions by it.

## 5. Optimal-word implication

### Theorem 5.1

If a certificate-decorated quotient cycle exists, then

\[
                         \nu(17)=24313.
\]

### Proof

Nonzero voltage lifts the quotient cycle to one 24310-owner Johnson cycle.
Rotate every representative age partition equivariantly.  Lemma 2.1 then
produces a periodic nonempty source-letter word `A` whose every four-letter
union is the corresponding rank-9 owner.  Cutting the period and retaining
the three wrap letters gives a linear word of length

\[
                         24310+3=24313.
\]

The residence statement above makes this factorization literal at every
cut away from the chosen periodic wrap, and the three retained wrap letters
restore the crossing windows.

At ranks `2,...,8`, the number of certified quotient slots equals the number
of target orbits.  Item 5 therefore covers every physical target exactly
once after equivariant lift.  Item 6 covers all 17 singleton targets.  The
rank-9 owners are the complete middle layer.  For source intervals of length
at least four, the derivative identity rewrites their unions as unions of
consecutive owners.  The upper-safe opening in item 8 supplies all strict
upper targets using nonwrapping owner intervals and hence literal intervals
of the linearized source word.  Therefore every nonempty subset of `[17]`
is a contiguous union.

The general deadline theorem gives the reverse inequality
`nu(17)>=B(17)=24313`.  `square`

## 6. What has and has not been reduced

This reduction removes two former mismatches:

* the fractional age denominator is not larger than the quotient owner
  supply; and
* deepest suffix coverage is exactly the lower-rainbow Johnson colour.

The live correlated object is still substantial.  The quotient cycle must
simultaneously realize prescribed type transitions, actual survivor
partitions, rank-2 through rank-7 target-orbit rainbows, nonzero voltage,
and an upper-safe physical opening carrying all higher witnesses.  Cyclic
upper-orbit coverage by itself is insufficient: a target whose only witness
crosses the chosen cut would be lost.  Rank counts alone do not prove those
rows.

Nevertheless, this is a 1430-owner-orbit finite construction problem, not a
24310-owner fractional rounding problem.  It is the natural exact quotient
lane for the first unresolved dimension.
