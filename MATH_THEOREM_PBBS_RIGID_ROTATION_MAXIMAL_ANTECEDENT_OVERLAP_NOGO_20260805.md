# Maximal antecedents of the rigid braid and residual cycles have zero literal overlap

**Date:** 2026-08-05  
**Method:** exact `d`-row intersection shapes and oriented cyclic run/gap
words; no computation or search  
**Status:** unconditional for `m>=6` at the bare maximal-antecedent scope.
The braid and every residual component are individually depth-`d`
factorable, but their maximal cyclic antecedent words have no source letter
in common.  Hence every direct suffix-prefix join between them has overlap
zero and costs exactly `d` new letters.  This is a sharp `Omega(d)` no-go
for concatenating the **maximal** antecedents; nonmaximal antecedents and
owner-level rethreads remain open.

## 1. Maximal source letters are `d`-row intersections

Let

\[
                         T=(T_j)_j
\]

be a cyclic owner chronology in which every positive coordinate run has
length at least `d+1`.  Its maximal depth-`d` antecedent is

\[
                         A_j=\bigcap_{h=0}^{d}T_{j-h}. \tag{1.1}
\]

If `H_i=T_i cap T_(i+1)` is the q1-row word, then equivalently

\[
                         A_j=\bigcap_{h=1}^{d}H_{j-h}. \tag{1.2}
\]

Indeed, a coordinate occurrence in source letter `A_j` covers precisely the
owner positions `j-d,...,j`; maximality puts it in `A_j` whenever all those
owners contain it.  The run-floor condition guarantees that the sliding OR
of (1.1) recovers every `T_j`.

Put

\[
                         R=m-d.                   \tag{1.3}
\]

For `m>=6`, the optimal deadline satisfies `d<=m-3`, so

\[
                         R>=3.                    \tag{1.4}
\]

Every maximal source letter below has rank `R`.

## 2. The two braid letter shapes

Index the terminal braid owners by

\[
 O_h=
 \begin{cases}
  P_0(-h),&h\text{ even},\\
  P_2(-h),&h\text{ odd}.
 \end{cases}
\]

Every braid edge inserts the coordinate `-h` at transition `h`.  Therefore
the maximal source letter at `O_j` is `O_j` with the last `d` inserted
coordinates removed.  Up to rotation, the two possible shapes are

\[
                         \mathsf I_R=[0,R-1],      \tag{2.1}
\]

and

\[
                         \mathsf J_R=[0,R-2]\cup\{R\}. \tag{2.2}
\]

Thus `mathsf I_R` has one occupied cyclic run of length `R`.  Starting at
the unique long occupied run, `mathsf J_R` has the oriented cyclic word

\[
 (\text{occupied }R-1, \text{zero gap }1,
  \text{occupied }1, \text{zero gap }m+d).       \tag{2.3}
\]

The long run is unique because `R>=3`.

## 3. Residual source-letter classification

The residual q1 word is concatenated from blocks

\[
 W_x=(A_1,A_2,\ldots,A_{m-1},B_1,\ldots,B_{m-3}),
 \qquad W_xW_{x+3}\cdots .                       \tag{3.1}
\]

Since `d<=m-3`, a `d`-row window crosses at most one of the boundaries
`A|B` or `B|A`.  There are four cases.

### 3.1 `A`-only windows

For an `A` window beginning at shape `A_j`, the intersection is one interval
of length `R-1` plus the common `A` singleton.  The two zero gaps separating
those occupied runs have lengths

\[
                         j+d,qquad m+1-j.         \tag{3.2}
\]

Here `1<=j<=R`, so both gaps are at least `d+1` and in particular neither is
one.

### 3.2 `B`-only windows

For a `B` window beginning at `B_j`, the intersection is a cyclic interval
of length `R+1` with one interior coordinate removed.  Its occupied run
lengths are

\[
                         j,qquad R-j,             \tag{3.3}
\]

and its zero gaps are `1` and `m+d`.  The available terminal block ends at
`B_(m-3)`, so

\[
                         1\le j\le R-2.           \tag{3.4}
\]

The only way (3.3) can have run lengths `1,R-1` is `j=1`.  In that case,
starting at the unique long run, the oriented word is

\[
 (\text{occupied }R-1, \text{zero gap }m+d,
  \text{occupied }1, \text{zero gap }1),         \tag{3.5}
\]

which is the reverse gap order from (2.3).  Rotation cannot change that
oriented order.

