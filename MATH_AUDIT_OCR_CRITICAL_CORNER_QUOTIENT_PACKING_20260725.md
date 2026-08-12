# The genuine zero-winding critical corner is quotient-packing negligible

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Verdict

Consider the genuine first zero-winding family from
`MATH_ATTACK_OCR_OVERLAP_BRIDGE_CRITICAL_FAMILY_20260725.md`.  Its data are

\[
 0\le t<u<s,\qquad d=u-t,\qquad K=s-d+1,
\]

and a strip path \(Y:0\to K\) in \([0,K]\).  Put

\[
 \overline T=0^K Y,\qquad S=Y0^K,
\]

and assume the two cap conditions

\[
 K\le s-1-t,\qquad K\le u.                       \tag{0.1}
\]

The construction is genuine: its displayed roots are the exact successive
\(\tau\)-roots, the return equation has winding zero, and every proper
prefix misses the return congruence.

The new packing conclusion is stronger than a count for one fixed phase
pair.  Every return interval in this construction contains the literal
quotient edge

\[
 \boxed{e_{C(s,K,Y)}},\qquad
 C(s,K,Y)=1^s0^K Y0^s.                            \tag{0.2}
\]

The edge (0.2) is independent of \((t,u)\).  Moreover, its word uniquely
determines \((s,K,Y)\).  Thus phase-pair multiplicity gives no packing
multiplicity: intervals with the same \((s,K,Y)\) all meet at (0.2).

Let \(B_m=\operatorname {Cat}_m\), and fix \(0<\alpha<A<\infty\).  Let
\(\Pi_m^{\rm corner}(\alpha,A)\) be the maximum quotient-edge-disjoint
packing of all nonwrapping intervals supplied by this construction with

\[
 \alpha\sqrt m\le s\le A\sqrt m,
\]

allowing every admissible \((t,u)\), every admissible \(K\), and every
strip path \(Y\) of rank \(m\).  Then

\[
 \boxed{
 \Pi_m^{\rm corner}(\alpha,A)
 \le {2\over3}\cdot4^m\cdot4^{-\lceil\alpha\sqrt m\rceil}
 =o_{\alpha,A}(B_m/\sqrt m).}                     \tag{0.3}
\]

In the displayed critical specialization

\[
 s=3q,\qquad t=q-1,\qquad u=2q,\qquad K=2q,
\]

the sharper fixed-parameter bound is

\[
 \boxed{
 \Pi_{m,q}^{\rm corner}
 \le 2^{2m-8q}.}                                  \tag{0.4}
\]

Consequently, whenever \(q\asymp\sqrt m\), this family is exponentially
smaller than \(B_m/\sqrt m\).  It does not furnish a critical packing and
does not kill the PBBS lane.  The strip kernel is critical only after its
deterministic collars have been deleted; those collars are exactly what
make the embedded Catalan family negligible.

This conclusion concerns this explicit corner construction.  It is not a
proof of the full zero-winding quotient-packing theorem for arbitrary PBBS
returns.

## 1. Exact roots and the exceptional block identities

Let \(Y\) have length

\[
 |Y|=K+2n,
\]

and put

\[
 L=|\overline T|=|S|=2K+2n,
 \qquad m=s+{L\over2}=s+K+n.                      \tag{1.1}
\]

The word \(\overline T\) has net zero and nonpositive prefixes, while
\(S\) is Dyck.  The fundamental literal identity is

\[
 \boxed{\overline T0^K=0^KS.}                    \tag{1.2}
\]

Use the staircase arrays

\[
 T_t=T,\qquad S_u=S,
\]

with every other \(T_j,S_j\), including \(S_s\), empty.  In the canonical
factorization

\[
 D_j=P_j1R_j0S_j,
\]

the prefix and terminal-corridor words are

\[
 P_j=
 \begin{cases}
  1^{s-1-t+j}\overline T1^{t-j},&0\le j\le t,\\
  1^{s-1},&t+1\le j\le u,\\
  1^{k-1}S1^{s-k},&j=u+k,\ 1\le k\le s-u,
 \end{cases}                                      \tag{1.3}
\]

