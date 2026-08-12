# Independent audit of the phase-compatible paired Kneser block bank

Date: 2026-08-01  
Audited source:
`MATH_THEOREM_CATALAN_PHASE_COMPATIBLE_PAIRED_KNESER_BLOCK_BANK_20260801.md`,
SHA-256
`ad5ecaa099598763e28a98b1c5fbd4cc101e667b5d8a1e95a27ac7747c29913a`.

Status: **PASS for the asymptotic resource-disjoint packet bank and exact
endpoint ledger, after the source's correction from a cyclic translate to
a uniform coordinate permutation in the odd case.**  Here
"phase-compatible" means that every packet plants the three literal local
C-phase incidence rows.  Extension of all planted rows to one common
perfect owner basis, membership of all central covers in one SCD, and the
decorated two-factor are not consequences of the resource count.

## 1. Raw blocks and exact resource loads

Let `|G|=2r+1`, let

\[
 N={2r+1\choose r},
\]

and let a flagged block consist of an unordered Kneser edge `{S,J}` and
flags `b in J`, `d in S`.  There are `N(r+1)/2` Kneser edges and `r^2`
flag pairs per edge, hence

\[
 B_0={N(r+1)r^2\over2}.
\]

A fixed central `r`-set has `r+1` Kneser neighbours and `r^2` flag pairs,
so its occurrence load is exactly

\[
 \mu_r=(r+1)r^2.
\]

For a fixed `(r+1)`-set `R`, the equality `L_S=R` fixes the opposite
endpoint and leaves `r+1` choices of `S` and `r^2` flags.  Thus the
`L`-load is `(r+1)r^2`.  For `V_S=R`, choose the deleted point of `R`,
the compatible opposite endpoint, and the reverse flag; the count is
again `(r+1)r^2`.  Consequently the combined `L/V` load is in fact
exactly

\[
 \mu_{r+1}=2(r+1)r^2.
\]

For fixed `Q in binom(G,r-1)`, choose `b in G-Q` in `r+2` ways, the
opposite Kneser endpoint in `r+1` ways, and its reverse flag in `r` ways.
Therefore

\[
 \mu_{r-1}=(r+2)(r+1)r.
\]

Each block exposes `2,4,2` resources in these three ranks.  The union
bound therefore gives

\[
 \Delta_{\rm blk}
 \le2\mu_r+4\mu_{r+1}+2\mu_{r-1}
 =4r(r+1)(3r+1).
\]

This is a safe maximum conflict-degree bound; multiple shared resources
only make the union bound looser.

An independent exhaustive enumeration for `r=2,3,4,5` gave

\[
\begin{array}{c|rrrr|c}
r&B_0&\mu_r&\mu_{r+1}&\mu_{r-1}&
 \text{all eight within-block resources distinct}\\
2&60&12&24&24&\text{yes}\\
3&630&36&72&60&\text{yes}\\
4&5040&80&160&120&\text{yes}\\
5&34650&150&300&210&\text{yes}.
\end{array}
\]

These finite values are only a count audit, not evidence for a residual
decorated completion.

## 2. The greedy asymptotic row

For the balanced hole family the forbidden one-special central core bank
has

\[
 f\le4\operatorname {Cat}_{m-1}-C={3C\over2r+3}.
\]

Deleting all blocks incident with it removes at most `f mu_r` blocks.  A
greedy selection of `t=C/2` blocks then succeeds whenever

\[
 f\mu_r+t(\Delta_{\rm blk}+1)<B_0.                 \tag{2.1}
\]

Using

\[
 {C\over N}={4(2r+3)\over(r+2)(r+3)},
\]

the two normalized terms are bounded exactly by

\[
 {f\mu_r\over B_0}\le {24\over(r+2)(r+3)},
\]

and

\[
 {t(\Delta_{\rm blk}+1)\over B_0}
 \le {C\over N}
 \left({4(3r+1)\over r}+{1\over(r+1)r^2}\right).
\]

They are `O(r^-2)` and `O(r^-1)`, respectively, so (2.1) holds for all
sufficiently large `r`.  For calibration, direct simplification of this
particular sufficient inequality has numerator

\[
 r^5-90r^4-285r^3-242r^2-56r-12,
\]

which is positive for every `r>=94`.  This is only a crude threshold for
the displayed greedy proof, not a claimed sharp existence threshold.

The separate pigeonhole check also passes:

\[
 2C\le N
 \quad\Longleftrightarrow\quad
 8(2m-1)\le m(m+1),
\]

which first holds at `m=15`.  Thus the abandoned shared-signature finite
instances through `m=9` really are impossible for that reason, whereas
the separate-target paired bank is an asymptotic construction.

## 3. Typed resources

For the `S` side,

\[
 U_S=L_S+b=G-Q_S,
\]

and similarly on the `J` side.  Hence distinct `Q` resources are exactly
what is needed to make the `U` cores distinct.  The outer labels
`alpha,beta` separate the two target shores.  Distinct combined `L/V`
resources make all same-signature old and new owner cores distinct, while
distinct `S,J` separate the lower banks and the two-special middle-owner
bank.  Auxiliary uppers contain both special letters and therefore cannot
collide with either one-special target shore.

Thus the three abstract resource rows in the source really do imply all
literal upper, lower, and physical-owner noncollision rows in its displayed
two-packet replacement.  No extra `U` collision row is missing.

They do **not**, however, imply a common rooted basis.  Every packet plants
the three rows

\[
 aS\mapsto aL,
 \qquad zS\mapsto azS,
 \qquad L\mapsto zL,
\]

with `a,z` swapped on the opposite stratum.  Resource disjointness proves
that these `3C` prescriptions form a partial incidence matching.  It does
not prove that the partial matching extends to a perfect matching.  The
source's residual Hall condition is the exact missing row, and arbitrary
selected covers `S<L` also need not be edges of one common SCD.

## 4. Odd seed

For the standard odd Kneser cycle, the banks `S_s,L_s,V_s,Q_s` are each
injective and `L` is disjoint from `V`.  One quick invariant is the cyclic
gap word: `L_s` is an interval, `V_s` has the prescribed interior gap, and
for `r>=3`, `Q_s` has one gap of length `2` and one of length `r+2`, which
anchors its start.  The case `r=2` is immediate.  Direct enumeration also
passed for every `2<=r<=19`.

The original phrase "random cyclic translate" would have been false: the
full cyclic-interval vertex bank is invariant under cyclic translation.
The revised source correctly uses a uniformly random coordinate
permutation.  Each one of the `2r+1` seed vertices is then uniform in
`binom(G,r)`, so linearity of expectation gives

\[
 \mathbb E|P_{\rm seed}\cap\mathcal F|
 ={(2r+1)|\mathcal F|\over N}=O(r^{-1})<1.
\]

Therefore some relabelled seed avoids the forbidden bank.  Relabelling
preserves every disjointness and injectivity property.  Reserving its
`O(r)` resources deletes only `O(r Delta_blk)` further raw paired blocks,
which is negligible compared with `B_0`.  Since both `C` and `2r+1` are
odd, the remaining packet count is even, and the stratum labels can be
balanced to differ by one.

## 5. Verdict and exact remaining gate

The revised theorem proves an asymptotic, resource-disjoint,
separate-target two-stratum packet bank with the exact endpoint-hole
cocycle.  It does not prove a fixed-`M_0`/single-SCD bank, residual
matching, cycle-hit decorated factor, residence, higher-shadow, or
compiler statement.  Any later use must retain those qualifications.
