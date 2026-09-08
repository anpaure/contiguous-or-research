# Exact candidate degrees for first-eligible \(B_4\) packets and the critical lognormal cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, Poisson
surrogate, or generic nibble theorem is used.

## 0. Verdict

Fix the local four-cycle

\[
 \mathcal A={14,12,23,34\}\subseteq\binom{[4]}2,
 \tag{0.1}
\]

and form the canonical first-\(r\)-eligible packet partition.  Let

\[
 W=\binom{2m}{m},\qquad r=o(m),\qquad H\ll r,
 \tag{0.2}
\]

with \(r\) a power of two and packet dimension \(h=2r\).

For a signed depth-\(q\) target \(T\), call a block \(E\) when its local
restriction belongs to \(\mathcal A\), and call it \(C^-\) when the
restriction is a singleton or \(C^+\) when it is a triple.  Put

\[
                         k=r-q+1,
 \tag{0.3}
\]

and let \(Z_q^\pm(T)\) be the number of \(C^\pm\)-blocks before the
\(k\)-th \(E\)-block.  If the \(k\)-th \(E\)-block does not exist, use
all \(C\)-blocks, but retain the target only when there are exactly
\(r-q=k-1\) \(E\)-blocks.

Then the exact physical candidate-packet degree is

\[
 \boxed{
 d_q^\pm(T)=\binom{Z_q^\pm(T)}q.}                    \tag{0.4}
\]

For the full legal support-preserving local-automorphism and block-
permutation menu, a candidate packet selects its unique physical face in
the exact fraction

\[
                         p_{r,q}={1\over\binom rq}.    \tag{0.5}
\]

Thus the barycentric candidate load is

\[
                         L_q^\pm(T)
 ={\binom{Z_q^\pm(T)}q\over\binom rq}.                \tag{0.6}
\]

Its mean is exactly critical:

\[
 \boxed{
 {1\over N_q}\sum_TL_q^\pm(T)={G\over N_q}=1+o(1),} \tag{0.7}
\]

where \(G=W-e^{-\Omega(m)}W\) is the retained owner mass and
\(N_q=\binom{2m}{m-q}\).

The requested lower-tail theorem is nevertheless false.  If

\[
                         q=c\sqrt r+o(\sqrt r),
 \qquad c>0,
 \tag{0.8}
\]

then, under the uniform physical target layer,

\[
 \boxed{
 L_q^\pm(T) \Longrightarrow\
 \exp\{-c^2+\sqrt2cN\},qquad N\sim N(0,1).}         \tag{0.9}
\]

Consequently

\[
 \boxed{
 {1\over N_q}\sum_T(1-L_q^\pm(T))_+
 \longrightarrow
 \delta(c):=2\Phi(c/\sqrt2)-1>0.}                   \tag{0.10}
\]

Since \(r=o(m)\), one has \(N_q=(1-o(1))W\) at this depth.  Therefore,
whenever \(H\ge c\sqrt r\), the candidate-degree lower tail contains
\((\delta(c)+o(1))W\) mass at one signed rank.  It is not \(o(W)\) in
aggregate through \(H\).

Here and below, a *block permutation* means a permutation of the \(r\)
already selected four-blocks.  This is the owner-preserving group relevant
to one-state-per-packet rounding.  A permutation of all \(b\) ambient
blocks changes which blocks are first eligible and hence changes the
packet atlas.

The phrase "all 24 local relabellings" requires a legality correction.
The stabilizer of \(\mathcal A\) in \(S_4\) has order eight.  Those eight
relabelings are the full local \(Q_2\)-automorphism group and are legal
states of one fixed packet.  The other sixteen relabelings send
\(\mathcal A\) to one of the other two four-cycles in \(K_4\), and hence
change the first-eligible packet partition itself.  They are not
one-state-per-packet alternatives on a common owner support.

Even if one formally averages the three packet atlases represented by the
24 relabelings, the lower tail stays linear.  The three normalized loads
converge jointly to correlated lognormals whose underlying Gaussian
correlation is \(3/4\).  Their average has a strictly positive lower-tail
defect.

If one goes further and formally averages independent local labels and all
ambient block orders, the exact pointwise load is (6.14).  This averaging
does remove the \(\sqrt r\) stopping fluctuation, but not the physical
profile fluctuation.  At \(q=A\sqrt m\),

\[
 \log\overline L_q(T)\Longrightarrow
 -{14\over3}A^2+\sqrt{{34\over3}}\,A\,N.             \tag{0.11}
\]

Thus a positive fraction of physical targets is still deficient.  In the
smaller range \(H=o(\sqrt m)\), the aggregate formal deficit is
\(\asymp WH^2/\sqrt m\), so it is \(o(W)\) only when
\(H=o(m^{1/4})\).

Independent one-state-per-packet selection also fails exactly, not by a
Poisson analogy.  Conditional on \(T\), its miss probability is

\[
                         (1-p_{r,q})^{d_q(T)},         \tag{0.12}
\]

and (0.9) makes the mean miss fraction converge to

