# Three-shell BRG, typed containment flow, and the event-curvature obstruction

Date: 2026-07-30<br>
Lane: K<br>
Status: **proved weakening of the BRG induction state; proved exact typed
Pascal circulation; proved a conserved obstruction to zero-frame
regeneration; solver-free calibration on the authenticated `k=11,13,15`
packages.  The paired-turn/witness-section existence theorem remains open.**

## 0. Verdict

The bulk-regeneration gate from

```text
MATH_THEOREM_K_RELATIVE_PPR_ROUTER_ATLAS_AND_PASCAL_REGENERATION_GATE_20260730.md
```

can be weakened in two ways, but it cannot be replaced by an ordinary
positive-expansion argument.

First, inside the direct four-sector Pascal architecture, one need carry
only the three compiler packages at depths

\[
                 d-1,\qquad d,\qquad d+1.                 \tag{0.1}
\]

The central child package is transported from these three parent packages;
the two child side packages may be constructed afresh.  A wider depth
interval, equality of all occurrence vectors, and a transported copy of the
old compiler matching are not needed.  This gives the **three-shell
regeneration property** `3BRG(r,d)` below.

Second, after the child `AA` Catalan forest has been fixed, a large part of
the generalized Pascal braid is an exact integral network problem.  Degree
two, both lower `q=1` decks, and the entire `z`-containing upper `q=1` deck
are equivalent to one typed lower-bound circulation on the Boolean
containment graph.  There is no hidden rounding step.

The first genuinely nonflow rows are the paired `BB` turns which must cover
the upper targets not containing `z`.  The authenticated data show that
these rows are essential: a deterministic joint circulation misses

\[
                    20,\qquad113,\qquad508              \tag{0.2}
\]

such targets at `k=11,13,15`, although the frozen factors cover all of them.

There is also a sharp negative theorem.  Fixed-depth occurrence vectors
determine every coordinate's run and gap histograms by discrete second
differences.  Hence an all-depth zero-frame router cannot improve either
Pascal event buffer.  Any successful regenerator must have a prescribed
nonzero rank-weighted drift in the first defective shell.  A library made
only from transported zero-frame atoms has charge lattice `{0}` and is
incapable of BRG whenever the raw Pascal child has a positive buffer defect.

The frozen packages calibrate both boundaries exactly.

* Their joint typed circulations pass, and their literal terminal
  `COMP_3` matchings pass.
* Their direct Pascal reuse fails before deeper Hall: the cyclic factors
  contain respectively

  \[
  143,429,1425
  \]

  length-four positive runs and

  \[
  44,117,330
  \]

  singleton zero gaps.  Thus the raw facet has forbidden length-three runs
  and the raw union row has repeated adjacent owners.

The exact remaining all-`r` lemma is therefore narrow: choose a buffered
`AA` Catalan forest and one compatible physical paired-turn/all-depth
witness section whose forced incidences extend through the typed circulation
and whose resulting chronology passes the three compiler SDRs and the
near-perfect opening.  Ordinary endpoint Hall, positive surplus, or
zero-frame transport does not imply this statement.

No SAT/CP solve, exhaustive search, web access, or heavy local computation
was used.  The finite replay is deterministic and takes about one second.

## 1. Conventions

Let

\[
 T=(T_i)
\]

be a cyclic rank-`s` Johnson factor.  Indices are cyclic on each physical
component.  Put

\[
 L_q(T)_i=\bigcap_{j=0}^{q}T_{i+j},\qquad
 U_q(T)_i=\bigcup_{j=0}^{q}T_{i+j}.                 \tag{1.1}
\]

The occurrence vectors are

\[
 a_q^T(S)=|\{i:L_q(T)_i=S\}|,\qquad
 b_q^T(Y)=|\{i:U_q(T)_i=Y\}|.                      \tag{1.2}
\]

Coverage means that every required target has at least one literal
occurrence.  Occurrence neutrality is the much stronger assertion

\[
 a_q^{T'}=a_q^T,qquad b_q^{T'}=b_q^T.              \tag{1.3}
\]

A **protected witness section** chooses one physical occurrence for every
target which must survive.  It is allowed to change unused duplicate,
wrong-rank, or alternative occurrences.  This is the correct weak
regeneration interface.

Write `P_q` for the complete occurrence-labelled compiler package at depth
`q`: the middle/envelope data, fixed physical pins, target-position
incidences, and the boundary ledger used by the facet/union identities.  The
package also records the pointwise expected-rank lower and upper shell rows
used by the symmetric event-buffer invariant.  The notation does not impose
the maximal-envelope normalization.  A fresh package may use any literal
solution of the declared compiler system.  The upper shell is a sufficient
Pascal-recursive invariant; it is stronger than the architecture-free
requirement of arbitrary-interval upper coverage alone.

