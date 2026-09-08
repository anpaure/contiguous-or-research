# The canonical (K=11) cyclic four-window support

> **Correction notice (2026-07-25).**  The original transcription of
> the nonzero hole list incorrectly included \(\{1,2,7,10\}\), which
> occurs in row E8, and omitted its required replacement
> \(\{3,4,7,10\}\).  The recursion, symmetry proof, A--B audit, and
> corrected splice witness are recorded in
> `K11_CANONICAL_SUPPORT_CORRECTION_AB_AUDIT_20260725.md`.  Sections
> 4, 7, and the splice tables below should be read with the replacement
> \(127(10)\mapsto347(10)\).

> **Resolved support warning (2026-07-25).**  The original displayed hole
> list had one transcription error.  Its own formulas give the witness
> below: using the (T_4) row
> (4217\mid6538) in class E gives
> 
> \[
> \pi=(0,4,5,7,2,1,10,6,8,9,3),
> \]
> 
> whose consecutive positions (3,4,5,6) form
> \(\{1,2,7,10\}\), although that set is listed as absent in (4.1).
> The corrected replacement is
> \(127(10)\mapsto347(10)\).  A complete positive-support certificate,
> proving that the corrected 32 sets are the entire complement and that
> the support is exactly 298, is in
> `K11_CORRECTED_CYCLIC4_POSITIVE_SUPPORT_CERTIFICATE_20260725.md`.
> The multiplicity histogram in Section 6 remains suspended: the fresh
> audit found further E-table transcription errors and the old triple list
> is not correct.

## Result

For the canonical Chung--Feller/Mütze--Standke--Wiechert exact wreath
factor at (n=11,m=5), the union of the cyclic length-four windows has
exactly

\[
298
\]

members.  Equivalently, exactly (32) of the
\(\binom{11}{4}=330\) four-sets are absent.

This is a hand classification from the recursive definition of the flip
sequence.  No search or numerical verifier is used.

## 1. Recursive order table

For a Dyck word (w), write its first-return decomposition as

\[
w=U p D q,
\qquad h=|p|+2.
\]

The flip sequence is recursively

\[
\Phi(w)=
[h]\,\Vert\,
[h-v:v\in\Phi(\operatorname{rc}(p))]\,\Vert\,
[1]\,\Vert\,
[h+v:v\in\Phi(q)],
\]

where \(\operatorname{rc}\) is reverse-complement.  Put

\[
I=\Phi(w)[1,3,5,\ldots],
\qquad
R=\Phi(w)[2,4,6,\ldots].
\]

The associated cyclic coordinate order is

\[
\pi(w)=(0,R,I).
\]

If \(p\) has semilength (r), the recursion gives

\[
I(w)=[h]\Vert(h-R(\operatorname{rc}(p)))\Vert(h+I(q)),
\]

\[
R(w)=(h-I(\operatorname{rc}(p)))\Vert[1]\Vert(h+R(q)).
\tag{1.1}
\]

The complete semilength-three table (T_3), written (R\mid I), is

```text
135|246   143|265   215|436   421|653   231|645
```

The complete semilength-four table (T_4) is

```text
1357|2468   1365|2487   1437|2658   1643|2875
1453|2867   2157|4368   2165|4387   4217|6538
2317|6458   6421|8753   6231|8745   4521|8673
2351|8467   2431|8657
```

Equation (1.1) partitions all (42=operatorname{Cat}_5) rows into the
following five classes.  Shifts and reflections are componentwise.

- **A, (r=0), 14 rows:**
  \[
  R=(1,2+R_4),\qquad I=(2,2+I_4),qquad (R_4\mid I_4)\in T_4.
  \]

- **B, (r=1), 5 rows:**
  \[
  R=(2,1,4+R_3),\qquad I=(4,3,4+I_3),qquad (R_3\mid I_3)\in T_3.
  \]

- **C, (r=2), 4 rows:**

```text
42179|653810   42187|653109
23179|645810   23187|645109
```

- **D, (r=3), 5 rows:**
  \[
  R=(8-I_3,1,9),\qquad I=(8,8-R_3,10),qquad (R_3\mid I_3)\in T_3.
  \]

- **E, (r=4), 14 rows:**
  \[
  R=(10-I_4,1),\qquad I=(10,10-R_4),qquad (R_4\mid I_4)\in T_4.
  \]

Reverse-complement merely permutes each complete (T_j), so these are
all 42 rows, without repetition.

