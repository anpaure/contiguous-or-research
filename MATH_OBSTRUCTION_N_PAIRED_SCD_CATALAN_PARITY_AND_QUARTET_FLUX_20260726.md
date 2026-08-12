# Paired SCDs: Catalan parity, exact pair incidence, and the quartet-flux obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Exact conclusion

Let \(\mathcal S\) be a symmetric-chain decomposition of \(B_{2m}\).
For every chain reaching ranks \(m-1,m,m+1\), write its central segment as

\[
 R_X\subset X\subset U_X,
 \qquad |R_X|=m-1,\quad |X|=m,\quad |U_X|=m+1,
 \tag{0.1}
\]

and let

\[
 g(X)=R_X\cup(U_X\setminus X)
 \tag{0.2}
\]

be the other middle corner.  Put

\[
 \mathcal A=\{X:\mathcal S(X)\text{ reaches rank }m-1\},
 \qquad
 \mathcal E=\binom{[2m]}m\setminus\mathcal A.
 \tag{0.3}
\]

Then

\[
 |\mathcal A|=N:=\binom{2m}{m-1},
 \qquad
 |\mathcal E|=D:=\binom{2m}m-\binom{2m}{m-1}
 =\frac1{m+1}\binom{2m}m=\operatorname {Cat}_m.
 \tag{0.4}
\]

The proposed all-\(m\) paired-SCD theorem is false.

### Theorem A (global Catalan obstruction)

Suppose that simultaneously replacing every \(X\in\mathcal A\) by
\(g(X)\), while leaving all nonmiddle sets and the singleton middle chains
\(\mathcal E\) unchanged, gives a second SCD.  Equivalently, suppose

\[
                         g:\mathcal A\longrightarrow\mathcal A
 \tag{0.5}
\]

is a permutation.  Then

\[
                         \operatorname {Cat}_m\equiv0\pmod2.
 \tag{0.6}
\]

Consequently no such pair exists for

\[
                         m=2^a-1\qquad(a\ge1).
 \tag{0.7}
\]

This is an obstruction to every SCD, not merely to BTK, Greene--Kleitman,
or fixed-priority product SCDs.  In particular, the complement-symmetric
\(B_4\) seed cannot extend to an exact all-\(m\) recursion.

The obstruction has two exact refinements.  First, the omitted middle
family must be a point design:

\[
 \boxed{\quad
 |\{E\in\mathcal E:x\in E\}|=D/2
 \quad\text{for every }x\in[2m].\quad}
 \tag{0.8}
\]

Second, if \(\mu_{xy}\) is the number of central diamonds whose two moving
coordinates are \(x,y\), then

\[
 \boxed{\quad
 \mu_{xy}=2|\{E\in\mathcal E:\{x,y\}\subseteq E\}|-K_m,
 \qquad
 K_m=\frac{m-2}{2m-1}D.\quad}
 \tag{0.9}
\]

Thus every pair multiplicity has the common parity

\[
                         \mu_{xy}\equiv K_m\pmod2,
 \tag{0.10}
\]

and every omitted-pair degree is at least \(\lceil K_m/2\rceil\).
These are genuine central-diamond constraints beyond point-margin Euler
balance.  They do not by themselves prove existence when \(D\) is even.

There is also a product obstruction independent of parity.

### Theorem B (fixed-quartet flux toll)

Fix \(b=\lfloor m/2\rfloor\) disjoint four-coordinate blocks.  In every
SCD, at least

\[
 \boxed{
 E_m=\left\lceil
 \frac{b(m-2)}{m(2m-1)}\binom{2m}{m-1}
 \right\rceil
 }
 \tag{0.11}
\]

central diamonds are not pure central \(B_4\)-seed diamonds in this fixed
block frame.  In particular,

\[
                         E_m=(1/4+o(1))\binom{2m}m.
 \tag{0.12}
\]

Therefore a fixed-block tensor or first-eligible outer packing made from
central \(B_4\) rotations on all but \(o(W)\) transitions cannot be the
central diamond system of an SCD.  It needs \(\Omega(W)\) off-centre,
cross-block, or moving-frame transitions.  Sparse seams cannot repair it.

