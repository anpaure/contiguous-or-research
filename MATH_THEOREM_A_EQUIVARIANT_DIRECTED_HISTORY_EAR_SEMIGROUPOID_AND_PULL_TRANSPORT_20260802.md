# Equivariant directed histories as a closed pull-ear state

**Date:** 2026-08-02  
**Lane:** A, integration of the `k=17` directed-history master with the
regenerative pull/packet theorem  
**Status:** unconditional state-algebra theorem and exact conditional pull
transport theorem.  This is not an existence theorem for a negative circuit,
a SAT verdict, or an all-`k` construction.

## 0. Verdict

The three canonical-frame labels in the frozen `k=17` master are not merely
a compact list of residence blockers.  They are the `d=3` instance of an
exact framed shift-register state.

For every odd Middle-Levels dimension and every fixed depth `d`:

1. directed owner transitions act on the last-`d` insertion history by a
   phase-covariant shift;
2. directed ears compose as finite weighted transformations;
3. the zero-cost face is exactly positive depth-`d` residence;
4. a `C6/C8` re-pairing is checked by composing only its retained-ear and
   connector transformations;
5. a co-oriented pull changes history only on the first `d` successors of
   each changed connector; and
6. an orientation-free ear must export both past-insertion and
   future-deletion histories.  One-sided history is not reversal-closed.

Thus the finite history state can replace raw run-blocker lists in the
closed-packet theorem.  It does **not** manufacture a negative packet or make
history costs scalar.  The previous two-pull/MST descent applies only after a
common history, or an exact context-independent history relation, proves
additivity.

The interface is dimension-uniform in form but not bounded in depth.  It
uses `d` coordinate registers per owner.  There is no transition-equivariant
section from depth `d` to depth `d+1`; a growing-depth induction must export
one new oldest label, retain a longer bidirectional buffer, or pass through a
genuine history-reset ear.

Upper `q1` is carried only by a separate literal cap-multiset identity.
Deeper shadows, source/erosion, and the common compiler remain separate.

## 1. The odd quotient has canonical phase

Put

\[
                            q=2r-1,
\]

and let `rho` generate the cyclic action on the `q` coordinates.  Every
rank-`r` owner necklace is free under this action.

### Lemma 1.1 (freeness of the owner action)

Every physical rank-`r` owner has a unique expression

\[
                         \rho^g S_u,\qquad g\in\mathbb Z_q,       \tag{1.1}
\]

relative to the chosen canonical representative `S_u` of its necklace.

#### Proof

If a binary word of length `q` has a proper rotational period, it is the
concatenation of `s>1` equal blocks, where `s` divides `q`.  Its weight is
then divisible by `s`.  For a rank-`r` owner this would make `s` divide both
`q=2r-1` and `r`, contradicting

\[
                              \gcd(2r-1,r)=1.
\]

Hence the orbit is free and (1.1) is unique.  \(\square\)

A directed quotient dart `e:u->v` therefore has a literal record

\[
                  e=(u,v;a_e,\beta_e,\delta_e),                    \tag{1.2}
\]

where:

- `a_e` is the coordinate deleted in the canonical frame at `u`;
- `beta_e` is the coordinate inserted in the canonical frame at `v`; and
- `delta_e` is the phase change from `u` to `v`.

Thus a source-frame label `x` is read in the target frame as

\[
                         \varphi_e(x)=x-\delta_e\pmod q.           \tag{1.3}
\]

For the `k=17` builder, the raw inserted label `b` is stored in the source
frame, so

\[
                              \beta_e=b-\delta_e.                  \tag{1.4}
\]

The physical endpoints determine the reverse dart.  It must be recomputed
in the reverse source frame; naively swapping the two stored source-frame
labels is not proof-safe.

The freeness statement is specific to the owner rank.  A rank-`(r+1)` cap
orbit can be shortened because

\[
                       \gcd(2r-1,r+1)=\gcd(3,r+1).                 \tag{1.5}
\]

Consequently upper-`q1` preservation must remain a literal physical
multiset calculation; quotient orbit counts alone are insufficient.

## 2. The framed history shift register

Let

