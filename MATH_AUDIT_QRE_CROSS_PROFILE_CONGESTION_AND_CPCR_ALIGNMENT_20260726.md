# Audit of QRE cross-profile congestion and CPCR alignment

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Audited source:

`MATH_THEOREM_QRE_CROSS_PROFILE_CONGESTION_AND_CPCR_ALIGNMENT_20260726.md`.

## 0. Verdict

The exact discrete parts of the note pass:

1. Theorem 3.3 has the correct predecessor generating functions,
   stars-and-bars bounds, cap-loss estimate, entropy exponent, and typical
   owner visibility estimate.
2. The normalization and both inequalities in (5.8) are exact, under the
   natural definition of `def_c` as lower-quota matching deficit.
3. The floor dual (7.2), including the use of the `r` largest coordinates,
   is exact. Substitution of `lambda=-y` gives precisely the `r` smallest
   term in (7.3).
4. The collision identity (6.4), the deviation bound (7.8), and the forward
   implication from CPCR to aggregate raw target coverage are exact under
   the imported CPCR hypothesis `c_q>=1`.

Theorem 3.4 has the correct algebraic and probabilistic constants, but its
proof as presently written omits one uniform analytic lemma. In particular,
the displayed Gaussian variance `4A^2`, the normalization

\[
 {1\over N_q}\sum_T H_{\tau(T),2}(T)=e^{A^2+o(1)},
\]

and the consequent formal lower-tail constant are all correct. What is not
proved in the audited file is that the tilted coefficient asymptotics and
exponential-moment convergence hold uniformly on a specified collection of
ordered profiles of total target mass `1-o(1)`. Until that lemma is supplied,
(3.18) is conditional rather than unconditional.

There are also two exact corrections and two scope qualifications:

- Outcome item 3 compares the predecessor count with the wrong quantity.
  Relative to `(0.2)`, namely `K_q=(3/2)^q`, the gap is

  \[
  {P_{b,q}\over K_q}
   =\exp\!\left((A/2+o(1))\sqrt m\log m\right),
  \]

  not `exp(Theta_A(sqrt m))`. The latter gap is the comparison with
  `K_q^cert` in (3.13).
- For an exact integral statement, (3.13) should use
  `binom(floor(b/13),q)`, unless generalized real binomial coefficients are
  explicitly intended. This floor changes the logarithm by `o(1)` and does
  not change (3.13).
- “Raw QRE is strictly weaker than CPCR” is proved only as a separation of
  abstract certificates. The supplied load vector should be realized by a
  graph, as done in Section 5 below. It does not prove that the particular
  rank-twisted atlas satisfies QRE while failing CPCR.
- “No common-order, payload, seam, or within-packet term survives” is valid
  only as a statement about the additive energy identity after a legal state
  has been fixed. Those conditions remain constraints on which legal states
  exist.

Thus the note does not prove QRE, CPCR, MWB, or coefficient one, and it does
not claim to do so. Its unconditional boundary should list (3.18) only after
the uniform saddle lemma below has been inserted.

## 1. Theorem 3.3

Let an ordered owner profile have half counts `(a_j,c_j)`. A lower
predecessor is specified uniquely by nonnegative decrements
`alpha_j<=a_j`, `gamma_j<=c_j`, with total decrement `q`. Therefore

\[
 P_q^-(\kappa)
 =[z^q]\prod_j(1+\cdots+z^{a_j})(1+\cdots+z^{c_j}).
\]

Complementing each half gives the upper formula. On a central profile all
`2b` caps are at least one, so restricting every decrement to zero or one
and then deleting all caps gives

\[
 \binom{2b}{q}\le P_q^\epsilon(\kappa)
 \le\binom{2b+q-1}{q}.
\]

Since `q=A sqrt(m)+O(1)`, `b=m/d+O(1)`, and `d=Theta(log m)`,

\[
 \log\binom{2b+q-1}{q}
 =q\log {2eb\over q}+O(q^2/b+\log q)
 =\left({A\over2}+o(1)\right)\sqrt m\log m.
\]

For a visible owner, the same argument with singleton-side caps gives
(3.11). If all caps are at least `L=c_0d`, a union bound over the `2b`
coordinates bounds the bad weak compositions by

\[
 2b\left({q\over2b}\right)^L
 =\exp[-\Theta((\log m)^2)].
\]

The hypergeometric lower-tail quarantine has relative size
`O(be^{-c_1d})=o(1)` after choosing the constant in `d=C log m` large
enough. Hence (3.12) is correct.

Finally,

\[
 \log{\binom{2b+q-1}{q}\over
          \binom{\lfloor b/13\rfloor}{q}(7/6)^q}
 =q\log{12\over7\rho}+O(q^2/b+\log q),
 \qquad \rho={1\over13}.
\]

Thus (3.13) passes after the harmless floor repair. It must not be
identified with the much smaller within-profile factor `(3/2)^q`.

## 2. Theorem 3.4: verified constants and missing lemma

With at most two promotions in a block, the numbers of allocation labels
of local sizes zero, one, and two are `1,2,3`. This proves exactly

