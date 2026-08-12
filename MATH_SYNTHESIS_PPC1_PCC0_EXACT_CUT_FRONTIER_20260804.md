# `PPC(1)`, `PCC(0)`, and the exact cut frontier

**Date:** 2026-08-04
**Status:** proof-safe synthesis of unconditional reductions and conditional
implications.  No new all-dimensional upper bound is claimed.

## 0. Verdict

The verified finite statement remains

\[
                    \nu(k)=B(k)\qquad(0\le k\le16),
\]

and `k=17` remains the first unresolved dimension.  None of the inputs
proves, for all `k`, any of

\[
 \nu(k)=B(k),\qquad \nu(k)\le B(k)+1,
 \qquad \nu(k)\le B(k)+O(1).
\]

For a materialized terminal certificate `C`, let

\[
 \tau(C)=c(C)+R({\cal H}(C)),                         \tag{0.1}
\]

where its literal scaffold has length `B(k)+c(C)`, `H(C)` is the complete
omitted family after the final replay, and `R(H)` is the shortest literal
repair length.  Then the exact implication ledger is

\[
\begin{array}{c|c}
\text{terminal charge}&\text{conclusion}\ \hline
\tau=0&\nu(k)=B(k)\text{, using the lower bound},\\
\tau\le1&\nu(k)\le B(k)+1,\\
\sup_k\tau<\infty&\nu(k)\le B(k)+O(1).
\end{array}                                            \tag{0.2}
\]

The new theorems make the lower and upper projection gates exact, but do
not put their witnesses in one literal word.  The strongest single missing
statement on the pivot route is still one parameterized **Protected
Pivot--Path Coinstantiation theorem** `PPC(C)`: `PPC(1)` would prove the
sharp `B+1` bound, while `PPC(C)` for one absolute finite `C` would prove
`B+O(1)`.  Within the current diagonal/folded exact architecture, the
corresponding zero-charge statement remains **Protected Converter--Cycle
Coinstantiation** `PCC(0)`.

## 1. Unconditional gains, at their exact scopes

### 1.1 Lower paths and exact serial Hall

For every widest Boolean rank, in either parity, there is an integral bank
of one saturated descending path per owner such that every rank-`s` set is
visited either

\[
 \left\lfloor{W\over C_s}\right\rfloor
 \quad\hbox{or}\quad
 \left\lceil{W\over C_s}\right\rceil                 \tag{1.1}
\]

times.  Thus lack of visitation is no longer an obstruction.

For a fixed path bank `P`, adaptive boundary counts `b_s`, retained counts
`N_s=C_s-b_s`, and row depth `d`, the exact deficiency is

\[
 \delta_{\rm low}({\cal P})=
 \max_{Q\subseteq{\cal P}}
 \left[
  \sum_s(e_s(Q)-b_s)_+-d|Q|
 \right]_+.                                           \tag{1.2}
\]

Hence capacity-only named flags exist exactly when every cut in (1.2)
vanishes.  If every target is visited and
`L=dW-sum_s N_s`, the equivalent complement form is

\[
 \sum_s\min\{u_s(R),N_s\}\ge d|R|-L
 \qquad(R\subseteq{\cal P}).                          \tag{1.3}
\]

This is capped union expansion, not merely a scalar load condition.

Balanced rank marginals alone cannot certify (1.2) at optimal depth: the
rankwise sharp envelope already exceeds the available depth by
`Theta(sqrt(r))` on a fixed-density cut.  This is a barrier to a
marginal-only proof, not a counterexample to a jointly decorrelated path
bank.  Empty, singleton, and whole-bank cuts are already automatic in the
balanced even specialization; the unresolved cuts are collective
intermediate families.

The no-adjacent-residual-rank law is not part of (1.2).  Restoring it gives
the exact coupled zero--one system consisting of exact rank counts, named
target uniqueness, residual nonadjacency, and owner depth.  Its feasibility
is strictly stronger than the capacity-only Hall family and remains open.