\[
                         \mathcal H_d=(\mathbb Z_q)^d.
\]

At owner orbit `u`, write

\[
                         h(u)=(h_1(u),\ldots,h_d(u)),               \tag{2.1}
\]

where `h_j(u)` is the coordinate inserted `j` owner transitions before
reaching the current physical occurrence, expressed in the canonical frame
of `S_u`.  The most recent insertion is `h_1`.

For a dart (1.2), define the total update

\[
 U_e(h_1,\ldots,h_d)
   =\bigl(\beta_e,\varphi_e(h_1),\ldots,
                    \varphi_e(h_{d-1})\bigr)                       \tag{2.2}
\]

and the event cost

\[
 \kappa_e(h)
   =\mathbf 1\!\left[a_e\in\{h_1,\ldots,h_d\}\right].           \tag{2.3}
\]

The hard residence transition is the restriction of `U_e` to the states
with `kappa_e(h)=0`.

### Theorem 2.1 (exact directed-history theorem)

Let `F` be an equivariant directed quotient cycle cover.  Then the actual
last-`d` insertion labels give a canonical assignment `h(u)` satisfying

\[
                             h(v)=U_e(h(u))                         \tag{2.4}
\]

on every selected dart `e:u->v`.  Moreover,

\[
               \Phi_{d,\mathrm{orb}}^{\rm ev}(F)
                 =\sum_{e\in F}\kappa_e(h(s(e)))                  \tag{2.5}
\]

is exactly the number of bad event-bearing **transition orbits**.  Because
the owner action is free, the number of bad physical occurrences in the full
development is

\[
                         q\,\Phi_{d,\mathrm{orb}}^{\rm ev}(F).     \tag{2.6}
\]

In particular, all hard transitions are legal if and only if every positive
run on every physical component has length at least `d+1`.

#### Proof

Equation (2.2) simply prepends the current insertion and transports the
previous labels to the target frame.  A coordinate deleted on `e` has a
positive run of length at most `d` exactly when its most recent insertion is
one of the preceding `d` transitions, which is exactly (2.3).  This proves
(2.4) and (2.5) for every nonconstant coordinate trace.

It remains to check a coordinate constant-present on an entire physical
component `C`.  Its run length is `|C|`.  If `|C|>=d+1`, that run is legal.
If `|C|<=d`, choose any transition of `C`, inserting a coordinate `y`.
Because the component closes, `y` is deleted within the following
`|C|<=d` transitions, so (2.3) detects a short event-bearing run on `y`.
Thus zero total event cost already excludes every short component, and every
constant-present run on an accepted component is long enough.  \(\square\)

The equality in (2.5) is an event-bearing count.  For a quantitative
potential that counts every bad coordinate run separately, retain the
whole-component token from the capped-age theorem:

\[
 \widehat\Phi_d(C)
   =\Phi_d^{\rm ev}(C)
      +\mathbf 1_{|C|\le d}\,|K^+(C)|,              \tag{2.7}
\]

where `K^+(C)` is the set of coordinates constant-present on `C`.  The token
is redundant for zero-versus-positive feasibility, but is load-bearing for
exact weights and for topology-changing intermediate factors.  If negative
residence is also required, add the dual deletion history and the
constant-absent token.

### Corollary 2.2 (phase-free quotient closure)

No phase variable at a quotient owner is needed.  If a quotient component
has `c` owner orbits and total voltage `Delta`, then its physical components
have length

\[
                    \frac{cq}{\gcd(q,\Delta)}.                     \tag{2.8}
\]

After one quotient revolution the physical phase and every absolute history
label are shifted by the same `Delta`; expressing the labels in the new
canonical frame gives the same state (2.1).  A connected physical lift needs

\[
                             \gcd(q,\Delta)=1.                     \tag{2.9}
\]

For `q=17`, this is simply `Delta!=0`.

## 3. Weighted ear semigroupoid

For a directed ear

\[
                              P=e_1e_2\cdots e_t,
\]

put

\[
 U_P=U_{e_t}\circ\cdots\circ U_{e_1},\qquad
 C_P(h)=\sum_{i=1}^t\kappa_{e_i}(h_{i-1}),          \tag{3.1}
\]

