# The asymmetric `K=16` nine-orbit seam catalogue and one-cut no-go

Date: 2026-07-29  
Lane: AD  
Status: exact finite provider theorem, exact cut/seam ledger, and a
solver-free one-cut obstruction proved.  No globally compatible repair or
literal word is claimed.

## 0. Verdict

For the frozen asymmetric factor

```text
scratch/k16_asymmetric_two_rail_factor_20260729.json
SHA-256 4f5368d063bcfddfe5c2be6d7f68d5ebc38327ee3c4f40d6b00d9d05c1ace139
```

the 123 fixed-window holes are exactly nine `C_15` orbits:

\[
\begin{array}{c|c|c}
\text{kind}&\text{orbit representatives}&\text{orbit sizes}\\ \hline
\text{lower }q=2&33337,33609,34069&15,15,15\\
\text{upper }q=3&36343,36599,39791,39911,40623,46811
 &15,15,15,15,15,3.
\end{array}                                             \tag{0.1}
\]

Thus the repair target is nine quotient row blocks.  For an equivariant
packet model they are nine scalar support rows.  For an arbitrary physical
splice they are nine circulant/vector row blocks, containing the original
123 literal inequalities; symmetry does not permit those phase coordinates
to be discarded.

The exact fixed-depth seam widths are smaller than six:

* every lower-`q2` target has an exact positive-residence-compatible local
  one-seam provider of width `3`;
* every upper-`q3` target, including all three members of the short orbit
  represented by `46811`, has such a provider of width `4`.

The rank bounds make these widths minimal.  Hence widths at most six do
suffice for the **local fixed-depth provider catalogue**; in fact the exact
maximum is four.  This does not prove that compatible providers can be
chosen simultaneously.

There is a sharp obstruction to the most economical splice.  The factor has
28 physical components, all of length at least 16.  Exhausting every
directed Johnson seam between two distinct source components, with both
independent component orientations, gives `1,269,120` local seam records.
No record creates more than three distinct members of the 123-hole family.
A one-cut-per-component splice has only 27 seams, and therefore creates at
most

\[
                            27\cdot3=81<123             \tag{0.2}
\]

missing fixed labels.  Consequently **no one-cut-per-source-component
splice can repair the fixed lower-`q2` and upper-`q3` decks**, even before
charging cut losses, other colours, or global residence.  At least one
source component must be cut more than once, or the carrier itself must be
changed before opening.

The locally separated multi-cut census is stronger.  Even when the two
packets come from the same old component, every honest single-seam
width-three/four ribbon hits at most three holes.  Therefore a fixed-depth
repair of the width-three lower plus width-four upper rows whose retained
packets all have at least four vertices needs at least 41 seams and 42 path
packets, hence at least 42 cuts: fourteen beyond one cut on each old
component.

For the weaker requirement of literal arbitrary-width upper coverage, a
rank-11 target may be supplied at a width larger than four.  The exact
endpoint-minimal theorem gives the complete WLOG range

\[
                       4\le w\le11.                    \tag{0.3}
\]

The concrete one-cut audit finds raw local occurrences at widths four
through seven, but raw width-six and width-seven occurrences are
endpoint-nonminimal.  An independent replay contracts every such occurrence
to a same-target subinterval and proves that the exact endpoint-minimal
support on the frozen cross-component arms is

\[
                              w\in\{4,5\}.              \tag{0.4}
\]

Thus widths at most six do suffice for the concrete one-cut witnesses; in
fact width five is the exact WLOG endpoint.  Moreover any successful one-cut
arbitrary-upper repair must use width-five columns for at least 42 upper
literals: the 27 seams can supply at most 81 distinct width-three/four
holes, and the 45 lower targets already consume 45 of those places.

Consequently:

* fixed upper-`q3` repair: exact width is `4`;
* frozen one-cut arbitrary-upper endpoint-minimal catalogue: exact widths
  are `4,5`, so `<=6` suffices and `<=5` is already complete; and
