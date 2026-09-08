# Gate A: exact scalar Palm recursion and the survival-selection obstruction

**Date:** 2026-08-22  
**Status:** exact one-step reduction and literal isolated-edge obstruction;
no punctured covariance theorem is claimed

This note attacks the scalar functional in (6.4) directly. Its main
conclusion is an exact identity. Deleting targets can only decrease the
carrier test, but conditioning terminal Palm mass selects carriers according
to their exact-size survival probability. The scalar increases in one step
if and only if the resulting positive survival-selection covariance exceeds
the deterministic erosion. Thus there is no hidden sign argument left:
the covariance is the punctured-specific quantity that a positive theorem
must control.

## 1. Setup and the literal exact-size kernel

Let \(H_0\) be a finite simple hypergraph on a labelled target universe
\(V\), and put \(H(S)=H_0[S]\). Let \(\Omega\) and \(\Omega^+\) be two
prescribed exact-size slices. A current nonnegative (possibly
unnormalised) measure on \(\Omega\) is denoted by \(\nu\).

In \(H(S)\), mark every edge independently with probability \(p(S)\), accept
the isolated marked edges in the conflict graph, and delete all targets in
the accepted edges. Restrict the transition to \(S'\in\Omega^+\), without
normalising its rows, and call the resulting subkernel \(P\). This is global
exact-size conditioning: the final Palm quotient below performs the only
normalisation.

For complete explicitness, if \(G_S\) is the conflict graph of \(H(S)\),
\(D=S\setminus S'\), and, for a graph \(J\),

\[
 \zeta_p(J)=\Pr(\text{independent Bernoulli-}p\text{ marks on }V(J)
 \text{ have no isolated marked vertex}),
\]

then

\[
 P(S,S')={\bf1}_{\{S'\subseteq S\}}W_{p(S),S}(D),           \tag{1.1}
\]

where

\[
 W_{p,S}(D)=
 \sum_{\substack{A\subseteq E(H(S))\text{ independent in }G_S\\
                  \bigcup_{F\in A}F=D}}
 p^{|A|}(1-p)^{|N_{G_S}(A)|}
 \zeta_p\!\left(G_S[E(H(S))\setminus N_{G_S}[A]]\right).    \tag{1.2}
\]

Thus every exact-size and conditional-environment weight is present in
\(P\); no independent-thinning replacement is made.

Fix a prescribed root set \(R_\star\subseteq V\).  An ordered rooted
twelve-carrier is \(\gamma=(v;F_1,\ldots,F_{12})\), where
\(v\in R_\star\) and the \(F_i\) are distinct edges through \(v\). Write
\(\gamma\preceq S\) when all of its targets survive, and set

\[
 t(S)=\sum_{v\in R_\star}(d_S(v))_{12}.                       \tag{1.3}
\]

For real \(c\ge11\), define

\[
 \varphi_c(d)=
 \begin{cases}
 (d-c)_+^{12}/(d)_{12},&d\ge12,\\
 0,&d<12,
 \end{cases}
 \qquad
 F_c(S)=\sum_{v\in R_\star}(d_S(v)-c)_+^{12}.                 \tag{1.4}
\]

The current Palm law and scalar are

\[
 \widehat\nu(S,\gamma)=
 {\nu(S){\bf1}_{\{\gamma\preceq S\}}\over\nu(t)},
 \qquad
 A_c(\nu)={\nu(F_c)\over\nu(t)}
          =\mathbb E_{\widehat\nu}\varphi_c(d_S(v)).         \tag{1.5}
\]

Multiplying \(\nu\) by a constant changes neither object.

## 2. Exact one-step recursion

For a current carrier state \(x=(S,\gamma)\), define its literal
exact-size survival submass

\[
 a(x)=\sum_{S'\in\Omega^+}P(S,S')
                    {\bf1}_{\{\gamma\preceq S'\}},            \tag{2.1}
\]

and its scalar erosion

\[
 e_c(x)=\sum_{S'\in\Omega^+}P(S,S')
 {\bf1}_{\{\gamma\preceq S'\}}
 \{\varphi_c(d_S(v))-\varphi_c(d_{S'}(v))\}.                 \tag{2.2}
\]

By (1.1), these can equivalently be written as sums over deletion sets:

\[
 a(S,\gamma)=\sum_{\substack{D\subseteq S:\ S\setminus D\in\Omega^+\\
                              D\cap V(\gamma)=\varnothing}}
 W_{p(S),S}(D),                                               \tag{2.3}
\]

\[
 e_c(S,\gamma)=\sum_{\substack{D\subseteq S:\ S\setminus D\in\Omega^+\\
                              D\cap V(\gamma)=\varnothing}}
 W_{p(S),S}(D)
 \{\varphi_c(d_S(v))-\varphi_c(d_{S\setminus D}(v))\}.      \tag{2.4}
\]

### Theorem 2.1 (sharp scalar Palm recursion)

Assume \(\nu(t)>0\) and \((\nu P)(t)>0\). Then

\[
 \boxed{
 A_c(\nu P)
 ={\mathbb E_{\widehat\nu}
       [a\,\varphi_c(d_S(v))-e_c]
     \over\mathbb E_{\widehat\nu}a}.}                       \tag{2.5}
\]

Equivalently,

\[
 \boxed{
 A_c(\nu P)-A_c(\nu)
 ={\operatorname {Cov}_{\widehat\nu}
          (a,\varphi_c(d_S(v)))-\mathbb E_{\widehat\nu}e_c
    \over\mathbb E_{\widehat\nu}a}.}                       \tag{2.6}
\]

In particular, one-step scalar contraction is equivalent to the single
inequality

\[
 \boxed{
 \operatorname {Cov}_{\widehat\nu}
          (a,\varphi_c(d_S(v)))
 \le \mathbb E_{\widehat\nu}e_c.}                            \tag{2.7}
\]

#### Proof

Every terminal carrier already existed at the current state, with the same
label. Consequently

\[
 {(\nu P)(t)\over\nu(t)}
 =\mathbb E_{\widehat\nu}a,                                  \tag{2.8}
\]

while summing the terminal test over all terminal carriers gives

\[
 {(\nu P)(F_c)\over\nu(t)}
 =\mathbb E_{\widehat\nu}
   \sum_{S'}P(S,S'){\bf1}_{\{\gamma\preceq S'\}}
                    \varphi_c(d_{S'}(v))
 =\mathbb E_{\widehat\nu}[a\varphi_c-e_c].                  \tag{2.9}
\]

Here a root of terminal degree \(d\ge12\) has \((d)_{12}\) ordered
carriers, whose total test is
\((d)_{12}\varphi_c(d)=(d-c)_+^{12}\); when \(d<12\), both quantities
are zero because \(c\ge11\).

Dividing (2.9) by (2.8) proves (2.5). Subtracting
\(\mathbb E_{\widehat\nu}\varphi_c\) and centering \(a\) proves
(2.6), hence (2.7). Notice that the total mass \((\nu P)(1)\) of the
exact-size event cancels; row-normalising \(P\) would give different
survival and erosion functions and a different history law. \(\square\)

### Lemma 2.2 (erosion is always favourable)

For \(c\ge11\), the function \(d\mapsto\varphi_c(d)\) is nondecreasing on
the nonnegative integers. Hence \(e_c(x)\ge0\) for every \(x\).

#### Proof

Only \(d>c\) needs checking. There

\[
 {\varphi_c(d+1)\over\varphi_c(d)}
 =\left({d+1-c\over d-c}\right)^{12}{d-11\over d+1}.
\]

Bernoulli's inequality and \(c\ge11\) give

\[
 \left(1+{1\over d-c}\right)^{12}
 \ge1+{12\over d-c}
 \ge1+{12\over d-11}={d+1\over d-11}.
\]

Induced target deletion never increases \(d_S(v)\), proving the second
claim term by term in (2.2). \(\square\)

Thus the covariance in (2.6) is the only sign-indefinite term. A clean
sufficient condition is that

\[
 d\longmapsto
 \mathbb E_{\widehat\nu}[a\mid d_S(v)=d]                       \tag{2.10}
\]

be nonincreasing. The rearrangement identity with two independent copies
then makes the covariance in (2.7) nonpositive.  Indeed, if
\(D=d_S(v)\), \(f(D)=\mathbb E[a\mid D]\), and \(D'\) is an independent
copy, then
\[
 \operatorname {Cov}(a,\varphi_c(D))
 ={1\over2}\mathbb E[(f(D)-f(D'))
                 (\varphi_c(D)-\varphi_c(D'))]\le0.          \tag{2.11}
\]
This condition is sufficient, not asserted for punctured residuals.

## 3. The exact relative-to-slice recursion

Let \(\lambda\) be the uniform law on the current exact slice.  More
explicitly, the target universe may be partitioned into fixed shores,
\(\Omega\) and \(\Omega^+\) prescribe respectively \(n_\sigma\) and
\(n^+_\sigma\le n_\sigma\) targets on every shore, and

\[
 U(S,S')={\mathbf1_{\{S'\subseteq S\}}\over C},\qquad
 C=\prod_\sigma {n_\sigma\choose n^+_\sigma}.                 \tag{3.0}
\]

Thus every row of \(U\) has mass one and double counting nested pairs
shows that \(\lambda U\) is the uniform law on \(\Omega^+\). Define
\(a^0,e_c^0\) from (2.1)--(2.2) with \(U\) in place of \(P\), and put

\[
 B=A_c(\lambda),\qquad B^+=A_c(\lambda U).
\]

When \(A=A_c(\nu)\), \(B\), \(A_c(\nu P)\), and \(B^+\) are positive, set

\[
 \Delta={\operatorname {Cov}_{\widehat\nu}(a,\varphi_c)
                    -\mathbb E_{\widehat\nu}e_c
                  \over\mathbb E_{\widehat\nu}a},
\quad
 \Delta^0={\operatorname {Cov}_{\widehat\lambda}(a^0,\varphi_c)
                    -\mathbb E_{\widehat\lambda}e_c^0
                  \over\mathbb E_{\widehat\lambda}a^0}.      \tag{3.1}
\]

Theorem 2.1 applied twice gives the exact comparison recursion

\[
 \boxed{
 {A_c(\nu P)/A_c(\lambda U)\over A_c(\nu)/A_c(\lambda)}
 ={1+\Delta/A\over1+\Delta^0/B}.}                            \tag{3.2}
\]

Therefore absolute contraction \(A_c(\nu P)\le A_c(\nu)\) is not by
itself Gate A: the reference tail contracts too. Relative one-step
contraction is equivalent to

\[
                         {\Delta\over A}\le{\Delta^0\over B}. \tag{3.3}
\]

For a fixed \(c\), iterating (3.2) through checkpoints at which the four
successive scalars are positive gives

\[
 \log {A_c(\nu_J)\over A_c(\lambda_J)}
 =\log {A_c(\nu_0)\over A_c(\lambda_0)}
 +\sum_{j<J}\left[
   \log\left(1+{\Delta_j\over A_j}\right)
  -\log\left(1+{\Delta_j^0\over B_j}\right)\right].          \tag{3.4}
\]

If a uniform-slice tail is zero, then nonnegativity and the full support of
the uniform slice make \(F_c\) identically zero on that slice, so every
actual measure supported there has the same zero tail; the comparison is
then automatic.  If the initial laws agree, the exact minimal scalar input
at a positive-tail horizon is an upper bound on the *total* sum in (3.4).
Bounding the sum of the positive parts of its summands is a convenient
stronger sufficient condition.  For a horizon-dependent terminal threshold,
one fixes that threshold \(c\) while telescoping backwards to that horizon;
no single telescope with a changing \(c\) is asserted.  In this precise
sense (3.4) is the scalar replacement for full terminal \(L^\infty\)
control.

## 4. What punctured symmetry proves

In the directed punctured catalogue every accepted row deletes exactly
\(2r\) targets on each shore, and accepted rows are target-disjoint. Thus
restricting the next shore sizes to a decrement \(2rq\) is exactly the event
that \(q\) rows are accepted. Equations (2.3)--(2.6) therefore apply
literally, with \(D\) the union of those \(q\) rows. In particular, the
quantity still needing control is the exact-size carrier-survival/high-tail
covariance

\[
 \boxed{
 \mathcal C_{c}(\nu,P)=
 \operatorname {Cov}_{\widehat\nu}
 \left(
  \sum_{\substack{D\subseteq S:\ S\setminus D\in\Omega^+\\
                         D\cap V(\gamma)=\varnothing}}
       W_{p(S),S}(D),
  \varphi_c(d_S(v))
 \right).}                                                       \tag{4.1}
\]

Assume here, as in the punctured process, that the exact-size restriction,
the marking rule \(p(S)\), and any stopping indicator are equivariant under
the relevant coordinate relabellings.  Coordinate relabelling then makes
both arguments of this covariance constant on state-carrier orbits. It does
not impose an order on the different orbits and hence supplies no sign for
(4.1). At the deterministic complete initial catalogue, take \(R_\star\)
to be either one chosen root shore.  All its roots have the same degree. The second
argument is then constant, so \(\mathcal C_c=0\) and (2.6) gives absolute
one-step contraction for that shore-specific scalar. After a nontrivial
residual is produced, the invariant law can have many state-carrier orbits;
the same argument no longer applies. No punctured counterexample to (2.7)
is asserted here, but neither (2.7) nor the relative inequality (3.3)
follows from equivariance alone.

For the coefficient-one program, the surviving positive input can be
stated without a full likelihood ratio.  Starting from the uniform initial
slice, prove for every relevant fixed terminal \(c\) that the total
normalised log-drift excess in (3.4) is at most
\((\kappa+o(1))\log r\), uniformly over the stopped horizons, with the
already required \(\kappa<2-20\alpha\).  Since the initial ratio is one,
the exact scalar statement is

\[
 \boxed{
 \sup_{J\le\tau_{\rm stop}}
 \sum_{j<J}\left[
   \log\left(1+{\Delta_{j,c}\over A_{j,c}}\right)
  -\log\left(1+{\Delta^0_{j,c}\over B_{j,c}}\right)
 \right]
 \le(\kappa+o(1))\log r.}                                    \tag{4.2}
\]

Here a terminal-horizon choice of \(c\) is held fixed throughout its own
sum.  A stronger sufficient target is the same bound for the sum of the
positive parts of the summands.  Formula (2.6) expresses each actual drift
exactly as survival-selection covariance minus favourable erosion; the
reference term in (4.2) must still be subtracted with its displayed
normalisation.  This is weaker and more targeted than terminal Palm
\(L^\infty\) domination.

## 5. Literal isolated-edge counterexample to monotonicity alone

The covariance obstruction is real even for an exact-size isolated-edge
bite. It is not claimed to be a punctured residual.

### Proposition 5.1

Fix \(M\ge1\) and let

\[
 H=K_{14}\mathbin{\dot\cup}M K_{12,12}. \tag{5.1}
\]

Take \(R_\star=V(H)\).  Regard this graph as a 2-uniform hypergraph with
one shore. Start from its
full vertex set, mark graph edges independently with probability \(p\),
accept isolated marked edges, and restrict the next size to \(N-2\). For
all sufficiently small \(p>0\),

\[
                              A_{12}(\nu P)>A_{12}(\nu).        \tag{5.2}
\]

Thus pointwise monotonicity of \(\varphi_c\) under deletion does not imply
scalar Palm contraction.

#### Proof

Exact next size \(N-2\) is precisely the event that the accepted set is a
singleton. Let \(Q_H(p)\) be the subprobability that this singleton lies in
the \(K_{14}\), and \(Q_L(p)\) the corresponding subprobability for one
fixed \(K_{12,12}\) component. For any fixed edge, the probability that it
is the unique accepted edge is \(p+O(p^2)\): the outcome in which it alone
is marked contributes \(p+O(p^2)\), and every other contributing marking
pattern has at least two marks. Therefore

\[
 Q_H(p)=91p+O(p^2),\qquad Q_L(p)=144p+O(p^2),                  \tag{5.3}
\]

so \(Q_L(p)>Q_H(p)\) for all sufficiently small positive \(p\).

Put

\[
 T_H=14(13)_{12},\qquad T_L=24(12)_{12}.                       \tag{5.4}
\]

Only the fourteen degree-thirteen vertices contribute to \(F_{12}\), each
by one. Hence initially

\[
                         A_{12}(\nu)={14\over T_H+MT_L}.        \tag{5.5}
\]

If the accepted edge lies in \(K_{14}\), deletion leaves \(K_{12}\), whose
degrees are eleven; the terminal numerator is zero and the terminal carrier
mass is \(MT_L\). If it lies in one low component, that component becomes
\(K_{11,11}\), while \(K_{14}\) is unchanged; the terminal numerator is
fourteen and the carrier mass is \(T_H+(M-1)T_L\). Consequently

\[
 A_{12}(\nu P)=
 {14M Q_L(p)\over
  M Q_L(p)[T_H+(M-1)T_L]+Q_H(p)MT_L}.                         \tag{5.6}
\]

Cross-multiplication of (5.5)--(5.6) shows that (5.2) is equivalent exactly
to \(Q_L(p)>Q_H(p)\), which follows from (5.3). All conditioning is through
the single global subkernel \(P\); no componentwise or rowwise
renormalisation has been used. \(\square\)

The covariance mechanism can also be read off exactly.  A twelve-carrier
rooted in \(K_{14}\) uses thirteen of that component's fourteen vertices,
so every edge of that component hits it.  A twelve-carrier rooted in a
\(K_{12,12}\) uses its root and the entire opposite part, so again every
edge of its own component hits it.  Consequently the survival submasses of
a high and a low carrier are respectively
\[
 a_H=M Q_L(p),\qquad a_L=Q_H(p)+(M-1)Q_L(p),                  \tag{5.7}
\]
and every carrier that survives has unchanged root degree.  Thus
\(e_{12}=0\) identically on the current Palm space, while
\(a_H-a_L=Q_L-Q_H>0\) and
\(\varphi_{12}(13)>\varphi_{12}(12)=0\).  The increase is precisely a
strictly positive survival-selection covariance: exact-size conditioning
selects away more degree-twelve Palm mass than degree-thirteen Palm mass.
This is the minimal mechanism that any punctured-specific positive
covariance theorem must exclude.

## 6. Certification boundary

The identities (2.5), (2.6), (3.2), and (3.4), the monotonicity lemma, and
Proposition 5.1 are unconditional finite statements for the globally
restricted subkernel specified above.  They do **not** prove (4.2) for the
punctured catalogue.  In particular, the remaining punctured-specific
mathematical input is a uniform upper bound on the normalised cumulative
survival-selection drift in (4.2), or any stronger condition implying it.
Equivariance and pointwise erosion alone do not provide that bound.

Even after (4.2), converting the Palm scalar back to the raw stopped tail
requires the separate carrier-mass comparison, and the coefficient-one
descent still uses its finite-bite and predictable-to-realised-centre error
transfers.  None of those auxiliary transfers is reproved or claimed in
this note.  Finally, row-normalising \(P(S,\cdot)\) would define a different
history law; the recursion remains algebraically valid for that different
kernel, but it would not certify the globally exact-history law analysed
here.