where `h_0=h` and `h_i=U_(e_i)(h_(i-1))`.  Equivalently, define the tropical
matrix

\[
 M_P(\alpha,\beta)=
 \begin{cases}
   C_P(\alpha),&U_P(\alpha)=\beta,\\
   +\infty,&\text{otherwise}.
 \end{cases}                                                       \tag{3.2}
\]

Endpoints live in specified canonical frames, so these matrices are
morphisms of a finite weighted semigroupoid.

### Theorem 3.1 (literal ear composition)

For composable ears `P,Q`,

\[
                  M_{PQ}=M_P\otimes M_Q,                            \tag{3.3}
\]

where `otimes` is min-plus matrix multiplication.  A closed directed
component `C` has exact event-bearing debt

\[
                       \min_{h\in\mathcal H_d}M_C(h,h),             \tag{3.4}
\]

and is resident exactly when this value is zero.  For the full weighted
potential, develop the quotient component and add the physical
whole-component term (2.7).

#### Proof

Both the output state and the accumulated cost in (3.1) are obtained by
ordinary sequential scanning.  Splitting that scan at the `P,Q` boundary
gives (3.3).  A cyclic history is precisely a fixed boundary state, giving
(3.4); Theorem 2.1 gives the residence equivalence.  \(\square\)

The full `q^d` matrix need not be materialized.  A proof-safe `O(d)`
**event-history** collar representation stores:

1. the first `d` framed deletion/insertion transitions;
2. the last `d` framed insertion transitions;
3. the total frame transport;
4. the input-independent event debt whose preceding `d` insertions are all
   internal.

Every guard after the first `d` transitions depends only on internal
insertions, and every output register after `d` transitions is supplied
internally.  Therefore those data reconstruct all cross-boundary event costs
and the output state exactly.  Full quantitative residence additionally
retains, in the literal fragment/topology ledger,

\[
              \min(|P|,d+1),\qquad
              K^+(P)=\bigcap_{T\text{ owner of }P}T,               \tag{3.5}
\]

so that a newly closed component's length and constant-present core can be
formed.  The core is a `q`-bit datum, not part of the `O(d)` event collar.

### Corollary 3.2 (tail reset)

If `P` has at least `d` transitions, `U_P(h)` is independent of `h`: it is
the last `d` insertions of `P`, transported into the exit frame.  The costs
of the first `d` transitions can still depend on the input state.  Thus a
long ear is an output reset, not automatically a universally admissible
reset.

## 4. Reversal requires bi-history

A one-sided insertion history is composition-closed for co-oriented ears,
but not under arbitrary fragment reversal.  Define

\[
 k(u)=(k_1(u),\ldots,k_d(u)),                        \tag{4.1}
\]

where `k_j(u)` is the coordinate deleted on the `j`th future transition
from `u`, expressed in the canonical frame at `u`.  On a dart `e:u->v`,

\[
 k_1(u)=a_e,\qquad
 k_j(v)=\varphi_e(k_{j+1}(u))\quad(1\le j<d).        \tag{4.2}
\]

Call

\[
                              \Omega(u)=(h(u),k(u))                 \tag{4.3}
\]

the **bi-history socket**.

### Theorem 4.1 (reversal involution)

Global orientation reversal acts by

\[
                         J(h,k)=(k,h),\qquad
                         \Delta\longmapsto-\Delta.                 \tag{4.4}
\]

For a compressed ear `P`, an orientation-free exact signature is

\[
                   \Sigma_d(P)=\bigl(M_P,M_{\overleftarrow P}\bigr),             \tag{4.5}
\]

where the reverse matrix is built from the literal reverse darts.  Then

\[
 \Sigma_d(PQ)=
 \bigl(M_P\otimes M_Q,
       M_{\overleftarrow Q}\otimes M_{\overleftarrow P}\bigr).    \tag{4.6}
\]

#### Proof

In reverse orientation, the past insertions are exactly the forward future
deletions, in the same nearest-first order; the reverse future deletions are
the forward past insertions.  Voltage changes sign.  This proves (4.4).
The reverse of `PQ` is the reverse of `Q` followed by the reverse of `P`,
which proves (4.6).  \(\square\)

