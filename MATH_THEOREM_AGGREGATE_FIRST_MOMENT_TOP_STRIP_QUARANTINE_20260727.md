# Conditional aggregate top-strip quarantine and the joint-hazard gate

Date: 2026-07-27

Scope: constant-one repaired promotion-ring slow-greedy hierarchy.

## Superseding status correction

The hereditary ordered-tower route audited below is refuted as an
unconditional proof.
MATH_THEOREM_FIRST_MOMENT_GRADED_TOP_STRIP_ADDITIVE_CLOSURE_AND_ROOT_QUARANTINE_20260727.md
proposes a different additive-child repair.  It is conditional on a
hereditary stopped one-row edge/coin path-mesh input through the enlarged
order and on the non-disjoint column-intersection extension used for the
absolute child.  Until those inputs are proved, it is a sufficient
criterion, not a closure theorem.  The ordered-tower argument below is
retained only as a refuted/conditional record.

The theorem-level audit, corrected additive reserve, soft-quarantine
proof, and exact marked cross-prefix gate are in
MATH_AUDIT_TOP_STRIP_FIRST_MOMENT_AND_NONCASCADING_QUARANTINE_20260727.md.

## Independent joint-hazard audit

The theorem below is not currently unconditional.  If the reference
contains prefix survival, terminal prefix death cannot be discarded by
the sign argument.  For the equality-resolved prefix resource union
$P_C$ and the genuinely new last-row resources
$R_C(f)=V(f)\setminus P_C$, the exact identity is

\[
 \Lambda_t(P_C\cup R_C(f))
 =\Lambda_t(P_C)+\Lambda_t(R_C(f))
 -\nu_t|\mathcal E_t(P_C)\cap\mathcal E_t(R_C(f))|.             \tag{JH}
\]

The negative prefix-death term cancels the prefix-survival derivative
of the base.  The last term in (JH) is positive and is the exact
cross-prefix hazard.  A regular compensated hypergraph example in
`MATH_AUDIT_AGGREGATE_TOP_STRIP_PREFIX_JOINT_HAZARD_20260727.md`
has its integrated value equal to $\log(1/z)$; hence marginal
compensation and $\mathsf K_C\le0$ do not imply uniform integrated
$o(1)$.

The pair-column reduction in Section 2 can represent this term, but three
further assertions are required:

1. every prefix-terminal event must be included through its exact
   equality-resolved union deficit, rather than discarded; and
2. the ordered extension family must allow a pair endpoint on a
   protected prefix column as well as on a formal row arm.  A selected
   event meeting a protected column and the last row is a
   column--row/column--column overlap, not one of the resource-disjoint
   row-arm pair columns currently covered by Lemma 1.1; and
3. Lemma 1.1 must be supplied with an all-order or hereditary
   initialization.  The proved endpoint estimate for an ordered tower
   of length $j$ has parameter $s+j$, so the fixed bound
   $\alpha^{s+j}$ is presently certified only for
   $s+j\le L_{\rm pm}$.  Fine analytic slabs do not by themselves
   regenerate the missing higher tower at each slab start.

Accordingly, the ordered-tower proof in Sections 3--8 is conditional on
a hereditary all-order estimate for the full equality-resolved resource
union.  There is a weaker possible replacement: an absolute
current-residual bound of size
$CL^{C_0}\alpha^{s+1}Y_\tau(t)$ for the resource-nondisjoint
prefix--last-row child would close by one-step Duhamel, since
$TL^{C_0}\alpha=o(1)$.  That bound is denoted ACH in
`MATH_AUDIT_AGGREGATE_TOP_STRIP_PREFIX_JOINT_HAZARD_20260727.md`; it is
not supplied by the presently cited pairwise resource-disjoint static
diagram theorem.

## 0. Theorem and correction

Let \(k=(1+o(1))m\) be the number of owner resources in one repaired
edge, let

\[
 L=C_1(\log m)^2,\qquad J=C_0\log m,\qquad
 s_*=\left\lfloor{L-2\over4}\right\rfloor+1,
\tag{0.1}
\]

and run only while the common survivor density is at least

\[
                         z=m^{-1/20}.
\tag{0.2}
\]

Write

\[
 \alpha=
 \max\{\alpha_E,\alpha_\circ\}
 \le {CL^4\over m^2z^2}
 =m^{-19/10+o(1)}.
\tag{0.3}
\]

