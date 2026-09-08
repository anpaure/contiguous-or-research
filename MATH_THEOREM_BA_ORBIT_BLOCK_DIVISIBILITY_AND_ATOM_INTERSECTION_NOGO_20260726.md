# Odd-\(m\) \(BA\)-orbit blocks: exact divisibility and the atom-intersection boundary

Date: 2026-07-26

Method: exact orbit and incidence counting. No computation is used.

## 1. Statement

Let

\[
 m=2r+1\ge3,\qquad n=2m+1,\qquad L=m(m+1),\qquad
 W=\binom{n}{m},
\]

and put \(C=BA\) on permutation states. For a \(C\)-orbit
\(O=\{C^t\pi:0\le t<L\}\), define its middle-owner block

\[
 \mathcal B(O)=
 \{\kappa(C^t\pi),\kappa(AC^t\pi):0\le t<L\}.
 \tag{1.1}
\]

For odd \(m\), (1.1) has \(2L\) distinct owners. Let \(Z(O)\) be the
set of labels occupying the length-\(m\) position cycle of \(C\).

### Theorem 1.1 (integral orbit-block congruence)

Let \(O_1,\ldots,O_t\) be \(C\)-orbits whose owner blocks are pairwise
disjoint, and let \(\mathcal L\) be the uncovered family of middle
owners. Write

\[
 \ell=|\mathcal L|,\qquad
 \ell_x=|\{X\in\mathcal L:x\in X\}|,\qquad
 d_x=|\{i:x\in Z(O_i)\}|.
\]

Then

\[
 \ell=W-2m(m+1)t,
 \tag{1.2}
\]

and, for every coordinate \(x\),

\[
 \ell_x=m\operatorname{Cat}_m-m^2t-md_x.
 \tag{1.3}
\]

In particular \(m\mid\ell_x\) for every \(x\). Hence a nonempty owner
leave has size at least \(m\).

Suppose in addition that the selected source states are partitioned
into canonical nested-star atoms. Since every such atom has zero signed
divergence at rank one, necessarily

\[
 d_x=\frac{mt}{n}\quad(x\in[n]),\qquad n\mid t.
 \tag{1.4}
\]

Consequently the owner leave is coordinate-regular:

\[
 \boxed{\ell_x=\frac{m\ell}{n}\quad(x\in[n])},
 \tag{1.5}
\]

and

\[
 \boxed{\ell\equiv W
 \pmod{\,2m(m+1)(2m+1)\,}}.
 \tag{1.6}
\]

Thus an exact owner cover compatible with a zero-divergence atom
partition is arithmetically possible only if

\[
 \boxed{2m(m+1)\mid\operatorname{Cat}_m.}
 \tag{1.7}
\]

For every odd prime \(m\), (1.7) fails. Hence no exact orbit-block /
nested-star intersection exists at an odd prime parameter. Moreover,
at an odd prime \(m\), every nonempty compatible leave satisfies

\[
 \ell\ge2(2m+1).
 \tag{1.9}
\]

### Theorem 1.2 (physical first-shadow obstruction)

For any such owner-disjoint family of \(t\) orbit blocks, its physical
rank-\((m-1)\) prefix support has size at most \(tL\). Therefore

\[
 M_1^-\ge
 \binom n{m-1}-tL
 =\frac{m-2}{2(m+2)}W+\frac{\ell}{2}.
 \tag{1.8}
\]

In particular \(M_1^-=(1/2-o(1))W\), even if \(\ell=o(W)\).
Partitioning the selected source states into nested-star atoms changes
neither the states nor their physical prefix words, so it cannot alter
(1.8).

Accordingly, an orbit-block near-factor would solve the owner rows and
the equation \(S=BA(S)\), but it cannot be the bulk constant-one
compiler. This conclusion is independent of the open question whether
the orbit-block hypergraph itself has a matching with polynomial or
\(o(W)\) leave.

## 2. Exact incidence vector of one block

The position permutation \(C\) has cycles of lengths \(m\) and \(m+1\).
For odd \(m=2r+1\), the owners in (1.1) have the product form

\[
 \bigl(\mathcal I_{m,r+1}\times\mathcal I_{m+1,r}\bigr)
 \;\dot\cup\;
 \bigl(\mathcal I_{m,r}\times\mathcal I_{m+1,r+1}\bigr),
 \tag{2.1}
\]

where \(\mathcal I_{a,b}\) denotes the \(a\) cyclic intervals of
length \(b\). If \(x\in Z(O)\), the two products contain \(x\) in

\[
 (r+1)(m+1)+r(m+1)=m(m+1)=L
\]

owners. If \(x\notin Z(O)\), they contain \(x\) in

\[
 mr+m(r+1)=m^2
\]

owners. Thus the coordinate-incidence vector of one block is