\[
 \mathbb E\exp\{-e^{-c^2+\sqrt2cN}\}>0.              \tag{0.13}
\]

At \(q\asymp\sqrt r\), degrees alone do not rule out a specially correlated
integral selection.  At every Gaussian depth \(q=A\sqrt m\), however, the
frozen-suffix weight of Section 8 gives a statewise Hall deficit
\(\kappa_AW-o(W)\), even for fractional mixtures of whole components.
Thus the proposed lower-tail and rounding route fails twice: the degree
estimate is false in the required range, and the 24-way average is not a
legal multiple-choice menu for a fixed packet partition.

## 1. The three local four-cycles and the legality of relabelling

The six two-subsets of \([4]\) are the edges of \(K_4\).  A four-cycle
support is the complement of one perfect matching.  Let

\[
 M_1=13|24,qquad M_2=14|23,qquad M_3=12|34,
 \tag{1.1}
\]

and put

\[
                         \mathcal A_\lambda
 =E(K_4)\setminus M_\lambda.                          \tag{1.2}
\]

After relabelling, (0.1) is one of these three supports.

### Lemma 1.1 (the \(S_4\)-orbit)

The \(S_4\)-orbit of \(\mathcal A\) contains exactly the three supports
\(\mathcal A_1,\mathcal A_2,\mathcal A_3\).  Every support occurs for
exactly eight of the 24 coordinate permutations.  Moreover,

\[
 |\mathcal A_\lambda\cap\mathcal A_\mu|=2
 \quad(\lambda\ne\mu),
 \qquad
 \bigcap_{\lambda=1}^3\mathcal A_\lambda=\varnothing. \tag{1.3}
\]

#### Proof

The three perfect matchings form one transitive \(S_4\)-orbit.  The
stabilizer of a matching, equivalently of its complementary four-cycle,
is the dihedral group of order eight.  Orbit--stabilizer proves the first
two claims.  Distinct perfect matchings are disjoint and together contain
four of the six edges, proving (1.3). \(\square\)

For a packet

\[
                         \mathcal P\cong\mathcal A_\lambda^r,
 \tag{1.4}
\]

only \(\operatorname {Stab}_{S_4}(\mathcal A_\lambda)\cong D_8\) acts on
the same owner support.  A relabelling outside this stabilizer maps (1.4)
to a different subset of the middle layer.  Applying such choices
independently to overlapping packets destroys the exact owner partition.

Hence the legal fixed-atlas menu is generated by

\[
                         D_8^r\rtimes S_r.             \tag{1.5}
\]

The 24 relabelings instead describe three complete alternative packet
atlases, each repeated eight times.

## 2. Exact physical candidate-packet degree

Fix one atlas \(\lambda\).  Its ordered four-blocks are

\[
                         B_1<B_2<\cdots<B_b,
 \qquad b=\lfloor m/2\rfloor,                         \tag{2.1}
\]

with at most three residual coordinates.

For a lower target \(T\in\binom{[2m]}{m-q}\), write

\[
 E_\lambda(T)=\{i:T\cap B_i\in\mathcal A_\lambda\},
 \qquad
 C^-(T)=\{i:|T\cap B_i|=1\}.                         \tag{2.2}
\]

For an upper target use

\[
 E_\lambda(T)=\{i:T\cap B_i\in\mathcal A_\lambda\},
 \qquad
 C^+(T)=\{i:|T\cap B_i|=3\}.                         \tag{2.3}
\]

Every singleton is the lower label of exactly one edge of the local cycle,
and every triple is the upper label of exactly one edge.  Thus a chosen
\(C^\pm\)-block has one unique local candidate edge.

Let \(Z_{\lambda,q}^\pm(T)\) count the \(C^\pm\)-blocks before the
\((r-q+1)\)-st \(E_\lambda\)-block.  If that block does not exist, use all
\(C^\pm\)-blocks and declare the count admissible only when the target has
exactly \(r-q\) \(E_\lambda\)-blocks in total.

### Theorem 2.1 (exact degree formula)

The number of canonical packets of atlas \(\lambda\) in which \(T\) is
the signed trace of a block-simple affine \(q\)-face is

\[
 \boxed{
 d_{\lambda,q}^\pm(T)
 =\binom{Z_{\lambda,q}^\pm(T)}q.}                    \tag{2.4}
\]

#### Proof

Choose the \(q\) touched blocks \(D\subseteq C^\pm(T)\), and complete
their unique local edges to middle rank.  The eligible blocks of every
middle owner in the resulting face are exactly

\[
                         E_\lambda(T)\cup D.           \tag{2.5}
\]

The canonical packet selects the first \(r\) indices of (2.5).  All
members of \(D\) belong to that list if and only if the largest member of
\(D\) has at most \(r-q\) members of \(E_\lambda(T)\) before it.  This is
equivalent to

\[
 D\subseteq
 \{C^\pm\text{-blocks before the }(r-q+1)\text{-st }E_\lambda\}.
 \tag{2.6}
\]

