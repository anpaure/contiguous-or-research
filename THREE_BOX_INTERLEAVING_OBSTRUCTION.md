# A multiscale anti-mixing obstruction for three-box central orders

## 1. Outcome

For an integer `s>=1`, let

\[
 H_s=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                    |x|,|y|,|z|\le s\},
 \qquad M_s=|H_s|=3s^2+3s+1.
\]

The concentric-ring obstruction only treated orders in which every complete
radius ring is contiguous.  The theorem below applies to an arbitrary order
of the middle targets.  It shows that the most obvious cure--mixing radii
uniformly--is actually much worse.

For each of the three top increments, look at its incidence word on an
ordering of `H_s`.  Its support is respectively

\[
 x=s,\qquad y=s,\qquad z=s.
\]

These three supports are pairwise disjoint and each has `s+1` points.  Let
`H` be the largest distance from an index outside their internal positive
runs to the nearest such run; the precise definition is in Section 3.

> **Anti-mixing theorem.**  Suppose a word of length `N=M_s+D` represents
> the whole box `[-s,s]^3` (after the usual translation to nonnegative chain
> coordinates).  Choose one witness for every member of `H_s`, and let `H`
> be the extreme-run mesh of their induced order.  Then
> \[
> \begin{split}
>  4s^3+\frac92s^2+\frac32s-1
>  \le{}&sM_s+2(H+1)D+3(s+1)D\\
>       &+3D^2+2D.                                      \tag{1.1}
> \end{split}
> \]
> In particular, if `D=O(s)`, then
> \[
>                         HD\ge \left(\frac12-o(1)\right)s^3. \tag{1.2}
> \]

Consequently a width-plus-perimeter construction, `D<=Cs`, forces

\[
                         H\ge \left(\frac1{2C}-o(1)\right)s^2. \tag{1.3}
\]

Thus a successful order must contain a **macroscopic run desert**: a
positive-fraction interval of its middle order is separated from every
internal run of all three positive extreme increments.  Any cross-radius
weave which spreads those extreme sides with subquadratic gaps is impossible.

This is a genuine extension beyond contiguous rings.  It excludes every
periodic sector/radius weave or low-discrepancy mixing scheme for which the
extreme-run mesh is subquadratic, and it excludes random mixing.  In fact a
uniformly random middle-layer order has `H=O(s log s)` with high probability;
(1.1) then forces

\[
                              D=\Omega(s^{3/2}),                \tag{1.4}
\]

not `O(s)`.

The argument also applies simultaneously to every near-outer concentric
subcube.  If a universal word for `[-a,a]^3` has length `M_a+O(a)`, then for
`s=a-j`, `j=o(sqrt(a))`, the induced order on `H_s` obeys

\[
 H_s\bigl(M_a-M_s+O(a)\bigr)
       \ge \left(\frac12-o(1)\right)s^3.              \tag{1.5}
\]

For fixed `j`, this requires an `Omega(a^2)` desert in the induced witness
order at every one of the outer radii `a,a-1,...`.  These induced orders use
different selected witness families; the theorem does **not** prove that the
deserts align in one common physical interval.

This is an obstruction, not a proof that the three-box conjecture is false.
Orders with aligned macroscopic deserts are not ruled out.

## 2. The unrestricted monotone band

The proof does not assume a prescribed central row.  Let a word have physical
positions `[1,N]`.  Choose one witnessing interval for each of the `M_s`
middle targets, and sort them by left endpoint:

\[
                         I_i=[\ell_i,r_i],\qquad 1\le i\le M_s.
\]

Distinct middle targets are incomparable.  Therefore no two selected
intervals contain one another.  Their left endpoints are distinct, their
right endpoints are distinct, and

\[
                  \ell_1<\cdots<\ell_{M_s},\qquad
                       r_1<\cdots<r_{M_s}.
\]

Put `D=N-M_s` and

\[
                  \alpha_i=\ell_i-i,\qquad \beta_i=r_i-i.
\]

The endpoint sequences are increasing subsets of `[N]`, hence

\[
 0\le\alpha_1\le\cdots\le\alpha_{M_s}\le D,
 \qquad
 0\le\beta_1\le\cdots\le\beta_{M_s}\le D,
 \qquad \alpha_i\le\beta_i.                           \tag{2.1}
\]

Write

\[
                              w_i=\beta_i-\alpha_i.     \tag{2.2}
\]

Thus every unrestricted near-width solution already supplies exactly the
monotone band used below.

## 3. Extreme-run mesh

Let `T_i in H_s` be the middle target represented by `I_i`.  Consider the
three valid chain increments

\[
 b_x=1_{x=s},\qquad b_y=1_{y=s},\qquad b_z=1_{z=s}       \tag{3.1}
\]

on the middle layer.  Each support has `s+1` targets and the supports are
pairwise disjoint.

