# R2 theorem: K17 short-basis fundamental-circuit Hall pricing and socket nonmatroid gate

**Date:** 2026-08-02
**Status:** proof-safe exchange and separation theorem, calibrated on the
authenticated compiler-aware carrier `R/H=1918/1681`.  The short-set
matroid theorem and the frozen phase projection shores are used exactly.
The socket conclusion is negative only for the audited fixed-table ticket
catalogue.  This document does not assert a state-balanced compiler,
residence zero, complete upper coverage, a source, or a word.

## 1. Authenticated rebase and scope

The carrier checkpoint is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_compiler_joint_res1918_deep1681_def59_zero49_s7/
```

Its relative 40-entry manifest has SHA

```text
b99333b131b5ddbf0ab36909ee91dfbdb4dcaeee8686c353f186c5290126eba9
```

and every entry passes `sha256sum -c`.  In particular,

```text
carrier model       37a160f2b3f02839fcd9621dccb42cce43a0297016cdf050ded742baa6f84748
independent audit   31b14cb81f9ed66ad8c45f6e52b15364adddb998defd0dc3af7106144d90a6ad
passive audit       098deb7b4dab3abe12d406e48dabdee7d1aab9eb0f3289199eec3725f76af37b
frozen guard bank   e64219c98e4191bbef8e6ba32567cec6286c777755782030fd9cca13669971fc
```

The connected carrier has both-opening values

```text
R=1918, holes[10..17]=[0,1449,230,2,0,0,0,0], H=1681, Phi=5517.
```

Its transported four-flag projections are

```text
phase  matching/heads  deficiency  zero heads  edges    one maximum shore
0      16841/16898         57           46      71926       72 - 15
1      16839/16898         59           49      71992       72 - 13
```

The shore SHAs are respectively

```text
a7275ecf8110b677a2317bc8895493ad5c9f8703867c34148dc7fa831a243864
16a9478bb66686eb4c938da4905a3df249b63476628b3950e4636f53d78f1779
```

These are exact Hall shores of the transported union projection.  They are
not DM/common-cap compiler certificates, and they do not impose same-role
state balance.  Every cut below is therefore stated first for this exact
projection and then lifted conditionally through literal activation.

## 2. The cotransversal short matroid and its rank oracle

Let `F` be the `1748` mandatory free receivers and `H` the `18646` eligible
hard slots.  Let `M` be the transversal matroid on `F dotcup H` induced by
the `18646` real bottom tokens.  A right-vertex set is independent precisely
when it can be matched injectively to distinct real tokens through the
containment graph.  Define

\[
                 N=M_{\rm short}=(M/F)^*                    \tag{2.1}
\]

on ground set `H`.  Its bases are exactly the `1748`-element sets of hard
slots occupied by dummies, hence shortened in an outer-feasible table.

### Theorem 2.1 (exact rank formula)

For every `S subseteq H`,

\[
\boxed{
 r_N(S)=|S|-18646+r_M\bigl(F\mathbin{\dot\cup}(H\setminus S)\bigr).
}                                                            \tag{2.2}
\]

Consequently every rank and independence query in `N`, including every
fundamental-circuit query, is one ordinary maximum bipartite matching.  No
SAT call is involved.

#### Proof

For a matroid `K` on a ground set `E`, duality gives

\[
 r_{K^*}(S)=|S|-r_K(E)+r_K(E\setminus S).             \tag{2.3}
\]

Take `K=M/F`, whose ground set is `H` and whose rank is

\[
 r(M/F)=r(M)-r_M(F)=18646-1748=16898.                 \tag{2.4}
\]

Also

\[
 r_{M/F}(H\setminus S)
 =r_M(F\mathbin{\dot\cup}(H\setminus S))-r_M(F).      \tag{2.5}
\]

Substitution of (2.4)--(2.5) into (2.3) gives (2.2).  The last rank is the
cardinality of a maximum matching in the defining transversal graph.
\(\square\)

### Theorem 2.2 (fundamental circuit by one alternating search)

Let `S` be a current basis of `N`, let `e in H-S`, and let `P` be any real
bottom matching saturating

\[
                    F\mathbin{\dot\cup}(H\setminus S).       \tag{2.6}
\]

Then

\[
 C_N(e,S)=\{e\}\mathbin{\dot\cup}
 \{f\in S:r_N(S-f+e)=1748\}.                         \tag{2.7}
\]

Equivalently, delete receiver `e` from (2.6).  Starting at the now-exposed
real token, run the usual alternating reachability search.  A short slot
`f in S` belongs to (2.7) exactly when the search can terminate at `f`.
Thus

\[
 S-f+e\text{ is an outer-feasible short basis}
 \quad\Longleftrightarrow\quad
 f\in C_N(e,S)-e.                                    \tag{2.8}
\]

#### Proof

Equation (2.7) is the defining fundamental-circuit property of a matroid.
Under duality it is the fundamental cocircuit of `e` relative to the primal
basis `H-S` of `M/F`.  Removing `e` exposes one matched real token; an
alternating path ending at `f` is exactly a rematching of the primal basis
with `f` replacing `e`.  This is equivalent to (2.8). \(\square\)

## 3. Weighted fundamental-circuit pricing

Let `c(v)` be an additive cost paid when hard slot `v` is short.  For fixed
`e notin S`, the best one-element outer exchange has price

\[
 \pi_c(e)=
 \min_{f\in C_N(e,S)-e}\{c(e)-c(f)\}
 =c(e)-\max_{f\in C_N(e,S)-e}c(f).                   \tag{3.1}
\]

Thus a single alternating search exposes all legal partners, and (3.1)
prices them.  For a globally modular objective on one matroid, absence of a
negative fundamental exchange is equivalent to minimum-weight-basis
optimality.

The compiler Hall objective is not globally modular in general.  For phase
`p` and a fixed head shore `X`, write

\[
 \Xi_{p,X}(S)=
 \sum_{v\in X}h^p_v(S)
 -\sum_{u\in U}{\bf1}[n^p_{X,u}(S)>0],               \tag{3.2}
\]

where `h` is active-head demand, `U` is the source-row shore, and
`n^p_{X,u}` is the number of activated records from source `u` into an
active head of `X`.  For `S'=S-f+e`, the exact exchange delta is

