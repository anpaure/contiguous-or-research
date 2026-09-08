# K16 global free-run Farkas inequalities and the exact waste-three scalar boundary

Date: 2026-07-30  
Lane: A  
Status: source-independent necessary inequalities; explicit scalar countermodels; no new K16 lower bound

## 1. Scope and conclusion

Let

\[
 A=(A_0,\ldots,A_{L-1}),\qquad A_i\ne\varnothing,
\]

be a hypothetical universal contiguous-OR word on `[16]`, and suppose

\[
 L=12873,\qquad r=8,\qquad W=\binom{16}{8}=12870.       \tag{1.1}
\]

This note uses only architecture-free consequences of universality.  Its
main positive conclusions are:

1. every first-middle column has lower-prefix depth at most `e-G`, not only
   delivery columns;
2. the complete one-coordinate phase ledger is

   \[
   \ell_x+E_x=3+a_x;
   \]

3. the coordinate-pair Hall cuts imply the rational Farkas inequality

   \[
   11\Delta+60N\ge51636;
   \]

4. every putative word has at least `1561` coordinate-free runs in total,
   hence at least `3092` units of adjacent Hamming variation.

These statements do **not** force a fourth first-delivery waste unit.  An
explicit integral independent-column model satisfies the inventory,
coordinate, aggregate pair, singleton and numerical run inequalities with
waste three.  A separate static model satisfies the entire subset-free
cardinality hierarchy.  Neither supplies a common delivery chronology.  The
intersection of all pointwise subset cuts with a common-order run system
remains open, as does the still stronger literal overlap problem.

## 2. First-middle inventory and a stronger depth cap

For a left endpoint `p`, let `f_p` be the number of initial interval ORs

\[
 A_p,\quad A_p\cup A_{p+1},\quad\ldots
\]

whose rank is below eight.  At the first rank-at-least-eight OR, call `p` a
delivery if the rank is eight and a jump if it is larger; if there is no such
OR, call it a stall.  As in the audited first-delivery inventory, let `F` be
the number of same-target, same-deadline flat extras and `G` the number of
same-target, different-deadline ghost extras.  Put

\[
 S=\#\{\hbox{stalls}\},\qquad J=\#\{\hbox{jumps}\},
 \qquad N=S+J.                                           \tag{2.1}
\]

Universality gives the exact inventory

\[
 L-W=N+F+G.                                              \tag{2.2}
\]

### Lemma 2.1 (all-endpoint depth cap)

For every endpoint `p`,

\[
                         f_p\le L-(W+G).                 \tag{2.3}
\]

#### Proof

There are exactly `W+G` distinct delivery deadlines.  If `f_p=t>0`, put
`q=p+t-1`; then `U(p,q)` has rank below eight.  At most `p` delivery groups
have a representative start before `p`.  Any remaining group has all its
starts at least `p`.  Its deadline must exceed `q`, since otherwise one of
its rank-eight delivery intervals would be contained in the rank-below-eight
interval `[p,q]`.  The remaining distinct deadlines occupy at most
`L-1-q` positions.  Consequently

\[
 W+G\le p+(L-1-q)=L-t.
\]

The case `t=0` is immediate.  This proves (2.3), including stalls and jumps.
\(\square\)

Every lower target occurs in one of the lower-prefix cells.  Put

\[
 \Lambda=\sum_{s=1}^{7}\binom{16}{s}=26332.
\]

Writing `d=3-G` and retaining the shortening of the final columns gives the
sharp scalar envelope

\[
 \Lambda\le\sum_{p=0}^{L-1}\min\{d,L-p\}
          =dL-\binom d2.                                 \tag{2.4}
\]

If `G>=1`, the right side is at most `2*12873-1=25745`, a contradiction.
Therefore every word in the scope of (1.1) obeys

\[
                         \boxed{G=0,\qquad N+F=3.}       \tag{2.5}
\]

The same conclusion holds after reversal.

## 3. Free-coordinate filtering

For `X subseteq [16]`, delete every letter meeting `X` and concatenate the
maximal surviving runs.  Write

\[
 c_X=\#\{p:A_p\cap X=\varnothing\}.                      \tag{3.1}
\]