If the stopping \(E\)-block is absent, a good completed owner requires
exactly \(r-q\) existing \(E\)-blocks, giving the stated convention.
Every admissible \(D\) determines the selected block list, exterior, and
therefore one packet.  Conversely every candidate packet supplies its
touched set \(D\).  This is a bijection, proving (2.4). \(\square\)

The formula is physical: different \(D\)'s give different canonical
packets, while the local singleton/triple labels determine the unique face
inside each packet.

## 3. Block permutations and the exact menu fraction

Inside a packet, the two local directions of every four-block are bottom
siblings in the recursive trace-injective factor.  Hence every
\(q\le r\) selected face is block-simple: it uses one direction in each of
\(q\) different blocks.

### Proposition 3.1 (transitive legal menu)

The group \(D_8^r\rtimes S_r\) acts transitively on the block-simple
affine \(q\)-faces of \(Q_{2r}\).  Their number is

\[
                         \binom rq4^r.                 \tag{3.1}
\]

The recursive factor selects exactly \(4^r\) such faces.  Therefore a
fixed candidate face is selected in exactly the fraction

\[
 \boxed{p_{r,q}=1/\binom rq}                          \tag{3.2}
\]

of the complete legal menu.

#### Proof

Choose the \(q\) touched blocks.  In a touched \(Q_2\), choose one of two
directions and one of two values of the fixed direction, giving four local
edges.  In an untouched block choose one of four vertices.  This proves
(3.1).  The group \(D_8=\operatorname {Aut}(Q_2)\) is transitive on the
four edges and on the four vertices, while \(S_r\) is transitive on the
touched block sets.  Hence the wreath action is transitive.

Packetwise shadow injectivity gives one distinct affine \(q\)-face at each
of the \(4^r\) starts.  Orbit averaging now gives (3.2). \(\square\)

Combining (2.4) and (3.2) gives the exact barycentric load (0.6).

The first moment follows without probability.  Every packet contains
\(4^r\binom rq\) block-simple affine \(q\)-faces.  There are
\(G_\lambda/4^r\) retained packets, so double counting physical
packet--target incidences gives

\[
 \boxed{
 \sum_Td_{\lambda,q}^\pm(T)=G_\lambda\binom rq,}
 \tag{3.3}
\]

and hence

\[
 {1\over N_q}\sum_T{d_{\lambda,q}^\pm(T)\over\binom rq}
 ={G_\lambda\over N_q}.                               \tag{3.4}
\]

This is the exact sense in which the mean is critical.

## 4. Exact finite slice distribution

The degree distribution can be written by one coefficient formula.  Put

\[
 B(x)=(1+x)^4,qquad e(x)=4x^2,
 \tag{4.1}
\]

\[
 c_-(x)=4x,qquad c_+(x)=4x^3,
 \qquad o_\epsilon(x)=B(x)-e(x)-c_\epsilon(x).        \tag{4.2}
\]

Let \(\ell=2m-4b\) be the residual size and
\(R(x)=(1+x)^\ell\).  For \(K_-=m-q\), \(K_+=m+q\), and
\(k=r-q+1\), define

\[
\begin{aligned}
 A_{q,z}^\epsilon
 =[x^{K_\epsilon}]R(x)
 \sum_{j=k+z}^{b}
 { (j-1)!\over(k-1)!z!(j-k-z)!}
 e(x)^kc_\epsilon(x)^z
 o_\epsilon(x)^{j-k-z}B(x)^{b-j}.                    \tag{4.3}
\end{aligned}
\]

This counts targets for which the \(k\)-th \(E\)-block exists and exactly
\(z\) \(C^\epsilon\)-blocks precede it.  The exceptional admissible case
with no \(k\)-th \(E\)-block is

\[
\begin{aligned}
 \widetilde A_{q,z}^\epsilon
 =[x^{K_\epsilon}]R(x)
 {b!\over(k-1)!z!(b-k+1-z)!}
 e(x)^{k-1}c_\epsilon(x)^z
 o_\epsilon(x)^{b-k+1-z}.                            \tag{4.4}
\end{aligned}
\]

Therefore the exact positive-degree histogram is

\[
 \boxed{
 \#\{T:d_{\lambda,q}^\epsilon(T)=d\}
 =\sum_{\substack{z\ge q\\ \binom zq=d}}
   (A_{q,z}^\epsilon+\widetilde A_{q,z}^\epsilon)
 \quad(d>0).}                                        \tag{4.5}
\]

The remaining atom is

\[
 \boxed{
 \#\{T:d_{\lambda,q}^\epsilon(T)=0\}
 =N_q-\sum_{z\ge q}
   (A_{q,z}^\epsilon+\widetilde A_{q,z}^\epsilon).}   \tag{4.6}
\]

It includes both admissible stopped words with \(z<q\) and words having
fewer than \(k-1\) total \(E\)-blocks.  Equations (2.4), (4.3)--(4.6) are
the requested complete physical candidate-degree distribution for one
legal atlas.

The formula is independent of \(\lambda\), by coordinate symmetry, but the
three degree functions on the same target layer are correlated.

## 5. Critical-scale asymptotics

We now evaluate (4.5) at the scale where concentration first fails.

Under the product measure of coordinate density

