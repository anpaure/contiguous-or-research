# Owner-duplication obstruction for the paired-diamond conveyor

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The rank-isolated four-template coboundary in
`MATH_ATTACK_FOUR_TEMPLATE_ROTOR_COBBOUNDARY_20260725.md` is a valid
local switch.  Its packed two-carrier conveyor, however, cannot itself be
the coefficient-one near-cover asserted in the open statement
\((\mathrm{PPD}_Q)\).

For every useful two-step diamond, the two carrier states at its source
have the same lower block and collars which differ by one adjacent swap in
positions \(p,p+1\).  Their middle owners are therefore identical unless
\(p=Q\).  A conveyor cycle has \(Q\) useful blocks and one front-injection
block; the injection source is coalesced, and at most one useful source has
\(p=Q\).  Consequently at least \(Q\) of the \(Q+1\) block sources in
every complete conveyor cycle have identical middle owners in the two
selected paths, independently of every switch-bit choice.

Since every block uses two updates, a length-\(M\) paired conveyor has at
least

\[
 \left(\frac12-o(1)\right)M
\]

pairwise disjoint pairs of equal middle-owner occurrences.  Pairing all
but \(o(N_H)\) carriers therefore forces middle duplicate excess at least

\[
 \boxed{\left(\frac14-o(1)\right)MN_H
        =\left(\frac14-o(1)\right)W.}
\]

Thus the packed conveyor has a linear positivity defect before its useful
rank-isolated directions are optimized.  The local coboundary survives,
but a global construction must separate the two positive carrier paths at
their block sources.  This requires a different multi-template gadget
(for example an eight-template separated coboundary), not merely a choice
of the existing conveyor bits.

## 1. Equality of the source middle owners

At one useful block the two source quotient states have the form

\[
\begin{aligned}
 \omega_0&=(L;z_1,\ldots,z_{p-1},a,b,z_{p+2},\ldots,z_{2Q};R_0),\\
 \omega_1&=(L;z_1,\ldots,z_{p-1},b,a,z_{p+2},\ldots,z_{2Q};R_1).
\end{aligned}
\]

Their middle owners are the lower block together with the first \(Q\)
collar labels.  Hence

\[
 F_Q(\omega_0)=F_Q(\omega_1)
 \quad\Longleftrightarrow\quad p\ne Q.
 \tag{1.1}
\]

Indeed, if \(p<Q\), both \(a,b\) belong to the first \(Q\) positions; if
\(p>Q\), neither does.  Only the swap \(p=Q\) straddles the middle cut.

The front-swap injection starts from two coalesced quotient states, so its
source middle owners are also equal.  The switch bits act only on the two
arrival orders after the useful source has already been exposed.  Thus
none of these equalities depends on the bit assignment.

The isolated rank in Lemma 8.1 of the source note is

\[
 r=m-Q+p+1.
\]

Therefore the only forward paired-diamond source which can occur inside
an owner-simple selected family is the case

\[
 p=Q,\qquad r=m+1.
 \tag{1.2}
\]

At every other isolated rank, the two required positive carrier paths
already collide at their source middle owner.  In this precise sense the
four-template gadget is locally compatible with an owner near-packing at
only one forward rank.  A time-reversed or complemented gadget may give
the analogous lower first-shadow direction, but it does not supply the
whole growing band.

## 2. Count in one conveyor cycle

In the odd-position conveyor the useful positions are

\[
 p=1,3,\ldots,2Q-1.
\]

There are \(Q\) useful blocks and one injection block per cycle.  Among
the useful positions, at most one equals \(Q\).  Therefore at least
\(Q-1\) useful sources, together with the injection source, are common
middle owners.  This gives at least \(Q\) equal source pairs in every
\(Q+1\)-block cycle.  The even-position conveyor has the same bound.

Each block consumes two updates.  Apart from the initial and terminal
\(O(Q)\) remainder used in Theorem 8.3 of the source note, the number of
complete cycles is

\[
 \frac{M}{2(Q+1)}+O(1).
\]

Hence one paired conveyor contains at least

\[
 Q\left(\frac{M}{2(Q+1)}+O(1)\right)
 =\left(\frac12-o(1)\right)M
 \tag{2.1}
\]

disjoint pairs of equal middle-owner occurrences.  They are disjoint as
occurrence indices because different block sources are different time
positions in each of the two paths.

## 3. Equal occurrence pairs charge duplicate excess

For a selected path family let \(\mu(X)\) be the multiplicity of middle
owner \(X\), and put

\[
 D_0=\sum_X(\mu(X)-1)_+.
\]

Suppose \(J\) disjoint pairs of occurrence indices have been designated,
with the two occurrences in every pair carrying the same owner.  If
\(j_X\) designated pairs carry owner \(X\), then

\[
 2j_X\le\mu(X),
 \qquad
 (\mu(X)-1)_+\ge j_X.
\]

Summing gives the elementary but useful inequality

\[
 \boxed{D_0\ge J.}
 \tag{3.1}
\]

Now pair \(N_H-o(N_H)\) carrier tags and install the conveyor on every
pair.  There are \((N_H-o(N_H))/2\) carrier pairs.  Equations (2.1) and
(3.1) give

\[
\begin{aligned}
 D_0
 &\ge
 \frac{N_H-o(N_H)}2
 \left(\frac12-o(1)\right)M\\
 &=\left(\frac14-o(1)\right)MN_H.
\end{aligned}
\tag{3.2}
\]

At the calibrated crossing, \(MN_H=W-o(W)\), proving the stated linear
lower bound.

## 4. Exact boundary

This argument does not invalidate the isolated four-template identity.
It proves that its present dense packing uses a common-source architecture
which is incompatible with a middle near-packing.

The surviving local target is therefore:

> Construct a positive rank-isolated rotor coboundary whose two
> alternatives retain the four-mask incidence rectangle but whose selected
> carrier paths have distinct middle owners at all but \(o(M)\) block
> sources.

An eight-template second difference in an additional carrier-separation
coordinate is a natural candidate, but no such legal separated
coboundary is proved here.
