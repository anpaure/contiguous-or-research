# Pump-first augmented ordered Hall damage and corridor avoidance

**Date:** 2026-08-02  
**Lane:** A, global corridor after the twisted-`C6` pump is reserved  
**Status:** unconditional pump-first local separation, exact augmented-table
Hall identity, explicit load sufficient conditions, and a sharp inference
obstruction.  A Boolean theorem proving the required corridor loads is not
claimed.

## 0. Result

Put `k=2m-1` and let `d` be the history depth.  Select one oriented twisted
`C6` pump first and retain its complete developed occurrence bank.  For

\[
 B_m(R)=\sum_{j=0}^{R}{m\choose j}{m-1\choose j},       \tag{0.1}
\]

the number of rank-`m` anchors avoiding a prescribed fixed coordinate `z`
and lying beyond Johnson distance `2d+4` from every pump owner is at least

\[
 {2m-2\choose m}-3(2m-1)B_m(2d+4).                    \tag{0.2}
\]

Thus the strict inequality

\[
 3(2m-1)B_m(2d+4)<{2m-2\choose m},
 \qquad m\ge\max\{3d+4,2d+13\},                       \tag{0.3}
\]

chooses a fixed-`z` seven-ear anchor whose complete local owner, facet, cap,
incidence, and occurrence-history bank is disjoint from the pump.  For
`d=O(sqrt(m))`, a `1-o(1)` fraction of the prescribed-`z` anchor bank is
safe.  This closes the pump-versus-local-ticket avoidance row by an
unconditional deterministic sufficient separation.  It is not a
characterization of every disjoint anchor.

The remaining corridor row has a sharp form.  Fix one safe local ticket,
one pump embedding, one closing join, one physical state table, and one
forward fragment order.  Let `B_0` be the raw tail/head split multigraph
before deleting joins which conflict with the fixed occurrence banks or fail
either endpoint history.  For a left shore `S`, let `D(S)` be the heads for
which **every** literal option from `S` is killed, and put

\[
                   \kappa_0(S)=|N_0(S)|-|S|.          \tag{0.4}
\]

On a capacity-faithful state expansion, the augmented spanning corridor
respecting every encoded occurrence and endpoint-history row exists if and
only if

\[
                         |D(S)|\le\kappa_0(S)
                         \qquad(S\subseteq L_0),       \tag{0.5}
\]

This is the requested literal Hall/avoidance inequality.  It counts
destroyed **heads**, not merely destroyed arcs.  If background charge is
matching-independent, its fixed value is checked once.  Otherwise the
functional charge row must be encoded in the state table or solved jointly;
Hall alone is then necessary but not sufficient for the charged corridor.

There is a usable load form.  If `m_(S,v)` is the number of raw literal
options from `S` to head `v`, `H_(S,v)` is the number rejected by either
history, and `Lambda_(S,v)(q)` is the number using forbidden occurrence
resource `q`, then it is sufficient that

\[
 \sum_{v\in N_0(S)}
  \min\left\{1,
   {H_{S,v}+\sum_{q\in Q}\Lambda_{S,v}(q)\over m_{S,v}}
      \right\}
       \le\kappa_0(S)                                 \tag{0.6}
\]

for every `S`.  After assuming raw Hall, a coarser sufficient row for every
nonempty `S` is

\[
 H(S)+\sum_{q\in Q}\Lambda_q(S)
       \le m_{\min}(S)\kappa_0(S).                    \tag{0.7}
\]

Once (0.5) or (0.6) holds, an ordinary perfect-matching algorithm gives the
literal spanning corridor deterministically provided the table is
capacity-faithful and its background charge is matching-independent or was
encoded in the state expansion.  Otherwise the functional group row still
requires a charge-constrained solve.

The K/A local load theorems do not imply (0.5).  A connected `2x2`
upper-triangular ordered table has a unique perfect matching and may force
one exterior occurrence `q_*`; forbidding `q_*` destroys Hall even if every
local ticket resource is pump-disjoint and the local atlas is arbitrarily
large.  Hence a new accepted-corridor load/expansion theorem is genuinely
necessary.

## 1. Pump-first local bank and quantifiers

