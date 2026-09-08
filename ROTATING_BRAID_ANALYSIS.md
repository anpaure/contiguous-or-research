# The rotating long-line braid: an exact transition obstruction

## 1. Outcome

Work in

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                   \ |x|,|y|,|z|\le a\},
 \qquad M_a=3a^2+3a+1.
\]

The remaining geometry in `UNIVERSAL_CAPPED_RUN_COVER.md` was described as
a rotating braid of long directed constant-coordinate peak plateaux.  This
note proves that the most literal version of that geometry cannot be the
whole obstruction.

Call the cost of a plateau with `s` positions `lambda=s-1`.  In a **direct
rotating braid**, consecutive peak plateaux are adjacent in the word and
their fixed coordinates rotate

\[
                     x,y,z,x,y,z,\ldots .             \tag{1.1}
\]

Every plateau is assumed directed: either cross-coordinate is strictly
monotone along it.  The braid is **clean at scale `q`** if no join of two
successive displayed plateaux creates a peak plateau of cost at most `q`.

### Theorem 1 (pure rotating-braid defect)

Let `P_1,...,P_m` be a direct rotating braid in an ordering of `H_a`, clean
at scale `floor(4a/3)`, and suppose

\[
                         \lambda(P_j)>\frac{4a}{3}
                                                               \tag{1.2}
\]

for every `j`.  Then

\[
 \boxed{
       \sum_{j=1}^m\lambda(P_j)
          \le \left(\frac{287}{96}+o(1)\right)a^2.}
                                                               \tag{1.3}
\]

The error in (1.3) is `O(a)`.  Since

\[
             \frac{287}{96}=3-\frac1{96},             \tag{1.4}
\]

such plateaux leave at least

\[
                         \frac1{96}a^2-O(a)            \tag{1.5}
\]

ordering edges outside them.  In particular, no direct rotating braid of
`(4/3)a`-long clean plateaux can occupy all but `o(a^2)` positions of
`H_a`.  Its maximum possible vertex density is at most

\[
                         \frac{287}{288}+o(1).         \tag{1.6}
\]

The estimate has genuine constant room.  Replacing `4/3` in (1.2) by
`4/3-1/1000` still gives

\[
        \sum_j\lambda(P_j)
             \le (3-1/200)a^2+O(a).                  \tag{1.7}
\]

Thus the conclusion is not an artefact of requiring a strict endpoint
constant.

This closes the **pure direct braid**, but not the arbitrary interleaved
case.  Gaps of peak-free points, reversals of the direction rotation, and
backtracking coordinate patterns are not covered by Theorem 1.  Moreover,
(1.5) alone does not prove a `(4-epsilon)a^3` weighted capped-run bound:
one long peak can service `Theta(a)` forward windows.  Section 7 makes this
remaining gap explicit.

## 2. Directed blocks and the two turn types

Write `c_j` for the fixed coordinate of `P_j` and `t_j` for its fixed
value.  Indices in this section are internal, so that `P_(j-1)` and
`P_(j+1)` exist.  Put

\[
                         p=c_{j-1},\qquad n=c_{j+1}.
\]

Because of (1.1), `p,c_j,n` are the three different coordinates.  On
`P_j`, the two cross-coordinates `p,n` sum to `-t_j`; directedness says
that one strictly increases and the other strictly decreases.

There are two types.

* `P_j` has **type A** when `p` decreases and `n` increases.
* `P_j` has **type B** when `p` increases and `n` decreases.

Type A is the outward turn seen in the standard triangular rotation.  Type
B points both cross-coordinate slopes into valleys at the two joins.  A
single type B turn is legal; two consecutive type B turns are not.

### Lemma 2 (two B turns create a short peak)

If `P_j` and `P_(j+1)` both have type B, their join contains a peak plateau
of cost zero or one in the third coordinate `c_(j-1)=c_(j+2)`.

#### Proof

Let `e=c_(j-1)=c_(j+2)`.  On the final part of `P_j`, type B makes `e`
strictly increase.  On the initial part of `P_(j+1)`, type B makes `e`
strictly decrease.  Let `u` and `v` be the values of `e` at the last point
of `P_j` and the first point of `P_(j+1)`.

If `u>v`, the last point of `P_j` is a singleton strict local maximum of
`e`.  If `v>u`, the first point of `P_(j+1)` is such a maximum.  If `u=v`,
the two boundary points form a two-position peak plateau.  The costs are
respectively zero, zero, and one.  \(\square\)

Consequently the B positions form an independent set in the block path,
up to the two harmless outer boundary blocks.  If `A` and `B` denote the
numbers of the two types, then

\[
                              B\le A+1.               \tag{2.1}
\]

### Lemma 3 (the A-turn level inequality)

Every internal type A block satisfies

