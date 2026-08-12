# Common-backbone conservation for multiscale queue packings

## Status

This note does **not** prove the constant-one conjecture.  It proves a sharp
no-go theorem for a tempting way of extending the quantitative queue-rounding
theorem: cover a shallow band first, and then append separately initialized
queue families for successive outer annuli.

The obstruction is independent of ABKV, codegrees, dummy completion, and the
choice of rank-dependent quotas.  Through every depth `d=o(sqrt(m))`, a
near-lossless certified queue ledger forces almost every middle-center
occurrence to be active all the way through depth `d`.  Hence all those ranks
must use one common backbone of `(1+o(1))W` center occurrences.  A new annular
queue family cannot repair the next shallow row at `o(W)` cost.

Throughout,

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

The common-backbone statement concerns the certified masks of
monotone-radius queue atoms.  The fresh-stage obstruction below is stronger:
it applies to **all** contiguous-OR words, including incidental OR values and
cross-boundary witnesses.

## 1. Exact center ledger

Consider an arbitrary multiset of monotone-radius queue atoms.  Atom `a` has
`H_a` middle centers and a nonincreasing radius profile

\[
 r_{a,0}\ge r_{a,1}\ge\cdots\ge r_{a,H_a-1}\ge0.
\]

Put

\[
 C=\sum_a H_a,
 \qquad
 A_q=\#\{(a,t):r_{a,t}\ge q\}.
\tag{1}
\]

Every center occurrence certifies one middle mask.  Every center occurrence
of radius at least `q` certifies exactly one lower and exactly one upper mask
at signed depth `q`.  Consequently the certified occurrence counts are

\[
 T_0=C,
 \qquad
 T_q^-=T_q^+=A_q.
\tag{2}
\]

For each row let `D` and `M` denote certified duplicate excess and missing
count.  The exact identity

\[
 M=N+D-T
\tag{3}
\]

therefore gives

\[
 C=W+D_0-M_0,
\tag{4}
\]

and

\[
 A_q=N_q+D_q^--M_q^-=N_q+D_q^+-M_q^+.
\tag{5}
\]

No randomness or asymptotic argument has entered.

## 2. Shallow multiscale collapse

### Theorem 1 (common-backbone conservation)

Let `d=d(m)=o(sqrt(m))`.  Suppose

\[
 D_0+M_0+
 \sum_{q=1}^d(D_q^-+M_q^-+D_q^++M_q^+)=o(W).
\tag{6}
\]

Then

\[
 \boxed{C=(1+o(1))W,\qquad A_d=(1+o(1))W,\qquad C-A_d=o(W).}
\tag{7}
\]

In particular, all but `o(W)` center occurrences have radius at least `d`.
The same `C-o(W)=(1+o(1))W` physical center occurrences certify every signed row at
every depth `q<=d`.

#### Proof

The binomial ratio is

\[
 \frac{N_d}{W}
 =\prod_{i=0}^{d-1}\frac{m-i}{m+i+1}
 =\exp\!\left(-\frac{d^2}{m}
       +O\!\left(\frac d m+\frac{d^3}{m^2}\right)\right)
 =1-o(1).
\tag{8}
\]

Equations (4), (5), and (6) give

\[
 C=(1+o(1))W,\qquad A_d=N_d+o(W)=(1+o(1))W.
\]

Since every depth-`d` active occurrence is a middle-center occurrence,
`A_d<=C`.  Subtracting the two estimates proves `C-A_d=o(W)`.  Radius
nestedness then implies that every one of these `A_d` occurrences is active
at every shallower depth.  QED

The theorem is stronger than an average quota statement.  In this shallow
regime, rank-dependent occupancies and mixtures of different maximum radii
collapse: asymptotically all of the center mass lies in the cohort reaching
the *outermost* requested depth.

### Quantitative form

Without assuming `d=o(sqrt(m))`, (4)--(5) give the exact estimate

\[
 C-A_d
 =W-N_d+(D_0-M_0)-(D_d^--M_d^-).
\tag{9}
\]

Thus, if the four displayed defect terms are `o(W)` and
`d=c\sqrt m+o(\sqrt m)` for fixed `c>=0`, then

\[
 A_d=(e^{-c^2}+o(1))W.
\tag{10}
\]

So even at a fixed Gaussian depth, a positive fraction of all middle-center
occurrences must belong to one depth-`d` backbone.  A separately appended
family can have `o(W)` center cost only after `d/sqrt(m)->infinity`, when
`N_d=o(W)`.

## 3. No additive annular iteration

### Lemma 2 (universal endpoint capacity)

