# Fixed-coordinate SCDs give an exact all-depth two-rail star packing

**Date:** 2026-08-06  
**Method:** symmetric-chain decomposition, a fixed separator coordinate,
and two consecutive full endpoints of a linear common-core star chart  
**Status:** unconditional marked-target packing theorem.  It gives much
more than the theta-reset target capacity at every depth simultaneously.
It does **not** by itself place the charts in the PBBS owner envelopes or
pay/identify their warm-up positions.

## 1. Statement

Let the ground set have size \(n\), fix one coordinate \(b\), and put

\[
                         N=n-1.
\]

Let star cores have size \(q\), and let \(d\ge1\).  Assume

\[
                         2q+d\le N.                         \tag{1.1}
\]

### Theorem 1.1 (fixed-coordinate SCD two-rail packing)

There are exactly

\[
                         \binom Nq                              \tag{1.2}
\]

linear common-core star charts, each on \(d+1\) distinct private
coordinates and with two marked full endpoints, such that all their
marked targets at depths \(1,\ldots,d\) are pairwise distinct.

More explicitly, the charts may be indexed by the \(q\)-sets
\(Q\subseteq[n]\setminus\{b\}\).  For each chart there is a saturated
chain segment

\[
 Q=R_1\subset R_2\subset\cdots\subset R_{d+1},
 \qquad |R_j|=q+j-1,                                      \tag{1.3}
\]

and its two depth-\(j\) targets are

\[
 \boxed{
 T_{0,j}=R_{j+1},\qquad T_{1,j}=R_j\cup\{b\}
 }
 \qquad(1\le j\le d).                                    \tag{1.4}
\]

Thus the construction packs

\[
                         2\binom Nq                         \tag{1.5}
\]

full endpoints with no marked-target collision at any depth.

## 2. Construction from an SCD

Take any symmetric-chain decomposition of the Boolean lattice
\(B([n]\setminus\{b\})\).

Every symmetric chain contains at most one set of rank \(q\).  Conversely,
the chain containing a \(q\)-set starts at some rank \(a\le q\) and ends
at rank \(N-a\ge N-q\).  Condition (1.1) gives

\[
                         q+d\le N-q,                         \tag{2.1}
\]

so that this chain contains all ranks \(q,q+1,\ldots,q+d\).
Truncate it to those ranks and call the resulting segment (1.3).

Different \(q\)-sets belong to different symmetric chains, because one
chain has only one vertex at a fixed rank.  The resulting
\(\binom Nq\) truncated segments are therefore vertex-disjoint.

Write

\[
                         R_{j+1}=R_j\cup\{a_j\},
                         \qquad 1\le j\le d.                \tag{2.2}
\]

The labels \(a_1,\ldots,a_d,b\) are distinct and all lie outside \(Q\).
Define a private linear order

\[
 z_{d-j}=a_j\quad(1\le j\le d),
 \qquad z_d=b.                                             \tag{2.3}
\]

Use the \(d+1\) common-core source letters

\[
                         Q\cup\{z_0\},\ldots,Q\cup\{z_d\}. \tag{2.4}
\]

The last two positions, \(d-1\) and \(d\), have a complete suffix history
of depths \(1,\ldots,d\).  At the first marked endpoint, the depth-\(j\)
suffix contains

\[
 \{z_{d-j},\ldots,z_{d-1}\}
   =\{a_j,a_{j-1},\ldots,a_1\},                            \tag{2.5}
\]

and hence its target is \(R_{j+1}\).  At the second endpoint, its
depth-\(j\) suffix contains

\[
 \{z_{d-j+1},\ldots,z_d\}
   =\{a_{j-1},\ldots,a_1,b\},                              \tag{2.6}
\]

and hence its target is \(R_j\cup\{b\}\).  This proves the literal
identity (1.4).

## 3. Target disjointness

Targets at different depths have different ranks.  Fix a depth \(j\).

* All \(T_{0,j}\)'s are distinct, because they are the distinct SCD
  vertices \(R_{j+1}\).
* All \(T_{1,j}\)'s are distinct, because deleting \(b\) recovers the
  distinct SCD vertices \(R_j\).
* No \(T_{0,j}\) equals a \(T_{1,j}\), because the first omits \(b\) and
  the second contains \(b\).

Therefore every one of the \(2d\binom Nq\) marked targets is distinct.
This proves Theorem 1.1.

## 3A. The two rails are genuine pieces of the recursive SCD

The construction has a stronger interpretation in the standard BTK
recursion from an SCD of \(B_N\) to one of \(B_{N+1}\).

Write a parent symmetric chain as

\[
 C=(C_a,C_{a+1},\ldots,C_{N-a}),\qquad |C_i|=i.             \tag{3.1A}
\]

The usual split at the new coordinate \(b\) is

\[
 \begin{aligned}
 C^0&=(C_a,C_{a+1},\ldots,C_{N-a},C_{N-a}\cup\{b\}),\\
 C^1&=(C_a\cup\{b\},C_{a+1}\cup\{b\},\ldots,
                         C_{N-a-1}\cup\{b\}).
 \end{aligned}                                             \tag{3.2A}
\]

For the parent chain containing \(Q=R_1=C_q\), equation (1.4) becomes

\[
 (T_{0,1},\ldots,T_{0,d})
   =(C_{q+1},\ldots,C_{q+d})\subset C^0,                    \tag{3.3A}
\]

