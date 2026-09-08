# A contractive-defect lift is enough for asymptotic optimality

## 1. Purpose

The previous suspension programme asked for an exact lift of a vertically
resolved wreath factor.  That is unnecessarily strong.  The width grows by
asymptotic factor four when two coordinates are added, whereas the number of
wreath blocks is smaller than the width by a linear factor.  Consequently a
dimension lift may:

* leave `O(Cat_m)` new seam defects at each controlled depth; and
* propagate every old defect into any fixed number `a<4` of new defects,

and still drive the normalized total defect to zero.

This note proves the precise reduction.  It is a theorem about what a lift
would imply; construction of such a lift remains the next combinatorial
task.

## 2. Wreath-shadow defect

Put

\[
 n_m=2m+1,\qquad
 W_m=\binom{2m+1}{m},\qquad
 C_m=\frac{W_m}{2m+1}=\operatorname {Cat}_m.
\]

A wreath factor `F_m` consists of `C_m` cyclic coordinate orders whose
cyclic `m`-intervals partition the middle layer.  For `q>=0`, let

\[
 M_{m,q}^-(F_m)
\]

be the number of rank-`m-q` sets which are not a cyclic interval in any
selected order, and define `M_(m,q)^+` analogously at rank `m+1+q`.  Write

\[
 E_{m,H}(F_m)
   =\sum_{q=0}^{H}\bigl(M_{m,q}^-(F_m)+M_{m,q}^+(F_m)\bigr).
\tag{2.1}
\]

The middle terms at `q=0` are zero (with the upper middle layer supplied by
complements), but retaining them makes the notation symmetric.

## 3. The contractive-lift hypothesis

Fix constants

\[
                         a<4,\qquad K<\infty.
\]

Call a family of maps `L_m` a **contractive Catalan lift** if, whenever
`H=o(m)` and `F_m` is a wreath factor, `L_m(F_m)` is a wreath factor in
dimension `2m+3` satisfying

\[
 E_{m+1,H}(L_m(F_m))
       \le a E_{m,H}(F_m)+K(H+1)C_m.                 \tag{3.1}
\]

No compatibility between lifts chosen for different final dimensions is
required.  The factor may be rebuilt separately for every `m`.

The additive term permits a bounded number of marked transversals per old
wreath and per controlled depth.  The coefficient `a` measures how many new
holes one old hole can produce.  Exact lifting would have `a=1,K=0`, but the
theorem below needs only `a<4`.

## 4. Defect-contraction theorem

### Theorem 1

If a contractive Catalan lift exists, then

\[
 \boxed{
   \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
 }
\tag{4.1}
\]

### Proof

It is enough first to treat odd dimensions.  Let `M` tend to infinity and
choose

\[
 H=\left\lceil\sqrt{M\,\omega(M)}\right\rceil,
 \qquad \omega(M)\longrightarrow\infty,
 \qquad \omega(M)=o(M).                              \tag{4.2}
\]

Start at `j_0=ceil(M/2)` with any exact middle wreath factor; the MSW factor
is available in every dimension.  Iterate the assumed lift from `j_0` to
`M`, always with the fixed depth `H`.  This is legitimate because
`H=o(j_0)`.

The exact width ratio is

\[
 R_j:=\frac{W_{j+1}}{W_j}
     =\frac{2(2j+3)}{j+2}
     =4-\frac2{j+2}.                                  \tag{4.3}
\]

Put `e_j=E_(j,H)/W_j`.  Dividing (3.1) by `W_(j+1)` gives

\[
 e_{j+1}
 \le \frac a{R_j}e_j
   +\frac{K(H+1)}{(2j+1)R_j}.                         \tag{4.4}
\]

Since `a<4`, there are `rho<1` and `j_1` such that `a/R_j<=rho` for
`j>=j_1`.  Also the second term in (4.4) is `O(H/j)`.  Iterating from
`j_0` yields

\[
 e_M
 \le \rho^{M-j_0}e_{j_0}
   +O\!\left(
       H\sum_{t=0}^{M-j_0-1}\frac{\rho^t}{M-t}
       \right)
 =o(1)+O(H/M)=o(1).                                  \tag{4.5}
\]