\[
       \boxed{\lambda(P_j)\le t_{j-1}+t_j+t_{j+1}-2.} \tag{2.2}
\]

#### Proof

Let `F,L` be the first and last points of `P_j`.  Since `P_(j-1)` is a
peak plateau and is immediately followed by `F`,

\[
                         p(F)\le t_{j-1}-1.           \tag{2.3}
\]

Similarly, since `P_(j+1)` is a peak plateau immediately preceded by `L`,

\[
                         n(L)\le t_{j+1}-1.           \tag{2.4}
\]

For a type A block, `n` strictly increases at each of its
`lambda(P_j)` ordering edges.  Its values are integral, so

\[
 n(L)-n(F)\ge\lambda(P_j).                            \tag{2.5}
\]

But `p(F)+n(F)=-t_j`.  Hence

\[
\begin{aligned}
 \lambda(P_j)
   &\le p(F)+n(L)+t_j\\
   &\le t_{j-1}+t_j+t_{j+1}-2,
\end{aligned}
\]

as required.  \(\square\)

This is the transition constraint absent from a raw line-capacity count.
It says that every outward long turn must be paid for by the three adjacent
fixed-coordinate levels.

## 3. Line capacities and level multiplicity

The coordinate line `c=t` contains exactly

\[
                             2a+1-|t|                \tag{3.1}
\]

points.  A plateau on that line therefore has

\[
                             \lambda\le2a-|t|.       \tag{3.2}
\]

Under (1.2), (3.2) gives

\[
                             |t|<\frac{2a}{3}.       \tag{3.3}
\]

There cannot be two displayed long plateaux on one fixed coordinate line:
their disjoint vertex sets would contain more than `8a/3` points in a line
of at most `2a+1` points.  Thus every integer level in (3.3) occurs at most
once in each of the three coordinate directions, and at most three times
in the pooled level multiset.

Peak edge sets are disjoint, so

\[
                        \sum_j\lambda(P_j)\le M_a-1. \tag{3.4}
\]

Together with (1.2), this bounds the number of blocks by

\[
                              m\le\frac94a+O(1).      \tag{3.5}
\]

## 4. The weighted level ledger

Discarding the first and last block changes all forthcoming estimates by
only `O(a)`.  For an internal block position `j`, define

\[
 d_j=\#\{r\in\{j-1,j,j+1\}:P_r\text{ has type A}\}. \tag{4.1}
\]

Sum Lemma 3 over all A blocks and use (3.2) on every B block.  Since every
internal B block has two A neighbours by Lemma 2,

\[
\begin{aligned}
 \sum_j\lambda(P_j)
 &\le \sum_jd_jt_j
       +\sum_{j\in B}(2a-|t_j|)+O(a)\\
 &=2aB+\sum_{j\in A}d_jt_j
       +\sum_{j\in B}(2t_j-|t_j|)+O(a)\\
 &\le2aB+\sum_{j\in A}d_jt_j
       +\sum_{j\in B}t_j+O(a).                      \tag{4.2}
\end{aligned}
\]

Here the harmless negative term `-2A` from (2.2) was discarded.  The
second line uses the two appearances of each B level in the sum of adjacent
A inequalities.  The last inequality uses

\[
                         2t-|t|\le t                 \tag{4.3}
\]

for every real `t`.

The A weights lie in `[1,3]`.  Counting each A indicator in the three
neighbourhoods which contain it gives

\[
                   \sum_{j\in A}d_j=3A-2B+O(1).     \tag{4.4}
\]

Among `A` numbers in `[1,3]` with this sum, the vector

\[
       \underbrace{3,\ldots,3}_{A-B},
       \underbrace{1,\ldots,1}_{B}                  \tag{4.5}
\]

majorizes every other possibility, up to `O(1)` boundary entries.  Adding
the `B` level terms from (4.2), the weighted level sum is therefore at most
the following relaxed extremum:

* give weight three to `A-B` levels;
* give weight one to `2B` further levels;
* choose all levels from a multiset in which each integer
  `|t|<2a/3` has multiplicity three.

Let `S_a(r)` be the sum of the `r` largest entries of that pooled multiset.
Uniformly for `r=O(a)`, direct summation gives

\[
             S_a(r)=\frac{2a}{3}r-\frac{r^2}{6}+O(a). \tag{4.6}
\]

The rearrangement inequality and (4.5) now turn (4.2) into

\[
 \sum_j\lambda(P_j)
 \le2aB+2S_a(A-B)+S_a(A+B)+O(a).                    \tag{4.7}
\]

This one-dimensional expression contains the entire braid obstruction.

## 5. Optimization and the constant `287/96`

Put

\[
                         A=\alpha a,qquad B=\beta a.
\]

Equations (2.1) and (3.5) give, up to vanishing errors,

