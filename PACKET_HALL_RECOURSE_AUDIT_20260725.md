# Self-audit of the Packet Hall and recourse theorem

Date: 2026-07-25

Audited source: PACKET_HALL_RECOURSE_20260725.md.

Method: independent theorem-by-theorem rederivation.  No computation,
search, solver, or external matching theorem is used.

## 0. Verdict

\[
\boxed{\text{PASS}}
\]

The survival-packet equivalence, the bounded-rank fractional-to-integral
rounding, the fixed-window implication, and both common-threshold recourse
bounds are correct.

The main advance is genuine but scoped.  It removes the *last*
fractional-to-integral deletion-cover gap at fixed Gaussian width.  It does
not produce the small fractional packet cover, choose the exact factor, or
prove MWB.

## 1. Binary owner incidences

For a cyclic order of \(n\) distinct labels and \(1\le r<n\), the \(n\)
cyclic \(r\)-intervals are distinct.

Indeed, if two different cyclic position intervals of length \(r\) had the
same label set, the corresponding proper consecutive position block would
be invariant under a nonzero cyclic shift.  A nonempty proper cyclic
interval cannot have such a period: at one boundary the shifted indicator
changes from zero to one, while invariance would force equality.  Thus one
wreath owns a target at most once at a fixed depth.

Consequently the owner objects \(\mathcal O_a\) in the source are sets, and
deleting a wreath removes exactly one incidence from every resource it owns.
Two different resources may generate the same wreath packet.  Treating
these as parallel resource-labelled constraints leaves the primal cover
polytope unchanged and makes the resourcewise dual decomposition valid.

## 2. Packet equivalence

Fix one resource with owner set \(O\), \(h=|O|\), and residual quota
\(\beta\).

For \(B\subseteq O\),

\[
 |O\setminus B|\le\beta
\]

if and only if every \((\beta+1)\)-subset of \(O\) meets \(B\).

* If more than \(\beta\) owners survive, choose any \(\beta+1\) of them.
* If a \(\beta+1\) packet avoids \(B\), those owners all survive.

Taking the union of these packet constraints over all depths and targets
still uses one common \(B\).  This proves source Theorem 2.1 without a
rankwise gluing assumption.

The packet size is \(\beta+1\).  Since a balanced quota is \(c_q\) or
\(c_q+1\), the maximum is \(c_q+2\), exactly as recorded.

## 3. Threshold rounding

Let \(\mathcal P\) have rank at most \(R\), and let

\[
 \sum_{v\in P}x_v\ge1
\qquad(P\in\mathcal P)
\]

with \(x_v\ge0\).  Capping \(x_v\) at one preserves feasibility.

Set \(B=\{v:x_v\ge1/R\}\).  If \(P\cap B=\varnothing\), then

\[
 \sum_{v\in P}x_v
 <|P|/R\le1,
\]

a contradiction.  Moreover

\[
 \sum_{v\in B}w_v
 \le R\sum_vw_vx_v
\]

for arbitrary nonnegative costs.  Therefore

\[
 \vartheta\le\tau\le R\vartheta.
\]

There is no use of total unimodularity, fixed-uniformity matching, or an
unverified growing-parameter theorem.

## 4. Relation to the old multicover LP

For one resource let \(h=|O|\), let \(d=h-\beta>0\), and let
\(P\subseteq O\) have size \(\beta+1\).  Then

\[
 |O\setminus P|=h-\beta-1=d-1.
\]

If \(0\le x\le1\) and \(\sum_{O}x\ge d\), then

\[
 \sum_Px
 \ge d-\sum_{O\setminus P}x
 \ge d-(d-1)=1.
\]

Thus every old fractional multicover is a fractional packet cover.  The
converse is false.  For one resource the packet system is the complete
\(k\)-uniform hypergraph with

\[
 k=\beta+1.
\]

Symmetrizing any fractional cover gives the exact optimum

\[
 \vartheta=h/k.
\]

An integral cover has size

\[
 h-k+1=h-\beta,
\]

which is also the old one-constraint multicover optimum.  The example
\((h,\beta)=(3,1)\) therefore verifies the strict inequality

\[
 3/2<2.
\]

The abstract integrality ratio tends to \(k\) as \(h\to\infty\), so the
factor \(R\) cannot be improved universally.

