# Near clones of a directed punctured configuration are polynomially sparse

**Status (2026-08-21).**  The uniform fixed-defect bound (0.2) is proved
analytically.  The proposed exact overlap tail

\[
 N_{4r}=1,\qquad N_{4r-1}=2,\qquad N_{4r-2}=4r+1       \tag{0.1}
\]

is exhaustively verified for `r=3,4,5` and by exact containment-path
reconstruction for every `3<=r<=20`.  The candidate configurations are
classified below.  A uniform analytic exhaustion of a finite family of
boundary/cross-paired two-seam templates remains open, so (0.1) is not
claimed as a theorem here.

For every defect `d`, the following uniform explicit bound is proved:

\[
 N_{4r-d}(E)
 \le {4r\choose d}\cdot2^{d+1}(2d+1)!(d+1)!.          \tag{0.2}
\]

Thus
\(N_{4r-d}(E)\le r^d\exp(O(d\log d))\), uniformly in the base
configuration.  This supplies the fixed-defect near-clone estimate needed
at the top of a polymer expansion.  It does not by itself prove the quenched
FIFO regeneration gate: defects growing with `r` and the adaptively thinned
law still require control.

## 1. Normalization and notation

Put

\[
 b=2r+1,
\]

write all indices modulo `b`, and use the identity word on the labels
`0,1,...,b-1`.  Its full cyclic windows are

\[
 L_i=\{i,i+1,\ldots,i+r-2\},\qquad
 M_i=\{i,i+1,\ldots,i+r-1\}.                            \tag{1.1}
\]

The base punctured configuration is

\[
 E=\{L_i,M_i:1\le i\le b-1\},                          \tag{1.2}
\]

with layer tags understood.  Its canonical containment path is

\[
 P=(L_1,M_1,L_2,M_2,\ldots,L_{b-1},M_{b-1}).           \tag{1.3}
\]

For any configuration `F`, define

\[
 \operatorname{def}_E(F)=4r-|E\cap F|,
 \qquad
 N_{4r-d}(E)=|\{F:\operatorname{def}_E(F)=d\}|.        \tag{1.4}
\]

Coordinate relabelling is transitive on directed words, so these numbers do
not depend on `E`.

For `s in Z_b`, define the two dihedral representations of the identity
cyclic order by

\[
 \rho_s=(s,s+1,\ldots,s+b-1),\qquad
 \tau_s=(s,s-1,\ldots,s-b+1).                          \tag{1.5}
\]

Finally put

\[
\begin{aligned}
 u^-&=(0,b-2,b-3,\ldots,2,1,b-1),\\
 u^+&=(b-1,1,2,\ldots,b-3,b-2,0).
\end{aligned}                                          \tag{1.6}
\]

## 2. The intrinsic reconstruction lemma

The following elementary identities drive the argument:

\[
 L_i\subset M_j\quad\Longleftrightarrow\quad
 j\in\{i-1,i\},                                       \tag{2.1}
\]

and

\[
 M_i\cap M_j=\varnothing\quad\Longleftrightarrow\quad
 j-i\in\{r,r+1\}.                                     \tag{2.2}
\]

Consequently, containment on the full two-layer deck is an alternating
cycle, and disjointness on the full middle deck is another cycle, whose
step is `r`.  Deleting `L_0,M_0` gives the containment path (1.3), while
deleting `M_0` gives the intrinsic middle-disjointness path

\[
R=(M_r,M_{2r},M_{r-1},M_{2r-1},\ldots,M_1,M_{r+1}).   \tag{2.3}
\]

Both graphs are defined from the target sets alone; they do not depend on a
displayed word.

The rank of a clean middle window in (2.3) is

\[
 \operatorname{rk}_R(M_j)=
 \begin{cases}
  2(r-j),&1\le j\le r,\\
  4r-2j+1,&r+1\le j\le2r.
 \end{cases}
\]

Thus two clean base middle windows are disjoint exactly when their `R`-ranks
are consecutive.

### Affine seam sublemma

