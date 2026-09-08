# `k=17` shuffle201 reverse: common-state DM obstruction and exact circuit-augmentation gate

Date: 2026-08-01  
Lane: A / rooted age-partition chronology  
Status: exact fixed-table theorem and exact palette-circuit relaxation.  No
repaired chronology is claimed.

## 0. Verdict and frozen input

This note specializes the common owner/root/`H` gate to

```text
scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201_reverse.candidate.tsv
SHA256 e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd
```

The final rooted flags have exact type masses and one occurrence of every
tight lower flag target.  Rebuilding the literal phase-labelled geometry
gives

```text
rank-eight roots / rank-nine owner orbits                    1430 / 1430
aligned attachment states                                         12870
raw rooted turns / labelled state arcs                       1855 / 14840
packet matching / zero out / zero in                         954 / 234 / 445
owner-projection matching / zero out / zero in              1079 / 0 / 351.
```

Neither projection is the common problem.  On the states having at least
one literal incoming and one literal outgoing arc, the exact root--owner
graph has

```text
eligible state columns / eligible simple edges                    1290 / 1290
zero eligible roots / zero eligible owners                         661 / 526
maximum matching                                                        718
DM Hall shore: roots / owner neighbourhood / deficiency          770 / 58 / 712.
```

Therefore this fixed flag table has no common 1,430-state root/owner/`H`
transversal, before connectivity, voltage, upper shadows, opening, or any
compiler row is imposed.

The exact partial common-cycle optimum is much smaller still.  Only 57
states lie in a directed cyclic SCC, and root/owner conflicts reduce their
maximum common cycle packing to 46 states.  An authenticated packing attains
46 with cycle lengths `17,14,13,2`.

The exact next finite problem is not to combine the packet matching 954
with the owner matching 1079.  It is to regenerate palette-neutral circuits
relative to this new table, rebuild all pairwise final-flag transitions,
and satisfy first the root--owner Hall system and then the conditional
state-transition Hall system.

## 1. Literal attachment states and transitions

Work on `Z_17`, and let `rho` denote cyclic rotation.  For a rank-eight
necklace root representative `Q_q`, the final age flag is an ordered
partition

\[
                  C_0(q)\mathbin{\dot\cup}C_1(q)
                  \mathbin{\dot\cup}C_2(q)=Q_q.       \tag{1.1}
\]

For every `a notin Q_q`, define the aligned attachment state

\[
                  s=(q,a).                              \tag{1.2}
\]

Its `D`-owner is the necklace orbit

\[
        o(s)=\operatorname{can}(Q_q\cup\{a\}),          \tag{1.3}
\]

with its canonical phase retained.  There are nine states at each root and
nine at each owner, hence 12,870 states.

One minor correction is essential.  A root--owner pair need not determine
a unique attachment state.  For the frozen table the 12,870 states project
to 12,862 distinct root--owner pairs: 12,854 pairs have multiplicity one
and eight have multiplicity two.  The exact formulation must retain the
state `a` (and phase), not only `(q,o)`.  In this particular table none of
the eight parallel pairs contributes two live columns; the 1,290
both-live states project to 1,290 distinct simple edges.  Thus the frozen
matching and Hall witness below remain exact.

To construct the directed state arcs, fix a source root `Q_q`, an entering
coordinate `beta notin Q_q`, and a leaving coordinate
`x in Q_q union {beta}`.  Put

\[
 U=Q_q\cup\{\beta\},\qquad
 Q' = U\setminus\{x\}=\rho^\delta Q_{q'}.             \tag{1.4}
\]

Let `D_i=rho^delta C_i(q')`, and let the target attachment in the
representative gauge be `a'=x-delta (mod 17)`.  The rooted age recurrence is
exactly

\[
 D_1\subseteq C_0(q),\qquad
 D_2\subseteq C_1(q),\qquad
 \{x\}\subseteq C_2(q),                               \tag{1.5}
\]

and

