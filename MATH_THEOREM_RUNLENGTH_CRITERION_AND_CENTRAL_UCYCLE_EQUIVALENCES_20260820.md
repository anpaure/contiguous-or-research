# The run-length criterion for asymptotic coefficient one, and the exact identification of the central layer problem with the wreath conjecture and central universal cycles

Date: 2026-08-20.
Status: new theorems with complete proofs (Theorems A, B, C, D, E and
Lemmas 1–6), one sharp new conditional criterion (Corollary B2), and a
calibrated identification of the remaining open core with two named
literature problems.  No computation was used; every numbered claim here is
proved in this file or cited to a specific prior theorem file of this
project or to the literature.

Throughout, `n=2m+1` is odd, `W=W(n)=binom(n,m)`,
`Cat_m=binom(2m,m)/(m+1)`, and `nu(n)` is as in `MASTER_HANDOFF.md`
Section 1.  We use `binom(n,m)=(2m+1)/(m+1)·binom(2m,m)=(2m+1)·Cat_m`,
i.e.

\[
n\cdot \mathrm{Cat}_m=\binom{n}{m}=W. \tag{0.1}
\]

This identity, which is the cycle lemma count, silently organizes the whole
central problem and is used repeatedly below.

## 0. Summary of what is new

1. **Theorem A (far-rank absorption).**  All targets whose rank differs
   from the middle by more than `H` can be appended verbatim, one letter
   per target, at total cost `2^{n+1}e^{-2H^2/n}`; this is `o(W)` exactly
   when `H >= (1/2+eps)sqrt(n ln n)`.  Consequently the full-cube problem
   at coefficient one is *equivalent* to the band problem at half-width
   `H* = Theta(sqrt(n log n))`, and no per-target repair scheme can push
   below that scale (Remark A3).  This locates the precise threshold that
   conjectures 7.2.6–7.2.7 of the master handoff are fighting: their scale
   `sqrt(m log log m)` is below `H*`, which is why they need batched
   (non-per-target) repair economics.

2. **Theorem B and Corollary B2 (the run-length criterion).**  Combining
   Theorem A with the already-proved PBBS collar ledger (equation (2.2) of
   `MATH_PBBS_FLAG_FACTOR_AND_FALSE_CONNECTOR_GATE_20260728.md`) gives, at
   `H=ceil(sqrt(n ln n))`:

   \[
   \nu(2m+1)\ \le\ W\Bigl(1+2\sqrt{\tfrac{\ln n}{n}}(1+o(1))\Bigr)
   +2(5H-1)\,\nu_H(P_m)+O\!\bigl(Wn^{-3/2}\bigr).
   \]

   Hence **if the canonical PBBS cycle cover satisfies
   `nu_H(P_m)=o(W/sqrt(n log n))` at `H=ceil(sqrt(n ln n))`, then
   `nu(k)=(1+o(1))W(k)` for all `k`** — the full asymptotic
   coefficient-one conjecture (handoff 7.1.3).  The entire conjecture is
   thereby reduced to a tail bound on the residence-run-length spectrum of
   one explicit permutation.  A geometric (memoryless) run-length tail
   would *fail* this criterion by exactly a factor `Theta(log n)`
   (Remark B3); so the criterion is genuinely at the edge, and it
   quantifies precisely how much better than memoryless the PBBS runs must
   be.

3. **Theorem C (defective central covering suffices; the singleton
   route).**  A second, PBBS-independent route: a cyclic singleton word of
   length `(1+o(1))W` with the gap property, whose length-`l` windows
   cover all but `o(W)` (summed over the band) of the rank-`l` targets for
   every band rank `l`, also implies coefficient one.  This strictly
   weakens handoff conjecture 7.2.5: the partition-into-chains and the
   thresholds are replaced by mere defective *covering*; multiplicity,
   chain structure, and exactness are all dropped, because surplus interval
   unions are logically harmless in this problem.

4. **Theorem D (the middle-levels lift).**  A doubly-exact central
   universal cycle (a cyclic word over singletons of `[n]` of length `W`
   whose `m`-windows enumerate `binom([n],m)` and whose `(m+1)`-windows
   enumerate `binom([n],m+1)`) exists **iff** the middle-levels graph
   `ML(2m+1)` has a Hamilton cycle
   `U_1 ⊂ V_1 ⊃ U_2 ⊂ V_2 ⊃ …` satisfying the shift condition

   \[
   b_j=a_{j-m}\quad\text{for all }j\ (\mathrm{mod}\ W),
   \]

   where `a_j=V_j∖U_j` is the entering element and `b_j=V_j∖U_{j+1}` the
   leaving element.  Every element then appears exactly `Cat_m` times and
   every dwell has length exactly `m` (FIFO discipline).  By Mütze's
   middle-levels theorem the *unconstrained* Hamilton cycles exist in
   abundance; the entire difficulty of the central Chung–Diaconis–Graham
   problem is the shift condition.  We could not locate this equivalence
   stated in the literature; the forward direction is folklore-adjacent,
   the converse (including the automatic derivation of the gap property
   and the exact-`m` dwell law) appears to be new.

