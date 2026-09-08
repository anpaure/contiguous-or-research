# K17 neutral-bridge interaction identity, renewal criterion, and exact accepting cut

**Date:** 2026-08-02  
**Status:** exact local theorem and independently audited K17 calibration.  The
finite evidence proves four bridge/quench instances and one minimal two-C6
interaction square.  It does not prove a bridge from every positive-residence
state.  Source, arbitrary deeper-upper completion, compiler, residency, and a
word are outside scope.

## 1. Frozen checkpoint and literal hard face

The current terminal checkpoint is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
    checkpoint_fullq1_escape_res1994/model
SHA256 127f97f02d238215367a1d5291853e0dd7ecb6d2d227cfcfed1c365e68d5ebcd
```

Its current frozen bindings are

```text
passive audit       9673e703985640504c41b95953cc96134be2a481639312ca59f553deaaab2343
independent audit   6bae984f36d2d72ca65af39e2e8438ef488404f21d8446e487c034037783e148
manifest file       0dc6f0fbba8b9d8e509811b329e02bd35ec6493d1b82c92cf28969bc26aef714
lineage table       3492efa528dcffa3ffd3340e52e8c57bbb64498ae153b9955ee826f820e8a391
```

The independently replayed endpoint has all `19,412` ordinary necessary
non-`D` rank-ten provider rows, all `19,448` opened rank-ten targets in each
literal orientation, one augmented-incidence component, and

```text
opened short-run histograms       (1267,727), (1268,726)
opened residence                  1994, 1994
opened holes ranks 10..17         (0,1520,271,4,0,0,0,0), both orientations.
```

The distinction `19,412` versus `19,448` is literal throughout this note.
The first is the ordinary non-`D` pair-provider bank.  The second is obtained
only after replaying each complete opening.

For a primary incidence selection `y`, rebuild every quadratic pair channel

```text
p[q,a,b](y)=y[q,a] y[q,b].                               (1.1)
```

Let `X` be the set of materialized factors satisfying all exact lower/owner
degree and aperture rows, the named protected boundary, all `16,261` frozen
clauses evaluated on `(y,p(y))`, all `19,412` ordinary provider inequalities,
both complete `19,448` opened decks, and exactly one augmented-incidence
component.  An arc of the strict state graph is one current-state alternating
`C6` or rank-seven-core star-`C8` whose head also lies in `X`.  Consequently
every physical prefix, not merely a terminal symmetric difference, is
literal-hard-row legal.

## 2. The exact interaction identity

Let `A` and `B` be two incidence toggles that are geometrically applicable on
the relevant corners of the square

```text
F --------B--------> BF
|                    |
A                    A
|                    |
v                    v
AF -------B--------> BAF.                               (2.1)
```

For any state function `f`, put

```text
Delta_A f(F)=f(AF)-f(F),
I_f(A,B;F)=f(BAF)-f(AF)-f(BF)+f(F).                      (2.2)
```

Then the state-relative effect of `B` after `A` is exactly

```text
Delta_B f(AF)=Delta_B f(F)+I_f(A,B;F),                   (2.3)
```

and the ordered packet identity is

```text
f(BAF)-f(F)=Delta_A f(F)+Delta_B f(F)+I_f(A,B;F).        (2.4)
```

This elementary mixed finite difference is the missing term in a static sum
of primitive scores.  It is generally nonzero for pair-provider loads, guard
slacks, opened chronology, short-component tokens, and topology.  It vanishes
for the linear exact-degree rows.  Thus `Az_A=Az_B=0` implies
`A(z_A+z_B)=0`, but the integer-cycle-space equation alone says nothing about
strict acceptance of `B` or the sign of the packet.

For a positive provider clause `C`, let `s_C(F)` be its number of live pair
literals and let `n_U(F)` be the load of its rank-ten target.  Equations
(2.3)--(2.4) apply to both integer loads.  For Boolean clause truth use
`g_C(F)=1[s_C(F)>=1]`; the same four-corner identity still applies, although
`g_C` is nonlinear.

For each opening `omega`, canonically label every internal length-one or
length-two run by its coordinate and its bracketed owner/lower trace.  Let
`D_omega(F)` be the resulting multiset.  If a packet phase `P` kills
`K_omega(P)` and births `N_omega(P)`, exact finite-port replay gives

```text
1_Domega(FP)-1_Domega(F)
       =1_Nomega(P)-1_Komega(P),                         (2.5)