\[
 p_-={m-q\over2m},qquad p_+={m+q\over2m},            \tag{5.1}
\]

erase every block except \(E_\lambda\) and \(C^\epsilon\).  For both
signs, the exact conditional probability of the next retained letter being
\(C\) is

\[
 \rho_q={m+q\over2m}.                                 \tag{5.2}
\]

Indeed, below one has block probabilities

\[
 4p_-^2(1-p_-)^2,qquad4p_-(1-p_-)^3,
\]

and above they are

\[
 4p_+^2(1-p_+)^2,qquad4p_+^3(1-p_+).
\]

Thus, before slice conditioning and apart from the exponentially unlikely
finite-word truncation,

\[
 \Pr\{Z=z\}
 =\binom{k+z-1}{z}(1-\rho_q)^k\rho_q^z.              \tag{5.3}
\]

This is an exact negative-binomial law, not a Poisson approximation.

### Lemma 5.1 (slice conditioning is asymptotically neutral)

Suppose \(r=o(m)\), \(q=O(\sqrt r)\), and inspect the stopped word through
\(O(r)\) physical blocks.  Conditioning the product measure in (5.1) on
total rank \(m\pm q\) changes the joint central-limit law of the stopped
word by \(o(1)\).

#### Proof

Truncate after \(Cr\) blocks.  Since the \(E\)-letter has probability
\(1/4+o(1)\), the probability that the \(k\)-th \(E\) has not appeared is
\(e^{-\Omega_C(r)}\) for sufficiently large fixed \(C\).

Fix a configuration on these \(O(r)\) coordinates whose local cardinality
deviates from its product mean by \(O(\sqrt r)\).  The ratio between its
conditional and product probabilities is the ratio of two binomial point
probabilities on the remaining \(2m-O(r)\) coordinates.  The local central
limit theorem gives this ratio as

\[
 1+o(1),
\]

uniformly on the stated central set, because the exponent correction is
\(O(r/m)=o(1)\).  Product concentration makes the complement of the
central set negligible.  Letting \(C\) be fixed proves the claim. \(\square\)

### Theorem 5.2 (critical lognormal degree law)

Let \(q=c\sqrt r+o(\sqrt r)\), where \(c>0\).  Then, in either signed
uniform target layer,

\[
 {Z_{\lambda,q}^\epsilon-(r-q)\over\sqrt{2r}}
 \Longrightarrow N(0,1),                             \tag{5.4}
\]

and

\[
 \boxed{
 {\binom{Z_{\lambda,q}^\epsilon}q\over\binom rq}
 \Longrightarrow e^{-c^2+\sqrt2cN}.}                \tag{5.5}
\]

#### Proof

The negative-binomial law (5.3) has mean

\[
 {k\rho_q\over1-\rho_q}=r-q+o(\sqrt r)
\]

and variance

\[
 {k\rho_q\over(1-\rho_q)^2}=2r+o(r),
\]

because \(r=o(m)\) and \(q=O(\sqrt r)\).  Its standard central limit
theorem, followed by Lemma 5.1, proves (5.4).

Write

\[
 Z=r-q+\sqrt{2r}N_r+o_p(\sqrt r),qquad N_r\Longrightarrow N.
\]

A Taylor expansion, uniform on \(|N_r|\le M\), gives

\[
\begin{aligned}
 \log{\binom Zq\over\binom rq}
 &=\sum_{j=0}^{q-1}\log{Z-j\over r-j}\\
 &=-c^2+\sqrt2cN_r+o_p(1).                            \tag{5.6}
\end{aligned}
\]

The error is \(O_p(q^2|r-Z|/r^2+q(r-Z)^2/r^2)=o_p(1)\).
Exponentiating proves (5.5). \(\square\)

The limiting variable has mean one, in agreement with the exact first
moment (3.4).  Its one-sided deficit is explicit:

\[
\begin{aligned}
 \mathbb E(1-e^{-c^2+\sqrt2cN})_+
 &=\Phi(c/\sqrt2)-\Phi(-c/\sqrt2)\\
 &=2\Phi(c/\sqrt2)-1.                                \tag{5.7}
\end{aligned}
\]

The function \(x\mapsto(1-x)_+\) is bounded and continuous, so convergence
in distribution in (5.5) already implies convergence of its expectation;
no uniform-integrability assertion is needed.  Hence (5.7) proves (0.10).

## 6. What all 24 relabelings actually give

There are two inequivalent meanings of this phrase.  First suppose one
coordinate relabelling is used diagonally in every physical four-block.
This produces three global atlases, each with eight labels.

For a target \(T\), let \(Z_{\lambda,q}^\epsilon(T)\) be the three stopping
counts associated with \(\mathcal A_\lambda\).  Since each atlas occurs
for eight coordinate permutations, the exact formal 24-atlas candidate
degree is

\[
 \boxed{
 d_{24,q}^\epsilon(T)
 =8\sum_{\lambda=1}^3
       \binom{Z_{\lambda,q}^\epsilon(T)}q.}           \tag{6.1}
\]

If one chooses one of the 24 global relabelings uniformly before choosing
the legal packet state, the normalized candidate load is