5. **Lemma 5 (seam cleanliness = endpoint age sum).**  For words factored
   into full permutation passes, all `m-1` seam-crossing middle windows
   between consecutive passes `sigma, sigma'` are clean **iff** every
   element `x` satisfies

   \[
   \mathrm{age}_\sigma(x)+\mathrm{pos}_{\sigma'}(x)\ \ge\ m+1,
   \]

   where `age` is position from the right end of `sigma` and `pos` from
   the left end of `sigma'`.  This is structurally the same inequality as
   the endpoint-age matching test of
   `MATH_THEOREM_COMPLEMENTARY_AGE_CROSS_STRATUM_COLLARS_20260804.md`,
   confirming that the residence-collar calculus and the seam calculus are
   one and the same constraint seen from two sides.

6. **Theorem E (factor-2 seam law).**  In any pass-factored word of total
   length `(1+delta)W`, in-pass windows can cover at most
   `(1+delta)(1/2+3/(4m))W` middle targets; hence any pass-factored word
   achieving `(1-o(1))`-coverage of the middle layer must extract
   `(1/2-o(1))W` *distinct, fresh* middle sets from its seams, and a
   `(1-o(1))`-fraction of all seams must be entirely clean in the sense of
   Lemma 5.  In particular the Baranyai–Katona wreath conjecture, even if
   fully true, does not by itself produce a coefficient-one word: the
   opened wreaths lose exactly half the layer, and seam design is not an
   optimization but half of the problem.  This sharpens and explains the
   role of the "thresholds" in handoff conjecture 7.2.5.

7. **Calibration against the literature (Section 7).**  The rank-`m`
   trace of handoff conjecture 7.2.5 *is* the Baranyai–Katona wreath
   conjecture at parameters `(n,k)=(2m+1,m)` (for `gcd(n,k)=1` a wreath is
   precisely the window family of a cyclic permutation).  That conjecture
   is open; the January 2025 Dyck-path paper verifies it only through
   `k<=4` and proposes Catalan-indexed strengthenings that resonate with
   this project's Catalan-forest indexing.  The sequence version is the
   central case of the Chung–Diaconis–Graham universal-cycle conjecture;
   the 2020 resolution by Glock–Joos–Kühn–Osthus (Euler tours in
   hypergraphs) covers only fixed `k` with `n>=n_0(k)` and its
   absorption/nibble machinery degrades in the uniformity, so the central
   regime `k=m~n/2` is genuinely open.  Generic near-perfect-matching
   technology (Pippenger–Spencer, Alon–Kim–Spencer, and successors) has
   defect exponents of the form `D^{-1/(k-1)}` and therefore cannot reach
   the required defect at uniformity `Theta(n)` (Section 6); this
   quantifies, in this corner of the problem, the master handoff's Section
   8 prohibition on independent rounding.

The single sharpest open question this file leaves behind is stated as
**Open Problem 1** (Section 8): the short-run tail of the PBBS map.

## 1. Notation and standing conventions

Ranks are cardinalities of targets.  The *band of half-width `H`* is the
set of ranks `l` with `m-H <= l <= m+1+H`; *far* targets are the nonempty
targets of all other ranks.  For a word `A` (all letters nonempty subsets
of `[n]`), an interval `[i,j]` *realizes* the target `U(i,j)`.  Appending
a letter equal to a set `S` realizes `S` as a length-one interval; this
trivial device is used systematically and is the entire content of
"per-target repair".

A *singleton word* is a word all of whose letters are singletons; we
identify it with a sequence `w_1,w_2,…` of elements of `[n]`.  Its
*length-`l` window* at position `j` is the interval `[j, j+l-1]`; the
window is *clean* if its `l` letters are pairwise distinct, in which case
its union is a rank-`l` target.  A singleton word has the *gap-`G`
property* if no element occurs twice within any `G` consecutive positions;
then every window of length `<= G` is clean.

For a cyclic cover `P` of the middle layer by closed Johnson-type owner
walks, a *coordinate residence run* is a maximal set of consecutive owners
on one cycle all containing a fixed coordinate; `nu_H(P)` denotes, as in
the PBBS file, the maximum number of projected-edge-disjoint positive
coordinate runs of length at most `H`.

## 2. Theorem A: far-rank absorption and the `sqrt(n log n)` threshold

**Theorem A.**  Let `n=2m+1`, let `H>=1`, and suppose `V` is any word over
nonempty letters realizing every target whose rank lies in the band of
half-width `H`.  Then

\[
\nu(n)\ \le\ |V|\ +\ 2^{n+1}e^{-2(H+1)^2/n}.
\]

*Proof.*  Let `F` be the set of far targets.  By complement symmetry of
binomial coefficients,

\[
|F|=\sum_{l\le m-H-1}\binom{n}{l}+\sum_{l\ge m+H+2}\binom{n}{l}
   =2\sum_{l\le m-H-1}\binom{n}{l}.
\]

Every `l<=m-H-1` deviates from the mean `n/2=m+1/2` by at least `H+3/2`,
so by Hoeffding's inequality
`sum_{l<=m-H-1} binom(n,l) <= 2^n e^{-2(H+1)^2/n}`.  Append to `V` one
letter per far target, namely the target itself; each appended letter is
nonempty and realizes its target as a length-one interval, and appending
letters never destroys already-realized targets (all old intervals
persist).  ∎

**Corollary A1 (threshold).**  Since `W=binom(n,m) >= 2^n/sqrt(2n)`, the
absorption cost is `o(W)` iff `e^{-2H^2/n}=o(n^{-1/2})`, i.e. iff

\[
H\ \ge\ \tfrac12\sqrt{n\ln n}\,(1+o(1)).
\]

With the concrete choice `H=ceil(sqrt(n ln n))` the cost is
`O(W n^{-3/2})`.

**Lemma A1′ (sharp two-sided tail — audit patch, 2026-08-20).**  The
second reader correctly noted that the "iff" of Corollary A1 and the
exactness claim of Remark A2 need a binomial LOWER-tail estimate,
which Hoeffding does not provide.  Here it is, elementarily.  For
`0 <= H = o(n^{2/3})`,

\[
\binom{n}{m-H}=\binom{n}{m}\prod_{i=0}^{H-1}\frac{m-i}{m+2+i}
=W\exp\Bigl(-\sum_{i=0}^{H-1}\ln\frac{m+2+i}{m-i}\Bigr)
=W e^{-\frac{2H^2}{n}(1+o(1))},
\]

since `ln((m+2+i)/(m-i)) = (2i+2)/m + O(i^2/m^2)` and the cumulative
error is `O(H/n + H^3/n^2) = o(1)` at `H = O(sqrt(n log n))`.
Consecutive terms of the tail decay by the factor
`(m-H-j)/(m+2+H+j) = 1 - (4H/n)(1+o(1))`, so

\[
\sum_{l\le m-H}\binom{n}{l}
=\binom{n}{m-H}\cdot\Theta\bigl(n/H\bigr)
=W\,e^{-\frac{2H^2}{n}(1+o(1))}\cdot\Theta(n/H).
\]

At `H = c·sqrt(n ln n)` this gives `|F| = W·n^{1/2-2c^2+o(1)}` IN
BOTH DIRECTIONS: for `c > 1/2` the absorption cost is `o(W)`
(recovering Corollary A1's sufficiency), and for `c < 1/2` any
per-target scheme costs `|F| = W·n^{1/2-2c^2} = omega(W)` —
establishing the LOWER half of the threshold claim that Hoeffding
could not.  The `iff` of Corollary A1 and the exactness of Remark
A2 now stand on the two-sided estimate.  ∎

**Remark A2 (per-set schemes cannot beat the threshold).**  Any scheme
that spends at least one letter per far target — and chain difference
words, one letter per set, are exactly such a scheme — costs at least
`|F|` letters, so the threshold of Corollary A1 is exact for the entire
class of per-target constructions.  Compression below `H*` requires letter
*reuse across many targets* at sub-band ranks, i.e. genuine sub-band
analogues of the central reuse structures; this is precisely what handoff
conjectures 7.2.6–7.2.7 attempt with their pairing economics
`min(c_Pi, L_|Z|)` at scale `sqrt(m log log m) < H*`.  Theorem A shows
those conjectures are *harder than necessary* for coefficient one: the
band at `H*` suffices, so any band structure valid at `H*` bypasses the
multiscale wreath entirely.

**Remark A3 (band tiling does not help below the threshold).**  One can
try to tile ranks below the band with secondary reuse structures centered
at ranks `m-jH`.  Any such level costs at least `binom(n, m-jH)` letters
(width bound), and the *lower cone below the last level* still needs
per-target or chain treatment; optimizing the level count reproduces the
same `Theta(sqrt(n log n))` threshold up to constants.  We record this to
prevent rediscovery: the threshold is robust, not an artifact of
Hoeffding.

## 3. Theorem B: the assembled bound and the run-length criterion

We now cite two proved facts from
`MATH_PBBS_FLAG_FACTOR_AND_FALSE_CONNECTOR_GATE_20260728.md`:

- **(PBBS flag support, its Theorem 1.1 and the complement projection.)**
  Along the cycles of the canonical PBBS cover `P_m`, every rank-`(m-q)`
  target (`1<=q<=m`) occurs as an intersection of `q+1` consecutive
  states, and dually every rank-`(m+1+q)` target occurs as a union of
  `q+1` consecutive complement-projected owners.

- **(Collar ledger, its equation (2.2).)**  For every `H<m` there is a
  literal nonzero word of length

  \[
  L_H\ \le\ W+2H\,\mathrm{Cat}_m+2(5H-1)\,\nu_H(P_m) \tag{3.1}
  \]

  realizing all PBBS lower intersections and upper unions through depth
  `H`; in particular all targets of every rank in the band of half-width
  `H`.

**Theorem B.**  For every `H<m`,

\[
\nu(2m+1)\ \le\ W+2H\,\mathrm{Cat}_m+2(5H-1)\,\nu_H(P_m)
+2^{n+1}e^{-2(H+1)^2/n}.
\]

*Proof.*  Feed the word of (3.1) into Theorem A as `V`.  ∎

**Corollary B1 (explicit form at the threshold).**  Taking
`H=ceil(sqrt(n ln n))` and using `Cat_m=W/n` (identity (0.1)):

\[
\nu(2m+1)\ \le\
W\Bigl(1+2\sqrt{\tfrac{\ln n}{n}}\,(1+o(1))+O(n^{-3/2})\Bigr)
+2(5H-1)\,\nu_H(P_m).
\]

**Corollary B2 (the run-length criterion).**  If

\[
\nu_{H}(P_m)\ =\ o\!\Bigl(\frac{W}{\sqrt{n\log n}}\Bigr)
\qquad\text{at } H=\lceil\sqrt{n\ln n}\rceil,
\]

then `nu(2m+1)=(1+o(1))W(2m+1)`.  Moreover the even dimensions follow:
`nu(2m+2) <= 2 nu(2m+1)` (top-bit splice, handoff Section 5.1) together
with the exact identity `binom(2m+2,m+1)=2 binom(2m+1,m)` preserves the
coefficient, and `nu(k) >= B(k) >= W(k)` always.  Hence the criterion
implies the full asymptotic coefficient-one conjecture (handoff 7.1.3):

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}\quad\text{for all }k.
\]

