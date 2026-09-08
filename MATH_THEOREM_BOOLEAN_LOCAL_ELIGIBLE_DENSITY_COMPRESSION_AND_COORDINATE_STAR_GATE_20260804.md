# Boolean-local eligible densities, shifted cut containers, and the coordinate-star gate

**Date:** 2026-08-04  
**Status:** unconditional deterministic eligible-density bounds, an
unconditional compression theorem for the local first-moment functional,
and an exact half-density classification at the top lower rank.  Principal
coordinate stars are checked at the optimal depth at the level of their
unavoidable core, and the locally uniform benchmark is strictly safe on
coordinate halfspaces.  This note does **not** prove the all-
\(Q\) multisocket cut, a switching MGF, or a path-bank construction.  No
computation is used.

## 0. Outcome

Put

\[
 n=2r,\qquad \mathcal O=\binom{[2r]}r,\qquad
 W=|\mathcal O|,\qquad C_s=\binom{2r}s,
\tag{0.1}
\]

and fix a floor/ceiling-balanced owner-path bank.  At rank \(s<r\), write

\[
 D_s=\binom{2r-s}{r-s},\qquad
 h_Q(S)=|\{T\in Q:S\subseteq T\}|,
\tag{0.2}
\]

and

\[
 m_s=\left\lfloor\frac W{C_s}\right\rfloor,
 \quad M_s=m_s+1,
 \quad a_s=(m_s+1)C_s-W,
 \quad c_s=W-m_sC_s.
\tag{0.3}
\]

The first result is a deterministic Boolean-local sandwich.  If
\(A_j(Q)=|\{S:h_Q(S)\ge j\}|\), then

\[
 |\{S:h_Q(S)=D_s\}|\le e_s(Q)\le F_s(Q),
\tag{0.4}
\]

where \(F_s(Q)\) is the value of the two-variable integer program

\[
 \max(x+y):
 \begin{cases}
 0\le x\le a_s,\quad 0\le y\le c_s,\\
 x+y\le A_{m_s}(Q),\quad y\le A_{m_s+1}(Q),\\
 m_sx+(m_s+1)y\le |Q|.
 \end{cases}
\tag{0.5}
\]

There is also a complementary sorted-capacity bound in Theorem 1.1.
Unlike the global rank envelope, both bounds see the eligible-owner
profile \(h_Q\).  They are unconditional, but they still discard
cross-rank nesting.

The local hypergeometric benchmark from
`MATH_THEOREM_RANDOM_BALANCED_PATH_LOCAL_DENSITY_AND_SWITCHING_GATE_20260804.md`
is

\[
 \mathcal B_s(Q)=\sum_{S\in\binom{[2r]}s}g_s(h_Q(S)),
\tag{0.6}
\]

where

\[
 g_s(h)=\frac{a_s}{C_s}\frac{(h)_{m_s}}{(D_s)_{m_s}}
 +\frac{c_s}{C_s}\frac{(h)_{m_s+1}}{(D_s)_{m_s+1}}.
\tag{0.7}
\]

This functional has a genuine compression theorem:

\[
 \boxed{\mathcal B_s(C_{ij}Q)\ge \mathcal B_s(Q)}.
\tag{0.8}
\]

Thus, at every fixed cardinality, a worst family for the **local first
moment** may be taken shifted, equivalently a downset in the usual
dominance order on \(r\)-sets.  The statement is not extended to the
actual deterministic \(e_s(Q)\) or to the exponential-moment functional;
the needed convexity is absent there.

The gap from the linear incidence bound has an exact Boolean energy lower
bound.  Put

\[
 \lambda_s=
 \begin{cases}
 c_s/C_s,&m_s=1,\\
 1,&m_s\ge2.
 \end{cases}
\tag{0.9}
\]

Then

\[
 \boxed{
 \frac{C_s}{W}|Q|-\mathcal B_s(Q)
 \ge
 \frac{\lambda_s}{D_s(D_s-1)}
 \sum_{T\in Q}\sum_{U\notin Q}
 \binom{|T\cap U|}{s}.}
\tag{0.10}
\]

