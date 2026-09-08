# Independent rank matchings: exact averaged Hall kernel and the all-cuts gap

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Outcome

In every macroblock \(B_j=A_j\mathbin{\dot\cup}C_j\), choose the
rank-\(k\) bijection

\[
 \pi_{j,k}:A_j\longrightarrow C_j
\]

independently and uniformly from all \(d!\) bijections.  The
rank-twisted owner partition remains exact for every realization.  No
part of the owner proof uses a relation between the matchings at
different ranks.

For the maximal exposed-edge graph, the random model has an exact
profile-compressed kernel.  If a lower target has half-counts

\[
 a=|T\cap A|,\qquad c=|T\cap C|,
\]

and a proposed source adds \(\alpha\) elements of \(A\) and \(\gamma\)
elements of \(C\), put

\[
 a'=a+\alpha,\qquad c'=c+\gamma,\qquad
 \ell=\alpha+\gamma.
\]

For one prescribed inclusion pair \(T\subset X\), the exact probability
that all added elements are exposed split endpoints in the rank-\((a'+c')\)
matching is

\[
 \boxed{
 P_d(a,c;\alpha,\gamma)
 ={(d-c')_\alpha(d-a')_\gamma\over(d)_\ell}.}         \tag{0.1}
\]

Consequently the expected number of compatible source extensions of
this half-increment type is

\[
 \boxed{
 K_d(a,c;\alpha,\gamma)
 =\binom{d-a}{\alpha}\binom{d-c}{\gamma}
   {(d-c-\gamma)_\alpha(d-a-\alpha)_\gamma
    \over(d)_{\alpha+\gamma}}.}                       \tag{0.2}
\]

For a global target profile
\(\tau=((a_j,c_j))_{j\le b}\), its exact expected compatible-source
degree is the coefficient

\[
 \boxed{
 \overline C_q(\tau)
 =[z^q]\prod_{j=1}^b
 \left(
 \sum_{\alpha,\gamma\ge0}
 K_d(a_j,c_j;\alpha,\gamma)z^{\alpha+\gamma}
 \right).}                                           \tag{0.3}
\]

Thus independent rank matchings replace the cyclic correlation
\(e_{t+\ell}(T)\) by a finite product kernel depending only on half-count
profiles.

There is genuine Gaussian smoothing.  At depth one the expected number
of compatible source extensions of a target is exactly

\[
 H_1(\tau)
 ={2\over d}\sum_j(d-a_j)(d-c_j).                     \tag{0.4}
\]

For a uniform rank-\((m-q)\) target with \(d\to\infty\),
\(d=O(\log m)\), and \(q=A\sqrt m\),

\[
 H_1(\tau)
 ={m\over2}+q+O_{\mathbb P}\left(\sqrt{m/d}\right).   \tag{0.5}
\]

The corresponding fluctuation in a depth-\(q\) exponential scale is

\[
 {q\over m}\sqrt{m/d}=O(d^{-1/2})=o(1).               \tag{0.6}
\]

This removes the order-one cyclic cross-correlation fluctuation from a
typical half-count profile.  It does not by itself prove Hall.  The
number of pairs of additions landing in the same macroblock is
\(\Theta(q^2/b)=\Theta(d)\); their without-replacement corrections
contribute at constant Gaussian order.  Formula (0.3), not the
depth-one approximation, is required to determine the limiting constant.

The averaged graph has an exact finite fractional-flow formulation in
Section 5.  A feasible solution with uniform slack would prove a
fractional injection in the permutation-averaged graph.  Bipartite
integrality would then give an injection in that averaged support graph.
It would not yet give an injection for one realized family of matchings:
one local permutation is reused by exponentially many raw
source--target pairs, and a realization is not symmetric inside a
half-count profile.  Profile cuts alone therefore do not exhaust its
Hall cuts.

No high-probability raw injection is claimed.  What is proved is the
exact random kernel, its typical first-order smoothing, and a precise
two-stage remaining theorem:

1. solve the profile-compressed fractional flow with Gaussian slack;
2. prove that one independent-permutation realization preserves every
   raw Hall cut, not merely the profile cuts.

Packet-axis selection and chronology are strictly later gates and are
not included in this maximal-graph statement.

## 1. Owner legality is deterministic

For each block \(j\) and local rank \(k\), fix any perfect matching
\(M_{j,k}\) between \(A_j\) and \(C_j\).  Status cells relative to
\(M_{j,k}\) partition the rank-\(k\) layer.  Cube moves preserve \(k\),
so they never change the matching used to define their cell.  Tensoring
over blocks and subdividing large product cubes therefore gives the same
exact owner tiling for every deterministic or random choice of the
\(M_{j,k}\).

Independence of the matchings is used only for the target-incidence
analysis below.

## 2. Exact probability for one inclusion pair

Fix one block and one inclusion \(T\subset X\).  Write

\[
\begin{aligned}
 a&=|T\cap A|,& c&=|T\cap C|,\\
 \alpha&=|(X\setminus T)\cap A|,&
 \gamma&=|(X\setminus T)\cap C|.
\end{aligned}
\]

The source half-counts are \(a'=a+\alpha\), \(c'=c+\gamma\), and its
rank-selected frame is a uniform bijection
\(\pi:A\to C\).