For each of the three incidence words, take all maximal `1`-runs which meet
neither end of the word.  Call the resulting family `mathcal R`.  It is
nonempty.  A boundary run may contain several indices, but the two boundary
runs together can involve at most two of the three pairwise-disjoint
supports.  The remaining extreme increment therefore has an internal run.

Let `E` be the union of the index sets of the runs in `mathcal R`.  Since
the three supports are disjoint,

\[
                              |E|\le3(s+1).             \tag{3.2}
\]

For `i notin E` and an internal run `R=[u,v]`, define its one-sided span
from `i` by

\[
 d(i,R)=
 \begin{cases}
    v+1-i,&i<u,\\
    i-u+1,&i>v.
 \end{cases}                                           \tag{3.3}
\]

The two cases exhaust the possibilities because `i notin E`.  Define the
**extreme-run mesh**

\[
                    H=\max_{i\notin E}\min_{R\in\mathcal R}d(i,R). \tag{3.4}
\]

It is harmless to put `H=0` if the maximum is over an empty set.  Informally,
after deleting the `O(s)` positions which themselves belong to internal
extreme runs, every remaining index sees such a run on one side within span
`H`.

If `G` denotes the largest contiguous component of the complement of `E`
(including the two boundary components), then

\[
                              H\le G+s+1.               \tag{3.5}
\]

Indeed, from any complement position use the adjacent internal run on the
nearer available side; crossing that run adds at most `s+1` positions to the
complement gap.  Hence a quadratic lower bound on `H` really does force a
quadratic run-free component, not merely a peculiarity of the definition.

## 4. The run inequality

Fix any chain increment and let `[u,v]` be an internal `1`-run in its
incidence word on `T_1,...,T_(M_s)`.  The neighboring targets omit the bit,
so every physical position in `I_(u-1)` and `I_(v+1)` is forbidden for it.
Every positive interval between them needs a legal pin.  Since its left
endpoint lies after `ell_(u-1)` and its right endpoint lies before
`r_(v+1)`, such a pin can only occur strictly between `r_(u-1)` and
`ell_(v+1)`.  Therefore

\[
                         r_{u-1}+2\le\ell_{v+1},        \tag{4.1}
\]

or equivalently

\[
                         \beta_{u-1}-\alpha_{v+1}\le v-u. \tag{4.2}
\]

Every run in `mathcal R` has length at most `s+1`, because the entire
support of its increment has that size.  Thus `v-u<=s`.

Now take `i notin E` and choose a run realizing the inner minimum in (3.4).
If `i<u`, monotonicity and (4.2) give

\[
\begin{split}
 w_i&=\beta_i-\alpha_i
 \le\beta_{u-1}-\alpha_i\\
 &\le s+\alpha_{v+1}-\alpha_i.                       \tag{4.3}
\end{split}
\]

If `i>v`, then

\[
\begin{split}
 w_i&\le\beta_i-\alpha_{v+1}\\
 &\le s+\beta_i-\beta_{u-1}.                         \tag{4.4}
\end{split}
\]

When (4.3) is summed, a fixed increment of the nondecreasing sequence
`alpha` can be charged only by indices lying among the previous `H`
positions.  Hence all the `alpha`-difference terms sum to at most `HD`.
The `beta`-difference terms in (4.4) similarly sum to at most `(H+1)D`.
The exceptional indices in `E` contribute at most `|E|D`.  Consequently

\[
                \sum_{i=1}^{M_s}w_i
                  \le sM_s+2(H+1)D+3(s+1)D.           \tag{4.5}
\]

No geometric property of rings was used here.

## 5. Avoidance capacity

Every target strictly below the middle layer must be represented by a
physical interval which contains no complete selected `I_i`.  The number
`Q` of all such physical intervals has the exact ledger

\[
\begin{split}
 Q={}&\sum_{x=1}^{\ell_1}(r_1-x)
 +\sum_{i=2}^{M_s}\left(\Delta_iw_i+{\Delta_i\choose2}\right)\\
 &+{N-\ell_{M_s}+1\choose2},                         \tag{5.1}
\end{split}
\]

where `Delta_i=ell_i-ell_(i-1)`.  From (2.1),

\[
 \Delta_i=1+(\alpha_i-\alpha_{i-1}),\qquad
 \sum_{i=2}^{M_s}(\Delta_i-1)\le D.
\]

Since `w_i<=D`, the first boundary term is at most `D(D+1)`, the weighted
gap excess is at most `D^2`, the quadratic gap terms total at most
`(D^2+D)/2`, and the final boundary term is at most `D(D+1)/2`.  Hence

\[
                              Q\le\sum_iw_i+3D^2+2D.    \tag{5.2}
\]

The number of nonempty below-middle points is

