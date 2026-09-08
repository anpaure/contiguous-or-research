# Two pair frames separated by one matching switch: exact components, trade cube, and a Gaussian transport obstruction

Date: 2026-07-26

Method: pure mathematics.  No search or solver input is used.

## 0. Outcome

Let

\[
 \mathcal P=\{\{a,A\},\{b,B\}\}\sqcup\mathcal P_0,
 \qquad
 \mathcal P'=\{\{a,B\},\{b,A\}\}\sqcup\mathcal P_0                 \tag{0.1}
\]

be two coordinate pairings of \([2m]\) separated by one four-coordinate
matching switch.  Let \(F_0,F_1\) be exact middle cube-cycle factors built
in the two frames, with the same block size \(R\).  Overlaying their block
partitions gives an \(R\)-regular bipartite multigraph.  Every connected
component has equally many blocks on its two shores, and either shore
partitions the same set of middle owners.  Consequently every component is
an independent exact trade.  If the components are \(K\), the complete
reachable load polytope is

\[
 \boxed{
  \mu_q(z)=\mu_q(F_0)+
       \sum_K z_K\bigl(\mu_{q,K}(F_1)-\mu_{q,K}(F_0)\bigr),
       \qquad z_K\in\{0,1\}.}                         \tag{0.2}
\]

Its convex hull is the affine image of the cube \([0,1]^{\mathcal K}\).
Thus the integral completion issue is isolated exactly: it is simultaneous
rounding of the component coordinates, with no remaining middle-ownership
constraint.

The local matching switch has macroscopic *raw* capacity.  Among rank
\(m-q\) targets, exactly

\[
 2\binom{2m-4}{m-q-2}                                \tag{0.3}
\]

targets move one pair-type step in each direction.  If
\(q=x\sqrt m+o(\sqrt m)\), this is

\[
 \left({e^{-x^2}\over8}+o(1)\right)W                 \tag{0.4}
\]

in either direction.  Transparent tail exchanges realize the same local
motion at incidence level: one packet transfers \(2q\) occurrences from
type \(f+1\) to type \(f\).

Nevertheless **two such frames cannot remove the fixed-frame Gaussian
deficit**.  The reason is a statewise transport invariant.  Associate the
one depth-\(q\) output occurrence of a selected factor to each of its
middle owners \(X\).  For every component choice and every owner,

\[
 \boxed{|f_{\mathcal P}(L_q(X))-f_{\mathcal P}(X)|\le2.}             \tag{0.5}
\]

Hence the output pair-type histogram \(\nu\) stays within earthmover
distance \(2W\) of the middle histogram \(V\):

\[
 \boxed{\mathsf W_1(\nu,V)\le2W.}                                  \tag{0.6}
\]

By contrast, covering all but \(o(W)\) rank-\((m-q)\) targets at a fixed
Gaussian depth requires

\[
 \mathsf W_1(\nu,V)=\Omega_x(W\sqrt m).                              \tag{0.7}
\]

In fact every two-frame component mixture leaves \(\Omega_x(W)\) targets
uncovered at that one depth.  Thus a four-coordinate switch can move
\(\Theta(W)\) adjacent type units, but the deficit \(D_{m,q}=\Theta_x(W)\)
has transport depth \(\Theta(\sqrt m)\).  Its correct cost is
\(\Theta_x(W\sqrt m)\), not \(\Theta_x(W)\).

More generally, if every allowed pairing is at matching-switch distance at
most \(t\) from a base pairing, the same argument gives

\[
 \mathsf W_1(\nu,V)\le2tW.                                           \tag{0.8}
\]

Therefore any mixed-frame proof based on local pairing switches needs
\(t=\Omega_x(\sqrt m)\).  Two frames, or any family contained in an
\(o(\sqrt m)\)-ball in the perfect-matching switch graph, cannot prove the
Gaussian-window statement.  Polynomially many genuinely distant pairings
remain open and are exactly what the fractional size-bias construction
uses.

## 1. The exact component graph

Let \(\mathcal B_i\) be the blocks of \(F_i\), \(i=0,1\).  Each block is
a cube cycle (or a certified recursive necklace) containing exactly \(R\)
middle owners, and each factor partitions \(\binom{[2m]}m\).

Define a bipartite multigraph

\[
 \Gamma(F_0,F_1),qquad V(\Gamma)=\mathcal B_0\sqcup\mathcal B_1,       \tag{1.1}
\]