The exact surviving problem is consequently narrower than the proposed
all-\(m\) theorem: in parity-admissible dimensions, construct a dense
moving-frame SCD whose central lift is a doubly-rainbow Johnson 2-factor,
and then control the number and lengths of its components.  Neither
Theorem A nor Theorem B supplies that construction.

## 1. Paired central flips are doubly-rainbow Johnson 2-factors

For \(X\in\mathcal A\), write

\[
 a_X=X\setminus R_X,
 \qquad
 b_X=U_X\setminus X.
 \tag{1.1}
\]

Then

\[
                         g(X)=X-a_X+b_X.
 \tag{1.2}
\]

Every rank-\((m-1)\) set occurs exactly once among the \(R_X\), and every
rank-\((m+1)\) set occurs exactly once among the \(U_X\).  Indeed, every
set at either rank lies in one SCD chain, whose unique middle member is in
\(\mathcal A\).  This proves both the count in (0.4) and the two
bijections

\[
 X\mapsto R_X:\mathcal A\longrightarrow\binom{[2m]}{m-1},
 \qquad
 X\mapsto U_X:\mathcal A\longrightarrow\binom{[2m]}{m+1}.
 \tag{1.3}
\]

The edge

\[
                         e_X=\{X,g(X)\}
 \tag{1.4}
\]

is a Johnson edge, with intersection \(R_X\) and union \(U_X\).

### Lemma 1.1 (distinct edges and no reverse pair)

The \(N\) edges \(e_X\), \(X\in\mathcal A\), are distinct.  Moreover,
\(g(X)\ne X\), and \(g(X)=Y\) implies \(g(Y)\ne X\).

#### Proof

The endpoints of a Johnson edge determine their intersection and union.
If \(e_X=e_Y\), then \(R_X=R_Y\); the SCD successor of that lower set is
unique, so \(X=Y\).  A fixed point is impossible because
\(a_X\ne b_X\).  A reverse pair would make the same diamond
\([R_X,U_X]\) belong to two distinct SCD chains, again contradicting the
uniqueness of the successor of \(R_X\).  \(\square\)

### Proposition 1.2 (exact central-diamond equivalence)

The following are equivalent.

1. Flipping every central diamond gives a second SCD with the same
   nonmiddle sets and the same singleton middle chains.
2. \(g\) is a permutation of \(\mathcal A\).
3. The edges \(e_X\) form a simple 2-factor on \(\mathcal A\), leaving
   precisely \(\mathcal E\) isolated.

When these conditions hold, the intersection colours of the factor are
all \((m-1)\)-sets exactly once and its union colours are all
\((m+1)\)-sets exactly once.  Its directed components are exactly the
cycles of \(g\), all of length at least four.

#### Proof

All nonmiddle ranks remain partitioned under the flip.  At rank \(m\),
the new nontrivial chains use the multiset \(g(\mathcal A)\), while the
singleton chains still use \(\mathcal E\).  These partition the middle
rank exactly if and only if \(g\) permutes \(\mathcal A\).

Every vertex of \(\mathcal A\) has one outgoing edge.  If \(g\) is a
permutation, it also has one incoming edge, and Lemma 1.1 turns these into
two distinct undirected edges.  Conversely, a 2-factor forces one incoming
edge at every active vertex and none outside, so \(g\) is a permutation of
\(\mathcal A\).  The colour assertion follows from (1.3), and the
component assertion follows from Lemma 1.1.  \(\square\)

To see the stronger length bound, every Johnson triangle is of one of two
types: either its three vertices contain a common \((m-1)\)-set, so all
three lower colours agree, or they lie in a common \((m+1)\)-set, so all
three upper colours agree. Double rainbowness excludes both types.

Thus a paired SCD gives exactly a **doubly-rainbow \(q=1\) Johnson
2-factor**.  It gives one Johnson cycle precisely when \(g\) is transitive.
The permutation condition alone gives only
\(1\le c(g)\le\lfloor N/4\rfloor\); it neither forces one component nor
asserts that every value in this range is realizable by an SCD.

