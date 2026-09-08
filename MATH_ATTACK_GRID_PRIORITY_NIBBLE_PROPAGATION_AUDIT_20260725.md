# Grid-aware priority nibble: the exact propagation gate

## 0. Outcome

This note combines two proved inputs:

1. the priority/deadline formula for a geodesic chunk;
2. the pruning theorem which removes every shared full-grid antichain of size three and leaves a balanced polynomial catalogue in which every two retained grids have intersection width at most two.

They give a complete **one-bite clearance recurrence**. They also show that all scalar losses, owner collisions, and clearance failures can be summed through enough bites to reduce the active tag density to \(1/\log m\).

What they do **not** yet give is hereditary residual-degree propagation. The precise missing quantity is the weighted transfer energy defined in (30) below. The original width-two census bounds its unweighted time-zero version, but not its later versions after the priority counts and owner indicators have reweighted the catalogue.

There is, however, a stronger way to use the three-antichain estimate: quarantine bad grids only against the chunks already selected, instead of permanently thinning the full catalogue. Section 10 proves deterministically that this dynamic quarantine loses only \(o(W)\) weighted tag/target fibres while retaining the original exponential entropy. This removes the polynomial-degree objection from the viable version of the architecture.

Thus the remaining problem in this lane is no longer an unspecified “nibble theorem”. After the dynamic quarantine of Section 10, it is the single combined estimate

\[
 \sum_{t<R}
 \left(
 \frac{\mathscr E_t}{\eta_t^2}
g\alpha^2\mathscr B_t
 \right)=o(W),
 \tag{GATE}
\]

for a suitable tolerance sequence.  Here \(\mathscr E_t\) is the weighted
degree-transfer energy and \(\mathscr B_t\) is the weighted current-bite
three-antichain mass.  Both are defined inside the current integral
residual catalogue.

---

## 1. Residual catalogue and fibre weights

Let \(g\asymp\sqrt{QH}=m^{1/2+o(1)}\) be the geodesic chunk length. A base catalogue object \(P\) has:

* one tag \(\tau(P)\);
* \(g\) middle owners \(X_1(P),\ldots,X_g(P)\);
* a full geodesic grid \(\mathcal G(P)\);
* all \(g!\) priority orders on its \(g\) phases.

It is important here to prune **base grids and retain their priority orders**, rather than regard the surviving priority orders as unrelated fixed hyperedges. Otherwise the adaptive deadline mechanism has already been destroyed.

This quotient form of the pruning is legitimate.  Bad adjacency depends only
on the two full grids, so every bad neighbouring base grid contributes the
same full set of priority copies.  Hence

\[
 \frac{\Delta_{\rm bad}^{\rm base}}{A^{\rm base}}
 =
 \frac{\Delta_{\rm bad}^{\rm decorated}}{A^{\rm decorated}}.
 \tag{0}
\]

Likewise, a fixed target occurs in at most one phase of a fixed signed row,
and, when it occurs, exactly \(c_q(g-1)!\) priority orders claim that phase.
Thus quotienting by the priority copies divides every tag fibre by \(g!\)
and every signed target fibre by the same stratum-dependent constant.  The
balanced pruning lemma applies directly to the quotient base-grid graph,
and retaining all priorities above each selected base grid restores the
calibrated target degrees.  This supplies the asserted base-grid version of
the pruning theorem; it is not an additional assumption.

After the three-antichain pruning, outside an exceptional family of total weighted size \(o(W)\), the retained catalogue has degree

\[
 D_0\ge \mu/4=m^{5/2-o(1)}
 \tag{1}
\]

in every tag fibre and every protected target fibre, and every two retained base grids have intersection width at most two.

We use the following fibre weights:

\[
 \operatorname{wt}(F)=
 \begin{cases}
 g,&F\text{ is a tag fibre},\\
 1,&F\text{ is a lower or upper target fibre}.
 \end{cases}
 \tag{2}
\]

Deleting a bad tag loses at most \(g\) middle owners, while declaring one target exceptional costs one literal repair. Hence these are exactly the relevant accounting weights. Since the number of tags is \(T\asymp W/g\),

\[
 \sum_{F\text{ tag}}\operatorname{wt}(F)=\Theta(W),
 \qquad
 \sum_{F\text{ target}}\operatorname{wt}(F)=O(QW).
 \tag{3}
\]

The initial pruning therefore removes only \(o(W)\) actual cost, despite having to balance \(O(QW)\) fibre incidences.

At time \(t\), let \(\mathcal O_t\) be the unused middle owners and let \(\mathcal Z_t\) be the set of targets still available for protected use. For a base grid \(P\), define

\[
 a_t(P)=
 \mathbf 1_{\{X_1(P),\ldots,X_g(P)\}\subseteq\mathcal O_t}
 \Pi_t(P),
 \tag{4}
\]

where \(\Pi_t(P)\) is the exact number of priority orders which remain feasible against the targets already used. The residual weighted tag degree is

\[
 D_t(U)=\sum_{P:\tau(P)=U}a_t(P).
 \tag{5}
\]

For \(D_t(U)>0\), the canonical sampling distribution in tag \(U\) is

\[
 \nu_{t,U}(P)=\frac{a_t(P)}{D_t(U)}.
 \tag{6}
\]

This definition incorporates both exact owner availability and all adaptive priorities. No fractional factor has been introduced: the weights merely count legal integral choices.

---

## 2. Exact deadline recurrence inside one grid

For a base grid \(P\), let \(B_{t,q}(P)\) be the number of phases whose first unavailable target has depth at most \(q\). Put

\[
 d_q=g-c_q^{(g)},\qquad
 n_{t,q}=B_{t,q}-B_{t,q-1},\qquad
 \sigma_{t,q}=d_q-B_{t,q}.
 \tag{7}
\]

The priority orders are feasible exactly when

\[
 B_{t,q}(P)\le d_q\quad(1\le q\le Q).
 \tag{8}
\]

Their number is

\[
 \Pi_t(P)=
 (g-B_{t,Q})!
 \prod_{q=1}^{Q}
 \frac{(d_q-B_{t,q-1})!}{(d_q-B_{t,q})!}.
 \tag{9}
\]

Suppose a newly used target changes the first-block depth of one phase from \(r\) to \(s<r\). Then the exact multiplicative update is

