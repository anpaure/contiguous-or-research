# Regenerative guarded-switch contraction and the constant-additive theorem

Date: 2026-07-31  
Status: exact conditional contraction and recompilation theorems; hypotheses
are explicit and fail on the frozen `K17` fixed skeleton; no unconditional
all-`k` bound is claimed

## 0. Outcome

The exact two-bank switch calculus can be turned into a genuine recursive
theorem, but only after separating four notions which scalar slack mixes.

1. **Central ownership may be exported at bounded cost.**  Exact Catalan
   ownership is convenient but not logically necessary for a constant-
   additive theorem: a bounded set of omitted middle masks can be appended
   once after recompilation.
2. **Host feasibility is hard.**  Every required `D^2` row bit needs a
   physical envelope host.  Until all such obligations are discharged, no
   lower compiler exists.
3. **Upper and common-cap debt is soft only when literal recompilation is
   supplied.**  A bounded list of omitted targets can be appended as
   singleton letters; an unhosted carrier row cannot.
4. **Local abundance must be guarded and correlated.**  Switch supports,
   protected provider tickets, and five-row cap halos have to be selected in
   one orthogonal bank.  Marginal switch counts or marginal Hall do not give
   this.

Under explicit column-support, guard-overlap, and min-cost Hall-expansion
hypotheses, one repair round has either of the exact forms

\[
                         \Pi'=0                         \tag{0.1}
\]

or

\[
                  \|\Pi'\|_1\le\rho\|\Pi\|_1+\beta,
                  \qquad 0\le\rho<1.                 \tag{0.2}
\]

If the same state recompiles and regenerates at every Pascal step, (0.2)
keeps the defect uniformly bounded.  The bounded-defect completion theorem
then gives

\[
                         \nu(k)\le B(k)+O(1).          \tag{0.3}
\]

The zero-defect form gives `nu(k)=B(k)`.

This is a conditional theorem, not the missing switch-supply result.  The
frozen `K16` equality word validates the zero-defect *terminal* interface.
The current `K17` fixed skeleton violates the expansion hypotheses: it has
immutable host packets and `218` rank-ten obligations with no residual-pair
provider at all.

## 1. Exact defect state

Let a regenerative frame at dimension `k` specify a proposed chain-aligned
middle chronology and its nonflat derivative row `Z`.

### 1.1 Hard host coordinate

For every required row bit `(i,x)`, put

\[
 \mathcal H_{i,x}(Z)=
 \{p\in I_i:x\in E_p(Z)\},                          \tag{1.1}
\]

where `I_i` is its physical carrier interval and `E` is the maximal
envelope.  Let `U(Z)` be a chosen packetization of the pairs having empty
host set.  A packet is allowed to contain several pairs only when one
declared actuator repairs all of them together.  Put

\[
                         u(Z)=|U(Z)|.                 \tag{1.2}
\]

For the depth-two zipper, `I_i={i,i+1,i+2}`.  The unpacketized value is the
row-bit defect count from the run-monoid theorem.

### 1.2 Central/palette coordinate

Let `C_cent(k)` be the required central target packets.  A packet contains a
middle mask and any owner or palette label demanded by the regenerative
sidecar.  Let `A_cent(Z)` be the physical central occurrences, and join a
packet to an occurrence exactly when that occurrence can realize its mask
with the required labels.  Define

\[
 c_{\rm cent}(Z)=|C_{\rm cent}(k)|-
                 \nu\bigl(G_{\rm cent}(Z)\bigr),             \tag{1.3}
\]

where `nu(G_cent)` is maximum matching size.  Thus `c_cent` is the exact
number of central target requirements which must be exported from the
carrier.  For unlabelled middle coverage it is simply the number of missing
distinct middle masks; repeated owners create the same matching deficiency.
Exact central ownership is the special case `c_cent=0`.

Terminally this coordinate is soft: each exported packet contributes its
middle mask as one appended singleton letter.  Recursively it is not free:
the exported packet must either be contracted or carried in the child state.

### 1.3 Scalar and exact cap coordinates

