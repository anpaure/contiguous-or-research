# Fixed-`z` completed tickets: collar-kernel thinning, topology, and postselected cap backups

**Date:** 2026-08-02  
**Lane:** A, bounded-load heptagonal regeneration  
**Status:** exact conditional subatlas theorem and sharp one-resource
obstruction.  No unconditional history-collar supply theorem is claimed.

## 0. Result

For a private rooted task, the fixed-`z` heptagon atlas has

\[
 N_{k,r}=(r-1)(r-2)(k-r)_4(k-r-4)=\Theta(k^7)             \tag{0.1}
\]

central choices in the central regime, and every nonanchor central resource
has load `O(k^6)`.  Voltage localization means that, after one protected
coprime-voltage seed, these zero-holonomy packets need no separate voltage
choice: a topology-safe one-cycle rethread preserves the inherited voltage.

The central load bound does **not** by itself survive the attachment of
`O(d)` history collars.  It does survive under either of two exact,
checkable hypotheses:

1. a bounded central-decoding certificate for every collar resource; or
2. the more general normalized collar-menu load bound of Theorem 2.1.

Under either hypothesis there is a completed fixed-`z` subatlas with
`Theta(k^7)` tickets, `O(d)` resources per ticket, and `O(k^6)` load on every
nonanchor central, history, and topology-port resource.  Hence fixed `H`
tasks pack greedily when `Hd=o(k)`.

Named duplicate-cap providers are then chosen **after** the completed
tickets.  They require no cap-provider load hypothesis.  This postselection
is a literal physical `ML_m` theorem; it does not extend a fully developed
cyclic quotient packet, and its arbitrary two-factor completion does not
preserve a prescribed one-cycle topology unless that topology is supplied by
a separate in-place or connected-completion theorem.

## 1. Central atlas and completed collars

Let `Z_t` be the fixed-`z` atlas for one private task anchor `t`.  Write
`C(Z)` for the nonprivate central resources of `Z`.  The frozen central
theorem supplies constants `c_0,C_0>0`, independent of `k`, such that

\[
 |Z_t|\ge c_0k^7,
 \qquad
 \max_a |\{Z\in Z_t:a\in C(Z)\}|\le C_0k^6.             \tag{1.1}
\]

Here resources mean literal owner, facet, cap, or selected row occurrences
on the physical face under consideration.  The private anchor skeleton is
not a cross-task resource and is omitted from (1.1).

Fix an admitted incoming bi-history state `omega`.  For `Z in Z_t`, let
`M_omega(Z)` be its finite menu of **complete collar realizations**.  A menu
member must already certify all of the following:

* the forward and reverse depth-`d` entrance and exit relations, including
  reset entrance guards and whole-component tokens;
* every literal source/compiler incidence and protected upper witness which
  the ticket claims to retain;
* the seven old seams on one directed quotient cycle in the retained-path
  order needed by the odd step-two rethread;
* one directed output quotient cycle; and
* zero seam displacement.

Thus topology and zero holonomy are admission tests, not conclusions of the
load estimate.  Every claimed physical incidence must be included in the
protected bank of the menu member.  Assume

\[
 |\operatorname{supp}(Z,M)|\le S_d\le A_s d+B_s.         \tag{1.2}
\]

Let

\[
 Z_t(\omega)=\{Z\in Z_t:M_\omega(Z)\ne\varnothing\}.     \tag{1.3}
\]

Positive completed-ticket supply is the separate hypothesis

\[
                         |Z_t(\omega)|\ge c_1k^7.        \tag{1.4}
\]

Raw central abundance does not imply (1.4).

## 2. Exact collar-kernel theorem

For a noncentral occurrence-labelled resource `q`, define its normalized
menu load

\[
 \Lambda_\omega(q)=
 \sum_{Z\in Z_t(\omega)}
 { |\{M\in M_\omega(Z):q\in\operatorname{supp}(Z,M)\}|
   \over |M_\omega(Z)|}.                                \tag{2.1}
\]

This is the expected load of `q` if one collar is chosen independently and
uniformly from each nonempty menu.

### Theorem 2.1 (normalized-menu thinning)

Assume the physical resource universe has size at most `exp(C_R k)` and

\[
                    \Lambda_\omega(q)\le C_1k^6          \tag{2.2}
\]

for every noncentral collar or topology resource `q`.  Then, for all
sufficiently large `k`, one may choose one `M_Z in M_omega(Z)` for every
`Z in Z_t(omega)` so that every nonprivate resource has completed-ticket
load at most

\[
 C_*k^6,
 \qquad
 C_*:=\max\{C_0,e^2(C_1+1)\}.                           \tag{2.3}
\]

