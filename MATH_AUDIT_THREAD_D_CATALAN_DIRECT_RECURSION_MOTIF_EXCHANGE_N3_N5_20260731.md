# Direct-recursion residence motifs: an immutable-sector theorem and the small-packet census

Date: 2026-07-31  
Status: exact all-parameter obstruction inside a fixed-filler strict
selection fibre;
solver-free complete census of one-shore alternating occurrence circuits of
orders at most three on the frozen child parameters `n=3,4,5`.  No no-go is
claimed for packets that change the filler or structural forest.

## 1. The forbidden motif

Orient a Johnson path as

\[
 v_{i+1}=v_i-a_i+b_i .
\]

A coordinate has trace `0110` on
\((v_{i-1},v_i,v_{i+1},v_{i+2})\) if and only if

\[
                         b_{i-1}=a_{i+1}.             \tag{1.1}
\]
It is independent of the orientation chosen for the
whole component: reversal takes `0110` to `0110`.

## 2. Exact immutable-sector obstruction

Let `F` be the structural Catalan path forest and let `G` be the independent
Catalan filler forest on the untouched `c` rail.  Let

\[
 \mathcal G(F,G,Q,S^-,S^+)
\]

be any strict direct-edgewise lift based on `F`, with filler `G`.  Here `Q`
is the common inherited-port basis and `S^-`,`S^+` are the two direct
occurrence SDRs.  By the independent-filler theorem, the entire translated
filler forest

\[
                           c+G                         \tag{2.1}
\]

is present literally.  Its edges do not depend on `Q`, `S^-`, or `S^+`.

### Theorem 2.1 (selection-fibre invariance)

If three consecutive edges of the chosen filler `G` contain a forbidden
motif, then the corresponding three edges in `c+G` contain the same motif
in every strict lift based on the same pair `(F,G)`.  This remains true
under an arbitrary, not necessarily bounded, packet that changes `Q` and
one or both direct SDRs while keeping `G` fixed.

#### Proof

The four filler vertices become

\[
 c+v_{i-1},\ c+v_i,\ c+v_{i+1},\ c+v_{i+2}.
\]

Adjoining the constant coordinate `c` changes none of the old-coordinate
traces.  All three translated edges belong to the fixed filler sector (2.1).
The variables `Q`, `S^-`, and `S^+` control only the punctured-center,
seam, and two pure-side edges.  Therefore none of the three motif edges is
removed by a selection-fibre exchange.  Equation (1.1) remains true.
\(\square\)

This is stronger than a bounded-circuit obstruction inside one fixed
filler fibre.  Once the chosen filler has one forbidden motif, **no point
of that fixed-`G` common-`Q` / two-SDR / graphic selection fibre is
residence-clean**.  It is not an obstruction to the two-parent recursion:
`G` may be chosen independently of the structural forest `F`.  A
regenerative induction may consequently use any of the following routes:

1. choose an independently residence-clean filler `G`;
2. the lift includes a nonflat actuator replacing at least one translated
   child edge of every old motif; or
3. a joint packet changes the filler Catalan forest (or the structural
   forest when another sector is defective) and then recomputes the
   affected rows.

A circuit only in the two direct occurrence matchings cannot change the
chosen filler, but the filler need not equal the structural parent.

## 3. Exact frozen-chain evidence

The authenticated strict chain is

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n5_20260731.witness.json
```

The audit reconstructs each complete ambient support and obtains

\[
\begin{array}{c|r|r|r}
\text{child }n&\text{all forbidden motifs}&
 \text{immutable motifs in frozen }c+G&\text{other/boundary motifs}\\ \hline
3&17&5&12\\
4&44&17&27\\
5&144&44&100.
\end{array}                                            \tag{3.1}
\]

The immutable counts are exactly the preceding row's residence debts, as
predicted by Theorem 2.1, because the frozen one-parent chain chose `G=F`.
Thus every retained row has a fixed-filler obstruction independent of how
the common basis and representatives are reselected.  The independent
filler theorem permits a different `G` and blocks any stronger inference.

## 4. Bounded one-shore circuit census

For additional occurrence-level evidence, fix `Q` and one shore.  Regard a
direct occurrence as an edge between its two required palette rows.  A
directed alternating circuit of order `s` replaces `s` selected occurrences
by `s` unselected occurrences and preserves both palette partitions.

The audit enumerates every such circuit for `s=1,2,3` on either shore.  For
each candidate it then rechecks, rather than assumes,

* both exact palette partitions;
* tail and head role injection;
* degree one at every seam anchor;
* preservation of the rooted condition when `c_0=0`, and otherwise no
  increase of the exact anchor-free charge;
* maximum physical degree two; and
* acyclicity of the complete three-rail support.

The exact counts are

\[
\begin{array}{c|c|r|r|r}
n&\text{shore}&\text{candidate orders}&\text{graphic-feasible}&
 \text{motif descents}\\ \hline
3&\text{upper}&1^2,3^2&2&0\\
3&\text{lower}&1^2&2&0\\
4&\text{upper}&1^{18},3^4&12&0\\
4&\text{lower}&1^{19}&12&0\\
5&\text{upper}&1^{80},3^{37}&39&0\\
5&\text{lower}&1^{69},2^3,3^6&33&0.
\end{array}                                            \tag{4.1}
\]

Every graphic-feasible packet in (4.1) is physically trace-identical: it
removes no old motif and creates no new motif.  The order-one packets are
parallel occurrence relabellings of the same physical diamond.  Nontrivial
palette circuits in this small bank are rejected by role/anchor/graphic
conditions before they produce a valid support change.

This finite statement is deliberately narrower than Theorem 2.1.  It does
not exclude:

* a `Q` exchange repairing a motif outside the frozen `c+G`;
* a simultaneous two-shore packet;
* a longer direct-occurrence circuit; or
* an alternating circuit that changes `F` or `G` itself.

It does show that the simplest proposed repair does not even begin to move
the physical chronology in the retained `n=3,4,5` rows.

## 5. The synchronized unit-`Q` packet is genuinely positive

The preceding negative census fixes `Q`, so it does not test the natural
common-basis exchange.  Let `e in Q`, `f notin Q`, and put

\[
                            Q'=Q-e+f.                 \tag{5.1}
\]

If the currently matched occurrence at `t_f` can be redirected to `t_e`
on the upper shore, and the currently matched occurrence at `h_f` can be
redirected to `h_e` on the lower shore, the two length-two alternating
paths change both SDRs to the same exposed bank `Q'`.  Together with the
two old seams at `e`, the old central edge at `f`, the new central edge at
`e`, and the two new seams at `f`, this is an exact physical `5 -> 5`
packet.

