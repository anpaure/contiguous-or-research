# The Hall-21 native DM atlas and the exact neutral-router/splitter gate

Date: 2026-07-28

Status: exact finite theorem and reproducible lightweight audit for the
authoritative Hall-21/six-zero carrier.  This note proves the complete
gap-one component census, the simultaneous native critical-shore pins, six
literal depth-two core-rebase ports, forty-five literal singleton
core-shrink ports, and a necessary-and-sufficient forced-pair criterion for
the next Hall descent.  It does **not** exhibit an H20 carrier and does not
claim that a critical-shore common controller already compiles the exterior
15,537 matching edges.

No braid, SAT, or exhaustive carrier search was run locally.  The new audit
only reconstructs the already-fixed compiler graph and takes connected
components and ordinary bipartite matchings.

## 1. Authoritative input and raw evidence

The route into the state studied here is

\[
 H22\xrightarrow{\operatorname{FF}(1320,5339,6194)}H22^{\rm port}
 \xrightarrow{\operatorname{FR}(778,2292,6368)}H21.             \tag{1.1}
\]

The final carrier and the independent route audit are

```text
scratch/k15_segment_braid_hall21_zero6.json
scratch/audit_k15_segment_braid_hall22_to21.json
```

with SHA-256 values

```text
8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447
cc862804ea8910371283e8fdb42c1ac94ce9ed1cb5e0d3b5cdd94e8d74211e5c
```

The new component audit and its machine-readable output are

```text
scratch/audit_k15_h21_dm_components.py
scratch/audit_k15_h21_dm_components.json
```

with SHA-256 values

```text
5b6ac90b3beb3eb96efd977257da222a8710b623734e3b425e4d40cfeab74999
eb33370c853bed9fa8df325c24a9ec5eac52024281cbd7fc2d6bc7a7939d18e7
```

The exact replay command is

```text
python3 scratch/audit_k15_h21_dm_components.py \
  --output scratch/audit_k15_h21_dm_components.json
```

It imports the independent compiler-graph constructor from
`scratch/audit_k15_segment_braid_descent.py`; it does not enumerate any
braid.

## 2. Fixed graph and native pins

Let $P=(P_0,\ldots,P_{6434})$ be the rank-eight middle path and let
$Q=(Q_0,\ldots,Q_{6437})$ be its maximal depth-three erosion controller.
For $d=0,1,2$, a physical compiler cell is the occurrence

\[
 c=(d,s),\qquad \tau(c)=\bigcup_{j=0}^{d}Q_{s+j}.                \tag{2.1}
\]

The exact mandatory-mask rule in the audit defines when a lower target
$x$, $1\le |x|\le7$, is incident with $c$.  Denote this target-cell
graph by $G$.  It has

\[
 |L(G)|=16383,\qquad |R(G)|=19311,\qquad \nu(G)=16362.          \tag{2.2}
\]

The final state is a permutation of all 6,435 rank-eight masks, a Johnson
path, depth-three resident, complete in every upper layer $q=1,\ldots,7$,
and has lower-hole vector

\[
 (4,18,9,1,0,0,0).                                             \tag{2.3}
\]

It has six degree-zero lower targets and Hall deficiency 21.

Take the alternatingly reachable Dulmage--Mendelsohn shore from an exact
maximum matching.  Write its left and right sides as $S,T$.  The exact
sizes are

\[
 |S|=846, |T|=825, |S|-|T|=21.                                 \tag{2.4}
\]

For every $c\in T$, its native trace $\tau(c)$ lies in $S$, is incident
with $c$, and the 825 values $\tau(c)$ are pairwise distinct.  Reserving
these 825 target-cell edges leaves residual matching rank exactly

\[
 15537;\qquad 825+15537=16362.                                  \tag{2.5}
\]

Thus the native shore matching extends to a global maximum matching.  This
is stronger than a scalar Hall count.  It is still not a claim that the
15,537 exterior edges can all be realized under this same literal controller
word.  More precisely, the 15,537 targets outside $S$ have a perfect
matching to cells outside $T$; this is the exterior matching used below.

## 3. Complete component census

### Theorem 3.1 (twenty-one gap-one components)

The bipartite graph induced by $S\cup T$ has exactly 21 connected
components.  Every component $(S_i,T_i)$ has

\[
 |S_i|=|T_i|+1.                                                 \tag{3.1}
\]

If

\[
 r_i=\bigcap_{x\in S_i}x,                                      \tag{3.2}
\]

then the native traces on $T_i$ are exactly $S_i\setminus\{r_i\}$.
Hence each component has one and only one native-missing target, its Boolean
core $r_i$.

The component-size histogram is

