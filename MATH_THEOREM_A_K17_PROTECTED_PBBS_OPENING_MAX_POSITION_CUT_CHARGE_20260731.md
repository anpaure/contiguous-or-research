# Protected PBBS openings: exact cut collars and max-position staircase charge

Date: 2026-07-31  
Status: exact theorem and a canonical-tail no-go for the frozen 11-cycle factor  
Scope: protected rethreads which delete old factor edges, retain every other
old edge, and reconnect the resulting segments by literal Johnson seams

## 0. Verdict

The staircase charge of opening a PBBS factor is not its number of cycles,
cuts, or new seams.  After the cuts and orientations are fixed, it is exactly
the maximum absolute start position of the surviving and seam-created short
runs.

This note proves three statements.

1. A deleted rank-`r` Johnson edge can boundary-touch at most `r+1`
   coordinate-labelled cyclic positive runs.  Hence `p` protected cuts can
   destroy at most `(r+1)p` old short-run occurrences.
2. Once seam-created short runs are excluded, exact canonical-tail
   feasibility is a two-deadline single-machine ordering problem.  For a
   complete seam-safe compatibility graph it is decided exactly by earliest
   deadline order, not by a seam count.
3. For the frozen K17 11-cycle double-q1 factor, nine cycles of total length
   24,300 retain an internal run two after every possible single cut.  In any
   whole-cycle opening, the last of those nine blocks starts at position at
   least

   \[
                         24300-5536=18764.
   \]

   Its surviving run two begins at position at least 18,765.  Therefore

   \[
             \rho_2\ge18765,\qquad \rho_3\ge18765,
             \qquad \rho_2+\rho_3\ge37530>7401.       \tag{0.1}
   \]

Thus **one cut per old cycle, with every cycle retained as one block, is
canonically staircase-impossible** for this factor, irrespective of the
new seams.  This does not exclude arbitrary omitted starts, extra protected
cuts, or alternating switches which change old internal edges.

## 1. Cyclic run collars

Let

\[
                 C=(v_0,v_1,\ldots,v_{m-1})
\]

be a cycle in `J(k,r)`, with edge `e_i=v_iv_{i+1}` and indices modulo `m`.
For a coordinate `x`, let

\[
               R=(v_a,v_{a+1},\ldots,v_{a+ell-1})
\]

be a coordinate-labelled maximal cyclic positive run.  Its **cut collar** is

\[
       \Gamma(R)=\{e_{a-1},e_a,\ldots,e_{a+ell-1}\}.   \tag{1.1}
\]

It consists of the two boundary edges and the `ell-1` internal edges.

### Lemma 1.1 (exact cut-collar criterion)

Delete a set `D` of old cycle edges and retain every other old edge.  The old
occurrence `R` remains an interior maximal run of length `ell` in one of the
resulting segments if and only if

\[
                         D\cap\Gamma(R)=\varnothing.    \tag{1.2}
\]

If (1.2) fails, pieces of `R` may still participate in a new short run after
the segments are reconnected, but that is a seam-created occurrence rather
than the untouched old occurrence.

#### Proof

If no collar edge is deleted, the run, its two zero neighbours, and all
edges between them lie in one segment, so the same interior maximal run
survives.  If a boundary collar edge is deleted, the run touches a segment
endpoint.  If an internal collar edge is deleted, the run is split between
two segment endpoints.  In either case it is no longer an interior old
occurrence.  These alternatives exhaust the collar.  \(\square\)

### Lemma 1.2 (rank-`r` cut capacity)

One deleted edge of `J(k,r)` belongs to the collars of at most `r+1`
coordinate-labelled cyclic positive runs, of all lengths combined.

#### Proof

Write the endpoints as `A,B`.  A coordinate run can meet the deleted edge
only if its coordinate belongs to \(A\cup B\).  For each such coordinate,
the one or two positive endpoints lie in one unique maximal cyclic positive
run.  Since a Johnson edge has

\[
                            |A\cup B|=r+1,
\]

there are at most `r+1` incident run occurrences.  \(\square\)

## 2. Count charge of a protected rethread

