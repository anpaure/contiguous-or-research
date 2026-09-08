# Q-Ary Tube Amplification and an Exact Finite Gate

Date: 2026-09-06. New scratch files only, suffix `c52e9`.

## 1. Results and Status

This branch does not itself improve the seven-accumulator coefficient
`c_st=1.18822944031087...`, which is its comparison constant below. The
separate eight-bit template now gives the stronger unconditional coefficient
`c_9=1.18070380384713...` in `../MASTER_HANDOFF.md`, Appendix A.7.
The positive result is a literal amplification theorem for **arbitrary finite
q-ary chain-pair covers**, not just binary ordered-path staircases. There is
also an exact improvement of the tube widths for three-coordinate shores.

Write `[q]={0,...,q-1}`, with `q>=2`. Suppose `[q]^d`, `d>=3`, is covered by `t` families

\[
 C_j\times D_j,
\]

where `C_j` and `D_j` are strict chains on complementary nonempty coordinate
subsets. The split can vary with `j`; chains may be nonsaturated and covers
may overlap. Let

\[
 M=\sum_j(|C_j|+|D_j|),\qquad
 E=\sum_j|C_j||D_j|-q^d.                              \tag{1}
\]

**Finite amplification theorem.** For every integer `m>=1`, there is an
explicit chain-pair cover of `[qm]^d` having

\[
 \boxed{\text{principal charge }M m^{d-1},\quad
        \text{number of rectangles }t m^{d-2},\quad
        \text{excess volume }E m^d.}                  \tag{2}
\]

It compiles into a nonzero set-word covering every nonempty member of an
actual product of `d` set chains of length `qm` **and its full complement**,
with length at most

\[
 M m^{d-1}+2t m^{d-2}+t(dqm+2).                      \tag{3}
\]

In particular, the error in (3) is lower order for fixed `q,d,t`, `d>=3`.
All overlap in (2) is retained and charged.

Let `tau` be the exit time from the unit ball of standard three-dimensional
Brownian motion started at zero, and let `S_r` be the sum of `r` independent
copies. Define

\[
 \beta_r=\sqrt{\pi/8}\,\mathbb E\sqrt{S_r}.
\]

**Boolean-cube consequence.** The explicit lift, together with the existing
minimum-accumulator construction, gives

\[
 \boxed{\nu(k)\le\left({M\over q^{d-1}}\beta_{d+1}+o(1)\right)W(k).}
                                                               \tag{4}
\]

Sections 2-5 prove the actual chain and interval constructions. Section 6
gives a stronger version of (2)-(4) when three-dimensional tube widths are
used rather than their generic upper bound.

The concrete computational outcome is an exact finite gap. If `M_int(q,6)`
is the minimum **integral** charge in (1), then

\[
 \boxed{1248\le M_{\rm int}(4,6)\le1280.}             \tag{5}
\]

The full fractional chain-pair-cover optimum, allowing every coordinate split
and every nonsaturated chain, is exactly

\[
 \boxed{M_{\rm frac}(3,6)=306,\qquad M_{\rm frac}(4,6)=1248.}       \tag{6}
\]

Both lower certificates and fractional covers are checked with exact
arithmetic. The fractional cover in (6) is **not** an interval-union word.

The remaining finite gate is particularly explicit:

\[
 \boxed{M_{\rm int}(4,6)\le1260
   \quad\Longrightarrow\quad
   \nu(k)\le\left({63\over64}c_{\rm st}+o(1)\right)W(k)
            <(1.1697+o(1))W(k).}                     \tag{7}
\]

Attaining the fractional value 1248 integrally would replace `63/64` in
(7) by `39/40`, giving `1.1585237043...`. Neither integral cover was found.

## 2. An Explicit Chain Partition of Every Cube Tube

Let `s>=1` and let `C` be any nonempty strict chain in `[q]^s`. Define its blown-up support

\[
 \mathcal T_m(C)=\bigcup_{v\in C}(mv+[m]^s).           \tag{8}
\]

### Tube Lemma

There is an explicit partition of (8) into exactly `m^(s-1)` nonempty
ascending chains, with total membership `|C|m^s`.

**Construction.** Complete `C` to a saturated lattice path `P` from the zero
corner to the top corner of `[q]^s`. The cells not belonging to `C` will be
deleted at the end. Let the coordinate of each successive path step be its
incoming/outgoing axis.

