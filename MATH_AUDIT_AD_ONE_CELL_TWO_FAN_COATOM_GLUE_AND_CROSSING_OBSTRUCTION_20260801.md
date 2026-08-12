# Exact two-fan coatom glue, and the crossing-pin obstruction to the proposed one-credit macro

Date: 2026-08-01  
Lane: AD, literal compiler/U5 transport  
Status: exact positive fan and derivative carving; exact negative verdict for
the proposed assignment of the `d-1` destroyed crossing cells to a packet
new-chain.  The obstruction occurs before global Hall or common-`Q`.

## 0. Verdict

The two endpoint transporters can indeed be glued around one inserted source
position `*`.  The resulting word has all of the following literal features.

* The cells `L_2,...,L_d` and `R_2,...,R_d` carry the two old coatom chains.
* Every source letter is nonempty.
* Every depth-`d` owner window crossing the glue has one common rank-`r`
  value `U`; inserting `*` adds exactly one more copy of `U`.  Thus the local
  carrier operation is an exact owner stutter and is compatible with `D^d`.
* The singleton `L_1=R_1={*}` can carry any prescribed nonempty subset of
  the common active base.

However, the proposed one-credit assignment is impossible for this literal
glue.  Fan exactness forces every internal filler coordinate to occur at two
complementary source positions, while the two extreme fillers and active
roles are forced on the nearest appropriate shores.  Every one of the
`d-1` pre-insertion crossing cells therefore contains **all** filler
coordinates and both active roles.  It consequently contains neither packet new-chain target.  In the
proved endpoint-transporter word all common-base coordinates occur as well,
so the `d-1` crossing cells are not merely unsuitable: they are all the same
rank-`r` mask `U` and have no edge to the strict-lower target shore.

The remaining singleton is not a common-`q1` ear.  In a natural cube
pairing its value lies in a common base of rank at most `r-d-1`; in the
same-packet prefix/suffix glue below it lies in `G`, of rank `r-d-2`.
Neither can have rank `r-1`.

Thus the count

```text
d-1 destroyed N pins + 2d-1 fan cells - 2(d-1) O pins = one credit
```

is a correct scalar cell count but is not a literal incidence statement.
The minimal missing operation is a basis-changing collar in which the two
fan chains do not force complementary copies of every filler, or an exterior
strict-lower crossing bank not obtained by deleting this star.

## 1. The two chains and the star-hidden cells

Fix `d>=2`.  Let

\[
 F=\{f_1,\ldots,f_d\},
\]

and let `G,{a},{b},F` be pairwise disjoint.  The two old packet chains are

\[
 O_h^L=G\cup\{a,f_1,\ldots,f_h\},\qquad
 O_h^R=G\cup\{b,f_{d-h+1},\ldots,f_d\},
 \quad 1\le h\le d-1.                                      \tag{1.1}
\]

Put the inserted source at position zero.  Write

\[
 L_{h+1}=[-h,0],\qquad R_{h+1}=[0,h],                       \tag{1.2}
\]

and let the old length-`d` cell destroyed at split `i` be

\[
 I_i=\{-i,\ldots,-1\}\cup\{1,\ldots,d-i\},
 \qquad 1\le i\le d-1.                                    \tag{1.3}
\]

After deleting position zero, (1.3) is one ordinary contiguous interval.
Its incidence code is

\[
 -t\in I_i\iff i\ge t,\qquad
 +t\in I_i\iff i\le d-t.                                  \tag{1.4}
\]

This is the exact two-threshold code recorded in handoff item `2368ROOT`.

## 2. All four natural twisted-cube cancellation pairings fail already at `d=2`

The exact compatibility test is Theorem 2.1 of
`MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md`.  Apply it first
to the four cancellation pairings in (3.5) of the twisted-cube theorem.
Each pairing has the following common form.  For distinct active labels
`x,y`, a fixed base `H`, and one nested flag

\[
 \varnothing=J_1\subseteq J_2\subseteq\cdots\subseteq J_{d-1},
\]

the two chains are

\[
       L_{h+1}=H\cup\{x\}\cup J_h,\qquad
       R_{h+1}=H\cup\{y\}\cup J_h.                          \tag{2.1}
\]

Their common singleton `Z` is necessarily contained in `H`: `x` is absent
from every right target and `y` from every left target.  The star-hidden
identity therefore forces, for every `1<=i<=d-1`,

