# The four-sector immediate-lower palette has an exact protected-edge alternating reset

Date: 2026-08-01  
Lane: additive-constant same-parity regeneration, immediate lower shadow  
Status: unconditional at the owner/q1 occurrence level; conditional for the
physical residence, upper-shadow and common-cap rows.

## 0. Outcome

The occurrence-labelled q1 condition of the odd four-sector child is not an
abstract existence obstruction once its exact q1-rainbow factor has been
constructed.

Let `F` be any spanning q1-rainbow two-factor in a middle Johnson layer and
let `e` be any edge of `F`.  There is a finite sequence of closed alternating
incidence circuits which

1. preserves every owner degree and every q1 colour occurrence exactly;
2. never changes `e`;
3. passes only through q1-rainbow spanning two-factors; and
4. ends at a q1-rainbow Hamilton cycle containing `e`.

Opening `e` therefore gives the exact `B1` state.  Moreover, when the owner
rank is at least `d+4`, one **prospectively prepared** fresh-q1 endpoint
coatom slot can be relabelled so that its length-`d` prefix equals the
missing colour of `e`.  Thus, on the prepared-slot face, the protected
opening colour has a literal boundary cell while the complete paired
`q>=2` endpoint chain is transported as before.

Applied after the direct four-sector factor theorem, this proves a cyclic
q1-injective child on the same complete child owner deck.  It also gives
zero cut-colour debt after the rethread:

\[
                         \eta_*=0.
\]

The qualifier **after the rethread** is essential.  The alternating
circuits live in the complete Middle Levels incidence graph and can change
arbitrarily many internal four-sector edges.  No claim is made that they
preserve the direct Pascal edge formulas, residence, ranks two and deeper,
upper interval support, or one common compiler cap.  Those protected-host
requirements are the remaining correlated theorem.

## 1. The incidence-factor equivalence

Let `Gamma` have odd size `2m-1`.  Put

\[
 {\cal U}={\Gamma\choose m},\qquad
 {\cal L}={\Gamma\choose m-1},\qquad
 W=|{\cal U}|=|{\cal L}|.
\]

Let `ML(Gamma)` be the bipartite containment graph between `L` and `U`.
Give a Johnson edge `AB` in `J(Gamma,m)` the q1 colour

\[
                            \chi(AB)=A\cap B.             \tag{1.1}
\]

### Lemma 1.1 (exact incidence lift)

There is a bijection between

* spanning q1-rainbow two-factors `F` of `J(Gamma,m)`; and
* spanning two-factors `Fhat` of `ML(Gamma)`.

The forward map replaces each edge `AB` of colour `Q` by

\[
                            A-Q-B.                         \tag{1.2}
\]

The inverse pairs the two upper neighbours of each lower vertex `Q`.
Connectivity is preserved: `Fhat` is one cycle if and only if `F` is one
cycle.

#### Proof

In a q1-rainbow Johnson factor every owner belongs to two factor edges and
every q1 colour labels one factor edge.  Thus (1.2) gives degree two at
every vertex on both shores.

Conversely, in a simple incidence two-factor a lower vertex `Q` has two
distinct upper neighbours `A,B`.  Both are rank-`m` supersets of the
rank-`m-1` set `Q`, so `A` and `B` differ only in their added elements and

\[
                             A\cap B=Q.
\]

Pairing them gives one Johnson edge of colour `Q`.  Upper degree two gives
owner degree two after projection.  Two different lower colours cannot
produce the same projected edge because a Johnson edge has one
intersection.  Hence the projection is a simple spanning q1-rainbow
two-factor.  Subdivision and suppression of the lower vertices preserve
components.  \(\square\)

## 2. A Hamilton target through a prescribed occurrence

### Lemma 2.1 (prescribed-edge Middle Levels cycle)

For every Johnson edge `e=AB` in `J(Gamma,m)`, `ML(Gamma)` has a Hamilton
cycle containing the two-edge incidence path

\[
                         A-(A\cap B)-B.                     \tag{2.1}
\]

#### Proof

The Middle Levels Theorem supplies one Hamilton cycle `H0`.  At any lower
vertex `Q0`, let its two cyclic neighbours be `A0,B0`.  Then
`A0 intersect B0=Q0`, so these three vertices project to a Johnson edge.

The symmetric group of `Gamma` is transitive on triples

\[
                (Q,Q+\{a\},Q+\{b\}),\qquad a\ne b,
\]

because it may map the `m-1` elements of `Q0` to those of `A intersect B`,
the two added elements separately, and the remaining coordinates
arbitrarily.  Applying such a coordinate permutation to `H0` gives a
Hamilton cycle containing (2.1).  \(\square\)

No stronger rooted version of the Middle Levels Theorem is used; ordinary
Hamiltonicity plus coordinate transitivity suffices.

## 3. Protected-edge alternating-circuit reset

