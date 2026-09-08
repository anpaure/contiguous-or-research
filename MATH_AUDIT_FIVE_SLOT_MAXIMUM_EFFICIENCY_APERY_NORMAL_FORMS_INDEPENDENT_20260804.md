# Independent audit: five-slot maximum-efficiency Apéry normal forms

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FIVE_SLOT_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md`  
**Audited theorem SHA-256:**
`2ba2be5a52e4761790f031fcc63955c8066fd032fc3afaa81de866b50abd9b9e`  
**Verdict:** **PASS.**  The availability filter, four efficiency branches,
all path counts, stabilization thresholds, and every explicitly listed
finite pulse are correct.  The additional size-two corollary in Section 8
below is also valid.  No computation or finite parameter search was used.

## 1. First-crossing scope and branch cover

If the first displayed value at least `A` occurred at index at most four,
first-crossing deletion would produce a prefix functional no larger than
the original one.  Complete positivity for grid size at most four would
make that prefix strictly positive.  Hence a nonpositive five-slot table
must satisfy

\[
                         c_1,c_2,c_3,c_4<A\le c_5.
\]

Internal superadditivity gives `c_2>=2c_1`, so size one cannot be the unique
maximum-efficiency generator.  At least one of `h=2,3,4,5` is a maximum;
the four branches cover all ties.

## 2. Availability-filtered Apéry identity

Fix a maximizing size `h`, put `lambda=c_h/h`, and give every denomination
`j` reduced weight

\[
                         d_j=c_j-j\lambda\le0.
\]

An exact fill of capacity `m` is a walk on `Z/hZ`.  If a residue repeats,
the intervening segment has ordinary capacity divisible by `h` and reduced
weight at most zero.  Deleting it therefore does not decrease reduced
weight.  Iteration leaves a simple path `Q` with

\[
                         \ell(Q)\le m.
\]

Conversely, every simple path ending at `m mod h` and satisfying
`ell(Q)<=m` can be padded by `(m-ell(Q))/h` size-`h` generators.  This is a
nonnegative integer, and the padding has zero reduced weight.  Thus

\[
 V_m=\lambda m+
 \max\{d(Q):Q\text{ simple},\ \ell(Q)\le m\}
\]

holds at every capacity.  Tied zero-weight cycles cause no exception:
deleting them preserves weight, and size-`h` padding restores capacity.

The path of `r<h` size-one steps proves nonemptiness and gives
`s_r>=r c_1>=0`; nonpositive reduced weights give
`s_r<=r lambda<h lambda=c_h`.

## 3. Stabilization thresholds and head lengths

A simple path on `h` residues has at most `h-1` edges.  The largest allowed
edge capacity is five for `h=2,3,4`, and four for `h=5`.  Hence the valid
uniform thresholds are

\[
                         (L_2,L_3,L_4,L_5)=(5,10,15,16).
\]

All simple witnesses are available at capacities at least `L_h`, so the
formal shifted lattice agrees termwise with the true clock there.  The
head correction over `0<=m<L_h` is therefore exact.  In particular, its
last indices are respectively `4,9,14,15`; there is no off-by-one error.

## 4. Size-two branch

Write `(c_1,...,c_5)=(x,y,z,w,T)` and suppose `y/2` is maximal.  Then

\[
 z\ge x+y,qquad T\ge y+z,qquad T\le5y/2,qquad
 2y\le w\le2y.
\]

Thus, with `s=T-2y`,

\[
                         x\le z-y\le s\le y/2,qquad w=2y.
\]

Modulo two, a simple nonzero-residue path consists of one odd edge.  The
size-five edge dominates size three and size one in reduced weight, but it
is unavailable before capacity five.  Therefore

\[
 V_1=x,qquad V_3=z,qquad V_{2q+1}=qy+s\quad(q\ge2),
\]

while every even value is `qy`.  Comparing capacities one and three with
the eventual odd lattice gives exactly

\[
 K(x)-K(s),qquad K(z)-K(y+s).
\]

No additional pulse exists.

## 5. Size-three branch

Put

\[
 p=c_3,qquad a=c_4-p,qquad b=c_5-p.
\]

Internal superadditivity and maximal efficiency give

\[
 c_1\le a\le p/3,qquad c_2\le b\le2p/3.
\]

Size four is the best residue-one edge and size five the best residue-two
edge.  The two simple path types in each residue yield exactly

\[
                         s_1=\max(a,2b-p),qquad
                         s_2=\max(b,2a).
\]

The double size-five witness has capacity ten; the double size-four
witness has capacity eight.  Before stabilization,

\[
 V_7=\max(p+c_4,c_5+c_2),qquad
 V_8=\max(2c_4,p+c_5).
\]

The latter already equals `2p+s_2`, so it creates no pulse.  The only
residue-one pulses occur at capacities `1,4,7`, and the only residue-two
pulses at `2,5`.  These are precisely the five corrections in the theorem.

## 6. Size-four branch

The size-five edge dominates the congruent size-one edge eventually because
`c_5>=c_4+c_1`.  Keeping the best edge in each nonzero residue, the simple
paths to a fixed target consist of one direct path, two one-intermediate
paths, and two orders through both intermediate vertices.  The one-
intermediate paths have equal weight in the relevant residue, leaving the
four distinct forms

\[
\begin{array}{c|l}
1&d_1,\ d_2+d_3,\ d_1+2d_2,\ 3d_3,\\
2&d_2,\ 2d_1,\ 2d_3,\ d_1+d_2+d_3,\\
3&d_3,\ d_1+d_2,\ 3d_1,\ 2d_2+d_3.
\end{array}
\]

Three size-five steps can have ordinary capacity fifteen, so the finite
head is exactly `m=0,...,14`.  The availability-filtered maximum still
contains the early size-one edge before size five becomes available; the
eventual dominance reduction does not erase that transient.

## 7. Size-five branch

For a fixed nonzero target in `Z/5Z`, a simple path is determined by an
ordered list of distinct intermediate vertices chosen from the other three
nonzero residues.  The number is

\[
                         1+3+3\cdot2+3\cdot2\cdot1=16.
\]

Every path has at most four edges of capacity at most four, so all paths
are available by capacity sixteen and the head is exactly
`m=0,...,15`.  Thus the theorem's four maxima of sixteen linear forms are
complete.

## 8. Follow-on size-two Gaussian gate

In first-crossing form on the size-two branch, `c_4=2y<A` and
`A<=T<=5y/2`.  Therefore

\[
                         {2A\over5}\le y<{A\over2}.
\]

For `s=T-2y`, the exact remaining interval is

\[
                         A-2y\le s\le y/2.
\]

Both transient corrections are nonnegative.  The first follows from
`x<=s<=y/2<A/4`.  For the second,

\[
                         z\le y+s\le3y/2<3A/4.
\]

The kernel is decreasing on `[0,3A/4]`.  Indeed, for `0<=t<=3/4`, the sign
of `-K'(At)` is the sign of

\[
 f(t)=\pi t-2\operatorname{arctanh}t.
\]

This function is concave, `f(0)=0`, and

\[
 f(3/4)=3\pi/4-\log7>9/4-2>0
\]

because `pi>3` and `e^2>7`.  Hence `f>=0` on the interval.  Consequently

\[
 K(x)-K(s)\ge0,qquad K(z)-K(y+s)\ge0.
\]

Thus the entire size-two branch reduces proof-safely to the single
two-lattice gate

\[
 \boxed{
 \mathcal L_2(y;s)>0,qquad
 {2A\over5}\le y<{A\over2},quad A-2y\le s\le y/2.
 }
\]

This gate is not signed by the audited theorem.

## 9. Scope

The normal forms are exact, but none of the remaining five-slot Gaussian
gates is proved positive here.  In particular, this audit does not prove
five-slot positivity, the all-grid Bellman inequality, or
`nu(k)<=B(k)+O(1)`.

**Final independent verdict: PASS.**