Let a 2-factor have `N_2` cyclic run-two occurrences and `N_3` cyclic
run-three occurrences.  Delete `p` old edges, hitting every old cycle at
least once, and reconnect the resulting `p` segments to one path.  Let
`d_i` be the number of old length-`i` occurrences whose collars meet a
deleted edge.

### Theorem 2.1 (survivor and canonical charge)

Every resulting path has

\[
 d_2+d_3\le (r+1)p,                                  \tag{2.1}
\]

\[
 n_2\ge N_2-d_2,qquad n_3\ge N_3-d_3,               \tag{2.2}
\]

where `n_i` counts final interior short runs.  If the final path is a
Johnson path, then its canonical frontiers satisfy

\[
 \rho_2+\rho_3
   \ge 2(N_2-d_2)+(N_3-d_3).                         \tag{2.3}
\]

Consequently, putting `C=(r+1)p`,

\[
\begin{split}
 \rho_2+\rho_3\ge{}&2N_2+N_3
       -2\min(N_2,C)\\
      &-\min\bigl(N_3,(C-N_2)_+\bigr).               \tag{2.4}
\end{split}
\]

Also

\[
             n_2+n_3\ge (N_2+N_3-C)_+.              \tag{2.5}
\]

In particular, zero short-run loss requires

\[
                  p\ge\left\lceil{N_2+N_3\over r+1}\right\rceil. \tag{2.6}
\]

#### Proof

Lemma 1.2 gives (2.1), and Lemma 1.1 gives (2.2); new seam runs can only
increase the final counts.  Distinct positive runs of a Johnson path have
distinct start edges, because an oriented Johnson edge inserts only one
coordinate.  Hence \(\rho_2\ge n_2\) and
\(\rho_3\ge n_2+n_3\), proving (2.3).
For fixed total cut capacity, the largest removable weight `2d_2+d_3` is
obtained by hitting run-two occurrences first.  This gives (2.4).
Equations (2.5) and (2.6) follow directly from (2.1).  \(\square\)

The inequalities are cut-capacity bounds, not constructions.  A cut may
spend capacity on a long run, several cuts may hit the same occurrence, and
the new seams may create additional short runs.

## 3. Exact max-position decomposition

After all old cuts, orient the resulting blocks as

\[
                 B_i=(w_{i,0},\ldots,w_{i,m_i-1}).
\]

For `j=2,3`, define the internal frontier `h_{ij}` to be the largest local
start of an interior positive run of length at most `j` in `B_i`; use
\(h_{ij}=-\infty\) when no such run exists.  For a block order \(\pi\), put

\[
                 b_t=\sum_{s<t}m_{\pi(s)}.            \tag{3.1}
\]

Let `kappa_j(pi)` be the largest global start of a length-at-most-`j` run
meeting at least one new seam, again \(-\infty\) if none.  It is computed
exactly by the capped prefix/suffix/all-one run-summary product.

### Theorem 3.1 (exact opening charge)

For the final concatenated path,

\[
 \boxed{\rho_j=
   \max\left(0,\ \max_t\{b_t+h_{\pi(t),j}\},\ \kappa_j(\pi)\right)}
       \qquad(j=2,3).}                                \tag{3.2}
\]

Thus, when run one is excluded by lower-colour simplicity, the exact
canonical staircase charge is the sum of the two maxima in (3.2).

#### Proof

Every final short run is either wholly internal to one opened block or
meets a new seam.  The first class has global start `b_t+h`; the second is
exactly the class defining `kappa_j`.  Taking the maximum is therefore
literal and exhaustive.  \(\square\)

This is why charging `O(1)` per seam is unsound.  One late seam-created run
can cost nearly `W` in (3.2), while arbitrarily many early seams can cost
nothing beyond an already larger frontier.

### Corollary 3.2 (zero-loss criterion)

Assume the old factor and final path have no run one, as is forced by the
lower-rainbow condition.  A protected rethread has
\(\rho_2=\rho_3=0\) if and only if

1. every old cyclic run of length two or three has a deleted edge in its
   collar; and
2. the final capped run-summary product creates no interior run of length
   two or three across the new seams.

If every opened block has length at least four, condition 2 is pair-local:
a run of length at most three cannot cross two seams.  Blocks of length at
most three require the full two-/three-seam summary, or must first be
contracted into compound blocks.

