# Literal four-slab rectangles: spectator flatness and frame-defect capacity

Date: 2026-07-26

This is a conditional audit of the claimed diverse compiler.  It uses only
coordinate-disjoint packet geometry, packet trace injectivity, and the
doubled-permutation direction count.  It does not repair the separately
recorded physical trace-decoder gap.

## 1. Literal traces of one physical orientation cube

Write a physical packet as

\[
\mathcal Q(F,E;D),
\]

where every element of (F) is fixed present, every element of (E) is
fixed absent, and (D) is a matching of active two-element swap pairs.  An
owner contains exactly one endpoint of every pair in (D).

For a directed isometric window with direction support (J\subseteq D),
the literal traces have the exact form

\[
\begin{aligned}
T^-(J)&=F\ \dot\cup\
 \{\text{the unchanged selected endpoint of }d:d\in D\setminus J\},\\
T^+(J)&=F\ \dot\cup\
 \bigcup_{d\in J}d\ \dot\cup\
 \{\text{the unchanged selected endpoint of }d:d\in D\setminus J\}.
\end{aligned}
\tag{1.1}
\]

In particular, a ground coordinate fixed present or fixed absent remains
visible with that value in both signs and at every depth.

## 2. Same-frame rectangles are exactly flat

Two axis-aligned subcubes of one common orientation cube are disjoint if and
only if some orientation coordinate is inactive in both and is fixed to
opposite endpoints.  By (1.1), that spectator endpoint remains visible in
every signed target.

### Theorem 2.1 (spectator separation)

Let (mathcal S_1,\ldots,\mathcal S_k) be pairwise owner-disjoint physical
slabs which are faces of one common orientation-cube frame.  For arbitrary
legal resolutions and arbitrary compiler options on those slabs,

\[
I_{mathcal S_i,q}^{\epsilon}
 \cap I_{mathcal S_j,q}^{\epsilon}=\varnothing
\qquad(i\ne j,\ q<R,\ \epsilon\in\{-,+\}).
\tag{2.1}
\]

Consequently their one-sided compound derivative is additive:

\[
\Delta\mathcal R(S)=\sum_{t\in S}\Delta\mathcal R(\{t\}).
\tag{2.2}
\]

In particular, no four-slab rectangle contained in one fixed physical frame
can be correcting when all four single-slab derivatives are nonnegative.

#### Proof

For any two disjoint faces, choose a common inactive orientation coordinate
on which their fixed bits disagree.  Every owner trajectory in either face
leaves that coordinate untouched.  Formula (1.1) puts opposite literal
endpoints in all of their lower and upper targets, proving (2.1).  Derivative
supports of distinct slabs are therefore disjoint, so the threshold
holonomy terms in the one-sided compound formula vanish, proving (2.2).
\(\square\)

This includes the canonical minimal construction
(Q_R\times\{	ext{four disjoint edges of }Q_3\}), for every perfect
matching of the residual (Q_3), not only the parallel matching.

## 3. The exact cross-frame overlap diagnostic

The only possible escape is to use different physical pair frames.  Encode
one packet by the affine Boolean constraints

\[
x_u=1\ (u\in F),\qquad x_u=0\ (u\in E),\qquad
x_u\oplus x_v=1\ (uv\in D).
\tag{3.1}
\]

For two packets, the union of their active matchings has maximum degree two,
so every component is an alternating path or an even alternating cycle.
If there is no direct fixed-coordinate conflict, the two owner cubes are
disjoint precisely when some alternating path has pinned endpoints whose
required parity disagrees with the parity of its length.  Call such a path a
**frame-defect path**.

In a signed trace, varying an active edge replaces its parity-one constraint
by the parity-zero constraint that both endpoints are absent (lower sign) or
both are present (upper sign).  Hence:

### Theorem 3.1 (defect-path transversal law)

If one literal signed target occurs in two owner-disjoint packets with no
direct pin conflict, then the union of their two window supports meets every
frame-defect path in an odd number of edges.  In particular it meets each
such path at least once.

#### Proof

Along a defect path, the unvaried parity-one edge constraints force the
endpoint xor to equal the path length modulo two, contrary to the pins.
Every varied edge changes one parity-one equation to parity zero.  Equality
of the two literal targets supplies one common Boolean assignment satisfying
the modified equations.  Its endpoint parity can agree with the pins only
if an odd number of path equations were changed. \(\square\)

This is the exact distinction between the flat and potentially correcting
cases.  Same-frame disjointness has a length-zero spectator conflict, which
no window can repair.  Cross-parent overlap requires an interlaced matching
frame with a positive-length defect path.

## 4. Quantitative capacity of a bounded rectangle

One packet contains (s=2^R) starts and (s/(2R)) doubled-permutation
cycles.  For (q<R), a fixed physical direction lies in exactly

\[
{qs\over R}
\tag{4.1}
\]

directed depth-(q) windows.  Trace injectivity allows occurrences and
targets to be counted identically.

Let two aggregate slab resolutions each consist of two packets.  Suppose
every relevant packet pair has a frame-defect path of length at most
(\ell).  Theorem 3.1 and a union bound over the directions of one such path
give

\[
\boxed{
|I_{t,q}^{\epsilon}\cap I_{u,q}^{\epsilon}|
 \le {8\ell q s\over R}.
}
\tag{4.2}
\]

The constant (8) only records two sides on which the first varied path
edge may occur and the four packet pairs; no asymptotic sharpness is
claimed.

For four slab moves, every nonadditive term in the exact threshold holonomy
contains a target touched by at least two slab derivatives.  Charge it to
one such slab pair and expand each derivative support into its old and new
resolution images.  Equations (4.2) and the six slab pairs imply

\[
\boxed{
\left|
 \Delta\mathcal R(S)-\sum_{t\in S}\Delta\mathcal R(\{t\})
\right|
 \le C{\ell q s\over R}
}
\tag{4.3}
\]

for an absolute constant (C).

Therefore a four-slab rectangle whose four single moves are nonimproving can
improve the hole count by at most (C\ell qs/R) at one signed depth.  A
pairwise owner-disjoint packing has at most (W/(8s)) such rectangles, so
its total possible correction is at most

\[
\boxed{
O\!\left({\ell q\over R}W\right).
}
\tag{4.4}
\]

For every bounded-frame rectangle ((\ell=O(1))) and every protected
(q=o(R)), this is (o(W)).  Such rectangles cannot repair a linear
missing-target defect.  Linear correction at depth (q) requires

\[
\ell=\Omega(R/q),
\tag{4.5}
\]

or a non-disjoint/nonlocal compound mechanism not covered by four packed
slabs.

## 5. Verdict

No literal correcting four-slab rectangle is constructed by the current
files.

What is proved here is a sharp two-part negative classification.

1. Every same-frame owner-disjoint rectangle is exactly trace-disjoint and
   threshold-flat.
2. A cross-frame rectangle can interact only through alternating
   frame-defect paths.  If those paths have bounded length, the entire
   scalable packing has only (o(W)) correction capacity at every
   (q=o(R)).

Thus the abstract (Q_3) trap/escape cannot be realized by the smallest
same-frame or bounded-defect four-slab rectangles.  The surviving literal
target is a genuinely moving-frame compound object with defect-path length
(\Omega(R/q)), together with enough owner-disjoint copies.  Neither the
rank-twisted slab theorem nor the diverse compiler theorem currently
constructs such an object.

