# A core-pinned three-ring reservoir and a coordinate-wall pull completion

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional reservoir strengthening and unconditional physical-topology
reduction.  The complete upper-damage reservoir of a coherent three-ring
can be chosen so that every one of its physical vertices contains one fixed
core coordinate.  In a complement-conjugate canonical pull system there is
a spanning pull tree entirely on the opposite coordinate half.  Therefore,
once the pinned bank has an accessible, phase-consistent **forest** phase
cover, the residual cographic connectivity condition is automatic: the
opposite-half tree extends the forced forest while touching no protected
edge.

This does not prove that the pinned reservoir has such a phase cover, that
it lies in an initially upper-complete globally resident carrier, or that a
typed common cap exists.  It removes one of the two static pull-basis rows:
under core pinning, graphic independence of the forced labels is the only
remaining **physical edge/factor** pull-host obstruction.  A typed cap or
global chronology still needs a separate invariance certificate; vertex
separation alone does not prove that a remote switch preserves occurrence
addresses or interval order.

## 0. Parameters

Work in `ML_m` on a ground set `Omega` of size `2m-1`.  Let

\[
 |B|=m-2,\qquad K=B\cup\{b\},\qquad
 E=\Omega\setminus K,\qquad |E|=m,
\tag{0.1}
\]

and choose distinct cyclic ring labels `a_0,a_1,a_2 in E`.  The coherent
three-ring has lower ports, owners, and seam bases

\[
 I_i=B\cup\{a_i\},\qquad
 L_i=K\cup\{a_i\},\qquad
 R_i=B\cup\{a_{i-1},a_i\},
\tag{0.2}
\]

\[
 U_i=K\cup\{a_{i-1},a_i\}.
\tag{0.3}
\]

Its complete upper-damage family is

\[
 \mathcal D_3=
 \{K\cup T:\varnothing\ne T\subsetneq E,
       \ \{a_{i-1},a_i\}\subseteq T\text{ for some }i\}.
\tag{0.4}
\]

Fix

\[
                         q_0\in B.                 \tag{0.5}
\]

Thus every ring vertex in (0.2), and both endpoints of every ring incidence,
contains `q_0`.

Assume throughout that

\[
 d=O(\sqrt m),\qquad d\longrightarrow\infty.
\tag{0.6}
\]

As usual, a Johnson path is `d`-clipped resident if every positive
coordinate run meeting neither endpoint has length at least `d+1`.

## 1. Pinned low-trace paths

Let `T subset E` have size `t`, and suppose

\[
                         3\le t\le m-d-2.           \tag{1.1}
\]

Put `h=m-t`, so `h>=d+2`, and linearly order

\[
 K-\{q_0\}=(k_0,k_1,\ldots,k_{m-3}).
\tag{1.2}
\]

For `0<=j<t`, define

\[
 W_{T,j}=\{k_j,k_{j+1},\ldots,k_{j+h-2}\},
\qquad
 V_{T,j}=T\cup\{q_0\}\cup W_{T,j}.
\tag{1.3}
\]

There is no wrap, because

\[
 (t-1)+(h-2)=m-3.
\tag{1.4}
\]

### Lemma 1.1 (core-pinned shortened path)

The word

\[
 \mathcal Q_T=(V_{T,0},V_{T,1},\ldots,V_{T,t-1})
\tag{1.5}
\]

is a simple rank-`m` Johnson path with union `K union T`.  Every owner,
immediate lower colour, and immediate upper colour contains `q_0`, and the
three resource rows are simple inside the path.  The path is `d`-clipped
resident.

#### Proof

Each owner has size

\[
 t+1+(h-1)=m.
\]

Successive owners delete `k_j` and insert `k_(j+h-1)`.  Their intersection
and union are respectively

\[
 T\cup\{q_0\}\cup
       \{k_{j+1},\ldots,k_{j+h-2}\},
\tag{1.6}
\]

\[
 T\cup\{q_0\}\cup
       \{k_j,\ldots,k_{j+h-1}\}.
\tag{1.7}
\]

Starting positions distinguish the owners and both immediate palettes.
Equation (1.4) says that the union of the windows is all of
`K-{q_0}`, hence the path union is `K union T`.