R_omega(FP)-R_omega(F)
       =|N_omega(P)|-|K_omega(P)|.                       (2.6)
```

For a bridge followed by a quench, the exact signed identity is

```text
1_Domega(FBQ)-1_Domega(F)
 = (1_Nomega(B)-1_Komega(B))
 + (1_Nomega(Q)-1_Komega(Q)).                            (2.7)
```

An intermediate carrier in `N_omega(B) cap K_omega(Q)` cancels from the
terminal ledger.  Formula (2.7), applied to the union port state or to exact
materialized prefixes, remains valid when primitive supports overlap.  An
independent sum of deltas computed at the root need not equal it; that omitted
quantity is precisely the trace version of `I_f`.

## 3. Minimal authenticated interaction square

The sharp local witness occurs inside seed13 iteration 3, immediately before
the accepted neutral primitive.  Call that prefix state `F`.  Its exact
opened data are

```text
ordinary provider coverage        19412/19412
opened rank-ten holes             (0,0)
opened residence                  (1999,1999)
upper holes ranks 10..13          (0,1522,270,4), both.
```

The two C6s are

```text
A: core 24136, labels 5,7,15
   remove 42017,42200,104090; add 42197,104091,42020
B: core  7880, labels 0,2,14
   remove 10973,10996,42193;  add 10990,42195,10978.     (3.1)