and

\[
 R_j=
 \begin{cases}
  0^{s-1},&0\le j\le t,\\
  0^{k-1}\overline T0^{s-k},
       &j=t+k,\ 1\le k\le d-1,\\
  0^{s-1},&u\le j\le s.
 \end{cases}                                      \tag{1.4}
\]

Condition (0.1) is exactly what is needed for these to be canonical.  In
the first line of (1.3), the descending word \(\overline T\) is based at
height at least \(s-1-t\ge K\).  In the last line, the \(S\)-excursion is
based at \(k-1\) and reaches at most

\[
 k-1+K\le s-u-1+K\le s-1.
\]

In the middle line of (1.4), after \(k-1\) zeroes and the initial \(0^K\),
the height is \(d-k\ge1\); during \(Y\) it stays between \(d-k\) and
\(s-k+1\le s\).  Thus the claimed prefix and corridor inequalities hold
at every phase.

The exact local rotation identities are

\[
 S_j1P_j=P_{j+1}1\overline T_j,
 \qquad
 \overline T_j0R_j=R_{j+1}0S_{j+1}.               \tag{1.5}
\]

Away from \(j=t,u-1,u\), these only move one delimiter through an empty
block.  At the exceptional phases they are literally

\[
 1(1^{s-1}\overline T)=1^{s-1}1\overline T,
 \qquad
 \overline T0^s=(\overline T0^{s-1})0,             \tag{1.6}
\]

\[
 0^{d-1}\overline T0^K=0^sS,                      \tag{1.7}
\]

and

\[
 S1^s=(S1^{s-1})1.                                \tag{1.8}
\]

Here (1.7) follows from (1.2) and \(d-1+K=s\).  Concatenating (1.5)
gives

\[
 D_{j+1}=S_j1P_j0R_j=\tau D_j.                   \tag{1.9}
\]

Consequently the successive normalized roots, including the second
boundary-edge root, are exactly

\[
 D_j=
 \begin{cases}
  1^{s-1-t+j}0^K Y1^{t-j+1}0^s,
       &0\le j\le t,\\[2mm]
  1^s0^{K+k-1}Y0^{s-k+1},
       &j=t+k,\ 1\le k\le d,\\[2mm]
  1^{k-1}Y0^K1^{s-k+1}0^s,
       &j=u+k,\ 1\le k\le s-u+1.
 \end{cases}                                      \tag{1.10}
\]

The middle line at \(k=d\) is \(D_u=1^s0^sY0^K\).  The last line at
\(k=s-u+1\) is

\[
 D_{s+1}=1^{s-u}Y0^K1^u0^s=\tau D_s.             \tag{1.11}
\]

Thus (1.10), rather than only an endpoint word equation, supplies every
literal quotient-edge identity needed below.

## 2. Exact first-return chronology

Write

\[
 c_j=|S_j|+1.
\]

Since only \(S_u\) is nonempty,

\[
 c_j=
 \begin{cases}
  L+1,&j=u,\\
  1,&j\ne u.
 \end{cases}                                      \tag{2.1}
\]

The first-maximum positions read directly from the canonical prefixes:

\[
 \delta(D_j)=
 \begin{cases}
  s+L,&0\le j\le t,\\
  s,&t+1\le j\le u,\\
  s+L,&u+1\le j\le s.
 \end{cases}                                      \tag{2.2}
\]

The accumulated deficit before phase \(j\) is

\[
 C_j:=\sum_{i<j}c_i=
 \begin{cases}
  j,&j\le u,\\
  j+L,&j\ge u+1.
 \end{cases}                                      \tag{2.3}
\]

For every proper phase \(1\le j<s\), equations (2.2)-(2.3) give

\[
 C_j<\delta(D_j):                                 \tag{2.4}
\]

in the middle block this is \(j<s\), and in the last block it is
\(j+L<s+L\).  At the terminal phase,

