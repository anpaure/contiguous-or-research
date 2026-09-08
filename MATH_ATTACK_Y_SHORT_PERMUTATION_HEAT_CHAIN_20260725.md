# Short-permutation component-Haar heat on exact wreath factors

## Intrinsic ternary cells, exact energy Dirichlet form, and class obstructions

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computational experiment was used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn,
\]

and let \(\mathfrak F_m\) be the finite nonempty set of exact middle
wreath factors. The original transposition heat is enlarged by the
permutations of transposition length at most two:

\[
\text{transpositions},\qquad
\text{double transpositions},\qquad
\text{3-cycles}.
\]

The correct enlargement is not the naive two-factor overlay with
\(F\) and \(\sigma F\). For a noninvolution such as a 3-cycle, that binary
cell is not intrinsic and its state-local averaging rule need not be
reversible or idempotent. The correct construction uses the cyclic group
\(\Gamma=\langle\sigma\rangle\), partitions the rows of \(F\) into
\(\Gamma\)-owner packets with invariant middle roots, and independently
Haar-translates every packet. A transposition or double transposition gives
a binary cell; a 3-cycle gives a ternary cell.

The main exact conclusions are as follows.

1. Every owner-group cell consists entirely of literal \(0/1\) exact
   factors and is intrinsic under rebasing. Uniform cell averaging is an
   orthogonal projection.

2. Averaging these projections over all short cyclic subgroups defines a
   symmetric positive-semidefinite Markov kernel \(K_{\rm sh}\). Its
   communicating classes are exactly the connected components of the union
   of the binary and ternary cell cliques. Every class is aperiodic and has
   the uniform law as its unique stationary measure. All stationary laws
   are mixtures of these class-uniform laws.

3. The multidepth floor energy has the exact conditional drift

   \[
   (K_\Gamma\mathcal Q_H)(F)-\mathcal Q_H(F)
   =V_\Gamma(F)-A_\Gamma(F),
   \]

   where \(A_\Gamma\) is coherent group smoothing and \(V_\Gamma\) is
   packet restitution. Every stationary class satisfies
   \(\mathbb EV_\Gamma=\mathbb EA_\Gamma\) separately for every short
   subgroup. Thus stationarity gives an equality, not an energy upper
   bound.

4. The Dirichlet form of \(\mathcal Q_H\) itself is an exact sum of
   squared interpacket Gram correlations:

   \[
   \operatorname{Var}_{\Gamma\text{-cell}}(\mathcal Q_H)
   =4\sum_{K<L}\frac1{|\Gamma|}
   \sum_{t\in\Gamma}
   \langle b_K,tb_L\rangle_H^2.
   \]

   Hence one active packet, or mutually group-orthogonal packet residuals,
   produces zero variance contribution for that fixed \(\Gamma\)-cell even
   when the coherent displacement is large.

5. For the uniform conjugacy average, the exact coherent gap on
   zero-point-margin Johnson loads is

   \[
   \frac4n
   \]

   for 3-cycle Haar and

   \[
   \frac{4(n-4)}{n(n-3)}
   =\frac4n+O(n^{-2})
   \]

   for double-transposition Haar. The length-two families double the
   leading transposition coherent constant; they do not produce
   dimension-free spectral or log-Sobolev contraction. These are
   target-profile spectra, not lower bounds for the exact-factor
   state-chain gap.

6. Literal compositions, reversibilizations, and operator commutators of
   old transposition-component moves cannot merge old communicating classes.
   A short owner packet can be a genuinely new bridge only when its middle
   root is invariant under the short permutation but not under a suitable
   pulled transposition factorization. At least two active packets with
   nonconstant phases are necessary. No actual bridge between two original
   classes is proved here.

7. The even-only short chain has a genuine invariant when \(m\) is even:
   the number of selected wreaths of each chirality is conserved. This
   obstructs irreducibility whenever more than one chirality-count sector
   is populated. Odd transposition packets remove the group-theoretic
   conservation mechanism, and an audited \(m=4\) packet changes the count,
   but no such theorem is asserted uniformly in \(m\). No nontrivial full
   mixed-chain invariant or Catalan-scale energy theorem is obtained.

Thus the short-permutation chain is a rigorous reversible enlargement, but
it does not prove

\[
\mathbb E_{\mathscr C}\mathcal Q_{H_A}
=O_A(H_A\operatorname{Cat}_m).
\]

The remaining open tasks for the intended mixing route are exact: determine
whether mixed packet phases bridge the old classes, and bound packet
restitution below coherent smoothing. Neither follows from a spectral or
log-Sobolev inequality alone. Bridging is not logically necessary if one
existing class already contains a low-energy factor.

## 1. Exact factors and floor energy

Let \(\Omega_m\) be the set of unoriented cyclic orders on \([n]\), modulo
rotation and reversal. For a row \(C\in\Omega_m\), write \(\mathcal W_r(C)\)
for its family of cyclic rank-\(r\) intervals. An exact factor is

\[
F\subseteq\Omega_m,
\qquad |F|=B,
\qquad
\{\mathcal W_m(C):C\in F\}
\text{ partitions }\binom{[n]}m.
\tag{1.1}
\]

For \(1\le q\le H\le m-1\), put

\[
r_q=m-q,
\qquad
N_q=\binom n{r_q},
\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\tag{1.2}
\]

where \(c_q=\lfloor\lambda_q\rfloor\) and
\(0\le\theta_q<1\). In the Gaussian application

\[
H=H_A=\lceil A\sqrt m\rceil
\]

with fixed \(A>0\), and \(m\) is sufficiently large that all
\(c_q\ge1\).

Let \(\mu_q^F(S)\) be the number of rows of \(F\) in which \(S\) is a
cyclic rank-\(r_q\) interval. Define

\[
f_q^F=\mu_q^F-\lambda_q\mathbf1,
\qquad
\beta_q=N_q\theta_q(1-\theta_q),
\tag{1.3}
\]

and use the weighted Hilbert norm

\[
\|f\|_H^2
=\sum_{q=1}^H\frac{\|f_q\|_2^2}{c_q},
\qquad
\langle f,g\rangle_H
=\sum_{q=1}^H\frac{\langle f_q,g_q\rangle_2}{c_q}.
\tag{1.4}
\]

The unhalved full floor-corrected energy is

\[
\begin{aligned}
\mathcal Q_H(F)
&=\sum_{q=1}^H\frac1{c_q}
\sum_{S\in\binom{[n]}{r_q}}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)\\
&=\|f^F\|_H^2-\mathfrak B_H,
\qquad
\mathfrak B_H=\sum_{q=1}^H\frac{\beta_q}{c_q}.
\end{aligned}
\tag{1.5}
\]

