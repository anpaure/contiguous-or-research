# Hall 19 candidate c0440: exact root migration, literal common-word readiness, and the exhausted direct Hall-18 neighbourhood

Date: 2026-07-28  
Lane: H  
Status: proved finite theorem with an explicit restricted no-go  

## 1. Conclusion

The priority neutral braid

\[
   c0440=\operatorname{FR}(3814,4556,5539)
\]

does **not** produce Hall deficiency 18.  It does, however, prove a useful
physical statement which the abstract profile census alone did not imply:
on the old root-960 target shore it creates a second occurrence of the
native child 9152, and either occurrence can be shrunk to 960 under one
literal nonempty controller word while retaining all 497 native target
types of the former positive DM shore after relocation.

This is exactly cancelled globally by root migration.  The old
\(161/160\) component rooted at 960 disappears, while a new \(25/24\)
component rooted at 9104 appears.  The two shores intersect in only the
single target 13264.  The new component has twelve raw root ports, but every
one consumes its unique native child; it has no duplicate-backed,
all-native-reserve-preserving root ear.

The complete protected one-braid neighbourhood of c0440 was scanned on the
H100 CPU.  Among 7,301 Hall-scored move descriptions its minimum deficiency
is 19.  The secondary candidate c0520 has the same restricted no-go among
7,304 scored descriptions.  Thus a continuation which keeps the migrated
root-9104 component must use an interacting/two-stage or larger braid to
supply a companion child while preserving the exterior.  A global route
which migrates or replaces a different DM component remains open.

## 2. Frozen data and notation

For \(k=15\), let

\[
 W=\binom{15}{8}=6435,\qquad P=W+3=6438,
 \qquad |\mathcal I_{\le7}|=16383.
\]

A carrier is a Johnson path
\(T=(T_0,\ldots,T_{W-1})\) through the rank-eight layer.  Its maximal
depth-three controller is

\[
 E_p=\bigcap_{i=\max(0,p-3)}^{\min(W-1,p)}T_i,
 \qquad 0\le p<P.
\]

For a compiler cell \((d,s)\), where \(0\le d\le2\), its native trace is

\[
 \tau_E(d,s)=\bigcup_{p=s}^{s+d}E_p.
\]

The compiler incidence graph joins a lower target \(S\) to \((d,s)\) when
some nonempty word \(Q\le E\) reconstructs every central window

\[
 T_i=Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3}
 \tag{2.1}
\]

and has \(\bigcup_{p=s}^{s+d}Q_p=S\).  Its Hall deficiency is

\[
 16383-\nu(G_T).
\]

The frozen carriers are

| label | move | SHA-256 | Hall/zero | DM shore |
|---|---|---|---:|---:|
| c0440 | `FR(3814,4556,5539)` | `a51f8631a9b2394405b8304c949bf9606d3b43f897f51ad9474de725df34584a` | 19/6 | 380/361 |
| c0520 | `RF(688,2636,2650)` | `897ab99092552874c0b66203bc4bbe1a4e4b68e349d58521b53ebf21dd126c39` | 19/6 | 485/466 |

The materialized files are respectively

```
scratch/k15_h19_neutral_c0440_fr3814_4556_5539.json
scratch/k15_h19_neutral_c0520_rf688_2636_2650.json
```

The freeze and remote-scan provenance is in
`scratch/k15_h19_c0440_c0520_freeze_manifest_20260728.json`.

## 3. Exact focal migration theorem

### Theorem 3.1

