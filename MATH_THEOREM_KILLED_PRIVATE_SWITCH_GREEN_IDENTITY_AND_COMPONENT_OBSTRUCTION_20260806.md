# Killed private-switch Green identity and the component obstruction

**Date:** 2026-08-06  
**Method:** exact finite-dimensional Green formula, induced-graph coarea,
and the Dirichlet projection onto private-switch components; no computation
or search  
**Status:** proof-safe algebraic reduction.  This note replaces the
type-unsafe scalar-resolvent use in the withdrawn `(FSW)` argument.  It
does **not** prove the stopped Bellman estimate.  It identifies two exact
terms which a private-switch proof must control: a cut flux and a
candidate-fibre intertwining defect.

The notation is chosen to separate the two Hilbert spaces which were
conflated in the failed argument:

* `H` is a resource-layer Hilbert space;
* `R=L^dagger B` acts only on `H`;
* `A` is the occurrence-labelled candidate set;
* the private-switch Laplacian acts on `R^A`.

Everything below is a frozen-state identity.  Predictable changes of the
actual vector, the weights, and the resolvent, as well as the non-isotropic
noise, remain separate Bellman terms.

## 1. Candidate realization of the pristine operators

Let `H` be a finite-dimensional real Hilbert space.  Let `A` be a finite
candidate set, let

\[
 M=\operatorname {diag}(m_a:a\in A),\qquad m_a>0,
\tag{1.1}
\]

and let

\[
 K:H\longrightarrow \mathbb R^A,
 \qquad (Kf)_a=\langle k_a,f\rangle_H.
\tag{1.2}
\]

Thus `k_a` is the occurrence-incidence row of candidate `a`; in the FIFO
application, `(Kf)_a` is the sum of `f` over the named resource
occurrences of that row.

Let `Gamma` be a weighted undirected graph on `A`, with private-switch
Laplacian

\[
 \Lambda=\sum_{\{a,b\}\in E(\Gamma)}
 w_{ab}(e_a-e_b)(e_a-e_b)^*,\qquad w_{ab}>0.
\tag{1.3}
\]

Define the pullback covariance and pullback switch generator by

\[
 B=K^*MK,
 \qquad
 L=K^*\Lambda K.
\tag{1.4}
\]

Assume

\[
 \ker L\subseteq\ker B,
 \qquad BL=LB.
\tag{1.5}
\]

These are the pristine Johnson-orbit hypotheses.  On `(ker L)^perp`, put

\[
 R=L^\dagger B.
\tag{1.6}
\]

Then `R` is self-adjoint and positive semidefinite, and

\[
 LR=RL=B.
\tag{1.7}
\]

For `f in H`, write

\[
 g=Kf,\qquad h=KRf.
\tag{1.8}
\]

### Proposition 1.1 (the well-typed pristine bilinear identity)

For every `f in H`,

\[
 \boxed{
 \langle f,Bf\rangle_H
 =\sum_{\{a,b\}\in E(\Gamma)}
 w_{ab}(g_a-g_b)(h_a-h_b).}
\tag{1.9}
\]

#### Proof

The right side is

\[
 \langle Kf,\Lambda KRf\rangle
 =\langle f,K^*\Lambda KRf\rangle
 =\langle f,LRf\rangle
 =\langle f,Bf\rangle.
\]

No resolvent is applied to the scalar `g_a`; `R` is first applied to the
resource vector `f`, after which `K` produces the second candidate
function `h`.  \(\square\)

This is the exact correction to the operator type error.  The private
switch form which is relevant to the Bellman drift is **bilinear** in
`Kf` and `KRf`, not the scalar Dirichlet form in `Kf` alone.

## 2. The exact induced-live-set identity

For a live candidate set `U subseteq A`, let `P_U` be coordinate
restriction to `U`.  Define

\[
 M_U=P_UMP_U,
\tag{2.1}
\]

and, crucially, let `Lambda_U` be the **induced-edge** Laplacian

\[
 \Lambda_U=
 \sum_{\{a,b\}\subseteq U}w_{ab}
 (e_a-e_b)(e_a-e_b)^*.
\tag{2.2}
\]

It is not the principal submatrix of `Lambda`: boundary-edge degrees are
deleted along with their edges.  Put

\[
 B_U=K^*M_UK,
 \qquad
 L_U=K^*\Lambda_UK.
\tag{2.3}
\]

