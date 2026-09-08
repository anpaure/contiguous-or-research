# Gate A: the complete punctured two-star has no universal favorable sign

**Date:** 2026-08-22  
**Status:** exact finite punctured counterexample; it rules out a sign-only
closure of the $s=2$ term but does not refute an asymptotic $o(z)$ bound

## 1. Statement

Use the complete directed-punctured catalogue at $r=2$, so the ground set
has size five.  Retain middle targets with probability

\[
 p_M={9\over10}
\]

and lower targets with probability

\[
 p_L={1\over10}.
\]

Fix a middle root $v$.  Its full catalogue star has degree $D=48$.
Let $K(F,H)=K_2^\circ(F,H)$ be the signed two-star kernel of
Appendix G.15, let \(\Pi_{12}\) be the ordered-pair factorial Palm law,
and let \(\Pi_{47}\) be the ordered-pair law induced by the cutoff tilt

\[
                       f_{47}(d)=(d-47)_+^{12}.
\]

Then

\[
\boxed{
 \Delta_{2,47}:=
 \mathbb E_{\Pi_{12}}K-\mathbb E_{\Pi_{47}}K
 ={94888059014964404224\over2510611211042938575}>0.}
                                                               \tag{1.1}
\]

Equivalently, by the exact likelihood identity

\[
 \Delta_{2,47}
 =-{\operatorname {Cov}_{\Pi_{12}}(K,S)\over
          \mathbb E_{\Pi_{12}}S},
\]

the global covariance \(\operatorname {Cov}_{\Pi_{12}}(K,S)\) is
strictly negative.  This is not merely an adverse overlap subcell: it is
the complete global $s=2$ comparison after all position and overlap-cell
cancellation.

The discrepancy is already macroscopic at the natural normalization.  A
punctured row has four targets on each shore, hence

\[
 q_0=p_M^4p_L^4,
 \qquad z=48p_M^3p_L^4,
 \qquad {q_0\over z}={p_M\over48}.
\]

Therefore

\[
 \boxed{
 {q_0\Delta_{2,47}\over z}
 ={2965251844217637632\over4184352018404897625}
 =0.7086525777\ldots>0.}                                \tag{1.2}
\]

## 2. Exact proof

There are $5!=120$ catalogue rows and fifteen tagged targets.  For a
pair of distinct root rows $F,H$, put

\[
 A=(G\cap F)-\{v\},\qquad B=(G\cap H)-\{v\},
 \qquad w(T)=\prod_{u\in T}p_u^{-1}.
\]

Summing over all 120 further rows gives

\[
 K(F,H)=\sum_G k_G(F,H),
\]

where the summand is zero if $A=\varnothing$ or $B=\varnothing$, and
otherwise

\[
 k_G(F,H)=
 \begin{cases}
 p_v^{-1}\{w(A\cup B)-w(A)-w(B)+1\},&v\in G,\\[2pt]
 w(A\cup B)-w(A)-w(B),&v\notin G.
 \end{cases}                                             \tag{2.1}
\]

For either degree weight $g$, exact extension counting assigns the
unordered pair $\{F,H\}$ the unnormalized mass

\[
 W_g(F,H)=
 \mathbb E[\mathbf1_{\{F,H\text{ live}\}}g(d_v)].       \tag{2.2}
\]

The unordered convention is harmless because $K$ and both weights are
symmetric.  For the factorial law use

\[
                         g_{12}(d)=(d-2)_{10};            \tag{2.3}
\]

for the cutoff law use

\[
 g_{47}(d)=
 \begin{cases}(d-47)_+^{12}/(d)_2,&d\ge2,\\0,&d<2.
 \end{cases}                                             \tag{2.4}
\]

Since $d_v\le48$, (2.4) is nonzero only at $d_v=48$.  Conditional on
that state every root pair is live, so \(\Pi_{47}\) is exactly the uniform
law on the $48\cdot47$ ordered pairs.  Direct rational summation of
(2.1)--(2.4) gives

\[
 \mathbb E_{\Pi_{12}}K
 ={27541902730054743803792\over53417259809424225},        \tag{2.5}
\]

\[
 \mathbb E_{\Pi_{47}}K
 ={158982160240\over308367}.                             \tag{2.6}
\]

Subtracting (2.6) from (2.5) gives (1.1), and multiplication by
\(p_M/48=3/160\) gives (1.2).  All sums are finite, and no floating-point
comparison enters the sign.

The standalone checker

`scratch/verify_gate_a_punctured_two_star_global_sign_no_go_20260822.py`

constructs the complete catalogue from permutations, enumerates all
\(2^{15}\) target states, evaluates every quantity as a
`fractions.Fraction`, and asserts (1.1), (1.2), (2.5), and (2.6).

## 3. Consequence for the live gate

This counterexample rules out the proposed shortcut

\[
 \operatorname {Cov}_{\Pi_{12}}(K,S)\ge0
 \quad\hbox{for every complete punctured catalogue and cutoff}. \tag{3.1}
\]

Thus neither product Harris association for a fixed carrier nor the
global punctured symmetries can close the two-star term by sign alone.
The live asymptotic target remains the weaker statement

\[
 q_0\left[
 \mathbb E_{\lambda_{12}}\overline K_2-
 \mathbb E_{\lambda_c}\overline K_2
 \right]_+=o(z),                                       \tag{3.2}
\]

or, more economically, the corresponding bound only after the signed sum
over $2\le s\le12$.  The witness is at fixed $r=2$, so it does **not**
disprove (3.2) as $r\to\infty$.  It does show that any proof of (3.2)
must obtain quantitative boundary decay or cancellation with the higher
connected kernels; a universal favorable-sign lemma is false.

Accordingly, this result changes only the route ledger.  It removes the
candidate lemma “the complete punctured $s=2$ covariance is always
favorable.”  It leaves unchanged the two valid Gate-A targets: prove the
positive part in (3.2) is $o(z)$ uniformly in the asymptotic density
range, or prove that bound only for the full signed combination

\[
 \sum_{s=2}^{12}{12\choose s}
 \left(\mathbb E_{\lambda_{12}}\overline K_s-
       \mathbb E_{\lambda_c}\overline K_s\right).
\]

No stopped-law, exact-slice, realized-center, or purge-transfer claim is
made here.
