# Independent audit of `PORTAL_LINEAR_FACTOR_COUPLING.md`

## 1. Verdict

The mathematical statements in the current source pass independent audit,
with their stated conditional scope.

In particular:

* the one-point rounding lemma is coordinatewise exact and preserves every
  old source-word interval maximum;
* `ARM_WORD_FACTOR_LIFT` preserves all source-word intervals, including
  suffix--prefix intervals across arbitrary virtual component seams;
* coverage of `L_(R-1)` is genuinely conditional on the retained-edge
  condition (4.3), and the source does not silently infer that condition
  from upper portal coverage;
* Lemma 6.1, Theorem 6.2, and the bounded-run extension (6.12)--(6.13) are
  correct, including all endpoint and off-by-one terms;
* the strict lower-ideal size in (6.10) is exact; and
* the fixed-delay peak count in (7.1) is correct.  The label `(A,B)=(0,0)`
  is unroundable but still supplies the singleton peak used in Section 7.

During audit, the source was clarified so that the rounded-run consequence
is expressly conditional on a **position-disjoint ordered selection** of
the two-position runs with the asserted gap bound.  This is necessary:
the asymptotic statements `s=O(m^2)` and `H=O(m)` do not by themselves
assert Proposition 6.3's geometric hypotheses.

The note is not an unconditional upper construction and not an
unrestricted lower bound for every array.  Its positive half assumes a
completed physical upper braid, and its negative half assumes one monotone
interval band realizing the prescribed occurrence row in that order.

## 2. Audit of the rounded connector

Write

\[
 X_0=Z-e_{h_2},\qquad W=Z-e_j,\qquad
 Y_0=Z-e_{h_1},
\]

where `j` is low, is distinct from `h_1,h_2`, and satisfies `Z_j>0`.
Then `W` is in `P_m` and has rank `R`.  The connector edge minima are

\[
 X_0\wedge W=Z-e_{h_2}-e_j,
 \qquad
 W\wedge Y_0=Z-e_j-e_{h_1}.
\]

With the incoming and outgoing orientations in Lemma 3.1, the four local
edge minima omit, at their incident vertices,

\[
\begin{array}{c|c}
\text{vertex}&\text{two half-edge labels}\\
\hline
X_0&h_1,j\\
W&h_2,h_1\\
Y_0&j,h_2
\end{array}
\]

Every pair is distinct, so the adjacent joins recover all three vertices.
No hidden equality case remains.

The noncontamination argument is also exact.  An old interval crossing the
old adjacency contains both `X_0` and `Y_0`, whose join is `Z`; the inserted
point satisfies `W<=Z`.  Old intervals stopping at `X_0` or starting at
`Y_0` simply use their corresponding shifted interval and do not contain
`W`.  Thus every old maximum has a same-maximum representative after the
insertion.

For the balanced coordinates, `delta>0` implies
`d_0=ceil(delta/2)>0`, so `W=Z-e_4` is legal.  For the swapped baseline,
`(A,B)!=(0,0)` gives a positive low coordinate.  At `(0,0)` the two high
coordinates are the only positive coordinates of `Z`, so the only
rank-`R` points dominated by `Z` are `X_0,Y_0`; the claimed degeneracy is
real.

## 3. Audit of the arm lift and lower-edge gate

For a source subpath `v_i,...,v_j`, the encoded interval specified in
`ARM_WORD_FACTOR_LIFT.md` contains every internal edge minimum and the two
minima incident with every internal source vertex.  The identity

\[
 b_{e_t}\vee b_{e_{t+1}}=v_t
\]

therefore gives the lower bound on its maximum, while every encoded letter
lies below an included source endpoint and gives the reverse bound.  The
same proof applies to a suffix, a prefix, or a singleton subpath.

