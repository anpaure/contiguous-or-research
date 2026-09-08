# The alternating hex is a literal `K17` q2 zipper, but residence is a conserved transfer

Date: 2026-07-31  
Lane: AD  
Status: dimension-uniform local theorem; independently replayed positive
`K17` packet; exact fixed-parent obstruction; no `K17` word is claimed

## 0. Exact verdict

The authenticated carrier

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

already contains every rank-nine owner and every rank-eight Johnson colour
exactly once.  The correct local actuator is therefore an alternating
incidence circuit, not a replacement chosen independently in the owner
cycle.

This note proves four facts.

1. Every rank-eleven interval union on a rank-nine Johnson path has a
   three-owner witness.  Thus both lower and upper `q2` ledgers are genuinely
   local width-three ledgers.
2. The smallest closed owner/q1-preserving actuator is an alternating
   hexagon.  Its lower-q2 delta has three terms, its upper-q2 delta has at
   most six terms, and its residence delta is exactly a finite weighted
   strand-gluing calculation.
3. One literal hex on the frozen carrier preserves all `24310` owners and
   all `24310` lower-q1 colours, removes two length-two runs and one
   length-three run with no new short run, and adds without loss:

   
   - two lower-q2 targets;
   - two upper-q1 targets; and
   - two upper-q2 targets.

   This is a concrete `K17` analogue of a facet zipper.
4. It cannot finish the present parent-induced branch by port flow or
   occurrence choice.  Every exact owner/q1 carrier has exactly
   `Cat_8=1430` positive runs per coordinate, so residence packets transfer
   run mass rather than delete run components.  More sharply, the fixed K15
   parent has `165` uniquely coloured minimum-run packets which survive
   every rank-six occurrence transversal and every macro port completion;
   the exact correlated optimum is stronger, namely `180` surviving
   internal short runs.  A flat child therefore needs a genuinely
   rethreaded parent chronology which hits the residual packets, or a
   nonflat compiler.  The same occurrence variables carry an exact marginal
   upper-provider deletion debt `505`; this reward row and the residence
   hyperclauses must be chosen jointly before the port flow.

The proved positive object is local and integral.  Compatible global packet
packing, higher shadows, endpoints, and the common lower compiler remain
open.

## 1. Incidence-cycle model

Let `|Omega|=2r-1`.  Write `I_r(Omega)` for the bipartite inclusion graph
between rank-`r` owners and rank-`r-1` colours.  A Hamilton cycle in this
graph has the form

\[
 V_0,C_0,V_1,C_1,\ldots,V_{N-1},C_{N-1},V_0,       \tag{1.1}
\]

where

\[
 C_i=V_i\cap V_{i+1}.                              \tag{1.2}
\]

Contracting the colour vertices gives a Johnson owner cycle.  Conversely,
a Johnson owner cycle whose intersections enumerate every rank-`r-1`
colour once lifts uniquely to (1.1).

For `K17`, `r=9` and

\[
 N=\binom{17}{9}=\binom{17}{8}=24310.              \tag{1.3}
\]

The frozen cycle is exactly such a Hamilton cycle.

Define the centered q2 labels

\[
 L_2(i)=V_{i-1}\cap V_i\cap V_{i+1},\qquad
 U_2(i)=V_{i-1}\cup V_i\cup V_{i+1}.              \tag{1.4}
\]

Only labels of ranks `r-2` and `r+2`, respectively, belong to the q2 decks.

## 2. Upper-q2 shortening is exact

### Theorem 2.1 (three-owner shortening)

Let `X_0,...,X_s` be a Johnson path of distinct rank-`r` sets.  If

\[
                         \bigcup_{i=0}^s X_i=H,qquad |H|=r+2,       \tag{2.1}
\]

then some three consecutive owners have union `H`.

#### Proof

