# Independent audit of `MULTISCALE_DIRECTION_COUPLING_NEXT.md`

## 1. Verdict

**PASS WITH LOCAL PRESENTATION REPAIRS AND A STRICT SCOPE
QUALIFICATION.**

I independently reconstructed the finite contraction law, the lifetime
bound, both broad ledgers, the direction--level coloring, the scalar
functional, the cross-line contradiction, and the quantitative wedge-cover
argument.  I found no substantive mathematical error in the frozen source.

Subject to the inherited audited three-box framework, the following new
statements are valid.

1. Tail predecessor lists at different thresholds are contractions of one
   marked order.  A surviving successor's predecessor gap is nondecreasing,
   and deleted plateau blocks and intervening gaps add exactly in an edge-slot
   convention.
2. The particular broad *static* family from
   `MIXED_PROFILE_SEAM_NEXT.md` cannot be the family of tail ledgers of one
   labelled order: on a positive surviving length band it would make a
   predecessor gap decrease from macroscopic size to zero.
3. There is nevertheless one explicit alternating-pair order whose tail
   contractions have broad length measure
   \[
                    2\mathbf 1_{[1,2]}(s)\,ds,
   \]
   obey the additive gap law at every fixed threshold, admit one fixed
   direction-labelled absorption allocation, and have scalar value strictly
   greater than four at every `1<c<2`.
4. That particular direction--level lift cannot be embedded by actual
   selected coordinate lines in the hexagon.  At `c downarrow 1`, line
   uniqueness forces intersecting-pair density at least `1/4`, while the
   cross-line inequality would require zero.
5. More generally, every actual broad-profile plateau family has at least
   \[
                     (5-2\sqrt6)a-o(a)
   \]
   plateaux on nonpositive fixed-coordinate lines.  Consequently its
   integrated absorption mass is at most
   \[
       \frac12-\frac{(5-2\sqrt6)^2}{8}+o(1).
   \]

The fifth statement does **not** exclude all broad profiles.  Its numerical
deficit is only
\[
  \frac{(5-2\sqrt6)^2}{8}=0.0012756\ldots,
\]
and no proved argument turns it into a strict-sub-four seam assignment at a
common threshold.  Broad, partially absorbed, jointly direction--level
realizable processes remain open.  In particular, this note does not prove a
quadratic lower bound for every three-box word and does not prove the
contiguous-OR conjecture.

Four local qualifications should accompany the source.

* Equation (2.3) is literally exact after gaps and plateau lengths are both
  counted in **word-edge slots**.  With the source's displayed set of word
  positions, every deleted plateau can contribute one endpoint correction.
  The total correction is `O(a)`, hence negligible in every normalized use.
* In Section 3, the contradiction between limiting gap allocations should
  use a bounded continuous monotone cutoff instead of the displayed sharp
  indicator, or first choose its cutoff away from every limiting atom.  The
  two gap populations are separated by a fixed positive amount, so this is a
  routine repair.
* The two copies of each finite integer length in Section 4 should be placed
  consecutively in the pair-occurrence order.  Then the explicit period-three
  direction coloring below proves the claimed no-reuse property.  The sole
  midpoint coincidence `L=H=3/2` is omitted or changed at `O(1)` cost.
* Formula (6.13) is most cleanly read as an infimum over submeasures of the
  broad measure, rather than only literal Borel subsets.  Since the broad
  measure is atomless, both formulations have the same value `q^2/8`.

None of these repairs changes a constant or a theorem.

## 2. Frozen sources

The source audited here is frozen at

```text
b13b7bd5ced0626fb1bf559764f4539ada905c363732a73b56b039620b8e1336  MULTISCALE_DIRECTION_COUPLING_NEXT.md
```

The principal inherited sources checked were

```text
01d863d66cf2a0a2e0fdc13f8b4e1b52d109de96c1c798819dc3e8a4cf4abd60  MIXED_PROFILE_SEAM_NEXT.md
6d5a31f5fe6221345ee9ba1916767bfd58f8570e8d4715dc3ea9857d30392ac5  MIXED_PROFILE_SEAM_INDEPENDENT_AUDIT.md
ae96c591b036233dd8a9250917e70b1b7c0425b38a20f3a1d97383cfa8493a31  POSITIVE_SEAM_CROSSLINE_COUPLING.md
3b16ee5b2e5d851090895c4c18d2d20da7daaabedb9943de65d19e81409875e3  POSITIVE_SEAM_CROSSLINE_COUPLING_AUDIT.md
34287b12488dd4e639b00f02af3d56336e37114ea96a5d03b635cb7434a811b9  LARGE_DEFECT_DICHOTOMY_NEXT.md
a0ab3855e954c353b6bb5bbf7c2e822eba52a2887ce298da2c8adb39842e696e  LARGE_DEFECT_DICHOTOMY_INDEPENDENT_AUDIT.md
```