Here a closed alternating circuit means an edge-simple closed alternating
trail; vertices may repeat.  Repeated-vertex circuits may be split further
whenever the two colour balances split, but simplicity is not needed for a
degree-preserving toggle.

### Theorem 3.1 (exact q1 occurrence routing)

Let `F` be a spanning q1-rainbow two-factor of `J(Gamma,m)`, and fix an edge
`e=AB` of `F`.  There are q1-rainbow spanning two-factors

\[
                    F=F_0,F_1,\ldots,F_t=H               \tag{3.1}
\]

such that

1. every `F_i` contains `e`;
2. `H` is a Hamilton cycle;
3. each transition is the projection of one closed alternating circuit in
   `ML(Gamma)`; and
4. one may take

\[
                              t\le W-1.                    \tag{3.2}
\]

#### Proof

Lift `F` to the incidence factor `Fhat` by Lemma 1.1.  By Lemma 2.1 choose
a Hamilton incidence cycle `Hhat` containing the path (2.1).  The two
incidences of that path belong to both factors.

Colour `Fhat minus Hhat` red and `Hhat minus Fhat` blue.  At every incidence
vertex, red degree equals blue degree: both original factors have degree
two and their common incidences have been deleted from both counts.  Pair
red and blue half-edges at every vertex.  Following the pairings decomposes
the symmetric difference into edge-disjoint closed alternating circuits.

Toggle these circuits one at a time.  On each circuit, every visited vertex
loses and gains the same number of incidences, so degree two is preserved.
The two common incidences in (2.1) are outside the symmetric difference,
so every intermediate factor still contains them.  Lemma 1.1 projects each
intermediate incidence factor to a q1-rainbow Johnson two-factor containing
`e`.  After every circuit has been toggled the terminal factor is `Hhat`,
whose projection `H` is Hamilton.

Each incidence factor has `2W` edges, and the two protected incidences are
common.  Therefore the symmetric difference has at most `4W-4` edges.  A
closed alternating circuit in a simple bipartite graph has length at least
four, proving (3.2).  \(\square\)

This is an explicit occurrence-routing proof: a lower incidence is a
particular occurrence `Q subset T`; a circuit deletes and installs equal
numbers of occurrences at every colour and every owner.  It is stronger
than separate palette counts and does not appeal to a scalar endpoint
state.

### Corollary 3.2 (four-sector q1 cycle)

Suppose the odd four-sector Pascal construction has produced the literal
q1-rainbow child factor supplied by the dimension-uniform four-sector
factor theorem.  Choose any one of its edges `e`.  Theorem 3.1 rethreads the
factor on the same owner deck to a q1-rainbow Hamilton cycle while retaining
`e`.

Consequently, at the unrestricted owner/q1 level, cyclic occurrence-labelled
injectivity is automatic.  Opening `e` gives a Hamilton path with sole q1
hole

\[
                              Q=A\cap B,                    \tag{3.3}
\]

and endpoint class

\[
                            (z,\ell,\rho,b)=(0,0,0,1).       \tag{3.4}
\]

Thus `delta_top=0`, and the resulting factor-opening sidecar has
`eta_*=0`.

#### Proof

The direct four-sector theorem gives the hypothesis of Theorem 3.1.  In the
terminal Hamilton cycle every q1 colour occurs once.  Removing `e` removes
only `Q`; both new global endpoints are `A,B` and contain `Q`.  This is
exactly (3.4).  The `B1` closure theorem gives `delta_top=0`.  A one-component
factor has no interior cut colour, so its recycling defect is zero.
\(\square\)

## 4. Literal alignment with the fresh-q1 transporter

The preceding argument gives a protected endpoint edge but is still stated
at the owner/q1 level.  The endpoint coatom transporter supplies the
corresponding physical short cell.

### Theorem 4.1 (prescribed B1 colour fits one prepared fresh transporter)

Let the child owner rank be `m`, let `d>=2`, and assume

\[
                              m\ge d+4.                     \tag{4.1}
\]

Assume a fresh-q1 coatom target block may be prospectively planted at the
left endpoint.  For the protected edge `e=AB` and `Q=A intersect B`, its
labels can be chosen with

\[
                         T_0=A,qquad
                         \bigcup_{j=0}^{d-1}A_j^a=Q.         \tag{4.2}
\]

Its prefixes of lengths `1,...,d-1` are the complete declared paired
`q>=2` endpoint chain; its length-`d+1` prefix is common.  A reversed copy
gives the analogous right-end construction.

#### Proof

Write `beta` for the unique element of `A minus Q`.  In the notation of the
fresh-q1 transporter, assign the active role `b=beta`.  The remaining
roles

\[
          \infty,c,a,x,f_1,\ldots,f_{d-1}
\]