Inside a microcube `[m]^s`, route chains between the incoming face `a=0`
and the outgoing face `b=m-1` as follows.

- If `a=b`, use all parallel axis-`a` lines.
- If `a!=b`, fix the other `s-2` coordinates. In the `(a,b)` square use
  the `m` hooks
  \[
  (0,j),(1,j),\ldots,(m-1-j,j),
       (m-1-j,j+1),\ldots,(m-1-j,m-1),\quad0\le j<m. \tag{9}
  \]

The hooks partition the square. They give a bijection from the incoming
face to the outgoing face: entry label `b=j` goes to exit label `a=m-1-j`.
Including the fixed coordinates gives `m^(s-1)` routed chains in either case.
In the initial and final cells use the first and last path axes, respectively,
on both faces.

Between consecutive macro cells the outgoing coordinate increases by one
fine-grid step, from local `m-1` to local `0` in the next cell. Match equal
values of all the other local coordinates. This concatenates the pieces
into exactly `m^(s-1)` increasing paths through the whole tube of `P`.
Every path has a nonempty piece in every macro cell.

Delete the pieces in `P\C`. The remaining paths are strict chains, though
possibly nonsaturated; none becomes empty. They partition precisely (8).
The membership and chain-count assertions follow. This construction depends
on actual coordinatewise comparability, not on a rank polynomial.

For example, in three dimensions two cells separated only in the first
coordinate induce the same poset whether that coordinate jumps by one or
by ten. Their rank supports differ, but their minimum chain counts do not.
Section 6 makes this distinction quantitative.

## 3. Product Covers, Overlap, and Literal Intervals

For a template rectangle `C x D` with shore dimensions `r,s`, `r+s=d`,
apply the tube lemma separately to `C` and `D`. Pair every resulting left
chain with every resulting right chain. Their number is

\[
                         m^{r-1}m^{s-1}=m^{d-2}.
\]

Their total paired charge is

\[
 (|C|m^r)m^{s-1}+(|D|m^s)m^{r-1}
                     =(|C|+|D|)m^{d-1}.              \tag{10}
\]

At a fine point `x`, the number of covering template families is exactly
the old multiplicity of `floor(x/m)`. Each macro cell has `m^d` points.
This proves all three identities in (2), including the exact excess volume.

Now place actual ascending set chains `A_i(0),...,A_i(qm-1)` on disjoint
coordinate supports `U_i`. Send an index tuple to the union of its indexed
members. This is an injective order embedding, so the lifted chains are
actual set chains on their assigned shores.

For a chain `F` on support `U`, use

\[
 \beta_U(F)=(F_0,F_1\setminus F_0,\ldots,
                     F_{a-1}\setminus F_{a-2},U\setminus F_{a-1}), \tag{11}
\]

omitting empty letters. Its prefixes give the chain, its suffixes give its
complements in `U`, and it has at most `a+1` letters.

For every lifted pair `(F,G)`, use both directed arcs between the bridge
vertices `(U,F)` and `(U^c,G^c)`, with `G^c` reversed into ascending order.
At one boundary a suffix and prefix realize `X union Y`; at the reverse
boundary they realize its full complement. A nonempty target has at least
one nonempty witness piece. Empty-letter deletion preserves its interval.

For one macro rectangle, all lifted pairs form a complete bipartite graph,
which is connected. Thus the union of all template graphs has at most `t`
nonisolated components. Euler-assemble each component and include a closing
copy of its starting bridge. The arc tails cost at most the principal charge
plus twice the number of paired rectangles. Each closing bridge has at most
`dqm+2` letters. This proves (3). No asserted witness crosses a component join.

This also explains why a separate three-bridge linear word for each fine
rectangle would be the wrong accounting. The complete bipartite families
share their occurrences before they are cut into a linear word.

## 4. Unequal Lengths and the Extra Accumulator

The equal-length hypothesis does not leave an unproved robustness condition.
Given `d` actual chain lengths `a_i`, set

\[
                       b=q\lceil\max_i a_i/q\rceil.
\]

Map `[b]` monotonically and surjectively onto each input chain, repeating its
top member when necessary. Apply the indexed equal-length construction.
Remove repeated members within a resulting set chain, and omit empty bridge
letters. Form the bridges **after** this replacement, taking complements in
the actual coordinate supports. No complement-preserving map from a fictitious
larger alphabet is assumed. The indexed witnesses realize every actual target, and
the length only decreases. The principal charge is bounded by

