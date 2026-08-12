# Independent audit of the four-box interleaving note

## 1. Verdict

The principal mathematical claims in
`FOUR_BOX_INTERLEAVING_RESEARCH.md` are correct.

In particular, this audit certifies all of the following as stated:

1. the exact one-sided depth defect

   \[
   D_{m,d}=\sum_{a=1}^{\min(d,m,2m-d)}
      \left(m+1-\left\lceil\frac{d+a}{2}\right\rceil\right)
      \left(m+2-\left\lceil\frac{d+a}{2}\right\rceil\right);
   \]

2. the fixed-depth estimates

   \[
   D_{m,d}=dm^2+O_d(m),\qquad
   \sum_{d=1}^D D_{m,d}=\frac{D(D+1)}2m^2+O_D(m);
   \]

3. the two-middle-point hull lemma and the resulting two-sided shadow
   sequence of length

   \[
   M_m+4\sum_{d=1}^D D_{m,d}
   =M_m+2D(D+1)m^2+O_D(m)
   \]

   for fixed `D`;

4. the radius-transfer identity;

5. the `4r-1`-term combined fan covering exactly the two `r^2` tail fibres
   associated with a fixed pair `(H,r)`;

6. the explicit all-depth two-sided shadow sequence of length

   \[
   \boxed{2m^3+5m^2+4m+1};
   \]

7. the counting obstruction showing that, in any middle-layer sequence of
   length `M_m+O(m^2)`, at least half of the old upper-tail targets have no
   witness shorter than `(1/8-o(1))m`.

The source note also correctly refuses to infer an OR-factor word or a bound
on `g_4` from these shadow statements.  That separation is essential: lower
points are produced as coordinatewise **meets** of middle points, whereas an
OR word must produce them as coordinatewise joins of suitable factor labels.

There is one interpretive overreach, rather than a false displayed theorem.
Proposition 7 rules out repair schemes in which all residual witnesses have
length `o(m)`.  It therefore rules out literal adjacent-pair repairs and any
notion of a bounded halo that bounds the **entire physical witness length**.
It does not, by itself, rule out every scheme described informally as a
"bounded halo": a window may extend only a bounded distance beyond a block
and still contain an entire block of length `Theta(m)`.  Similarly, the
two-point hull identities remain potentially useful as endpoints of shared
long windows; only realizing every identity as its own bounded two-point
gadget is excluded.  Lines 52--56 and 544--548 should be read with this
qualification.

Two small proof details should also be made explicit in a polished version:

* in Lemma 4, `P` is well-defined because
  `R=H-r+|q| >= |q|`, in addition to `0<=R<=H`;
* the equality of the upper and lower depth ledgers follows inside each
  imbalanced rectangle by replacing the lower-tail coordinate `b` by
  `2K-b`; it does not require the hook-chain decomposition itself to be
  complement invariant.

Neither omission affects the claims.

## 2. Line-by-line status map

