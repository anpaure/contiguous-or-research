# Joint radius-rainbow extraction and the phase-switch implication defect

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome

Let

\[
 n=2m,\qquad W=\binom{2m}m,\qquad
 M=m+H,\qquad N=\binom{2m}M,                            \tag{0.1}
\]

at the calibrated height, so

\[
 MN=W-o(W),\qquad HN=o(W).                             \tag{0.2}
\]

Let \(D=O(1)\), fix \(\eta>0\), and choose the protected rainbow depth so
that

\[
 Q+D\le(1-\eta)H.                                      \tag{0.2a}
\]

For a direct literal-tail conclusion one may take

\[
 Q=\lfloor\alpha H\rfloor,\qquad
 {1\over\sqrt2}<\alpha<1.                              \tag{0.2b}
\]

The deterministic gap-permutation catalogue supplies, on every carrier
\(U\in\binom{[2m]}M\),
many cyclic owner trajectories which are simultaneously exact-rainbow at
every rank \(m\pm q\), \(q\le Q\), and whose adjacent phase switches are
literal commuting arrival diamonds.

This note fuses that catalogue with the multiscale radius law and proves the
following.

1. The common priority order in a decorated catalogue path assigns an exact
   radius \(d(t)\) to every phase.  If

   \[
   \kappa_0=M,\qquad
   \kappa_q=\min\left\{M,
            \left\lfloor{N_q\over N}\right\rfloor\right\},
   \qquad N_q=\binom{2m}{m-q},                         \tag{0.3}
   \]

   then one path has

   \[
   a_d=\kappa_d-\kappa_{d+1}\quad(d<Q),\qquad
   a_Q=\kappa_Q                                       \tag{0.4}
   \]

   phases of exact radius \(d\).  Across all \(N\) carriers this differs
   from the canonical symmetric-chain radius law only by the already proved
   catalogue floors.

2. A **single joint extraction theorem** suffices for coefficient one:
   choose one decorated catalogue trajectory \(P_U\) on every carrier and
   require only

   \[
   \boxed{
   \mathfrak D(P)
   :=D_0+\sum_{q=1}^Q(D_q^-+D_q^+)=o(W),}
   \tag{0.5}
   \]

   where \(D_q^\sigma\) is the actual duplicate excess of the selected
   claimed flags.  Exact matching is unnecessary.  Radius supply,
   internal shadow compatibility, and successor/predecessor compatibility
   are already carried by each trajectory edge.

3. The full decorated catalogue has an exact **joint fractional packing**,
   not merely separate-rank Hall inequalities.  Equivalently, for every
   nonnegative weight \(w\) on all protected Boolean targets,

   \[
   \boxed{
   \sum_U\min_{P\in\mathcal P(U)}
      \sum_{S\in E(P)}w_S
   \le\sum_Sw_S.}
   \tag{0.6}
   \]

   Thus no weighted fractional cross-rank cut remains.

4. For the \(D=1\) adjacent-switch catalogue, the same-rank pair-overlap
   kernel after phase-column contraction is

   \[
   \boxed{O(m^{-2}).}                                  \tag{0.7}
   \]

   The order-\(m^{-1}\) correlations are precisely the vertical nested
   cover links inside one phase column; switches move the whole column, so
   these links are not independent conflicts.

5. Fixing one commuting switch cube on every carrier turns the remaining
   integral choice into a weighted \(2\)-SAT instance.  If \(P_{\rm fix}\)
   is the number of unavoidable fixed-column collision pairs and
   \(\tau(\Phi)\) is the minimum clause weight whose deletion makes the
   phase-switch formula satisfiable, then

   \[
   \boxed{
   \min_x\sum_S\binom{\mu_x(S)}2
   =P_{\rm fix}+\tau(\Phi).}
   \tag{0.8}
   \]

   Consequently the exact phase-switch sufficient inequality is

   \[
   \boxed{
   \min_{\text{cube anchors}}
   \bigl(P_{\rm fix}+\tau(\Phi)\bigr)=o(W).}
   \tag{0.9}
   \]

Equation (0.9) is strictly sharper than a generic common-hypergraph
matching theorem.  It is a concrete contradictory-cycle deletion problem
in the implication graphs of the vertically contracted phase switches.
The orbit calculation (0.7) shows that repeated nonvertical overlap is
already at the \(m^{-2}\) scale.  What is not proved is that the
contradictory implication core has weight \(o(W)\).  This is the exact
remaining inequality isolated here.