### Lemma 3.1 (free-set filter)

For every proper `X subset [16]`,

\[
                         \boxed{c_X\ge\nu(16-|X|).}       \tag{3.2}
\]

#### Proof

Every nonempty target contained in `[16]\X` has an original witness which
uses no letter meeting `X`.  That witness lies wholly in one maximal
`X`-free run and remains contiguous after the runs are concatenated.  The
filtered word is therefore universal on `[16]\X`.  \(\square\)

Concatenation creates virtual seams.  Lemma 3.1 transfers a length bound,
not a run-count, residence or chronology theorem.

For one coordinate `x`, abbreviate `c_x=c_{\{x\}}`.  Since
`nu(15)=6438`, put

\[
 c_x=6438+a_x,\qquad a_x\in\mathbb Z_{\ge0}.             \tag{3.3}
\]

## 4. Corrected extra-incidence vector

Let `D_x` be the number of delivery occurrences whose rank-eight target
omits `x`.  There are exactly

\[
 \binom{15}{8}=6435
\]

distinct such targets.  Since `G=0`, the surplus

\[
 E_x=D_x-6435                                             \tag{4.1}
\]

counts flat extras whose delivered target omits `x`.  Let `ell_x` count
`x`-free endpoints which are stalls, jumps, or deliveries of a target
containing `x`.  Partitioning all `x`-free endpoints gives

\[
 c_x=6435+E_x+\ell_x,
\]

and hence the exact coordinate equation

\[
                         \boxed{\ell_x+E_x=3+a_x.}       \tag{4.2}
\]

Every flat contributes the complement of one rank-eight target to `E`.
Thus

\[
 E\in F\Delta(16,8)\cap\mathbb Z^{16},                  \tag{4.3}
\]

or equivalently

\[
 0\le E_x\le F,\qquad \sum_xE_x=8F.                     \tag{4.4}
\]

Conversely, (4.4) characterizes the integer points in (4.3).  Indeed it is
the degree-sequence condition for an `F` by `16` zero-one matrix with every
row sum eight.  For any `s` of the `F` row vertices,

\[
 \sum_x\min\{E_x,s\}\ge {s\over F}\sum_xE_x=8s
\]

when `F>0`; this is the Gale/max-flow condition.  Integral flow gives the
required decomposition into `F` eight-subsets.  The case `F=0` is trivial.

Put

\[
 \delta=\sum_xa_x,
 \qquad
 \Delta=\sum_{p=0}^{L-1}(8-|A_p|).                       \tag{4.5}
\]

The second quantity is signed; letters above rank eight contribute
negatively.  Summing (3.3) and (4.2) gives the exact identities

\[
 \boxed{\Delta=24+\delta,\qquad
        \sum_x\ell_x=\Delta+8N.}                         \tag{4.6}
\]

This is the correction missed by an argument which assigns all `48`
surplus one-coordinate incidences to the three nonprimary positions.  Flat
delivery occurrences contribute the vector `E`, and primary delivery cells
may omit coordinates of their targets.

## 5. The atom identity and forced singleton charge

Choose one primary delivery occurrence for every rank-eight target.  Every
other delivery is now a flat.  Since a delivery start satisfies
`A_p subseteq T_p`, equation (4.2) has the coordinatewise atom form

\[
 \boxed{
 \ell+E=
 \sum_{p:\ p\text{ is primary}}\mathbf1_{T_p\setminus A_p}
 +\sum_{p:\ p\text{ is flat or a nondelivery}}
       \mathbf1_{[16]\setminus A_p}.}                    \tag{5.1}
\]

For a flat, the two parts are exactly

\[
 \mathbf1_{[16]\setminus T_p}+
 \mathbf1_{T_p\setminus A_p}
 =\mathbf1_{[16]\setminus A_p}.
\]

Universality forces a literal singleton letter `{x}` for every coordinate
`x`; these sixteen sites are distinct.  A primary singleton contributes
seven atoms to (5.1).  A flat or nondelivery singleton contributes fifteen.
Charge seven to each of the sixteen singleton sites.  Every flat supplies a
further eight atoms: if it is a singleton these are the remaining eight of
its fifteen, and otherwise `A_p subseteq T_p` gives `|A_p|<=8`.
Consequently

