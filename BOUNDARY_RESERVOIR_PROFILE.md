# Boundary reservoirs and the unsaturated atom profiles

## 1. Outcome

This note adds one position-sensitive invariant to the corrected scalar
profile system.  It is enough to exclude the entire family

\[
                    \mu=2\delta_x,
       \qquad {4\over3}\le x<{3\over2},
       \qquad H(c)=0.                              \tag{1.1}
\]

The scalar laws alone do **not** exclude (1.1).  The missing information is
where the complement of the dangerous plateaux occurs.  If that complement
forms a macroscopic boundary reservoir, most of its indices have a complete
one-sided window containing no dangerous plateau.  The small-cap run-spectrum
inequality then sees those indices even though the first-dangerous seam
functional does not.

The basic proved estimate is the following quadratic law.  Let `R_c` be any
set of middle-order indices such that, for every `i in R_c`, some valid
forward or backward window of length

\[
                              L=4a+2                \tag{1.2}
\]

contains no complete directed peak plateau of edge length greater than
`ca`.  If the witness slack is `D=o(a^2)`, then, for every fixed
`0<c<2/3`,

\[
                     \boxed{
       |R_c|\le\left({9\over4}c^2+o(1)\right)a^2.} \tag{1.3}
\]

Thus the density of a region which is locally free of `c`-dangerous
plateaux is `O(c^2)`, not merely `O(c)`.

For an atom profile `mu_a -> 2 delta_x` with vanishing first-dangerous seam
functional at every sufficiently small fixed threshold, the plateau
complement has density `3-2x`.  Vanishing seam mass makes all but `o(a^2)`
of that complement visible to one-sided dangerous-free windows.  Equation
(1.3) therefore gives

\[
                         3-2x\le {9\over4}c^2       \tag{1.4}
\]

for every small fixed `c`.  Sending `c` to zero forces `x>=3/2`; edge
disjointness forces `x<=3/2`.  Hence only the saturated endpoint

\[
                              \mu=2\delta_{3/2}     \tag{1.5}
\]

survives this invariant.

This does **not** prove the three-box obstruction.  The saturated endpoint
has no macroscopic complement reservoir, so a transition or level-geometry
theorem is still required there.

## 2. Inherited framework

We use the audited three-box selected-middle-order notation.

* The middle order has length

  \[
                         M_a=3a^2+3a+1.             \tag{2.1}
  \]

* One middle witness is selected for every middle target, with total band
  slack `D`.
* A run assigned to an index is internal, avoids that index, and may point
  either forward or backward.
* For an integer cap `1<=h<=a`, the exact lower-layer deficit is

  \[
       B_a(h):=hM_a-|S_h|
              ={h(h+1)(2h+1)\over6}.               \tag{2.2}
  \]

The audited subset form of the run-spectrum inequality says that if runs
are assigned only to a subset `J`, with assigned costs `lambda_i`, then

\[
 |S_h|\le
 \sum_{i\in J}\min\{\lambda_i,h\}
 +(M_a-|J|)h+(C_\alpha+C_\beta+h)D.                \tag{2.3}
\]

If every assigned run lies in a forward or backward length-`L` window,
then

\[
                       C_\alpha,C_\beta\le L+1.    \tag{2.4}
\]

The dangerous-free-window lemma is also inherited and audited for every
fixed `c>0`:

> If a length-`L` one-sided window contains no complete directed peak
> plateau of cost greater than `ca`, it contains an internal avoiding run
> of cost at most `ca`.

The fixedness of `c` matters.  The estimates below first let `a` tend to
infinity for a fixed `c`; only afterward do they let `c` tend to zero.

## 3. The quadratic reservoir law

### Theorem 3.1 (finite cap form)

Let `R_c` have the property stated in Section 1 and put `K=|R_c|`.  For
every integer `h` satisfying

\[
                       \lfloor ca\rfloor<h\le a,   \tag{3.1}
\]

one has

