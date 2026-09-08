# Near-`3/2` transition geometry: a transparent rotating counterexample

## 1. Outcome

The proposed geometric obstruction is false in its local form.

For every fixed

\[
                         0<\varepsilon<1/2,          \tag{1.1}
\]

and all sufficiently large even `a`, there is an explicit subword of an
ordering of `H_a` containing `Theta_epsilon(a)` directed internal peak
plateaux with all of the following properties:

1. every plateau lies on a distinct central coordinate line;
2. its edge cost lies in

   \[
   [(3/2-\varepsilon)a,,(3/2+\varepsilon)a];        \tag{1.2}
   \]

3. consecutive plateaux are separated by exactly one word position;
4. the fixed coordinate directions rotate `x,y,z,x,y,z,...`;
5. every transition is a transparent A-type handoff; and
6. away from `O(1)` outer boundary positions, the only internal peak
   plateaux of any coordinate are the displayed long line blocks.

Consequently every full-word internal threshold run contained in the clean
bulk has cost at least

\[
                         (3/2-\varepsilon)a-O(1).    \tag{1.3}

Thus neither peak maximality, A/B signs, distinct central-line capacity,
nor `O(1)` gap size forces a cheap nonpeak threshold component.  The
construction occupies `Omega_epsilon(a^2)` positions, so it is genuinely
positive density.

This is a geometric strengthening of the scalar counterprofile in
`MULTISCALE_DANGEROUS_PROFILE.md`.  It does not prove that the resulting
full order is a survivor of the global run-spectrum inequality: the unused
points form a large prefix which may be cheaply serviced.  It proves
exactly that the near-`3/2` plateau packet itself cannot be eliminated by a
local transition theorem.

## 2. Parameters

Fix `epsilon` as in (1.1).  Let `a` be even and choose

\[
 K=\left\lfloor\frac{\varepsilon a}{2}\right\rfloor-1. \tag{2.1}
\]

For sufficiently large `a`, `K>=1`; also `2K+1<a/2`.  For
`1<=j<=K`, put

\[
 t_j=\frac a2+K+1+j,
 \qquad
 r_j=\frac a2+j.                                    \tag{2.2}

These numbers obey

\[
 a-t_j<r_j<t_j<t_{j+1},                             \tag{2.3}
\]

and

\[
 \frac a2<t_1<\cdots<t_K<a.                        \tag{2.4}

The offset `K+1` between the `r` and `t` ranges is deliberate.  It makes
all separator coordinates different from every selected line level.

## 3. Full directed line blocks

For a positive level `t`, define the full line blocks

\[
\begin{aligned}
 X_t&=((t,y,-t-y):-a\le y\le a-t),
       &&y\text{ increasing},\\
 Y_t&=((-t-z,t,z):-a\le z\le a-t),
       &&z\text{ increasing},\\
 Z_t&=((x,-t-x,t):-a\le x\le a-t),
       &&x\text{ increasing}.
\end{aligned}                                       \tag{3.1}

Each contains

\[
                         2a-t+1                     \tag{3.2}

points and has edge cost

\[
                         \lambda(t)=2a-t.           \tag{3.3}

Along `X_t`, the coordinate signs are

\[
                         (x,y,z)=(0,+,-),            \tag{3.4}

and `Y_t,Z_t` are its cyclic images.  Hence every block is directed.

For the levels (2.2),

\[
 \lambda_j:=2a-t_j
 =\frac{3a}{2}-K-1-j.                               \tag{3.5}

Since `1<=j<=K` and `2K+1<=epsilon*a+O(1)`,

\[
 (3/2-\varepsilon)a+O(1)
 \le\lambda_j<3a/2,                                \tag{3.6}

which is the required near-`3/2` band after absorbing rounding.

## 4. Transparent separator points

Insert

\[
\begin{aligned}
 R^z_j&=(r_j,a-r_j,-a),\\
 R^x_j&=(-a,r_j,a-r_j),\\
 R^y_j&=(r_j,-a,a-r_j).
\end{aligned}                                       \tag{4.1}

The clean word is

\[
 \begin{aligned}
 X_{t_1},R^z_1,Y_{t_1},R^x_1,Z_{t_1},R^y_1,
 X_{t_2},R^z_2,Y_{t_2},R^x_2,Z_{t_2},R^y_2,
 \ldots,
 X_{t_K},R^z_K,Y_{t_K},R^x_K,Z_{t_K},
 \end{aligned}                                      \tag{4.2}

where the final `R^y_K` is omitted.  Thus every two consecutive line
blocks have exactly one intervening position.

### 4.1 All displayed points are distinct

Parallel selected lines have different levels.  Lines from different
coordinate directions could intersect only if two selected positive
levels had sum at most `a`.  But (2.4) gives

\[
                         t_j+t_k>a,                 \tag{4.3}

so all `3K` full line blocks are pairwise disjoint.

The two positive coordinates of a separator are

\[
 r_j\in[a/2+1,a/2+K],
 \qquad
 a-r_j\in[a/2-K,a/2-1],                             \tag{4.4}

while every selected level lies in

\[
 [a/2+K+2,a/2+2K+1].                               \tag{4.5}

Hence no separator lies on a selected full line.  Separators of one type
are distinct because the `r_j` are distinct; separators of different types
put `-a` in different coordinates, while their other coordinates are
positive.  Thus (4.2) is a word of distinct points of `H_a`.

## 5. Exact transition signs

The endpoints of the full blocks are

\[
\begin{array}{c|c|c}
 &\text{first}&\text{last}\\ \hline
 X_t&(t,-a,a-t)&(t,a-t,-a)\\
 Y_t&(a-t,t,-a)&(-a,t,a-t)\\
 Z_t&(-a,a-t,t)&(a-t,-a,t).
\end{array}                                         \tag{5.1}

### 5.1 Same-level turns

At `X_(t_j)|R^z_j|Y_(t_j)`, the boundary triple is

\[
 (t_j,a-t_j,-a),
 (r_j,a-r_j,-a),
 (a-t_j,t_j,-a).                                   \tag{5.2}

By (2.3), `x` strictly decreases, `y` strictly increases, and `z=-a` is a
three-position constant plateau.  The neighboring values inside `X` and
`Y` are `-a+1`, so this `z` plateau is a strict local minimum, not a peak.

At `Y|R^x|Z`, the same statement holds after cyclically permuting the
coordinates: `y` decreases, `z` increases, and `x=-a` is a strict local
minimum.

### 5.2 Cross-level turns

At `Z_(t_j)|R^y_j|X_(t_(j+1))`, the varying coordinates satisfy

\[
 a-t_j<r_j<t_{j+1},                                 \tag{5.3}
\]

and

\[
 t_j>a-r_j>a-t_{j+1}.                               \tag{5.4}

The first inequality follows from (2.3).  The second is equivalent to
`r_j>a-t_j` and `r_j<t_(j+1)`, the same two facts.  Therefore `x` strictly
increases, `z` strictly decreases, and the three-position `y=-a` plateau
is a strict local minimum.

No separator creates a local maximum in any coordinate.

### 5.3 A-type interpretation

The fixed directions rotate

\[
                         x\to y\to z\to x.          \tag{5.5}

On every block, the preceding fixed coordinate decreases and the next
fixed coordinate increases.  Thus every displayed block has the A-type
sign pattern from the direct-braid analysis.  The separator merely
interpolates monotonically between its two boundary values; it introduces
no B-type reversal and no short peak.

The level ledger is also consistent with peak maximality.  Three adjacent
levels are all approximately `a/2`, so the A-turn capacity
`t_(j-1)+t_j+t_(j+1)` is approximately `3a/2`, exactly the scale of
`lambda_j`.  There is no level-sum contradiction to exploit.

## 6. Peak maximality and complete peak classification

Each `X_(t_j)` block is preceded and followed by positions whose
`x` coordinate is one of the `r` values and hence strictly below `t_j`.
Thus its full constant-`x` block is an internal peak plateau.  The same
argument applies cyclically to `Y_(t_j)` and `Z_(t_j)`.

Inside a line block, the two cross coordinates are strictly monotone, so
they create no interior peak.  Section 5 shows that across each separator
they continue monotonically, while the only new constant plateau is the
three-position `-a` local minimum.

Therefore, away from the two outer boundaries of (4.2), the complete list
of internal peak plateaux of all three coordinate words is

\[
             X_{t_j},Y_{t_j},Z_{t_j}quad(1\le j\le K). \tag{6.1}

This is stronger than merely verifying that the displayed blocks are
legal: it excludes hidden singleton or two-position seam peaks.

## 7. No cheap nonpeak threshold escape in the clean bulk

Every internal maximal upper-threshold component in a scalar word contains
an internal peak plateau.  Indeed, choose a maximal constant plateau on
which the component attains its largest value.  Its neighbors inside the
component are smaller by maximality; at an endpoint of the component, the
outside neighbor is below the threshold and hence also smaller.

Let `R` be any full-word internal threshold run lying wholly inside the
clean interior of (4.2), away from its two outer seams.  Its internal peak
plateau is one of (6.1).  Therefore

\[
 \lambda(R)\ge\min_j\lambda_j
 =\frac{3a}{2}-2K-1
 \ge(3/2-\varepsilon)a-O(1).                        \tag{7.1}

So the one-position gaps do not merely avoid creating cheap **peak** runs;
they avoid every cheap internal threshold component in the clean bulk.

In particular, for every start whose adjacent `L=4a+2` windows remain
inside the clean bulk, every avoiding run contained in either window has
cost at least the right side of (7.1).  Since the clean word has
`Theta_epsilon(a^2)` positions and only `O(a)` lie within distance `L` of
its outer boundaries, this applies at positive density.

## 8. Mass and density

There are

\[
                              3K=\Theta_\varepsilon(a) \tag{8.1}

displayed peak plateaux.  Their total edge mass is

\[
\begin{aligned}
 E
 &=3\sum_{j=1}^K
   \left(\frac{3a}{2}-K-1-j\right)\\
 &=\frac92K(a-K-1).                                  \tag{8.2}
\end{aligned}

With `K=(epsilon/2+o(1))a`,

\[
 \frac{E}{a^2}
 =\frac94\varepsilon-rac98\varepsilon^2+o(1)>0.  \tag{8.3}

The blocks are vertex-disjoint, and the separators add only `O(a)`
positions.  Hence their vertex union also has `Theta_epsilon(a^2)` size.
Relative to `M_a=3a^2+O(a)`, the clean packet occupies asymptotic fraction

\[
                         \frac34\varepsilon
                         -\frac38\varepsilon^2>0.   \tag{8.4}

Thus this is not a sparse seam curiosity.

## 9. Completion to a full ordering

Reserve one unused point with `x=-a` immediately before the first `X` block
and one unused point with `z=-a` immediately after the last `Z` block.
Such points exist outside the selected positive-level lines and separators.
They make the first and last displayed blocks strict peaks as well.

Place every other unused point of `H_a` in an arbitrary prefix, followed by
the first reserved point, the clean word (4.2), and the final reserved
point.  This is a full permutation of `H_a`.

The arbitrary prefix can create additional peaks and threshold runs, but it
cannot alter any local comparison inside the clean word except at the one
outer seam.  Discarding `O(L)=O(a)` positions near that seam leaves all
claims of Sections 5--7 intact.  Thus the positive-density packet is an
actual subword of a valid full ordering, not an abstract length profile.

For a completely explicit pair of boundary points one may use

\[
                         B_L=(-a,0,a),qquad
                         B_R=(a,0,-a),               \tag{9.1}

which are not on any selected line because all selected levels are strictly
between `a/2` and `a`.

## 10. What this resolves

The construction disproves each of the following possible local lemmas:

1. `Theta(a)` near-`3a/2` peak plateaux with `O(1)` gaps cannot occupy
   positive density.
2. Every A-type handoff between such plateaux creates a cheap peak.
3. Every short separator creates a cheap nonpeak upper-threshold component.
4. Distinct central-line capacities alone force a subquadratic total mass.

It does **not** disprove a global obstruction.  For fixed small `epsilon`,
the clean packet occupies only the fraction (8.4); the arbitrary prefix may
have a cheap run assignment, and the full order may fail the run-spectrum
necessary condition.  A global proof can still succeed by showing that a
survivor needs several such packets whose line resources or boundary
reservoirs cannot coexist.

The correct next question is therefore global:

> Can clean transparent packets on several disjoint level bands cover the
> `1-o(1)` fraction of the order required by a survivor, or must the resets
> between packets expose enough cheap threshold service?

The A/B transition calculus has no local contradiction at the
near-`3/2` scale; the transparent A-turn is an explicit equality-type
geometry.