Assume temporarily that `u(Z)=0`.  Let `R^*(Z)` be every lower target and
every upper target having no long provider which must therefore use a short
physical cell.  Let `C_short` be the available singleton/pair cells after
fixed prepins, and let `s_aux` count short cells consumed without serving a
distinct target.  Define

\[
 \omega(Z)=
 \bigl[|R^*(Z)|+s_{\rm aux}-|C_{\rm short}|\bigr]_+. \tag{1.4}
\]

Let `d_cap(Z)` be the minimum number of target requirements which must be
removed from `R^*(Z)` to make the exact matching-plus-common-cap system
feasible.  Necessarily `d_cap>=omega`; put

\[
                  \kappa(Z)=d_{\rm cap}(Z)-\omega(Z). \tag{1.5}
\]

Thus `omega+kappa` is exactly the minimum number of short targets that a
best common-cap recompilation must export as exceptions.  Before host
feasibility, set both values to `infinity` for logical ordering purposes.

The lexicographic defect state is

\[
             \Pi(Z)=(c_{\rm cent},u,\omega,\kappa). \tag{1.6}
\]

When all coordinates are finite, write

\[
          \|\Pi\|_1=c_{\rm cent}+u+\omega+\kappa. \tag{1.7}
\]

This sharpens a scalar owner-slot ledger.  It records central export debt,
then hard host feasibility, then scalar target overflow, and finally the
genuinely correlated common-cap loss beyond counting.

## 2. Proof-safe actuator columns

A **guarded actuator column** `e` consists of one Hamilton-safe signed-
fragment switch, component option, or compound packet, together with the
following literal data.

1. `supp(e)`: every changed owner incidence, fragment and component
   resource.
2. `halo(e)`: every changed derivative row enlarged by the exact
   five-row envelope/common-cap collar.
3. `serv(e)`: the hard-host and soft-target obligation packets repaired by
   the column.
4. `Delta_e`: its exact `R_d` run derivative and truncated interval-union
   provider derivative through every protected upper rank.
5. `debit_e(Y)`: occurrence tickets removed from each already covered
   target `Y`, bounded globally by its spare load `mu(Y)-1`.
6. `Gamma_e`: permanent position bits, protected-row hosts, selected-target
   hosts, prepins, and the before/after cap-collar relation.
7. `c(e)`: its nonnegative short-cell or owner-slot cost.
8. `child(e)`: the exact protected ports and recurrence state exported to
   the next Pascal braid.

A column is **priority-safe at level `j`** when it creates no obligation in
coordinates `1,...,j-1`.  Every new packet in coordinates `j,...,4` is
listed explicitly in a boundary-leakage vector.  It may repair obligations
of later priorities for free.

Two columns are **orthogonal** when:

* their changed incidence/component resources and five-row halos are
  disjoint;
* their provider debits use disjoint preallocated tickets;
* their cap guards agree on every transported position and protected host;
  and
* their child port states compose without identifying two occurrence-
  labelled sockets.

These are local, checkable hypotheses.  Disjoint geometric edges without
the provider and guard rows are not orthogonality.

### Lemma 2.1 (orthogonal batch additivity)

For an orthogonal set `X` of columns:

1. all columns may be applied in any order and the final owner factor and
   derivative row are the same;
2. their labelled run defects and signed upper-provider derivatives add;
3. their common-cap collar transitions are the disjoint product of the
   individual transitions; and
4. their resource cost is `sum_(e in X)c(e)`.

If every column is provider-safe and priority-safe, the batch loses no
protected target and creates no unlisted higher-priority obligation.

#### Proof

Disjoint incidence support makes the literal switches commute.  The
weighted run monoid transports every untouched fragment interior and has
disjoint seam composition on disjoint halos.  The interval-union derivative
is a signed occurrence vector, so disjoint preallocated provider tickets
make its protected withdrawals additive.  The five-row cap-transport lemma
localizes every changed common-cap equation to the disjoint halos; agreement
of the transported guards proves their product is exact.  Resource and
child-socket additivity are part of the declared column state.  \(\square\)