Every numerator product in the first line is a nonnegative integer;
\(\mathcal Q_H\) is nonnegative but, because of the factors \(1/c_q\), need
not be integral. Every exact centered load has zero Johnson degrees zero
and one: its total is zero, and for every coordinate \(x\),

\[
\sum_{S\ni x}\mu_q^F(S)=r_qB
=\lambda_q\binom{n-1}{r_q-1}.
\tag{1.6}
\]

## 2. The intrinsic owner-group cell

Let \(\Gamma=\langle\sigma\rangle\le S_n\) have prime order
\(p\in\{2,3\}\). The cases used below are:

\[
\begin{array}{c|c|c}
\sigma& p&\text{transposition length}\\ \hline
\text{transposition}&2&1\\
\text{double transposition}&2&2\\
\text{3-cycle}&3&2.
\end{array}
\tag{2.1}
\]

For a middle set \(T\), let \(o_F(T)\in F\) denote its unique owner.
Form the \(\Gamma\)-owner graph on vertex set \(F\) by joining

\[
o_F(T)\quad\text{to}\quad o_F(\sigma T)
\tag{2.2}
\]

for every middle set \(T\). Loops and parallel edges are harmless. Let
\(\mathcal K_\Gamma(F)\) be its connected components. For
\(K\in\mathcal K_\Gamma(F)\), define its middle root

\[
U_K=\bigcup_{C\in K}\mathcal W_m(C).
\tag{2.3}
\]

This graph is independent of which generator of \(\Gamma\) is named. For
\(p=3\), replacing \(\sigma\) by \(\sigma^{-1}=\sigma^2\) gives the same
undirected edge set after substituting \(T\mapsto\sigma^2T\); for \(p=2\)
there is only one nonidentity generator.

### Theorem 2.1 (intrinsic binary/ternary owner cell)

For every \(m\ge2\), every exact factor \(F\), and every group in (2.1):

1. \(\sigma U_K=U_K\) for every owner component \(K\);

2. every phase \(\sigma^aK\), \(a\in\mathbb Z_p\), is a wreath
   factorization of the same root \(U_K\);

3. independently choosing one phase \(\sigma^{a_K}K\) for every owner
   component produces a literal squarefree exact factor;

4. the resulting cell is intrinsic: after rebasing at any child, its
   \(\Gamma\)-owner components are precisely the chosen translates
   \(\sigma^{a_K}K\);

5. after discarding components whose phases all coincide as physical row
   sets, a cell with \(k\) active components has exactly \(p^k\) states.

#### Proof

If \(T\in U_K\), its owner lies in \(K\). The edge (2.2) places the owner
of \(\sigma T\) in the same component. Thus
\(\sigma U_K\subseteq U_K\), and equality follows from finiteness.

The rows of \(K\) partition \(U_K\). Applying \(\sigma^a\) shows that
\(\sigma^aK\) partitions \(\sigma^aU_K=U_K\). The roots \(U_K\) partition
the entire middle layer, so choosing one phase over every root covers every
middle set exactly once.

No physical row can be selected from two distinct phased components. If a
row belonged to \(\sigma^aK\cap\sigma^bL\), its middle support would lie in
both disjoint roots \(U_K\) and \(U_L\), forcing \(K=L\). Thus the selected
factor is squarefree.

Let

\[
G=\bigcup_K\sigma^{a_K}K
\]

be a child. The root sets remain disjoint and invariant, so no owner edge
of \(G\) crosses two roots. Inside \(U_K\), the owner graph of
\(\sigma^{a_K}K\) is the \(\sigma^{a_K}\)-image of the old graph, because
\(\Gamma\) is cyclic and hence commutative. It remains connected. Therefore
the new components are exactly the selected translates, proving
intrinsicity.

For prime \(p\), the stabilizer of a component phase is either all of
\(\Gamma\) or trivial. Every active component therefore has exactly \(p\)
distinct phases. Choices over disjoint roots are independent, proving the
last assertion. \(\square\)

For a transposition, this recovers the usual intrinsic ownership cell. For
a double transposition, it automatically bundles the component orbits that
a raw two-layer overlay can separate. For a 3-cycle, it gives a genuinely
ternary heat bath.

## 3. Why the raw binary 3-cycle overlay fails

It is tempting to compare only \(F\) and \(\sigma F\), take the connected
components of that two-factor ownership overlay, and choose old or new on
each component. That construction is exact at its base point, but for a
3-cycle it need not define an intrinsic cell. The failure already has a
purely analytic \(m=2\) witness.

### Proposition 3.1 (nonintrinsic binary 3-cycle heat)

Let \(m=2\), \(n=5\), and let \(\sigma\) be any 3-cycle. For every exact
factor \(F\), the raw ownership overlay of \(F\) with \(\sigma F\) is
connected, as is the overlay of \(\sigma F\) with \(\sigma^2F\). Moreover,

\[
F,\qquad \sigma F,\qquad \sigma^2F
\tag{3.1}
\]

are pairwise distinct. Consequently the binary state-local rule

\[
D_\sigma(F,\cdot)=\tfrac12\delta_F+
\tfrac12\delta_{\sigma F}
\tag{3.2}
\]

satisfies

\[
D_\sigma(F,\sigma F)=\frac12,
\qquad
D_\sigma(\sigma F,F)=0.
\tag{3.3}
\]

It is neither reversible with respect to the uniform law nor idempotent.
The owner-group construction replaces the two-state sets in (3.2) by the
intrinsic three-state orbit (3.1).

#### Proof

An unoriented cyclic order on five points is the same object as a Hamilton
5-cycle in \(K_5\). Its five middle windows are its edges, and the complement
of those five edges is another Hamilton 5-cycle. Thus an exact factor is a
complementary pair of Hamilton cycles. There are twelve Hamilton cycles and
hence six exact factors.

The action of \(S_5\) on the six factors is transitive: map either Hamilton
cycle in one pair to either Hamilton cycle in the other, and complements
map to complements. Thus a factor stabilizer has order \(120/6=20\). It
contains no element of order three. Therefore no 3-cycle fixes a factor,
and (3.1) is pairwise distinct.

Two distinct factors cannot share a row: a Hamilton cycle determines its
unique complementary partner. The ownership overlay of two factors is a
5-regular bipartite multigraph with two vertices on each side. Every
connected component has equally many vertices on its two sides. If the
overlay were disconnected, it would therefore be a union of two
one-vertex-per-side components. The two rows in either such component would
own the same five edges and hence would be the same Hamilton cycle,
contradicting absence of a common row. Thus both overlays in the statement
are connected.