\[
 \frac{\Pi_{t+1}(P)}{\Pi_t(P)}
 =
 \frac{\sigma_{t,s}}{\sigma_{t,r}+n_{t,r}}
 \prod_{q=s+1}^{r-1}
 \frac{\sigma_{t,q}}{\sigma_{t,q}+n_{t,q}},
 \tag{10}
\]

where the unblocked class is \(r=Q+1\), with denominator equal to its current population. Multiple new targets are handled by applying (10) successively; the final result is independent of the order because both sides equal the factorial quotient (9).

In particular, the one-bite recurrence is completely explicit:

\[
 B_{t+1,q}(P)
 \le B_{t,q}(P)+\Delta_{t,q}(P),
 \qquad
 \sigma_{t+1,q}(P)
 \ge\sigma_{t,q}(P)-\Delta_{t,q}(P),
 \tag{11}
\]

where \(\Delta_{t,q}(P)\) is the number of formerly unblocked phases of \(P\) hit through depth \(q\) by the current bite.

This is the clearance-majorization recurrence. It is an identity/inequality about actual integral priorities, not a heuristic occupancy approximation.

---

## 3. What width two gives in one bite

Because every retained grid intersection has width at most two, the grid-intersection lemma gives, for every pair \(P,E\),

\[
 |\mathcal G(P)\cap\mathcal G(E)\text{ in ranks }m\pm[0,q]|
 \le 2(2q+1).
 \tag{12}
\]

Activate each currently live tag independently with probability \(\alpha\), and in an activated tag \(U\) sample \(E\sim\nu_{t,U}\). Before the standard alteration, the variables contributed by distinct tags are independent. For fixed \(P,q\), write \(Y_{U,q}(P)\) for the number of phases of \(P\) newly blocked through depth \(q\) by the tentative choice from \(U\), with \(Y_{U,q}=0\) if \(U\) is inactive. Then

\[
 0\le Y_{U,q}(P)\le 4q+2,
 \qquad
 \Delta_{t,q}(P)\le\sum_UY_{U,q}(P).
 \tag{13}
\]

If the current target loads obey the conditional PDRC bound

\[
 \sum_U
 \Pr_{E\sim\nu_{t,U}}
 \{S\text{ is exposed by }E\}
 \le \rho_t\lambda_r
 \tag{14}
\]

for every protected lower and upper target \(S\) at signed depth \(r\),
then double counting the \(2q\) signed rows gives

\[
 \mathbb E\Delta_{t,q}(P)
 \le 2\alpha\rho_t g\Lambda_q,
 \qquad
 \Lambda_q:=\sum_{r\le q}\lambda_r.
 \tag{15}
\]

Moreover, Bernstein's inequality applied to the independent bounded variables in (13) yields the completely conditional estimate

\[
 \Pr\!\left(
 \Delta_{t,q}(P)-\mathbb E\Delta_{t,q}(P)\ge x
 \mid\mathcal F_t
 \right)
 \le
 \exp\!\left[
 -\frac{x^2}
 {2\big((4q+2)\mathbb E\Delta_{t,q}(P)+(4q+2)x/3\big)}
 \right].
 \tag{16}
\]

Thus width two removes the former large-jump obstruction in one round. It does not, by itself, imply that (14) remains true in later rounds.

---

## 4. Summable clearance and collision losses

Choose a slowly growing \(\omega_m\) and put

\[
 \varepsilon_m=\frac{g}{m^{2/3}\omega_m},
 \qquad
 L_m=(\log m)^2,
 \qquad
 \alpha=\frac{\varepsilon_m}{L_mg}
 =\frac1{m^{2/3}\omega_m(\log m)^2}.
 \tag{17}
\]

Enlarge the deadline allowance to

\[
 \bar d_q=\max\{d_q,\lceil\varepsilon_m\Lambda_q\rceil\},
 \tag{18}
\]

capped at \(g\). The exact scalar ledger already proves

\[
 \sum_{q\le Q}(\bar d_q-d_q)=o(g),
 \tag{19}
\]

so this enlargement costs \(o(W)\) globally.

Under (14), (15) and dyadic Markov imply that in one bite only an

\[
 O(\log m/L_m)=O(1/\log m)
 \tag{20}
\]

fraction of the activated tag mass violates some enlarged deadline. Deleting those tentative chunks costs at most

\[
 O(\alpha W\log m/L_m)
 \tag{21}
\]

middle-owner weight in that bite.

The owner-conflict alteration loses an \(O(\alpha g)\) fraction of the remaining tentative chunks, hence costs

\[
 O(\alpha^2gW)
 \tag{22}
\]

per bite.

To lower the active tag density from \(1\) to \(1/\log m\) takes

\[
 R=(1+o(1))\alpha^{-1}\log\log m
 \tag{23}
\]

bites. Summing (21) and (22) gives respectively

\[
 O\!\left(W\frac{\log\log m}{\log m}\right)=o(W)
 \tag{24}
\]

and

\[
 O\!\left(W\alpha g\log\log m\right)=o(W).
 \tag{25}
\]

The final unused tag mass is \(W/\log m=o(W)\). Therefore **all non-propagation ledgers close** at the desired stopping density.

---

## 5. A self-contained conditional degree-concentration lemma

Let \(\mathscr F_t\) be the current collection of good tag and target fibres. For \(F\in\mathscr F_t\), let \(D_t(F)>0\) be its current weighted catalogue degree. Let

\[
 Y_{t,F}=Y_{t,F}(X_U:U\text{ live tag})
 \tag{26}
\]

be its post-bite degree, after the exact priority updates (9)--(10), but before deleting newly exceptional fibres. The variables \(X_U\) are independent tentative tag choices: inactive with probability \(1-\alpha\), and otherwise sampled from \(\nu_{t,U}\).

There is an exact binary representation of this random variable.  Expand
each base grid into its currently feasible fixed priority decorations.
For decorated candidates \(e,f\), write \(e\sim f\) when they share a
middle owner or a currently protected claimed target.  For the degree
calculation use an **auxiliary wasteful catalogue restriction**: after the
actual alteration, voluntarily discard from the *future catalogue* every
decorated candidate conflicting with any tentative choice, including a
choice not accepted by the alteration.  This is only a pessimistic
restriction of future options; it neither declares the corresponding
physical target used nor creates a repair obligation.  A lower bound for
this restricted degree is therefore a valid lower bound on the available
actual catalogue.  The word still emits only the chunks retained by the
stated alteration ledgers.