\[
\begin{array}{c|rrrrrrr}
|S_i|/|T_i|&169/168&161/160&160/159&5/4&3/2&2/1&1/0\\ \hline
\#&1&3&1&2&2&6&6.
\end{array}                                                     \tag{3.3}
\]

The five large components are

\[
\begin{array}{c|c|c|c}
r_i&|S_i|/|T_i|&(|x|=4,5,6,7)&\#\text{ core atoms}\\ \hline
1920 &169/168&(1,9,44,115)&9\\
960  &161/160&(1,9,43,108)&9\\
8217 &161/160&(1,9,43,108)&9\\
24610&161/160&(1,9,43,108)&9\\
8218 &160/159&(1,9,43,107)&9.
\end{array}                                                     \tag{3.4}
\]

All ten nontrivial small components are exact Boolean stars: every right
cell has restricted shore $\{r_i,a\}$, where $a$ is its native atom, and
different atoms use different cells.  Their complete target sets and cell
addresses are

\[
\begin{array}{c|c|l|l}
r_i&|S_i|/|T_i|&S_i&\text{cell/start/native/mandatory}\\ \hline
4213&5/4&4213,4221,4469,5237,12405&
13289/414/4221/4181;\ 15610/2735/12405/4177;\\
&&&16994/4119/4469/4145;\ 18292/5417/5237/85\\
7504&5/4&7504,7506,7512,7536,15696&
13391/516/7512/7440;\ 16706/3831/15696/7424;\\
&&&18225/5350/7536/7184;\ 18701/5826/7506/7424\\
1103&3/2&1103,1359,5199&
17314/4439/1359/79;\ 18989/6114/5199/1095\\
18970&3/2&18970,19098,19226&
17206/4331/19226/16920;\ 17280/4405/19098/18968\\
2420&2/1&2420,2932&18663/5788/2932/2416\\
2575&2/1&2575,2607&16684/3809/2607/519\\
2676&2/1&2676,10868&15770/2895/10868/2672\\
9524&2/1&9524,9588&15772/2897/9588/1332\\
17683&2/1&17683,21779&15761/2886/21779/17683\\
19568&2/1&19568,27760&16699/3824/27760/19536.
\end{array}                                                     \tag{3.5}
\]

Every cell in (3.5) has depth two.  The six isolated components are

\[
 {5801},\{13616},\{13620},\{17738},\{21641},\{29776}.    \tag{3.6}
\]

They are exactly the six zero-candidate targets.

#### Proof

The audit reconstructs every cell occurrence with multiplicity and every
target-cell incidence.  Hopcroft--Karp gives (2.2); alternating reachability
gives $S,T$, and undirected breadth-first search in $G[S\cup T]$ gives
the 21 rows above.  For every row it independently checks (3.1), computes
the intersection (3.2), and checks that the injective native traces are
exactly $S_i\setminus\{r_i\}$.  For every small component it records each
cell's depth, start, envelope, mandatory mask, controller values, native
trace, and restricted shore.  The sums of the component sides are

\[
 \sum_i|S_i|=846,qquad \sum_i|T_i|=825,
\]

so no component is omitted.  The complete target lists and target-set
SHA-256 values are stored in the JSON evidence.  □

## 4. Forty-five exact singleton core-shrink ports

### Theorem 4.1 (large-component half-splitters)

Each of the nine atoms in each large component has a unique native depth-zero
occurrence $Q_p=a$.  Replacing this one controller letter by the core
$r\subset a$

\[
 Q_p=a\longmapsto r                                             \tag{4.1}
\]

keeps every central depth-three row equal to its prescribed middle target,
keeps every other one of the 824 native shore pins, and changes the focal pin
from $a$ to $r$.  All letters remain nonzero.  There are exactly 45 such
ports.

The complete `(atom@position[mandatory, number of overlapping selected
pins])` atlas is

```text
core 1920:
  1922@108[1152,2], 1924@6329[1152,4], 1928@4096[1152,3],
  1936@4053[1152,2], 1952@1454[1152,2], 1984@1650[1152,2],
  6016@5863[1152,5], 10112@4932[1152,2], 18304@4919[1152,2]
core 960:
  961@1634[576,2], 962@109[576,3], 964@6328[576,4],
  968@4097[576,4], 992@1453[576,3], 3008@622[576,5],
  5056@5864[576,4], 9152@4933[576,4], 17344@4920[576,3]
core 8217:
  8219@1630[8193,2], 8221@6324[8193,3], 8345@3609[8193,5],
  8473@3189[8193,2], 8729@3024[8193,2], 9241@361[8193,2],
  10265@618[8193,2], 12313@5868[8193,2], 24601@4924[8193,2]
core 24610:
  24611@4749[24576,2], 24614@1642[24576,2],
  24626@4046[24576,5], 24674@1657[24576,2],
  24738@3606[24576,2], 24866@3192[24576,2],
  25122@3027[24576,2], 25634@364[24576,3],
  26658@615[24576,2]
core 8218:
  8222@6323[18,4], 8250@1644[18,2], 8282@1659[18,5],
  8346@3608[18,4], 8474@3190[18,3], 8730@3025[18,3],
  9242@362[18,3], 10266@617[18,3], 12314@5869[18,4]
```