The only raw binary choices based at \(F\) are \(F,\sigma F\), while those
based at \(\sigma F\) are \(\sigma F,\sigma^2F\). This proves (3.3). It also
gives
\[
D_\sigma^2(F,F)=\frac14\ne\frac12=D_\sigma(F,F),
\qquad
D_\sigma^2(F,\sigma^2F)=\frac14\ne0=D_\sigma(F,\sigma^2F),
\]
so the rule is not idempotent. \(\square\)

Symmetrizing \(D_\sigma\) with a separately defined reverse rule can repair
detailed balance, but it does not turn the overlapping two-point sets into
intrinsic heat-bath cells. The full cyclic owner cell of Theorem 2.1 is the
canonical projection used below.

## 4. The reversible short-permutation chain

Let \(\mathscr G_{\rm sh}\) be the family of cyclic subgroups consisting of

\[
\begin{split}
&\langle(a\ b)\rangle,\\
&\langle(a\ b\ c)\rangle,\\
&\langle(a\ b)(c\ d)\rangle.
\end{split}
\tag{4.1}
\]

Subgroups, rather than generators, are counted. Hence

\[
L_{\rm sh}:=|\mathscr G_{\rm sh}|
=\binom n2+\binom n3+3\binom n4.
\tag{4.2}
\]

For \(\Gamma\in\mathscr G_{\rm sh}\), let
\(\mathcal P_\Gamma\) be the partition of \(\mathfrak F_m\) into the
intrinsic cells of Theorem 2.1, and define

\[
(K_\Gamma\Phi)(F)
=\frac1{|\mathscr D_\Gamma(F)|}
\sum_{G\in\mathscr D_\Gamma(F)}\Phi(G),
\tag{4.3}
\]

where \(\mathscr D_\Gamma(F)\) is the cell containing \(F\). The short heat
kernel is

\[
K_{\rm sh}=\frac1{L_{\rm sh}}
\sum_{\Gamma\in\mathscr G_{\rm sh}}K_\Gamma.
\tag{4.4}
\]

### Theorem 4.1 (projection, classes, and stationary laws)

For every \(m\ge2\):

1. each \(K_\Gamma\) is a stochastic self-adjoint idempotent, hence the
   orthogonal projection onto functions constant on \(\Gamma\)-cells;

2. \(K_{\rm sh}\) is stochastic, self-adjoint, and positive semidefinite;

3. its communicating classes are exactly the connected components of the
   graph obtained by making every cell in every \(\mathcal P_\Gamma\) a
   clique;

4. each class \(\mathscr C\) is a union of complete \(\Gamma\)-cells for
   every \(\Gamma\), is irreducible and aperiodic, and has the uniform law
   \(\pi_{\mathscr C}\) as its unique stationary law;

5. every stationary law of the full chain is a mixture of the laws
   \(\pi_{\mathscr C}\), and

   \[
   \ker(I-K_{\rm sh})
   =\bigcap_{\Gamma\in\mathscr G_{\rm sh}}
   \operatorname{Ran}K_\Gamma.
   \tag{4.5}
   \]

#### Proof

Intrinsicness says precisely that the cell relation is an equivalence
relation. Uniform averaging on the blocks of a finite partition is a
stochastic self-adjoint idempotent. An average of such projections is
stochastic and self-adjoint. Moreover,

\[
\langle\Phi,K_{\rm sh}\Phi\rangle
=\frac1{L_{\rm sh}}
\sum_\Gamma\|K_\Gamma\Phi\|_2^2\ge0,
\tag{4.6}
\]

where the unnormalized counting inner product may be used.

A one-step transition has positive probability exactly when the two states
belong to a common cell for at least one \(\Gamma\). Thus communication is
connectivity in the union of the cell cliques. If a class meets a cell, the
whole clique lies in that class, proving the union assertion. Every state
has positive holding probability, so a class is aperiodic. Symmetry gives
the uniform stationary law; finite irreducibility makes it unique. Standard
finite-chain decomposition then gives all stationary mixtures.

Finally,

\[
\langle\Phi,(I-K_{\rm sh})\Phi\rangle
=\frac1{L_{\rm sh}}
\sum_\Gamma\|(I-K_\Gamma)\Phi\|_2^2.
\tag{4.7}
\]

The left side vanishes exactly when every summand does, which is (4.5).
\(\square\)

For a class \(\mathscr C\), normalize the inner product by

\[
\langle\Phi,\Psi\rangle_{\pi_{\mathscr C}}
=\frac1{|\mathscr C|}\sum_{F\in\mathscr C}\Phi(F)\Psi(F).
\tag{4.8}
\]

The exact state-space Dirichlet form is

\[
\begin{aligned}
\mathscr E_{\mathscr C}^{\rm sh}(\Phi,\Phi)
&:=\langle\Phi,(I-K_{\rm sh})\Phi\rangle_{\pi_{\mathscr C}}\\
&=\frac1{L_{\rm sh}}
\sum_\Gamma\sum_{\substack{\mathscr D\in\mathcal P_\Gamma\\
\mathscr D\subseteq\mathscr C}}
\frac{|\mathscr D|}{|\mathscr C|}
\operatorname{Var}_{\mathscr D}(\Phi)\\
&=\frac1{2L_{\rm sh}|\mathscr C|}
\sum_\Gamma\sum_{\substack{\mathscr D\in\mathcal P_\Gamma\\
\mathscr D\subseteq\mathscr C}}
\frac1{|\mathscr D|}
\sum_{F,G\in\mathscr D}(\Phi(F)-\Phi(G))^2.
\end{aligned}
\tag{4.9}
\]

Because the transposition subgroups occur in (4.1), every short-chain class
is a union of communicating classes of the original transposition heat. It
is also \(S_n\)-stable: choosing the same phase on all owner packets gives
the global coordinate image, and transpositions generate \(S_n\). Formula
(4.5), rather than an unproved combinatorial label, is the complete exact
invariant algebra currently available for the full mixed chain.

## 5. Exact multidepth heat and integer orbit floors

Fix \(F\), \(\Gamma=\langle\sigma\rangle\), and its owner packets. For a
packet \(K\), let \(a_{K,q}\) be its raw depth-\(q\) load:

\[
a_{K,q}(S)=|\{C\in K:S\in\mathcal W_{r_q}(C)\}|,
\qquad a_K=(a_{K,q})_{q\le H}.
\tag{5.1}
\]

The weights \(1/c_q\) enter only through (1.4). Let the coordinate action
on target profiles be

\[
(h x)_q(S)=x_q(h^{-1}S),
\qquad
P_\Gamma=\frac1p\sum_{h\in\Gamma}h.
\tag{5.2}
\]

