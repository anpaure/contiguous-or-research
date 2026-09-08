# Gate C: factorial local deck entropy has a near-total common core

**Status (2026-08-22).**  Every assertion below is proved.  Starting from
the factor-adapted antipodal staircase tour, one may arbitrarily permute
`k` consecutive unused residue pairs, subject only to parity.  This gives

\[
 \lfloor k/2\rfloor!\,\lceil k/2\rceil!
   =\exp\{k\log k-k\log2-k+O(\log k)\}                 \tag{0.1}
\]

rooted coherent labellings, and every one loses at most `k(b-1)` more
factor flags than the staircase tour (up to one boundary row).

This factorial entropy does **not** solve the packing gate.  All those
labellings have exactly the same flag deck on `b-k-1` residue rows.  Their
factor intersections consequently share `q-o(q)` flags when `j,k=o(b)`.
Thus the natural local-permutation family has matching number one, despite
having enough parameter entropy when `k=c b/log b` and `c>log 4`.

Throughout,
\[
 n=2b,\qquad b\ge5\text{ odd},\qquad q=b(b-1).          \tag{0.2}
\]

## 1. The staircase base and a local residue interval

Let
\[
 X=\{b-1-4u:0\le u<j\}\subseteq\mathbb Z_b,
 \qquad 1\le j,\quad4j\le b-1,                         \tag{1.1}
\]
and let `tau_X` interchange `x` and `x+b` for every `x in X`, fixing all
other coordinates.  Applied to the descending Hamilton listing
\[
 H^*=(0,2b-1,2b-2,\ldots,1),                            \tag{1.2}
\]
this is the factor-adapted staircase tour.  Its intersection with the
Catalan-switched central flag factor `F*` in either phase has size
\[
 M_j=q-L_j,\qquad
 L_j=(4j+1)b-9j+2,                                     \tag{1.3}
\]
except that the last constant is `1` when `4j=b-1`.

Choose an ordinary, non-wrapping residue interval
\[
 S=\{a,a+1,\ldots,a+k-1\}\subseteq\{0,\ldots,b-1\},
 \qquad S\cap X=\varnothing,\quad a+k\le b.            \tag{1.4}
\]
Let `alpha` be any permutation of `S` which preserves parity, extended by
the identity off `S`.  Lift it antipodally, without changing layers:
\[
 \widehat\alpha(x)=\alpha(x),\qquad
 \widehat\alpha(x+b)=\alpha(x)+b\quad(0\le x<b).       \tag{1.5}
\]
Since `alpha(S)=S`, the sets `S` and `X` are disjoint, and `alpha` fixes
`X`, the two
coordinate permutations commute:
\[
 \widehat\alpha\tau_X=\tau_X\widehat\alpha.             \tag{1.6}
\]
Define the rooted directed Hamilton listing
\[
                         H_\alpha=\widehat\alpha\tau_X(H^*).    \tag{1.7}
\]

## 2. Exact row-deck invariance

For `r in Z_b`, put
\[
 I_r=\{r+u:0\le u\le b\}\subseteq\mathbb Z_{2b},
 \qquad
 Y_r=\{r+t:1\le t<b\}.                                 \tag{2.1}
\]
Here and below the displayed integers are read modulo `2b`.  The canonical
coherent row of the descending tour has full `(b+1)`-set `I_r`, allowed
deletion set `Y_r`, and predecessor arc `r->r-1`.  Hence the staircase
row has
\[
 S_r^X=\tau_X(I_r),\qquad Z_r^X=\tau_X(Y_r),\qquad
 \tau_X(r)\longrightarrow\tau_X(r-1).                 \tag{2.2}
\]

Call
\[
                         U=S\cup\{a+k\}\pmod b.         \tag{2.3}
\]
The extra residue is the successor of the interval.  Since `k<b`, one has
`|U|=k+1`.

### Lemma 2.1 (safe rows are identical as flag sets)

