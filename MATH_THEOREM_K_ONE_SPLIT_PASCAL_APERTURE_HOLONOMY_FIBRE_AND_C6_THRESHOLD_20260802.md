# One phase-split Pascal aperture has a two-point holonomy fibre, not a free pump

**Date:** 2026-08-02  
**Status:** unconditional voltage-cover and ordered-rail theorem for the
minimal `K_(2,2)` aperture with one additional endpoint/closure option;
exact cap/bi-history/private-edge correlation; and sharp arithmetic and
simple-graph lower bounds.  No Boolean `C6` host, upper deck, source,
residence, or compiler construction is claimed.

## 0. Verdict

Adding one alleged phase-split endpoint to the minimal Pascal square does
not create a freely tunable deck phase.

There are two distinct cases.

1. If the new endpoint is meant to be another lift of the **same** literal
   ordered-rail port edge, lift uniqueness forces its landing phase.  More
   generally, the difference of two same-rail landings lies in the ordered
   rail stabilizer.  The pivot singleton rail has trivial stabilizer, so the
   second landing coincides with the first and its holonomy defect is zero.

2. If one adds a genuinely different parallel closure orbit `g`, its gain
   differs from the old closure by one fixed element `eta`.  The two legal
   branch totals are

   \[
                    w \quad\hbox{and}\quad w+\eta .       \tag{0.1}
   \]

   The branch selector is binary; `eta` is a label of the supplied port
   orbit, not a free phase variable.  After cap, positive-history,
   negative-history, topology and private-edge filtering, the actual fibre
   is an arbitrary subset of (0.1), possibly empty or a singleton.

For a neutral base `w=0`, one coherently lifted integer defect works modulo
**every** odd modulus exactly when it is `+/- 2^a`.  But the common ordered
rail does not supply such a defect.  For an arbitrary inherited `w`, no
fixed two-point menu `{w,w+eta}` is a universal tuner over odd composite
moduli, even when `eta` itself is a unit.

Moreover a nonzero phase split cannot preserve the same literal pivot
history/rail state: it translates that state.  It may export the translated
state as a separate correlated branch, but cap/history postselection cannot
turn it into a same-state transparent pump.

Consequently the one-split face does not discharge the child-native pump.
In the one-copy simple occurrence-labelled matching model, the first
state-returning face not excluded by this argument is an alternating `C6`
with a genuine internal phase/role converter (or paired boundary
converters).  A `C6` contained entirely in one
trivial-stabilizer rail still has zero holonomy, so a literal construction
must contain a genuine non-common-rail role conversion.  Whether Boolean
ports realize that accepted `C6` remains open.

## 1. Lift uniqueness and the ordered-rail stabilizer

Let `p: Gtilde -> G` be a regular cover with deck group

\[
                              A=\mathbb Z_N .             \tag{1.1}
\]

For an oriented quotient edge `e:x->y`, choose quotient vertex
representatives.  Its gain `delta(e)` means that the lift of `e` starting
at `x_g` ends at `y_(g+delta(e))`.

### Lemma 1.1 (one endpoint cannot be split inside one edge orbit)

For a fixed quotient edge orbit `e` and a fixed lifted tail `x_g`, there is
exactly one lifted edge over `e`, and hence exactly one landing occurrence
`y_(g+delta(e))`.

Thus replacing only its head by `y_(g+delta(e)+eta)` is a literal edge lift
if and only if `eta=0`.  A nonzero alternative landing requires a different
quotient edge orbit, not merely another representative of `e`.

#### Proof

This is the unique path-lifting property for a covering graph, applied to a
path of length one.  Equivalently it follows directly from the definition
of `delta(e)`.  \(\square\)

Now let `W` be the complete ordered rail carried by a port, and put

\[
                    H=\operatorname{Stab}_A(W),           \tag{1.2}
\]

where every displayed block and its position are fixed.  Let `ell_i` and
`r_j` be phases of left and right occurrences relative to a canonical
copy of `W`.

### Lemma 1.2 (same-rail landing ambiguity)

Every literal same-rail port from left occurrence `i` to right occurrence
`j` has gain

