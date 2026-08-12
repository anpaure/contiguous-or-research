# Minimal asymmetric tight-enumeration repair and the common-core transfer theorem

Date: 2026-07-31  
Status: exact all-`m` local-transfer criterion; complete `m=3` distance-two
and strict six-distinct-port alternating-`C6` audit; explicit minimum
asymmetric tight enumeration and ordered four-transversal; no all-`m`
existence theorem

## 0. Verdict

The complement-symmetric no-go is escaped at the first possible larger
edge distance.  Among all `3024` complement-half-turn lower-tight Hamilton
cycles of `J(6,3)`:

* no Hamilton `C4`/2-opt exchange leaves a lower-tight cycle with occurrence
  rank `15`;
* one strict six-distinct-port alternating `C6` exchange does; the complete
  census of that subclass contains `1440` successful source-packet
  incidences.

Hence the minimum number of removed physical edges is exactly three, or
equivalently the minimum physical symmetric-difference size is six.  One
certificate is

```text
remove  11-13, 19-49, 25-41
add     11-19, 13-41, 25-49.
```

It takes occurrence rank `14` to `15`, breaks complement symmetry, retains
the cap-two load histogram `1^10 2^5` on both shores, and yields a literal
tight enumeration and a `Cat_3=5`-path ordered four-transversal.

The winning circuit is an alternating Johnson `C6`, not a standard
projected Boolean-incidence hexagon.  All `18720` lower-tight Hamilton
outputs in that strict incidence-hex subclass still have rank at most `14`.
Thus the positive local object is a general alternating circuit with an
exact common-core augmenting linkage.

## 1. Setup

Let `|Omega|=2m`, and put

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1},
\]

\[
 K=\operatorname {Cat}_m,\qquad
 N=|\mathcal L|=mK,\qquad
 M=|\mathcal X|=(m+1)K=N+K.                 \tag{1.1}
\]

For a Johnson edge `e=XY`, write

\[
             \ell(e)=X\cap Y,\qquad u(e)=X\cup Y.   \tag{1.2}
\]

For a physical edge set `R`, let `G(R)` be the bipartite occurrence graph
on `mathcal L sqcup mathcal U` containing `ell(e)--u(e)` for each `e in R`.
The pair `(ell(e),u(e))` determines `e` uniquely, so `G(R)` is simple.

If a Hamilton cycle `C` is lower-complete, choosing one occurrence of every
lower colour and subdividing those edges gives a tight cyclic enumeration
of ranks `{m-1,m}`.  If `G(E(C))` has a perfect matching, its selected
physical edges are a proper subset of `C`, hence a spanning linear forest
with exactly `M-N=K` components and an ordered four-transversal.

## 2. Exact all-`m` local-transfer criterion

Let `C,C'` be Hamilton cycles of `J(2m,m)` and put

