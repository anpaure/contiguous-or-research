# The complete `ML(13)` closure of the two-hex `T2` relay is cyclic-support monotone, with two exact resident-lift seam defects

**Date:** 2026-08-13  
**Status:** unconditional finite theorem for the complete old and switched
`ML(13)` wreath factors.  The base cyclic upper-owner deck loses no value
at any old width.  The globally induced `Z_13` tag clock closes both
topologies, but its conservative all-height certificate has two
irreducible width-two seam defects after all unchanged-cycle origin shifts.
The internal rank-six half-clock and the complete rank-seven tag clock are
kept separate below.

## 1. Literal complete-factor reconstruction

Let `Omega=[12]`, let `z` be a thirteenth coordinate, and let

\[
 E_0\subseteq {\Omega\choose6}\times{\Omega\choose7}
\tag{1.1}
\]

be the canonical semilength-six MSW incidence factor.  Let `A` be its set
of `264` path endpoints.  For any z-free incidence factor `E` with the
same endpoints, define the full middle-levels two-factor `H(E)` by the
following three edge classes:

\[
\begin{array}{ll}
\text{z-free:}&X--Y,\qquad (X,Y)\in E,\\
\text{return:}&z+(\Omega\setminus Y)--z+(\Omega\setminus X),
                         \qquad(X,Y)\in E_0,\\
\text{vertical:}&X--(z+X),\qquad X\in A.
\end{array}                                                    \tag{1.2}
\]

The return and vertical edges are fixed; only the z-free incidences are
switched.  Notice especially that the vertical mate of `X` is `z+X`, not
`z+(Omega setminus X)`.  The crossed return endpoints agree because the
two endpoints of a canonical path are complements.

Let `E_2` be obtained from `E_0` by the two frozen `T2` hexagons.  Exact
reconstruction verifies for both `H(E_0)` and `H(E_2)`:

* `1716` vertices on each of ranks six and seven;
* degree two at every vertex;
* `1584` z-free, `1584` return, and `264` vertical edges; and
* literal coverage of every vertex of `ML(13)` once.

Suppress the rank-six shore and call the cyclic rank-seven vertices the
**upper owners**.

## 2. Exact topology

### Theorem 2.1

The old and new upper-owner component histograms are

\[
 \boxed{H(E_0):\{13^{132}\},\qquad
        H(E_2):\{13^{127},65^1\}.}                         \tag{2.1}
\]

Thus the two hexagons merge exactly five old wreaths into one cycle.  The
ten z-free endpoints met by the merged traversal, in one orientation, are

```text
111111000000, 111100110000, 000011001111, 110101110000,
001010001111, 111110010000, 000001101111, 000001011111,
111110100000, 000000111111.
```

### Proof

Traverse the degree-two graphs from `(1.2)` and count their rank-seven
vertices.  The asserted histogram and endpoint trace are the complete
component output.  `square`

## 3. Complete cyclic all-width support

For a collection `F` of upper-owner cycles, let `D_q(F)` be the support of
literal unions of `q` consecutive upper owners, with an interval making at
most one turn around its component.

### Theorem 3.1 (complete closure support domination)

For every old width,

\[
                  \boxed{D_q(H(E_0))\subseteq D_q(H(E_2))
                         \quad(1\le q\le13).}              \tag{3.1}
\]

The complete support table is

\[
\begin{array}{c|rrrrrrrrrrrrr}
q&1&2&3&4&5&6&7&8&9&10&11&12&13\\ \hline
|D_q^-|&1716&1111&617&262&78&13&1&1&1&1&1&1&1\\
|D_q^+|&1716&1112&619&268&85&27&18&13&6&4&2&1&1\\
\text{loss}&0&0&0&0&0&0&0&0&0&0&0&0&0.
\end{array}                                                   \tag{3.2}
\]

In particular the return and vertical closure create no global casualty.

If one artificially compares only the five affected old cycles with the
new merged cycle, the loss counts at widths `1,...,13` are

```text
0, 3, 7, 9, 8, 1, 0, 0, 0, 0, 0, 0, 0.
```

Every one of these `28` local losses has a literal witness on an
unaffected new 13-cycle.  Therefore the unaffected bank is load-bearing
for `(3.1)`; component-local domination is false.

### Width convention