This action is unitary for \(\langle\cdot,\cdot\rangle_H\), and
\(P_\Gamma\) is its orthogonal invariant projection. Put

\[
b_K=(I-P_\Gamma)a_K.
\tag{5.3}
\]

If the child phases \(h_K\in\Gamma\) are independent and uniform, then

\[
f^{F_{\mathbf h}}
=P_\Gamma f^F+\sum_K h_Kb_K.
\tag{5.4}
\]

Indeed, the child raw load is \(\sum_Kh_Ka_K\), while, with blockwise
notation \(\boldsymbol\lambda\mathbf1=(\lambda_q\mathbf1)_{q\le H}\),
\(P_\Gamma f^F=\sum_KP_\Gamma a_K-\boldsymbol\lambda\mathbf1\).

Define coherent displacement and packet restitution by

\[
A_\Gamma(F)=\|(I-P_\Gamma)f^F\|_H^2,
\qquad
V_\Gamma(F)=\sum_K\|b_K\|_H^2.
\tag{5.5}
\]

Equivalently, the second quantity is

\[
V_\Gamma(F)=\sum_K\frac1p\sum_{h\in\Gamma}
\|ha_K-P_\Gamma a_K\|_H^2.
\tag{5.6}
\]

### Theorem 5.1 (exact short-Haar heat identity)

For every \(F,\Gamma,H\) in the stated ranges,

\[
(K_\Gamma\mathcal Q_H)(F)-\mathcal Q_H(F)
=V_\Gamma(F)-A_\Gamma(F).
\tag{5.7}
\]

For every communicating class \(\mathscr C\) of \(K_{\rm sh}\), and for
every fixed \(\Gamma\in\mathscr G_{\rm sh}\),

\[
\mathbb E_{F\sim\pi_{\mathscr C}}V_\Gamma(F)
=\mathbb E_{F\sim\pi_{\mathscr C}}A_\Gamma(F).
\tag{5.8}
\]

#### Proof

The invariant vector \(P_\Gamma f^F\) is orthogonal to every \(h_Kb_K\).
The packet residuals have mean zero and are independent. Therefore (5.4)
gives

\[
\mathbb E_{\mathbf h}\|f^{F_{\mathbf h}}\|_H^2
=\|P_\Gamma f^F\|_H^2+\sum_K\|b_K\|_H^2.
\tag{5.9}
\]

Since \((I-P_\Gamma)f^F=\sum_Kb_K\), subtracting
\(\|f^F\|_H^2\), and observing that the constant
\(\mathfrak B_H\) cancels, proves (5.7).

By Theorem 4.1, \(\mathscr C\) is a union of full \(\Gamma\)-cells. Hence
the uniform law on \(\mathscr C\) is invariant under \(K_\Gamma\)
separately, not merely under their average. Averaging (5.7) proves (5.8).
\(\square\)

The integer correction in (5.7) becomes transparent orbit by orbit. Fix a
depth \(q\), suppress \(q\), and put

\[
h_c(z)=(z-c)(z-c-1).
\tag{5.10}
\]

Let \(O\) be a target orbit under \(\Gamma\). Its size is
\(d\in\{1,p\}\). Write its conserved total as

\[
\ell=\sum_{S\in O}\mu(S)=da+s,
\qquad 0\le s<d.
\tag{5.11}
\]

Define

\[
J_{c,d}(\ell)
=(d-s)h_c(a)+s h_c(a+1),
\qquad
\phi_d(\ell)=\frac{s(d-s)}d.
\tag{5.12}
\]

### Proposition 5.2 (exact \(C_2/C_3\) orbit floor)

For \(x=(\mu(S))_{S\in O}\), put

\[
G_O(x)=
\left\|x-\frac\ell d\mathbf1\right\|_2^2-\phi_d(\ell).
\tag{5.13}
\]

Then \(G_O(x)\ge0\) and

\[
\sum_{S\in O}h_c(\mu(S))
=J_{c,d}(\ell)+G_O(x).
\tag{5.14}
\]

For the random child, define

\[
V_O=\sum_K\frac1p\sum_{h\in\Gamma}
\left\|h a_{K,O}-P_\Gamma a_{K,O}\right\|_2^2,
\qquad
C_O=V_O-\phi_d(\ell).
\tag{5.15}
\]

Then \(C_O\ge0\) and

\[
\mathbb E_{\mathbf h}
\sum_{S\in O}h_c(\mu^{F_{\mathbf h}}(S))
=J_{c,d}(\ell)+C_O,
\tag{5.16}
\]

so the exact orbit drift is

\[
\mathbb E\Delta Q_O=-G_O+C_O.
\tag{5.17}
\]

#### Proof

Among integral \(d\)-vectors of sum \(\ell\), strict convexity of
\(\sum_i x_i^2\), or a one-unit balancing exchange, shows that the minimum
has \(d-s\) coordinates \(a\) and \(s\) coordinates \(a+1\). Its squared
distance from the constant mean is \(s(d-s)/d\). Since the linear and
constant terms in \(\sum_i h_c(x_i)\) depend only on \(\ell\), this proves
(5.13)--(5.14).

On the transitive orbit \(O\), \(P_\Gamma x=(\ell/d)\mathbf1\). Formula
(5.4), restricted to \(O\), and independence give

\[
\mathbb E\left\|x'-\frac\ell d\mathbf1\right\|_2^2=V_O.
\tag{5.18}
\]

Every child load is integral, so the left side of (5.18) is pointwise at
least \(\phi_d(\ell)\); hence \(C_O\ge0\). The same fixed-sum expansion proves
(5.16), and subtraction gives (5.17). For \(d=1\), every displayed excess
and drift is zero. \(\square\)

For \(C_2\), \(\phi_2\) is \(0\) or \(1/2\). For \(C_3\),

\[
\phi_3(\ell)=
\begin{cases}
0,&3\mid\ell,\\
2/3,&3\nmid\ell.
\end{cases}
\tag{5.19}
\]

Thus the ternary floor is not an optional lower-order correction.

## 6. The exact Dirichlet form of the energy

The drift (5.7) sees only the difference between coherent smoothing and
packet restitution. The Dirichlet form of the energy itself has a sharper
and different exact structure.

### Theorem 6.1 (interpacket Gram formula)

For a fixed \(\Gamma=\langle\sigma\rangle\) of order \(p\), the variance of
\(\mathcal Q_H\) under uniform resampling of the \(\Gamma\)-cell of \(F\) is

\[
\boxed{
\operatorname{Var}_{\Gamma\text{-cell}}(\mathcal Q_H)
=4\sum_{K<L}\frac1p\sum_{t=0}^{p-1}
\langle b_K,\sigma^tb_L\rangle_H^2.}
\tag{6.1}
\]