### Order statistics and incidence counting

For a resource with \(k=\beta+1\), all packet inequalities hold if and only
if the sum of the \(k\) smallest owner weights is at least one.  This is
tautologically the minimum packet sum, so source (3.9) is exact.

Averaging all \(\binom hk\) packet inequalities counts each owner
\(\binom{h-1}{k-1}\) times and yields

\[
 \sum_{E\in O}x_E\ge h/k.
\]

One wreath owns exactly \(n\) targets at each controlled depth.  Therefore,
after summing over all over-capacity resources, every wreath weight is
counted at most \(nK_A\) times.  This proves source (3.12).  Since

\[
 h/k\ge1,\qquad h\le R_A(h/k),
\]

source (3.13) follows.  At
\(\|x\|_1=o_A(t/\sqrt m)\) and \(K_A=O_A(\sqrt m)\), its right side is
\(o_A(nt)=o_A(W)\), with the same conclusion for total violating
occurrence mass.

### Compressed dual

For packet weights \(y_P\), define

\[
 Y_a=\sum_{P\in\mathcal P_a}y_P,\qquad
 z_{a,E}=\sum_{P\in\mathcal P_a:E\in P}y_P.
\]

Then

\[
 0\le z_{a,E}\le Y_a,\qquad
 \sum_Ez_{a,E}=k_aY_a,
\]

and unit wreath congestion is \(\sum_az_{a,E}\le1\).

Conversely, after division by \(Y_a>0\), the local vector \(z_a/Y_a\)
lies in

\[
 \{p:0\le p_E\le1,\ \sum p_E=k_a\}.
\]

Every vertex of this polytope is integral: if two coordinates were
fractional they could be perturbed oppositely, while exactly one fractional
coordinate is impossible because the coordinate sum is the integer \(k_a\).
Its vertices are therefore precisely the incidence vectors of
\(k_a\)-subsets.  This proves the local packet decomposition used in source
Theorem 3.2.

For fixed \(Y\), the remaining \(z\)-system is a bipartite flow.  A cut
with resource side \(X\) and owner side \(Z\) gives

\[
 \sum_{a\in X}
 Y_a(k_a-|\mathcal O_a\setminus Z|)\le|Z|.
\]

For each fixed \(Z\), including exactly the resources with positive
coefficient is the strongest choice of \(X\).  This yields

\[
 \sum_aY_a(k_a-|\mathcal O_a\setminus Z|)_+\le|Z|,
\]

and max-flow/min-cut proves sufficiency.  Thus the compressed cut dual
(3.14) is exact; no packet constraint is lost.

### Direct overload transfer

For the chosen balanced quota \(\beta_q\),

\[
 O_q(F)
 \le\sum_S(\mu_q^F(S)-\beta_q(S))_+.
\]

For a contributing resource, write \(h=\mu_q^F(S)\) and
\(k=\beta_q(S)+1\).  Then its excess is \(h-k+1\le h\).  Also

\[
 k\in\{c_q+1,c_q+2\},
\qquad k/c_q\le3.
\]

Therefore

\[
 \sum_{q\le H}\frac{O_q(F)}{c_q}
 \le3\sum_{a\in\mathcal V}h_a/k_a.
\]

The averaged packet inequalities give
\(h_a/k_a\le\sum_{E\in\mathcal O_a}x_E\).  Since a wreath owns exactly
\(n\) targets at each depth, summing through \(H\) depths counts one
wreath weight at most \(nH\) times.  Hence

\[
 \sum_{q\le H}O_q(F)/c_q
 \le3nH\|x\|_1.
\]

No bounded-rank hypothesis enters this argument.  With
\(\|x\|_1=o(t/H)\) and \(W=nt\), the right side is \(o(W)\), validating
source Theorem 3.3.

## 5. Fixed-window quantifiers

For \(q\le A\sqrt m\),

\[
 \log\frac{W}{N_q}
 =\frac{q(q+1)}m+O_A(m^{-1/2}),
\]

so \(\max c_q\le C_A\) for fixed \(A\).  Hence \(R_A=C_A+2\) is independent
of \(m\).

If

\[
 \vartheta_A=o_A(t/\sqrt m),
\]

threshold rounding gives

\[
 |B|\le R_A\vartheta_A=o_A(t/\sqrt m).
\]