\[
 D_{b,q}=[z^q](1+2z+3z^2)^b.
\]

Its saddle satisfies

\[
 z_0={q\over2b}(1+o(1))
     ={Ad\over2\sqrt m}(1+o(1)).
\]

At the central point `a_j=c_j=d/2`, write

\[
 r(f)=(d-a-c+f)
 \left({1\over a-f+1}+{1\over c-f+1}\right).
\]

Then

\[
 r'(d/4)={16\over d}+O(d^{-2}),
 \qquad
 \operatorname {Var} f={d\over16}+O(1).
\]

Typical empirical second-moment control of the ordered half counts gives
the same two relations on average over the blocks. Since `b=m/d+O(1)`,

\[
 z_0^2\sum_j\operatorname {Var}r_j
 ={A^2d^2\over4m}\,{16m\over d^2}+o(1)
 =4A^2+o(1).
\]

Thus the fluctuation in `log H` is exactly `2AZ`, not `AZ` or
`sqrt(2)AZ`. Also

\[
 bz_0^3=O(d^2/\sqrt m)=o(1),
\]

and the centered quadratic term, multiplied by `z_0^2`, is
`O_P(d^{3/2}/sqrt(m))=o_P(1)`. These estimates and all constants in
(3.14)--(3.21) pass.

Double counting an overlap component gives

\[
 \sum_{T\in\tau}R_{\tau\kappa}(T)=E_{\tau\kappa}.
\]

Uniform visibility on the safe arcs gives
`E_{tau kappa}=(1-o(1))|kappa|`. Every retained central owner profile has
exactly `D_{b,q}` truncated predecessors, whence

\[
 \sum_TK_{\tau(T),2}(T)=(1-o(1))D_{b,q}W.
\]

Since

\[
 {W\over N_q}
 ={\binom{2m}{m}\over\binom{2m}{m-q}}
 =e^{q^2/m+o(1)}=e^{A^2+o(1)},
\]

(3.17) is exactly normalized.

If one has, uniformly on profiles of total mass `1-o(1)`,

\[
 \log H_{\tau,2}(T)=C_\tau+2AZ+o_{L^1(e^{\cdot})}(1),
 \qquad Z\Rightarrow N(0,1),
\]

then

\[
 M_\tau=e^{C_\tau+2A^2+o(1)}.
\]

Markov gives target-profile mass at least `(1/2-o(1))N_q` on which
`M_tau<=2e^{A^2+o(1)}`. Hence
`C_tau<=log 2-A^2+o(1)`, and on those profiles

\[
 \Pr\{H_{\tau,2}<1\}
 \ge \Phi\left({A^2-\log2\over2A}\right)-o(1).
\]

This verifies the deduction of (3.18) from the missing uniform lemma.

### Minimum missing analytic lemma

The proof needs the following statement, with all errors uniform.

> There is a class of safe ordered target profiles of total target mass
> `1-o(1)` such that, for every profile in the class, the independent block
> coefficient array in (3.19) satisfies a tilted local central limit theorem
> at coefficient `q`; after centering the Taylor remainder, its mean is
> absorbed into `C_tau`, its centered sum is `o_P(1)`, and
> `log H-C_tau` has moment generating functions converging to those of
> `N(0,4A^2)` uniformly for tilts in a fixed compact interval containing
> `1`.

The audited proof says only that a tilted local central limit theorem gives
(3.16). It neither defines the profile class nor proves its `1-o(1)` mass,
uniform local-CLT error, or uniform integrability at tilt one. The last item
is essential for the passage from (3.16) to the profile mean. Also `xi_j` in
(3.20) must be the *centered* Taylor remainder; its deterministic mean is
part of `C_tau`.

No wrong Gaussian constant was found. The issue is proof completeness and
uniformity, not the proposed asymptotic formula.

## 3. Exact retained normalization in (5.8)

Let `d_q(T)` be selected owner-degree. Every selected owner has exactly
`binom(R,q)` signed depth-`q` targets. Therefore

\[
 \sum_Td_q^\epsilon(T)=G\binom Rq,
 \qquad
 \sum_T\widetilde Z_q^\epsilon(T)=G,
 \qquad
 \sum_TZ_q^{G,\epsilon}(T)=N_q.
\]

Give every selected owner-target edge flow `1/binom(R,q)`. Each owner sends
one unit and target `T` receives `tilde Z(T)`. Discard flow received above
the cap `c_q`; the retained fractional lower-quota matching has size at
least

\[
 \sum_T\min\{c_q,\widetilde Z(T)\}.
\]

Bipartite integrality then gives, for

\[
 \operatorname {def}_{c_q}:=
 c_qN_q-\nu(\text{source capacity }1,\text{ target capacity }c_q),
\]

the first inequality

\[
 \operatorname {def}_{c_q}
 \le\sum_T(c_q-\widetilde Z(T))_+.
\]

Since `tilde Z=g_q Z^G` and `c_q<=g_q`, pointwise