| Source lines | Status | Audit |
|---|---|---|
| 5--12 | Correct | Inclusion--exclusion gives `M_m=((2m+3 choose 3)-4(m+2 choose 3))=(2m^3+6m^2+7m+3)/3`. |
| 14--50 | Correct summary | The fixed-depth coefficient includes both sides, and the all-depth length has asymptotic ratio `3` to `M_m`. |
| 52--56 | Correct only with a scope qualification | The proved obstruction is to uniformly `o(m)` witness lengths.  See Sections 7--8 below for what it does not exclude. |
| 58--59 | Correct and essential | No factor word, `g_4` bound, or Boolean OR construction follows. |
| 63--91 | Correct | The hook coordinates are bijective and have rank `m+p`. |
| 93--112 | Correct | Maxima and minima of intervals in the middle diagonal cover precisely the central square `|p|<=K` when `H>K`. |
| 116--148 | Correct | The displayed exact depth ledger and both fixed-parameter asymptotics are valid. |
| 150--205 | Correct | The variables `a`, `K`, and `delta` count each oriented tail point exactly once. |
| 207--208 | Correct asymptotically | For fixed `d` or `D`, `A=d` once `m` is sufficiently large. |
| 210--224 | Correct | Summing over depth gives the old exact one-sided defect; uniformly for `1<=D<=m/2` the partial sum is `Theta(m^2D^2)`. |
| 231--269 | Correct | The two-middle-point hull construction is coordinatewise and works through the extreme depths as well. |
| 271--300 | Correct shadow theorem | Each missed target gets a dedicated adjacent pair.  This is intentionally a sequence with repetitions, not a factorization. |
| 307--369 | Correct, with one omitted validity check | In addition to `0<=R<=H`, one needs and has `|q|<=R`, so `gamma_R(-q)` is defined. |
| 374--432 | Correct | Direct coordinate extrema prove both fan identities; `V_r=A_0` is the only required shared occurrence. |
| 434--448 | Correct | `(x,m-r+t)` parametrizes bijectively all square-hook points of radius `<r`. |
| 450--487 | Correct | Central squares and the two orientations of the fans partition the coverage task; the arithmetic gives exactly `2m^3+5m^2+4m+1`. |
| 489--492 | Correct as a research target | The fan gives endpoint compression, not packing into a near-Hamilton order. |
| 494--542 | Correct counting theorem | The exact short-interval count is even smaller than `nL`; the stated asymptotic constants follow. |
| 544--548 | Needs the scope qualification above | Only implementations forcing bounded physical witness length are excluded.  Long windows based on the same transfer identities are not excluded. |
| 550--589 | Correct | Both missing implications--near-width packing and OR-compatible factor/pinning--are accurately identified. |

## 3. Verification of the hook coordinates and central coverage

For `-H<=p<=H`,

\[
\gamma_H(p)=
\begin{cases}
(H+p,m-H),&p\le0,\\
(H,m-H+p),&p\ge0.
\end{cases}
\]

It is coordinatewise increasing in `p`, and its coordinate sum is `m+p`.
Given `(x,y) in [0,m]^2`, set

\[
H=\max(x,m-y),\qquad p=x+y-m.
\]

If `x<=m-y`, then `H=m-y`, `p<=0`, and
`gamma_H(p)=(x,y)`.  If `x>=m-y`, then `H=x`, `p>=0`, and the same identity
holds.  This also proves uniqueness.

Assume `H>K`.  For `-K<=s<=t<=K`, an interval of the middle diagonal has

\[
\bigvee_{u=s}^t T_{H,K}(u)
   =(\gamma_H(t),\gamma_K(-s)),
\]

and

\[
\bigwedge_{u=s}^t T_{H,K}(u)
   =(\gamma_H(s),\gamma_K(-t)).
\]

Thus a point `X(H,p;K,q)` with `|p|<=K` is obtained as a join when
`p+q>=0` (take `s=-q,t=p`) and as a meet when `p+q<=0` (take
`s=p,t=-q`).  Conversely every such interval has `|p|<=K`.  Since every
second-pair coordinate automatically has `|q|<=K`, this proves the exact
central-square statement.  The remaining `p>K` and `p<-K` regions have
strictly positive and strictly negative rank deviation respectively.

## 4. Verification of the exact depth ledger

For the orientation `H>K`, write `delta=H-K`.  An upper-tail point in local
chain coordinates is

\[
(H+K+a,b),\qquad 1\le a\le\delta,\quad0\le b\le2K,
\]

and has depth `d=a+b`.  Fixing `a` and `d` fixes `b=d-a`.  Such a point
exists precisely when

\[
K\ge K_0=\left\lceil\frac{d-a}{2}\right\rceil,
\qquad
a\le\delta\le m-K.
\]

For a fixed `K`, the second inequality gives `m-K-a+1` choices of `delta`.
The `K`-sum is nonempty exactly when

\[
1\le a\le d,\qquad a\le m,\qquad d+a\le2m.
\]

