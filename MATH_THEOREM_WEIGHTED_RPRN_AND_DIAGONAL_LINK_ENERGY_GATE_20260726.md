# Weighted RPRN and the diagonal link-energy gate

Date: 2026-07-26

Scope: constant-one repaired promotion-ring packing only.

## 0. Verdict

The exceptional-neighbourhood clause in the original RPRN formulation is
too strong.  The correct condition is weighted: if the bad owners carry
total residual edge incidence

\[
                    \sum_{X\in\mathcal B_t}d_t(X)
                    =o(N_HR_t),                         \tag{0.1}
\]

then they are harmless, regardless of how many root neighbourhoods their
static containments or literal residual links cover.

The support-reachable family from the preceding counterexample satisfies
(0.1).  Indeed, with

\[
 Q=\binom{m+H}{H},\qquad
 |\mathcal F|=(1+o(1)){m^2\over Q}W,
\]

and \(D_X=(1+o(1))R\),

\[
 \sum_{X\in\mathcal F'}d_{\rm res}(X)
 \le |\mathcal F|D_X
 \le {m^3+o(m^3)\over Q}\,N_HR
 =o(N_HR).                                           \tag{0.2}
\]

Thus that family is not an obstruction to weighted regeneration even
though its actual residual links meet \((4/5-o(1))N_H\) roots.

For \(O_z(m)\) unbiased slow-greedy time, weighted regeneration follows
from one exact incidence-weighted diagonal mesh estimate, stated in
Section 4.  The required martingale calculation and all constants close:
the bad owner incidence is at most

\[
  \exp[-c_z(\log m)^2]\,rE_t=o(E_t)=o(N_HR_t).       \tag{0.3}
\]

What is not presently proved is the dynamic diagonal mesh estimate.
The plain disjoint-mesh catalogue controls distinct next edges.  The
new multiplicity powers \(B^h\) correctly encode repeated use of the same
next edge at one state, but their \(O_z(m)\)-time propagation still needs
a buffered order hierarchy.  Without that buffer, a level \(J-1\) energy
can leave the recorded hierarchy in one generator step.

Accordingly the rigorous status is:

\[
 \boxed{\text{weighted regeneration is reduced to the diagonal
 link-energy hierarchy (4.4); that hierarchy remains the sole gate.}}
                                                               \tag{0.4}
\]

## 1. The weighted criterion

At time \(t\), let

\[
 \mathcal H_t=(\mathcal A_t,\mathcal X_t;\mathcal E_t)
\]

be the active rooted owner hypergraph.  Put

\[
 E_t=|\mathcal E_t|,qquad
 I_t^R=\sum_{A\in\mathcal A_t}d_t(A)=E_t,qquad
 I_t^O=\sum_{X\in\mathcal X_t}d_t(X)=rE_t.           \tag{1.1}
\]

For fixed surviving root density \(x_t\ge z>0\), the reference degree
ledger gives

\[
 E_t=(1+o(1))N_Hx_tR_t=\Theta_z(N_HR_t).             \tag{1.2}
\]

### Definition 1.1 (WRPRN at density \(z\))

At every time before \(x_t=z\), choose exceptional root and owner sets
\(\mathcal B_t^R,\mathcal B_t^O\).  The nonexceptional resources obey the
reference degree, internal-overlap, and path-link estimates needed for a
fresh slow bite.  The exceptional sets are required only to satisfy

\[
 \boxed{
 \sum_{A\in\mathcal B_t^R}d_t(A)
 +\sum_{X\in\mathcal B_t^O}d_t(X)=o(E_t).}            \tag{1.3}
\]

No bound is imposed on the number of roots in

\[
 \bigcup_{X\in\mathcal B_t^O}
 \{A:\Lambda_t(A,X)=1\}.                             \tag{1.4}
\]

The normalization \(o(E_t)\), rather than \(o(I_t^O)\), is essential.
Every active edge contains \(r\sim m\) owners.  An \(o(1)\)-fraction of
owner incidences could still charge a positive fraction of all active
edges; (1.3) rules that out.

## 2. Weighted exceptions are harmless

### Proposition 2.1

WRPRN\((z)\) is sufficient for the slow-bite trajectory down to density
\(z\).  If it holds for every fixed \(z>0\), diagonalization gives a
matching missing \(o(N_H)\) roots and hence an \(o(W)\) owner leave.

#### Proof

Suppress every active edge incident to an exceptional vertex.  The number
of suppressed edges is at most

\[
 \sum_{A\in\mathcal B_t^R}d_t(A)
 +\sum_{X\in\mathcal B_t^O}d_t(X)=o(E_t).            \tag{2.1}
\]

Thus suppression changes the total jump rate and every edge-averaged
drift by \(o(1)\).

For completeness, the same conclusion holds rootwise after a second
weighted cleaning.  Let \(L_t(A)\) be the number of suppressed options
at root \(A\).  Since every edge has one root,

\[
 \sum_A L_t(A)\le o(E_t).                            \tag{2.2}
\]

Choose \(\epsilon_m\downarrow0\) slowly enough that the right side of
(2.2) is \(o(\epsilon_mE_t)\).  Roots with
\(L_t(A)>\epsilon_mR_t\) number \(o(N_H)\).  Under the reference degree
cap \(d_t(A)=O_z(R_t)\), their total degree mass is \(o(E_t)\), so they
may be added to \(\mathcal B_t^R\).  Every remaining root loses only
\(o(R_t)\) options.

The clean active pool therefore has the same slow-bite drift as the
reference pool up to \(o(1)\).  Running for

\[
                  T_z=K\log(1/z)+o_z(K)=O_z(m)       \tag{2.3}
\]

leaves at most \((z+o(1))N_H\) roots.  Applying this for fixed
\(z=1/a\) and taking a sufficiently slow diagonal \(a=a(m)\to\infty\)
gives root leave \(o(N_H)\).  The exact owner ledger then gives
\(o(W)\). \(\square\)

## 3. The weighted martingale calculation

Use continuous random greedy with rate

\[
                 \nu_t={1\over KR_t}                \tag{3.1}
\]

on every active edge.  For a protected owner \(X\) and pairwise disjoint
protected edges \(e_1,\ldots,e_j\), write

\[
 A_C=a_{X,t}(e_1,\ldots,e_j),\qquad
 A_C(g)=a_{X,t}(e_1,\ldots,e_j,g),                  \tag{3.2}
\]

where \(C=(X;e_1,\ldots,e_j)\) and \(g\) is disjoint from all protected
resources.  Selection of \(g\) changes the cluster size by exactly
\(-A_C(g)\).

Put

\[
 J=\lceil C_0\log m\rceil,
 \qquad
 \varepsilon_j(t)={C_1j^4\over m^2u_t},
 \qquad u_t\ge z.                                    \tag{3.3}
\]

For \(j=0\), \(A_C=d_t(X)\) and \(A_C(g)=a_{X,t}(g)\).
The conditional quadratic variation of the normalized degree martingale
is

\[
 {d\langle M_X\rangle_t\over dt}
 ={1\over KR_t}\sum_g{a_{X,t}(g)^2\over d_t(X)^2}.   \tag{3.4}
\]

If the right side is \(O((m^2u_t)^{-1})\), then over \(T_z=O_z(m)\)
the normalized quadratic variation is \(O_z(1/m)\).  A constant relative
degree deviation consequently has probability \(e^{-\Omega_z(m)}\).
That estimate is already strong enough in principle, because the weighted
criterion needs bad-owner probability \(o(1/m)\), not a union bound over
all \(W\) owners.

To make the stopping argument regenerate (3.4), one must also control the
same martingale for every protected mesh cluster.  This is where diagonal
powers enter.

## 4. The exact diagonal link-energy estimate

The required statement is the following.

### DLE\((z,J)\) (diagonal link-energy regeneration)

Uniformly before root density \(z\), outside clusters whose base owner
incidence mass is \(o(E_t)\), for every

\[
 0\le j<J,qquad 2\le\ell\le J-j,
\]

one has

\[
 \boxed{
 \sum_{g}^{*} A_C(g)^\ell
 \le (1+o(1))KR_t A_C^\ell
       \left({C_z(j+\ell)^4\over m^2u_t}\right)^{\ell-1}.}
                                                               \tag{4.1}
\]

The star restricts to next edges \(g\) disjoint from the protected
cluster.  For \(j=0,\ell=2\), (4.1) is exactly

\[
 \sum_g a_{X,t}(g)^2
 \le(1+o(1))KR_td_t(X)^2{C_z\over m^2u_t},           \tag{4.2}
\]

which inserted in (3.4) gives the desired quadratic variation.

An incidence-weighted version is sufficient.  Let
\(\mathcal B_{j,\ell,t}\) be the owners \(X\) for which some active
protected \(j\)-cluster centred at \(X\) violates (4.1).  It is enough
that

\[
 \boxed{
 \sum_{X\in\mathcal B_{j,\ell,t}}d_t(X)=o(E_t)
 \quad\text{uniformly for }j+\ell\le J.}             \tag{4.3}
\]

One then suppresses the edges meeting these owners.  This is the literal
weighted form: diagonal-energy failure is permitted on arbitrary static
neighbourhoods, provided its owner incidence is \(o(E_t)\).

For use independent of normalization conventions, the minimal required
consequence can be stated directly as

\[
 \boxed{
 {1\over I_t^O}
 \sum_X d_t(X)\,
 \Pr\!\left(
   \sup_{s\le T_z}
   \left|{d_s(X)\over\mathcal D_O(s)}-1\right|>m^{-1/10}
   \ \middle|\ \mathcal F_t
 \right)
 =o(1/m).}                                           \tag{4.4}
\]

Because \(I_t^O=rE_t\), the left side of (4.4) is the expected bad-owner
incidence fraction.  The bound \(o(1/m)\) is exactly what makes the
expected bad-owner degree mass \(o(E_t)\).  DLE implies (4.4), as shown
next.

## 5. DLE implies weighted regeneration

### Theorem 5.1 (conditional weighted trajectory theorem)

Assume DLE\((z,J)\), its root analogue, and the corresponding
first-moment drift identities.  Then WRPRN\((z)\) holds with probability
\(1-o(1)\) throughout \(T_z=O_z(m)\) continuous unbiased slow-greedy time.

#### Proof

Apply the generator to \(A_C^s\).  A jump caused by \(g\) contributes

\[
 (A_C-A_C(g))^s-A_C^s
 =\sum_{\ell=1}^s(-1)^\ell\binom s\ell
       A_C^{s-\ell}A_C(g)^\ell.                    \tag{5.1}
\]

After summing over (g), the term of order \(\ell\) is the diagonal
power in (4.1).  DLE therefore bounds the complete generator, not merely
its quadratic part.

Choose \(c_0>0\) small enough that \(2s\le J\), and put

\[
 s=\lceil c_0\log m\rceil,
 \qquad \eta=m^{-1/10}.                             \tag{5.2}
\]

Since \(u_t\ge z\) and \(T_z=O_z(m)\), the effective accumulated mesh
parameter is

\[
 T_z{Cs^4\over m^2u_t}
 =O_z\!\left({(\log m)^4\over m}\right).            \tag{5.3}
\]

The standard conditional Bell-polynomial expansion of (5.1), now
justified term by term by DLE, yields

\[
 {1\over I_t^O}
 \mathbb E\sum_X d_t(X)
 \left|{M_{T_z}(X)\over d_t(X)}\right|^{2s}
 \le
 \left({Cs^5\over m}\right)^s.                    \tag{5.4}
\]

The power \(s^5\) consists of the \(s\) from the Bell partition count and
the \(s^4\) in the mesh catalogue.  No hidden \(K\)-dependent constant
occurs.

Weighted Markov applied to (5.4) gives

\[
 {1\over I_t^O}
 \mathbb E\sum_{X:\,|M_{T_z}(X)|>\eta d_t(X)}d_t(X)
 \le
 \left({Cs^5\over m\eta^2}\right)^s
 \le\exp[-c(\log m)^2].                           \tag{5.5}
\]

Indeed \(m\eta^2=m^{4/5}\), whereas \(s^5=(\log m)^{O(1)}\).
The identical calculation applies at \(O_z(1)\) checkpoints and to the
root and drift energies.  Markov's inequality over the process randomness
therefore gives, with probability \(1-o(1)\), bad owner incidence at most

\[
 \beta_m I_t^O,
 \qquad \beta_m=\exp[-c'(\log m)^2].               \tag{5.6}
\]

Since \(I_t^O=rE_t\) and

\[
                  r\beta_m=o(1),                   \tag{5.7}
\]

the bad owner mass in (5.6) is \(o(E_t)\).  The root calculation is
already normalized by \(I_t^R=E_t\).  Hence (1.3) holds at every
checkpoint.  Proposition 2.1 completes the trajectory. \(\square\)

## 6. Exact status of the multiplicity hierarchy

The available catalogue bounds quantities of the form

\[
 \sum_{(g_1,\ldots,g_\ell)}^*
 a_{X,t}(e_1,\ldots,e_j,g_1,\ldots,g_\ell)^2,        \tag{6.1}
\]

where the \(g_i\) are distinct and pairwise disjoint.  In contrast, the
order-\(\ell\) generator term in (5.1) is

\[
                  \sum_g A_C(g)^\ell.               \tag{6.2}
\]

This repeats the same next edge \(g\), \(\ell\) times.  Equation (6.2) is
not “exactly a distinct-edge disjoint mesh energy of order \(j+\ell\)”.
Replacing it by (6.1) discards the diagonal, and no marginal-product
argument recovers that diagonal.

The multiplicity-aware quantities

\[
 B_X^{\boldsymbol c}(e_1,\ldots,e_j)
 =\sum_{f\ni X}\prod_i\binom{|f\cap e_i|}{c_i}
\]

and their power energies do repair this algebraic defect: the power
\((B_X^{\boldsymbol c})^\ell\) records the repeated-\(g\) diagonal.
However, a finite hierarchy through total witness order \(J\) is not
automatically regenerative.  Starting from order \(J-1\), one generator
increment may require order \(J+1\).  Thus the statement that every term
first leaving the hierarchy contains \(J\) small factors is false for
high starting levels.

A sufficient buffered closure is the following.  Take

\[
 J=C_0\log m,\qquad L=C_1(\log m)^2,                \tag{6.3}
\]

prove the multiplicity-power catalogue through order \(L\), and require
regeneration only through core order \(J\).  Any generator chain leaving
the buffer from a core energy then contains
\(\Omega((L-J)/J)=\Omega(\log m)\) order-raising steps.  At fixed \(z\),
each step costs at most

\[
 T_z\,{CL^4\over m^2z^2}
 =O_z\!\left({(\log m)^8\over m}\right).             \tag{6.4}
\]

The buffer tail is consequently
\[
 \exp[-\Omega((\log m)^2)].
\]
Proving the corresponding stopped generator inequality for the whole
buffer, or proving DLE directly, is the exact remaining propagation
estimate.

A sufficient route to DLE would be the conditional ratio bound

\[
 \max_g{A_C(g)\over A_C}
 \le {C_z(j+1)^4\over m^2u_t},                    \tag{6.5}
\]

together with the exact first-moment identity

\[
 \sum_g^*A_C(g)=(1+o(1))KR_tA_C.                   \tag{6.6}
\]

Indeed, multiplying (6.6) by the \((\ell-1)\)-st power of (6.5) gives
(4.1).  The initial static path-mesh catalogue gives an absolute bound on
\(A_C(g)\), but not the dynamic relative bound (6.5) when \(A_C\) has
been depleted.  Proving (6.5) outside incidence mass \(o(E_t)\), proving
the buffered closure (6.3)--(6.4), or
proving (4.3) directly without a pointwise ratio, is the exact remaining
link-energy theorem.

## 7. Consequences and scope

The weighted criterion resolves the apparent conflict with the reachable
counterexample: a family may touch every root and still carry too little
edge mass to perturb the slow bite.

The \(O_z(m)\) martingale constants close once DLE is supplied.  In
particular, neither an exponential union bound over owners nor the old
exceptional-neighbourhood clause is needed.

The multiplicity powers justify the one-state repeated-edge diagonal.
What is not yet justified is their unbuffered propagation for all
\(O_z(m)\) time.  Until DLE or the buffered generator closure is proved,
the full weighted trajectory theorem remains conditional.  This is
strictly sharper than the former generic “hereditary regeneration” gate:
it is the explicit family (4.1), its weighted form (4.3), or equivalently
the buffer estimate (6.3)--(6.4).
