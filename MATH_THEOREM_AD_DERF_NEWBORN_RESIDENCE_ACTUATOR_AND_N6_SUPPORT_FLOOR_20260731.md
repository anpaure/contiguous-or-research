# DERF newborn residence: an exact finite-collar actuator and the `n=6` support floor

Date: 2026-07-31  
Status: exact fixed-structural-parent actuator theorem; exact authenticated
`n=6 -> 7` body and unit-packet audit; exact interval-transversal lower
bound.  No all-parameter actuator supply theorem is claimed.

## 0. Result and scope

The synchronized DERF exchange language and the minimum-three residence
language fit exactly, but they do not imply a bounded residence repair.

Fix a structural Catalan forest `F`, its path-orientation vector `epsilon`,
an independent filler `G`, a common puncture bank `Q`, the two direct SDRs
`M^-`,`M^+`, and a physical forest `H`.  A proposed packet has a complete
old/new physical support `(A,B)`, including changed root edges when a rooted
certificate is required.  Then it is a legal pure residence actuator if and
only if:

1. the two SDR symmetric differences are alternating cycles and alternating
   paths with the same exposed-bank change `Q -> Q'`;
2. every literal role, seam-anchor and degree cap holds;
3. the complete rooted transfer minor is nonsingular; and
4. the finitely many three-edge collars meeting `A union B` create no new
   `0110` motif and `A` hits the requested old motif.

For fixed `F,epsilon`, SBE is preserved **identically**: its occurrence
graphs and endpoint Boolean cuts do not depend on `Q` or either SDR.  If
path orientations also change, SBE preservation has the exact cut-slack
update in Theorem 2.2 below.  If the changed physical output is to become
the next structural parent, its SBE state is a separate exact row given by
Theorem 2.3; it is not inherited merely from fixed-parent invariance.

This theorem is positive but conditional on a packet.  The authenticated
`n=6 -> 7` fixture shows why no small universal local supply should be
asserted.  Its body motifs are

\[
\begin{array}{c|rrrr}
\text{sector}&0&c&cz&z\\ \hline
\text{bad body windows}&28&144&37&19,
\end{array}                                                    \tag{0.1}
\]

and their exact minimum edge-transversal orders are

\[
\begin{array}{c|rrrr}
\text{sector}&0&c&cz&z\\ \hline
\tau&26&116&32&18.
\end{array}                                                    \tag{0.2}
\]

After supplying a clean independent `c+G` filler, any one structural packet
which clears all remaining `0,z,cz` body motifs must delete at least

\[
               \tau_0+\tau_{cz}+3\tau_z
                 =26+32+54=112                              \tag{0.3}
\]

old physical edges.  This floor precedes every new-window, degree, rooted,
or next-state SBE test.  Thus no single fixed-`F` structural packet with
fewer than `112` old physical deletions can clear all old `0,z,cz` body
motifs in this fixture.  Feasibility at or above `112` is not asserted.

There is also a sharp finite warning.  Among all support-minimal direct unit
packets on the stored `n=6` state, no unit is a pure eliminator of a `0`,
`z`, or `cz` body motif.  Nor is any pair or triple formed from the `31`
individually linear-forest-safe units using distinct `Q` rows and `5r`
distinct old/new supports.  Some packets improve the **total** residence
count, so this is an exact obstruction only for the stated base-unit
catalogue, not for every order-three augmenting packet.

Two scopes must not be conflated.

* The independent-filler theorem makes `c+G` a direct summand.  Therefore a
  structural packet cannot alter the 144 `c`-body motifs.  Under the
  supplied hypothesis that a clean parameter-six filler is available,
  replacing `G` erases them without changing the structural palettes or
  topology.  The currently frozen finite clean-filler replay itself stops
  at parameter five; hence clean `G_6` is an input to, not a conclusion of,
  the present `n=6` audit.