\[
 \|\ell+E\|_1\ge112+8F.
\]

Since `ell+E=3*1+a`, this proves

\[
                         \boxed{\delta\ge64+8F.}         \tag{5.2}
\]

There is a small but genuine physical strictness.

### Proposition 5.1 (equality is not chronological)

Every physical universal word in the scope of (1.1) satisfies

\[
                         \boxed{\delta\ge65+8F.}         \tag{5.3}
\]

#### Proof

Suppose equality held in the atom charge.  Then there are exactly sixteen
singleton sites.  Every non-singleton primary has `A_p=T_p`; every
non-singleton flat has `A_p=T_p`; and every non-singleton nondelivery is the
full set.  If `b` singleton sites are flats, then `16-b` singleton sites are
modified primaries.  The remaining `F-b` non-singleton flats can supply the
literal rank-eight letter of at most `F-b` of those modified targets.
Therefore at least

\[
 (16-b)-(F-b)=16-F\ge13                                  \tag{5.4}
\]

distinct modified primary targets have no contained letters available other
than their eight singleton letters.  A witness for each such target must be
a contiguous block of exactly those eight singleton sites.  Sixteen ordered
singleton sites have at most nine length-eight contiguous blocks, even when
they occupy consecutive physical positions.  This contradicts (5.4).
Thus equality is impossible, and integrality gives (5.3).  \(\square\)

Proposition 5.1 strengthens the phase slack, not the first-delivery inventory
`N+F=3`; it therefore does not prove waste four.

## 6. The coordinate-pair Hall/Farkas certificate

Fix a coordinate pair `X={x,y}`.  Exactly

\[
 \binom{14}{8}=3003
\]

distinct middle targets avoid `X`.  Let `E_X` count flat delivery extras
whose target avoids `X`, and let `ell_X` count `X`-free endpoints which do
not deliver such a target.  The exact pair ledger is

\[
 c_X=3003+E_X+\ell_X.                                    \tag{6.1}
\]

Lemma 3.1 and `nu(14)=3434` give

\[
                         E_X+\ell_X\ge431.               \tag{6.2}
\]

Moreover `ell_X<=ell_x+ell_y` and `E_X<=F`, so pointwise

\[
 \boxed{\ell_x+\ell_y\ge431-E_X\ge428+N.}               \tag{6.3}
\]

Equivalently,

\[
 a_x+a_y\ge425+E_x+E_y-E_X,                              \tag{6.4}
\]

where the correction on the right counts flat extras omitting at least one
of `x,y`.

The aggregate pair inequality is substantially stronger.  Put

\[
 d_p=16-|A_p|.
\]

Summing Lemma 3.1 over all `120` pairs gives

\[
 \sum_p\binom{d_p}{2}\ge120\cdot3434=412080.             \tag{6.5}
\]

There are `L-N` delivery starts and `N` nondeliveries.  At a delivery,
`8<=d_p<=15`, and convexity between the endpoints gives

\[
 \binom{d_p}{2}\le28+11(d_p-8)=11d_p-60.                \tag{6.6}
\]

At a nondelivery, `0<=d_p<=15` and

\[
 \binom{d_p}{2}\le11d_p.                                \tag{6.7}
\]

Since `sum d_p=8L+Delta`, (6.5)--(6.7) yield the exact rational
Farkas cut

\[
 \boxed{11\Delta+60N\ge51636.}                          \tag{6.8}
\]

Thus the four inventory faces obey

\[
\begin{array}{c|c|c|c}
N&F&\Delta\text{ lower bound}&\delta=\Delta-24\text{ lower bound}\\ \hline
0&3&4695&4671\\
1&2&4689&4665\\
2&1&4684&4660\\
3&0&4678&4654
\end{array}                                               \tag{6.9}
\]

This is the strongest new scalar restriction in the present lane.  It
correctly retains repeated-delivery incidence: each flat supplies exactly
`binom(8,2)=28` pair incidences, rather than being silently discarded.

It also forces many genuinely non-immediate deliveries.  If

\[
 P=\sum_{p:\ p\text{ is a delivery}}(8-|A_p|),
\]