Every coordinate of `T union {q_0}` occurs throughout.  An internal
positive run of a `K-{q_0}` coordinate has length exactly `h-1`, and

\[
                         h-1\ge d+1.
\]

Thus the path is `d`-clipped resident. \(\square\)

The three size-two seam traces are represented by the ring hinges
themselves.  They already contain `q_0`.  Moving the single boundary layer
`t=m-d-1` from the low construction to the high-tail construction below is
the only cost of pinning.

## 2. Pinned high-tail paths

Now let

\[
 t=m-h,\qquad 1\le h\le d+1,
\tag{2.1}
\]

and put `Z=K union T`, so

\[
                         |Z|=2m-h-1.                \tag{2.2}
\]

Choose a partition

\[
 Z=C\mathbin{\dot\cup}X\mathbin{\dot\cup}Y,
 \qquad q_0\in C,
 \qquad |C|=h+1,
 \qquad |X|=|Y|=t-1,
\tag{2.3}
\]

and orders `X=(x_1,...,x_(t-1))`,
`Y=(y_1,...,y_(t-1))`.  Define

\[
 A_j=C\cup\{x_{j+1},\ldots,x_{t-1}\}
       \cup\{y_1,\ldots,y_j\},
 \qquad 0\le j<t.
\tag{2.4}
\]

This is a monotone Johnson geodesic, all of whose owners and immediate
palettes contain `q_0`, and whose endpoint union is `Z`.  It has no
internal positive run: `X`-coordinates have initial runs,
`Y`-coordinates have terminal runs, and `C`-coordinates occur throughout.

Choose (2.3)--(2.4) uniformly subject to `q_0 in C`.  The stabilizer of
`q_0` is transitive on every relevant resource layer.  Therefore, writing
`N=|Z|`, a fixed contained resource which contains `q_0` is hit with
probability

\[
 {t\over\binom{N-1}{m-1}}
 \quad\text{for an owner},                         \tag{2.5}
\]

\[
 {t-1\over\binom{N-1}{m-2}}
 \quad\text{for a lower colour},                   \tag{2.6}
\]

\[
 {t-1\over\binom{N-1}{m}}
 \quad\text{for an upper colour}.                  \tag{2.7}
\]

For `h<=d+1=O(sqrt m)`, all three denominators are
`2^(2m-o(m))`.  The number of high-tail traces is at most

\[
 \sum_{h=1}^{d+1}\binom mh=2^{o(m)}.               \tag{2.8}
\]

Before one high path is selected, the ring, all low paths, and all earlier
high paths forbid at most `O(m(2^m+2^{o(m)}))` resources in each layer.
The union bound using (2.5)--(2.7) is `2^{-m+o(m)}<1`.  Hence the high paths
can be chosen greedily so that all owners and immediate palettes are
pairwise distinct and avoid every earlier resource.

We have proved the following strengthening of the clipped reservoir
theorem.

### Theorem 2.1 (core-pinned complete upper-cone reservoir)

For all sufficiently large `m`, the complete three-ring damage family
`mathcal D_3` has a protected Johnson-path bank `P_3(q_0)` such that:

1. every physical vertex of every path, including every lower and upper
   immediate-palette vertex, contains `q_0`;
2. the bank has maximum incidence degree at most two and has no repeated
   owner, lower-q1 colour, or upper-q1 colour;
3. every target in `mathcal D_3` is the union of one contiguous protected
   path;
4. every constituent path is `d`-clipped resident; and
5. the total incidence size is

   \[
                           O(m2^m)=o\!\binom{2m-1}m.
   \tag{2.9}
   \]

The three seam-base paths are the ring hinges themselves.

#### Proof

Use the ring hinges for trace size two, Lemma 1.1 for (1.1), and the greedy
packing above for the remaining traces.  Distinct low traces have distinct
exact intersections with `E`.  All cross-family collisions involving a
high path were included among its forbidden resources.  The path count and
length bound give (2.9). \(\square\)

## 3. The opposite-half pull tree