\[
 \boxed{
 L_{24,q}^\epsilon(T)
 ={1\over3}\sum_{\lambda=1}^3
 {\binom{Z_{\lambda,q}^\epsilon(T)}q\over\binom rq}.} \tag{6.2}
\]

The joint finite distribution is also exact.  Use the automaton state

\[
 (a_1,a_2,a_3)\in\{0,1,\ldots,k\}^3,                 \tag{6.3}
\]

where \(a_\lambda\) records the number of
\(E_\lambda\)-letters seen, capped at \(k\).  For a local subset
\(R\subseteq[4]\), let \(M_R(y_1,y_2,y_3)\) increment every applicable
\(a_\lambda\), and before that increment multiply by \(y_\lambda\) when
\(R\) is a singleton/triple and \(a_\lambda<k\).  Let the component of
the terminal column \(\mathbf v(\mathbf u)\) indexed by
\(\mathbf a=(a_1,a_2,a_3)\) equal
\(\prod_{\lambda=1}^3u_{\lambda,a_\lambda}\).  Then

\[
 \boxed{
 [x^{m\pm q}\mathbf y^{\mathbf z}
   \prod_{\lambda=1}^3u_{\lambda,a_\lambda}]
 (1+x)^\ell
 \mathbf e_0^\top
 \left(\sum_{R\subseteq[4]}x^{|R|}M_R(\mathbf y)\right)^b
 \mathbf v(\mathbf u)}                                \tag{6.4}
\]

is the exact number of physical targets with joint stopped \(C\)-count
\(\mathbf z\) and terminal \(E\)-state \(\mathbf a\).  In coordinate
\(\lambda\), states \(a_\lambda=k\) and \(a_\lambda=k-1\) have degree
\(\binom{z_\lambda}q\); states \(a_\lambda\le k-2\) have degree zero.
Thus (6.1) and (6.4) give the complete diagonal 24-label degree
distribution without assuming independence among the atlases.  The
terminal variables are essential for the end-of-word convention.

The critical joint limit is explicit.  At density \(1/2\), put

\[
 Y_\lambda={\bf1}_{C}-{\bf1}_{E_\lambda}.
\]

One block has

\[
 \operatorname {Var}Y_\lambda={1\over2},
 \qquad
 \operatorname {Cov}(Y_\lambda,Y_\mu)={3\over8}
 \quad(\lambda\ne\mu).                               \tag{6.5}
\]

The renewal delta method and Lemma 5.1 therefore give

\[
 \left({Z_{\lambda,q}-(r-q)\over\sqrt{2r}}\right)_{\lambda=1}^3
 \Longrightarrow(N_1,N_2,N_3),                       \tag{6.6}
\]

where the Gaussian vector has diagonal covariance one and off-diagonal
covariance \(3/4\).  Consequently

\[
 L_{24,q}\Longrightarrow
 {1\over3}\sum_{\lambda=1}^3
 e^{-c^2+\sqrt2cN_\lambda}.                           \tag{6.7}
\]

This average still has a positive lower tail.  Indeed, on the positive-
probability event \(N_1,N_2,N_3\le0\), its value is at most \(e^{-c^2}\).
Therefore

\[
 \boxed{
 \liminf {1\over N_q}\sum_T(1-L_{24,q}(T))_+
 \ge(1-e^{-c^2})
 \Pr\{N_1,N_2,N_3\le0\}>0.}                          \tag{6.8}
\]

Thus even the formal average of all 24 relabelings does not have an
\(o(W)\) lower tail.

If instead the 24 labels are chosen independently in the \(b\) physical
blocks, their support word is

\[
                 \boldsymbol\lambda=(\lambda_1,\ldots,\lambda_b)
                 \in\{1,2,3\}^b.                    \tag{6.9}
\]

For each fixed word the exact degree remains (2.4), with block \(i\)
declared \(E\) according to \(\mathcal A_{\lambda_i}\); the complete formal
distribution is obtained from (6.4) by adjoining \(\lambda_i\) to the
one-block transfer and summing it with weight \(1/3\).  Equivalently, a
rank-two local state is declared eligible with probability \(2/3\), while
the singleton/triple letter is unchanged.  This gives an exact finite
coefficient formula for all \(24^b b!\) labelled atlases.

It does **not** enlarge the state set of any fixed packet.  Distinct words
in (6.9) have different middle-owner supports and different first-eligible
partitions.  On one four-block the three support cells have incidence
matrix

\[
 \begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},       \tag{6.10}
\]

whose exact-cover equation has the unique solution
\((1/2,1/2,1/2)\).  Its determinant is two, so no integral union of whole
seed cells covers the six local middle owners once.  Hence the independent
24-label average is an average of incompatible packetizations, not a
multiple-choice distribution which can be rounded one state per old
packet.

### 6.1 Exact degree after formal local-label and ambient-order averaging

Although this average is not a legal packet simplex, its physical
candidate-degree distribution can be computed exactly.  This also tests
whether the hoped-for lower-tail statement is numerically true after the
strongest formal symmetrization.