For a block \(B\) and coordinate \(x\), let \(r_x(B)\) be the length of
its terminal positive run, capped at four, and let \(l_x(B)\) be the
analogous capped initial length.  A zero endpoint gives length zero.

### Lemma 3.3 (exact one-seam guard)

Let \(B,C\) both have length at least four.  The seam \(B\mid C\) creates
no interior positive run of length at most three meeting that seam if and
only if, for every coordinate \(x\),

\[
       r_x(B)+l_x(C)=0
       \quad\hbox{or}\quad
       r_x(B)+l_x(C)\ge4.                            \tag{3.3}
\]

#### Proof

If both seam endpoints omit \(x\), no positive run meets the seam.  In
every other case the unique positive run meeting the seam consists of the
terminal positive arm of \(B\), when nonempty, followed by the initial
positive arm of \(C\), when nonempty.  If its total is at most three, both
arms are known exactly by their capped lengths and the run is interior at
this global seam.  A capped value four already certifies total length at
least four.  This proves (3.3).  \(\square\)

### Corollary 3.4 (exact zero-loss cut-selection graph)

Suppose every opened cycle has length at least four.  For cycle \(C_i\),
let \({\cal A}_i\) be its allowed protected cut edges and put

\[
 {\cal K}_i={\cal A}_i\cap
     \bigcap_{R\in{\cal R}_{2,3}(C_i)}\Gamma(R),       \tag{3.4}
\]

where the intersection is over all coordinate-labelled cyclic runs of
length two or three.  Make a directed graph whose states are the two
orientations of every cut \(e\in{\cal K}_i\).  Join a state of \(C_i\) to
a state of \(C_j\) when the resulting endpoint seam is protected-legal and
passes (3.3).

A one-cut-per-cycle staircase-zero opening exists if and only if this graph
has a directed Hamilton path selecting exactly one state from each cycle.
If seam colours or other resources are globally constrained, the selected
arcs must additionally satisfy those global constraints; they are not
encoded by pairwise adjacency alone.

#### Proof

Lemma 1.1 says that a zero-loss opening must choose its cut from
\({\cal K}_i\), and Lemma 3.3 says that its consecutive oriented states are
arcs of the displayed graph.  This proves necessity.  Conversely, the cut
condition leaves no internal old short run, and every selected graph arc is
short-safe.  Since all blocks have length at least four, no short run can
cross two seams.  The selected transversal Hamilton path therefore has zero
staircase loss.  Pair-local protected legality is inherited from its arcs;
any stated global resource condition is inherited from the additionally
required arc-set constraint.  \(\square\)

For a cycle of length at most three, replace its state by the exact compound
state including one or both neighbours; a pairwise graph on the uncontracted
short cycle is not exact.

## 4. Exact deadline theorem when seams are fail-closed

Assume every block has length at least four; shorter blocks may first be
contracted with fixed neighbours into compound blocks whose internal summary
is carried exactly.  For an internal frontier put

\[
 d_{ij}=m_i-h_{ij},                                  \tag{4.1}
\]

and put \(d_{ij}=+\infty\) when \(h_{ij}=-\infty\).  If block `i` completes
at global time `C_i`, its internal contribution is

\[
                         C_i-d_{ij}.                  \tag{4.2}
\]

Fix integers \(0\le R_2\le R_3\) with
\(R_2+R_3\le\Delta\), and define the completion
deadline

\[
             D_i(R_2,R_3)=
             \min\{R_2+d_{i2},\ R_3+d_{i3}\}.        \tag{4.3}
\]

### Theorem 4.1 (earliest-deadline opening theorem)

Suppose every ordered pair of the chosen oriented blocks is an allowed seam
whose two-block trace creates no short run across that seam.  Because every
block has length at least four, no length-at-most-three run can cross two
seams, so every block order is globally fail-closed.  There exists a block
order with

\[
                       \rho_2\le R_2,qquad \rho_3\le R_3 \tag{4.4}
\]

if and only if ordering the blocks by nondecreasing `D_i(R_2,R_3)` gives

\[
                 \sum_{s\le t}m_{\pi(s)}
                    \le D_{\pi(t)}(R_2,R_3)           \tag{4.5}
\]

for every prefix `t`.

#### Proof

