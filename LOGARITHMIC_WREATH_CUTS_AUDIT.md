# Independent audit of `LOGARITHMIC_WREATH_CUTS.md`

## Verdict

The main results survive the audit.

* The boundary-edge multigraph of one first-shadow colour is indeed a simple
  matching.
* The occurrence formula for a core cut is exact.
* Every fringe and boundary case in the five-rainbow-cut theorem is covered,
  and the constant five is sharp at `m=2`.
* The pairwise double-colour ledger is correct.
* Full covering coordinates are exactly the common kernel of the hole
  family, and the point-transitive dichotomy follows.
* The gap-surplus identities, the exact maximization formula `P_q(m,t)`, its
  `q=1` specialization, and the full-covering multiplicity identity are all
  correct.
* The kernelized matching formulation is exactly equivalent to the desired
  full-cut condition.

The note also keeps the two cut notions logically separate.  A
core-rainbow cut is used only at depth one and is a strong sufficient
certificate for a full depth-one covering cut.  Every multidepth
amplification statement after Section 5 uses the weaker full-covering
meaning.

One sentence in Section 7 should be weakened.  The uniform fractional
perfect matching proves that all shadow lower quotas are feasible in the
fully symmetric fractional relaxation and that there is no total-count
barrier.  It does not, by itself, exclude every integral divisibility or
trade-lattice obstruction; hypergraph matching problems can have integral
lattice barriers despite possessing a symmetric fractional perfect
matching.  The note's later insistence on critical integral rounding is
correct and already reflects this distinction.

There is also one exact endpoint correction in Section 6.  Formula (6.8),
written as a ratio with denominator `m+2-t`, is not defined at `t=m+2`.
At that endpoint `N=m-1` and the binomial difference on its left is exactly
one.  The ratio formula is valid in its intended range `t<=m+1` (and the
later logarithmic asymptotic lies well inside that range).

The result is structural, not existential: no logarithmic-kernel exact
wreath factor is constructed.

## 1. The two cut notions

For an exact middle wreath factor on

\[
 n=2m+1,qquad W=\binom{n}{m},qquad
 B=W/n=\operatorname{Cat}_m,
\]

there are two different properties.

1. A full depth-`q` covering cut at `z` requires every `(m-q)`-set avoiding
   `z` to occur somewhere as a cyclic short interval.  Repetitions and
   fringe occurrences are allowed.
2. A depth-one core-rainbow cut at `z` requires the `mB` internal cut slots
   to enumerate the `binom(2m,m-1)=mB` coordinate-free first-shadow colours
   exactly once.

The second implies the first at depth one.  The converse is false: full
coverage can use fringe slots and arbitrary multiplicities.  Nothing in the
proof of the five-cut theorem applies to the weaker full-covering cuts.

Consequently, the bound of five obstructs only the proposal to use
logarithmically many **core-rainbow** certificates.  It does not obstruct
logarithmically many full covering coordinates, nor the extreme case of a
globally complete shadow in which every coordinate is full covering.

## 2. Boundary matching model

Fix an `(m-1)`-set `S`.  In one cyclic occurrence, write

\[
                    \cdots,a,S,b,\cdots.
\]

The two adjacent middle intervals are

\[
                         S\cup\{a\},\qquad S\cup\{b\}.
\]

If two occurrences of `S` had boundary edges sharing `a`, then the middle
set `S+a` would occur twice in the selected wreath factor.  Even the
possibility that both facets came from one middle interval cannot evade the
argument: the two endpoint-deleted `(m-1)` facets of a middle interval are
different.  Exact middle factorization therefore makes the boundary edges
pairwise vertex-disjoint.  Repeated edges are excluded as a special case.

Thus `Gamma(S)` is a simple matching on

\[
 |[n]\setminus S|=(2m+1)-(m-1)=m+2
\]

vertices, and

\[
              0\le\mu(S)\le\left\lfloor\frac{m+2}{2}\right\rfloor.
\]

No assumption about rainbowness is used here.

## 3. Exact occurrence count at one core cut

After cutting a row at `z`, write

\[
                      (z,y_0,\ldots,y_{2m-1}).
\]

The full coordinate-free length-`m-1` starts are

\[
                         0,1,\ldots,m+1.
\]

The internal core starts are `1,...,m`; start `0` and start `m+1` are the
two fringes.

An occurrence of a `z`-free colour `S` is core precisely when `z` is neither
inside `S` nor one of its two boundary symbols.  Since `Gamma(S)` is a
matching, `d_(Gamma(S))(z)` is zero or one, and therefore

\[
                         c_z(S)=\mu(S)-d_{\Gamma(S)}(z)
\]