## 3. Finite tail contraction and gap addition

Give the word edges the half-open indices between consecutive word
positions.  Each plateau then owns a disjoint interval of `lambda_i` edge
slots.  At threshold `h`, delete precisely the plateau intervals with
`lambda_i<=h` and retain their physical identities in the ordered list.

If `i` survives at both `h_1<h_2`, its predecessor at `h_2` is obtained by
iterating the `h_1` predecessor until the first plateau surviving `h_2` is
reached.  This proves

\[
                    \pi_{h_2}(i)=\pi_{h_1}^{q}(i).
\]

Suppose the deleted active-at-`h_1` plateaux between the new predecessor and
`i` are `j_1,...,j_r`.  In edge slots, the interval between the new
predecessor and `i` is the disjoint union of

* the old gap immediately preceding `i`;
* each deleted plateau's `lambda_{j_q}` edge slots; and
* the old gap immediately preceding that deleted plateau.

Therefore

\[
 g_{h_2}(i)=g_{h_1}(i)+
       \sum_{q=1}^r\bigl(\lambda_{j_q}+g_{h_1}(j_q)\bigr) .
\]

In particular `g_{h_2}(i)>=g_{h_1}(i)` for the same physical successor.
If gaps are instead sets of word *vertices*, a deleted closed plateau brings
one extra endpoint unless it is already owned by a neighbouring block.  This
is exactly the source's stated endpoint-convention issue.  There are `O(a)`
long plateaux, so even one unit per contraction changes total gap mass by
`O(a)` and every cubic seam ledger by only `O(a^2)=o(a^3)`.

The edge `j->i` is present precisely when both endpoints survive and every
strictly intervening plateau is deleted.  Hence its threshold lifetime is

\[
 \max_{j<q<i}\lambda_q\le h<\min\{\lambda_j,\lambda_i\}.
\]

For a linear word there is no wraparound predecessor.  Removing the first
survivor at each of finitely many fixed thresholds costs one mark per
threshold, hence `O(1/a)` in normalized seam count.  A countable diagonal
subsequence is enough for all later limiting uses; no uniform assertion over
uncountably many thresholds is required.

## 4. Absorption lifetime

Fix a surviving successor of normalized length `s`, fixed-coordinate level
`t`, and current predecessor length `p_c`.  Filtering at a larger threshold
can only replace a deleted predecessor by a plateau longer than that new
threshold, so `p_c` is nondecreasing at its jumps.  More directly, whenever
the seam is absorbed,

\[
                       p_c-1\le t\le2-s,
\]

and predecessor activity gives `p_c>c`.  Thus every absorption threshold is
contained in

\[
              1<c<\min\{s,1+t\}.
\]

Its total Lebesgue measure, even if direction changes make the actual set
disconnected, is at most

\[
 \min\{s-1,t\}_+le \min\{s-1,2-s\}_+.
\]

For the broad measure this integrates to

\[
 2\int_1^{3/2}(s-1)\,ds+2\int_{3/2}^2(2-s)\,ds
 =\frac12.
\]

The original static reflected ledger absorbs normalized mass
`2(3-2c)` on `1<c<3/2`; its threshold integral is also `1/2`.  Hence it
saturates rather than violates this bound.  Equality for a successor with
`s>3/2` forces `t=2-s`, exactly as stated in the source.

## 5. Why the old broad static family is not nested

For `1<c<3/2`, the old static construction uses

\[
 r(c)=\sqrt{2(c^2-3c+4)},\qquad
 z_c(s)=s\mathbf1_{[3-c,r(c)]}(s).
\]

Here `r'(c)=(2c-3)/r(c)<0`, while

\[
 r(c)^2-(3-c)^2=c^2-1>0.
\]

Choose `c_1<c_2` sufficiently close that `r(c_2)>3-c_1`.  The positive
length band

\[
                         B=(r(c_2),r(c_1))
\]

lies above both thresholds.  At `c_1`, every successor in this band has
normalized predecessor gap `z=s>=r(c_2)`; at `c_2`, the same displayed
ledger gives `z=0`.  But finite contraction says that the gap attached to
the same surviving physical plateau cannot decrease.