## 2. The three-shell induction state

The intact child sectors have the exact depth chart

\[
\begin{array}{c|c|c}
\text{sector}&L_q&U_q\\ \hline
A=\{x,y\}+\partial T&\{x,y\}+L_{q+1}(T)&
                         \{x,y\}+U_{q-1}(T)\\
X=\{x\}+T&\{x\}+L_q(T)&\{x\}+U_q(T)\\
Y=\{y\}+T&\{y\}+L_q(T)&\{y\}+U_q(T)\\
B=\nabla T&L_{q-1}(T)&U_{q+1}(T).
\end{array}                                         \tag{2.1}
\]

The compiler envelopes obey the same shifts.

### Definition 2.1 (the three-shell state `S3(r,d)`)

An admissible decorated rank-`r` parent has state `S3(r,d)` when it carries

1. the three literal packages `P_(d-1),P_d,P_(d+1)`;
2. a named physical protected witness section covering every required lower
   target and every required arbitrary-upper target; and
3. the strict/event-buffer clauses encoded by the expected-rank rows of
   those packages.

The witness section is part of the state: after regeneration one may select
new occurrences, but the output must again name one occurrence for every
required target.  Thus `S3` is closed under a successful induction step.

### Definition 2.2 (`3BRG(r,d)`)

Fix the direct four-sector Pascal architecture and a declared physical
correction atlas.  `3BRG(r,d)` means that every admissible decorated parent
with state `S3(r,d)`, in particular carrying

\[
                P_{d-1},P_d,P_{d+1}                  \tag{2.2}
\]

has a corrected physical child with the following properties.

1. Every old lower and arbitrary-upper target has a retained or declared
   replacement witness, and every new-signature target is covered.
2. The central child package `P_d` is obtained from the three parent
   packages and the declared service cells.
3. Fresh child packages `P_(d-1)` and `P_(d+1)` exist.  They need not be
   images of old pins.
4. The child chronology is an admissible decorated parent with state
   `S3(r+1,d)`: it is strict, has the encoded event buffer, and comes with a
   newly named full protected witness section.
5. A near-perfect physical opening and the exact terminal `COMP_d` boundary
   ledger are supplied.

Only protected witnesses and immutable pins must survive.  Unprotected
occurrence loads may change.

### Theorem 2.3 (three-shell induction)

Suppose one authenticated boundary-PPR base at semilength `r_0` has state
`S3(r_0,d)`, and `3BRG(r,d)` holds for every `r>=r_0`.  Then boundary-PPR
holds at depth `d` for every `r>=r_0`.  Consequently

\[
 \nu(2r+1)\le \binom{2r+1}{r+1}+d                  \tag{2.3}
\]

throughout the induction.

#### Proof

At child depth `d`, sector `A` uses the lower slice of the parent package at
`d+1` and the upper slice at `d-1`; sector `B` uses the lower slice at
`d-1` and the upper slice at `d+1`; and `X,Y` use both slices at `d`.
Within each lower or upper compiler shore the four new-label signature
classes are disjoint, and their physical sector-position shores are
disjoint as well.  Hence the transported lower and upper partial matchings
combine shore by shore without fractional rounding.  Definition 2.2
supplies the actual seam/service corrections and reconstructs the two
auxiliary child packages.  Its output clause explicitly returns state
`S3(r+1,d)`, so induction applies.  The final opening and `COMP_d` clauses give (2.3) by the
boundary-PPR compiler theorem. \(\square\)

### Proposition 2.4 (three-depth dependence of intact transport)

Assume `1<=d<=r-2`, all four signature shores in (2.1) are nonempty, and no
missing slice is regenerated or derived from another one.  Verbatim intact
transport of the central package references all three depths in (2.2):
`A` uses lower `d+1` and upper `d-1`, `X/Y` use `d`, and `B` uses lower
`d-1` and upper `d+1`.

This is a dependence statement, not an architecture-free minimality claim.
A construction which regenerates a missing slice, derives it from extra
structure, or builds the entire child chronology and compiler from scratch
need not expose three complete parent packages.

## 3. Run curvature and the forced regenerative charge

Fix a coordinate `x`.  On every nonconstant component its trace has cyclic
one-runs and zero-gaps.  A component on which the trace is constant is
regarded as having no finite run of that sign; it never creates a short-run
defect.  Assume the component lengths exceed the depths under discussion,
as in all authenticated packages.

Put

\[
 E_{x,q}(T)=\sum_{S\ni x}a_q^T(S),\qquad
 F_{x,q}(T)=\sum_{Y\not\ni x}b_q^T(Y).              \tag{3.1}
\]