\[
 K\bigl(h-\lfloor ca\rfloor\bigr)
 \le B_a(h)+(2L+2+h)D.                              \tag{3.2}
\]

#### Proof

At every index of `R_c`, choose the cheap run supplied by its
dangerous-free one-sided window.  Its integer edge cost is at most
`floor(ca)`.  Leave all other indices unassigned and apply (2.3).  By
(2.4),

\[
 |S_h|\le K\lfloor ca\rfloor+(M_a-K)h+(2L+2+h)D.
\]

Move `|S_h|` to the other side and use
`hM_a-|S_h|=B_a(h)`.  This is exactly (3.2).  No distributional or
concentration hypothesis is used.  \(\square\)

### Corollary 3.2 (optimized small-cap form)

Assume `D=o(a^2)`.  For fixed `0<c<2/3`, take

\[
                         h=\left\lfloor{3ca\over2}\right\rfloor. \tag{3.3}
\]

Then (2.2) and (3.2) give

\[
 \begin{aligned}
 {K\over a^2}
 &\le {\frac13(3c/2)^3+o(1)\over c/2}+o(1)\\
 &= {9\over4}c^2+o(1).                             \tag{3.4}
 \end{aligned}
\]

This proves (1.3).

The constant `9/4` is the optimum obtainable from this cap calculation.
Indeed, putting `h=ya`, with `c<y<=1`, gives

\[
                  {K\over a^2}\le {y^3\over3(y-c)}+o(1),          \tag{3.5}
\]

whose derivative vanishes at `y=3c/2`.

### Interpretation

The global average-cost statement only says that many indices must receive
large runs.  Theorem 3.1 is sharper for a prescribed spatial set: every
index in a dangerous-free reservoir incurs a deficit of roughly
`h-ca`, while the entire rank deficit available at cap `h` is only about
`h^3/3`.  Choosing `h=3ca/2` converts the cubic rank deficit into the
quadratic density bound (1.3).

## 4. From vanishing seam mass to a deep reservoir

We now specialize to the atom profiles which survived the corrected scalar
system.

Let the directed peak plateaux, normalized as a counting measure, be

\[
             \mu_a={1\over a}\sum_P
                       \delta_{\lambda(P)/a}.       \tag{4.1}
\]

Assume, along a sequence `a -> infinity`, that

\[
                         \mu_a\Longrightarrow2\delta_x,
                  \qquad 0<x\le{3\over2}.          \tag{4.2}
\]

Fix `c` with `0<c<x`.  List the `c`-dangerous plateaux in word order as

\[
                         P_j=[u_j,v_j],
                 \qquad \lambda_j=v_j-u_j>ca.      \tag{4.3}
\]

Their edge sets are disjoint and consecutive plateaux share at most one
vertex.  Let `g_(j-1)` be the number of complement positions between
`P_(j-1)` and `P_j`.  The audited first-dangerous seam functional is

\[
 H_a(c)={1\over a^3}\sum_{j\ge2}
       (\lambda_j-ca)\min\{g_{j-1},L-\lambda_j\}.   \tag{4.4}
\]

We assume

\[
                              H_a(c)\longrightarrow0              \tag{4.5}
\]

for every sufficiently small fixed positive `c`.  This is the geometric
meaning required by the scalar notation `H(c)=0`; a single numerical
statement at a threshold bounded away from zero is not enough.

### Lemma 4.1 (almost all complement positions are deep)

Under (4.2), for every fixed `c<x` satisfying (4.5), the number of
positions in the complement gaps lying within `L` positions of a gap end
is `o(a^2)`.  The two outside word boundaries contribute only `O(a)` more.

#### Proof

Choose `epsilon>0` so small that

\[
              c<x-\epsilon,
       \qquad x+\epsilon<4.                         \tag{4.6}
\]

Call a dangerous plateau regular when
`|lambda_j/a-x|<epsilon`.  Weak convergence in (4.2), on the compact
interval `[0,2]`, implies that all but `o(a)` dangerous plateaux are
regular.  A regular successor satisfies