\[
       0\le\beta\le\alpha,\qquad \alpha+\beta\le\frac94. \tag{5.1}

\]

Substituting (4.6) into (4.7) gives

\[
 {1\over a^2}\sum_j\lambda(P_j)
 \le F(\alpha,\beta)+o(1),                           \tag{5.2}

\]

where

\[
 F(\alpha,\beta)
 =2\alpha+\frac43\beta-\frac12\alpha^2
      +\frac13\alpha\beta-\frac12\beta^2.           \tag{5.3}

\]

It is useful to put `s=alpha+beta`.  Then

\[
 F=2s-\frac12s^2
      +\left(\frac43s-\frac23\right)\beta
      -\frac43\beta^2.                              \tag{5.4}

\]

For fixed `s>1/2`, the maximum occurs at

\[
                         \beta=\frac{s}{2}-\frac14. \tag{5.5}

\]

The resulting maximum is increasing for `s<=9/4`, so (5.1) makes
`s=9/4`.  Thus

\[
             \beta=\frac78,qquad \alpha=\frac{11}{8}, \tag{5.6}

\]

and

\[
 \max F
   =\frac{63}{32}+\frac{49}{48}
   =\boxed{\frac{287}{96}}.                          \tag{5.7}

\]

This proves Theorem 1.

For completeness, use a general long threshold `lambda>=ca`, with `c`
near `4/3`.  Then the allowed level half-width is `(2-c)a+O(1)` and the
block-count bound is `(3/c)a+O(1)`.  The same calculation has maximum

\[
 \Phi(c)=\frac{18}{c}-9-\frac{9}{2c^2}
     +\frac3{16}\left(4c+\frac4c-6\right)^2.         \tag{5.8}

\]

At `c=4/3`, this is `287/96`.  Direct substitution at
`c=4/3-1/1000` gives

\[
                         \Phi(c)<2.9944<3-\frac1{200}, \tag{5.9}

\]

which proves (1.7).

The same proof permits several braid components.  If the critical
plateaux split into \(r\) direct rotating components, discard the two end
blocks of every component.  This changes the edge sum and the weighted
level ledger by \(O(ar)\), while line-level multiplicity remains global.
Therefore the proved multi-component form is

\[
 \sum_{P\ {\rm critical}}\lambda(P)
 \le\frac{287}{96}a^2+O(ar+a)                       \tag{5.10}
\]

at threshold \(4a/3\), and

\[
 \sum_{P\ {\rm critical}}\lambda(P)
 \le\left(3-\frac1{200}\right)a^2+O(ar+a)           \tag{5.11}
\]

at threshold \((4/3-1/1000)a\).  In particular, a bounded or sublinear
number of transition gadgets cannot erase the quadratic edge defect.

## 6. Top-line constraints and the explicit density counterexample

The top lines already show why a completely peak-free braid is impossible.

### Lemma 4 (one short top peak is unavoidable)

Every linear ordering of `H_a` contains an internal peak plateau of cost at
most `a` among the three top coordinate lines `x=a`, `y=a`, `z=a`.

#### Proof

Each top line has `a+1` points.  Every maximal block of its occurrences
which meets neither word endpoint is automatically a peak, because no
higher coordinate value exists.  If one top line has no internal block,
all its occurrences must be contained in its prefix and suffix blocks, so
it uses at least one of the two word endpoints.  The three top lines are
pairwise disjoint, and one endpoint cannot belong to two of them.  Hence at
most two top lines can avoid an internal block.  The remaining line has an
internal peak block containing at most `a+1` positions, of cost at most
`a`.  \(\square\)

This lemma yields only `O(a)` cheap forward windows, not a positive density.
That limitation is real.  `SHORT_PEAK_DENSITY.md` gives an explicit
search-free order with a clean rotating suffix of full high lines

\[
                    X_t\Vert Y_t\Vert Z_t,
 \qquad t>a/2,                                      \tag{6.1}

\]

for which at most `3/8+O(1/a)` of the length-`(4a+2)` windows contain a
threshold run of cost at most `a`.  The proof and its exact count have been
independently checked:

\[
 |B_a|=\frac{15}{8}a^2+O(a),\qquad
 |H_a\setminus B_a|=\frac98a^2+O(a).                \tag{6.2}

\]

At every join in (6.1), the third coordinate forms a two-position plateau
at its global minimum `-a`; it is a valley, not a peak.  This is exactly
the A-turn geometry of Lemma 3.  Thus the proposed `2/3+eta` short-window
density lemma is false, even though the more demanding `(4/3)a` pure braid
is obstructed by Theorem 1.

The obvious weighted assignment on this counterexample still does not beat
the critical constant.  On the clean suffix, assign a position in one full
line block to the next complete line block.  Up to a boundary cost of order
$a^2$, its total charge is