Let `R_x^+(ell)` and `R_x^0(g)` count finite one-runs and zero-gaps.

### Theorem 3.1 (run-curvature identity)

For every relevant `q`,

\[
 E_{x,q}=\sum_{\ell}(\ell-q)^+R_x^+(\ell)+C_{x}^{+},\qquad
 F_{x,q}=\sum_g(g-q)^+R_x^0(g)+C_x^0,               \tag{3.2}
\]

where the constant-component terms are independent of `q`.  Hence

\[
 R_x^+(\ell)=E_{x,\ell-1}-2E_{x,\ell}+E_{x,\ell+1},\tag{3.3}
\]

\[
 R_x^0(g)=F_{x,g-1}-2F_{x,g}+F_{x,g+1}.             \tag{3.4}
\]

#### Proof

A `q`-edge window lies wholly in a one-run of `ell` states at exactly
`max(ell-q,0)` starts.  The zero-gap statement is identical.  A constant
component contributes all its starts at each of the displayed depths, hence
a `q`-independent term.  The second difference of
`max(ell-q,0)` is one at `q=ell` and zero elsewhere, proving
(3.3)--(3.4). \(\square\)

Define the cyclic rank defects

\[
 \Phi_h^-(T)=\sum_i\bigl(|L_h(T)_i|-(s-h)\bigr),    \tag{3.5}
\]

\[
 \Phi_h^+(T)=\sum_i\bigl((s+h)-|U_h(T)_i|\bigr).  \tag{3.6}
\]

Every summand is nonnegative for a Johnson chronology.

### Theorem 3.2 (exact event-defect formula)

For a cyclic factor,

\[
 \Phi_h^-(T)=
   \sum_x\sum_{\ell<h}(h-\ell)R_x^+(\ell),         \tag{3.7}
\]

\[
 \Phi_h^+(T)=
   \sum_x\sum_{g<h}(h-g)R_x^0(g).                  \tag{3.8}
\]

Consequently, `Phi_h^-` vanishes exactly when every finite positive run has
length at least `h`; `Phi_h^+` has the dual interpretation.

#### Proof

The total number of state-coordinate incidences is `sW`.  Every physical
transition starts one finite positive run, so the total number of finite
positive runs over all coordinates is `W`; constant components contribute
incidences but no transition.  Summing (3.2) therefore gives

\[
 \sum_i|L_h(T)_i|
 =sW-hW+
  \sum_x\sum_{\ell<h}(h-\ell)R_x^+(\ell).
\]

This is (3.7).  The zero-gap proof uses `(n-s)W` zero incidences and one
new finite zero-gap per deletion transition. \(\square\)

### Corollary 3.3 (Pascal shift)

Whenever the facet and union rows are strict,

\[
 \Phi_q^-(\partial T)=\Phi_{q+1}^-(T),\qquad
 \Phi_q^+(\nabla T)=\Phi_{q+1}^+(T).                \tag{3.9}
\]

#### Proof

Use `L_q(partial T)=L_(q+1)(T)` and
`U_q(nabla T)=U_(q+1)(T)`.  Their expected ranks also agree:

\[
 (s-1)-q=s-(q+1),\qquad
 (s+1)+q=s+(q+1). \quad\square
\]

Thus a parent which is resident only at the current threshold generally
produces a raw child whose outer package is defective.  Repairing the child
`P_(d+1)` package to pointwise expected rank simultaneously restores the
child residence/dual-residence state needed by Definition 2.1.  The event
buffer is not an independent scalar once this package is literal.

Explicitly, the raw outer defects are

\[
 \Phi_{d+1}^-(\partial T)=\Phi_{d+2}^-(T),\qquad
 \Phi_{d+1}^+(\nabla T)=\Phi_{d+2}^+(T).             \tag{3.10}
\]

### Theorem 3.4 (zero-frame rigidity)

If a router preserves the lower occurrence vectors at depths
`ell-1,ell,ell+1`, it preserves every coordinate's number of one-runs of
length `ell`.  The analogous assertion holds for upper occurrences and
zero-gaps.

In particular, an all-depth zero-frame router cannot improve either event
buffer.

#### Proof

Occurrence equality preserves the coordinate marginals (3.1).  Apply the
second-difference identities (3.3)--(3.4). \(\square\)

This is a strict obstruction to the strong reading of old `BRG` clauses
"preserve all occurrence vectors" and "restore the event buffer".  The
correct word is **coverage**, not load neutrality.

### Theorem 3.5 (forced curvature charge)

Let `T,T'` be equal-length cyclic rank-`s` chronologies and put