## 3. Hall deficiency inside one orthogonal layer

Let `O` be one priority class of obligation packets and `S` one orthogonal
column bank.  Join `o in O` to `e in S` when `e` safely repairs all pairs in
`o`.  For `X subset O`, let `N(X)` be its column neighbourhood and define

\[
             \delta(G)=\max_{X\subseteq O}(|X|-|N(X)|).        \tag{3.1}
\]

### Lemma 3.1 (deficient Hall)

The maximum number of obligation packets simultaneously repaired by
distinct columns is

\[
                         |O|-\delta(G).             \tag{3.2}
\]

If the minimum cost of such a maximum matching is at most the available
reserve, it is a physically admissible orthogonal repair batch.

#### Proof

Equation (3.2) is the deficiency form of Hall's theorem.  A source--
obligation--column--sink network with unit capacities and column costs has
an integral minimum-cost maximum flow.  Lemma 2.1 turns its matching into a
simultaneous physical batch.  \(\square\)

The cost condition is independent of cardinality Hall.  It cannot be
replaced by positive total slack.

## 4. The contraction lemma

Consider one priority coordinate with `n` current packets.  For the soft
coordinates `c_cent`, `omega`, and `kappa`, this requires a chosen maximum-
matching-deficiency, minimum-deletion, or cap-conflict witness whose units
are represented by literal obligation packets; the witness is recomputed
after every higher-priority phase.  Without such a packet witness, scalar
`c_cent`, `omega`, or `kappa` cannot be fed into the Hall theorem.

Suppose the eligible columns can be divided into `q` orthogonal layers.
Assign each obligation packet to at least one layer and then choose a
partition

\[
                         O=O_1\dot\cup\cdots\dot\cup O_q.       \tag{4.1}
\]

In layer `ell`, retain only columns orthogonal within that layer and safe for
the obligations in `O_ell`.  Assume:

* its Hall deficiency is at most `delta`;
* a maximum matching has cost within the declared reserve; and
* applying such a matching creates a listed leakage vector of total mass at
  most `beta_0` at braid or seam boundaries and none at an earlier priority.

### Theorem 4.1 (one-round guarded contraction)

One layer supplies a physically legal repair with

\[
             n'\le\left(1-{1\over q}\right)n
                    +\delta+\beta_0.                 \tag{4.2}
\]

For `q=1`, `delta=beta_0=0`, the coordinate is repaired exactly.

#### Proof

Some part in (4.1) has size at least `n/q`.  Lemma 3.1 repairs at least
`|O_ell|-delta` of its packets.  Priority safety leaves all other old
packets unchanged and introduces at most `beta_0` boundary packets.  Hence

\[
 n'\le n-(n/q-\delta)+\beta_0,
\]

which is (4.2).  \(\square\)

Apply Theorem 4.1 successively to `c_cent`, `u`, `omega`, and `kappa`,
requiring each later bank to preserve all earlier coordinates.  With

\[
 q=\max_j q_j,\qquad
 \delta=\sum_j\delta_j,\qquad
 \beta=\sum_j\beta_j,                               \tag{4.3}
\]

the finite defect state satisfies

\[
        \|\Pi'\|_1\le\left(1-{1\over q}\right)
                           \|\Pi\|_1+\delta+\beta.   \tag{4.4}
\]

This scalar inequality is weaker than the lexicographic phase statement but
is convenient for recursion.  Here every phase's `beta_j` bounds its total
new mass in the current and later coordinates, not only leakage back into
the coordinate being repaired.  Therefore leakage created before a later
phase is either repaired there or remains charged once; later phases create
no earlier-coordinate leakage.  This proves (4.4) by summing the four
phase inequalities.

### Corollary 4.2 (exact guarded repair)

If each priority admits one orthogonal bank satisfying full Hall, zero
boundary leakage, compatible exact cap guards, and a matching within the
reserve, then

\[
                              \Pi'=0.                \tag{4.5}
\]

The conclusion is exact physicalization, not merely zero marginal holes.

## 5. Adding the Pascal braid