with one edge \(e_X\) for each middle owner \(X\).  The edge joins the
unique block of \(F_0\) containing \(X\) to the unique block of \(F_1\)
containing \(X\).

### Theorem 1.1 (component trades)

Every vertex of \(\Gamma\) has degree \(R\).  For every connected component
\(K\), if \(\mathcal B_{i,K}\) is its shore in \(F_i\), then

\[
 |\mathcal B_{0,K}|=|\mathcal B_{1,K}|,
 \qquad
 \bigsqcup_{C\in\mathcal B_{0,K}}\operatorname{mid}(C)
 =
 \bigsqcup_{C\in\mathcal B_{1,K}}\operatorname{mid}(C)=:U_K.          \tag{1.2}
\]

Choosing independently, for every \(K\), either \(\mathcal B_{0,K}\) or
\(\mathcal B_{1,K}\) produces another exact middle factor.

#### Proof

Regularity is immediate from the definition: the incident edge labels of a
block are exactly its \(R\) middle owners.  If \(E(K)\) is the owner set in
a component, counting its edges from either shore gives

\[
 |E(K)|=R|\mathcal B_{0,K}|=R|\mathcal B_{1,K}|.
\]

Moreover the edge labels show that both shores partition precisely
\(U_K=E(K)\).  The components partition the middle layer, so independent
shore choices preserve exact ownership. \(\square\)

For a depth \(q\), write \(\mu_{q,i,K}\) for the target-load vector
contributed by shore \(i\) of component \(K\).  Theorem 1.1 proves (0.2).
There are no further compatibility equations among the \(z_K\)'s.

### Corollary 1.2 (the exact fractional dual)

For a target cap \(b\), the fractional component problem

\[
 \min_{0\le z_K\le1}\sum_S(\mu_q(z;S)-b)_+                          \tag{1.3}
\]

has dual

\[
 \boxed{
 \max_{0\le\alpha_S\le1}
 \left[
  \langle\alpha,\mu_q(F_0)-b\mathbf1\rangle
  -\sum_K
   \bigl\langle\alpha,mu_{q,0,K}-\mu_{q,1,K}\bigr\rangle_+
 \right].}                                                         \tag{1.4}
\]

This is only a fractional statement.  The affine image of a cube need not
be integral after the positive-part epigraph variables are added; an
independent component-signing theorem is still needed for simultaneous
target control.

#### Proof

Use
\((y-b)_+=\max_{0\le\alpha\le1}\alpha(y-b)\), interchange min and max
on compact convex polytopes, and minimize each scalar \(z_K\) independently.
\(\square\)

## 2. The six-pattern local skeleton

