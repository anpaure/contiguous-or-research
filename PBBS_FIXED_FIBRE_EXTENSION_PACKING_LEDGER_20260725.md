# Fixed-fibre extension runs: exact packing ledger and sharp obstruction

Date: 2026-07-25

This note develops the adjacent-shadow dictionary in
`PBBS_ADJACENT_SHADOW_EQUALITY_RESIDENCE_DICTIONARY_20260725.md` into a
quantitative packing statement.  It works at one depth \(q\) on a cyclic
rank-\(k\) Johnson owner sequence with \(E\) projected transition edges.

## 1. Good fixed-target windows

For a rank-\((k-q)\) target \(S\), call the start \(i\) a good
\(S\)-window when

\[
 L_{i,q}:=\bigcap_{h=0}^{q}X_{i+h}=S.
 \tag{1.1}
\]

Call \(i\) an \(S\)-extension when both \(i\) and \(i+1\) are good
\(S\)-windows.  By the adjacent-equality dictionary, an \(S\)-extension
is exactly one exposed positive coordinate residence of length \(q\).
Its residence support consists of the \(q+1\) transition edges from the
entry edge through the exit edge.

For fixed \(S\), the owners containing \(S\) induce a partial-permutation
digraph under the projected PBBS permutation.  Good \(S\)-windows are
directed \(q\)-edge windows in this fibre whose common intersection is
exactly \(S\).  Extensions are precisely two consecutive such good
windows.

## 2. Exact structure of a connected extension run

Suppose starts

\[
 i,i+1,\ldots,i+r-1
\]

are consecutive \(S\)-extensions.  Thus the \(r+1\) starts
\(i,ldots,i+r\) are all good \(S\)-windows.

### Theorem 2.1 (sliding representation)

There are token occurrences

\[
 \gamma_0,\gamma_1,\ldots,\gamma_{r+2q-1}
\]

such that, after translating \(i\) to zero,

\[
 \boxed{
 X_t=S\cup\{\gamma_t,\gamma_{t+1},\ldots,
                    \gamma_{t+q-1}\},
 \qquad0\le t\le r+q.}
 \tag{2.1}
\]

Every displayed length-\(q\) token window has distinct labels.  Labels in
nonoverlapping windows may repeat.

The union of the residence supports of the \(r\) extensions is exactly

\[
 \boxed{r+q\text{ distinct projected transition edges}.}
 \tag{2.2}
\]

#### Proof

Write

\[
 X_{t+1}=X_t-\{\alpha_t\}+\{\beta_t\}.
\]

The first good \(S\)-window says that the \(q\) initial extra coordinates
depart once each in the first \(q\) transitions.  Order them by departure
and put

\[
 \gamma_t=\alpha_t\quad(0\le t<q).
\]

For \(t\ge0\), put \(\gamma_{q+t}=\beta_t\).  Every extension at start
\(t\le r-1\) gives

\[
 \beta_t=\alpha_{t+q}
\]

by Theorem 1.1 of the adjacent-shadow dictionary.  Induction through the
Johnson updates now gives (2.1).  Distinctness in every active token window
is exactly the fact that \(X_t\setminus S\) is a set of size \(q\).

The extension at start \(t\) uses edge interval
\([t,t+q]\).  The union over \(0\le t<r\) is
\([0,r+q-1]\), which has \(r+q\) edges. \(\square\)

Theorem 2.1 is precisely the fixed-core sliding collar.  Consequently the
whole owner segment has a literal lower-and-upper compiler of length

\[
 (r+q)+q+1=r+2q+1,
\]

only \(q\) more than its \(r+q+1\) owner positions.  Thus long extension
runs are favorable both for packing and for direct fusion.

## 3. Exact packing contribution of a run

The \(r\) residence supports in a run are the intervals

\[
 [t,t+q],\qquad0\le t<r.
\]

Their exact interval-packing number is

\[
 \boxed{\left\lceil\frac{r}{q+1}\right\rceil.}
 \tag{3.1}
\]

Indeed their starts must differ by at least \(q+1\), and the greedy
choice \(0,q+1,2(q+1),\ldots\) attains the bound.

Let \(C_q\) be the total number of extensions and \(R_q\) the total
number of maximal nonempty extension runs, summed over all targets and
all projected cycles.  Ignoring conflicts between distinct runs can only
increase a packing, so

\[
 \boxed{
 \nu_q\le
 \sum_{\mathcal R}\left\lceil\frac{r_{\mathcal R}}{q+1}\right\rceil
 \le\frac{C_q}{q+1}+R_q.}
 \tag{3.2}
\]

This is the exact place where a long-run theorem would yield a vanishing
factor.  The scalar extension count alone does not control \(R_q\).