Fix one pump branch in the original cyclic child cover.  Let `O_P` be its
`3k` developed owners.  K's radius theorem proves that every owner of a
seven-ear local cycle rooted at `X` lies in

\[
                         B_J(X,2d+3).                  \tag{1.1}
\]

Equality of a local and pump lower facet or immediate cap would put
incident owners at Johnson distance at most one.  Therefore

\[
                d_J(X,O_P)>2d+4                       \tag{1.2}
\]

separates all local owners, lower facets, caps, incidences, and
occurrence-labelled histories.  Bare coordinate names are not treated as
capacity-one occurrence resources.

There are `{2m-2 choose m}` anchors avoiding prescribed `z`, and a radius
`R` Johnson ball has exactly `B_m(R)` members.  Union-bounding the `3k` pump
owners proves (0.2)--(0.3).

For every safe anchor, **all** locally admissible role tickets survive; the
pump kills zero of them.  With `z` externally prescribed and the aperture
labels/banks fixed, their exact role count is

\[
              N_z=(m-1-2d)_2(m-2d-9)_4.               \tag{1.3}
\]

If `z` remains the seventh packet role, the count is instead

\[
 N=(m-1-2d)_2(m-2d-8)_4(m-2d-12).                    \tag{1.4}
\]

These are different quantifiers.  Formula (0.2) belongs to the
prescribed-`z` fibre.  It is also useful to retain the direct polynomial
margin: for every fixed `c>0`,

\[
 3kB_m(2d+4)+ck^7\le {2m-2\choose m}                  \tag{1.5}
\]

leaves at least `ck^7` safe anchors.  For `d=O(sqrt(m))`, (1.5) holds for
all sufficiently large `m` because the Johnson balls are subexponential and
the anchor bank is exponential.

The elementary nonprivate load estimate cannot replace (1.2).  The closed
pump already has `15k` typed owner/facet/cap/incidence resources.  Multiplying
this by an `O(k^6)` per-resource ticket load gives only `O(k^7)`, the same
order as the unconditioned local atlas.  Worse, a collision with the
task-private closure can erase the whole rooted atlas.  Johnson separation
avoids the complete local occurrence closure and makes the actual deletion
count zero.

## 2. Literal raw and augmented ordered tables

Reserve the opened pump path and the opened seven-ear path as two protected
fragments before choosing any spanning completion.  Fix all other fragment
orientations and states, an ambient closing join, and a total order with the
protected root first and final fragment last.  The closing join is required
already to pass both endpoint histories, avoid every private bank, and carry
its literal resource and charge ledger.  Subtract its complete contribution,
and the contributions of the two protected paths, before forming residual
capacities.  Split each fragment into a tail and a head occurrence and keep
only forward joins.  Remove the final tail and protected-root head.  The
resulting balanced literal option multigraph is

\[
                         B_0=(L_0,R_0,E_0).            \tag{2.1}
\]

Parallel options are retained because the same tail/head pair may have
different literal frames, cap tokens, histories, or sidecars.  Write
`E_0(S,v)` for all options from `S subseteq L_0` to `v in R_0`, and
`N_0(S)` for the corresponding head set.

Let `Q` be the complete fixed zero-residual **join/port occurrence** bank
after the preceding subtraction.  It includes the persistent pump-private
occurrences, saturated facet/cap/join tokens, and protected history/private
resources.  An endpoint owner already counted as a fragment resource is not
consumed again merely because a join is incident with it; only a separately
named join/port occurrence belongs to `Q`.  Define an option `e` to be killed
when

1. either exact endpoint-history relation rejects it; or
2. `R(e)` meets `Q` in a resource of zero residual capacity.

Let `F subseteq E_0` be the killed option set, and let `B=B_0-F`.  Shared
resources of positive residual capacity must still be represented by an
exclusive state gadget or retained as explicit packing rows.  The Hall
theorems below assume a **capacity-faithful** expansion: every perfect
matching of `B` projects bijectively to a literal selection satisfying all
owner/facet/cap/history/private rows.  For an at-most-one row, the
four-endpoint pair-deletion test from the endpoint-conditioned
materialization theorem is exact.  An exact-one row also needs the
complementary no-avoidance test; a general residual capacity needs min/max-
cost matching (or the corresponding endpoint-deletion tests), and coupled
multi-resource rows require an exclusive-state gadget or the exact master.
Without capacity faithfulness, Hall is only a projection and the exact
resource master remains necessary.

