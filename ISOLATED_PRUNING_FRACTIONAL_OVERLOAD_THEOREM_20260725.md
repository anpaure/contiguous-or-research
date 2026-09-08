# Isolated pruning gives a coefficient-safe fractional overload point

Date: 2026-07-25

Method: pure mathematics only.

## 0. Result

The weighted-cut obstruction for an arbitrary large-degree pruned
catalogue is real, but the **random isolated pruning itself** contains more
information than lower fibre degrees.  Its aggregate two-sided degree
deviations produce a tag-saturating fractional point with total target
overload (o(W)).

Applied to the protected-strip three-antichain conflict, this proves:

> There is a width-two-pruned return-free geodesic catalogue on all but
> (o(W/g)) chunk tags, together with one probability distribution on the
> paths above every retained tag, whose total capacity-one overload over
> all owners and all protected signed targets is (o(W)).

This closes the fractional weighted-cut gate.  It does not round the point
to an integral selection of one path per tag.

## 1. Abstract calibrated catalogue

Let there be (T) tags.  Every tag has exactly (A) candidate paths, and
every path claims exactly (K) targets from a universe (V).  For
(v\in V), let (d_v) be its catalogue degree.  Assume the calibration

\[
 \boxed{d_v\le A\qquad(v\in V).}
 \tag{1.1}
\]

Let (B) be any graph on the candidate paths, with maximum degree
(Delta).  Fix (L\to\infty) and put

\[
 p={1\over L(\Delta+1)},
 \qquad
 \mu=pA.
 \tag{1.2}
\]

Mark every path independently with probability (p), and retain a marked
path if none of its (B)-neighbours is marked.  Denote the retained family
by ({\cal I}), and its fibre above tag (U) by ({\cal I}_U).

### Theorem 1.1 (aggregate fractional-overload bound)