\[
                         M(b/q)^{d-1}.                \tag{12}
\]

This is repetition of existing sets, not enlargement of the coordinate
universe. Near equal lengths, the padding is a vanishing volume proportion.
It can add multiplicities, but these are already charged by (12).

If another chain of length `r` must be included, adjoin it to the first shore
of every macro rectangle. Decompose each product `F x [r]` by the elementary
two-chain product SCD. It has `min(|F|,r)<=r` chains and membership `r|F|`.
Consequently the entire principal charge is at most `r` times (12). Every
child is retained. Dividing by the full product volume cancels `r` exactly.

There is also a uniform fallback. Isolate a longest factor and partition the
other factors into lines along a second-longest factor. Its normalized charge
is exactly

\[
                         {1\over a_{(d)}}+{1\over a_{(d-1)}}.      \tag{13}
\]

Choose the cheaper of (12) and this compiler. If `B` is the least of the
`d` retained lengths, the continuum normalized upper value is

\[
 T(\mathbf a)=\min\left\{
 {M\over q^{d-1}}{(\max a_i)^{d-1}\over\prod a_i},
 {1\over a_{(d)}}+{1\over a_{(d-1)}}\right\}\le {2\over B}.        \tag{14}
\]

This fallback is important: padding alone would give unnecessarily high
inverse powers of a small radius.

## 5. Proof of the Boolean-Cube Consequence

The only probabilistic ingredient reused is the minimum-clock analysis from
`SEVEN_ACCUMULATOR_SIX_STAIRCASE_UPPER_20260906_91bc7.md`, with `7` replaced by
`d+1`. Here are the details needed for this new terminal compiler.

Fix `n>=d+1`. Use `n` pivoted Boolean blocks, an SCD in each block minus its
pivot, and the usual `2^(n-1)` signed complementary product pairs. Keep
`d+1` labeled accumulator chains. Merge each unread factor into a shortest
accumulator using a complete product SCD, retaining every child. The choice
of accumulator is made before inspecting the unread length.

At a terminal tuple, set aside a shortest chain. Apply (12)-(14) to the other
`d` factors, and absorb the set-aside chain as in Section 4. This specifies
every actual chain family and every bridge word.

For fixed `n,q,d` the usual SCD inventory has uniform Gaussian moment bounds.
If `L` is the sum of the initial chain lengths, the initial merges have at
most `O(L^(n-d-1))` leaves. A template leaf after absorption has at most
`O(L^(d-1))` fine paired rectangles. Hence all endpoint letters number
`O(L^(n-2))` per initial tuple. Each template graph has at most `t` components;
closing its circuits costs `O(L)` per leaf, also `O(L^(n-2))` for `d>=2`.
The principal bound is `O(L^(n-1))`. After summing the SCD tuples, all
nonprincipal costs are `O_n(W(nh)/sqrt(h))`.

Volume-biased SCD lengths tend to `chi_3`, and a volume-biased product child
has kernel

\[
              K(a,b;dr)={r\over2ab}\mathbf1_{|a-b|<r<a+b}\,dr.    \tag{15}
\]

Use inputs `chi_3/sqrt(n)`. The fixed-`n` principal upper coefficient tends
to at most `sqrt(pi/8) E T(Y_{1,n},...,Y_{d,n})`, where the `Y` are the `d`
largest terminal radii. This normalization follows directly from

\[
 M_{\rm global}=2^{nh-1}\mathbb E_{\rm volume}
                           {P(\mathbf a)\over\prod a_i}.
\]

Couple the radii to `d+1` independent three-dimensional Brownian motions,
advancing a currently shortest path's clock by `1/n`. Let `omega_n` be their
maximum within-mesh oscillation. The `d` largest current radii lie in an
interval of length `omega_n`. If `A_n` is their maximum and

\[
 A=\sup\{a:\textstyle\sum_{i=1}^{d+1}\tau_i(a)\le1\},
\]

the deterministic first-hitting bounds give

\[
       A_n-\omega_n\le A\le A_n+2\omega_n,\qquad Y_{i,n}\to A
                                                        \tag{16}
\]

almost surely. Brownian scaling gives `A^(-2)` the law of `S_(d+1)`.

For clarity, reciprocal convergence is justified, not assumed. Put `r=d+1`.
The second smallest radius never decreases under minimum updates, and after
the initial `r` updates,

