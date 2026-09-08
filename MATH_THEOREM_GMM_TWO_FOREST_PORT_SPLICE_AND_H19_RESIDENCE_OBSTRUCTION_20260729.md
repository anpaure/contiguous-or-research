# GMM two-forest port splicing and the H19 AA-support residence obstruction

Date: 2026-07-29

Status: exact theorem, exact constants, and independently rebuilt `k=15`
audit.  This note proves a smaller constructive normal form for generalized
Pascal braids and a sharp obstruction for the authoritative Hall-19 carrier.
It does **not** construct a new literal contiguous-OR word and does not claim
the coefficient-one theorem.

The only finite calculations used here are bounded exact audits of saved
artifacts: one complete Johnson-edge catalogue and two explicitly delimited
minimum-support port enumerations.  No SAT, path LNS, broad chronology
search, H100 job, or other heavy process was run.

## 1. Odd middle-deck split

Let

\[
 \Omega=[2m],\qquad z\notin\Omega,
 \qquad W=\binom{2m}{m},
 \qquad C=\frac1{m+1}\binom{2m}{m}.
\]

Split the rank-\((m+1)\) middle deck of `Omega+z` into

\[
 \mathcal A=\{\{z\}\cup T:T\in\tbinom\Omega m\},
 \qquad
 \mathcal B=\tbinom\Omega{m+1}.
\tag{1.1}
\]

For later use put

\[
 L=\binom{2m}{m-1}=\binom{2m}{m+1}=W-C,
 \qquad
 U=\binom{2m}{m+2},
\tag{1.2}
\]

and

\[
 D=L-U
   =\frac{3m}{m+2}C.
\tag{1.3}
\]

An `AA` Johnson edge has lower colour
`z+(rank m-1)` and upper colour `z+(rank m+1)`.  A cross
edge from `z+T` to `V` exists exactly when `T subset V`; its lower colour is
`T` and its upper colour is `z+V`.  A `BB` edge has a rank-`m`
intersection colour and a rank-`m+2` union colour.

## 2. The two canonical GMM forests

We use the proved two-level tight-enumeration theorem in the following exact
form.

> A tight enumeration of two consecutive Boolean levels contracts to a
> Hamilton Johnson cycle on the larger owner class.  Each vertex of the
> other level lies between two incident owners and therefore marks one
> Johnson edge, with its set as the intersection or union colour.  Every
> vertex of that other level marks exactly one edge.

This is the local theorem audited in the GMM tight-enumeration reports.  The
following extraction is elementary but important.

### Theorem 2.1 (two marked path forests)

For every `m` for which the two tight enumerations are fixed, there are
spanning path forests

\[
 F_A\subseteq J(2m,m),
 \qquad
 F_B\subseteq J(2m,m+1)
\]

with the following exact data.

1. `F_A` has `W` vertices, `L` edges, and exactly `C` path
   components.  Its edge intersections enumerate every member of
   \(\binom\Omega{m-1}\) exactly once.

2. `F_B` has `L` vertices, `U` edges, and exactly `D` path
   components.  Its edge unions enumerate every member of
   \(\binom\Omega{m+2}\) exactly once.

Singleton vertices are allowed and count as one-vertex path components with
two coincident degree ports.

#### Proof

Contract a tight enumeration of levels `{m-1,m}` to its Hamilton cycle on
\(\binom\Omega m\), and retain only the `L` edges marked by rank-`m-1`
vertices.  The retained graph is a proper subgraph of one cycle, hence is a
spanning path forest.  Its marked colours are pairwise distinct and exhaust
the rank-`m-1` level.  Its component count is

\[
 W-L=C.
\]

Apply the upper version of the same theorem to levels `{m+1,m+2}`.  Retain
the `U` edges marked by rank-`m+2` vertices.  They form a spanning path
forest on the `L` rank-`m+1` owners, their unions are the rank-`m+2`
sets exactly once, and their component count is

\[
 L-U=D.
\]

Finally,

\[
\begin{aligned}
L-U
&=\frac m{m+1}W
  -\frac{m(m-1)}{(m+1)(m+2)}W\\
&=\frac{3m}{(m+1)(m+2)}W
 =\frac{3m}{m+2}C.
\end{aligned}
\]

This proves every claim. \(\square\)

## 3. Port graph

Every path component of `F_A` and `F_B` has two degree ports.  For a
singleton component the two ports are distinct copies attached to the same
owner.  A selected external edge consumes one port at each end.

Allowed external edges are of two types.

* A cross port edge joins an endpoint `T` of an A path to an endpoint `V`
  of a B path exactly when `T subset V`.
* A B-merge port edge joins endpoints `V,V'` of two B paths exactly when
  they are Johnson adjacent.

No `A--A` port edge is allowed.  Repeated use of one physical middle edge is
forbidden.  Contract each original path component to one vertex; selected
external edges then form the **component quotient**.

Two cautions are immediate.  First, the protected edges of `F_B` need not
have distinct intersection labels merely because their union labels are
distinct.  A collision already inside `F_B` makes the lower-injectivity
hypothesis below impossible.  Second, a singleton A path has two cross ports
at the same owner `T`; using both creates the lower label `T` twice.  Thus a
successful exact-lower port splice automatically has no singleton A
component.  GMM tightness by itself supplies neither property.

For an external selection `S`, write

\[
 S=S_X\mathbin{\dot\cup}S_B
\]

for its cross and B-merge edges.

## 4. Exact cyclic port-splice theorem

### Theorem 4.1 (cyclic completion)

Assume that an external selection `S` satisfies all of the following.

1. Every A and B port is used exactly once.
2. The component quotient is connected.
3. The rank-`m` intersection labels on

   \[
   F_B\cup S_B\cup S_X
   \tag{4.1}
   \]

   are pairwise distinct.
4. The rank-`m+1` labels supplied by the unions of `F_A` together with the
   B endpoints of `S_X` cover all of \(\binom\Omega{m+1}\).