For every nonempty proper \(Q\), the gap is strict.  This both explains
why coordinate families are exceptional and identifies the correct
container energy: it is a weighted Johnson-local edge boundary, not a
function of \(|Q|\).

At \(s=r-1\), (0.10) is an equality and the energy is the edge boundary
in \(J(2r,r)\).  Its exact spectral inequality gives

\[
 \mathcal B_{r-1}(Q)
 \le \frac{C_{r-1}}W|Q|
 -\frac{2|Q|(1-|Q|/W)}{r(r+1)}.
\tag{0.11}
\]

At half density, equality holds exactly for the \(4r\) coordinate
halfspaces

\[
 \{T:x\in T\},\qquad \{T:x\notin T\}.
\tag{0.12}
\]

This is a complete, sharp one-rank container classification.  It does not
classify the sum over all ranks.

Finally, for a fixed \(t\)-set \(A\), the principal coordinate star

\[
 Q_A=\{T\in\mathcal O:A\subseteq T\}
\tag{0.13}
\]

has forced core at rank \(s\) exactly
\(\{S:A\subseteq S\}\).  If \(t\) is fixed and \(r\to\infty\), then

\[
 \frac{1}{|Q_A|}\sum_{s<r}|\{S:A\subseteq S\}|
 =\frac{\sqrt\pi}{2}\sqrt r-\frac{t+1}{2}+O_t(r^{-1/2}).
\tag{0.14}
\]

The optimal depth satisfies
\(d\ge(\sqrt\pi/2)\sqrt r-1/2+o(1)\), more precisely the comparison in
Section 5 uses the exact triangular definition.  Hence every fixed-width
principal star's unavoidable core passes the Hall cut, with asymptotic
depth margin \(t/2\) per owner.  For \(t=1\), the locally uniform weighted
benchmark has in addition a strict top-rank margin

\[
 \frac{N_{r-1}}{C_{r-1}}\frac{W}{2r(r+1)}.
\tag{0.15}
\]

This verifies the coordinate boundary case for the correct local
first-moment model.  It does not bound the realized leakage
\(e_s(Q_x)-\binom{2r-1}{s-1}\) in one deterministic path bank.

## 1. Deterministic eligible-density bounds

At rank \(s\), the visitor sets \(V_s(S)\) partition \(\mathcal O\).
Exactly \(a_s\) blocks have size \(m_s\), and exactly \(c_s\) have size
\(m_s+1\).  Also

\[
 V_s(S)\subseteq \mathcal U_s(S):=\{T:S\subseteq T\}.
\tag{1.1}
\]

### Theorem 1.1 (eligible-density sandwich)

For every \(Q\subseteq\mathcal O\), let \(R=\mathcal O\setminus Q\).
Then (0.4)--(0.5) hold.

There is a second upper bound.  Arrange the \(C_s\) integers

\[
 \gamma_S=\min\{M_s,h_R(S)\}
\tag{1.2}
\]

in nonincreasing order
\(\gamma_{(1)}\ge\cdots\ge\gamma_{(C_s)}\), and put

\[
 \kappa_s(R)=\min\left\{j:
       \sum_{i=1}^j\gamma_{(i)}\ge |R|\right\}.
\tag{1.3}
\]

Use the convention \(\kappa_s(\varnothing)=0\).

Then

\[
 \boxed{e_s(Q)\le C_s-\kappa_s(R).}
\tag{1.4}
\]

### Proof

If \(h_Q(S)=D_s\), every eligible owner of \(S\) belongs to \(Q\).
By (1.1), \(V_s(S)\subseteq Q\), proving the lower bound in (0.4).

Let \(x\) and \(y\) be the numbers of captured visitor blocks of sizes
\(m_s\) and \(m_s+1\).  There are only \(a_s\) and \(c_s\) blocks of
the respective sizes.  A captured block of size \(j\) requires at least
\(j\) eligible owners in \(Q\), so