The focal atom's native occurrence is unique among all 19,311 cells in every
one of the 45 cases.  Therefore (4.1) alone is a Robin--Hood exchange, not a
rank gain: it serves $r$ but loses $a$.  A neutral router must first create
or preserve a second legal occurrence of $a$, or an equivalent independent
cell, before the core shrink becomes a splitter.

#### Proof

For each listed port the audit checks `mandatory subset core` and direct
incidence of the depth-zero cell with the core.  It then materializes (4.1),
checks all 6,435 central unions, all 825 selected native-pin unions, and
nonemptiness of all 6,438 controller letters.  Every overlapping nonfocal pin
listed in the JSON has unchanged union.  Finally it scans the native trace of
all 19,311 cells and finds the focal atom only at the displayed occurrence.
□

The smallest collar certificate is, for example,

\[
 (r,a,p)=(1920,1922,108).                                      \tag{4.2}
\]

Only the focal pin and the overlapping depth-one pin at cell 6546 meet this
position, and the latter remains target 1986.  Thus an exact neutral creation
of a second native 1922 occurrence would immediately activate (4.2), subject
to the exterior condition in Section 6.

## 5. Six exact depth-two core-rebase ports

The six $2/1$ circuits have an even sharper common-controller half-splitter.
For each pair $r<a=r\cup\{z\}$, delete $z$ from all three controller
letters of its sole depth-two cell.  The exact atlas is

\[
\begin{array}{c|c|c|c|c|c}
r&a&\text{cell/start}&z&\text{old triple}&\text{new triple}\\ \hline
2420&2932&18663/5788&10&(868,2884,2836)&(356,2372,2324)\\
2575&2607&16684/3809&6&(2601,2602,2604)&(2569,2570,2572)\\
2676&10868&15770/2895&14&(10788,8804,8308)&(2596,612,116)\\
9524&9588&15772/2897&7&(8308,9300,9552)&(8244,9236,9488)\\
17683&21779&15761/2886&13&(5394,21762,20739)&(1298,17666,16643)\\
19568&27760&16699/3824&14&(10352,11360,25696)&(2160,3168,17504).
\end{array}                                                     \tag{5.1}
\]

Coordinates in (5.1) are one-based.  In every row:

1. the old triple union is $a$ and the new triple union is $r$;
2. every central depth-three middle row is unchanged;
3. every other one of the 824 native pins is unchanged;
4. all controller letters remain nonzero; and
5. the old native occurrence of $a$ is unique among all physical cells.

In fact, before the rebase the displayed depth-two cell is the only legal
candidate cell in the entire compiler graph for either $r$ or $a$.  Every
one of its three old controller letters contains the extra coordinate $z$;
therefore no adjacent pair inside the old triple has trace $r$.  The local
two-row incidence column is exactly $(1,1)^T$.

For the two overlapping rows at starts 2895 and 2897, one rebase meets the
other selected depth-two interval, but its union remains respectively 9588
or 10868.  The other four rebases meet no selected pin except the focal one.

In particular, the previously studied `2575/2607` port survives the new
neutral router **exactly**, but at the new address

\[
 c=16684, s=3809,                                               \tag{5.2}
\]

not at its old H22 address.  Its mandatory mask remains 519.  Replacing
$(2601,2602,2604)$ by $(2569,2570,2572)$ is a literal central-safe and
common-pin-safe rebase from 2607 to 2575.  It still does not improve Hall by
itself because it displaces the unique 2607 pin.

Thus the sharp zero-six-preserving local target is:

> route a second legal 2607 occurrence while keeping cell 16684 and the
> other 824 critical-shore pins; then apply the rebase (5.2).

The five other rows of (5.1) are equally valid alternative targets.  The
special preference for `2575/2607` is provenance and its already-developed
graded-circuit theory, not an asserted uniqueness theorem.

#### Proof of the six rebases