Here the crude initial bound `e_(j_0)<=2(H+1)` is enough, and its
contribution is killed exponentially.  Thus the final factor misses only
`o(W_M)` central-band targets in total.

Turn the factor into an OR word as follows.  For each selected cyclic order
`pi`, write the `n_M` cyclic intervals

\[
 I_\pi(i,M-H),\qquad i\in\mathbb Z_{n_M},             \tag{4.6}
\]

and repeat its first `2H+1` entries.  Consecutive unions in this block are
exactly all cyclic intervals of ranks `M-H,...,M+1+H`.  Across all `C_M`
wreaths the block length is

\[
 W_M+(2H+1)C_M=W_M+O(HW_M/M)=W_M+o(W_M).             \tag{4.7}
\]

Append every missing central-band target literally, costing `E_(M,H)=o(W_M)`.
Finally append the two-tail word from `TRUNCATED_IDEAL_PRODUCT.md`.  Because
`H^2/M=omega(M)->infinity`, that tail has length `o(W_M)`.  The resulting
word is universal and has length `W_M+o(W_M)`.

For the following even dimension use the trimmed one-bit lift.  Since

\[
 \nu(2M+2)\le2\nu(2M+1),\qquad
 \binom{2M+2}{M+1}=2\binom{2M+1}{M},                 \tag{4.8}
\]

the same asymptotic ratio holds.  The Sperner lower bound supplies the
opposite inequality, proving (4.1).  QED.

## 5. A stronger rankwise version

The scalar hypothesis (3.1) follows, for example, if a lift has bounded
banded propagation

\[
 M_{m+1,q}^{\epsilon}
 \le
 \sum_{|r-q|\le c}\sum_{\delta\in\{-,+\}}
       a_{q,r}^{\epsilon,\delta}M_{m,r}^{\delta}
 +K C_m,                                             \tag{5.1}
\]

where `c` is fixed and every column sum of the nonnegative propagation
matrix is at most some `a<4`.  Summing (5.1) over the band loses only `O(c)`
boundary depths, which may be absorbed into the additive
`O((H+1)C_m)` term.

This is the appropriate format for auditing a grid-shuffle construction:
one does not need exact equality of every positional flag.  One needs only
to tabulate how a missing old flag propagates and to count the marked seam
families.

## 6. Consequence for the current Catalan seam programme

The coordinate-cut shuffle currently under study appears to transport all
bulk flags and leave only a bounded list of marked transversals per old
complementary path: the cut vertex, the flip upper/lower colour, and a bounded
number of corner flags.  Such a table would give precisely the additive
term in (3.1).

The decisive remaining audit is now much weaker than exact Haar suspension:

> Prove that the cut/grid-shuffle lift completes to a new wreath factor and
> that the total number of descendants of one old missing flag is uniformly
> less than four.

If that statement holds, Theorem 1 proves asymptotic optimality even if no
individual lifted factor is vertically perfect and even if the finite
`m=4` Haar edge itself has no pointwise lift.

## 7. Repair cost is weaker than missing-mask count

The scalar defect `E_(m,H)` is still stronger than the OR problem requires.
Several missing targets may be the interval ORs of one short auxiliary word.
Define

\[
 R_{m,H}(F_m)
\tag{7.1}
\]

to be the minimum length of a set-valued word whose interval unions contain
every central-band target missing from the wreath shadows of `F_m`.  The word
is allowed to contain arbitrary additional masks.  Certainly

\[
                         R_{m,H}(F_m)\le E_{m,H}(F_m),             \tag{7.2}
\]

by listing missing targets literally, but the inequality can be very far
from equality.

### Theorem 2 (contractive repair lift)

The conclusion of Theorem 1 remains valid if (3.1) is replaced by

\[
 R_{m+1,H}(L_m(F_m))
    \le aR_{m,H}(F_m)+K(H+1)C_m,
 \qquad a<4.                                      \tag{7.3}
\]