For a set \(Y\subseteq[2m]\), let \(f(Y)\) and \(f'(Y)\) be its number of
full pairs in \(\mathcal P\) and \(\mathcal P'\), respectively.  Everything
outside \(\{a,A,b,B\}\) cancels.  On the sixteen local patterns,

\[
 f'(Y)-f(Y)=
 \begin{cases}
  +1,&Y\cap\{a,A,b,B\}\in\{\{a,B\},\{b,A\}\},\\
  -1,&Y\cap\{a,A,b,B\}\in\{\{a,A\},\{b,B\}\},\\
  0,&\text{otherwise}.
 \end{cases}                                                       \tag{2.1}
\]

In particular

\[
                         |f'(Y)-f(Y)|\le1.                           \tag{2.2}
\]

The only nontrivial stratum-incidence skeleton occurs when the local set
has size two.  Suppress a fixed outside pair signature.  On the
\(\mathcal P\)-shore there is one split stratum containing

\[
 ab,\ aB,\ Ab,\ AB,                                                  \tag{2.3}
\]

and two full strata represented by \(aA,bB\).  On the
\(\mathcal P'\)-shore there is one split stratum containing

\[
 ab,\ aA,\ bB,\ AB,                                                  \tag{2.4}
\]

and two full strata represented by \(aB,bA\).  The incidence skeleton has
edges

\[
\begin{array}{c|c}
\text{local patterns}&\text{stratum edge}\\ \hline
ab,AB&L_{\rm split}-R_{\rm split},\\
aB,bA&L_{\rm split}-R_{aB},\ L_{\rm split}-R_{bA},\\
aA,bB&L_{aA}-R_{\rm split},\ L_{bB}-R_{\rm split}.
\end{array}                                                        \tag{2.5}
\]

Thus the coarse six-pattern skeleton is connected (a double star with a
double central edge).  The actual cube-cycle overlay is obtained by
refining every stratum vertex into its cycle blocks; its connected
components are exactly the components of that refined incidence graph.
The coarse connectivity does **not** imply that the refined graph is
connected, which is why Theorem 1.1 is the correct exact formulation.

For rank \(m-q\), each prescribed local two-pattern occurs
\(\binom{2m-4}{m-q-2}\) times.  Equation (2.1) therefore proves (0.3),
and the local central limit ratio

\[
 {\binom{2m-4}{m-q-2}\over\binom{2m}{m}}
   ={e^{-x^2}\over16}+o(1)                                         \tag{2.6}
\]

proves (0.4).

## 3. The componentwise transport invariant

Let an owner \(X\) lie on the \(\mathcal P'\)-shore, and let \(L_q(X)\)
be its lower depth-\(q\) target.  Pair flips in the \(\mathcal P'\)-frame
empty split \(\mathcal P'\)-pairs and hence preserve the number of full
\(\mathcal P'\)-pairs:

\[
                         f'(L_q(X))=f'(X).                            \tag{3.1}
\]

Combining (3.1) with (2.2) gives

\[
\begin{aligned}
 |f(L_q(X))-f(X)|
 &\le |f(L_q(X))-f'(L_q(X))|
       +|f'(X)-f(X)|\\
 &\le2.                                                            \tag{3.2}
\end{aligned}
\]

On the \(\mathcal P\)-shore the corresponding displacement is exactly
zero.  The same proof, with full and empty interchanged, applies to upper
targets.

Let

\[
 V_f=\#\{X\in\tbinom{[2m]}m:f(X)=f\}                                \tag{3.3}
\]

and let \(\nu_f\) count the selected factor's lower depth-\(q\) output
occurrences of \(\mathcal P\)-type \(f\).  The owner-to-output association
is a coupling of the equal-mass histograms \(V\) and \(\nu\).  Equation
(3.2) gives

\[
 \mathsf W_1(\nu,V)
 :=\sum_k\left|\sum_{f\le k}(\nu_f-V_f)\right|
 \le2W,                                                            \tag{3.4}
\]

which proves (0.6).  More sharply, if \(U\) is the union of components on
which the \(\mathcal P'\)-shore was selected, then

\[
                         \mathsf W_1(\nu,V)\le2|U|.                  \tag{3.5}
\]

This estimate is independent of the sizes, number, or expansion of the
overlay components.

For pairings at matching-switch distance \(t\), the analogue of (2.2) is
\(|f'(Y)-f(Y)|\le t\); hence the same proof gives (0.8).

## 4. Gaussian deficit has \(\Theta(W\sqrt m)\) transport cost

Let

\[
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}                          \tag{4.1}
\]

be the number of rank-\((m-q)\) targets of \(\mathcal P\)-type \(f\).
Recall that \(V_f/T_{f,q}=\lambda_{f,q}\) is strictly increasing in
\(f\).  Thus \(T_{f,q}-V_f\) is positive below one crossing and negative
above it.

The following is the first-moment refinement of the local central limit
calculation giving

\[
 D_{m,q}/W\longrightarrow
 e^{-x^2}\Phi(x/2)-\Phi(-3x/2).                                    \tag{4.2}
\]

### Lemma 4.1 (weighted Gaussian deficit)

Let \(q=x\sqrt m+o(\sqrt m)\), \(x>0\), and put

\[
 \mu_0={m(m-1)\over2(2m-1)},\qquad
 a_m=\mu_0-{3q\over8}+O(1).                                        \tag{4.3}
\]

For \(Z\sim N(0,1)\), set

\[
 \psi(t)=\mathbb E(t-Z)_+=t\Phi(t)+\phi(t).                         \tag{4.4}
\]

Then

\[
 {1\over W\sqrt m}
 \sum_f(a_m-f)_+(T_{f,q}-V_f)
 \longrightarrow
 c(x):={1\over4}
 \left[e^{-x^2}\psi(x/2)-\psi(-3x/2)\right]>0.                    \tag{4.5}
\]

The same limit remains positive if \((a_m-f)_+\) is truncated at
\(R\sqrt m\), for all sufficiently large fixed \(R=R(x)\).

#### Proof

For a uniformly random perfect matching and a fixed \(r\)-set, the number
of full matched pairs has mean

\[
 {r(r-1)\over2(2m-1)}                                                \tag{4.6}
\]

and variance \(m/16+o(m)\), uniformly for
\(r=m+O(\sqrt m)\).  The pairing exposure martingale (or the standard
matching local CLT) gives asymptotic normality and uniform integrability on
the \(\sqrt m\)-scale.  For \(r=m\), the standardized location of \(a_m\)
is \(-3x/2+o(1)\); for \(r=m-q\), it is \(x/2+o(1)\).  Also

\[
 {N_q\over W}\longrightarrow e^{-x^2}.                              \tag{4.7}
\]

Taking the first lower partial moment on the two laws gives (4.5), since
their common standard deviation is \(\sqrt m/4+o(\sqrt m)\).  Positivity
also follows directly from the one-crossing property: the summands are
nonnegative below the crossing and have positive limiting mass.  Gaussian
tail uniform integrability permits a fixed truncation \(R\) while retaining
a positive constant. \(\square\)

### Theorem 4.2 (macroscopic holes in every two-frame mixture)

Let \(H_q\) be the number of rank-\((m-q)\) targets missed by a factor
obtained through arbitrary component choices between \(F_0,F_1\).  For
every fixed \(x>0\), if \(q=x\sqrt m+o(\sqrt m)\), then

\[
                         H_q\ge c_xW                                \tag{4.8}
\]

for some \(c_x>0\) and all sufficiently large \(m\).

#### Proof

Let \(h_f\) be the missed targets of type \(f\).  Coverage of the remaining
targets implies

\[
                         \nu_f\ge T_{f,q}-h_f.                       \tag{4.9}
\]

Choose \(R\) as in Lemma 4.1 and let

\[
 \varphi_m(f)=\min\{(a_m-f)_+,R\sqrt m\}.                            \tag{4.10}
\]

This is nonnegative and one-Lipschitz.  By Kantorovich duality and (3.4),

\[
 \sum_f\varphi_m(f)(\nu_f-V_f)\le\mathsf W_1(\nu,V)\le2W.          \tag{4.11}
\]

On the other hand, (4.9), Lemma 4.1, and
\(0\le\varphi_m\le R\sqrt m\) give a constant \(c'_x>0\) such that

\[
 \sum_f\varphi_m(f)(\nu_f-V_f)
 \ge c'_xW\sqrt m-R\sqrt m\,H_q+o(W\sqrt m).                       \tag{4.12}
\]

Combining (4.11)--(4.12) yields

\[
 H_q\ge(c'_x/R-o(1))W,
\]

which proves (4.8). \(\square\)

## 5. Relation to the transparent local trade

For the transparent pairing two-switch, the exact upper action is

\[
 \Delta\mu_q^+
 =\sum_{k=1}^q
 \left(
 e_{Q_{k,q}+A+b}+e_{Q_{k,q}+B+a}
 -e_{Q_{k,q}+A+a}-e_{Q_{k,q}+B+b}
 \right).                                                          \tag{5.1}
\]

Relative to \(\mathcal P\), each negative target in (5.1) has one more
full local pair than each positive target.  Hence one packet transports
exactly \(2q\) incidence units by one type step in the useful direction.
If \(\Theta(W/H)\) owner-disjoint packets are available, their raw
depth-\(q\) capacity is

\[
                         \Theta(qW/H),                               \tag{5.2}
\]

which is \(\Theta(W)\) at \(q\asymp H\).

Equation (5.2) is genuine positive local progress.  Theorem 4.2 explains
why it does not settle mixed-frame rounding: at Gaussian depth the deficit
mass is spread across \(\Theta(\sqrt m)\) adjacent pair types.  One local
frame switch supplies one layer of adjacent transport, whereas eliminating
the deficit requires \(\Theta(\sqrt m)\) layers.  This identifies the exact
next scale:

\[
 \boxed{\text{a successful mixed-pair construction must traverse }
        \Omega(\sqrt m)\text{ independent matching-switch directions.}} \tag{5.3}

This is compatible with the polynomial random-pairing reservoir, whose
pairings are typically at distance \(\Theta(m)\), but rules out completing
that fractional construction by rounding only two nearby exact factors.