Consequently, on every short-chain class \(\mathscr C\),

\[
\boxed{
\mathscr E_{\mathscr C}^{\rm sh}(\mathcal Q_H,\mathcal Q_H)
=\frac4{L_{\rm sh}}
\sum_{\Gamma\in\mathscr G_{\rm sh}}
\mathbb E_{F\sim\pi_{\mathscr C}}
\sum_{K<L}\frac1p\sum_{t=0}^{p-1}
\langle b_K,\sigma^tb_L\rangle_H^2.}
\tag{6.2}
\]

#### Proof

By (5.4), orthogonality of invariant and noninvariant subspaces, and
unitarity of every phase,

\[
\mathcal Q_H(F_{\mathbf h})
=C(F,\Gamma)+2\sum_{K<L}
\langle h_Kb_K,h_Lb_L\rangle_H,
\tag{6.3}
\]

where

\[
C(F,\Gamma)=\|P_\Gamma f^F\|_H^2+
\sum_K\|b_K\|_H^2-\mathfrak B_H
\tag{6.4}
\]

is phase-independent. Every cross term in (6.3) has mean zero. Two
different unordered packet pairs have zero covariance: if they are
disjoint, independence suffices; if they share one packet, condition on
that packet and average either unshared zero-mean phase.

For a fixed pair \(K,L\), invariance of the inner product gives

\[
\mathbb E_{h_K,h_L}
\langle h_Kb_K,h_Lb_L\rangle_H^2
=\frac1p\sum_{t=0}^{p-1}
\langle b_K,\sigma^tb_L\rangle_H^2.
\tag{6.5}
\]

Taking the variance of (6.3) proves (6.1). Formula (4.9) says that the
Dirichlet contribution of \(K_\Gamma\) is the class average of its cell
variance. Averaging (6.1) over \(\Gamma\) proves (6.2). \(\square\)

For \(p=2\), put

\[
d_K=a_K-\sigma a_K=2b_K.
\tag{6.6}
\]

Since \(\sigma b_K=-b_K\), (6.1) reduces to

\[
\operatorname{Var}_{\Gamma\text{-cell}}(\mathcal Q_H)
=\frac14\sum_{K<L}\langle d_K,d_L\rangle_H^2.
\tag{6.7}
\]

Equations (6.1)--(6.2) expose a locking mechanism invisible to a coherent
spectral estimate. For a fixed generator cell, one active packet gives no
pair in (6.1), and residual packets satisfying

\[
\langle b_K,\sigma^tb_L\rangle_H=0
\quad(K\ne L,\ 0\le t<p)
\tag{6.8}
\]

give zero contribution. These are local statements for that fixed
\(\Gamma\)-cell; they do not assert that the other generators in
\(K_{\rm sh}\) also have zero contribution.

In particular, if the \(\Gamma\)-owner graph is connected, the cell consists
only of the global coordinate phases \(\sigma^aF\). Coordinate invariance of
\(\mathcal Q_H\) makes it constant on the cell. Equivalently, (5.7) gives

\[
V_\Gamma(F)=A_\Gamma(F)
\tag{6.9}
\]

pointwise. Thus the full coherent gain can be restored before stationarity
is even invoked.

## 7. Exact coherent spectra of the short families

The next calculation concerns the coordinate action on target profiles. It
does **not** calculate the spectrum of \(K_{\rm sh}\) on exact factors.

On \(\binom{[n]}r\), let \(E_{r,j}\) be Johnson degree \(j\),
\(0\le j\le\min(r,n-r)\). The permutation representation on \(r\)-sets is
multiplicity-free:

\[
\mathbb R^{\binom{[n]}r}
=\bigoplus_j E_{r,j},
\qquad
E_{r,j}\cong S^{(n-j,j)}.
\tag{7.1}
\]

The positive Johnson Laplacian has eigenvalue

\[
\lambda_j=j(n-j+1)
\tag{7.2}
\]

on \(E_{r,j}\). One elementary construction of (7.1) takes the nested
spaces spanned by the incidence vectors of \(j\)-subsets and their
orthogonal differences; the inclusion incidence identities give (7.2).
The dimension is

\[
d_j=\binom nj-\binom n{j-1}.
\tag{7.3}
\]

For a conjugacy class element \(g\), its scalar on \(E_{r,j}\) after class
averaging is the character ratio

\[
\rho_j(g)=\frac{\chi^{(n-j,j)}(g)}{d_j}.
\tag{7.4}
\]

This is independent of \(r\) whenever the degree \(j\) occurs.

### Theorem 7.1 (3-cycle Haar spectrum)

Let \(T_3\) be the average coordinate action over all 3-cycles, and let
\(\overline P_{C_3}\) be the average of \(P_\Gamma\) over all
\(\binom n3\) cyclic 3-subgroups. On Johnson degree \(j\),

\[
\rho_j^{(3)}
=1-\frac{3\lambda_j}{n(n-1)},
\tag{7.5}
\]

and

\[
\overline P_{C_3}
=\frac13(I+2T_3),
\qquad
\pi_j^{(C_3)}
=1-\frac{2\lambda_j}{n(n-1)}.
\tag{7.6}
\]

The full nonconstant target-profile gap is \(2/(n-1)\), attained at
\(j=1\). On the zero-point-margin subspace \(j\ge2\), whenever degree two
occurs, the sharp coherent gap is

\[
1-\pi_2^{(C_3)}=\frac4n.
\tag{7.7}
\]

For the exact multidepth load,

\[
\begin{aligned}
\mathbb E_{\Gamma:C_3}A_\Gamma(F)
&=\frac4n\|f^F\|_H^2\\
&\quad+\frac{2}{n(n-1)}
\sum_{q=1}^H\frac1{c_q}
\sum_{j\ge3}(j-2)(n-j-1)
\|f_{q,j}^F\|_2^2.
\end{aligned}
\tag{7.8}
\]

#### Proof

A \(k\)-set fixed by a 3-cycle contains either none or all three moved
points. With the convention that out-of-range binomial coefficients vanish,

\[
\operatorname{Fix}_k(3\,1^{n-3})
=\binom{n-3}k+\binom{n-3}{k-3}.
\tag{7.9}
\]

The subset permutation character is the sum of the two-row characters
through degree \(k\); hence

\[
\chi^{(n-j,j)}(g)
=\operatorname{Fix}_j(g)-\operatorname{Fix}_{j-1}(g).
\tag{7.10}
\]

Substitution of (7.9) into (7.10), division by (7.3), and cancellation give
(7.5). A cyclic Haar projector is
\((I+\sigma+\sigma^2)/3\). Each cyclic subgroup contributes its two
nonidentity 3-cycles, proving (7.6).