Let `A` be any OR word and append a word `B` of length `L`.  Fix a cardinality
`r`.  Then `A||B` represents at most `L` rank-`r` masks that were not already
represented by `A`.

#### Proof

Every newly represented mask has a witnessing interval whose right endpoint
lies in `B`; an interval ending in `A` was already available before the
append.  Fix one right endpoint `j` in `B`.  As the left endpoint moves from
`j` toward the beginning of the concatenated word, the interval ORs form an
inclusion chain.  Two distinct members of an inclusion chain cannot have the
same cardinality.  Hence endpoint `j` contributes at most one new rank-`r`
mask.  Summing over the `L` new right endpoints proves the lemma.  QED

The lemma already allows intervals crossing the old/new seam.  It is
therefore not an artefact of insisting that witnesses stay inside individual
queue atoms.

### Lemma 3 (the validated shallow word has a cardinality gap)

Concatenate standard monotone-radius queue words whose maximum radii are at
most `h`, and then append literal repair masks from the ranks
`m-h,...,m+h`.  Every represented mask has cardinality either at most `2h`
or at least `m-h`.  In particular, if `m>3h+1`, the entire rank `m-h-1` is
absent.

#### Proof

In a standard atom word

\[
 R,\{z_{-d}\},\ldots,\{z_{d-1}\},L_0,\ldots,L_{H-1},
\]

with `d<=h`, the entries `R` and `L_t` all have cardinality at least `m-h`.
Every literal repair entry also has cardinality at least `m-h`.  Call these
entries large.  The only other entries are singletons, and every maximal
consecutive singleton run has length at most `2d<=2h`; large entries separate
such runs both inside atoms and across atom boundaries.

An interval containing a large entry has OR-cardinality at least `m-h`.  An
interval containing no large entry lies inside one singleton run and has
OR-cardinality at most `2h`.  This proves the gap.  QED

### Corollary 4 (the quantitative theorem cannot be extended by appending)

Let `A_h` be the literal word produced by the validated quantitative
queue-rounding theorem, including its literal band repairs.  If `B` is any
word such that `A_h||B` covers rank `m-h-1`, then

\[
 \boxed{|B|\ge N_{h+1}.}
\tag{11a}
\]

For its proved parameter `h=o(sqrt(m))`, this is

\[
 |B|\ge(1-o(1))W.
\tag{11b}
\]

Thus an appended continuation of that concrete `W+o(W)` word has total
length at least `2W-o(W)`, even if it is not a queue word and even if it uses
all cross-boundary intervals.

#### Proof

The theorem's parameter satisfies `m>3h+1`.  Lemma 3 says that `A_h` misses
all `N_(h+1)` masks of rank `m-h-1`.  Lemma 2 says that appending `|B|`
entries can create at most `|B|` of them.  Finally `N_(h+1)/W=1-o(1)` because
`h=o(sqrt(m))`.  QED

### Theorem 5 (fresh-stage lower bound)

Let a previously emitted arbitrary OR word miss `R_d` masks in one of the
ranks `m-d` or `m+d`.  If an appended word repairs all but `o(W)` of these
holes, its length is at least

\[
 \boxed{R_d-o(W).}
\tag{11}
\]

In particular, if the old word has no occurrence in that row and
`d=o(sqrt(m))`, the appended word length is `N_d-o(W)=W-o(W)`.  If the
previous shallow construction already had length `W+o(W)`, this two-stage
architecture has length at least

\[
 \boxed{2W-o(W).}
\tag{12}
\]

#### Proof

Apply Lemma 2 in the indicated rank.  The appendage must create at least
`R_d-o(W)` formerly absent masks, so it needs at least that many new right
endpoints.  If `R_d=N_d`, equation (8) gives (12).  QED

Thus an `o(W)` appendage can repair only `o(W)` actual holes in any fixed
rank.  This remains true if the appendage is not a queue word and if all
cross-seam interval ORs are exploited.

### Corollary 6 (one dominant stage)

Suppose several separately emitted queue stages together have total center
count `W+o(W)` and satisfy (6).  Then one common collection consisting of
`C-o(W)=(1+o(1))W` of those physical center occurrences reaches depth `d`; all other
center occurrences together number only `o(W)`.

Consequently, splitting the depths `1,...,d` among disjoint queue stages
cannot yield an asymptotic coefficient one.  The construction must deepen
the already paid-for middle backbone **in place**.

#### Proof

Apply Theorem 1 to the union of the stages.  The set of depth-`d` active
centers has size `(1+o(1))W` and differs from the full center multiset by only
`o(W)` occurrences; by radius nestedness, it is simultaneously active
at every shallower depth.  Equation (7) leaves only `o(W)` other centers.
QED