```

They share the rank-eight lower socket `q=24264`.  The selected incidences at
that socket form the literal square

| state | selected `y` at lower `24264` | selected owner masks |
|---|---|---|
| `F` | `42193,42200` | `24265,57032` |
| `AF` | `42193,42197` | `24265,24296` |
| `BF` | `42195,42200` | `24268,57032` |
| `BAF` | `42195,42197` | `24268,24296` |

Both toggles are alternating and degree preserving on the displayed square.
The hard state `BF`, however, is inadmissible.  Among all `16,261` guards it
fails exactly zero-based row `12668` (one-based `12669`), the 45-literal
positive provider row for

```text
U=24300={2,3,5,6,7,9,10,11,12,14}.                      (3.2)
```

On these four assignments the only live candidates in that row are

```text
p_old=p262698=y10993*y10996,
p_new=p387503=y42195*y42197.                             (3.3)
```

Their exact truth table is

| state | `p262698` | `p387503` | guard `g_U` |
|---|---:|---:|---:|
| `F` | 1 | 0 | 1 |
| `AF` | 1 | 0 | 1 |
| `BF` | 0 | 0 | 0 |
| `BAF` | 0 | 1 | 1 |

Thus `A` plants the complementary half-edge `y42197`; `B` deletes the old
provider half `y10996` and installs the other new half `y42195`.  Neither
primitive creates `p_new` alone.  The exact interaction is

```text
I_g(A,B;F)=1,
n_24300(F),n_24300(AF),n_24300(BF),n_24300(BAF)=(1,1,0,1). (3.4)
```

The opened chronology gives the same literal fact in both orientations:
`U=24300` has one witness at `F`, one at `AF`, none at `BF`, and one new
witness at `BAF`.  Hence `BF` has one opened rank-ten hole in each orientation,
whereas `F`, `AF`, and `BAF` have none.  All other guard/provider rows remain
true on the retained strict path `F -> AF -> BAF`; its endpoints are connected
and preserve the protected aperture.

### Proposition 3.1 (alternating half-provider square)

Let `A` be alternating at a hard-legal state `F`, and let `B` be alternating
at `AF`; if the rejected corner `BF` is used diagnostically, also require `B`
to be geometrically applicable at `F`.  Assume that `F,AF,BAF` satisfy the
linear rows, protection, and required topology.
For every provider row that could become tight under `B`, assume there are an
old literal `p_old=y_r y_d` and a replacement literal `p_new=y_a y_b` such
that

```text
A: y_a 0->1 and leaves y_r,y_d selected;
B: y_d 1->0, y_b 0->1, and leaves y_a selected after A;
p_old is live at F and AF;
p_new is live at BAF;
the row has positive exact slack at F, AF, and BAF.       (3.5)
```

Assume every other ordinary provider, both opened provider decks, and every
other guard row has positive exact load at `AF` and `BAF`.  Then `A` followed
by `B` is a strict q1/guard-safe pair even if `BF` is inadmissible.  If in
addition its exact union-port trace replay gives

```text
R_omega(BAF)<R_omega(F),             omega=0,1,           (3.6)
```

then it is a negative closed alternating packet on the full hard face `X`.

#### Proof

The two circuits preserve the linear rows by alternation.  At every critical
provider row, (3.5) keeps the old witness through the first prefix and has the
new witness after the second; the remaining load assumptions cover every
other ordinary, opened, and guard row.  The topology and protection
assumptions supply the non-load hard predicates.  Thus the retained path is
in `X`, and (3.6) supplies strict descent.  Notice that no condition is imposed
on the rejected corner `BF`.  \(\square\)

The seed13 square realizes (3.5) with
`(y_r,y_d,y_b,y_a)=(y10993,y10996,y42195,y42197)`.

### 3.2 Exact short-component transport and merge

The first C6 is genuinely residence neutral in both openings, but not trace
neutral.

* In coordinate 7 it extends the short run
  `{28328,24232}` from length two to length three, killing one defect.
* In coordinate 15 it cuts a long trace and creates a new length-two defect
  `{56424,64552}`, paying back exactly one defect.
* In coordinate 6 it transports the length-two defect
  `{56424,56904}` to `{24264,24137}` while rearranging the adjacent long
  pieces.  Coordinate 5 undergoes only an endpoint/internal transport.

Therefore `Delta_A R_omega(F)=0` for both `omega`, while the state contains a
newly positioned coordinate-6 length-two component through the shared socket.

After `A`, the second C6 merges both coordinate-6 length-two defects

```text
{24264,24137},       {7881,6873}                         (3.7)
```

into components of lengths at least three (one is the displayed length-22
merge in each opening).  It kills two short runs and creates no coordinate-6
short run.  Its coordinate-9 change transports `{7884}` to `{7884,7821}`
without changing the count, and its coordinate-5 change is count neutral.
Consequently

```text
Delta_B R_omega(AF)=-2,             omega=0,1.            (3.8)
```

By contrast, `B` applied directly to `F` is passively residence neutral.  It
kills only the coordinate-6 defect `{7881,6873}` and creates a coordinate-9
singleton `{24264}`; these cancel in the count.  Therefore the exact trace
interaction is

```text
R_omega(F),R_omega(AF),R_omega(BF),R_omega(BAF)
       =(1999,1999,1999,1997),