The frozen stopped Bellman residue is

\[
 \mathcal D_U(f)
 =\langle f,B_Uf\rangle
 -\operatorname {Re}\langle f,RL_Uf\rangle.
\tag{2.4}
\]

All objects are real here, so `Re` only records the correct symmetric
interpretation.

Define the candidate intertwining defect

\[
 \boxed{\mathcal H=MK-\Lambda KR.}
\tag{2.5}
\]

It is invisible after pulling back to the complete resource layer:

\[
 \boxed{K^*\mathcal H=B-LR=0.}
\tag{2.6}
\]

It need not vanish candidate by candidate.

### Theorem 2.1 (killed private-switch Green identity)

For every live set `U` and every `f in H`,

\[
 \boxed{
 \begin{aligned}
 \mathcal D_U(f)
 ={}&\langle P_UKf,P_U\mathcal Hf\rangle_{\mathbb R^A}\\
 &+\sum_{\substack{a\in U,\ b\notin U\\\{a,b\}\in E(\Gamma)}}
 w_{ab}\,g_a(h_a-h_b).
 \end{aligned}}
\tag{2.7}
\]

Equivalently, since the complete pullback of `mathcal H` vanishes,

\[
 \langle P_UKf,P_U\mathcal Hf\rangle
 =-\langle P_{A\setminus U}Kf,
          P_{A\setminus U}\mathcal Hf\rangle.
\tag{2.8}
\]

#### Proof

By (2.5), pointwise on candidate space,

\[
 Mg=\Lambda h+\mathcal Hf.
\tag{2.9}
\]

Discrete Green summation over `U` gives

\[
 \begin{aligned}
 \sum_{a\in U}g_a(\Lambda h)_a
 ={}&\sum_{\{a,b\}\subseteq U}
       w_{ab}(g_a-g_b)(h_a-h_b)\\
 &+\sum_{\substack{a\in U,\ b\notin U\\a\sim b}}
       w_{ab}g_a(h_a-h_b).
 \end{aligned}
\tag{2.10}
\]

Insert (2.9) in the covariance term of (2.4), and subtract the first sum
in (2.10), which is exactly
`<f,R L_U f>`.  This proves (2.7).  Equation (2.8) follows from

\[
 \langle Kf,\mathcal Hf\rangle
 =\langle f,K^*\mathcal Hf\rangle=0.
\]

\(\square\)

The first term in (2.7) is not a switch resistance and is not indexed by a
boundary blocker.  It is the price of knowing only the projected identity
`K^* Lambda K=L`, rather than a pointwise intertwining identity on
candidate space.

### Corollary 2.2 (one killed batch)

Let `S subseteq U`, and put `U'=U\setminus S`.  With the vector `f` and all
weights frozen,