\[
                  \delta_{ij}=\ell_i-r_j+h_{ij},
                  \qquad h_{ij}\in H .                  \tag{1.3}
\]

Hence two port orbits with the same two ordered occurrence roles have gain
difference in `H`.  If `H={0}`, their gains agree.

For the pivot rail

\[
                W=(\{\rho_1\},\ldots,\{\rho_{d-1}\})   \tag{1.4}
\]

with `d>=2`, `H={0}`.  Therefore a purported second closure obtained only
by phase-splitting one endpoint of the same pivot port has zero defect.

#### Proof

Identifying the two ordered copies requires the phase difference
`ell_i-r_j`; the only ambiguity is an element fixing the complete ordered
rail.  This proves (1.3).  A deck translation fixing the singleton
`{rho_1}` fixes its coordinate, hence is the identity in the cyclic
coordinate action.  \(\square\)

The empty rail at `d=1` is exceptional and must retain its full stabilizer
state.  Nothing below silently treats it as rigid.

### Lemma 1.3 (a consistently split endpoint is only a gauge change)

Suppose one quotient vertex representative is shifted by `eta`, and every
edge incident with that occurrence is shifted consistently.  Gains of
edges entering it increase by `eta`, while gains of edges leaving it
decrease by `eta`.  Hence the voltage of every closed directed word is
unchanged.

In particular, translating the start occurrence of `P_0` while translating
the complete path occurrence and both incident seams does not pump the
Pascal output.  Translating only its closing seam leaves an uncancelled
`eta`, but then Lemma 1.1 says that seam is not a lift of the old edge
orbit: it is precisely the additional parallel orbit of Section 2.

#### Proof

The two gain changes telescope at the shifted vertex.  This is the usual
vertex-gauge invariance of voltage around a closed walk.  \(\square\)

## 2. The genuine one-parallel-closure extension

Take two co-oriented ported child paths

\[
 P_i:s_i\leadsto t_i,
 \qquad e_i:t_i\to s_i,
 \qquad w_i=\widetilde\delta(P_i)+\widetilde\delta(e_i),
                                                               \tag{2.1}
\]

using coherent integer lifts.  Let the ordinary crossed square have seams
`f_01:t_0->s_1` and `f_10:t_1->s_0`.  On the common-lift face its output
total is

\[
                             w=w_0+w_1 .                \tag{2.2}
\]

Broaden the port catalogue by one genuinely different closure orbit

\[
                         g_{10}:t_1\to s_0              \tag{2.3}
\]

with coherent integer gain defect

\[
              \eta=\widetilde\delta(g_{10})
                         -\widetilde\delta(f_{10}).     \tag{2.4}
\]

The two branches select exactly one of `f_10,g_10` as the private closure.
Selecting both is not a degree-two ported chronology.

### Theorem 2.1 (exact two-point fibre and topology)

The ordinary branch and split branch are respectively

\[
 P_0 f_{01}P_1 f_{10},
 \qquad
 P_0 f_{01}P_1 g_{10}.                                \tag{2.5}
\]

Each is one directed quotient cycle, and their coherent integer totals are
`w` and `w+eta`.  Opening at the selected last edge leaves the same directed
internal path `P_0 f_01 P_1` and exports that selected edge as the private
aperture.  The developments have respectively

\[
                 \gcd(N,w),\qquad \gcd(N,w+\eta)       \tag{2.6}
\]

physical cycles.

#### Proof

The two words differ in exactly their last edge, so subtracting their edge
sums gives (2.4).  Their projected endpoint order is identical, proving the
one-cycle and opening assertions.  The standard voltage-cover component
formula gives (2.6).  \(\square\)

This is the exact positive content of one additional closure orbit: it
provides one fixed defect, not a deck-phase variable.

## 3. Cap/history/private-edge correlation

Let `S` contain the exact cap current and prefix debt, the phase-labelled
positive and negative directed histories, and the literal topology/private
resource state.  For branch `b in {0,1}`, let `A_b` be the relation of
accepted tuples

\[
        (x,y;z,c;R^+,R^-;f_b;v),                      \tag{3.1}
\]

where `f_0=f_10`, `f_1=g_10`, and every field is computed on the same
literal word.  Then