Choose a shortest consecutive subinterval with union `H`, and relabel it
`X_0,...,X_t`.  Minimality at the left end gives a coordinate `a` occurring
only in `X_0`; minimality at the right gives a coordinate `b` occurring only
in `X_t`.  Every interior owner omits both `a` and `b`.  Since it is an
`r`-subset of the `(r+2)`-set `H`, it must equal the unique set

\[
                              H\setminus\{a,b\}.                    \tag{2.2}
\]

The owners are distinct, so there is at most one interior owner.  Adjacent
Johnson owners have union of rank `r+1`, hence there must be one interior
owner.  Thus `t=2`.  \(\square\)

### Corollary 2.2 (the arbitrary-width upper-q2 deck is local)

For every cyclic Johnson owner sequence, the set of rank-`r+2` unions of
arbitrary intervals equals

\[
 \{U_2(i):|U_2(i)|=r+2\}.                          \tag{2.3}
\]

Consequently a rethread changes upper-q2 service only at owners whose
neighbour pair changes.  No suffix/prefix crossing-cone state is needed for
q2.  Such a state remains necessary for higher upper ranks.

On the frozen `K17` carrier the centered occurrence profile is

\[
                         11^{22695}10^{1615}.                         \tag{2.4}
\]

It contains `11466` distinct rank-eleven targets and misses `910`.

## 3. The four-coordinate target packet

The marginal geometry behind both q2 shores is useful even though it does
not by itself install a legal rethread.

### Theorem 3.1 (complete q2 flag-path classification)

Let

\[
 L\in\binom\Omega{r-2},\qquad
 H\in\binom\Omega{r+2},\qquad L\subset H.          \tag{3.1}
\]

Order `H-L` as `(a,b,c,d)` and put

\[
 A=L+ab,\qquad V=L+bc,\qquad B=L+cd,              \tag{3.2}
\]

\[
 C=L+b,\qquad D=L+c.                               \tag{3.3}
\]

Then

\[
                         A-C-V-D-B                  \tag{3.4}
\]

is an incidence path and

\[
 A\cap V\cap B=L,\qquad A\cup V\cup B=H,         \tag{3.5}
\]

\[
 A\cup V=H-d,\qquad V\cup B=H-a.                 \tag{3.6}
\]

Conversely, every three-owner Johnson path whose intersection has rank
`r-2` and union has rank `r+2` has this form.  Fixed `L,H` have exactly `24`
directed phases and `12` phases up to reversal.

#### Proof

The displayed identities are direct.  Conversely, write the two Johnson
steps as two deletions and two insertions.  Equality at both extreme ranks
forces those four coordinates to be distinct.  Their complement in the
union is `L`, and the chronological order of the two steps yields (3.2).
\(\square\)

### Lemma 3.2 (correct exact residence guard)

Place `A,V,B` between retained owner fragments `P` and `Q`.  Let `s_P(x)`
be the length of the terminal positive `x`-run of `P`, and `p_Q(x)` the
length of the initial positive `x`-run of `Q`.  Assume all runs internal to
`P,Q` are already of length at least four.

Also require every boundary run which the packet does not extend to be
empty or already of length at least four.  Explicitly this applies to

\[
 p_Q(a),p_Q(b),s_P(c),s_P(d),                       \tag{3.7}
\]

and to both boundary runs for every coordinate outside `H`.

Then every run meeting `P || A,V,B || Q` has length at least four if and
only if

\[
 s_P(a)\ge3,\quad s_P(b)\ge2,\quad
 p_Q(c)\ge2,\quad p_Q(d)\ge3,                      \tag{3.8}
\]

and

\[
                         s_P(x)+p_Q(x)\ge1\quad(x\in L).             \tag{3.9}
\]

#### Proof

Across the packet the four phase words are

\[
 a:100,\qquad b:110,\qquad c:011,\qquad d:001,     \tag{3.10}
\]

coordinates of `L` have word `111`, and coordinates outside `H` have word
`000`.  The extended run lengths are therefore

