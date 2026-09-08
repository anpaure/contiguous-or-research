# Private-switch bilinear first-kill identity and a regular counterexample

**Date:** 2026-08-06  
**Method:** exact operator deletion algebra and a three-state regular model;
no computation or search  
**Status:** proof-safe.  The corrected covariance/generator defect has an
exact signed first-kill decomposition.  A killed covariance row does not
dominate its incident switch boundary, even in a transitive regular
one-occurrence host.  A future-potential or host-specific signed
carre-du-champ lemma is genuinely necessary.

## 1. Abstract private-switch frame

Fix one resource Hilbert space `H`.  Let `V` be a finite set of atomic
candidate rows.  Associate to `a in V` an incidence vector `z_a in H`, a
positive covariance weight `mu_a`, and put

\[
 B=\sum_{a\in V}\mu_a z_az_a^*.
\tag{1.1}
\]

Let `G=(V,E)` be a weighted private-switch graph.  For `ab in E`, assume

\[
 b_{ab}:=z_a-z_b
\]

is one signed Johnson occurrence, and give the edge weight `w_ab`.  Put

\[
 L=\sum_{ab\in E}w_{ab}b_{ab}b_{ab}^*.
\tag{1.2}
\]

Assume the pristine normalization

\[
 B=RL=LR
\tag{1.3}
\]

on `H`, with `R` positive semidefinite.  This is the well-typed form of
the pristine Johnson identity.

For a live candidate set `S subseteq V`, take the literal induced current
operators

\[
 B_S=\sum_{a\in S}\mu_a z_az_a^*,
 \qquad
 L_S=\sum_{ab\in E(S)}w_{ab}b_{ab}b_{ab}^*.
\tag{1.4}
\]

This is exactly the frozen-coefficient model in which a covariance row is
present iff its candidate is live and a private switch is present iff both
of its endpoint candidates are live.

For a real scalar `eta`, define the symmetrized stopped operator defect

\[
 H_S^{(\eta)}
 =B_S-B+{\eta\over2}
 \left(R(L-L_S)+(L-L_S)R\right).
\tag{1.5}
\]

Its quadratic form is

\[
 \langle f,H_S^{(\eta)}f\rangle
 =\langle f,(B_S-B)f\rangle
   +\eta\operatorname {Re}\langle f,R(L-L_S)f\rangle.
\tag{1.6}
\]

The coefficient `eta=2` is the row requested in the parent task; the
identity below is stated for arbitrary `eta` so normalization conventions
remain visible.

## 2. Exact signed first-kill identity

Suppose `a in S` is killed and put `S'=S-{a}`.  Write

\[
 u_c=\langle z_c,f\rangle,
 \qquad v_c=\langle z_c,Rf\rangle.
\tag{2.1}
\]

### Theorem 2.1 (one-step identity)

One has exactly