For `S subseteq L_0`, define the completely destroyed head set

\[
 D(S)=\{v\in N_0(S):E_0(S,v)\subseteq F\}.             \tag{2.2}
\]

Then

\[
                         N_B(S)=N_0(S)-D(S).           \tag{2.3}
\]

The complete occurrence ledger has a second exact audit.  Assume `B` has at
least one perfect matching.  For a residual occurrence resource `q`, let
`E_q` be its option set and define

\[
 m_q^- =\min_{M\in PM(B)}|M\cap E_q|,
 \qquad
 m_q^+ =\max_{M\in PM(B)}|M\cap E_q|.                 \tag{2.4}
\]

### Lemma 2.1 (automatic exact-resource rows)

The row

\[
                    a_q\le |M\cap E_q|\le b_q         \tag{2.5}
\]

holds for every perfect matching if and only if
`m_q^->=a_q` and `m_q^+<=b_q`.  For an exact unit row this is equivalent to
both of the following.

1. `B-E_q` has no perfect matching.
2. For every two vertex-disjoint options `e,f in E_q`, deleting their four
   endpoints leaves no perfect matching.

#### Proof

The first statement is the definition of the two extrema.  A perfect
matching avoids `E_q` exactly when it is a perfect matching of `B-E_q`.
A perfect matching uses two members `e,f` exactly when they are disjoint and
extend by a perfect matching after their endpoints are deleted. \(\square\)

Thus ordinary Hall is enough for the complete occurrence ledger only after
every required row passes Lemma 2.1 or has been encoded by an exact exclusive
state gadget.  Checking only the at-most-one half is insufficient for a
required cap/facet token.

## 3. Exact Hall-damage theorem

### Theorem 3.1 (necessary and sufficient encoded augmented Hall row)

On a fixed capacity-faithful table, the protected pump and seven-ear paths
extend through every residual fragment to one co-oriented spanning cycle
respecting all encoded occurrence and endpoint-history rows if and only if

\[
                 |D(S)|\le |N_0(S)|-|S|
                 \qquad(S\subseteq L_0),              \tag{3.1}
\]

If background charge is matching-independent, the full charged corridor
exists precisely when its fixed value is the required one.  If charge depends
on the chosen matching, (3.1) is necessary and sufficient only for the
uncharged encoded corridor; the functional group row must be encoded or
imposed jointly.

#### Proof

By (2.3), Hall's inequality in the augmented graph is

\[
 |N_0(S)|-|D(S)|\ge |S|,
\]

which is exactly (3.1).  A perfect matching then selects one forward join
out of every nonfinal fragment and into every noninitial fragment.  Forward
acyclicity and the unique two exposed roles make it one spanning path;
adding the fixed closing join gives one cycle.  Capacity faithfulness and
literal expansion give every encoded exact occurrence and history row.

Conversely, contract any claimed literal cycle and delete its closing join.
The selected forward joins give a perfect matching of `B`, so Hall and
(3.1) follow.  The additive fragment ledger gives the stated charge
qualification. \(\square\)

The theorem remains valid when the raw table itself fails Hall: then some
`kappa_0(S)` is negative and (3.1) is impossible.  On A's rigid same-rail
face, every perfect matching has one fixed background charge, so it is
evaluated once.  Outside that face, the additive group row remains a
functional matching constraint and is not implied by (3.1).

### Corollary 3.2 (exact global min--max certificate)

Let `A` be a declared family of literal choices
`a=(theta,omega,e_cl,prec,Sigma)` of a pump-disjoint seven-ear ticket, common
endpoint state, already-legal closing join, forward order, and state table.
Each member is capacity-faithful and also **charge-faithful**: its charge is
either fixed at the required value or encoded in the expanded state.  For
choice `a`, write `D_a,kappa_a` for (2.2) and (0.4), and put

