# Exact two-sided run-service envelopes and tropical contraction

## 1. Exact service intervals

Fix a word of `M` middle-layer targets and a permitted one-sided span
`Lambda`.  For an internal threshold run

\[
                         R=[u,v],\qquad \lambda(R)=v-u,
\]

the exact starts which may use `R` from the left and right are

\[
 \Omega_R^\to
 = [\max(1,v+1-\Lambda),u-1],                       \tag{1.1}
\]

\[
 \Omega_R^\leftarrow
 = [v+1,\min(M,u-1+\Lambda)].                       \tag{1.2}
\]

Indeed, for `i<u` the audited span is `v+1-i`; for `i>v` it is
`i-(u-1)`.  Thus (1.1)--(1.2) are equivalent to the span convention and
automatically ensure that the chosen run avoids its source.

For a contracted seam `e` containing a family `D_e` of deleted internal
runs, define its two service envelopes

\[
 \kappa_e^\varepsilon(i)
 =\min\{\lambda(R):R\in D_e, i\in\Omega_R^\varepsilon\},
 \qquad \varepsilon\in\{\to,\leftarrow\},           \tag{1.3}
\]

with value `+infinity` when the set is empty.  The pair

\[
                    K(e)=(\kappa_e^\to,\kappa_e^\leftarrow) \tag{1.4}
\]

is the exact two-sided service state.  If orientation is irrelevant, use
the combined envelope `kappa_e=min(kappa_e^to,kappa_e^leftarrow)`.

## 2. Tropical threshold contraction

Raise the plateau threshold so that retained runs
`P_1,...,P_s` disappear and old seams `e_0,...,e_s` merge into `e'`.
For a deleted run `P`, let

\[
 a_P^\varepsilon(i)=
 \begin{cases}
  \lambda(P),&i\in\Omega_P^\varepsilon,\\
  +\infty,&\text{otherwise}.
 \end{cases}                                         \tag{2.1}
\]

Then, exactly and pointwise,

\[
 \boxed{
 \kappa_{e'}^\varepsilon
 =\min(\kappa_{e_0}^\varepsilon,\ldots,
       \kappa_{e_s}^\varepsilon,
       a_{P_1}^\varepsilon,\ldots,a_{P_s}^\varepsilon).}
                                                               \tag{2.2}
\]

No correction is present: the physical word and all its internal runs are
unchanged when the marked threshold rises.  Runs merely move from the
retained list into the merged seam state.

Equivalently, define the offer multiplicity

\[
 \eta_e^\varepsilon(t,i)
 =\#\{R\in D_e:\lambda(R)\le t,
                 i\in\Omega_R^\varepsilon\}.         \tag{2.3}
\]

The measures `eta` add under contraction, while

\[
 \kappa_e^\varepsilon(i)
 =\min\{t:\eta_e^\varepsilon(t,i)>0\}.               \tag{2.4}
\]

Thus threshold contraction has two equivalent exact algebras:

* service offers add;
* minimum-cost envelopes combine by tropical addition (pointwise minimum).

The usual scalar gap length still adds, but it is only the zeroth moment of
this richer state and cannot recover (2.2).

## 3. Global service envelope

Let all internal runs in the word contribute their offers and put

\[
 q_h(i)=\min\left(h,
       \min_{R:i\in\Omega_R^\to\cup\Omega_R^\leftarrow}\lambda(R)
              \right).                                \tag{3.1}
\]

When `q_h(i)<h`, assign a minimizing run; when `q_h(i)=h`, leave the source
unassigned.  All assigned runs have one-sided span at most `Lambda`, so

\[
                      C_\alpha+C_\beta\le2\Lambda.    \tag{3.2}
\]

Combining the fan-capped avoidance theorem with the heterogeneous run-cover
lemma gives

\[
 \boxed{
 |S_h|\le\sum_{i=1}^M q_h(i)+(2\Lambda+h)D.}          \tag{3.3}
\]

Here `S_h` is the lower rank slab of height `h` and `D` is the witness-band
defect.

## 4. Layer-cake service volume

For integer `0<=t<h`, define the set of starts covered by a run of cost at
most `t`:

\[
 C_t=\bigcup_{\lambda(R)\le t}
       (\Omega_R^\to\cup\Omega_R^\leftarrow).        \tag{4.1}
\]

Discrete layer cake gives the exact identity

\[
 \sum_i q_h(i)=hM-\sum_{t=0}^{h-1}|C_t|.             \tag{4.2}
\]

Therefore (3.3) is equivalent to the service-volume obstruction

\[
 \boxed{
 \sum_{t=0}^{h-1}|C_t|
 \le hM-|S_h|+(2\Lambda+h)D.}                        \tag{4.3}
\]

For the three-box middle hexagon, take `h=3a-1` and `Lambda=4a+3`.  The
exact slab deficit is

\[
 hM-|S_h|=5a^3+{3\over2}a^2-{3\over2}a,
\]

so

\[
 \sum_{t=0}^{3a-2}|C_t|
 \le5a^3+{3\over2}a^2-{3\over2}a+(11a+5)D.          \tag{4.4}
\]

In particular, a near-width sequence with `D=o(a^2)` cannot have service
volume exceeding `(5+o(1))a^3`.

## 5. Fractional certificate form

Let `x_(R,i)>=0` satisfy

\[
 x_{R,i}=0\quad(i\notin\Omega_R^\to\cup\Omega_R^\leftarrow),
 \qquad \sum_Rx_{R,i}\le1.                           \tag{5.1}
\]

Then

\[
 \boxed{
 \sum_{R,i}x_{R,i}(h-\lambda(R))_+
 \le hM-|S_h|+(2\Lambda+h)D.}                       \tag{5.2}
\]

For each source the left side is at most its best available saving
`h-q_h(i)`, so (5.2) follows from (4.3).  Conversely, choosing one minimizing
run per source attains the layer-cake value.  Hence (5.2) is an exact
fractional formulation, not a weaker relaxation.

The `long--separator--desert` assignment in
`GAP_SERVICE_PROFILE_SURVIVOR_AUDIT.md` is one such certificate.  Its cost
`7a^3/2+O(a^2)` corresponds to service volume

\[
  (3a-1)M-Q={11\over2}a^3+O(a^2),
\]

which violates (4.4) when `D=o(a^2)`.

## 6. Exact remaining geometric theorem

This section is an exact bookkeeping reduction, not evidence that the
proposed strict service-volume lower bound is true.  The contraction
bookkeeping is now complete.  The all-profile three-box
problem has become the following geometric alternative:

* prove that every proposed survivor forces
  `sum_(t<h)|C_t|>(5+epsilon)a^3-o(a^3)` for some absolute `epsilon>0`; or
* construct a physical middle order whose nested two-sided service envelopes
  stay at or below `5a^3+o(a^3)` while satisfying all complete-line, seam,
  and pinning constraints.

The missing information is the union volume of the source intervals in
(4.1), including their overlap.  Scalar gap length, total deleted plateau
mass, and one-threshold absorption cannot determine it.