\[
\begin{split}
 \Delta_{p,X}(e,f)
 &=\Xi_{p,X}(S')-\Xi_{p,X}(S)\\
 &=\sum_{v\in X}\bigl(h^{p\prime}_v-h^p_v\bigr)
 -\sum_{u\in U}
 \left({\bf1}[n^{p\prime}_{X,u}>0]
             -{\bf1}[n^p_{X,u}>0]\right).           \tag{3.3}
\end{split}
\]

Formula (3.3) counts loss of the last provider and addition of the first
provider exactly.  Counting activated records instead of distinct source
neighbors is unsound.

For an incumbent shore `X`, the exchanged element `e` is currently long
and `f` is currently short.  Hence `f` is not an incumbent demanded head,
and, absent another head-changing actuator,

\[
 \Delta_{p,X}(e,f)
 =-\mathbf 1[e\in X]
 -\sum_u\left({\bf1}[n^{p\prime}_{X,u}>0]
                    -{\bf1}[n^p_{X,u}>0]\right).     \tag{3.4}
\]

Thus shortening a shore head buys one unit only if the accompanying payload
change does not destroy its last distinct source neighbor.  A native
all-real C6/C8 fibre circuit changes only the provider term in (3.4), not
the short-basis demand term.

### Corollary 3.1 (private-ticket modular price)

If, on a declared subbank, every relevant shore resource is carried by one
fixed short element and no activation side effect is shared, then

\[
                 \Xi_{p,X}(S)=\kappa_{p,X}
                    +\sum_{v\in S}g_{p,X}(v).         \tag{3.5}
\]

For nonnegative Benders multipliers `lambda_(p,X)`, put

\[
 \bar c_\lambda(v)=c(v)+
       \sum_{p,X}\lambda_{p,X}g_{p,X}(v).            \tag{3.6}
\]

Then (3.1) with `c` replaced by `bar c_lambda` is the exact weighted
fundamental-circuit price for that fixed linearization.  Without the
private-ticket hypothesis, (3.3), not (3.5), is load-bearing.

## 4. Tight-shore crossing and takeover

For one phase let

\[
 D(S)=\max_X\Xi_X(S),\qquad
 \mathcal T(S)=\{X:\Xi_X(S)=D(S)\}.                 \tag{4.1}
\]

For an exchange `S'=S-f+e` define

\[
 \eta(e,f)=\max_{X\in\mathcal T(S)}\Delta_X(e,f),   \tag{4.2}
\]

and

\[
 \sigma(e,f)=D(S')-\bigl(D(S)+\eta(e,f)\bigr)\ge0. \tag{4.3}
\]

Then

\[
                 D(S')-D(S)=\eta(e,f)+\sigma(e,f).  \tag{4.4}
\]

Hence improving every incumbent maximum shore, `eta<0`, is necessary but
not sufficient.  A previously slack shore, a newly long head, or another
phase can take over.  A fresh maximum matching/min-cut computes `D(S')` and
therefore `sigma`; strict improvement is equivalent to

\[
                         \eta+\sigma<0.              \tag{4.5}
\]

All incumbent maximum shores can be compared without enumerating their DM
lattice.  Lexicographically maximize `(Xi_old(X),Xi_new(X))` by maximum
closure: share the head-selection nodes, duplicate the old/new neighbor
nodes, weight the old layer by a constant greater than the full possible
range of the new score, and impose head-to-neighbor closure arcs in each
layer.  One closure gives (4.2); a second ordinary separator gives (4.3).

For the authenticated carrier, a robust target `D<=58` gives the literal
current-shore rows

\[
 \sum_u q^1_{X_1,u}\ge\sum_{v\in X_1}h^1_v-58,      \tag{4.6}
\]

and

\[
 \sum_u q^0_{X_0,u}\ge\sum_{v\in X_0}h^0_v-58.      \tag{4.7}
\]

Here

\[
 q^p_{X,u}\Longleftrightarrow
       \bigvee_{v\in X} a^p_{uv}                    \tag{4.8}
\]

is encoded in both directions.  At the root, (4.6) reads `13>=14` and is
violated by one; (4.7) reads `15>=14` and has one unit of slack.  If phase
0 is required not to worsen at all, replace `58` by `57` in (4.7), making
it tight.  Crossing just the two displayed shores is necessary only; the
fresh separator in (4.3) is the exact acceptance oracle.

With the sign convention of (3.3), every current phase-1 maximum shore must
satisfy `Delta<=-1` to reach deficiency `58`.  Phase 0 may satisfy
`Delta<=1` under the robust-only bound, or `Delta<=0` under phasewise
nonworsening.  A weighted average of these requirements is not a sound
replacement for their conjunction.

## 5. Native bottom-relay actuators are zero-basis fibre circuits

The frozen consecutive-suffix atlas has the exact census

```text
family   raw suffix sockets   native matching circuits
C6             96619                    246
C8            287269                     16
C10                0                      0
```

Its theorem and audit have SHAs

```text
c97b9ebcec98c481717908260ae12df5a2a5c4474e83826e6b08b3327dd18b31
c158ef6d43d706ce57de010d97b0a18201af1a4e09b46d32fe5d4edf3e8f0c61
```

Those native counts are relative to the atlas table with SHA
`029d3be53e...`; the transported compiler projection uses the later
round-47 table `95dee6e971...`.  The 262 native atlas rows are therefore
conditional pricing columns at the `1918/1681` root: their old alternating
edges must be present in the final bottom matching before activation.  This
theorem does not silently assert that all 262 remain native after the
round-47 relay lineage.

Each native C6 or C8 is an all-real alternating circuit.  It permutes
bottoms among currently long hard slots and therefore leaves the short
basis `S` unchanged.  It is not a fundamental circuit of `M_short`; it is a
**fibre circuit over the same basis**.  It may nevertheless change the
literal lower Hall graph because the long payloads and their socket records
change.

The proof-safe price domain is therefore the pair

\[
 (S-f+e,\ A),
 \qquad f\in C_N(e,S)-e,                              \tag{5.1}
\]

where `A` is a current-native C6/C8 fibre circuit, or a compatible union
whose final bottom matching is binary.  Materialize (5.1), regenerate every
changed long and short mode and both owner phases, and evaluate (3.3).  A
sum of stale singleton deltas is not a certificate.  Raw nonnative C6/C8
sockets may become alternating after the basis exchange, but their
activation must be recomputed from the final matching.

There is no saturated C10 suffix socket in the frozen suffix catalogue.
Because bottom relays do not change suffixes, no C10 may be introduced in
this pricing face.  A C10 option requires a separately audited suffix
rethreading.

The actuator theorem preserves the lower payload partition and the induced
co-middle deck, but not common-state sockets, residence, upper shadows, or a
compiler.  Those remain decoder gates after every packet (5.1).

## 6. Exact outer and activation master

A short basis alone records which hard slots are empty; it does not record
which real bottom occupies each long or free slot.  The joint master must
retain a witness matching `z`:

\[
\begin{aligned}
 \sum_wz_{a,w}&=1 &&(a\text{ a real bottom}),\\
 \sum_az_{a,f}&=1 &&(f\in F),\\
 \sum_az_{a,v}&\le1 &&(v\in H),\\
 s_v&=1-\sum_az_{a,v}.                               \tag{6.1}
\end{aligned}
\]

Equations (6.1) are TU and exactly assert `S={v:s_v=1}` is a basis of
`M_short`.  Fundamental circuits are a pricing language, not a replacement
for the final matching witness.

For every retained socket/state record `g`, activation must be an
equivalence with the final materialized carrier and bottom matching.  In
particular,

\[
 \sum_{g\in\mathcal G_v}r_g=s_v,
 \qquad r_g\le z_e\quad(e\in P(g)),                  \tag{6.2}
\]

together with the shared in/out long-flag equations and the one-common-short
state equation.  One-way implications or a menu generated before a relay
are insufficient.  Hall adjacency `a^p_{uv}` in (4.8) is the OR of exactly
the final activated records supporting that source/head pair.

For every separated shore `X`, introduce `q^p_(X,u)` and add

\[
\begin{aligned}
 q^p_{X,u}&\ge a^p_{uv} &&(v\in X),\\
 q^p_{X,u}&\le\sum_{v\in X}a^p_{uv},\\
 \sum_uq^p_{X,u}&\ge\sum_{v\in X}h^p_v-\bar d_p.    \tag{6.3}
\end{aligned}
\]

Rows (6.3) remain valid when an exchange deactivates an old head or
activates a new one.  The zero-head bound `Z<=bar Z` has the exact extended
form

\[
 h^p_v\le\zeta^p_v+\sum_ua^p_{uv},
 \qquad \sum_v\zeta^p_v\le\bar Z.                   \tag{6.4}
\]

For the next robust face use `bar d_0=bar d_1=58` and `bar Z=49`, together
with `R<=1918`, `H<=1681`, full q1, upper containment, guards, and connected
carrier topology.  Literal state balance is still an additional open gate.

## 7. The socket constraints are not an authenticated second matroid

A useful second matroid does exist under a strict private-ticket theorem:

1. every short element has a fixed, selection-independent ticket menu;
2. frozen states only delete elements or contract mandatory elements;
3. tickets are assigned injectively from a fixed resource set; and
4. there are no lower quotas, implications, mode swaps, shared owner/flag
   equations, or completion side effects.

Under these hypotheses the selectable sets form a transversal matroid.
Fixed partition or laminar upper quotas give the corresponding partition or
laminar matroid.  If every ticket is genuinely private, the rank-`1748`
bases are simply those of a uniform matroid on the supported bank.  Weighted
matroid intersection is then proof-safe; one common exchange is legal when
the two fundamental circuits admit the same removed element.

The frozen K17 files do not meet these hypotheses.  They encode one fixed
`7395`-short table and contain

```text
socket hyperarcs                 2188
short IDs with any socket        1426
short IDs with zero socket       5969
required dynamic short rank      1748
```

Thus even the entire supported fixed-table bank is smaller than the needed
rank, and every private subbank is smaller still.  Moreover, the map has no
outer bottom-placement activation variables, so it cannot certify a family
of alternative rank-`1748` short bases.  No useful second socket matroid is
currently authenticated.  This does not prove that the complete global
variable-bottom catalogue has no such subbank.  The phase-0 catalogue has
since been built, but its aggregate per-slot degree/mask rows are not an
exchange oracle: a physical augmentation verdict still requires all
occurrence-labelled endpoint tickets for the tested slots.

### Theorem 7.1 (smallest literal augmentation obstruction)

In the frozen two-socket endpoint-incidence relaxation let

\[
 I=\{4353\},\qquad J=\{2637,6211\}.                  \tag{7.1}
\]

Each short ID has exactly one ticket:

```text
var 177078: 4350 -> 4353 ->  6218, flags/address (2,8,2)
var 176894: 7785 -> 2637 ->  6218, flags/address (0,7,0)
var 177294: 4350 -> 6211 -> 12481, flags/address (2,4,2)
```

The two tickets of `J` have distinct predecessor-out and successor-in long
roles, so `J` is feasible in this incidence relaxation.  But

* `I+2637` repeats successor-in role `6218`; and
* `I+6211` repeats predecessor-out role `4350`.

Hence `|I|<|J|` and no element of `J-I` augments `I`.  The matroid
augmentation axiom fails.  Three ground elements are minimal: on at most
two elements, heredity makes every smaller feasible set augmentable toward
a larger feasible set.

This is deliberately not called a full-CNF basis counterexample.  The fixed
full CNF is already globally UNSAT because of `5969` empty short rows, so it
cannot certify either `I` or `J` as extendable complete configurations.  The
witness is exact for the natural frozen endpoint-ticket packing relaxation,
and is enough to forbid treating that relaxation as the missing second
matroid.

The independent verifier is frozen at

```text
scratch/r2_k17_mshort_socket_exchange_20260802/
  verify_r2_k17_mshort_socket_exchange_20260802.cpp
  audit.json
```

with source and audit SHAs

```text
f568cef7b7def3d05eba8bf29e08206b098bbccca247f264eb093f08a7b5a853
6fee69bebcff905c8ff78b95e7ec48055fa6a5ec678ec3b2b02237710502bd65
```

## 8. Fail-closed exchange oracle

The resulting proof-safe loop is:

1. Maintain the exact real-bottom matching `z` and its short basis `S`.
2. For each `e notin S`, compute `C_N(e,S)` by one alternating matching
   search using (2.2)--(2.8).
3. Price every `f in C_N(e,S)-e` by the exact current-shore delta (3.3),
   optionally composed with the 246 native C6 and 16 native C8 fibre
   circuits.  Do not generate C10 on the frozen suffix.
4. Materialize the complete bottom matching and carrier endpoint.  Rebuild
   both owner phases, every changed state/socket record, distinct-neighbor
   counts, zero heads, q1, upper containment, and topology.
5. Compute all old-tight crossing values by (4.2), then run fresh phase
   maximum matchings to compute takeover (4.3).
6. Add the exact rows (6.3)--(6.4) for every violated shore and repeat.
7. Accept only an endpoint passing every encoded hard row with a strict
   declared objective improvement.

For a decoded candidate, rank, fundamental circuits, Hall separation, and
takeover are polynomial.  The integral joint optimization is not proved
polynomial: shared activation ORs, owner/flag balance, carrier topology, and
upper containment destroy the one-network TU argument.  Benders or
branch-and-cut is exact; ordinary min-cost matching is exact only for the
outer additive/private-ticket relaxation.

Absence of a negative single fundamental exchange is a global optimum
certificate only for one modular matroid-basis objective.  It is not a
no-go for shared activation, native-fibre pivots, multi-exchange paths, or
the full compiler.

## 9. Exact exclusions

This theorem proves the cotransversal rank/fundamental-circuit oracle, the
sound Hall-shore cuts, the native C6/C8 fibre interface, and the scoped
socket nonmatroid obstruction.  It does not prove:

* a complete global bottom-dependent socket catalogue;
* same-role state balance or a connected literal chronology;
* DM/common-cap compiler feasibility;
* residence zero or ranks 11--17 completion;
* a lower source, exterior cross-window completion, or a terminal compiler;
* suffix rethreading or any C10 actuator; or
* a length-`24313` word.