The numbers \(\lambda_j\) increase through \(j\le n/2\). This proves the
two gap assertions. By (1.6), \(f_q^F\) has no degrees zero or one, and

\[
\lambda_j-\lambda_2=(j-2)(n-j-1).
\tag{7.11}
\]

Finally,
\(\mathbb E_\Gamma A_\Gamma
=\langle f,(I-\overline P_{C_3})f\rangle_H\).
Equations (7.6), (7.7), and (7.11) give (7.8). \(\square\)

Equivalently,

\[
\overline P_{C_3}
=I-\frac{2}{n(n-1)}L_J
\tag{7.12}
\]

on each target slice.

### Theorem 7.2 (double-transposition Haar spectrum)

Let \(T_{22}\) average the coordinate action over the conjugacy class
\(2^2 1^{n-4}\), and average \(P_\Gamma=(I+\sigma)/2\) over the
\(3\binom n4\) double-transposition subgroups. On degree \(j\),

\[
\rho_j^{(22)}
=1-\frac{
4\lambda_j\bigl(n^2-4n+6-\lambda_j\bigr)}
{n(n-1)(n-2)(n-3)},
\tag{7.13}
\]

and

\[
\pi_j^{(22)}
=1-\frac{
2\lambda_j\bigl(n^2-4n+6-\lambda_j\bigr)}
{n(n-1)(n-2)(n-3)}.
\tag{7.14}
\]

For \(n\ge9\), the full nonconstant target-profile gap is \(2/(n-1)\),
attained at \(j=1\). On the exact zero-point-margin space, whenever degree
two occurs, it is

\[
1-\pi_2^{(22)}
=\frac{4(n-4)}{n(n-3)}
=\frac4n+O(n^{-2}).
\tag{7.15}
\]

More precisely, for \(n\ge9\),

\[
\begin{aligned}
\mathbb E_{\Gamma:C_2(22)}A_\Gamma(F)
&=\frac{4(n-4)}{n(n-3)}\|f^F\|_H^2\\
&\quad+\sum_{q=1}^H\frac1{c_q}\sum_{j\ge3}
\frac{
2(j-2)(n-j-1)
\bigl((n-2)(n-4)-\lambda_j\bigr)}
{n(n-1)(n-2)(n-3)}
\|f_{q,j}^F\|_2^2.
\end{aligned}
\tag{7.16}
\]

#### Proof

A set fixed by two disjoint swaps includes both or neither point from each
swapped pair. Therefore

\[
\operatorname{Fix}_k(2^2 1^{n-4})
=\binom{n-4}k+2\binom{n-4}{k-2}
+\binom{n-4}{k-4}.
\tag{7.17}
\]

Equations (7.10), (7.17), and (7.3) simplify to (7.13); taking
\((1+\rho_j^{(22)})/2\) gives (7.14).

As an independent constant check, if \(X\) is the sum of all transpositions
in the group algebra, then

\[
X^2
=\binom n2e
+3\sum_{\text{3-cycles}}g
+2\sum_{\text{double transpositions}}\sigma.
\tag{7.18}
\]

The coefficients count ordered factorizations. Substituting the
transposition ratio \(1-2\lambda_j/[n(n-1)]\) and (7.5) in (7.18)
reproduces (7.13).

The gap in (7.14) is proportional to
\(x(n^2-4n+6-x)\) at \(x=\lambda_j\). For \(n\ge9\) and
\(j\le(n-1)/2\),

\[
\lambda_j\le\lambda_{(n-1)/2}
<\frac{n^2-4n+6}{2},
\tag{7.19}
\]

so it increases with \(j\). Substitution of \(\lambda_1=n\) and
\(\lambda_2=2(n-1)\) gives the asserted gaps. Finally,

\[
\begin{aligned}
&(1-\pi_j^{(22)})-(1-\pi_2^{(22)})\\
&\quad=
\frac{
2(j-2)(n-j-1)
\bigl((n-2)(n-4)-\lambda_j\bigr)}
{n(n-1)(n-2)(n-3)}.
\end{aligned}
\tag{7.20}
\]

Degree decomposition proves (7.16). \(\square\)

All eigenvalue formulas (7.13)--(7.14) are exact at the small endpoints
where the representations occur. The monotonicity and full-gap assertion
above were deliberately stated only for \(n\ge9\); at \(n=7\), degrees two
and three tie, and the \(n=5\) full-gap endpoint is different. The Gaussian
depth regime is eventually within \(n\ge9\).

For comparison, conjugacy-averaged transposition Haar has degree-\(j\)
gap \(\lambda_j/[n(n-1)]\), hence gap \(2/n\) on degrees \(j\ge2\).
Thus both length-two families improve the leading coherent constant by a
factor of two, not its order.

### 7.3 Spectral and log-Sobolev scope

For a fixed subgroup \(\Gamma\), \(P_\Gamma\) has many nonconstant invariant
profiles and therefore no positive gap on the whole target space. The gaps
(7.7) and (7.15) belong to the **uniform conjugacy average** of the target
Haar projectors.

Under the convention

\[
\operatorname{Ent}_\pi(g^2)
\le\frac2{\alpha_{\rm LS}}\,
\langle g,(I-\overline P)g\rangle_\pi,
\tag{7.21}
\]

linearizing at \(g=1+\varepsilon u\), with \(\mathbb E_\pi u=0\), gives

\[
\alpha_{\rm LS}\le\operatorname{gap}(\overline P).
\tag{7.22}
\]

Consequently the target kernels in Theorems 7.1--7.2 have
\(\alpha_{\rm LS}\le2/(n-1)\) for \(n\ge9\). In particular, this route
cannot yield dimension-free target contraction.

None of (7.5)--(7.22) lower-bounds the exact-factor state-chain gap. If
\(K_{\rm sh}\) has more than one communicating class, its global Poincaré
and log-Sobolev constants are zero. On each finite irreducible class they
are positive, but no bound uniform in \(m\) is proved here. Even a strong
within-class mixing bound would only give convergence to
\(\pi_{\mathscr C}\); it would not upper-bound
\(\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H\).

## 8. Compositions, commutators, and the class-bridge screen

Write \(\mathscr C_{\rm tr}(F)\) for the communicating class generated by
the original transposition-component cells.

### Proposition 8.1 (old kernel words cannot merge old classes)

Every composition, convex mixture, holding perturbation, or
reversibilization built from the original kernels \(K_\tau\) is block
diagonal on the partition \(\{\mathscr C_{\rm tr}\}\). In particular it
cannot merge two original classes. The operator commutator

\[
[K_\tau,K_\upsilon]
=K_\tau K_\upsilon-K_\upsilon K_\tau
\tag{8.1}
\]