\[
 s_P(a)+1, s_P(b)+2, 2+p_Q(c), 1+p_Q(d),
 s_P(x)+3+p_Q(x).                                  \tag{3.11}
\]

The hypotheses (3.7) handle the separated boundary runs which (3.11) does
not include.  The threshold-four inequalities are exactly (3.8)--(3.9).
\(\square\)

The extra boundary hypothesis is essential.  For example, an initial
length-two `a`-run in `Q` is separated from `A` by the final packet owner
`B`, which does not contain `a`.

## 4. Alternating hex zipper

Let `K` be an incidence Hamilton cycle as in Section 1.  Suppose

\[
 C_jS_j\in K,qquad C_jS_{j+1}\notin K
 \quad(j\in\mathbb Z/m)                            \tag{4.1}
\]

form a simple alternating circuit.  Let `P_j` be the other selected owner
incident with `C_j`, and let `F_j` be the other selected colour incident
with `S_j`.  Toggle

\[
 C_jS_j\quad\longmapsto\quad C_jS_{j+1}.           \tag{4.2}
\]

### Theorem 4.1 (exact incidence and q2 ledger)

The toggle preserves degree two at every owner and colour.  Hence it
preserves all owners and all lower-q1 colours.  It is a Hamilton carrier if
and only if the resulting two-factor is connected.

Assume for the displayed local formula that the `2m` owner ports
`P_j,S_j` are distinct.  Let `R_j` be the other owner-neighbour of `P_j`,
and `T_j` the other owner-neighbour of `S_j`, before the toggle.  Then the
complete signed lower-q2 delta is

\[
 \Delta_-(L)=
 \sum_j [F_j\cap C_{j-1}=L]
 -\sum_j [F_j\cap C_j=L],                          \tag{4.3}
\]

and the complete signed upper-q2 delta is

\[
\begin{aligned}
 \Delta_+(U)=\sum_j\bigl(&
 [R_j\cup P_j\cup S_{j+1}=U]
 -[R_j\cup P_j\cup S_j=U]\\
 &+[T_j\cup S_j\cup P_{j-1}=U]
 -[T_j\cup S_j\cup P_j=U]\bigr).                 \tag{4.4}
\end{aligned}
\]

Only rank-`r-2` terms in (4.3) and rank-`r+2` terms in (4.4) enter the q2
decks.  Thus exactly `m` lower-q2 occurrences and at most `2m` upper-q2
occurrences change.  Final target multiplicities, not merely the set of
new labels, are the necessary and sufficient no-loss/service test.

#### Proof

Each circuit vertex loses one selected incidence and gains one.  At `S_j`,
the incident colour pair changes from `(F_j,C_j)` to
`(F_j,C_(j-1))`, giving (4.3).  At `P_j`, the neighbour through `C_j`
changes from `S_j` to `S_(j+1)`.  At `S_j`, that neighbour changes from
`P_j` to `P_(j-1)`.  These are the two lines of (4.4); every other owner
keeps the same unordered neighbour pair.  Corollary 2.2 proves completeness
for arbitrary-width upper-q2 service.  \(\square\)

### Proposition 4.2 (hexagons are smallest)

The Boolean inclusion graph between ranks `r-1` and `r` has no four-cycle.
Therefore `m=3`, an alternating hexagon, is the smallest nontrivial closed
q1-preserving packet.

#### Proof

If two distinct rank-`r` owners contained two distinct common rank-`r-1`
facets, the union of those facets would be a rank-`r` set contained in both
owners, forcing the owners equal.  \(\square\)

### Theorem 4.3 (exact residence strand test)

Delete the old owner seams `P_j-S_j`.  For one coordinate `x`, retain all
maximal positive fragments meeting a deleted seam and weight each by its
number of owners.  Add the new seams `P_j-S_(j+1)` whenever both endpoints
contain `x`.  The connected components of this finite weighted fragment
graph are exactly the new `x`-runs meeting the packet, and their run lengths
are the component weight sums.

