# K16 `j3959`: minimal service blocks, the exact depth-two signature graph, and the donor-gap obstruction

Date: 2026-07-30  
Lane: K, combinatorial braid  
Status: **proved finite classification and explicit buffered post-flat path; unrestricted mixed-depth splice remains open**

## 1. Frozen input and scope

The source is

```text
scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
SHA256 edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
```

It has length `12873`, with flat starts `6433,12869,12871` (zero based).  Its five missing upper targets are

\[
  4e79\subset 6f79,
  \qquad
  ca79\subset ea79\subset eb79.
\]

This note answers three separate questions.

1. What are all minimal rank-eight blocks which supply these targets and are internally resident at depth two?
2. Which such blocks fit the physical depth-two ports of `j3959`?
3. Can the useful local ports be assembled into a literal occurrence-conserving braid?

The first two questions are solved exactly.  For the third, an explicit occurrence-conserving block order makes the entire post-flat part exact and supplies all five targets, but three depth-three donor gaps remain.  A fixed contracted atlas is proved unable to repair the first gap.  This is not a global K16 no-go.

## 2. Constant-depth residence is a finite endpoint signature

Let a binary coordinate trace run through a word at constant depth two.  Its erosion cells are the ANDs of three consecutive trace bits, and a row is reconstructed by the OR of the three erosion cells covering it.

### Lemma 2.1 (run criterion)

A finite trace is exactly reconstructed at every position whose full depth-two collar lies inside the trace if and only if every positive run closed inside the trace has length at least three.

#### Proof

A positive row is recovered precisely when it belongs to an all-one length-three window.  Every member of a positive run belongs to such a window if and only if the run has length at least three.  Zero rows are automatic because erosion cannot create a one.  Applying this independently to the sixteen coordinates proves the claim. \(\square\)

For an oriented fragment, let

\[
  S_1,S_2,S_3
\]

be the masks of coordinates whose terminal positive run has length exactly one, exactly two, or at least three.  Define \(P_1,P_2,P_3\) analogously at the beginning of the next fragment.

### Lemma 2.2 (exact two-sided port rule)

Two internally resident fragments of length at least three may be joined at depth two exactly when

\[
\begin{aligned}
S_1&\subseteq P_2\cup P_3,\\
S_2&\subseteq P_1\cup P_2\cup P_3,\\
P_1&\subseteq S_2\cup S_3,\\
P_2&\subseteq S_1\cup S_2\cup S_3.
\end{aligned}
\tag{2.1}
\]

#### Proof

If the coordinate is one on both sides, the two endpoint runs must have combined length at least three.  A terminal run of length one therefore needs an initial run of length at least two; a terminal run of length two needs at least one.  The two reverse implications are identical.  If the coordinate is zero on one side, the positive run on the other side must already have length at least three, which is also encoded by (2.1). \(\square\)

The root census used the fuller capped signature

\[
  \sigma_b=3\epsilon_b+\min\{3,\ell_b\},
\]

where \(\epsilon_b\) is the endpoint bit and \(\ell_b\) is the initial or terminal constant-run length.  This remembers zero runs as well.  Residence compatibility itself factors through the positive quotient (2.1).

Four physical rows on either side give a complete replay audit: a depth-two seam changes two erosion cells and therefore can change exactly two reconstructed rows on each side.

## 3. Complete nested-chain block census

Put

\[
H_c=\mathtt{ca79},\qquad H_e=\mathtt{ea79},\qquad H_b=\mathtt{eb79},
\qquad A=\mathtt{4a79},\qquad C_0=\mathtt{4e39},\qquad C_1=\mathtt{4d39}.
\]

Consider

\[
  M(V_0,V_1,V_2)
   =(V_0,V_1,V_2,A,C_0,C_1).
\tag{3.1}
\]

The required witnesses are

\[
\begin{aligned}
V_2\cup A&=H_c,\\
V_1\cup V_2\cup A&=H_e,\\
V_0\cup V_1\cup V_2\cup A&=H_b,\\
A\cup C_0&=4e79.
\end{aligned}
\tag{3.2}
\]

### Theorem 3.1 (exact `34560 -> 5166 -> 4866` classification)

There are exactly

\[
  8\cdot36\cdot120=34560
\]

raw ordered triples in (3.1).  Exactly `5166` are internally depth-two resident.  Their full capped two-sided signatures number exactly `4866`, with multiplicity histogram

\[
  4566\cdot 1+300\cdot 2=5166.
\]

Their positive residence signatures number `2551`.

#### Proof