The alternative `j=R-1`, which would give (2.3), is exactly the missing
terminal `B_(m-2)` row and is excluded by (3.4).

### 3.3 Windows crossing `A|B`

Suppose the window has `a>=1` final `A` rows and `b>=1` initial `B` rows,
where `a+b=d`.  Its intersection has occupied run lengths `R-1,1`.  The
zero gap from the singleton to the long run has length `a+1>=2`; hence its
oriented gap word is not (2.3).

### 3.4 Windows crossing `B|A`

Suppose the window has `a>=1` final `B` rows and `b>=1` initial `A` rows of
the next block, with `a+b=d`.  Again the occupied run lengths are `R-1,1`,
but the corresponding separating gap has length `b+1>=2`.  This also is not
(2.3).

These four cases exhaust the residual maximal antecedent.

## 4. Exact overlap obstruction

### Theorem 4.1 (no common source letter)

No maximal source letter on the braid equals a maximal source letter on any
residual component.

#### Proof

Every residual letter has at least two occupied runs, so none equals the
one-run braid shape `mathsf I_R`.

To equal `mathsf J_R`, a residual letter must have occupied run lengths
`R-1,1` and the oriented gaps `(1,m+d)` after the long run.  The `A`-only
case has neither gap equal to one.  The crossing cases have the relevant
gap at least two.  In the `B`-only case, the sole candidate is `j=1`, whose
oriented gaps are `(m+d,1)` by (3.5), the reverse order.  Since the long run
is unique, no cyclic rotation can exchange these two orders.  Thus no
residual letter is a rotation, and hence no literal translate, of either
braid shape.  `square`

### Corollary 4.2 (exact maximal-antecedent join cost)

Let `U` be any cyclic cut of the maximal braid antecedent and `V` any cyclic
cut of any maximal residual antecedent.  Their longest suffix-prefix overlap
has length

\[
                         \boxed{0}.               \tag{4.1}
\]

Consequently their order-`d` de Bruijn reset distance is

\[
                         \boxed{\delta_d(U,V)=d}.  \tag{4.2}

The same holds in the reverse join direction.

#### Proof

A positive overlap contains, in particular, one equal source letter,
contradicting Theorem 4.1.  The exact reset formula is
`delta_d=d-overlap`.  Reversing the join does not create a common letter.
`square`

## 5. Consequence for a component tour

The terminal factor has one braid and at least one residual component.  Any
linear ordering of all its maximal antecedent components contains a
braid--residual boundary, even if the braid is placed at an endpoint.
Therefore direct concatenation of the maximal component antecedents incurs
at least

\[
                         d=\Theta(\sqrt k)         \tag{5.1}
\]

new source letters.  It cannot prove `B(k)+O(1)`.

This is a bare chronology obstruction and is stronger after guards are
added: owner, palette, residence, upper-witness or common-cap restrictions
can only remove allowable joins, not create a literal suffix-prefix equality
which is absent already.

## 6. Exact scope and possible escapes

The no-go applies to:

1. the **maximal** cyclic antecedent on each fixed terminal component;
2. direct component concatenation measured by literal suffix-prefix overlap;
3. arbitrary cyclic cuts and either join orientation.

It does not rule out:

1. coordinated nonmaximal antecedents whose source letters are strict
   subsets of (1.1);
2. a zero-position owner-level rethread which changes the terminal
   components before factorization;
3. a compound source packet spanning the component boundary; or
4. paying `d` temporarily and recovering the charge through a separate
   global length identity.

Thus the next additive-constant target is no longer residence or target
support.  It is a **nonmaximal common boundary state** or a final owner-level
component fusion preserving the proved support bank.

## 7. Dependencies

Componentwise biresidence and existence of the maximal antecedents are in

* `MATH_THEOREM_PBBS_RIGID_ROTATION_BRAID_EXACT_BIRESIDENCE_20260805.md`,
* `MATH_THEOREM_PBBS_RIGID_ROTATION_RESIDUAL_EXACT_RESIDENCE_20260805.md`.

The residual block word is in

`MATH_THEOREM_PBBS_RIGID_ROTATION_TWO_SOLITON_BLOCK_TRANSPORT_AND_ONE_ORBIT_LEAVE_20260805.md`.

The exact reset metric is in

`MATH_THEOREM_A_UNSATURATED_HINGE_SKELETON_DAMAGE_AND_TWO_SWITCH_EXPANSION_20260802.md`.
