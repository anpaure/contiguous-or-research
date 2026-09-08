# The depth-three complement-list colouring face is a pointed Steiner decomposition

**Date:** 2026-08-01  
**Status:** unconditional exact equivalence and an infinite parity no-go for
one proposed block-regular sufficient face.  This does **not** obstruct
nonregular punctured-containment Hall solutions or the unrestricted
depth-three co-design master.

## 0. Setup and result

Put

\[
             v=2m-1,\qquad k=m-2,
\]

and let `V` be a set of size `v`.  The block-regular construction in
`MATH_THEOREM_D3_QUOTIENT_FLAG_NORMAL_FORM_FUNCTIONAL_HALL_AND_COMPACT_CODESIGN_20260801.md`
asks for a map

\[
 c:{V\choose k}\longrightarrow V
\]

such that

\[
 c(A)\notin A                                                     \tag{0.1}
\]

and adjacent vertices of the Johnson graph receive different colours:

\[
 |A\cap B|=k-1\quad\Longrightarrow\quad c(A)\ne c(B).            \tag{0.2}
\]

For `x in V`, write

\[
                  {\cal F}_x=\{A:c(A)=x\}.
\]

### Theorem 0.1 (pointed Steiner equivalence)

A colouring satisfying (0.1)--(0.2) exists if and only if the complete
family of `k`-sets can be partitioned as

\[
                    {V\choose k}=\mathop{\dot\bigcup}_{x\in V}{\cal F}_x
                                                                    \tag{0.3}
\]

so that, for every `x`,

\[
       {\cal F}_x\subseteq {V-\{x\}\choose k}
\]

is a Steiner system

\[
                       S(k-1,k,v-1).                              \tag{0.4}
\]

Consequently, the construction is impossible whenever `m>=5` is odd.  In
particular, the first unresolved prospective case `m=5` would require an
`S(2,3,8)`, which does not exist.

## 1. Packing equality forces a Steiner system in every colour

Fix a colour `x`.  By (0.1), every block in `F_x` avoids `x`.  By (0.2),
two blocks in `F_x` cannot contain the same `(k-1)`-subset.  Counting the
incidences

\[
       (B,A),\qquad B\in{V-\{x\}\choose k-1},\quad
       A\in{\cal F}_x,\quad B\subset A,
\]

gives

\[
            k|{\cal F}_x|\le {v-1\choose k-1}.                    \tag{1.1}
\]

Sum (1.1) over all `v` colours.  Since the colour classes partition all
`k`-sets,

\[
 {v\choose k}
 =\sum_x|{\cal F}_x|
 \le {v\over k}{v-1\choose k-1}
 ={v\choose k}.                                                \tag{1.2}
\]

Every inequality in (1.1) must therefore be equality.  Hence every
`(k-1)`-subset of `V-{x}` lies in exactly one member of `F_x`, proving
(0.4).

Conversely, suppose (0.3)--(0.4) hold.  The avoidance condition gives
(0.1).  If adjacent `k`-sets had the same colour `x`, their common
`(k-1)`-subset would occur in two blocks of the Steiner system `F_x`, a
contradiction.  Thus (0.2) holds.  This proves Theorem 0.1.

## 2. The parity obstruction

Assume `m>=4`.  In an `S(k-1,k,v-1)`, fix a `(k-2)`-subset `D`.  The number of blocks
containing `D` must be

\[
 { (v-1)-(k-2) \choose 1}\big/{ {k-(k-2)\choose1} }
 = {v-k+1\over2}
 = {m+2\over2}.                                             \tag{2.1}
\]

It is an integer only if `m` is even.  Therefore no colouring
(0.1)--(0.2) exists for any odd `m>=5`.  (The exceptional calibration
`m=3` has `k=1`, so there is no `(k-2)`-subset and this divisibility test
does not apply.)

More generally, all Steiner divisibility conditions are necessary:

\[
 { {2m-2-i\choose m-3-i} \over m-2-i}\in\mathbb Z,
       \qquad0\le i\le m-3.                                 \tag{2.2}
\]

Equivalently, on putting `j=m-2-i`,

\[
                  j\mid {m+j\choose j-1},
                  \qquad1\le j\le m-2.                     \tag{2.3}
\]

This also rules out the target semirank `m=8` relevant to `k=17`: at
`j=6`,

\[
        |{\cal F}_x|={ {14\choose5}\over6}
                     ={1001\over3}\notin\mathbb Z.          \tag{2.4}
\]

Thus the complement-list/block-regular sufficient face is impossible at
`k=17`, even though `m=8` passes the first parity test.  Any successful
functional punctured-containment solution there must be nonregular or use a
different regularization.

For `m=5`, equation (2.1) is `7/2`; equivalently each colour class would
have to be a Steiner triple system on eight points.  This gives the direct
first no-go.

At the two positive calibrations already in the depth-three note:

* `m=3` reduces to a derangement of the five singleton colours;
* `m=4` makes every `F_x` a perfect matching of `V-{x}`; the midpoint
  colouring over `Z_7` supplies the required pointed decomposition.

There is a useful sufficient source of pointed decompositions.

### Lemma 2.1 (Steiner lift)

If a Steiner system `S(k,k+1,v)` exists, the required complement-list
colouring exists.

For a `k`-set `A`, let `B(A)` be its unique containing block and put

\[
                         c(A)=B(A)-A.                         \tag{2.5}
\]

This colour lies outside `A`.  If adjacent `A,A'` had the same colour `x`,
then the `k`-set `(A intersect A')+{x}` would occur in the two distinct
blocks `A+{x}` and `A'+{x}`, contradicting the Steiner property.

The Fano system `S(2,3,7)` gives the `m=4` colouring, and the Witt system
`S(4,5,11)` gives a positive `m=6` colouring.  These sporadic lifts do not
remove the divisibility failures or give an all-even-`m` theorem.

## 3. Exact scope for the OR construction

The no-go applies only to the particular complement-list colouring used to
force every aligned `z`-block of the depth-three predecessor graph to be
regular.  It does not show that:

* another, nonregular block can fail Hall;
* the functional attachment face is empty;
* the compact quotient co-design master is infeasible; or
* `nu(k)>B(k)` in any dimension.

Its proof-safe consequence is narrower: a uniform all-`m` proof cannot use
that complement-list regularization unchanged, because it fails in every
odd owner semirank `m`.  The live route remains the exact alignment-flux
cuts followed by the punctured-containment Hall cuts, or a different
regularization which does not partition the Johnson vertices by an avoided
point colour.