\[
 \lambda_j-ca\ge(x-\epsilon-c)a=:\eta a,
 \qquad
 L-\lambda_j\ge(4-x-\epsilon)a+O(1)=:\kappa a+O(1),               \tag{4.7}
\]

with `eta,kappa>0`.

Equation (4.4) and (4.5) therefore give

\[
 \sum_{\substack{j\ge2\\P_j\ \mathrm{regular}}}
       \min\{g_{j-1},L-\lambda_j\}=o(a^2).          \tag{4.8}
\]

Since `L-lambda_j>=kappa a+O(1)` and `2L=O(a)`, a constant depending only
on `x,epsilon` satisfies

\[
             \min\{g_{j-1},2L\}
       \le C\min\{g_{j-1},L-\lambda_j\}             \tag{4.9}
\]

for every regular successor.  The exceptional successors are only `o(a)`
in number, and each contributes at most `2L=O(a)` to the truncated-gap
sum.  Hence all internal gaps together satisfy

\[
                         \sum\min\{g_j,2L\}=o(a^2). \tag{4.10}
\]

The prefix and suffix gaps were omitted from (4.4), but deleting at most
`2L` positions from each costs only `O(a)`.  This proves the lemma.
\(\square\)

### Lemma 4.2 (size of the complement)

Under (4.2), the union of the `c`-dangerous plateau vertices has size

\[
                            (2x+o(1))a^2,            \tag{4.11}
\]

and its complement has size

\[
                            (3-2x+o(1))a^2.          \tag{4.12}
\]

#### Proof

Weak convergence on `[0,2]` also gives convergence of the first moment.
Plateaux outside any fixed neighborhood of `x` are `o(a)` in number and
have length at most `2a`; because `c<x` is fixed, the total edge length of
the `c`-dangerous plateaux is therefore

\[
                         \sum_j\lambda_j=(2x+o(1))a^2.             \tag{4.13}
\]

There are `(2+o(1))a` such plateaux.  Passing from edge mass to vertex-union
mass adds one vertex per plateau and subtracts at most one shared endpoint
per consecutive pair, an `O(a)` correction.  Subtract (4.11) from
`M_a=3a^2+O(a)`.  \(\square\)

### Corollary 4.3 (deep reservoir density)

Delete the first and last `L` positions from every complement gap, whenever
present.  Every remaining position has a forward or backward length-`L`
window wholly inside that gap, hence belongs to `R_c`.  Lemmas 4.1 and 4.2
give

\[
                       |R_c|\ge(3-2x+o(1))a^2.      \tag{4.14}
\]

The point is precisely that (4.4) omits the two boundary gaps, while
(4.14) does not: a macroscopic boundary gap loses only `O(a)` positions
when it is clipped by a length-`L` window.

## 5. Saturation theorem for the atom continuum

### Theorem 5.1 (boundary-reservoir saturation)

Assume

1. `D=o(a^2)`;
2. `mu_a -> 2 delta_x` for some `0<x<=3/2`; and
3. `H_a(c)->0` for every sufficiently small fixed `c>0`.

Then

\[
                                  x={3\over2}.       \tag{5.1}
\]

#### Proof

Fix any sufficiently small `c<min{x,2/3}`.  Corollary 4.3 and the quadratic
reservoir law give

\[
               3-2x\le {9\over4}c^2.               \tag{5.2}
\]

First let `a` tend to infinity with `c` fixed, as required by the
`O_c` estimates.  Then let `c` decrease to zero.  This gives `x>=3/2`.
On the other hand, disjointness of directed plateau edges gives

\[
             \int t\,d\mu(t)=2x\le3,               \tag{5.3}
\]

so `x<=3/2`.  \(\square\)

### Consequence for the corrected scalar counterprofiles

The continuum

\[
             2\delta_x,\qquad {4\over3}\le x\le{3\over2},       \tag{5.4}
\]