Here \(\alpha_E\) and \(\alpha_\circ\) are respectively the proved
edge-column and compensation-resource endpoint factors in the
arbitrary mixed-diagram theorem.  Thus compensation is included in
\(\alpha\); no inference of the coin endpoint from the edge influence
is made.

For every compressed mixed type \(\tau\) of excess
\(s_*\le s\le L\), let \(Z_{\tau,X}(t)\) be its current count at center
\(X\), and let \(B_{\tau,X}(t)\) be its complete current first-moment
base, including degrees, private-column exponential factors, and
survivor densities, but excluding \(\alpha^s\).

Let

\[
 \mathfrak I_O(t)=kE_{\rm ref}(t),\qquad
 \mathfrak I_R(t)=E_{\rm ref}(t)
\tag{0.3a}
\]

be the deterministic owner- and root-incidence references on the
degree-stopped core.  Actual incidences are within \(1+o(1)\) of these
values.

Then the following statements hold up to the already established
degree stopping time.

1. **Aggregate first moment.**  Subdivide the trajectory into
   first-moment reference slabs on which the common catalogue degree
   \(D_t\), and hence total incidence \(kE_t\), changes by at most a
   fixed factor.  Every \(B_{\tau,X}(t)\) is still transported exactly
   inside the slab.  Uniformly through such a slab,

   \[
   \mathbb E\left[
   {1\over\mathfrak I_O(t)}
   \sum_Xd_t(X){Z_{\tau,X}(t)\over B_{\tau,X}(t)}
   \right]
   \le e^{o(1)}C_\tau\alpha^s.
   \tag{0.4}
   \]

   Here the deterministic logarithmic derivative of
   \(\mathfrak I_O(t)\) is included in the transported base, and

   \[
                         C_\tau\le\exp[Cs\log(s+1)].
   \tag{0.5}
   \]

   The same estimate holds maximally after stopping and for the
   root-incidence lift, using \(\mathfrak I_R(t)\).

2. **Top-strip quarantine.**  Stop monitoring an owner \(X\) when

   \[
   \sum_{s=s_*}^{L}\ \sum_{\tau\in\mathcal T_s}
       \alpha^{-s/2}{Z_{\tau,X}(t)\over B_{\tau,X}(t)}>1.
   \tag{0.6}
   \]

   With probability \(1-o(1)\), the total normalized stopped owner
   incidence satisfies

   \[
       \sum_{X\ {\rm stopped}}
       {d_{\tau_X}(X)\over\mathfrak I_O(\tau_X)}
       \le\beta,\qquad
       \beta=\exp[-c(\log m)^3].
   \tag{0.7}
   \]

   The root-centered version has the same statement with
   \(d_{\tau_R}(R)/\mathfrak I_R(\tau_R)\).  There are

   \[
                         C_{\rm cp}=O(m\log m)
   \tag{0.7a}
   \]

   such fine slabs.  Their polynomial number is absorbed by decreasing
   \(c\).  The coarser graded-moment checkpoints need not be changed.

3. **No cascade.**  The quarantine in (0.6) is analytical: stopped
   centers are no longer monitored, but their incident catalogue edges
   are not recursively removed.  If a literal cleaned core is wanted,
   remove only the primary bad-owner edges once and put

   \[
                         \eta=\sqrt{C_{\rm cp}\beta k},
   \tag{0.8}
   \]

   where \(C_{\rm cp}=O(m\log m)\) is the number of first-moment
   reference slabs.  Roots
   losing more than an \(\eta\)-fraction of their degree number at most

   \[
                         \eta N_H=o(N_H).
   \tag{0.9}
   \]

   Owners losing more than an \(\eta\)-fraction are added only to the
   analytical exception set; their remaining stars are not deleted.
   Their total owner mass is \(o(W)\).  Hence there is one cleaning
   generation and no suppression cascade.

Conditional on the audited cross-prefix and hereditary tower estimates,
the first-moment top strip would be closed.  Together with the proved
graded moments

\[
                         q(2s+1)\le L,
\tag{0.10}
\]

there would then be no remaining formal outer boundary in the finite
excess hierarchy.

The fine subdivision is purely analytic.  It asks for no additional
moment: stop a slab whenever the deterministic current reference degree
has changed by a factor two.  Since the logarithm of a repaired-ring
degree is \(O(m\log m)\), (0.7a) suffices.

Two points correct the former draft.  First, a random factor \(d_t(X)\)
cannot simply be multiplied into a local supermartingale; it must be
realized as a marked live incidence.  Second,
\(o(E_t/m)\) is not the same as \(o(N_H)\), because
\(E_t=N_tD_t\).  Section 6 gives the required division by the current
root degree and the noncascading ledger.