## 2. Coordinate Euler balance and Catalan parity

Form the coordinate-swap multigraph \(Q\) on \([2m]\) by putting one
edge \(\{a_X,b_X\}\) for every \(X\in\mathcal A\).  Multiplicity is
retained.

### Lemma 2.1 (exact regularity)

Every coordinate has degree \(D\) in \(Q\).

#### Proof

For each flag \((R_X,U_X)\),

\[
 \mathbf1_{x\in U_X\setminus R_X}
 =\mathbf1_{x\in U_X}-\mathbf1_{x\in R_X}.
 \tag{2.1}
\]

Summing and using (1.3) gives

\[
\begin{aligned}
 d_Q(x)
 &=\binom{2m-1}{m}-\binom{2m-1}{m-2}\\
 &=\frac1{m+1}\binom{2m}m=D.
\end{aligned}
\tag{2.2}
\]

\(\square\)

### Lemma 2.2 (componentwise Euler orientation)

If \(g\) is a permutation, each component of \(Q\) contributed by one
cycle of \(g\) has a balanced orientation.  Hence every degree in \(Q\)
is even.

#### Proof

Orient the coordinate edge of the transition

\[
                         X\longmapsto X-a_X+b_X
\]

from \(a_X\) to \(b_X\).  Around a closed orbit of sets, every coordinate
is inserted as often as it is deleted.  Thus its indegree equals its
outdegree on that orbit.  Summing components proves the assertion.
\(\square\)

Theorem A now follows immediately from Lemmas 2.1--2.2.  For completeness,
the parity classification of the Catalan numbers is

\[
 v_2(\operatorname {Cat}_m)
 =s_2(m)-v_2(m+1),
 \tag{2.3}
\]

where \(s_2(m)\) is the number of ones in the binary expansion of \(m\).
The integer \(v_2(m+1)\) is the number of trailing ones of \(m\), so the
right-hand side vanishes exactly when all the ones of \(m\) are trailing,
that is, when \(m=2^a-1\).  Hence (0.7).

This proof uses only the closed middle-state orbits and the complete two
colour ledgers.  It therefore survives arbitrary chain priorities,
context-dependent recursion, and complement symmetry.

## 3. The omitted-family point and pair identities

Assume henceforth that \(g\) is a permutation.  Let

\[
 r_x=|\{E\in\mathcal E:x\in E\}|.
 \tag{3.1}
\]

Count incidences of \(x\) with the two endpoints of every edge \(e_X\).
For one diamond,

\[
 \mathbf1_{x\in X}+\mathbf1_{x\in g(X)}
 =\mathbf1_{x\in R_X}+\mathbf1_{x\in U_X}.
 \tag{3.2}
\]

Since the Johnson factor has degree two on \(\mathcal A\), summing gives

\[
 2\left(\binom{2m-1}{m-1}-r_x\right)
 =\binom{2m-1}{m-2}+\binom{2m-1}{m}.
 \tag{3.3}
\]

The right binomial simplification is \(2r_x=D\), proving (0.8).

Now fix a pair \(P=\{x,y\}\).  Put

\[
 r_P=|\{E\in\mathcal E:P\subseteq E\}|,
 \qquad
 \mu_P=|\{X\in\mathcal A:U_X\setminus R_X=P\}|.
 \tag{3.4}
\]

For one diamond the exact two-point identity is

\[
 \mathbf1_{P\subseteq X}+\mathbf1_{P\subseteq g(X)}
 =\mathbf1_{P\subseteq R_X}+\mathbf1_{P\subseteq U_X}
  -\mathbf1_{U_X\setminus R_X=P}.
 \tag{3.5}
\]

Indeed, the two middle corners both contain \(P\) when \(P\subseteq R_X\),
exactly one contains it when precisely one moving coordinate lies in
\(P\), and neither contains it when \(P=U_X\setminus R_X\).
Summing (3.5) yields

