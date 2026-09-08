# Root audit: `b268` activated-Hall Benders and the protected `438` Pareto table

**Date:** 2026-08-02  
**Status:** exact finite positive theorem and exact optimization oracle on the
declared protected `b268` LLR face.  The terminal strict-Pareto checkpoint of
the radius-one chain is a protected `438`-transfer table with socket tuple
`(3102,2259,1843,3518)` and generalized supplier rank `16813/16898`.
This is not a common occurrence-labelled state, chronology,
compiler, or `k=17` word.  The second socket phase is still a transported
opening marginal, not an authenticated private phase.

## 1. Common-parent face

The target parent is the authenticated private-bank materialization

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  scratch/k17_phase0_retained_witness_private_basis_20260802/
    private_h_outer_materialized.tsv
```

The transfer catalogue was generated after deleting every edge meeting any
of the `7,213` physical row addresses in the ticket bank.  Its exact ledger is

```text
protected structural edges                 93,234
native phase-0 marginal-positive edges      23,342
transported phase-1 marginal-positive       25,173
positive in both phases                     11,893
maximum row-disjoint common matching           464
```

The load-bearing hashes are

```text
30fac2b299c353446024a83fb93525d66e6b6720eacbd1895db68c5544598c89
  b268_llr.protected.all_edges.tsv
c5c4e00f35e5300e02274142d05252fb122d9e4156e4fdca44b14e887bc08859
  b268_llr.protected.native_phase0.tsv
637a046bf5ed7552b204e3727b9693ef71442538f39547b51ba7140dba4203fe
  b268_llr.protected.transported_phase1.tsv
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
  selected_tickets.tsv
```

## 2. Exact activated-Hall master

For every common transfer edge `e`, let `z_e` say that it is selected.  The
row equations

\[
  \sum_{e\ni v} z_e\le 1
\]

make the selected transfers a row-disjoint matching.  Every incident row has
one old state and one edge-labelled state for each incident transfer.  Host
states must remain edge-labelled because the new `LLR` bottom is the donor's
lower target.

For a mode-labelled deficient head set `X`, exact supplier mode `sigma`, and
head mode `tau`, the primitive predicate is recomputed literally from the
row flags.  Bidirectional Tseitin ANDs activate the compatible primitive
incidences, and a bidirectional OR defines whether supplier identity `u` is
a neighbour of any active occurrence in `X`.

For requested supplier deficiency at most `k`, the exact Benders row is

\[
 \sum_{h\in X} a_h(z)-\sum_u n_{X,u}(z)\le k.              \tag{2.1}
\]

Fixed active modes are handled as Boolean constants, not CNF variable zero.
An inactive mode-labelled head pays one unit on the right side of the
cardinality form of (2.1).  Every master candidate is materialized, its full
`6/9/4` supplier graph is rebuilt, and a fresh maximum matching plus
alternating DM shore supplies the next exact cut.

SAT candidates need no proof.  If a master reports UNSAT, the same frozen CNF
is rerun under Kissat with textual DRAT and accepted only after an independent
`drat-trim` replay.  Thus SAT is certified by literal materialization and
matching replay; UNSAT is proof-producing.

The implementation is

```text
d0e736ce16682ab7c5afba6e6a2a51c4e3e33d2dcf42780c20c163d994473572
  scratch/solve_k17_llr_supplier_benders_20260802.cpp
```

It supports both a declared edge subface and all `11,893` common edges, a
minimum transfer-cardinality floor, compact exact binary cardinality for that
floor, and small unary support counters for Hall shores.

## 3. Strict `438` table

Starting from the protected `437` table of the DM-descent audit, global common
edge `57336` is row-disjoint from the incumbent and enters donor row `16316`.
Adding it first gives supplier deficiency `96`.  A proof-safe radius-one
selector then removes global edge `41` and adds global edge `89826`.  The swap
preserves all four complete DNF counts and raises supplier rank by one.  The
retained table has

```text
selected transfers                       438
phase-0 positive short roles             3098
transported phase-1 positive             2253
positive in both phases                  1839
positive in either phase                 3512
supplier rank                      16803/16898
supplier deficiency                        95
zero supplier heads                        80
maximum-deficiency shore               109/14
```

Against the `b268` baseline

```text
(phase0,phase1,both,either,supplier)
  = (2687,1891,1422,3156,16796),