use `d+3` distinct elements of `Q`, and put the remaining
`m-d-4` elements of `Q` into the core `K`.  Condition (4.1) is exactly what
makes this possible.  Choose `f_0` outside `A`, and distribute unused
ambient labels arbitrarily.

The first coatom target of the transporter is then `T_0=A`.  Its
length-`d` alternatives are

\[
                         T_0-\{b\}=Q,
              \qquad     T_0-\{a\}.                         \tag{4.3}
\]

Selecting the first gives (4.2).  Corollary 2.6 of the endpoint-transporter
theorem proves the remaining prefix and common-return statements.  Reversal
interchanges the two boundary shores.  \(\square\)

For a `B1` hole, one of the two endpoint banks already suffices for the
candidate-cap assignment.  Two disjoint mirrored copies may be retained
when the deeper compiler construction needs symmetric endpoint chains.
The theorem certifies this one candidate prefix cell only.  It does not show
that changing to this alternative preserves every other q1 assignment or
that the terminal common-cap matching accepts the change.
This is a candidate incidence, not net global q1 coverage: selecting `Q`
may displace the alternative `T_0-{a}` from that physical address.  A final
compiler must keep that alternative supported elsewhere and realize this
cell in the same legal common-cap state.

## 5. Exact scope: what is closed and what is not

The combination of Theorems 3.1 and 4.1 closes the following statement on
the prepared-endpoint face:

> Starting from any literal q1-rainbow four-sector child factor, there is an
> occurrence-integral rethread on the same owner deck to a q1-rainbow cycle,
> with a protected opening edge whose missing colour has a literal fresh-q1
> endpoint cell and whose deeper endpoint chain is transported exactly.

It does **not** prove a protected Pascal rethread.  In particular:

* a B1 parent cycle alone does not imply the union-occurrence transversal
  and cap-two hypotheses needed to construct the direct four-sector factor;
* an alternating circuit may use incidence edges absent from the direct
  four-sector `A/X/Y/U` catalogue;
* the number and total length of circuits need not be bounded independently
  of the dimension;
* planting the required endpoint coatom target block in the actual Pascal
  chronology is an additional host-availability hypothesis;
* intermediate or terminal chronologies need not preserve residence,
  arbitrary-width upper OR support, component-private packet slots, or a
  common compiler cap; and
* the transporter is basis-preserving and does not supply an unused-cell
  augmenting ear.

Therefore the exact remaining q1-correlated theorem is no longer plain
palette injectivity.  It is:

> **Protected incidence-router theorem.**  Find the Hamilton target and its
> alternating circuits inside the incidence subgraph whose occurrences have
> simultaneous U1--U4 and terminal-cap certificates, while keeping the
> prepared endpoint transporter fixed.

This is complementary to the cut-colour provider-transversal theorem.  If
one insists on retaining the opened interiors of the original factor and
only changing certified seam slots, the exact residual debt is the Rado
deficiency

\[
 \max_{X\subseteq\Delta^\circ}
       \bigl(|X|-r_{\mathcal M}(N(X))\bigr).
\]

The complete-host circuit reset does not bound that restricted deficiency:
it is allowed to change the interiors themselves.  Conversely, a full Rado
transversal inside a protected seam matroid would make the present global
rethread unnecessary.  The two statements address different physical
faces.

On that restricted host, even a nontrivial cut with fewer than two allowed
incidences is an immediate obstruction to a Hamilton target.  The complete
Middle Levels host used in Theorem 3.1 has no such restriction.

## 6. Replay

Run

```text
python3 scratch/audit_o1_four_sector_q1_alternating_reset_20260801.py
```

The dependency-free replay uses the exact two-component q1-rainbow factor
in `J(5,3)` from the rainbow-sidecar audit.  It finds a Hamilton target
through a retained edge, decomposes the incidence symmetric difference,
and checks every intermediate projection.  In this smallest fixture the
entire reset is one alternating `C6`.  It also checks that all 30 Johnson
edges lie in coordinate images of the target Hamilton cycle and replays the
fresh transporter for `2<=d<=24`.

Expected status:

```text
PASS_O1_FOUR_SECTOR_Q1_ALTERNATING_RESET
```

The generated JSON is

```text
scratch/o1_four_sector_q1_alternating_reset_20260801.audit.json
```

with payload SHA-256

```text
1b6d8f4a1bea7297ba8742feb858ec894f27bebd93b6fc31544ce9d0a825e3a8
```

Dependencies, used at their stated scope only:

* `MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md`;
* `MATH_THEOREM_TOP_SHADOW_PASCAL_RAINBOW_SIDECAR_REGENERATION_20260801.md`;
* `MATH_THEOREM_REBASED_SERIAL_EXTERIOR_EAR_CONTRACTION_20260801.md`;
* `MATH_THEOREM_O1_Q1_CUT_COLOUR_RECYCLING_RADO_GATE_20260801.md`; and
* the ordinary Middle Levels Theorem.

No product-lattice statement is used.