* unrestricted multi-cut/compiler repair: theorem-level complete detection
  range is widths `4,...,11`.

## 1. Frozen source and exact symmetry reduction

Let `rho` rotate coordinates `0,...,14` and fix coordinate `15`.  The frozen
factor consists of 28 simple physical cycles with lengths

```text
6390,3900,345,330,255,255,255,245,245,245,75,45,45,
16,16,16,16,16,16,16,16,16,16,16,16,16,16,16.
```

It contains all 12,870 rank-eight owners exactly once, every edge is a
Johnson edge, its edge set is `C_15`-invariant, and its minimum positive run
is four.  The frozen independent audit is

```text
scratch/k16_asymmetric_two_rail_factor_20260729.audit.json
SHA-256 d7aa0e13f0e30d0d814187d6892662cc4234d7f81e901c70bac4559fe3377e23
```

It proves that the only fixed-shadow holes are the 45 lower masks in the
three free orbits and the 78 upper masks in the six orbits of (0.1).  It
also proves that those same 78 rank-eleven masks have no upper occurrence
of any cyclic width in the source components.

For an orbit `O`, let `d_O=|O|`.  A full `C_15` orbit of physical ribbon
occurrences mapping to `O` gives every literal target in `O` the uniform
load

\[
                              h_O=15/d_O.               \tag{1.1}
\]

Thus `h_O=1` on the eight free orbits and `h_O=5` on the short upper orbit
represented by `46811`.  As usual, physical multiplicity uses (1.1), while
a Boolean support row still has coefficient one.

## 2. One-cut opening and its seam ribbons

Orient every source component independently.  Write its oriented successor
as `H`.  Cut one edge `t -> Ht`; the resulting path has head `Ht` and tail
`t`.  A directed seam `a=(x,y)` joins the tail `x` of one opened component
to the head `y` of another, with `x` and `y` Johnson adjacent.

For a seam `a=(x,y)`, a width-`w` crossing ribbon with left split `s`,
`1<=s<w`, is the literal sequence

\[
 R(a,w,s)=
 (H^{-(s-1)}x,\ldots,H^{-1}x,x,
   y,Hy,\ldots,H^{w-s-1}y).                            \tag{2.1}
\]

Its lower and upper labels are

\[
 I(a,w,s)=\bigcap R(a,w,s),\qquad
 U(a,w,s)=\bigcup R(a,w,s).                            \tag{2.2}
\]

The exact fixed-hole provider catalogue consists of

\[
\begin{aligned}
 \mathcal P^-&=\{(a,3,s):s=1,2, I(a,3,s)\in\mathcal H^-\},\\
 \mathcal P^+_4&=\{(a,4,s):s=1,2,3, U(a,4,s)\in\mathcal H^+\},
                                                               \tag{2.3}
\end{aligned}
\]

where `mathcal H^-` and `mathcal H^+` are the 45 and 78 literal hole sets.
For arbitrary-width upper repair, replace the second line by

\[
 \mathcal P^+_{\le11}=
 \{(a,w,s):4\le w\le11, 1\le s<w,
                    U(a,w,s)\in\mathcal H^+\}.          \tag{2.4}
\]

The component orientation and chosen cut determine both arms in (2.1);
provider events are not independent of their seam.  In an exact `0-1`
model one may duplicate each directed seam by the two orientation signs of
each incident component, precompute (2.1)--(2.2), and guard its provider
bits by the selected cut-tail/root and seam bit.  Component indegree,
outdegree, and order potentials are exactly those of the arbitrary-component
splice decoder; no unit-voltage or common-orientation condition is added.

### Lemma 2.1 (exact positive seam filter)

For a proposed seam `x -> y`, let `lambda^-_c(x)` be the capped length,
at most four, of the terminal inward positive `c`-run ending at `x`, and let
`lambda^+_c(y)` be the analogous initial inward run beginning at `y`.  The
seam creates no positive run shorter than four exactly when, for every
coordinate `c`,