\[
 x+y\le A_{m_s}(Q),\qquad y\le A_{m_s+1}(Q).
\tag{1.5}
\]

Captured blocks are disjoint subsets of \(Q\), whence

\[
 m_sx+(m_s+1)y\le |Q|.
\tag{1.6}
\]

Thus \((x,y)\) is feasible in (0.5), and
\(e_s(Q)=x+y\le F_s(Q)\).

For the complementary bound, let

\[
 n_S=|V_s(S)\cap R|.
\tag{1.7}
\]

Every owner of \(R\) occurs in exactly one visitor block, so
\(\sum_Sn_S=|R|\).  Moreover

\[
 n_S\le |V_s(S)|\le M_s,
 \qquad n_S\le h_R(S),
\tag{1.8}
\]

and hence \(n_S\le\gamma_S\).  If \(u_s(R)\) targets are hit by
\(R\), the sum of the corresponding \(u_s(R)\) capacities is at least
\(|R|\).  The largest possible sum of \(j\) capacities is the sum of
the first \(j\) sorted values, so \(u_s(R)\ge\kappa_s(R)\).  The exact
identity \(e_s(Q)=C_s-u_s(R)\) now gives (1.4). \(\square\)

The bounds use only one-rank information.  They are therefore safe inputs
to a later container argument, but they cannot certify that the same
\(Q\) is harmless at all ranks.

## 2. Compression of the local first moment

For \(i<j\), the usual \((i,j)\)-shift replaces
\(T\ni j, i\notin T\) by
\((T\setminus\{j\})\cup\{i\}\) when the latter set is not already in
the family.  Denote the shifted family by \(C_{ij}Q\).

### Lemma 2.1 (convex eligible-density compression)

If \(\varphi:\{0,1,\ldots,D_s\}\to\mathbb R\) is discretely convex,
then

\[
 \sum_{S\in\binom{[2r]}s}\varphi(h_{C_{ij}Q}(S))
 \ge
 \sum_{S\in\binom{[2r]}s}\varphi(h_Q(S)).
\tag{2.1}
\]

### Proof

Targets containing neither or both of \(i,j\) have unchanged eligible
counts.  Pair the remaining targets as

\[
 A\cup\{i\},\qquad A\cup\{j\},qquad |A|=s-1.
\tag{2.2}
\]

For a fixed \(A\), ignore the common owners containing both coordinates.
Among the remaining owner pairs indexed by
\(B\supseteq A\), \(|B|=r-1\), let \(p\) be the number with occupancy
pattern \((1,0)\) in \((Q_i,Q_j)\), and \(q\) the number with pattern
\((0,1)\).  Shifting replaces all \((0,1)\) patterns by \((1,0)\).
Therefore the sum of the two counts in (2.2) is unchanged, while the
absolute value of their difference changes from \(|p-q|\) to \(p+q\).
The shifted pair majorizes the original pair.  Discrete convexity gives
the desired inequality for this pair, and summing over \(A\) proves
(2.1). \(\square\)

### Theorem 2.2 (shifted first-moment reduction)

For every \(s<r\),

\[
 \mathcal B_s(C_{ij}Q)\ge\mathcal B_s(Q).
\tag{2.3}
\]

Consequently, for fixed \(|Q|\), the maximum of any nonnegative weighted
sum \(\sum_s w_s\mathcal B_s(Q)\) is attained by a shifted family.

### Proof

For every \(\ell\ge1\), the integer function
\((h)_\ell=\ell!\binom h\ell\) is discretely convex, since its second
difference is

\[
 \Delta^2\binom h\ell=\binom h{\ell-2}\ge0.
\tag{2.4}
\]

Thus \(g_s\), a nonnegative linear combination of two such functions,
is discretely convex.  Apply Lemma 2.1.  Iterating all shifts terminates
at a shifted family without decreasing the functional. \(\square\)

This is the promised downset reduction, with two important limits.
First, \(e_s(Q)\) depends on the realized visitor blocks and is not the
functional (0.6).  Second,
\(h\mapsto\log(1+(z^{w_s}-1)g_s(h))\) need not be convex.  Hence
Theorem 2.2 does not prove compression of the switching MGF or of its
entropy sum.

