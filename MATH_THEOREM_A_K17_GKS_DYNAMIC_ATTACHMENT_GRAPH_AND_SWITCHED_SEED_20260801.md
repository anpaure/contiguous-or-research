# `k=17`: exact GKS attachment chronology and an alternating-switch dynamic seed

Date: 2026-08-01  
Lane: A / GKS flag chronology  
Status: exact state graph and independently replayed constructive seed; not a full state-transversal cycle cover or Hamilton chronology

## 0. Result and boundary

Start with the authenticated 1,430-row GKS static flag factor.  Retain all
nine rank-`2,...,8` type masses and all tight lower necklace covers, but
allow the low target assigned to a skip or pair packet to move by an
alternating `2 x 2` containment switch and allow its aligned phase to
change.

There is an exact finite changing-owner graph with

\[
             1430\cdot9=12870
\]

attachment states.  Its arcs are characterized by three survivor
containments and one refresh identity (Theorem 2.1 below).  The original
static certificate has only `669` edges in a maximum loop-free
packet-projection matching, with `738` packets having no nonloop successor
and `523` having no predecessor.  Thus the static certificate is not a
dynamic seed merely by choosing its phases.

Exact alternating low-containment switches produce an independently
replayed static certificate with the same complete flag tower and a much
larger changing-owner support.  The frozen certificate currently used in
this note has:

```text
legal quotient turns                         3828
labelled attachment-state arcs              30624
loop-free packet-projection maximum matching 1158
packets with no nonloop successor             202
packets with no predecessor                   191
loop-free attachment states with no successor 2227
loop-free attachment states with no predecessor 10789
```

The value `1158` is exact for the **packet projection of this fixed
certificate**.  It is an upper bound on any state/owner-compatible partial
cycle cover supported by this certificate.  It is not a feasible cycle
cover: the owner-orbit transversal, equality of the incoming and outgoing
attachment state, subtour, and voltage rows have not been discarded.  In
particular the remaining zero packet rows rigorously rule out a Hamilton
chronology on this fixed certificate.

## 1. Attachment states

For packet `p`, write its frozen rank-eight root as

\[
 Q_p=C^p_0\mathbin{\dot\cup}C^p_1
             \mathbin{\dot\cup}C^p_2.
\]

For every `a notin Q_p`, define the attachment state

\[
 s=(p,a),\qquad T_s=Q_p\cup\{a\},\qquad C^s_3=\{a\}.
                                                        \tag{1.1}
\]

All nine physical incidences are retained, including parallel incidences
which have the same owner necklace orbit.  A state transversal must choose
one state of every packet and one state of every rank-nine owner orbit.
This is precisely a perfect matching of the 9-regular rank-eight/rank-nine
quotient incidence multigraph; it must not be replaced by nine independent
choices.

## 2. Literal changing-owner criterion

Let `s=(p,a)` and let `t=(q,b)` be a target packet state.  Rotate the target
flag through phase `v` and put

\[
 D_i=\rho^v C^q_i\quad(0\le i\le2),\qquad
 D_3=\{\rho^v b\}.
\]

### Theorem 2.1

There is a literal changing-owner transition from `s` to the phase-`v`
copy of `t` iff there is a coordinate `beta` outside `Q_p`, with
`beta != a`, such
that

\[
 T_s-\rho^vT_t=\{a\},\qquad
 \rho^vT_t-T_s=\{\beta\},                           \tag{2.1}
\]

and

\[
 D_1\subseteq C^p_0,qquad
 D_2\subseteq C^p_1,qquad
 D_3\subseteq C^p_2,                               \tag{2.2}
\]

\[
 D_0=\{\beta\}\mathbin{\dot\cup}(C^p_0-D_1)
                    \mathbin{\dot\cup}(C^p_1-D_2)
                    \mathbin{\dot\cup}(C^p_2-D_3).\tag{2.3}
\]

#### Proof

In a literal depth-three age update, the old class-three singleton `a`
is deleted.  Every survivor of old age `i` assigned new age `i+1` must lie
in `C^p_i`, proving (2.2).  Every other retained coordinate is refreshed,
and the entering coordinate `beta` is new, so their disjoint union is
exactly (2.3).  This also proves (2.1).  Conversely (2.1)--(2.3) partition
the new owner into the declared target age classes, and appending `D_0`
performs exactly the asserted deletion, ageing and refresh.  Hence the
conditions are sufficient as well.  `square`

For a legal unlabelled packet turn, `a` may be any of the eight absent
coordinates other than `beta`.  This explains the exact factor eight
between turn and labelled-state-arc counts.

## 3. Exact packet support and its scope