A one-transition ear already shows why `M_P` alone is insufficient as an
orientation-free socket.  Its forward shift erases the oldest input history
coordinate, while the reverse input depends on the next exterior deletion,
which the forward output does not determine.

On a complete directed cycle, `k` adds no new feasibility constraint: it is
read from the future of the already selected cycle.  It is essential only
when ears are opened, stored, reversed, and re-paired.

## 5. Exact pull-ear transport

Consider a fixed occurrence-labelled `C6/C8` pull packet.  Delete its old
selected incidences, obtaining oriented retained ears, and add its new
physical connector darts.  Use the port-permutation formula for component
topology and the literal dart voltages for phase.

### Theorem 5.1 (history-closed pull criterion)

The packet transports a positive depth-`d` history state exactly if and only
if the following hold.

1. Every new connector is a physical dart with definite source/target
   frames, labels, and voltage.
2. The retained ears and new connectors admit compatible bi-history sockets
   at every port.  A reversed ear uses its reverse morphism from (4.5).
3. On every output component, the composed morphism has a cyclic fixed
   state.  Its event-bearing cost is (3.4), and the full cost includes the
   developed whole-component term (2.7).
4. Every prescribed exterior socket is returned literally, or is transported
   according to a separately stated boundary relation.

These rows are necessary and sufficient for the history/residence part of
the fixed-fragment packet.  The packet is a negative accepting packet for
the current construction only after separately checking:

5. legal factor degrees, protected resources, component topology, and lift
   voltage;
6. equality of the **final** physical upper-`q1` cap multiset; and
7. negative full history-plus-component cost.

For overlapping two-pull packets, neither cap deltas nor history costs are
automatically additive.  The final union collar and final turn-neighbour
multiset must be replayed.  Per-pull addition is justified only on a prepared
disjoint-incidence face.

#### Proof

Theorem 3.1 gives exact directed-ear composition, Theorem 4.1 gives the
reverse orientation, and fixed points close the output components.  The
remaining rows are precisely the independent factor, voltage, protected,
and cap resources.  No other residence datum exists on the fixed literal
fragment table.  \(\square\)

### Corollary 5.2 (bounded co-oriented collar)

Suppose no retained ear is reversed and `s` connector darts change.  Relative
to an incumbent history assignment, histories can change only on the first
`d` owner occurrences downstream of the new connector heads.  Everywhere
else the shift register has seen `d` unchanged internal insertions and has
forgotten the old boundary.  Hence at most `sd` occurrence rows require
history reconstruction: at most `3d` for one `C6`, `4d` for one `C8`, and
twice these bounds for two pulls before overlap is removed.

The cost delta is supported on those successor rays together with the
changed connector tails.  If a retained ear reverses, its histories can
change throughout; the bi-history relation, not a bounded one-sided collar,
is then mandatory.

## 6. Fixed-history circuits and prepared-tree descent

Every directed factor, resident or not, has its literal canonical history
assignment `h`.  Freeze such an assignment and define the compatible dart
graph

\[
 G_h=\{e:u\to v: U_e(h(u))=h(v)\}.                  \tag{6.1}
\]

### Theorem 6.1 (fixed-history circuit lemma)

Every directed one-factor contained in `G_h` returns the exact history `h`.
Its event-bearing debt is the linear dart cost

\[
                 \Phi_{d,\mathrm{orb}}^{\rm ev}(F)
                    =\sum_{e\in F}\kappa_e(h(s(e))).              \tag{6.2}
\]

If a circuit replaces dart set `A^-` by `A^+`, both sets lie in `G_h`, and
the result remains a directed factor, then

\[
 \Delta\Phi_{d,\mathrm{orb}}^{\rm ev}
   =\sum_{e\in A^+}\kappa_e(h(s(e)))
       -\sum_{e\in A^-}\kappa_e(h(s(e))).           \tag{6.3}
\]

Add the explicit whole-component-token delta for `widehat_Phi_d`.  Thus the
circuit is a literal negative accepting packet whenever it also returns the
protected ledger, topology/voltage, exterior sockets, and the exact cap
multiset.