Then the lifted union

\[
 (\{z\}+F_A)\cup F_B\cup S
\tag{4.2}
\]

is one Hamilton cycle on the entire odd middle deck.  It has exact lower
`q=1` ownership and complete upper `q=1` support.

The selected channel counts are forced:

\[
 AA=L,
 \qquad
 BB=W-2C,
 \qquad
 \lvert S_X\rvert=2C,
\tag{4.3}
\]

and the B-merge count is

\[
 \lvert S_B\rvert=D-C
 =\frac{2(m-1)}{m+2}C.
\tag{4.4}
\]

#### Proof

After internal paths are contracted, every quotient vertex has degree two,
because its two ports are used.  A connected finite degree-two graph is one
cycle.  Expanding its vertices back to their internally vertex-disjoint
paths gives one Hamilton cycle on all A and B owners.

Every A component has two cross ports and no A--A external port.  Hence

\[
 |S_X|=2C.
\]

The quotient has `C+D` vertices and therefore `C+D` edges.  Its remaining
edges are B merges, so

\[
 |S_B|=C+D-2C=D-C.
\]

The final BB count is

\[
 U+(D-C)=L-C=W-2C.
\]

The number of no-`z` lower edges in (4.1) is

\[
 (W-2C)+2C=W.
\]

There are exactly `W` rank-`m` targets.  Hypothesis 3 therefore makes the
intersection map a bijection.  The AA intersections are already the other
`L` lower targets exactly once by Theorem 2.1.

The edges of `F_B` already supply every no-`z` upper target exactly once;
adding B merges cannot erase them.  Hypothesis 4 is exactly the remaining
`z`-upper cover. \(\square\)

If connectivity is omitted, the same hypotheses give an exact `q=1`
2-factor, possibly with several cycles.

## 5. Exact open-path port-splice theorem

The open form is the one relevant to the current Hall-19 B-to-B carrier.

### Theorem 5.1 (open B-to-B completion)

Assume `m>=2`.  Suppose an external selection satisfies:

1. every A port and all but two B ports are used exactly once;
2. the two unused ports belong to the B shore;
3. the component quotient is connected;
4. the intersection labels on `F_B union S_B union S_X` are pairwise
   distinct; and
5. the unions of `F_A`, together with the B endpoints of the cross edges,
   cover every rank-`m+1` old-ground set.

Then the lifted graph is a Hamilton path through the entire odd middle
deck, with both physical endpoints in B.  Its AA lower deck is exact, its
no-`z` lower deck has exactly one hole and no duplicate, and both upper
`q=1` decks are complete.

The exact external counts are

\[
 |S_X|=2C,
 \qquad
 |S_B|=D-C-1,
\tag{5.1}
\]

so the final channel counts are

\[
 AA=L,
 \qquad
 BB=W-2C-1,
 \qquad
 \text{cross}=2C.
\tag{5.2}
\]

#### Proof

The quotient has `C+D` vertices.  All A vertices have degree two; all B
vertices have degree two except for the two quotient endpoints forced by
the unused B ports.  Connectivity makes the quotient one path.  It has
`C+D-1` external edges.  Since all `2C` A ports are cross ports,

\[
 |S_B|=(C+D-1)-2C=D-C-1.
\]

The final BB count is

\[
 U+(D-C-1)=W-2C-1.
\]

Consequently the no-`z` lower channel has

\[
 (W-2C-1)+2C=W-1
\]

edges.  Injectivity leaves exactly one of the `W` rank-`m` targets uncovered.
All other ownership and upper-cover conclusions are identical to Theorem
4.1. \(\square\)

### Corollary 5.2 (distinguished-coordinate residence)

In either Theorem 4.1 or 5.1, the maximal runs containing `z` are exactly the
path components of `F_A`.  Therefore depth-`d` residence at `z` holds if and
only if every A component has at least `d+1` vertices.

This conclusion is exact because every external edge incident with A is a
cross edge to B, and no B owner contains `z`.  It says nothing about
residence of the old coordinates.

### Corollary 5.3 (direct-jump specialization)

For the particular B forest extracted from one tight enumeration, let `J`
be the `D` unmarked direct edges of its contracted Hamilton cycle.  After
the marked forest components are contracted, `J` is their component cycle.
Consequently one may restrict every B merge in Theorems 4.1 and 5.1 to `J`:

* retaining any `D-C` jumps leaves `C` B paths for the cyclic splice;
* retaining any `D-C-1` jumps leaves `C+1` B paths for the open splice.

The colour, port, and full-quotient connectivity conditions remain.  In
particular, arbitrary choice of the correct number of jumps does not imply
the opposite lower-colour injection or cross Hall conditions.

#### Proof

The contracted tight enumeration is one Hamilton cycle, partitioned into
the marked path forest and the deleted direct edges.  Contracting every
marked path turns the deleted edges into a cycle on the `D` components.
Adding fewer than all `D` cycle edges creates no cycle and lowers the
component count by exactly the number added.  Substitute `D-C` or
`D-C-1`. \(\square\)

## 6. The `m=7` constants

For the `14 -> 15` lift,

\[
\begin{array}{c|c}
W=\binom{14}{7}&3432\\
L=\binom{14}{6}=\binom{14}{8}&3003\\
U=\binom{14}{9}&2002\\
C=\mathrm{Cat}_7&429\\
D=L-U&1001.
\end{array}
\tag{6.1}
\]

Thus:

\[
\begin{array}{c|cc}
&\text{cyclic factor}&\text{open B--B path}\\ \hline
A\text{ paths}&429&429\\
\text{initial B paths}&1001&1001\\
B\text{-merge edges}&572&571\\
\text{cross edges}&858&858\\
\text{external quotient edges}&1430&1429.
\end{array}
\tag{6.2}
\]