## 3. Exact local energy

### Theorem 3.1 (weighted Johnson-boundary gap)

For every \(Q\subseteq\mathcal O\), (0.10) holds.  More precisely,

\[
 \sum_Sh_Q(S)(D_s-h_Q(S))
 =\sum_{T\in Q}\sum_{U\notin Q}\binom{|T\cap U|}{s}.
\tag{3.1}
\]

If \(\varnothing\ne Q\ne\mathcal O\), then

\[
 \mathcal B_s(Q)<\frac{C_s}{W}|Q|.
\tag{3.2}
\]

### Proof

For \(m_s=1\), direct subtraction in (0.7) gives

\[
 \frac h{D_s}-g_s(h)
 =\frac{c_s}{C_s}
   \frac{h(D_s-h)}{D_s(D_s-1)}.
\tag{3.3}
\]

For \(m_s\ge2\), the probability that a uniformly chosen eligible
\(\ell\)-set lies in a fixed \(h\)-set decreases with \(\ell\).  Hence

\[
 g_s(h)\le\frac{(h)_2}{(D_s)_2},
\tag{3.4}
\]

and therefore

\[
 \frac h{D_s}-g_s(h)
 \ge\frac{h(D_s-h)}{D_s(D_s-1)}.
\tag{3.5}
\]

Double counting incidences gives

\[
 \sum_S\frac{h_Q(S)}{D_s}=\frac{C_s}{W}|Q|.
\tag{3.6}
\]

Summing (3.3) or (3.5) and using (3.6) proves (0.10).

For (3.1), choose an \(s\)-set \(S\), an owner \(T\in Q\) containing
it, and an owner \(U\notin Q\) containing it.  For fixed \((T,U)\),
there are exactly \(\binom{|T\cap U|}{s}\) choices of \(S\).

If the right side of (3.1) vanished, every eligible star
\(\mathcal U_s(S)\) would lie wholly in \(Q\) or wholly outside it.
Adjacent vertices of \(J(2r,r)\) share an \((r-1)\)-set and hence an
\(s\)-set, so they would have the same membership.  The Johnson graph is
connected, forcing \(Q=\varnothing\) or \(Q=\mathcal O\).  Thus every
nontrivial \(Q\) has positive energy.  Since \(\lambda_s>0\) at every
strict lower rank, (3.2) follows. \(\square\)

Equation (3.1) is the Boolean-local replacement for the invalid global
density \(|Q|/W\).  It also gives a precise target for a container theorem:
low first-moment gap means small boundary simultaneously in several
Johnson-distance graphs.

## 4. The sharp top-rank container

Let \(J(2r,r)\) join two owners when their intersection has size
\(r-1\), and write \(\partial_JQ\) for its unordered edge boundary.

### Lemma 4.1 (Johnson Poincare inequality and equality)

For every \(Q\subseteq\mathcal O\),

\[
 |\partial_JQ|\ge2r|Q|\left(1-\frac{|Q|}{W}\right).
\tag{4.1}
\]

For a nonempty proper family, equality is possible only when
\(|Q|=W/2\), and then \(Q\) is one of the coordinate halfspaces (0.12).

### Proof

The Johnson graph is \(r^2\)-regular.  Its adjacency eigenvalues are

\[
 \theta_j=(r-j)^2-j\qquad(0\le j\le r),
\tag{4.2}
\]

so its Laplacian eigenvalues are

\[
 \mu_j=j(2r-j+1).
\tag{4.3}
\]

For completeness, (4.2) follows by decomposing functions on the
\(r\)-layer into the successive orthogonal differences of the inclusion
spaces generated by functions on \(j\)-sets; counting the swaps which
preserve, delete, or add a fixed \(j\)-set gives (4.2).  In particular,
the first positive eigenvalue is \(2r\).

Apply the spectral gap to
\(f=1_Q-|Q|/W\).  Its squared norm is
\(|Q|(1-|Q|/W)\), while its Laplacian quadratic form is exactly
\(|\partial_JQ|\).  This proves (4.1).