The new coordinate in \(H_c\setminus A\) must lie in \(V_2\), after which one of the eight coordinates of \(A\) is omitted: `8` choices.  The new coordinate in \(H_e\setminus H_c\) must lie in \(V_1\), so one chooses seven of the other nine coordinates: \(\binom97=36\).  Similarly \(V_0\) must contain the new coordinate in \(H_b\setminus H_e\), giving \(\binom{10}7=120\).

The remaining figures are an exact exhaustive application of Lemma 2.1 to these `34560` six-row traces, followed by literal signature hashing.  The independent audit reconstructs the domains from the set equations; it does not read the earlier `5166`-block catalogue.  Its ordered resident-block digest is

```text
362f39187408f280a0003b2c2d000d0604e03a9022879d9ea9c928ae49ca2166
```

and asserts every identity in (3.2). \(\square\)

Every one of the `5166` blocks has positive suffix signature

\[
  (S_1,S_2,S_3)=(0100,0400,4839).
\tag{3.3}
\]

### Theorem 3.2 (physical `M`-port graph)

There are `6429` constant-depth-two physical cuts whose four rows on each side lie safely between the first two flats, namely cuts `6438,...,12866`.  The bipartite graph between these cuts and the `5166` blocks has:

| quantity | exact value |
|---|---:|
| physical cuts of positive degree | 34 |
| block-cut edges | 26,227 |
| full-signature-cut edges | 25,219 |
| positive-signature-cut edges | 9,842 |
| covered blocks | 4,472 |
| covered full signatures | 4,197 |
| covered positive signatures | 2,037 |

In particular the graph is nonempty.  One exact collar is

```text
be42 b742 a762 a572
  a179 a279 8a79 4a79 4e39 4d39
a53a a13b b03b b82b
```

at cut `6490`.  Direct erosion/reconstruction of the entire collar passes.

#### Proof

Apply (2.1) to the left port and the block prefix, and to the fixed suffix (3.3) and the right port.  The independent audit evaluates this finite bipartite graph and then replays the displayed collar from triple intersections. \(\square\)

This is a destination-port theorem.  It does not yet remove the six rows from their old physical positions.

## 4. Minimal `6f79` blocks form a nonseparable two-row state

The mask `6f79` has rank eleven.  A single rank-eight row cannot realize it.  If two rank-eight rows \(Y_0,Y_1\) have union `6f79`, then

\[
  |Y_0\cap Y_1|=5.
\]

Writing

\[
  I=Y_0\cap Y_1,\qquad
  A_Y=Y_0\setminus Y_1,\qquad
  B_Y=Y_1\setminus Y_0,
\]

partitions the eleven coordinates into sizes `5+3+3`.

### Theorem 4.1 (complete minimal-pair census)

There are exactly

\[
  \binom{11}{5}\binom63=9240
\]

ordered minimal blocks and `4620` classes modulo reversal.  Their full capped endpoint signatures are all distinct.

#### Proof

Choose \(I\), then the ordered three-set \(A_Y\) from the six remaining coordinates; \(B_Y\) is forced.  The first and last endpoint masks are recoverable from the full endpoint signature, so two distinct ordered pairs cannot have the same signature. \(\square\)

A two-row block is too short for its left and right tests to separate: the five common coordinates form a run of length two across the entire block.

### Lemma 4.2 (exact ternary port condition)

Let \(L\) end immediately before \((Y_0,Y_1)\), and let \(R\) begin immediately after it.  Let \(L_1,L_2\) be the exact-one and exact-two terminal positive-run masks of \(L\), and \(R_1,R_2\) the corresponding initial masks of \(R\).  Then

\[
  L\mid(Y_0,Y_1)\mid R
\]

is depth-two resident exactly when

\[
\begin{aligned}
A_Y&\subseteq L_{-2}\cap L_{-1},\\
B_Y&\subseteq R_0\cap R_1,\\
I&\subseteq L_{-1}\cup R_0,\\
L_1&\subseteq I, & L_2&\subseteq Y_0,\\
R_1&\subseteq I, & R_2&\subseteq Y_1.
\end{aligned}
\tag{4.1}
\]

#### Proof

A coordinate in \(A_Y\) occurs only in the first block row, so it needs two preceding ones.  A coordinate in \(B_Y\) needs two following ones.  A coordinate in \(I\) already has a run of length two and must be extended on at least one side.  Finally a length-one exterior run needs both block rows, whereas a length-two exterior run needs the adjacent block row.  These seven necessary conditions are plainly sufficient coordinate by coordinate. \(\square\)

