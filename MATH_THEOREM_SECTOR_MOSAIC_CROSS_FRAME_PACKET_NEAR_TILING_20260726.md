# A deterministic sector-mosaic cross-frame packet near-tiling

Date: 2026-07-26

Method: pure mathematics only. No random-like nibble, computation, finite
search, solver, or web input is used.

## 0. Outcome

The unrestricted packet architecture admits a structured cross-frame
near-tiling with the two properties which the whole-component atlas could
not have simultaneously:

1. the selected \(Q_r\) packets are literally owner-disjoint; and
2. every selected packet changes frame on every active quartet slot
   relative to one fixed reference matching.

Assume first that \(m\) is even and put \(b=m/2\). Partition the
\(2m=4b\) coordinates into \(b\) quartets. Let \(r=4\cdot2^t\) satisfy

\[
                         r\log m=o(m).                            \tag{0.1}
\]

Partition the quartet indices into \(r\) sectors of nearly equal size.
A deterministic local three-frame mosaic partitions the six rank-two
states of every quartet into three physical \(Q_1\)'s. Two cells use
directions outside a fixed reference matching. In every sector select the
first such cross-frame cell and freeze every other local orientation axis.

This gives pairwise owner-disjoint physical \(Q_r\) packets
\({\cal P}_{m,r}\) with

\[
 \boxed{
 \left|\binom{[2m]}m\setminus\bigcup_{P\in{\cal P}_{m,r}}P\right|
 \le(2m+1)r\left({3\over4}\right)^{\lfloor b/r\rfloor}W
 =m^{-\omega(1)}W.}                                  \tag{0.2}
\]

Every active pair is a nonreference quartet edge, so the frame-change
density is one. Different packets may use different alternatives in
different sectors, while their owner overlap is zero.

Install the proved parity-alternating recursive compiler after identifying
the selected axis in sector \(i\) with leaf \(i\) of its dyadic direction
tree. For every depth-\(d\) tree block and every consecutive \(q\)-window,
the number of directions in that block differs from \(q/2^d\) by at most
\(d\). Thus a window with

\[
                         q>2^d d                                \tag{0.3}
\]

meets all \(2^d\) macroscopic sector groups. This also escapes the
one-block localization obstruction of the rotation-necklace atlas.

For parameters

\[
 {H\over\sqrt m}\to\infty,\qquad {H\over r}\to0,\qquad
 r\log m=o(m),                                      \tag{0.4}
\]

the owner leave is \(o(W/H)\), exactly the owner part required by CPM.
Owner packing, positive-density frame motion, and multiscale window
transport are therefore proved together by a deterministic resolution.

The colored target condition is now refuted for this frozen quartet atlas.
The audit
`MATH_AUDIT_SECTOR_MOSAIC_COMPATIBLE_CAPACITY_GAUSSIAN_NOGO_20260726.md`
proves that a target profile \(\pi=(g,h,u,\ldots)\) can use only the forced
source profile \(\pi^\uparrow=(g-q,h,u+q,\ldots)\), and that the exact
selected-source/target ratio is

\[
 \gamma_{\rm sec}(\pi^\uparrow)
 {2^q\binom gq\over\binom{u+q}q}
 \le {2^q\binom gq\over\binom{u+q}q}.
\]

At \(q=\lfloor A\sqrt m\rfloor\), this tends to \(e^{-6A^2}\) on a
positive-density central profile family.  Thus owner packing, frame motion,
and dispersion remain valid, but the selected packets have a linear
Gaussian Hall deficit.  Escaping it requires positive-density cross-block
paths or owner-dependent re-atlasing; no choice of compiler inside the same
packets can suffice.

## 1. The local six-owner mosaic

Write one quartet as \(Q=\{0,1,2,3\}\). Its rank-two states are partitioned
by

\[
\begin{aligned}
 C_0&=\{01,02\},\\
 C_1&=\{03,13\},\\
 C_2&=\{12,23\}.
\end{aligned}                                                   \tag{1.1}
\]

Each \(C_j\) is a physical \(Q_1\). Their active direction pairs are,
respectively,

