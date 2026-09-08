# Audit of the multiscale anti-mixing obstruction

## 1. Verdict

The core theorem in `THREE_BOX_INTERLEAVING_OBSTRUCTION.md` is correct.
For an arbitrary ordering induced by selected middle-layer witnesses, the
endpoint normal form, the extreme-run pin inequality, the charging estimate,
and the exact avoidance ledger do imply

\[
\begin{split}
4s^3+\frac92s^2+\frac32s-1
 \le{}&sM_s+2(H+1)D+3(s+1)D\\
      &+3D^2+2D,
\end{split}
\]

where `D=N-M_s`.  Consequently, at surface error `D=O(s)`,

\[
                     HD\ge \left(\frac12-o(1)\right)s^3.
\]

The random-order consequence and the inequality obtained by applying the
argument separately to an embedded near-outer subcube are also valid.

There is, however, one material overstatement in the interpretation of the
nested-subcube result: the argument forces a quadratic desert in the
selected-witness order for **each** near-outer subcube, but it does not prove
that the deserts for different subcubes are aligned in the physical word.
That alignment would require an additional compatibility argument between
the independently chosen witness families.  The theorem should therefore
retain the individual multiscale inequalities but retract the words
"aligned" and any claim that hierarchical phase separation has already been
proved.

There are also minor presentational corrections:

1. Boundary runs can contain more than the endpoint itself.  What is true is
   that only the supports containing `T_1` or `T_(M_s)` can have a boundary
   run, and the two endpoints belong to at most two of the three disjoint
   extreme supports.  This still proves that at least one internal run exists.
2. `H_s` is used both for the middle hexagon and, in Section 8, for its mesh.
   Use different symbols, for example `mathcal H_s` for the set and `h_s` for
   the mesh.
3. In a proper embedded subcube its minimum is not the empty global target.
   Thus there are actually one more usable below-middle targets than (5.3)
   counts.  Discarding that one target makes the stated inequality valid, but
   this should be said explicitly.

The statement should also explicitly assume `s>=1`; at `s=0` the three
"extreme" supports coincide and the nonempty-below-middle formula is not the
one being used.  All asymptotic and construction applications already have
`s>=1`.

Subject to these wording repairs, the main anti-mixing obstruction is
certified.

## 2. Endpoint normal form

Let the selected intervals for the `M_s` distinct middle targets be

\[
                         I_i=[\ell_i,r_i].
\]

Two different selected intervals cannot have the same left endpoint: with a
common left endpoint, the one with smaller right endpoint would be contained
in the other.  The same argument applies to equal right endpoints.  More
generally, after sorting by increasing left endpoint, a weakly decreasing
pair of right endpoints would give containment.  Since interval containment
implies containment of their OR targets and distinct equal-rank box points
are incomparable, both endpoint sequences are strictly increasing.

Every increasing `M_s`-subset of `[N]`, with `N=M_s+D`, has its `i`-th entry
between `i` and `i+D`.  Hence

\[
 \ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
\]

with

\[
0\le\alpha_1\le\cdots\le\alpha_{M_s}\le D,
\quad
0\le\beta_1\le\cdots\le\beta_{M_s}\le D,
\quad
\alpha_i\le\beta_i.
\]

This part uses no fixed-row or prescribed-window assumption.  It is the
correct unrestricted monotone-band normal form for the chosen antichain
witnesses.

## 3. Extreme supports and existence of an internal run

In centered chain coordinates the increment at the positive end of the
first coordinate occurs in a middle target exactly when `x=s`; similarly for
`y` and `z`.  On

\[
 \mathcal H_s=\{(x,y,z):x+y+z=0,\ |x|,|y|,|z|\le s\},
\]

each of the three supports has `s+1` points.  They are pairwise disjoint,
because, for example, `x=y=s` would force `z=-2s`, outside the box when
`s>0`.

The source sentence saying that "only `T_1` and `T_(M_s)` can lie in
boundary runs" is literally false: a boundary run may contain several
successive targets.  The needed conclusion nevertheless follows.  A support
can have a maximal run meeting the left boundary only if it contains `T_1`,
and can have one meeting the right boundary only if it contains `T_(M_s)`.
Because the three supports are disjoint, at most two supports can be wholly
accounted for by boundary runs.  The remaining nonempty support has an
internal maximal run.  Thus `mathcal R` is nonempty.

The union `E` of internal extreme-run positions satisfies

\[
                              |E|\le3(s+1).
\]