\[
 \Delta_P=
   \min_{a\in A}\ \max_{S\subseteq L_a}
        \bigl(|D_a(S)|-\kappa_a(S)\bigr),              \tag{3.2}
\]

with value `+infinity` when there is no candidate `a`.  The empty shore
makes each inner maximum nonnegative.  The desired pump-first augmented
corridor within `A` exists if and only if

\[
                              \Delta_P=0.              \tag{3.3}
\]

#### Proof

For fixed `a`, (2.3) gives

\[
 \max_S(|S|-|N_B(S)|)
   =\max_S(|D_a(S)|-\kappa_a(S)).                     \tag{3.4}
\]

Thus the inner maximum is the exact matching deficiency, and Theorem 3.1
gives (3.3) after minimizing over `A`.  If `A` is proved exhaustive in the
strong sense that it contains the literal state restriction induced by every
valid physical corridor, then (3.3) is also equivalent to unrestricted
existence.  Without that exhaustiveness proof it is exactly a certificate for
the declared family and no more. \(\square\)

K's Johnson-ball theorem proves only that the ticket coordinate of `a` has
a nonempty domain.  It does not prove `Delta_P=0`.

### Corollary 3.3 (complete-option survival)

If `B_0` satisfies Hall and, for every `S` and every `v in N_0(S)`, at least
one option in `E_0(S,v)` survives, then `D(S)` is empty and the same ordered
Hall certificate survives the planted bank.

This strong condition is often easier to certify than a new global matching:
one needs a literal survivor for every raw tail-set/head incidence, not
independent marginal survivors at the two pump endpoints.

## 4. Explicit resource/history load inequalities

For `v in N_0(S)`, put

\[
 m_{S,v}=|E_0(S,v)|,                                  \tag{4.1}
\]

let `H_(S,v)` count the options in `E_0(S,v)` rejected by at least one of
the two endpoint histories, and for `q in Q` let

\[
 \Lambda_{S,v}(q)=
   |\{e\in E_0(S,v):q\in R(e)\}|.                     \tag{4.2}
\]

Define

\[
 K_{S,v}=H_{S,v}+\sum_{q\in Q}\Lambda_{S,v}(q).       \tag{4.3}
\]

This is a union upper bound; an option killed for several reasons may be
counted several times.

### Theorem 4.1 (weighted Hall-avoidance inequality)

For every `S`,

\[
 |D(S)|\le
 \sum_{v\in N_0(S)}
       \min\left\{1,{K_{S,v}\over m_{S,v}}\right\}.   \tag{4.4}
\]

Consequently (0.6) for all `S` is sufficient for a spanning augmented
corridor.

#### Proof

If `v in D(S)`, every one of its `m_(S,v)` options is killed and therefore
is counted at least once in (4.3).  Hence `K_(S,v)>=m_(S,v)` and the
corresponding minimum in (4.4) is one.  Every other summand is nonnegative.
Summing proves (4.4), and Theorem 3.1 proves the conclusion. \(\square\)

For the coarser form, assume raw Hall and take nonempty `S`; then
`N_0(S)` is nonempty.  Let

\[
\begin{aligned}
 H(S)&=\sum_{v\in N_0(S)}H_{S,v},\\
 \Lambda_q(S)&=\sum_{v\in N_0(S)}\Lambda_{S,v}(q),\\
 m_{\min}(S)&=\min_{v\in N_0(S)}m_{S,v}.
\end{aligned}                                         \tag{4.5}
\]

Every destroyed head consumes at least `m_min(S)` killed-option counts, so

\[
 |D(S)|\le
 {H(S)+\sum_{q\in Q}\Lambda_q(S)\over m_{\min}(S)}.   \tag{4.6}
\]

This proves (0.7).  A uniform but stronger sufficient condition is

\[
 H_{S,v}+\sum_{q\in Q}\Lambda_{S,v}(q)<m_{S,v}
 \quad\text{for every }S,v;                           \tag{4.7}
\]

then `D(S)=\varnothing` and raw Hall is unchanged.

## 5. Certificate-family avoidance

The same argument may be applied after topology and exact resource rows
have already been solved.  Let `M_0` be any finite family of literal rooted
common-base certificates for one pump-first table, all with the required
background charge.  Let `H(M_0)` count certificates rejected by either
endpoint history, and for a fixed occurrence resource `q` let