Let \(T\) be the frozen Hall-19 base carrier and let \(T'\) be c0440.
Then:

1. `FR(3814,4556,5539)` materializes \(T'\) exactly.  Both words contain
   every rank-eight state exactly once, are Johnson paths, and have no
   internal coordinate run shorter than four.
2. Every upper rank \(8+q\), \(1\le q\le7\), remains completely supported.
   The lower-hole vectors of \(T,T'\) are respectively
   \[
      (4,18,11,1,0,0,0),\qquad(4,18,13,1,0,0,0).
      \tag{3.1}
   \]
   In particular immediate-lower support remains at four holes, while the
   depth-three lower support loses two colours.
3. Both compiler graphs have matching number 16364, hence deficiency 19,
   and both have six zero-degree targets.  Their positive DM shores are
   \(516/497\) and \(380/361\).
4. The base root-960 DM component has type \(161/160\).  In \(T'\), the
   fixed 161-target shore has 161 neighbouring cells and matching rank 161.
5. The canonical child DM decomposition has no root-960 component.  It has
   instead a root-9104 component of type \(25/24\).  The two focal target
   shores intersect only in target 13264.
6. On the fixed old shore, the restricted profile \(\{960,9152\}\) occurs
   once in the base, at cell 6053, and twice in c0440, at cells 4800 and
   6053.  Thus its signed multiplicity gain is exactly one.

### Proof

The carrier transformation is evaluated by the explicit signed-block map
for `FR`; comparison of all 6,435 output entries with the frozen child gives
equality.  Rank, distinctness, Johnson adjacency, residence, and every
upper/lower support count are then literal set operations on the frozen
word.  The upper support sizes are

\[
 5005,3003,1365,455,105,15,1,
\]

the full binomial layer sizes.

For the compiler claims, construct every depth-0, depth-1, and depth-2 cell
from the maximal controller, form its exact target neighbourhood, and run
an integral bipartite maximum matching.  Alternating reachability from the
unmatched targets gives the canonical DM components.  This gives the
matching and shore numbers in items 3--5.

Finally restrict every physical cell neighbourhood to the old 161-target
shore.  The base and child restricted-profile counters differ at
\(\{960,9152\}\) by \(+1\).  The complete physical rows are exactly

\[
  \text{base}:\{6053\},\qquad
  \text{child}:\{4800,6053\}.
\]

Both rows have depth zero, envelope and native trace 9152, mandatory mask
576, and restricted shore \(\{960,9152\}\).  The induced matching ranks
are 160 and 161.  This proves every assertion.  The independent checker is
`scratch/audit_k15_h19_c0440_root9104.py`; its output is
`scratch/k15_h19_profile_20260728/audit_k15_h19_c0440_root9104.json`.
\(\square\)

## 4. Literal common-word root-960 theorem

### Theorem 4.1

For either \(s\in\{4800,6053\}\), define

\[
 Q^{(s)}_p=
 \begin{cases}
   960,&p=s,\\
   E_p,&p\ne s.
 \end{cases}
 \tag{4.1}
\]

Then:

1. \(Q^{(s)}\) is nonempty and satisfies every one of the 6,435 central
   equalities (2.1).
2. The depth-zero cell at \(s\) has trace 960.  The other member of
   \(\{4800,6053\}\) retains trace 9152.
3. One occurrence of every one of the 497 native targets in the entire
   frozen \(516/497\) positive DM shore can be selected on distinct cells
   under the same word,
   together with the new root-960 cell.  Thus c0440 has a literal
   498-pin common-word witness on the former 516-target shore.
4. More strongly, all 520 target types in the union of the 160 nonroot
   targets of the old root-960 component and the 361 canonical child-DM
   native targets survive simultaneously; these sets overlap in one target.
   Together with root 960 this gives 521 distinct target types under the
   same word.
5. This is not fixed-cell preservation.  With \(s=4800\), only 369 of the
   497 frozen base target/cell pairs remain exact on their original cells;
   with \(s=6053\), only 368 do.  All 497 target types survive only after
   relocating the failed pins.

The two word hashes are

\[
\begin{array}{c|c}
s&\operatorname{SHA256}(Q^{(s)})\\ \hline
4800&\texttt{d4a366e3037bb702f02b369af41acf3da160935a9a9421c1fa94722b0780855c}\\
6053&\texttt{746bf0bd9048dac284793196585e734e55b90f8e1354c630402a4547b919d590}
\end{array}
\]

### Proof

At both exceptional positions, \(E_s=9152=960\cup\{8192\}\), so (4.1)
deletes precisely mask 8192 and remains nonempty.  All central windows not
meeting \(s\) are unchanged.  The four possibly affected starts are

\[
 4797,4798,4799,4800
\]

or

\[
 6050,6051,6052,6053.
\]

Direct union in each of these windows still equals its prescribed middle
state.  Hence (2.1) holds everywhere.  The exceptional depth-zero trace is
960 by construction, and the companion 9152 occurrence is disjoint from
the changed position.

For every protected native target, enumerate all cells whose native trace
has that target value and retain those whose trace under \(Q^{(s)}\) is
still exact.  Every one of the 497 base types and every one of the stated
520 union types has a survivor.  Distinct target values necessarily use
distinct physical cells, because one cell has one trace under a fixed word.
The exact selected-pin hashes and the fixed-cell failure lists are frozen in
`scratch/k15_h19_c0440_fixed_physical_readiness_audit.json` and independently
reconstructed by
`scratch/audit_k15_h19_c0440_fixed_readiness_independent.py`.
\(\square\)

## 5. Why this readiness does not lower Hall deficiency

### Theorem 5.1

For either word in Theorem 4.1, use the explicit deterministic surviving-pin
injection frozen by the audit.  The following relaxed incidence residuals
for those selected cells are exact:

1. Reserve the 160 old-shore nonroot pins and the new root-960 pin, and
   delete the 161 old-shore targets.  The remaining 16,222 targets have
   maximum matching rank 16,203.  Hence the total is
   \[
       161+16203=16364.
       \tag{5.1}
   \]
2. Reserve relocated pins for all 497 frozen-base native targets together
   with root 960, and delete the full 516-target frozen positive DM shore.
   The remaining 15,867 targets have maximum matching rank 15,866.  Hence
   \[
       498+15866=16364.
       \tag{5.2}
   \]

These residual ranks are computed in the candidate compiler incidence
graph after deleting the reserved cells.  Exterior edges are **not** claimed
to coexist under \(Q^{(s)}\); consequently (5.1)--(5.2) are relaxed upper
bounds on a literal common-word extension.  In particular neither witness
reaches the Hall-18 threshold 16,365.

### Proof

Delete the stated target and selected cell sets from the exact candidate
incidence graph and run integral bipartite maximum matching.  The ranks are
16,203 and 15,866 for both displayed injections.  Any exterior matching
realizable under the forced word with that injection is a subgraph matching
of this relaxed graph, so it cannot have larger rank.  Adding back the
already reserved distinct pins gives (5.1)--(5.2).

For the two full-base injections, the selected-pin hashes are respectively

```
cef5cc9d14601da7dc59363198ef89d0806ccc203586d153c5b2d206c27ed704
87023bbf2d09047c933c8a30125059acf08ebd29714b218f92cd875db67da0ad
```

The equality values are asserted only for the frozen selected injections,
not for every possible relocation of the same target types.  Nevertheless
the global matching number 16,364 implies the universal upper bounds
16,203 and 15,866 for *any* disjoint 161-pin or 498-pin injection on the
same deleted target shores: a larger residual would combine with the pins
to give a matching larger than 16,364.  \(\square\)

The theorem pinpoints the cancellation: the old fixed shore becomes
saturated, but the global canonical defect migrates rather than disappears.

## 6. The fixed-component root-9104 portal

### Theorem 6.1

The canonical c0440 component rooted at 9104 is a \(25/24\) native basis.
Its 24 native children each have exactly one physical native occurrence.
There are twelve raw child-to-root sockets.  Shrinking any one of them to
9104 preserves every central window **after releasing that child's unique
native pin**, but:

\[
 \text{number of duplicate-backed, all-24-native-pin-preserving sockets}=0.
 \tag{6.1}
\]

Thus the component has twelve rank-neutral basis pivots and no certified
rank-gaining ear.

### Proof

The DM cell traces are 24 distinct targets in the 25-target shore, leaving
only 9104 exposed.  For each child occurrence adjacent to 9104, intersect
the controller letters on its cell with 9104 and check the affected central
windows.  Exactly twelve pass.  Requiring the original child target as well
fails in every case because its occurrence is unique; there is no distinct
companion cell.  A simultaneous common-word check therefore gives twelve
central-safe release-and-replace pivots and zero reserve-preserving rebases.
The full socket table is in the output cited after Theorem 3.1.  \(\square\)

Consequently, within the twelve audited root-9104 ports, the smallest local
positive object is one two-for-two (or larger) controller circuit which
retains all 24 native children and adds a 9104 cell.  To prove incidence
Hall 18 by this fixed-component strategy it must coexist with an exterior
matching of size 16,340 on targets and cells disjoint from this 25-target
component; the physical compiler additionally requires every one of those
16,365 edges under the same word, as stated in Section 9.

## 7. Exhausted direct one-braid theorem

Write a carrier as \(A|B|C|D\), with fixed global endpoints.  The direct
catalogue consists of every endpoint-compatible transformation

\[
\begin{array}{ccl}
\mathrm{FF}&:&A|C|B|D,\\
\mathrm{RF}&:&A|\overleftarrow C|B|D,\\
\mathrm{FR}&:&A|C|\overleftarrow B|D,\\
\mathrm{RR}&:&A|\overleftarrow C|\overleftarrow B|D,
\end{array}
\tag{7.1}
\]

where RR is represented by reversal of one interval.  A description is
Hall-scored only after it passes:

1. Johnson endpoint compatibility;
2. depth-three residence;
3. complete upper support in every depth \(1\le q\le7\);
4. at most four immediate-lower holes.

### Theorem 7.1

The complete catalogue (7.1) has the following exact census of move
descriptions.  Different descriptions are not asserted to materialize
distinct carrier words; degenerate singleton RR descriptions are included.

| carrier | Johnson descriptions | resident | upper-safe | Hall-scored |
|---|---:|---:|---:|---:|
| c0440 | 549,329 | 12,021 | 9,202 | 7,301 |
| c0520 | 548,467 | 11,956 | 9,165 | 7,304 |

No scored move from either carrier has deficiency at most 18.  The complete
c0440 score histogram is

\[
\begin{array}{c|r}
(H,z)&\#\\ \hline
(19,6)&7124\\
(19,7)&1\\
(20,6)&115\\
(20,7)&6\\
(21,6)&44\\
(21,7)&1\\
(22,6)&6\\
(23,6)&4
\end{array}
\]

and the c0520 histogram is

\[
\begin{array}{c|r}
(19,6)&7124\\
(19,7)&2\\
(20,6)&115\\
(20,7)&8\\
(21,6)&44\\
(21,7)&1\\
(22,6)&4\\
(23,6)&5\\
(24,6)&1.
\end{array}
\]

### Proof

For each cut \(a\), the scanner traverses every Johnson-neighbour choice for
the two new internal ports and accepts precisely the closing-port adjacency
conditions for the four orientations (7.1).  Thus each endpoint-compatible
description occurs in the loop.  Residence and upper support need inspection
only in windows meeting an old or new seam; the program nevertheless
recomputes the corresponding exact local deltas.  Every surviving move with
at most four immediate-lower holes is materialized, its complete compiler
graph is constructed, and an integral maximum matching is computed.

The terminal summaries and complete score histograms give the displayed
counts.  Both processes returned zero, and neither output contains an
`EMIT` line or a histogram entry with \(H\le18\).  Source rebuilt with

```
g++ -O3 -march=native -std=c++20
```

has the exact executed-binary hash

```
2ddea75b76e2dfae40b382ceea9c8669dab47f3cc1dc0cd5e725fa3b192fe376
```

and the scanner-source hash is

```
889379685f55e1938f24fceffd889951332966fe547021874b5482b1c2fa7d29
```

The two frozen result/output hashes are listed in the freeze manifest.
\(\square\)

### Scope audit

This is a no-go only for one fixed-endpoint FF/RF/FR/RR move satisfying all
four protected predicates immediately.  It does not exclude a
neutral-plus-improving pair, a four-or-more-block braid, a global
rethreading, or a route which temporarily loses residence, upper support,
or the four-hole bound before restoring it.

The scheduler used for the run records the first `BEST` line rather than the
last.  That generic parser defect is harmless here: each of these two
outputs contains exactly one `BEST` line, and the complete histogram itself
has minimum Hall value 19.

## 8. Secondary candidate c0520

The candidate

\[
 c0520=\operatorname{RF}(688,2636,2650)
\]

replaces the old \(321/319\) root-8216 core by a compressed canonical pair:
a \(129/128\) component rooted at 8217 and a \(161/160\) component rooted at
8218.  Their union has size \(290/288\), so this is a \(31/31\) contraction,
not a literal partition of the old target shore.  It is defect-neutral, and
the global matching number remains 16,364.  Its total positive DM shore is
\(485/466\).  By Theorem 7.1, no further direct protected move in the same
catalogue lowers its deficiency below 19.  It remains a secondary
multistage-router seed, not a direct Hall-18 carrier.

## 9. Sharp remaining theorem

The following is the sharp sufficient gate which retains the current c0440
DM decomposition.  It is not necessary for every conceivable global
rethreading, since a larger braid may migrate or replace the root-9104
component itself.

> **Root-9104 interacting-ear gate.**  Construct a shadow- and
> residence-safe rethreading of c0440, outside the exhausted one-braid
> catalogue, with a target/cell matching of size 16,365 that uses all 25
> targets of the root-9104 component and 16,340 exterior targets, together
> with one nonempty controller word which realizes every edge of that
> matching.

The twelve raw ports from Theorem 6.1 are the exact local entrances for this
fixed-component strategy.  Each
currently loses one of the 24 native children, so the minimal *local*
replacement is a duplicate-child creation or a closed two-for-two controller
circulation retaining all 24 children.  That local replacement must then be
lifted to the same common word as the 16,340 exterior edges.  The old
root-960 ear is a proved physical readiness witness, but it cannot substitute
for this migrated canonical gate.

## 10. Audit artifacts

Primary frozen artifacts:

```
scratch/k15_h19_c0440_c0520_freeze_manifest_20260728.json
scratch/k15_h19_c0440_direct_h18_result.json
scratch/k15_h19_c0440_direct_h18_scan.out
scratch/k15_h19_c0440_direct_h18_scan.err
scratch/k15_h19_c0520_direct_h18_result.json
scratch/k15_h19_c0520_direct_h18_scan.out
scratch/k15_h19_c0520_direct_h18_scan.err
```

Common-word and focal-migration audits:

```
scratch/audit_k15_h19_c0440_root960_common_q.py
scratch/audit_k15_h19_c0440_root9104.py
scratch/k15_h19_profile_20260728/audit_k15_h19_c0440_root9104.json
scratch/score_k15_h19_physical_readiness.py
scratch/k15_h19_c0440_fixed_physical_readiness_audit.json
scratch/audit_k15_h19_c0440_fixed_readiness_independent.py
scratch/audit_k15_h19_c0440_fixed_readiness_independent.json
```

No SAT, Kissat, or exhaustive job was run on the local Mac.  The exhaustive
one-braid scans ran on the H100 host's CPU.  The local work consisted only
of frozen-artifact inspection, exact postprocessing, and documentation.