is exact.

If `z` is core-rainbow, every `z`-free colour has core multiplicity one, so

\[
                         \mu(S)-d_{\Gamma(S)}(z)=1.
\]

It follows immediately that `mu(S)` is one or two.  It is two exactly when
the matching has one edge incident with `z`.

For several rainbow coordinates `Z`, put `R=Z minus S`.  If `R` is nonempty,
the same equation holds for every `z in R`.

* If `mu(S)=1`, every such degree is zero, so the unique boundary edge
  avoids `R`.
* If `mu(S)=2`, every such degree is one.  The two disjoint matching edges
  must collectively contain `R`, whence `|R|<=4`.

This proves every assertion of Corollary 2.2, including the stated
occurrence-level compatibility.

## 4. Audit of the five-rainbow-cut theorem

Fix one row and one marked coordinate `z`.  Its decomposition

\[
 z\mid F_+\mid u\mid v\mid F_-
\]

has sizes

\[
 1+(m-1)+1+1+(m-1)=2m+1.
\]

The two fringe colours have boundary edges

\[
                         \{z,u\},\qquad\{v,z\}.
\]

### The `F_+` inequality

The displayed `F_+` occurrence is incident with `z`.  Core rainbowness at
`z` forces `mu(F_+)=2`; by the matching lemma the second boundary edge is
disjoint from `{z,u}`.

Every marked coordinate missing from `F_+` must have degree one in the
two-edge matching.  The marked coordinates already accounted for by the
displayed edge are `z` and, if marked, `u`.  The remaining missing marked
coordinates are exactly

\[
                         Z\cap F_-
\]

and `v` when `v in Z`.  They must fit on the two endpoints of the second
edge, so

\[
                 |Z\cap F_-|+1_{v\in Z}\le2.
\]

No marked coordinate in `F_+` is missing from the colour, and no coordinate
is left unclassified.

### The `F_-` inequality

The identical argument with the current edge `{v,z}` gives

\[
                 |Z\cap F_+|+1_{u\in Z}\le2.
\]

The four summands in these inequalities partition `Z minus {z}` because
`F_+,u,v,F_-` partition the remaining coordinates.  Hence

\[
                         |Z|-1\le4,
\]

and `|Z|<=5`.

This argument works unchanged at `m=2`: each fringe is a singleton and the
four non-`z` coordinates are still partitioned as asserted.  The theorem
correctly excludes only `m=1`, where first-shadow intervals have length zero
and the occurrence model degenerates.

### Equality statements

If `|Z|=5`, both two-endpoint inequalities must be equalities for every
choice of row and marked `z`.  The next `m` cyclic positions after `z` are
`F_+ union {u}`, and the preceding `m` are `{v} union F_-`; each contains
exactly two other marked coordinates.  Since an odd cyclic order places
exactly one of each pair in the next `m` positions, the induced orientation
on `Z` is a regular five-vertex tournament.

The second boundary edge for each fringe must use precisely the two
remaining marked coordinates in its inequality.  These are necessary
equality constraints, not an existence proof for larger `m`, exactly as the
note states.

## 5. Sharp `m=2` certificate

For `m=2`, the two cyclic orders are

\[
 (0,1,2,3,4),\qquad(0,2,4,1,3).
\]

Their middle edges are respectively

\[
 \{01,12,23,34,40\}
\]

and

\[
 \{02,24,41,13,30\}.
\]

These ten edges are exactly all edges of `K_5`, so the two rows form an exact
middle wreath factor.

At a cut `z`, a core first-shadow slot is a singleton.  In the first cycle,
the two core singletons are the two non-neighbours of `z`; the second cycle
is the complementary Hamilton cycle and contributes the two first-cycle
neighbours.  Hence each of the other four coordinates appears exactly once.
All five cuts are core-rainbow, proving sharpness.

## 6. Double-colour ledgers

For a rainbow coordinate `z`, a colour in

\[
 \mathcal D_z=\{S:z\notin S,\ \mu(S)=2\}
\]

has exactly one boundary edge incident with `z`, and therefore exactly one
`z`-fringe occurrence.  Conversely every `z`-fringe colour has multiplicity
two.  The `2B` fringe occurrences are distinct as colours: two such
occurrences of one colour would give two matching edges incident with `z`.
Thus

\[
                         |\mathcal D_z|=2B.
\]

Now let `z,w` both be rainbow.  In one row:

* if `w` is one of the central positions `u,v`, both `z`-fringes avoid `w`;
* otherwise `w` belongs to exactly one fringe, so exactly one fringe avoids
  it.