\[
 \Delta_{M_0}(q)=|\{M\in M_0:q\in R(M)\}|.            \tag{5.1}
\]

### Theorem 5.1 (accepted-base union bound)

A compatible literal rooted common base exists whenever

\[
 |M_0|>H(M_0)+\sum_{q\in Q}\Delta_{M_0}(q).           \tag{5.2}
\]

#### Proof

The right side upper-bounds the certificates removed by the two histories
or any forbidden resource.  Strict inequality leaves one certificate.
\(\square\)

This is the exact place where a future bounded-load accepted-corridor atlas
would close the theorem.  The `Theta(k^7)/O(k^6)` result presently available
for local fixed-`z` packets is not such an atlas: it says nothing about the
loads `Delta_(M_0)(q)` after the residual common-base, topology, histories,
and cap rows have been imposed.

There is also an exact ticket-first averaging form.  Let `Theta` be a family
prefiltered for pump/Johnson-ball compatibility and all local protected-bank
rows.  The tickets are literally aligned on the same physical
`L_0,R_0,E_0`, closing join, order, and state roles; coordinate-relabelled
tables are not identified.  Every filtered table is capacity-faithful and,
when the charge is not fixed, charge-faithful.  Every ticket-dependent edge
deletion must be charged to an endpoint-history indicator or to a saturated
occurrence resource.  A ticket-level failure not attached to an edge must be
prefiltered or represented by a mandatory dummy row.  Ticket `theta` has its
own filtered graph and destroyed sets `D_theta(S)`.  Put

\[
 {\cal B}(S,v)=
   |\{\theta\in\Theta:v\in D_\theta(S)\}|.             \tag{5.3}
\]

### Theorem 5.2 (one ticket satisfies every shore)

Assume raw Hall, so `kappa_0(S)>=0`.  If

\[
 \sum_{S\subseteq L_0}
   {\sum_{v\in N_0(S)}{\cal B}(S,v)
      \over \kappa_0(S)+1}
       <|\Theta|,                                      \tag{5.4}
\]

then one ticket in `Theta` satisfies every augmented Hall shore
simultaneously.

#### Proof

If ticket `theta` fails Hall, some `S` has
`|D_theta(S)|>=kappa_0(S)+1`.  Hence

\[
 \sum_S{|D_\theta(S)|\over\kappa_0(S)+1}\ge1.         \tag{5.5}
\]

If every ticket failed, summing (5.5) over `theta` and reversing the order
of summation would make the left side of (5.4) at least `|Theta|`, a
contradiction. \(\square\)

The blocking counts in (5.3) admit a literal load bound.  Let `eta_e` be
the number of tickets whose endpoint histories reject option `e`, and let
`lambda_e(q)` be the number of tickets for which resource `q` makes `e`
individually infeasible after all fixed residual demand has been subtracted.
For a unit-demand, zero-residual occurrence this is exactly the number of
tickets whose saturated bank contains `q`; for a general multiplicity it is
not.  Then

\[
 {\cal B}(S,v)\le {1\over m_{S,v}}
  \sum_{e\in E_0(S,v)}
       \left(\eta_e+\sum_{q\in R(e)}\lambda_e(q)\right).            \tag{5.6}
\]

Indeed, every completely blocking ticket contributes at least `m_(S,v)`
killed option incidences.  Equations (5.4)--(5.6) are the precise bridge
from an aligned accepted-ticket load theorem to one common-base certificate.
The current local `O(k^6)` decoder does not bound `eta_e` or `lambda_e(q)`
on this aligned residual table.

## 6. Sharp inference obstruction

The missing implication already fails for the smallest connected ordered
table.  Let

\[
 L_0=\{\ell_1,\ell_2\},\qquad R_0=\{r_1,r_2\},
\]

and take the upper-triangular edges

\[
        \ell_1r_1,\quad \ell_1r_2,\quad \ell_2r_2.    \tag{6.1}
\]