The quotient has only `C+D=1430` component vertices.  This is the promised
replacement for an unconstrained selection over every cross and BB diamond:
once the two rainbow forests are fixed, one selects a port Hamilton cycle or
path with exact colour side constraints.

This is a conditional reduction, not an unconditional GMM fusion theorem.
In particular, the B forest's protected lower labels, endpoint containment
Hall inequalities, lower-label complement, and quotient connectivity remain
simultaneous constraints.

## 7. Exact H19 decomposition

The authoritative H19 carrier is

```text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
SHA-256 86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

At `z=14` it has

\[
 AA=3004,
 \qquad
 \text{cross}=856,
 \qquad
 BB=2574.
\tag{7.1}
\]

Its B-sector graph is already a spanning path forest with 429 components.
Its 2,574 edges cover all 2,002 rank-nine union colours.  Choose one edge
for each union colour.  Since this is a subgraph of a forest, the chosen
2,002 edges form an upper-rainbow spanning path forest with

\[
 3003-2002=1001
\]

components.  The remaining 572 old BB edges are literally component-merging
edges.  Thus the H19 B sector realizes the exact `1001 -> 429` cyclic count
of Theorem 4.1.

This statement does not assert that the chosen 2,002-edge forest is the
particular GMM output; only its exact rainbow and path-forest properties are
used.

## 8. Sharp H19 AA-support residence obstruction

The H19 AA lower labels cover all 3,003 rank-six old-ground sets, with one
duplicate:

\[
 756
\]

on path-edge starts

\[
\begin{array}{c|c|c}
2582&(17142,21236)&\text{old union }4854\\
5917&(17148,17396)&\text{old union }1020.
\end{array}
\tag{8.1}
\]

### Theorem 8.1 (no resident exact forest inside the current AA support)

There is no exact AA lower-rainbow path forest contained in the present H19
AA edge set whose components all have at least four vertices.

More precisely:

* deleting edge 2582 splits its old four-vertex A run into lengths `2+2`;
* deleting edge 5917 splits its old eight-vertex A run into lengths `3+5`.

Consequently no arbitrary rechoice of BB merges and cross port edges can
turn either retained-support AA forest into a depth-three-resident
generalized braid.

#### Proof

An exact AA lower-rainbow forest has 3,003 edges.  Every present AA edge
whose lower label is not 756 is the sole present occurrence of its label, so
all 3,002 such edges are forced.  Exactly one of the two 756 edges is also
forced.  Hence the only two exact subsets are obtained by deleting edge 2582
or edge 5917.

In the first case the containing A run occupies positions 2581 through
2584; deleting its middle edge gives component sizes two and two.  In the
second case the containing run occupies positions 5915 through 5922;
deleting the selected edge gives sizes three and five.  Corollary 5.2 now
proves the residence failure, independently of every B and cross choice.
\(\square\)

### Corollary 8.2 (exact AA support-distance lower bound)

Any depth-three-resident exact AA forest has at least one AA edge outside the
present H19 AA support.  If it has the forced 3,003 edges, it must delete at
least two present AA edges and add at least one new AA edge.  Thus its AA
edge symmetric difference from H19 has size at least three.

#### Proof

Theorem 8.1 excludes a subset solution, so at least one new edge is used.  If
`a` present edges are deleted and `b>=1` new edges are added, edge count gives

\[
 3004-a+b=3003,
\]

so `a=b+1>=2`. \(\square\)

This is stronger than the existing three-seam no-go in one direction: it
allows an arbitrary global B/cross port rethreading, but freezes the AA edge
support.  It does not exclude a genuinely new AA braid.

## 9. Degree-preserving short BB trades do not supply the missing move

Let a BB edge `e=XY` have lower and upper labels

\[
 \lambda(e)=X\cap Y,
 \qquad
 \upsilon(e)=X\cup Y.
\]

A BB trade deleting `R` and adding `A` preserves B degrees exactly when

\[
 \sum_{e\in R}{\bf1}_{v\in e}
 =\sum_{e\in A}{\bf1}_{v\in e}
 \qquad\text{for every B owner }v.
\tag{9.1}
\]

It preserves complete rank-nine support exactly when

\[
 m_9(V)-r_9(V)+a_9(V)\ge1
 \qquad(V\in\tbinom\Omega9).
\tag{9.2}
\]

For H19, the only BB edges whose deletion can consume a present non-AA
excess are

\[
\begin{array}{c|c|c}
840&(14733,13197)&\lambda=12685\\
5046&(13709,12687)&\lambda=12685\\
2553&(3900,3996)&\lambda=3868.
\end{array}
\tag{9.3}
\]

The four holes are

\[
 \{5801,7267,8877,13620\}.
\tag{9.4}
\]

An added BB edge carrying a hole `h` must have both endpoints containing
`h`.  None of the six endpoints in (9.3) contains any of the four holes.
Therefore a degree-preserving two-edge trade, which is an alternating C4
after cancellation, cannot reduce the hole count.

For a connected three-edge trade, cancellation leaves an alternating C6.
If `D=d_0d_1` is the consumed excess edge and `pq` is a new hole edge, the
other two old edges must be `pr,qs`, while the remaining two new edges must
match `r,s` to `d_0,d_1`.  The complete nonempty return-port table is

\[
\begin{array}{c|c|c|c|c}
D&h&p&\text{old port }p-r&\text{return adjacency}\\ \hline
840&5801&6057&5562:6057-13225&13225\sim13197\\
840&8877&9133&382:9133-12717&12717\sim14733,13197\\
5046&8877&9133&382:9133-12717&12717\sim13709,12687\\
5046&13620&13628&929:13628-13740&13740\sim13709.
\end{array}
\tag{9.5}
\]

Every other `(D,h)` pair has no return port.  An alternating C6 needs two
compatible return ports, whereas every row of (9.5) supplies at most one.
If two excess old-edge groups are consumed, every new edge meets an excess
endpoint, and the preceding containment test again forbids a hole edge.
Hence:

> No degree-preserving H19 BB trade on at most three edges reduces the four
> non-AA lower holes.  Rank-nine support and chronology can only impose
> additional restrictions.

This theorem closes a staged C4/C6 BB preparation.  The correct open braid
itself changes the BB count from 2,574 to 2,573, so a successful construction
must be a coupled degree-changing AA/BB/cross circulation rather than a BB
cycle followed by an independent cross augmentation.

## 10. Full-q1 feasibility and the remaining boundary

The fixed-path generalized model has already solved simultaneous q1:

```text
scratch/k15_generalized_pascal_braid/full_q1_s15105.json
SHA-256 e8092469c88b0a224bf0b11ed2661e06b5de260cc349717ea704732f47e00f29
```

The saved factor has

\[
 AA=3003,
 \qquad
 \text{cross}=858,
 \qquad
 BB=2574,
\]

both lower q1 decks exact, both upper q1 decks complete, and nine physical
cycles.  It also has 1,527 depth-three residence defects, including 97 at
`z` (52 runs of length two and 45 of length three).  Thus q1 compatibility
is feasible; chronology is not a marginal obstruction.

The independent lightweight audit is

```text
scratch/audit_k15_gmm_port_h19_residence_obstruction.py
scratch/k15_gmm_port_h19_residence_obstruction.audit.json
```

It rebuilds:

* all constants in (6.1)--(6.2);
* the H19 sector counts and file hash;
* the canonical `2002-edge/1001-component + 572 merges` B decomposition;
* the two exact AA deletion choices and their `2+2`, `3+5` splits; and
* the full-q1 factor hash and residence counts.

The exact remaining constructive theorem is now smaller but still
substantial:

1. choose a lower-rainbow A forest whose components are all residence-safe
   and whose protected windows support the required deeper flags;
2. choose an upper-rainbow B forest whose protected intersection labels do
   not already collide;
3. find a connected port path/cycle satisfying the no-z lower injection and
   z-upper cover simultaneously;
4. audit old-coordinate residence, all deeper shadows, seam collars, and one
   common physical compiler word.

The port theorem proves that an unconstrained 84k-scale diamond selection is
not intrinsic once the two forests are fixed.  It does **not** prove that a
residence-safe GMM forest or a compiler-compatible port Hamilton path exists.
Those are the sharp unproved gates.

## 11. Exact fixed-forest circulation

The port formulation can be sharpened to an ordinary capacitated matching
once the two forests and the retained B jumps are fixed.

Let `E_A` be the set of A-path endpoint labels.  For a full exact lower deck
these labels must be distinct, so

\[
 |E_A|=2C,
 \qquad
 I_A=\binom\Omega m\setminus E_A,
 \qquad
 |I_A|=W-2C=L-C.
\tag{11.1}
\]

Let `E_0` be the `U` protected edges of the upper-rainbow B forest, let `J`
be the `D` direct jumps of its component cycle, and write `ell(e)` for the
rank-`m` intersection of a B edge.

### Theorem 11.1 (opposite-lower jump criterion)

For a cyclic completion, a subset of `D-C` direct jumps supplies the exact
BB lower deck `I_A` if and only if:

1. the labels `ell(E_0)` are pairwise distinct and lie in `I_A`; and
2. every member of `I_A minus ell(E_0)` occurs on a direct jump, from which
   one occurrence of each is selected.

For an open B-to-B completion, the corresponding condition is that there is
one

\[
 h\in I_A\setminus\ell(E_0)
\]

such that every member of

\[
 I_A\setminus(\ell(E_0)\cup\{h\})
\]

occurs on a direct jump.  Selecting one of each gives `D-C-1` jumps and
leaves precisely `h` as the open lower hole.

#### Proof

All B lower labels must be distinct and complementary to the cross labels
`E_A`.  The protected edges cannot be deleted.  In the cyclic case the
number still required is

\[
 |I_A|-|E_0|=(L-C)-U=D-C.
\]

The open case has one fewer B edge.  Corollary 5.3 makes every indicated
jump selection a forest of the required component count. \(\square\)

Now fix the resulting B forest `P_B` and put

\[
 b_V=2-\deg_{P_B}(V)
 \qquad(V\in\tbinom\Omega{m+1}).
\tag{11.2}
\]

Also let

\[
 \lambda_V
 =|\{e\in F_A:\operatorname{union}(e)=V\}|.
\tag{11.3}
\]

### Theorem 11.2 (cross Hall and upper repair)

In the cyclic case, cross completion exists if and only if

\[
 \lambda_V+b_V\ge1
 \quad\text{for every }V
\tag{11.4}
\]

and

\[
 |S|\le\sum_{V\in N(S)}b_V
 \quad\text{for every }S\subseteq E_A.
\tag{11.5}
\]

In the open case, it exists if and only if there are integers

\[
 0\le\kappa_V\le b_V,
 \qquad
 \sum_V\kappa_V=2C,
\tag{11.6}
\]

such that

\[
 \lambda_V+\kappa_V\ge1
\tag{11.7}
\]

and

\[
 |S|\le\sum_{V\in N(S)}\kappa_V
 \quad(S\subseteq E_A).
\tag{11.8}
\]

Here `T` is adjacent to `V` exactly when `T subset V`.  In either case the
resulting component quotient must still be tested for connectedness.

#### Proof

Every A endpoint has cross demand one.  In a cycle every B port is used, so
the cross load at `V` is exactly `b_V`; in an open path two B ports remain
unused, giving the choice `kappa`.  Equations (11.4) and (11.7) are exactly
the z-upper cover.  Equations (11.5) and (11.8) are the capacitated Hall
criterion for matching every distinct A endpoint label to a containing B
port. \(\square\)

Theorems 11.1 and 11.2 are coupled: the chosen B jumps determine the degree
capacities in the Hall network.  They cannot in general be optimized in two
independent stages.

## 12. Quarantined four-level tight-enumeration equivalence

This section independently cross-audits and specializes
`MATH_THEOREM_QUARANTINED_FOUR_LEVEL_TIGHT_ENUMERATION_BRAID_20260729.md`
to the H19 repair problem.

Consider the four-level band

\[
 \mathcal Q_{m-1,m,m+1,m+2}
 =\bigcup_{j=m-1}^{m+2}\binom\Omega j.
\tag{12.1}
\]

The parity class consisting of ranks `m-1,m+1` has size `2L`; the other
class has size `W+U`.  Their imbalance is

\[
 2L-(W+U)=D-C.
\tag{12.2}
\]

### Lemma 12.1 (tight parity accounting)

Every cyclic enumeration of the band has total Hamming length at least

\[
 |\mathcal Q_{m-1,m,m+1,m+2}|+(D-C)=4L.
\tag{12.3}
\]

Equality holds if and only if:

1. every opposite-parity transition has Hamming length one;
2. there are exactly `D-C` same-parity transitions, all in the larger
   parity class; and
3. every such same-parity transition has Hamming length two.

#### Proof

Let `p=2L`, `q=W+U`, and let `s_p,s_q` count same-class adjacencies in the
two classes.  Counting cyclic incidences gives

\[
 s_p-s_q=p-q=D-C.
\]

Opposite-class transitions cost at least one and same-class transitions at
least two.  Relative to one per transition, the excess is at least

\[
 s_p+s_q=(p-q)+2s_q.
\]

This proves (12.3) and every equality condition.  Direct substitution of
the binomial values gives `|Q|+D-C=4L`. \(\square\)

Call a tight enumeration **B-quarantined** when all its distance-two steps
join two rank-`m+1` vertices.

### Theorem 12.2 (four-band contraction and converse)

A B-quarantined tight enumeration contracts, after deleting ranks `m-1`
and `m+2`, to a Hamilton cycle on the odd middle deck with exact channel
counts

\[
\begin{array}{c|c}
AA&L\\
BB\text{ mediated by rank }m+2&U\\
BB\text{ direct}&D-C\\
\text{cross}&2C.
\end{array}
\tag{12.4}
\]

Its AA intersections enumerate every rank-`m-1` set exactly once, and its
mediated BB unions enumerate every rank-`m+2` set exactly once.

Conversely, suppose a Hamilton cycle on the central A/B deck has:

1. every rank-`m-1` AA intersection exactly once; and
2. every rank-`m+2` BB union at least once.

Then it expands to a B-quarantined tight enumeration of the four-level band.

#### Proof

Under quarantine, every rank-`m-1` vertex is flanked by two rank-`m`
owners, and every rank-`m+2` vertex by two rank-`m+1` owners.  Contracting
them produces `L` AA and `U` mediated BB edges.  Lemma 12.1 supplies exactly
`D-C` direct BB steps.  The remaining edges of the central Hamilton cycle
are

\[
 (W+L)-L-U-(D-C)=2C
\]

cross edges.

For the converse, the A-induced subgraph of the central Hamilton cycle is a
path forest.  It has `W` vertices and `L` edges, hence `C` components and
`2C` cross boundary edges.  The BB count is therefore `L-C`.  Select one BB
edge for each of the `U` upper colours.  Insert its rank-`m+2` union between
its endpoints, and insert each rank-`m-1` intersection between its unique AA
endpoints.  The remaining BB edges number

\[
 (L-C)-U=D-C
\]

and stay as direct distance-two steps.  Every inserted pair of unit steps
replaces one distance-two central edge, so the total Hamming length is

\[
 2L+2(L-C)+2C=4L,
\]

which is tight by Lemma 12.1.  All unmediated distance-two steps are BB.
\(\square\)

This equivalence supplies global component chronology, but not the opposite
lower deck, z-upper coverage, residence, deeper shadows, or compiler
compatibility.

### Corollary 12.3 (H19 is not a quarantined four-band contraction)

At `m=7`, H19 has `AA=L+1=3004`, so it cannot be the contraction of a
B-quarantined tight enumeration.  In fact the same count excludes a
contraction of any tight four-band enumeration, because Lemma 12.1 permits
no distance-two step in the smaller parity class and each rank-six vertex
can mediate at most one AA edge.

Moreover its fixed endpoints are

\[
 9901,\qquad7779,
\]

with

\[
 |9901\mathbin\triangle7779|=8.
\]

Cutting one contracted Hamilton cycle would leave endpoints joined by the
removed Johnson edge and hence at Hamming distance two.  Therefore a repair
toward one four-band cycle must also move the endpoint/collar geometry; an
internal edit retaining the two H19 endpoints cannot suffice.

If the desired open chronology is obtained by cutting a `BB` edge of a
quarantined contracted cycle, its channel counts are

\[
 (AA,BB,X)=(L,W-2C-1,2C).
\tag{12.5}
\]

Relative to H19, the exact channel current is therefore

\[
 \Delta(AA,BB,X)=(-1,-1,+2).
\tag{12.6}
\]

Thus recognizing the H19 path as the desired object is impossible, while
repairing it has a very specific form: one AA adjacency and one BB adjacency
must be traded for two cross adjacencies, and the two final B endpoints must
also be Johnson adjacent so that the missing BB edge closes the four-band
cycle.  Counts alone do not supply either the degree circulation or that
endpoint condition.

### Corollary 12.4 (exact global cut interface)

Let `P` be a Hamilton path on the odd middle deck with both endpoints in B.
Then `P` is a one-BB-edge cut of a q1-perfect Hamilton cycle, and hence
expands to a decorated B-quarantined four-level tight enumeration, if and
only if all of the following hold:

1. the path intersections are pairwise distinct and omit exactly one no-z
   rank-`m` colour `h`;
2. its two endpoints are Johnson adjacent and have intersection `h`; and
3. the path unions together with the endpoint-edge union cover the complete
   upper q1 level.

#### Proof

Necessity follows by deleting the closing BB edge from a q1-perfect cycle.
Conversely, add the endpoint edge.  Condition 2 fills exactly the sole lower
hole, so the cycle intersections enumerate the complete lower q1 level
exactly.  Condition 3 gives complete upper q1.  Theorem 4.1 of
`MATH_THEOREM_TRACE_QUARANTINE_COLLAPSE_20260729.md` now expands this global
q1-perfect carrier to the decorated quarantine. \(\square\)

Thus the H19 repair does not need to recover either preselected GMM forest.
The global degree/colour circulation plus the closing-edge test subsumes the
fixed-forest port Hall and connectivity conditions.  Residence, deeper
shadows, and compiler compatibility remain outside this collapse.

## 13. Complete minimum AA exchange classification

Corollary 8.2 gives a lower bound of two old AA deletions and one new AA
edge.  This bound is attained.

The deterministic audit

```text
scratch/audit_k15_h19_minimal_resident_aa_exchanges.py
scratch/k15_h19_minimal_resident_aa_exchanges.audit.json
```

enumerates all 81,080 off-support AA Johnson edges and all 162,134 possible
minimum-distance exact-colour repairs.  Exactly 17 produce a spanning
429-path AA forest whose every component has at least four vertices.  All
17 delete duplicate edge 5917; none uses edge 2582.

The candidate index below is zero-based in the audit JSON.  Edge endpoints
and colours have `z` removed.

\[
\begin{array}{c|c|c|c|c}
i&\text{new AA edge}&\text{lower}&\text{other old edge removed}&
\text{new endpoint labels}\\ \hline
0&4813-4841&4809&503&764,1012,13001\ (4813\text{ removed})\\
1&764-4348&252&852&508,1012\\
2&764-4796&700&1401&701,1012\\
3&1741-4813&717&1674&764,1012,8909\ (4813\text{ removed})\\
4&2765-4813&717&1674&764,1012,1741,8909\ (2765,4813\text{ removed})\\
5&4813-8909&717&1674&764,1012,1741\ (4813\text{ removed})\\
6&762-764&760&3532&1012,1016,2808\ (762\text{ removed})\\
7&764-1016&760&3532&1012,2808\\
8&764-2808&760&3532&1012,1016\\
9&764-8952&760&3532&1012,1016,2808\ (8952\text{ removed})\\
10&4813-4821&4805&3731&764,1012,4837\ (4813\text{ removed})\\
11&4813-6733&4685&3932&764,1012,4717\ (4813\text{ removed})\\
12&764-8924&732&5033&1012,1756\\
13&638-764&636&5878&1012,4732\\
14&4557-4813&4301&6367&764,1012,5325\ (4813\text{ removed})\\
15&4813-5325&4301&6367&764,1012,4557\ (4813\text{ removed})\\
16&4813-6349&4301&6367&764,1012,4557,5325\ (4813,6349\text{ removed}).
\end{array}
\tag{13.1}
\]

Every row also deletes 5917.  Parenthetical labels are old endpoints removed
from the cross-demand set.  The audit checks degrees, acyclicity, exact
rank-six colours, 429 components, and minimum component length four by exact
interval arithmetic on the old A runs.

Thus the AA gate is not obstructed at support distance three.  Its output is
the exact endpoint-demand catalogue for the coupled B/cross circulation.

## 14. First coupled-circulation obstruction

For each AA candidate let `E_A` be its 858 endpoint labels.  The desired
open BB label set has the form

\[
 \binom{[14]}7\setminus(E_A\cup\{h\})
\tag{14.1}
\]

for one open hole `h`.  Comparing (14.1) with the old BB multiset gives six
best AA rows:

\[
 i\in\{1,2,7,8,12,13\}.
\tag{14.2}
\]

Each forces four old BB lower labels to be retired and three of the four old
holes to be inserted.  The exact forced retirements are

\[
\begin{array}{c|c}
i&\text{old BB lower labels}\\ \hline
1&508,1012,3868,12685\\
2&701,1012,3868,12685\\
7&1012,2808,3868,12685\\
8&1012,1016,3868,12685\\
12&1012,1756,3868,12685\\
13&1012,3868,4732,12685.
\end{array}
\tag{14.3}
\]

The BB occurrences of 3868 and 1012 have unique upper colours

\[
 4028,\qquad2044.
\tag{14.4}
\]

None of the four old lower holes is a rank-seven subset of either colour in
(14.4).  Hence every repair in (14.2) needs at least two additional upper
relays: replace each unique lost incidence by another lower facet of the
same upper colour and retire that facet's old BB occurrence.  Rows 2, 7, and
13 attain the resulting incidence lower bound

\[
 6\text{ old BB edges removed},
 \qquad
 5\text{ new BB edges added}.
\tag{14.5}
\]

For row 2 the third apparently unique upper colour 9917 can be carried by
the new hole label 8877.  Rows 7 and 13 have slack on their fourth forced
old upper colour.  The other three rows require at least three relays.

The word *incidence* is essential here.  For example, row 2 has an explicit
lower/upper-colour ledger at the `6 -> 5` bound.  Besides its forced old
labels, retire the donor occurrences

\[
 764:\ (8956,1788),\quad \upsilon=9980,
 \qquad
 956:\ (9148,1980),\quad \upsilon=10172,
\tag{14.6}
\]

and insert

\[
 (1020,1788),\quad \lambda=764,\ \upsilon=2044,
 \qquad
 (1980,3004),\quad \lambda=956,\ \upsilon=4028.
\tag{14.7}
\]

The old donor unions in (14.6) have multiplicity two, so their deletion
loses no upper colour.  Row 2 also loses upper colour 9917 when lower label
701 is retired; the hole edge

\[
 (8893,9901),\quad \lambda=8877,\ \upsilon=9917
\tag{14.8}
\]

repairs it.  Hence the lower and upper colour equations themselves attain
the `6 -> 5` bound after the other two required hole labels are assigned.
This is only an incidence-ledger witness; it is not asserted to satisfy the
B-owner degree equations, form a forest, or supply a chronology.  The
obstruction below is therefore a separate port calculation rather than a
hidden colour-count obstruction.

The bounded exact search

```text
scratch/search_k15_h19_minimal_coupled_sector_circuits.py
scratch/k15_h19_minimal_coupled_sector_circuits.audit.json
```

then tests the complete minimal architecture for rows 2, 7, and 13:

* both choices of the old 12685 occurrence;
* every possible lower-facet relay of upper colours 4028 and 2044;
* every choice of the one open hole; and
* every hole-labelled Johnson edge on the removed B-port set.

There are 11,784 relay pairs.  Across all of them the removed B-port set
contains **no** Johnson edge carrying even one of the four hole labels:

\[
 \max\{\text{supported old holes}\}=0.
\tag{14.9}
\]

Consequently there is no degree-balanced `6 old -> 5 new` BB augmenting
path whose two degree deficits are filled merely by adding the two new cross
edges while all 856 old cross edges remain fixed.

This is a sharp scoped obstruction.  It does not exclude a longer coupled
circulation that removes and reroutes old cross edges, uses additional BB
return ports, or changes more than the minimum three AA edges.  It proves
that the first viable global move must do at least one of those things.

### Theorem 14.1 (strong open-path minimum support is not attainable)

Restrict to residence-safe exact AA forests at the minimum possible AA
support distance three from H19.  Any degree-two open generalized braid with
both q1 lower decks exact up to the one unavoidable open lower hole and both
q1 upper decks complete has total sector-edge symmetric difference at least
18 from H19.  The final physical endpoints are allowed to move.

#### Proof

The independent exhaustive classification in Section 13 gives AA distance
at least three.  For every one of its 17 equality cases, the raw opposite-
lower ledger needs at least four old BB deletions and three BB additions.
The two universally forced unique-upper losses (14.4) require at least two
further old BB deletions and two additions.  Thus BB symmetric difference is
at least

\[
 6+5=11.
\]

The channel current (12.6) forces two more cross edges than H19, so cross
symmetric difference is at least two.  Therefore total distance is at least
`3+11+2=16`.

Equality 16 forces all three minima simultaneously.  The only AA rows with
BB distance 11 are 2, 7, and 13.  Cross distance two means that all 856 old
cross edges remain and exactly two new cross edges are inserted.  The first
11,784-case port audit leading to (14.9) rules out the repair when the old
endpoint degree vector is retained.

Here equality also forces the open lower hole to lie in the four-label set
`H` of old holes.  If instead `h notin H`, the raw BB current is at least
`5 old -> 4 new`; because the **path itself** must restore both unique upper
losses 2044 and 4028, two neutral relays are still required, giving BB
distance at least 13 and total distance at least 18.

Endpoint relocation cannot evade this certificate.  For a B owner `v`, let
`r_v,s_v,x_v` be respectively its removed-BB, inserted-BB, and new-cross
incidences, and let `o_v,f_v` indicate membership in the old and final
physical endpoint pairs.  Comparing old degree `2-o_v` with new degree
`2-f_v` gives the exact boundary equation

\[
 f_v=o_v+r_v-s_v-x_v.
\tag{14.10}
\]

Thus every endpoint of an inserted BB edge lies in the removed-port set
`supp(r)` or is one of the two old endpoints: outside their union the right
side of (14.10) would be negative.  Equation (14.9) says that no required
hole-labelled BB edge has both endpoints in `supp(r)`.  Therefore each of
the three required hole edges must consume an old-endpoint incidence.

For rows 2, 7, and 13 neither old endpoint is incident with a removed BB
edge, and neither contains either new A endpoint label, so `r_v=x_v=0` at
both old endpoints.  Equation (14.10) then gives `s_v<=1` at each of them.
The two old endpoints can support at most two hole edges, whereas three are
required.  This contradiction allows the final endpoints to move
arbitrarily.

The endpoint-relocation audit

```text
scratch/audit_k15_h19_distance16_endpoint_relocation.py
scratch/k15_h19_distance16_endpoint_relocation.audit.json
```

then admits the two old B endpoints as positive degree ports and allows an
arbitrary new B endpoint pair.  It tests all 23,568 choices of one old 12685
occurrence together with the 11,784 valid relay pairs.  Of these, 22,128
already overload a B owner.  The remaining 1,440 are degree-feasible before
the three required hole edges are inserted.  In 1,080 cases no required
hole has an available Johnson edge on the positive-capacity port set; in the
other 360 cases only hole 8877 does.  Thus no case supports all three hole
labels, even before connectivity, endpoint adjacency, or residence is
imposed.  The unique type of partial escape is row 2's edge
`8893--9901`, of lower colour 8877 and upper colour 9917; the other two hole
edges still have no ports.  This independently checks the boundary proof.
Distance 16 is impossible with arbitrary endpoint relocation under the
strong open-path-upper hypothesis.

Finally, in each sector the symmetric-difference parity equals the parity
of its edge-count change.  The three changes in (12.6) have parities odd,
odd, and even, so their total symmetric difference is even.  The next value
after 16 is therefore at least 18. \(\square\)

This theorem is finite and sharply scoped: it assumes minimum-distance AA
repair and requires complete upper q1 before the closing edge is added.  It
does not rule out a residence-safe braid at distance 18 or a larger AA
exchange.  It also does not close the weaker marked-cycle distance-16 class
in which a non-old-hole closure itself restores one of 2044 or 4028; that
scope gap is identified and then closed by the complete unbranched model in
`MATH_THEOREM_H19_DISTANCE18_MARKED_CYCLE_CIRCULATION_NORMAL_FORM_20260729.md`.

## 15. Exact global augmenting object left open

For completeness, an arbitrary repair can be written without relaxing the
chronology.  Let `delta_A,delta_B,delta_X` be signed incidence vectors of
removed and inserted sector edges.  A repaired B-to-B Hamilton path cut
from a quarantined four-band cycle must satisfy simultaneously:

1. the channel sums (12.6);
2. at each middle owner `v`,

   \[
   \sum_{e\ni v}(\delta_A+\delta_B+\delta_X)_e
    =1_{v\in E_{\rm old}}-1_{v\in E_{\rm new}},
   \tag{15.1}
   \]

   where `E_old={9901,7779}` and `E_new` is a Johnson-adjacent B pair;
3. AA current `-1` at duplicated label 756, while the exact non-AA target
   row is the complement of the final A-endpoint labels and the marked
   closure lower label `h`;
4. nonnegative final multiplicity at least one for every upper q1 colour;
5. one connected path, with every A run of length at least four.

Equations (15.1) are a degree-boundary flow, but the lower-colour equations
couple nonlinearly to its allowed Johnson edges and the run-length condition
is chronological.  Theorem 14.1 shows that the smallest strong-path-upper
support is not a physical flow, even with endpoint relocation.  The first
still-open possibilities in that strong scope are:

* reroute at least one old cross edge, which raises cross distance from two
  to at least four;
* use at least one additional BB return pair, raising BB distance from 11 to
  at least 13; or
* leave the 17-row minimum AA class and use a larger AA exchange.

Every remaining case begins at total distance at least 18.  A positive
construction must additionally move the final endpoint pair to a
Johnson-adjacent B pair, expand through all extreme colours to obtain the
literal four-level tight enumeration, and then pass residence, deeper-shadow,
and common-compiler audits.  No such global augmenting path is proved here.

### Theorem 15.1 (alternating-trail normal form with old crosses retained)

Suppose the old physical endpoints and all 856 old cross edges are retained,
and two new cross edges are inserted.  Let their new A endpoints be `a_1,
a_2` and their B endpoints be `b_1,b_2`.  Then any degree-two sector repair
has the following signed-difference decomposition.

1. The AA difference decomposes into red/blue alternating cycles and one
   alternating trail from `a_1` to `a_2` that starts and ends with a removed
   AA edge.  At resident AA support distance three this trail is exactly
   `old-new-old` and there are no AA cycles.
2. The BB difference decomposes into red/blue alternating cycles and one
   alternating trail from `b_1` to `b_2` that starts and ends with a removed
   BB edge.
3. The two new cross edges close the two distinguished alternating trails
   into one alternating full-deck circuit (up to the independent alternating
   cycles).

Here red means an old edge removed and blue means a new edge inserted.

#### Proof

At every A owner other than `a_1,a_2`, preservation of total degree and of
the old cross incidences gives equal removed and inserted AA degree.  At
`a_1,a_2` there is one extra removed AA incidence, compensating the new
cross incidence.  Pair red and blue half-edges arbitrarily at every balanced
owner.  At each of `a_1,a_2` leave one red half-edge unpaired.  Following the
pairings decomposes the AA symmetric difference into alternating cycles and
one alternating trail between the two unpaired ends.  Its first and last
edges are red.  Distance three forces the unique pattern red-blue-red.

The same argument on B applies because the new cross at `b_1,b_2` must be
compensated by one extra removed BB incidence there, while every other B
degree is unchanged.  Adding the blue cross edges joins the red ends of the
two distinguished trails alternately, producing the asserted circuit.
\(\square\)

Thus, under retained crosses, the remaining positive problem is literally
a coloured alternating-trail problem in the B Johnson graph, not an
independent selection of BB labels.  The 11,784-case certificate proves that
no trail decomposition of total BB length 11 carries the required lower and
upper currents for any of the three incidence-minimal AA trails.  A proof at
the next scale must produce a length-at-least-13 BB trail system, or else
leave this normal form by rerouting old crosses.

## 16. Audit provenance and exact boundary

The finite classifications in Sections 13--14 were rebuilt independently.
The frozen verifier hashes are

```text
b1efa46f656d8d22879e6f5a79bb4dc2cbb0c8929246149b270e5075a11b0f00
  scratch/audit_k15_h19_minimal_resident_aa_exchanges.py
