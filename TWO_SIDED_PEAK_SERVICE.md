# Two-sided service between consecutive long peak runs

## 1. Outcome

Let an arbitrary order of the middle hexagon `H_a` contain an ordered
family of `m=O(a)` internal constant-coordinate peak plateaux

\[
                         P_1,\ldots,P_m.
\]

Write `lambda_j` for the edge cost of `P_j` and `g_j` for the number of word
positions strictly between `P_j` and `P_(j+1)`.  Put `L=4a+2`.

Call seam `j` **short-hull** when

\[
          \lambda_j+g_j+\lambda_{j+1}+2\le L+1.       \tag{1.1}
\]

After omitting the `O(a)` shared endpoints and two boundary records, there
is a heterogeneous internal-run assignment with one-sided span at most
`L+1` and cost

\[
\begin{aligned}
Q\le{}&
 \sum_{j\in\mathcal G}
   \bigl[(\lambda_j+1)\lambda_{j+1}
          +g_j\min(\lambda_j,\lambda_{j+1})\bigr]\\
&+2a\sum_{j\notin\mathcal G}(\lambda_j+1+g_j)
 +2aB+O(a^2),                                      \tag{1.2}
\end{aligned}
\]

where `mathcal G` is the set of short-hull seams and `B` is the number of
positions in the two outside tails **together with the final run `P_m`**, so
that every physical start belongs to one indexed record or to `B`.

This is an exact ordered-service constraint that is absent from scalar gap
contraction.

## 2. Geometry of the peak intervals

Two distinct constant-coordinate peak plateaux cannot share a word edge.
If they did, the endpoints of that edge would agree in two coordinates and,
because their coordinate sum is zero, also in the third.  Plateaux of one
coordinate are distinct maximal intervals.  Hence the ordered plateau
intervals are edge-disjoint and may share at most one endpoint.

Omit every shared endpoint from the set of assignment starts.  Since
`m=O(a)`, this creates only `O(a)` unassigned starts and hence only an
`O(a^2)` term in the capped ledger.  The runs themselves are not trimmed.

## 3. A short-hull seam

Fix consecutive runs

\[
 P_j=[u_j,v_j],\qquad P_{j+1}=[u_{j+1},v_{j+1}].
\]

For simplicity first suppose they do not share an endpoint.  Then

\[
 u_{j+1}=v_j+g_j+1.
\]

For every start belonging to `P_j`, assign the next run `P_(j+1)`.  It
avoids the start and its largest forward span is

\[
 v_{j+1}+1-u_j
 =\lambda_j+g_j+\lambda_{j+1}+2\le L+1.             \tag{3.1}
\]

Every gap start may use either neighboring run.  The largest backward span
to `P_j` is `lambda_j+g_j+1`, and the largest forward span to `P_(j+1)` is
`g_j+lambda_(j+1)+1`; both are at most the right side of (3.1).  Assign the
cheaper of the two runs.  The seam cost is therefore

\[
 (\lambda_j+1)\lambda_{j+1}
 +g_j\min(\lambda_j,\lambda_{j+1}).                  \tag{3.2}
\]

If the runs share an endpoint, the displayed no-share relation for
`u_(j+1)` is replaced by `u_(j+1)=v_j`.  Omit that shared start; then `g_j=0`
and both the hull condition and the cost upper bound have additional slack.

## 4. Bad seams and congestion

For starts in records which fail (1.1), use the universal peak-mesh
assignment: a forward or backward window of `4a+2` positions supplies an
internal peak run of cost at most `2a`.  Only `O(a)` global boundary starts
need be omitted.  This gives the second line of (1.2).

Every direct or fallback run has one-sided span at most `L+1`.  A fixed
adjacent increment of either monotone endpoint-offset sequence can therefore
be charged by at most `L+1` starts.  Thus the endpoint congestions are
`O(a)` independently of the number of good and bad seams.

## 5. Limiting necessary inequality

On a good seam put

\[
 p_j={\lambda_j\over a},\qquad
 s_j={\lambda_{j+1}\over a},\qquad
 z_j={g_j\over a}.
\]

Let

\[
 \rho_a={1\over a}\sum_{j\in\mathcal G}
                 \delta_{(p_j,s_j,z_j)},
 \qquad
 b_a={1\over a^2}
 \left[B+\sum_{j\notin\mathcal G}(\lambda_j+1+g_j)\right].
\]

After passing to a weak limit, (1.2) gives

\[
 \limsup {Q\over a^3}
 \le \int\bigl[ps+z\min(p,s)\bigr]d\rho+2b.         \tag{5.1}
\]

The fan-capped lower bound says that a word with defect `D=o(a^2)` must
satisfy `Q>=(4-o(1))a^3`.  Therefore every such survivor obeys the new
necessary service-moment inequality

\[
 \boxed{\int\bigl[ps+z\min(p,s)\bigr]d\rho+2b\ge4.}  \tag{5.2}
\]

The concrete process of `GAP_SERVICE_PROFILE_SURVIVOR.md` has `b=0` and
the left side `7/2`, which recovers its closure without using any internal
ordering of the desert chunks.

## 6. Scope

Equation (5.2) does not yet prove the universal three-box theorem.  A
remaining order may put positive mass into bad long-hull seams, or may have
a good-seam service moment at least four.  It does add an exact ordered
constraint which the complete-line and scalar seam relaxations did not see.
The next analytic target is to combine (5.2) with full-line coarea and the
already proved atomic seam exclusion; alternatively one must construct a
physical profile satisfying all three simultaneously.

The normalized record masses also obey

\[
                 \int(p+z)\,d\rho+b=3,               \tag{6.1}
\]

up to `o(1)`.  Hence (5.2) is equivalently

\[
 \int\left[ps+z\min(p,s)-{4\over3}(p+z)\right]d\rho
       +{2\over3}b\ge0.                              \tag{6.2}
\]

If the selected runs are the complete list above one fixed threshold `ca`,
the bad-gap fallback can be sharpened.  A dangerous-free gap of size `g`
has cost at most

\[
 ca\,g+(2-c)a\,u_L(g),
\quad
u_L(g)=
\begin{cases}
g,&g\le L,\\
2L-g,&L<g<2L,\\
0,&g\ge2L.
\end{cases}                                         \tag{6.3}
\]

Thus the bad-record term in (1.2) may be replaced by

\[
 2a(\lambda_j+1)+ca\,g_j+(2-c)a\,u_L(g_j).          \tag{6.4}
\]

Even the service moment plus unlabelled coarea is not sufficient by itself.
The relaxed diagonal profile

\[
 \mu(ds)=2\,1_{[1,2]}(s)ds,\qquad p=s,\quad z=b=0,
\]

has service moment `14/3` and statically saturates complete parallel-line
coarea.  It is not a physical peak order: two consecutive gap-zero blocks
on the same coordinate cannot both be internal peaks.  The next missing
condition is therefore direction/order coupling—parallel coarea saturation
must force valleys, separators, or direction changes—not another scalar
moment inequality.