\[
 \begin{aligned}
  \mathcal A_0&\subseteq \mathcal S\times\{f_{10}\}\times\{w\},\\
  \mathcal A_1&\subseteq \mathcal S\times\{g_{10}\}\times\{w+\eta\}.
 \end{aligned}                                        \tag{3.2}
\]

For any fixed nonvoltage state `xi`, its accepting voltage fibre obeys

\[
                       K_{\rm acc}(\xi)
                         \subseteq\{w,w+\eta\}.        \tag{3.3}
\]

Equality is not automatic.  The two branches can have different cap
prefixes, boundary histories, private-resource conflicts, or topology
guards.

### Corollary 3.1 (exact accepted unit test)

For a fixed literal nonvoltage boundary state `xi`, the one-split face has
an accepted one-component development if and only if at least one of

\[
 \begin{array}{ll}
 \text{ordinary branch accepted at `xi`}
      &\text{and }\gcd(N,w)=1,\\
 \text{split branch accepted at `xi`}
      &\text{and }\gcd(N,w+\eta)=1
 \end{array}                                           \tag{3.4}
\]

holds.  This is necessary and sufficient; no separate cap, history or
private-edge marginal may be substituted for branch acceptance.

### Proposition 3.2 (a pure phase split translates the boundary state)

Suppose the extra closure is obtained by a deck translation `tau_eta` of a
complete endpoint occurrence and all labels incident with it.  Then its
phase-labelled history/rail state is `tau_eta xi`, not `xi`.  It preserves
the same named state only if

\[
                          \tau_\eta\xi=\xi .           \tag{3.5}
\]

For a state containing the literal pivot singleton rail, its stabilizer is
contained in `H={0}`.  Hence a nonzero split cannot be a same-state
cap/bi-history-transparent closure.

#### Proof

Deck translation acts on every coordinate name in the endpoint rail and
in the positive and negative histories.  The history transition maps are
equivariant, so translating the endpoint translates their input/output
tuples.  Any stabilizer of the complete state must in particular stabilize
the literal rail; Lemma 1.2 makes this stabilizer trivial.  \(\square\)

It is sound to export `tau_eta xi` as a different correlated branch.  It is
not sound to forget the phase, combine its voltage with the unsplit cap
state, and combine its histories with whichever branch happens to accept.

## 4. Complete coprimality audit

### Theorem 4.1 (neutral-base all-odd criterion)

Let `eta` be a fixed nonzero coherent integer.  Then

\[
              \gcd(N,\eta)=1\quad\hbox{for every odd }N\ge3
                                                               \tag{4.1}
\]

if and only if

\[
                              \eta=\pm2^a              \tag{4.2}
\]

for some integer `a>=0`.

#### Proof

Every power of two is coprime to every odd integer.  Conversely, if the
nonzero integer `eta` is not a signed power of two, it has an odd prime
divisor `p`; taking `N=p` contradicts (4.1).  \(\square\)

Thus a **supplied and accepted** parallel closure with defect `+/-2^a`
would pump a neutral base in every odd dimension.  Lemmas 1.1--1.2 show
that this closure is not generated by merely choosing another lift of the
same rigid ordered-rail port.

### Theorem 4.2 (one binary knob is not a universal inherited-base tuner)

For every fixed nonzero integer `eta`, there are an odd composite modulus
`N` and an integer `w` such that neither `w` nor `w+eta` is a unit modulo
`N`.

#### Proof

Choose distinct odd primes `p,q` not dividing `eta`.  By the Chinese
remainder theorem choose

\[
                         w\equiv0\pmod p,
               \qquad w\equiv-\eta\pmod q.           \tag{4.3}
\]

For `N=pq`, the first menu value is divisible by `p` and the second by
`q`.  \(\square\)

For comparison, when `N` is an odd prime power and `eta` is a unit modulo
`N`, at least one of `w,w+eta` is a unit: if `w` is divisible by the prime,
then `w+eta` is not.  The failure in Theorem 4.2 is genuinely the
multi-prime composite gate.

## 5. First possible larger face