\[
 2\left(\binom{2m-2}{m-2}-r_P\right)
 =\binom{2m-2}{m-3}+\binom{2m-2}{m-1}-\mu_P.
 \tag{3.6}
\]

Therefore

\[
 \mu_P=2r_P-K_m,
 \tag{3.7}
\]

where

\[
\begin{aligned}
 K_m
 &=2\binom{2m-2}{m-2}
   -\binom{2m-2}{m-3}-\binom{2m-2}{m-1}\\
 &=\frac{m-2}{2m-1}\operatorname {Cat}_m.
\end{aligned}
\tag{3.8}
\]

This proves (0.9)--(0.10).  Notice that (3.7) is pointwise in the
coordinate pair; it is not an averaged point-margin statement.

For \(m=2\), the seed below has \(D=2\), \(K_2=0\), omitted family
\(\{13,24\}\), and swap multiplicities

\[
                         \mu_{13}=\mu_{24}=2,
 \tag{3.9}
\]

with every other \(\mu_P=0\), exactly as (3.7) requires.

## 4. Complement symmetry and the Kneser component reduction

Suppose, in addition, that the SCD is invariant under ordinary set
complementation and that complementation reverses its chains.  The flag
paired with \((R_X,U_X)\) is then

\[
                         (U_X^c,R_X^c).
 \tag{4.1}
\]

Define

\[
                         \tau(R_X)=U_X^c.
 \tag{4.2}
\]

Then \(R_X\cap\tau(R_X)=\varnothing\), and (4.1) gives
\(\tau^2(R_X)=R_X\).  Thus the complement orbits of flags form a perfect
matching of

\[
                         KG(2m,m-1).
 \tag{4.3}
\]

Each Kneser matching edge \(\{R,S\}\) lifts canonically to the two
complementary Johnson edges with lower colours \(R,S\).  The lift of the
matching is exactly the central diamond 2-factor.  Hence:

* its owner-degree condition is precisely that this lift have degree zero
  or two at every middle set;
* its components are precisely the cycles of \(g\);
* obtaining one middle cycle is precisely connectedness of the nonisolated
  lift.

This is a useful existence reduction, but a Kneser perfect matching alone
does not construct the lower and upper arms of an SCD.  Nor does ordinary
perfect-matching connectivity control the component structure of its
Johnson lift.

The explicit \(B_4\) seed uses the twisted anti-automorphism
\(S\mapsto\pi([4]\setminus S)\), with
\(\pi=(1\ 3)(2\ 4)\), rather than ordinary complementation.  That twist
may fix middle states, so the elementary argument that singleton chains
must occur in complement pairs is unavailable.  The Euler proof in
Section 2 is unaffected by the twist and is therefore the relevant
all-symmetry obstruction.

## 5. The exact \(B_4\) seed and direct tensor scaling

On \([4]\), the chains

\[
\begin{array}{ccl}
 \varnothing&\subset&1\subset14\subset124\subset1234,\\
 2&\subset&12\subset123,\\
 3&\subset&23\subset234,\\
 4&\subset&34\subset134,\\
 &&13,\\
 &&24
\end{array}
\tag{5.1}
\]

form an SCD and have central permutation

\[
                         14\to12\to23\to34\to14.
 \tag{5.2}
\]

Its lower colours are \(1,2,3,4\) and its upper colours are
\(124,123,234,134\), each exactly once.  It is therefore the smallest
positive paired-SCD seed.  Here \(m=2\) and \(D=2\), in agreement with
Theorem A.

Fix \(r\) disjoint four-coordinate blocks inside \([2m]\), and require
each block to be in one of the four active states in (5.2).  The number of
compatible global middle owners is exactly

\[
                         4^r\binom{2m-4r}{m-2r}.
 \tag{5.3}
\]

When \(m-2r\to\infty\), Stirling's formula gives

\[
 \frac{4^r\binom{2m-4r}{m-2r}}{\binom{2m}m}
 =(1+o(1))\,4^{-r}\sqrt{\frac m{m-2r}}.
 \tag{5.4}
\]