Consequently the packet creates no run below four if and only if every new
component has weight at least four and every untouched old run was already
safe.  Capping all weights and sums at four gives an exact finite-state test.

#### Proof

All positive adjacencies inside retained fragments are unchanged.  A new
seam joins precisely the two boundary fragments whose endpoint owners both
contain `x`.  Transitive closure gives exactly the new maximal positive
components, and weights count their owners.  \(\square\)

This is the exact integral packet interface: connectedness, (4.3), (4.4),
and the strand test are evaluated for the same alternating circuit.

## 5. Residence is a Catalan-conserved transfer

### Theorem 5.1 (dimension-uniform run count)

In every Hamilton cycle of `I_r(Omega)`, every coordinate has exactly

\[
 \binom{2r-2}{r-1}-\binom{2r-2}{r-2}
 =\operatorname{Cat}_{r-1}                         \tag{5.1}
\]

positive owner runs.

#### Proof

There are `M_x=binom(2r-2,r-1)` owners containing `x`, contributing
`2M_x` selected incidences.  There are
`C_x=binom(2r-2,r-2)` colour vertices containing `x`; their `2C_x`
selected incidences stay wholly within the positive shore.  The remaining
`2(M_x-C_x)` incidences correspond bijectively to mixed owner adjacencies.
Every positive cyclic run has two such boundary adjacencies.  \(\square\)

For `K17`, every coordinate therefore has

\[
 12870-11440=1430=\operatorname{Cat}_8              \tag{5.2}
\]

runs and total positive mass `12870`.  If `h_x(ell)` changes by
`delta_x(ell)` under an exact owner/q1 exchange, then

\[
 \sum_\ell\delta_x(\ell)=0,
 \qquad
 \sum_\ell \ell\delta_x(\ell)=0.                 \tag{5.3}
\]

At threshold four the scalar excess over four per run is

\[
                         12870-4\cdot1430=7150.      \tag{5.4}
\]

Thus mass is abundant, but it must be moved through compatible sockets.

### Corollary 5.2 (two-run donor threshold)

Suppose the complete affected run-length multiset for one coordinate is
replaced as

\[
                         \{t,L\}\longmapsto\{u,v\},\qquad u,v\ge4,  \tag{5.5}
\]

with every other run length fixed.  Repairing `t<4` then requires

\[
                             L\ge 8-t.              \tag{5.6}
\]

Indeed two output runs each have length at least four and their total mass
is `L+t`.  Hence a length-two run needs a donor of at least six, and a
length-three run needs a donor of at least five.

### Theorem 5.3 (current-cycle hitting floor)

The frozen carrier has `1063` length-two and `1829` length-three runs.  Give
each run its entering edge, internal edges, and leaving edge.  If a final
cut/rejoin chronology retains all those support edges, that short run is
unchanged.  Every old edge belongs to at most three short-run supports.
Therefore every flat intact-fragment repair of this cycle deletes at least

\[
              \left\lceil\frac{1063+1829}{3}\right\rceil=964        \tag{5.7}
\]

old seams.  Consequently, a repair using only three-cut hexes needs at least
`322` noncancelled hex packets.  This is necessary, not sufficient.

### Theorem 5.4 (hex-only service floors)

One alternating hex changes exactly three owner seams, exactly three
lower-q2 centers, and at most six upper-q2 centers.  Every rank-`r+1`
interval union already occurs on two adjacent owners: take the first step at
which the union acquires its one coordinate outside the initial owner.
Therefore one hex creates at most three new upper-q1 targets.

Starting from the frozen defect banks, any sequential repair in which every
intermediate output remains a simple Hamilton owner order, using only
alternating hexes and no literal appended holes, consequently uses at least