To phrase this entirely in weak-limit language, take a continuous
nondecreasing function which is zero below `r(c_2)/4` and one above
`r(c_2)/2`.  The marked-gap integral over physical successors with lengths
in a slightly shrunken subband of `B` is positive at `c_1`, zero at `c_2`,
contradicting monotonicity.  A linear word loses only one possible first
successor.  Thus the particular thresholdwise static family is genuinely
non-nested.

This proves nothing against the broad length marginal itself.

## 6. The alternating-pair nested ledger

### 6.1 Finite discretization and additive gaps

At integer scale, omit the single midpoint if necessary and take each low
edge length

\[
                      r\in[a,3a/2]
\]

twice.  Pair it with the complementary high length `3a-r`, and put the two
copies consecutively:

\[
 L(r),H(r),L(r),H(r).
\]

Grouping these occurrences into `K_a` bins with
`K_a->infinity`, `K_a=o(a)` ensures that lengths in a bin differ by `o(a)`
and that the one threshold-cut bin contains only `o(a)` plateaux.  There are
`a+o(a)` pair occurrences and `2a+o(a)` plateaux.  Their empirical measure
is

\[
            \frac1a\sum_i\delta_{\lambda_i/a}
       \Longrightarrow2\mathbf1_{[1,2]}(s)\,ds.
\]

Initially give consecutive blocks zero edge gap.  If `1<c<=3/2`, then:

* for `u>c`, both `L(u)` and `H(u)` survive and consecutive edges have
  `p=3-s`, `z=0`;
* for `u<c`, only `H(u)` survives, and the deleted low block immediately
  before the next high block gives `p=s+o(1)`, `z=3-s+o(1)`.

For `3/2<c<2`, all lows are deleted and the surviving high bins form a
prefix, giving `p=s+o(1)`, `z=3-s+o(1)` internally.  Deleted terminal bins
belong to the outside-word reservoir and are not an internal predecessor
gap.  There are only `O(K_a)=o(a)` bin-transition edges, with total edge
mass `O(K_a a)=o(a^2)`.  Thus the limiting ledger is exactly (4.7)--(4.8),
and at finite scale every deletion obeys the additive formula of Section 3.

### 6.2 Exact three-color assignment

Index the plateau occurrences in the displayed four-term blocks and assign
fixed-coordinate directions periodically

\[
                         d_n=n\pmod3.
\]

Adjacent directions differ.  The two copies of a low length occupy
positions differing by two, as do the two copies of its complementary high
length, so equal length--hence equal level--copies also receive different
directions.  Distinct lengths have distinct levels under

\[
                         t=2-s.
\]

The midpoint `s=3/2`, where low and high coincide and four copies would
request one level, is one `O(1)` exception and may be omitted.  Hence no
direction--level pair is reused.

Orient plateau `n` so that its rising cross-coordinate is `d_{n+1}`.  This
is possible because `d_n!=d_{n+1}`.  Every reflected edge surviving a
threshold is an original adjacency, so it absorbs on the successor line at

\[
                  t=2-s=p-1.
\]

Contracted high--high edges are deliberately nonabsorbed.  The total level
pushforward is `2 dt` on `[0,1]`, while each direction receives limiting
density `2/3`, below its separate capacity `dt`.  The assignment is fixed
before `c` is chosen.  Thus the source's direction-labelled capacity claim
is valid; it is not merely the weaker aggregate `3 dt` claim.

This coloring is only an abstract line-label allocation.  It does not claim
that all of those complete coordinate lines can coexist with disjoint
plateau intervals in `H_a`.

## 7. Scalar value of the nested ledger

For every threshold,

\[
                         e_c=(2-c)^2.
\]

A nonabsorbed high edge has

\[
 p=s,\qquad z=3-s.
\]

Therefore its seam density and guaranteed saving are

\[
 (s-c)(3-s),\qquad
 \phi(s,s,3-s)=\min\{s,1\}(2s-3)=2s-3.
\]

For `1<c<=3/2`, integrating over `3-c<s<=2` gives

\[
 U_1(c)=\frac{29}{3}-10c+7c^2-\frac53c^3.
\]

Its derivative is `-10+14c-5c^2<0`, so

\[
                    U_1(c)-4\ge U_1(3/2)-4=\frac{19}{24}.
\]

For `3/2<=c<2`, integrating over `c<s<=2` gives

\[
 U_2(c)=\frac{56}{3}-19c+7c^2-\frac13c^3.
\]