Consider switches between two perfect matchings in a simple bipartite
occurrence graph.  Their symmetric difference is a disjoint union of even
alternating cycles.  A `C4` lying in one ordered rail has holonomy in its
rail stabilizer, and hence zero on the rigid pivot rail.  A single split
endpoint is either illegal by lift uniqueness or is the one fixed parallel
edge of Section 2, which translates rather than returns the boundary state.

Within the one-copy payload model, a boundary split must either be paired
with a return conversion or moved into an internal role-converting circuit.
A second `C4` using the duplicated role as an additional simultaneous
vertex would duplicate that role's owner/payload; treating it merely as an
alternative makes the change the binary branch of Section 2.  Thus the
first simple alternating support beyond the already decided one-copy
`C4` face is `C6`.  This threshold is scoped to the one-copy model: a
multigraph with a supplied parallel edge has the two-edge comparison of
Section 2, and a construction which deliberately adds a second payload
copy is a different interface.

### Theorem 5.1 (same-rail cycles cannot pump)

For any alternating cycle entirely inside one ordered rail `W`, write each
oriented port gain as in (1.3).  All left and right phase potentials cancel
in the alternating sum, leaving an element of `H`.  In particular every
`C_(2t)` in a trivial-stabilizer rail has zero switch holonomy.

Thus a candidate `C6` pump must include at least one genuine rail/role
converter or another edge orbit whose gain is not the common-rail endpoint
gradient.  It must additionally prove:

1. nonzero accepted holonomy, preferably a signed power of two for a
   dimension-uniform neutral-base pump;
2. one directed output cycle with co-oriented retained fragments;
3. return of the cap-prefix and both history states, rather than only their
   unlabelled projections; and
4. survival of one literal private aperture edge.

These four rows are sufficient at the voltage/cap/history/topology level.
The present theorem proves neither a Boolean `C6` satisfying them nor a
need to pass to `C8`: `C6` is exactly the first simple face not excluded by
the minimal ordered-rail argument.

## 6. Scope and exact next lemma

The theorem closes the minimal one-split classification:

* an endpoint-only split supplies no new edge;
* a same-rail split has defect in the rail stabilizer and zero defect on the
  protected pivot rail;
* one genuinely different parallel closure gives exactly a binary fixed
  defect menu, correlated with cap, both histories and the private edge;
* a neutral-base dimension-uniform defect must be dyadic;
* no binary menu universally repairs arbitrary inherited bases over odd
  composite moduli; and
* exact same-state transparency forces at least a larger role-converting
  face, with `C6` the first possible simple alternating support.

The next constructive lemma is therefore a **role-converting accepted
`C6` pump** (or a proof that Boolean resource identities force its
holonomy to vanish).  It must export the complete correlated relation

\[
 (\eta;\Delta,b;\mathcal R_d^+,\mathcal R_d^-;
          f_{\rm ap};\mathcal P_{\rm priv})           \tag{6.1}
\]

on one literal chronology.  Source/envelope transport, arbitrary upper
shadows, ambient residence beyond the encoded histories, and the terminal
common-cap compiler remain separate gates.

## 7. Source chain

The rigid `K_(2,2)` transporter theorem is
`MATH_THEOREM_K_MINIMAL_PHASE_COHERENT_K22_APERTURE_PUMP_NOGO_20260802.md`.
The fragment voltage and aperture state are in
`MATH_THEOREM_K_PASCAL_COPRIME_SEED_TRANSPORT_AND_APERTURE_VOLTAGE_GATE_20260802.md`.
The exact port graph and ordered-rail rectangle are in
`MATH_THEOREM_K_PASCAL_PORT_RECTANGLE_CALCULUS_AND_REGENERATIVE_BOX_GATE_20260802.md`.
The cap/history product and pivot reset are in
`MATH_THEOREM_K_CAP_BACKUP_HISTORY_TICKET_MONOID_AND_HEPTAGON_HOST_GATE_20260802.md`
and
`MATH_THEOREM_K_DIRECTED_HISTORY_PORT_MONOID_AND_PIVOT_RESET_20260802.md`.
The companion finite-fibre arithmetic classification is
`MATH_THEOREM_K_FINITE_HOLONOMY_FIBRE_UNIVERSAL_UNIT_CRITERION_20260802.md`.