\[
                 \boxed{\{x,y\}\subseteq C_i.}              \tag{2.2}
\]

Indeed `x in L_(i+1)` and `y in R_(d-i+1)`, and neither belongs to `Z`, so
equation (2.2) of the authoritative star theorem applies to both.

Every target in either chain (2.1), in either phase, contains exactly one
of `x,y`.  Hence no crossing cell equals any target in the required
new-chain bank.  In fact every twisted-cube lower-chain target
`E_(ijk)(R)` contains exactly one of `a_0,a_1`, so a crossing cell from any
of these four pairings has no edge to the **entire** twisted-cube chain
bank, not merely to its paired row.  The four literal substitutions are

\[
\begin{array}{c|c|c|c}
\text{cube pairing}&x,y&H&J_h\\ \hline
0P\leftrightarrow1P&a_0,a_1&K\infty b_0c_0&A_h\\
0S\leftrightarrow2P&a_0,a_1&K\infty b_1c_0&B_h\\
1S\leftrightarrow3P&a_0,a_1&K\infty b_0c_1&B_h\\
2S\leftrightarrow3S&a_0,a_1&K\infty b_1c_1&A_h.
\end{array}                                                  \tag{2.3}
\]

Thus every one of the four natural coefficientwise cancellation pairings
has zero crossing-to-new-chain incidence.  The smallest instance is
`d=2`: there is one crossing cell, it contains both `a_0,a_1`, and each of
the two candidate chain values contains exactly one.  This is a one-target,
zero-neighbour Hall witness.  No `d=3` or higher exceptional pairing exists.

The argument allows every interval-zero programming choice on star
coordinates from the authoritative theorem.  It fails because `a_0,a_1`
are outside the common star base, so that freedom cannot affect (2.2).

## 3. A same-packet prefix/suffix glue forces the full filler bank

### Theorem 3.1 (two-sided threshold obstruction)

Let `A` be any set-valued source word satisfying

\[
 A(L_{h+1})=O_h^L,\qquad A(R_{h+1})=O_h^R
 \quad(1\le h\le d-1),                                    \tag{3.1}
\]

where `A(J)` denotes the union of the source letters on `J`.  Then

\[
 \boxed{\{a,b\}\cup F\subseteq A(I_i)
       \quad(1\le i\le d-1).}                              \tag{3.2}
\]

Moreover `A_0 subseteq G`.

#### Proof

Intersecting all left and right labels in (3.1) gives

\[
 A_0\subseteq
 (G\cup\{a,f_1\})\cap(G\cup\{b,f_d\})=G.                 \tag{3.3}
\]

The coordinate `a` is present in `L_2` but absent from `A_0`, so it occurs
at `-1`; similarly `b` occurs at `+1`.  Both positions belong to every
`I_i`.

For `2<=t<=d-1`, the coordinate `f_t` is absent from `L_t` and present in
`L_(t+1)`, so it must occur at source position `-t`.  On the other shore it
is absent through `R_(d+1-t)` and present in `R_(d+2-t)`, so it must also
occur at `+(d+1-t)`.  By (1.4), the first copy lies in `I_i` when `i>=t`,
and the second lies in `I_i` when `i<=t-1`.  These cases partition all
`i=1,...,d-1`.  The endpoint filler `f_1` is forced at `-1` and hence lies
in every `I_i`; symmetrically `f_d` is forced at `+1`.  Thus every `I_i`
contains every filler, proving (3.2).
\(\square\)

The packet new chains are

\[
 N_h^L=G\cup\{b,f_1,\ldots,f_h\},\qquad
 N_h^R=G\cup\{a,f_{d-h+1},\ldots,f_d\}.                    \tag{3.4}
\]

Every `N_h^L` omits `a`, and every `N_h^R` omits `b`.  Therefore (3.2)
immediately gives

\[
 A(I_i)\notin\{N_h^L,N_h^R:1\le h\le d-1\}.               \tag{3.5}
\]

for every crossing cell.  This conclusion is independent of how common
base coordinates are distributed and independent of the common-`Q` choice.

## 4. Literal positive glue and exact `D^d` replay

The proved endpoint transporters give the following particularly transparent
word.  Choose any nonempty `S subseteq G` and put

