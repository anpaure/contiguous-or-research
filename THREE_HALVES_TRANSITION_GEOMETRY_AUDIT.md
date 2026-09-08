# Independent re-audit of `THREE_HALVES_TRANSITION_GEOMETRY.md`

## 1. Verdict

The explicit near-`3a/2` transparent packet is correct.  Re-deriving every
coordinate transition gives the advertised monotonicity signs, all points
are distinct, the mass coefficient is correct, and no hidden short peak or
nonpeak threshold component occurs in the clean bulk.

The exact proved conclusion is:

> For every fixed `0<epsilon<1/2` and all sufficiently large even `a`, a
> full permutation of `H_a` contains a positive-density interval with
> `Theta_epsilon(a)` distinct directed internal line peaks, each of cost in
> `[(3/2-epsilon)a,(3/2)a)`, separated by one-point transparent gaps.  Every
> internal threshold run wholly contained in the bulk of that interval has
> cost at least `(3/2-epsilon)a-O(1)`.

There are two scope qualifications.

1. The blocks have the **A sign pattern**, but they are not A blocks in the
   literal definition of the direct-braid theorem, because one separator
   position lies between consecutive peak plateaux.  Direct-adjacency
   A-turn inequalities cannot be cited without a bounded-gap extension.
2. Completing the packet to a full permutation can create additional peaks
   in the arbitrary prefix.  The construction proves local positive-density
   feasibility, not that the complete order satisfies the global
   run-spectrum lower law or has only the displayed dangerous plateaux.

No computational check is used below.

## 2. Parameter audit

Let `a` be even and

\[
 K=\left\lfloor\frac{\varepsilon a}{2}\right\rfloor-1,
 \qquad
 t_j=\frac a2+K+1+j,
 \qquad
 r_j=\frac a2+j                                  \tag{2.1}
\]

for `1<=j<=K`.  For sufficiently large `a`, `K>=1`.  Since

\[
 2K+1\le\varepsilon a-1<a/2,                       \tag{2.2}
\]

we have `t_K<a`.  Direct subtraction gives