*Proof.*  Immediate from Corollary B1 since
`2(5H-1)nu_H = O(sqrt(n log n))·o(W/sqrt(n log n)) = o(W)`, plus the two
cited facts for even `k` and the lower bound.  ∎

**Remark B3 (the criterion sits exactly at the memoryless edge).**  In
the cover `P_m` each step exchanges `O(1)` coordinates, so the total
number of positive runs across all coordinates is `Theta(W)` and the mean
run length is `Theta(m)`.  If run lengths had a memoryless (geometric)
tail at that mean, the number of runs of length `<= H` would be
`Theta(W·H/m)=Theta(W sqrt(log n)/sqrt(n))`, exceeding the criterion's
budget `o(W/sqrt(n log n))` by exactly `Theta(log n)`.  So Corollary B2
requires the short-run tail of the explicit PBBS dynamics to be lighter
than memoryless by a log factor — a concrete, falsifiable analytic
question about one explicit map (Open Problem 1), not a search problem.
Conversely, this explains *why* the multiscale conjectures 7.2.6–7.2.7
were formulated at `sqrt(m log log m)`: below the Theorem-A threshold a
memoryless tail is affordable, but then far-rank absorption is not, and
batched repair must be invented.  The two regimes pivot exactly at `H*`.

**Remark B4 (self-contained abstract variant).**  If one does not wish to
cite (3.1), the following weaker ledger is easy to prove from scratch by
the erosion/dilation argument (as in the file's Theorem 2.1, whose proof
is reproduced in our terms in Section 5): with all-runs-long hypothesis
replaced by per-run damage accounting, one obtains
`L_H <= W+2Hc+H^2·nu_H` where `c` is the number of cycles: each short run
of length `l` can ruin at most `l(l+1)/2 <= H(H+1)/2` flag occurrences,
each repairable per-target.  The criterion then reads
`nu_H = o(W/(n log n))`.  Everything else in this file is unaffected;
(3.1) simply improves `H^2` to `10H` via the circular interval
transversal, and we use it as cited.

## 4. Theorem C: the defective central covering route (singleton corner)

The PBBS route uses large letters and short intervals.  The opposite
corner of design space uses singleton letters and length-`~m` intervals.
The following theorem replaces the partition-plus-thresholds object of
handoff conjecture 7.2.5 by a strictly weaker covering object.