## 1. Canonical radius quota inside one rainbow trajectory

For a decorated trajectory \(P\), let \(\prec\) be its common priority
order on the \(M\) phases.  At signed depth \(q\), claim the first
\(\kappa_q\) phases.  Since

\[
 M=\kappa_0\ge\kappa_1\ge\cdots\ge\kappa_Q,             \tag{1.1}
\]

the claimed phase sets are nested.  Define the exact radius of phase \(t\)
by

\[
 d(t)=\max\{q:t\text{ is among the first }\kappa_q
                    \text{ priority phases}\}.         \tag{1.2}
\]

Then exactly \(a_d\) phases have radius \(d\), with \(a_d\) as in (0.4).
The phase column is

\[
 \mathcal C_t(P)
 =\{X_t\}\cup
   \{L_q(t),U_q(t):1\le q\le d(t)\}.                   \tag{1.3}
\]

The gap-permutation rainbow theorem gives:

* every set in (1.3) is a literal consecutive intersection or union flag of
  the owner cycle;
* for each fixed rank, the claimed targets in one trajectory are distinct;
* the directed transitions
  \[
  X_t\longrightarrow X_{t+1}                           \tag{1.4}
  \]
  give one compatible predecessor and successor to every phase.

Thus a decorated trajectory is one ordered edge

\[
 E(P)=\{t_U\}\cup\bigsqcup_{t\in\mathbb Z_M}
       \mathcal C_t(P),                                \tag{1.5}
\]

where the disjoint-union sign records slots; as Boolean targets, different
phase columns can meet only across different selected trajectories because
of internal exact rainbowness.

Now put

\[
 \delta_q=N_q-N\kappa_q\quad(0\le q\le Q),              \tag{1.6}
\]

where \(\delta_0=W-MN\).  Let the canonical truncated global radius counts
be

\[
 C_d=N_d-N_{d+1}\quad(d<Q),\qquad C_Q=N_Q.              \tag{1.7}
\]

### Proposition 1.1 (exact quota-floor relation)

For \(d<Q\),

\[
 \boxed{
 C_d-Na_d=\delta_d-\delta_{d+1},}
 \tag{1.8}
\]

while

\[
 \boxed{C_Q-Na_Q=\delta_Q.}                            \tag{1.9}
\]

Equivalently, for every \(q\le Q\),

\[
 \boxed{
 \sum_{d=q}^QNa_d=N\kappa_q=N_q-\delta_q.}
 \tag{1.10}
\]

#### Proof

Substitute \(a_d=\kappa_d-\kappa_{d+1}\) and
\(\delta_q=N_q-N\kappa_q\):

\[
 \begin{aligned}
 C_d-Na_d
 &=(N_d-N_{d+1})-N(\kappa_d-\kappa_{d+1})\\
 &=\delta_d-\delta_{d+1}.
 \end{aligned}
\]

The endpoint case and the telescoping form are immediate. \(\square\)

The deterministic catalogue calculation gives

\[
 \boxed{
 \delta_\Sigma
 :=\delta_0+2\sum_{q=1}^Q\delta_q=o(W).}
 \tag{1.11}
\]

For completeness, at a noncapped depth \(0\le\delta_q<N\), so all such
floors contribute \(O(QN)=o(W)\).  A capped depth has
\(\kappa_q=M\), hence \(N_q\ge MN\); the calibrated crossing estimate
shows that there are only \(O(\sqrt H)\) such depths, each with
\(\delta_q\le W-MN=O(WH/m)\).  Their total is
\(O(WH^{3/2}/m)=o(W)\), proving (1.11).

Thus the common priority is already a homogeneous multiradius bundle with
the correct global tail quotas up to total \(o(W)\).  No separate
radius-mixing extraction is required.

## 2. The joint collision extraction theorem

Choose one decorated trajectory \(P_U\) for every carrier.  For a protected
target \(S\), let \(\mu(S)\) be its number of selected claimed occurrences.
At the middle rank define

\[
 D_0=\sum_{S\in\binom{[2m]}m}(\mu(S)-1)_+,             \tag{2.1}
\]