\[
\begin{array}{ll}
 \lambda^-_c(x)+\lambda^+_c(y)\ge4,&c\in x\cap y,\\
 \lambda^-_c(x)\ge4,&c\in x\setminus y,\\
 \lambda^+_c(y)\ge4,&c\in y\setminus x,
\end{array}                                             \tag{2.5}
\]

with no condition when `c` is absent at both endpoints.  This is the exact
terminal-run case split.  The local audit below applies this filter to every
reported positive-safe provider.  Global residence still requires the
chosen cuts and all seams to be checked together.

## 3. Exact loss/gain identity for arbitrary cut sets

The usual sum of independent cut losses is not exact when several cuts lie
within one width window.  The following union form is exact without any
separation hypothesis.

Fix orientations of the old cycles and a finite cut set `X`, with at least
one cut on every old component.  Removing `X` gives path segments.  Let a
set `Y` of seams order all segments into one global Hamilton path with
partial successor `G`; the final tail maps to `bottom`.

For an old cyclic width-`w` start `x`, let `E_w(x)` be its `w-1` transition
edges and let `lambda_w^-(x),lambda_w^+(x)` be its intersection and union.
Define the exact cut loss

\[
 L_{X,w}^{\pm}(S)=
 \#\{x:\lambda_w^{\pm}(x)=S, E_w(x)\cap X\ne\varnothing\}.
                                                               \tag{3.1}
\]

For an active post-splice start `x`, let `Q_w(x)` be
`x,Gx,...,G^(w-1)x`.  Define the exact seam gain

\[
 G_{Y,w}^{\pm}(S)=
 \#\{x:\lambda^{\pm}(Q_w(x))=S,
       Q_w(x)\text{ uses at least one seam}\}.          \tag{3.2}
\]

### Theorem 3.1 (multi-cut literal ledger)

For every literal target `S` and every valid width `w`, the multiplicity in
the assembled word is

\[
 \boxed{
 m_{w}^{\pm}(S)=\mu_w^{\pm}(S)
                 -L_{X,w}^{\pm}(S)+G_{Y,w}^{\pm}(S).}  \tag{3.3}
\]

#### Proof

Partition post-splice windows according to whether they use a seam.  A
window using no seam is a unique old cyclic window and survives precisely
when none of its transition edges was cut.  These are counted by
`mu-L`.  All remaining post-splice windows use at least one seam and are
counted once by (3.2), even when a short intermediate segment makes a window
cross several seams.  The classes are disjoint and exhaustive.  QED.

Thus every previously covered required target must satisfy

\[
                 \mu_w^{\pm}(S)-L_{X,w}^{\pm}(S)
                      +G_{Y,w}^{\pm}(S)\ge1.            \tag{3.4}
\]

For each of the nine hole orbits, the relevant old multiplicity is zero and
the loss is automatically zero.  Their repair rows are therefore pure gain
rows.

If every retained segment has at least `w` vertices, no width-`w` window can
meet two seams and no old window can meet two cuts.  Then (3.1)--(3.2)
decompose into the familiar sums over individual cuts and seams.  With `D`
cuts and `D-1` seams,

\[
 \sum_Sm_w^{\pm}(S)
   =W-D(w-1)+(D-1)(w-1)=W-w+1.                         \tag{3.5}
\]

For one cut on each frozen source component, every opened path has at least
16 vertices.  Hence the individual-seam formula is exact simultaneously for
all widths through 11.

With multiple cuts and short segments, the one-seam ribbon list alone is
not complete.  The exact finite replacement is to enumerate the length-3
and length-4 words of the global successor `G` for fixed-depth repair, or
all widths through 11 for arbitrary upper repair.  Such a word can contain
several seams, but (3.2) counts it once.

## 4. Why the width catalogue is complete

### Theorem 4.1 (tailored minimal-width theorem)

1. Every lower rank-six occurrence in a simple rank-eight Johnson path
   contains an endpoint-minimal subinterval of width exactly three with the
   same intersection.