and

\[
 (T_{1,1},\ldots,T_{1,d})
   =(C_q\cup\{b\},\ldots,C_{q+d-1}\cup\{b\})\subset C^1.  \tag{3.4A}
\]

There is no recursive endpoint exception. Since \(a\le q\), the top of
\(C\) has rank at least \(N-q\), while (1.1) gives

\[
                         q+d-1<N-q.                         \tag{3.5A}
\]

Thus \(C_{q+d-1}\) is not the omitted top vertex of \(C^1\), and both
displayed rails exist in full.

Consequently, when the slab consists of ranks

\[
                         q+1,q+2,\ldots,q+d,                \tag{3.6A}
\]

the two target rails are two actual full SCD pieces in that same slab,
one in each recursive child of a single parent chain. The literal word
(2.4) is therefore an explicit shared star serialization of this paired
BTK piece.

## 4. Top PBBS slab

For the odd top full slab use

\[
 n=2m+1,qquad s=m-2d,qquad q=s-1=m-2d-1,qquad N=2m.       \tag{4.1}
\]

Condition (1.1) is automatic:

\[
 2q+d=2m-3d-2\le2m=N.                                     \tag{4.2}
\]

Equivalently, the entire segment even lies below the middle rank:

\[
                         q+d=m-d-1<m=N/2.                  \tag{4.3}
\]

Let

\[
                         W=\binom{2m+1}{m}.
\]

The exact packet count is

\[
 \binom{2m}{m-2d-1}
   ={m-2d\over2m+1}\binom{2m+1}{m-2d}.                    \tag{4.4}
\]

Using the already established local central limit

\[
 {\binom{2m+1}{m-2d}\over W}\longrightarrow e^{-\pi},    \tag{4.5}
\]

we obtain

\[
 \boxed{
 {\#\text{ charts}\over W}\longrightarrow{e^{-\pi}\over2},
 \qquad
 {\#\text{ marked full endpoints}\over W}\longrightarrow e^{-\pi}.
 }                                                           \tag{4.6}
\]

The theta-reset deficit coefficient is

\[
 \eta=4\sum_{r\ge1}e^{-4\pi r^2}=0.0000139\ldots,         \tag{4.7}
\]

whereas \(e^{-\pi}=0.0432\ldots\).  Hence this exact integral bank has
more than a factor \(3000\) of marked-endpoint capacity over the theta
deficit.

## 5. Why the random distance-stratified route was weaker

For comparison, take two cores \(P,Q\) at Johnson distance

\[
 |P\setminus Q|=|Q\setminus P|=h
\]

and independently random private cyclic orders on complements of size
\(v\).  Put \(A=P\setminus Q\), \(B=Q\setminus P\).  A common depth-\(j\)
target has the unique form

\[
 P\cup(B\cup D)=Q\cup(A\cup D),
 \qquad D\subseteq[n]\setminus(P\cup Q),\quad |D|=j-h.     \tag{5.1}
\]

A fixed \(j\)-set is a cyclic interval with probability
\(v/\binom vj\).  Thus a union bound gives

\[
 \Pr(P,Q\text{ collide at depth }j)
 \le
 \binom{v-h}{j-h}\left({v\over\binom vj}\right)^2.        \tag{5.2}
\]

For two marked endpoint chains rather than full cycles, the corresponding
bound is

\[
 \Pr(P,Q\text{ collide somewhere})
 \le
 4\sum_{j=h}^d{\binom{v-h}{j-h}\over\binom vj^2},          \tag{5.3}
\]

whose leading term is \(4/\binom vh^2\).

At core density \(\rho\), summing the leading terms over the
\(\binom qh\binom vh\) distance-\(h\) neighbours gives the incident
first-moment scale

\[
 4\rho\sum_{h=1}^d{\binom qh\over\binom vh}.               \tag{5.4}
\]

In the top slab \(q/v=1-\Theta(1/d)\), so the sum in (5.4) is
\(\Theta(d)\).  Ordinary alteration and the standard variable-event LLL
therefore only see the divergent scale \(\Theta(\rho d)\); at constant
\(\rho\) they do not prove the desired packing.  The fixed-coordinate SCD
construction bypasses this dependence accumulation by making the two
rails live on disjoint \(b\)-shores and by assigning each shore an
already-disjoint chain factor.

Equation (5.4) is a limitation of those random-order methods, not a
nonexistence theorem.

## 6. Scope and the exact next interface

Proved here:

* an explicit all-depth marked-target matching;
* exactly \(\binom{n-1}{q}\) two-endpoint linear star charts;
* identification of the two rails with actual paired pieces in the
  recursive BTK SCD;
* no target collision at any depth \(1,\ldots,d\);
* an integral top-slab capacity of \((e^{-\pi}+o(1))W\), far exceeding
  the theta deficit.

Not proved here:

* that the first \(d-1\) warm-up positions of every linear chart are free
  in the merged PBBS physical ledger;
* placement of the selected charts in the varying PBBS owner envelopes;
* an owner-compatible Euler order joining the charts;
* preservation of the short-piece/global compiler interface; or
* \(\nu(k)\le B(k)+O(1)\).

Thus the growing-uniformity/random-rounding obstruction is removed for the
**two-marked-endpoint star subproblem**.  The remaining question is now a
physical embedding/accounting problem, not target-disjointness of those
two rails.
