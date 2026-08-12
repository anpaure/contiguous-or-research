# A post-hoc vertical-rounding obstruction for monotone queue atoms

This note addresses one natural proposed route around the multiscale ABKV
ceiling:

1. give every middle set its lower and upper chain flags (possibly after
   obtaining exact middle ownership);
2. independently randomize those vertical flags;
3. only afterwards pack the annotated middle sets into monotone queue paths;
4. repair a sublinear number of bad annotations by an alteration or absorber.

The theorem below shows that this order of operations fails already at depth
two.  With high probability even the relaxed graph of necessary rotor-prefix
transitions between radius-at-least-two centers has only `O(W/m^2)` edges.
Consequently almost
every such center would need its own queue initialization.  More strongly,
even an optimal post-processing alteration must change a linear number of
center annotations before an `o(W)`-component queue packing is possible.

This is an obstruction to **independent vertical-first rounding**, not to a
simultaneous correlated queue construction.  It pinpoints the correlation
that a hierarchical queue-rounding theorem has to create from the outset.

Throughout,

\[
 W=\binom{2m}{m}.
\]

## 1. Independently annotated middle centers

Give each middle set `S` a radius `r(S)`.  Conditional on the radii, choose
independently for every `S`

* a uniformly random ordered `r(S)`-tuple
  \(x_0(S),\ldots,x_{r(S)-1}(S)\) of distinct elements of `S`;
* a uniformly random ordered `r(S)`-tuple
  \(y_1(S),\ldots,y_{r(S)}(S)\) of distinct elements of `S^c`.

The lower and upper tuples are mutually independent, both within one center
and between distinct centers.  All radii under discussion satisfy `r(S)<m`,
as they do in the target central band.

The advertised vertical chain through `S` is

\[
 S\setminus\{x_0,\ldots,x_{q-1}\},\qquad
 S\cup\{y_1,\ldots,y_q\},
 \qquad 0\le q\le r(S).
\tag{1}
\]

The middle sets themselves are already owned exactly once.  Thus the model is
literally a random vertical annotation **conditioned on exact middle
ownership**.  It deliberately gives the later horizontal packing algorithm
the strongest possible freedom: after seeing all annotations it may choose
the path decomposition optimally.

Put

\[
 \mathcal R_2=\{S:r(S)\ge2\},\qquad R_2=|\mathcal R_2|.
\tag{2}
\]

In any certified ledger with depth-two duplicate plus missing count `o(W)`,
one necessarily has

\[
 R_2=(1-o(1))W.
\tag{3}
\]

Indeed, every radius-at-least-two middle occurrence contributes exactly one
certified lower depth-two mask, so

\[
 R_2=T_2^-=N_2+D_2^--M_2^-
       =(1-o(1))W.
\tag{4}
\]

The same conclusion follows from the upper row.

## 2. The exact rotor transition law

Suppose an annotated center `S` of radius `r` is followed in a genuine queue
atom by a center `S'` of radius `e`, where `2 <= e <= r`.  Write the queue as

\[
 S=\{z_t,z_{t+1},\ldots,z_{t+m-1}\},\qquad
 S'=\{z_{t+1},\ldots,z_{t+m}\}.
\]

The old flags are

\[
 x_i=z_{t+i}\quad(0\le i<r),
 \qquad y_j=z_{t-j}\quad(1\le j\le r).
\tag{5}
\]

Put `a=z_{t+m}`.  Then necessarily

\[
 S'=S-\{x_0\}+\{a\}.
\tag{6}
\]

For the new center, the upper flag is forced completely through depth `e`:

\[
 (y'_1,\ldots,y'_e)=(x_0,y_1,\ldots,y_{e-1}).
\tag{7}
\]

If `e<r`, the new lower flag is also forced completely:

\[
 (x'_0,\ldots,x'_{e-1})=(x_1,\ldots,x_e).
\tag{8}

\]

If `e=r`, its first `r-1` entries are forced:

\[
 (x'_0,\ldots,x'_{r-2})=(x_1,\ldots,x_{r-1});
\tag{9}
\]

The final lower coordinate is the next, previously unseen, queue coordinate;
in particular it lies in
`S\setminus\{x_0,\ldots,x_{r-1}\}` and is not the incoming coordinate `a`.

Equations (6)--(9) are necessary regardless of how the atom is later
factorized or reset.  Call a directed pair `(S,S')` satisfying the displayed
forced-prefix relations a **high forced-prefix transition**.  Every genuine
rotor transition is a high forced-prefix transition; using the relaxed graph
only strengthens the forthcoming upper bound.