then the `N` nondeliveries contribute at most `7N` to `Delta`, so

\[
                         P\ge\Delta-7N.                  \tag{6.10}
\]

As one delivery contributes at most seven, the four faces `N=0,1,2,3`
have respectively at least

\[
                         671,\ 669,\ 668,\ 666           \tag{6.11}
\]

non-immediate delivery starts.

More generally, summing Lemma 3.1 over all coordinate `h`-sets gives the
valid zeta hierarchy

\[
 \boxed{
 \sum_p\binom{16-|A_p|}{h}
 \ge\binom{16}{h}\nu(16-h),\qquad 1\le h\le15.}          \tag{6.12}
\]

## 7. Exact phase-run inequalities

For a coordinate `x`, let the maximal linear `x`-free run lengths be
`lambda_(x,1),...,lambda_(x,t_x)`.  Let `s_(x,1)` and `s_(x,2)` count runs of
length one and two.  The numbers of internal intervals of lengths at most
three and four are exactly

\[
 H_{3,x}=3c_x-3t_x+s_{x,1},                              \tag{7.1}
\]

\[
 H_{4,x}=4c_x-6t_x+3s_{x,1}+s_{x,2}.                    \tag{7.2}
\]

These formulas include both linear boundaries; no cyclic correction is
present.

All `16383` nonempty rank-at-most-seven targets avoiding `x` have witnesses
inside `x`-free runs.  Lemma 2.1 makes their lengths at most three.  Hence

\[
 \boxed{3t_x-s_{x,1}\le2931+3a_x.}                      \tag{7.3}
\]

Let `j_x` count `x`-free endpoints whose first rank-at-least-eight crossing
occurs inside the free run and overshoots rank eight.  Besides the lower
witnesses, `H_(4,x)` contains all `6435+E_x` rank-eight delivery intervals
avoiding `x` and all `j_x` overshoot intervals.  These selected intervals are
distinct: their OR ranks separate the three classes, and starts separate
members within a delivery or jump class.  Therefore

\[
 \boxed{
 6t_x-3s_{x,1}-s_{x,2}+E_x+j_x
 \le2934+4a_x.}                                          \tag{7.4}
\]

The same statement has an exact multi-coordinate form.  If `X` is any
coordinate set, put `n=16-|X|`, let `H_(q,X)` count intervals of length at
most `q` lying in `X`-free runs, and define `E_X,j_X` analogously.  Then

\[
 H_{3,X}\ge\sum_{u=1}^{\min\{7,n\}}\binom nu,            \tag{7.5}
\]

and, when `n>=8`,

\[
 H_{4,X}\ge\sum_{u=1}^{7}\binom nu+\binom n8+E_X+j_X.   \tag{7.6}
\]

Writing

\[
 T=\sum_xt_x,\quad S_i=\sum_xs_{x,i},\quad
 J_{\rm free}=\sum_xj_x,
\]

and summing gives

\[
 3T-S_1\le46896+3\delta,                                \tag{7.7}
\]

\[
 6T-3S_1-S_2+8F+J_{\rm free}
 \le46944+4\delta.                                      \tag{7.8}
\]

For example, (7.7) is exactly the Hadamard-window inequality

\[
\begin{aligned}
16\cdot16383\le{}&
 \sum_p|\overline{A_p}|+
 \sum_p|\overline{A_p}\cap\overline{A_{p+1}}|\\
&+\sum_p|\overline{A_p}\cap\overline{A_{p+1}}
                         \cap\overline{A_{p+2}}|,
\end{aligned}                                             \tag{7.7a}
\]

where sums use only valid linear windows.

There is also a lower phase-run bound.  Let `rho_x` count `x`-free lost
endpoints whose remaining free-run suffix stays below rank eight.  Then

\[
 \ell_x=j_x+\rho_x,
 \qquad \rho_x\le3t_x.                                  \tag{7.9}
\]

The second inequality follows from Lemma 2.1: an unresolved suffix has at
most three starting positions in one free run.  A global jump counted by
`j_x` has crossing rank at least nine and therefore omits at most seven
coordinates.  Hence

\[
 \sum_xj_x\le7J.
\]

Together with (4.6),