The central case occurs precisely when the circular distance between `z`
and `w` is `m`, i.e. their two directed distances are `m` and `m+1`.  If it
occurs in `a_(zw)` rows, exactly

\[
                         B+a_{zw}
\]

distinct `z`-fringe colours avoid `w`.  By rainbowness at `w`, these are
exactly `D_z cap D_w`.  In each central row, exactly one current fringe edge
is `{z,w}`.  In a noncentral row, the `z`-incident and `w`-incident edges of
the common double colour are different.  This proves both parts of
Proposition 4.1.

For the horizontal identity, a cyclic row in which `z,w` have circular
distance `d<=m` has exactly `m-d` length-`m` intervals containing both.
Exact middle factorization therefore gives

\[
 \sum_{\pi}(m-\operatorname{dist}_\pi(z,w))
   =\binom{2m-1}{m-2}=rac{m-1}{2}B.
\]

The resulting average distance is `(m+1)/2`.  This identity uses only
middle exactness, not rainbowness.

## 7. Full covering cuts and point transitivity

At depth `q`, let `H_q` be the missing `(m-q)`-sets.  A coordinate `z` is a
full covering cut exactly when no missing target avoids it, equivalently
when

\[
                            z\in S\quad(S\in\mathcal H_q).
\]

Hence

\[
 C_q=\bigcap_{S\in\mathcal H_q}S
\]

when holes exist, and every coordinate covers when there is no hole.  This
is the exact full-cut/common-hole identity.

If a coordinate-transitive automorphism group preserves the factor, it
preserves `H_q` and therefore its intersection `C_q`.  Transitivity makes
`C_q` empty or all of `[n]`.  For a nonempty hole family, `C_q=[n]` would
force every coordinate into an `(m-q)`-set, impossible because `m-q<n`.
Thus a point-transitive factor is either shadow-complete at that depth or
has no full covering coordinate.

This dichotomy concerns full covering coordinates.  It places no direct
bound on the number of core-rainbow cuts.

## 8. Gap-surplus identities

Let `Z` have `t>=1` marked coordinates.  The `t` cyclic gaps of unmarked
symbols have sizes `g_1,...,g_t` with

\[
                       \sum_i g_i=N=2m+1-t.
\]

A cyclic length-`s` interval avoids `Z` precisely when it lies inside one
unmarked gap, and a gap of size `g` contains `(g-s+1)_+` such intervals.
Therefore

\[
                  A_s(\pi,Z)=\sum_i(g_i-s+1)_+.
\]

For one gap, shortening from `m` to `m-q` changes this count by

\[
 f_q(g)=
 \begin{cases}
 0,&g<m-q,\\
 g-m+q+1,&m-q\le g\le m-1,\\
 q,&g\ge m.
 \end{cases}
\]

This equals both

\[
 \min\{q,(g-m+q+1)_+\}
\]

and

\[
 q-\min\{q,(m-1-g)_+\}.
\]

Summing proves (6.2)--(6.3) and the crude upper bound `qt`.

## 9. Exact maximization of the gap surplus

Call a gap active when `g>=m-q`.  Suppose exactly `ell` gaps are active.
This is feasible only if

\[
             0\le\ell\le
             \min\left(t,\left\lfloor\frac{N}{m-q}\right\rfloor\right).
\]

Give each active gap a baseline of `m-q-1` positions.  Every subsequent
position contributes one surplus unit until that gap has received `q`
surplus positions.  Hence the total surplus is at most

\[
                         \min\{\ell q,
                              N-\ell(m-q-1)\}.
\]

Conversely, feasibility guarantees

\[
 N-\ell(m-q-1)\ge\ell,
\]

so the indicated number of surplus positions can be distributed with at
least one and at most `q` to each active gap.  If all active gaps saturate,
any remaining positions can be dumped into one saturated gap without
altering the surplus.  The inactive gaps may have size zero.  This realizes
the bound for every positive feasible `ell`.

If no active gap is feasible, then `N<m-q`; all mass can be placed in one
inactive gap and the maximum is zero.  Thus including `ell=0` in the maximum
formula is harmless, and

\[
 P_q(m,t)=
 \max_{0\le\ell\le
   \min(t,\lfloor N/(m-q)\rfloor)}
 \min\{\ell q,N-\ell(m-q-1)\}
\]

is exact.

At `q=1`, every active gap contributes exactly one, so

\[
 P_1(m,t)=min\left(t,left\lfloor
                \frac{2m+1-t}{m-1}\right\rflooright).
\]

For `m>=2`, direct evaluation gives

