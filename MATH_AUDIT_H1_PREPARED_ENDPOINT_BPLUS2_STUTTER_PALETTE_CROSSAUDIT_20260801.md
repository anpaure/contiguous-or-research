# Cross-audit of the prepared-endpoint `B+2` stutter palette

Date: 2026-08-01  
Lane: H1 split-pivot endpoint wrap / independent audit  
Status: exact local owner-window theorem and exact flat-surplus count.  The
`B+2` conclusion is owner-palette feasibility only; no full source/common-cap
word is constructed.

## 0. Verdict

The local stutter calculation is correct.  For the displayed collars, the
`d` width-`d+1` windows crossing the new seam have multiset

\[
       2[U]+\sum_{j=2}^{d-1}[D_j],\qquad D_j=U-\{f_j\}.       \tag{0.1}
\]

The two endpoint coatoms `D_1,D_d` do not occur at the new seam.  This gives
the sharp flat count:

* with one surplus owner-window, at most one of `D_1,D_d` can have a retained
  occurrence, so the prepared-bank `B+1` recut is impossible;
* with two surplus windows, the old row may retain one extra occurrence of
  each of `D_1,D_d`.  After the recut those two retained occurrences become
  the unique endpoint coatoms, while the new seam supplies the internal
  coatoms and two nonmiddle `U` windows.

There are two different possible dropped-bank statements and they must not be
conflated.  The prepared old bank is

\[
                         [D_d]+\cdots+[D_1].                 \tag{0.2}
\]

Relative to (0.2), the new bank performs the signed exchange

\[
                         [D_1]+[D_d]\longmapsto 2[U].        \tag{0.3}
\]

Alternatively, one may demand an old cut carrying a second literal copy of
the same stutter collar.  Its dropped bank then equals (0.1) exactly.  That is
a stronger collar-existence hypothesis, not a consequence of the one
prepared suffix and prefix at the new exterior seam.

## 1. Literal crossing calculation

Fix `d>=2`.  Let `f_1,...,f_d` be distinct fillers disjoint from a common
aperture `C`.  Choose `A,B` contained in `C` with `A union B=C`, and choose a
filler-free stutter letter

\[
                         \varnothing\ne K\subseteq C.         \tag{1.1}
\]

The nonemptiness in (1.1) is needed only when empty source letters are
forbidden.  Put

\[
\begin{aligned}
 F&=\{f_1,\ldots,f_d\},& U&=C\cup F,&D_j&=U-\{f_j\},\\
 Z&=A\cup\{f_1\},&T&=B\cup\{f_d\}.                          \tag{1.2}
\end{aligned}
\]

Consider the two length-`d` collars

\[
\begin{aligned}
 Q&=(\{f_{d-1}\},\{f_{d-2}\},\ldots,\{f_2\},K,Z),\\
 P&=(T,K,\{f_{d-1}\},\{f_{d-2}\},\ldots,\{f_2\}).          \tag{1.3}
\end{aligned}
\]

The filler lists are empty at `d=2`.  Index the crossing windows by their
start in `Q`.  For `0<=s<=d-1`, let

\[
 G_s=\operatorname{OR}(Q_s,\ldots,Q_{d-1},P_0,\ldots,P_s).   \tag{1.4}
\]

These are exactly all `d` width-`d+1` windows crossing `Q|P`.

### Theorem 1.1 (exact gained sequence)

In order,

\[
 (G_0,G_1,\ldots,G_{d-1})
       =(U,D_{d-1},D_{d-2},\ldots,D_2,U).                    \tag{1.5}
\]

Hence the gained multiset is exactly (0.1), including multiplicity two at
`U`.  At `d=2`, (1.5) is simply `(U,U)`.

#### Proof

Every crossing window contains the adjacent letters `Z,T`; they supply `C`,
`f_1`, and `f_d`.  The first window contains all internal fillers on the
`Q` shore, so `G_0=U`.  After the first shift, `f_(d-1)` has left while the
filler-free `K` has entered, giving `D_(d-1)`.  On each subsequent shift the
previous missing filler enters from `P` exactly when the next filler leaves
from `Q`.  The unique omission therefore walks through

\[
                         f_{d-1},f_{d-2},\ldots,f_2.
\]

At the last start, every internal filler has entered from `P`, so
`G_(d-1)=U`.  No property of `K` beyond containment in `C` is used.
\(\square\)

The positions of the filler-neutral insertions are sharp inside these two
monotone collars: inserting one `K` into

\[
 (f_{d-1},\ldots,f_2,Z),\qquad(T,f_{d-1},\ldots,f_2)
\]

produces (1.5) only when it is immediately before `Z` in the first word and
immediately after `T` in the second.  The audit exhausts these positions for
`2<=d<=10`.

## 2. The prepared dropped bank and the `B+1` obstruction

Let the flat owner row have `W+c` windows and cover `W` distinct required
middle owners.  Thus `c` is the complete occurrence surplus: duplicate
required owners and nonmiddle windows together consume at most `c` slots.

In the prepared endpoint orientation, the `d` old windows removed by the
recut are

\[
                  \mathcal D_{\rm prep}
                     =[D_d]+[D_{d-1}]+\cdots+[D_1].          \tag{2.1}
\]