If `G` is the largest component of `[M_s] setminus E`, then the definition of
the one-sided span gives

\[
                              H\le G+s+1.
\]

Indeed, from a complement component use an adjacent internal run; the
distance across the component contributes at most `G`, and traversing that
run contributes at most its length `s+1`.  Hence a lower bound
`H=Omega(s^2)` really does imply a component of `[M_s] setminus E` of length
`Omega(s^2)`.  This is a desert for **internal** extreme runs; it may include
one of the at most two boundary runs.

## 4. Pin/run inequality

Fix one extreme increment and an internal positive run `[u,v]` in its
incidence word.  The targets represented by `I_(u-1)` and `I_(v+1)` omit the
increment.  Therefore no array entry at a physical position belonging to
either interval may contain it.

On the other hand, a selected interval `I_t`, `u<=t<=v`, represents a target
containing the increment, so at least one occurrence (pin) of the increment
must lie in it.  Because left and right endpoints are strictly increasing,
such a pin cannot lie before `ell_u>ell_(u-1)` or after
`r_v<r_(v+1)`.  Avoiding the two neighboring zero intervals leaves only the
strict corridor

\[
                         r_{u-1}<p<\ell_{v+1}.
\]

Consequently this corridor must contain an integer position:

\[
                         r_{u-1}+2\le\ell_{v+1}.
\]

Substitution of `r_i=i+beta_i` and `ell_i=i+alpha_i` gives exactly

\[
                         \beta_{u-1}-\alpha_{v+1}\le v-u.
\]

This is a necessary condition imposed by the selected central witnesses.
Other target assignments can forbid additional positions, so it should not
be described as sufficient for global factorability.

Every selected internal extreme run has length at most the size `s+1` of its
whole support, hence `v-u<=s`.

## 5. Charging the band widths

Put `w_i=beta_i-alpha_i`.  For `i notin E`, choose a run `[u,v]` attaining
the minimum in the mesh definition.

If `i<u`, then `v+1-i<=H`, and monotonicity plus the run inequality gives

\[
 w_i\le s+\alpha_{v+1}-\alpha_i.
\]

If `i>v`, then `i-(u-1)<=H`, and similarly

\[
 w_i\le s+\beta_i-\beta_{u-1}.
\]

To verify the summation, expand a difference such as
`alpha_(v+1)-alpha_i` into adjacent increments.  A fixed adjacent increment
can be charged only by indices `i` among the preceding `H` positions.
Therefore all alpha differences sum to at most

\[
                         H(\alpha_{M_s}-\alpha_1)\le HD.
\]

The beta differences obey the same estimate (the source's `(H+1)D` is a
harmless one-unit relaxation).  Finally, each exceptional `i in E` has
`w_i<=D`.  Thus the slightly sharper bound

\[
 \sum_i w_i\le sM_s+2HD+3(s+1)D
\]

holds; in particular the displayed source bound

\[
 \sum_i w_i\le sM_s+2(H+1)D+3(s+1)D
\]

is valid.  There is no unproved geometric-density assumption in this charge.

## 6. Exact avoidance ledger and constants

For a physical interval start `x`, let `i` be the first selected interval
with `ell_i>=x`.  If such an `i` exists, `[x,y]` avoids containing every
complete `I_j` exactly when `y<r_i`; if no such `i` exists, every
`y>=x` is allowed.  Partitioning starts by the gaps between consecutive
`ell_i` proves

\[
\begin{split}
 Q={}&\sum_{x=1}^{\ell_1}(r_1-x)
 +\sum_{i=2}^{M_s}\left(\Delta_iw_i+{\Delta_i\choose2}\right)\\
 &+{N-\ell_{M_s}+1\choose2}.
\end{split}
\]

This counts nonempty physical intervals and is exact, including both
boundaries.

Writing `e_i=Delta_i-1=alpha_i-alpha_(i-1)`, one has
`sum e_i<=D` and `w_i<=D`.  The four excess contributions are bounded by

\[
\begin{array}{c|c}
\text{contribution}&\text{upper bound}\\ \hline
\text{first boundary}&D(D+1)\\
\sum e_iw_i&D^2\\
\sum {1+e_i\choose2}&D(D+1)/2\\
\text{last boundary}&D(D+1)/2.
\end{array}
\]

The convexity bound in the third row is attained by concentrating all
`sum e_i` into one gap.  Summing proves

\[
                              Q\le\sum_iw_i+3D^2+2D.
\]