We continue to use the block-preserving recursive factor, so a
\(q\le r\) window touches a four-block at most once.  Arbitrary
permutations of the \(2r\) individual cube directions can separate sibling
directions and create empty/full two-direction traces; that is a different
full-affine catalogue, not the block-permutation menu analyzed here.

For a lower target let

\[
 C(T)=\#\{i:|T\cap B_i|=1\},\qquad
 N_2(T)=\#\{i:|T\cap B_i|=2\};                       \tag{6.11}
\]

for an upper target replace local rank one by rank three.  Conditional on
the target, an independently relabelled seed contains each rank-two local
state for exactly 16 of its 24 labels.  Hence the number \(E\) of forced
eligible blocks has the exact law

\[
                         E\sim\operatorname {Bin}(N_2(T),2/3). \tag{6.12}
\]

Fix \(q\) boundary blocks.  Under a uniform permutation of all \(b\)
ambient blocks, these \(q\) blocks all occur among the first \(r\) members
of their union with the \(E\) forced blocks in the exact fraction

\[
 \Phi_{r,q}(E)=
 \mathbf1_{\{E+q\ge r\}}
 { \binom E{r-q}\over\binom{E+q}r}
 =
 \mathbf1_{\{E+q\ge r\}}
 { (r)_{\underline q}\over(E+q)_{\underline q}}.     \tag{6.13}
\]

Therefore the atlas-averaged geometric degree and normalized load are

\[
\boxed{\begin{aligned}
 \overline d_q(T)
 &=\binom{C(T)}q\,\mathbb E\Phi_{r,q}(E),\\
 \overline L_q(T)
 &={\overline d_q(T)\over\binom rq}
 =(C(T))_{\underline q}\,
   \mathbb E\!\left[
   {\mathbf1_{\{E+q\ge r\}}\over(E+q)_{\underline q}}
   \right].
\end{aligned}}                                      \tag{6.14}
\]

This identity has no limiting approximation.  In particular, the
first-eligible parameter \(r\) cancels outside the exponentially rare
event in the indicator.

The exact physical profile multiplicities completing (6.14) are

\[
\begin{aligned}
 \mathcal N^-_{u,v}
 &=[x^{m-q}](1+x)^\ell
   {b!\over u!v!(b-u-v)!}
   (4x)^u(6x^2)^v(1+4x^3+x^4)^{b-u-v},\\
 \mathcal N^+_{u,v}
 &=[x^{m+q}](1+x)^\ell
   {b!\over u!v!(b-u-v)!}
   (4x^3)^u(6x^2)^v(1+4x+x^4)^{b-u-v}.
                                                               \tag{6.15}
\end{aligned}
\]

Thus \(\mathcal N^\pm_{u,v}\) targets have the value obtained from
(6.14) by putting \(C=u,N_2=v\).  Equations (6.12)--(6.15) are the
complete pointwise degree distribution under all \(24^b b!\) labelled
local relabellings and ambient block orders.  The eight stabilizer labels
only repeat the same physical support.  If labels rather than their
normalized average are counted, the raw degree is exactly
\[
                         d_q^{\rm raw}(T)=24^b b!\,\overline d_q(T).
                                                               \tag{6.15a}
\]

### Theorem 6.2 (physical-profile lognormal law)

Assume \(r\le m/16\) and \(q=A\sqrt m+o(\sqrt m)\), \(A>0\).  In either
uniform signed target layer,

\[
 \boxed{
 \log\overline L_q(T)
 \Longrightarrow
 -{14\over3}A^2+\sqrt{{34\over3}}\,A\,N,
 \qquad N\sim N(0,1).}                               \tag{6.16}
\]

Let \(G_{\rm av}\) denote the retained middle-owner mass averaged over
the labelled atlases.  Consequently the load mean is exactly critical,

\[
 {1\over N_q}\sum_T\overline L_q(T)
 ={G_{\rm av}\over N_q}\longrightarrow e^{A^2},     \tag{6.17}
\]

but its deficient fraction and deficient mass satisfy

\[
\begin{aligned}
 {1\over N_q}\#\{T:\overline L_q(T)<1\}
 &\longrightarrow
 \Phi\!\left({14A\over\sqrt{102}}\right),\\
 {1\over N_q}\sum_T(1-\overline L_q(T))_+
 &\longrightarrow
 \Phi\!\left({14A\over\sqrt{102}}\right)
 -e^{A^2}\Phi\!\left({-20A\over\sqrt{102}}\right)>0.
                                                               \tag{6.18}
\end{aligned}
\]

#### Proof

It suffices by complementation to treat the lower layer.  Put

\[
 D=C-\frac23N_2.
\]

Use product density \(p=(m-q)/(2m)\), and then condition the total rank.
At \(p=1/2\), for one complete block,

\[
\begin{aligned}
 \operatorname {Var}D&={1\over4}+{4\over9}{3\over8}
 ={5\over12},\\
 \operatorname {Var}|T\cap B_i|&=1,\qquad
 \operatorname {Cov}(D,|T\cap B_i|)=-{1\over4}.
\end{aligned}                                        \tag{6.19}
\]