**Definition (defective central covering word).**  A `DCC(n,H,delta)` is
a singleton word `w` of length `N <= (1+delta)W` with the gap-`(m+H+2)`
property such that for every band rank `l` (i.e. `m-H<=l<=m+1+H`), the
number of rank-`l` targets not realized as a (clean) length-`l` window of
`w` is `Delta_l`, with `sum_l Delta_l <= delta·W`.

**Theorem C.**  If `DCC(n,H_n,delta_n)` exists for every odd `n=2m+1`
with `H_n=ceil(sqrt(n ln n))` and `delta_n -> 0`, then
`nu(k)=(1+o(1))W(k)` for all `k`.

*Proof.*  Append one letter per missed band target (`<= delta_n W`
letters), then apply Theorem A (`o(W)`), then the even splice and the
lower bound as in Corollary B2.  Windows of length `l <= m+H+2` are clean
by the gap property, so each realizes exactly one rank-`l` target; all
other interval unions of `w` are harmless surplus, because this problem
only ever demands that targets *occur*.  ∎

The force of Theorem C is negative space: no chain structure, no
thresholds, no partition, no multiplicity control, no exactness — the
only asks are the gap property, near-optimal length, and defective
multirank window coverage.  Any future construction should be measured
against this minimal interface.

## 5. Theorem D: the middle-levels lift of the central ucycle problem

Let `ML(2m+1)` be the bipartite containment graph between ranks `m` and
`m+1` of `[n]`.  A *doubly-exact central universal cycle* is a cyclic
singleton word of length exactly `W` whose `m`-windows are pairwise
distinct (hence enumerate `binom([n],m)` by (0.1)) and whose
`(m+1)`-windows are pairwise distinct (hence enumerate `binom([n],m+1)`).

**Theorem D.**  Doubly-exact central universal cycles for `[n]` are in
canonical bijection with Hamilton cycles
`U_1, V_1, U_2, V_2, …, U_W, V_W` of `ML(2m+1)` that satisfy the shift
condition

\[
b_j=a_{j-m}\ \text{ for all } j\in\mathbb Z_W,
\qquad a_j:=V_j\setminus U_j,\quad b_j:=V_j\setminus U_{j+1}. \tag{5.1}
\]

Under the bijection the word is `w_j=b_j`, every element occurs exactly
`Cat_m` times, every dwell (maximal presence interval in the sliding
`m`-window) has length exactly `m`, and the gap-`(m+1)` property holds
automatically.

*Proof.*  (⇒)  Given the word `w`, set `U_j={w_j,…,w_{j+m-1}}` and
`V_j={w_j,…,w_{j+m}}`.  Cleanliness of all `m`-windows forces
`U_{j+1} != U_j`; if some element repeated with gap exactly `m` then the
`m`-window would slide onto itself, contradicting distinctness of the
`U_j`; hence the gap is at least `m+1`, all `V_j` have rank `m+1`, and
`U_j ⊂ V_j ⊃ U_{j+1}` is a closed walk in `ML(2m+1)` of length `2W`
visiting `W` distinct lower vertices and `W` distinct upper vertices —
all of them, by (0.1) — each exactly once: a Hamilton cycle.  The
entering element at step `j` is `a_j=w_{j+m}` and the leaving element is
`b_j=w_j`, so `b_{j+m}=w_{j+m}=a_j`, which is (5.1).

(⇐)  Given a Hamilton cycle with (5.1), define `w_j:=b_j`.  On a Hamilton
cycle `U_{j+1} != U_j`, so `a_j != b_j` and `b_j ∈ U_j`,
`b_j ∉ U_{j+1}`, `a_j ∉ U_j`, `a_j ∈ U_{j+1}`.  Thus the element `x=a_t`
enters the `U`-trajectory at step `t` and, by (5.1), the element removed
at step `t+m` is exactly `a_t`; so `x ∈ U_s` for `s∈[t+1,t+m]` and
`x ∉ U_{t+m+1}` unless re-entered.  Suppose `x` entered again at `t'`
with `0 < t'-t < m`.  Then at step `t+m` the cycle removes `x`
(`b_{t+m}=a_t=x`), so `x ∉ U_{t+m+1}`; but the entry at `t'` guarantees
`x ∈ U_s` for `s∈[t'+1, t'+m]`, and `t+m+1 <= t'+m`, a contradiction.  If
`t'-t=m` exactly, then `b_{t+m}=a_t=x=a_{t+m}` gives `U_{t+m+1}=U_{t+m}`,
impossible on a Hamilton cycle.  Hence consecutive entries of every
element are more than `m` apart: dwell intervals `[t+1,t+m]` are pairwise
disjoint and the gap-`(m+1)` property holds for the word `w` (note
`w_{t+m}=b_{t+m}=a_t`, so occurrences of `x` in `w` are the times
`t+m` for entries `t`).  Consequently membership is well-defined and

\[
U_j=\{a_t:\ t\in[j-m,\,j-1]\}=\{w_{t+m}:\ t\in[j-m,\,j-1]\}
=\{w_j,…,w_{j+m-1}\},
\]

so the `m`-windows of `w` are exactly the `U_j` (distinct, Hamilton), the
`(m+1)`-windows are the `V_j` (distinct), and `w` is a doubly-exact
central universal cycle.  The two constructions are mutually inverse by
inspection.  Finally, the number of occurrences of `x` in `w` equals its
number of dwells; dwells have length exactly `m` and
`#{j: x∈U_j}=binom(n-1,m-1)=binom(2m,m-1)`, so `x` occurs
`binom(2m,m-1)/m=Cat_m` times.  ∎

**Remark D1.**  Mütze's middle-levels theorem supplies Hamilton cycles in
`ML(2m+1)` for all `m>=1`, and later counting results supply
double-exponentially many.  Theorem D says the central
Chung–Diaconis–Graham problem is *exactly* the question of whether the
shift relation (5.1) can be satisfied inside this enormous family; the
FIFO discipline (every dwell exactly `m`) is not a design choice but a
theorem.  Defective versions transfer verbatim: a Hamilton cycle
satisfying (5.1) on all but `o(W)` indices, repaired by cutting at
violations and per-target patching, yields a `DCC`-grade middle layer.
This gives the singleton route of Theorem C a concrete attack surface:
construct middle-levels Hamilton cycles with *local* freedom (e.g. from
2-factor plus flip constructions) and satisfy (5.1) approximately.