Let `Pi_k` be the accepted defect state at one odd regenerative frame, and
let the next odd/even Pascal construction produce a pre-repair state
`widehat Pi_(k')`.  Suppose uniformly that

\[
       \|\widehat\Pi_{k'}\|_1
          \le\lambda\|\Pi_k\|_1+b_0.                \tag{5.1}
\]

Here `lambda` is the exact inheritance multiplicity of old obligations and
`b_0` counts new seam/collar packets.  Suppose the guarded repair bank
removes a fraction `eta` of every finite pre-repair state, up to Hall and
boundary debt `b_1`:

\[
       \|\Pi_{k'}\|_1
          \le(1-\eta)\|\widehat\Pi_{k'}\|_1+b_1.    \tag{5.2}
\]

Theorem 4.1 supplies `eta=1/q` and `b_1=delta+beta` under its hypotheses.

### Theorem 5.1 (regenerative contraction)

If

\[
                         \rho=(1-\eta)\lambda<1,     \tag{5.3}
\]

then

\[
 \|\Pi_{k'}\|_1\le\rho\|\Pi_k\|_1+
                 \underbrace{(1-\eta)b_0+b_1}_{B_0}. \tag{5.4}
\]

Along a compatible infinite regenerative spine,

\[
 \sup_k\|\Pi_k\|_1
 \le \|\Pi_{k_0}\|_1+{B_0\over1-\rho}.             \tag{5.5}
\]

If every pre-state instead satisfies Corollary 4.2 and exports a zero-defect
child state, then `Pi_k=0` identically.

#### Proof

Substitution of (5.1) into (5.2) gives (5.4).  Iterating the affine
recurrence gives the geometric series (5.5).  The last claim is induction
using (4.5).  \(\square\)

The strict inequality (5.3) is essential.  A local repair which removes
half the debt after a braid duplicates every old obligation has `rho=1` and
does not prove a constant bound.

## 6. Regenerative recompilation gives `B(k)+O(1)`

The hard host coordinate must vanish before the ordinary maximal-cap
compiler can run.  There are two proof-safe interfaces.

* **Host-exact interface:** every accepted state has `u=0`.
* **Padded-host interface:** every residual host packet has an explicit
  literal collar gadget using at most `tau` extra positions, all gadgets
  are mutually compatible, and recompiling with those gadgets exports the
  same regenerative state.

Assume one of these interfaces and constants `c_0,tau` such that an accepted
state at dimension `k` recompiles to a physicalization of length at most

\[
                 B(k)+c_0+\tau u(k),                \tag{6.1}
\]

with at most `c_cent(k)+omega(k)+kappa(k)` literal target exceptions.
Assume the protected state needed for both Pascal children is exported again.

### Theorem 6.1 (constant-additive consequence)

Under Theorem 5.1 and the recompilation hypothesis,

\[
                         \nu(k)\le B(k)+O(1)         \tag{6.2}
\]

uniformly along the odd spine and its even children.  More explicitly, with

\[
 C=\|\Pi_{k_0}\|_1+{B_0\over1-\rho},               \tag{6.3}
\]

one has

\[
                         \nu(k)\le B(k)+c_0+(\tau+1)C. \tag{6.4}
\]

If the host-exact zero-defect form has `c_0=0`, then

\[
                         \nu(k)=B(k).                \tag{6.5}
\]

#### Proof

Theorem 5.1 bounds `c_cent+u+omega+kappa` by `C`.  Apply the bounded-defect
completion theorem to the recompiled word: append one singleton letter for
each of the `c_cent+omega+kappa` exceptional masks.  This costs at most
`c_0+tau*u+c_cent+omega+kappa`, bounded by the right side of (6.4).
Recompilation is fresh at each child dimension, so the additive bound does not accumulate
with the length of the spine.  At zero defect, the resulting upper bound
`B(k)` meets the proved deadline lower bound.  \(\square\)

The padded-host interface is a substantive hypothesis.  Merely appending
the missing row bit as a target letter does not repair a failed derivative
row.

## 7. Calibration

### 7.1 Frozen `K16` equality word

The authenticated word `answers/k16.word` has length `B(16)=12873` and
literal coverage `65535/65535`.  Its endpoint-rerooted carrier has:

```text
exact middle ownership and complete upper coverage,
three omitted starts and three omitted deadlines,
one fixed top singleton,
26331 residual lower targets,
32229 available cells,
one exact common cap,
Pi = (0,0,0,0).
```

Thus `K16` validates the terminal recompilation conclusion with `c_0=0`.
The cap/facet bridge also demonstrates that a small component plus its
four-row cut halo can be rebuilt without paying two parent compiler halos.
It does **not** prove a switch-bank Hall expansion, bounded guard overlap, or
regeneration into `K17`; those are precisely the hypotheses above.

### 7.2 Current `K17` fixed skeleton

For the connected OPTIMAL28 zipper,

```text
unpacketized hard host obligations                 3759
upper holes at ranks 10/11/12             1900/911/128
combined short-cell reserve if all holes are paid           354
central/palette coordinate                              0
common-cap coordinate                         undefined (u>0).
```

The fixed residual-pair atlas has `141255` owner-pair columns, but local
column abundance is irrelevant to the contraction hypothesis:

* `141` unselected macro interiors carry `227` immutable facet-run defects;
* the union of every relaxed residual-pair provider still has `218`
  unsupported rank-ten targets.

Taking those `218` targets as `X` in (3.1) gives \(N(X)=\varnothing\) and Hall
deficiency at least `218`.  The immutable host packets likewise have no
column in the fixed atlas.  Hence neither the exact nor contractive theorem
applies to residual incidence rectangles on this skeleton.  The next live
input must be a regenerated macro/occurrence/nonflat option bank which
changes those interiors and exports the full column state of Section 2.

A newer occurrence catalogue gives a more precise but still negative
calibration.  It contains `438` genuinely full-safe columns (`441` raw
columns minus three which consume selected empty-port components).  On the
complementary-owner subledger with baseline `724`, the best single column
only reaches `718`; three upper-friendly columns reach `719` while adding
two rank-ten holes.  These figures prove that useful local directions exist,
but they do **not** give an orthogonal layer cover, Hall expansion, affordable
joint cost, or any numerical `rho<1`.  In particular, no contraction rate is
inferred from the single-column improvement.

This is useful negative calibration: the obstruction is failure of a named
hypothesis, not evidence against the contraction theorem or against
`nu(17)=B(17)`.

## 8. Exact missing all-dimension statement

The strongest concise theorem now sufficient for a constant additive bound
is:

> **Uniform regenerative guarded-switch contraction.**  Along one compatible
> odd Pascal spine, every child pre-state has a proof-safe actuator atlas
> whose support-conflict graph admits uniformly bounded orthogonal layers,
> whose layer graphs have uniformly bounded Hall deficiency and affordable
> min-cost maximum matchings, whose provider tickets and five-row cap guards
> are preserved, whose boundary leakage is uniformly bounded, and whose
> inheritance/repair constants satisfy `(1-eta)lambda<1`.  The accepted
> state admits uniform regenerative recompilation.

The zero-defect strengthening replaces bounded deficiency/leakage by full
Hall and zero leakage.  It implies the exact formula.

Nothing presently proves this statement.  Its advantage is falsifiability:
every phrase corresponds to a literal column field, a conflict edge, a Hall
cut, a cost, or a replayed child state.

## 9. Dependencies and nonclaims

This note uses the exact switch monoids and cap transport from

```text
MATH_THEOREM_K17_TWO_BANK_SWITCH_MONOIDS_AND_GUARDED_REPAIR_HALL_20260731.md
```

and the bounded-defect completion implication from

```text
MATH_THEOREM_ALLK_OWNER_FACTOR_BOUNDED_DEFECT_PHYSICALIZATION_20260731.md
```

It proves the conditional implications (0.1)--(0.3).  It does not prove the
uniform actuator atlas, the contraction inequality for the actual Pascal
transition, a `K17` word, or an unconditional `B(k)+O(1)` theorem.