This graph is connected and has the unique perfect matching
`{ell_1r_1,ell_2r_2}`.  Give `ell_2r_2` one exterior occurrence resource
`q_*`, accept every history, and give every edge zero background charge.
If the planted pump reserves `q_*`, the augmented graph isolates `ell_2`.
For `S={ell_2}`,

\[
                  \kappa_0(S)=0,\qquad |D(S)|=1.      \tag{6.2}
\]

Replicate this state table for arbitrarily many pairwise-disjoint local
seven-ear tickets, retaining the same exterior `q_*`.  Every local bank may
obey K's Johnson separation and every nonprivate local resource may have
the proved `O(k^6)` load, while every spanning corridor is killed.

This is an abstract endpoint-state table, not a Boolean-host nonexistence
theorem.  It proves exactly that local anchor abundance and local ticket
loads cannot logically imply (0.5), (0.6), or (5.2).  A Boolean-specific
accepted-corridor expansion or deterministic construction is indispensable.

The failure persists even when every ticket resource has load one.  For
`m>=1`, let the left vertices be `ell_1,...,ell_m`, the right vertices be
`r_1,...,r_m`, and put an option `ell_i r_j` exactly when `i<=j`.  The raw
table has the unique diagonal perfect matching.  For each `i`, make a ticket
`theta_i` reserve one private occurrence `q_i`, and let only the forced
diagonal option `ell_i r_i` use `q_i`.  The resources `q_i` are pairwise
distinct and each appears in one ticket and one option.  Nevertheless ticket
`theta_i` deletes its forced diagonal.  For the suffix shore

\[
 S_i=\{\ell_i,\ldots,\ell_m\},
 \qquad N_0(S_i)=\{r_i,\ldots,r_m\},                  \tag{6.3}
\]

the raw slack is zero and `r_i` is completely destroyed.  Hence every
ticket fails Hall although the cross-ticket resource load is one.  What is
missing is correlation between ticket choice and corridor flexibility, not
merely a better marginal load constant.

## 7. Exact remaining row

The pump-first architecture is now separated into two rigorous stages.

1. Equations (0.2)--(0.3) choose a safe anchor; every local ticket rooted
   there survives with zero pump collision.
2. On one fixed augmented physical table, (0.5) is necessary and sufficient
   for the rooted spanning corridor, while (0.6), (0.7), and (5.2) are
   explicit proof-safe sufficient inequalities.

No arbitrary `S_k` conjugation is used, and the pump is never appended to a
completed factor.  It is a protected fragment before the ordered table is
built.

The remaining positive theorem is therefore sharply named: prove a
Boolean-specific lower bound on `m_(S,v)` or on the accepted rooted-base
family, together with upper bounds on `H_(S,v)` and
`Lambda_(S,v)(q)`, strong enough for (0.6); or construct one table directly.
The residual Ore--Ryser `b`-factor is a necessary owner/lower projection,
but it does not by itself prove the ordered topology, endpoint histories,
complete cap ledger, or zero background charge.

Deeper upper shadows, source/envelope transport, common compiler, and
Pascal regeneration remain downstream.

## 8. Prospective three-fragment Boolean-hex planting

The same calculus gives an exact answer to the stronger proposal in which
the complete old Boolean hex is fixed before the host is completed.  Write

\[
 o_i=t_i\longrightarrow s_i\quad(i\in\mathbb Z_3)     \tag{8.1}
\]

for the three old seams, with `o_0=e` the nonprivate pump edge and `o_1,o_2`
the two fixed partners.  Cutting them exposes three protected directed path
fragments `P_0,P_1,P_2`.  Put the seven-ear fragment in the same ordered
block as `P_1`, and put `P_2` in a third block.  Thus a valid completion must
make three old components before the switch.  Let the coherent Boolean-hex
rotation insert

\[
 n_i=t_i\longrightarrow s_{\pi(i)},                  \tag{8.2}
\]

where `pi` is a 3-cycle.

The literal candidate data must include all of the following.

1. A partition `V=V_0 \dot\cup V_1 \dot\cup V_2`, with `P_i in V_i` and the
   seven-ear fragment in `V_1`, and one total order on each `V_i`.
2. All six seams in (8.1)--(8.2) pass their applicable endpoint-history
   tests and avoid every private bank.
