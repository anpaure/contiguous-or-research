# Pair-shared tags cannot physicalize the aligned four-C8 relation

Date: 2026-08-01  
Lane: H2, four-relabelled octagon / physical lift  
Status: exact solver-free no-go for the fixed aligned four-block sharp-source
fibre with addressed residual matching.  Cross-address rematching, changed
source geometry and tags shared by three or four blocks are outside scope.

## 0. Result

Use the four sharp octagon inverse blocks in order

\[
       1,\quad \beta=(a_1\ a_3),\quad
       \alpha=(a_0\ a_2),\quad \alpha\beta
\]

and phase vectors `0110` and `1001`.  Introduce four new tag labels

\[
                t_{02},t_{03},t_{12},t_{13}.                 \tag{0.1}
\]

The tag `t_ij` may occur arbitrarily in blocks `i,j` and nowhere else.  Its
occurrence schedule in the two blocks need not be synchronized.  Thus the
available tag alphabets are

\[
\begin{array}{c|c}
0&\{t_{02},t_{03}\}\\
1&\{t_{12},t_{13}\}\\
2&\{t_{02},t_{12}\}\\
3&\{t_{03},t_{13}\}.
\end{array}                                                  \tag{0.2}
\]

Suppose every phase-sensitive interval is transported at the same relative
address: within each untagged OR-value class, the old and new occurrences
must have the same multiset of tag unions.  Then no such tagging makes the
rank-`d+3` owner bank simple, for any `d>=1`.

The obstruction is already four windows.  In the old state the owner

\[
                         F\cup\{a_2\}                         \tag{0.3}
\]

occurs at

\[
 (0,d+2),\quad(3,3d+8),\quad(1,5d+14),\quad(2,7d+20),        \tag{0.4}
\]

where a pair is `(block,start)` and every window has width `d+1`.  Addressed
OR preservation forces the tag union of every one of these windows to be
empty.  Hence all four tagged owners in (0.4) remain identical.

## 1. The cycle forcing lemma

For an owner window beginning at address `p`, let `v_b^old(p)` and
`v_b^new(p)` be its untagged values in block `b`, and let `s_b(p)` be its
tag union.  Tags are phase independent, so one `s_b(p)` is used on both
sides.

At `p=d+2`, the active parts are

\[
\begin{array}{c|cccc}
 &0&1&2&3\\ \hline
 old&a_2&a_1&a_3&a_0\\
 new&a_3&a_2&a_0&a_1.
\end{array}                                                  \tag{1.1}
\]

The filler part is common.  Every untagged value in (1.1) is distinct, so
equality of the tagged occurrence multisets forces

\[
             s_0=s_1=s_3=s_2=s_0.                            \tag{1.2}
\]

But by (0.2), a common tag set lies in

\[
 \{t_{02},t_{03}\}\cap\{t_{12},t_{13}\}
 \cap\{t_{02},t_{12}\}\cap\{t_{03},t_{13}\}=\varnothing.  \tag{1.3}
\]

Therefore all four tag unions are empty.  The same argument applies whenever
the value-matching permutation is either of the two directed four-cycles

\[
        (0\ 1\ 3\ 2),\qquad(0\ 2\ 3\ 1).                    \tag{1.4}
\]

No assumption about equality of the two physical schedules of one pair tag
was used.

## 2. The repeated-owner core

The four addresses in (0.4) have the matching permutations in (1.4), so
their tag unions are all empty by Section 1.  Direct maximal-erosion formulas
give

\[
\begin{aligned}
 v_0^{old}(d+2)
 &=v_3^{old}(3d+8)\\
 &=v_1^{old}(5d+14)
  =v_2^{old}(7d+20)
  =F\cup\{a_2\}.                                           \tag{2.1}
\end{aligned}
\]

All starts lie in `0,...,8d+22`, the owner-start range of a sharp source of
length `9d+23`.  Thus (2.1) supplies four distinct physical owner-window
occurrences with identical tagged value.  A simple owner bank is impossible.

This proves more than failure of a periodic rail ansatz: every arbitrary,
independently chosen occurrence schedule on the four pair rails fails.

## 3. Exact scope

The theorem rules out only the following physicalization:

* the fixed aligned four sharp blocks and their fixed relative addresses;
* four tag labels with the incidence restrictions (0.2);
* phase-independent tag placements; and
* addressed transport inside each untagged residual value class.

It does **not** rule out a tag shared by all blocks, a three-block tag,
cross-address reassignment of equal-width intervals, a quotient weave which
identifies or moves the windows in (0.4), or a changed/nonflat source word.
It is not a no-go for the underlying graded OR relation, whose signed action
is exactly `4g8`.

## 4. Replay

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_h2_c8_pair_shared_tagged_weave_owner_nogo_20260801.py --write
```

The replay checks `1<=d<=64`, the exact two four-cycle rows, the full
owner-address tag-domain histogram

\[
      1^{4d+12},\qquad 4^2,\qquad 256^{4d+9},               \tag{4.1}
\]

under completely independent endpoint schedules, and the fourfold collision
(2.1).