\[
 \mathbb E B_n^{-2}\le rn,\qquad
 \Pr(\omega_n>\epsilon)\le12rn e^{-n\epsilon^2/6}.
\]

The unit-ball exit time has mean `1/3` and the Markov-property bound
`Pr(tau>=t)<=2^(-floor(3t/2))`. Thus
`Pr(A<=u)<=r 2^(-floor(3/(2ru^2)))`. Take `epsilon=n^(-1/4)` and remove
`{omega_n>epsilon} union {A<=6epsilon}`. Its contribution to (14) is at
most `2 sqrt(rn Pr(bad))=o(1)`. On its complement, (14)-(16) give domination
by a constant times `1/A`, whose expectation is finite. Therefore

\[
 \limsup_n\sqrt{\pi/8}\mathbb E T(Y_n)
       \le {M\over q^{d-1}}\sqrt{\pi/8}\mathbb E(1/A)
       ={M\over q^{d-1}}\beta_{d+1}.                  \tag{17}
\]

The fixed-`n` Riemann limits use the unweighted polynomial bounds above;
integer padding changes only lower-order terms. Taking a slow diagonal in
`n`, followed by the ordinary top-bit splices, proves (4) in every dimension.
There is no unproved persistence, selector, or growing-rank matching premise.

## 6. A Better Exact Width for Three-Dimensional Tubes

The generic `m^2` chain count can be reduced for some nonsaturated macrochains.
For a chain `C` in `[q]^3`, label each successive step by the set of coordinates
which change. The size of the change, beyond being positive, does not matter.

- If any step changes just one coordinate, the exact tube width is `m^2`.
- Otherwise let `L` be one plus the longest run of identical two-coordinate
  change sets; put `L=1` if there is no such step. The exact tube width is
  \[
       \boxed{R_L(m)=\sum_{j=0}^{m-1}
                           \min\{m,L(2m-1-2j)\}.}     \tag{18}
  \]

Consequently its leading coefficient is

\[
 \boxed{\rho(C)=1\ \text{in the first case};\qquad
        \rho(C)=1-{1\over4L}\ \text{otherwise}.}       \tag{19}
\]

Examples are `3/4` for a single cube or a fully diagonal chain, `7/8` for one
two-coordinate jump, and `11/12` for two repeated jumps in the same two
coordinates. A long jump in just one coordinate still has coefficient one.

**Proof.** A one-coordinate jump contains an induced poset isomorphic to
`[2m] x [m] x [m]`, whose width is `m^2`; the generic tube partition supplies
the matching upper bound.

Otherwise, if an antichain has points in cells numbered `i<j`, not all three
coordinates can have changed between those cells: then every point in the
first cell would be below every point in the last. All intervening changes
must therefore be the same two-coordinate set. Every antichain lies in one
of the runs specified in (18), or in a single cell.

A run of `L` cells is isomorphic to

\[
              ([m]^2\oplus\cdots\oplus[m]^2)\times[m],            \tag{20}
\]

with `L` ordinal-sum copies. Glue equal-index square SCD chains through the
copies. Their lengths are `L(2m-1-2j)`. Product-SCD with `[m]` gives the upper
bound (18).

For the lower bound, divide the last coordinate into `L` consecutive bands
of sizes differing by at most one, allowing empty bands if `L>m`, in
decreasing order of cell index.
Antichains chosen in the different cell-band products are incomparable.
For a band of size `h`, the relevant three-box width is
`sum_j min(h,2m-1-2j)`. If the band sizes sum to `m` and differ by at most one,
their sum equals (18), term by term in `j`. This proves exactness. It also
covers `L=1`, giving `m^2-floor(m^2/4)`.

An actual optimal chain partition of the complete tube can be constructed
by the standard bipartite matching algorithm: use two copies of its point
set and edges `x_L -> y_R` whenever `x<y`. A maximum matching gives the
minimum chain cover by following its directed paths. The alternating-path
minimum vertex cover supplies the matching antichain bound. Thus (18) is
an actual set-chain compiler, not a rank-profile feasibility assertion.

Use (19) on three-coordinate shores and the upper factor one on other
shores. The new exact rectangle count and principal charge are
\[
 N_m=\sum_j R_{C_j}(m)R_{D_j}(m)\le t m^{d-2},
\]
\[
 P_m=\sum_j\bigl(|C_j|m^{r_j}R_{D_j}(m)
                  +|D_j|m^{s_j}R_{C_j}(m)\bigr),
 \qquad r_j+s_j=d.
\]
Thus the old rectangle-count identity becomes an upper bound. The
asymptotic principal coefficient replaces `M` by