Its unique interior minimum is at `c=7-sqrt(30)`, with

\[
 U_2(c)-4=\frac{331}{3}-20\sqrt{30}
          =0.788821\ldots>0.
\]

The two formulas agree at `c=3/2`.  Consequently one and the same nested
scalar process has `U(c)>4` for every fixed `1<c<2`.  Exact threshold
contraction, additive gaps, fixed direction labels, and separate line
capacity therefore do not suffice by themselves for a strict-sub-four
theorem.

## 8. Cross-line failure of the explicit lift

For the explicit lift, reflected absorption forces `t=2-s`.  Letting fixed
continuity thresholds decrease to one, the exceptional contracted high
block has mass `O(c-1)` and vanishes.  The total limiting level measure is

\[
                      \nu_x+\nu_y+\nu_z
                  =2\mathbf1_{[0,1]}(t)\,dt.
\]

Line uniqueness gives `nu_d<=dt`.  Put

\[
                         a_d=\nu_d([0,1/2]).
\]

Then `sum_d a_d=1` and `0<=a_d<=1/2`.  A line at level `u` in one direction
and a line at level `v` in another genuinely intersect in `H_a` whenever
`u+v<=1`; hence all cross-direction pairs from `[0,1/2]` intersect.  Thus

\[
 I\ge a_xa_y+a_ya_z+a_za_x
   =\frac{1-\sum_d a_d^2}{2}\ge\frac14.
\]

All selected limiting levels are nonnegative.  A triple intersection
requires their three signed levels to sum to zero, so only the zero-level
exception is possible; absolute continuity gives `theta=0`.  Also

\[
                         f=2,\qquad \ell=3,\qquad \tau=1.
\]

The exact complete-line-union inequality

\[
                         \ell\le2f-\tau-I+\theta
\]

would then require `I<=0`, contradicting `I>=1/4`.  This argument uses only
fixed positive thresholds followed by a diagonal subsequence and then
`c downarrow 1`; it does not invoke a theorem at the literal threshold one.

## 9. The integrated absorption deficit

Let `q_a a` be the number of broad-family plateaux on nonpositive fixed
lines.  Broad convergence gives

\[
 \#\{P\}=(2+o(1))a,
 \qquad \sum_P\lambda(P)=(3+o(1))a^2.
\]

The selected plateau edge intervals are disjoint and their vertex overlaps
are `O(a)`.  Since `|H_a|=3a^2+3a+1`, their vertex union, and hence the union
`Lambda` of their complete fixed-coordinate lines, misses only `o(a^2)`
hexagon points.

There are `a` positive integer levels in each of three directions.  At most
`(2-q_a+o(1))a` distinct positive lines are selected, so if `r_d` positive
levels are missing in direction `d`, then

\[
                         r_x+r_y+r_z
                    \ge(1+q_a+o(1))a.
\]

For a missing positive level `t`, take the `t-1` points on that line whose
other two coordinates are strictly negative.  These wedge sets are disjoint
over all directions and levels, and none lies on a selected positive line.
For `r_d` missing levels, their total size in direction `d` is at least
`r_d(r_d-1)/2`.  Convexity therefore gives total wedge size

\[
 \sum_d\frac{r_d(r_d-1)}2
 \ge\frac{(r_x+r_y+r_z)^2}{6}-O(a).
\]

A fixed nonpositive line intersects at most `a` such wedge points in each of
the other two directions, hence at most `2a` in total.  Since `Lambda`
misses only `o(a^2)` points,

\[
                  \frac{(1+q)^2}{6}\le2q
\]

for every limit point `q` of `q_a`.  The relevant root is

\[
                         q\ge q_0=5-2\sqrt6.
\]

An absorbed successor must have positive level because
`t>=p_c-1>c-1>0`.  Thus no nonpositive-line plateau absorbs.  Define

\[
                         w(s)=\min\{s-1,2-s\}.
\]

Under the broad measure, the distribution function near the two endpoints
satisfies `mu{w<=r}=4r` for `0<=r<=1/2`.  The bathtub principle therefore
gives, for every submeasure of normalized mass `q`,

\[
                     \int w\,d\sigma\ge
                     \int_0^q\frac u4\,du=\frac{q^2}{8}.
\]

Summing the individual lifetime bound from Section 4 and deleting the
nonpositive subfamily yields

\[
 \limsup_{a\to\infty}\int_1^2A_a(c)\,dc
 \le\frac12-\frac{(5-2\sqrt6)^2}{8}.
\]