### 1.2 Fixed slots lift; adaptive slots do not follow

For fixed lower and upper banks that are disjoint unions of complete
Boolean layers, a scalar rank transport lifts to an integral named
containment matching.  Iterating over fixed banks gives vertex-disjoint
owner-rooted inclusion ladders.

This theorem does not choose a time bank for each named target.  Adding the
target-across-times rows produces determinant-`2` minors, and the natural
variable-slot formulation is not totally unimodular.  Thus fixed-slot
transport is a genuine positive face, not a rounding of the full named
flag problem.

### 1.3 The random route is localized exactly

Independent abstract balanced partitions have an exact falling-factorial
expectation and a within-rank factorial moment bound.  Their boundary-
weighted normalized expectation is maximized at density one.  These facts
do not transfer to Boolean paths: coordinate stars force visitor blocks to
live inside eligible-owner families and rule out global exchangeability or
density-only domination.

Under a local-uniform visitor marginal, the correct first moment uses
`h_Q(S)/D_s` and is at most `(C_s/W)|Q|`.  The remaining probabilistic route
is precisely a cross-rank local switching moment inequality plus an
energy-sensitive container/entropy estimate.  Both are hypotheses of a
valid reduction; neither was proved by the random-path theorem.

There is now deterministic Boolean-local progress before that missing
step.  At one rank the realized count has the exact eligible-density
sandwich

\[
 |\{S:h_Q(S)=D_s\}|\le e_s(Q)
 \le\min\{F_s(Q),\ C_s-\kappa_s({\cal P}\setminus Q)\}, \tag{1.4}
\]

where `F_s` is the two-block integer capacity bound and `kappa_s` is the
sorted complementary eligible-capacity bound.  For the local
hypergeometric first-moment functional `B_s(Q)`, ordinary set shifting can
only increase `B_s`; hence a fixed-size maximizer may be taken shifted.
Its deficit from the linear incidence bound is at least a positive multiple
of the exact Johnson-local energy

\[
 \sum_{T\in Q}\sum_{U\notin Q}{|T\cap U|\choose s}.   \tag{1.5}
\]

At rank `r-1` and half density, coordinate halfspaces are the unique
maximizers of this local benchmark.  Every fixed-width principal
coordinate star's unavoidable core passes the optimal-depth Hall cut, and
the coordinate-halfspace local benchmark has strict slack.  What remains
is realized multi-rank leakage: shifting has not been proved for `e_s` or
for the switching MGF, and the one-rank bounds in (1.4) have not been shown
to sum below `d|Q|` for every common `Q`.

### 1.4 Retained-old upper witnesses and forests

Fix an occurrence-labelled upper factor `F`, colour classes `E_R`, quotas
`b_R=|E_R|-1`, and a protected rainbow bank `P`.  A joint upper-exact
forest retaining an old witness of every higher target exists exactly when
there is a deletion set `D` which

1. avoids `P`;
2. uses exactly `b_R` occurrences of every colour;
3. meets every factor cycle; and
4. is not a transversal of the witness family of any target.

Equivalently, one occurrence variable per colour satisfies the natural
join of all target and component relations.  Forced-cut cores are only the
singleton blockers; the exact multi-edge guard is the full minimal-
transversal clutter.

After a rainbow witness selector `sigma` is fixed, extension to a rooted
upper-exact forest is ordinary partition--graphic matroid intersection.
Equivalently, with `K` ranging over old factor components,

\[
\partial(H_\sigma)=
 \max_{Y\subseteq{\cal K}}
 \left(
  |Y|-\sum_{R:N_R^\sigma\cap Y\ne\varnothing}b_R
\right)                                               \tag{1.6}
\]

is the exact number of components that must remain unbroken, and extension
is possible exactly when `partial(H_sigma)=0`.  The outer minimum over
selectors is exact but unevaluated.  Witness-token compatibility is an
independent-transversal problem and is not a matroid in general.

### 1.5 Residual physical suffix routing