\[
       \widehat M=\sum_j\{|C_j|\rho(D_j)+|D_j|\rho(C_j)\}          \tag{21}
\]

gives the corresponding asymptotic bound, with `O(m^(d-2))` additional
rounding error in the principal charge. Tube memberships and overlap are
unchanged. This improves some lifts, but did not close the finite gate below.

## 7. Exact Fractional Certificates, Not Words

Here the objective is the original flat charge (1), and every proper support
split and every strict chain is allowed.

### Positive Certificates

`q4d6_fractional_template_20260906_c52e9.py` records a seven-type fractional
cover of `[3]^6` of cost 306 and a fourteen-type fractional cover of `[4]^6`
of cost 1248. Each chain pair is developed uniformly under coordinate
permutations and simultaneous reflection of all coordinates.

For `[4]^6` the weights have denominator 15. Under this symmetry there are
44 point orbits, indexed by a coordinate-value histogram up to reversal.
For every orbit `O`, the checker verifies the integer inequality

\[
          \sum_j n_j\,|(C_j\times D_j)\cap O|\ge15|O|,
\]

and verifies `sum n_j(|C_j|+|D_j|)=18720`. This is exactly a fractional cover
of cost `18720/15=1248`. Its occurrence volume and excess are

\[
                       80608/15,\qquad19168/15.        \tag{22}
\]

The ternary certificate has cost 306, volume 927, and excess 198.

### Complete Lower Certificates

The C++ checker `qary_dual_verify_20260906_c52e9.cpp` gives nonnegative
coordinate-symmetric rational point weights `y_x` such that

\[
 \sum_{x\in C\times D}y_x\le |C|+|D|
                 \quad\text{for every strict chain pair}.       \tag{23}
\]

Their total weights are 306 on `[3]^6` and 1248 on `[4]^6`. Positive point
weights make (23) valid for covers with arbitrary overlap.

Here is how the universal quantifier is checked exactly. For each shore size
`r=1,2,3`, enumerate every chain `C` on that shore. For a point `z` on the
other shore put `g(z)=sum_(x in C) 12y_(x,z)-12`. The maximum of `sum g(z)`
over all chains `D` is computed by a grid dynamic program: at `z`, take the
maximum value in its immediate predecessor downsets and add `max(g(z),0)`.
Any chain extends to a saturated path; nonpositive nodes can be skipped.
Thus this dynamic program prices **every** nonsaturated right chain, not only
a chosen catalogue of paths. Its value must be at most `12|C|`.

The exact left-chain counts checked are

| Grid | `1+5` Split | `2+4` Split | `3+3` Split |
|---|---:|---:|---:|
| `[3]^6` | 7 | 103 | 3271 |
| `[4]^6` | 15 | 1007 | 257295 |

Coordinate symmetry handles every split of the same size; exchanging shores
handles the remaining sizes. All arithmetic in this lower certificate is
integer arithmetic. Together with the positive certificates, it proves (6).

### The Integral Gap

Lifting the audited five-row binary six-staircase cover by `m=2` gives an
integral `[4]^6` template of charge 1280 and 80 rectangles. Its 4096 targets
are checked directly. This proves the upper half of (5).

The 1248 certificate is not an integral template. Neither arbitrary
coordinate relabeling nor fractional multiplicity permits its substitution
into the literal compiler. In particular, independently rounding orbit
weights does not guarantee that every macro target is covered.

An 18,080-rectangle pool was formed from the fourteen positive orbit types
and the integral baseline. Two 120-second integer searches retained cost
1280. An exact search for every improving two-to-at-most-two replacement
from that pool found none. These are scoped search outcomes, **not** proofs
that the integral optimum is 1280.

Since `c_st=(5/4) beta_7`, the nominal constants are

| Template Charge | Coefficient From (4) |
|---:|---|
| ternary 306 | `(136/135)c_st = 1.1970311398...` |
| quaternary 1280 | `c_st = 1.1882294403...` |
| quaternary 1260, still missing | `(63/64)c_st = 1.1696633553...` |
| quaternary 1248, fractional only | `(39/40)c_st = 1.1585237043...` |

The exact concrete remaining gate is an **integral** `[4]^6` chain-pair cover
of cost at most 1260, or a comparably efficient weighted template under (21).
Its interval realizability and asymptotic amplification would then follow
from the already proved constructions above.