Equivalently, assign each of the five coordinates of \(I\) to a left or right extension.  The resulting `32` resolved states make (4.1) separable.  Thus the correct object is a small streaming-state graph or a ternary hyperedge, not two independent ordinary seams.

### Theorem 4.3 (diagonal no-go, cross-port existence)

No one of the `9240` pairs fits both sides of any single unchanged safe depth-two cut of `j3959`.  Nevertheless the full cross-port relation is nonempty.  An explicit exact edge is

```text
4e71 c671 c879 a879
  2979 6719
ef08 cf88 cdc8 c9e8
```

using left cut `6438` and right cut `6467`.  For this fixed pair there are `141` admissible left ports, `73` admissible right ports, and `773` compatible cross-port pairs, none diagonal.

#### Proof

For each physical cut, the audit writes `6f79=I disjoint-union A_Y disjoint-union B_Y`, enumerates the \(\binom{11}{5}=462\) possible common sets and the twenty ordered splits of the complement, and applies (4.1).  The diagonal count is zero.  The displayed cross-port collar passes both (4.1) and exact triple-intersection replay. \(\square\)

So an unchanged local insertion is impossible, but an intervening rethread can in principle carry the pair.

There is also a literal source-phase obstruction to treating this as a pure depth-two splice.  In the authenticated word all three free rows \(V_0,V_1,V_2\) of every one of the `5166` blocks occur in the depth-two sector, while the fixed rows `4a79,4e39,4d39` occur uniquely at positions `3959,4620,4621`, all at depth three.  Among the `165` rank-eight subsets of `6f79`, `164` occur at depth three and only `4679` occurs at depth two.  Consequently the `9240` ordered pairs split as

\[
  9128\text{ of source type }(3,3),
  \qquad
  112\text{ of source type }(2,3),
\]

and none has both source occurrences at depth two.  Every occurrence-preserving service braid must therefore open at least one depth-three donor port.  The depth-two destination graph is necessary but cannot be a complete splice certificate.

An independent native-context graph makes this sharper.  Keep the original left context of the first row and the original right context of the second row, and test (4.1).  Exactly `933` ordered value pairs give `940` occurrence-labelled compatible arcs.  Their source-sector histogram is

\[
\begin{array}{c|r}
3\to3&898\\
\text{first flat}\to3&25\\
3\to\text{first flat}&4\\
3\to2&8\\
2\to3&5.
\end{array}
\]

There are zero \(2\to2\) arcs.  These arcs retain the two chosen native one-sided contexts; they still do not close the complementary source cuts.

### Theorem 4.4 (sharp three-row depth-two socket)

The minimum length of a `6f79` service block fitting an unchanged safe depth-two cut is exactly three.  At cut `6622` the exact collar is

```text
c74c c74a c56a e562
  2a79 6a39 4f19
e532 b532 b1b2 b19a
```

and

\[
  2a79\cup6a39\cup4f19=6f79.
\]

Neither adjacent pair suffices:

\[
  2a79\cup6a39=6a79,
  \qquad
  6a39\cup4f19=6f39.
\]

Thus all three rows are essential.  The four-row collar replay has no empty erosion and no reconstruction defect.  The lower bound three is Theorem 4.3.

This block is row-disjoint from the six-row block

```text
a179 a279 8a79 4a79 4e39 4d39
```

at cut `6490`; the two collars are disjoint, so inserting both gives an exact simultaneous depth-two destination placement for all five missing upper targets.  It adds nine rows and is not occurrence-conserving.  Its three variable rows occur natively at positions `913,4513,1633`, all at depth three, so source recharge remains unavoidable.

## 5. An explicit buffered post-flat service path

The preceding abstract edge has a stronger literal counterpart.  Cut the authenticated physical word into the following occurrence-labelled blocks (zero-based, half-open):

| name | interval | rows |
|---|---|---|
| \(Q\) | `[894,897)` | `5743 4763 4771` |
| \(P\) | `[3956,3959)` | `2c6d 287d 6879` |
| \(A\) | `[3959,3960)` | `4a79` |
| \(D\) | `[4620,4622)` | `4e39 4d39` |
| \(F_2\) | `[6538,6542)` | `da46 d946 cd46 c566` |
| \(F_1\) | `[12721,12725)` | `8f45 8f61 8f70 8f38` |
| \(L\) | `[12823,12826)` | `eb60 ea61 ca71` |

Let \(R_0,\ldots,R_6\) be the intervening unchanged fragments, and define

\[
\begin{aligned}
M&=L\mid A\mid D\\
 &=eb60,ea61,ca71,4a79,4e39,4d39,\\
N&=P\mid\operatorname{rev}(Q)\\
 &=2c6d,287d,6879,4771,4763,5743.
\end{aligned}
\tag{5.1}
\]