is also block diagonal, but is a signed operator rather than a Markov
kernel.

#### Proof

Every \(K_\tau\) preserves every original communicating class by
definition. The collection of operators preserving all blocks is closed
under products, sums, adjoints, and insertion of the identity. Formula
(8.1) therefore preserves the blocks as well, while its negative
coefficients preclude a Markov interpretation in general. \(\square\)

Thus a group commutator used as a new coordinate permutation must be
distinguished from an operator commutator of old heat kernels. The former
can define a new owner-group cell; the latter cannot create a new edge.
For example, with the convention
\([x,y]=xyx^{-1}y^{-1}\),

\[
[(a\ b),(b\ c)]=(a\ c\ b),
\tag{8.2a}
\]

so the ternary \(C_3\) cells above are literal short
group-commutator cells. They are not the signed operator (8.1).

There is also a direct deterministic test showing when a proposed
short-permutation packet phase is already an old-class path.

### Theorem 8.2 (pulled-generator reachability)

Let

\[
\sigma=\tau_L\cdots\tau_1,\qquad
\sigma_i=\tau_i\cdots\tau_1,\qquad
\sigma_0=e,
\tag{8.2}
\]

where every \(\tau_i\) is a transposition. Define the pulled
transpositions

\[
\rho_i=\sigma_{i-1}^{-1}\tau_i\sigma_{i-1}.
\tag{8.3}
\]

Then

\[
\rho_1\rho_2\cdots\rho_L=\sigma.
\tag{8.4}
\]

Suppose an exact factor decomposes as

\[
F=P\mathbin{\dot\cup}R,
\tag{8.5}
\]

where the rows \(P\) factorize a middle-root set \(U\), the rows \(R\)
factorize \(U^c\), and

\[
\rho_iU=U\qquad(1\le i\le L).
\tag{8.6}
\]

Then

\[
\sigma P\mathbin{\dot\cup}R
\in\mathscr C_{\rm tr}(F).
\tag{8.7}
\]

More precisely, applying \(\rho_L,\rho_{L-1},\ldots,\rho_1\) successively
to the current \(P\)-packet is a legal path of ordinary
transposition-component switches.

#### Proof

Induction gives

\[
(\rho_1\cdots\rho_{i-1})\rho_i
=\sigma_{i-1}\sigma_{i-1}^{-1}\tau_i\sigma_{i-1}
=\sigma_i,
\tag{8.8}
\]

which proves (8.4).

At a stage involving \(\rho_i\), the current \(P\)-packet still factorizes
\(U\), because every already applied pulled transposition stabilizes \(U\).
The unchanged residual still factorizes \(U^c\). In the ordinary owner
graph for \(\rho_i\), a middle set in \(U\) is joined only to another set
in \(U\), by (8.6); likewise for \(U^c\). Hence no ownership component
crosses the cut \(U/U^c\). The current \(P\)-packet is therefore a union of
whole legal \(\rho_i\)-components, all of which may be switched while all
components in \(R\) are retained.

Applying the pulled transpositions in reverse index order acts on \(P\) by
\(\rho_1\cdots\rho_L=\sigma\). This gives (8.7). \(\square\)

Theorem 8.2 gives a sufficient no-bridge certificate. In particular, if
\(\sigma\) admits a product into transpositions that stabilize \(U\) in
the pulled sense (8.6), then the \(\sigma\)-phase of a root packet is not a
new class edge. Failure of (8.6) for one chosen factorization is **not**
proof of a bridge.

### Proposition 8.3 (two mixed packets are necessary for a bridge)

In an intrinsic \(\Gamma=\langle\sigma\rangle\) cell:

1. a cell with no active packet is a singleton;

2. if exactly one packet is active, every child is a global coordinate
   image \(\sigma^aF\);

3. more generally, choosing the same phase on all active packets produces
   \(\sigma^aF\).

All these children lie in \(\mathscr C_{\rm tr}(F)\). Consequently a new
edge between original classes requires at least two active packets carrying
different phases.

#### Proof

An inactive packet is fixed as a physical row set by all powers of
\(\sigma\). If \(K\) is the sole active packet, then

\[
\sigma^aF=\sigma^aK\cup
\bigcup_{L\ne K}\sigma^aL
=\sigma^aK\cup\bigcup_{L\ne K}L,
\tag{8.9}
\]

which is the corresponding child. The same argument applies when all
active phases agree. Any global coordinate permutation is a product of
transpositions, and the global action of one transposition is obtained by
switching all components of its ordinary cell. Thus every global image is
old-class reachable. \(\square\)

The owner-group theorem guarantees only \(\sigma U=U\), not (8.6). Mixed
short phases are therefore genuine candidate bridges. The following two
statements remain unproved and are not used elsewhere in this report:

* **Unproved bridge existence \(\mathrm{SHB}_m\).** Some mixed short cell
  joins two distinct original transposition classes.

* **Unproved bridge completeness \(\mathrm{SHC}_m\).** The short cells join
  all exact factors, or admit a complete explicit invariant separating
  their classes.

Neither statement follows from Theorem 8.2 or Proposition 8.3.

## 9. A conserved invariant for the even-only short chain

Let

\[
\mathscr G_{\rm ev}
=\{\text{cyclic 3-subgroups and double-transposition subgroups}\},
\qquad
K_{\rm ev}
=\frac1{|\mathscr G_{\rm ev}|}\sum_{\Gamma\in\mathscr G_{\rm ev}}K_\Gamma.
\tag{9.1}
\]

Every phase in this chain is an even coordinate permutation.

### Theorem 9.1 (unoriented-wreath chirality)

Assume \(m\) is even. The set \(\Omega_m\) of unoriented cyclic orders
splits into exactly two \(A_n\)-orbits. After naming them
\(\Omega_m^+\) and \(\Omega_m^-\), the chirality count

\[
\chi(F)=|F\cap\Omega_m^-|
\tag{9.2}
\]

is conserved by every \(K_{\rm ev}\)-move. Hence every communicating class
of \(K_{\rm ev}\) lies in one level set of \(\chi\).

If \(m\) is odd, this chirality is not well-defined on unoriented cyclic
orders and \(A_n\) is transitive on \(\Omega_m\).

#### Proof

Choose an oriented cyclic order representative. A rotation of \(n\) odd
points is an even permutation. A reflection has cycle type
\(1\,2^m\), hence sign \((-1)^m\). When \(m\) is even, the entire dihedral
stabilizer lies in \(A_n\), so the sign of a representative is independent
of rotation and reversal. The two signs are precisely the two
\(A_n\)-orbits.

