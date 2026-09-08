# Composite switches do not carry their own pair root: the exact survivor-ticket gate

**Date:** 2026-08-06  
**Method:** literal composite-row, occurrence-role, and coefficient audit; no
computation or search  
**Status:** proof-safe obstruction, a conditional complete-orbit transport
theorem, and a sufficient reduction.  The naive declaration
`Q={x,y}` is invalid.  A different involution, transporting the entire
blocker tuple `(tau A,G,y)` to `(A,tau G,x)`, does close the unmarked raw
row when the stopped switch is the full composite conjugate and the ledger
is complete-host.  One-component switches and non-covariant marked
cylinders still require the survivor-ticket condition below.

This note continues
`MATH_THEOREM_SERVICE_DAMPED_FIRST_KILL_CLOSURE_AND_TRANSPORTED_ROC_GATE_20260806.md`.
The actual stopped rows are composite objects

\[
 A=(Q,E,F),\qquad
 \mu_i(A)=c_i(Q,E,F)R_i(E,F;Q),
\tag{1.1}
\]

not independently weighted atomic switch candidates.  In particular, the
audit in
`MATH_AUDIT_RAW_SWITCH_FOUR_ROLE_COEFFICIENT_AND_UNANCHORED_CHANGE_OBSTRUCTION_20260806.md`
forbids inserting an additional atomic factor `a_C/X` into (1.1).

## 1. One-component private switch

Fix an occurrence role `\alpha` of `E`.  Suppose its old physical resource is
`x` and a private Johnson switch replaces it by `y`.  Write

\[
 E^x=E_0\mathbin{\dot\cup}\{x\},\qquad
 E^y=E_0\mathbin{\dot\cup}\{y\},
\tag{1.2}
\]

at the occurrence level.  The notation permits other roles in the macro to
use the same *set value* only on a separately declared repeat face.  Away
from that face, `x` occurs in `E^x` and not `E^y`, while `y` occurs in `E^y`
and not `E^x`.

The two stopped rows are therefore

\[
 A_x=(Q_x,E^x,F),\qquad A_y=(Q_y,E^y,F),
\tag{1.3}
\]

whenever both rooted rows are valid.  A selected blocker can kill `A_y`
without killing `A_x` by hitting the mate-side resource `y`.

The transported energy in `(TROc)` contains

\[
                 (f_i(x)-f_i(y))^2.
\tag{1.4}
\]

The ordinary first-entry ledger sees the hit endpoint `y`.  Its missing
part is the unhit survivor endpoint `x` with the *same actual
hypothetical-survivor coefficient*.

## 2. Pair-root impossibility lemma

### Lemma 2.1

On the resource-simple face of (1.2), the set `\{x,y\}` cannot be the
distinguished common pair root of either `A_x` or `A_y`.

#### Proof

A distinguished pair root of `(Q,E,F)` is contained in both macro rows; in
particular

\[
                         Q\subseteq E\cap F.
\tag{2.1}
\]

But `y` is absent from `E^x`, so `\{x,y\}` is not a subset of `E^x`.
Likewise `x` is absent from `E^y`, so `\{x,y\}` is not a subset of `E^y`.
Thus (2.1) fails on both shores.  \(\square\)

This is an occurrence statement.  If another role happens to realize the
opposite physical value, the set-valued row may contain both `x` and `y`.
That is a repeat/role-collision face, not the generic private switch.  It
requires its own occurrence-labelled multiplicity and coefficient audit;
it cannot justify the unrestricted switch row.

### Corollary 2.2

The authenticated pair-rooted closure `(ROc)` cannot be applied to (1.4)
merely by declaring `Q=\{x,y\}`.  The proposed root is not a root of the
actual composite row.

In particular, the complete-orbit average in `(ROc)` does not itself
transport a first-entry ticket from `y` to the Johnson neighbour `x`.

## 3. Why full conjugation is a different operation

Let `tau` interchange the underlying coordinates producing `x` and `y`.
The natural symmetry action on a composite row is

\[
 (Q,E,F)\longmapsto(\tau Q,\tau E,\tau F).
\tag{3.1}
\]

This is not the one-component move (1.3): it transports every occurrence
of the affected coordinates in `Q`, `E`, and `F`.  Moreover, in a stopped
or marked process it also transports the availability history and the
marked-cylinder label.  Coordinate invariance of the *unconditioned*
complete orbit therefore gives no equality between the two conditional
coefficients unless one proves all of