ac8674a52c34b55c524dde87c235224ec113418369bdcf683953fa166a38d453
  scratch/k15_h19_minimal_resident_aa_exchanges.audit.json
a2ee0cb0df83e7fb16d788434fed24214fa86938bc718feb108c666d34e17ce8
  scratch/search_k15_h19_minimal_coupled_sector_circuits.py
d7baaba1dce0674555601d5b5d9df7f6d66666d22bd5731bffcf9f355656c1db
  scratch/k15_h19_minimal_coupled_sector_circuits.audit.json
5fb06b71fd8c162837affa0585e07843fd6fd11e24355d6b0cb140463b46c36b
  scratch/audit_k15_h19_distance16_endpoint_relocation.py
0eb18f0d50b0e8a8f94782b48d388e757cf2f3f6931855f9f89c2a5edd01de33
  scratch/k15_h19_distance16_endpoint_relocation.audit.json
```

No heavy search, SAT model, or H100 job was launched for this result.  The
17-row and port computations are bounded exact audits of the frozen H19
artifact.  The proved boundary is:

* global four-band chronology equivalence: proved;
* H19 nonrecognition and exact repair current: proved;
* minimum resident-AA catalogue and strong-open-path-upper distance-16
  coupled no-go: proved;
* weak marked-cycle distance 16 with a non-old-hole closure: not handled by
  this audit, but subsequently closed by the unbranched marked-cycle model;
* existence of a distance-at-least-18 endpoint-moving alternating
  circulation: open;
* old-coordinate residence, deeper shadows, common compiler, and literal
  contiguous-OR realization after such a circulation: open.