After one common state, one frozen compensation linkage, all shared
capacities, terminal types, and private prefixes are fixed, let `Gamma` be
the residual typed suffix gammoid and `A_g` the complete physical port menu
of claim `g`.  The weakest exact one-coordinate condition is

\[
 r_\Gamma\!\left(\bigcup_{g\in X}A_g\right)\ge |X|
 \qquad(X\subseteq G).                                \tag{1.7}
\]

For an exact private incidence lift to a port--sink graph `H`, this becomes

\[
 |A(X)\setminus Y|+|N_H(Y)|\ge|X|
 \quad(X\subseteq G,\ Y\subseteq A(X)).               \tag{1.8}
\]

A literal residual `q1` factor-diamond lift supplies a full one-coordinate
router by alternating perfect matchings.  Boolean or Johnson expansion of
values alone does not supply the residual occurrence lift.  A single
frozen compensation path can erase arbitrarily large suffix rank, and two
full marginal routers can still share one insufficient terminal cut.

## 2. Exact remaining cut and correlation ledger

The remaining `B+1` pivot proof is not one unnamed Hall problem.  Its
current exact interfaces are:

1. **Lower serial cuts:** all subsets in (1.2), followed by the stronger
   residual-nonadjacency zero--one lift.  On the current random/container
   route the still-missing uniform step is control of realized multi-rank
   leakage over shifted low-energy families; (1.4)--(1.5) do not yet prove
   the all-subset family.
2. **Upper witness/forest cuts:** the blocker/CSP condition of Section 1.4;
   after a selector is fixed, all component sets in (1.6).
3. **Connector topology:** for the residual component-port graph `B`,
   `delta(B)=max_X(|X|-|N_B(X)|)<=1` is exact for one path plus cycles.
   A direct Hamilton path requires Hall in one ordered prescribed-endpoint
   forward graph; otherwise serial protected cycle accessibility is an
   additional occurrence theorem.
4. **Physical suffix cuts:** (1.7), or (1.8) on a private lift, formed only
   after the fixed background deletion.  If two occurrence coordinates
   are used, the exact common deficiency on nonstructural tickets `G` is

   \[
   \max_{X_0\cap X_1=\varnothing}
   \left[
    |X_0|-r_{\Gamma_0}(A_0(X_0))+
    |X_1|-r_{\Gamma_1}(A_1(X_1))
   \right],                                            \tag{2.1}
   \]

   together with global product closure and an explicit allocation of
   shared capacities.
5. **Literal replay and regeneration:** every preceding witness must live
   in one word and state, the final omitted family must be charged by
   (0.1), and the exported odd child must be literal.

Separate solutions of these rows do not compose.  In particular, (1.2),
(1.6), and (1.7) may be witnessed by different path banks, occurrence
sections, cap states, or backgrounds.

## 3. The single missing pivot theorem: `PPC(C)`

### Protected Pivot--Path Coinstantiation `PPC(C)`

There are one compatible selected odd spine and terminal-only taps on its
even neighbours such that every terminal certificate is one materialized
literal object with total charge at most `C`.  Each odd certificate uses
the one-pivot scaffold and jointly supplies:

1. the exact pattern-faithful named lower inventory on one path bank;
2. one protected rainbow upper-exact forest and a protected Hamilton/all-
   width chronology satisfying the blocker, component, residence, and
   opening rows;
3. the sharp-aperture pivot with a transported background fixed away from
   its cells and literal service of the singleton and both rays;
4. either a direct literal compiler, or residual physical router data
   satisfying the applicable fixed-state cuts and product closure;
5. a complete final replay with its actual repair charge; and
6. literal export of the next odd state.

Each even tap may choose independent terminal-only chronology, cap,
compiler, and repair data, but every datum declared persistent in the odd
state is shared literally.  It need not regenerate or agree with other
even taps.

Then `PPC(1)`, plus separate verification of the finite prefix before the
spine begins, implies

\[
                         \nu(k)\le B(k)+1              \tag{3.1}
\]