For each row, the audit intersects the three displayed controller letters
with the core and materializes the resulting 6,438-letter controller.  It
checks nonemptiness, all 6,435 central depth-three unions, and all 825 native
pin intervals.  The focal interval changes from atom to core; every other
selected interval is unchanged.  A scan of all cells verifies the stated
native-occurrence uniqueness.  The `2/1` component census verifies that the
displayed cell is the full candidate neighbourhood of both focal targets. □

## 6. Exact Hall-21 to Hall-at-most-20 splitter theorem

### Theorem 6.1 (forced-pair contraction at H21)

Let $G'$ be the compiler graph of a legal endpoint carrier.  Fix one of the
six pairs $C=\{r,a\}$ in (5.1), and let $c_r,c_a$ be distinct physical
cells with legal incidences

\[
 r-c_r,\qquad a-c_a.                                           \tag{6.1}
\]

Let $H=G'-C-\{c_r,c_a\}$.  Then the maximum size of a matching in $G'$
constrained to use both edges (6.1) is exactly

\[
 2+\nu(H).                                                      \tag{6.2}
\]

Consequently the pair is an H21-to-Hall-at-most-20 splitter if and only if

\[
 \nu(H)\ge16361.                                               \tag{6.3}
\]

If the endpoint also has a target shore of gap 20, its Hall deficiency is
exactly 20.  Without that upper certificate, (6.3) proves the stronger-safe
statement `deficiency at most 20`, not equality.

#### Proof

Deleting the two forced edges from a constrained matching leaves a matching
of $H$.  Conversely, any matching of $H$ can be adjoined to the two
disjoint edges in (6.1).  Thus (6.2) is exact.  Since
$16383-20=16363$, (6.3) is equivalent to a constrained matching of size at
least 16,363.  □

For the current H21 state, reserve the 824 nonfocal native pins and the
15,537-edge exterior matching from (2.5).  These already contribute

\[
 824+15537=16361.                                               \tag{6.4}
\]

Therefore a router/splitter which transports those cell occurrences
injectively and adds the two focal edges automatically satisfies (6.3).
Equivalently, if occurrence transport is not explicit, one exact residual
max-flow check of (6.3) is necessary and sufficient.

### Theorem 6.2 (neutral router plus literal rebase)

Start from the fixed H21 carrier.  Suppose a finite legal braid composition
has the following properties for one row $(r,a,c)$ of (5.1):

1. it preserves the complete middle deck, Johnson endpoints, depth-three
   residence, every upper support layer, the four immediate-lower holes, and
   the six degree-zero targets;
2. it retains or transports 824 pairwise target-distinct nonfocal native
   pins and an exterior matching of size 15,537, with all targets and all
   physical cells disjoint between the two families;
3. under one nonzero controller word $Q'$, it retains a legal occurrence
   $c_a$ whose interval union is $a$, and it retains a distinct occurrence
   $c_r$ on which the corresponding literal rebase in (5.1) has interval
   union $r$; both focal targets and cells are disjoint from the two
   families in item 2;
4. the same $Q'$ reconstructs every central middle row and realizes all
   826 critical-shore pins: the 824 nonfocal pins together with
   $r-c_r,a-c_a$.

Then the endpoint has compiler matching rank at least 16,363 and Hall
deficiency at most 20.  Its H21 critical shore has a literal common-$Q'$
injection of size 826.

#### Proof

Items 2--3 give $15537+824+2=16363$ disjoint target-cell edges.  Item 4
makes the whole critical-shore part literal under one controller rather than
a collection of unrelated targetwise witnesses.  The count proves the Hall
claim; the 826 distinct critical pins prove the common-controller claim. □

The same theorem applies to any singleton port in Section 4: a neutral
router must supply a second occurrence of its unique atom, after which the
one-letter shrink supplies the missing core.

## 7. Exact remaining boundary

The component coloring and the local common-$Q$ half-splitters are no longer
missing.  The exact obstruction is occurrence duplication under protected
chronology:

* every one of the 45 singleton-port atoms has exactly one native occurrence;
* every one of the six (2/1)-circuit atoms has exactly one native
  occurrence;
* applying any audited rebase without first creating a companion atom merely
  exchanges which target is unresolved;
* Hall improvement additionally requires the residual rank condition
  (6.3), or an explicit transport of the 15,537 exterior and 824 nonfocal
  edges; and
* a critical-shore common controller does not by itself prove a single
  literal word for all 16,383 lower targets.

Thus the next H100 search or proof should target the exact decorated event

\[
 \text{second atom occurrence}
 +\text{ retained rebase port}
 +\text{ residual rank }16361
 +\text{ one common controller},                               \tag{7.1}
\]

not merely a scalar Hall-20 neighbour.  For the most developed target this
event is the creation of a second 2607 occurrence compatible with the fixed
`16684/start 3809` rebase frame.