\[
 \boxed{3T\ge\Delta+8S+J.}                              \tag{7.10}
\]

Combining (7.10) with (6.9), and minimizing at `S=0,J=N`, gives

\[
\begin{array}{c|c}
N&T\text{ lower bound}\\ \hline
0&1565\\
1&1564\\
2&1562\\
3&1561
\end{array}                                               \tag{7.11}
\]

Thus every hypothetical word has

\[
                         \boxed{T\ge1561,}               \tag{7.12}
\]

so some coordinate has at least `98` free runs.  The exact run-start identity

\[
 T=16-|A_0|+\sum_{p=1}^{L-1}|A_{p-1}\setminus A_p|       \tag{7.13}
\]

implies at least `1546` one-to-zero coordinate transitions.  Applying the
same argument after reversal gives at least `1546` zero-to-one transitions.
Therefore

\[
 \boxed{
 \sum_{p=1}^{L-1}|A_{p-1}\mathbin\triangle A_p|
 \ge3092.}                                                \tag{7.14}
\]

There is also a pointwise pair distribution law.  From (6.3), (7.9),
`j_x<=J`, and `E_X<=F`,

\[
 3(t_x+t_y)\ge431-E_X-2J\ge428+N-2J.                    \tag{7.15}
\]

Thus every coordinate pair has at least `143` free runs in total on the
faces `N=0,1`, and at least `142` on the faces `N=2,3`.

## 8. Feasible scalar models at waste three

### 8.1 Tight one-coordinate atom model

Take one abstract primary row for every rank-eight target `T`.  For three
distinct coordinates `1,2,3`, choose distinct targets `T_j` containing `j`,
replace the row letter `T_j` by `T_j\{j}`, and append the singleton rows
`{1},{2},{3}` as three nondeliveries.  Then

\[
 N=3,\quad F=G=0,
\]

and every coordinate has exactly `6438` free letters: for `j=1,2,3`, the
deleted owner incidence replaces the one free incidence lost at `{j}`; every
other coordinate is omitted by all three appended singletons.  Thus

\[
 a_x=0,\quad E_x=0,\quad\ell_x=3,
 \quad \sum_p|A_p|=102960.                               \tag{8.1}
\]

This is an exact integer point of the one-coordinate incidence relaxation,
but not a chronology and not a lower-target cover.  It proves that the
uncorrected `48/15` argument fails precisely because primary target cells may
omit target coordinates.

### 8.2 Pair-and-run numerical model

There is also an integer point surviving the aggregate pair and run cuts.
Take the inventory face

\[
 N=3,\qquad F=G=0,
\]

with the following independent-column rank histogram:

\[
 672\text{ rank-one primary starts},\qquad
 12198\text{ immediate rank-eight primaries},\qquad
 3\text{ rank-sixteen jumps}.                            \tag{8.2}
\]

To balance the first group, choose any `336` complementary pairs of
rank-eight targets.  Their `672`-by-`16` incidence graph is biregular of
degrees `8` and `336`.  The constant fractional orientation `1/8` is
integralizable by bipartite total unimodularity, assigning exactly `42`
chosen targets to each coordinate contained in it.  Use that coordinate as
the singleton start.

This gives, for every coordinate,

\[
 \Delta=4680,\quad \delta=4656,\quad
 a_x=291,\quad c_x=6729,\quad E_x=0,\quad\ell_x=294.      \tag{8.3}
\]

Set in the scalar run system

\[
 t_x=98,\quad s_{x,1}=s_{x,2}=j_x=0,\quad\rho_x=294.     \tag{8.4}
\]

Then (4.2), (4.6), (6.8), and the numerical rows
(7.3)--(7.10) all hold; in
particular `11*4680+60*3=51660>=51636`.  The pair moment of the rank
histogram is `412104`, leaving exactly `24` units above (6.5).  This is an
integer point of the displayed coupled numerical system.

It is not a physical word or a common ordered trace.  The `672`
singleton-to-rank-eight promotions are independent columns, and the run
variables in (8.4) are assigned numerically rather than obtained from one
ordering of the letters.

### 8.3 The full subset hierarchy is separately static-feasible