#### Proof

Membership in `G_h` is exactly the transition equality (2.4), so `h` is a
consistent history on every selected component.  Equation (2.5) then gives
(6.2), and subtraction gives (6.3).  \(\square\)

This lemma makes the previous prepared-tree additivity hypothesis
checkable.  Suppose:

- every forest state uses darts in one common `G_h`;
- pull supports are dart-disjoint, or have an explicitly additive
  symmetric-difference ledger;
- whole-component tokens are zero or assigned additively; and
- protected and physical cap ledgers return exactly.

Then

\[
 \widehat\Phi_d(F_S)
    =\widehat\Phi_d(F_0)+\sum_{e\in S}w_e             \tag{6.4}
\]

is a theorem, with `w_e` given by the local dart and component-token delta.
The two-pull fundamental-tree exchange from the prepared pull theorem
therefore preserves the complete history state and changes residence by
`w_f-w_e`.

Without a common transported history, the weight of a connector depends on
its input socket: already for `d=1`, a dart deleting `a` has cost one at
`h_1=a` and zero at `h_1!=a`.  The exact replacement is a
relation-labelled gluing-tree dynamic program using (3.3), not an ordinary
minimum spanning tree.  Finite history closes the state interface; it does
not prove positive circuit supply.

The radius-`(2d)` literal collar hypothesis in the previous theorem already
fixes the same past and future data as `Omega=(h,k)`.  The present result
compresses it to the exact socket relation and local cost; it does not make
that relation automatically context-independent.

## 7. State growth and the no-section obstruction

The symbolic update law is uniform in `q,d`, and uses `d` coordinate
registers per owner.  A one-hot formulation has

\[
            O(|V|dq)\text{ history variables},\qquad
            O(|E|dq)\text{ local transport clauses}.              \tag{7.1}
\]

The semantic state space has size `q^d`.  On a zero-debt rank-`r` owner, the
last `d` inserted coordinates are distinct and still present, so there are

\[
                              (r)_d=\frac{r!}{(r-d)!}              \tag{7.2}
\]

ordered zero-debt histories.

### Theorem 7.1 (no bounded-depth history state)

For `d<=r-1`, any deterministic boundary interface recognizing all legal
depth-`d` histories at a fixed rank-`r` owner has at least

\[
                              {r\choose d}                         \tag{7.3}
\]

distinguishable states.  In particular, the three-register `k=17` state is
not an all-depth bounded state.

#### Proof

Fix an owner `T`.  For every `d`-subset \(A\subset T\), use `d` distinct
buffer coordinates outside `T` and insert the elements of `A` one by one,
deleting the buffers, to reach `T` with recently inserted set `A`.  If
`A!=B`, choose `x` in their symmetric difference.  The legal next Johnson
transition deleting `x` is a short-run violation for exactly the history
whose recent set contains `x`.  Thus the two histories are distinguishable.
\(\square\)

There is a sharper depth-growth obstruction.  Truncation

\[
 \pi_{d+1,d}(h_1,\ldots,h_{d+1})=(h_1,\ldots,h_d)                  \tag{7.4}
\]

commutes with the shift updates, but has no transition-compatible section.
Indeed, suppose a section had the form

\[
 s(h_1,\ldots,h_d)=(h_1,\ldots,h_d,f(h_1,\ldots,h_d)).             \tag{7.5}
\]

For one dart with insertion `beta` and frame map `varphi`, commutation would
force

\[
 f(\beta,\varphi h_1,\ldots,\varphi h_{d-1})
                         =\varphi h_d.                              \tag{7.6}
\]

Choose two legal histories agreeing through `h_(d-1)` but with distinct
last entries `h_d,h'_d`.  Their depth-`d` images under the same shift are
identical, so the left side of (7.6) is identical, while the two right sides
are distinct.  This is impossible.  On the zero-debt owner face the same
argument is physically realizable whenever `d<=r-1`, by choosing the common
`d-1` labels and the two alternatives inside one rank-`r` owner.

Therefore a same-parity induction whose deadline increases must do at least
one of the following:

1. export the new oldest history label;
2. retain a longer past/future socket; or
3. pass through a certified reset ear whose output and first-`d+1` guard
   domain are both controlled.

An ear of length at least `d+1` resets its **output** register, by Corollary
3.2, but its first `d+1` deletion guards can still depend on the incoming
state.  Output reset alone is not a regenerative theorem.

## 8. The frozen `k=17,d=3` specialization

For `q=17`, (2.2) is exactly

\[
\begin{aligned}
 h_1(v)&=b-\delta,\\
 h_j(v)&=h_{j-1}(u)-\delta\qquad(2\le j\le3),
\end{aligned}                                                       \tag{8.1}
\]

with the current deletion excluded from all three source registers.  The
frozen master contains

\[
 1430\text{ owner orbits},\quad 232\text{ protected edges},\quad
 35713\text{ residual options},\quad 71874\text{ directed darts},          \tag{8.2}
\]

and

\[
                         1430\cdot3\cdot17=72930                  \tag{8.3}
\]

one-hot history variables.  The hard CNF is the `sum kappa=0` face of the
weighted system above.

Independent audits verify the phase convention, directed degree logic,
history equations, source hashes, and exact count arithmetic.  They do not
give a SAT/UNSAT verdict for the live master.  Connectivity, nonzero voltage,
literal physical replay, ranks `11+`, source/envelopes, and the compiler
remain subsequent gates.

## 9. Exact surviving supply theorem

The finite-history master has therefore changed the form, but not the truth
status, of the all-`k` positive-supply gate.

The weakest exact target is now:

> Construct a cap- and protected-exact family of physical pull ears whose
> bi-history relations admit an accepting gluing-tree root and whose full
> history-plus-component cost decreases; or construct a common-history dart
> graph `G_h` containing a negative resource-zero circuit basis and a
> unit-voltage connected endpoint.

For a fixed depth this is a finite relation/flow problem with exact local
composition.  For growing depth it additionally needs a history-extension
or certified-reset theorem.  Neither the `k=17` CNF nor the state algebra
proves that the required ears or circuits exist.

Upper `q1` is included only when the final physical cap multiset is exactly
returned.  Deeper upper shadows, source/erosion, and compiler compatibility
are not inferred.

## 10. Frozen provenance

- `MATH_THEOREM_K17_PHASE_FREE_DIRECTED_HISTORY_MASTER_20260802.md`, SHA-256
  `b4617ba79bce723cb4fafd73bc126a82c2426ba8cd9f5eec1d52dbdf90421906`;
- `scratch/build_k17_marker58_directed_history_master_20260802.cpp`, SHA-256
  `82a20aeec38a0ebce6467c2558a1b604a32fbed26b2818d7d2575a82af75dc4a`;
- `scratch/ad_k17_directed_history_independent_audit_20260802/directed_history.independent.audit.json`,
  SHA-256
  `058ea27da915f591b7214256d7b1e4ca22a21b8c94a36eb7a125b3f0b8f74970`;
- `scratch/r2_k17_residence_master_round1_20260802/directed_history/directed_history_source_semantics.audit.json`,
  SHA-256
  `a8c800e3cb66b812bbd90843b36d90ace49854a686b44b63b0929d37a170db6d`;
- `MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md`,
  SHA-256
  `dd404a9ab078ed7fe7ea26329adecf1527ee333fbc999adfb0558cf12105176e`;
- `MATH_THEOREM_A_MIDDLE_LEVELS_PULL_EAR_GAP_MONOID_AND_PREPARED_TREE_DESCENT_20260802.md`,
  SHA-256
  `60f0248ab5e78becb26514fc780c46ed25c66caa09d59ea172e4a8b1686bce36`.

The general `d`-register recurrence itself was already present in the `k=16`
history theorem, and the preceding pull-ear theorem already supplied a
general capped-age weighted collar calculus.  The new synthesis here is the
smaller framed shift-register/tropical specialization, its forward/reverse
packaging, the fixed-`G_h` linear circuit lemma feeding prepared-tree descent,
and the exact state lower bound/no-section obstruction across a depth
increase.