\[
 \boxed{
 \begin{aligned}
 \langle f,(H_{S'}^{(\eta)}-H_S^{(\eta)})f\rangle
 ={}&-\mu_a u_a^2\\
 &+\eta\sum_{b\in N_G(a)\cap S'}
 w_{ab}(u_a-u_b)(v_a-v_b).
 \end{aligned}}
\tag{2.2}
\]

#### Proof

The covariance difference is

\[
 B_{S'}-B_S=-\mu_a z_az_a^*.
\]

The switch edges removed at this step are precisely `ab` with
`b in S'`, so

\[
 L_S-L_{S'}
 =\sum_{b\in N(a)\cap S'}w_{ab}b_{ab}b_{ab}^*.
\]

Insert these two identities into `(1.5)`.  Since

\[
 \langle b_{ab},f\rangle=u_a-u_b,
 \qquad
 \langle b_{ab},Rf\rangle=v_a-v_b,
\]

the symmetric two terms are equal real scalars and give `(2.2)`.  \(\square\)

### Corollary 2.2 (pathwise earliest-kill partition)

For a deletion order `a_1,...,a_m`, every switch edge `ab` occurs in
exactly one sum in `(2.2)`: the step at which its first endpoint is killed.
Thus

\[
 \boxed{
 \begin{aligned}
 \langle f,(H_{S_m}^{(\eta)}-H_{S_0}^{(\eta)})f\rangle
 ={}&-\sum_{a\in S_0-S_m}\mu_a u_a^2\\
 &+\eta\sum_{ab\in E(S_0)\setminus E(S_m)}
 w_{ab}(u_a-u_b)(v_a-v_b).
 \end{aligned}}
\tag{2.3}
\]

This is the exact signed first-kill formula sought in the raw switch
programme.  It pairs every missing generator edge to the covariance row
killed first, but makes no sign assertion.

Compensated future weights add their predictable coefficient increments to
`(2.2)`; they do not change its incidence algebra.

## 3. The paired killed row does not dominate

The failure is already present in the smallest nontrivial transitive
model.

Let

\[
 \mathcal H={\bf1}^\perp\subset\mathbb R^3,
 \qquad V=\{1,2,3\},
 \qquad z_a=\Pi_{\mathcal H}e_a,
 \qquad \mu_a=1.
\]

Take the complete switch graph `K_3` with

\[
 w_{ab}=1/3.
\]

Then every switch changes exactly one occurrence,

\[
 z_a-z_b=e_a-e_b,
\]

and, on `H`,

\[
 B=I_{\mathcal H},
 \qquad L=I_{\mathcal H},
 \qquad R=I_{\mathcal H}.
\tag{3.1}
\]

The model is fully `Sym(3)`-transitive and regular.  Start from
`S={1,2,3}`, kill candidate `a=1`, and take

\[
 f=(0,1,-1)\in\mathcal H.
\]

The killed covariance row has value

\[
 \mu_1u_1^2=f_1^2=0,
\]

whereas its two incident switch edges give

\[
 \sum_{b=2,3}w_{1b}(u_1-u_b)(v_1-v_b)
 ={1\over3}(1+1)={2\over3}.
\]

Consequently

\[
 \boxed{
 \langle f,(H_{S-\{1\}}^{(\eta)}-H_S^{(\eta)})f\rangle
 ={2\eta\over3}>0}
\tag{3.2}
\]

for every `eta>0`; at the requested normalization `eta=2` it is `4/3`.
The boundary can therefore be positive while its paired killed covariance
row is exactly zero.

This rules out every pointwise inequality of the form

\[
 \text{switch boundary at the first kill}
 \le C\,\mu_a(Kf(a))^2
\]

under only transitivity, regularity, one-occurrence switching, and the
pristine identity `B=RL`.

## 4. What a Schur-complement argument would have to add

An induced subgraph simply deletes all switch conductances incident to a
killed candidate.  Thomson monotonicity controls the quadratic resistance

\[
 \langle b_{ab},Rb_{ab}\rangle,
\]

but the stopped linear boundary in `(2.2)` is the signed product

\[
 (u_a-u_b)(v_a-v_b).
\]

There is no pointwise comparison between the latter and `u_a^2`, as
`(3.2)` shows.

A genuine Schur-complement closure would need to replace the induced
generator `L_S` by a Kron-reduced generator and simultaneously replace the
covariance frame so that a current identity

\[
 B_S=R_S L_S
\]

survives every kill.  Neither operation is part of the present raw FIFO
process.  Applying Thomson's principle to the pristine resistance alone
does not manufacture this identity.

## 5. Exact remaining signed lemma

The local target can now be stated without a type ambiguity.

> **Private-switch first-kill carre lemma.**  For the actual FIFO private
> frame, the future-weighted sum of the positive Bellman contributions
> in `(2.2)`, together with the coefficient, adapted-vector, and noise
> increments, admits a nonnegative Doob supersolution whose initial value
> and priced `(ROc)`/`(FE3)` injections total `O(M/d^4)`.

Equivalently, one needs a host-specific signed estimate for

\[
 \Gamma_a(u,v)
 :=\sum_{b\in N(a)\cap S'}w_{ab}
       (u_a-u_b)(v_a-v_b),
 \qquad v=K Rf,
\tag{5.1}
\]

after pairing it with `-mu_a u_a^2` and the future relation potential.

The exact first-kill decomposition `(2.2)` is useful progress: there is no
occupation-time loss and every switch edge is charged once.  The regular
counterexample proves that the signed future-potential input cannot be
deleted from the lemma.