Any interval representing a strictly below-middle target must avoid every
complete selected middle interval: otherwise its OR would contain a
middle-rank box point and hence have rank at least the middle rank.  Distinct
targets require distinct physical intervals.  The standalone box has

\[
 V_s=\frac{(2s+1)^3-M_s}{2}-1
    =4s^3+\frac92s^2+\frac32s-1
\]

nonzero below-middle targets.  Therefore `V_s<=Q`.  Combining the two
audited estimates proves (1.1), with every numerical constant as stated.

## 7. Asymptotic and random-order consequences

Subtracting `sM_s` from `V_s` gives

\[
 V_s-sM_s=s^3+\frac32s^2+\frac12s-1.
\]

When `D=O(s)`, all terms in (1.1) except `2HD` and the leading `s^3` are
`O(s^2)`.  Thus

\[
                         HD\ge\left(\frac12-o(1)\right)s^3.
\]

For a uniformly random middle permutation, the exact probability that a
fixed block of `h` positions avoids the `K=3(s+1)` extreme points is

\[
 \frac{{M_s-h\choose K}}{{M_s\choose K}}
 =\prod_{t=0}^{K-1}\left(1-\frac{h}{M_s-t}\right)
 \le\left(1-\frac h{M_s}\right)^K.
\]

With `h=Cs log s`, a union bound over `O(M_s)` starts succeeds for any fixed
`C>3`.  Removing the at most two boundary runs enlarges a complement gap by
at most `s+1`, so `H=O(s log s)` with high probability.  Substitution into
the exact quadratic inequality shows `D=Omega(s^(3/2))`: if
`D=o(s^(3/2))`, then `D^2`, `sD`, and `HD` are all `o(s^3)`, a
contradiction.

The source's statements about periodic, sector, or low-discrepancy weaves
should be read conditionally: they are excluded once one verifies that their
extreme-run mesh is `o(s^2)`.  No formal definition of those classes is
given in the paper, so they are not separate proved corollaries as written.

## 8. Embedded-subcube application

Embed the centered subcube `[-s,s]^3`, `s=a-j`, in `[-a,a]^3`, and select
one witness in the original word for each member of its middle hexagon.
Those targets remain an antichain, so the same endpoint proof applies with

\[
 D_s=N-M_s=D_a+M_a-M_s=D_a+3j(a+s+1).
\]

The three increments at the positive ends of the embedded coordinate
chains have supports `x=s`, `y=s`, and `z=s` on that middle hexagon, so the
same run proof also applies.  Every strictly below-middle subcube point is a
target of the large box and cannot contain a selected subcube-middle witness.

When `j>0`, the minimum of the embedded subcube is not the empty target of
the large box.  Hence the large word actually has

\[
             \frac{(2s+1)^3-M_s}{2}=V_s+1
\]

eligible below-middle subcube targets.  Discarding any one of them recovers
the source's conservative count `V_s`, so its inequality remains valid.

If `j=o(sqrt(a))`, then

\[
 D_s=o(a^{3/2}),\qquad D_s^2=o(a^3),\qquad sD_s=o(a^3).
\]

The exact rearranged inequality therefore yields, for the mesh `h_s` of
this selected witness order,

\[
                         h_sD_s\ge\left(\frac12-o(1)\right)s^3.
\]

For fixed `j` and `D_a<=Ca`, this gives

\[
 h_{a-j}\ge
 \left(\frac1{2(C+6j)}-o(1)\right)a^2.
\]

This conclusion is valid for every chosen witness family and for each fixed
`j`.  What does **not** follow is that the long complement components for
different `j` occupy the same physical region.  The order indices for two
subcubes come from different selected interval families, and the proof
contains no nesting or intersection theorem for their deserts.  Thus the
safe conclusion is:

> Every fixed near-outer subcube separately forces a quadratic internal-run
> desert in its induced middle-witness order.

The stronger claim that a successful construction must have *aligned* or
already-proved *hierarchical* phase separation remains an open next lemma.

## 9. Certified scope

The audited theorem rigorously rules out every proposed near-width scheme for
which the induced middle order has extreme-run mesh `o(s^2)`.  In particular,
it rules out a uniformly random order with high probability and any explicit
mixing family for which such a mesh estimate is proved.

It does not rule out a highly phase-separated interleaving, does not show
that complete upper shadows force a small mesh, and does not prove that the
quadratic deserts arising at different subcube scales are incompatible.
Those are exactly the remaining mathematical gaps.