The conditional multivariate central limit theorem therefore gives

\[
 {D\over\sqrt m}
 \Longrightarrow
 N\!\left({A\over4},{17\over96}\right).              \tag{6.20}
\]

Indeed, the mean follows from

\[
 4p(1-p)^3-4p^2(1-p)^2
 =4p(1-p)^2(1-2p)
 ={A\over2\sqrt m}+O(m^{-1})
\]

per block, while the conditional variance is

\[
 {b\over m}\left({5\over12}-{(1/4)^2\over1}\right)
 \longrightarrow {17\over96}.                       \tag{6.21}
\]

Given \(N_2\), put \(\mu=2N_2/3\).  Uniformly on the central profile set,
the falling-factorial expansions and the exact binomial moment-generating
function yield

\[
\begin{aligned}
 \log(C)_{\underline q}
 &=q\log C-{q(q-1)\over2C}+o(1),\\
 \log\mathbb E{1\over(E+q)_{\underline q}}
 &=-q\log\mu-{q(q+1)\over2\mu}
   +{q^2\operatorname {Var}(E)\over2\mu^2}+o(1).
                                                               \tag{6.22}
\end{aligned}
\]

Here \(C/m,\mu/m\to1/8\) and
\(\operatorname {Var}(E)/m\to1/24\).  The event \(E+q<r\) is
exponentially unlikely, also after the bounded exponential tilt in
(6.22).  Substitution in (6.14) gives

\[
 \log\overline L_q
 =8A\,{D\over\sqrt m}-{20\over3}A^2+o_p(1).          \tag{6.23}
\]

Equations (6.20) and (6.23) prove (6.16).  Its lognormal mean is
\(\exp(A^2)\), agreeing with the exact double count (6.17).  The two
truncated-normal integrals in (6.18) now follow from

\[
 \mathbb E[e^{\mu+\sigma N}\mathbf1_{\{\mu+\sigma N<0\}}]
 =e^{\mu+\sigma^2/2}\Phi\!\left({-\mu-\sigma^2\over\sigma}\right).
\]

The second expression in (6.18) is positive because the limiting
lognormal has positive probability strictly below one. \(\square\)

There is also a sharp small-window consequence.  If
\(1\ll H=o(\sqrt m)\), the same expansion uniformly for \(q\le H\)
gives

\[
 {1\over N_q}\sum_T(1-\overline L_q(T))_+
 \sim\sqrt{{17\over3\pi}}\,{q\over\sqrt m}.          \tag{6.24}
\]

Hence the aggregate formal deficiency through \(H\), for either one
fixed sign, is

\[
 \left(\sqrt{{17\over3\pi}}+o(1)\right)
 {H^2\over2\sqrt m}\,W.                              \tag{6.25}
\]

The sum over both signs is twice (6.25).  Even after averaging
incompatible ambient atlases, it is \(o(W)\) only in the range
\(H=o(m^{1/4})\); at Gaussian \(H\) one depth already has a linear deficit
by (6.18).

## 7. Exact independent rounding and the surviving integral problem

Fix one legal atlas \(\lambda\), and choose one menu state independently
and uniformly in every packet.  A target with candidate degree \(d(T)\)
is missed exactly when all of its candidate packets miss their unique
faces.  Proposition 3.1 gives the exact conditional probability

\[
 \boxed{
 \Pr\{T\text{ missed}\}
 =\left(1-{1\over\binom rq}\right)^{d(T)}.}           \tag{7.1}
\]

This is a finite multiple-choice identity, not a Poisson model.  At the
critical scale, \(p_{r,q}=1/\binom rq\to0\), and Theorem 5.2 yields

\[
 \left(1-p_{r,q}\right)^{d(T)}
 \Longrightarrow
 \exp\{-e^{-c^2+\sqrt2cN}\}.                         \tag{7.2}
\]

The limiting expectation is strictly positive, so independent rounding
leaves \(\Theta(W)\) expected holes.

At the mesoscopic depth \(q\asymp\sqrt r\), this calculation alone does
not prove that every correlated integral choice fails.  The
exact one-state-per-packet fractional dual is

\[
 \boxed{
 \max_{0\le\alpha_T\le1}
 \left[
  \sum_T\alpha_T
  -\sum_{P}\max_{g\in\mathfrak G_P}
       \sum_{T\in\mathcal S(P,g)}\alpha_T
 \right].}                                           \tag{7.3}
\]

The degree calculation controls the uniform barycenter of (7.3), not its
packetwise maxima for arbitrary residual weights.  Therefore it cannot be
promoted to a deterministic cover merely by edge transitivity.

## 8. A statewise Hall cut at Gaussian depth

For the actual SCI range, the fixed ordered atlas has a stronger
deterministic obstruction.  Assume \(r\le m/16\), fix \(A>0\), and take

\[
                         q=\lfloor A\sqrt m\rfloor\le H. \tag{8.1}
\]

Let \(R\) be the union of the last
\(j=\lfloor b/4\rfloor\) physical four-blocks and put \(s=|R|\).  Then
\(s/(2m)\to1/4\).  Call a packet normal when none of its first \(r\)
eligible blocks meets \(R\).