The residual core is dominated by the already chosen balanced quotas, and
\(B\subseteq F\), so exact completion is automatic.  This is precisely the
antecedent of the audited hard-quota charging theorem.

Conversely, an integral exceptional family is itself a fractional packet
cover.  Thus at the little-\(o(t/\sqrt m)\) scale,

\[
 \exists\,\tau_A=o(t/\sqrt m)
 \quad\Longleftrightarrow\quad
 \exists\,\vartheta_A=o(t/\sqrt m)
\]

for every fixed \(A\).  Constants may depend arbitrarily on \(A\);
diagonalization is performed only after the fixed-window theorem.  The
source correctly avoids claiming a uniform result for growing \(A(m)\).

## 6. Dynamic common-threshold theorem

### 6.1 Aggregate version

Choose \(\theta\) uniformly in \((0,1/R]\), and put

\[
 z_v^{(j)}=\min\{x_v^{(j)},1/R\}.
\]

Every packet contains a coordinate of value at least \(1/R\), so it is hit
for every allowed threshold.  For a fixed vertex,

\[
 \Pr(v\in B_j)=Rz_v^{(j)}
\]

and

\[
 \Pr(v\in B_j\triangle B_{j-1})
 =R|z_v^{(j)}-z_v^{(j-1)}|.
\]

Linearity of expectation gives the aggregate holding-plus-recourse formula.
Coordinatewise clipping is 1-Lipschitz, giving the displayed upper bound in
the source.

### 6.2 Pointwise-holding version

Choose \(\theta\) uniformly in \([1/(2R),1/R]\).  Packets are still hit.
For every possible threshold,

\[
 |B_j|
 \le2R\|x^{(j)}\|_1,
\]

because membership implies \(x_v^{(j)}\ge1/(2R)\).

For one coordinate, its membership changes only if the common threshold
lies between the two fractional values.  The interval from which the
threshold is drawn has length \(1/(2R)\), hence

\[
 \Pr(v\in B_j\triangle B_{j-1})
 \le2R|x_v^{(j)}-x_v^{(j-1)}|.
\]

After summation, one threshold attains the expected recourse bound while
the pointwise size inequality holds automatically.  This validates source
equations (5.4)--(5.5) and the exact-factor corollary.

Extending \(x^{(j)}\) by zero outside \(F_j\) is safe: every chosen threshold
is positive, so \(B_j\subseteq F_j\).

## 7. Boundary cases

1. If the packet hypergraph is empty, \(\vartheta=\tau=0\); the convention
   \(R=1\) is harmless.
2. If \(h\le\beta\), the resource creates no packet and no deletion demand.
3. If \(h=\beta+1\), there is one full owner packet; fractional and integral
   cover values are both one.
4. Equality at the threshold is safe because the rounded set uses
   \(x_E\ge\theta\).
5. The packet LP is finite because the exact factor and the controlled
   window are finite, even though explicitly listing all packets may be
   exponentially expensive.  The note is existential, not algorithmic.
6. Balanced quotas remain chosen separately by depth, exactly as allowed in
   the unlabelled hard-quota route.  The common object across depths is the
   deletion family.
7. The bottom-\(k\) order-statistic form is per resource; no invalid
   averaging across different targets is used.
8. The compressed packet dual uses real capacitated flow only; it is an LP
   identity, not an integral matching assertion.
9. The direct overload estimate uses \(k/c_q\le3\), which remains valid at
   all depths because \(c_q\ge1\); it is not restricted to fixed \(A\).

## 8. Correct scope

The source does not establish the fractional survival-packet theorem
\((\mathrm{FSP}_A)\).  In particular:

* no small packet cover is constructed;
* no exact factor is shown to have the required packet geometry;
* no cyclic-alignment theorem is inferred from an abstract nested flow;
* no growing-\(A\) black box is invoked; and
* no pointwise recourse claim stronger than equations (5.4)--(5.5) is made.

The mathematical frontier is genuinely narrowed:

\[
\boxed{
\text{integral hard-quota absorber}
\quad\rightsquigarrow\quad
\text{bounded-rank fractional survival-packet cover}.
\]

At fixed Gaussian width, integer rounding and integer recourse now cost
only a constant depending on that width.  The surviving problem is the
correlated fractional packet geometry of one exact cyclic-wreath factor.