## 8. What Would Make the Coefficient Tend to One?

The flat lift (2) preserves `M/q^(d-1)` exactly under repeated homothetic
refinement. Therefore merely reapplying it to the same template does not
produce a self-improvement `f(c)<c`.

It does identify the quantization cost and the appropriate new finite target.
Let `W_q(d)` be the width of `[q]^d`. A chain-pair rectangle contributes at
most `min(|C|,|D|)` points to a fixed rank. Hence every integral or fractional
cover with the flat charge obeys

\[
                           M\ge2W_q(d).               \tag{24}
\]

For fixed `q>=2`, as `d` tends to infinity,

\[
 W_q(d)=(1+o(1))q^d\sqrt{6\over\pi d(q^2-1)},\qquad
 \beta_{d+1}=(1+o(1))\sqrt{\pi(d+1)/24}.              \tag{25}
\]

The first is the lattice local central limit theorem for sums of uniforms;
the second follows from `E tau=1/3`, the law of large numbers, and uniform
integrability. Thus the **flat nominal coefficient** has the lower limit

\[
                         {q\over\sqrt{q^2-1}}.         \tag{26}
\]

For `q=2,3,4,8` this is approximately `1.15470,1.06066,1.03280,1.00791`.
It is a limitation of this flat transfer ledger, not a lower bound on `nu`
or on the improved-width version (21).

Consequently a family of integral multi-bin covers satisfying
`M<=(2+o(1))W_q(d)`, with sufficiently large `d` for each growing `q`, would
give coefficient one through (4). The order of limits can be diagonalized:
first a fixed finite template, then its Boolean block size, then accumulator
count, and finally the template parameters. Such finite covers have **not**
been constructed here. Formula (26) explains why adding bins is a meaningful
new direction, but it is not their existence proof.

### Why an Arbitrary Finite OR Word Is Not Yet a Template

An interval word does not automatically give products of chains on disjoint
coordinate supports. Its left and right suffix/prefix chains can overlap in
coordinates, and independent refinement of their endpoints need not preserve
the old union. The tube compiler requires the actual chain-pair cover, not
just a short word or two endpoint chain partitions.

Even the naive word-length scaling fails in two coordinates. The word
`(1,0),(0,1)` is universal for the nonzero points of `[2]^2`. A word for the
nonzero points of `[2m]^2` needs at least `4m-2` letters: each positive value
on either coordinate axis must occur as an axis-supported letter, since an
interval maximum is attained at a letter. Thus a direct `2m+O(1)` lift of
that two-letter seed is impossible. Adding a zero macro letter changes the
proposed leading cost to `3m`, still too small. This does not exclude more
structured word compilers; it prevents assuming one from length alone.

## 9. Checks, Scope, and Reproduction

No existing file was modified. The new exact checkers need only Python's
standard library and a C++17 compiler:

```sh
python3 -B scratch/qary_tube_compiler_20260906_c52e9.py
python3 -B scratch/q4d6_fractional_template_20260906_c52e9.py
clang++ -std=c++17 -O2 -Wall -Wextra -pedantic \
  scratch/qary_dual_verify_20260906_c52e9.cpp \
  -o /var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/qary_dual_verify_20260906_c52e9
/var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/qary_dual_verify_20260906_c52e9
```

The tube checker tests 360 actual partitions in dimensions one through five,
including nonsaturated macrochains, and 72 exact minimum three-dimensional
widths. It also checks nine literal paired-product words, including ternary
templates and six-axis words using the improved three-dimensional widths.
The fractional checker verifies the complete orbit inequalities and exact
costs. The dual checker exhaustively prices all chain pairs as described above.

`qary_template_search_20260906_c52e9.py` is the exploratory LP/MILP and column
pricing driver. Its optional solver modes require NumPy/SciPy or HiGHS; none
is a premise of the exact certificates. The failed integer searches are
preserved, with no UNSAT or global integrality claim.

The existing cautions checked include the fixed-split and synchronous-tensor
density barriers, the three-box endpoint/precedence obstructions, the paired
SCD seed-scaling obstruction, and the explicit overlap qualifications in the
cross-hook and six-staircase notes. This work does not redo the binary
Catalan family or optimize the centered Bellman recursion. Its unresolved
part is the integral multi-bin template, not a hidden interval compiler.