\[
\begin{array}{c|c}
\text{row}&\text{hex lower bound}\\ \hline
\text{upper q1}&\lceil1891/3\rceil=631\\
\text{lower q2}&\lceil1623/3\rceil=541\\
\text{upper q2}&\lceil910/6\rceil=152\\
\text{old short-run support}&\lceil964/3\rceil=322.
\end{array}                                         \tag{5.8}
\]

Hence a hex-only full repair needs at least `631` packets.  The count is
valid even when packets are chosen adaptively: assign every originally
missing target to the first packet which creates an occurrence of it.  It is
only a lower bound; losses, repeated service, topology, and the fixed-parent
residence packets can force more.

## 6. One literal Pareto-positive `K17` hex

Let

\[
 Q=\mathtt{0x78a2},\qquad (a,b,c)=(0,3,8).          \tag{6.1}
\]

The three colours and owners are

\[
\begin{array}{c|c}
\text{colours}&mathtt{78a3},\mathtt{78aa},\mathtt{79a2}\\
\text{owners}&mathtt{78ab},\mathtt{79aa},\mathtt{79a3}.
\end{array}                                        \tag{6.2}
\]

Toggle the selected incidences

\[
 (\mathtt{78a3},\mathtt{79a3}),
 (\mathtt{78aa},\mathtt{78ab}),
 (\mathtt{79a2},\mathtt{79aa})                    \tag{6.3}
\]

to

\[
 (\mathtt{78a3},\mathtt{78ab}),
 (\mathtt{78aa},\mathtt{79aa}),
 (\mathtt{79a2},\mathtt{79a3}).                   \tag{6.4}
\]

In the frozen owner cycle, this deletes the seams at zero-based indices

\[
                              5607,quad8324,quad11990.              \tag{6.5}
\]

Their literal old/new ledger is

\[
\begin{array}{c|c|c}
5607&\mathtt{79aa}-[\mathtt{79a2}]-\mathtt{7ba2}
    &\mathtt{79a3}-[\mathtt{79a2}]-\mathtt{7ba2}\\
8324&\mathtt{78ab}-[\mathtt{78aa}]-\mathtt{78ba}
    &\mathtt{79aa}-[\mathtt{78aa}]-\mathtt{78ba}\\
11990&\mathtt{79a3}-[\mathtt{78a3}]-\mathtt{7ca3}
     &\mathtt{78ab}-[\mathtt{78a3}]-\mathtt{7ca3}.
\end{array}                                        \tag{6.6}
\]

Define the three forward fragments

\[
\begin{aligned}
 A&=T[5608:8325],      &|A|&=2717,\\
 B&=T[8325:11991],     &|B|&=3666,\\
 C&=T[11991:24310]\Vert T[0:5608],&|C|&=17927.
\end{aligned}                                        \tag{6.7}
\]

The new Hamilton chronology is the literal order

\[
                              T'=C\Vert B\Vert A.                    \tag{6.8}
\]

Its canonical decimal serialization has SHA-256

```text
ee236c63fcb3b2e391918eae926c47ac0ee8360ec2fa35da7fff367bd3173f94
```

and its q1 colour sequence is a permutation of the old complete layer.

### Theorem 6.1 (exact packet delta)

The chronology (6.8) has all `24310` owners and all `24310` lower-q1
colours exactly once.  Relative to the frozen cycle it has the following
strict improvements and no target loss in any displayed deck:

\[
\begin{array}{c|c|c}
\text{deck}&\text{old distinct}&\text{new distinct}\\ \hline
\text{lower q2}&17825&17827\\
\text{upper q1}&17557&17559\\
\text{upper q2}&11466&11468.
\end{array}                                         \tag{6.9}
\]

The newly supplied targets are

\[
\begin{array}{c|c}
\text{lower q2}&\mathtt{70a3},\mathtt{782a}\\
\text{upper q1}&\mathtt{7cab},\mathtt{79ba}\\
\text{upper q2}&\mathtt{7bb3},\mathtt{7eab}.
\end{array}                                         \tag{6.10}
\]