\[
                         12,\qquad01,\qquad13.                   \tag{1.2}
\]

Thus (1.1) is an exact mixed-frame partition with completed local frames

\[
                         12\mid03,\qquad
                         01\mid23,\qquad
                         13\mid02.                               \tag{1.3}
\]

Take \(M^\star=01\mid23\) as the reference. Call \(C_0,C_2\) cross cells
and \(C_1\) the reference cell. Both cross-cell directions lie outside
\(M^\star\).

Complete (1.1) to a partition \({\cal L}(Q)\) of \(2^Q\) by making each
state of rank different from two a singleton. Thus \({\cal L}(Q)\) has
ten singleton cells and three \(Q_1\)-cells.

## 2. Product resolution and sector selection

Let \(Q_1,\ldots,Q_b\) be the quartets and tensor their local partitions:

\[
                         {\cal L}
 ={\cal L}(Q_1)\times\cdots\times{\cal L}(Q_b).       \tag{2.1}
\]

Every product cell is a physical orientation cube. Its local rank vector
is fixed, so the product cells restrict to a partition of the middle
layer.

Partition \([b]\) into sectors \(S_0,\ldots,S_{r-1}\) with

\[
 |S_i|\in\{\lfloor b/r\rfloor,\lceil b/r\rceil\}.    \tag{2.2}
\]

Call a product cell good if every sector contains a symbol \(C_0\) or
\(C_2\). In a good cell let \(i_j(C)\) be the first cross symbol in
sector \(S_j\), and put

\[
                         I(C)=\{i_0(C),\ldots,i_{r-1}(C)\}.       \tag{2.3}
\]

This set is constant throughout \(C\), since a local cube move changes
orientation but not its symbol. Freeze every free orientation outside
\(I(C)\). The resulting parallel \(Q_r\)-subcubes partition \(C\).
Doing this in every good middle product cell defines
\({\cal P}_{m,r}\).

### Theorem 2.1 (exact owner matching)

The packets in \({\cal P}_{m,r}\) are pairwise owner-disjoint and cover
every owner in a good product cell exactly once.

#### Proof

The product cells (2.1) are disjoint. Inside one good cell, fixing all
complementary free coordinates is the standard partition of a cube into
parallel \(r\)-subcubes. \(\square\)

Every selected packet has one active axis in every sector, and every such
axis belongs to \(C_0\) or \(C_2\). By (1.2)--(1.3), all \(r\) axes are
nonreference directions.

## 3. Exact leave

Choose a uniformly random subset \(X\subseteq[2m]\) before rank
conditioning. Different quartet restrictions are independent. The union
\(C_0\cup C_2\) contains four of the sixteen local states, so

\[
 \Pr\{X\cap Q_i\text{ is cross}\}={1\over4}.         \tag{3.1}
\]

A sector of length \(\ell\) contains no cross symbol with probability
\((3/4)^\ell\). A union bound gives

\[
 \Pr\{X\text{ lies in a bad product cell}\}
 \le r\left({3\over4}\right)^{\lfloor b/r\rfloor}.   \tag{3.2}
\]

Conditioning on \(|X|=m\) costs at most

\[
                         {4^m\over W}\le2m+1.         \tag{3.3}
\]

This proves (0.2). Under (0.1), \(b/r-\log m\to\infty\), so the leave is
\(m^{-\omega(1)}W\). Odd \(m\) or divisibility remainders are handled by
isolating one bounded block; only the prefactor changes.

## 4. Sparse overlap and frame motion

The selected supports satisfy