Delete quotient loops and join packets `p,q` when at least one labelled
arc `(p,a)->(q,b)` exists.  Hopcroft--Karp gives the exact maximum number
of pairwise distinct tail packets and head packets.  Every genuine
state-transversal cycle cover projects to such a matching, so this number
is an unconditional upper bound for the fixed certificate.  The converse
is false: a packet matching may use different incoming and outgoing states
of one packet, repeat an owner orbit, or fail the subtour and voltage rows.

The exact state-transversal cycle-cover and ordered-Hamilton min--max are
proved separately in
`MATH_THEOREM_K17_PACKET_STATE_TRANSVERSAL_CYCLE_MINMAX_AND_GKS_ALTERNATING_REPAIR_20260801.md`.
They are the theorem-faithful consumer of the graph constructed here.

## 4. Alternating low-containment switches

Fix the central rank-`6,7,8` GKS skeleton.  A nontriple packet has one low
target item `S`, aligned as `C_0=rho^u S` inside its fixed base `B`.  If
packets `p,q` are on the same skip/pair shore and both cross containments

\[
       \rho^uS_q\subseteq B_p,qquad
       \rho^wS_p\subseteq B_q                         \tag{4.1}
\]

hold for some phases, exchange the two target items and use those phases.
Then each literal packet partition remains valid, every target item is
used with the same multiplicity, and the complete suffix-orbit covers and
all nine type masses are unchanged.  Phase-only changes are parallel-edge
versions of the same operation.  Thus every accepted search move is an
exact alternating containment switch, not a marginal type edit.

The frozen seed differs from the original static factor on 912 packet
rows (`231` skip, `277` broken-pair and `404` native-pair rows), but changes
no central base.  Of those rows, 589 change type.  The independent replay
still obtains the exact masses

\[
 (139,297,8,20,20,140,127,237,442)
\]

and suffix-orbit counts

\[
 (8,40,140,364,728,1144,1430).
\]

## 5. What this supplies to the incidence/deletion-spine master

The output is constructive in two senses:

1. it is a complete literal static flag factor, not a list of desired type
   counts; and
2. every phase-coherent changing-owner turn and every attachment state is
   materialized and independently replayed.

Consequently K's master may use this certificate as a priced dynamic
column bank.  It may not assert a connected carrier from the
packet-projection matching.  The remaining exact order is:

1. choose a packet/owner state transversal;
2. solve the induced directed matching/cycle-cover rows;
3. impose connectedness and nonzero voltage;
4. impose the deletion-spine and upper-opening rows.

Central GKS rank-six alternating surgery is a further enlargement of the
column bank.  It is not performed by the low-switch certificate above.

## 6. Frozen artifacts

```text
scratch/threadA_k17_gks_dynamic_switched_seed2512_20260801.tsv
  SHA256 908651cb50f5a6e8d8f9fead205d252ed67efc95c36a220ec4e052bb089b2451
scratch/threadA_k17_gks_dynamic_switched_seed2512_turns_20260801.tsv
  SHA256 6b417b8413afb915ad03becec0154927f2a659642d26bfdae8bdd80eb909f7b9
scratch/threadA_k17_gks_dynamic_switched_seed2512_static_replay_20260801.audit.json
  SHA256 e0d7c0c28605e3cecd3c78feb3b9fb8b3776ed75baa7c458581bcb7c49fe4b7e
scratch/threadA_k17_gks_dynamic_switched_seed2512_dynamic_20260801.audit.json
  SHA256 59c11f67cf57686c67edd4001b456e9029d47b94b62317babd7f212bfc6b9693
scratch/threadA_k17_gks_dynamic_switched_seed2512_independent_replay_20260801.audit.json
  SHA256 b3b7bbe84bc20c52f888f1c5d8aa71877ebd3aec6efd4b543a05ed314f88f9ac
scratch/search_threadA_k17_gks_dynamic_low_switches_20260801.cpp
  SHA256 0c271ad903ec03b173a879b2dc31fc7d48e01811617fb48dc5be892796502a10
```

The exact min--max wrapper is

```text
MATH_THEOREM_K17_PACKET_STATE_TRANSVERSAL_CYCLE_MINMAX_AND_GKS_ALTERNATING_REPAIR_20260801.md
  SHA256 afe5042b7a3441c4ed1f76ba1506798c708d6332755669489789b74d04dd19c1
```

The independent central `2 x 2` scan subsequently raises packet support to
1,159, while the owner-exact state-transversal search gives a literal
988-edge directed path/cycle forest.  Those strictly stronger but
differently scoped outputs are frozen in
`MATH_THEOREM_A_K17_GKS_CENTRAL_2X2_SINGLE_SWITCH_HIT_20260801.md` and
`MATH_THEOREM_A_K17_GKS_OWNER_EXACT_STATE_TRANSVERSAL_AND_COMPLEMENT_DUAL_AUDIT_20260801.md`.