Let `C_m` be a canonical Middle-Levels factor with a tree-compatible,
pairwise-support-disjoint pull host `H_m`.  The fixed-boundary lollipop
theorem gives, for any coordinate `q`, a pull spanning tree every one of
whose circuit vertices contains `q`.

First choose a nonloop all-six-coherent pull `g_0` in this system.  Its
incidence hexagon together with its three unchanged stubs uses at most
`m+2<2m-1` coordinates, so for `m>=5` choose `q` outside that complete
local support.  Use the fixed-boundary theorem with this same coordinate
`q`, obtaining a compatible pull spanning tree `R_q` whose circuit
vertices all contain `q`.  In particular, `g_0` is vertex-disjoint from
every pull in `R_q`.

Apply Boolean complementation `kappa`.  It is an automorphism of `ML_m`,
interchanging the two shores.  It carries the factor, pull host, circuit
phases, graphic compatibility, and spanning-tree property to a conjugate
system

\[
 (F_0,H)=(\kappa(C_m),\kappa(H_m)).
\tag{3.1}
\]

The complemented distinguished tree, denoted `R^0_q`, has the property

\[
 \boxed{\text{every physical vertex of every pull in }R^0_q
        \text{ avoids }q.}                         \tag{3.2}
\]

Let `g=kappa(g_0)`.  Then every
vertex of `g`, including its unchanged ring stubs, contains `q`; coherence
and nonloopness are preserved.  Thus `g` is a coherent three-ring pull in
the same conjugate factor system, and

\[
                         Z_g\cap Z_e=\varnothing
                         \quad(e\in R^0_q)           \tag{3.3}
\]

at the vertex level.

For the joint construction the quantifier order is: choose this coherent
pull and the absent coordinate first, complement them, and then use the
resulting ring core `B`, common label `b`, and pinned coordinate `q in B`
as the data of Sections 0--2.  No claim is made that an arbitrarily
prescribed ring is realized in this one conjugate host.

## 4. Coordinate-wall basis extension

The following graphic lemma is elementary but is the useful quantifier
swap.

### Lemma 4.1

Let `R` be a spanning tree of a connected graph `H`.  Every graphic forest
`J subseteq E(H)` extends to a spanning tree

\[
                         J\subseteq T\subseteq J\cup R.
\tag{4.1}
\]

#### Proof

Contract every component of `J`.  The image of the connected graph `R` is
connected, after loops are deleted.  Choose a spanning tree of that image
and lift its edges.  Adjoining them to `J` gives (4.1). \(\square\)

For the next theorem, let `H` be any pairwise-support-disjoint,
tree-compatible pull host on the components of `F_0` which contains the
guaranteed labels `R^0_q union {g}`.  This is an explicit hypothesis.  The
construction above proves compatibility of `R^0_q union {g}` itself; it
does **not** prove that every additional canonical pull belongs to one
larger jointly tree-compatible host.

Now let `D` be any common occurrence-labelled protected edge bank all of
whose endpoints contain `q`.  Keep the old and new ring phases
`O_g,N_g` outside `D`, as in the exact last-ring basis theorem.  Define its
forced installation labels `A_D` by accessibility in this fixed host `H`.
In particular,

\[
                         D\cap Z_g=\varnothing.     \tag{4.3}
\]

### Theorem 4.2 (coordinate-wall last-ring completion)

Suppose:

1. `D` is accessible and phase-consistent;
2. `J=A_D union {g}` is a graphic forest.

Then there is a pull spanning tree `T` containing `J` such that:

* `T-{g}` gives a two-component factor containing `D union O_g`;
* toggling `g` gives a Hamilton factor containing `D union N_g`; and
* every completing pull in `T-J` is physically vertex-disjoint from `D`
  and the complete ring state.

In particular, the residual cographic condition of the exact last-ring
basis theorem is automatic.

#### Proof

Apply Lemma 4.1 to `J` and the opposite-half spanning tree `R^0_q`.  This
gives

\[
                         J\subseteq T\subseteq J\cup R^0_q.
\tag{4.2}
\]

Every circuit in `R^0_q` has all vertices in the `q=0` half, whereas every
edge of `D` and every ring edge has its vertices in the `q=1` half.  Hence
the completion labels `T-J` delete no protected old edge and touch no ring
edge.  Accessibility and phase consistency install `D` through `A_D`.