## 3. Expected number of compatible high transitions

### Theorem 1 (depth-two post-hoc compatibility bound)

Conditional on an arbitrary deterministic radius assignment, the independent
flag model above satisfies

\[
 \boxed{
 \mathbb E E_2\le \frac{R_2}{m(m-1)}\le\frac{W}{m(m-1)},
 }
\tag{10}
\]

where `E_2` is the number of directed high forced-prefix transitions.
Consequently

\[
 \boxed{E_2=O(W/m^2)}
\tag{11}
\]

with probability tending to one.  In particular the weaker Markov estimate is

\[
 \Pr(E_2>W/m^{1/2})\le m^{-3/2}(1+o(1)).
\tag{12}
\]

#### Proof

Fix `S` of radius `r>=2` and condition on all of its flags.  Once the
incoming coordinate `a in S^c` is chosen, equation (6) determines `S'`.
There are at most `m` choices of `a`.  If `r(S')=e>=2`, the annotation at
`S'` is independent of the one at `S`.

If `e<r`, equations (7)--(8) prescribe two ordered `e`-tuples.  The
conditional probability is therefore either zero or

\[
 \frac1{(m)_e^2}.
\tag{13}
\]

If `e=r`, equation (9) prescribes the first `r-1` lower entries, while (7)
prescribes all `r` upper entries.  The conditional probability of the relaxed
forced-prefix event is either zero or

\[
 \frac1{(m)_{r-1}(m)_r}.
\tag{14}
\]

For a genuine transition there is the additional final-coordinate condition
just noted, so its probability is smaller by the factor
`(m-r)/(m-r+1)`.  Only the upper bound (14) is used below.

For every `r>=e>=2`, both (13) and (14) are at most

\[
 \frac1{m^2(m-1)};
\tag{15}
\]

the largest case is `r=e=2`.  Summing (15) over at most `m` possible incoming
coordinates gives expected high outdegree at most

\[
 \frac1{m(m-1)}.
\tag{16}
\]

Summing over `R_2` possible tails proves (10).  Markov's inequality gives
(12).

For the sharper high-probability form (11), expose one independent center
annotation at a time and use the maximal depth-two graph (12a) below.  Changing
one center annotation changes at most `m` outgoing candidate edges and at
most `m^2` incoming candidate edges.  Hence the bounded-differences constant
is at most `m^2+m`.  McDiarmid's inequality, with `W` independent center
annotations, gives

\[
 \Pr\left(E_2>\frac{2W}{m(m-1)}\right)
 \le
 \exp\left(-\Omega(W/m^8)\right)=o(1).
\tag{12b}
\]

This proves (11).  QED

There is also an adaptive-radius version.  Sample an ordered lower pair and
an ordered upper pair independently at **every** middle center before any
radii are assigned.  Define the maximal depth-two graph by the necessary
relations

\[
 S'=S-\{x_0\}+\{a\},\qquad
 x'_0=x_1,\qquad (y'_1,y'_2)=(x_0,y_1).
\tag{12a}
\]

For each possible `a`, (12a) has probability

\[
 \frac1m\frac1{m(m-1)}=\frac1{m^2(m-1)}.
\]

Thus the entire maximal graph, before any high-center subset is chosen, has
expected size at most `W/[m(m-1)]`.  Every genuine transition between two
centers subsequently assigned radius at least two is an edge of this graph.
Consequently (11)--(12) remain valid even if the radii and the set
`R_2` are selected adversarially **after** all independent flags are seen.

The estimate is much smaller than a generic pair-codegree statement.  It is
the exact probability of satisfying the two opposed rotor shifts at once.
At depth two, independently chosen vertical flags miss the required
horizontal correlation by a factor of order `m^2`.

The same calculation has a useful all-depth form.  If `E_q` counts directed
transitions whose two endpoint radii are at least `q>=2`, then

\[
 \mathbb E E_q
 \le
 |\{S:r(S)\ge q\}|\,
 \frac{m}{(m)_{q-1}(m)_q}
 =O_q\!\left(Wm^{-2q+2}\right)
\tag{16a}
\]

Indeed, the largest compatibility probability occurs when both radii equal
`q`; it is `1/((m)_{q-1}(m)_q)` for each of at most `m` possible incoming
coordinates.  The exact falling-factorial estimate is valid for growing `q`;
the final power-law notation in (16a) is asserted only for fixed `q`.  Thus
depth two is already the weakest obstruction.

## 4. Consequence for path count and reset cost