For a live tag \(U\), define the conditional collision probabilities

\[
 p_{t,U}(e)=
 \Pr_{E\sim\nu_{t,U}}(E\sim e),
 \qquad
 p_{t,U}(e,f)=
 \Pr_{E\sim\nu_{t,U}}(E\sim e,\ E\sim f).
 \tag{26a}
\]

Let \(I_e\) be the indicator that \(e\) survives the tentative bite.
Independence between tag choices gives the exact identities

\[
 \boxed{
 \mathbb E I_e
 =
 \prod_U(1-\alpha p_{t,U}(e))}
 \tag{26b}
\]

and

\[
 \boxed{
 \mathbb E(I_eI_f)
 =
 \prod_U
 \left[
 1-\alpha\bigl(
 p_{t,U}(e)+p_{t,U}(f)-p_{t,U}(e,f)
 \bigr)
 \right].}
 \tag{26c}
\]

Consequently, for the decorated fibre
\(\widehat{\mathcal C}_{t,F}\),

\[
 \boxed{
 \mathbb E Y_{t,F}
 =
 \sum_{e\in\widehat{\mathcal C}_{t,F}}
 \prod_U(1-\alpha p_{t,U}(e))}
 \tag{26d}
\]

and

\[
 \boxed{
 \operatorname{Var}Y_{t,F}
 =
 \sum_{e,f\in\widehat{\mathcal C}_{t,F}}
 \left[
 \prod_U
 \left(1-\alpha(p_U(e)+p_U(f)-p_U(e,f))\right)
 -
 \prod_U(1-\alpha p_U(e))(1-\alpha p_U(f))
 \right].}
 \tag{26e}
\]

Thus the one-round conditional covariance is exactly the common-link
probability \(p_U(e,f)\), together with the harmless negative product
term.  Equations (26b)--(26e) are valid after arbitrary previous history;
all history is contained in the current measures \(\nu_{t,U}\).

For a stratum \(s\) (tag fibres, or one specified signed depth of target fibres), choose a reference contraction \(\rho_{t,s}\). Define the normalized one-round transfer energy

\[
\begin{aligned}
 \mathscr E_t:=
 \sum_s\sum_{F\in s}\operatorname{wt}(F)
 \Bigg[&
 \left(
 \frac{\mathbb E[Y_{t,F}\mid\mathcal F_t]}{D_t(F)}
 -\rho_{t,s}
 \right)^2\\
 &+\frac1{2D_t(F)^2}
 \sum_U
 \mathbb E\left(
 Y_{t,F}(X)-Y_{t,F}(X^{(U)})
 \right)^2
 \Bigg],
 \tag{27}
\end{aligned}
\]

where \(X^{(U)}\) is obtained by independently resampling the \(U\)-coordinate. We minimize (27) over the reference numbers \(\rho_{t,s}\).

### Proposition 5.2 (one-round weighted concentration)

For every \(\eta>0\), the expected total weight of fibres satisfying

\[
 \left|\frac{Y_{t,F}}{D_t(F)}-\rho_{t,s(F)}\right|>2\eta
 \tag{28}
\]

is at most

\[
 \boxed{\frac{\mathscr E_t}{\eta^2}.}
 \tag{29}
\]

#### Proof

For each fixed \(F\), Efron--Stein gives

\[
 \operatorname{Var}Y_{t,F}
 \le\frac12\sum_U
 \mathbb E\big(Y_{t,F}(X)-Y_{t,F}(X^{(U)})\big)^2.
\]

If (28) holds, then either the normalized conditional mean differs from the reference by more than \(\eta\), or the normalized random fluctuation about its mean exceeds \(\eta\). Markov on the first deterministic alternative and Chebyshev on the second give a probability at most the corresponding bracket in (27), divided by \(\eta^2\). Multiply by \(\operatorname{wt}(F)\) and sum. \(\square\)

This proposition treats tag fibres with weight \(g\) and all target fibres with weight one in one line. It is valid for the actual nonlinear priority update, since Efron--Stein needs only that \(Y_{t,F}\) be a function of the independent tentative tag variables.

If after each bite the fibres in (28) are declared exceptional, then the sufficient hereditary propagation condition is

\[
 \boxed{
 \sum_{t<R}\frac{\mathscr E_t}{\eta_t^2}=o(W),
 \qquad
 \sum_{t<R}\eta_t=o(1).
 }
 \tag{30}
\]

The second condition keeps the multiplicative degree distortion bounded by \(1+o(1)\); the first says the cumulative actual cost of exceptional tag and target fibres is \(o(W)\). Together with Sections 2--4, (30) propagates the conditional PDRC state down to tag density \(1/\log m\).

---

## 6. Relation with the width-two exponential census

For intuition, define the fractional influence of a tentative chunk \(E\) on a fibre \(F\) by

\[
 I_{t,F}(E)=
 \frac1{D_t(F)}
 \sum_{P\in F}a_t(P)
 \left(1-\frac{\Pi_t(P\mid E)}{\Pi_t(P)}\right),
 \tag{31}
\]

where the ratio is zero if \(E\) uses a middle owner of \(P\), and otherwise is the exact product of the hazard multipliers (10). Resampling a tag changes \(Y_{t,F}/D_t(F)\) by at most the sum of two such influences. Hence the variance part of (27) is bounded, up to an absolute constant, by

\[
 \alpha\sum_{F}\operatorname{wt}(F)
 \sum_U\mathbb E_{E\sim\nu_{t,U}} I_{t,F}(E)^2.
 \tag{32}
\]

This is exactly a weighted bow-tie energy.  Put

\[
 h_t(P,E)=1-\frac{\Pi_t(P\mid E)}{\Pi_t(P)},\qquad
 p_{t,F}(P)=\frac{a_t(P)}{D_t(F)},
 \tag{32a}
\]

with \(h_t(P,E)=1\) for an owner collision, and define the common-link
kernel

