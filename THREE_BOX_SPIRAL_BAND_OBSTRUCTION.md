# No monotone width-plus-perimeter band can use a ring-by-ring spiral order

## 1. Outcome

The concentric-hexagon walk has perfect all-depth intersection and union
shadows, but its ring-by-ring order cannot be the central witness order of a
`width+O(perimeter)` OR construction.

The obstruction is not a failed pin heuristic.  It occurs before labels are
chosen.

> **Spiral-band obstruction.**  Let the middle-layer occurrences of
> `[0,2a]^3` be ordered ring by ring, with each radius-`s` hexagon traversed
> contiguously (either orientation and any corner cut), and allow `O(a)`
> repetitions and boundary occurrences.  Suppose their selected witness
> intervals have the unrestricted monotone-band form
> \[
>       I_i=[i+\alpha_i,i+\beta_i],\qquad
>       0\leq\alpha_1\leq\cdots\leq\alpha_L\leq D,
>       \quad
>       0\leq\beta_1\leq\cdots\leq\beta_L\leq D,
> \]
> with `alpha_i<=beta_i` and `D=O(a)`.  If these central intervals are
> coordinatewise factorable, then they leave only
> \[
>                         3a^3+O(a^2)
> \]
> physical intervals which could possibly represent below-middle targets.
> But there are
> \[
>                         4a^3+O(a^2)
> \]
> such targets.  Hence no labeling of this band is universal.

This kills the entire monotone-band realization of the outward closed
spiral, not merely the radius band `I_i=[i,i+s]`.  The shadow theorem remains
valid and useful, but a successful construction must interleave different
radii (so the short extreme-coordinate runs are no longer `O(a)`-dense), or
use a central skeleton not organized as one contiguous block per ring.

## 2. Exact count of intervals avoiding an antichain band

The counting statement below is useful independently of the spiral.

Let

\[
                    I_i=[\ell_i,r_i],\qquad 1\leq i\leq L,
\]

where both endpoint sequences are strictly increasing.  Put

\[
                    w_i=r_i-\ell_i,
            \qquad \Delta_i=\ell_i-\ell_{i-1}\quad(i\geq2).
\]

### Lemma 1 (avoidance ledger)

Apart from the two boundary regions before `ell_1` and after `ell_L`, the
number `Q` of physical intervals containing no complete `I_i` satisfies the
exact formula

\[
 Q=\sum_{i=2}^L
       \left(\Delta_iw_i+{\Delta_i\choose2}\right)
       +\text{(the two boundary terms)}.                         \tag{2.1}
\]

For the monotone normal form

\[
             \ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
             \qquad0\leq\alpha_i\leq\beta_i\leq D,             \tag{2.2}
\]

in a physical word with only `O(D)` additional boundary positions, (2.1)
implies

\[
                         Q\leq\sum_iw_i+O(D^2).                 \tag{2.3}
\]

### Proof

Fix a physical left endpoint `x`, and let `i` be the first index for which
`ell_i>=x`.  An interval beginning at `x` must end before `r_i`; otherwise
it contains `I_i`.  For

\[
                         \ell_{i-1}<x\leq\ell_i
\]

the number of allowed right endpoints is `r_i-x`.  Summing over these
`Delta_i` starts gives

\[
 \sum_{h=0}^{\Delta_i-1}(w_i+h)
       =\Delta_iw_i+{\Delta_i\choose2},
\]

which is (2.1).

In (2.2),

\[
             \Delta_i=1+(\alpha_i-\alpha_{i-1}),
             \qquad \sum_i(\Delta_i-1)\leq D,
             \qquad w_i\leq D.
\]

The excess of the first term in (2.1) over `sum_i w_i` is at most `D^2`,
and the sum of the quadratic gap terms is at most `O(D^2)`.  Each boundary
region has length `O(D)` and contributes another `O(D^2)`.  This proves
(2.3).  \(\square\)

If the `I_i` witness incomparable middle-rank targets, every below-middle
target interval must be counted by `Q`: an interval containing any complete
`I_i` has OR rank at least the middle rank.

## 3. Exact run inequality for a general band

Fix one chain increment (one Boolean coordinate of the embedded box), and
write `epsilon_i=1` when it belongs to the `i`th middle target.

### Lemma 2 (band run inequality)

If `[u,v]` is an internal 1-run of the incidence word, coordinatewise
factorability requires

\[
                 r_{u-1}+2\leq\ell_{v+1},                       \tag{3.1}
\]

or equivalently, in (2.2),

\[
                 \beta_{u-1}-\alpha_{v+1}\leq v-u.             \tag{3.2}
\]

### Proof

The zero interval immediately before the run forbids the coordinate through
position `r_(u-1)`, and the zero interval immediately after the run forbids
it beginning at `ell_(v+1)`.  Every positive witness in the run needs a
legal integer pin strictly between those two forbidden regions.  Such a pin
exists only if (3.1) holds.  Substitution gives (3.2).  \(\square\)