If one base owner is the union of `d+1` source letters, then `s`
consecutive owner windows have source width `d+s`.  A window of `q`
consecutive q1 incidence colours spans `q+1` rank-six path owners and
therefore has source width `d+q+1`.  In particular the q2 turn is at
source width `d+3`.  This indexing does not alter the direct rank-seven
upper-owner statement `(3.1)`.

## 4. The ordinary half-clock cannot close the complete cycles

Every old upper-owner cycle has odd length `13`, and the merged cycle has
odd length `65`.  Hence no map to two phases can alternate on every
suppressed owner edge of either complete factor.  The bipartite half-clock
theorem from
`MATH_THEOREM_ORIENTED_T2_PHASE_CLOCK_INTERNAL_ALLH_SUPPORT_LIFT_20260813.md`
applies to z-free open path intervals only; it cannot be extended across
these complete closures without a phase reset or a different tag clock.

The obstruction is topological, not a choice of path gauge.

## 5. A common cyclic `Z_13` voltage exists

Orient the new 65-cycle and independently orient the five affected old
13-cycles.  The equations

\[
                         t(w)=t(v)+1\pmod {13}       \tag{5.1}
\]

on every directed old or new edge have exactly two orientation solutions,
related by global reversal:

```text
new forward, old reversal mask 28;
new reverse, old reversal mask 3.
```

In either solution every tag occurs five times on the 65 affected owners.
Thus the complete odd topology itself admits the cyclic tag block from
`MATH_THEOREM_P_TAG_CYCLIC_PHASE_CLOCK_DILATION_20260813.md`.

For `h>=2`, the correct doubled block is

\[
\begin{aligned}
 (&V+p_a+D_0,\ldots,V+p_a+D_h,\\
  &V+p_{a+1}+D_h,V+p_{a+1}+D_{h+1},\ldots,
             V+p_{a+1}+D_{2h}),                    \tag{5.2}
\end{aligned}
\]

where `D_(2h)=D_0`.  The second clock half advances forward from `h` to
`2h`; it is not the reverse list `D_h,...,D_0`.

## 6. Exact finite tag-current failure

Retain the conservative base signature

\[
                         (T,s,t(\text{first})).      \tag{6.1}
\]

Give every unchanged 13-cycle an arbitrary common origin shift in the old
and new states.  Before shifting those origins, the signature supports
have sizes

```text
old 5384, new 5471, loss 42, birth 129.
```

Forty losses individually have mates on one or more unchanged cycles after
a suitable origin shift.  Exactly two losses have no unchanged-cycle mate
for any of the thirteen shifts:

```text
B = 1011110011010, span 2, old start tag 2;
C = 1010111011010, span 2, old start tag 1.
```

The origin constraints for the other forty are not jointly independent.
An exact binary MILP with one of thirteen origins on each of the `127`
unchanged cycles proves that all forty cannot be covered simultaneously.
The maximum is

\[
                         \boxed{39\text{ of the }42\text{ losses}.} \tag{6.2}
\]

One optimum leaves the two zero-mate seams above and

```text
1010111011110, span 3, start tag 0,
```

whose sole candidate origin conflicts with another forced demand.  Thus
arbitrary unchanged-cycle origins leave at least three conservative
signatures, not merely the two intrinsic seams.

Their literal affected seams are

```text
B old: 1010110011010 -> 1011100011010, tags 2 -> 3
B new: 1011110001010 -> 1010110011010, tags 1 -> 2

C old: 1010011011010 -> 1010110011010, tags 1 -> 2
C new: 1010110011010 -> 1000111011010, tags 2 -> 3.
```

Thus the relay swaps the two required seam tags.  The obstruction is not
the absence of a common voltage; it is the failure of literal tag-current
support at these two rank-eight seams.

As an implementation cross-check, exact enumeration of the correctly
ordered doubled lift gives

\[
\begin{array}{c|rrrr}
h&|Deck^-|&|Deck^+|&\text{loss}&\text{birth}\\ \hline
2&100539&101737&738&1936\\
3&151212&152847&1039&2674\\
4&208439&210512&1344&3417.
\end{array}                                                   \tag{6.3}
\]

These are failures of this uniform-tag lift, not a no-go for every
possible finite collar.

The more general variable-successor tag construction cannot remove the
two intrinsic seams by recolouring.  Put

```text
a = 1010110011010,  b = 1011100011010,
c = 1011110001010,  d = 1010011011010,
e = 1000111011010.
```

Then the old and new successors of `a` are `b` and `e`.  Every literal
variable-tag block must therefore satisfy

\[
                 t(b)=t(e)=t^+(a)\ne t(a).          \tag{6.4}
\]