Consequently the selected completed-ticket subatlas has size at least
`c_1k^7` and support at most `S_d=O(d)` per ticket.

#### Proof

Choose the menu member for each `Z` independently and uniformly.  For a
fixed noncentral resource `q`, its load `X_q` is a sum of independent
Bernoulli variables and

\[
                         E X_q=\Lambda_\omega(q)\le C_1k^6.
\]

Put `T=e^2(C_1+1)k^6`.  The standard binomial tail estimate gives, whenever
the mean is nonzero,

\[
 P(X_q\ge T)
 \le \left({eE X_q\over T}\right)^T
 \le e^{-T}.                                             \tag{2.4}
\]

For zero mean the probability is zero.  A union bound over at most
`exp(C_R k)` resources is strictly below one for all sufficiently large
`k`, since `T-C_Rk -> infinity`.  Hence one simultaneous choice has all
noncentral loads at most `T`.  Choosing one collar per central packet does
not change which central resources it contains, so (1.1) bounds their load
by `C_0k^6`.  This proves (2.3). \(\square\)

The exponential resource-universe bound is harmless for Boolean packets:
all subset masks, directions, bounded roles and occurrence types together
form `exp(O(k))` possibilities.

### Corollary 2.2 (bounded central decoding)

Suppose there is an absolute constant `w` and, for every collar resource
`q`, a set `W(q)` of at most `w` nonanchor central resources such that

\[
 q\in\operatorname{supp}(Z,M)
 \quad\Longrightarrow\quad
 C(Z)\cap W(q)\ne\varnothing                           \tag{2.5}
\]

for every admitted `(Z,M)`.  Then **every** choice of one admitted collar
per central packet has collar load at most `wC_0k^6`; no random thinning is
needed.

#### Proof

Every ticket using `q` belongs to the union, over `a in W(q)`, of the
central tickets using `a`.  Apply (1.1) and the union bound. \(\square\)

Condition (2.5) is the most useful local audit target: a history occurrence
must recover one of only `O(1)` central owner/facet/row tokens.  Recovery only
after guessing one of `d` collar offsets yields merely `O(dk^6)` load and is
not enough for the sharp `Hd=o(k)` packing scale.

## 3. Fixed-task packing

### Theorem 3.1 (completed fixed-`z` transversal)

Assume Theorem 2.1 uniformly for each of `H` private task families and that
all capacity-one physical collisions are represented among the ticket
resources.  Then the families admit one pairwise compatible completed ticket
each whenever

\[
       c_1k^7>(H-1)S_dC_*k^6.                            \tag{3.1}
\]

In particular, selection succeeds when

\[
                         Hd=o(k).                        \tag{3.2}
\]

#### Proof

Choose the task families successively.  One selected ticket contains at most
`S_d` nonprivate resources.  Each such resource occurs in at most `C_*k^6`
tickets of a later family, so one selection excludes at most
`S_dC_*k^6` later candidates.  Before the last choice, the right side of
(3.1) is an upper bound on all exclusions.  Greedy selection works.
\(\square\)

The topology part is exact: every admitted ticket is already a one-cycle
step-two rethread of zero seam displacement.  The voltage-localization
theorem therefore preserves the one coprime voltage carried by the protected
seed at every serial prefix.  Topology-port occurrences still count in
`S_d` and (2.2); zero holonomy removes only a separate voltage-choice load.

## 4. Postselected cap backups

Let the selected ticket `g_i` have a protected physical incidence bank
`P(g_i)` of at most `ell_d` edges and name at most `q_d` old cap occurrences
which need duplicate witnesses.  Put

\[
 P=\bigcup_{i=1}^H P(g_i),\qquad
 L=|E(P)|\le H\ell_d,\qquad q\le Hq_d.                  \tag{4.1}
\]

### Theorem 4.1 (postselection removes cap-provider load)

If

\[
 {m+1-H\ell_d-2Hq_d\choose2}>H\ell_d+Hq_d              \tag{4.2}
\]

and

\[
                       H\ell_d+2Hq_d\le m-2,            \tag{4.3}
\]

then one may choose all named provider paths after the completed tickets,
pairwise vertex-disjoint and disjoint from `P`, and extend their union to a
spanning owner/facet two-factor.

#### Proof

The crude bounds `v_O(P),v_F(P)<=L` turn (4.2) into the greedy provider
inequality.  Every provider adds two incidence edges, and (4.3) is exactly
the small protected-factor budget. \(\square\)

Thus cap-provider sockets, provider-versus-collar conflicts, and provider
per-resource loads do not belong in (2.2).  Only the **names and number** of
the endangered cap occurrences remain in the ticket state.  If
`ell_d,q_d=O(d)`, `d=Theta(sqrt(m))`, and `H` is fixed, (4.2)--(4.3) hold for
all sufficiently large `m`.