for every `k`.  On every odd one-pivot certificate `c=1`, so `PPC(1)`
forces `H=emptyset`.  An even tap of charge at most one may instead have
`(c,R)=(1,0),(0,0)`, or `(0,1)`; zero omission is forced only in the first
case.

For one absolute finite `C`, `PPC(C)` implies `B+O(1)`; its finite prefix
can be absorbed by enlarging the constant.  Thus `PPC(1)` is the strongest
single missing pivot theorem, and its bounded-charge relaxation is the
corresponding single missing `O(1)` theorem.

## 4. Exact `B`: `PCC(0)`

Within the present diagonal/cap-two/folded-ticket architecture,
**Protected Converter--Cycle Coinstantiation `PCC(0)`** asks for one
compatible selected odd spine with zero-charge odd terminals and
zero-charge even taps, all materialized in their own complete states.  In
each terminal state it requires simultaneously:

1. the exact pattern-faithful lower inventory, including prescribed
   boundary cells;
2. a q1-exact cyclic diagonal owner row and a literal cap-two selector;
3. one Hamilton/all-width chronology and a safe linear opening when needed;
4. full-depth conversion of every folded cross-ray ticket to accepted
   physical occurrence types;
5. zero structural zeros, zero two-coordinate deficiency in (2.1), fixed
   background coexistence, and global product closure;
6. literal regeneration on the odd spine; and
7. no extra position and no omitted target after replay.

`PCC(0)`, together with exact verification of every finite dimension before
the spine begins, implies `nu(k)=B(k)` by (0.2).  It is an architecture-
relative missing theorem, not a claim that every exact construction must
use a folded converter.  The converter is genuinely growing-depth on the
current route; it cannot be treated as a bounded local socket.

## 5. Parity scope

Balanced path coverage and fixed complete-layer transport do not require
even dimension.  The reciprocal-envelope calculation and the local-density
random analysis were specialized to `k=2r`.  The retained-old `B+1` factor
and the odd equal-shore diagonal arguments live on their displayed odd-host
faces and do not construct the opposite parity.

An odd spine does not by itself prove an all-dimensional bound.  The
weakest tap-decorated implication needs only one terminal-only even
certificate on each selected odd state.  If the odd and even charge bounds
are `q_o` and `q_e`, respectively, the all-parity bound is

\[
                    B(k)+\max\{q_o,q_e\},             \tag{5.1}
\]

not their sum.  No even-to-even regeneration is required.

The unconditional closed top-bit splice is not a bounded-charge tap.  From
an odd word of excess `q`, its exact even excess is

\[
 2q+\chi_K,\qquad
 \chi_K=2d_{K-1}-d_K\in\{d_K,d_K+2\}=\Theta(\sqrt K). \tag{5.2}
\]

For a splice-relative even word saving `s` positions and omitting `H`, the
exact `B+Q` condition is

\[
                s-R(H)\ge2q+\chi_K-Q.                 \tag{5.3}
\]

Conditional even bilayer slack or router counts are not the physical
saving `s` until one complete even word and replay exist.

## 6. Confidence-neutral conclusion

The new results replace several vague bottlenecks by exact max-flow,
blocker, CSP, matroid-intersection, Rado, and charge conditions.  They also
rule out three generic shortcuts: independent rankwise balance, variable-
slot TU rounding, and globally exchangeable Boolean visitor blocks.

They do not decide whether the exact cut families can be met jointly in one
regenerating literal object.  The proof status is therefore unchanged:
`PPC(1)`, bounded-charge `PPC(C)`, and architecture-relative `PCC(0)` are
open; so are the three all-dimensional bounds in Section 0.  No likelihood
or confidence estimate is attached to any of them.

## 7. Frozen input ledger

Only the following frozen files are treated as direct inputs to this
synthesis.