```

the coordinatewise gain is

\[
                  (+411,+362,+417,+356,+7).                \tag{3.1}
\]

The final selected list, table, and projection audit have hashes

```text
d6dca87229b542481f4f686f851c15700939db9b952cd26ce9df3b47d19bb8f0
  radius1_def95.selected.tsv
ae44aebdae38c0ca5cb5d76ab2a6a305a67b52f17b4e395a3aedbd3d97300374
  radius1_def95.table.tsv
54ec235f807cdc73ce09f1b42fa8639b1f10820f0c9aea5e2f54fbf164d733ae
  radius1_def95.projection.audit.json
```

An independent invocation of the activated-Hall driver rebuilt the table
byte-for-byte and returned

```text
FACE scope=all common_edges=11893 protected_rows=7213
ITER 0 transfers=438 supplier=16803/16898 def=95 shore=109/14
PASS_BENDERS supplier=16803 deficiency=95 iter=0
```

Hence (3.1) is not a sum of marginal edge scores: both complete DNF tables and
the full supplier maximum matching were replayed after materialization.

## 4. Monotone radius chain and terminal strict-Pareto point

Starting from the deficiency-`97` protected table, a locked radius-one
controller repeatedly solved the exact activated-Hall decision on the face
of one dropped and one added common edge.  Each accepted table retained
exactly `438` transfers, preserved all `7,213` protected rows, did not decrease
any of the four complete DNF counts, and increased supplier rank by one.

The accepted supplier checkpoints were

```text
deficiency   rank    zero heads   maximum shore
    97       16801       82          111/14
    96       16802       81          110/14
    95       16803       80          109/14
    94       16804       79          108/14
    93       16805       78          107/14
    92       16806       77          106/14
    91       16807       76          105/14
    90       16808       76          104/14
    89       16809       75          103/14
    88       16810       75          101/13
    87       16811       74          100/13
    86       16812       73           99/13
    85       16813       72           98/13
```

The deficiency-`85` endpoint has the exact tuple

\[
 (P_0,P_1,P_{\cap},P_{\cup},r_{m supplier})
   =(3102,2259,1843,3518,16813),                            \tag{4.1}
\]

so its gain over `b268` is

\[
                  (+415,+368,+421,+362,+17).               \tag{4.2}
\]

Its frozen hashes are

```text
0fb9a812e0afd7e9590d6ba690d2c3d7bee3f15a9462e3236b784a17de48b59f
  def85 selected.tsv
ea0e8803b666dd51e4e5b073e50938ca5c508f3c2d7066f04ec2a0bd9f083aa8
  def85 table.tsv
038739aa6dad705ce48ac0aee0fba80d3eacd858dcf9c7de8a255e44a4460637
  def85 projection.audit.json
18e6ebc3027350918c5e6c463d812fafaeb18f96a215870265c075c677c495ca
  def85 native_phase0.dnf.tsv
897d934d5463b7830a291fd9b72ca9b80731cdbeae95d7b69e652566435fc8df
  def85 transported_phase1.dnf.tsv
```

The activated-Hall driver independently rebuilt the deficiency-`85` table
byte-for-byte and replayed supplier rank `16813` and shore `98/13`.

The next radius decision did find a supplier-improving deficiency-`84` table,
but its two complete phase counts were `(3100,2257)`, down from
`(3102,2259)`.  The locked controller therefore rejected it and stopped.
Accordingly, deficiency `85` is the terminal point of this **strict socket-
monotone radius-one chain**, not a proof that every protected `438` table has
supplier deficiency at least `85`.  Wider exchanges or an objective allowing
temporary socket loss remain open.

During development, one target-`95` output path was accidentally opened by
two matching processes.  That run was frozen as `UNKNOWN`, all exact matching
process groups were stopped after cmdline checks, and none of its output was
used.  The contaminated CNF itself had SHA-256
`9d89529f7a464bd89d3921e277ead19e85aa91e1909e230bf3216b5e3a0f8373`.

## 5. Exact scope

This closes a real common-target-parent correlation: one protected table
simultaneously improves both measured socket marginals, their intersection
and union, and the exact supplier matching.  It does not yet prove

* the residual complete outer matching after the transfers;
* one occurrence-labelled state shared by the two phases;
* that the transported phase-1 opening belongs to the same carrier;
* chronology, residence, complete upper shadows, common cap, lower compiler;
* a length-`24313` word or any improved upper bound for `nu(17)`.