There is an outcome of the isolated pruning and a retained tag family
({\cal T}'\) such that

\[
 \boxed{
 T-|{\cal T}'|
 \le 2T\left(e^{-\mu/32}+{4\over L}\right)
 }
 \tag{1.3}
\]

and such that the uniform weights

\[
 x_P={1\over|{\cal I}_U|}
 \qquad(P\in{\cal I}_U, U\in{\cal T}')
 \tag{1.4}
\]

satisfy

\[
 \boxed{
 \sum_{v\in V}(\ell(v)-1)_+
 \le
 2\left(
 {|V|\over\sqrt\mu}
 +KT\left({1\over\sqrt\mu}+{1\over L}\right)
 \right),}
 \tag{1.5}
\]

where

\[
 \ell(v)=\sum_{P\ni v}x_P.
\]

#### Proof

For a tag (U), let (Y_U) be its number of marked candidates and let
(Z_U) be the number of those candidates deleted because they have a
marked bad neighbour.  Put

\[
 A'_U=|{\cal I}_U|=Y_U-Z_U.
\]

Then

\[
 Y_U\sim {\rm Bin}(A,p),
 \qquad \mathbb EY_U=\mu,
\]

and a union bound over bad neighbours gives

\[
 \mathbb EZ_U\le Ap^2\Delta\le{\mu\over L}.
 \tag{1.6}
\]

Call (U) good when (A'_U\ge\mu/2).  If (U) is not good, then either
(Y_U<3\mu/4) or (Z_U>\mu/4).  Chernoff and Markov therefore give

\[
 \Pr(U\hbox{ bad})
 \le e^{-\mu/32}+{4\over L}.
 \tag{1.7}
\]

Also

\[
 \mathbb E|A'_U-\mu|
 \le\mathbb E|Y_U-\mu|+\mathbb EZ_U
 \le\sqrt\mu+{\mu\over L}.
 \tag{1.8}
\]

Take ({\cal T}') to be the good tags.  For a target (v), let (Y_v)
be the number of all marked candidates which claim (v), and let
(n_{Uv}) be the number of retained candidates above a good tag (U)
which claim (v).  Put (n_v=\sum_U n_{Uv}).  Since deletion and removal
of bad tags can only decrease this count,

\[
 n_v\le Y_v,
 \qquad
 Y_v\sim{\rm Bin}(d_v,p).
 \tag{1.9}
\]

For the uniform weights (1.4),

\[
\begin{aligned}
 \ell(v)
 &=\sum_{U\in{\cal T}'}{n_{Uv}\over A'_U}\\
 &\le {n_v\over\mu}
 +\sum_{U\in{\cal T}'}n_{Uv}
       \left|{1\over A'_U}-{1\over\mu}\right|.
\end{aligned}
 \tag{1.10}
\]

By calibration,

\[
 {pd_v\over\mu}={d_v\over A}\le1.
\]

Consequently

\[
 (\ell(v)-1)_+
 \le{(Y_v-pd_v)_+\over\mu}
 +\sum_U n_{Uv}
       \left|{1\over A'_U}-{1\over\mu}\right|.
 \tag{1.11}
\]

The binomial variance bound gives

\[
 \mathbb E(Y_v-pd_v)_+
 \le\sqrt{pd_v}\le\sqrt\mu.
 \tag{1.12}
\]

Sum (1.11) over (v).  For the second term, every retained path has
exactly (K) claims, so

\[
\begin{aligned}
 &\sum_v\sum_U n_{Uv}
       \left|{1\over A'_U}-{1\over\mu}\right|\\
 &\qquad=
 K\sum_{U\in{\cal T}'}A'_U
       \left|{1\over A'_U}-{1\over\mu}\right|\\
 &\qquad={K\over\mu}
       \sum_{U\in{\cal T}'}|A'_U-\mu|.
\end{aligned}
 \tag{1.13}
\]

Equations (1.8), (1.12), and (1.13) show that the expected overload is
at most the parenthesized quantity in (1.5).  Equation (1.7) bounds the
expected bad-tag count by the unmultiplied quantity in (1.3).  Divide the
two random variables by these two bounds and add them.  The expectation
of the resulting nonnegative sum is at most two, so some outcome has sum
at most two.  Each summand separately then gives (1.3) and (1.5).
\(\square\)

## 2. Protected geodesic application

Include the (g) middle owners of a chunk among its targets, in addition
to its calibrated protected lower and upper claims.  Then

\[
 |V|\le(2Q+1)W,
 \qquad
 K\le(2Q+1)g,
 \qquad
 KT\le(2Q+1)W.
 \tag{2.1}
\]

Coordinate symmetry and the integer calibration give

\[
 {d_v\over A}=
 \begin{cases}
 Tg/W,&v\text{ is a middle owner},\\[1mm]
 Tc_q/R_q,&v\text{ is in signed row }q,
 \end{cases}
 \le1.
 \tag{2.2}
\]

For the protected three-antichain graph,

\[
 {\Delta+1\over A}=m^{-3+o(1)}.
\]

Choose, for example,

\[
 L=Q\log m.
 \tag{2.3}
\]

In the truncated regime (Q=m^{1/2+o(1)}), this gives

\[
 \mu={A\over L(\Delta+1)}=m^{5/2-o(1)},
 \qquad
 {Q\over\sqrt\mu}+{Q\over L}=o(1).
 \tag{2.4}
\]

Theorem 1.1 yields

\[
 \boxed{
 \sum_{v\in V}(\ell(v)-1)_+=o(W).}
 \tag{2.5}
\]

The physical middle-owner capacity of the discarded tags is

\[
 g(T-|{\cal T}'|)=O(W/L)+o(W)=o(W).
 \tag{2.6}
\]

For an uncapped row,
(c_q=\lfloor R_q/T\rfloor) leaves scalar deficit less than (T).
The capped rows have (c_q=g); there are (O(\sqrt H)) of them and each
has deficit at most

\[
 R_q-gT\le W-gT=O(WH/m).
\]

Consequently the total calibration deficit, including both signs, is

\[
 O(QT)+O(WH^{3/2}/m)=o(W).
 \tag{2.7}
\]

The deadline enlargement used by the priority construction removes a
further (o(W)) scalar claims, already accounted for in its exact slack
ledger.

Discarding bad tags removes at most (K) further claims per tag.  By
(1.3), (2.1), and (L=Q\log m), this costs

\[
 K(T-|{\cal T}'|)
 =O(QW/L)+o(W)=O(W/\log m)+o(W).
 \tag{2.8}
\]

Thus (2.5), equal total-mass accounting, and (2.7)--(2.8) also give
\(o(W)\) total fractional underload.

## 2.1 A sharper pointwise form outside (o(W)) targets

For the later integral problem it is useful to spend more pruning entropy.
Put

\[
 \delta=m^{-2/3},
 \qquad
 L=Qm^{2/3}\log m.
 \tag{2.9}
\]

The protected bad-degree ratio is (m^{-3+o(1)}), so now

\[
 \mu={1\over Lm^{-3+o(1)}}=m^{11/6-o(1)},
 \qquad
 \delta^2\mu=m^{1/2-o(1)}.
 \tag{2.10}
\]

The relative estimate also needs a lower bound on the target-fibre mean.
For an uncapped row, with \(\lambda_q=R_q/T\ge1\),

\[
 {d_v\over A}={\lfloor\lambda_q\rfloor\over\lambda_q}\ge{1\over2}.
\]

For a capped row and for the middle owners, the ratio is at least
\(gT/W=1-o(1)\).  Thus every controlled fibre has mean
\(\Theta(\mu)\), so the exponent in (2.10) is uniform.

Apply the relative-degree pruning Corollary 1.2 from
`RECTANGLE_BAD_GRAPH_BALANCED_PRUNING_LEMMA_20260725.md` simultaneously
to tag and protected-target fibres, now with tag weight (Qg).  This extra
factor (Q) puts the total tag ledger and the total protected-target ledger
on the same (QW) scale; tag weight (g) alone would yield only an
(O(1/\log m)) exceptional tag fraction.  The
weighted exceptional proportion is

\[
 2e^{-m^{1/2-o(1)}}+{2\over L\delta}
 =O\!\left({1\over Q\log m}\right).
 \tag{2.11}
\]

Consequently the exceptional target set has size (o(W)), while the
exceptional tag fraction is (o(1/Q)).  On every good fibre,

\[
 |A'_U-\mu|\le\delta\mu,
 \qquad
 |d'_v-pd_v|\le\delta pd_v.
 \tag{2.12}
\]

The raw marked count of every target is at most (2\mu) with positive
probability simultaneously with (2.11): its upper-tail failure is
(e^{-\Omega(\mu)}), whereas the number of targets is only
(\exp(O(m))).  Hence the exceptional targets carry only (o(W)) total
fractional incidence as well.

Use uniform weights on every good tag.  For a good target, (2.2) and
(2.12) give the pointwise bound

\[
 \ell(v)
 \le{(1+\delta)pd_v\over(1-\delta)pA}
 \le1+3\delta.
 \tag{2.13}
\]

After scaling all real path weights by ((1+3\delta)^{-1}), one obtains a
genuine fractional matching on every good target.  Its lost tag mass,
including exceptional tags, is

\[
 O(\delta T)+o(T/Q)=o(T/Q),
 \tag{2.14}
\]

because (Q\delta=o(1)).  The omitted exceptional targets and their total
incidence have scalar mass (o(W)).

Thus the integral rounding problem may be posed with target capacities
exactly one, fractional tag deficit (o(T/Q)), and only an (o(W))
exceptional target ledger.

## 3. Remaining theorem

The fractional overload dual is now automatically satisfied by the point
constructed above.  What remains is genuinely integral:

> Round this one tag-saturating fractional point to one path per retained
> tag so that total duplicate target excess is (o(W)), while preserving
> the already legal geodesic chronology.

The protected width-two exponential census supplies the raw overlap
hierarchy down to density (1/\log m), but a self-contained growing-rank
nibble/absorption theorem performing this rounding has not yet been
proved.

## 4. Edge-coloring audit

`MATH_ATTACK_ISOLATED_FRACTIONAL_POINT_EDGE_COLORING_AUDIT_20260725.md`
verifies Theorem 1.1 and the sharper coefficient-scale substitution.
Choose rational

\[
 \rho\le(1+3\delta)^{-1},
 \qquad 1-\rho=o(1/Q).
\]

After omitting the exceptional ledgers, the point may be rationally
scaled to a multihypergraph with tag degree \(\rho D\) and target degree
at most \(D\).

The audit also proves that these degrees and the nonlinear width-two
intersection moments do not imply even a \((1+o(1))D\) edge coloring.  A padded
projective-plane system has zero nonlinear intersection excess between
different tags, zero fractional overload, and chromatic index
\(\Theta(KD)\).  The exact full-coloring gate is instead

\[
 \sum_e m_ey_e
 \le(1+o(1/Q))D
 \max_{M\text{ matching}}\sum_{e\in M}y_e
 \qquad(y_e\ge0).
\]

For coefficient one, a complete edge coloring is unnecessary, but tag
count alone is insufficient.  Without a separate chain-aligned reserve,
one needs a color missing only \(o(T/Q)\) tags and \(o(W)\) protected
targets; equivalently the coloring/palette overhead must be \(o(1/Q)\).
The projective-plane weighted cut is an obstruction to decomposing the
whole fractional point, not to one large color: its private filler edges
give a perfect tag matching.  The economical remaining gate is therefore
a direct matching meeting \(T-o(T/Q)\) tags, while the full-color gate is
the displayed weighted inequality.  The present nonlinear census is
uniform and time zero, and it is blind to singleton intersections.