\[
 \mu_i(Q,E,F)=\mu_i(\tau Q,\tau E,\tau F),
 \quad
 h_i(Q,E,F)=h_i(\tau Q,\tau E,\tau F),
\tag{3.2}
\]

with the stopped state and every occurrence mark transported as well.
Those identities are not consequences of `(ROc)`.

Conversely, holding `Q` and `F` fixed and switching only `E` is a valid
local candidate only after deriving the two actual coefficients

\[
             \mu_i(A_x),\qquad \mu_i^+(A_x;G)
\tag{3.3}
\]

and their mate-side analogues.  If `x` or `y` occurs in `F` or `Q`, the
intersection exponent, union exponent, or root validity can change.  Such
terms may eventually inject into one-entry or two-entry ledgers, but the
injection must start from (3.3); an independent atomic candidate factor is
not available.

## 4. The exact survivor-ticket condition

Let `\mathcal B_i` be the literal set of first-kill switch births at time
`i`.  For `e\\in\\mathcal B_i`, write

\[
 e=(A_e,A'_e,G_e;x_e,y_e),
\]

where `A_e` is the surviving composite row, `A'_e` is the killed mate,
`y_e` is the hit endpoint, and `x_e` is the unhit survivor endpoint.  Let
`w_i(e)` be its actual nonnegative hypothetical-survivor coefficient in
the capacity-faithful birth operator.  Thus the one-step contribution to
`(TROc)` is

\[
 {\beta_i d\over X_i}
 \sum_{e\in\mathcal B_i}w_i(e)
             (f_i(x_e)-f_i(y_e))^2.
\tag{4.1}
\]

For every available occurrence-labelled survivor ticket `t=(A,x,\\xi)`,
where `\xi` includes the complete stopped/marked-cylinder state, let
`s_i(t)` denote its coefficient in the authenticated future-service or
rooted one-entry budget.  A **coefficient-faithful survivor allocation** is
a map

\[
                         \pi:e\longmapsto t_e=(A_e,x_e,\xi_e)
\tag{4.2}
\]

which preserves the occurrence, phase, and cylinder labels and satisfies
the pointwise load inequality

\[
 \boxed{
 \sum_{e:\,\pi(e)=t}{\beta_i d\over X_i}w_i(e)
       \le C s_i(t)
       \quad\hbox{for every literal ticket }t.}
\tag{STA}
\]

An equivalent chronological formulation may allocate a birth to the first
later service or kill of `(A_e,x_e,\\xi_e)`, provided the corresponding
predictable Hardy inequality has exactly the left side of `(STA)`.

### Theorem 4.1 (survivor-ticket sufficiency)

Assume:

1. the mate-side terms obey the already authenticated hit/rooted estimate,
   with the literal coefficients `w_i(e)`;
2. `(STA)` holds in every required marked cylinder; and
3. the service ledger gives

   \[
   \mathbb E\sum_{i,t}s_i(t)f_i(x_t)^2\le C\mathsf A.
   \tag{4.3}
   \]

Then `(TROc)` holds.

#### Proof

Use

\[
 (f(x)-f(y))^2\le2f(x)^2+2f(y)^2.
\tag{4.4}
\]

The hit/rooted estimate pays the second term.  Assign the first term by
(4.2), apply `(STA)`, and then sum (4.3).  Every coefficient and every
marked label is unchanged by this argument.  \(\square\)

The theorem is intentionally taut at the coefficient level.  A map of
unweighted switch incidences, or a map that changes the cylinder label,
does not prove `(STA)`.

## 5. A local FIFO obstruction to deriving `(STA)` from hit-only data

The one-edge example already shows that hit-only control does not pay the
survivor endpoint.  There is also a multiplicity obstruction to replacing
`(STA)` by the assertion that every switch has some surviving endpoint.

Take one resource-simple survivor word containing private occurrences
`x_1,...,x_m`.  For each `j`, form a mate by the one-occurrence switch
`x_j -> y_j`, with all `y_j` distinct.  Let a legal blocker word meet all
`y_j` and none of the survivor resources.  Then one accepted blocker kills
all `m` mates and leaves the common survivor live.  With

\[
                   f(x_j)=1,\qquad f(y_j)=0,
\tag{5.1}
\]

every mate-side hit square is zero while the transported energy is

\[
                        \sum_{j=1}^m w_j.
\tag{5.2}
\]

No pair `\{x_j,y_j\}` is a common root by Lemma 2.1.  Hence any proof must
show that the survivor service has coefficient capacity at least the
weighted load in (5.2), or prove that the literal canonical FIFO geometry
forbids this joint-blocker pattern.

This is a local set-system obstruction, not a claim that every canonical
macro realizes arbitrary `m`.  Its purpose is exact: private occurrence
switching and earliest-kill uniqueness alone do not imply a bounded-load
survivor allocation.  The missing information is precisely the
coefficient/capacity statement `(STA)`.

## 6. Marked-cylinder covariance is a separate requirement

Suppose a birth is evaluated under a future event `h`.  Full conjugation
usually sends `h` to `tau h`, while the desired estimate remains in the
original cylinder.  Therefore even a static equality

\[
                         \omega_A=\omega_{\tau A}
\]

does not imply equality of future-weighted coefficients.  A valid ticket
must either:

* stay inside the same literal cylinder and use its actual continuation
  ratio; or
* transport the cylinder label and prove a measure-preserving bijection of
  the complete marked event.

Finite size-two/three marked replay is still required after the unmarked
allocation is proved.

## 7. The complete-orbit blocker-conjugation involution

Lemma 2.1 rules out only the false move of declaring `{x,y}` itself to be
the common distinguished root.  It does **not** rule out transporting the
whole first-entry tuple.

Assume now that the stopped switch is genuinely the full composite
conjugation

\[
                         A\longleftrightarrow\tau A,
\tag{7.1}
\]

rather than the one-component move (1.3).  Suppose `A` survives the
accepted blocker `G`, while `tau A` is killed.  Let `y` be one blocker-hit
changed resource of `tau A`, and put

\[
                         x=\tau y,\qquad H=\tau G.
\tag{7.2}
\]

Then `H` contains `x`.  Also, because `G` is disjoint from every resource
of the survivor `A`, `H=tau G` is disjoint from every resource of `tau A`.
Thus `(A,H,x)` is the coordinate-conjugate counterfactual first-entry tuple:
`H` hits the `A` shore at `x`.

### Lemma 7.1 (raw coefficient preservation)

On the complete unmarked coordinate orbit, the map

\[
 \boxed{
 \Phi_\tau:(\tau A,G,y)\longmapsto(A,\tau G,\tau y)}
\tag{7.3}
\]

preserves the raw hypothetical first-entry coefficient.

#### Proof

Coordinate conjugation preserves the base blocker rate,

\[
                         a_{\tau G}(i)=a_G(i),
\tag{7.4}
\]

and transports the complete composite index, including its root:

\[
               (\tau Q,\tau E,\tau F)\mapsto(Q,E,F).
\]

The deterministic next-density factors depend only on the transported
intersection, union, slot, and rank counts.  Because the same deterministic
update is used when either live shore is hypothetically retained, the raw
counterfactual identity and then coordinate conjugation give

\[
 \mu_i^+(A;G)=\mu_i^+(\tau A;G)
 =\mu_i^+(A;\tau G).
\tag{7.5}
\]

Multiplying (7.4)--(7.5) proves equality of

\[
 {a_G(i)\over X(i)}\mu_i^+(\tau A;G)
 \quad\hbox{and}\quad
 {a_{\tau G}(i)\over X(i)}\mu_i^+(A;\tau G).
\]

The extra predictable scalar `\beta_i d/X_i` in `(TROc)` is common to the
whole resource type at the fixed state and is unchanged by the map.
\(\square\)

The target tuple need not be dynamically live.  The authenticated static
`(ROc)` ledger is a complete-host/counterfactual sum.  The earliest-kill
restriction on the source only deletes nonnegative target tuples.

### Lemma 7.2 (multiplicity)

Retain the transposition label `\tau` and the changed physical resource
`y` in the source tuple.  On a resource-simple composite row, (7.3) is
injective before forgetting `\tau`.  After forgetting `\tau`, a fixed target
tuple has at most `|\mathcal T|` preimages, where `\mathcal T` is the set of
coordinate transpositions.  Therefore the switch normalization

\[
                         \kappa_k={1\over|\mathcal T|}
\tag{7.6}
\]

makes the total forgotten-label load at most one.

#### Proof

For fixed `\tau`, (7.3) is an involution: the inverse sends
`(A,H,x)` to `(\\tau A,\\tau H,\\tau x)`.  Resource simplicity makes `x`
identify its occurrence in `A`; hence there is no additional role fibre.
There are at most `|\\mathcal T|` possible forgotten transposition labels,
which is cancelled by (7.6).  \(\square\)

If one physical resource occurs in several switch roles, the remaining
load is exactly that occurrence multiplicity.  It must be retained in an
occurrence-labelled `(ROc)` replay; set-valued `(ROc)` does not erase it.

### Theorem 7.3 (raw transported endpoint closure)

Assume:

1. every stopped switch in the row is a full composite conjugate (7.1);
2. its raw coefficient is the full hypothetical coefficient in Lemma 7.1;
3. the complete-host `(ROc)` first-entry ledger is valid with the
   occurrence multiplicity in Lemma 7.2; and
4. the usual density change from selection time to the static kernel is
   coordinate invariant.

Then the survivor-endpoint part of `(TROc)` is bounded by the same
`(ROc)` budget as the hit-endpoint part.  Consequently the unmarked raw
`(TROc)` row holds.

#### Proof

For every source summand `f_i(x)^2`, apply (7.3).  Lemma 7.1 preserves its
coefficient, Lemma 7.2 controls its multiplicity, and the target is a
complete-host first-entry summand rooted at the hit resource `x`.  The
time-to-static density kernel is unchanged because conjugation preserves
every overlap count.  Thus `(ROc)` pays the transported squares.  It
already pays the literal hit squares `f_i(y)^2`; now use

\[
                  (f_i(x)-f_i(y))^2
                  \le2f_i(x)^2+2f_i(y)^2.
\]

This is `(TROc)`.  \(\square\)

The theorem uses a **single-root first-entry tuple at `x`**, not the
invalid pair root `{x,y}`.

### Scope boundary

Theorem 7.3 does not apply automatically in either of two cases.

* For a one-component switch `(Q,E^x,F)->(Q',E^y,F)`, the mate need not be
  `tau A`; applying `tau` also changes all other occurrences of the two
  coordinates in `Q,E,F`.  The target of (7.3) is then not the desired
  survivor row.
* In a fixed marked cylinder `h`, conjugation generally sends the tuple to
  cylinder `tau h`.  The theorem extends if the marked family is summed
  over a complete coordinate orbit, or if an explicit bijection proves
  equality of the two continuation ratios.  It does not extend merely
  from an unmarked coefficient equality.

In these two cases `(STA)` remains the exact sufficient condition.

### Corollary 7.4 (orbit-summed marked families)

Let `\sigma` be a fixed finite occurrence-role pattern, and let
`\mathcal H_\sigma` contain every allowed coordinate labelling of that
pattern with coordinate-invariant weight.  If the required bottom estimate
sums over all `h\\in\\mathcal H_\\sigma`, then (7.3), augmented by

\[
                         h\longmapsto\tau h,
\tag{7.7}
\]

is a bijection of the marked complete-host ledger.  Therefore Theorem 7.3
holds after summing this marked family, even though it need not hold in one
fixed labelled cylinder.

#### Proof

The transposition fixes the occurrence roles and permutes only their
coordinate labels.  Completeness of `\mathcal H_\sigma` makes (7.7) a
bijection.  Every base, overlap, and future-density factor is coordinate
invariant after simultaneously transporting the labels.  Apply Theorem
7.3 termwise and then sum over `h`.  \(\square\)

The annealed quarantine reduction asks for the raw aggregate
selected-relation expectation, not a Doob transform by one terminal
cylinder.  Its authenticated marked base rows are complete coordinate
orbits with finitely many fixed role patterns.  Hence Corollary 7.4 removes
the marked-label caveat for that raw aggregate, subject only to the already
stated finite occurrence-multiplicity replay.  A pre-reserved bank does not
invalidate the domination: the source tuples must avoid it, while the
complete-host target ledger may include additional counterfactual tuples
which are not dynamically available.

### Lemma 7.5 (two-block closure of a lower deletion switch)

Use the fresh lower path

\[
 S_j=C\cup\{a_{j+1},\ldots,a_d\}
       \cup\{b_1,\ldots,b_j\},\qquad0\le j\le d.
\tag{7.8}
\]

Swap adjacent deletion labels `a_q,a_{q+1}`, where `1<=q<d`.  In the
current block exactly `S_q` changes.  Every current owner set is unchanged,
because the complementary outgoing-queue prefix changes in the opposite
way.  The outgoing ordered queue is changed by that adjacent swap.

In the next block, write its new deletion order as
`a'_1,...,a'_d`.  For owner copy `c`, its queue tail has the form

\[
 Q_j^c=(a_{j+1},\ldots,a_d,a'_1,\ldots,a'_j).
\tag{7.9}
\]

Thus exactly `Q_q^c`, and hence exactly the role-`q` owner in copy `c`,
changes.  At the end of the next block the outgoing queue is
`(a'_1,...,a'_d)`, independent of the old order.  Therefore the global
coordinate transposition `(a_q a_{q+1})` has closed two-block support

\[
                         1+h\le4:
\tag{7.10}
\]

one current lower occurrence and one next-block owner occurrence in each
of the `h\\in\\{2,3\\}` copies.  Every other lower, owner, mark, slot, and later
queue occurrence contains both labels or neither and is fixed.

#### Proof

Before role `q`, the relevant prefix or suffix contains neither changed
event; after role `q`, it contains both.  Formula (7.8) leaves only `S_q`.
The current owner is the disjoint union of the lower state and its queue
tail, so the two changes cancel setwise there.  Formula (7.9) leaves only
the next-block role `q`.  The next outgoing queue uses only the primed
deletion order, proving closure after two blocks.  \(\square\)

This converts the lower queue holonomy from a growing obstruction into a
constant-support full coordinate conjugation.  It does **not**, by itself,
prove its entire `(TROc)` row: a blocker which kills one shore may hit only
one of the at most four changed mate resources.  Theorem 7.3 pays every
blocker-hit component.  The remaining at most three unhit components need
either the complete switched-row first-entry square, an occurrence-labelled
constant-size cluster replay, or `(STA)`.  They are now a finite
endpoint/cluster family, not a depth-`d` transport family.

## 8. Capacity-faithful birth is a separate row

There are two meanings of the deletion operator in the surrounding notes.

1. If `A_i=L_i-\widetilde L_i` is literally the Laplacian of generator
   edges removed from the current Johnson generator, with their generator
   conductances, then

   \[
                         0\le A_i\le L_i
   \]

   is automatic.
2. If `A_i` is obtained after projecting and summing composite boundary
   rows with weights `mu_i(Q,E,F)`, it is a reweighted Johnson-edge
   operator.  Many composite rows may project to the same physical edge.
   Factoring out one `mu_A` does not prove

   \[
                         A_i\le L_i.
   \]

   One still needs the edgewise/capacity inequality saying that the total
   projected hypothetical-survivor weight on every private generator
   fibre is at most its conductance, or the corresponding positive-operator
   domination.

Thus blocker conjugation can prove `(TROc)` without making `(CFB)`
fiberwise trivial.  The two conditions must not be conflated.

There is, however, a clean sufficient criterion which applies to a
complete private-switch orbit.

### Proposition 8.1 (complete-orbit capacity domination)

Fix one resource layer.  Let `\mathcal S_i` be a complete coordinate orbit
of occurrence-labelled private switches.  Give each switch `s` a positive
weight `\nu_i(s)` satisfying

\[
                         \nu_i(\tau s)=\nu_i(s)
\tag{8.1}
\]

under coordinate conjugation.  Suppose first that every switch changes one
resource, with Johnson incidence `b_s`.  Put

\[
 L_i^{\rm full}=\sum_{s\in\mathcal S_i}\nu_i(s)b_sb_s^*.
\tag{8.2}
\]

Then

\[
                         L_i^{\rm full}=\alpha_iL
\tag{8.3}
\]

for some `\alpha_i\ge0`, where `L` is the normalized Johnson Laplacian.  For
every adapted subfamily `\partial\mathcal S_i\subseteq\mathcal S_i`,

\[
 0\le A_i:=\sum_{s\in\partial\mathcal S_i}\nu_i(s)b_sb_s^*
 \le\alpha_iL.
\tag{8.4}
\]

#### Proof

The complete weighted orbit is invariant under the full coordinate group,
which is transitive on directed Johnson edges.  Every directed edge
therefore has the same total conductance, proving (8.3).  Equation (8.4)
follows by deleting nonnegative rank-one summands.  \(\square\)

For a switch with at most `m_0` changed occurrences, write its projected
incidence as

\[
                         u_s=\sum_{j=1}^{m_s}\epsilon_{s,j}b_{s,j},
                         \qquad m_s\le m_0.
\]

Then

\[
                         u_su_s^*
 \le m_s\sum_{j=1}^{m_s}b_{s,j}b_{s,j}^*.
\tag{8.5}
\]

Each fixed occurrence role on the right has a complete coordinate orbit,
so its sum is a scalar multiple of `L`.  Consequently every boundary
subfamily satisfies

\[
                         0\le A_i\le C_{m_0}\alpha_iL
\tag{8.6}
\]

after one fixed normalization of the complete switch measure.  For the
two-block lower holonomy, `m_0<=4`.

The proposition allows `\nu_i(s)` to include a composite future weight
`\mu_i(Q,E,F)`, provided the *complete counterfactual family* is present and
that weight is coordinate-covariant.  Hence `(CFB)` is automatic if the
actual Duhamel birth operator is precisely the normalized restriction of
this full weighted switch operator.  What remains to audit is this literal
identification: if the Duhamel expansion inserts an additional
candidate-dependent factor after the projection, or uses only a
non-orbit-closed family before normalization, Proposition 8.1 does not
apply.

### Proposition 8.2 (exact orbit-scalar normalization)

Suppose the complete counterfactual operator at state `i` is

\[
 L_i^0=\alpha_iL,
 \qquad B_i^0\ge0,
 \qquad P_i^0=I-{L_i^0\over X_i},
\tag{8.7}
\]

and the current stopped operator is `L_i^0-A_i`, with
`0<=A_i<=L_i^0` from Proposition 8.1.  If `\alpha_i>0`, define

\[
 \overline L_i={L_i^0\over\alpha_i}=L,
 \qquad
 \overline A_i={A_i\over\alpha_i},
 \qquad
 \overline B_i={B_i^0\over\alpha_i},
 \qquad
 \overline X_i={X_i\over\alpha_i}.
\tag{8.8}
\]

Then exactly

\[
 I-{L_i^0\over X_i}
 =I-{\overline L_i\over\overline X_i},
 \qquad
 {B_i^0\over X_i}
 ={\overline B_i\over\overline X_i},
 \qquad
 0\le\overline A_i\le\overline L_i.
\tag{8.9}
\]

Hence the discrete Lyapunov equation and its Duhamel identity are unchanged
by the simultaneous normalization (8.8).  The total rate `X_i` absorbs
`\alpha_i` exactly; no extra algebraic coefficient remains in `(CFB)`.

#### Proof

Every identity in (8.9) follows by cancelling `\alpha_i`.  Both terms which
define the Gramian,

\[
                         {B_i^0\over X_i}
 \quad\hbox{and}\quad
 a_i(P_i^0)^*R_iP_i^0,
\]

are therefore identical before and after normalization.  The same is true
of the current operator with `A_i` inserted.  \(\square\)

There is one exact analytic remainder.  The normalized service parameter
is

\[
 \boxed{
 \overline\lambda_i
 =\overline X_i(1-a_i)
 ={X_i(1-a_i)\over\alpha_i}.}
\tag{8.10}
\]

The service-damped estimates quoted in the parent theorem assume this
quantity is bounded above and below by positive constants.  Therefore
Propositions 8.1--8.2 close `(CFB)` completely once one proves

\[
 \boxed{
 0<c\le {X_i(1-a_i)\over\alpha_i}\le C}
\tag{8.11}
\]

on the stopped interval, with `\alpha_i` computed from the full weighted
private-switch orbit.  If the old normalization already has
`X_i(1-a_i)=Theta(1)`, this is exactly the assertion
`\alpha_i=\Theta(1)`.

A predictable time dependence of `\alpha_i` is not itself an obstruction
in the state-space Bellman equation: (8.8) is an identity at every state.
If one instead freezes one Gramian across several states, the increment of
`\alpha_i` contributes to the ordinary predictable `\Delta R_i` row and must
be retained.  Thus the precise missing normalization is (8.11), not a new
switch-multiplicity or covariance condition.

## 9. Exact proof boundary

The pair-root idea does not close `(TROc)`.  Its failure is structural, not
spectral:

\[
 \boxed{
 \text{switch endpoints are alternatives in one role, not a common
 distinguished pair root.}}
\tag{9.1}
\]

The service-damped resolvent already removes the inverse-gap loss and
coalesces same-resource quadratic stars.  For the **unmarked full-composite
switch row**, Theorem 7.3 supplies the transported endpoint.  Outside that
scope the remaining analytic statement is exactly one of the following
coefficient-level repairs:

1. prove the survivor allocation `(STA)` from the complete FIFO orbit and
   future-service ledger;
2. prove a chronological Hardy estimate with the same stopped and marked
   coefficients; or
3. prove a full composite conjugation identity including availability,
   root transport, and cylinder transport.

Without Theorem 7.3's full-conjugation/covariance hypotheses or one of
these replacement statements, hit-only `(ROc)`, distinct-hit `(FE3)`, and
abstract Johnson adjacency do not imply `(TROc)`.  Independently, the
projected composite birth operator still needs `(CFB)` unless it is
literally a sub-Laplacian.