and define \(D_q^\pm\) analogously at ranks \(m\pm q\).

Let \(h_0,h_q^\pm\) be the corresponding numbers of uncovered targets.
The total selected occurrence counts are fixed, independently of the chosen
trajectories:

\[
 T_0=MN=W-\delta_0,\qquad
 T_q^\pm=N\kappa_q=N_q-\delta_q.                       \tag{2.2}
\]

### Lemma 2.1 (exact joint hole identity)

\[
 \boxed{
 h_0=\delta_0+D_0,\qquad
 h_q^\pm=\delta_q+D_q^\pm.}
 \tag{2.3}
\]

#### Proof

At any rank, if \(T\) is the total number of occurrences, \(V\) their
distinct support, \(D=T-V\) their duplicate excess, and \(h=N_{\rm rank}-V\),
then

\[
 h=N_{\rm rank}-T+D.                                   \tag{2.4}
\]

Substitute (2.2). \(\square\)

### Joint canonical-radius rainbow extraction \((\mathrm{JCRE}_Q)\)

Select one decorated exact-rainbow gap trajectory on every carrier so that

\[
 \mathfrak D
 =D_0+\sum_{q=1}^Q(D_q^-+D_q^+)=o(W).                 \tag{2.5}
\]

This is one joint assertion.  It does not multiply owner, shadow, or
successor marginals.

### Theorem 2.2 (\(\mathrm{JCRE}_Q\) implies coefficient one)

Assume (1.11), \(QN=o(W)\), and that the Boolean tails outside the protected
band have size \(o(W)\).  Then \(\mathrm{JCRE}_Q\) gives a nonzero
contiguous-OR word of length

\[
 W+o(W).                                               \tag{2.6}
\]

The tail hypothesis holds for (0.2b).  Indeed, the consecutive layer ratios
and a geometric-tail estimate give

\[
 2\sum_{q>Q}N_q
 =O\!\left(W{m\over Q}e^{-Q^2/m}\right)
 =W\,m^{\,1/2-\alpha^2+o(1)}
 =o(W).                                                \tag{2.6a}
\]

#### Proof

Cut each cyclic trajectory once and compile its radius-\(Q\) rotor word.
The total primary length is at most

\[
 (M+2Q+1)N
 =MN+(2Q+1)N
 =W+o(W).                                              \tag{2.7}
\]

The successor/predecessor chronology and all flags in (1.3) are preserved
because they belong to the same literal trajectory.

By Lemma 2.1, the total protected holes are

\[
 \delta_\Sigma+\mathfrak D=o(W).                       \tag{2.8}
\]

Append them literally, then append the \(o(W)\) outer-tail masks.  This
gives (2.6). \(\square\)

The theorem is strictly weaker than the old common matching: exact
disjointness would force every \(D_q^\sigma=0\), whereas (2.5) permits
arbitrary collision geometry of total size \(o(W)\).  It is also sharper
than the multiscale common-backbone gate: whole catalogue trajectories
already carry compatible histories, so no cross-radius successor matching
remains.

## 3. One exact joint fractional flow

Let \(\mathcal P(U)\) be the full labelled deterministic catalogue on
carrier \(U\), including the common priorities.  Retain labelled
multiplicities.  If \(A=|\mathcal P(U)|\), give every
\(P\in\mathcal P(U)\) weight \(1/A\).

The catalogue degree calculation gives

\[
 \sum_{P\in\mathcal P(U)}{1\over A}=1                 \tag{3.1}
\]

at every carrier tag, and for every protected target \(S\) at depth \(q\),

\[
 \sum_{\substack{U,P\in\mathcal P(U)\\S\in E(P)}}
 {1\over A}
 ={N\kappa_q\over N_q}\le1.                            \tag{3.2}
\]

Thus the variables

\[
 x_{U,P}={1\over A}                                    \tag{3.3}
\]

solve the complete grouped packing LP

\[
 \sum_{P\in\mathcal P(U)}x_{U,P}=1\quad(U),            \tag{3.4}
\]

\[
 \sum_{U,P:S\in E(P)}x_{U,P}\le1\quad(S),\qquad
 x_{U,P}\ge0.                                          \tag{3.5}
\]

This LP already couples all ranks and all phase histories.

### Theorem 3.1 (joint weighted Hall inequality)