The complete hierarchy (6.12) also has a symmetric rational static point.
It uses the same rank masses as Section 8.2, but it is a separate relaxation:
no common ordering is asserted.

Put

\[
 \theta={672\over12870}={112\over2145}.
\]

For every rank-eight target `T`, assign primary-start mass `1-theta` to the
letter `T`, and mass `theta/8` to each singleton letter `{x}`, `x in T`.
The primary mass of every target is one.  Since every coordinate belongs to
`6435` middle targets, each singleton label receives total mass

\[
 6435{\theta\over8}=42.
\]

Append three full-set nondelivery jumps.  The total rank masses are therefore

\[
 672\text{ at rank one},\qquad
 12198\text{ at rank eight},\qquad
 3\text{ at rank sixteen}.                               \tag{8.5}
\]

This point has exactly the coordinate data (8.3).  For a coordinate set `X`
of size `h>=1`, its free-letter mass is

\[
 c_h=42(16-h)+{2033\over2145}\binom{16-h}{8},             \tag{8.6}
\]

where the binomial term is zero when `h>8`.  The first values are

\[
 c_1=6729,qquad c_2={17171\over5}=3434.2,qquad
 c_3={8829\over5}=1765.8.
\]

For `h=4,...,15`, direct substitution in (8.6), using the exact already
proved values of `nu(16-h)`, also gives

\[
 c_h\ge\nu(16-h).                                        \tag{8.7}
\]

Here the comparison vector for `h=1,...,15` is

\[
 (\nu(15),\nu(14),\ldots,\nu(1))
 =(6438,3434,1719,926,465,254,128,72,37,21,12,7,4,2,1),
\]

so (8.7) is a finite exact arithmetic check, not an asymptotic estimate.

Thus every pointwise free-set cut (3.2), and hence every zeta moment
(6.12), holds.  Pointwise pair loss is `c_2-3003=431.2`, while
`ell_x+ell_y=588`, so (6.2)--(6.4) also hold.

The atom ledger is balanced: the singleton branches delete total mass
`672*7=4704`, namely `294` in each coordinate, and the full-set jumps delete
none.

This is a rational point, not an integral word.  That is enough to exclude a
rational Hall/Farkas certificate made only from the pointwise free-set
cardinality rows and static target containments.  It does **not** instantiate
the common-order relations (7.9)--(7.15), because no ordering or actual
first-middle intervals are assigned.  Its failure is that the fractional
singleton-to-rank-eight primary columns are not one common family of
delivery windows.

## 9. Exact boundary

The following statements are unconditional for every universal K16 word of
length `12873`:

* `G=0` and `N+F=3` in both directions;
* the corrected hypersimplex ledger (4.2)--(4.6);
* the singleton inequalities (5.2)--(5.3);
* the pointwise and aggregate pair cuts (6.3), (6.8), and the zeta hierarchy
  (6.12);
* the phase-run inequalities (7.3)--(7.15).

They do not prove `N+F>=4`.  Section 8.2 proves feasibility of the inventory,
atom, aggregate pair-Farkas and numerical phase-run relaxation.  Section 8.3
separately proves feasibility of every pointwise free-set cardinality cut
and static target containment.  Neither decides the intersection of the
full pointwise hierarchy with a common ordered run system, even before the
simultaneous physical equations

\[
 U(p,q)=A_p\cup U(p+1,q)=U(p,q-1)\cup A_q               \tag{9.1}
\]

are imposed.  A stronger coupled higher-order-coordinate/run Farkas
inequality could still succeed; failing that, one must use an
overlap/target-diversity invariant coupling adjacent columns.

The independently proved three-hole core staircase of handoff item 1998a is
the natural physical host for that next step.  It already supplies ordered
middle intervals, the exact endpoint-hole area ledger, and common envelopes
`K_j`.  The inequalities here add pairwise zeta load, phase-run distribution
and Hamming-variation requirements, but do not contradict that staircase.
The precise surviving lane is therefore to combine (6.2)--(7.15) with
`A_j subseteq K_j` and `union_(j in I_i) K_j=T_i`; no source-relative basin
or flat-carrier assumption is justified.

The exact bracket remains

\[
                         12873\le\nu(16)\le12874.
\]