```text
0959212ab0d1b945b560ee578b856304496aaec0cddd116d755b031b7ee3ab77  MATH_SYNTHESIS_EXACT_B_BPLUS1_ZERO_CHARGE_COINSTANTIATION_20260803.md
d7f8e3547c3c090e75e628035dcf0c5bd362117bd128c0e893ccd1280e7f05ba  MATH_AUDIT_EXACT_B_BPLUS1_ZERO_CHARGE_COINSTANTIATION_20260803.md
5dc12b3da7eec6270d7f998f82a53eb9c268855e649a6923aa52b7cc5327ff62  MATH_THEOREM_BALANCED_OWNER_PATH_MULTISOCKET_HALL_AND_RECIPROCAL_BARRIER_20260803.md
11ce91ba1aca7421766c44fe1838573579f7b07632bfc9913ae6834cf4ea0787  MATH_THEOREM_BALANCED_OWNER_PATH_MULTISOCKET_HALL_AND_RECIPROCAL_BARRIER_INDEPENDENT_AUDIT_20260803.md
9fa093fa802dea9de8b72be67e248b9b5a3a1424ea20c2855c2bb335cca28cc7  MATH_THEOREM_MIXED_COMPLETE_LAYER_TRANSPORT_FIXED_SLOT_LADDER_20260803.md
480a03c1151593de5019e17e765e5cb1e151234a9ec6127f8c305c3721dfd487  MATH_AUDIT_VARIABLE_SLOT_LAYERED_FLOW_NONTU_20260803.md
0595249d93f037238d59e2bd94161af9f2144214731c4387c749f914e9a9b9dd  MATH_THEOREM_RANDOM_BALANCED_PATH_LOCAL_DENSITY_AND_SWITCHING_GATE_20260804.md
7ee0e7c6647e9206d5e2f006f10346568da0e54cf23bd9f15ecbd73c06db0cf9  MATH_AUDIT_RANDOM_BALANCED_PATH_LOCAL_DENSITY_AND_SWITCHING_GATE_INDEPENDENT_20260804.md
da91a6421e47f3467704648f04128fae1210962eb44ad359fb175c1204028a0f  MATH_THEOREM_BOOLEAN_LOCAL_ELIGIBLE_DENSITY_COMPRESSION_AND_COORDINATE_STAR_GATE_20260804.md
0ad08b18a0d667347129c18b3a6dce010244313e22f417b7f3edf498cf1fc20c  MATH_AUDIT_BOOLEAN_LOCAL_ELIGIBLE_DENSITY_COMPRESSION_AND_COORDINATE_STAR_GATE_INDEPENDENT_20260804.md
55cb74c849435cf779322c3898c3d2b550361f47ccbc0f6f809d70c5a0889bb4  MATH_THEOREM_BOOLEAN_JOHNSON_PRIVATE_SUFFIX_RADO_ROUTER_20260803.md
08863fb597d62c610a84de132bbf972e26ec530fe723ae7cd814c6593149c7da  MATH_AUDIT_BOOLEAN_JOHNSON_PRIVATE_SUFFIX_RADO_ROUTER_20260803.md
e9d32b46c907ef85bf1fb791de57d6d6918fb26746521f91ef876b4d919e4c2e  MATH_THEOREM_BPLUS1_RAINBOW_FOREST_BLOCKER_CSP_AND_MATROID_MINMAX_20260804.md
818d1155e7391236f266791e0892dc98b520cf81a6399e6f5e8054ddcc1d0530  MATH_AUDIT_BPLUS1_RAINBOW_FOREST_BLOCKER_CSP_AND_MATROID_MINMAX_20260804.md
d704f94ea276934f0b9fba4d4b6e58a3757d97110805338cd40cc284c699144e  MATH_THEOREM_WEAKEST_EVEN_TERMINAL_TAP_AND_CLOSED_SPLICE_PARITY_TOLL_20260804.md
4c78d07f31d296d64eff57e76912d0719699dda903657fec22fdf0666cfe4b72  MATH_AUDIT_WEAKEST_EVEN_TERMINAL_TAP_AND_CLOSED_SPLICE_PARITY_TOLL_20260804.md
```