By (4.2), (4.4) is equivalent to the ordinary completion-deadline
constraints \(C_i\le D_i\).  With all jobs available at time zero and no useful
idle time, the standard adjacent-inversion exchange puts any feasible order
into nondecreasing deadline order without violating a deadline: if
`D_i>D_j` but `i` precedes `j`, swapping them makes `j` finish no later than
the old completion of `j`, hence by `D_j`, while `i` then finishes at the
same time the old `j` finished, hence by `D_j<D_i`.  Iteration proves the
criterion.  \(\square\)

For a restricted protected-seam digraph on these length-at-least-four
blocks, (4.5) remains the exact deadline attached to each block, but the
remaining object is a directed Hamilton path respecting all prefix
deadlines.  Earliest-deadline sorting is then only a relaxation unless its
consecutive pairs are allowed seams.  Uncontracted blocks of length at most
three require the full summary state in addition to that digraph.
Global rainbow, upper-witness, or owner-resource constraints remain an
intersection with this staircase theorem; pairwise seam availability does
not enforce them.

## 5. Frozen K17 consequences

### 5.1 The protected 11-cycle double-q1 factor

The source is

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components
SHA-256 3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e
```

It has `N_2=2025`, `N_3=1221`, and `p=11` under one-cut-per-cycle opening.
Theorem 2.1 gives

\[
 n_2+n_3\ge3136,qquad \rho_2+\rho_3\ge5051.          \tag{5.1}
\]

Thus count capacity alone does not refute the K17 budget 7,401, but zero
loss would require at least

\[
                         \lceil3246/10\rceil=325       \tag{5.2}
\]

old-edge deletions, not eleven.

The exact collar census is

```text
scratch/audit_k17_pbbs_protected_opening_cut_collars_20260731.py
SHA-256 a92fd4951d55e7d520a31de40d39cb211b6acfba0a8bd978c21639624950a3e4
scratch/k17_pbbs_protected_opening_cut_collars_20260731.audit.json
SHA-256 725e826c145f403d4e248c25a3572e5e8eecb683084af6f41e41660d60cd2333
payload 379f5d2c13b35a892b1ee0f4be888bb420695c0fe3e24ceab1feea12146f3313
```

Only the cycles of lengths seven and three admit a cut hitting every old
run two.  The other nine cycles have total length 24,300, and the largest
has length 5,536.  Lemma 1.1 therefore proves (0.1): in any whole-cycle
order, the last run-two-dirty block starts after at least 18,764 preceding
vertices and contains a surviving run two at local start at least one.

### 5.2 The 989-cycle lower-perfect tripleflow factor

The frozen census has

\[
                N_2=7887,\qquad N_3=7940,qquad p=989.
\]

Here Theorem 2.1 gives

\[
             n_2+n_3\ge5937,qquad
             \rho_2+\rho_3\ge5937.                  \tag{5.3}
\]

and zero loss requires at least

\[
                         \lceil15827/10\rceil=1583    \tag{5.4}
\]

cuts.  The lower bound 5,937 is below 7,401, so it is not a
\(\Delta\)-obstruction.  The exact remaining canonical question is whether
allowed protected cuts and seams admit summaries satisfying Theorem 4.1 or
the restricted deadline-Hamilton condition after seam events are included.

## 6. Exact boundary

The following are proved:

* the collar condition for every retained old short occurrence;
* the `(r+1)p` cut-capacity law;
* the exact max-position decomposition;
* the earliest-deadline theorem under complete fail-closed seam
  compatibility; and
* the canonical-tail no-go (0.1) for the frozen 11-cycle whole-block
  opening.

The following remain open:

* an arbitrary-start schedule, where late runs can be shielded and the full
  adjusted-frontier loss must replace (4.4);
* a multi-cut protected segmentation with enough legal lower/upper colours;
* a deadline-compatible Hamilton path in the actual protected seam graph;
* seam-created run summaries, especially through the length-three cycle;
  and
* the lower common-cap compiler.

Accordingly, protected PBBS opening is neither proved nor globally
refuted.  What is refuted is the zero-loss intuition and, for the frozen
11-cycle factor, every canonical-tail construction that opens each old cycle
only once and otherwise keeps it as one block.
