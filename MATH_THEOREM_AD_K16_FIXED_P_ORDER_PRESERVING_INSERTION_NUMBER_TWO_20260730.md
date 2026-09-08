# The fixed-`P` order-preserving insertion number is exactly two at `k=16`

## 1. Frozen scope and authenticated data

Let

\[
P=(p_0,\ldots,p_{12872})
\]

be the word in `scratch/k16_12873_repaired_partial.word`.  Its SHA-256 is

```text
0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

and exact contiguous-OR replay gives precisely the three missing nonzero
16-bit masks

\[
H=\{a,b,c\}=\{0x287d,0xce61,0xce63\}.
\]

This note permits only **order-preserving insertions into this fixed word**:
the old cells retain both their values and their relative order.  It does not
permit a substitution, deletion, cyclic rotation followed by a different cut,
or any rethreading of the carrier.

The authenticated length-12,875 completion is
`answers/k16_upper12875.word`, SHA-256

```text
d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9
```

and is exactly

\[
P\mid 0x0200\mid 0x287d.
\]

## 2. Exact gap-set criterion

For a word of length \(n\), number its gaps by \(g=0,\ldots,n\): gap
\(g<n\) is immediately before \(p_g\), and gap \(n\) is after
\(p_{n-1}\).  An old interval straddles gap \(g\) if it has the form
\([i,j]\) with

\[
0\le i\le g\le j+1\le n.
\]

The empty interval \([g,g-1]\), whose OR is zero, is allowed.  Write
\(u(J)\) for the OR of an old interval \(J\).

### Lemma 2.1 (exact common-gap lemma)

Let \(H\) be any nonempty family of holes of a fixed word \(P\), put

\[
I=\bigcap_{h\in H}h,\qquad q_h=h\setminus I=h\mathbin{\&}\neg I,
\]

and define

\[
G_h=\left\{g:\text{ some old interval }J\text{ straddling }g
\text{ has }q_h\subseteq u(J)\subseteq h\right\}.
\]

There is a nonzero cell \(x\) whose insertion at gap \(g\) supplies every
hole in \(H\) if and only if

\[
g\in\bigcap_{h\in H}G_h.
\]

#### Proof

Suppose first that inserting \(x\) supplies every \(h\in H\).  An interval
avoiding the new cell is an unchanged old interval, so it cannot witness an
old hole.  Every new witness therefore contains \(x\), and hence
\(x\subseteq h\) for every \(h\), so \(x\subseteq I\).  Removing \(x\)
from a witness leaves one old interval \(J_h\) straddling \(g\).  If
\(u_h=u(J_h)\), then \(u_h\subseteq h\).  Every bit of \(h\) outside \(I\)
must come from \(u_h\), so \(q_h\subseteq u_h\).  Thus
\(g\in G_h\) for every \(h\).

Conversely, suppose \(g\in\bigcap_hG_h\), and choose a compatible
straddling interval \(J_h\) for every \(h\).  Put

\[
x=\bigvee_{h\in H}\bigl(h\setminus u(J_h)\bigr).
\]

Because \(q_h\subseteq u(J_h)\), every bit in
\(h\setminus u(J_h)\) lies in \(I\).  Hence \(x\subseteq I\subseteq h\)
for every \(h\), while

\[
x\vee u(J_h)=h.
\]

Finally, \(x\ne0\): otherwise every selected old interval would already
have OR equal to its corresponding hole.  Inserting this \(x\) at \(g\)
therefore supplies all holes.  \(\square\)

This is an exact criterion for supplying the old holes.  A positive candidate
would still require checking targets whose old witnesses cross the chosen
gap, but an empty common gap set is already an unconditional insertion
no-go.

## 3. Exact evaluation for the authenticated word

For the three holes of \(P\),

\[
I=a\cap b\cap c=0x0861,
\]

and

\[
q_a=0x201c,\qquad q_b=0xc600,\qquad q_c=0xc602.
\]

All ranges below are inclusive integer gap ranges.  Direct monotone-OR
enumeration of the compatible old intervals gives 16 compatible intervals
and 42 gaps for \(a\):

\[
\begin{aligned}
G_a={}&[586,588]\cup[1339,1341]\cup[1347,1348]\cup[1789,1791]\\
&\cup[1853,1855]\cup[2454,2455]\cup[2523,2524]\cup[2541,2543]\\
&\cup[3183,3186]\cup[4661,4663]\cup[4833,4836]\cup[5619,5620]\\
&\cup[5922,5925]\cup[5931,5934].
\end{aligned}
\]

It gives 20 compatible intervals and 38 gaps for \(b\):

\[
\begin{aligned}
G_b={}&[6721,6723]\cup[6774,6776]\cup[7551,7553]\cup[8363,8364]\\
&\cup[8638,8639]\cup[9485,9486]\cup[10035,10037]\cup[10525,10526]\\
&\cup[10677,10679]\cup[11038,11039]\cup[11584,11585]\cup[11910,11911]\\
&\cup[12237,12238]\cup[12325,12326]\cup[12429,12430]\cup[12775,12777].
\end{aligned}
\]

It gives 18 compatible intervals and 43 gaps for \(c\):

\[
\begin{aligned}
G_c={}&[6720,6723]\cup[6804,6806]\cup[7335,7337]\cup[7588,7591]\\
&\cup[7638,7641]\cup[7679,7680]\cup[8010,8014]\cup[8340,8342]\\
&\cup[9484,9486]\cup[10697,10699]\cup[11018,11019]\\
&\cup[12050,12052]\cup[12742,12745].
\end{aligned}
\]

The decisive separation is

\[
\max G_a=5934<6720=\min(G_b\cup G_c).
\]

Consequently \(G_a\cap G_b\cap G_c=\varnothing\).  Lemma 2.1 proves that
no single order-preserving insertion anywhere in the fixed word can even
supply all three old holes.

## 4. Exhaustive one-cell cut-kernel census

Every inserted cell capable of supplying all three holes must be a nonzero
submask of \(I=0x0861\).  There are exactly \(2^4-1=15\) such masks.  Thus
the complete relaxed census has

\[
(12873+1)\cdot15=193110
\]

gap/literal rows.  If the score of a row is the number of the three old holes
supplied by an interval through the inserted cell, an independent left/right
OR-state recurrence gives

\[
\begin{array}{c|rrr}
\text{score}&0&1&2\\ \hline
\text{rows}&192518&560&32.
\end{array}
\]

There are no score-3 rows.  The authenticated checker independently confirms
all 193,110 rows, zero full hits, maximum score two, and 32 maximizing rows.
The word "relaxed" matters: this score ignores old targets whose witnesses
might be displaced at a cut.  That omission can create false positive rows,
but it cannot invalidate the zero-full-hit no-go.

## 5. An exact 128-member two-append family

The final old suffix states needed here are

\[
p_{12871}\vee p_{12872}=0xcc61,
\qquad
p_{12870}\vee p_{12871}\vee p_{12872}=0xcc63.
\]

Let \(x\) be any mask satisfying

\[
0x0200\subseteq x\subseteq0xce61.
\]

Then

\[
0xcc61\vee x=0xce61=b,
\qquad
0xcc63\vee x=0xce63=c.
\]

Since \(0xce61\) has eight bits and the bit \(0x0200\) is mandatory, there
are exactly

\[
2^{8-1}=128
\]

such first append cells.  For every one of them, append \(a=0x287d\) as the
second cell.  The singleton second cell supplies \(a\), the two displayed
suffix intervals supply \(b,c\), and appending preserves every old witness.
Thus every word

\[
P\mid x\mid0x287d,
\qquad 0x0200\subseteq x\subseteq0xce61,
\]

is universal.  The retained certificate uses the minimal member
\(x=0x0200\).  The previously considered \(x=0x0661\) is another member of
the same family, but it is not the retained authenticated upper word.

## 6. Frozen theorem and strict boundary

### Theorem 6.1

For the authenticated fixed word \(P\), the minimum number of nonzero
order-preserving cell insertions required to obtain a universal contiguous-OR
word is exactly two.  Two terminal appends suffice, in the 128 ways described
above.

#### Proof

The word \(P\) is not universal because it has the three authenticated holes.
Section 3 proves that one insertion anywhere is impossible.  Section 5 gives
128 explicit two-append completions.  \(\square\)

This theorem is **not** a global lower bound \(\nu(16)\ge12875\).  In
particular, it does not exclude an unrelated length-12,874 word, nor a repair
using substitutions, deletions, reorderings, a different carrier, or a
simultaneous cut-and-rethread operation.  Its exact conclusion is only that
the frozen length-12,873 prefix \(P\), with all old cells fixed in order,
cannot be completed with one inserted cell and can be completed with two.

## 7. Replay anchors

The light exact checker
`scratch/audit_threadA_k16_one_cell_insertion_20260730.py` has SHA-256

```text
480c83a2080c0202da5219fa9d916a79463bb310ae949df025d7f74e7c257dfa
```

and terminates with

```text
PASS_ONE_CELL_INSERTION_NOGO_TWO_APPEND_OPTIMAL
```

on the authenticated inputs.  Its frozen audit record is
`scratch/threadA_k16_one_cell_insertion_20260730.audit.json`, SHA-256

```text
5fe80b3a51c711b92fa7d5c9cd47570a1a879a351b4573a2baee0a89c99899b6
```

with status `PASS_ONE_CELL_INSERTION_NOGO_TWO_APPEND_OPTIMAL`.