### Corollary 2 (post-hoc packing needs linearly many atoms)

Assume (3).  After the annotations have been exposed, form any family of
vertex-disjoint monotone-radius queue atoms using them without alteration and
covering all but `o(W)` members of `R_2`.  If `p_2` is the number of atoms
that contain a radius-at-least-two center, then, with high probability,

\[
 \boxed{p_2=(1-o(1))W.}
\tag{17}
\]

#### Proof

In a monotone-radius atom, the radius-at-least-two centers form an initial
consecutive segment.  If that segment has `k` centers, it uses `k-1` high
forced-prefix transitions.  Summing over the atoms gives

\[
 R_{2,\mathrm{cov}}-p_2\le E_2.
\tag{18}
\]

Now `R_{2,cov}=(1-o(1))W` and Theorem 1 gives `E_2=o(W)`.  This proves (17).
QED

For the standard literal atom (with maximum radius strictly below `m`), an
atom whose maximum radius is at least two
has word length

\[
 \#\{\text{centers}\}+2d_0+1
 \ge \#\{\text{centers}\}+5.
\tag{19}
\]

Thus the independently annotated construction has length at least

\[
 R_{2,\mathrm{cov}}+5p_2=(6-o(1))W
\tag{20}
\]

even before paying for other missing masks.  The exact constant in (20) is
not important; the decisive point is that the reset charge is `Theta(W)`,
not `o(W)`.

## 5. Sublinear alteration cannot repair the model

The failure is not cured by changing a sparse exceptional set of flags.

### Theorem 3 (linear alteration lower bound)

Expose independent ordered lower and upper pairs at every center and let
`E_2` be the maximal graph (12a).  Then choose the initial radii, even
adaptively.  Change the relevant ordered depth-two flags and/or radii at a set
`C` of centers, where `C` contains every center whose relevant data changed.
Suppose the altered annotations admit monotone queue atoms covering
`(1-o(1))W` centers whose **final** radius is at least two, with `p=o(W)`
atoms.  Then, with high probability,

\[
 \boxed{|C|\ge(1/2-o(1))W.}
\tag{21}
\]

#### Proof

Delete the altered centers from the final path family.  The remaining
unaltered high centers split into at most `p+|C|` runs: deleting one vertex
from a path increases the number of surviving runs by at most one.

Every adjacency inside one of these unaltered runs was already a high
forced-prefix transition in the original annotation.  If `U` unaltered high
centers survive, their runs therefore use at least

\[
 U-(p+|C|)
\]

original compatible transitions.  Hence

\[
 U\le E_2+p+|C|.
\tag{22}
\]

The total number of covered high centers is at most `U+|C|`, so

\[
 (1-o(1))W\le E_2+p+2|C|.
\tag{23}
\]

Theorem 1 gives `E_2=o(W)`, and `p=o(W)` by hypothesis.  Rearranging proves
(21).  QED

Therefore an absorber that touches only `o(W)` independently rounded center
annotations cannot create the required long queue paths.  A successful
absorber may still be small in **word length**, but it must control a linear
number of center flags through correlated switches; it cannot be a local
cleanup applied after independent vertical resolution.

## 6. Exact implication for the multiscale black box

At the target depth

\[
 d=(1+o(1))\sqrt{m\log\log m},
\]

the row-two quota is already

\[
 \rho_2=\frac{\binom{2m}{m-2}}{\binom{2m}{m}}=1-O(1/m).
\]

Hence every duplicate-plus-missing `o(W)` ledger has (3).  Theorem 1 then
shows that the following natural candidate is impossible:

> resolve the vertical flags (even with exact middle ownership), randomize
> them independently at the centers, and subsequently find or alter a
> horizontal queue packing.

The missing hierarchical theorem has to reverse or fuse those steps.  It
must construct the rotor paths and the vertical ownership together, so that
for almost every consecutive pair the depth-two lower tail and upper head
are the prescribed shifts (8)--(9) and (7).  Depth-one two-sided-rainbow
forests provide precisely the first instance of this correlation; independent
chain flags destroy it.

This obstruction does **not** rule out:

* a simultaneous path/flag nibble;
* an iterative absorber whose switches globally correlate a linear number of
  flags while using only `o(W)` extra word entries;
* an explicit SCD whose annotated centers are already organized into rotor
  paths;
* shared-reset words outside the separate-atom model.

It does rule out a broad and tempting post-hoc strategy, with a quantitative
gap of `Theta(m^2)` already at the first nontrivial multidepth transition.