## 2. The eleven window templates

Write

\[
\pi=(0,r_1,r_2,r_3,r_4,r_5,i_1,i_2,i_3,i_4,i_5).
\]

The four cyclic windows containing (0) are

\[
\begin{aligned}
&\{0,r_1,r_2,r_3\},
&&\{0,i_3,i_4,i_5\},\\
&\{0,i_4,i_5,r_1\},
&&\{0,i_5,r_1,r_2\}.
\end{aligned}
\tag{2.1}
\]

The seven windows avoiding (0) are

\[
\begin{aligned}
&\{r_1,r_2,r_3,r_4\},
&&\{r_2,r_3,r_4,r_5\},\\
&\{r_3,r_4,r_5,i_1\},
&&\{r_4,r_5,i_1,i_2\},\\
&\{r_5,i_1,i_2,i_3\},
&&\{i_1,i_2,i_3,i_4\},\\
&\{i_2,i_3,i_4,i_5\}.
\end{aligned}
\tag{2.2}
\]

Substitution of classes A--E into (2.1)--(2.2) is therefore an
exhaustive symbolic classification.

## 3. Missing windows containing (0)

Exactly the following sixteen are absent:

\[
\begin{gathered}
\{0,1,4,7\},\ \{0,1,6,9\},\\
\{0,2,3,7\},\ \{0,2,4,7\},\ \{0,2,5,6\},\
\{0,2,5,7\},\ \{0,2,5,8\},\ \{0,2,5,10\},\\
\{0,3,4,7\},\ \{0,3,6,9\},\\
\{0,4,6,9\},\ \{0,4,7,8\},\ \{0,4,7,9\},\
\{0,4,7,10\},\ \{0,4,8,9\},\\
\{0,5,6,9\}.
\end{gathered}
\tag{3.1}
\]

For a compact complement audit, remove the (0) and sort triples by
their least entry.  The omissions are

```text
least 1: 147, 169
least 2: 237, 247, 256, 257, 258, 25(10)
least 3: 347, 369
least 4: 469, 478, 479, 47(10), 489
least 5: 569
least at least 6: none
```

Every other one of the (120) triples occurs in one of the four
templates (2.1).  Hence (104) zero-containing four-sets occur.

## 4. Missing windows avoiding (0)

Exactly the following sixteen are absent:

\[
\begin{gathered}
\{1,2,6,9\},\ \{3,4,7,10\},\
\{1,3,6,9\},\ \{1,3,6,10\},\\
\{1,4,5,9\},\ \{1,4,6,9\},\
\{1,4,7,8\},\ \{1,4,7,9\},\
\{1,5,8,10\},\\
\{2,3,6,9\},\ \{2,4,7,10\},\
\{2,5,7,10\},\ \{2,5,8,9\},\
\{2,5,8,10\},\ \{2,5,9,10\},\
\{2,6,7,10\}.
\end{gathered}
\tag{4.1}
\]

The lexicographic complement audit is

```text
least 1:
  1269, 1369, 136(10),
  1459, 1469, 1478, 1479, 158(10)
least 2:
  2369, 247(10), 257(10), 2589,
  258(10), 259(10), 267(10)
least 3:
  347(10)
least at least 4: none
```

Every other one of the (210) nonzero four-sets occurs in one of the
seven templates (2.2).  Hence (194) nonzero four-sets occur.

## 5. Exact support

Combining the two parts,

\[
|\operatorname{supp}_4|=104+194=298,
\]

and the missing family has size

\[
16+16=32.
\]

In the physical cycle automaton associated with a wreath order,

\[
B_i=\{z_{i-4},z_{i-3},z_{i-2},z_{i-1}\},
\]

while

\[
Y_i=\{z_{i+2},z_{i+3},z_{i+4},z_{i+5}\}.
\]

As (i) runs cyclically these are the same eleven four-windows.
Therefore both the lower and upper four-colour ledgers have this same
support (298).

The canonical exact wreath factor consequently falls (21) support
units short of the required threshold (319).

## 6. Exact multiplicity histogram

> **Retracted.**  The histogram and triple list in this section were
> derived from a transcription containing at least the false E13/E14
> entries `1236,1235` in place of `1346,1345`; several asserted triples
> have only two occurrences in the corrected rows.  Do not use (6.1)--
> (6.2).  The support value 298 is independently re-certified, but this
> multiplicity refinement is not.

Sorting the occurrences in the same A--E template table gives