## 4. The necessary path-length scale

Let `p_d` be the number of atoms containing at least one radius-at-least-`d`
center.  Because every atom's radius profile is nonincreasing, its high-radius
centers form one initial segment.  The usual literal initialization for such
an atom costs at least `2d+1` entries in addition to its one-per-center
updates.  Hence

\[
 L_{\rm queue}\ge C+(2d+1)p_d.
\tag{13}
\]

### Corollary 7 (long common paths are necessary)

Under Theorem 1, a separately initialized queue construction of length
`W+o(W)` must satisfy

\[
 \boxed{p_d=o(W/d)}
\tag{14}
\]

and the average number of radius-at-least-`d` centers per high atom is

\[
 \boxed{\frac{A_d}{p_d}=\omega(d).}
\tag{15}
\]

#### Proof

Equations (7) and (13) force `(2d+1)p_d=o(W)`, proving (14).  Since
`A_d=(1+o(1))W`, division gives (15).  QED

At the inner-reservoir threshold

\[
 d=(1+o(1))\sqrt{m\log\log m},
\]

this says that almost all middle centers must already be organized into
common rotor paths whose average high-radius run length is
`omega(sqrt(m log log m))`.  A hierarchy of short independent annular paths
cannot be joined afterwards without repaying the reset ledger.

## 5. Exact positive transfer once common ownership is supplied

The conservation theorem also isolates the only missing input.  Suppose one
has `p` genuine queue paths, with `H_a` centers and maximum radius `d_a<=d`,
whose certified masks have total duplicate-plus-missing count `Q` in the
band.  Emitting the standard literal word for every path and then appending
the missing masks gives

\[
 L\le \sum_a H_a+\sum_a(2d_a+1)+Q.
\tag{16}
\]

In the uniform case `H_a=H`, `d_a<=d`, and `pH<=W+o(W)`,

\[
 \boxed{L\le W+\frac{2d+1}{H}W+Q+o(W).}
\tag{17}
\]

Thus `H/d->infinity` and `Q=o(W)` are sufficient.  No additional
factorability or pin-survival theorem is required; the queue words are
literal OR factors.

The validated quantitative queue theorem proves (17) only for

\[
 d=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).
\]

Theorem 1 shows why appending another queue packing cannot extend that depth.
The next theorem must keep essentially the same `W` center occurrences and
choose deeper, mutually compatible flag ownership on them.  Equivalently, it
must be a common-ownership/deepening theorem, not an annular covering theorem.

## 6. Small exact sanity checks

The endpoint bound is sharp already on three coordinates.  Take

\[
 A=(001),\qquad B=(010,100).
\]

The prefix `A` represents one singleton.  After appending the two entries of
`B`, exactly the two new singleton masks `010` and `100` appear.  Thus the
number of newly represented masks in rank one equals the number of new right
endpoints.

For the cardinality gap, take `m=5`, `h=d=1`, and `H=2`, with queue positions
`z_{-1},...,z_8`.  One standard atom is

\[
 \{z_5,z_6,z_7,z_8\},\{z_{-1}\},\{z_0\},
 \{z_1,z_2,z_3,z_4\},\{z_2,z_3,z_4,z_5\}.
\]

Its exhaustive interval-OR cardinalities are

\[
 1,2,4,5,6,7,10.
\]

In particular it represents none of the `binom(10,3)=120` rank-three masks,
exactly as Lemma 3 predicts.

The standard-library audit is
`scratch/audit_queue_common_backbone_small.py`.  It was run on RunPod and
reported

```
PASS
endpoint equality: new rank-1 masks = 2 append length = 2
m=5,h=1,H=2 queue word length = 5
represented cardinalities = [1, 2, 4, 5, 6, 7, 10]
rank 3 represented = 0 of 120
```

## Verdict

For every `d=o(sqrt(m))`, near-lossless multidepth queue coverage has a
single-backbone law:

\[
 \boxed{\text{All but }o(W)\text{ of the }(1+o(1))W
 \text{ center occurrences must reach depth }d.}
\]

Therefore neither rank-dependent occupancy mixtures nor iterative disjoint
annuli can bridge the current polylogarithmic queue theorem toward the outer
reservoir while retaining leading constant one.  Such methods pay a fresh
`W-o(W)` as soon as the next uncontrolled row has `Theta(W)` holes.

The only viable queue continuation is in-place deepening of the existing
middle backbone, with paths of average high-radius length `omega(d)` and a
simultaneous ownership transversal whose total defect is `o(W)`.