I_Romega(A,B;F)=-2,                 omega=0,1.            (3.9)
```

The complete upper vectors at the retained corners are

```text
F       (0,1522,270,4),
AF      (0,1521,270,4),
BAF     (0,1519,270,4).                                  (3.10)
```

The inadmissible `BF` has vector `(1,1522,271,4)`: its total including the
rank-ten hole is `1798`, while its deeper rank-11-plus subtotal is `1797`.
This spelling avoids treating the rank-ten failure as a deeper hole.

Equations (3.4) and (3.9) are the exact mechanism: a neutral first circuit
plants both a quadratic provider backup and a trace socket; the second circuit
uses both, replacing the last q1 witness while merging two short components.

## 4. The earlier 2025 neutral bridge and the repeated lineage

At the independently frozen strict floor `F_P` with opened residence `2025`,
the accepted seed-2 bridge is catalogue id `2508`, a C6 with core `15640`,
labels `5,7,9`, and roots `15672,15768,16152`.  It leaves the ordinary and
opened residence unchanged and changes no canonical ordinary short-defect
key.  Its role is purely a nonlinear resource transport:

```text
{p322481,p323382,p326152}
    -> {p322482,p323380,p326154}.                         (4.1)
```

The regenerated guard-safe catalogue changes from `14,119` to `14,122`
rows: eight geometry signatures enter and five leave.  The number of
lossless, connected, opened-full negative singletons changes from zero to one.
The subsequent ordered quench uses ids `2446,12688,2243` and has ordinary
short-defect ledger

```text
bridge: killed 0, born 0;
quench: killed 8, born 1;                 net -7.         (4.2)
```

Two quench C8 schemas are alternating on the parent but hard-row unsafe there.
Core `15128`, labels `0,10,1,15`, loses the sole slack of one-based clause
`8383`; after the bridge its root-`16152` pair transition instead installs
protecting literal `p326147`.  Core `13624`, labels `0,1,11,16`, loses the
sole slack of one-based clause `14771`; the bridge transfers that clause's
backup from `p322481` to `p323380`, so the later root-`15672` transition does
not remove the last live literal.  Applying the three quench toggles without
the bridge is alternating, degree exact, and terminal-connected, but fails
exactly clauses `8383,14771`, covers only `19,410/19,412` ordinary targets,
and leaves two holes in each opened deck.  With the bridge every physical
prefix passes and the endpoint has residence `2018`.

The four authenticated bridge/quench macros have the exact ordinary
short-defect counts

| macro | bridge `(killed,born)` | quench `(killed,born)` | net residence |
|---|---:|---:|---:|
| seed2, `2025 -> 2018` | `(0,0)` | `(8,1)` | `-7` |
| seed13 i1, `2018 -> 2013` | `(4,2)` | `(7,4)` | `-5` |
| seed13 i2, `2013 -> 2003` | `(5,2)` | `(11,4)` | `-10` |
| seed13 i3, `2003 -> 1994` | `(9,5)` | `(7,2)` | `-9` |

The bridge-born, quench-consumed carrier sets have cardinalities `0,1,1,4`.
They are exactly

```text
i1  7:2:12731,13242
i2  5:2:36661,36668
i3  15:3:37626,37850,103098
    15:3:56936,64616,64680
     6:3:24265,24296,24393
     7:3:104603,104633,105144.                           (4.3)