### Lemma 8.1 (frozen suffix)

All but \(U_m\le e^{-\Omega(m)}W\) retained middle owners belong to
normal packets.  Every lower or upper target emitted by any legal state of
a normal packet has the same restriction to \(R\) as its phase owner.

#### Proof

Among the first \(b-j\) blocks, eligibility has product probability
\(1/4\), so its unconditioned mean is
\((b-j)/4=3b/16+O(1)\), whereas \(r\le b/8+O(1)\).
Chernoff gives an \(e^{-\Omega(m)}\) lower tail; conditioning on middle
rank costs only \(O(\sqrt m)\).  This proves the owner estimate.

Every legal local relabelling and internal block permutation moves
coordinates only in the packet's selected blocks.  These are disjoint
from \(R\) for a normal packet.  Intersections and unions of consecutive
vertices consequently preserve the phase owner's restriction to \(R\).
\(\square\)

For an integer \(a\), define

\[
\begin{aligned}
 \mathcal Z_{q,a}^-&=
 \{T\in\tbinom{[2m]}{m-q}:|T\cap R|\le a\},\\
 \mathcal Z_{q,a}^+&=
 \{T\in\tbinom{[2m]}{m+q}:|T\cap R|\ge s-a\},
\end{aligned}                                        \tag{8.2}
\]

and

\[
 B_a=\sum_{t\le a}\binom st\binom{2m-s}{m-t}.        \tag{8.3}
\]

Every exact fractional mixture of whole packet components has total
occurrence capacity at most \(B_a+U_m\) on either target set in (8.2).
Indeed, Lemma 8.1 identifies membership of every normal target occurrence
in (8.2) with the corresponding middle-owner event, whose total fractional
mass is at most \(B_a\).  Exceptional owners contribute at most \(U_m\).
Thus every integral one-state-per-packet factor misses at least

\[
             |\mathcal Z_{q,a}^{\pm}|-B_a-U_m        \tag{8.4}
\]

distinct signed targets.  This is the weighted cut (7.3) with the
indicator weight of \(\mathcal Z_{q,a}^{\pm}\).

Take

\[
 a=\left\lfloor{s\over2}-c\sqrt m\right\rfloor,
 \qquad v={3\over32}.                                \tag{8.5}
\]

The exact lower-layer count is

\[
 |\mathcal Z_{q,a}^-|
 =\sum_{t\le a}\binom st\binom{2m-s}{m-q-t},         \tag{8.6}
\]

and complementation gives the same count for the upper set.  The
hypergeometric central limit theorem and
\(N_q/W\to e^{-A^2}\) give, with
\(x=c/\sqrt v\) and \(d=A\sqrt{2/3}\),

\[
 {B_a\over W}\longrightarrow\Phi(-x),\qquad
 {|\mathcal Z_{q,a}^{\pm}|\over W}
 \longrightarrow e^{-A^2}\Phi(d-x).                 \tag{8.7}
\]

Choose \(x>d\) so large that

\[
 e^{-A^2}\Phi(d-x)>\Phi(-x).                         \tag{8.8}
\]

Such an \(x\) exists because Mills' formula gives

\[
 {\Phi(d-x)\over\Phi(-x)}
 ={x\over x-d}\exp\{xd-d^2/2+o(1)\}\longrightarrow\infty.
                                                               \tag{8.9}
\]

Consequently, for

\[
 \kappa_A=e^{-A^2}\Phi(d-x)-\Phi(-x)>0,              \tag{8.10}
\]

every integral packet-state selection, and even every fractional
owner-exact mixture of whole components, misses

\[
                         \boxed{\kappa_AW-o(W)}       \tag{8.11}
\]

lower targets and the same number of upper targets at depth \(q\).

The qualification is exact: an ambient permutation of all \(b\) blocks
changes the first-eligible atlas and can move the frozen suffix.  It is not
an owner-preserving state of the old packets.  To use many ambient orders
one must first construct an owner-exact cross-atlas repacketization; neither
the degree average nor the 24 local labels supply it.

The exact conclusions are:

1. the complete physical degree distribution is (2.4), (4.3)--(4.6), and
   for diagonal and independent 24-label symmetrizations,
   (6.1)--(6.4) and (6.12)--(6.15);
2. the normalized mean is critical by (3.4) and (6.17);
3. the lower-tail demand requested in the proposed route is false by
   (5.7), (6.8), and the full ambient-order limit (6.18);
4. independent integral rounding has the exact linear-hole limit (7.2);
5. the other sixteen local relabelings are not legal states of fixed
   packets; and
6. at Gaussian depth the suffix weight in Section 8 violates the
   correlated Hall problem by \(\kappa_AW-o(W)\).

Hence this candidate-degree route does not prove SCI, and the fixed ordered
first-eligible atlas cannot be repaired by owner-preserving local
relabelings or internal block permutations.  A viable replacement must
transport owners between genuinely different ambient block orders or use
components that move the exterior; no degree lower-tail theorem can supply
that missing transport.