\[
 K_t(P,P')=
 \sum_U\mathbb E_{E\sim\nu_{t,U}}
 h_t(P,E)h_t(P',E).
 \tag{32b}
\]

Then, by expanding the square,

\[
 \boxed{
 \sum_U\mathbb E_{E\sim\nu_{t,U}} I_{t,F}(E)^2
 =
 \sum_{P,P'\in F}
 p_{t,F}(P)p_{t,F}(P')K_t(P,P').}
 \tag{32c}
\]

For a binary regular collision graph, \(K_t(P,P')\) is the normalized
common-neighbour count.  Thus (32c) is the residual weighted analogue of
the triangle/bow-tie (equivalently, diagonal four-walk) statistic.  This
identity is preferable to a maximum point-mass hypothesis: a residual
measure may concentrate on one isolated candidate, making its point mass
arbitrarily large while (32c), correctly, remains zero.

At time zero the weights \(a_0(P)\) are uniform within each retained base-grid fibre, and the proved width-two shape census bounds the corresponding exponential overlap sums for every \(1\le w\le C\log m\). Thus it controls the raw version of (32), including all higher terms in the inclusion--exclusion expansion.

At time \(t>0\), however,

\[
 a_t(P)=\mathbf1_{\operatorname{owners}(P)\subseteq\mathcal O_t}\Pi_t(P)
 \tag{33}
\]

is highly nonuniform. The pair census is an unweighted row-sum estimate and supplies no domination of the weighted sums in (31)--(32). In particular, the feasible priority mass may concentrate on a small family of mutually correlated grids even though that family had negligible raw catalogue density.

This is exactly why the time-zero second moment is not a propagation theorem. Formula (30), or equivalently the hereditary weighted influence bound obtained from (31)--(32), is the single unsummed term.

---

## 7. Why polynomial pruning cannot justify quasirandom propagation

There is a simple quantitative warning. After pruning, a tag has only

\[
 D_0=m^{5/2-o(1)}
 \tag{34}
\]

retained base grids, each using \(g=m^{1/2+o(1)}\) middle owners. If the unused owner set at density \(z=1/\log m\) behaved independently of these grids, the expected number of owner-compatible retained grids in one tag would be

\[
 D_0z^g
 =m^{5/2-o(1)}(\log m)^{-m^{1/2+o(1)}}
 =o(1).
 \tag{35}
\]

Therefore no proof based on quasirandom independent residual owners can propagate this polynomial catalogue to density \(1/\log m\). A successful argument must prove that the matching process leaves an **aligned** residual, and precisely such alignment is measured by the later-time weights in (33) and the transfer energy (27).

This does not prove that propagation is impossible. It proves that the proved raw width-two census alone cannot establish it.

---

## 8. Exact frontier

The following pieces are now rigorous:

1. three-antichain pruning reduces all retained grid intersections to width at most two while losing weighted \(o(W)\);
2. the width-two shape census controls the entire unweighted exponential overlap expansion at time zero;
3. the priority count and every one-phase update are exact, equations (9)--(10);
4. the one-bite clearance recurrence is (11), with concentration (16);
5. scalar slack, clearance failures, owner collisions, and the final \(1/\log m\) tag residue together cost \(o(W)\);
6. Proposition 5.1 gives the exact weighted recurrence needed for tag and target fibres.

The only unproved propagation assertion in this lane is the combined
hereditary estimate

\[
 \sum_{t<R}
 \left(
 \frac{\mathscr E_t}{\eta_t^2}
g\alpha^2\mathscr B_t
 \right)=o(W),
\]

with \(\mathscr E_t\) defined by (27) and \(\mathscr B_t\) by (52). The
initial grid census bounds only their unweighted \(t=0\) analogues.
Proving their hereditary weighted estimate, or replacing the nibble by an
explicit residual-alignment operation which forces it, is the next
mathematical theorem.

---

## 9. A growing-width tradeoff

One might try to repair the entropy loss in (35) by forbidding a shared
\(s\)-antichain with \(s=s(m)\to\infty\), instead of taking \(s=3\).
The same counting argument exposes an incompatible pair of requirements
for this particular one-shot-pruning architecture.

For an \(s\)-antichain, there are \(2(s-1)\) positive successive coordinate
gaps.  Summing their membership-atom costs gives, uniformly in the range
needed below,

\[
 \xi_s
 \le
 m^{1+o(1)}
 \left(\frac{Cs}{m}\right)^{2(s-1)}.
 \tag{36}
\]

Indeed, after fixing the first cell, each ordered list of positive gaps
prescribes \(s-1\) disjoint nonempty coordinate blocks.  The reciprocal
multinomial sum is at most \((Cs/m)^{s-1}\) for each of the two axes; the
choice of the first cell and its rank contributes \(m^{1+o(1)}\).

The balanced independent thinning with parameter
\(p=[L(\Delta_s+1)]^{-1}\) consequently retains typical fibre degree

\[
 \log\mu_s
 =
 O\!\left(s\log\frac{m}{s}\right).
 \tag{37}
\]

On the other hand, after forbidding an \(s\)-antichain, an intersection has
width at most \(s-1\).  Repeating the shape count with \(s-1\) chains gives
successive-span ratio at least on the scale

\[
 \frac{g}{m}(Cw)^{\,s-1}.
 \tag{38}
\]

Thus the same **width-only shape-count proof** of the exponential census at
\(w\asymp\log m\) is summable only when

\[
 s=O\!\left(\frac{\log m}{\log\log m}\right).
 \tag{39}
\]

In that whole range, (37) gives

\[
 \log\mu_s
 =O\!\left(\frac{(\log m)^2}{\log\log m}\right)
 =o(g\log\log m).
 \tag{40}
\]

Therefore at owner density \(z=1/\log m\),

\[
 \mu_sz^g=o(1).
 \tag{41}
\]

Conversely, merely making the exchangeable owner-survival expectation
nonvanishing would require

\[
 s=\Omega\!\left(\frac{g\log\log m}{\log m}\right),
 \tag{42}
\]

which is far outside (39).

Hence **no choice of a fixed-before-the-nibble antichain threshold \(s\)**
simultaneously supplies, through these two estimates, (a) the entropy
required by an exchangeable residual at density \(1/\log m\) and (b) the
\(w\asymp\log m\) width-only census used for second-moment propagation,
when combined with the balanced independent thinning at
\(p=[L(\Delta_s+1)]^{-1}\).

This is an architectural ceiling, not a theorem against aligned
constructions.  It points to two remaining possibilities:

1. roundwise, residual-aware pruning which continues to use the original
   exponential catalogue entropy; or
2. an explicit alignment/factor-trade mechanism which makes the owner
   residual highly nonexchangeable and proves (30) directly.

---

## 10. Dynamic three-antichain quarantine preserves exponential entropy

The first alternative at the end of Section 9 has a deterministic
degree ledger.

Let \(\mathcal C_U\) be the full base-grid catalogue over tag \(U\), of
size \(A\).  Let \(B\) be the graph joining grids on distinct tags when
they share a three-antichain.  The proved conflict estimate is

\[
 \Delta(B)\le \xi A,\qquad \xi=m^{-3+o(1)}.
 \tag{43}
\]

Every base grid belongs to at most

\[
 K\le g(2Q+1)=m^{1+o(1)}
 \tag{44}
\]

protected target-occurrence fibres.  Every calibrated good target fibre
has original degree \((1-o(1))A\).

Let \(\mathcal S\) be any already selected family of mutually disjoint
chunks, with

\[
 |\mathcal S|\le T\asymp W/g.
 \tag{45}
\]

Delete from the current catalogue every grid in

\[
 \mathcal N_B(\mathcal S)
 :=\bigcup_{E\in\mathcal S}N_B(E).
 \tag{46}
\]

Then every remaining grid has width-two intersection with every selected
grid.

### Proposition 10.1 (deterministic quarantine ledger)

For every \(\eta>0\), the total tag-fibre weight of fibres losing more
than an \(\eta\)-fraction of their original catalogue is at most

\[
 \boxed{\frac{W\xi}{\eta}.}
 \tag{47}
\]

The number, hence total weight, of protected target fibres losing more
than an \(\eta\)-fraction is at most

\[
 \boxed{\frac{WK\xi}{g\eta}.}
 \tag{48}
\]

#### Proof

The total number of forbidden grid incidences is at most

\[
 |\mathcal N_B(\mathcal S)|
 \le|\mathcal S|\Delta(B)
 \le T\xi A.
 \tag{49}
\]

If a tag fibre is \(\eta\)-bad, it contains more than \(\eta A\)
forbidden grids.  Hence the number of such tags is at most
\(T\xi/\eta\).  Multiplying by tag weight \(g\), and using \(gT\asymp W\),
proves (47).

For target fibres, double count pairs \((P,F)\) with
\(P\in\mathcal N_B(\mathcal S)\cap F\).  Each forbidden grid is in at
most \(K\) such fibres, so their total forbidden incidence is at most
\(KT\xi A\).  Every \(\eta\)-bad target fibre contributes
\((1-o(1))\eta A\).  This proves (48). \(\square\)

Take, for example, \(\eta=m^{-1}\).  Equations (43)--(44) give

\[
 \frac{W\xi}{\eta}=Wm^{-2+o(1)}=o(W),
 \tag{50}
\]

and

\[
 \frac{WK\xi}{g\eta}
 \le WQm^{-2+o(1)}
 =Wm^{-3/2+o(1)}
 =o(W).
 \tag{51}
\]

Thus, for **every possible selected family** \(\mathcal S\), dynamic
quarantine leaves at least a \(1-m^{-1}\) fraction of the original
exponential catalogue in all but \(o(W)\) weighted fibres.  There is no
conditioning or random-residual assumption in this statement.

Within a new tentative bite, reject both endpoints of every newly chosen
bad pair.  The exact residual quantity governing this loss is not the
largest point mass.  It is the weighted bad-edge mass

\[
 \mathscr B_t=
 \sum_{U\ne V}
 \mathbb E_{\substack{P\sim\nu_{t,U}\\E\sim\nu_{t,V}}}
 \mathbf1_{\{PE\in B\}}.
 \tag{52}
\]

The expected number of ordered bad pairs in the tentative bite is exactly
\(\alpha^2\mathscr B_t\).  Deleting both endpoints therefore costs at most

\[
 2g\alpha^2\mathscr B_t
 \tag{53}
\]

in middle-owner weight.  Under the uniform raw catalogue measure,
\(\mathscr B_t\le T\xi\), and (53), summed through
\(R=O(\alpha^{-1}\log\log m)\) bites, is

\[
 O(W\alpha\xi R)
 =Wm^{-3+o(1)}\log\log m
 =o(W).
 \tag{54}
\]

The deterministic quarantine (47)--(51) itself does not require this
uniformity: every candidate retained after quarantine has
width-two intersection with every previously selected chunk, and the raw
catalogue remains exponential rather than \(m^{5/2-o(1)}\).  The hypothesis
needed for current-bite alteration is exactly

\[
 \boxed{g\alpha^2\sum_{t<R}\mathscr B_t=o(W).}
 \tag{55}
\]

This is a genuine improvement over fixed pruning.  It removes all
past/current three-antichain conflicts at negligible raw fibre cost and
removes the fixed polynomial-degree ceiling of Sections 7 and 9.  The
remaining transfer-energy gate (30) now concerns the exponentially large
dynamically quarantined catalogue.  Its unresolved part is precisely the
owner/priority reweighting (which includes the weighted bad-edge mass
(52)), not a raw count of width-three grids.

---

## 11. The transfer term reduces to a hereditary pair-square profile

The companion pair-square calculation in
MATH_ATTACK_CATALOGUE_PAIR_SQUARE_AND_BOWTIE_GATE_20260725.md
sharpens the remaining term.

Let

\[
 K(x,y)=\frac{d(x,y)}{\sqrt{d(x)d(y)}}
 \tag{56}
\]

be the symmetrically normalized target codegree kernel.  For a fixed
protected target \(x\), its raw blockwise squared rows satisfy

\[
 \sum_{\substack{y:|y|=|x|\\y\ne x}}K(x,y)^2=O(m^{-2}),
 \tag{57}
\]

and, at nonzero rank gap \(h\),

\[
 \sum_{|y|=|x|+h}K(x,y)^2
 \le C(|h|+1)^2|h|!(C/m)^{|h|}.
 \tag{58}
\]

The sum of the block \(\ell_2\)-norms is \(O(m^{-1/2})\).  Schur's
test gives operator norm at most \(g\) for every rank-to-rank block.
Consequently the raw bow-tie energy is

\[
 \boxed{
 \mathfrak T(x)=
 \sum_{y,z\ne x}K(x,y)K(y,z)K(z,x)
 =O(g/m)=m^{-1/2+o(1)}.}
 \tag{59}
\]

This is the regular binary specialization of the exact weighted identity
(32c).

Suppose that at unused-resource density \(z\ge1/\log m\), the residual
pair-square blocks obey their ideal inflation:

\[
 \sum_{y\text{ in gap }h}K_z(x,y)^2
 \le Cz^{-2}\times\text{the right side of (57) or (58)}.
 \tag{60}
\]

Then the same Schur argument gives

\[
 \mathfrak T_z(x)\le Cg/(mz^2).
 \tag{61}
\]

At \(z=1/\log m\),

\[
 \mathfrak T_z(x)\log\log m
 \le
 \frac{Cg(\log m)^2\log\log m}{m}
 =o(1).
 \tag{62}
\]

Thus the full degree-covariance martingale closes under (60).  The
weighted transfer energy in (GATE) need not be controlled by an arbitrary
multiple-codegree hierarchy; the following pair-square assertion is
sufficient:

> **Hereditary pair-square theorem.**  Outside weighted \(o(W)\) fibres,
> dynamic quarantine and the priority nibble preserve (60) uniformly down
> to \(z=1/\log m\).

This is strictly narrower than the original residual-degree problem.  Its
one-step kernel is exactly the weighted four-walk (32c).

Four-antichain dynamic quarantine improves the raw bad fraction to
\(m^{-5+o(1)}\) and leaves width-three intersections; its raw exponential
census is also summable.  A fixed four-antichain pruning still leaves only
polynomial degree and fails the entropy test (35).  Hence \(s=4\) improves
the dynamic constants but does not remove the hereditary pair-square
theorem.

---

## 12. Aggressive quarantine preserves switch squares and raw denominators

The tolerance in Proposition 10.1 can be made much smaller than \(m^{-1}\).

For three-antichain quarantine, take

\[
 \eta_3=m^{-12/5}.
 \tag{63}
\]

Since \(\xi_3=m^{-3+o(1)}\), the exceptional tag weight is

\[
 W\xi_3/\eta_3=Wm^{-3/5+o(1)}=o(W),
 \tag{64}
\]

and the exceptional target weight is

\[
 WQ\xi_3/\eta_3=Wm^{-1/10+o(1)}=o(W).
 \tag{65}
\]

For four-antichain quarantine, take

\[
 \eta_4=m^{-4}.
 \tag{66}
\]

Using \(\xi_4=m^{-5+o(1)}\), the corresponding ledgers are
\(Wm^{-1+o(1)}\) and \(WQm^{-1+o(1)}=o(W)\).

Write a good tag fibre as a disjoint union
\(\Omega\times Q_k\), where
\(k=\lfloor M/2\rfloor=\Theta(m)\) are the commuting adjacent switches
and \(\Omega\) contains all other decorations.  Let \(A\) be the
schedules surviving quarantine and put
\(B=(\Omega\times Q_k)\setminus A\).  If
\(|B|\le\eta|\Omega|2^k\), then

\[
 \frac1{|A|}
 \sum_{(\omega,x)\in A}
 \#\{i:(\omega,x\oplus e_i)\in B\}
 \le\frac{k\eta}{1-\eta}.
 \tag{67}
\]

This follows by counting directed cube edges from \(A\) to \(B\) at their
\(B\)-endpoint.

More generally, the fraction of \((\omega,x)\in A\) whose radius-\(r\)
cube ball inside its own \(\omega\)-slice is not wholly contained in \(A\)
is at most

\[
 \frac{\eta}{1-\eta}
 \sum_{j=0}^r\binom kj.
 \tag{68}
\]

Consequently:

* under (63), all but \(m^{-2/5+o(1)}\) of the surviving schedules retain
  their complete radius-two switch neighbourhood;
* under (66), all but \(m^{-1+o(1)}\) retain their complete radius-three
  switch neighbourhood.

In particular, three-antichain dynamic quarantine preserves almost every
commuting switch square.  A square gives all four independent choices of
two affected vertical columns, the exact local object relevant to a
pair-square/four-walk calculation.  Four-antichain quarantine preserves
almost every switch \(3\)-cube.

There is also a direct denominator consequence.  Let
\(d_0(x),d_0(x,y)\) be raw target degrees/codegrees and let
\(d_A(x),d_A(x,y)\) be their values after quarantine.  For nonexceptional
target fibres,

\[
 d_A(x)\ge(1-\eta)d_0(x),
 \qquad
 d_A(x,y)\le d_0(x,y).
 \tag{69}
\]

Therefore

\[
 \boxed{
 \frac{d_A(x,y)}{\sqrt{d_A(x)d_A(y)}}
 \le
 \frac1{1-\eta}
 \frac{d_0(x,y)}{\sqrt{d_0(x)d_0(y)}}.}
 \tag{70}
\]

Every blockwise pair-square sum after quarantine is at most
\((1-\eta)^{-2}\) times its raw value.  Thus dynamic quarantine itself
preserves the pair-square denominator with \(1+o(1)\) loss; it cannot be
the source of a failure of (60).

What (67)--(70) do **not** yet control is the later feasibility weighting

\[
 \mathbf1_{\operatorname{owners}(P)\subseteq\mathcal O_t}\Pi_t(P).
\]

That weighting may delete opposite corners of an otherwise intact raw
switch square.  The hereditary theorem is now reduced further:

> prove that owner/priority conditioning preserves a weighted
> \(1-o(1)\) fraction of the quarantine-intact switch squares, or directly
> prove its pair-square consequence (60).

So the aggressive tolerance gives a genuine lower-degree and local
exchange advance.  It does not, by itself, close the final weighted
conditioning step.

---

## 13. Owner/priority conditioning is a subcube intersected with a down-set

The commuting switches give additional exact structure to the remaining
conditioning.

Fix a tag, its coordinate labelling, its priority order, and every
decoration except the \(k\) switch bits.

For switch bit \(i\), let \(X_i^0,X_i^1\) be its two alternative middle
owners.  All other middle owners are independent of the bit assignment.
Hence the owner-feasible assignments are

\[
 \prod_{i=1}^k A_i,\qquad
 A_i=\{b\in\{0,1\}:X_i^b\text{ is unused}\},
 \tag{71}
\]

provided every fixed owner is unused.  Thus owner conditioning is either
empty or a subcube: a bit is free, forced, or dead.

Restrict to the free bits.  For bit \(i\), let \(r_i^b\) be the first
blocked depth of its alternative vertical column, with \(Q+1\) meaning
unblocked.  Orient the bit so that \(r_i^0\ge r_i^1\); orientation zero is
the better column.  Relative to the all-zero baseline, choosing one adds
one blocker exactly to the deadline prefixes

\[
 r_i^1\le q<r_i^0.
 \tag{72}
\]

The exact feasibility inequalities (8) therefore have the form

\[
 \sum_i a_{i,q}x_i\le s_q,\qquad a_{i,q}\in\{0,1\}.
 \tag{73}
\]

They are monotone in every bit.  Consequently:

\[
 \boxed{\text{the owner-and-priority feasible switch assignments form a
 down-set inside an owner subcube.}}
 \tag{74}
\]

This rules out an arbitrary adversarial residual subset of the native
switch cube.

There is a quantitative square consequence.  Let \(A\subseteq\{0,1\}^f\)
be a nonempty down-set, let \(X\) be uniform on \(A\), put

\[
 s=\log_2|A|,\qquad \mu=\mathbb E|X|,
 \]

and let \(h_2\) be binary entropy.  Downward closure gives
\(\Pr(X_i=1)\le1/2\).  Entropy subadditivity and concavity imply

\[
 s=H(X)\le\sum_i h_2(\Pr(X_i=1))
 \le f h_2(\mu/f).
 \tag{75}
\]

Thus

\[
 \boxed{\mu\ge f\,h_2^{-1}(s/f).}
 \tag{76}
\]

Every one-coordinate descent from \(x\in A\) stays in \(A\), so the
number of internal cube edges is exactly

\[
 |A|\mu.
 \tag{77}
\]

Likewise every pair of one-coordinate descents spans a full lower square,
and convexity gives at least

\[
 \boxed{
 |A|\,\mathbb E\binom{|X|}{2}
 \ge |A|\frac{\mu(\mu-1)}2}
 \tag{78}
\]

anchored switch squares.

The usual cube edge-isoperimetric inequality gives the complementary
boundary statement

\[
 \boxed{
 |\partial A|
 \ge |A|\log_2\frac{2^f}{|A|}
 =|A|(f-s).}
 \tag{79}
\]

Indeed, the number of internal edges of an \(s\)-bit set of size
\(|A|=2^s\) is at most \(|A|s/2\); subtract twice this number from the
total incident degree \(f|A|\).  The same inequality for nonintegral
\(s=\log_2|A|\) follows by the standard induction on \(f\).

Every boundary edge of the actual feasible down-set has a witness in its
toggled vertical column.  If the edge leaves the owner subcube, the
alternative owner is already used.  Otherwise the feasible and infeasible
endpoints differ by one worse first-block column; at the first violated
deadline, that column's first blocked target is a witness.  Thus

\[
 \partial A
 \longrightarrow
 \{\text{used owner/first-block target occurrences in toggled columns}\}.
 \tag{80}
\]

This is an exact charging map (several boundary edges may have the same
physical witness).

Hence any feasible slice with entropy \(s=\Theta(f)\) retains
\(\Theta(f^2)\) switch squares per assignment.  Even for smaller \(s\),
(76) gives the exact square supply.

The missing lower-degree statement can now be phrased as an entropy
statement:

> outside weighted \(o(W)\) slices, the owner/priority feasible down-set
> has enough entropy that the square mass in (78) survives the
> \(m^{-12/5}\) quarantine.

This would imply the local weighted four-walk denominator needed in (60).
No such entropy lower bound is proved here; a slice may in principle be a
small down-set even though other labellings keep the total tag degree
large.  The crude charging bound from (80) is only one unit per
candidate-column occurrence, which is of order \(f\) per candidate and
matches the right side of (79) in the worst case.  Hence cube
isoperimetry alone does not force \(s=f-o(f)\).  To close the argument one
needs a sublinear boundary-witness multiplicity, precisely a dispersal or
pair-square estimate.  Formula (74) is nevertheless a genuine structural
restriction on the final gate.

---

## 14. Only the switches meeting the physical chunk count

There is a bookkeeping correction to Sections 12--13.  Corollary 3.2 of
the deterministic catalogue supplies \(\lfloor M/2\rfloor\) commuting
switches on the **full** \(M\)-phase trajectory.  A single adjacent
switch changes only the intermediate state of its two-step arrival
diamond, and the paths agree at every other state.  Consequently, after
restricting to one emitted geodesic chunk of length \(g\), only

\[
 k_{\rm eff}\le \lceil g/2\rceil+O(1)
 \tag{81}
\]

switches change a physical owner or protected target of that chunk.  The
remaining switches are genuine schedule multiplicities, but their cube
edges and squares have identical physical labels at both endpoints and
cannot support the pair-square denominator.

All aggressive-quarantine conclusions remain valid, with more room.  In
(68) one should use \(k_{\rm eff}=O(g)\) for physically useful balls.
Thus

\[
 \eta_3 k_{\rm eff}^2
 \le m^{-12/5}g^2=o(1),
 \qquad
 \eta_4 k_{\rm eff}^3
 \le m^{-4}g^3=o(1).
 \tag{82}
\]

So almost every surviving chunk still has every physically relevant
switch square under three-antichain quarantine and every physically
relevant switch cube under four-antichain quarantine.  What must not be
used is the artificial \(\Theta(m^2)\) supply of squares involving two
switches lying wholly outside the chunk.

---

## 15. Dense feasible down-sets have almost uniform local label cells

The entropy statement can be sharpened in the exact form needed by the
adjacent-switch labels.

Let \(A\subseteq Q_f\) be a nonempty down-set, let \(X\) be uniform on
\(A\), and write

\[
 \rho=|A|2^{-f}=2^{-b},\qquad
 p_i=\Pr(X_i=1),\qquad
 p_{ij}=\Pr(X_i=X_j=1).
 \tag{83}
\]

Put

\[
 R=\sqrt{(\ln2)fb/2}.
 \tag{84}
\]

### Proposition 15.1 (one- and two-cell regularity)

For every down-set \(A\),

\[
 p_i\le\frac12,
 \qquad
 p_{ij}\le\frac14,
 \tag{85}
\]

and

\[
 \boxed{
 \sum_i\left(\frac12-p_i\right)\le R.}
 \tag{86}
\]

Moreover,

\[
 \boxed{
 \sum_{i<j}\left(\frac14-p_{ij}\right)
 \le \frac f8+\frac{fR}{2}.}
 \tag{87}
\]

If \(p_{ij}^{ab}=\Pr(X_i=a,X_j=b)\), then

\[
 \boxed{
 \sum_{i<j}\sum_{a,b\in\{0,1\}}
 \left|p_{ij}^{ab}-\frac14\right|
 \le C(f+fR).}
 \tag{88}
\]

In particular, if \(b=o(f)\), the average one-bit marginal is
\(1/2-o(1)\) and the average two-bit cell distribution is
\(1/4-o(1)\) in total variation.

#### Proof

Every section of a down-set in one coordinate is either empty, a
singleton containing zero, or the full two-point fibre.  Pairing the
points in full fibres proves \(p_i\le1/2\).  Similarly, whenever a point
with \((X_i,X_j)=(1,1)\) occurs, its complete lower two-dimensional
square also lies in \(A\).  These squares are disjoint after fixing all
other coordinates, so \(p_{ij}\le1/4\).

The entropy calculation (75)--(76), together with
\(1-h_2(1/2-u)\ge2u^2/\ln2\), gives

\[
 \mu:=\sum_ip_i\ge f/2-R,
\]

which is (86).  Downward closure gives

\[
 \sum_{i<j}p_{ij}=\mathbb E\binom{|X|}{2}
 \ge\frac{\mu(\mu-1)}2.
\]

Subtracting this from \(\binom f2/4\), and using \(\mu\ge f/2-R\),
gives (87) after discarding a negative \(-R^2/2\) term.

Write

\[
 \delta_i=\frac12-p_i,\qquad
 e_{ij}=\frac14-p_{ij}.
\]

Then the four cell deviations are

\[
 -e_{ij},\quad e_{ij}-\delta_i,\quad
 e_{ij}-\delta_j,\quad
 \delta_i+\delta_j-e_{ij}.
\]

Their absolute sum is at most
\(4e_{ij}+2\delta_i+2\delta_j\).  Sum this inequality and use
(86)--(87) to obtain (88).  \(\square\)

For an active adjacent switch, Corollary 3.2 says that every protected
row changes at exactly one intermediate phase and agrees everywhere
else.  Therefore, in one fixed outer schedule slice, the incidence
indicator of a physical target is either constant, zero, or a one-bit
dictator.  Simultaneous row injectivity prevents the same physical target
from being two different dictator labels in that slice.  Likewise, a
pair of physical target labels depends on at most two switch bits.

It follows from (86)--(88) that, inside every slice with
\(b=o(f)\), owner/priority conditioning changes the aggregate one-target
and two-target occurrence tables from their uniform-switch values by only

\[
 O\!\left(\sqrt{b/f}+1/f\right)
 \tag{89}
\]

in normalized \(\ell_1\) mass.  This conclusion is label-aware: it
applies after pushing the bit cells forward to their actual Boolean
target labels.

This removes arbitrary **within-slice** concentration from the final
gate.  Write \(\omega\) for all decorations outside the physically active
switch bits and

\[
 \rho_\omega=|A_\omega|/2^{f_\omega}.
 \tag{90}
\]

Replace each feasible down-set temporarily by the uniform fractional
weight \(\rho_\omega\) on its full switch cube.  Proposition 15.1 shows
that, on all dense large-dimensional slices, this replacement changes
the target and target-pair tables by weighted \(o(1)\) in aggregate.
The exact remaining term is therefore the outer scalar-slice kernel

\[
 \boxed{
 d_\rho(x,y)=
 \sum_\omega\rho_\omega d^0_\omega(x,y),
 \qquad
 d_\rho(x)=
 \sum_\omega\rho_\omega d^0_\omega(x).}
 \tag{91}
\]

One must prove that the dynamically generated scalar weights
\(\rho_\omega\) preserve the raw blockwise pair-square profile, outside
weighted \(o(W)\) target fibres.  Thus the cross-slice term can be
narrowed once more:

\[
 \boxed{
 \text{the unresolved concentration is in the scalar outer-slice
 weights, not in the switch-cell distribution inside a dense down-set.}}
 \tag{92}

The still-unproved hypotheses are that almost all size-biased active
slices have \(f_\omega\to\infty\) and \(b_\omega=o(f_\omega)\), and that
the scalar kernel (91) has the required dispersal.  Proposition 15.1 does
not assert either hypothesis, but it eliminates one whole layer of the
weighted four-walk problem.

There is a sharper consequence for the affine two-moment dispersal
theorem.  Give the anchored lower square in directions \(i,j\) its
normalized weight

\[
 w_\omega(i,j)=p_{ij}
 =\Pr(X_i=X_j=1).
 \tag{93}
\]

By (85), \(w_\omega(i,j)\le1/4\) pointwise.  By (87), when
\(b=o(f)\),

\[
 \sum_{i<j}w_\omega(i,j)
 =(1-o(1))\binom f2/4.
 \tag{94}
\]

Consequently

\[
 \boxed{
 \max_{i<j}w_\omega(i,j)
 \le (1+o(1))
 {\sum_{i<j}w_\omega(i,j)\over \binom f2}.}
 \tag{95}
\]

up to an absolute constant (the displayed \(1+o(1)\) may be replaced by
two uniformly).  This is exactly the pointwise direction-pair condition
needed to apply the affine cross-slice collision count to the
nonuniform down-set weights.  Thus the former inverse-degree replacement
bridge disappears for the anchored-square main term.

Combined with the affine two-moment theorem, the scalar kernel in (91)
has cross-slice collision factor \(m^{-1+o(1)}\) provided that, on almost
all size-biased mass,

\[
 f_\omega=p\,m^{-o(1)},
 \qquad b_\omega=o(f_\omega),
 \tag{96}
\]

and provided the affine-base switch-orbit retains the calibrated fibre
degrees.  Therefore the remaining affine-switch gate is now (96) plus
that degree audit; arbitrary scalar outer-slice weights themselves are no
longer an obstruction once these hypotheses hold.