\[
 \sum_{X\in\mathcal B(O)}\mathbf1_X
 =m^2\mathbf1_{[n]}+m\mathbf1_{Z(O)}.
 \tag{2.2}
\]

Every coordinate lies in

\[
 \binom{2m}{m-1}=m\operatorname{Cat}_m
 \tag{2.3}
\]

middle owners. Subtracting (2.2) for all selected blocks from (2.3)
proves (1.3), while (1.2) follows from the block size \(2L\).
The divisibility \(m\mid\ell_x\) is immediate. If the leave were
nonempty with \(\ell<m\), every positive \(\ell_x\) would be at most
\(\ell<m\), contradicting that it is a positive multiple of \(m\).

### Theorem 2.1 (complete pair-codegree census)

Let \(\mathcal H_m\) be the simple hypergraph of distinct coordinate
relabels of one block (2.1). Its block stabiliser is

\[
 D_m\times D_{m+1},
\]

so

\[
 |E(\mathcal H_m)|=\frac{n!}{4L},\qquad
 D_{\rm simp}=\frac{m!(m+1)!}{2}.
 \tag{2.4}
\]

For \(0\le d\le m\), let \(c_d\) be the average number of members of
one block at Johnson distance \(d\) from a member of that block. Put

\[
\begin{aligned}
 A(z)&=1+2\sum_{i=1}^{r}z^i,\\
 B(z)&=1+2\sum_{i=1}^{r-1}z^i+3z^r,\\
 H(z)&=1+2\sum_{i=1}^{r}z^i+z^{r+1},\\
 P(z)&=2\sum_{i=1}^{r}z^i+z^{r+1},\\
 Q(z)&=2\sum_{i=0}^{r}z^i.
\end{aligned}
\tag{2.5}
\]

Then the exact distance enumerator is

\[
 \boxed{\sum_{d=0}^{m}c_dz^d
 =P(z)Q(z)+\frac{A(z)(B(z)+H(z))}{2}.}
 \tag{2.6}
\]

Equivalently,

\[
c_d=
\begin{cases}
1,&d=0,\\
8d,&1\le d\le r-1,\\
8r+\tfrac12,&d=r,\\
8r+\tfrac72,&d=r+1,\\
16r-8d+12,&r+2\le d\le2r,\\
3,&d=2r+1=m.
\end{cases}
\tag{2.7}
\]

For fixed ambient owners \(X,Y\) at Johnson distance \(d\), their
codegree is

\[
 \boxed{\frac{\lambda_d}{D_{\rm simp}}
 =\frac{c_d}{\binom md\binom{m+1}d}.}
 \tag{2.8}
\]

For every odd \(m\ge3\), the unique maximum distance class is \(d=m\):

\[
 \boxed{\frac{\Delta_2}{D_{\rm simp}}=\frac3{m+1},\qquad
 \Delta_2=\frac32(m!)^2.}
 \tag{2.9}
\]

If edges are indexed by actual \(BA\)-state orbits rather than by
distinct geometric blocks, each block has multiplicity four (the two
cycle orientations may be independently reversed). Thus

\[
 D_{\rm orb}=2m!(m+1)!,\qquad
 \Delta_{2,\rm orb}=6(m!)^2.
 \tag{2.10}
\]

All normalized codegrees remain (2.8).

#### Proof

The coordinate loads in (2.2) recover \(Z(O)\) from the block.
On each of \(Z(O)\) and its complement, the interval families recover
the underlying undirected cyclic order. Hence the setwise stabiliser
is exactly \(D_m\times D_{m+1}\), of order \(4L\). Orbit--stabiliser
and incidence double-counting give (2.4).

For two intervals of the same permitted length on the odd
\((2r+1)\)-cycle, the Johnson-distance enumerator is \(A\).
On the even \((2r+2)\)-cycle it is \(B\) for length \(r\), and \(H\)
for length \(r+1\). For intervals of the two different lengths, the
odd-cycle deletion enumerator is \(P\), and the even-cycle deletion
enumerator is \(Q\). Distances on the two coordinate cycles add.
Averaging the two same-type products and adding the cross-type product
gives (2.6); coefficient extraction gives (2.7).

The stabiliser of one ambient owner is transitive on owners at Johnson
distance \(d\). Double-counting ordered distance-\(d\) owner pairs
inside blocks gives (2.8).

At \(d=m\), (2.7)--(2.8) give \(3/(m+1)\). At \(d=1\), the ratio is
\(8/[m(m+1)]\), except that \(c_1=17/2\) when \(m=3\); it is still
smaller than \(3/(m+1)\). For \(2\le d\le m-2\), (2.7) gives
\(c_d\le4m\), while

\[
 \binom md\binom{m+1}d
 \ge\binom m2\binom{m+1}2.
\]