Replacing a packet \(K\) by \(hK\), with \(h\in A_n\), preserves the
chirality of every row. It therefore preserves (9.2), packet by packet.

When \(m\) is odd, a reflection is odd. Thus the two representative signs
describe the same unoriented order. Equivalently,
\(S_n=A_nD_{2n}\), which makes the \(A_n\)-action transitive. \(\square\)

This is a genuine state-space obstruction for the even-only chain whenever
more than one count in (9.2) is populated by exact factors. It does not
force lower-shadow energy. Indeed, \(A_n\) is transitive on every rank-\(r\)
target slice: a permutation carrying one \(r\)-set to another can have its
parity corrected by a transposition inside the target or its complement.
Thus the associated target-orbit totals are only the already fixed total
loads.

Once transposition cells are included, the acting coordinate groups
generate \(S_n\), and the group-theoretic proof of conservation disappears.
An odd packet phase changes the count by

\[
|K|-2|K\cap\Omega_m^-|.
\tag{9.3}
\]

Therefore \(\chi\) is not a structural invariant of the full mixed move
family whenever a legal packet has nonzero imbalance. Such a packet is
known in the previously audited \(m=4\) exact example. No theorem asserting
one for every even \(m\) is claimed here, and no replacement invariant for
the full mixed chain has been proved.

## 10. What the energy identities reduce the route to

For a class \(\mathscr C\), average restitution over one move type:

\[
\overline V_3(F)
=\mathbb E_{\Gamma:C_3}V_\Gamma(F),
\qquad
\overline V_{22}(F)
=\mathbb E_{\Gamma:C_2(22)}V_\Gamma(F).
\tag{10.1}
\]

Let \(\mathcal S_3(F)\) be the nonnegative second line of (7.8), and let
\(\mathcal S_{22}(F)\) be the nonnegative second line of (7.16). Separate
stationarity (5.8) and the exact spectral decompositions give:

### Theorem 10.1 (stationary restitution ledger)

For every short-chain communicating class \(\mathscr C\), and \(n\ge9\),

\[
\mathbb E_{\pi_{\mathscr C}}\overline V_3
=\frac4n
\left(
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H+\mathfrak B_H
\right)
+\mathbb E_{\pi_{\mathscr C}}\mathcal S_3,
\tag{10.2}
\]

and

\[
\mathbb E_{\pi_{\mathscr C}}\overline V_{22}
=\frac{4(n-4)}{n(n-3)}
\left(
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H+\mathfrak B_H
\right)
+\mathbb E_{\pi_{\mathscr C}}\mathcal S_{22}.
\tag{10.3}
\]

In particular,

\[
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
\le\frac n4\,
\mathbb E_{\pi_{\mathscr C}}\overline V_3-\mathfrak B_H,
\tag{10.4}
\]

and exactly

\[
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
=\frac n4\mathbb E_{\pi_{\mathscr C}}\overline V_3
-\mathfrak B_H
-\frac n4\mathbb E_{\pi_{\mathscr C}}\mathcal S_3.
\tag{10.4a}
\]

#### Proof

Average (5.8) over the indicated conjugate subgroups, then substitute
(7.8) or (7.16) and use
\(\|f^F\|_H^2=\mathcal Q_H(F)+\mathfrak B_H\). Nonnegativity of the
surplus gives (10.4). \(\square\)

Thus a sufficient restitution gate for the desired stationary estimate is

\[
\mathbb E_{\pi_{\mathscr C}}\overline V_3
\le\frac4n\left(\mathfrak B_H+C_AHB\right)
\tag{10.5}
\]

for at least one class \(\mathscr C\). This would imply
\(\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H\le C_AHB\), hence some literal
exact factor in that class has the same bound. Statement (10.5) is
**unproved**. It is a sufficient condition, not a reformulation of MWB and
not a labelled synchronization assertion.

The exact energy Dirichlet form (6.2) does not supply (10.5). If a
within-class state gap \(\gamma_{\mathscr C}\) were known, Poincaré would
only say

\[
\operatorname{Var}_{\pi_{\mathscr C}}(\mathcal Q_H)
\le\frac1{\gamma_{\mathscr C}}
\mathscr E_{\mathscr C}^{\rm sh}(\mathcal Q_H,\mathcal Q_H).
\tag{10.6}
\]

This controls fluctuations about the stationary mean, not that mean.
Moreover, (6.1) may vanish for a generator even when \(A_\Gamma\) is large.
The log-Sobolev inequality has the same limitation.

## 11. Independent audit and exact final status

Two independent theorem audits were run without web search or finite
computation.

1. The first audit rederived the owner-group rebasing theorem, the class
   partition, (5.4)--(5.18), and every factor in the Gram variance
   (6.1)--(6.7). It specifically checked covariance cancellation for packet
   pairs sharing one endpoint and the fixed-orbit endpoint \(d=1\).

2. The second audit independently rederived both character ratios,
   Haar eigenvalues, coherent gaps, surplus factorizations, the
   pulled-generator order in Theorem 8.2, the two-packet necessity, and the
   chirality theorem.

The audits forced the following scope corrections, all incorporated above:

* fixed \(C_2/C_3\) target orbits have size \(1\) or \(p\), not always \(p\);

* coherent gaps belong to conjugacy-averaged target projectors, not fixed
  projectors and not the exact-factor state chain;

* double-transposition monotonicity is asserted only for \(n\ge9\);

* destruction of chirality by transposition packets is not asserted
  uniformly for every even \(m\);

* zero Gram variance for one generator is not zero Dirichlet form for the
  full mixed chain.

The proved theorem-level output is therefore:

* intrinsic literal binary and ternary owner cells for all short cyclic
  subgroups;

* a reversible positive-semidefinite short heat chain with exact
  communicating-class and stationary-law description;

* the exact multidepth drift, every binary/ternary integer orbit floor, and
  the exact squared-Gram energy Dirichlet form;

* exact \(C_3\) and double-transposition coherent spectra, both only
  \(4/n+O(n^{-2})\) on exact centered loads;

* a rigorous old-class reachability screen for permutation words and
  commutators;

* a genuine chirality invariant for the even-only chain when \(m\) is
  even.

The following remain expressly unproved:

1. existence of a mixed short-packet bridge between two old classes;

2. connectivity, or a complete nontrivial invariant, for the full mixed
   short chain;

3. a state-chain spectral or log-Sobolev bound uniform in \(m\);

4. the restitution estimate (10.5), or any consequence of order
   \(O_A(H_A\operatorname{Cat}_m)\).

Accordingly, the short-permutation/commutator enlargement is mathematically
sound and supplies additional intrinsic cells, but it does not yet prove
the contiguous-OR width conjecture, MWB, or labelled common-owner
synchronization.