\[
 (c_q-g_qz)_+\le g_q(1-z)_+,
\]

which is exactly the second inequality in (5.8). If
`c_q<=tilde Z(T)<=c_q+1` for every target, the same unit source flow lies in
the bipartite polytope with integral target bounds. Total unimodularity
gives an integral assignment with all loads in `{c_q,c_q+1}`. Thus (5.8)
and (5.9) pass exactly.

For formal completeness, Theorem 5.1 should quantify depths as
`1<=q<=H` and state `R->infinity`; otherwise the displayed
`O(W/sqrt R)=o(W)` conclusion is not literally implied by `H=o(R)` alone.

## 4. The exact floor dual

Let `A` be the convex hull of raw load vectors. It is the Minkowski sum

\[
 A=\sum_X\operatorname {conv}\{e_T:T\sim X\}.
\]

Hence

\[
 \min_{a\in A}\langle\lambda,a\rangle
 =\sum_X\min_{T\sim X}\lambda_T.
\]

For

\[
 B=\{c\mathbf1+u:0\le u_T\le1,\ \sum_Tu_T=r\},
\]

the support function is

\[
 \max_{b\in B}\langle\lambda,b\rangle
 =c\sum_T\lambda_T+\sum_{r\ {m largest}\ T}\lambda_T.
\]

Two compact convex sets intersect if and only if

\[
 \min_{a\in A}\langle\lambda,a\rangle
 \le\max_{b\in B}\langle\lambda,b\rangle
\]

for every real `lambda`: a strict separator in the opposite orientation is
converted to this one by replacing `lambda` with `-lambda`. This proves
(7.2). The associated source-target flow polytope has integral lower and
upper bounds and a totally unimodular incidence matrix, so nonempty
fractional intersection implies an integral assignment.

Putting `lambda=-y` turns the `r` largest entries of `-y` into minus the
`r` smallest entries of `y`; multiplying by `-1` proves (7.3). Thus neither
the inequality direction nor the largest/smallest choice needs correction.
Theorem 7.2 is the identical Minkowski-sum argument with one option simplex
per independent packet choice group, and also passes. Coupled slab trades
must indeed be treated as one joint group.

## 5. Exact CPCR implications and scope

For integer `L`, put

\[
 D_T=(c-L(T))_+,
 \qquad U_T=(L(T)-c-1)_+.
\]

If `L<=c-1`, the floor energy is `D_T(D_T+1)>=2D_T`; if
`L>=c+2`, it is `U_T(U_T+1)>=2U_T`; and it vanishes at `c,c+1`.
Thus (7.8) is exact. Under the authoritative CPCR packetization the owner
leave is exponentially small, so `G>N_1` and consequently `c_q>=1` for
every protected `q>=1`. Every missing target then contributes at least one
unit to `D`, proving aggregate missing mass `o(W)`. Selecting one occurrence
of every nonmissing target gives distinct owners because each packet image
is injective and distinct packets have disjoint owner sets.

The reverse separation can be made rigorous at the abstract graph level.
Take even `N`, `G=2N`, and `N/2` disjoint target stars with one private owner
and `N/2` disjoint target stars with three private owners. The graph has a
matching saturating every target, but every all-owner assignment has loads
one and three. With `c=2,r=0`, its floor energy is `N` and no balanced
assignment exists. This proves that unit Hall alone does not imply the raw
floor theorem. Giving each abstract packet only one option also separates
unit Hall from the grouped mean/covariance requirement.

This is an abstract separation of properties. It does not prove failure of
CPCR in the actual rank-twisted compiler whenever that compiler has QRE.
Accordingly, the safe wording is:

\[
 \text{CPCR}\Longrightarrow
 \text{aggregate near-floor raw loads}\Longrightarrow
 \text{unit raw coverage after an }o(W)\text{ deletion},
\]

where no converse follows from those abstract properties alone. The actual
reverse implications remain unproved, rather than disproved, for the
rank-twisted state space.

Finally, (6.4) proves that, *within any already legal compiler state*, the
only additive floor-energy term is excess cross-parent collision count.
It does not remove the common-option, chronology, payload, or seam
conditions from the definition of legality.

## 6. Corrected proved boundary

Unconditionally verified in the audited note:

1. Theorems 3.1 and 3.3, with the floor in `K_q^cert`;
2. the literal fixed-rank cut of Proposition 4.2;
3. Theorem 5.1 and the exact retained normalization (5.8), with the stated
   `q>=1`, `R->infinity` conventions;
4. the collision identity (6.4);
5. the raw and grouped mean floor duals (7.2) and (7.6); and
6. the forward CPCR coverage implication under the imported
   exponentially-small-leave hypothesis.

Conditionally verified:

1. Theorem 3.4 and (3.18), conditional only on the uniform typical-profile
   tilted coefficient lemma isolated in Section 2 above.

Not obtained:

1. a nonuniform weighted predecessor allocation;
2. raw rank-diverse QRE;
3. a legal common all-depth compiler realization;
4. CPCR; or
5. MWB and coefficient one.