3. The three old seams and three new seams have the same complete encoded
   owner/facet/cap/occurrence resource vector.  Their group-charge difference

   \[
       \chi_{\rm hex}=\sum_i\delta(n_i)-\sum_i\delta(o_i)             \tag{8.3}
   \]

   is either zero, or is explicitly included in the desired charge row.
4. After subtracting the three old seams and all protected paths, the
   residual option expansion is capacity-faithful and, when needed,
   charge-faithful.

Keep only forward joins whose two ends lie in the same `V_i`; remove the
three terminal tails `t_i` and the three initial heads `s_i`.  Call the
resulting balanced raw table

\[
 B_0^{(3)}=(L_0^{(3)},R_0^{(3)},E_0^{(3)}).           \tag{8.4}
\]

Filter it by the exact residual occurrence and history bank, and define
`D_3(S)` and

\[
 \kappa_3(S)=|N_0^{(3)}(S)|-|S|                      \tag{8.5}
\]

exactly as in (2.2) and (0.4).

### Theorem 8.1 (exact three-fragment augmented Hall row)

For fixed candidate data satisfying items 1--4, there is a literal residual
completion into three co-oriented spanning paths, one in each `V_i`, if and
only if

\[
                    |D_3(S)|\le\kappa_3(S)
          \qquad(S\subseteq L_0^{(3)}).               \tag{8.6}
\]

Adding the old seams then gives three cycles containing respectively the
pump fragment, the seven-ear/`o_1` fragment, and the `o_2` fragment.
Replacing (8.1) by (8.2) gives one cycle because `pi` is a 3-cycle.  Every
encoded occurrence resource is preserved by item 3, both endpoint-history
states are legal by item 2, and the final charge changes by exactly
`chi_hex`.

#### Proof

The three within-block forward tables are disjoint.  A perfect matching of
their union selects one outgoing and one incoming join at every nonterminal
fragment.  Forward acyclicity makes the restriction to each block one
spanning path.  Conversely, three such paths give a perfect matching.  The
identity

\[
 N_{B^{(3)}}(S)=N_0^{(3)}(S)-D_3(S)                  \tag{8.7}
\]

turns Hall's theorem into (8.6).  The old closures are three separate
cycles.  The new closures act on their three path blocks by `pi`, hence form
one cycle exactly when `pi` is a 3-cycle.  The remaining assertions are the
literal resource, history, and charge hypotheses. \(\square\)

Thus prospectively fixing `o_1,o_2` really does remove the later
mutual-codegree search and the later question whether the partners lie on
three distinct components.  It does so **conditionally**: those conditions
have been moved into the candidate domain and the stricter table (8.4), not
proved automatically.

### Proposition 8.2 (forward order alone is insufficient)

There are uncharged, history-free tables for which the ordinary one-root
ordered Hall row holds but (8.6) fails.  Take three left roles `ell_i`, three
right roles `r_i`, and only the options

\[
                  \ell_i r_{i+1}\qquad(i\in\mathbb Z_3).             \tag{8.8}
\]

The unrestricted table has a perfect matching.  Assign `ell_i,r_i` to
block `V_i`.  The within-block table (8.4) has no edge at all, so a singleton
shore has `kappa_3=-1`.  Consequently a global forward order and an ordinary
common base need not retain the prescribed three old components.

The counterexample has no resource collision, history failure, or charge
defect.  Therefore block membership (or an equivalent three-role state
expansion) is logically necessary.  The exact global certificate for the
prospective-hex architecture is the analogue of (3.2), minimizing the
maximum left side of (8.6) over all legal choices of partners, three-block
partition, orders, endpoint states, and charge-faithful expansions.  A zero
value is sufficient and, for an exhaustive candidate family, necessary.

This old-phase three-component architecture is not required if the three
**new-phase** seams are prescribed directly in the final cycle.  In that
weaker prospective architecture, the fixed pump path plus the new seams leave
exactly two residual corridors.  The root two-corridor reduction and its
two-root/two-sink specialization of (3.1) give the smaller exact table; the
old phase then serves only as the central-resource and integer-voltage
identity.  No old three-component escape row survives, but role-separated
cyclic order, common endpoint histories, and the functional charge row do.