But the unique `B` seams are old `a->b` and new `c->a`.  Their
block-boundary auxiliary tags are `t(b)` and `t(a)`, so matching the `B`
fibre would require `t(b)=t(a)`, contradicting `(6.4)`.  The `C` seams are
old `d->a` and new `a->e`; matching them requires `t(a)=t(e)`, the same
contradiction.  This is independent of the size of the tag alphabet.

Hence pure successor-tag recolouring is exactly impossible.  Both defects
localize at the single owner `a`; a positive construction needs a literal
reset/backup collar there (or extra occurrences of the two values), not a
different colouring.

## 7. Target-rank boundary: two different clock routes

There are two distinct base-owner conventions and they must not be
conflated.

1. The internal half-clock expands the rank-six path owners `X_i`.  A q2
   value spans three such blocks.  Any crossing interval contains a full
   middle clock block, so a doubled full-clock version contributes all
   `2h` clock labels (and tags).  This exceeds the `h+1` suffix labels
   outside a core of size `m-h-7`; that route cannot realize literal
   `T_0V`.

2. The complete cyclic tag clock expands the rank-seven upper owners,
   which are the q1 colours themselves.  A rank-eight q2 target is the
   union of two consecutive upper owners.  At a base seam, the last owner
   of one block and first owner of the next contribute exactly
   `D_0` plus one tag, of size `h+1`.  Therefore the three-block rank
   obstruction does **not** apply to this route.  Its exact remaining
   obstruction is the two-seam tag mismatch in Section 6.

For example the newly created `T0` seam is

```text
1000110011110 -> 1100100011110, tags 2 -> 3,
```

and its block-boundary lift contributes `D0 union {p3}`, exactly `h+1`
auxiliary labels.  A two-seam backup or another tag-current repair could
therefore still turn the complete cyclic construction positive.

## 8. Direct no-clock chronology obstruction

On the complete switched owner factor, the exact cyclic run minima are

\[
                         \min r_+=2,\qquad \min r_0=1.          \tag{8.1}
\]

Concrete zero-run-one witnesses occur on the merged cycle at

```text
coordinate 4, owner 1010011101010;
coordinate 6, owner 1010110101010.
```

Consequently the fixed switched owner chronology cannot itself be the
owner image of a depth-`h` maximal/common-history source for `h>=2`.
Long context must change or dilate the owner chronology; merely choosing a
different antecedent does not repair `(8.1)`.

## 9. Reproducibility

The principal verifier is

```text
scratch/audit_msw_t2_complete_ml13_cyclic.py
```

with SHA-256

```text
3cc7c9aee72d716c99bc183dfd194d6232965b03f01bb1f2a4cd2047eabe0960.
```

The exact H100 transcript is

```text
scratch/audit_msw_t2_complete_ml13_cyclic_20260813.h100.out
```

with SHA-256

```text
33424ae1ba52af7c23fad39522a1b2e917203e07ad46b2587ae60a3c235aefb7.
```

The independent successor-tag/run diagnostic is

```text
scratch/audit_msw_t2_variable_tag_quotient.py
```

with SHA-256

```text
56ffe75976ac0bbc8c1cbd8b0ebdd7c3c4038bf575d752dfb53449aa23e62ea8.
```

All exhaustive computation was run on `h100`; local work was limited to
source inspection, patching, and hashes.

The exact origin-shift MILP is

```text
scratch/audit_msw_t2_tag_origin_csp.py
```

with SHA-256

```text
29fcb796ffa7c0fd10c63d03a39f9d0c0cd7886fc993f1e1c97dad6193e1847c.
```

Its H100 transcript is

```text
scratch/audit_msw_t2_tag_origin_csp_20260813.h100.out
```

with SHA-256

```text
a3d1c15447e412c29bface60cdc8f68b5822585256972c02af680dcc54b9be5e.
```

## 10. Exact conclusion

\[
 \boxed{\text{complete base cyclic support: PASS; fixed-chronology direct
 source: NO; every pure tag lift: one forced reset owner.}}      \tag{10.1}
\]

The smallest remaining local target is a literal backup for the `B,C`
tag seams, or one non-tag reset collar at `a`, which preserves the newly
created `T0` seam.  The prepared-prism
or annulus route is relevant only if its context rails alter the owner
chronology while using coordinates already inside the suffix target; an
auxiliary full-clock rail would reintroduce the internal rank obstruction.