\[
 P_1(m,t)=
 \begin{cases}
 1,&t=1,\\
 2,&2\le t\le3,\\
 1,&4\le t\le m+2,\\
 0,&m+3\le t\le2m+1,
 \end{cases}
\]

including all endpoint cases at `m=2`.

## 10. Full-cover multiplicity identity

Assume every coordinate of `Z` is a full depth-`q` covering cut.  Every
short target disjoint from `Z` is then occupied, because it avoids every
coordinate in the nonempty set `Z`.

Exact middle factorization implies that the total number of middle
occurrences disjoint from `Z` is exactly

\[
                          \binom Nm.
\]

In one row, shortening contributes

\[
                         A_{m-q}(\pi,Z)-A_m(\pi,Z)
\]

additional coordinate-free occurrences.  Hence the total number of short
occurrences disjoint from `Z` is

\[
 \binom Nm+sum_{\pi\in\mathcal F}
       (A_{m-q}(\pi,Z)-A_m(\pi,Z)).
\]

Since all `binom(N,m-q)` possible targets are occupied, multiplicity beyond
one is exactly

\[
 E_{q,Z}=\binom Nm-\binom N{m-q}
  +\sum_{\pi\in\mathcal F}
       (A_{m-q}(\pi,Z)-A_m(\pi,Z)).
\]

Nonnegativity and the rowwise maximum `P_q(m,t)` give

\[
 \binom N{m-q}-\binom Nm\le BP_q(m,t).
\]

Every nonempty subset of `Z` also consists of full covering coordinates, so
the same inequality applies after replacing `t,N` by the corresponding
subset size and unmarked count.

For `q=1`,

\[
 \binom N{m-1}-\binom Nm
 =\binom Nm\frac{t-2}{m+2-t}
\]

for `t<=m+1`, where `N>=m` and the division used to obtain the ratio is
valid.  At the omitted endpoint `t=m+2`,

\[
 N=m-1,\qquad
 \binom N{m-1}-\binom Nm=1,
\]

whereas the displayed rational expression has denominator zero.  For
`t>=m+3`, both binomial coefficients vanish.  This is a boundary correction
to the literal scope of (6.8), not to the logarithmic argument.
For `t=o(\sqrt m)`, Stirling/product expansion gives

\[
 \frac1B\left(\binom N{m-1}-\binom Nm\right)
 =2(t-2)2^{-t}\exp(O(t^2/m)).
\]

The formula may be negative for `t=1`; in that range the nonnegativity
condition is merely vacuous.  In the logarithmic range it is positive and
`o(1)`, while `P_1=1`.  Therefore this gap count supplies no arithmetic
obstruction to logarithmically many full cuts.

## 11. Kernel size and the family that must be covered

If all coordinates of `Z` are full covering, every hole must contain all of
`Z`.  The allowed hole reservoir has size

\[
                      \binom{n-t}{m-q-t}.
\]

The family which must be covered is its complement in the entire layer and
has size

\[
 \binom n{m-q}-\binom{n-t}{m-q-t}.
\]

This is almost the whole central layer for logarithmic `t`.  The
`2^{-t}`-scale family is the reservoir in which holes may remain, not a
small target family that can be covered independently by a few dedicated
wreaths.  Section 8.1 uses the correct direction.

## 12. Fractional matching formulation

The wreath hypergraph has the middle `m`-sets as vertices and one
`n`-vertex hyperedge for every wreath.  It is symmetric and regular, so
assigning equal weight to all wreaths gives a fractional perfect matching.
The total selected edge weight is `B`, and every selected wreath contributes
`n` depth-`q` interval occurrences.  Coordinate symmetry therefore gives
every one of the

\[
                         \binom n{m-q}
\]

depth colours the same fractional load

\[
 \lambda_q=\frac{Bn}{\binom n{m-q}}
           =\frac{W}{\binom n{m-q}}
           =\frac{(m+2)^{\overline q}}{(m)_q}\ge1.
\]

For `q=o(sqrt(m))`, summing logarithms of the `q` factors gives

\[
 \log\lambda_q
 =\sum_{i=0}^{q-1}log\frac{m+2+i}{m-i}
 =\frac{q(q+1)}m+O(q^3/m^2).
\]

Thus the complete lower quotas are feasible in the symmetric fractional
relaxation.  This proves there is no fractional or aggregate-count barrier.
It does **not** prove the absence of every integral divisibility/lattice
barrier, nor does it provide a rounding theorem.  The integral problem is
critical because `lambda_1=1+2/m`.

The kernelized matching statement is exact: a selected perfect matching has
all depth-`q` holes containing `Z_q` if and only if every depth target not
containing all of `Z_q` occurs at least once.  By the full-cut kernel theorem,
this is equivalent to making every coordinate in `Z_q` a full covering cut.