\[
 \boxed{
 \begin{aligned}
 \mathcal D_{U'}(f)-\mathcal D_U(f)
 ={}&-\sum_{a\in S}m_ag_a^2\\
 &+\sum_{\substack{\{a,b\}\in E(\Gamma[U])\\
                    \{a,b\}\cap S\ne\varnothing}}
 w_{ab}(g_a-g_b)(h_a-h_b).
 \end{aligned}}
\tag{2.11}
\]

For one killed candidate `a`, this is

\[
 -m_ag_a^2+
 \sum_{b\in U\setminus\{a\}}w_{ab}
 (g_a-g_b)(h_a-h_b).
\tag{2.12}
\]

#### Proof

Passing from `U` to `U'` deletes precisely the mass rows in `S` and every
induced switch edge having at least one endpoint in `S`.  Subtract (2.4)
for the two sets.  \(\square\)

Equation (2.11) is the coefficient-free, frozen-vector version of the
earliest-kill boundary.  The actual future-fugacity coefficient must
multiply the whole right side.  It is not enough to identify only the
coefficient of the first, negative term.

## 3. Dirichlet and Schur-complement boundary

Let `Q` be orthogonal projection in candidate space onto

\[
 \ker\Lambda
 =\operatorname {span}\{{\bf1}_{C}:C
          \text{ is a connected component of }\Gamma\}.
\tag{3.1}
\]

Applying `Q` to (2.5) gives the exact invariant obstruction

\[
 \boxed{Q\mathcal H=QMK.}
\tag{3.2}
\]

### Proposition 3.1 (component-charge criterion)

For a fixed `f`, the candidate Poisson equation

\[
 \Lambda u=MKf
\tag{3.3}
\]

has a solution if and only if, for every component `C` of `Gamma`,

\[
 \boxed{
 \sum_{a\in C}m_a(Kf)_a=0.}
\tag{3.4}
\]

It has a solution simultaneously for every `f in H` if and only if

\[
 \boxed{
 \sum_{a\in C}m_ak_a=0\quad\text{as a functional on }H
 \quad(C\in\operatorname {Comp}(\Gamma)).}
\tag{3.5}

When `(3.4)` holds, the minimum-energy solution is

\[
 u=\Lambda^\dagger MKf
\tag{3.6}

modulo component constants, and the ordinary Dirichlet/Thomson principle
applies.  When `(3.4)` fails, no Schur complement built solely from the
private-switch edges can absorb that component charge.

#### Proof

The range of a finite graph Laplacian is the orthogonal complement of its
component constants.  This proves (3.4) and (3.5).  The Moore--Penrose
solution (3.6) is the standard minimum-energy solution on that range.
Equation (3.2) shows that the orthogonal component is present in every
attempt using the prescribed `KRf`.  \(\square\)

For arbitrary `f`, the exact projected Dirichlet decomposition is

\[
 \boxed{
 \begin{aligned}
 \langle Kf,MKf\rangle
 ={}&\langle Kf,
      \Lambda\Lambda^\dagger MKf\rangle\\
 &+\langle Kf,QMKf\rangle.
 \end{aligned}}
\tag{3.7}
\]

If `M` is constant, with value `m_C`, on each component `C`, the second
term is the manifestly nonnegative invariant-mode energy

\[
 \boxed{
 \langle Kf,QMKf\rangle
 =\sum_Cm_C|C|\,\overline g_C^{,2},
 \qquad
 \overline g_C={1\over|C|}\sum_{a\in C}g_a.}
\tag{3.8}
\]

Thus private switches can control the within-fibre fluctuations while
leaving an entire between-fibre covariance untouched.  In the FIFO
application, a component fixes endpoint and exterior data; componentwise
balance is a new row and does not follow from global coordinate-orbit
balance.

Component balance is still not sufficient for the particular pristine
resource resolvent.  The strong pointwise condition needed to erase the
first term of (2.7) is

\[
 \boxed{MK=\Lambda KR.}
\tag{SL}
\]

`(SL)` implies (3.5), but also fixes the range component of the Poisson
solution.  By contrast, the already proved projected relation is only

\[
 K^*MK=K^*\Lambda KR.
\tag{3.9}
\]

The difference between `(SL)` and (3.9) is exactly `mathcal H`.

## 4. A four-candidate counterexample

The next example shows that projected resolvent cancellation, global
candidate centering, a connected switch graph, and a one-edge kill do not
give a favorable stopped boundary.

Take `H=R`, let `Gamma` be the unit-weight path

\[
 1-2-3-4,
\tag{4.1}
\]

put `M=I`, and define

\[
 Kt=t(1,1,-2,0)^T.
\tag{4.2}
\]

The candidate vector is globally centered.  Directly,

\[
 B=K^*K=6,
 \qquad
 L=K^*\Lambda K=13,
 \qquad
 R={6\over13}.
\tag{4.3}
\]

For `f=1`,

\[
 g=(1,1,-2,0),
 \qquad
 h={6\over13}(1,1,-2,0).
\tag{4.4}

The full bilinear switch energy is carried by the last two path edges and
equals `6`, as required by (1.9).  Now kill only candidate `4`, so
`U={1,2,3}`.  The killed covariance row has value

\[
 m_4g_4^2=0.
\tag{4.5}

Nevertheless the deleted switch edge `3-4` contributes

\[
 (g_3-g_4)(h_3-h_4)
 =(-2)\left(-{12\over13}\right)
 ={24\over13}>0.
\tag{4.6}

Indeed

\[
 \mathcal D_U(f)
 =6-3\cdot{18\over13}
 ={24\over13}.
\tag{4.7}

The intertwining defect is

\[
 \mathcal Hf
 =\left(1,-{5\over13},{4\over13},-{12\over13}\right)^T,
 \qquad K^*\mathcal H=0,
\tag{4.8}

but `mathcal H` is not zero.  Since `Gamma` is connected and
`sum_a g_a=0`, even the component-charge condition (3.4) holds.  Thus
component balance makes a candidate Poisson solution exist, but it does
not identify that solution with `KRf`.

This example refutes each of the following abstract implications:

1. projected pristine cancellation implies a nonpositive killed residue;
2. the negative killed covariance row pays the broken generator edge;
3. global candidate centering implies strong lumpability `(SL)`;
4. a one-occurrence switch makes the bilinear Bellman boundary automatic.

It does **not** refute a host-specific payment of (4.6) by the literal
`(ROc)`/`(FE3)` injection.  It proves that such a payment, or an additional
intertwining theorem, is logically necessary.

## 5. The corrected private-switch target

At one frozen stopped state, the exact unresolved quadratic form is not
the withdrawn scalar `(FSW)`.  It is (2.7).  Accordingly, a proof-safe
private-switch Bellman lemma must establish one of the following.

### Route A: strong killed lumpability

Construct a coefficient-faithful private-switch generator for which

\[
 MK=\Lambda KR
\tag{5.1}
\]

on every unpriced composite/marked face.  Then the only stopped term is
the cut flux in (2.7).  Its first-kill increment is the bilinear
one-occurrence edge in (2.11), which may then be injected, with its actual
future coefficient, into `(ROc)`/`(FE3)`.

### Route B: invariant-mode plus cut-flux domination

For the actual monotone live sets `U_i` and actual predictable vectors
`f_i`, prove directly that

\[
 \boxed{
 \begin{aligned}
 \mathbb E\sum_i {\beta_i\over X_i}
 \Bigg[
 &\langle P_{U_i}Kf_i,P_{U_i}\mathcal H_i f_i\rangle\\
 &+\sum_{\substack{a\in U_i,b\notin U_i\\a\sim b}}
 w_{ab}^{(i)}g_{i,a}(h_{i,a}-h_{i,b})
 \Bigg]_+
 =O(M/d^4),
 \end{aligned}}
\tag{KBG}
\]

after subtracting the already authenticated root, pair, slot, and marked
injections.  Here all density and future-fugacity factors must be the
actual ones; `(KBG)` is schematic only in their common prefactor.

The private one-occurrence theorem addresses the geometry of the second
line.  It says nothing by itself about the first line.  A natural division
of labor is therefore:

* private switches pay within-fibre cut flux;
* the joint root/pair potential pays the component-invariant part of
  `mathcal H`;
* a range-intertwining lemma pays the remaining part of `mathcal H`.

This three-way decomposition is exact, not heuristic.

## 6. Self-audit and scope

1. **Operator types.**  `R` is applied only to `f in H`.  The candidate
   functions are `Kf` and `KRf`.  No scalar candidate value is placed in an
   `R`-norm.
2. **Graph convention.**  `Lambda_U` is the induced-edge (Neumann)
   Laplacian.  Using the principal submatrix would add boundary degrees and
   change (2.7).
3. **Static scope.**  Equations (2.7) and (2.11) freeze `f`, `M`, `K`,
   `Lambda`, and `R`.  A stochastic Bellman proof must additionally include
   vector innovations, coefficient drift, changing future weights, and
   non-isotropic noise.
4. **Coefficient scope.**  The note does not assert that the private edge
   weights equal the composite future-fugacity weights.  That normalization
   is a separate host audit.
5. **Candidate components.**  The actual private-order graph fixes endpoint
   and exterior data and is highly disconnected.  Global orbit centering
   does not imply (3.4) component by component.
6. **Counterexample scope.**  Section 4 is an abstract operator
   counterexample, not a claim about reachability in the atomic FIFO host.
   It rules out a purely formal Schur-complement closure from the currently
   proved pullback identity.
7. **No final theorem claim.**  Neither `(KBG)` nor `(SL)` is proved for the
   FIFO host here.  Therefore this note does not establish `(JVAL)`, the
   bottom expectation bound, or `nu(k)=B(k)+O(1)`.

The smallest new host-specific question is now exact:

\[
 \boxed{
 \text{Does the private FIFO switch generator satisfy strong
 lumpability `(SL)` after the joint root/pair invariant modes are
 removed?}}
\]

If yes, the remaining boundary is genuinely one-occurrence and may be
priced by the existing first-hit ledgers.  If no, the surviving
`mathcal H` term is the precise extra potential which must be added to the
Bellman function.