Every new window crossing `Z|T` contains both `f_1` and `f_d`.  Consequently
no new crossing window can equal `D_1` or `D_d`, independently of the
internal filler order.

### Theorem 2.1 (sharp one-surplus no-go)

If `c=1`, a recut dropping (2.1) and gaining only windows crossing `Z|T`
cannot preserve the complete required owner palette.

#### Proof

Both occurrences of `D_1,D_d` in (2.1) are removed, and neither value is
present in the gained bank.  Preservation would therefore require one
retained occurrence of each outside (2.1).  Since `D_1` and `D_d` are
distinct, the old row would then contain all `W` required owners plus two
occurrences beyond their first occurrences, at least `W+2` windows.  But a
one-surplus row has only `W+1`.  \(\square\)

This is not an unrestricted `B+1` lower bound.  Its hypotheses include a flat
fixed-width owner row, the prepared dropped bank (2.1), and a `Z|T` gained
seam.  It says nothing about a nonflat deadline staircase, another dropped
bank, a remote width-changing witness, or a separately rebuilt carrier.

## 3. What the `B+2` owner schedule actually says

Subtracting multisets in Theorem 1.1 and (2.1) gives exactly

\[
\begin{aligned}
 \mathcal D_{\rm prep}-\mathcal G&=[D_1]+[D_d],\\
 \mathcal G-\mathcal D_{\rm prep}&=2[U],                    \tag{3.1}
\end{aligned}
\]

where \(\mathcal G\) is the gained bank (0.1).  All internal coatoms cancel.

### Corollary 3.1 (prepared-bank `B+2` palette completion)

Suppose the untouched `W-d+2` owner windows form a bijection onto all
required owners except `D_2,...,D_(d-1)`.  In particular they contain one
retained `D_1` and one retained `D_d`.  Then:

1. before the recut, (2.1) plus the untouched bank covers every owner, with
   `D_1,D_d` as the two duplicate-surplus occurrences;
2. after the recut, the untouched bank plus (0.1) covers every owner exactly
   once, and the two `U` occurrences are the two nonmiddle surplus windows.

Thus the owner count closes exactly at surplus two.

This is coverage of the required palette, not equality of the complete
owner-window multiset: the multiplicities change according to (3.1).

### Corollary 3.2 (conditional identical-bank version)

If the old cut independently has suffix `Q` and prefix `P` from (1.3), its
dropped bank is another copy of (0.1).  The dropped and gained owner-window
multisets are then identical.

This version needs two seam instances, one at the old cut and one at the new
cut.  In the collar-disjoint regime that means a `Q` and a `P` collar at each
cut.  A single prepared global suffix `Q` and global prefix `P` supplies only
the new wrap seam.  It does not establish the second pair, their legal source
caps, or their cost.  Therefore Corollary 3.2 cannot by itself be called a
`B+2` word construction.

## 4. Exact scope boundary

The following statements are frozen by this audit:

* the gained sequence and multiset (1.5);
* the prepared dropped bank (2.1) as an explicit hypothesis;
* the signed owner exchange (3.1);
* the `B+1` one-surplus impossibility under those hypotheses; and
* the two conditional owner-level completions in Corollaries 3.1--3.2.

None of those statements supplies any of the following:

* a full source word of length `B(k)+2`;
* a legal depth-`d` antecedent whose width-`d+1` row is the proposed owner
  row;
* simultaneous occurrence of all old-cut and new-cut collars;
* nonempty source letters and their exact positionwise caps beyond the local
  assumption (1.1);
* one integral common-cap/common-`Q` state across phases;
* Johnson simplicity or the required path-forest topology;
* residence, `q1`, lower-row, arbitrary-width upper-row, task, or protected
  witness replay.

In particular, a full `B+2` theorem requires the actual source/common-cap
rows.  Owner colours written in isolation do not certify that they are the
width-`d+1` windows of one legal word.

## 5. Independent replay

Run

```text
python3 scratch/audit_h1_prepared_endpoint_bplus2_stutter_crossaudit_20260801.py
```

The dependency-free replay checks every `2<=d<=64` and all `189` triples
`(A,B,K)` over a three-coordinate aperture with `A union B=C` and nonempty
`K` contained in `C`.  It verifies (1.5), both multiset differences in (3.1), the
absence of every one-surplus completion, the unique two-surplus endpoint
allocation, and the conditional identical-collar bank.  For `2<=d<=10` it
also exhausts every position of the two stutters.

It reports

```text
PASS_PREPARED_ENDPOINT_BPLUS2_STUTTER_OWNER_PALETTE_CROSSAUDIT
```

with canonical payload SHA-256

```text
4f748ac757afe1bae7e9b3866900d5cd062b524b23d8af61695ccdb03d978386
```

Frozen artifacts:

```text
scratch/audit_h1_prepared_endpoint_bplus2_stutter_crossaudit_20260801.py
scratch/h1_prepared_endpoint_bplus2_stutter_crossaudit_20260801.audit.json
```

Primary audited claim:

```text
MATH_THEOREM_H1_FLAT_BPLUS1_ENDPOINT_WRAP_NOGO_AND_BPLUS2_STUTTER_PALETTE_20260801.md
```