The complete changed run-length multisets are

\[
\begin{array}{c|c}
x&\text{old}\longmapsto\text{new}\\ \hline
0&\{12,13\}\to\{6,19\}\\
1&\{18,19,31\}\to\{8,28,32\}\\
3&\{3,23\}\to\{5,21\}\\
5&\{9,13,19\}\to\{11,14,16\}\\
7&\{2,20,25\}\to\{4,14,29\}\\
8&\{15,32\}\to\{18,29\}\\
11&\{2,5,12\}\to\{4,6,9\}\\
12&\{7,9\}\to\{8,8\}\\
13&\{11,13\}\to\{10,14\}\\
14&\{5,13\}\to\{7,11\}.
\end{array}                                         \tag{6.11}
\]

Every other coordinate run multiset is unchanged.  Hence

\[
 (h_2,h_3):(1063,1829)\longmapsto(1061,1828),       \tag{6.12}
\]

with exactly three short runs removed and none created.

#### Proof

The incidence hex proves owner/q1 degree preservation.  The port order
(6.8) is one cycle, proving connectedness.  Equations (4.3)--(4.4) give the
six displayed target gains after final multiplicities are checked.  The
independent replay reconstructs every owner, every q1 colour, all `24310`
centered lower/upper q2 occurrences, and all cyclic coordinate runs.  It
records the full signed multiplicity changes, not only the hole counts.
\(\square\)

The packet is a genuine positive theorem, but it is a port-level phase
transfer.  It does not alter the fixed macro interiors and therefore cannot
touch the fixed-parent internal debt of the next section.

## 7. The fixed parent pays an unavoidable one-unit residence tax

The following statement assumes the parent is lower-rainbow, which excludes
length-one coordinate runs.

### Theorem 7.1 (odd-diamond run-loss identity)

Let `T_i` be a cyclic lower-rainbow Johnson component and

\[
                              C_i=T_i\cap T_{i+1}.                    \tag{7.1}
\]

For every coordinate, a parent run of length `ell` becomes a run of length
exactly `ell-1` in the `C` sequence, and every positive `C` run arises this
way.

#### Proof

The entering parent edge inserts the coordinate, the leaving edge deletes
it, and the `ell-1` edge intersections beginning at the entering edge retain
it.  Distinct lower edge colours forbid `ell=1`, since the two colours
flanking a singleton run would be equal.  \(\square\)

Thus a flat child needing minimum run `d+1` requires parent minimum run at
least `d+2`, unless an explicit cut/facet/nonflat actuator hits every parent
run of length `d+1`.

For the fixed K15 parent and `d=3`, there are exactly

\[
                         95\cdot15=1425                              \tag{7.2}
\]

parent length-four runs.  They become A-shore patterns `0,111,0`.  Exactly
`165`, eleven per old coordinate, use four rank-six trace colours each of
which has a unique physical occurrence.  Every occurrence transversal must
retain all four edges of each such pattern.

### Corollary 7.2 (solver-free fixed-parent no-go)

No choice of one occurrence of every rank-six trace colour, no macro
permutation or reversal, and no integral port-flow completion based on this
fixed parent can produce a flat depth-three-resident K17 child.

The exact residence CNF has `2805` occurrence variables, `1425` run clauses,
and `165` empty clauses.  The empty clauses are the literal unique-colour
packets; no SAT conclusion is used.

### Proposition 7.3 (exact correlated optimum)

Over all rank-six occurrence transversals of this fixed parent, the exact
minimum number of surviving internal A-shore short runs is

\[
                                  \boxed{180}.                       \tag{7.3}
\]