If `r notin U`, then
\[
 \widehat\alpha(I_r)=I_r,\qquad
 \widehat\alpha(Y_r)=Y_r,\qquad
 \widehat\alpha(r)=r,\qquad
 \widehat\alpha(r-1)=r-1.                              \tag{2.4}
\]
Consequently the complete `b-1`-flag row deck of `H_alpha` is exactly the
same **set of labelled flags** as the row deck of `tau_X(H*)`; only its
column parameter is permuted.

#### Proof

If `r<a`, the interval `I_r` contains the lower-layer copy of every
residue in `S` and no upper-layer copy; if `r>a+k`, it contains every
upper-layer copy and no lower-layer copy.  These are the only possibilities
when `r` lies outside `S union {a+k}`.  The lift `widehat alpha` permutes the selected
copy of `S` setwise, and therefore fixes `I_r` setwise.  Since neither
`r` nor `r-1` lies in `S`, removing the two copies of the endpoint pair
shows that it also fixes `Y_r` setwise and fixes the arc endpoints.  This
proves (2.4).

Now commute `widehat alpha` past `tau_X` using (1.6).  A base row flag
obtained by deleting `y in Z_r^X` has middle `S_r^X\{y}`.  After applying
`widehat alpha` it has the same arc and middle
\[
 S_r^X\setminus\{\widehat\alpha(y)\}.
\]
As `y` runs through `Z_r^X`, so does `widehat alpha(y)`.  Thus the entire
row deck, not merely its cardinality, is unchanged. \(\square\)

The same proof applies after translating the row by `b`.  The coherent
phase formula sends its `b` stages bijectively to residue rows
`r in Z_b`, although the chosen lift of a row may depend on the column.
Since each individual lift is invariant, Lemma 2.1 applies phase by phase.

### Theorem 2.2 (factor-overlap guarantee)

For every parity-preserving `alpha` supported on `S`, the intersection of
either coherent phase of `H_alpha` with `F*` has size at least
\[
 M_j-(k+1)(b-1),                                        \tag{2.5}
\]
and hence its loss from `q` is at most
\[
                         L_j+(k+1)(b-1)=O(b(j+k)).       \tag{2.6}
\]

#### Proof

All factor flags in the `b-k-1` safe rows survive literally by Lemma 2.1.
Discarding every flag in the other `k+1` rows can remove at most
`(k+1)(b-1)` of the `M_j` base factor flags. \(\square\)

## 3. Entropy and the common-core obstruction

Let `e` and `o` be the numbers of even and odd residues in `S`.  The number
of allowed permutations is
exactly
\[
                             e!o!.                       \tag{3.1}
\]
Since consecutive residues have alternating parity,
`{e,o}={floor(k/2),ceil(k/2)}`, and Stirling gives (0.1).  Distinct
`alpha` give distinct rooted Hamilton listings because `H*` contains every
coordinate once and `tau_X` is invertible.

At
\[
                         k={c b\over\log b}+O(1),        \tag{3.2}
\]
equation (0.1) becomes
\[
                         \log(e!o!)=(c+o(1))b.           \tag{3.3}
\]
Thus `c>log 4` supplies more than `4^b` times every fixed polynomial in
`b` rooted labellings for all sufficiently large `b`, while
`j,k=o(b)` keeps (2.6) equal to `o(q)`.

The same row identity proves that this entropy is unusable for a matching.
Let `C` be the set of base factor flags lying in the safe rows.  It is
independent of `alpha`, is contained in every factor intersection, and
satisfies
\[
 |C|\ge M_j-(k+1)(b-1)
      =q-L_j-(k+1)(b-1).                                \tag{3.4}
\]
Therefore, if `j,k=o(b)`, every two members share `q-o(q)` factor flags.
In particular no two full factor intersections in this family are
disjoint: its matching number is one.

This identifies the exact remaining diversity requirement.  A successful
Gate-C family must change a positive proportion of the row decks (or use a
different global factor/coverdown mechanism); factorially many column
relabelings inside only `o(b)` cut rows cannot be rounded into disjoint
near-tours.

## 4. Finite audit

The companion checker
`scratch/verify_gate_c_local_deck_entropy_common_core_20260822.py` verifies
commutation, exact safe-row deck equality, the phase overlap bound, the
common core, and the factorial count on exhaustive small instances.  It is
confirmatory; all general proofs are above.