Thus a direct fixed tensor power is exponentially sparse as soon as
\(r\to\infty\).  Choosing active blocks context-dependently can repair
this owner census, but the next section shows that it cannot repair SCD
compatibility with only sparse seams.

## 6. Exact quartet flux

Fix disjoint quartets \(B_1,\ldots,B_b\), where
\(b=\lfloor m/2\rfloor\), and define

\[
 Z(S)=|\{i:B_i\subseteq S\}|-|\{i:B_i\cap S=\varnothing\}|.
 \tag{6.1}
\]

This function is monotone under inclusion.  Adding one coordinate changes
it by either zero or one.  Hence every central interval has

\[
                         0\le Z(U_X)-Z(R_X)\le2.
 \tag{6.2}
\]

Because the \(R_X\)'s and \(U_X\)'s exhaust their complete ranks, their
total flux is forced independently of all chain choices.

### Lemma 6.1 (exact mean central flux)

For every SCD,

\[
 \sum_{X\in\mathcal A}\bigl(Z(U_X)-Z(R_X)\bigr)
 =N\frac{2b(m-2)}{m(2m-1)}.
 \tag{6.3}
\]

#### Proof

For a uniformly chosen \(k\)-set and a fixed quartet, the probabilities of
being full and empty are

\[
 \frac{(k)_{\underline4}}{(2m)_{\underline4}},
 \qquad
 \frac{(2m-k)_{\underline4}}{(2m)_{\underline4}}.
 \tag{6.4}
\]

Therefore the mean difference between ranks \(m+1\) and \(m-1\) is

\[
 \frac{2b\bigl((m+1)_{\underline4}-(m-1)_{\underline4}\bigr)}
      {(2m)_{\underline4}}.
 \tag{6.5}
\]

Using

\[
 (m+1)_{\underline4}-(m-1)_{\underline4}
 =4(m-1)(m-2)(2m-3)
 \tag{6.6}
\]

reduces (6.5) to \(2b(m-2)/(m(2m-1))\).  Multiplication by \(N\) proves
(6.3).  \(\square\)

By (6.2), at least half of the total flux in (6.3) must come from distinct
positive-flux diamonds.  This proves (0.11).

A pure central \(B_4\) transition has local lower rank one and local upper
rank three in its active quartet.  Neither local set is empty or full, so
its \(Z\)-flux is zero; all frozen quartets contribute equally at the two
ends.  Thus every positive-flux diamond counted by (0.11) must be
off-centre, cross-quartet, or expressed in a changed quartet frame.  This
proves Theorem B.

The conclusion applies in particular to a first-eligible packetization
using the four states (5.2) in a fixed disjoint quartet partition.  Such a
packetization can cover \(W-o(W)\) middle owners and can have excellent
internal Johnson cycles, but its central transitions all have zero
quartet flux.  Since every SCD requires \((1/4+o(1))W\) nonzero-flux
central diamonds, deleting the \(D=O(W/m)\) singleton-chain owners and
adding \(o(W)\) seams cannot promote it to a paired SCD.

## 7. Precise proved and open boundary

What is proved is:

1. an exact paired central flip is impossible in every Mersenne Catalan
   dimension \(m=2^a-1\);
2. every surviving exact pair must satisfy the point design (0.8), the
   pointwise pair identity (0.9), and the doubly-rainbow Johnson 2-factor
   condition;
3. ordinary complement symmetry reduces component control to the
   2-regular/connected lift of a Kneser perfect matching;
4. the complement-symmetric \(B_4\) seed is valid, but fixed tensor powers
   have the sparse owner census (5.3)--(5.4), while context-dependent
   fixed-frame packings require \(\Omega(W)\) genuinely noncentral
   transitions by (0.11).

What remains unproved is existence in every parity-admissible dimension
\(m\ne2^a-1\).  In particular, no argument here constructs the dense
moving-frame recursion required by Theorem B, proves that its Johnson lift
has few components, or joins those components while retaining the two
rainbow colour ledgers.  The all-\(m\) exact theorem is definitively closed;
an all-admissible-\(m\) theorem and an asymptotic \(o(W)\)-leave theorem
remain open.