An authenticated transversal attains `12` per old coordinate and literal
replay reconstructs all `1430` macros.  For the lower bound, the bound-179
CNF asks whether at most `14` of the `1260` non-forced patterns can survive
in addition to the `165` forced ones.  Its DRAT proof is independently
verified, with a `5531`-clause core and `99145` resolution steps.  Thus the
extra `15` runs are an exact cross-coordinate integral-correlation debt, not
an optimizer bound.

### Proposition 7.4 (occurrence coherence with upper service)

The same occurrence variables decide which parent upper-unique providers
remain internal.  For a rank-six fibre `Z`, let `u_Z` be the number of its
physical occurrences whose parent upper union has no other provider.  A
one-occurrence-per-`Z` transversal deletes at least

\[
                              \sum_Z(u_Z-1)^+                        \tag{7.4}
\]

such internal witnesses, and this marginal lower bound is attained when
residence is ignored: retain one upper-unique occurrence whenever the fibre
has one.

#### Proof

At most one physical edge is retained in each `Z`-fibre, so at least
`(u_Z-1)^+` of its upper-unique edges are deleted.  If `u_Z>0`, retaining any
one of them attains that fibre's bound; if `u_Z=0`, retain an arbitrary
occurrence.  The fibres are disjoint, so these choices attain the sum.
\(\square\)

For the fixed parent,

\[
                    u_Z:0^{1835}1^{2685}2^{465}3^{20},              \tag{7.5}
\]

so the exact marginal upper-provider deletion debt is

\[
                              465+2\cdot20=505.                      \tag{7.6}
\]

These deleted internal witnesses may be recreated at ports, so `505` is
not a child upper-hole lower bound.  More importantly, the upper rewards
and the `1425` residence hyperclauses live on the same occurrence variables.
The separate marginal optima `505` and `180` are not known to be attained by
one transversal.  Their formal sum gives the valid inequality
`U+R>=685`, but `685` must not be treated as an attainable joint optimum or
as a common physical child-hole count, and separate marginal minimizers
cannot be composed.

The authoritative occurrence-coherence theorem records the saved octahedral
parent's two separate ledgers as upper-provider debt `405` and exact
residence debt `150`; the present note independently reconstructs only the
`405` fibre profile.  It is a genuine alternative parent input, but neither
number by itself closes its port, deeper-shadow, or compiler rows.

The exact recursive export is occurrence-labelled.  For one transversal
`x`, it must retain together

\[
  (\mathcal R(x),\mathcal A(x),\sigma(x)),           \tag{7.7}
\]

where `R(x)` is the actual surviving minimum-run packet set, `A(x)` the
actual retained upper-unique provider set, and `sigma(x)` the induced macro
paths, endpoint colours, and port-degree demand.  Cardinalities alone lose
the target identities needed downstream.  The residual b-flow is chosen
only after this common state is fixed.

Therefore the live flat route must change the parent chronology or use a
rethread which explicitly cuts the residual internal debt.  The other live
route is a genuinely nonflat compiler.  Merely changing retained
occurrences or recomputing the port flow is closed.

This residence no-go does not close upper q1.  In the fixed macro family the
rank-ten holes split by two-new-coordinate tag `none/Y/X/XY` as

\[
                              618,\quad623,\quad650,\quad0.           \tag{7.8}
\]

The one-tag missing-interior banks have `984` port opportunities each, and
the pure bank has `4021` opportunities for `3003` targets.  These scalar
counts prove no matching, but they also give no capacity obstruction.  Upper
q1 remains a distinct constrained port-turn covering problem.

## 8. Marginal q2 geometry is not the obstruction

For completeness, form the containment graph between the frozen carrier's
`910` missing rank-eleven targets and `1623` missing rank-seven targets,
joining `H` to `L` when `L subset H`.  The graph has

\[
                              33701                                  \tag{8.1}
\]

edges, left degrees between `16` and `91`, and a matching saturating all
`910` upper holes.  Exactly `889` upper holes have at least one missing
rank-ten facet; the corresponding bonus subgraph also has a matching
saturating all `889`.