\[
 \delta_h^-(S)=a_h^{T'}(S)-a_h^T(S),\qquad
 \delta_h^+(Y)=b_h^{T'}(Y)-b_h^T(Y).                \tag{3.11}
\]

Then

\[
 \Phi_h^-(T')-\Phi_h^-(T)=
       \sum_S|S|\delta_h^-(S),                      \tag{3.12}
\]

\[
 \Phi_h^+(T')-\Phi_h^+(T)=
      -\sum_Y|Y|\delta_h^+(Y).                      \tag{3.13}
\]

Hence an exact repair to an `h`-buffered chronology must satisfy

\[
 \boxed{\sum_S|S|\delta_h^-(S)=-\Phi_h^-(T)},       \tag{3.14}
\]

\[
 \boxed{\sum_Y|Y|\delta_h^+(Y)=+\Phi_h^+(T)}.       \tag{3.15}
\]

These equations are necessary and, for the two scalar buffer rows, exact.

#### Proof

Sum the ranks in the two occurrence vectors.  Their unweighted drifts are
zero because both chronologies have the same number of starts.  Equations
(3.12)--(3.13) follow from (3.5)--(3.6); setting the final defects to zero
gives (3.14)--(3.15). \(\square\)

For a compatible physical atom `g`, define its curvature charge

\[
 \kappa_h(g)=
 \left(
   \sum_S|S|\delta_{g,h}^-(S),
   \sum_Y|Y|\delta_{g,h}^+(Y)
 \right).                                           \tag{3.16}
\]

If compound columns have been materialized occurrence by occurrence, a
packet repairing `T` must represent

\[
             (-\Phi_h^-(T),+\Phi_h^+(T))            \tag{3.17}
\]

in the integer capacity cone generated by their charges.  This supplies an
exact parity, gcd, lattice, or cone obstruction before Hall or compiler
work.  Overlapping atoms may be added only after their union has been
recomputed as one compound column; separate baseline ledgers are not
additive across overlapping collars.

Fixed common cores do not change the charge: their rank contribution is a
constant times an occurrence drift whose total is zero.  Facet/union images
shift the charge depth according to (3.9).  Consequently a recursively
transported zero-charge library remains zero-charge.  Whenever (3.17) is
nonzero, the fully materialized repair packet or compound must have nonzero
net charge.  The curvature identity alone does not force that charge to
reside in one atom or to have bulk support.

### Proposition 3.6 (no scalar provider-mass obstruction)

Let `k=2s-1`, let `T` be a lower-`q=1`-exact rank-`s` factor, and put

\[
 C=\operatorname{Cat}_{s-1}.
\]

For every coordinate there are exactly `C` finite positive runs and `C`
finite zero-gaps.  The total numbers of states containing and avoiding the
coordinate are `sC` and `(s-1)C`.  Therefore an `h`-biresident trace has the
necessary scalar ceiling

\[
                         h\le s-1.                  \tag{3.18}
\]

If all positive runs have length at least `q`, then the number of depth-`q`
windows containing a fixed coordinate is

\[
                         (s-q)C.                    \tag{3.19}
\]

The number of expected rank-`s-q` lower targets containing that coordinate
satisfies

\[
 \binom{2s-2}{s-q-1}\le (s-q)C,                    \tag{3.20}
\]

with equality at `q=1` and strict inequality afterwards.

#### Proof

Lower-`q=1` exactness forces `2C` coordinate-crossing edges by the universal
coordinate-split count, hence `C` runs and gaps.  The state counts are the
two binomial coefficients

\[
 \binom{2s-2}{s-1}=sC,qquad
 \binom{2s-2}{s}=(s-1)C.
\]

Constant trace components only reduce the total length available to finite
runs of one sign, so the zero-gap side gives (3.18).  Subtracting `q` starts
from each of the `C` positive runs gives (3.19), with constant-one components
contributing unchanged.  Equation (3.20) is equality at `q=1`.  On increasing
`q` by one, its left side is multiplied by

\[
 \frac{s-q-1}{s+q},
\]

whereas the right side is multiplied by

\[
 \frac{s-q-1}{s-q}.
\]

The first multiplier is no larger. \(\square\)

Thus `h=o(s)` is not blocked by total run mass or by a coordinatewise count
of deeper providers.  The live obstruction is simultaneous chronology,
collision dispersion, and the paired physical witness section.

## 4. The exact typed Pascal containment circulation

Fix `r>=2`, a ground set `Omega` of size `2r`, and a distinguished new
coordinate `z`.  The child middle owners split as

\[
 \mathcal A=\{z\}+\binom{\Omega}{r},\qquad
 \mathcal B=\binom{\Omega}{r+1}.                    \tag{4.1}
\]

Let `P` be a spanning nonisolated linear forest on
`C(Omega,r)` such that its edge intersections enumerate every
rank-`r-1` set exactly once.  In the intended application, `P` is the
selected `AA` Catalan forest.  Put

\[
 E=\{T:d_P(T)=1\},\qquad I=\{T:d_P(T)=2\}.          \tag{4.2}
\]

For each selected `AA` edge `TT'`, its upper label is `T union T'`.  Let

\[
 M=\left\{U\in\binom{\Omega}{r+1}:
   U\ne T\cup T'\text{ for every }TT'\in P\right\}.\tag{4.3}
\]

### Theorem 4.1 (typed containment-circulation theorem)

The completions of `P` to a child two-factor which have

1. degree two at every child owner;
2. both lower `q=1` decks exact; and
3. the complete `z`-containing upper `q=1` deck

are in bijection with the integral solutions `x_(T,U)` of

\[
 x_{T,U}\in\{0,1\},\qquad x_{T,U}=0\text{ unless }T\subset U, \tag{4.4}
\]

\[
 \sum_{U\supset T}x_{T,U}=
 \begin{cases}
 1,&T\in E,\\
 2,&T\in I,
 \end{cases}                                        \tag{4.5}
\]

\[
 \sum_{T\subset U}x_{T,U}=2
 \qquad(U\in\mathcal B),                           \tag{4.6}
\]

\[
 \sum_{\substack{T\in E\\T\subset U}}x_{T,U}\ge1
 \qquad(U\in M).                                   \tag{4.7}
\]

The system is a lower-bound network circulation and is therefore integral.

#### Proof

For `T in E`, its one chosen incidence `T subset U` gives the cross edge

\[
                         (\{z\}\cup T)U.            \tag{4.8}
\]

For `T in I`, its two selected supersets `U_1,U_2` are distinct and give
the `BB` edge

\[
                             U_1U_2.                 \tag{4.9}
\]

Their intersection is exactly `T`.  Thus every endpoint lower colour is
used once by (4.8), every internal lower colour once by (4.9), and every
`A` owner reaches degree two after its `P` degree is included.  Equation
(4.6) gives degree two on `B`.

The selected `AA` intersections already give the exact lower deck
containing `z`.  Equations (4.8)--(4.9) give the exact lower deck not
containing `z`.  A `z`-upper target `z union U` is witnessed either by an
`AA` edge of union `U` or, when `U in M`, by the endpoint incidence forced
in (4.7).

Conversely, delete the fixed `AA` edges from such a child factor.  An `A`
endpoint has one cross edge, an `A` internal vertex has none, and every
lower colour `T in I` is represented by the unique `BB` edge of intersection
`T`.  Recording its one or two incident `B` owners recovers (4.4)--(4.7).

For integrality, split every right owner `U` into endpoint-input and
internal-input nodes.  Endpoint `T` nodes send unit-capacity arcs to the
first type and internal `T` nodes to the second.  Send both input nodes to
an aggregator `U`, put lower bound one on the endpoint-input arc exactly
when `U in M`, and require two units from `U` to the sink.  Source-to-`T`
arcs have the exact demands in (4.5).  This is an ordinary directed network
with integral lower and upper bounds. \(\square\)

The max-flow/min-cut inequalities of this network are the exact
Pascal-coupled Hall condition.  They may be tight; no positive surplus is
part of the theorem.

### Proposition 4.2 (the first nonflow row)

For

\[
 V\in\binom{\Omega}{r+2},                            \tag{4.10}
\]

the upper target `V` not containing `z` is covered exactly when

\[
 \bigvee_{\substack{T\in I,\ T\subset V\\V\setminus T=\{a,b\}}}
 \left(x_{T,T\cup\{a\}}\wedge x_{T,T\cup\{b\}}\right) \tag{4.11}
\]

is true.  These paired-incidence `BB`-turn rows are not rows of the network
in Theorem 4.1.

#### Proof

Every no-`z` upper edge is a `BB` edge.  The edge created at `T in I` has
endpoints `T+a,T+b` and union `T+a+b`.  This is `V` precisely in (4.11).
\(\square\)

Thus ordinary containment expansion cannot complete the Pascal induction.
The paired turn selected at each internal `T` is the first nonlinear memory.

## 5. Fixed witnesses leave an integral residual flow

The turn rows and the deeper shadows nevertheless admit an exact
representative-plus-flow formulation.

Fix an allowed physical incidence atlas.  Choose one literal simple path
occurrence for every required fixed lower target and one literal simple
path of arbitrary allowed length for every upper target.  Include one turn
from (4.11) for every no-`z` upper first-shadow target.  Let `F` be the union
of the **variable typed-containment incidences** used by these paths.  The
fixed `AA` forest edges are already present and are not charged again to
`F`; every selected path must of course be compatible with them.

For a left incidence label `T` and a right owner `U`, put

\[
 c_L(T)=
 \begin{cases}
  1-d_F(T),&T\in E,\\
  2-d_F(T),&T\in I,
 \end{cases}
 \qquad c_R(U)=2-d_F(U).                            \tag{5.1}
\]

Retain the endpoint/internal types and the right lower quotas from
Theorem 4.1, reducing every demand and capacity by the arcs already in `F`.

### Theorem 5.1 (typed protected-witness completion)

For a fixed physical witness section, a child factor containing all chosen
witnesses exists if and only if

1. the forced incidences respect the typed quotas:
   `d_F(T)<=1` for `T in E`, `d_F(T)<=2` for `T in I`, and
   `d_F(U)<=2` on the right;
2. every reduced lower bound is compatible with the reduced capacity; and
3. every cut of the resulting lower-bound network has nonnegative residual
   capacity.

Whenever it exists, the completion is integral and differs from any fixed
baseline completion by a disjoint union of alternating incidence circuits.

#### Proof

The forced paths consume their incidence capacities.  The remaining system
is exactly the network constructed in Theorem 4.1 with reduced integral
bounds.  Feasible-circulation/max-flow-min-cut is necessary and sufficient,
and network integrality gives a physical zero-one completion.  The symmetric
difference of two degree-two bipartite incidence factors is even and
decomposes into alternating circuits. \(\square\)

The outer choice of one common witness section is not a flow.  Different
depths may share physical arcs, the paired turns use two incidences at one
internal owner, and arbitrary-upper witnesses are accepting paths in an
accumulated-union automaton.  Theorem 5.1 says exactly where TU begins: after
the common physical section is fixed.

## 6. The compiler Hall layer

Fix the final chronology, its physical envelopes, and a compiler core.  Let
`P_fix` be the positions occupied by immutable pins, let `A` be the old
targets whose pins may be rematched, and let `D` be the newly regenerated
targets.  In the literal target-position graph `G`, retain an edge only when
the fixed core and envelope allow that target at that position.

### Theorem 6.1 (exact rematching Hall condition)

The immutable pins extend to the rematchable and regenerated targets if and
only if

\[
 \boxed{|N_G(X)\setminus P_{\rm fix}|\ge |X|
   \quad(X\subseteq A\cup D).}                      \tag{6.1}
\]

The extension is integral.

#### Proof

Delete the occupied positions and apply Hall's theorem to the remaining
bipartite graph. \(\square\)

A Hall-tight set whose entire alternative neighbourhood is occupied by
immutable pins is an exact compiler packet lock.  Provider multiplicity
outside this graph does not remove it.

If the core is variable, Hall on the union of all possible target-position
edges is not sufficient: two individually matchable assignments may force
incompatible adjacent core values.  Therefore the exact variable-core
formulation is a chronology-constrained SDR; (6.1) becomes exact only after
the chronology and core are fixed.

For `3BRG`, apply Theorem 6.1 separately to the three auxiliary package
copies at `d-1,d,d+1`.  The terminal physical word still uses the one actual
`COMP_d` package specified by boundary-PPR.

## 7. Authentication on `k=11,13,15`

The replay fixes the split coordinate used by the authenticated routers and
reconstructs the frozen factor, opening, and compiler word.

### 7.1 Typed circulation and turn rows

Let `C=Cat_r`.  The fixed `AA` forest has `2C` endpoints and
`(r-1)C` internal vertices.

\[
\begin{array}{c|r|r|r|r|r|r}
k&|E|&|I|&|\mathcal B|&\text{incidences}&|M|&
   \text{frozen BB upper}\\ \hline
11&84&168&210&420&40&120/120\\
13&264&660&792&1584&147&495/495\\
15&858&2574&3003&6006&508&2002/2002.
\end{array}                                         \tag{7.1}
\]

The endpoint-neighbour degrees of the missing `AA` upper targets are

\[
\begin{array}{c|l}
k&\text{degree histogram on }M\\ \hline
11&1^1,2^5,3^{20},4^{13},5^1\\
13&1^8,2^{35},3^{52},4^{40},5^{10},6^1,7^1\\
15&1^{47},2^{96},3^{93},4^{71},5^{58},6^{66},7^{73},8^4.
\end{array}                                         \tag{7.2}
\]

Thus each quota graph is matchable, but its minimum Hall surplus is zero.
Any all-`r` theorem demanding positive surplus on these raw quota graphs
would exclude all three authenticated optima.

There is a sharper coupling warning.  If one first takes a deterministic
matching from `M` to the endpoints and only then tries to complete the
remaining containment degrees, the residual flows are

\[
 380/380,\qquad1437/1437,\qquad5494/5498.            \tag{7.3}
\]

At `k=15` the exact deficient left set has `346` endpoints and `2573`
internal vertices, with

\[
 b(X)=5492,qquad \operatorname{cap}N(X)=5488.       \tag{7.4}
\]

The joint lower-bound circulation of Theorem 4.1 is nevertheless feasible
in all three cases:

\[
 840/840,\qquad3168/3168,\qquad12012/12012.          \tag{7.5}
\]

So an independently chosen matching of the upper deficits is not guaranteed
to extend, even on the authenticated atlas.  Quota matchability alone is not
a completion certificate: the quota choice must be coordinated with the
residual flow, for example by the joint circulation.  This does not deny an
existential sequential decomposition; every joint solution contains a quota
matching whose own residual completion succeeds.

A deterministic joint circulation which ignores (4.11) covers only

\[
 100/120,\qquad382/495,\qquad1494/2002              \tag{7.6}
\]

`BB` upper targets.  The frozen completions cover all of them.  This proves
that the paired-turn rows are genuinely additional and are not consequences
of the TU core.

### 7.2 Event curvature

At `d=3`, the next three-shell outer test is `h=5`.  The exact cyclic
curvatures are shown below; `phi_(5,z)^-` and `phi_(5,z)^+` denote the
single designated split coordinate's contributions to the two sums.

\[
\begin{array}{c|r|r|r|r}
k&\Phi_5^-&\Phi_5^+&
  \phi_{5,z}^-&\phi_{5,z}^+\\ \hline
11&143&605&13&55\\
13&429&1976&33&152\\
15&1425&5760&95&384.
\end{array}                                         \tag{7.7}
\]

The positive factors are already depth-three resident, so `Phi_5^-` is
exactly the number of length-four positive runs.  The singleton zero-gap
counts are

\[
                     44,117,330.                    \tag{7.8}
\]

They give exactly the same numbers of repeated adjacent owners in the raw
union derivatives.  Thus none of the three factors is an unchanged
three-shell Pascal parent.

After the authenticated openings, the internal facet length-three defects
are

\[
                    142,429,1424,                   \tag{7.9}
\]

and the union adjacent equalities are

\[
                     44,118,329.                    \tag{7.10}
\]

For the designated split, no cut or seam hits a singleton `B` motif.  Across
all coordinates, only the `k=15` cut `19065--26745` hits one such motif,
at coordinate `13`.  The finite routers are therefore terminal opening
packages, not raw recursive buffer regenerators.

### 7.3 Literal compiler pins

The frozen maximal-envelope words have exact first-occurrence pin matchings:

\[
\begin{array}{c|r|l}
k&\text{pin count}&\text{rank histogram}\\ \hline
11&233&1{:}11,2{:}55,3{:}165,4{:}1,5{:}1\\
13&1093&1{:}13,2{:}78,3{:}286,4{:}715,5{:}0,6{:}1\\
15&4945&1{:}15,2{:}105,3{:}455,4{:}1365,5{:}3003,6{:}0,7{:}2.
\end{array}                                         \tag{7.11}
\]

All three satisfy `DA=DP`.  At `k=11,13` the promoted opening halos are
hollow and the residual targets have explicit boundary positions.  At
`k=15` the compiler was solved afresh; its two exceptional rank-seven pins
are exactly the boundary colours `18553,18033`.  Hence `k=15` verifies full
rematching Hall for its final chronology, not transport of an immutable
parent pin set.

The three packages authenticate the terminal central `COMP_3` slice.  They
do not authenticate fresh child packages at depths two and four, so they are
not finite proofs of `3BRG`.

## 8. A literal segment-lock obstruction

For every short trace motif

\[
 0\,1^\ell\,0\quad\text{or}\quad1\,0^g\,1,
 \qquad \ell,g<h,                                   \tag{8.1}
\]

take the physical transition interval spanning the motif.  If a segment
braid leaves that entire interval inside one retained fragment, the short
run or gap survives; reversal does not change its length.

### Proposition 8.1 (protected motif lock)

Every buffer-regenerating segment braid must cut every short motif interval
or change an internal edge of it.  If immutable witness/compiler supports
forbid every such action on one motif, no segment braid in that atlas can
satisfy `3BRG`.

Hitting all motifs is only necessary.  New seams can create new short runs,
so the final collar automaton or the curvature equations must still pass.

This is the local form of the charge obstruction.  It also explains why an
endpoint router which merely permutes intact sector paths cannot be the bulk
regenerator: it preserves every untouched internal motif.

## 9. Exact remaining lemma

Define `PCTBRG(r,d)` to be the following statement.

For every admissible decorated parent with state `S3(r,d)`, there exist a
physical nonisolated exact `AA` Catalan forest `P`, a common literal
paired-turn/all-depth witness section, and a completion in the declared
correction atlas whose corrected child satisfies:

1. the forced section respects the typed quotas (endpoint at most one,
   internal and right-owner at most two) and passes every residual cut of
   the typed lower-bound circulation;
2. the central child package `P_d` is obtained by the intact three-depth
   transports in (2.1), repaired only through the declared service cells;
3. every lower fixed target and every arbitrary-upper target has a retained
   or selected literal witness;
4. the final chronology has zero required outer curvatures and passes the
   full event-history automaton;
5. after fixing the three cores, the `d-1,d,d+1` compiler graphs satisfy
   (6.1);
6. a near-perfect physical opening satisfies the terminal boundary and
   suffix clauses.
7. the output is an admissible decorated child carrying a newly named
   protected section and the complete state `S3(r+1,d)`.

### Theorem 9.1 (all-odd reduction through `PCTBRG`)

If one authenticated boundary-PPR base has state `S3(r_0,d)` and
`PCTBRG(r,d)` holds for every `r>=r_0`, then `PCTBRG` implies `3BRG` step by
step, and the coefficient-one upper construction follows by Theorem 2.3.

The content of `PCTBRG` is not another endpoint-matching condition.
Theorem 4.1 has already discharged the complete TU portion.  The unresolved
choice is the common paired-turn/all-depth witness section with the required
curvature charge (nonzero whenever the raw outer defect is positive) and
compatible compiler cores.

The finite data make the boundary sharp:

* positive endpoint surplus is false;
* quota matchability alone does not certify residual completion;
* joint typed flow is true;
* joint typed flow without turn rows is insufficient;
* occurrence-zero regeneration is impossible;
* terminal `COMP_3` is true, but recursive side packages are unaudited.

No broader obstruction to unrelated Boolean/Johnson carriers is claimed.

## 10. Frozen replay

```text
scratch/audit_k11_k13_k15_pascal_coupled_brg_flow_20260730.py
ff1a37d0a9d436c933d25d786a7390f0f7adfa15419374f65e24b6d8d6f2b78f

scratch/k11_k13_k15_pascal_coupled_brg_flow_20260730.audit.json
4f1a13142592f23efb5e669da586595d302479e6894696166b9b05018ebe4349
```

The audit pins the six authenticated inputs at

```text
answers/k11.word
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850

answers/k15.word
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b

scratch/ad_k11_fixed_chronology_onecore_20260729.word
77948a035af179339e4dfc88f56efb11039daa33beef657b5ca215836448dc5b

scratch/ad_k13_fixed_chronology_onecore_20260729.word
749f3bbc21c62fd2a89148401ba078d4543ef71867d7ae8e2eea82cbb10e9858

scratch/k13_two_cycle_one_seam_path_000.json
baa204bf8208c531cc1905c6cf53a2438db85a0b778231c0e59a631eef4b7973

scratch/k15_fixed_matching_pbbs_resident_20260729/
  from3_markov_s7_merge.components.json
f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151
```

The script hash-pins the frozen source factors and compiler words;
reconstructs the `AA` forests and frozen typed incidences; solves the
independent endpoint matching, sequential residual flow, and joint
lower-bound circulation deterministically; records the exact deficient
`k=15` cut; evaluates the `BB` turns; computes the cyclic and opened event
defects; and reconstructs the literal compiler pin matchings.

Its scope is finite and explicit.  It does not solve the paired-turn,
deeper-shadow, chronology, recursive-buffer, or all-`r` existence problem.

## 11. Final proved boundary

The strongest proved positive theorem is the typed containment circulation:
after a buffered exact `AA` forest is chosen, all degree, lower `q=1`, and
`z`-upper `q=1` constraints are one integral network with lower bounds.

The strongest proved negative theorem is run-curvature rigidity: an
occurrence-zero physical router cannot regenerate a consumed Pascal event
buffer, and a fixed atom library must generate the exact required curvature
charge (3.17), which is nonzero whenever the displayed raw defect is
positive.

The all-`k` gate is now one simultaneous object rather than a list of broad
requirements: a paired-turn/all-depth physical witness section whose forced
arcs pass the typed circulation and whose required curvature endpoint passes
the three fixed-core compiler Hall systems and the near-perfect opening.
The authenticated `k=11,13,15` packages show that none of the displayed
qualifiers follows merely from the typed flow or from endpoint quota
matchability; they do not yet supply the parametric section.