For every nonnegative weight vector \(w=(w_S)\) on the protected targets,

\[
 \boxed{
 \sum_U\min_{P\in\mathcal P(U)}w(E(P))
 \le\sum_Sw_S,}
 \tag{3.6}
\]

where

\[
 w(E(P))=\sum_{S\in E(P)\setminus\{t_U\}}w_S.          \tag{3.7}
\]

#### Proof

For each carrier,

\[
 \min_{P\in\mathcal P(U)}w(E(P))
 \le\sum_{P\in\mathcal P(U)}x_{U,P}w(E(P)).            \tag{3.8}
\]

Sum over \(U\), reverse the order of summation, and use (3.5):

\[
 \sum_{U,P}x_{U,P}w(E(P))
 =\sum_Sw_S\sum_{U,P:S\in E(P)}x_{U,P}
 \le\sum_Sw_S.
\]

\(\square\)

Equation (3.6) is the complete fractional Farkas cut for choosing one
trajectory per carrier against all target capacities.  Separate-rank Hall
is only a projection of it.  Therefore the remaining obstruction is
integrality, not an undiscovered fractional cross-rank inequality.

## 4. Bounded-displacement gap geometry and higher overlap

Fix a \(D\)-banded gap trajectory.  At rank \(r=m\pm q\), let \(F_r(t)\)
denote its phase-\(t\) flag and let \(I_r(t)\) be the corresponding ordinary
cyclic interval flag.  The bounded-displacement theorem gives

\[
 d_J(F_r(t),I_r(t))\le D.                              \tag{4.1}
\]

For two cyclic intervals of common length \(r\) in an \(M\)-cycle, whose
start phases have circular distance \(k\),

\[
 d_J(I_r(s),I_r(t))
 =\min\{k,M-k,r,M-r\}.                                 \tag{4.2}
\]

Throughout \(q\le Q\),

\[
 \min\{r,M-r\}\ge H-Q.                                 \tag{4.3}
\]

### Lemma 4.1 (near-phase multiplicity)

If

\[
 a+2D<H-Q,                                             \tag{4.4}
\]

then, for fixed \(s\), the number of phases \(t\) satisfying

\[
 d_J(F_r(s),F_r(t))\le a                               \tag{4.5}
\]

is at most

\[
 \boxed{2(a+2D)+1.}                                    \tag{4.6}
\]

#### Proof

The triangle inequality and (4.1) give

\[
 d_J(I_r(s),I_r(t))\le a+2D.                           \tag{4.7}
\]

By (4.2)--(4.4), the circular phase distance is at most \(a+2D\).
There are at most \(2(a+2D)+1\) such phases. \(\square\)

Now symmetrize over all carrier choices and all bijective coordinate
labellings.  Conditional on one fixed phase slot having image
\(P\in\binom{[2m]}r\), a second slot at template Johnson distance \(a\)
is uniform on the stabilizer orbit

\[
 \{R\in\binom{[2m]}r:d_J(P,R)=a\},                     \tag{4.8}
\]

whose size is

\[
 \binom ra\binom{2m-r}a.                               \tag{4.9}
\]

### Proposition 4.2 (same-rank higher-overlap kernel)

For \(D=O(1)\), \(H-Q=\Omega(H)\), and every two distinct same-rank targets
\(P,R\), the normalized catalogue codegree, after averaging over the
possible phase slot of \(P\), is at most

\[
 \boxed{
 {2(a+2D)+1\over\binom ra\binom{2m-r}a}
 +\exp(-\Omega(H\log(m/H))),}
 \qquad a=d_J(P,R).                                    \tag{4.10}
\]

Consequently

\[
 \boxed{
 \max_{P\ne R}
 {\operatorname{codeg}(P,R)\over\deg(P)}
 =O\!\left({D+1\over m^2}\right).}
 \tag{4.11}
\]

#### Proof

For \(a+2D<H-Q\), combine Lemma 4.1 with the orbit size (4.9).  For
\(a+2D\ge H-Q\), there are at most \(M\) phase slots, while (4.9) is at
least

\[
 \binom{m-Q}{H-Q-2D}                                   \tag{4.12}
\]