\[
                         P\cap P'=\varnothing
 \qquad(P\ne P'\in{\cal P}_{m,r}).                  \tag{4.1}
\]

This is stronger than a bounded-codegree hypothesis and comes from an
exact resolution, not conflict deletion.

For each selected packet, complete its active pair in a quartet to the
corresponding matching in (1.3), and complete frozen coordinates
arbitrarily. This gives a physical frame \(M(P)\). On every selected
quartet,

\[
                         M(P)|_{Q_i}\ne M^\star|_{Q_i}.           \tag{4.2}
\]

The alternative \(12\mid03\) or \(13\mid02\) is determined by the product
cell and varies among sectors and packets. Hence this is a literal
mixed-frame packet mosaic, not a whole-component shore choice.

## 5. Dyadic dispersion from the compiler

Identify the \(r=4\cdot2^t\) packet axes with the leaves of the
parity-alternating recursive direction tree. At every internal node,
successive moves alternate between its children, and the subsequence of
moves in one child is a consecutive child trajectory.

For a tree node \(B\) at depth \(d\), let \(n_B(J)\) count directions in
\(B\) during a consecutive transition interval \(J\) of length \(q\).

### Theorem 5.1 (all-window dyadic discrepancy)

\[
                         \left|n_B(J)-{q\over2^d}\right|\le d.  \tag{5.1}
\]

#### Proof

At depth one, alternation gives error at most one. Suppose the assertion
holds at depth \(d-1\) inside either child. A parent interval of length
\(q\) induces a consecutive interval in that child of length
\(q'\in\{\lfloor q/2\rfloor,\lceil q/2\rceil\}\). Hence

\[
 \left|n_B(J)-{q'\over2^{d-1}}\right|\le d-1,\qquad
 \left|{q'\over2^{d-1}}-{q\over2^d}\right|\le1.      \tag{5.2}
\]

The triangle inequality proves (5.1). \(\square\)

Label sector \(S_i\) by leaf \(i\). The depth-\(d\) nodes are macroscopic
sector groups. If \(q>2^dd\), (5.1) makes every group nonempty in every
\(q\)-window. Thus no sufficiently long protected window is confined to
one block of a fixed bounded-depth dyadic sector partition.

## 6. CPM owner advancement and Gaussian target failure

For example, choose an admissible power of two

\[
                         m^{3/5}\le r\le2m^{3/5}                  \tag{6.1}
\]

and

\[
                         H=\lfloor\sqrt m\log\log m\rfloor.      \tag{6.2}
\]

Then (0.1), (0.4), and the local compiler range hold for large \(m\), and

\[
 W-\left|\bigcup_{P\in{\cal P}_{m,r}}P\right|
 =m^{-\omega(1)}W=o(W/H).                           \tag{6.3}
\]

Install the proved local compiler on every packet with the
sector-to-leaf assignment of Section 5. The family now has:

1. the owner leave required by CPM;
2. one common compiler option serving every \(q\le H\);
3. literal frame change on all active axes; and
4. deterministic nonlocal support for every sufficiently long window.

Let \(Q_{q,\epsilon}\) be the exact integer floor energy of the selected
target loads. The coefficient-one claim would require

\[
                         \sum_{q\le H,\epsilon}Q_{q,\epsilon}=o(W).          \tag{6.4}
\]

Equivalently, one would have to control the explicit deterministic overlap kernel

\[
 \sum_{\substack{P,P'\in{\cal P}_{m,r}\\P\ne P'}}
 |\mathcal T_{P,q}^{\epsilon}
       \cap\mathcal T_{P',q}^{\epsilon}|              \tag{6.5}
\]

against its floor-balanced baseline, simultaneously in \(q\).  The
compatible-capacity audit shows that (6.4) is false already at one fixed
Gaussian depth.  Specifically, for a target profile
\(\pi=(g,h,u,\ldots)\), the sector selection retains only a fraction
\(\gamma_{\rm sec}(\pi^\uparrow)\le1\) of the unique compatible source
profile, so

\[
 { |S_\pi^{\rm sec}|\over|A_\pi|}
 =\gamma_{\rm sec}(\pi^\uparrow)
   {2^q\binom gq\over\binom{u+q}q}.
\tag{6.6}
\]

The fixed **whole-frame** cut is indeed avoided, and Theorem 5.1 still
avoids bounded-block direction localization.  What survives is the
mixed-frame fixed-**quartet-profile** capacity cut: varying frames inside
the same immutable product atlas does not move capacity between the forced
profile fibres.  Any continuation must use a positive-density family of
windows crossing product cells, or re-atlas a positive-density owner set so
that central targets acquire sources from other old-atlas profiles.