Equality puts \(f\) in the first eigenspace, so

\[
 1_Q(T)=c+\sum_{i\in T}\alpha_i,\qquad \sum_i\alpha_i=0.
\tag{4.4}
\]

Swapping \(i\) for \(j\) shows that every difference
\(\alpha_i-\alpha_j\) is in \(\{-1,0,1\}\).  Thus the coefficients have
at most two levels, separated by one.  If the high-level coordinate set
has size between \(2\) and \(2r-2\), the quantity in (4.4) takes at
least three values as \(|T\cap A|\) varies, contradicting
\(1_Q\in\{0,1\}\).  Hence the high-level set, or its complement, is a
singleton.  These are exactly the coordinate halfspaces, all of size
\(W/2\). \(\square\)

### Theorem 4.2 (exact half-density maximizers of the local benchmark)

At rank \(s=r-1\), for every \(Q\), equation (0.11) holds.  If
\(|Q|=W/2\), equality holds precisely for the coordinate halfspaces.

### Proof

Here

\[
 C_{r-1}=\frac r{r+1}W,\quad D_{r-1}=r+1,\quad
 m_{r-1}=1,\quad \frac{c_{r-1}}{C_{r-1}}=\frac1r.
\tag{4.5}
\]

Also (3.1) is exactly \(|\partial_JQ|\), since an adjacent owner pair
has a unique common \((r-1)\)-set.  Thus (3.3) gives the identity

\[
 \frac{C_{r-1}}W|Q|-\mathcal B_{r-1}(Q)
 =\frac{|\partial_JQ|}{r^2(r+1)}.
\tag{4.6}
\]

Insert Lemma 4.1.  Its equality classification gives the final claim.
\(\square\)

This theorem rigorously identifies coordinate halfspaces as the worst
half-density families for one rank of the correct Boolean-local model.
It is the first exact container layer, not an all-rank container theorem.

## 5. Principal coordinate stars and the optimal boundary

Fix \(A\in\binom{[2r]}t\), where \(t\ge1\) is fixed, and put

\[
 Q_A=\{T:A\subseteq T\},\qquad
 q_t=|Q_A|=\binom{2r-t}{r-t}.
\tag{5.1}
\]

### Proposition 5.1 (exact forced core)

For \(s<r\),

\[
 h_{Q_A}(S)=D_s
 \quad\Longleftrightarrow\quad A\subseteq S.
\tag{5.2}
\]

Consequently the unavoidable part of the principal-star Hall cut is

\[
 K_t:=\sum_{s=1}^{r-1}|\{S:A\subseteq S\}|
 =\sum_{j=0}^{r-t-1}\binom{2r-t}{j}.
\tag{5.3}
\]

For every fixed \(t\),

\[
 \frac{K_t}{q_t}
 =\frac{K_0}{W}-\frac t2+O_t(r^{-1/2}),
\qquad
 K_0=\sum_{j=0}^{r-1}\binom{2r}{j}.
\tag{5.4}
\]

### Proof

If \(A\subseteq S\), every owner containing \(S\) contains \(A\).  If
some \(a\in A\setminus S\), then \(S\) can be extended to an \(r\)-set
while omitting \(a\), so not every eligible owner lies in \(Q_A\).
This proves (5.2), and (5.3) follows by deleting the fixed set \(A\).

Let \(K_j\) and \(q_j\) denote the quantities in (5.3) and (5.1) with
\(t=j\).  Pascal's identity gives

\[
 K_j=2K_{j+1}+q_{j+1},
 \qquad
 \frac{q_{j+1}}{q_j}=\frac{r-j}{2r-j}.
\tag{5.5}
\]

Writing \(z_j=K_j/q_j\), this is

\[
 z_{j+1}=z_j-\frac12+\frac{jz_j}{2(r-j)}.
\tag{5.6}
\]

The central-binomial estimate gives \(z_j=O(\sqrt r)\) for fixed \(j\).
Iterating (5.6) a fixed number of times proves (5.4). \(\square\)