up to a harmless symmetric choice of side.  To see that this covers the
whole remaining range, note that two rank-\(r\) targets in one carrier have
Johnson distance at most \(M-r\); beyond that distance the codegree is zero.
Throughout the possible range \(a=O(H+Q)=o(m)\), the relevant binomial
factors are increasing before their central point.  Since \(H=o(m)\), the
resulting ratio is
\(\exp(-\Omega(H\log(m/H)))\).

For the maximum in (4.11), the first term of (4.10) is largest at \(a=1\):

\[
 {O(D+1)\over r(2m-r)}=O((D+1)/m^2).                  \tag{4.13}
\]

The terms \(a\ge2\) are smaller, and the large-\(a\) term is negligible.
\(\square\)

Different-rank cover pairs can still have normalized codegree
\(\Theta(1/m)\): once an owner or flag is fixed, selecting one prescribed
deleted or inserted coordinate has probability \(1/\Theta(m)\).  These are
the only possible one-coordinate slot types.  The canonical instances are
the vertical nested links inside the phase columns (1.3), together with
their shifted Pascal copies.  A phase switch changes the complete vertical
column.  Hence target collisions in the contracted option system are
governed by the \(O(m^{-2})\) same-rank kernel (4.11), not by treating the
\(O(m^{-1})\) cover links as independent choices.

This is a genuine higher-overlap saving.  It does not by itself prove an
integral rounding theorem: a sparse binary conflict system can contain a
linear contradictory core even when each nonvertical pair mode is small.

## 5. Commuting switch cubes as a binary column system

Fix, for every carrier \(U\):

1. a bijective cyclic labelling of \(U\);
2. a common priority order of its phases;
3. the ordinary gap schedule \(\rho(c)=c+H\);
4. a set of disjoint adjacent phase pairs.

For every chosen pair, either keep or transpose it.  The resulting switches
commute.  Every bit vector gives a legal \(D=1\) zero-winding schedule and
hence an exact-rainbow trajectory.

An adjacent switch changes exactly one intermediate phase column and agrees
with the other orientation at every other phase.  Let \(\mathcal E\) be the
set of switch bits over all carriers.  For \(e\in\mathcal E\), write

\[
 C_e^0,\ C_e^1                                         \tag{5.1}
\]

for the two possible claimed vertical columns at its affected phase.  Let
\(f(S)\) be the number of occurrences of target \(S\) among all phase
columns unaffected by every chosen switch.

For an assignment \(x\in\{0,1\}^{\mathcal E}\), the protected target load is

\[
 \boxed{
 \mu_x(S)=f(S)+
 \sum_{e\in\mathcal E}\mathbf1_{\{S\in C_e^{x_e}\}}.}
 \tag{5.2}
\]

The canonical radius of \(C_e^b\) is fixed by the priority of its phase and
is independent of \(b\).  Likewise, every assignment preserves all
predecessor/successor relations because it is one genuine gap permutation
on each carrier.

Thus all three requirements in the user-level extraction problem are
present in one binary object:

* canonical radius quota: fixed by the phase priorities;
* shadow collision: measured by the loads (5.2);
* chronological compatibility: guaranteed by the commuting switch cube.

## 6. Exact reduction to weighted \(2\)-SAT

Define the pair-collision energy

\[
 \mathcal P(x)=\sum_S\binom{\mu_x(S)}2.                \tag{6.1}
\]

It dominates the duplicate excess:

\[
 \sum_S(\mu_x(S)-1)_+\le\mathcal P(x).                 \tag{6.2}
\]

Construct a weighted \(2\)-CNF formula \(\Phi\) as follows.

1. For every target \(S\), every occurrence \(S\in C_e^b\), and every fixed
   occurrence of \(S\), add the unit clause
   \[
   x_e\ne b,                                           \tag{6.3}
   \]
   with multiplicity \(f(S)\).