\[
 \sum_{i=0}^{s-1}c_i=s+L=\delta(D_s).             \tag{2.5}
\]

Also

\[
 s+L=2m-s<2m+1=N.                                \tag{2.6}
\]

Hence every quantity in (2.4) lies strictly between zero and \(N\), so
no hidden multiple of \(N\) can turn a proper inequality into a return
congruence.  Equation (2.5) is the return equation with winding exactly
zero, and (2.4) proves that it is the first return.  This audits both
genuineness and chronology without invoking a converse theorem.

## 3. Exact quotient-edge support and the corner charge

Use the insertion-edge convention: \(e_D\) is the quotient transition
which inserts the coordinate omitted at normalized root \(D\).  For an
odd return gap \(2s+1\), the full projected cut support is

\[
 \boxed{
 Q(D_0,s)=\{e_{D_0},e_{D_1},\ldots,e_{D_{s+1}}\}.} \tag{3.1}
\]

It has \(s+2\) edges.  The deficit roots in (2.5) are
\(D_0,\ldots,D_{s-1}\), \(D_s\) is the terminal \(\delta\)-root, and
\(D_{s+1}\) is the second boundary edge.  Formula (1.10) therefore
identifies every edge in (3.1).

The phase \(j=t+1\) is present because (0.1) implies \(u\ge2t+2\), and
the middle line of (1.10) with \(k=1\) gives

\[
 \boxed{D_{t+1}=1^s0^K Y0^s=C(s,K,Y).}            \tag{3.2}
\]

Thus every constructed interval contains the corner edge (0.2).

This word has a unique parse.  Its initial run of ones has length exactly
\(s\); the next zero run has length exactly \(K\), because a strip path
from zero to positive height \(K\) begins with a one; and its terminal zero
run has length exactly \(s\), because such a path ends with a one.  After
these runs are removed, the remaining word is exactly \(Y\).  Therefore