For monotone endpoints this condition is also sufficient coordinatewise,
but only necessity is needed below.

## 4. Dense short runs on concentric hexagons

Translate the middle layer to

\[
 H_a=\{(x,y,z):x+y+z=0,\ |x|,|y|,|z|\leq a\}.
\]

On a radius-`s` ring, the vertices with `y=s` form one side of the hexagon,
an internal incidence run of exactly `s+1` vertices.  The vertices with
`z=s` form another such internal run.  These are the incidence words of the
valid chain increments `y>=s` and `z>=s`, respectively.  With a different
corner cut, at most one of the three positive extreme sides meets the cut,
so two other coordinate directions always supply the same two internal
runs.

Choose these two runs on every ring.  In a ring-by-ring traversal:

* the two chosen starts on one ring are separated by at most `2s+O(1)`;
* the second chosen start on radius `s` and the first chosen start on the
  next ring are separated by at most `4s+O(1)`;
* every chosen run has length at most `a+1`.

Consequently, except for a final suffix of `O(a)` occurrences, every index
`i` lies before a selected run `[u,v]` with

\[
                       i\leq u-1,\qquad v+1-i\leq5a+O(1).     \tag{4.1}
\]

The statement is unchanged by reversing the traversal, permuting the
coordinate names, changing the corner cuts, or listing the complete rings
in another order: the constant in (4.1) changes, but remains absolute.  It
also tolerates `O(a)` extra/repeated occurrences.

For precision about the last clause, a repeated positive occurrence can
lengthen a selected run.  Write its new length minus one as `s+e_R` instead
of `s`.  The selected runs are disjoint, so `sum_R e_R=O(a)`.  Each excess
is charged to only `O(a)` preceding indices below, contributing `O(a^2)` in
total.  Insertions enlarge the distances in (4.1) by at most `O(a)` as
well.  Thus repetitions do not change the leading term.  Alternatively,
delete the repeated middle occurrences and apply the argument to the
`M_a` distinct ring vertices.

## 5. Charging the total witness length

Write

\[
                         w_i=\beta_i-\alpha_i.
\]

For an index outside the final suffix, choose the next short run `[u,v]` as
in (4.1).  Monotonicity and (3.2) give

\[
\begin{split}
 w_i
   &=\beta_i-\alpha_i\\
   &\leq\beta_{u-1}-\alpha_i\\
   &\leq a+e_R+\alpha_{v+1}-\alpha_i.                          \tag{5.1}
\end{split}
\]

Sum (5.1).  An increment of the nondecreasing sequence `alpha` can occur in
`alpha_(v+1)-alpha_i` only for indices `i` lying within `5a+O(1)` positions
before it.  Since the total increase of `alpha` is at most `D`,

\[
             \sum_i(\alpha_{v(i)+1}-\alpha_i)=O(aD).            \tag{5.2}
\]

The final `O(a)` indices contribute at most `O(aD)`, and the total `e_R`
charge is `O(a^2)`.  Therefore

\[
                         \sum_iw_i\leq aL+O(aD+a^2).            \tag{5.3}

\]

For the closed spiral, or any ring-by-ring middle enumeration with only
`O(a)` repetitions,

\[
                         L=3a^2+O(a).
\]

If `D=O(a)`, equations (2.3) and (5.3) give

\[
                         Q\leq3a^3+O(a^2).                      \tag{5.4}

\]

On the other hand the number of nonempty points strictly below the middle
layer of `[0,2a]^3` is

\[
 { (2a+1)^3-(3a^2+3a+1)\over2}-1
       =4a^3+{9\over2}a^2+{3\over2}a-1.                        \tag{5.5}

\]

For all sufficiently large `a`, (5.4) is strictly smaller than (5.5).
This proves the spiral-band obstruction.

## 6. What ordering property is now required

The failure is caused by the same two facts on every radius:

1. two extreme-coordinate supports are internal runs of length only
   `Theta(a)`;
2. another such pair occurs after only `Theta(a)` more middle vertices.

Together they cap average witness delay at `a+O(1)`, whereas the lower-half
volume requires average delay `4a/3+O(1)`.

A viable central ordering must therefore destroy this dense-run pattern.
One concrete necessary target is:

> For every choice of two coordinate directions, a positive fraction of
> middle occurrences must be farther than `Omega(a)` (with a sufficiently
> large constant) from the next short internal extreme-threshold run, or
> the short supports must be moved to monotone-band transitions whose total
> offset increase is still only `O(a)`.

Interleaving arcs from many radii is the natural way to attempt this.  The
complete-shadow walk in `THREE_BOX_HEX_SPIRAL.md` remains a useful source of
arcs, but the radii cannot remain contiguous blocks in the central witness
order.