\[
\boxed{m_0=32,\qquad m_1=149,\qquad m_2=134,\qquad m_3=15.}
\tag{6.1}
\]

The zero-containing and nonzero subhistograms are respectively

\[
(16,46,52,6)
\qquad\hbox{and}\qquad
(16,103,82,9).
\]

The fifteen multiplicity-three colours are

\[
\begin{gathered}
\{0,1,4,9\},
\{0,2,3,9\},
\{0,2,4,9\},
\{0,2,7,9\},
\{0,2,7,10\},
\{0,2,8,9\},\\
\{1,2,3,4\},
\{1,2,3,5\},
\{1,2,3,6\},
\{1,2,5,10\},
\{1,3,8,10\},\\
\{2,4,6,8\},
\{3,4,6,8\},
\{3,4,6,9\},
\{3,4,7,8\}.
\end{gathered}
\tag{6.2}
\]

As checks on (6.1),

\[
149+134+15=298,
\]

and

\[
149+2(134)+3(15)=462.
\]

Thus exactly 149 old cycle edges have unique colours.  If 42 old
edges are cut and 36 cross edges are added, let (L) be the number of
old colours all of whose occurrences were cut and let (G) be the
number of genuinely new distinct cross colours.  The final support is
exactly

\[
298-L+G,
\]

so the target 319 is equivalent to (G-L\ge21).

## 7. Backward-physical splice colours

Consider a canonical tail with five consecutive source coordinates

\[
(t_0,t_1,t_2,t_3,t_4)
=
(z_{i-5},z_{i-4},z_{i-3},z_{i-2},z_{i-1}).
\]

The exact backward-physical splice criterion permits only

\[
\beta=z_{i-4}=t_1
\quad\hbox{or}\quad
\beta=z_{i-3}=t_2.
\]

Consequently the possible new lower colour is respectively

\[
\{t_0,t_2,t_3,t_4\}
\quad\hbox{or}\quad
\{t_0,t_1,t_3,t_4\}.
\tag{7.1}
\]

Thus (7.1) is obtained from a cyclic five-window by deleting its second
or third entry.  Applying these two additional templates to the same
42-row A--E table shows that 30 of the 32 canonical holes are
backward-repairable.  Explicit witnesses are below; the underlined entry
is the deleted coordinate.

| hole | canonical five-window witness |
|---|---|
| \(\{0,1,4,7\}\) | \((7,\underline{10},0,1,4)\) |
| \(\{0,1,6,9\}\) | \((6,\underline{10},9,0,1)\) |
| \(\{0,2,3,7\}\) | \((7,\underline{10},0,2,3)\) |
| \(\{0,2,4,7\}\) | \((7,\underline{10},0,2,4)\) |
| \(\{0,2,5,6\}\) | \((0,\underline{4},6,5,2)\) |
| \(\{0,2,5,7\}\) | \((0,2,\underline{3},5,7)\) |
| \(\{0,2,5,8\}\) | \((0,8,\underline{4},5,2)\) |
| \(\{0,3,4,7\}\) | \((0,\underline{1},4,3,7)\) |
| \(\{0,3,6,9\}\) | \((9,0,\underline{1},3,6)\) |
| \(\{0,4,6,9\}\) | \((4,6,\underline{10},9,0)\) |
| \(\{0,4,7,8\}\) | \((7,0,\underline{1},8,4)\) |
| \(\{0,4,7,9\}\) | \((4,\underline{10},9,7,0)\) |
| \(\{0,4,7,10\}\) | \((4,\underline{8},7,10,0)\) |
| \(\{0,4,8,9\}\) | \((4,\underline{10},8,9,0)\) |
| \(\{0,5,6,9\}\) | \((6,5,\underline{10},9,0)\) |
| \(\{1,2,6,9\}\) | \((6,2,\underline{3},1,9)\) |
| \(\{1,2,7,10\}\) | \((7,\underline{4},2,1,10)\) |
| \(\{1,3,6,9\}\) | \((9,\underline{0},1,3,6)\) |
| \(\{1,3,6,10\}\) | \((10,\underline{0},1,3,6)\) |
| \(\{1,4,5,9\}\) | \((9,\underline{0},1,4,5)\) |
| \(\{1,4,6,9\}\) | \((9,\underline{0},1,4,6)\) |
| \(\{1,4,7,8\}\) | \((1,4,\underline{3},8,7)\) |
| \(\{1,4,7,9\}\) | \((1,4,\underline{3},7,9)\) |
| \(\{2,3,6,9\}\) | \((3,6,\underline{5},9,2)\) |
| \(\{2,4,7,10\}\) | \((2,4,\underline{8},7,10)\) |
| \(\{2,5,7,10\}\) | \((7,2,\underline{6},5,10)\) |
| \(\{2,5,8,9\}\) | \((9,2,\underline{6},5,8)\) |
| \(\{2,5,8,10\}\) | \((5,2,\underline{4},10,8)\) |
| \(\{2,5,9,10\}\) | \((5,2,\underline{4},10,9)\) |
| \(\{2,6,7,10\}\) | \((7,2,\underline{4},6,10)\) |