\[
 C(s,K,Y)=C(s',K',Y')
 \quad\Longrightarrow\quad
 (s,K,Y)=(s',K',Y').                              \tag{3.3}
\]

In contrast, \((t,u)\) is absent from (3.2).  For fixed \((s,K,Y)\), all
admissible phase pairs have the same corner edge and hence no two of their
intervals can belong to one quotient-edge-disjoint packing.  This is the
packing-level fact that a raw count over phase pairs misses.

The argument applies a fortiori after the short quotient cycles are
discarded.  No assumption about the period of \(D_0\) is needed for the
upper bound.

## 4. Packing bound at fixed rank

Fix \(m,s,K\).  Equation (1.1) forces

\[
 n=m-s-K,
 \qquad
 |Y|=K+2n=2m-2s-K.                               \tag{4.1}
\]

Let \(a_{K,n}\) be the number of valid strip paths.  The exact strip
formula is

\[
 a_{K,n}=[x^{K+2n}]\,{x^K\over Q_{K+1}(x^2)},   \tag{4.2}
\]

but for packing it suffices to retain that these paths form a subset of
all binary words of the length in (4.1):

\[
 a_{K,n}\le2^{2m-2s-K}.                          \tag{4.3}
\]

Map each selected interval to its edge (3.2).  Edge-disjointness and
(3.3) make this map injective into the union of the corresponding corner
words.  Since \(t<u<s\) gives \(2\le K\le s\), extending both sums can
only increase the result:

\[
\begin{aligned}
 \Pi_m^{\rm corner}(\alpha,A)
 &\le
 \sum_{s=\lceil\alpha\sqrt m\rceil}^{\lfloor A\sqrt m\rfloor}
 \sum_{K=2}^{s}2^{2m-2s-K}\\
 &\le
 4^m
 \left(\sum_{s\ge\lceil\alpha\sqrt m\rceil}4^{-s}\right)
 \left(\sum_{K\ge2}2^{-K}\right)\\
 &= {2\over3}\cdot4^m\cdot4^{-\lceil\alpha\sqrt m\rceil}.
                                                               \tag{4.4}
\end{aligned}
\]

For an elementary Catalan comparison, the central binomial coefficient is
the largest of the \(2m+1\) coefficients of \((1+1)^{2m}\).  Hence

\[
 B_m={1\over m+1}{2m\choose m}
 \ge {4^m\over(m+1)(2m+1)}.                      \tag{4.5}
\]

Combining (4.4) and (4.5) gives

\[
 {\Pi_m^{\rm corner}(\alpha,A)\over B_m/\sqrt m}
 \le {2\over3}(m+1)(2m+1)\sqrt m\,
       4^{-\lceil\alpha\sqrt m\rceil}
 \longrightarrow0.                               \tag{4.6}
\]

This proves (0.3).

For \(s=3q,K=2q\), (4.3) is exactly

\[
 a_{2q,m-5q}\le2^{2m-2(3q)-2q}=2^{2m-8q},       \tag{4.7}
\]

which proves (0.4).  If \(q\ge c\sqrt m\), then

\[
 {\Pi_{m,q}^{\rm corner}\over B_m/\sqrt m}
 \le(m+1)(2m+1)\sqrt m\,2^{-8c\sqrt m}=o(1).     \tag{4.8}
\]

## 5. Why the critical strip mass does not contradict the packing bound

The exact local strip kernel satisfies

\[
 \sum_Y2^{-|Y|}=G_K(1/2)={2\over K+2}.            \tag{5.1}
\]

But the embedded corner root (3.2) has

\[
 2m=2s+K+|Y|.                                     \tag{5.2}
\]

Consequently its full critical binary mass is not (5.1), but

\[
 \boxed{
 \sum_Y2^{-2m}
 =2^{-2s-K}G_K(1/2)
 ={2^{-2s-K+1}\over K+2}.}                       \tag{5.3}
\]

At \(s,K\asymp\sqrt m\), the missing deterministic-collar factor in
(5.3) is exponentially small in \(\sqrt m\).  Thus the statement that the
free strip corridor is coefficientwise critical is correct, while the
inference that the resulting fixed-rank Dyck family could have critical
Catalan packing mass is false.

There are also literal collisions inside the family, so its intervals are
not automatically edge-disjoint.  On the boundary \(u=2t+2\), which
includes \((s,t,u,K)=(3q,q-1,2q,2q)\), one has

\[
 K=s-1-t,\qquad K+t+1=s.                          \tag{5.4}
\]

For any \(Z:0\to K\) in the strip, set

\[
 Y=1^K0^KZ,
 \qquad
 Y'=Z0^K1^K.                                      \tag{5.5}
\]

Both are valid strip paths of the same length.  Equations (1.10) and
(5.4) give the exact cross-interval edge identity

\[
\begin{aligned}
 D_{u+1}(Y)
 &=Y0^K1^s0^s\\
 &=1^K0^KZ0^K1^s0^s\\
 &=1^K0^KY'1^{t+1}0^s
 =D_0(Y').                                        \tag{5.6}
\end{aligned}
\]

Whenever \(Y\ne Y'\), the two distinct supports therefore share

\[
 e_{D_{u+1}(Y)}=e_{D_0(Y')}.                     \tag{5.7}
\]

Such choices exist for every \(K\ge2\); for example, take
\(Z=10\,1^K\).

This collision is not needed for the little-oh upper bound, but it rules
out the stronger unsupported claim that all paths in the strip kernel can
be packed simultaneously.

## 6. Proved boundary

The critical transported-overlap construction survives the mathematical
audit:

1. all canonical height caps hold;
2. (1.10) lists every successive \(\tau\)-root;
3. (2.4)-(2.6) prove genuine first zero winding;
4. (3.1) includes both boundary edges with the correct \(s+2\) convention.

Its proposed role as a packing obstruction does not survive.  The common
corner edge (3.2) removes phase-pair multiplicity, and the fixed collars
force (0.3).  Therefore this family belongs on the negligible side of the
PBBS quotient gate.  Any actual critical packing, if one exists, must avoid
a deterministically parseable \(\Theta(\sqrt m)\)-length collar charge of
this kind.