Concatenating encoded component blocks preserves the literal order of
their endpoint copies.  Hence a source interval crossing virtual seams is
represented by an encoded suffix, complete intervening blocks, and an
encoded prefix.  These pieces are physically contiguous.  The preservation
claim does not require the virtual seam itself to be a graph edge.

If a retained rank-`R` adjacency is

\[
 (x+e_i,x+e_j),\qquad i\ne j,
\]

then its edge minimum is exactly `x`.  Thus (4.3) is sufficient for every
`x in L_(R-1)` to occur as an encoded letter.  Conversely, upper interval
coverage places no requirement that a retained adjacency of this form be
chosen for each lower `x`; the source correctly leaves (4.3) as an
additional gate.  An `O(m^2)` family of individually missing cut-edge
minima can be appended literally, but this repair is available only after
one has proved that the uncut failure family is of that size.

The length comparison is also correct.  A component with `h` retained
edges contributes `h+2` encoded letters; summing gives one minimum per
retained edge plus two literal endpoints per component.  Rounding and an
`O(m^2)` component/cut family therefore cost only `O(m^2)` occurrences.

## 4. Failure of naive maximal iteration

With `(h_1,h_2,j)=(1,3,2)`, the four consecutive first-factor letters are

\[
 Z-e_1-e_3,\quad Z-e_2-e_3,\quad
 Z-e_1-e_2,\quad Z-e_1-e_3.
\]

Every adjacent meet is

\[
 Z-e_1-e_2-e_3.
\]

Thus the next maximal edge-minimum factor cannot recover the two middle
letters by adjacent joins.  This proves exactly the scoped failure claimed
in Section 5, not a failure of every sparse or nonmaximal factor.

## 5. Singleton-run inequality and Lemma 6.1

The selected central intervals are

\[
 I_i=[i+\alpha_i,i+\beta_i],\qquad
 w_i=\beta_i-\alpha_i.
\]

At a singleton atom run `p`, a legal pin in `I_p` must lie strictly between
`I_(p-1)` and `I_(p+1)`.  The exact integer condition is

\[
 (p-1+\beta_{p-1})+1
 \le (p+1+\alpha_{p+1})-1,
\]

which simplifies with no lost unit to

\[
 \beta_{p-1}\le\alpha_{p+1}.
\]

Consequently

\[
 w_p\le
 (\beta_p-\beta_{p-1})+
 (\alpha_{p+1}-\alpha_p).
\]

Summing over the selected peaks costs at most `2d`.  In an intervening gap,

\[
 w_i\le
 \beta_{p_(j+1)-1}-\beta_{p_j-1};
\]

there are at most `H` indices per gap, and the displayed beta increments
are ordered and telescope to at most `d`.  Prefix and suffix together cost
at most `2Hd`.  This proves

\[
 \sum_i w_i\le 3Hd+2d.
\]

Adjacent or differently coloured peak atoms do not create a collision in
this charging: each alpha or beta increment is charged at most once in the
peak sum.

## 6. Endpoint supply and the exact ideal size

The right endpoints `r_i=i+beta_i` are strictly increasing.  At a selected
right endpoint `r_i`, any interval for a target of rank below `R` must start
strictly after `ell_i`; otherwise it contains `I_i`.  Hence only

\[
 r_i-\ell_i=w_i
\]

physical suffixes are eligible there.

There are exactly `d=N-L` unselected right endpoints.  At any one of them,
the distinct suffix joins form a strict chain of nonzero points of ranks
`1,...,R-1`, so it contains at most `R-1=2m-2` lower targets.  Selecting one
witness per lower target and grouping by its right endpoint therefore gives

\[
 |\{x:1\le |x|<R\}|
 \le \sum_iw_i+(2m-2)d.
\]

No pin or natural-core assumption enters this count.

Rank symmetry in `[0,m]^4`, together with

\[
 |L_{2m}|={2m^3+6m^2+7m+3\over3},\qquad
 |L_{2m-1}|=|L_{2m}|-(m+1),
\]

gives