### Corollary 5.2 (the forced coordinate core passes at optimal depth)

Let

\[
 \Lambda=\sum_{s=1}^{r-1}C_s,qquad
 d=\min\left\{q:qW+\binom{q+1}{2}\ge\Lambda\right\},
\tag{5.7}
\]

and let \(b_s\ge0\) be any triangular boundary multiplicities.  For each
fixed \(t\ge1\), and all sufficiently large \(r\),

\[
\sum_s\left(\binom{2r-t}{s-t}-b_s\right)_+
 \le K_t<dq_t.
\tag{5.8}
\]

Here \(\binom{2r-t}{s-t}=0\) when \(s<t\).

More precisely, if
\(\sigma_r=d-K_0/W\), then \(\sigma_r\ge-o(1)\) and

\[
 d-\frac{K_t}{q_t}
 =\frac t2+\sigma_r+O_t(r^{-1/2})
 \ge\frac t2-o_t(1).
\tag{5.9}
\]

### Proof

Since \(K_0=\Lambda+1\), (5.7) gives

\[
 d\ge\frac{K_0}{W}
 -\frac{\binom{d+1}{2}+1}{W}.
\tag{5.10}
\]

Here \(d=O(\sqrt r)\), so the last fraction is \(o(1)\).  Combine
(5.4) and (5.10).  Boundary subtraction only decreases the left side of
(5.8). \(\square\)

For \(t=1\), \(q_1=W/2\) and

\[
 \frac{K_1}{q_1}=\frac{K_0}{W}-\frac12
\tag{5.11}
\]

holds exactly.  Thus the unavoidable coordinate-halfspace core has
asymptotic capacity slack \(W/4\), before realized leakage is counted.

### Corollary 5.3 (strict safety of the local coordinate benchmark)

Let \(Q_x=\{T:x\in T\}\), let \(N_s=C_s-b_s\), and put
\(N=\sum_sN_s\le dW\).  Then

\[
 \sum_s\frac{N_s}{C_s}\mathcal B_s(Q_x)
 \le \frac N2-\frac{N_{r-1}}{C_{r-1}}
                 \frac{W}{2r(r+1)}
 <\frac{dW}{2}
\tag{5.12}
\]

whenever \(N_{r-1}>0\).

### Proof

The local incidence bound gives
\(\mathcal B_s(Q_x)\le C_s/2\) at every rank.  At rank \(r-1\),
Theorem 4.2 is sharp on \(Q_x\), and its strict deficit is
\(W/(2r(r+1))\).  Weight and sum.  Since \(N\le dW\), (5.12) follows.
\(\square\)

Corollary 5.3 is a statement about the locally uniform benchmark.  It is
not a concentration theorem and not a deterministic upper bound for one
sampled path bank.

## 6. Exact remaining gate

The proof-safe reduction is now narrower than a generic call for
"decorrelation."

1. The realized cut has the deterministic eligible-density bounds in
   Theorem 1.1.
2. The correct first moment compresses to shifted owner families by
   Theorem 2.2.
3. Its deficit is the Johnson-local energy (3.1).
4. At the top lower rank and half density, coordinate halfspaces are the
   unique extremizers.
5. Fixed-width principal coordinate stars have enough scalar room at the
   optimal depth, and coordinate halfspaces are strictly safe in the
   local first-moment model.

What remains unproved is a theorem of either of the following forms.

\[
 \boxed{
 \begin{array}{l}
 \text{a switching law controlling the realized }e_s(Q)
 \text{ uniformly over shifted low-energy }Q;\\
 \text{or a deterministic multi-rank expansion theorem showing that}\
 \text{the bounds of Theorem 1.1 sum to at most }d|Q|.
 \end{array}}
\tag{6.1}
\]

Theorem 2.2 does not reduce (6.1) to coordinate juntas, and Theorem 4.2
does so only at one rank and one density.  In particular, no complete
multisocket Hall theorem, residual nonadjacency lift, or named lower flag
factor is claimed.
