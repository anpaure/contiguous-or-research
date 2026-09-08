# Independent audit of split-letter contraction and exact task-hosting scope

Date: 2026-08-01  
Lane: H2 independent replay / regenerative sidecar  
Status: **GO**, with an explicit deadline-and-host scope.

## 1. Block contraction is exact

Let \(A=(A_0,\ldots,A_{N-1})\) be a word of nonempty sets.  At any set of
positions \(R\), replace each letter \(A_r\) by a consecutive nonempty block

\[
 B_r=(B_{r,1},\ldots,B_{r,\ell_r}),\qquad
 \bigcup_{j=1}^{\ell_r}B_{r,j}=A_r.                 \tag{1.1}
\]

For an old interval \([a,b]\), take the interval in the expanded word from
the first member of the block replacing \(A_a\) through the last member of
the block replacing \(A_b\).  Its OR is exactly the old OR.  The map on
physical intervals is injective.  This proves simultaneous preservation at
arbitrarily many split sites; separation is unnecessary for unrestricted
interval-OR coverage.

For one split \(X=Z\cup T\), with \(Z,T\ne\varnothing\), this is precisely

\[
                         X\longmapsto Z,T.           \tag{1.2}
\]

The conclusion concerns literal interval values.  A transported interval's
length increases by the number of split sites it contains.  Therefore a
fixed-width compiler or flat derivative needs corresponding deadline slack,
or a separate proof that the overflowing cells are unused.  Block
contraction by itself proves neither condition.

## 2. Exact singleton-host characterization

Let \(\mathcal T\) be a family of nonempty task masks.  Restrict attention to
**singleton-host expansions**: every task must be one member of a block
replacing an old source letter.  Such an expansion exists if and only if

\[
       \forall T\in\mathcal T\quad\exists r\quad T\subseteq A_r. \tag{2.1}
\]

Necessity follows from (1.1), since every block member is contained in its
block union.  For sufficiency, assign each task to one containing letter
\(X\), and replace that letter by

\[
                         X,T_1,\ldots,T_s.            \tag{2.2}

\]

The union of the block is still \(X\), so Section 1 preserves every old
interval while every task is a singleton.

Consequently the exact number of actual old host letters needed is the set
cover parameter

\[
 \kappa_A(\mathcal T)=
 \min\{|R|:\forall T\in\mathcal T\ \exists r\in R, T\subseteq A_r\}.
                                                               \tag{2.3}
\]

Thus “all tasks group under \(O(1)\) actual letters” is exactly
\(\kappa_A(\mathcal T)=O(1)\) in this model.  This does **not** say that the
length charge is \(\kappa_A\): (2.2) adds one position per distinct singleton
task (or per occurrence when cell-injective duplicate occurrences are
required).  For a fixed-\(H\) sidecar this is still an exact \(+H=O(1)\)
zero-loss reset.

## 3. What one added position can carry

For one host \(A_r=X=Z\cup T\), the interval values which can be genuinely
new after the two-letter split are exactly the two endpoint rays

\[
 \left\{Z\cup\bigcup_{i=a}^{r-1}A_i:a\le r\right\}
 \quad\text{and}\quad
 \left\{T\cup\bigcup_{i=r+1}^{b}A_i:b\ge r\right\}.       \tag{3.1}
\]

Every interval containing both \(Z\) and \(T\) is the contraction image of
an old interval and hence has an old value.  Therefore one extra position
can serve many genuinely new tasks only when they form the literal endpoint
rays (3.1), up to tasks which were already covered.  Cardinality or nesting
without the common host and physical prefix/suffix order is insufficient.

There is also an exact several-host trace criterion.  Split the selected
letters \(A_r=X_r\) as \(Z_r,T_r\).  For an old interval \([a,b]\) with
\(a<b\), an expanded interval has a value of the form

\[
 L_a\cup\bigcup_{a<i<b}A_i\cup R_b,                       \tag{3.2}
\]

where \(L_a=A_a\), or \(L_a=T_a\) when \(a\) is split, and
\(R_b=A_b\), or \(R_b=Z_b\) when \(b\) is split.  At a singleton split
position the three possibilities are \(Z_r,T_r,X_r\); an unsplit singleton
has value \(A_r\).  These are all
possibilities: every interior block is either wholly included or absent,
and only the two endpoint blocks can be trimmed.

It follows that \(q\) added positions carry a task family exactly when one
can choose \(q\) actual host positions and decompositions
\(A_r=Z_r\cup T_r\) such that every task has enough distinct literal cells
among (3.2), the singleton cases, and unchanged old cells wholly outside
the displayed endpoint range.  For ordinary set coverage “enough”
means at least one cell.  For occurrence-labelled, cell-injective tasks it
is the Hall condition in the target-versus-trace-cell equality graph.

The local endpoint-ray certificate is the one-trimmed-end specialization of
(3.2).  Cross-host intervals give the two-trimmed-end values

\[
 T_a\cup\bigcup_{a<i<b}A_i\cup Z_b.                       \tag{3.3}
\]

Thus the set-cover number (2.3) alone is not enough for a \(+q\) result:
the exact ordered trace identities (3.2), and multiplicity Hall when
needed, are the additional and unavoidable condition.

## 4. Rotating-hole replay

In the frozen \(H=1\) rotating-hole family the old task-position letter is

\[
                         X=\{\epsilon\}\cup\tau.       \tag{4.1}

\]

Replace it by \(\{\epsilon\},\tau\).  The only genuinely new task needed is
the singleton \(\tau\).  The displaced old cell and the \(h-1\) alleged
casualties are old reference intervals containing \(X\), so block
contraction restores all of them automatically.  The replay confirms:

* source length rises by exactly one;
* every old physical interval has an injective equal-OR image;
* every one of the \(h-1\) plus-state casualties is restored;
* the complete rotating-hole owner sequence is unchanged; and
* owners crossing the split use deadline \(h+2\), while all others retain
  deadline \(h+1\).

Hence the earlier linear complete-damage ledger is a fixed-length/fixed-cell
phenomenon, not an additive-length obstruction.

## 5. Independent audit and exact scope

Run

```text
python3 scratch/audit_h2_split_letter_block_contraction_independent_20260801.py
```

The script independently exhausts all nonzero three-bit words of lengths at
most four (2,800 words and 75,166 ordered valid two-piece splits), checks
literal interval transport, verifies the complete one- and many-split trace
sets (3.1)--(3.3), and reconstructs the rotating-hole family for
\(2\le h\le64\).

This audit proves unrestricted interval-OR preservation and the
singleton-host criterion.  It does not prove inserted-source Johnson
adjacency, a flat derivative, fixed compiler-width admissibility, a global
Pascal-child host supply, or a common-cap assignment whose admissible cell
set excludes the longer transported intervals.