2. Every upper rank-eleven occurrence contains an endpoint-minimal
   subinterval of width `w` with

   \[
                              4\le w\le11.              \tag{4.1}
   \]

#### Proof

This is the minimal shadow-witness theorem with `r=8`.  At depth two the
bound is

\[
 B_{8,2}=\binom80+2=3,
\]

while the rank lower bound is `q+1=3`.  At upper depth three,

\[
 B_{8,3}=\binom91+2=11,
\]

and the lower bound is four.  Deleting endpoints from any witness until it
is minimal preserves its target.  QED.

Because no old source component contains any of the nine hole targets at
the relevant widths (and the upper targets occur at no old width at all),
every repaired minimal occurrence uses a seam.  In a one-cut splice it uses
exactly one seam because every opened component is longer than 11.  This
proves completeness of (2.3) for fixed-depth repair and of (2.4) for
arbitrary upper repair.

The upper endpoint 11 is sharp for simple Johnson chronologies and can be
relabelled to any prescribed rank-eleven target.  This sharpness is not a
claim that the frozen carrier itself forces a width above six.  It proves
only that widths through 11 are the correct unconditional WLOG catalogue
unless additional frozen-carrier structure is used.

For the frozen cross-component one-cut arms, the exact local audit supplies
additional structure.  Raw provider occurrences occur only at widths four,
five, six, and seven, but endpoint-minimal occurrences occur only at widths
four and five.  Indeed, every raw width-six or width-seven occurrence keeps
its target after deleting a suitable endpoint, and repeated endpoint
deletion leaves a crossing subinterval of width four or five.  The target
cannot disappear into one old component because every audited upper target
has old multiplicity zero at every width.  Hence the exact complete WLOG
endpoint for the frozen one-cut arms is five.  Raw support through seven is
an occurrence census, not a reason to retain nonminimal columns.

## 5. Nine quotient provider rows

For arbitrary physical seam choices, retain phase.  For a target orbit `O`
of size `d_O`, index its literal targets as `T_(O,j)`, `j in Z_(d_O)`.  A
quotient ribbon type `p` has a fixed label offset `delta_p`; let `z_(p,s)`
mean that its physical phase-`s` occurrence is active.  The exact row block
is the circulant system

\[
 \sum_p\sum_{\substack{s\in\mathbb Z_{15}\\
                  s+\delta_p\equiv j\pmod {d_O}}}
        z_{p,s}\ge1
 \qquad(j\in\mathbb Z_{d_O}).                           \tag{5.1}
\]

There are nine such row templates: eight have 15 phase rows and the short
upper orbit has three, for `8*15+3=123` literal inequalities.  Equation
(5.1) is the exact way to exploit symmetry without assuming an equivariant
physical splice.

If decisions are restricted to full invariant ribbon packets, all fifteen
phase variables in a packet are equal.  Equation (5.1) then collapses to one
scalar support row per target orbit; its physical load coefficient is
`h_O=15/d_O`, equal to five for orbit `46811` and one otherwise.  This
packet restriction is sufficient, not WLOG for the arbitrary physical
component splice.

The same phase-resolved construction applies to every loss and preservation
row in (3.4).  An orbit support count without phase is not an exact literal
post-cut ledger.

## 6. Concrete local provider census

The deterministic audit

```text
scratch/audit_ad_k16_asymmetric_seam_provider_widths_20260729.py
SHA-256 94a58651826124a210a96339bcfbb8ca6f7a78d34acad0190b5aededfc5a2766

scratch/ad_k16_asymmetric_seam_provider_widths_20260729.audit.json
SHA-256 099f4e430e7264b86c09c218f755514b1bdd7477f75be50def30b01b9605c7a2
```

authenticates both frozen source hashes, reconstructs all components and
their rotations, and enumerates only target-induced local seam records.  It
does not solve a compatibility problem.

For every literal in an orbit, rotation gives the same provider census.
The exact positive-safe minimum-width counts per literal are:

| kind | representative | orbit size | minimum width | safe records per literal at that width |
|:--|--:|--:|--:|--:|
| lower | 33337 | 15 | 3 | 90 |
| lower | 33609 | 15 | 3 | 74 |
| lower | 34069 | 15 | 3 | 74 |
| upper | 36343 | 15 | 4 | 210 |
| upper | 36599 | 15 | 4 | 198 |
| upper | 39791 | 15 | 4 | 286 |
| upper | 39911 | 15 | 4 | 282 |
| upper | 40623 | 15 | 4 | 228 |
| upper | 46811 | 3 | 4 | 340 |

Thus there is no marginal provider shortage at widths three and four.  The
unproved issue is simultaneous component-root, seam matching, cut-loss, and
global residence compatibility.

The independent endpoint-minimal replay is

```text
scratch/audit_ad_k16_asymmetric_endpoint_minimal_widths_20260730.py
SHA-256 6deb39221878d902c96285bdf6073e45aaaff3bf913713df38a1b3ec4023e2c8

scratch/ad_k16_asymmetric_endpoint_minimal_widths_20260730.audit.json
SHA-256 0ba51a8a68f010c6e5c974f0624b3aba585823953fea829d13f24d1a5ee415b9
```

For one representative of each upper target orbit, its exact counts are:

| representative | endpoint-minimal `w=4` | endpoint-minimal `w=5` | positive-safe minimal `w=5` |
|--:|--:|--:|--:|
| 36343 | 1066 | 56 | 6 |
| 36599 | 868 | 46 | 12 |
| 39791 | 1220 | 88 | 20 |
| 39911 | 1066 | 82 | 30 |
| 40623 | 1028 | 86 | 18 |
| 46811 | 1310 | 80 | 30 |

Equivariance transports these counts to every literal member of the
corresponding orbit.  The replay audits all widths four through eleven,
finds raw support `4,5,6,7`, and finds endpoint-minimal support exactly
`4,5`, both before and after the local positive-seam filter.

The full fixed-width local seam census is

```text
directed cross-component oriented seam records     1,269,120
records hitting 0 / 1 / 2 / 3 missing labels
                                 1,176,660 / 89,220 / 3,180 / 60
useful records                                          92,460
maximum distinct missing labels on one seam                  3
```

The four histogram entries sum to `1,269,120`.  The maximum is attained by
60 oriented records.  The audit does not impose the positive seam filter in
this maximum calculation, so `3` is an upper bound even before residence
and is safe for the obstruction below.

### Theorem 6.1 (one-cut splice no-go)

No splice obtained by independently orienting the 28 frozen components,
cutting each exactly once, and joining the resulting paths can cover all 45
lower-`q2` and 78 upper-`q3` fixed holes.

#### Proof

Such a splice has exactly 27 seams.  Since each path has at least 16
vertices, a width-three or width-four interval crosses at most one seam.
Every hole has old multiplicity zero, so every repaired occurrence must be
one of the seam gains in (2.3).  The exhaustive local catalogue proves that
one seam supplies at most three distinct holes.  Hence all seams together
supply at most 81 distinct holes, less than 123.  QED.

The proof ignores cut losses, preservation of q1 and other shadows, and
residence, so adding those constraints cannot invalidate it.  It does not
exclude multiple cuts on a source component, an earlier factor rethread, or
repair aimed only at arbitrary upper coverage rather than the fixed upper
`q3` row.

For arbitrary upper coverage, Theorem 4.1 makes the unconditional one-cut
target catalogue lower width three and upper widths four through eleven.
The frozen-arm endpoint-minimal census reduces the latter to widths four and
five.  The same
maximum-three calculation applies to the lower width-three plus upper
width-four labels.  Since all 45 lower holes must be supplied at width three,
at most `81-45=36` upper holes can be supplied at width four.  Therefore at
least 42 of the 78 upper masks must be supplied at width five
in any successful frozen one-cut arbitrary-upper splice.  No such splice is
claimed.