At \(d=m-1\), (2.7) gives \(c_d=12\) and the denominator is
\(m\binom{m+1}{2}\). These bounds are all strictly below
\(3/(m+1)\), proving (2.9). Finally, passing from undirected cyclic
orders to the two independent directed orders multiplies every simple
block fourfold, which proves (2.10).

## 3. Rank-one divergence forces a regular \(Z\)-design

The rank-one signed divergence of the \(A\)-switches in one full
\(C\)-orbit is

\[
 \partial_1(O)=
 m\sum_{x\notin Z(O)}\mathbf e_x
 -(m+1)\sum_{x\in Z(O)}\mathbf e_x.
 \tag{3.1}
\]

Indeed the length-\(m\) position cycle is visited \(m+1\) times by the
relevant singleton endpoint, while the length-\((m+1)\) cycle is
visited \(m\) times.

The coefficient of \(\mathbf e_x\) in the sum of (3.1) over the \(t\)
orbits is

\[
 m(t-d_x)-(m+1)d_x=mt-nd_x.
 \tag{3.2}
\]

Every canonical nested-star atom cancels its signed divergence, so an
atom partition makes (3.2) zero for every \(x\). This proves (1.4);
\(n\mid t\) follows from \(\gcd(m,n)=1\).

Substitute \(d_x=mt/n\) into (1.3), and use

\[
 \ell=n\operatorname{Cat}_m-2m(m+1)t.
\]

Since \(n+1=2(m+1)\), the result is (1.5). Writing \(t=nu\) in
(1.2) proves (1.6). If \(\ell=0\), then

\[
 2m(m+1)nu=n\operatorname{Cat}_m,
\]

which proves (1.7).

If \(m=p\) is an odd prime, then

\[
 \binom{2p}{p}
 =2\binom{2p-1}{p-1}
 \equiv2\pmod p,
\]

because

\[
 \binom{2p-1}{p-1}
 =\prod_{j=1}^{p-1}\frac{p+j}{j}\equiv1\pmod p.
\]

As \(p+1\equiv1\pmod p\), this gives
\(\operatorname{Cat}_p\equiv2\pmod p\). In particular
\(p\nmid\operatorname{Cat}_p\), proving the prime-parameter
obstruction. Dividing (1.6) by \(n\) gives

\[
 \frac{\ell}{n}\equiv\operatorname{Cat}_p
 \equiv2\pmod p.
\]

The least nonnegative integer in this class is \(2\), which proves
(1.9).

## 4. Audit of the physical prefix ledger

At prefix length \(s=m-1=2r\), the two base prefix position sets have
the same allocation \((r,r)\) between the two position cycles. On the
length-\(m\) cycle they differ by a one-step rotation, and on the
length-\((m+1)\) cycle they agree. The Chinese remainder theorem
therefore puts them in the same \(C\)-orbit. Each of its \(L\) targets
occurs twice among the \(2L\) physical prefix occurrences of one owner
block.

Thus \(t\) blocks have combined support at most \(tL\), regardless of
collisions between different blocks. Since

\[
 \binom n{m-1}=\frac{m}{m+2}W,\qquad
 tL=\frac{W-\ell}{2},
\]

subtraction gives (1.8).

This also audits the role of the atom partition. An atom is a grouping
of already selected source states and their \(A\)-successors. It can
certify cancellation of signed load vectors, but it does not replace
any state or literal prefix. Hence the two-to-one prefix collision
persists after every possible atom regrouping.

## 5. Fractional/integral boundary

There is no fractional obstruction at the orbit-block level. In the
simple coordinate-orbit hypergraph every owner has degree

\[
 D=\frac{m!(m+1)!}{2};
\]

weight \(1/D\) on every block covers every owner exactly. The same
uniform fractional point has zero rank-one divergence, because a fixed
coordinate belongs to \(Z(O)\) in fraction \(m/n\) of the blocks.

The integral constraints (1.4)--(1.7) are therefore genuine rounding
congruences. Every compatible leave lies in the single congruence class
(1.6), whose least nonnegative numerical representative is below the
polynomial modulus \(2m(m+1)(2m+1)=O(m^3)\). This observation does not
construct a leave, but it shows that the congruence alone cannot force
an exponential or positive-density loss. It therefore does not exclude
a matching with \(o(W)\) leave.

Conversely, the known degree and pair-codegree data do not prove such a
matching: the block rank is \(2m(m+1)\), and disjoint owner pairs have
relative codegree \(3/(m+1)\). A specialised product-interval factor
theorem would still be required.

For the constant-one route, however, that matching theorem is no longer
the decisive gate: the unconditional physical obstruction (1.8) rules
out positive-density use of these strict alternating blocks before the
separate star-atom partition problem is reached.