really does satisfy all corrected scalar inequalities when `H=0`.  Theorem
5.1 uses new information and excludes every member of (5.4) except its
saturated endpoint.  Thus the correct ledger is:

* scalar profile laws alone: unsaturated atoms survive;
* scalar laws plus clipped, position-resolved dangerous-free service at
  every small cap: unsaturated atoms die;
* saturated atom `2 delta_(3/2)`: still open.

## 6. A more general invariant and what it can see

The proof of Theorem 3.1 did not use an atom profile.  If

\[
 r(c):=\limsup_{a\to\infty}{|R_c|\over a^2},         \tag{6.1}
\]

then for every fixed `0<c<2/3`,

\[
                              r(c)\le{9\over4}c^2.   \tag{6.2}
\]

This is a minimal boundary theorem: any proposed near-width order must make
all but `O(c^2a^2)` indices have no valid one-sided length-`L` window that is
free of complete directed plateaux longer than `ca`.  It couples three pieces which the
scalar measure separates:

1. physical position in the word;
2. clipping of service intervals at the two word boundaries; and
3. the entire family of small caps `h`, rather than one average cap.

The estimate can also be written before optimization.  For every
`c<y<=1`,

\[
             r(c)(y-c)\le {y^3\over3}.              \tag{6.3}
\]

Equation (6.2) is the envelope of (6.3).

## 7. Limitations and counterexamples to stronger readings

### 7.1 The scalar system cannot prove Theorem 5.1

The profile `2 delta_(4/3), H=0` is a genuine counterexample to any claimed
derivation of saturation using only `(mu,e,S,H,sigma)`.  Spatial placement
is essential.  The quadratic reservoir law introduces the missing spatial
quantity `R_c`.

### 7.2 Vanishing seam mass is used essentially in the atom corollary

Theorem 3.1 is unconditional under `D=o(a^2)`, but Lemma 4.1 is not.  If
`H_a(c)` has positive limiting mass, the complement can be broken into
`Theta(a)` gaps of length `Theta(a)`, every point lying within `L` of a
dangerous plateau.  Then the complement may be macroscopic while `R_c` is
small.  The present theorem does not exclude such a profile.

The minimal missing extension for a general profile is therefore a theorem
forcing either

\[
             r(c)=\Omega(3-\sigma)
\quad\hbox{or}\quad
             H(c)\ge\Phi(3-\sigma,c)                \tag{7.1}
\]

with a quantitatively useful `Phi`.  The first-dangerous seam bound gives
an upper bound on `H`; it does not yet supply the required lower bound.

### 7.3 Saturation remains invisible

At `x=3/2`, equation (4.12) leaves only `o(a^2)` complement positions, so
(1.3) is consistent with equality.  Reversal symmetry or two-sided windows
do not improve this particular budget: there is no macroscopic reservoir
left to charge.  One must use transitions between the three plateau
letters, distinct line levels, or another invariant internal to the
saturated plateau union.

### 7.4 This is an obstruction, not a construction

Nothing here constructs a universal OR word or proves that a scalar profile
is geometrically realizable.  Theorem 5.1 only removes a class of abstract
survivors from a hypothetical `D=o(a^2)` three-box order.

## 8. Theorem ledger

### Proved

* The finite subset inequality (3.2).
* The optimized quadratic reservoir law (1.3).
* Lemma 4.1 under its explicit atom and vanishing-seam hypotheses.
* The atom saturation theorem: `2 delta_x, H=0` forces `x=3/2`.

### Conditional on stated hypotheses, but rigorous

* Translating a scalar notation `H(c)=0` into Theorem 5.1 requires
  `H_a(c)->0` at every sufficiently small fixed threshold along the same
  subsequence.
* Generalizing from one atom to a broad measure requires controlling
  exceptional short plateaux uniformly near `c=0`; that is not done here.

### Not proved

* Exclusion of `2 delta_(3/2)`.
* A universal lower bound on seam mass for fragmented reservoirs.
* The full three-box obstruction or the original Boolean-lattice
  conjecture.