**Remark D2 (relation to the project's ML machinery).**  Handoff Section
5.2 already centers on `ML(2m±1)` 2-factors, Catalan path forests, and
turn-colour bijections; Theorem D adds the precise statement of *which*
extra structure on a Hamilton object the serialization needs in the
singleton corner: the `m`-shift relation, nothing more.

## 6. The pass calculus: seams, the factor-2 law, and nibble obstructions

**Lemma 5 (seam cleanliness).**  Let `sigma, sigma'` be two passes
(permutations of `[n]`) written consecutively.  For `1<=j<=m-1` the
seam-crossing `m`-window taking the last `j` letters of `sigma` and first
`m-j` of `sigma'` is clean for **all** `j` simultaneously iff for every
element `x`,

\[
\mathrm{age}_\sigma(x)+\mathrm{pos}_{\sigma'}(x)\ \ge\ m+1,
\]

where `age_sigma(x)=n+1-position of x in sigma` (so `age=1` for the last
letter) and `pos_{sigma'}(x)` is the position in `sigma'`.

*Proof.*  A collision in the `j`-th seam window is an element `x` with
`age_sigma(x)<=j` and `pos_{sigma'}(x)<=m-j`.  Such `(x,j)` exists iff
some `x` has `age_sigma(x)+pos_{sigma'}(x)<=m` (take
`j=age_sigma(x)`).  ∎

This is the same "two endpoint ages sum to at least `L`" inequality as
the residence relabeling test of
`MATH_THEOREM_COMPLEMENTARY_AGE_CROSS_STRATUM_COLLARS_20260804.md`; the
collar calculus and the seam calculus are one constraint.

**Theorem E (factor-2 seam law).**  Let `A` be a concatenation of `T`
passes, `Tn<=(1+delta)W`.  Then the number of distinct middle targets
realized by in-pass windows is at most

\[
T(m+2)\ \le\ (1+\delta)\,W\Bigl(\tfrac12+\tfrac{3}{4m}\Bigr),
\]

so if `A` realizes `(1-eps)W` middle targets, then at least
`W(1/2-eps-delta/2-3/(4m))` of them are realized only by seam-crossing
windows; since the total number of seam windows is `T(m-1)<(1+delta)W/2`,
a `(1-o(1))`-fraction of all seam windows must be clean, pairwise
distinct, and distinct from all in-pass windows, whenever
`eps,delta=o(1)`.

*Proof.*  A pass of length `n` has `n-m+1=m+2` in-pass `m`-windows, and
each window realizes exactly one set; multiply and use (0.1).  The seam
count is `m-1` windows per seam and at most `T` seams (cyclically).  The
rest is arithmetic.  ∎

**Corollary E1 (the wreath conjecture alone is insufficient).**  A
perfect wreath decomposition (Section 7) supplies `Cat_m` cyclic orders
whose *cyclic* window families partition the middle layer; but any
serialization must open each cycle, and Theorem E shows the opened system
loses `(1/2-o(1))W` of the layer to wraps, which must be re-supplied by
seams satisfying Lemma 5 or by a second traversal (coefficient `3/2` via
`(n+m)`-length passes) — never for free.  This is the precise sense in
which the "thresholds" of handoff conjecture 7.2.5 carry half the
difficulty.

**Lemma 6 (degrees and codegrees of the wreath hypergraph).**  Fix
`l`-sets as vertices.  (i) The number of cyclic orders of `[n]` having a
given `l`-set as an arc is `l!(n-l)!`; uniformly in the set.  (ii) For
distinct `m`-sets `S,T` with `j=|S∩T|`, the number of cyclic orders
having both as arcs is `2·(m-j)!·j!·(m-j)!·(j+1)!` (interpreting the
`j=0` case with the singleton complement block), i.e. a fraction

\[
R_j=\frac{2}{\binom{m}{j}\binom{m+1}{j+1}}
\]

of the degree `m!(m+1)!`; the maximum is `R_0=2/(m+1)` at disjoint pairs.
(iii) Consistency: `sum_j binom(m,j) binom(m+1,m-j) R_j = 2m = n-1`,
matching the fact that a cyclic order has `n` middle arcs.

*Proof.*  (i) Among the `n!` linear orders, those in which the set is a
cyclic arc number `n·l!·(n-l)!` (start position, internal, external);
divide by `n` rotations.  (ii) Both arcs force the cyclic block pattern
`[S∖T][S∩T][T∖S][R]` or `[S∖T][R][T∖S][S∩T]`, with
`|R|=n-2m+j=j+1>=1`; multiply internal orders.  (iii) Using
`binom(m+1,m-j)=binom(m+1,j+1)` each summand is `2`.  ∎

**Proposition 6.1 (independent families stall at `1-1/e`).**  Let
`sigma_1,…,sigma_T` be i.i.d. uniform passes, `T=c·Cat_m`.  The
probability that a fixed middle set is realized by an in-pass window of
some pass is at most `1-(1-(m+2)/W)^T = 1-e^{-c/2+o(1)}`, so the expected
number of middle targets covered in-pass is at most
`W(1-e^{-c/2}+o(1))`; and the coverage count concentrates within `o(W)`
(McDiarmid: changing one pass changes it by at most `2n`, and
`Tn^2=o(W^2/n)` gives exponentially small deviation at scale `eps W`).
Hence near-perfect coverage at near-optimal length is impossible for
independently sampled pass families, quantifying, in this corner, the
handoff Section 8 prohibition on independent rounding.  (Seam windows are
deterministic given the passes and add at most `T(m-1)` further covered
sets, which changes `e^{-c/2}` to at worst `e^{-c}`; the stall constant
survives.)

**Remark 6.2 (why generic nibble technology fails here).**  Formulating
the middle-layer packing with edges = wreaths (edge size `n`) or edges =
passes (edge size `m+2`) meets modern near-perfect matching bounds of
shape `defect ~ N·D^{-1/(k-1)}` (Alon–Kim–Spencer and successors) with
uniformity `k=Theta(n)`: the defect guarantee degrades to a `1-o(1)`
fraction, i.e. no guarantee at all.  The codegree ratios of Lemma 6 are
factorially small, but no known black-box converts that into a defect
`o(1/sqrt(n log n))` at uniformity `Theta(n)`.  Conclusion: the central
covering problems must be attacked through their *sliding-window/Euler*
structure (as Glock–Joos–Kühn–Osthus do for fixed `k`, and as Theorem D
makes available at the central rank via `ML(2m+1)`), or through the
run-length criterion of Corollary B2 — not through generic packing.

## 7. Identifications with named open problems, with exact scopes

**7.1 Wreaths.**  For `gcd(n,k)=1`, an `(n,k,pi)`-wreath in the sense of
Baranyai–Katona is `{ {pi((i-1)k+1),…,pi(ik)} : i in Z_n }`; since
stepping by `k` is a bijection on `Z_n`, this is exactly the family of
all `n` cyclic `k`-arcs of the cyclic order `pi` — the window family of a
cyclic permutation.  At `(n,k)=(2m+1,m)`: `gcd=1`, and by (0.1) a
decomposition of `binom([n],m)` into wreaths uses exactly `Cat_m` cyclic
orders.  The rank-`m` trace of handoff conjecture 7.2.5 (Catalan-many
cyclic orders whose interval chains partition the Boolean lattice)
therefore *is* the Baranyai–Katona wreath conjecture at these parameters:
7.2.5 is at least as strong.  Status: open in general; the 2025
Dyck-path paper (arXiv:2501.07277, El. J. Comb.) proves an interval
counting formula (`iota_k(k,l)=binom(k,l)^2`), proposes two Catalan/Dyck
indexed strengthenings, and verifies `k<=4`.  Its Dyck-path indexing of
the `Cat_m` wreaths matches this project's Catalan-forest and cycle-lemma
bookkeeping (rotation orbits of middle sets are counted by `Cat_m` with
all orbits full, since `gcd(m,2m+1)=1`), suggesting the "one wreath per
rotation orbit" refinement as the natural common target.

**7.2 Universal cycles.**  A ucycle for `m`-subsets of `[2m+1]` is a
cyclic word of length `W` over `[n]` whose `m`-windows are distinct sets;
Theorem D characterizes the doubly-exact ones.  The divisibility
condition of Chung–Diaconis–Graham holds centrally by (0.1).
Glock–Joos–Kühn–Osthus ("Euler tours in hypergraphs") resolve the
conjecture for every fixed `k` and `n>=n_0(k)`; their method (random
walk + decomposition + absorption) is not uniform in `k`, and no result
is known at `k=m~n/2`.  Both the exact central ucycle and the wreath
conjecture imply strong versions of the middle-layer half of our
covering objects; neither is known, and by Corollary E1/Theorem C the
*defective covering* versions are strictly easier and already suffice
for coefficient one.  Any progress on either named problem transfers
into this project through Theorem C; any counterexample would not
falsify coefficient one, precisely because defects are absorbed.

**7.3 The three-regime `H`-spectrum.**  All known routes are organized by
one parameter: the guaranteed coordinate residence/run scale `H` of a
central enumeration.

- `H=Theta(sqrt m)`: the residence machinery of handoff Section 5.3
  (three-pairing covers, pair cells, `L=O(sqrt r)` separations; the
  2-adic obstruction `M<=s_2(r)` forces cut blocks).  Below the
  Theorem-A threshold: far ranks cannot be absorbed per-target, so this
  regime *must* invent batched repair (7.2.6–7.2.7 at
  `sqrt(m log log m)`).
- `H=Theta(sqrt(n log n))`: the pivot regime of this file.  Absorption is
  free (Theorem A); the only obstruction is the short-run tail
  (Corollary B2); a memoryless tail misses by exactly `Theta(log n)`
  (Remark B3).
- `H=m`: maximal runs; enumerations are unions of wreaths; exactness at
  this end is the wreath/ucycle pair (7.1, 7.2), and even granted, seams
  cost half the layer (Theorem E) unless the Lemma-5 age inequality is
  engineered globally, which is the `ML`-shift condition (5.1) in
  disguise.

The project's prior conjectures 7.2.5–7.2.7 are the two extreme regimes;
Corollary B2 opens the middle regime, which had no named conjecture, and
where the required input is an analytic property of an already-explicit
object rather than a new existence theorem.

## 8. Open problems this file sharpens

**Open Problem 1 (short-run tail of PBBS; sufficient for handoff
conjecture 7.1.3).**  Prove `nu_H(P_m)=o(W/sqrt(n log n))` at
`H=ceil(sqrt(n ln n))` for the canonical PBBS cover `P_m` — or exhibit
any owner cycle cover with complete band flag support, `O(Cat_m)`
components, and this short-run tail.  By Corollary B2 this implies
`nu(k)=(1+o(1))binom(k,floor(k/2))` for all `k`.  Note the freedom: the
cover may be changed, only the ledger (3.1) hypotheses must survive.

**CORRECTED STATUS (2026-09-07):** The former negative resolution relied
on the false Q6 of the companion queue-flush file. The family
`D_q=1(1100)^q0` has height three but planted lifetime `3q`; see
`scratch/PBBS_Q6_RETRACTION_AND_FIXED_HEIGHT_COUNTERFAMILY_20260907.md`.
The claimed positive-density packing obstruction is not established by
that argument. This audit neither proves nor refutes the first alternative.
The compiler implication still requires every displayed hypothesis,
including actual band flag support, not only a short-run estimate.

**Open Problem 2 (defective shift-Hamilton cycles).**  Construct
middle-levels Hamilton cycles satisfying the shift relation (5.1) on all
but `o(W)` indices.  Via Theorem D/Remark D1 and Theorem C this also
implies coefficient one, independently of PBBS.

**Open Problem 3 (rotation-orbit wreaths).**  Decide whether the `Cat_m`
wreaths can be chosen as a transversal-compatible system for the `Cat_m`
rotation orbits of the middle layer (one wreath per orbit in a suitable
exact or defective sense), aligning the 2025 Dyck-path indexing with the
cycle lemma.  Even a defective version feeds Theorem C.

## 9. The medium-gap return function, the log-`n` seam, and corner duality

Historical development, added the same day after reading
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` in full detail, proposed
replacing Open Problem 1 by a stronger bound on one arithmetic function
of the explicit PBBS dynamics. Three estimates fell short of that bound.
This did not prove that the physical packing difficulty was equivalent
to that arithmetic target. The
proposed stronger raw-count target was refuted by the independent
2026-09-07 argument recorded in Section 9.3; it must not be substituted
for the still-open physical packing problem.

**9.1 The exact PBBS dynamics.**  By Lemma 8.1 of the cited file, in
normalized Dyck-root coordinates a state is `0D` with `D` a Dyck word of
semilength `r`, and one PBBS step is the skew product
`(u,D) -> (u+delta(D) mod N, phi(D))` with `D=P1Q` split at the first
up-step attaining the maximum height, `delta(D)=|P|+1`, and
`phi(D)=barQ 0 barP`.  On sets this is: complement, delete the root.
Consequently one step of `g=f^2` is the exact Johnson exchange

\[
g(S)\;=\;S+u(S)-u(f(S)),
\]

i.e. the coordinate entering at a `g`-step is the current root and the
coordinate leaving is the next odd-parity root.  A coordinate residence
run of length `<=H` is therefore precisely an **exact odd-parity return
of the root walk within `2H` steps**. The quantity `nu_H` of Corollary B2
is the maximum edge-disjoint packing of the associated repair intervals,
NOT the number of all such returns.

**9.2 The return-count function.**  For odd `gap>=3` let `A_g(r)` be the
number of Dyck roots of semilength `r` that start a consecutive
omitted-label return of gap `g`.  The proved record is:

- `A_3(r)=0` for all `r` (no-gap-three theorem);
- `A_5(r)=Theta(r^2)`: gap five forces `r-pk(D)=1` (peak-collapse,
  equation (16.4) of the cited file), and paths with `r-1` peaks number
  `N(r,r-1)=binom(r,2)`;
- the height-gap theorem `g>=2·ht(D)+1` (its Theorem 16.1) plus the
  Chebyshev count of low paths gives
  `A_g(r) <= 4^r·exp(-c r/g^2)·poly(r)`, which yields the proved
  sub-Gaussian packing window `H=o(sqrt(r/log r))` (its Corollary 16.2:
  `nu_H = o(Cat_r)` there).

**Proposition 9.1 (renormalization recursion and its ceiling).**  The
equality-particle renormalization behind the height-gap theorem gives,
for `g>=5`,

\[
A_g(r)\ \le\ \sum_{r_1<r}\Bigl(\max_{D_1}\#\{D:\partial D=D_1,\
\mathrm{sl}(D)=r\}\Bigr)\,A_{g-2}(r_1)
\ \le\ \sum_{r_1<r}\binom{r+r_1}{r-r_1}A_{g-2}(r_1),
\]

since a `∂`-preimage of `D_1` adding `p=r-r_1` peaks is determined by a
multiset of insertion slots among the `2r_1+1` contour gaps, at most
`binom(2r_1+p,p)<=binom(r+r_1,r-r_1)` choices.  With
`sum_k binom(r+k, r-k)=F_{2r+1}` (Fibonacci diagonal) this yields e.g.
`A_7(r)=O(r^2·varphi^{2r})`, `varphi` the golden ratio — and
`varphi=2cos(pi/5)`, exactly the height-2... height-3 Chebyshev base.  In
general the recursion's growth bases reproduce `(2cos(pi/(s+2)))^2`
level by level: **peak-pruning entropy alone can never beat the height
bound**, confirming the cited file's closing remark by an independent
computation.  So the window `H=o(sqrt(r/log r))` is the ceiling of the
entire entropy mechanism, not of one proof.

**9.3 The log-`n` seam (historical stronger raw target, now refuted).**
The following raw-count condition would suffice for Corollary B2;
it is stronger than that corollary's physical PACKING requirement:
`sum_{g<=2H} N·A_g(r) = o(W/H)` at `H=ceil(sqrt(n ln n))`, i.e.

\[
\boxed{\ \sum_{3\le g\le 2\lceil\sqrt{r\ln r}\rceil} A_g(r)
\;=\;o\!\Bigl(\frac{4^r}{r^{2}\sqrt{\log r}}\Bigr)\ }
\tag{9.1}
\]

(using `Cat_r ~ 4^r r^{-3/2}` and `H ~ sqrt(2r·ln r)` up to constants).
Three independent estimates each miss (9.1) by exactly `Theta(log n)`:

1. *Memoryless run tails* (Remark B3): geometric tails at mean `Theta(m)`
   give `nu_H ~ W·H/m`, over budget by `H^2/m·(1) = Theta(log n)`.
2. *Spatial-return heuristic*: even if the voltage walk `sum delta`
   equidistributed perfectly, an exact return in a window of `2H` steps
   has probability `~2H/N`, giving `nu_H ~ W·H/N`, again over budget by
   `H^2/N=Theta(log n)`.
3. *Medium-run repair inside the ledger*: repairing runs of length in
   `(sqrt(r)/log r, H]` through the `10H`-per-run transversal costs
   `~Cat·H·10H = 10W·H^2/n = Theta(W log n)`.

Thus no generic mechanism suffices; (9.1) requires the *exact*
arithmetic of the PBBS returns to remain rigid through the window
`g in [sqrt(r/log r), sqrt(r log r)]`, a regime where the proved pattern
(`A_3=0`, `A_5` polynomial, sub-height counts up to the entropy ceiling)
must persist one log-factor beyond where entropy alone protects it.  The
evidence for rigidity is that at small `g` the true counts are not merely
sub-Gaussian but *polynomially small* — astronomically below both
heuristics 1 and 2 — because a return forces exact algebraic collapse
(peak-collapse at `g=5`), not merely low height.  The refined open
problem is therefore:

**Historical target 1′ (refuted as stated; see status below).** Determine the growth of
`A_g(r)` for `g` between `sqrt(r/log r)` and `sqrt(r log r)`; prove
(9.1).  By Theorem B and Corollary B2, (9.1) implies
`nu(k)=(1+o(1))·binom(k,floor(k/2))` for all `k`.

**UPDATED STATUS (2026-09-07): the stronger RAW census (9.1) is false.**
The earlier Q6 proof remains invalid. Independently, the exact TRUE
zero-budget product now gives Omega(4^r/r^2) normalized newborn roots
with T=height in any chosen fixed positive Gaussian band (the full
audited local limit gives an explicit positive band constant). Their
gaps 2T+1 lie inside the displayed cutoff for all sufficiently large r.
This contradicts the requested o(4^r/(r^2 sqrt(log r))) raw count.
See `scratch/PBBS_TRUE_GAUSSIAN_RAW_CENSUS_OBSTRUCTION_20260907.md`
for an elementary coefficient lower bound and the exact scope.
This does NOT refute Corollary B2's edge-disjoint PACKING condition,
an efficient shared repair, or coefficient one. The raw count and the
physical packing number must not be identified.

**9.4 Shoulder tightness (no assembly dodge).**  In the erosion
architecture the band at depth `H` serves rank `m-t` with surplus factor
`exp(2t^2/n)`; at `t ~ sqrt(r)/log r` the surplus is `1+O(1/log n)`, so
the "shoulder" ranks between the proved window and the absorption
threshold are essentially as tight as the middle layer and require full
multiplexing; splitting the band between two structures, or serving the
shoulder by pockets of deeper erosion, costs at least one letter per
shoulder target and fails by the mass count `Theta(W sqrt n)`.  The
window in (9.1) is therefore forced, within this architecture, from
both sides.

**9.5 Corner duality.**  The two clean architectures have disjoint
obstructions.  The erosion corner (letters of size `~m`, windows of
length `~sqrt(n log n)`, targets as intersections/erosions) has *free
coverage* (Theorem 1.1 flag support at every depth) and is blocked only
by the run tail (9.1).  The singleton corner (letters of size 1,
windows of length `~m`, targets as unions) has *no run obstruction at
all* — the gap property is automatic in near-ucycles by the FIFO law of
Theorem D — and is blocked only by coverage (the defective central
covering of Theorem C, i.e. ucycle-hardness).  Any interpolating
architecture (letters of intermediate size `s`, windows `~m/s`) trades
one obstruction against the other; nothing in the present record rules
out that the trade is strictly favorable at some intermediate `s`, and
this is recorded as:

**Open Problem 4 (intermediate-scale architectures).**  For letter scale
`s=s(n)` with `1<<s<<m`, formulate the analogue of the collar ledger and
of the covering defect, and determine whether the product of the two
obstructions can be beaten at some intermediate `s` — specifically
whether coverage-hardness decays faster in `s` than run-hardness grows.

## 10. Addendum (same day): FIFO 2-factors and the `omega(1)`-wreath-chaining problem

The singleton corner was developed independently of the now-withdrawn Q6
route-closure claim. Four facts, each with proof, and one minimal open problem.

**Proposition 10.1 (wreath decompositions are FIFO 2-factors).**  For a
cyclic order `sigma` of `[n]`, the alternating sequence of its `m`-arcs
and `(m+1)`-arcs (each `(m+1)`-arc the union of its two consecutive
`m`-arcs) is a cycle of length `2n` in `ML(2m+1)` satisfying the shift
condition (5.1) locally; the generating word is `sigma` repeated, with
every dwell exactly `m+...`-periodic.  Since the complement of an
`m`-arc of `sigma` is an `(m+1)`-arc of `sigma`, a wreath decomposition
(partition of `binom([n],m)` into `Cat_m` wreaths) simultaneously
partitions `binom([n],m+1)` and hence is exactly a spanning FIFO
2-factor of `ML(2m+1)` with `Cat_m` cycles of length `2n`.  This places
the Baranyai–Katona object inside the middle-levels machinery of
handoff Section 5.2 as the maximally fragmented FIFO object.

**Lemma 10.2 (splice loss).**  Serializing a FIFO 2-factor with `c`
cycles into one word costs the `~m` windows crossing each of the `c`
junk seams; the lost coverage is `Theta(mc)`.  At the wreath scale
`c=Cat_m=W/n` this is `Theta(W)` — the factor-2 seam law (Theorem E)
seen from the ML side.  Coverage loss `o(W)` requires `c=o(W/m)`,
i.e. **average FIFO cycle length `omega(n)`**: beating the wreath
fragmentation by any diverging factor suffices.

**Lemma 10.3 (seam statistics).**  For two independent uniformly rotated
orders, the expected number of violations of the seam-cleanliness
inequality of Lemma 5 (`age+pos>=m+1`) is `Theta(m)`; so random
chaining of wreaths essentially never produces clean seams and seam
design must be structural.  At the opposite pole, a repeated order is
always clean (`age+pos=n+1`), but consecutive near-identical orders
share almost all arcs and fail window novelty; slow-morphing chains are
therefore excluded by duplication, fast-varying chains by dirt.  The
block/complementary-structure escape reproduces exactly the
collar/pair-cell designs of handoff Section 5.3, with their 2-adic
obstruction.

**Verification at `(m,g)=(2,2)`.**  Chaining the two wreaths of `Z_5`
as `1,2,3,4,5,1,3,5,2,4` (cyclically) gives gap `>=3` and windows
`12,23,34,45,15,13,35,25,24,14` — all ten `2`-subsets exactly once: for
`m=2` chaining all `Cat_2=2` wreaths is already the perfect central
universal cycle.

**Open Problem 5 (`omega(1)`-wreath chaining).**  Find `g=g(n)\to\infty`
and a family of `Cat_m/g` cyclic gap-`(m+1)` words, each a chain of `g`
opened cyclic orders with clean seams, whose `W` middle windows are
`(1-o(1))`-distinct, and whose length-`l` windows cover
`(1-o(1))`-fractions at every band rank `l` (total band defect `o(W)`).
By Lemma 10.2 and Theorem C this implies
`nu(k)=(1+o(1))binom(k,floor(k/2))` for all `k`.  This is strictly
weaker than the central Chung–Diaconis–Graham problem (`g=Cat_m`, zero
defect, single cycle) and than the wreath conjecture (which by Lemma
10.2 is *insufficient* on its own); it is the weakest unsolved link on
the singleton side identified so far.

## 11. Scope guard

Nothing in this file touches the exact conjectures `nu(k)=B(k)` or
`nu(k)<=B(k)+O(1)`: the assembled upper bounds here are
`W+Theta(W sqrt(log n)/sqrt n)` at best, far above `B(k)=W+Theta(sqrt k)`.
The finite `k=17` problem is untouched.  No claim in Sections 2–5 depends
on unproved statements except where explicitly labeled as citing (3.1),
whose scope is the PBBS instance as recorded in its source file;
Remark B4 gives the self-contained fallback.  The literature statuses in
Section 7 are as of 2026-08-20.