The same audit includes seams between two packets cut from the same source
cycle when the cut edges are distinct, their depth-three collars are
vertex-disjoint, and neither cut removes an edge of the opposite collar.
These conditions make all five width-three/four crossing windows honest.
The expanded census is

```text
directed oriented locally separated segment seams       3,189,780
records hitting 0 / 1 / 2 / 3 missing labels
                                  3,063,690 / 121,950 / 4,080 / 60
maximum distinct missing labels on one seam                   3
```

### Corollary 6.2 (separated multi-cut lower bound)

If every retained packet has at least four vertices, a fixed-depth literal
path repair of the width-three lower and width-four upper rows needs at least
41 seams and therefore at least 42 packets/cuts.  Starting from 28 old
components, it needs at least 14 additional cuts.  A fixed-depth cyclic
rethread needs at least 41 packets and seams.

#### Proof

A width-three or width-four window cannot cross two seams when the
intermediate packet has at least four vertices.  The expanded catalogue
includes every honest different-source or same-source single seam and still
gives at most three holes per seam.  Since `ceil(123/3)=41`, a path needs 41
seams and 42 packets; a cyclic rethread needs 41 of each.  QED.

This corollary does not cover packets shorter than four, where one fixed
window can cross several seams.

## 7. Exact next model and proved boundary

The next exact fixed-depth model must allow multiple cuts.  In the
four-separated packet subclass it may use the segment records and
single-seam ribbons above, together with the 42-packet lower bound.  Without
a packet-length restriction, a complete fallback uses one bit for every
directed physical Johnson adjacency, exactly

\[
                 Wr^2=12870\cdot64=823680              \tag{7.1}
\]

arc bits.  One start bit, one end bit, and ordinary strict order potentials
make the selected arcs one Hamilton path.  A selected source arc is a
retained old edge; every other selected arc is a replacement seam.  The
fixed-depth rows inspect the exact guarded words

\[
 (x,Gx,G^2x),\qquad (x,Gx,G^2x,G^3x),                 \tag{7.2}
\]

so a short packet and a multi-seam window are handled literally.  Arbitrary
upper repair propagates through `G^10x`, giving widths four through eleven.

Equivalently, its construction checklist is:

1. choose a nonempty cut set on every source cycle, or directly choose the
   retained/replacement arcs of the global path;
2. route every resulting path segment exactly once;
3. compute the global successor `G`;
4. install the nine phase-resolved gain blocks (5.1) using exact width-three
   intersections and width-four unions;
5. install (3.4) for every required previously covered target; and
6. audit positive residence on the literal global path.

The one-cut no-go proves that at least one old component must be cut more
than once.  Corollary 6.2 sharpens this to 42 cuts for fixed-depth repair in
the separated packet architecture.  No 42-cut bound is claimed for the
unrestricted arc fallback, because packets shorter than four may create
multi-seam fixed windows.

For arbitrary upper-mask rather than fixed-depth repair, replace step 4's
upper layer by widths `4,...,11` in the unrestricted global-successor model.
For the frozen cross-component one-cut arms, raw occurrences extend through
width seven but endpoint-minimal support is exactly `4,5`; `<=5` is complete
for frozen one-cut detection.  After unrestricted multi-cut rethreading, a
minimal witness can cross several seams, so only the theorem-level endpoint
`11` is proved complete without an additional packet-length or
carrier-structure lemma.

Proved:

* exact nine-orbit compression, including the size-three stabilizer five;
* exact one- and multi-cut literal loss/gain ledgers;
* complete fixed-depth widths three and four;
* exact frozen one-cut endpoint-minimal upper widths four and five;
* complete arbitrary-upper widths four through eleven;
* positive-safe local providers for every literal hole; and
* the `81<123` one-cut obstruction and 42-packet separated lower bound.

Not proved:

* a globally compatible multiple-cut splice;
* preservation of every previously covered mask for any proposed cuts;
* global residence after choosing many seams;
* common-compiler Hall; or
* a literal length-12,873 contiguous-OR word.