Hence `1<=a<=A=min(d,m,2m-d)`.  With

\[
n_a=m-a-K_0+1
    =m+1-\left\lceil\frac{d+a}{2}\right\rceil,
\]

the number for this orientation is

\[
\sum_{a=1}^A\frac{n_a(n_a+1)}2.
\]

Transposing the two coordinate pairs doubles it, proving (3.2).  There is
no missing contribution from balanced rectangles because they have no
tails.

For completeness, in the same rectangle a lower-tail point can be written

\[
(H-K-a,b),\qquad1\le a\le H-K,\quad0\le b\le2K,
\]

and its depth below the middle is `2K+a-b`.  The involution
`b -> 2K-b` changes this to `a+b`, proving equality of the upper and lower
depth distributions without appealing to a global complement symmetry.

For fixed `d`, eventually `A=d` and each `n_a=m+O_d(1)`, so
`D_{m,d}=dm^2+O_d(m)`.  Summing over fixed `1<=d<=D` yields (3.4).  If
`D<=m/2`, then for all `d<=D` one has `A=d` and

\[
m/2\le n_a\le m,
\]

up to harmless additive constants.  Summing `d` terms at depth `d` proves
the uniform `Theta(m^2D^2)` estimate.

Finally, summing by rectangles gives

\[
\sum_{d\ge1}D_{m,d}
=2\sum_{H=1}^m\sum_{K=0}^{H-1}(H-K)(2K+1)
=\frac{m(m+1)^2(m+2)}6.
\]

This independently verifies the complete ledger.

## 5. Verification of the hull lemma and fixed-depth theorem

Let `X=(x_1,x_2,x_3,x_4)` have rank `2m+d`.  Each coordinate-pair sum is
at least `d`, since the other pair has sum at most `2m`.  Decrement `d`
units using only the first pair to obtain one rank-`2m` point, and decrement
`d` units using only the second pair to obtain another.  The decrements have
disjoint coordinate support, so the join of the two resulting points is
exactly `X`.

For rank `2m-d`, apply the same argument to unused capacities and additions.
Each pair has at least `d` unused units, and adding in the two disjoint pairs
produces middle points whose meet is `X`.

The base diagonal concatenation contains every middle point once and
already represents all central-square targets by Section 3.  There are
`sum_{d<=D}D_{m,d}` missed targets on each side.  Appending two middle points
for each target therefore costs at most

\[
4\sum_{d=1}^D D_{m,d}.
\]

Every appended pair is itself a contiguous witness.  No seam property,
adjacency condition, or factorability assertion is used.  The fixed-depth
theorem follows exactly, including the coefficient in (4.5).

## 6. Verification of radius transfer and the fan

For Lemma 4, `r<=H`, `|q|<=K<r`, and

\[
R=H-r+|q|
\]

satisfy both `0<=R<=H` and `|q|<=R`; all four hook coordinates in (5.1) are
therefore defined.  If `p=r`, then

\[
\gamma_r(-r)=(0,m-r)\le\gamma_K(q),
\qquad
\gamma_R(-q)\le\gamma_H(r).
\]

One component of `P` and the complementary component of `Q` equal the
target components, so their join is the target.  For `p=-r`,

\[
\gamma_r(r)=(r,m)\ge\gamma_K(q),
\qquad
\gamma_R(-q)\ge\gamma_H(-r),
\]

and the same complementary equalities prove the meet identity.

Now order the upper fan as

\[
U_{r-1},U_{r-2},\ldots,U_0,V_1,V_2,\ldots,V_r.
\]

The interval `U_x,...,V_t` has first-pair parameter sequence that reaches
its unique maximum `r` at `U_0`.  Its second-pair first coordinate reaches
maximum `x` at the initial term, while its second coordinate reaches maximum
`m-r+t` at the final term.  Its maximum is therefore exactly (5.5).

Order the lower fan as

\[
A_0,A_1,\ldots,A_r,B_{r-1},B_{r-2},\ldots,B_1.
\]