```

Bridge-to-quench root overlaps are respectively

```text
seed2       {15672,16152}
seed13 i1   {12730}, direct new-to-old incidence 19273
seed13 i2   empty
seed13 i3   {24264,70330}, direct new-to-old incidence 124029. (4.4)
```

Thus a shared root or direct incidence handoff is one sufficient interaction
channel, but it is not necessary: iteration 2 interacts through the changed
pair/trace/defect state despite empty bridge/quench root overlap.  Also, only
the first bridge packet is net residence neutral.  The three later bridge
phases already change ordinary residence by `-2,-3,-4`; each portfolio admits
one neutral-budget primitive, but the phase as a whole is not neutral.  The
authenticated recurrence is therefore an exploratory bridge plus regenerated
quench, not repetition of one fixed neutral circuit.

## 5. A sufficient alternating provider-square renewal theorem

Let `Y` be an endpoint-closed subset of `X`, and use the complete materialized
factor (or an injective Markov-equivalent encoding) as the renewal state.  Fix
integers `b,q,delta>=1`.

> **Provider-square trace-expansion hypothesis `PSTE(b,q,delta;Y)`.**  For
> every `F in Y` with positive opened residence there are an accepted bridge
> path `A` of at most `b` primitive C6/star-C8 arcs and a state-relative
> quench path `B` of at most `q` arcs such that:
>
> 1. every materialized prefix of `A` and of `B` lies in `X`;
> 2. the terminal state `H=BAF` lies in `Y` and all temporary batch masks or
>    one-use budgets have been cleared or are literal coordinates of `H`;
> 3. for every last-provider row touched by `B`, the bridge either leaves the
>    old provider alive or plants all complementary half-incidences needed by
>    `B` to install a replacement provider; every other ordinary/opened q1 and
>    guard row has positive exact prefix load;
> 4. the full port replay, not a root-computed primitive sum, satisfies
>
>    ```text
>    R_omega(H) <= R_omega(F)-delta,       omega=0,1.     (5.1)
>    ```

### Theorem 5.1 (bounded repeatable descent)

`PSTE(b,q,delta;Y)` implies a renewable strict packet of length at most
`b+q` from every positive-residence state in `Y`.  Repeated regeneration
reaches a zero-residence state after at most

```text
ceil(max(R_0(F_initial),R_1(F_initial))/delta)            (5.2)
```

macros.  Every prefix preserves both literal opened decks, all `16,261`
guards, ordinary q1, the protected aperture, and one component.

#### Proof

Conditions 1 and 3 give strict hard-row legality in the declared order;
alternation of each primitive gives the linear degree rows.  Condition 4 and
the exact trace identity (2.7) give the claimed decrease in both openings.
Condition 2 makes the endpoint a fresh member of the same quantified family,
so the hypothesis applies again.  The nonnegative integer
`max(R_0,R_1)` falls by at least `delta` per macro, proving (5.2).  \(\square\)

The four-corner half-provider square in Section 3 is a local, checkable
sufficient way to establish item 3 for one critical row: an old sole provider
`y_r y_d` stays alive through `A`; `B` deletes `y_d`, installs `y_b`; `A`
installs `y_a`; and `y_a y_b` is a provider in the same positive clause.  It
does not establish the quantified supply of such a square at every state.

## 6. Exact finite obstruction and why universality is not proved

The frozen data enumerate complete current-state C6/star-C8 catalogues only
at the recorded lineage states and replay the recorded prefixes.  They give
no transitive symmetry or exact weighted bisimulation taking an arbitrary
member of the guarded component to one of those states.  They also show more
than one interaction channel: a defect-neutral pair-channel bridge, direct
shared-root handoffs, and an empty-root-overlap iteration.  Therefore neither
the single square nor the four successful macros implies

```text
every positive-residence F in X has a bridge.             (6.1)
```

There is, however, an exact finite alternative.

Fix bridge/quench bounds `b,q`, a permitted bridge debt `D`, and a root `F`.
Let `B_b^D(F)` be all hard-row-legal bridge endpoints `G` of length at most
`b` and debt at most `D`.  For each such `G`, let

```text
d_q(G)=minimum of Phi(H)-Phi(G) over hard-row-legal
       quench paths G -> H of length at most q,           (6.2)
```

with `+infinity` if no declared accepting endpoint is reachable.  Here `Phi`
may be the exact two-opening sorted lexicographic objective, implemented by
successive optimal faces; for residence-only descent one may take
`Phi=R_0+R_1` while separately requiring both coordinates to fall.

### Theorem 6.1 (accepting-neighborhood cut)

A bounded negative bridge/quench macro exists exactly when

```text
min_{G in B_b^D(F)}
  {Phi(G)-Phi(F)+d_q(G)} < 0.                             (6.3)
