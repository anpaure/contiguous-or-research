# Independent audit: heptagonal cap/history product monoid and backup tickets

**Date:** 2026-08-02  
**Audited note:**
`MATH_THEOREM_K_HEPTAGONAL_CAP_HISTORY_PRODUCT_MONOID_AND_REGENERATIVE_SELECTOR_GATE_20260802.md`  
**Verdict:** the literal cap-prefix monoid, physical global-slack theorem,
and conditional greedy implication are correct.  Two scope corrections are
load-bearing: shortened cap orbits require stabilizer weights (or a literal
physical expansion), and the two-polarity pivot entrance is an admissible
joint bi-history domain, not an unrestricted Cartesian product.  The exact
same-cap boundary-ticket condition additionally includes endpoint
present/absent consistency.

## 1. Cap-prefix monoid: PASS

For a literal cap `U`, let the atomic signed changes be
`delta_1(U),...,delta_t(U)` and put

\[
 Z_p(U)=\sum_{j\le p}\delta_j(U),\qquad
 b(U)=-\min_{0\le p\le t}Z_p(U).                       \tag{1.1}
\]

An initial load `1+s(U)` remains positive after every prefix exactly when
`s(U)>=b(U)`.  If `A` precedes `B`, prefixes of `AB` are the prefixes of
`A` and the vectors `Delta_A+Z_p^B`, so

\[
 \Delta_{AB}=\Delta_A+\Delta_B,
 \qquad
 b_{AB}=\max\{b_A,b_B-\Delta_A\}.                      \tag{1.2}
\]

This independently rederives Proposition 1.2 and proves associativity.
For one simultaneous atom, `b=(-delta)_+`; since the signed total is zero,

\[
 \sum_U b(U)=\frac12\|\delta\|_1.                      \tag{1.3}
\]

The result is exact for literal physical caps.  Requiring every conceptual
submove of a simultaneous circuit to preserve support can create a larger,
artificial prefix bank; the theorem correctly treats the chosen atomic
packet decomposition as part of the state.

## 2. Theorem 2.1: physical statement PASS

For `k=2r-1`, a degree-two factor on

\[
                         W={2r-1\choose r}
\]

has exactly `W` edges.  Rank-`(r+1)` cap completeness consumes one baseline
copy of each of

\[
 {2r-1\choose r+1}=W\frac{r-1}{r+1}
\]

caps.  Hence the exact physical repeat mass is

\[
                         W-W\frac{r-1}{r+1}
                         =\frac{2W}{r+1}.               \tag{2.1}
\]

For a fixed cap `U`, its `r+1` rank-`r` subsets are the only possible
endpoints of edges with union `U`.  Their degrees inside the selected
factor are at most two, so at most `r+1` selected edges have cap `U`.
Thus one cap carries at most `r` repeat units, and at least

\[
                   \left\lceil\frac{2W}{r(r+1)}\right\rceil
                                                                  \tag{2.2}
\]

caps have positive slack.  This proves the displayed theorem (with the
ceiling understood because the left side is integral).

At `r=9`, (2.1) is `4862`; dividing by seventeen on the free `Z_17` face
gives quotient repeat mass `286`, and (2.2) gives at least
`ceil(286/9)=32` repeated quotient caps.  The later authenticated terminal
ledger

\[
                       1^{984}2^{97}3^3 4^{57}5^3
\]

indeed has `160` repeated quotient caps.  This finite number comes from the
terminal-factor audit, not from the local heptagon theorem alone.

### Required quotient correction

The phrase “for a free equivariant action the same statements divide by the
orbit size” is valid only when the owner, edge, and cap resources being
compressed have the same free orbit size.  In general the rank-`r` owner
action can be free while a rank-`(r+1)` cap has a stabilizer.  Then one
quotient edge orbit can contribute several copies to each physical cap in a
short cap orbit.

Accordingly Sections 1--2 must use one of the following conventions.

1. Work throughout with literal physical caps; or
2. give each cap orbit `O` its physical size `w_O`, define `M(O)` as the
   common per-cap load, and use the weighted equations

   \[
       \sum_O w_O\delta(O)=0,
       \qquad
       \sum_Ow_O(M(O)-1)=\text{physical repeat mass}.   \tag{2.3}
   \]

Without this qualification, the unweighted equality
`sum_O delta(O)=0`, the half-`L1` formula, and division of (2.1) need not be
valid.  The `Z_17` calibration is unaffected because every nonempty proper
subset orbit is free.

## 3. Balanced reset sandwich: PASS after a joint-domain correction