\[
 D_0=\{\beta\}\cup(C_0(q)\setminus D_1)
                  \cup(C_1(q)\setminus D_2)
                  \cup(C_2(q)\setminus\{x\}).         \tag{1.6}
\]

For every source attachment `a notin Q_q` with `a != beta`, (1.4)--(1.6)
give the labelled arc

\[
        (q,a)\longrightarrow(q',a')
        \quad\hbox{labelled }(\beta,x,\delta).          \tag{1.7}
\]

There are exactly eight such source attachments for every raw turn.  This
explains `14840=8*1855`.  The frozen table has no quotient or state loop,
but a general augmentation must retain every literal loop admitted by
(1.4)--(1.7).

The identity which couples `D` and `H` is

\[
 \operatorname{owner}_H(1.7)
 =\operatorname{can}(U)
 =\operatorname{can}(Q'\cup\{x\})
 =o(q',a').                                            \tag{1.8}
\]

Thus the `H` owner of an arc is literally the `D` owner of its head state.

## 2. The first exact matching layer

For a fixed final flag table `F`, write `A(F)` for the full state-arc set
(1.7).  A state is **common-live** when

\[
 d_F^+(s)>0\quad\hbox{and}\quad d_F^-(s)>0.             \tag{2.1}
\]

Let `G_live(F)` be the bipartite multigraph with left side the 1,430 roots,
right side the 1,430 owner orbits, and one column `(q,a)` from `q` to
`o(q,a)` for every common-live state.  Parallel attachment columns are
retained when selecting a physical state; they may be merged only for the
cardinality matching calculation.

### Theorem 2.1 (common-live transversal min--max)

The largest number of roots which can be assigned pairwise distinct owner
orbits through individually in/out-live attachment states is

\[
 \nu(G_{\rm live}(F))
 =1430-\max_{P\subseteq\mathcal R}
                 \bigl(|P|-|N_F(P)|\bigr).            \tag{2.2}
\]

In particular, every literal common root/owner/`H` cycle cover requires

\[
                         |N_F(P)|\ge |P|
                         \qquad(P\subseteq\mathcal R). \tag{2.3}
\]

Condition (2.3) is necessary but not sufficient for a common cycle cover.

#### Proof

The equality is the deficiency form of Hall's theorem.  In a common cycle
cover, the selected state at every root has one incoming and one outgoing
arc and is therefore common-live.  Root exactness and `D`-owner exactness
make these selected columns a perfect matching in `G_live(F)`, proving
(2.3).

Conversely, a perfect matching in `G_live(F)` chooses an individually
incoming-live and outgoing-live state at each root and owner.  The witness
arcs establishing those two properties may use unselected endpoint states,
so they need not form one transition matching.  This is precisely why the
converse fails.  \(\square\)

### Theorem 2.2 (the frozen DM obstruction)

For the `e28a8ee...` table, `nu(G_live)=718`.  Alternating reachability from
the unmatched roots in the authenticated maximum matching gives a root set
`P_0` and its exact owner neighbourhood `O_0=N_F(P_0)` with

\[
                |P_0|=770,\qquad |O_0|=58.            \tag{2.4}
\]

Their sorted identifier-list hashes are

```text
P_0 SHA256 980087d9fa6dbd3fc87a8c5ba90179a31aa727f71db5aaffdbbde6395dcd4773
O_0 SHA256 87a3c7dfbcb139dfe64c5f6994f063599247ae18c3f9e1a74820288ac36e25dd
```

Hence every repaired final table `F'` which admits a common
root/owner/`H` cycle cover satisfies the necessary fixed-shore augmentation
inequality

\[
             |N_{F'}(P_0)|\ge770,                    \tag{2.5}
\]

or, equivalently,

\[
 |N_{F'}(P_0)\setminus O_0|
 -|O_0\setminus N_{F'}(P_0)|\ge712.                  \tag{2.6}
\]

#### Proof

The independent decoder rebuilds all flags and arcs and runs an exact
Hopcroft--Karp matching.  The standard alternating shore has neighbourhood
exactly `O_0`, not merely a subset, and deficiency `770-58=712`.  Equation
(2.5) is the Hall row for the same fixed root set in any repaired table;
(2.6) is its set-difference expansion.  \(\square\)

The number 712 is a required **net number of distinct owner neighbours**,
not a lower bound of 712 circuits or 712 changed roots.  A circuit can alter
several eligibility columns, and a change outside `P_0` can make a state
inside `P_0` live by supplying its missing incoming or outgoing endpoint.

## 3. The second exact matching layer

Use a binary `z_s` for every aligned state and a binary `y_a` for every
literal arc.  For fixed `F`, impose

\[
 \sum_{s:\operatorname{root}(s)=q}z_s=1
       \quad(q\in\mathcal R),\qquad
 \sum_{s:o(s)=o}z_s=1
       \quad(o\in\mathcal O),                         \tag{3.1}
\]

and

\[
 \sum_{a:\operatorname{tail}(a)=s}y_a=z_s,
 \qquad
 \sum_{a:\operatorname{head}(a)=s}y_a=z_s.           \tag{3.2}
\]

### Theorem 3.1 (exact common state/owner/root/`H` equivalence)

Equations (3.1)--(3.2) are feasible if and only if the fixed flag table has
a literal depth-three quotient cycle cover with exactly one `D` incidence
at every root and owner and exactly one `H` incidence at every root and
owner.

#### Proof

Equations (3.1) choose one attachment state at each root and make their
`D` owners a bijection.  Equations (3.2) choose one incoming and outgoing
literal arc at every selected state and no arc at an unselected state, so
the selected arcs form a directed cycle cover.  There is one outgoing `H`
incidence at every root.  By (1.8), the `H` owner of every incoming arc is
the `D` owner of its head state.  The selected head states have pairwise
distinct owners by (3.1), so `H` is also owner-exact.  The converse reads
off `z` and `y` from any declared common cover.  \(\square\)

For a root--owner state transversal `Z`, let `B_Z` be the split bipartite
graph of active arcs whose two endpoints lie in `Z`, and define

\[
 \delta_F(Z)=\max_{X\subseteq Z}
                   (|X|-|N^+_{F,Z}(X)|).              \tag{3.3}
\]

Then (3.2) is feasible exactly when `delta_F(Z)=0`.  Consequently the
two-stage fixed-table feasibility test is

\[
 \min_{\substack{Z\text{ satisfying }(3.1)\\
                  Z\subseteq S_{\rm live}(F)}}
                  \delta_F(Z).                        \tag{3.4}
\]

There is a common cover if and only if the feasible family in (3.4) is
nonempty and its minimum is zero.  The frozen table already fails at the
nonemptiness test, so its conditional transition DM shore is not yet
defined.

This theorem does not assert that the quotient cycle cover is connected or
that a lifted cycle has nonzero voltage.

### Theorem 3.2 (exact fixed-table partial common cycle optimum)

On the frozen `e28a8ee...` state graph, the largest set of attachment states
which

1. uses every root and owner at most once, and
2. has exactly one selected incoming and outgoing literal transition at
   every selected state,

has size exactly 46.  There is a witness consisting of four directed cycles
of lengths

\[
                         17,\ 14,\ 13,\ 2.             \tag{3.5}
\]

#### Proof

The 12,870-state directed graph has 12,817 strongly connected components.
Exactly four are cyclic, with sizes `22,19,14,2`; all other states lie in
trivial acyclic components and cannot occur in a directed cycle.  Exact
subset matching inside the four cyclic SCCs, with root and owner uniqueness,
gives component upper bounds `17,13,14,2` (sorted:
`17,14,13,2`).  Their sum is 46.  The independently replayed certificate
uses 46 distinct roots and owners and realizes the four cycles (3.5), so the
componentwise upper bound is attained.  \(\square\)

This does not contradict the common-live matching value 718.  Common-live
matching only asks that each chosen state have some incoming and some
outgoing arc in the full graph; Theorem 3.2 requires those arcs to close on
the same selected root/owner set.

## 4. Exact palette-preserving augmentation

Let `r(f)` be the common type/lower-target resource vector of a flag, with
the inner and outer occurrence of the same lower target using the same
coordinate.  Relative to the frozen flag `f_q^0`, put

\[
                         \Delta_q(f)=r(f)-r(f_q^0).    \tag{4.1}
\]

The complete disjoint support-at-most-two circuit menu is

\[
\begin{split}
 \mathcal C_1&=\{(q;f):f\ne f_q^0,\ \Delta_q(f)=0\},\\
 \mathcal C_2&=\{(p,f;q,g):p<q,\
                    \Delta_p(f)=-\Delta_q(g)\ne0\}.
                                                               \tag{4.2}
\end{split}
\]

Selecting root-disjoint members of (4.2) is a matching: a binary circuit
is an edge between its two roots and a unary circuit is an edge from its
root to a private dummy vertex.  This is a complete basis only for factors
whose changed roots partition into resource-neutral blocks of size at most
two.  It is not claimed to generate the entire palette fibre.

The menu must be regenerated relative to `e28a8ee...`.  The menu which was
used to reach this table is relative to its predecessor and cannot safely
be reused as a next-layer circuit list.

For circuit variables `x_c`, reconstruct the unique final flag `F(x)` at
every root and rebuild (1.4)--(1.7) on every ordered pair of final flags.
In the dynamic formulation below, a state is option-labelled,
`s=(q,f,a)`, and is gated by the assertion that `f` is the final flag at
`q`.  Define state liveness variables

\[
 \ell_s^+=\bigvee_{a:\operatorname{tail}(a)=s}c_a,
 \qquad
 \ell_s^-=\bigvee_{a:\operatorname{head}(a)=s}c_a,
 \qquad
 b_s=\ell_s^+\wedge\ell_s^-,                         \tag{4.3}
\]

where `c_a` is true exactly when the complete endpoint flags of the literal
arc `a` are final.  For a root set `P` and owner `o`, put

\[
 n_{P,o}=\bigvee_{\substack{s:\operatorname{root}(s)\in P\\o(s)=o}}b_s.
                                                               \tag{4.4}
\]

The exact first-stage Hall rows are

\[
                         \sum_o n_{P,o}\ge |P|
                         \qquad(P\subseteq\mathcal R). \tag{4.5}
\]

A maximum matching in `G_live(F(x))` is a complete separation oracle for
(4.5).  The frozen shore (2.4) supplies the first cut without any SAT run.
After (4.5) closes, use (3.1)--(3.2), or separate a second maximum matching
on `B_Z`.

In this option-labelled form, (3.1)--(3.2) also include the gates

\[
                 z_{q,f,a}\le p_{qf},\qquad
                 y_e\le c_e,                          \tag{4.5a}
\]

where `p_qf` is the exact final-flag channel reconstructed from the selected
circuits.  Thus neither a state of an unselected option nor a transition
whose endpoint option is absent can be used.

For the requested optimization order, define

\[
 D^+(x)=|\{q:d^+_{A(F(x))}(q)=0\}|,\qquad
 D^-(x)=|\{q:d^-_{A(F(x))}(q)=0\}|.                  \tag{4.5b}
\]

A proof-safe zeros-first lexicographic objective is

\[
 \left(D^+(x)+D^-(x),\ D^+(x),\
       1430-\nu(G_{\rm live}(F(x))),\
       \min_Z\delta_{F(x)}(Z),\
       \operatorname{cost}(x)\right),                \tag{4.5c}
\]

where `Z` ranges over common-live root--owner transversals and the fourth
entry is evaluated only after such a transversal exists.  Reversing the
second tie-break is a different declared objective; hard-closing
`D^+=D^-=0` before Hall separation is the order-independent feasibility
version.

### Theorem 4.1 (minimal circuit augmentation, exact declared face)

For either cost

\[
 \operatorname{cost}_{\rm roots}(x)=\sum_c|S(c)|x_c,
 \qquad
 \operatorname{cost}_{\rm circuits}(x)=\sum_cx_c,     \tag{4.6}
\]

minimizing (4.6) subject to root-disjointness, exact reconstruction
(4.3)--(4.4), and (3.1)--(3.2) gives exactly the smallest augmentation in
the disjoint support-at-most-two palette-circuit face which admits a common
root/owner/`H` cycle cover.

If only (4.5) is imposed, the optimum is exactly the smallest augmentation
which reaches the common-live relaxation.  It is a lower bound on the full
optimum, not a chronology witness.

#### Proof

Every selected circuit has zero resource change and disjoint supports, so
the final factor remains palette-perfect.  Conversely, every factor in the
declared face has at least one root-disjoint circuit decomposition; distinct
pairings of equal opposite resource differences can represent the same
final factor, and duplicate catalogue records can represent the same local
replacement map.  Equations
(4.3)--(4.5) are precisely Theorem 2.1 on the rebuilt final table, while
(3.1)--(3.2) are precisely Theorem 3.1.  The two objectives in (4.6) count,
respectively, changed roots and selected neutral blocks.  \(\square\)

### Theorem 4.2 (smallest-support authenticated DM escape)

There is a palette-neutral augmentation of support one which increases the
common-live matching from 718 to 719.  It changes root 1080 from

\[
 (\operatorname{type},C_0,C_1,C_2)=(0,1024,10564,9)
\]

to option 2056402,

\[
 (\operatorname{type},C_0,C_1,C_2)=(0,64,11524,9).    \tag{4.7}
\]

The common both-live incidence change is exactly

\[
              -(175,712)+(937,781).                  \tag{4.8}
\]

Here root 937 is in the old DM tail `P_0`, while owner 781 is outside its
old neighbourhood `O_0`.  Fresh replay gives

```text
common-live matching / deficiency          718 / 712  ->  719 / 711
new DM tail / neighbourhood                              767 / 56
packet matching / zero out / zero in                  954 / 234 / 445
owner zero out / zero in                                    0 / 352.
```

This is an absolute minimum-support nonidentity augmentation, because no
nonidentity circuit has support zero.  It is the unique matching gainer
among the complete 220 zero-resource unary extensions on the 574 roots left
untouched by the preceding 449-circuit packet.  No uniqueness is claimed
among every unary flag in the unrestricted fresh `e28` fibre.

#### Proof

The old and new flags in (4.7) have the same type, the same `C_2`, and

\[
                    C_0\cup C_1=11588
\]

on both sides.  Both `C_0` sets have rank one and therefore carry no tight
target resource.  Thus the complete type/lower-target resource difference
is zero relative to both the old `d44b...` packet and the current
`e28a8ee...` table.  The independent verifier reconstructs the final row,
all resources, all literal transitions and the maximum matching; it gives
(4.8) and matching 719.  Support one is nonzero and hence minimal.  The
exhaustive eligible-unary scan supplies the stated scoped uniqueness.
\(\square\)

This move is neutral on the requested root zero-out/zero-in objective and
strictly improves the next common-live objective.  It is not monotone in
all relaxations: owner zero-in worsens from 351 to 352 and one additional
state becomes zero-out.  An escaping Hall edge therefore remains only a
filter; every candidate needs a fresh maximum-matching replay.

## 5. Why circuit gains cannot be added

Eligibility is an ordered-pair predicate.  If two selected circuits change
the flags at roots `p` and `q`, the arc is tested on the final pair
`(f'_p,f'_q)`.  It need not equal either one-sided test
`(f'_p,f_q)` or `(f_p,f'_q)`.  Moreover, changing a head outside a Hall
shore can activate an incoming arc at an unchanged state inside it.

Therefore a DM shore is a pricing certificate, not a list of roots which
must be edited.  The following procedures are unsound:

* adding the individual arc gains of selected circuits;
* requiring all 712 new neighbours in (2.6) to come from changed roots of
  `P_0`;
* solving the packet graph and owner graph independently; or
* selecting a root--owner perfect matching and then assuming its live arcs
  can be paired.

The proof-safe order is:

1. regenerate the unary/opposite-difference circuit menu at `e28a8ee...`;
2. choose a root-disjoint palette-neutral circuit matching;
3. rebuild the complete final flag table and all labelled transitions,
   retaining loops;
4. optimize or hard-close root zero-out and zero-in counts under an
   explicitly declared lexicographic order;
5. separate the root--owner Hall rows (4.5), beginning with (2.4);
6. select the physical attachment state at every root and owner;
7. separate the induced transition matching (3.3).

The old `761/848` zero-root counts belong to the `ad9e15...` predecessor.
For the present frozen table the exact corresponding counts are `234/445`.
Mixing those baselines or their circuit identifiers is invalid.

## 6. Scope and authenticated artifacts

This note proves an exact finite obstruction and an exact minimal-relaxation
formulation.  It proves neither infeasibility of larger/overlapping palette
circuits nor existence of a repaired table.  It deliberately adds no upper
shadow, residence, connectedness, voltage, opening, or compiler gate.

```text
scratch/audit_k17_support2_common_live_transversal_dm_20260801.py
SHA256 b47b06bd46a9b63af55a4a45753c87e8ab1bea50641b34597b0f9dac865ce630

scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/
  shuffle201_reverse.common_live_dm.audit.json
SHA256 3ae325d494eb8ecaa2c068a8a0fd1af280882be3604f6078af283cd57a979dac

scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201_reverse.audit.json
SHA256 2e45e0893199ca046c8dd351a1572494ed26185e9641a50c1e83cbe90a1459b2

scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201_reverse.independent.audit.json
SHA256 264ba804b98b96a216b9087a948f5e74c305f13f3be2d07270ccdd3d94e752a0

scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  reverse.owner.audit.json
SHA256 b332ccc08662e3931d7e6afe59f945ce8e49df32f95311c7315b1b0c64b80e3d

scratch/threadA_k17_shuffle201_common_state_20260801/
  audit_threadA_k17_rooted_common_cycle_core_20260801.cpp
SHA256 7fc6853304a9317614ecb9ad178d0c05c57a13cc2e14bbc43e65b7ed7fefa4f3

scratch/threadA_k17_shuffle201_common_state_20260801/
  common_cycle.certificate.tsv
SHA256 36a28071b4068421d9ba5965f017110bd7ecc045de0a4aae6efef172b2936539

scratch/threadA_k17_shuffle201_common_state_20260801/
  common_cycle.independent.audit.json
SHA256 46de23cd0ca31a817d779eb15413a8f32614b1f569940de01fe8fecbd248240d

scratch/search_k17_e28_dm_unary_augmentation_20260801.cpp
SHA256 6d6cc906c47958eca3316a3426250fa718e581a1c3095534c894cb9e5547ec88

scratch/k17_e28_dm_augmentation_20260801/unary_scan.audit.json
SHA256 9b0fda0403fe2cbb868518b0fd752c0d8f55eb57333704254186534ec549b33f

scratch/k17_e28_dm_augmentation_20260801/
  unary_scan.best_unary.candidate.tsv
SHA256 a3aa2fb148c3b4fdfc92e6069c0b97578dd18b5e34e66469b7899804555d9036

scratch/k17_e28_dm_augmentation_20260801/
  unary_scan.best_unary.e28_primitive.selected_circuits.tsv
SHA256 6143d1e2825445d859473452249e453eaae3b1e17fa2bedaf196c3b7e6d4408a

scratch/k17_e28_dm_augmentation_20260801/
  unary_scan.best_unary.e28_primitive.independent.audit.json
SHA256 e118768a9a5f2e32aaa4c18f48d1ffcd94e7f50309fa4e4029bcf9e15a520a9a
```

The common-live audit's docstring says “unique aligned state” for a
root--owner incidence.  The executable computation is sound because it
ORs every eligible attachment into the simple adjacency set.  The literal
uniqueness wording is false in eight full-table pairs and is superseded by
the multistate formulation in Section 1.