### Proof

Repeat the proof of Theorem 1 with

\[
                         r_j=R_{j,H}(F_j)/W_j.
\]

The initial bound `r_(j_0)<=2(H+1)` again follows by literal listing.  After
division by `W_(j+1)`, recurrence (7.3) is identical to (4.4), so
`R_(M,H)=o(W_M)`.  Concatenate the erosion blocks (4.6), one optimal repair
word witnessing (7.1), and the truncated outer-tail word.  These three parts
cover the whole Boolean lattice and have total length `W_M+o(W_M)`.  The
even-dimensional transfer is unchanged.  QED.

### Why this matters at a coordinate cut

At depth `q`, a raw cut audit sees `Theta(q)` windows crossing one marked
seam.  Summing their *number* through depth `H` gives

\[
                         \Theta(H^2 C_m),                         \tag{7.4}
\]

which is too large: after normalization it is `Theta(H^2/m)`, while the
tail construction requires `H^2/m -> infinity`.

However, all crossing windows at all depths form a triangular family of
subintervals of an `O(H)`-neighbourhood of the seam.  If the grid/cap lift
labels that neighbourhood by a word `G_P` of length `O(H)` for each old
complementary path `P`, then every one of the `Theta(H^2)` seam targets is
already an interval OR of `G_P`.  Concatenating these local halo words costs
only

\[
                         O(HC_m),                                  \tag{7.5}

exactly the additive term permitted in (7.3).

Thus the next local statement should be formulated as a **seam-halo lemma**,
not as an injective completion of every crossing shadow:

> For each coordinate-cut product path, exhibit one `O(H)`-entry word whose
> interval unions contain every unresolved central-band cut and corner flag.

Together with a two-section lift of an old repair word, this would give
`a=2` in (7.3), while the width ratio is `4-O(1/m)`.

The purely word-theoretic part of that lemma is automatic.

### Lemma 3 (cut-halo compression)

Let `A=(A_1,...,A_N)` be any set-valued word, let `C` be a set of cuts
between consecutive entries, and let `L>=1`.  All OR values of length-at-most
`L` intervals which cross at least one cut in `C` can be covered by an
auxiliary word of length at most

\[
                              2L|C|.                              \tag{7.6}
\]

### Proof

For a cut after position `c`, append the halo

\[
 A_{\max(1,c-L+1)},\ldots,A_{\min(N,c+L)}.            \tag{7.7}
\]

It has at most `2L` entries.  Every interval of length at most `L` crossing
that cut is a contiguous subinterval of (7.7), so its OR is retained.
Concatenate one halo for every cut.  Previously represented values survive
concatenation, proving (7.6).  QED.

Consequently the grid audit need only prove a **provenance statement**:
every unresolved cut/corner target must already be a bounded-length window
of one raw pre-splice word.  Once that provenance is explicit, Lemma 3
compresses all `Theta(H^2)` individually counted targets to `O(H)` physical
entries per path with no matching or injectivity requirement.

The inherited part is equally elementary once the section count is known.

### Lemma 4 (tagged repair transport)

Let `R=(R_1,...,R_t)` cover a target family `X` by interval ORs, and let
`Z_1,...,Z_b` be fixed masks on new coordinates, disjoint from the old
ground set.  Then the concatenation of the `b` tagged copies

\[
 (Z_j\cup R_1,\ldots,Z_j\cup R_t),\qquad 1\le j\le b, \tag{7.8}
\]

has length `bt` and covers every target in

\[
                    \{Z_j\cup S:S\in X,\ 1\le j\le b\}.           \tag{7.9}
\]

### Proof

Use in the `j`th copy the same witness interval which represented `S` in
`R`.  Its new union is exactly `Z_j union S`.  QED.

Thus if the coordinate-cut lift sends every inherited hole into at most two
fixed endpoint sections, Lemma 4 gives the coefficient `a=2` required in
(7.3).  The remaining work is entirely structural: certify that no third or
fourth descendant sector is omitted, and give raw-window provenance for the
bounded list of seam and corner families.