## 1. Fixed-row ordered extension tower

Private degree-one columns have already been summed by the proved
exponential generating function.  A top-strip core of excess \(s\)
has at most \(2s\le2L\) formal core incidences and at most \(2L\)
formal row arms after equality compression.

Fix a type \(\tau\).  For \(j\ge0\), let
\(\mathcal E_j(\tau)\) be the family obtained by adjoining an ordered
list of \(j\) **pair columns**.  A pair column is either

1. one selected-edge column with two owner-witness incidences assigned
   to two formal row arms, allowing the two arm labels to agree when the
   selected edge has two witnesses on one physical row; or
2. one compensation-resource column common to two displayed arms.

All endpoint colors, row equalities, and physical witness coincidences
are retained.  Let \(Z_{\tau,j,X}\) be the aggregate count over
\(\mathcal E_j(\tau)\), normalized by its full first-moment base but
not by an excess factor.  Thus \(Z_{\tau,0,X}=Z_{\tau,X}/B_{\tau,X}\).

### Lemma 1.1 (static ordered tower, certified range)

Let $L_{\rm pm}$ be the largest total witness order for which the
joint path-mesh maximum and internal census have been certified.  At a
reference-slab start, for $s+j\le L_{\rm pm}$,

\[
 \boxed{
 \sum_Xd(X)Z_{\tau,j,X}
 \le C_\tau\,\alpha^{s+j}\sum_Xd(X)
 \qquad(s+j\le L_{\rm pm}).}
\tag{1.1}
\]

The same statement holds with a marked root incidence.  Extension to
every $j$, and hereditary reinitialization at later slab starts, are
additional assertions rather than consequences of static row
exploration.

#### Proof

Use the proved row-exploration theorem on the base type \(\tau\).
An adjoined pair column has one free incidence.  After its first arm is
fixed, its second arm is exactly one edge-column or resource-column
endpoint constraint.  It therefore costs at most
\(\max(\alpha_E,\alpha_\circ)\le\alpha\).

There are at most \(O(L^2)\) choices of its two formal arms and only a
constant number of edge/coin colors and orientations.  These choices,
the witness-order choices, and the \(u^{-2}\) conditioning loss are
already covered by the factor \(CL^4/(m^2z^2)\) in (0.3).

Explore the ordered pair columns successively while retaining their
physical disjointness.  Row exploration gives one endpoint factor per
added column, but its envelope depends on total exposed order $s+j$.
Hence the fixed factor $CL^4/(m^2z^2)$ proves (1.1) only in the
displayed certified range.  Dropping disjointness and then invoking the
disjoint path-mesh estimate would be invalid.

To obtain the factor \(d(X)\) literally, mark one additional current
catalogue edge through \(X\).  The marked edge is another displayed
arm with no imposed new excess.  Row exploration still has at most
\(2L+1\) arms, so the same \(CL^4\) envelope applies.  This is the
marked-incidence lift; no random external weight is inserted after the
count.  The root case is identical and its endpoint counts are smaller.
\(\square\)

An assertion for every $j$ is an all-order static catalogue theorem.
The time-order simplex in Section 3 supplies factorial coefficients, but
does not itself bound the initial high-$j$ catalogue or regenerate it
at the next slab start.

## 2. Exact pair domination of first-moment drift

Consider one displayed configuration after private columns have been
summed.  Resolve all physical resource equalities first and let $U$ be
the union of the protected columns, the previously adjoined pair
columns, and the formal row arms.  For each event $g$, let $t_g$ be
the number of distinct marginal survival factors in the current base
whose equality-resolved resource sets are hit by $g$.  The exact
normalized union-hazard correction of $g$ is

\[
                         (t_g-1)_+.                             \tag{2.0}
\]

This includes events meeting a protected column.  Their negative
terminal contribution cancels the protected-column survival derivative
in the base; only after this cancellation may the remaining common-event
deficit be bounded above.  Discarding such an event before subtracting
the base derivative is invalid.

For (2.3) to follow, $\mathcal E_{j+1}(\tau)$ must therefore contain
pair columns whose two endpoints range over **all** equality-resolved
marginal survival factors in $U$, including a protected prefix column
and a last-row resource.  The present definition in Section 1 assigns
both selected-edge witnesses to formal row arms and does not prove the
required column--row or column--column endpoint estimate.