Every added \(A\)-element must be mapped into \(C\setminus X\), a set of
size \(d-c'\).  Every added \(C\)-element must have its preimage in
\(A\setminus X\), a set of size \(d-a'\).  These domain and image
requirements are disjoint.  Choose the images of the \(\alpha\) added
\(A\)-elements and the preimages of the \(\gamma\) added \(C\)-elements,
then complete the remaining bijection.  The number of acceptable
permutations is

\[
 (d-c')_\alpha(d-a')_\gamma(d-\alpha-\gamma)!.
\]

Division by \(d!\) proves (0.1).

There are

\[
 \binom{d-a}{\alpha}\binom{d-c}{\gamma}
\]

source supersets \(X\) with the prescribed increment counts.  Multiplying
by (0.1) proves (0.2).  Since the matchings at distinct block/rank pairs
are independent, multiplication over blocks and coefficient extraction
prove (0.3).

Equation (0.3) is an expectation of the number of distinct raw source
neighbors.  A pair \(T,X\) has a unique increment vector, so it is not
counted more than once.

## 3. Exact depth-one smoothing

At \(\ell=1\), either \((\alpha,\gamma)=(1,0)\) or \((0,1)\).
Formula (0.2) gives

\[
\begin{aligned}
 K_d(a,c;1,0)
 &={(d-a)(d-c)\over d},\\
 K_d(a,c;0,1)
 &={(d-c)(d-a)\over d}.
\end{aligned}
\]

Summing over blocks proves (0.4).

Ignore \(o(m)\) residual coordinates for notation.  Write

\[
 a_j={d\over2}+u_j,\qquad
 c_j={d\over2}+v_j.
\]

The target rank constraint is

\[
 \sum_j(u_j+v_j)=-q.
\]

Expanding (0.4) gives the exact identity

\[
 H_1(\tau)
 ={m\over2}+q+{2\over d}\sum_j u_jv_j.                \tag{3.1}
\]

Under the unconditioned Bernoulli law with density
\((m-q)/(2m)\), the two half-count deviations in one block are
independent up to their deterministic mean shift, and

\[
 \operatorname {Var}(u_jv_j)=O(d^2).
\]

There are \(b=m/d+O(1)\) blocks, so

\[
 \operatorname {Var}\left({2\over d}\sum_j u_jv_j\right)
 =O(m/d).                                             \tag{3.2}
\]

Conditioning on the total rank changes this estimate by at most a
constant factor; this follows equally from coefficient extraction in the
four-variable block generating function.  Chebyshev's inequality gives
(0.5), and (0.6) follows.

The same calculation for a fixed source profile gives its expected split
count

\[
 \overline S(\kappa)
 ={1\over d}\sum_j
 \bigl(a'_j(d-c'_j)+(d-a'_j)c'_j\bigr)
 ={m\over2}-{2\over d}\sum_j u'_jv'_j.                \tag{3.3}
\]

It has the same \(O(\sqrt{m/d})\) typical fluctuation.

## 4. Collision corrections cannot be discarded

If \(q\) additions were assigned independently among
\(b=m/d+O(1)\) blocks, the expected number of colliding pairs would be

\[
                         \binom q2{1\over b}
 =\left({A^2\over2}+o(1)\right)d.                     \tag{4.1}
\]

Thus only \(o(q)\) additions collide, but the number of collisions tends
to infinity.  A local without-replacement correction is typically
\(1+O(1/d)\); multiplying it over \(\Theta(d)\) collisions changes the
Gaussian limiting ratio by a nonvanishing constant.

It is therefore invalid to replace (0.3) by
\(\binom{H_1(\tau)}q\) or to treat the additions as independent.
The coefficient in (0.3) retains every collision multiplicity and every
rank-dependent matching reuse exactly.

## 5. Exact profile-compressed fractional flow

Let

\[
 \tau=((a_j,c_j))_{j\le b},
 \qquad
 \sum_j(a_j+c_j)=m-q
\]

be a target half-count profile.  Its number of raw targets is

\[
 w_T(\tau)=\prod_j\binom d{a_j}\binom d{c_j}.          \tag{5.1}
\]

A source profile is

\[
 \kappa=((a_j+\alpha_j,c_j+\gamma_j))_{j\le b},
 \qquad
 \sum_j(\alpha_j+\gamma_j)=q,
\]

and has weight

\[
 w_X(\kappa)=
 \prod_j\binom d{a_j+\alpha_j}
          \binom d{c_j+\gamma_j}.                     \tag{5.2}
\]

For compatible \(\tau,\kappa\), define the expected number of
\(\kappa\)-profile source neighbors of one fixed \(\tau\)-profile target
by

\[
 D_{\tau\kappa}
 =\prod_jK_d(a_j,c_j;\alpha_j,\gamma_j).              \tag{5.3}
\]

Double counting expected inclusion pairs gives the reverse degree

\[
 D'_{\kappa\tau}
 ={w_T(\tau)\over w_X(\kappa)}D_{\tau\kappa}.          \tag{5.4}
\]

A profile-symmetric fractional matching in the averaged graph is
equivalent to nonnegative edge weights
\(\theta_{\tau\kappa}\) satisfying

\[
\begin{aligned}
 \sum_\kappa D_{\tau\kappa}\theta_{\tau\kappa}
 &=1 &&(\tau\text{ a target profile}),\\
 \sum_\tau D'_{\kappa\tau}\theta_{\tau\kappa}
 &\le1 &&(\kappa\text{ a source profile}).
\end{aligned}                                         \tag{5.5}
\]

This is a finite transportation LP.  Its exact Hall dual says that
(5.5) is feasible if and only if, for every set \({\cal P}\) of target
profiles,

\[
 \sum_{\tau\in{\cal P}}w_T(\tau)
 \le
 \sum_{\kappa\in N({\cal P})}w_X(\kappa),             \tag{5.6}
\]

where \(N({\cal P})\) uses the positive entries of (5.3).

Equation (5.6) is only the support version.  For a robust rounding to one
random realization one needs a quantitative normalized expansion, for
example a solution of (5.5) with source loads at most \(1-\eta_A\) after
quarantining \(o(W)\) profiles, where \(\eta_A>0\) is independent of
\(m\).

The number of half-count profiles is

\[
 (d+1)^{2b}
 =\exp\left(O\left({m\log d\over d}\right)\right)
 =e^{o(m)}.                                           \tag{5.7}
\]

This compression is substantial, but it does not make the random
realization profile-symmetric.

## 6. A source-normalized fractional certificate

For one realized atlas, let

\[
 d(X)=\binom{S(X)}q
\]

be the degree of a source in the maximal graph.  Give every incident edge
\((T,X)\) weight \(1/d(X)\).  Every source of degree nonzero then has
total load one.  The load received by a target is

\[
 \boxed{
 L(T)=\sum_{X\sim T}{1\over\binom{S(X)}q}.}            \tag{6.1}
\]

If

\[
                         L(T)\ge1                     \tag{6.2}
\]

for every nonquarantined target, then these weights give a fractional
matching covering those targets.  Since the graph is bipartite, the
fractional matching polytope is integral, and an injective assignment of
the nonquarantined raw targets to distinct sources follows.

Thus (6.2) is a clean sufficient theorem to seek.  The exact expectation
of (6.1) is obtained by summing (0.1) with the conditional distribution
of the split counts in the same random permutations.  It does not
factor into (0.3), because the denominator and compatibility event share
the source matching.

The global mass identity is nevertheless exact for every realization:

\[
 \sum_TL(T)
 =\#\{X:S(X)\ge q\}
 =W-o(W).                                             \tag{6.3}
\]

Hence the average target load is
\((1+o(1))W/N_q=(1+o(1))e^{A^2}\).  Proving only this
average repeats the potential-capacity mistake.  What is needed is a
uniform or aggregate lower-tail bound for (6.1).

## 7. Why profile averaging does not yet imply high-probability Hall

The averaged kernel is invariant under coordinate permutations within
each half of each block.  A realized atlas is not.  One permutation
\(\pi_{j,k}\) is reused simultaneously by all sources having local rank
\(k\) in block \(j\), so it controls exponentially many raw incidence
edges.

Consequently:

* concentration of \(D_{\tau\kappa}\) for one fixed profile pair does
  not control an adversarial raw target subset;
* the worst Hall subset may depend on the realized permutations and need
  not be a union of half-count profiles; and
* a union bound over the \(e^{o(m)}\) profiles is not a union bound over
  the raw Hall cuts.

A valid positive theorem needs one of the following.

1. A symmetrization theorem showing that every minimum Hall cut of the
   realized graph can be replaced, with no larger neighborhood, by an
   approximately profile-symmetric cut.
2. A cut-norm concentration theorem for the permutation-generated
   incidence matrix, uniform over all raw target/source subsets.
3. A constructive fractional certificate proving (6.2) targetwise or
   with \(o(W)\) total deficit.

No such theorem is proved here.

## 8. Raw injection versus packet chronology

An injection in the maximal graph chooses, for every covered target,
one distinct middle source and one set of exposed source edges.  It does
not require those chosen edges to lie in the source's selected \(Q_r\)
packet, and it does not require them to form the source's consecutive
compiler window.

Therefore the implications are only

\[
\text{packet/chronological assignment}
\Longrightarrow
\text{selected-axis injection}
\Longrightarrow
\text{maximal raw injection}.                         \tag{8.1}
\]

The random-rank-matching problem in this note concerns only the weakest
rightmost statement.  A positive solution would remove the raw
source-capacity obstruction but would leave the selector-fibre grouping
and chronological-factor gates intact.

## 9. Certified boundary

Proved:

1. arbitrary independent rank matchings preserve the exact owner tiling;
2. the one-pair compatibility probability is (0.1);
3. the complete averaged target kernel is (0.3);
4. typical depth-one profile fluctuations are \(o(1)\) on the Gaussian
   exponential scale;
5. collision corrections have constant-order cumulative effect;
6. the averaged profile flow is exactly (5.5); and
7. the source-normalized load (6.1) is a sufficient fractional-injection
   certificate.

Not proved:

1. Gaussian-slack feasibility of (5.5);
2. a lower-tail theorem for (6.1);
3. preservation of all raw Hall cuts by one random atlas;
4. a raw target injection; or
5. packet/chronology grouping.

Independent rank matchings are therefore a plausible repair of the
cyclic-correlation defect, but the decisive theorem is an all-cuts
concentration or source-normalized load bound, not uniform randomness of
the local frames.