If one common kernel `Z` of size `t` works at every controlled depth, the
audited multidepth amplification bound gives

\[
 \sum_{q\le H}\frac{M_q}{W}
 \le2^{-t}\sum_{q\ge1}e^{-q^2/(2m)}.
\]

Thus `t>=0.5 log_2(m)+omega(1)` is sufficient in the inherited
tail-compatible range.  This remains conditional on constructing the exact
factor.

## 13. Completion and recursion scope

Reserving `o(B)` wreaths cannot cover the full-cut target family from
scratch: those wreaths contribute only `o(B)n=o(W)` short occurrences,
whereas the family of targets which fail to contain all of a logarithmic
kernel is a `1-o(1)` fraction of the central layer.  Sparse trades can only
be an absorber after a base factor has already covered almost everything.

Likewise, consuming only `o(W)` middle vertices does not guarantee exact
completion.  For an uncovered middle set `A`, all wreaths through `A` use
two members of its odd-graph neighbourhood

\[
 \{[n]\setminus(A\cup\{x\}):x\in[n]\setminus A\},
\]

which has size `m+1`.  Removing this small neighbourhood blocks every wreath
through `A`.  Any completion theorem needs local resilience, not just a
global cardinality bound.

The proposed two-coordinate recursion remains a target, not a theorem.  A
covered child occurrence need not provide a canonical parent for a missing
child target; a kernel-respecting capacitated Hall or absorption theorem is
still absent.  The trade-lattice route likewise requires an integral
saturation theorem at near-unit first-shadow load.

## 14. Claim ledger

| Claim | Audit status | Qualification |
|---|---|---|
| Boundary occurrence graph is a simple matching | proved exactly | Uses exact middle factorization only. |
| Core occurrence formula `c_z=mu-d_z` | proved exactly | Applies to `z`-free colours. |
| Multi-rainbow matching compatibility | proved exactly | Requires `R=Z minus S` nonempty. |
| At most five core-rainbow coordinates | proved | All fringe, central-position, and `m=2` cases checked. |
| Five is sharp | proved | Two complementary Hamilton cycles of `K_5`. |
| `|D_z|=2B` and pairwise law | proved exactly | These are core-rainbow consequences. |
| Horizontal distance identity | proved exactly | Independent of rainbowness. |
| Full cuts equal common hole kernel | proved exactly | Empty-hole convention gives all coordinates. |
| Point-transitive dichotomy | proved | Concerns full covering cuts, not core cuts. |
| Gap shortening identities | proved exactly | Per gap and after summation. |
| Formula `P_q(m,t)` is exact | proved | Includes `ell=0` endpoint and all feasible active-gap counts. |
| Piecewise `P_1` formula | proved | Valid for `m>=2`, including `m=2`. |
| Binomial ratio (6.8) | needs endpoint scope | Valid for `t<=m+1`; at `t=m+2` the left side is `1` and the ratio is undefined. |
| Full-cover excess identity (6.5) | proved exactly | Requires nonempty `Z` of full covering coordinates. |
| Common-kernel family size | proved exactly | The small family is the allowed hole reservoir. |
| Symmetric fractional load `lambda_q` | proved exactly | Establishes fractional quota feasibility. |
| No possible divisibility/lattice obstruction | not established | Fractional symmetry rules out only fractional/aggregate barriers. |
| Logarithmic full kernels exist | open | No exact factor construction appears here. |
| Logarithmically many core-rainbow cuts | impossible | At depth one, universal bound is five. |
| Perfect first shadow implies every coordinate full covering | proved | It need not imply any core-rainbow cut. |

## 15. Safe handoff statement

The following can be reused without conflating the cut notions.

> In an exact middle wreath factor, the boundary pairs of every first-shadow
> colour form a matching.  This forces at most five simultaneous depth-one
> core-rainbow cuts, with equality at `m=2`.  The theorem does not bound full
> covering cuts.

> At any depth, the full covering coordinates are exactly the intersection
> of all holes.  If `t_q` coordinates are full covering, all holes contain
> their kernel and the multidepth amplification estimate applies.  A
> point-transitive factor either has complete shadow at that depth or no
> full covering coordinate.

> The exact gap-surplus law imposes the necessary inequalities (6.6), but
> these have ample slack for logarithmic kernels.  Uniform fractional wreath
> weights meet every shadow lower quota with load
> `lambda_q=(m+2)^overline(q)/(m)_q`; the unresolved step is integral,
> kernel-preserving rounding or absorption.