The interval beginning at `A_x`, passing through `A_r`, and ending at `B_t`
(or at `A_r` when `t=r`) reaches first-pair minimum parameter `-r` at
`A_r`; its second-pair coordinate minima are `x` and `m-r+t`.  This proves
(5.7).  The equality `V_r=A_0` saves exactly one occurrence.

The map

\[
(x,t)\longmapsto(x,m-r+t),\qquad0\le x<r,\quad1\le t\le r,
\]

is a bijection onto the square points of hook radius

\[
\max(x,r-t)<r.
\]

Consequently a combined fan for `(H,r)` covers exactly all upper and lower
tail fibres with first hook radius `H`, first centered parameter `+r` or
`-r`, and second hook radius less than `r`.  Summing over `1<=r<=H<=m` and
then transposing covers every imbalanced rectangle exactly in the required
orientation.

The number of appended occurrences is

\[
2\sum_{H=1}^m\sum_{r=1}^H(4r-1)
=\frac{m(m+1)(4m+5)}3.
\]

Adding

\[
M_m=\frac{2m^3+6m^2+7m+3}{3}
\]

gives

\[
2m^3+5m^2+4m+1.
\]

Thus Theorem 6 and its exact length are certified.

The term "walk" here has the explicit definition in lines 231--234: it is a
sequence whose interval extrema cover the desired targets.  The theorem
does not assert that arbitrary seams between separately concatenated blocks
are Johnson edges.

## 7. Verification and exact scope of the linear-window obstruction

There are

\[
E_m=\frac{m(m+1)^2(m+2)}6
   =(1/6+o(1))m^4
\]

old upper-tail targets.  A sequence of length `n` has exactly

\[
\sum_{\ell=1}^{\min(L,n)}(n-\ell+1)
\]

intervals of length at most `L`, which is at most `nL`.  One interval has
one maximum, so distinct tail targets require distinct witnessing intervals.
This proves `nL>=E_m`.

If `n=M_m+O(m^2)=(2/3+o(1))m^3`, then

\[
\frac{E_m}{n}=(1/4-o(1))m,
\]

which proves (6.3).  Likewise fewer than `E_m/2` distinct target values can
be attained by intervals shorter than `E_m/(2n)`, so at least half the
targets have no witness below

\[
\frac{E_m}{2n}=(1/8-o(1))m.
\]

The cross-rectangle assertion is also correct, but benefits from one extra
sentence.  The middle points in a hook rectangle are exactly its central
diagonal.  In an imbalanced target rectangle, no subset of those middle
points can attain a tail coordinate beyond the central diagonal's coordinate
range.  Points contained in any single different rectangle have their join
in that different product of two chains.  Hence every witness of an old tail
must contain occurrences from at least two hook rectangles.

What the proposition proves is a lower bound on **physical interval
length**.  It excludes bounded-length adjacent seam gadgets.  It does not
prove that a witness cannot use a long suffix and prefix of one or two blocks,
nor that a fixed number of block interfaces is insufficient when the blocks
themselves have length `Theta(m)`.  Those stronger conclusions would require
an additional incidence or capacity argument.

## 8. No OR-word consequence

The all-depth fan sequence has

\[
2m^3+5m^2+4m+1=(3+o(1))M_m
\]

middle occurrences.  It is not near-width.  More importantly, its lower
targets are interval meets of middle points.  A Boolean OR factor would need
an array below the selected middle witnesses whose interval joins realize
those same lower targets while preserving the middle and upper witnesses.
That is an independent variable-band factorization and coordinate-pinning
problem.

Therefore the strongest audited conclusions are exactly:

* a correct fixed-depth two-sided **shadow** theorem at surface cost;
* a correct all-depth two-sided **shadow** theorem at length `(3+o(1))M_m`;
* a correct `Omega(m)` physical-witness-length obstruction at near width;
* no new upper bound on `g_4` and no new universal contiguous-OR array.