The positive pivot is a constant-output `d`-step history reset on its exact
triangular entrance domain.  Its deletion-history dual is likewise a
constant-output reset.  If `P` maps the joint pivot output `H_*` into the
joint entrance domain of the second pivot, and if the cap word is balanced
and prefix-safe, then

\[
                            \Pi P\Pi                    \tag{3.1}
\]

returns both the cap slack and the history state.  The proof of Theorem 5.1
is therefore correct under its private-resource and cap-neutral hypotheses.

The entrance domain must, however, be written as an exact subset of the
physical bi-history state:

\[
  G_{\rm joint}
   =\{(H^+,H^-):H^+\in G^+,\ H^-\in G^-,
                     (H^+,H^-)\text{ is endpoint-realizable}\}.  \tag{3.2}
\]

It is not generally the full Cartesian product `G^+ times G^-`.  At a
fixed owner, recent inserted labels are present and recent deleted labels
are absent; in particular the same coordinate cannot occupy both roles.
For `d=1`, the formal pair `(H^+,H^-)=((x),(x))` can pass two unrelated
triangular label exclusions while being physically impossible at any owner.
Thus (5.2) should either define `G` by (3.2), or state that `mathscr H_d`
already contains only endpoint-realizable joint sockets and intersect the
Cartesian guards with it.  The constant output `H_*` must belong to that
same joint state space.

The phrase “cap-neutral on the declared upper-cap bank” must also mean all
caps whose support the regenerative class claims.  Neutrality on a strict
subbank cannot justify return of the full cap vector.

## 4. Exact literal same-cap history ticket

The audited theorem correctly leaves balanced backup/history planting open.
There is a useful exact local sharpening.  Let `U` be a cap of size
`n=r+1` and consider the prospective connector

\[
                       U-\alpha\longrightarrow U-\beta,
                  \qquad\alpha\ne\beta,                \tag{4.1}
\]

which deletes `beta` and inserts `alpha`.  Let

* `H_I,H_D` be the recent insertion/deletion collars at its left endpoint;
* `F_D,F_I` be the future deletion/insertion collars at its right endpoint.

Assume the adjacent retained ears are internally biresident.  The connector
realizes those literal endpoint sockets and is biresident exactly when:

\[
\begin{aligned}
 H_I\cup F_D&\subseteq U,\\
 (H_D\cup F_I)\cap U&=\varnothing,                     \tag{4.2}\\
 \alpha,\beta&\in U\setminus(H_I\cup F_D),
                       \quad\alpha\ne\beta,
\end{aligned}
\]

and the old positive and negative cross-collar inequalities hold.  If

\[
                         W_U=U\setminus(H_I\cup F_D),
\]

the exact oriented ticket count is

\[
                         |W_U|(|W_U|-1).                \tag{4.3}
\]

Indeed, recent insertions and future deletions must be present at their
respective endpoints; recent deletions and future insertions must be absent.
The connector event excludes both missing labels from the positive collars
and excludes the possible endpoint exceptions from the negative collars,
giving (4.2).  Once (4.2) holds, any two distinct missing labels in `W_U`
work.  If `n>=2d+1`, the menu has size at least

\[
                         (n-2d)(n-2d-1).                \tag{4.4}
\]

This endpoint-realizability row is essential when the ticket endpoints are
being chosen prospectively.  Testing only connector event exclusions while
holding arbitrary collars fixed can count tickets whose recent/future
histories are incompatible with `U-alpha,U-beta`.

The cap-prefix monoid and this local ticket theorem are combined in
`MATH_THEOREM_K_CAP_BACKUP_HISTORY_TICKET_MONOID_AND_HEPTAGON_HOST_GATE_20260802.md`.
They still do not embed the chosen ticket into one degree-two factor.

## 5. Proposition 6.1: conditional scope PASS

The greedy statement

\[
                         L>(H-1)\Delta                 \tag{5.1}
\]

is exact once `L` counts **complete** tickets and `Delta` bounds conflicts
between complete-ticket lists.  The rooted heptagon theorem supplies these
orders only for central projected tokens.  It does not prove that history,
backup, topology, deeper-upper, source, or compiler filtering retains
`Theta(k^7)` tickets or `O(dk^6)` conflict load.  The audited note states
this dependence explicitly, so no correction to the conditional conclusion
is needed.

The sharp remaining theorem is therefore correlated host planting: select
the cap-slack locations, endpoint-realizable bi-history tickets, retained
ears, and topology in the same prospective factor.  Total repeat mass and
raw central packet abundance are necessary but not sufficient.