Let `M'_1,...,M'_(2r)` be the middle windows in the canonical start order
of another punctured deck, and write `f(i)=j` whenever the common target
`M'_i` equals `M_j`.  On every oriented common containment block,

\[
                         f(i)=\epsilon i+c,
 \qquad \epsilon\in\{+1,-1\}.                         \tag{2.3a}
\]

If positions `i` and `i+r` are both retained and common, their middle
windows must be disjoint, and hence

\[
                    f(i+r)-f(i)\in\{r,r+1\}\pmod b.    \tag{2.3b}
\]

For a step-`r` test crossing from an affine piece `(epsilon,c)` to
`(epsilon',c')`, the left side of (2.3b) is

\[
\begin{array}{c|c}
(\epsilon,\epsilon')&f(i+r)-f(i)\\ \hline
(+,+)&r+c'-c\\
(-,-)&r+1+c'-c\\
(+,-)&c'-c-r-2i\\
(-,+)&c'-c+r+2i.
\end{array}                                             \tag{2.3c}
\]

Consequently two consecutive admissible tests crossing an
opposite-orientation seam are impossible: their values differ by `2` modulo the odd integer
`b>=7`, whereas the two allowed values differ by `1`.  Across a
same-orientation seam, (2.3b) forces respectively

\[
 c'-c\in\{0,1\}\quad\text{or}\quad c'-c\in\{-1,0\}.    \tag{2.3d}
\]

These are exactly the constants which continue a base segment across one
of its two original neighbouring targets.  This proves the affine seam
sublemma.

Write the vertices of `P` as `p_0,...,p_(4r-1)`, and, for an adjacent hole
`p_h,p_(h+1)`, put

\[
 A_h=(p_0,\ldots,p_{h-1}),\qquad
 B_h=(p_{h+2},\ldots,p_{4r-1}).                        \tag{2.4}
\]

The signs `+,-` on a block below mean its forward and reverse orientations,
and `X,X` are the two new vertices.

### Candidate 2.1 (two-seam rigidity)

Suppose a second punctured deck has exactly `4r-2` targets in common with
`E`.  Its two missing base targets consist of one lower and one middle
target, and they are adjacent in `P`.  With `h` denoting the first hole
index, the simultaneous containment- and middle-disjointness-seam equations
have exactly the following solutions:

\[
\begin{array}{c|c|c|c}
\text{holes}&\text{common-block order in }P_F&
 \text{new-middle seam(s)}&\text{word completion}\\ \hline
h=2t-2&B_h^+,X,X,A_h^+&
 M_0\sim M_r,M_{r+1}\ \text{when present}&\rho_t\\
h=2t-1,\ t\ne r+1&A_h^-,X,X,B_h^-&
 M_0\sim M_r,M_{r+1}\ \text{when present}&\tau_{t+r-1}\\
h=2r+1&A_h^-,X,X,B_h^-&M_0\sim M_r&\tau_{b-1}\\
h=2r+1&A_h^-,X,X,B_h^-&M^-\sim M_r&u^-\\
h=2r+1&A_h^+,X,X,B_h^+&M^+\sim M_1&u^+,
\end{array}                                             \tag{2.5}
\]

where

\[
 M^-=\{1,\ldots,r-1,b-1\},\qquad
 M^+=\{0,r+1,\ldots,b-2\}.                             \tag{2.6}
\]

In the first two rows a missing member of `{M_r,M_(r+1)}` is simply omitted
from the seam list.  The base-index differences in every displayed
dihedral middle seam are `r` or `r+1` modulo `b`, exactly as required by
(2.2).  Every unlisted block orientation either uniquely restores a missing
base target or exposes two shared middle targets whose index difference is
not in `{r,r+1}`.

#### Proved reductions and unresolved exhaustion

Let `S` be the common target set.  Intrinsic containment gives
`P_E[S]=P_F[S]`.  After the two holes are removed, every component of this
graph is a fixed path block in `P_F`; different blocks cannot touch without
one of the two new vertices between them.

First, the holes cannot have the same layer.  If both holes were lower, all
clean middle targets would be common.  The intrinsic graph joining two
middle windows when their intersection has size `r-1` is the path
`M_1,M_2,...,M_(b-1)`.  Hence the middle start order in the second deck is
this path or its reverse.  The successive set differences recover the word;
the forward order gives `rho_0`, and the reverse order gives `tau_(r-1)`.
Their lower defects are respectively zero and one, not two.  The dual
argument with the clean lower-window path gives `rho_0` or `tau_(r-2)` when
both holes are middle.  Thus there is one hole in each layer.

The affine seam sublemma eliminates every cross-pairing traversed by two
consecutive step-`r` tests.  To complete the analytic proof, one must still
eliminate the single-test and boundary block permutations.  The required
exhaustion table is

\[
\begin{array}{c|c|c}
\text{hole positions in }P&\text{block atoms in }P_F&
 \text{result of (2.3c)--(2.3d)}\\ \hline
1\le a<c\le4r-2,\ c>a+1&CXCXC&
 \text{original pairing restores a hole; every cross-pair fails a seam}\\
a=0,\ 2\le c\le4r-2&CXXC&
 \text{fails a seam unless }c=1\\
1\le a\le4r-3,\ c=4r-1&CXXC&
 \text{fails a seam unless }a=4r-2\\
a=0,\ c=4r-1&XXC,\ CXX,\ XCX&
 \text{one constant fails (2.3d)}\\
c=a+1&CXXC\text{ or an endpoint truncation}&
 \text{the adjacent solutions in (2.5)}.
\end{array}                                             \tag{2.7}
\]

Here `a,c` are zero-based indices of the deleted `p`-vertices.  The table
is the desired conclusion, not a proved exhaustion: its single-test and
boundary rows are verified by the exact reconstructor through `r=20`, but
their uniform symbolic substitutions are still missing.  In the
first row, a natural join is a common--new--common repair and hence equals
the unique deleted intersection or union.  Every other ordering reverses a
block or changes its affine constant.  Either two consecutive step-`r`
tests cross that seam, so (2.3c)--(2.3d) reject it, or one block is a
one-vertex boundary block and direct substitution gives the same failed
constant condition.  The next three rows are the endpoint cases,
where the still-required endpoint substitution should give the displayed
adjacent exceptions.

It remains to solve the adjacent case.  If `h=2t-2`, the holes are
`L_t,M_t`; following (2.3) across the two seams gives the first row of
(2.5).  If `h=2t-1`, the holes are `M_t,L_(t+1)` and the common blocks must
be reversed, giving the second row.  The step-`r` path (2.3) has endpoints
`M_r,M_(r+1)`.  Therefore the only odd hole with an additional endpoint
completion is `t=r+1`, i.e. `h=2r+1`.  Direct set subtraction at that
endpoint gives exactly the last three rows and the two sets (2.6).

For a literal check of the word completions, if

\[
 P_F=(L'_1,M'_1,\ldots,L'_{2r},M'_{2r}),
\]

then

\[
 M'_i\setminus L'_i=\{w_{i+r-1}\}\quad(1\le i\le2r),
 \qquad
 M'_i\setminus L'_{i+1}=\{w_i\}\quad(1\le i<2r).       \tag{2.8}
\]

The first two rows of (2.5) recover `rho_t` and `tau_(t+r-1)`.  At the
central forward seam the only unknown word positions are `0,r-1,2r`, and
their remaining-label assignments leave only `u^+`.  At the central reverse
seam the same three positions leave exactly `tau_(b-1)` and `u^-`.  Every
other assignment changes a third retained window.  This verifies every
surviving completion after adjacency is assumed, but does not close the
unproved exhaustion rows in (2.7).

### Conjecture 2.2 (defect-two path reconstruction)

Let `r>=3`, and let `F=E(w)` satisfy `|E\cap F|>=4r-2`.  Then exactly one of
the following occurs.

\[
\begin{array}{c|c|c}
\operatorname{def}_E(F)&E\setminus F&w\\ \hline
0&\varnothing&\rho_0\\
1&\{L_1\}&\tau_{r-1}\\
1&\{M_{b-1}\}&\tau_{r-2}\\
2&\{L_t,M_t\},\ 1\le t\le b-1&\rho_t\\
2&\{M_t,L_{t+1}\},\ 1\le t\le b-2&\tau_{t+r-1}\\
2&\{M_{r+1},L_{r+2}\}&u^-\\
2&\{M_{r+1},L_{r+2}\}&u^+.
\end{array}                                             \tag{2.9}
\]

The subscript of `tau` is reduced modulo `b`.  In particular the last two
rows are the only non-dihedral configurations in this overlap range.

#### Conditional derivation and evidence

Let `S=E\cap F` and `d=4r-|S|`.  Containment between two vertices of `S` is
intrinsic, so `P_E[S]=P_F[S]`.

For `d=0`, this gives the entire canonically oriented path, and the
containment-path injectivity theorem gives `w=rho_0`.  For `d=1`, an
interior deletion leaves two common blocks.  In their original order and
orientation, the single new vertex is the unique intersection of its two
common middle neighbours or the unique union of its two common lower
neighbours, so it restores the deleted base target.  Swapping the blocks or
reversing one of them changes an affine constant or sign in (2.3c); the two
available step-`r` tests then violate (2.3b).  If one block has only one
vertex, direct substitution of its endpoint in (2.3d) gives the same
failure in every tested instance.  A uniform written elimination of those
single-test boundary instances is part of the same seam gap.  Conditional
on it, the deleted base vertex is an endpoint of (1.3); the two completions
are `tau_(r-1)` and `tau_(r-2)`.

For `d=2`, Candidate 2.1 gives exactly the last four families in (2.9),
conditional on its open seam exhaustion.  The exact path-template checker
verifies the whole table for every tested `3<=r<=20`.

The restriction `r>=3` is necessary for this clean statement.  At `r=2`
several short-arc coincidences create additional defect-one and defect-two
words.

## 3. Proved lower bounds and the exact-count conjecture

### Proposition 3.1 (explicit near clones)

For every `r>=3` and every directed punctured configuration `E`,

\[
 N_{4r}=1,\qquad N_{4r-1}\ge2,\qquad N_{4r-2}\ge4r+1.  \tag{3.1}
\]

#### Proof

The `2b` words in (1.5) describe the same full cyclic two-layer deck.  A
forward word `rho_s` deletes the containment edge `{L_s,M_s}`.  A reverse
word `tau_s` deletes

\[
 \{M_t,L_{t+1}\},\qquad t=s-r+1.                       \tag{3.2}
\]

The base configuration deletes `{L_0,M_0}`.  The same deleted edge gives
the unique defect-zero word `rho_0`.  Exactly two edges of the full
containment cycle are adjacent to `{L_0,M_0}`; these give the two defect-one
words in (2.9).  The other

\[
 2b-3=4r-1                                             \tag{3.3}
\]

dihedral words have defect two.  Direct substitution of the two words
`u^-` and `u^+` from (1.6) gives two further defect-two configurations, so

\[
 N_{4r-2}\ge(4r-1)+2=4r+1.                             \tag{3.4}
\]

The analytic directed-deck injectivity theorem ensures that all listed
words give distinct configurations. `square`

The two exceptional words can also be checked directly.  Each loses
exactly `M_(r+1),L_(r+2)` from `E`.  Their new target pairs are respectively

\[
\begin{array}{c|c|c}
&\text{new middle}&\text{new lower}\\ \hline
u^-&\{1,\ldots,r-1,b-1\}&\{1,\ldots,r-2,b-1\}\\
u^+&\{0,r+1,\ldots,b-2\}&\{0,r+2,\ldots,b-2\}.
\end{array}                                             \tag{3.5}
\]

All their other retained targets are base targets.

### Conjecture 3.2 (sharpness)

All three inequalities in (3.1) are equalities, i.e. (0.1) holds for every
`r>=3`.  This is exhaustive computation at `r=3,4,5` and exhaustive
containment-path reconstruction at every `3<=r<=20`; the only missing
uniform step is the seam exhaustion in Candidate 2.1.

## 4. Uniform fixed-defect bound

### Theorem 4.1

For every `r>=2`, every base configuration `E`, and every
`0<=d<=4r`, inequality (0.2) holds.  Consequently, for fixed `D`,

\[
 \sum_{d=0}^D N_{4r-d}(E)=O_D(r^D),                    \tag{4.1}
\]

uniformly in `E`.

#### Proof

Fix `F` of defect `d`, and put `S=E\cap F`.  First choose the set
`E\setminus S`, in at most `binom(4r,d)` ways.  The intrinsic common
containment graph is obtained from the path `P_E` by deleting these `d`
vertices, so it has at most `d+1` nonempty path components.

By intrinsic containment, each component occurs as one block in the
canonical path of `F`.  To overcount the possible path templates, orient
each component in at most two ways, treat the `d` new vertices as labelled
singleton atoms, and order all component and singleton atoms arbitrarily.
The singleton labelling is already included in this ordering count.  There
are at most

\[
 2^{d+1}(2d+1)!                                        \tag{4.2}
\]

such templates.

Fix one template.  Of the `2r` canonical same-start pairs
`(L'_i,M'_i)` in `F`, at most `d` contain a new vertex.  Every other pair
fixes one word position through the first identity in (2.8).  Hence at
least `max(0,2r-d)` of the `b=2r+1` word positions are fixed, and at most
`d+1` positions remain.  Once their remaining labels are assigned, the
word, all new target sets, and `F` are determined.  There are at most
`(d+1)!` assignments.

Multiplication gives (0.2).  The map from words to configurations is
injective, so no further multiplicity is present.  Summing (0.2) for
`d<=D` proves (4.1). `square`

Equivalently, the explicit bound is

\[
 N_{4r-d}(E)\le r^d\exp(O(d\log d)).                   \tag{4.3}
\]

For fixed defect this is substantially smaller than either vertex degree,
which is factorial in `r`.

## 5. Consequence and remaining polymer gate

Theorem 4.1 rules out a superpolynomial hidden family of almost identical
configurations.  For any fixed `D`, only `O_D(r^D)` configurations share all
but at most `D` targets with a given edge.  This is exactly the form needed
to isolate the top, high-overlap polymers in a cluster expansion.

The conclusion is deliberately narrower than `QFR(alpha)`.  The constant
in (0.2) grows as `exp(O(d log d))`, and the theorem says nothing about the
adaptive correlations of the surviving process.  A complete regeneration
proof must still control intermediate and growing defects and sum their
conditional weights uniformly over `O(r log r)` rounds.

## 6. Reproducibility

The standard-library checker is

`scratch/audit_punctured_near_clone_tail_20260821.py`.

It has two independent modes:

1. full permutation enumeration at `r=3,4`; and
2. polynomial containment-path reconstruction, which explicitly arranges
   and orients every common path component, fills the at most `d+1` unknown
   word positions, and checks the resulting deck.

The finite audit is a regression check, not the proof of the uniform
statements above.

On H100 (`arboghast`, Python 3.12.3), containment-path reconstruction passed
for every `3<=r<=20`, always returning the exact defect counts
`1,2,4r+1`.  Full permutation enumeration passed at `r=3,4` over `5,040`
and `362,880` words.  Checker SHA-256:

```text
6d34e750c020d3bac01978eba18a6712015826974df5f7b6f65e8de0a5a3124d
```

As a third independent check, the existing compiled intersection census
`scratch/research_punctured_configuration_intersection_profile_20260821.cpp`
exhausted all `11!=39,916,800` words at `r=5` and returned

```text
18:21, 19:2, 20:1
```

at the top of its overlap histogram.  Its source SHA-256 is

```text
b4e866badbc4bf21e43df4092638149ac055f38769f1deb4928aea34deb34fac
```