\[
\begin{aligned}
|\{x:1\le |x|<2m-1\}|
&={(m+1)^4-|L_{2m}|\over2}-|L_{2m-1}|-1\\
&={m^4+2m^3-m-2\over2}.
\end{aligned}
\]

Substitution yields (1.1) exactly.

## 7. Bounded positive runs

For a maximal positive run `[u,v]` of length at most `C`, the exact run
condition is

\[
 \beta_{u-1}-\alpha_{v+1}\le v-u\le C-1.
\]

For each position in the following gap this gives

\[
 w_i\le\beta_i-\beta_{u-1}+C-1.
\]

Across the internal gaps the beta differences telescope to at most `d`;
the two boundary gaps add at most `2Hd`, and the additive run error costs
at most `(C-1)Hs`.  This is the claimed

\[
 3Hd+(C-1)Hs
\]

gap contribution.

For `p in [u,v]`, insertion of both boundaries gives

\[
 w_p\le
 (\beta_v-\beta_{u-1})+
 (\alpha_{v+1}-\alpha_u)+(C-1).
\]

There are at most `C` positions in each run.  Because the selected runs
are position-disjoint and ordered, their beta-increment intervals and
alpha-increment intervals have disjoint interiors; each family sums to at
most `d`.  Thus the run contribution is at most

\[
 2Cd+C(C-1)s.
\]

Adding both contributions proves

\[
 \sum_iw_i\le(3H+2C)d+(C-1)(H+C)s.
\]

Combining this with the endpoint supply count gives (6.13), including its
denominator `3H+2C+2m-2`.

At a rounded connector, the threshold atom of `h_1` is absent at the
incoming line neighbour, present at `X_0,W`, and absent at `Y_0`; hence it
is indeed a maximal two-position run when those neighbours exist.  A dense
rounded-braid corollary must select such runs position-disjointly and retain
bounded prefix, suffix, and intervening gaps.  The current source now says
this explicitly.  Under `C=2`, `s=O(m^2)`, and `H=O(m)`, the correction in
the numerator is `O(m^3)`, so (6.13) still forces `d=Omega(m^3)`.

## 8. Fixed-delay neighbourhood count

For one orientation, the labels with

\[
 A+B\le q-1,\qquad B\le q-2
\]

number

\[
 \sum_{B=0}^{q-2}(q-B)={q(q+1)\over2}-1.
\]

This includes `(A,B)=(0,0)`, for which `X_1,X_0,Y_0` exists and has the
claimed coordinate-1 singleton peak.  Across four orientations the total is

\[
 4\left({q(q+1)\over2}-1\right)=2q(q+1)-4.
\]

The three-position neighbourhoods are separate physical block
occurrences.  A literal delay-`D` repair which preserves their local order
must enlarge each singleton positive run from length one to at least
`D+1`, requiring at least `D` added positive occurrences per neighbourhood.
This proves (7.2) within its stated fixed-order scope.

## 9. Applicability ledger

The proved implications are:

1. a completed physical portal braid plus the local rounding hypotheses
   gives a surface-cost first factor;
2. retained lower-edge coverage (4.3), or a separately bounded literal
   repair family, gives the next lower layer;
3. a prescribed occurrence row with one monotone interval band and dense
   singleton or bounded positive runs cannot also cover the full lower ideal
   with subcubic slack; and
4. the displayed connector is not self-similar under naive maximal factor
   iteration.

The note does **not** prove:

* existence of the required completed upper braid;
* lower-edge coverage for an arbitrary portal direction assignment;
* a linear-depth lower factor;
* that an arbitrary universal word must realize every repeated portal
  occurrence in the portal order; or
* an impossibility theorem for clustered reservoirs, nonsharp shared pins,
  multiple central bands, or nonmaximal factors.

Subject to this ledger, the source is suitable for inclusion as a proved
conditional coupling result and a scoped obstruction theorem.