For a selected edge \(g\), put \(t=t_g\).  Replacing its distinct
physical resource hits by their displayed witness incidences only
enlarges this value and automatically includes multiple intersections
with one row or protected column.  The difference between the sum of
the \(t\) marginal resource hazards and their union hazard is

\[
                         (t-1)_+\le\binom t2.
\tag{2.1}
\]

Every pair on the right side of (2.1) is precisely one selected-edge
pair column.  Its two witness incidences may lie on two different rows
or twice on one row.  Shared physical witnesses and all higher
intersection multiplicities are expanded by the already proved
binomial-inversion and equality-partition mixed types.

If a compensation coin at \(y\) deletes \(t\) equality-resolved
marginal resource factors, the same identity applies.  The marginal
reference counts $y$ once on each such factor; the actual coin rings
once.  Each pair in (2.1) is one compensation-resource pair column.

Thus a first-moment generator step needs only a degree-two new column,
regardless of \(t\).  In particular it raises excess by exactly one.
This is stronger than the general replicated estimate
\(q(2s+1)\): it uses the linear union-deficit identity special to
\(q=1\).

Let

\[
 F_{\tau,j}(t)=\sum_Xd_t(X)Z_{\tau,j,X}(t)
\tag{2.2}
\]

with the marked-incidence interpretation from Lemma 1.1.  Transport by
the exact current first-moment bases and by the harmless degree error.
Then the stopped generator satisfies

\[
 \boxed{
 \mathcal G\widetilde F_{\tau,j}(t)
 \le \kappa(t)\widetilde F_{\tau,j+1}(t),
 \qquad \int_{t_0}^{t_1}\kappa(t)\,dt\le C(t_1-t_0).}
\tag{2.3}
\]

Here

\[
 \widetilde F_{\tau,j}(t)=
 \exp\left[-\int_{t_0}^t\epsilon_\tau(v)\,dv\right]
 F_{\tau,j}(t),
\tag{2.4}
\]

and the already proved first-order degree/internal-overlap comparison
gives, uniformly for at most \(2L+1\) arms and after summing over all
reference slabs,

\[
 \int_0^T\sup_\tau|\epsilon_\tau(v)|\,dv
 \le {CL^4\log m\over m}=o(1).
\tag{2.5}
\]

#### Justification of (2.3)

Private \(t=1\) event columns are exactly the logarithmic derivative of
the current base.  Terminal deletion is favorable.  Every remaining
positive common-event multiplicity is bounded by (2.1), and summing its
pairs gives \(F_{\tau,j+1}\).  The free incidence of the new event
column cancels its edge-clock or coin-clock normalization:

\[
 {1\over k\Delta_t}\,(K\Delta_t)=O(1),
 \qquad
 {1\over k}\,K=O(1).
\tag{2.6}
\]

What remains is a bounded \(\kappa(t)\).  The edge and coin endpoint
colors have already been combined in \(\alpha\).

The marked edge used for \(d_t(X)\) is part of the displayed
configuration.  Its death is favorable, and a common event involving it
is again one of the pairs in (2.1).  Hence (2.3) applies to the marked
aggregate itself.  This is the step missing from an argument which
multiplies a local supermartingale by \(d_t(X)\) after the fact.

## 3. Backward first-moment potential

Fix a reference slab \([t_0,t_1]\) and put

\[
                         A(t)=\int_t^{t_1}\kappa(v)\,dv.
\tag{3.1}
\]

Define

\[
 \Phi_\tau(t)=
 \sum_{j\ge0}{A(t)^j\over j!}\widetilde F_{\tau,j}(t).
\tag{3.2}
\]

This series is finite in the physical catalogue; monotone convergence
also permits the displayed infinite notation.