* The stored `n=6 -> 7` row is an exact unrooted palette/degree-two/acyclic
  fixture, but it is **not** on the anchor-rooted/no-empty side face.  Its
  side anchor histograms have `c_0^-=12` and `c_0^+=16`.  The rooted theorem
  below applies to a state already carrying the stated rooted base.  The
  finite audit uses either unrooted graphic legality or an explicitly
  weaker arbitrary-endpoint root bank; it does not manufacture the missing
  DERF anchor-rooted state.

## 1. Exact residence and packet notation

Orient a physical path and write its Johnson edges as

\[
                v_{i+1}=v_i-a_i+b_i.                         \tag{1.1}
\]

For a four-vertex window `W=(v_0,v_1,v_2,v_3)`, put

\[
  \mu(W)=(v_1\cap v_2)\setminus(v_0\cup v_3).                 \tag{1.2}
\]

Intersection-palette injectivity makes a positive singleton run impossible
and makes `mu(W)` either empty or a singleton.  The window has a forbidden
positive run of length two exactly when

\[
                    b_0=a_2,                                  \tag{1.3}
\]

equivalently its coordinate trace is `0110`.

Let `H` be the selected physical forest.  A packet removes the nonroot
physical edge set `A_H` and adds `B_H`; if root edges change, write the full
rooted exchange as

\[
                       T'=T-A+B,                               \tag{1.4}
\]

where `T` is the current root-augmented graphic base and `A,B` include all
changed root edges.  Cancel common edges, so `|A|=|B|=t`.

Delete `A_H` from `H`.  Its maximal path pieces are the **retained
fragments**.  Every old bad window wholly contained in one retained fragment
survives, possibly reversed.  Every destroyed bad window meets `A_H`, and
every new bad window meets `B_H`.

## 2. The exact actuator theorem

### Theorem 2.1 (fixed-`F` rooted finite-collar actuator)

Let

\[
             (F,G,\epsilon,Q,M^-,M^+,T)                         \tag{2.1}
\]

be a DERF state whose declared root augmentation `T` is a graphic base.
Let `Q',N^-,N^+` be a proposed structural terminal state on the same
`F,G,epsilon`.  After cancelling common selected and root edges, let its
complete exchange be `T'=T-A+B`.

For `a in A`, `b in B`, define

\[
 K_{a,b}=1
   \quad\Longleftrightarrow\quad
 a\text{ lies on the unique }T\text{-path between the ends of }b. \tag{2.2}
\]

Let `D` be a specified family of old bad residence windows.  The terminal
state preserves both direct palettes, all declared capacities, the rooted
graphic base, and the parent SBE state, and satisfies