2. For every target \(S\), distinct bits \(e\ne e'\), and orientations
   \(b,b'\) with
   \[
   S\in C_e^b\cap C_{e'}^{b'},                         \tag{6.4}
   \]
   add the binary clause
   \[
   (x_e\ne b)\ \lor\ (x_{e'}\ne b').                  \tag{6.5}
   \]
   If two option columns share several targets, retain parallel clauses.

The unavoidable fixed-fixed pair count is

\[
 P_{\rm fix}=\sum_S\binom{f(S)}2.                      \tag{6.6}
\]

### Theorem 6.1 (exact phase-switch clause identity)

For every switch assignment \(x\),

\[
 \boxed{
 \mathcal P(x)
 =P_{\rm fix}
  +\#\{\text{weighted clauses of }\Phi
              \text{ violated by }x\}.}
 \tag{6.7}
\]

#### Proof

For a fixed target \(S\), every unordered pair among its selected
occurrences is of exactly one of three types:

1. two fixed occurrences, counted by (6.6);
2. one fixed occurrence and one selected option occurrence, counted by the
   corresponding unit clause (6.3);
3. selected option occurrences from two distinct switch bits, counted by
   the clause (6.5).

Two orientations of the same bit are never selected simultaneously, and one
phase column contains at most one occurrence of any fixed-rank target.
Therefore every collision pair is counted exactly once.  Sum over \(S\).
\(\square\)

Let \(\tau(\Phi)\) be the minimum total clause weight whose deletion makes
\(\Phi\) satisfiable.  Unit and parallel clauses retain their usual
weights.

### Corollary 6.2 (exact implication-defect formula)

\[
 \boxed{
 \min_x\mathcal P(x)=P_{\rm fix}+\tau(\Phi).}
 \tag{6.8}
\]

#### Proof

If an assignment violates clauses of total weight \(v\), deleting those
clauses leaves a satisfiable formula, so \(\tau(\Phi)\le v\).  Conversely,
after deleting an optimal clause set of weight \(\tau(\Phi)\), choose an
assignment satisfying the remaining formula.  It can violate only deleted
clauses, so its violation weight is at most \(\tau(\Phi)\).  Apply
Theorem 6.1. \(\square\)

For zero defect, the familiar implication-graph criterion follows:
\(\Phi\) is satisfiable exactly when no variable and its negation lie in the
same strongly connected component.  For approximate extraction,
\(\tau(\Phi)\) is the exact minimum weight of clauses which must be removed
to destroy all contradictory implication cores.

## 7. The single sharpened extraction inequality

The cube anchors in Section 5 were arbitrary.  Minimize over all carrier
labellings, priorities, and disjoint adjacent-pair systems.  Define

\[
 \Psi_Q
 =\min_{\text{cube anchors}}
   \bigl(P_{\rm fix}+\tau(\Phi)\bigr).                 \tag{7.1}
\]

### Theorem 7.1 (phase-switch extraction gate)

If

\[
 \boxed{\Psi_Q=o(W),}                                  \tag{7.2}
\]

then \(\mathrm{JCRE}_Q\) holds and therefore coefficient one follows.

#### Proof

Choose anchors attaining (or asymptotically attaining) (7.1), and use
Corollary 6.2 to choose a switch assignment with pair energy
\(\Psi_Q=o(W)\).  By (6.2), the aggregate duplicate excess
\(\mathfrak D\) is \(o(W)\).  Apply Theorem 2.2. \(\square\)

Equation (7.2) is the promised exact minimal remaining inequality for the
phase-switch route.  It is sharper than generic common matching in four
ways.

1. It allows \(o(W)\) total collisions instead of demanding a matching.
2. It enforces one trajectory per carrier automatically.
3. It keeps the canonical radius profile and every shadow rank in one
   vertical option.
4. It enforces all successor/predecessor histories automatically through
   the switch cube.

The weighted Hall inequality (3.6) proves that the unrestricted catalogue
has no fractional joint obstruction.  Proposition 4.2 proves that the
uncontracted \(m^{-1}\) codegrees are vertical cover links, while the
same-rank switch-conflict kernel is \(O(m^{-2})\).  Neither fact alone bounds
\(\tau(\Phi)\): a family of small pair modes can still form a contradictory
implication core of linear total weight.

Thus the remaining mathematical statement is no longer “find a common
matching in a growing hypergraph.”  It is:

> Choose the carrier cube anchors so that the fixed collision count plus the
> minimum contradictory-clause deletion weight of the resulting
> phase-switch implication graphs is \(o(W)\).

This condition is necessary and sufficient for the pair-energy
phase-switch method, and sufficient for coefficient one.

## 8. Optional fractional switch dual

For fixed anchors, relax each bit to choose its two columns fractionally:

\[
 x_{e,0}+x_{e,1}=1,\qquad x_{e,b}\ge0.                 \tag{8.1}
\]

Allow target exceptions \(z_S\ge0\) and minimize \(\sum_Sz_S\) subject to

\[
 f(S)+\sum_{e,b:S\in C_e^b}x_{e,b}\le1+z_S.           \tag{8.2}
\]

Linear-programming duality gives the exact value

\[
 \boxed{
 \max_{0\le w_S\le1}
 \left[
 \sum_e\min_{b\in\{0,1\}}w(C_e^b)
 -\sum_S(1-f(S))w_S
 \right],}
 \tag{8.3}
\]

where \(w(C)=\sum_{S\in C}w_S\).

Therefore the fixed-anchor fractional phase-switch defect is \(o(W)\) if
and only if

\[
 \boxed{
 \sum_e\min\{w(C_e^0),w(C_e^1)\}
 \le\sum_S(1-f(S))w_S+o(W)}
 \tag{8.4}
\]

for every \(w\in[0,1]^{\mathcal V}\).

Equation (8.4) is a weighted phase-column Hall inequality.  It is sharper
than separate-rank Hall because one minimum chooses a complete vertical
column.  The unrestricted catalogue satisfies the larger grouped
fractional system by Section 3; what is not known is whether anchors can be
chosen so that both (8.4) and the integral implication defect (7.2) have
only \(o(W)\) loss.

## 9. Audit ledger

### Proved

1. The common priority gives the exact per-trajectory radius counts (0.4).
2. The global radius discrepancy is exactly (1.8)--(1.10), with total
   floor leave \(o(W)\).
3. Aggregate duplicate excess \(o(W)\), rather than exact matching, is
   sufficient for coefficient one.
4. The catalogue has one exact joint grouped fractional packing and obeys
   every weighted joint Hall cut (3.6).
5. Bounded gap displacement gives the near-phase multiplicity bound (4.6).
6. For \(D=O(1)\), the same-rank normalized pair codegree is \(O(m^{-2})\).
7. A commuting adjacent-switch cube is one binary vertical-column system
   carrying quota, shadows, and chronology simultaneously.
8. Its pair-collision energy is exactly weighted Max-\(2\)-SAT, and its
   optimum is \(P_{\rm fix}+\tau(\Phi)\).
9. The single inequality \(\Psi_Q=o(W)\) implies coefficient one.

### Still open

1. No construction here proves \(\Psi_Q=o(W)\).
2. The \(O(m^{-2})\) higher-overlap kernel does not by itself rule out a
   linear contradictory \(2\)-SAT core.
3. The unrestricted joint fractional packing need not restrict to a
   low-defect binary cube after anchors are chosen.
4. A proof must now establish either:
   * an anchor-selection theorem with
     \(P_{\rm fix}+\tau(\Phi)=o(W)\); or
   * a nonbinary gap-permutation rounding theorem with
     \(\mathfrak D=o(W)\) directly.

## 10. Fixed-template orbit matching shortcut

`MATH_ATTACK_AUGMENTED_TEMPLATE_ORBIT_MATCHING_SYMMETRIZATION_20260725.md`
proves an alternative exact route.  Fix one internally rainbow augmented
trajectory template \(A\) and take its indexed \(S_{2m}\)-orbit.  If that
single edge-transitive orbit has a matching of size

\[
 N-r,\qquad r=o(N/\sqrt m),
\]

then its collision defect is zero and its exact protected-hole ledger is

\[
 \delta_\Sigma+r\left(M+2\sum_{q=1}^Q\kappa_q\right)=o(W).
\]

Hence Theorem 2.2 applies directly.  Moreover, orbiting this one matching
proves every nonnegative weighted edge cut:

\[
 \nu_y\ge {N-r\over |E|}y(E)
 ={1-r/N\over D_{\rm tag}}y(E).
\]

After a common blow-up, its coordinate translates are an exact proper
edge coloring.  Thus no separate hereditary weighted-cut theorem is
needed once the unweighted orbit matching is known.

Geometrically, such a matching is a template-tiled partial band
SCD/rotor resolution.  It is stronger than the present collision-tolerant
JCRE selection and is not implied by an arbitrary SCD: the latter need
not partition into coordinate copies of the fixed schedule, priority
pattern, and carrier block \(A\).  Existence of the required unweighted
orbit matching remains open.