\[
 V_s={ (2s+1)^3-M_s\over2}-1
       =4s^3+\frac92s^2+\frac32s-1.                  \tag{5.3}
\]

Distinct targets require distinct physical intervals, so `V_s<=Q`.
Combining (4.5), (5.2), and (5.3) proves (1.1).

Since

\[
 V_s-sM_s=s^3+\frac32s^2+\frac12s-1,                 \tag{5.4}
\]

equation (1.2) follows whenever `D=O(s)`.

## 6. Deterministic consequences for interleaving

The exact inequality can be rearranged as

\[
\begin{split}
 2(H+1)D\ge{}&s^3+\frac32s^2+\frac12s-1\\
              &-3(s+1)D-3D^2-2D.                    \tag{6.1}
\end{split}
\]

Thus:

1. If `D<=Cs`, then (1.3) holds.
2. If `H=o(s^2)`, no construction with `D=O(s)` exists.
3. If every interval of `h=o(s^2)` consecutive middle targets meets an
   internal maximal run of one of the three extreme increments (up to the
   `O(s)` run positions themselves), then `H=O(h+s)=o(s^2)`, so the order is
   impossible at surface error.
4. More quantitatively, if `H=O(s log s)`, the quadratic inequality (6.1)
   forces `D=Omega(s^(3/2))`.

The third item covers genuine cross-radius schedules: the radii may be split
into arbitrarily many arcs and interleaved in any order, but if the three
positive outer sides remain low-discrepancy throughout the order, the
construction fails.  To remain viable they must be concentrated into
macroscopic phases.

## 7. Random orders are maximally unhelpful

For completeness, take a uniformly random permutation of `H_s`.  The union
of the three extreme supports has `K=3(s+1)` points among
`M_s=3s^2+O(s)` positions.  A standard spacing union bound gives maximum
gap `O(s log s)` with probability tending to one: for a block of length
`h=C s log s`,

\[
 \Pr(\hbox{the block contains no extreme point})
 \le\left(1-\frac h{M_s}\right)^K
 \le\exp\left(-\frac{Kh}{M_s}\right)=s^{-C+o(1)},     \tag{7.1}
\]

and `O(M_s)` candidate block starts are absorbed by taking `C>3`.

Consecutive points of the same extreme support merely merge into a run;
such a run has length at most `s+1`.  The two possible boundary runs also
have length at most `s+1`.  Therefore the internal-run mesh is still
`H=O(s log s)` with high probability.  Equation (6.1) then implies
`D=Omega(s^(3/2))`, proving (1.4).

Thus randomization is useful neither as a proof heuristic nor as a likely
seed for the desired width-plus-perimeter construction.  The required order
must be exceptionally nonrandom.

## 8. Nested subcube obstruction

Now suppose a word of length

\[
                              N=M_a+D_a,qquad D_a=O(a), \tag{8.1}
\]

covers the full cube `[-a,a]^3`.  Fix `s=a-j` and restrict attention to the
embedded subcube `[-s,s]^3`.  Its middle targets form `H_s`, and all of its
below-middle targets are also targets of the original word.  Select their
witnesses from the same physical word.  The preceding proof applies with

\[
 D_s=N-M_s=D_a+M_a-M_s
     =D_a+3j(a+s+1).                                  \tag{8.2}
\]

If `j=o(sqrt(a))`, then `D_s^2=o(a^3)` and `sD_s=o(a^3)`.  Equation (6.1)
therefore gives

\[
                         H_sD_s\ge\left(\frac12-o(1)\right)s^3, \tag{8.3}
\]

which is (1.5).  In particular, if `D_a<=Ca` and `j` is fixed,

\[
                  H_{a-j}\ge
                  \left(\frac1{2(C+6j)}-o(1)\right)a^2. \tag{8.4}
\]

So every proposed recursive weave must create a quadratic desert separately
in each induced near-outer witness order.  Proving that these deserts align,
or that their separate requirements are incompatible, is an additional open
step.

## 9. Exact status

Proved here:

* the exact inequality (1.1) for every unrestricted central witness family;
* the product tradeoff `HD >= (1/2-o(1))s^3` at surface error;
* exclusion of all subquadratically mixed cross-radius orders;
* the random-order `Omega(s^(3/2))` slack lower bound; and
* the multiscale nested-subcube version (1.5).

Not proved here:

* that every complete-upper-shadow order must have subquadratic mesh;
* that the required macroscopic deserts for different radii are mutually
  incompatible;
* that every cross-radius interleaving is impossible; or
* that the three-chain interval-join conjecture is false.

The live construction target is now narrower.  A successful order must be
both shadow-complete and highly phase-separated in every induced near-outer
witness order.  Alignment of those separate phase requirements is not yet a
theorem.  Uniform weaving, random weaving, and every weave with certified
subquadratic extreme-run mesh are rigorously dead.