For the pure fixed-`z` central heptagon the immediate cap multiset is already
exact, so its central contribution to `q_d` is zero.  The allowance in
Theorem 4.1 is for cap debts introduced by collars, source guards, or other
attached terminal data.

The conclusion of Theorem 4.1 is deliberately static.  The arbitrary
protected completion can have many components, can attach the provider-path
endpoints with rejecting history states, and need not realize the retained-
fragment order used in Theorem 3.1.  Consequently Theorem 3.1 and Theorem
4.1 may be combined without an additional argument only on the owner/facet
and named-cap support rows.  A final connected resident carrier still needs
an in-place host, a connected protected completion, or a subsequent
resource-returning topology/history repair.

## 5. Sharp failure without a collar kernel

### Proposition 5.1 (one-resource concentration obstruction)

Neither `Theta(k^7)` central supply, `O(k^6)` central load, nor an `O(d)`
collar size implies (2.2).  There is an extension system satisfying all
three in which every completed ticket has one mandatory common collar
resource `q_*`.  Then

\[
       \operatorname{load}(q_*)=|Z_t(\omega)|=\Theta(k^7). \tag{5.1}
\]

#### Proof

Attach the same formal mandatory resource `q_*` to the unique collar menu of
every central ticket.  This does not alter any central token or its load and
adds only one resource per ticket. \(\square\)

The obstruction has exactly the incidence form of a common history boundary
or topology port; no claim is made here that the current Boolean fixed-`z`
atlas realizes this worst case.  Postselected cap providers cannot repair
it.  A positive construction must either prove (2.1), make the common
resource private to the task anchor, or replace the primitive by a compound
packet which returns that resource internally.

If the best audit gives only `O(dk^6)` collar load, the naïve conflict bound
becomes `O(d^2k^6)`.  At `d=Theta(sqrt(k))` the supply/conflict ratio is only
`Theta(1)`, so no dimension-growing slack follows.

## 6. Physical versus quotient development

Theorems 2.1--4.1 are literal physical statements when their resources are
physical occurrences.

For an equivariant quotient ticket, a selected quotient row develops through
all `n` phases.  Its protected bank then has `Theta(n d)` physical incidence
edges, not `O(d)`.  In particular a developed heptagon already has `14n`
central incidence edges.  Therefore the literal protected-factor condition
`L+2q<=m-2` cannot be applied to a full free `Z_(2m-1)` development.

There are two proof-safe quotient uses.

1. Work orbitwise inside an already existing equivariant factor and require
   every packet to be an exact in-place symmetric difference.  Then (2.1)
   must be audited with orbit-capacity resources and stabilizer weights;
   Theorem 4.1 is not invoked.
2. Prove a new quotient-equivariant protected-extension theorem.  No such
   theorem is supplied here.

On the first face, a free-orbit ticket has `O(d)` resource **orbits**, and an
orbitwise version of Theorems 2.1--3.1 is valid if the normalized load bound
is proved for those orbit resources.  Freeness of owner orbits does not imply
freeness of cap or deeper-shadow orbits, so unweighted quotient cap rows are
not generally valid.

## 7. Exact remaining theorem

After voltage localization and cap-provider postselection, the sole local
spread statement is:

\[
 \boxed{
 \begin{array}{c}
 \text{for every admitted bi-history state, a positive fraction of the}\\
 \text{fixed-`z` central atlas has accepting one-cycle collars satisfying}\\
 \text{the normalized load bound (2.2), or the decoder condition (2.5).}
 \end{array}}
                                                               \tag{7.1}
\]

This includes source/compiler incidences and protected upper witnesses only
when they are literal members of the collar support.  Global upper
surjectivity, deeper unprotected shadows, the construction or transport of
the exceptional coprime-voltage seed, growing-depth history reset, and the
terminal common compiler remain separate.

## 8. Provenance

This note uses:

* `MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`;
* `MATH_THEOREM_COPRIME_VOLTAGE_LOCALIZATION_AND_ZERO_HOLONOMY_REPAIR_20260802.md`;
* `MATH_THEOREM_HEPTAGON_PROTECTED_HOST_AND_DUPLICATE_CAP_BACKUPS_20260802.md`;
* `MATH_THEOREM_A_HEPTAGONAL_CAP_BACKUP_AND_BIHISTORY_TICKET_INTERFACE_20260802.md`; and
* `MATH_THEOREM_A_EQUIVARIANT_DIRECTED_HISTORY_EAR_SEMIGROUPOID_AND_PULL_TRANSPORT_20260802.md`.

No finite search, SAT result, or marginal-overlap assumption is used.