The complete theorem, including the contracted graphic/fundamental-cycle
test, is in

```text
MATH_THEOREM_THREAD_D_CATALAN_STRICT_FIVE_EDGE_PACKET_AND_MOTIF_DESCENT_20260731.md
```

The solver-free finite census exhausts every directly redirectable pair on
the same three frozen rows.  After the correction that isolated nonanchors
must be included in the rooted component universe, the exact counts are

\[
\begin{array}{c|r|r|r|r}
n&\text{redirectable}&\text{graphic-safe}&\text{strict valid}&
 \text{motif descents}\\ \hline
3&2&1&1&1\\
4&9&9&9&2\\
5&20&19&9&2.
\end{array}                                            \tag{5.2}
\]

The best motif changes are respectively `-2,-1,-1`.  At `n=5` the packet

```text
e=188 in Q  ->  f=67 outside Q
```

is a pure eliminator: it deletes the sole structural motif

```text
bit 0x100 on 0xe62,0xf42,0xf0a,0xe8a
```

and creates none.  Its full old/new physical edge ledger has five edges on
each side; both complete palettes are equal before and after; degree and
acyclicity pass; and the side anchor histograms are unchanged.  In
particular the lower histogram is

\[
                        0^2,1^{44},2^{44},             \tag{5.3}
\]

while the upper histogram is `1^48,2^42`.

For `n=3,4` a count descent exists but every improving unit packet creates
some new motif; the census contains no pure eliminator in this support-
minimal class.  This is finite evidence, not a uniform supply theorem.

The producer and independent literal replay are

```text
scratch/audit_threadD_catalan_strict_five_edge_packet_n3_n5_20260731.py
scratch/threadD_catalan_strict_five_edge_packet_n3_n5_20260731.audit.json
scratch/verify_threadD_catalan_strict_five_edge_packet_n3_n5_20260731.py
scratch/threadD_catalan_strict_five_edge_packet_n3_n5_20260731.independent.audit.json
```

The independent replay checks every retained row against literal edge
count, equality of both complete palettes, full spanning-vertex rooted
histograms, acyclicity, degree two, motif signatures and fixed-filler
invariance.  Candidate-bank exhaustiveness remains the producer census's
scope.

## 6. Sharp surviving exchange gate

For a motif wholly in fixed `c+G`, the minimum logical support of a useful
packet contains a filler-forest edge variable.  More economically, one may
choose a different guard filler before the structural rows.  The exact
two-parent gate is the tuple

\[
                  (F',G',Q',S'^-,S'^+)               \tag{5.1}
\]

such that

1. `F'` and `G'` each have the two Catalan palettes and are linear forests;
2. `G'` is clean for the required filler-residence guard;
3. `Q'` is common to the two direct pulled-back transversal systems of
   `F'`;
4. `S'^-`,`S'^+` are the corresponding direct SDRs; and
5. the complementary three-sector rooted/contracted support is acyclic and
   motif-safe.

The occurrence banks depend on `F'`, while the filler guard depends only on
`G'`.  Thus (5.1) is a two-parent **choose-filler plus
regenerate-after-structural-circuit** relation, not an alternating circuit
in one fixed matching graph.  This is the smallest noncircular induction
state consistent with Theorem 2.1 and the independent-filler theorem.

## 7. Reproducibility and scope

The solver-free program

```text
scratch/audit_threadD_catalan_derf_local_motif_exchanges_n3_n5_20260731.py
```

writes

```text
scratch/threadD_catalan_derf_local_motif_exchanges_n3_n5_20260731.audit.json
```

It uses only the frozen witness, reconstructs every physical edge, and
enumerates the complete stated circuit class.  No SAT status or random
search is used.  The result is an exact obstruction to fixed-filler
selection-fibre regeneration and exact finite evidence against one-shore
circuits of order at most three.  It is not an all-parameter no-go for
choosing an independent guard filler, structural/filler-changing packets,
or the full Catalan/RSB theorem.