The tree `T-{g}` has exactly two components, so tree compatibility gives a
two-component factor.  Adding the final tree edge `g` gives a Hamilton
factor and changes exactly the coherent ring phase.  This is the same
last-ring argument as the exact basis theorem, but (4.2)--(3.2) supply the
residual connectivity and physical protected-edge avoidance simultaneously.
\(\square\)

The preceding physical separation has the following conditional typed
consequence.  If a fixed typed state `Theta` has already
been proved invariant under every pull whose complete vertex support lies
in the `q=0` half, and every forced pull in `J` is jointly valid in
`Theta`, then the same tree preserves `Theta`.  Merely placing the named
physical edges of `Theta` in the `q=1` half is not enough: a disjoint pull
may still change global occurrence addresses, interval order, or a cap
route.  Without this extra invariance premise, Theorem 4.2 is a physical
factor theorem only.

### Corollary 4.3 (pinned-reservoir specialization)

Take `D` to be the pinned bank `P_3(q_0)` together with the unchanged ring
stubs and every other common resource whose physical endpoints contain
`q_0`.  If its forced labels form a phase-consistent graphic forest with
the coherent ring pull **inside a tree-compatible extension `H` as above**,
then the bank and ring admit a zero-position-cost last-ring Hamilton
completion.  No separate cographic cut proof is needed.

For the guaranteed minimal host `R^0_q union {g}`, accessibility of a
`q=1` bank forces `D subseteq F_0` and hence `A_D=emptyset`, because every
new phase outside `g` lies entirely in the `q=0` half.  Nontrivial forced
installation therefore requires exactly the additional compatible-host
premise just stated.

### Proposition 4.4 (the wall cannot repair pinned-coordinate residence)

Every completion pull in `T-J` leaves unchanged every factor edge having
at least one endpoint in the `q=1` half.  Consequently, for either fixed
choice of the ring phase, it preserves the entire induced `q=1` path
system, including the multiset of maximal positive `q`-run lengths.  In
particular, a short positive `q`-run present after the forced installation
and the chosen ring phase cannot be repaired by the opposite-half
completion tree.

#### Proof

Every edge of a completion circuit in `R^0_q` has both endpoints in the
`q=0` half.  Its toggle therefore changes no edge incident with a `q=1`
vertex, including no cross edge which inserts or deletes `q`.  Maximal
`q=1` segments and their lengths are determined by precisely those
unchanged edges. \(\square\)

Thus core pinning decouples physical topology but not global residence.
The forced phase or base factor must already join the clipped endpoint runs
into legal global `q`-runs.

## 5. What remains

The joint static ring/reservoir/pull problem has been reduced from

\[
 \text{accessibility}
 +\text{forced graphic independence}
 +\text{residual cographic connectivity}
\]

to

\[
 \boxed{\text{accessibility and forced graphic independence}}
\tag{5.1}
\]

for a reservoir with one common core coordinate.

This is a strict reduction, not the desired all-dimensional host theorem.
The missing theorem must still choose the pinned paths so that their
nonfactor edges are phases of a forest of pulls in the conjugate host, or
else construct a base factor containing them.  The result also does not
upgrade clipped residence to global cyclic residence, create ambient upper
completeness, produce a global antecedent, or prove the terminal
guard-pruned Hall condition.  Nor does coordinate separation alone certify
typed/common-cap invariance under the completing pull tree.

## 6. Dependencies

- `MATH_THEOREM_COHERENT_SINGLE_PULL_THREE_RING_HAMILTON_PLANTING_20260804.md`
- `MATH_THEOREM_THREE_RING_CLIPPED_UPPER_CONE_RESERVOIR_AND_ALLWIDTH_TRANSPARENCY_20260804.md`
- `MATH_THEOREM_FORCED_PULL_PHASE_LAST_RING_BASIS_AND_CONJUGATION_NOGO_20260804.md`
- `MATH_THEOREM_ODD_MIDDLE_LEVELS_FIXED_BOUNDARY_LOLLIPOP_EXISTENCE_20260802.md`