Since \(A'(t)=-\kappa(t)\), (2.3) gives

\[
\begin{aligned}
 \mathcal G\Phi_\tau
 &\le
 \sum_{j\ge0}{A^j\over j!}\kappa\widetilde F_{\tau,j+1}
 -
 \sum_{j\ge1}{\kappa A^{j-1}\over(j-1)!}
       \widetilde F_{\tau,j}\\
 &=0.
\end{aligned}
\tag{3.3}
\]

Thus \(\Phi_\tau\) is a nonnegative stopped supermartingale and
\(\Phi_\tau(t)\ge\widetilde F_{\tau,0}(t)\).

By Lemma 1.1,

\[
\begin{aligned}
 \mathbb E\Phi_\tau(t_0)
 &\le
 C_\tau\alpha^s\sum_Xd_{t_0}(X)
 \sum_{j\ge0}{(A(t_0)\alpha)^j\over j!}\\
 &=
 C_\tau\alpha^s
 \exp[A(t_0)\alpha]\sum_Xd_{t_0}(X).
\end{aligned}
\tag{3.4}
\]

Over the entire trajectory,

\[
 A(t_0)\alpha
 \le CT\alpha
 =O\left(m^{-9/10}(\log m)^9\right)=o(1).
\tag{3.5}
\]

Equations (2.5), (3.3), and (3.4) prove (0.4).  More importantly,
Doob's maximal inequality applies to \(\Phi_\tau\).  No moment above
the first is used in the top strip.

The ordered static tower and the time-simplex factorial in (3.2) are
both essential.  A finite buffer would expose an uncontrolled last
term; a raw monotonicity argument would lose
\(\exp[-\Theta(m)]\) of reference density in one checkpoint.

## 4. Simultaneous top-strip score

Core compression and the proved equality-partition enumeration give

\[
                         |\mathcal T_s|
 \le\exp[Cs\log(s+1)].
\tag{4.1}
\]

For one center \(X\), define its stopped score

\[
 \mathcal S_X(t)=
 \sum_{s=s_*}^{L}\ \sum_{\tau\in\mathcal T_s}
 \alpha^{-s/2}{Z_{\tau,X}(t)\over B_{\tau,X}(t)}.
\tag{4.2}
\]

Sum the marked potentials
\(\alpha^{-s/2}\Phi_\tau\) over all \(s,\tau\), and stop the marked
center when \(\mathcal S_X\) first exceeds one.  At that crossing the
potential carries at least the current marked incidence \(d_t(X)\).
Therefore

\[
 \mathbb E I_Q
 \le e^{o(1)}
 \left[
 \sum_{s=s_*}^{L}
 \exp[Cs\log(s+1)]\alpha^{s/2}
 \right]kE_{t_0}.
\tag{4.3}
\]

Since

\[
 \log(1/\alpha)=\left({19\over10}+o(1)\right)\log m
\tag{4.4}
\]

and \(s_*=L/4+O(1)\), the bracket in (4.3) is

\[
 \beta_0\le\exp[-c_0L\log m]
 \le\exp[-c_1(\log m)^3].
\tag{4.5}
\]

Markov's inequality at level \(\beta_0^{1/2}kE_{t_0}\) gives failure
probability at most \(\beta_0^{1/2}\).  Rename
\(\beta=\beta_0^{1/2}\); it still has the form in (0.7).
Summing over \(C_{\rm cp}=O(m\log m)\) reference slabs only changes
\(c\).

The root-incidence lift gives identically

\[
                         I_Q^R\le\beta E_{t_0}.
\tag{4.6}
\]

This proves the aggregate stopped quarantine, not merely a pointwise
expectation.

## 5. Why analytical quarantine does not cascade

When \(X\) crosses (0.6), stop only the observables centered at \(X\).
Do not suppress its incident catalogue edges during the stochastic
trajectory.

This is legitimate for two reasons.

1. A good center's generator is controlled by its own ordered extension
   tower.  It does not assume that edges through stopped centers have
   disappeared.
2. If the same concentration later appears at another center, that
   center contributes its own marked incidence to (4.3).  The aggregate
   supermartingale already charges it.

Thus analytical quarantine changes no degree, creates no compensation
coin, and has literally zero suppression cascade.

At the terminal matching, if the application does not trust selected
edges containing a quarantined owner, discard those selected edges once.
On the degree-stopped core, \(d_t(X)\ge cD_t\) at every crossing.
Grouping crossings by reference slab gives

\[
 |Q_O|
 \le \sum_{\rm cp}{I_Q^{O}\over cD_t}
 \le C_{\rm cp}\beta kN_H=o(N_H),
\tag{5.1}
\]

because \(\beta k\log m=o(1)\).  Directly quarantined roots satisfy

\[
                         |Q_R|
 \le C_{\rm cp}\beta N_H=o(N_H).
\tag{5.2}
\]

A matching edge contains only one root.  Assign every discarded
selected edge to one quarantined owner which it contains, or to its
quarantined root.  Therefore the number of discarded roots is at most

\[
 |Q_O|+|Q_R|=o(N_H).
\tag{5.3}
\]

The corresponding additional owner leave is at most

\[
 k(|Q_O|+|Q_R|)
 =O(C_{\rm cp}\beta k^2N_H)=o(W),
\tag{5.4}
\]

since \(W=(1+o(1))kN_H\) and
\(\beta k\log m=o(1)\).

No star is removed and no second generation is formed.

## 6. Optional one-generation literal cleaning

Some consumers require a literal current subcatalogue rather than an
analytical exception list.  Suppress all edges incident with the
primary owner set \(Q_O\), but do this only once.  In one reference slab the
number of removed edges is at most

\[
                         F\le I_Q^O\le\beta kE_t.
\tag{6.1}
\]

Let \(\ell_R\) and \(\ell_X\) be the root- and owner-degree losses caused
by these \(F\) edges.  Then

\[
 \sum_R\ell_R=F,\qquad
 \sum_X\ell_X=kF.
\tag{6.2}
\]

Assume the stopped core degrees are between \(cD_t\) and \(CD_t\), and
write \(E_t=(1+o(1))N_tD_t\).  Put

\[
                         \eta=\sqrt{C_{\rm cp}\beta k}.
\tag{6.3}
\]

The roots with \(\ell_R>\eta D_t\) number at most

\[
 {F\over\eta D_t}
 \le {\beta k\over\eta}N_t.
\tag{6.4}
\]

After all reference slabs their union has size at most

\[
 {C_{\rm cp}\beta k\over\eta}N_H
 =\eta N_H=o(N_H).
\tag{6.5}
\]

Similarly, owners with \(\ell_X>\eta D_t\) have total cardinality at
most

\[
 {kF\over\eta D_t}
 \le {\beta k^2\over\eta}N_t.
\tag{6.6}
\]

Relative to \(W=(1+o(1))kN_H\), their total mass over all reference
slabs is
at most

\[
 {C_{\rm cp}\beta k\over\eta}W
 =\eta W=o(W).
\tag{6.7}
\]

Add these owners only to the analytical exception list.  Do **not**
suppress their remaining stars.  Every unexceptional root and owner
loses at most an \(\eta\)-fraction of its reference degree, which is
absorbed by the next slab's ordinary degree tolerance.

This is the promised noncascading cleaning: primary bad-owner stars are
removed once, high-loss roots are charged, and secondary high-loss
owners are stopped but do not generate another removal wave.

## 7. Interface with the graded stochastic core

For \(s<s_*\), the proved choice

\[
 q(s)=\min\left\{J,
          \left\lfloor{L\over2s+1}\right\rfloor\right\}
\tag{7.1}
\]

has \(q(s)\ge2\), and the replicated diagram remains below the ceiling
\(L\).  For \(s\ge s_*\), Sections 1--4 give the first-moment envelope
and aggregate maximal quarantine.

The score threshold implies, on every unquarantined center,

\[
 {Z_{\tau,X}(t)\over B_{\tau,X}(t)}
 \le\alpha^{s/2}.
\tag{7.2}
\]

At the entrance to the top strip,

\[
 \alpha^{s/2}
 \le\alpha^{L/8+O(1)}
 =\exp[-\Omega((\log m)^3)].
\tag{7.3}
\]

This is smaller than the checkpoint failure budget, the cumulative
degree tolerance, and both leave ledgers.  No square, \(J\)-th moment,
or scalar outer-flux hypothesis is used above the graded ceiling.

## 8. Status

Used as proved inputs:

1. arbitrary static mixed diagrams by row exploration, including the
   edge/coin colors, equality partitions, and private-column
   exponential generating function;
2. the exact excess increment and the graded
   \(q(2s+1)\le L\) moment theorem;
3. the exact compensated first-moment reference and the ordinary degree
   stopping estimates.

Conditional on the joint-hazard/hereditary all-order tower estimates,
first-moment high-incidence events reduce to ordered pair columns and
the backward tower (3.2) absorbs all orders beyond the top strip.
Alternatively, ACH supplies the first moment directly by one-step
Duhamel.  Under either conditional route:

1. aggregate incidence mass remains \(O(\alpha^s)\);
2. maximal top-strip quarantine has
   \(\exp[-\Omega((\log m)^3)]\) incidence;
3. analytical quarantine has no cascade; and
4. optional literal cleaning costs \(o(N_H)\) roots and \(o(W)\)
   owners in one generation.

Thus the quarantine and cleaning ledgers are valid conditional
consequences, but the first-moment graded top strip remains open until
either XPH with its ordered-tower boundary, or the weaker
resource-nondisjoint absolute child estimate ACH, is proved in the
repaired-ring process.