\[
\begin{aligned}
 t_j-r_j&=K+1>0,\\
 r_j-(a-t_j)&=K+1+2j>0,\\
 t_{j+1}-r_j&=K+2>0.                               \tag{2.3}
\end{aligned}

Thus

\[
                         a-t_j<r_j<t_j<t_{j+1}.     \tag{2.4}

All selected levels lie in

\[
 [a/2+K+2,a/2+2K+1]\subset(a/2,a).                \tag{2.5}

The edge cost of a full line at level `t_j` is

\[
 \lambda_j=2a-t_j
 =\frac{3a}{2}-K-1-j.                              \tag{2.6}

Its minimum occurs at `j=K`:

\[
 \lambda_K=\frac{3a}{2}-2K-1
 \ge(3/2-\varepsilon)a+1.                          \tag{2.7}

Its maximum is strictly below `3a/2`.  Therefore every displayed cost lies
in the claimed band, with slightly more room than the `O(1)` formulation.

## 3. Distinctness audit

### 3.1 Full lines

Parallel coordinate lines at distinct levels are disjoint.  An `x=t` line
and `y=u` line meet at `(t,u,-t-u)`, which lies in `H_a` only if
`t+u<=a` for positive `t,u`.  Every selected level exceeds `a/2`, so

\[
                         t_j+t_k>a.                 \tag{3.1}

Thus selected lines from different coordinate directions are also
disjoint.  The same calculation applies to the `x/z` and `y/z` pairs.

### 3.2 Separators versus lines

The separator coordinates other than `-a` lie in

\[
\begin{aligned}
 r_j&\in[a/2+1,a/2+K],\\
 a-r_j&\in[a/2-K,a/2-1].                            \tag{3.2}
\end{aligned}

The selected line levels begin at `a/2+K+2`.  Hence none of
`r_j,a-r_j,-a` equals a selected level, so no separator belongs to a
selected full line.

Within one separator type, `r_j` determines `j`, so the points are
distinct.  Across types, the coordinate equal to `-a` occurs in different
positions, while the other two coordinates are positive; two different
types therefore cannot coincide.

This proves that every point in the displayed packet occurs exactly once.

## 4. Six seam transitions, checked explicitly

Write `t=t_j`, `r=r_j`, and `t'=t_(j+1)`.  Put

\[
 d=t-r=K+1>0,
 \qquad e=r-(a-t)=K+1+2j>0,
 \qquad f=t'-r=K+2>0.                               \tag{4.1}

There are six directed edges around the three separator types.

### 4.1 `X_t -> R^z_j`

\[
 (t,a-t,-a)\longrightarrow(r,a-r,-a)               \tag{4.2}
\]

has coordinate difference

\[
                         (-d,+d,0).                 \tag{4.3}

### 4.2 `R^z_j -> Y_t`

\[
 (r,a-r,-a)\longrightarrow(a-t,t,-a)               \tag{4.4}
\]

has difference

\[
                         (-e,+e,0).                 \tag{4.5}

Thus across the complete `X|R^z|Y` seam, `x` decreases, `y` increases,
and `z=-a` is constant for three positions.

### 4.3 `Y_t -> R^x_j`

\[
 (-a,t,a-t)\longrightarrow(-a,r,a-r)               \tag{4.6}
\]

has difference

\[
                         (0,-d,+d).                 \tag{4.7}

### 4.4 `R^x_j -> Z_t`

\[
 (-a,r,a-r)\longrightarrow(-a,a-t,t)               \tag{4.8}
\]

has difference

\[
                         (0,-e,+e).                 \tag{4.9}

Thus across `Y|R^x|Z`, `y` decreases, `z` increases, and `x=-a` is
constant.

### 4.5 `Z_t -> R^y_j`

\[
 (a-t,-a,t)\longrightarrow(r,-a,a-r)               \tag{4.10}
\]

has difference

\[
                         (+e,0,-e).                 \tag{4.11}

### 4.6 `R^y_j -> X_(t')`

\[
 (r,-a,a-r)\longrightarrow(t',-a,a-t')             \tag{4.12}
\]

has difference

\[
                         (+f,0,-f).                 \tag{4.13}

Thus across `Z_t|R^y|X_(t')`, `x` increases, `z` decreases, and `y=-a`
is constant.

Inside the adjacent full blocks, the coordinate equal to `-a` rises to
`-a+1` on both sides of each three-position constant seam.  Hence every
such `-a` plateau is a strict local **minimum**, never a peak.

All other seam-coordinate changes in (4.3), (4.5), (4.7), (4.9), (4.11),
and (4.13) are strict.  This excludes hidden equal-value two-position
plateaux.

## 5. Peak maximality

Inside the blocks the sign patterns are

\[
 X:(0,+,-),\qquad Y:(-,0,+),\qquad Z:(+,-,0).      \tag{5.1}

For an interior `X_(t_j)` block, its preceding `R^y_(j-1)` has

\[
 r_{j-1}<t_j,
\]

and its following `R^z_j` has `r_j<t_j`.  For the first `X` block, the
reserved boundary point has `x=-a<t_1`.

A `Y_(t_j)` block has neighboring `y` values `a-r_j` and `r_j`, both less
than `t_j` by (2.4).  A `Z_(t_j)` block similarly has neighboring `z`
values `a-r_j<t_j`; the last block's reserved right neighbor has `z=-a`.

Therefore every displayed full line block is a maximal internal peak
plateau in its fixed coordinate.

The cross coordinates are strictly monotone inside each block.  Section 4
shows that they continue with the same monotonicity across separators.
Consequently, apart from possible `O(1)` effects at the two outer packet
seams, the complete set of internal peak plateaux of all three coordinate
words consists exactly of the displayed full line blocks.  There are no
hidden singleton peaks at a separator.

### Terminological correction

The sign pattern is the A pattern: the preceding fixed coordinate decreases
and the next fixed coordinate increases along each block.  But the direct
braid defines consecutive A blocks to be literally adjacent word intervals.
Here a separator lies between them.  Thus “transparent A-type handoff” is
accurate; “an A block to which the direct-adjacency lemma applies” is not.

## 6. Threshold-run audit

Let `R` be an internal maximal upper-threshold component of one scalar
coordinate word.  Choose a maximal constant plateau attaining the largest
coordinate value on `R`.  At either end inside the component, maximality
makes the neighboring value smaller.  At a component boundary, the outside
value is below threshold and hence below the maximum.  Thus `R` contains an
internal peak plateau.

If `R` lies wholly inside the clean bulk, Section 5 says this peak is one of
the displayed blocks.  Therefore

\[
 \lambda(R)\ge\lambda_K
 \ge(3/2-\varepsilon)a+1.                          \tag{6.1}

This proves the claimed absence of cheap **nonpeak** threshold components,
not merely the absence of cheap peak plateaux.

For a length-`L=4a+2` window lying wholly in the bulk, the universal peak
theorem additionally guarantees that at least one internal run exists
inside the window.  By (6.1), every such run has the long cost.  Removing
the two `L`-neighborhoods of the outer packet seams discards only `O(a)`
starts.

## 7. Mass calculation

There are `3K` blocks.  Summing (2.6),

\[
\begin{aligned}
 E
 &=3\sum_{j=1}^K
   \left(\frac{3a}{2}-K-1-j\right)\\
 &=3\left(\frac{3aK}{2}-K^2-K-\frac{K(K+1)}2\right)\\
 &=\frac92K(a-K-1).                                \tag{7.1}
\end{aligned}

Since `K=(epsilon/2+o(1))a`,

\[
 \frac{E}{a^2}
 =\frac94\varepsilon-\frac98\varepsilon^2+o(1).      \tag{7.2}

Each block contributes one more vertex than edge, and there are `3K-1`
internal separator positions.  Hence the packet has

\[
                         E+3K+(3K-1)=E+6K-1         \tag{7.3}

positions before the two optional boundary sentinels.  The linear term does
not affect density.  Dividing by

\[
                         M_a=3a^2+O(a)              \tag{7.4}

gives the stated limiting fraction

\[
                         \frac34\varepsilon
                         -\frac38\varepsilon^2>0.  \tag{7.5}

The mass and density coefficients in the source are correct.

## 8. Completion to a full permutation

The proposed sentinels

\[
                         B_L=(-a,0,a),
 \qquad B_R=(a,0,-a)                               \tag{8.1}

are points of `H_a`.  They are not on selected lines: selected fixed levels
lie strictly between `a/2` and `a`, while the sentinel coordinate values
relevant to `X,Y,Z` are `-a,0,a` in the wrong fixed-coordinate locations.
They also do not equal any separator, whose two non-`-a` coordinates lie in
the positive ranges (3.2).

Place all other unused points in an arbitrary prefix, followed by `B_L`,
the transparent packet, and `B_R`.  Every point of `H_a` then occurs once.
The immediate fixed-coordinate comparisons with `B_L,B_R` make the first
`X` and final `Z` blocks peaks.

The arbitrary prefix may create new dangerous plateaux and cheap runs.  It
can affect the packet's comparison ledger only at the single prefix/`B_L`
seam.  After deleting `O(L)=O(a)` nearby starts, the positive-density clean
bulk and all of Sections 4--7 remain unchanged.

Thus completion proves existence of a valid full order containing the
packet.  It does **not** prove:

* that the displayed blocks are all dangerous plateaux of the full order;
* that the full order meets the run-spectrum survivor condition;
* that its global first-dangerous profile is the scalar atom from
  `MULTISCALE_DANGEROUS_PROFILE.md`; or
* that multiple packets cover `1-o(1)` of `H_a` without resource conflict.

## 9. Corrected theorem ledger

**Proved:**

* exact point distinctness;
* all six seam sign identities;
* maximality and directedness of every displayed block;
* absence of every other interior peak plateau in the packet;
* absence of cheap internal threshold components in its clean bulk;
* total edge mass `(9/2)K(a-K-1)` and positive-density coefficient; and
* embedding as a positive-density interval of a full permutation.

**Terminology only:** the handoffs have A signs but are separated by one
point, so direct-adjacency A/B lemmas do not automatically apply.

**Not proved globally:** completion without additional dangerous plateaux,
global run-spectrum survival, or coexistence of enough transparent packets
to dominate the entire order.

The construction is a valid local geometric counterexample.  The remaining
obstruction must couple multiple packets or use the unused boundary mass;
it cannot come from a hidden error in the six local seam transitions.