\[
                       \operatorname{Bad}(H')
                \subseteq \operatorname{Bad}(H)\setminus D      \tag{2.3}
\]

if and only if all of the following hold.

1. On each shore, `M^sigma triangle N^sigma` is a disjoint union of
   alternating cycles and alternating paths whose endpoints are exactly

   \[
      \partial_\sigma(Q\setminus Q')\ \sqcup\
      \partial_\sigma(Q'\setminus Q),                           \tag{2.4}
   \]

   with the same `Q,Q'` on both shores.
2. Every terminal occurrence role, physical degree, seam-anchor, and other
   declared literal capacity row holds.
3. `K` is nonsingular over `F_2`.
4. Every window in `D` meets `A_H`; every terminal bad window wholly inside
   a retained fragment is an old bad window outside `D`; and every new
   three-edge window meeting `B_H` is good.

For a packet changing `p=|A_H|=|B_H|` nonroot physical edges, item 4 is
decided by at most `3p` old and `3p` new edge-window incidences.

#### Proof

The alternating path/cycle condition is necessary and sufficient for the
two direct palette equations with exposed banks `partial_sigma Q'`.
Item 2 is literal.  In the graphic representation based at `T`, the column
of a new edge `b` is its fundamental-cycle incidence vector.  Replacing the
basis columns `A` by `B` gives a basis exactly when the square minor `K` is
nonsingular.

The residence assertion follows from (1.3).  A retained fragment has the
same ordered vertices and edges, up to reversal, and `0110` is palindromic.
Thus its old bad windows survive.  Every other changed three-edge window
meets a deleted or added edge, and a fixed changed edge has only three
possible positions in such a window.  Item 4 is therefore necessary and
sufficient for (2.3).

Finally, fixed `F,epsilon` fixes both SBE occurrence graphs, both endpoint
banks and every Boolean cut coefficient.  Neither `Q` nor a representative
choice appears in an SBE cut, so its truth value is identical before and
after the packet.  This proves the theorem. `square`

### Theorem 2.2 (exact orientation-flip update)

For shore `sigma` and outer-family cut `U`, let `s_sigma(U)` be the old
**Boolean endpoint-count slack** after the orientation-independent
contribution and the rounded right-hand side have been removed.  Thus its
units are selected endpoints, not the scaled Hall units of (2.8).  If path
orientations in `J` are flipped, and
`z_i^sigma(epsilon_i)` is the old weight-one terminal of path `i`, then the
new orientation is SBE-feasible exactly when, for every `sigma,U`,

\[
 s_\sigma(U)+\sum_{i\in J}
 \left(
  {\bf1}\{z_i^\sigma(1-\epsilon_i)\in N_\sigma(U)\}
  -{\bf1}\{z_i^\sigma(\epsilon_i)\in N_\sigma(U)\}
 \right)\ge0.                                                \tag{2.5}
\]

In particular `min_{sigma,U}s_sigma(U)>=|J|` is sufficient.

#### Proof

Orientation changes only the selected weight-one terminal of each flipped
path.  Subtracting the old endpoint contribution and adding the new one
gives (2.5); the right side of every SBE inequality and all nonterminal
incidences are unchanged.  Each summand is at least `-1`, proving the
sufficient bound. `square`

This theorem concerns the SBE state of the fixed parent `F`.  The physical
output forest is the next structural parent.  If a packet changes it, its
own next-state occurrence graphs and orientation cuts must be recomputed.
Moreover, if the input path orientations themselves change, (2.5) certifies
only the SBE rows: the exposed banks `partial_sigma Q` and both SDR palette
path systems must be regenerated separately.

### Theorem 2.3 (exact next-parent SBE guard)

Let a parameter-`m` output forest `H` have shore occurrence graph
`G_sigma(H)`.  Put

\[
 N=\binom{2m}{m-1},\qquad C=\operatorname{Cat}_{m+1},\qquad R=N-C. \tag{2.6}
\]

For an outer-family cut `U`, write

\[
 D=N_{G_\sigma(H)}(U),                                      \tag{2.7}
\]

and let `Z_sigma(epsilon)` contain every isolate and the weight-one terminal
selected by `epsilon` on every nontrivial path.  Its scaled SBE slack is

\[
 S_\sigma(U)=R|D|+(N-R)|D\cap Z_\sigma|-N|U|.               \tag{2.8}
\]

For a changed output `H',epsilon'`, put `D'=N_{G_sigma(H')}(U)` and define
`Z'_sigma` analogously.  The output remains SBE-feasible exactly when

\[
 S_\sigma(U)+R(|D'|-|D|)
 +(N-R)(|D'\cap Z'_\sigma|-|D\cap Z_\sigma|)\ge0            \tag{2.9}
\]

for every shore and every `U`.

A sufficient local guard is: preserve the isolate set and the unordered
path-endpoint pairs, retain every old occurrence adjacency on both shores
(parallel surviving providers count), and choose the same weight-one
terminals.  Then
`D subseteq D'` and `D cap Z subseteq D' cap Z`, so every slack weakly
increases.

#### Proof

Equation (2.8) is the scaled weighted Hall form of SBE: neighbours outside
`Z` have weight `R/N`, while neighbours in `Z` have weight one.  Subtracting
the old expression from the new one gives (2.9).  Under the sufficient
guard every old neighbour and every old selected terminal neighbour
survives, proving monotonicity. `square`

For the input parent `F_6`, the coefficients are `R=363` and `N-R=429`.
For the changed produced parent `F_7` in the authenticated `n=6 -> 7`
step, the relevant next-state coefficients are instead
`R=1573` and `N-R=1430`.  Unlike parent-SBE invariance, (2.9) can be a global min-cut separation;
last-provider protection is sufficient but not necessary.

### Corollary 2.4 (disjoint packet packing)

Suppose packets `P_1,...,P_r` have pairwise vertex-disjoint occurrence
alternating supports, disjoint literal changed physical/capacity supports,
pairwise disjoint `Q` deletions and insertions, and radius-two collar
separation: every source and combined-terminal three-edge window meets the
changed support of at most one packet.  Suppose also that their full rooted
transfer matrix is block diagonal with nonsingular diagonal blocks.  If
each packet passes Theorem 2.1 and their target sets are disjoint, their
union is a simultaneous residence actuator.  Its transfer determinant is
the product of the diagonal determinants, and radius-two separation excludes
every new cross-packet bad window.

The block-diagonal hypothesis can be weakened to nonsingularity of the
complete transfer matrix.  The displayed form is the smallest directly
composable local certificate.

## 3. Exact pinning and transversal floors

### Lemma 3.1 (sector pinning)

In a fixed strict DERF output:

1. a bad `0`-body window can be destroyed only by deleting one of its three
   selected upper-representative edges;
2. a bad `cz`-body window can be destroyed only by deleting one of its
   three selected lower-representative edges;
3. a bad `z`-body window can be destroyed only by deleting one of its three
   retained central edges, equivalently by putting at least one of their
   child labels into the terminal `Q'`; and
4. a bad `c`-body window is immutable under every fixed-`G` structural
   packet.

#### Proof

Each body window lies wholly in the named direct summand and its three
physical edges have the stated type.  By retained-fragment invariance, a
packet which deletes none of them preserves the window.  A central edge
`d_q` occurs precisely for `q notin Q`, so it is deleted precisely when
`q` enters `Q'`.  The `c+G` summand is disjoint from all structural packet
edges. `square`

For a sector `s`, let `I_s` be the collection of three-edge intervals of
its bad body windows along the output paths and let `tau_s` be their minimum
edge-transversal order.

### Theorem 3.2 (general structural support floor)

Any fixed-`F` packet eliminating every `0,z,cz` body motif has

\[
             |A_H|\ge \tau_0+\tau_{cz}+3\tau_z.                 \tag{3.1}
\]

If it is a sequence of support-minimal unit `Q` packets, at least

\[
                       \max(\tau_0,\tau_{cz},\tau_z)             \tag{3.2}
\]

unit steps are necessary.

#### Proof

Lemma 3.1 forces at least `tau_0` deleted upper representatives and
`tau_cz` deleted lower representatives.  Let

\[
             s=|Q\setminus Q'|=|Q'\setminus Q|.
\]

Hitting all `z` intervals requires at least `tau_z` distinct old central
edges to disappear, so `s>=tau_z`.  For every label leaving `Q`, the old
support contains two seam edges; for every label entering `Q`, it contains
one central edge.  These are `3s` distinct old structural edges.  The three
sector edge types are disjoint, giving (3.1).

A support-minimal unit packet has at most one physically effective old
deletion in each of the `0`, `cz`, and `z` body banks; in the literal
distinct-support `5 -> 5` subfamily it has exactly one in each.  It can
therefore contribute at most one selected cut position to each interval
transversal, which proves (3.2). `square`

### Corollary 3.3 (authenticated `n=6` floor)

For the frozen `n=6 -> 7` state,

\[
        (\tau_0,\tau_c,\tau_{cz},\tau_z)=(26,116,32,18).         \tag{3.3}
\]

Hence (3.1) is the old-support floor `112`, and any cleanup by unit packets
uses at least `32` unit steps.  These are lower bounds only: a cut edge may
remove several motifs, but added seams may create new motifs and the degree
or rooted transfer tests may fail.

#### Proof

On one path, the bad windows are ordinary intervals `[i,i+2]` in its edge
order.  Greedily selecting the smallest right endpoint is an optimal
interval transversal.  The output paths are disjoint, so the pathwise
optima add.  Literal replay gives (3.3); substituting in Theorem 3.2 gives
the claims. `square`

## 4. The authenticated `n=6` fixture

The source is

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
```

with SHA-256

```text
220994673d2b6f091c8c3493c4ef82023770211ca38df2548eace392a8efa26d
```

The independently frozen literal replay has SHA-256

```text
69e95c7635d2d99d75af17994394212037b3bb2a95591fcd8a4567ba97d2e173
```

and verifies `|Q|=429`, `495` representatives per shore, `429` output
paths, exact palettes, maximum degree two and cycle rank zero.

There are `512` bad windows in total: the `228` body windows in (0.1) and
`284` windows meeting one or two sector transitions.  Thus a body-only
objective is not a complete residence objective.

One literal representative of each body type is:

\[
\begin{array}{c|c|c}
\text{sector}&\text{coordinate}&(v_0,v_1,v_2,v_3)\\ \hline
0&6&(397,2d7,2f6,ab6)_{16}\\
cz&10&(3287,3487,3495,3295)_{16}\\
z&0&(232e,2327,2b25,2f24)_{16}\\
c&10&(1aaa,1ea2,1e86,1b86)_{16}.
\end{array}                                                    \tag{4.1}
\]

The displayed `z` window consists of child edges `789,790,791`, all outside
`Q`; therefore a fixed-`Q` representative circuit cannot alter it.

The current parent `n=6` orientation and the produced `n=7` forest both
pass the independently audited two-shore SBE inequalities with zero maximum
violation.  This authenticates the starting SBE state.  Theorem 2.1 explains
why a fixed-parent `Q`/SDR packet cannot damage the parent certificate; it
does not preserve the output's next-state certificate automatically.

This statement is imported from

```text
scratch/catalan_strict_balanced_expansion_n3_n7_20260731.audit.json
```

with SHA-256

```text
5b11055a39e6dc33e1a53fbb553bb7f8e32c1795b2c29a51a5a0076eddaf7cd2
```

and canonical payload

```text
9acf4f4b11ed5f87d0ca3ffb653cc8d2294e225b705df94e6250b8a4291b7ba0
```

The exact side anchor histograms are

\[
 (c_0,c_1,c_2)^-=(12,141,144),\qquad
 (c_0,c_1,c_2)^+=(16,133,148).                              \tag{4.2}
\]

Consequently this particular fixture supplies no anchor-rooted/no-empty
base to preserve.  Any theorem using that stronger state must first choose
another representative system or jointly eliminate all `28` anchor-free
components.

## 5. Palette reachability and the complete direct-unit audit

### 5.1 Every structural `0/cz/z` body motif at `n=6` has a short palette route

For one fixed-Q shore matching, orient the matching exchange digraph as
follows.  If outer row `o` is currently matched to `m(o)` and the direct
catalogue also contains `(o,x)`, insert the arc

\[
                             x\longrightarrow m(o).              \tag{5.1}
\]

### Lemma 5.1 (exact palette exchange digraph)

An old selected representative `(o,m(o))` can be removed by a fixed-Q
palette circuit if and only if an arc `x -> m(o)` belonging to an
alternative for row `o` lies on a directed cycle.  More generally, changing
`Q` by `Q-a+f` on shore `sigma` is possible if and only if the exchange
digraph contains a directed path

\[
                  \partial_\sigma a\longrightarrow
                  \partial_\sigma f.                            \tag{5.2}
\]

A synchronized unit change requires such paths on both shores for the same
`a,f`.  Compound changes require vertex-disjoint path systems with the same
two endpoint banks, together with any optional vertex-disjoint alternating
cycles.

#### Proof

Selecting the alternative `(o,x)` and deleting `(o,m(o))` matches `x` and
exposes `m(o)`, so exposure moves along the arc `x -> m(o)`.  A closed
exposure walk is exactly an alternating matching cycle.  An open walk
starting at the old exposed vertex `partial_sigma a` and ending at the new
exposed vertex `partial_sigma f` is exactly an alternating augmenting path.
Disjoint path systems are the usual symmetric-difference decomposition of
two matchings. `square`

A directed cycle's order is the number of old (and new) representatives.
Exact replay on the authenticated `n=6` state gives:

\[
\begin{array}{c|c|c}
\text{body sector}&\text{maximum shortest cycle order}&
 \text{shortest-order profile}\\ \hline
0&9&2^6,3^6,4^2,5^3,6^6,7^3,8^1,9^1\\
cz&8&2^3,3^7,4^3,5^7,6^7,7^8,8^2.
\end{array}                                                    \tag{5.3}
\]

Thus every `0` or `cz` body motif has a palette-preserving fixed-Q circuit
through at least one of its three representatives.

For a `z` motif, fixed-Q circuits are impossible by Lemma 3.1.  Searching
the two synchronized exchange digraphs for one `Q` label leaving and one of
the motif's three central labels entering gives the exact occurrence
half-support profile

\[
                         5^9,\quad6^6,\quad7^4.                  \tag{5.4}
\]

Here half-support means the three old structural central/seam occurrences
plus the numbers of old upper and lower augmenting-path occurrences; root
auxiliaries and literal physical duplicate cancellation are excluded.
Consequently every `z` body motif has a palette route of half-support at
most seven, but ten of nineteen have no direct `5 -> 5` route.

This closes the **palette-only** local existence question on the frozen
fixture.  It does not certify physical degree, the rooted transfer minor,
absence of new residence motifs, or next-output SBE.  Those are exactly the
additional rows of Theorems 2.1 and 2.3.

### 5.2 Support-minimal direct packets

The new lightweight audit reconstructs every support-minimal synchronized
one-`Q` exchange with length-two representative redirections on both shores.
It finds

\[
\begin{array}{c|r}
\text{stage}&\text{count}\\ \hline
\text{direct redirection pairs}&67\\
\text{literal }5\to5\text{ supports}&67\\
\text{degree safe}&32\\
\text{graphic safe}&63\\
\text{simultaneously linear-forest safe}&31\\
\text{anchor-histogram preserving}&27\\
\text{total-motif improving}&10\\
\text{pure eliminators}&1.
\end{array}                                                    \tag{5.5}
\]

### Corollary 5.2 (authenticated targeted unit descents)

With one root edge attached to the stored first endpoint of each ambient
path, the following literal `5 -> 5` packets preserve both direct palettes,
maximum degree two, acyclicity, that complete fixed ambient-root basis, the
two side anchor histograms, and the fixed-parent SBE state:

\[
\begin{array}{c|c|c|r}
Q\text{ swap}&\text{old motifs eliminated}&\text{new motifs created}&
 \Delta|\operatorname{Bad}|\\ \hline
4\to597&cz^2+\mathrm{cross}&cz+\mathrm{cross}&-1\\
303\to727&z+cz+\mathrm{cross}&\mathrm{cross}^2&-1\\
600\to608&0+\mathrm{cross}&\mathrm{cross}&-1.
\end{array}                                                    \tag{5.6}
\]

Thus there is an actual bounded net residence descent targeting each of the
three structural body sectors on this fixture.  None is a pure global
actuator: the deleted body debt is partly transported to a seam collar.
Moreover the root statement is the explicitly chosen arbitrary-endpoint
graphic base, not the absent anchor-rooted/no-empty DERF side state, and
next-output SBE still requires Theorem 2.3.

#### Proof

The audit constructs the ten old/new physical edges from the two direct
length-two matching paths and the three changed central/seam edges.  It
replays the complete palettes and graph, verifies exactly one retained root
endpoint in every terminal component, recomputes the anchor histograms, and
scans every four-vertex window.  The displayed signed motif ledgers are the
literal differences.  Fixed-parent SBE follows from Theorem 2.1. `square`

The best scalar change is `-2`.  The only pure unit eliminator removes a
sector-crossing motif; it removes no `0,z,cz` body motif.  Across all `31`
linear-forest-safe units, the numbers of body motifs whose old three-edge
support is even cut are only

\[
                         (4,5,4)\quad\text{on }(0,cz,z).         \tag{5.7}
\]

With the explicitly chosen, weaker arbitrary-terminal ambient root bank,
only `7` units preserve every fixed root, and the corresponding cut-coverage
counts are `(1,3,1)`.

Starting from the `31` individually linear-forest-safe units, the audit also
composes every pair and triple that is mutually `Q`-disjoint and
support-disjoint, and replays the complete physical edge set instead of
assuming composability:

\[
\begin{array}{c|r|r|r|r|r}
\text{order}&\text{literal forests}&\text{best delta}&
 \text{pure}&\text{pure body}&\text{fixed ambient-root safe}\\ \hline
2&461&-3&2&0&21\\
3&4379&-4&1&0&35.
\end{array}                                                    \tag{5.8}
\]

Thus order at most three in this exact **individually-safe base-unit
catalogue** cannot give a pure newborn-body actuator.  This is not an
impossibility for a combination containing an individually unsafe unit
whose defect cancels only jointly, longer SDR augmenting paths, a packet not
decomposable into base-state units, another `F`, or another orientation.

## 6. The proved boundary

The exact positive theorem is Theorem 2.1: once a synchronized packet is
specified, palette preservation, SBE preservation, rooted legality and
residence correction reduce to alternating paths, one transfer minor, and
a bounded collar replay.

What is false is the stronger inference that the required **physical**
packet has
bounded support merely because the two palette systems and graphic base are
matroids.  Abstract occurrence ladders force arbitrarily long alternating
paths.  The authenticated Boolean fixture has short palette routes for each
individual motif, but adds a concrete joint obstruction:
complete structural body repair already has old-support floor `112`, and
the full order-three catalogue generated by the individually safe direct
units has no pure body actuator.

The next exact constructive target is therefore one of:

1. a compound augmenting packet which deliberately transports seam debt and
   later cancels it;
2. a regenerated structural parent `F'` with a labelled palette/root
   correspondence and a new SBE orientation solution; or
3. a right-total clean filler plus a nonlocal structural residence packing
   meeting the `112`-edge floor.

No deep-shadow, compiler, or `nu=B` conclusion follows here.

## 7. Audit artifacts

The new audit is

```text
scratch/audit_ad_derf_n6_newborn_residence_packets_20260731.py
scratch/ad_derf_n6_newborn_residence_packets_20260731.audit.json
```

It fail-closes on the authenticated `n=6` witness and the previously
audited five-edge replay core, reconstructs all four sector motif sets,
proves the interval-transversal counts by pathwise greedy replay, exhausts
the direct unit catalogue, and literally replays all pair/triple terminal
forests and palettes.  Its packet-enumeration scope is exactly Section 5.2;
its motif and interval outputs also authenticate Sections 0, 3, and 4.

The independent palette-only exchange-digraph audit is

```text
scratch/audit_ad_derf_n6_residence_exchange_digraph_20260731.py
scratch/ad_derf_n6_residence_exchange_digraph_census_20260731.audit.json
```

It implements Lemma 5.1, proves the finite profiles (5.3)--(5.4), and
independently reproduces (0.1)--(0.3), while explicitly excluding every
physical/rooted/new-window/output-SBE claim.