Consider the complete occurrence order

\[
R_0\mid R_1\mid R_2\mid R_3\mid R_4\mid R_5
\mid M\mid\operatorname{rev}(F_1)\mid N\mid F_2\mid R_6.
\tag{5.2}
\]

### Theorem 5.1 (exact post-flat braid and exact donor residue)

The order (5.2) has the following properties.

1. It has length `12873` and exactly the same physical occurrence multiset as the source.
2. Its flat starts are `6424,12869,12871`; the two tail flats remain fixed.
3. Its scalar capacity is `32167`, every horizon is in bounds, and it has no empty envelope cell.
4. From the first flat onward, the suffix of \(R_3\) and the path

   \[
   R_3^{\mathrm{post}}\mid R_4\mid R_5\mid M\mid\operatorname{rev}(F_1)
   \mid N\mid F_2\mid R_6
   \]

   has zero erosion/reconstruction defects.
5. The five literal witnesses are

   \[
   \begin{array}{c|c}
   ca79&ca71\mid4a79\\
   ea79&ea61\mid ca71\mid4a79\\
   eb79&eb60\mid ea61\mid ca71\mid4a79\\
   4e79&4a79\mid4e39\\
   6f79&6879\mid4771.
   \end{array}
   \]

6. Exactly three pre-flat joins fail, in exactly twelve rows:

   | join | lost coordinate | affected targets |
   |---|---|---|
   | \(R_0\to R_1\) | `0001` | `165b,545b,5653` |
   | \(R_0\to R_1\) | `0100` | `4778,437c` |
   | \(R_1\to R_2\) | `0010` | `6a71` |
   | \(R_2\to R_3\) | `0200` | `47c9,47a9,4f29` |
   | \(R_2\to R_3\) | `0010` | `5d31,5935,1975` |

#### Proof

Occurrence equality is a literal `Counter` equality of the two 12,873-row lists.  Every displayed witness is checked by direct interval OR.  Every post-flat seam is checked by the exact four-row depth-two replay.  The cross-seam erosion pairs, in order, are

```text
R3/R4             c006 8046
R4/R5             8c04 8a04
R5/M              eb00 ea40
M/reverse(F1)     0c38 0d30
reverse(F1)/N     0c41 0845
N/F2              4242 5042
F2/R6             4440 4420
```

The full variable-depth replay then gives precisely the twelve one-bit deficits in the table and no others. \(\square\)

The six-row buffer \(N\) is essential in this concrete lane.  If a bare pair \((X,Y)\) with \(X\cup Y=6f79\) is placed directly between the fixed tail of \(M\) and the head of \(R_6\), coordinate `2000` has left trace `000` and right trace `001`.  The pair must have pattern `10`, `01`, or `11`; these create a closed run of length `1`, `1`, or `2`.  Hence all `9240` bare pairs fail, by one coordinate alone.

## 6. The exact fixed-atlas obstruction

The construction above proves that all five service obligations are mutually compatible with residence after the first flat.  The remaining issue is source recharge.

There is already a coordinatewise return requirement at the two fixed \(M\)-source gaps.  Removing `4a79` alone shortens the depth-three positive runs of bits `0008` and `0010` from four to three, so any single return row closing that gap must contain

\[
  0018.
\tag{6.1}
\]

Removing the consecutive pair `4e39,4d39` shortens the corresponding runs of bits `0010` and `0200` to three, so a single return row there must contain

\[
  0210.
\tag{6.2}
\]

Thus residual-order extraction with no source return is impossible before any global Hall or upper-shadow test.  Moving larger source fragments or attaching different flanks can evade (6.1)--(6.2), so these are port requirements rather than global invariants.

Among the `5166` blocks of Theorem 3.1:

| test | exact count |
|---|---:|
| \(R_5\to M\) depth-two arcs | 748 |
| distinct full signatures among them | 738 |
| \(M\to\operatorname{rev}(F_1)\) arcs | 5,166 |
| direct \(M\to N\) arcs | 0 |
| \(F_2\to M\) cycle-closing arcs | 0 |

Both zeroes have coordinate certificates.  At a direct \(M\to N\) join, coordinate `0100` has trace `001|000`, a closed run of length one.  At an \(F_2\to M\) join, the `2000` trace ends with `000` on \(F_2\); every admissible \(M\) has \(V_1=1,V_2=0\) in this coordinate, so \(V_0V_1V_2\) is `010` or `110`, giving a closed run of length one or two.