This argument actually proves the displayed deficit for every actual broad
realization; the preliminary saturation assumption is needed only for the
short contradiction “almost every plateau would have to absorb.”

## 10. Combined process and large-defect scope

An actual word supplies one physical marked order, and every fixed-threshold
ledger is obtained from it by deletion.  Its absorption labels obey the same
direction--level constraints, its line marginals obey the exact cross-line
inequality, and its seam cost uses the actual contracted triples.  Thus the
combined process (7.1)--(7.4) is a valid necessary relaxation, after taking
limits along countably many continuity thresholds.  The notation
`alpha_d(c)` for direction mass should not be confused with the absorbed
seam submeasure `alpha_c`; this is only a notation issue.

If one proved that every such realizable process has `U(c)<4` at one common
threshold, the forward seam assignment would satisfy the hypotheses of the
audited large-defect transfer theorem and force a positive quadratic defect.
The alternating-pair object proves that Items 1--3 and scalar cost alone
cannot give that theorem.  Its line contradiction removes only that one
explicit lift.  The integrated deficit removes exact lifetime saturation,
not all partial-absorption tradeoffs.

## 11. Adversarial stress tests

### 11.1 Threshold atoms

All continuum comparisons may be made at continuity thresholds.  The broad
measure is atomless, and the bin containing a fixed threshold has `o(a)`
marks.  No mass is silently lost at `s=c`.

### 11.2 Macroscopic gaps and terminal bins

Gap monotonicity remains true for macroscopic gaps.  In the alternating
order, terminal deleted bins for `c>3/2` lie after the last survivor and are
not internal predecessor gaps.  Treating that boundary reservoir as a seam
would be an overcount; the source correctly discards it.

### 11.3 Direction labels

Aggregate `3 dt` is not being confused with three separate resources.  The
explicit period-three coloring satisfies each separate `dt` constraint and
the predecessor-rise equality on every absorbed original adjacency.

### 11.4 Same-line repetitions

The duplicate-length coloring prevents same direction--level reuse.  In the
general wedge theorem, repeated selected lines only reduce the number of
distinct positive lines and make the missing-level bound stronger.

### 11.5 Triple intersections

The lower bound on `I` counts intersecting *pairs*, including pairs meeting
at a triple point.  Inclusion--exclusion restores triple points through
`theta`.  For the explicit nonnegative-level lift, all positive-density
triple intersections are impossible, so `theta=0` is legitimate.

### 11.6 The limit `c downarrow 1`

No uniform threshold theorem is used.  Apply every finite inequality at a
fixed `c>1`, take a common subsequence, and only then send a countable
sequence of continuity thresholds down to one.  The nonreflected mass is
`O(c-1)`.

### 11.7 Partial absorption

The source does not prove that the small lifetime deficit forces a
strict-sub-four threshold.  A broad process may use fewer positive absorbing
lines, alter its predecessor coupling and gaps, and trade the resulting seam
saving against cross-line geometry.  Excluding every such jointly realizable
process is precisely the remaining problem.

## 12. Exact theorem ledger

### Certified by this audit

1. Finite tail contraction, predecessor-gap monotonicity, additive gap
   merging, and contiguous lifetime of each fixed predecessor edge.
2. Non-nestedness of the old thresholdwise broad static family.
3. Existence of one common alternating-pair broad scalar ledger satisfying
   the contraction law at every fixed threshold.
4. A finite, fixed, direction-labelled capacity assignment for its absorbed
   reflected edges.
5. The scalar formulas `U_1`, `U_2`, and `U(c)>4` for all `1<c<2`.
6. Non-realizability of that explicit lift by selected hexagon lines, via
   `I>=1/4`.
7. The wedge-cover lower bound `q>=5-2sqrt(6)` and integrated absorption
   deficit `(5-2sqrt(6))^2/8` for every actual broad realization.
8. The combined marked-process relaxation as a necessary condition on any
   actual order.

### Not certified or claimed

1. Exclusion of every partially absorbed broad marked process.
2. A strict-sub-four threshold for every mixed plateau profile.
3. A quadratic lower bound for unrestricted three-box words.
4. A subquadratic three-box construction.
5. A realizable broad order in the hexagon.
6. The all-`k` contiguous-subarray OR formula.

The next valid target is exactly the source's final one: couple one nested
predecessor process to the same fixed direction--level line arrangement and
its cross-line/additive-triple geometry, then prove that no partially absorbed
broad tradeoff can keep the seam value at least four at every threshold.