Theorem 3.1 therefore supplies marginal target phases.  Theorem 4.1 shows
why this does not settle chronology: one must realize those phases inside
alternating circuits, preserve one connected factor, pass the run-strand
test, and preserve final q2 multiplicities simultaneously.

## 9. Exact composition boundary

A collection of alternating packets yields an owner/lower-q1-exact,
residence-safe carrier with both q2 decks and every upper deck complete if
and only if all of the following hold in the common final incidence factor.

1. Every owner and colour has degree two and the factor is connected.
2. Every coordinate's weighted positive-strand graph has no component of
   weight below four; every old short-run support is hit.
3. The final lower- and upper-q2 occurrence loads are positive on every
   target.  They must be computed either directly as final minus initial
   centered loads, or by sequential deltas recomputed in the current state;
   precomputed deltas of overlapping packets cannot simply be summed.
4. Every rank-`r+1` target has positive final adjacency-union load.
5. Every higher upper target has a retained or new interval witness: every
   old missing target is supplied, and every old target whose last witnesses
   cross deleted seams is restored in the exact suffix/prefix crossing-cone
   ledger.

For pairwise disjoint packets, degree preservation is automatic.  The other
four rows are not automatic: disjoint packets may interlace globally, spend
the same donor strand, or share the last witness of a target.  They may be
composed safely either by one global port/strand/shadow replay or
sequentially in the current carrier.  A laminar family is sufficient only
when every module exposes a genuine two-terminal transparent state.

Even an accepting carrier is not yet a word.  Endpoint opening, staircase
envelopes, and one integral common lower compiler remain separate necessary
rows.

## 10. Reproducibility and hashes

Primary marginal audit:

```text
scratch/audit_ad_k17_q2_flag_packet_geometry_20260731.py
scratch/ad_k17_q2_flag_packet_geometry_20260731.audit.json
```

Independent literal hex replay:

```text
scratch/audit_ad_k17_hex_q2_residence_packet_independent_20260731.py
scratch/ad_k17_hex_q2_residence_packet_independent_20260731.audit.json
```

Independent second hex calibration:

```text
MATH_AUDIT_K17_PURE_U_HEX_PACKET_AND_THREE_CHUNK_PHASE_20260731.md
scratch/audit_k17_pure_u_hex_packet_20260731.py
scratch/k17_pure_u_hex_packet_20260731.cycle
scratch/k17_pure_u_hex_packet_20260731.audit.json
```

Residence-transfer companion:

```text
MATH_THEOREM_K17_CATALAN_RESIDENCE_TRANSFER_AND_PHASE_PORT_COMPOSITION_20260731.md
```

Fixed-parent obstruction and occurrence CNF:

```text
MATH_THEOREM_K17_FIXED_MACRO_RESIDENCE_OBSTRUCTION_20260731.md
MATH_THEOREM_ODD_DIAMOND_RESIDENCE_TAX_20260731.md
MATH_THEOREM_ODD_DIAMOND_OCCURRENCE_COHERENCE_20260731.md
scratch/build_k17_macro_residence_cnf_20260731.py
scratch/k17_macro_residence_20260731.cnf
scratch/k17_macro_residence_20260731.map.json
scratch/solve_k17_macro_residence_maxsat_20260731.py
scratch/k17_macro_residence_optimal_20260731.json
scratch/verify_k17_macro_residence_optimum_20260731.py
scratch/k17_macro_residence_optimal_20260731.verify.json
scratch/build_k17_macro_residence_bound_cnf_20260731.py
scratch/k17_macro_residence_bound179_20260731.cnf
scratch/k17_macro_residence_bound179_20260731.drat
scratch/k17_macro_residence_bound179_20260731.dratcheck.txt
```

All finite statements are scoped to the frozen cycle or parent named above.
No computation here proves packet packability, a complete K17 carrier, a
common compiler, or `nu(17)=B(17)`.