\[
 3\sum_{t=a/2+O(1)}^{a-1}(2a+1-t)(2a-t)
       =\frac{19}{8}a^3+O(a^2).                     \tag{6.3}
\]

Using only the universal cost $2a$ on the arbitrary complement prefix adds
at most

\[
 2a\left(\frac98a^2+O(a)\right)
       =\frac94a^3+O(a^2).                          \tag{6.4}
\]

The resulting bound is $37a^3/8+O(a^2)$, which is larger than
$4a^3$.  This is not a lower bound on the optimum assignment; it simply
confirms that the weighted problem is genuinely still open after the density
counterexample.

## 7. What the theorem does not yet imply

For a peak plateau `P=[u,v]` of cost `lambda`, the forward windows of
length `L=4a+2` which can use it have start indices

\[
                       v-L\le i\le u-1.              \tag{7.1}

\]

There are `L-lambda` such starts.  Hence a single long plateau still
services `Theta(a)` windows.  The edge defect (1.5) does **not** imply that
a positive density of forward windows has a short available peak: service
intervals of the remaining long peaks may overlap and cover the defect.

Nor does every survivor have to be a direct braid.  Between two long
plateaux it may insert a peak-free valley segment of length up to `4a+1`;
it may backtrack from `x` to `y` to `x`; or it may switch the cyclic
orientation after a nontrivial transition gadget.  Lemmas 2 and 3 use
adjacency and the fixed three-cycle essentially.

Accordingly, the rigorous ledger is now:

* the binary short-window density route is false (`SHORT_PEAK_DENSITY.md`);
* a clean direct braid at the critical `4a/3` scale loses a fixed fraction
  of the order (Theorem 1);
* this fixed edge defect alone does not prove
  `sum_i q_i <=(4-epsilon)a^3`; and
* the remaining mathematical target is a **transition-gadget theorem**:
  either compress every peak-free gap into a generalized A/B turn while
  retaining a level inequality, or show that the gap itself supplies
  enough short non-peak threshold components to lower the weighted cost.

The most useful next inequality would be a gap version of Lemma 3.  If a
transition from a `c_(j-1)` plateau to a `c_j` plateau and then to a
`c_(j+1)` plateau uses `g_j` intervening positions, one needs a bound of
the schematic form

\[
 \lambda(P_j)
   \le t_{j-1}+t_j+t_{j+1}+O(g_{j-1}+g_j),          \tag{7.2}

\]

together with a proof that a large total gap term itself yields a cheap
heterogeneous threshold-run cover.  The direct case proved here is exactly
`g_j=0`.  Establishing this dichotomy would convert the structural
`1/288` defect into the desired weighted saving.

The bare additive gap estimate just displayed should not itself be treated
as a conjecture: ordering steps may jump by \(2a\), so a one-point gap can
reset a coordinate by order \(a\).  The correct quantitative target is a
disjunction which charges such a reset as a cheap threshold component.

Fix

\[
                         c=\frac43-\frac1{1000}.     \tag{7.3}
\]

In an arbitrary order, take all directed peak plateaux of cost at least
\(ca\), join adjacent ones whenever their coordinates continue one fixed
three-cycle and their join is clean, and let \(r\) be the number of
resulting maximal direct components.  Put

\[
 G=M_a-1-\sum_{P\ {\rm critical}}\lambda(P),         \tag{7.4}
\]

the number of ordering edges outside the critical plateaux.  A sufficient
**gap-compression/cheap-gap lemma** is the existence of absolute constants
\(\gamma,C>0\) and a heterogeneous internal-run assignment, with \(O(a)\)
congestion and \(O(a)\) omitted indices, satisfying

\[
 \sum_i\min(\lambda_i,3a-1)
 \le4a^3-\gamma aG-\gamma a^2r+Ca^2.                \tag{7.5}
\]

This is strictly a proposed lemma, not a result proved here.  It is
quantitatively sufficient.  Indeed (5.11) gives, for an absolute \(C_0\),

\[
             G\ge\frac1{200}a^2-C_0ar-O(a).          \tag{7.6}
\]

If \(r\le a/(400C_0)\), then \(G\ge a^2/400-O(a)\), and the first saving
term in (7.5) is cubic.  If \(r>a/(400C_0)\), the second saving term is
cubic.  Either case would give

\[
       \sum_i\min(\lambda_i,3a-1)
              \le(4-\varepsilon)a^3+O(a^2)          \tag{7.7}
\]

for an absolute \(\varepsilon>0\), completing the fan-capped obstruction.

The local content required for (7.5) is now precise.  A nontrivial gap must
either be compressible into a generalized A turn retaining a level charge,
or supply a short threshold component whose service interval has length
\(\Theta(a)\); the selected service intervals must have bounded overlap.
That is the exact transition/top-line theorem still missing.