The only two canonical holes which never occur in either fixed-forward
pattern (7.1)
are

\[
\boxed{\{0,2,5,10\},\qquad \{1,5,8,10\}.}
\tag{7.2}
\]

Nonoccurrence in (7.2), and completeness of the witness table, follow
by applying the two deletion templates to classes A--E exactly as in
Sections 3--4.  This is only the backward half of splice admissibility:
the unique canonical owner of the candidate head must additionally pass
the forward head tests.

## 8. Reverse-tail completion and forward-owner checks

The exception in (7.2) is specific to the fixed-forward orientation.
For a canonical six-window

\[
(t_0,t_1,t_2,t_3,t_4,t_5),
\]

the reversed-tail backward formula is

\[
B_{\rm rev}=U\setminus\{t_0,\beta\},
\qquad \beta\in\{t_3,t_4\},
\tag{8.1}
\]

where (U=\{t_0,t_1,t_2,t_3,t_4,t_5\}).  The two
fixed-forward exceptions have the following genuine reverse-tail
witnesses.

* In row D4, the six-window
  \[
  (7,10,0,2,3,5)
  \]
  with \(\beta=3=t_4\) gives
  \[
  B_{\rm rev}=\{0,2,5,10\},
  \qquad S'_h=\{0,2,5,7,10\}.
  \]

* In row E11, the six-window
  \[
  (6,5,1,10,4,8)
  \]
  with \(\beta=4=t_4\) gives
  \[
  B_{\rm rev}=\{1,5,8,10\},
  \qquad S'_h=\{1,5,6,8,10\}.
  \]

Consequently, when both tail orientations are allowed, all 32
canonical cyclic-four holes are backward candidates.  This statement
does not yet assert that the corresponding splices are globally
compatible, nor even that every candidate head passes its forward
physicality test.

For reference, let the candidate head have its canonical ordered
five-window positions numbered (0,1,2,3,4), and let (r) and (t)
be the final old tail coordinate and the entering head coordinate.  The
forward criterion is:

\[
\begin{array}{c|c}
\operatorname{pos}(t)&\text{condition}\\ \hline
2&\text{always admissible},\\
1&\operatorname{pos}(r)\ne4,\\
3&\operatorname{pos}(r)\ne0.
\end{array}
\tag{8.2}
\]

The positions (0) and (4) for (t) would reproduce an already
supported lower colour, so they do not occur for a genuine hole in the
present audit.  Direct owner lookup in the A--E table has so far
verified the following nine forward-admissible candidates:

| new colour | candidate head | owner/window | ((\operatorname{pos}(r),\operatorname{pos}(t))) |
|---|---|---|---|
| \(0147\) | \(01457\) | A13, \((0,1,4,5,7)\) | \((2,3)\) |
| \(0169\) | \(01369\) | A5, \((9,0,1,3,6)\) | \((2,3)\) |
| \(0237\) | \(02357\) | E10, \((0,2,3,5,7)\) | \((4,3)\) |
| \(0247\) | \(02347\) | E12, \((0,2,4,3,7)\) | \((4,3)\) |
| \(0256\) | \(01256\) | B3, \((0,2,1,6,5)\) | \((1,2)\) |
| \(0257\) | \(01257\) | B1, \((0,2,1,5,7)\) | \((4,2)\) |
| \(0258\) | \(01258\) | B2, \((0,2,1,5,8)\) | \((4,2)\) |
| \(0469\) | \(01469\) | A14, \((9,0,1,4,6)\) | \((1,2)\) |
| \(0479\) | \(01479\) | A14, \((7,9,0,1,4)\) | \((2,3)\) |

These nine checks are local certificates only.  The remaining owner
lookups and the simultaneous (42\)-cycle-to-six-path fusion problem
remain open.