```

Equivalently, if

```text
N^-(G)={H: G -> H by an accepted q-bounded quench and Phi(H)<Phi(F)},
```

then the finite obstruction is the empty accepting neighborhood

```text
union_{G in B_b^D(F)} N^-(G)=empty.                       (6.4)
```

#### Proof

Every declared macro has a unique bridge endpoint `G`; its telescoping cost
is `Phi(G)-Phi(F)+Phi(H)-Phi(G)`.  Minimizing first over quenches and then over
bridges gives (6.3), and (6.4) is the same statement without costs.
\(\square\)

To certify (6.4), build the layered product-state graph containing the full
`y,p`, all guard slacks, all ordinary and both opened provider loads, protected
state, complete component/port matching, and both trace states.  Regenerate
the primitive catalogue at every vertex.  Add a sink only from accepted
terminal states and a unit reset arc back to the root.

* If the sink is unreachable, the root-reachable shore `S` has no physical
  outgoing arc to the accepting shore.  With the head-minus-tail incidence
  matrix `N`, `z=-1_S` satisfies `N^T z<=0` and
  `(e_sink-e_root)^T z=1`; this is the exact Farkas cut.
* If the sink is reachable but every accepting path is nonnegative, a
  Bellman--Ford potential `pi` satisfies

  ```text
  pi[v]-pi[u] <= c(u,v),
  pi[sink]-pi[root] >= 0,                                (6.5)
  ```

  and certifies the nonnegative bounded optimum.

Failure of a random portfolio, a root-disjoint plateau, or absence of a
shared-root pair is neither certificate.  At minimum, a strict packet needs
one hard-row-legal outgoing primitive; a positive state with none is the
smallest one-vertex reachable-shore obstruction.

For the complete unbounded finite strict graph, the global obstruction has a
particularly precise form.  For any chosen finite well-ordered objective
`Phi`, every nonterminal state reaches a lower-`Phi` state if and only if every
sink strongly connected component contains a `Phi`-terminal state.  If a
sink component has positive minimum, choose a minimum-`Phi` vertex in it: no
reachable vertex is lower.  Conversely every state reaches a sink component,
and strong connectivity reaches its terminal vertex.  No frozen K17 artifact
currently enumerates this full condensation graph, so this criterion is a
mathematical target, not an authenticated conclusion.

## 7. Audit bindings and exclusions

The minimal provider-square audit is frozen locally at

```text
scratch/k17_fullq1_seed13_i3_guard_cut_independent_20260802/
```

with independent report SHA
`3a307521c607cda4b74ca3514b97be01c0dcd6ac29247628ced711135da97cf1`.
It reconstructs all `875,088` pair variables from the map and evaluates all
`16,261` rows on `F,AF,BF,BAF`.  The independent single-model replays in
`scratch/k17_fullq1_seed13_i3_bridge_identity_20260802/` certify the two
retained prefixes' degrees, guards, q1, topology, both openings, residence,
and upper vectors.  The packet table SHA is
`f930f8563e62e843b65872bf8bd9c1e5da42856784b6291602f32b636bfe50b3`.

The four-macro ledgers and seed-2 controls are frozen under

```text
scratch/audit_k17_fullq1_floor_compounds_20260802/
```

In particular the exact bridge-unlock report, support-overlap ledger,
pair-channel ledger, defect ledger, and 22-prefix metric table have SHAs

```text
9682dadfed6edef04e6259253602550629becb3a3dea19c17da948f04daf23b6
8c0853f3965f382b082d54c12ea7e9bfa03aad0c91d1e18362b822b0f98a79f1
961431d72969786e96bffee5921e544cc9594944889afa8285037b40fd1708c5
bd246434d1c554d2d54ea67dfaccf52fdb574e6ab5f7d41bbad5e8841ec54c61
2aa9356bfc48465350496d401fa7d98b674185e5095084a667d8dfc5ee33295a.
```

Nothing here asserts that residence `1994` is a floor, that all deeper upper
targets are covered, or that an arbitrary source/compiler state can realize
these packets.  The theorem is a strict guarded-factor and opened-chronology
statement only.