\[
 A=E(C)\setminus E(C'),\qquad
 B=E(C')\setminus E(C),\qquad |A|=|B|=t.     \tag{2.1}
\]

Let

\[
                  G_0=G(E(C)\cap E(C'))       \tag{2.2}
\]

be the common occurrence graph, and let `G_B=G(B)`.

For a lower colour `L`, write `a_L` and `b_L` for its multiplicities among
the removed and added edges.  Define `a_U,b_U` similarly on the upper shore.

### Theorem 2.1 (palette, Hall and linkage transfer)

The following statements hold with no symmetry assumption.

1. The exact occurrence-load ledgers are

   \[
   \mu'_{\ell}(L)=\mu_{\ell}(L)-a_L+b_L,
   \qquad
   \mu'_u(U)=\mu_u(U)-a_U+b_U.                 \tag{2.3}
   \]

   In particular, the terminal cycle is lower-tight exactly when

   \[
                 b_L\ge a_L-\mu_{\ell}(L)+1
                 \qquad(L\in\mathcal L).       \tag{2.4}
   \]

2. The terminal occurrence graph has a perfect matching exactly when

   \[
   \boxed{
   |N_{G_B}(S)\setminus N_{G_0}(S)|
      \ge |S|-|N_{G_0}(S)|\qquad(S\subseteq\mathcal L).}
                                                            \tag{2.5}
   \]

3. Let `Q` be a maximum matching of `G_0`, of size `N-r`.  Orient every
   non-`Q` occurrence edge from the lower shore to the upper shore and
   every `Q`-edge backwards.  Then (2.5) holds exactly when there are `r`
   mutually vertex-disjoint directed augmenting paths whose initial
   vertices are all lower vertices exposed by `Q` and whose terminal
   vertices are all upper vertices exposed by `Q`.

4. If `d=N-nu(G(E(C)))` is the old occurrence deficiency, then every
   successful `t`-edge packet necessarily satisfies

   \[
                         d\le r\le d+t,
                         \qquad d\le t.          \tag{2.6}
   \]

   Every one of the `r` paths in item 3 uses a distinct added occurrence,
   so also `r<=t`.

#### Proof

Equation (2.3) is literal deletion and addition of occurrences, and (2.4)
is the condition that every final lower load be positive.

The terminal neighbour set is

\[
 N_{G(E(C'))}(S)=N_{G_0}(S)\cup N_{G_B}(S).
\]

Substitution into Hall's inequality gives (2.5).

For item 3, `r` vertex-disjoint `Q`-augmenting paths increase the matching
size by `r`, proving sufficiency.  Conversely, symmetric difference of `Q`
with any terminal perfect matching decomposes into alternating cycles and
exactly `r` vertex-disjoint augmenting paths joining all exposed vertices.
No augmenting path can lie wholly in `G_0`, because `Q` is maximum there;
hence each path uses a distinct edge of `G_B`.

Deleting `t` edges from the old occurrence graph lowers its matching rank
by at most `t`, while it cannot raise it.  Therefore `d<=r<=d+t`.
Adding `t` terminal edges can raise matching rank by at most `t`, so a
perfect terminal matching requires `d<=t`.  This proves (2.6).  \(\square\)

### Corollary 2.2 (fixed matching preservation)

If the old occurrence graph has a fixed perfect matching `P` and

\[
                         s=|P\cap A|,              \tag{2.7}
\]

then `P\setminus A` has exactly `s` exposed vertices on each shore.  It
extends to a terminal perfect matching exactly when the terminal occurrence
graph contains `s` vertex-disjoint augmenting paths covering those exposed
vertices.  Thus a `t`-edge physical packet exports linkage width at most
`t`; if `P\cap A` is empty, occurrence Hall is preserved automatically.

The theorem deliberately keeps physical and occurrence conditions
separate.  The new edges `B` must also reconnect `C-A` into one Hamilton
cycle.  For a multi-cycle terminal factor, a perfect occurrence matching
is not enough for a linear forest unless the selected matching omits an
edge of every physical component.

## 3. Exact finite frontier at `m=3`

The source class is the complete set of `3024` complement-half-turn,
lower-tight Hamilton cycles from the `K10` quotient audit.  Their occurrence
ranks are

\[
                         10^{864},12^{1440},14^{720}. \tag{3.1}
\]

### Theorem 3.1 (minimum symmetry-breaking distance)

Among all lower-tight Hamilton cycles `C'` and all audited sources `C`, the
minimum value of

\[
                     |E(C)\setminus E(C')|          \tag{3.2}
\]

subject to `G(E(C'))` having a perfect matching is exactly three.

#### Finite proof and completeness

Two distinct simple two-factors have even alternating symmetric difference.
They cannot differ by one removed and one added edge.  If (3.2) equals two,
the symmetric difference is one alternating `C4`, equivalently a Hamilton
2-opt.  The audit exhausts every such packet from all `3024` sources:

```text
candidate C4 packets                         131040
Hamilton terminals                            57600
Hamilton and lower-tight terminals            26640
occurrence-rank-15 terminals                       0
```

For three removed edges, it is enough for the upper bound to exhibit one
strict alternating `C6`.  The complete census of simple alternating `C6`
packets on six distinct owner ports is

```text
candidate C6 packets                        1213920
Hamilton terminals                           650880
Hamilton and lower-tight terminals           234720
occurrence-rank-15 terminals                    1440
```

The zero-change case is excluded by (3.1), one removed edge is impossible
for distinct simple two-factors, and the complete `C4` census excludes
distance two.  Section 4 supplies a distance-three witness.  Hence the
minimum is exactly three.  This minimum proof does not require the strict
`C6` census to cover repeated-owner, degree-four alternating closed trails
at distance three.  \(\square\)

The strict projected Boolean-incidence-hex subclass contributes `18720`
lower-tight Hamilton packet rows.  Their rank transitions are

\[
10\to10:2160,\quad10\to11:4320,\quad
12\to11:1440,\quad12\to12:6480,\quad
14\to13:3600,\quad14\to14:720.                \tag{3.3}
\]

Thus no standard incidence hex succeeds.  The extra generality of an
arbitrary alternating Johnson `C6` is essential already at `m=3`.

## 4. Literal minimum packet

Take the complement-half-turn source

```text
7 11 13 44 14 26 25 41 35 42
56 52 50 19 49 37 38 22 28 21.
```

It has occurrence rank `14` and cap-two load histogram `1^10 2^5` on both
shores.  Toggle the alternating circuit

\[
11\mathrel{-}13\mathrel{+}41\mathrel{-}25
  \mathrel{+}49\mathrel{-}19\mathrel{+}11,       \tag{4.1}
\]

where minus edges are removed and plus edges are added.  The target cycle is

```text
7 11 19 50 52 56 42 35 41 13
44 14 26 25 49 37 38 22 28 21.
```

It is asymmetric, lower- and upper-complete, retains load histogram
`1^10 2^5` on each shore, and has the perfect occurrence matching

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
L&3&5&6&9&10&12&17&18&20&24&33&34&36&40&48\\ \hline
U&15&23&54&45&30&46&57&51&29&27&53&43&39&58&60.
\end{array}                                           \tag{4.2}
\]

The common graph after deleting the three old occurrences has rank `13`.
One maximum common matching is

\[
\begin{split}
Q=\{&(3,15),(5,23),(6,54),(10,30),(12,45),(18,51),
       (20,29),\\
    &(24,27),(33,53),(34,43),(36,39),(40,58),(48,60)\}.
\end{split}                                           \tag{4.3}
\]

The three added occurrence pairs are

\[
                         (3,27),\ (9,45),\ (17,57).  \tag{4.4}
\]

They enable the two disjoint augmenting linkages

\[
 L_9-U_{45}-L_{12}-U_{46},\qquad
 L_{17}-U_{57}.                                      \tag{4.5}
\]

The third new occurrence `(3,27)` is unused by (4.2); it pays physical
cycle and palette legality.  This explicitly exhibits the separation
between local Hall service and the rest of an alternating packet.

The selected physical forest has the five paths

```text
11-7-21-28
13-41
19-50
22-38-37-49-25-26-14-44
35-42-56-52.
```

Subdividing its fifteen selected cycle edges by their lower colours gives
the literal tight cyclic enumeration

```text
7 3 11 19 18 50 52 48 56 40 42 34 35 41 9 13 44 12
14 10 26 24 25 17 49 33 37 36 38 6 22 28 20 21 5.
```

It lists all twenty rank-three owners and all fifteen rank-two colours
exactly once and has cyclic Hamming length `40=2M`.  Thus the packet does
not merely repair a marginal graph: it produces an actual asymmetric tight
enumeration and the ordered four-transversal encoded by (4.2).

## 5. All-`m` implication and exact boundary

For any proposed alternating `C_(2t)` packet in any dimension, the complete
local certificate is now:

1. the load inequalities (2.4), and their upper analogues when desired;
2. physical Hamilton reconnection of `C-A` by `B`;
3. a complete common-core augmenting linkage of width `r<=t`.

When these hold, the terminal perfect occurrence matching selects a
spanning `Cat_m`-path forest and hence an ordered four-transversal.  This is
a polynomially checkable sufficient-and-necessary criterion for a supplied
packet.

What is **not** proved is an all-`m` supply theorem for packets meeting
these conditions.  In particular, neither complement symmetry nor strict
Boolean-incidence hexagons suffice.  The positive `m=3` fixture shows that
allowing a general alternating `C6` is enough at the base and identifies
the exact recursive state that must be exported: palette slack, physical
reconnection, and a bounded common-core linkage.  Residence, deeper shadow
coverage, compiler chronology, and the full `nu=B` implication are outside
this theorem.

## 6. Reproducible audits

Primary complete census:

* `scratch/audit_ad_m3_asymmetric_switch_frontier_20260731.py`,
  SHA-256 `ea38edfda300d8708e464c53d90994e422f4673747fb3395147e347703272fcf`;
* `scratch/ad_m3_asymmetric_switch_frontier_20260731.audit.json`,
  SHA-256 `c6a8f419732bda6f16b2ff3745a40811fbef3bfcd43f650b9ac11e168b012898`,
  payload `2189a8581c695843a2245db6586719c92290f70f0abca1d8775ac4cbe2566123`.

Independent source reconstruction, complete `C4` replay, literal packet,
linkage, tight-enumeration and ordered-four-transversal replay:

* `scratch/verify_ad_m3_asymmetric_switch_frontier_20260731.py`,
  SHA-256 `6e1997f9c3c02e96bd20dac8860b60dd28ea0429cfd5acf6e275bcce26be32b7`;
* `scratch/ad_m3_asymmetric_switch_frontier_20260731.independent.audit.json`,
  SHA-256 `25acdfdd3fc70a091c2c08dd9834d18b714cda05675b18b6ceca1de578f97041`,
  payload `585d97661009eae205331d2d878ef5df673008f0a2396f1cdb4d0b07e147d062`.

The primary audit is complete for all one-`C4` packets and all simple
six-distinct-port alternating-`C6` packets from the `3024` source cycles.
It does not enumerate distance-three alternating closed trails with a
repeated owner of symmetric-difference degree four.  The independent audit
re-enumerates the entire `C4` frontier and replays the positive `C6`
certificate; it does not independently repeat all `1,213,920` strict `C6`
candidate rows.