\[
\begin{array}{rclcrcl}
 A_0&=&S,&&&&\\
 A_{-1}&=&G\cup\{a,f_1\},
 &\quad&A_{+1}&=&G\cup\{b,f_d\},\\
 A_{-t}&=&\{f_t\},
 &&A_{+t}&=&\{f_{d+1-t}\}\quad(2\le t\le d-1),\\
 A_{-d}&=&\{a,b,f_d\},
 &&A_{+d}&=&\{a,b,f_1\}.
\end{array}                                                  \tag{4.1}
\]

The one-sided continuations are the maximal-erosion tails from the two
endpoint-transporter theorem.  Direct union gives (3.1).  Put

\[
                         U=G\cup\{a,b\}\cup F.              \tag{4.2}
\]

Before inserting zero, every length-`d+1` window crossing the cut has `i`
left sources and `d+1-i` right sources for some `1<=i<=d`; its union is
`U`.  After inserting zero, the corresponding windows have `i` left
sources, the star, and `d-i` right sources for `0<=i<=d`; their union is
again `U`.  All one-sided windows are the endpoint-transporter windows.
Consequently

\[
 D^dA^+=\operatorname{stutter}_U(D^dA^-),                   \tag{4.3}
\]

with exactly one additional copy of `U`.  In the coatom parameters

\[
 |G|=r-d-2,\qquad |U|=r.                                   \tag{4.4}
\]

The same calculation with length `d` rather than `d+1` gives

\[
                         A^-(I_i)=U                           \tag{4.5}
\]

for every `i`.  Hence the crossing bank has one repeated middle value and
zero strict-lower incidences.

This proves that the fan and carrier parts of the proposal are compatible.
The failure is specifically the attempted use of the destroyed cells as
distinct lower pins.

## 5. Exact common-`Q` and open-ear scope

The word (4.1) is nonzero and literally realizes all `2(d-1)` fan labels.
It therefore supplies a feasible common-`Q` witness for those pins; by the
exact maximal common-`Q` theorem, their positive-cover and nonzero tests
pass.  The singleton can simultaneously realize the target `S`.

Conversely, (3.3) is necessary for every realization of the fan labels.
Thus the exact local target menu of the singleton is

\[
                 \{S:\varnothing\ne S\subseteq G\}.         \tag{5.1}
\]

In particular it has no rank-`(r-1)` member, since

\[
                         |S|\le r-d-2<r-1.                   \tag{5.2}
\]

The fresh-`q1` endpoint face does not alter this conclusion.  Its native
length-`d` prefix becomes a length-`d+1` hull after the star is inserted and
leaves the short-cell band.  The remaining `L_d` or `R_d` fan omits the last
endpoint filler and is one of the deep chain cells, not the fresh `q1`
cell.

Therefore a prescribed `q1` task and the singleton form a one-row Hall cut
with demand one and incidence zero.  Likewise the desired `d-1` new-chain
crossing pins have incidence zero to the crossing bank.  These are literal
cuts, not merely failures of a chosen matching.

## 6. Consequence for the one-credit ledger

Theorem 4.1 of the Pascal-stutter note correctly counts `2d-1` new fan cells,
`d-1` destroyed cells, and net band growth `d`.  What fails is the extra
identification of those destroyed cells with packet new-chain targets.
Accordingly the claimed local augmenting surplus `alpha=ell+1` does not
follow from the two endpoint transporters.

A positive one-credit macro must change at least one of the following.

1. Use a basis-changing collar whose old crossing values are strict lower
   targets rather than `U`.
2. Do not place the complementary prefix and suffix occurrences of every
   filler on opposite sides of the same inserted star.
3. Supply the typed open ear from an exterior cell whose cap is not bounded
   by the intersection `G` of all fan targets.

This is the exact residual physical gate.  No obstruction is asserted for a
different, non-complementary collar or for an exterior source position.

## 7. Independent symbolic replay

The dependency-free audit checks (2.1), (3.1), (4.3), (4.5), the ranks, and the
absence of every new-chain crossing edge for `2<=d<=32`:

```text
scratch/audit_ad_one_cell_two_fan_coatom_glue_20260801.py
```

It reports

```text
PASS_TWO_FAN_GLUE_AND_LITERAL_CROSSING_OBSTRUCTION
payload_sha256=1400d4bca88dac45822762d5c18c8f2da773d01e5c5d8cbe3c2c764ec52b6762
```