Exactly `2250` of these blocks are internally valid at depth three, but none is a valid successor of \(R_0\).  Among the retained contracted blocks

\[
R_1,R_2,R_3,N,\operatorname{rev}(F_1),F_2,
\]

none is a complete depth-three successor of \(R_0\).  The original forward block

```text
Q = 5743 4763 4771
```

is the only retained valid continuation in this atlas, but it has already been consumed in reverse inside \(N\).

### Corollary 6.1 (scoped absence theorem)

The occurrence partition (5.2), even after replacing \(M\) by any of the `5166` authenticated alternatives, cannot close to an exact carrier using only its present contracted blocks.  A completion must introduce at least one new pre-flat donor buffer, use a different `6f79` provider macro which releases \(Q\), or enlarge the braid beyond this atlas.

This is architecture-specific.  It does **not** rule out an unrestricted mixed-depth buffered compound splice.

## 7. What the compatibility graph must remember

The calculation identifies the minimum honest state for the next braid theorem.  A vertex cannot be merely an endpoint mask.  It must carry:

1. the current flat phase/depth;
2. the first and last `2d` physical rows, or their exact erosion transition state;
3. the occurrence inventory, so destination gains are paired with source-gap repairs;
4. the five protected upper-witness tokens;
5. the lower Hall/compiler tokens.

At depth two, Lemma 2.2 gives ordinary edges for blocks of length at least three, while Lemma 4.2 gives a 32-state resolved hyperedge for a two-row provider.  At depth three the unresolved donor charge of (5.2) is the exact vector

\[
3e_{0001}+2e_{0100}+4e_{0010}+3e_{0200},
\]

with its twelve occurrence-labelled row demands shown above.

The sharp next lemma is therefore:

> **Depth-three donor absorber.**  Find a physical packet which replaces the use of forward \(Q\) at \(R_0\), closes the three source joins in (5.2), and returns a valid successor to the post-flat path, while preserving all old upper witnesses and creating three genuinely distinct exterior Hall neighbours.

The post-flat service problem itself is solved; the donor absorber and the lower compiler are not.

## 8. Authenticated artifacts

Independent abstract census and signature graph:

```text
scratch/audit_k16_j3959_minimal_service_blocks_and_signature_graph_20260730.py
SHA256 202f852be58bb9113c2bbe7ee40802552df760af071504333ca1f056ad5cd8fd

scratch/k16_j3959_minimal_service_blocks_and_signature_graph_20260730.audit.json
SHA256 3bc3a0b1d5ba16ca5436eca18cd493789dce0fd9c77cec293374bf0ebf0900e3
payload 83b92cc7d2f762c66f5aedfe8bb640db5dff7218769cb37d2d84889e7b9de352
```

Independent literal buffered-path replay:

```text
scratch/audit_k16_j3959_buffered_compound_path_20260730.py
SHA256 9633db75922314e76abe9160e7925414da38792a5040980dac55a45250a844a6

scratch/k16_j3959_buffered_compound_path_20260730.audit.json
SHA256 f287496a69eba173ece59727f0d5fccdf4eda5d05fbf21ac6a7ebff3b742a7df
payload 4b63acc6f459bdd6cb64ce6ab08b351414e7bb9907167010fb52106447816b23
```

The two audits are logically independent at the decisive points: the first reconstructs the `5166`-block atlas and the physical port graph from raw set equations; the second replays an explicit occurrence partition and localizes its complete residual defect.

Independent signature/source-context cross-audit:

```text
scratch/audit_k16_j3959_service_signature_graph_independent_20260730.py
SHA256 bf99d59495d7863fd15b84d2a9a361e0c2f5ab73bcf7d24379eb3ccf44f2ec8c

scratch/k16_j3959_service_signature_graph_independent_20260730.audit.json
SHA256 ebdc97473afec3f1f387e5beb10f8805bda367cd0913dd2f8a665f06c2ed6091
payload ef1e2b7d03acf7a83572f96a924ba24ea20f4ac012db2e2583b2f13e1082079b
```

This third audit reproduces the census and `34`-cut graph, gives a one-coordinate obstruction certificate for every one of the `6429` diagonal `6f79` cuts, constructs the `940` native cross-context arcs, and derives the source-return masks (6.1)--(6.2).

Its theorem-level independent audit is

```text
MATH_AUDIT_K16_J3959_MINIMAL_SERVICE_SIGNATURE_GRAPH_20260730.md
SHA256 a6463f026b6e985e93ecae92eec71844df4abcdabad349643aca2c040a2f51e6
```