## 4. Edge-incidence and multiplicity double counts

Each extension support contains \(q+1\) edges.  A fixed projected edge can
lie in supports whose starts are only the \(q+1\) preceding positions.
Every start has one uniquely determined shadow target.  Hence

\[
 \boxed{(q+1)C_q\le(q+1)E,
        \qquad C_q\le E.}                          \tag{4.1}
\]

Similarly, the union support of a maximal run \(\mathcal R\) has
\(r_{\mathcal R}+q\) edges by (2.2), and any edge belongs to at most
\(q+1\) such union supports.  Therefore

\[
 \boxed{C_q+qR_q
       =\sum_{\mathcal R}(r_{\mathcal R}+q)
       \le(q+1)E.}                                 \tag{4.2}
\]

Neither inequality improves the ordinary edge-capacity scale
\(E/(q+1)\).

There is also an exact target-multiplicity ledger.  Let

\[
 \mu_q(S)=\#\{i:L_{i,q}=S\}
\]

count good windows.  On a linear component, adjacent equal pairs of
value \(S\) are at most \((\mu_q(S)-1)_+\).  Opening each cyclic owner
component costs at most one extra pair.  If every rank-\((k-q)\) target
occurs, as in the canonical PBBS support theorem, then

\[
 \boxed{
 C_q\le
 \sum_S(\mu_q(S)-1)_++c_{\rm cyc}
 =\Bigl(\sum_S\mu_q(S)\Bigr)-N_q+c_{m cyc}
 \le E-N_q+c_{\rm cyc}.}                          \tag{4.3}
\]

Here \(N_q\) is the number of rank-\((k-q)\) targets and
\(c_{\rm cyc}\) is the number of projected owner cycles.  In the PBBS
application \(E=W\) physically and \(c_{\rm cyc}\le B\).

For \(q=A\sqrt r\), the ratio \(N_q/W\) tends to a nonzero constant.
Thus (4.3) permits \(C_q=\Theta(W)\), or \(\Theta(B)\) after quotienting
by the \(N=2r+1\) spatial phases.  Combining this with the interval length
\(q+1\) gives only the critical packing scale

\[
 \Theta(B/q)=\Theta(B/\sqrt r),
\]

not a little-oh improvement.

## 5. Sharp isolated-extension obstruction

The arbitrary-depth suspension construction in
`PBBS_ARBITRARY_DEPTH_SUSPENSION_OBSTRUCTION_20260725.md` shows that the
loss above is real for Johnson/odd-graph incidence data.

At depth \(q=H\), its correct shadows are the cyclic sequence

\[
 \{b_0\},\{b_0\},\{b_1\},\{b_1\},\ldots,
 \{b_{R-1}\},\{b_{R-1}\}.
 \tag{5.1}
\]

Every repeated pair gives one extension, and all maximal extension runs
have length one.  Thus

\[
 C_q=R_q=R.
\]

The residence supports start two edges apart and have length \(q+1\), so
a greedy subfamily has order \(R/q\) pairwise disjoint members.  This
matches the edge-capacity scale up to an absolute factor.  At all depths
strictly below \(q\), the shadows in this construction are pairwise
distinct and floor-correct.  It also has the standard local odd-graph
lift.

Therefore no argument using only

* exact target multiplicities,
* floor-correctness,
* rainbowness at all shallower depths,
* partial-permutation fibre structure, or
* the fact that a run consumes \(r+q\) edges

can supply the missing vanishing factor.  Such data permit a critical
family of isolated extensions.

## 6. Exact surviving coefficient-one boundary

The fixed-fibre formulation separates two possible uses of long runs.

For the residence-packing route, (3.2) shows that one still has to beat

\[
 \frac{C_q}{q+1}+R_q.
\]

Even \(R_q=o(E/q)\) is not enough by itself: the term
\(C_q/(q+1)\) can remain at the critical edge-capacity scale.  Thus the
packing proof needs either \(C_q=o(E)\) on the critical depths, or a
genuinely multidepth/global conflict showing that the per-run greedy
packings cannot coexist.

For the compiler route, Theorem 2.1 is more favorable: a whole length-
\(r\) run can be recoded at overhead \(q\), not \(r\).  Hence a bound
such as

\[
 \sum_q qR_q=o(W)
\]

would be the correct scalar seam ledger **provided** one also proves a
global owner-disjoint, multidepth collar decomposition preserving every
cross-run target.  That global decomposition is not supplied here.

The generic double counts prove neither alternative.  The required input
is again canonical PBBS chronology (or the two-dimensional carrier
constraint), not shadow multiplicity alone.
