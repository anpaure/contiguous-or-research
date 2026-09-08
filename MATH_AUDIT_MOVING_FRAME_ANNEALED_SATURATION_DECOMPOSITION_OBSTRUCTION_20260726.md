# Moving-frame annealed saturation does not decompose into target coverage

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Proposition 7.1 of
MATH_THEOREM_WEIGHTED_QUOTIENT_LIFT_GAUSSIAN_OBSTRUCTION_20260726.md
proves exact orbit flattening of each one-point source/target ratio.  With
normalized shared-source capacities, it gives an annealed pointwise score
larger than one.

This has no deterministic missing-target consequence beyond weighted
averaging.  Even under the strictly stronger assumption that the orbit
flow has already been lifted to a distribution on globally legal
packet/compiler states satisfying

\[
                         \mathbb E L(T)\ge1
 \quad\text{for every target }T,                   \tag{0.1}
\]

the expected number of holes can be linear.

There is an explicit infinite multiple-choice packet counterexample.  For
every fixed \(r\ge2\), it has \(r\) packets with two whole-packet options
each, injective image sets of size \(s=2^R\), and exact shared owner
capacity.  Every target has annealed load \(r/2\), yet every integral
state misses exactly a \(2^{-r}\) fraction of targets.  Tensoring gives
\(\Omega(W)\) holes in every state.  Thus arbitrary fixed annealed slack
does not repair the implication.

Bipartite matching integrality and Birkhoff decomposition do not apply:
they permit source-target incidences to be selected independently, while
all incidences in one packet option are bundled.  The bundled cover matrix
has a fractional vertex and no integral cover already for two packets and
four target classes.

The strongest valid deterministic consequence is only this:

> For each fixed nonnegative target weight vector \(y\), some legal frame
> state has weighted total incidence score at least its annealed average.

The maximizing state may depend on \(y\).  This is not one state covering
all targets.

## 1. Shared-capacity formulation

Let \(\mathfrak P\) be the packet family.  Packet \(P\) has legal options
\(\Omega_P\), each fixing one physical frame and one common compiler
chronology for all its occurrences.  Frame choices may be coupled; let

\[
                         \mathcal S
 \subseteq\prod_{P\in\mathfrak P}\Omega_P           \tag{1.1}
\]

be the globally legal integral states.  A state \(\xi\) chooses one option
\(\omega_P(\xi)\) per packet, with injective target image

\[
                         I_{P,\xi}\subseteq\mathcal T,
 \qquad |I_{P,\xi}|=|P|.                            \tag{1.2}
\]

Its literal load is

\[
                         L_\xi(T)
 =\sum_P\mathbf1_{\{T\in I_{P,\xi}\}}.              \tag{1.3}
\]

A legal randomized state is

\[
                         \pi_\xi\ge0,\qquad
                         \sum_{\xi\in\mathcal S}\pi_\xi=1.       \tag{1.4}
\]

Its packet-option marginals satisfy

\[
 x_{P,\omega}
 =\sum_{\xi:\omega_P(\xi)=\omega}\pi_\xi,
 \qquad \sum_\omega x_{P,\omega}=1.                \tag{1.5}
\]

Not every list of marginals comes from a distribution on \(\mathcal S\).
The expected load and expected holes are

\[
 \overline L(T)=\sum_\xi\pi_\xi L_\xi(T),           \tag{1.6}
\]

\[
 \mathbb E_\pi{\cal H}
 =\sum_T\Pr_\pi[L_\xi(T)=0].                        \tag{1.7}
\]

No linear identity recovers (1.7) from (1.6).

At quotient level, if global frame \(g\) is sampled with probability
\(p_g\), the exact source time-sharing constraints are

\[
 p_g\ge0,\qquad\sum_gp_g=1,\qquad
 \sum_\tau c_{\tau\kappa g}\le p_g
 \quad(\kappa,g).                                  \tag{1.8}
\]

Giving every \(g\) a separate unit source copy is illegal.  Proposition
7.1 controls the annealed score

\[
 \sum_{\kappa,g}c_{\tau\kappa g}R_{\tau\kappa}^{g}(T),           \tag{1.9}
\]

not the configuration distribution (1.4) or hole probabilities (1.7).
The counterexample below grants those missing lifts and still refutes the
inference.

## 2. Strongest direct averaging consequence

Assume, more strongly than Proposition 7.1, that a legal distribution
satisfies \(\overline L(T)\ge1\) for all \(T\).  For fixed \(y_T\ge0\),

\[
 \mathbb E_\pi\sum_Ty_TL_\xi(T)
 =\sum_Ty_T\overline L(T)\ge\sum_Ty_T.              \tag{2.1}
\]

Hence some state \(\xi_y\) has weighted score at least \(\sum_Ty_T\).
The state depends on \(y\).  Simultaneous validity for all \(y\ge0\)
would be the desired pointwise coverage and does not follow.

For \(y\equiv1\), the weighted score is the fixed total occurrence mass,
so the conclusion is usually tautological.

If \(L_\xi(T)\le D_T\), one only gets

\[
 \Pr[L_\xi(T)>0]\ge{\overline L(T)\over D_T},        \tag{2.2}
\]

which permits constant hole probability whenever \(D_T>1\).

## 3. Infinite bundled-option obstruction

Fix \(r\ge2\), let \(s=2^R\) with \(r-1\le R\), and put

\[
                         \ell={s\over2^{r-1}}.       \tag{3.1}
\]

There are \(r\) packets \(P_1,\ldots,P_r\), each with options
\(b\in\{0,1\}\).  For every word
\(a\in\{0,1\}^r\), create a disjoint target block

\[
                         \mathcal T_a,\qquad
                         |\mathcal T_a|=\ell.        \tag{3.2}
\]

Define

\[
                         I_{i,b}
 =\mathop{\dot\bigcup}_{a:a_i\ne b}\mathcal T_a.    \tag{3.3}
\]

Exactly half the words satisfy \(a_i\ne b\), so

\[
                         |I_{i,b}|=2^{r-1}\ell=s.   \tag{3.4}
\]

Thus every option is an injective image of the correct packet size, and
one option—not two owner copies—is selected per packet.

### Theorem 3.1

Under independent uniform options,

\[
                         \mathbb E L(T)={r\over2}
 \quad\text{for every }T.                          \tag{3.5}
\]

For every integral state \(b=(b_1,\ldots,b_r)\),

\[
 \boxed{
 \{T:L_b(T)=0\}=\mathcal T_b,\qquad
 {\cal H}(b)=\ell.}                                \tag{3.6}
\]

#### Proof

For \(T\in\mathcal T_a\), packet \(i\) covers \(T\) iff
\(b_i\ne a_i\), with probability \(1/2\), proving (3.5).
It is missed deterministically iff \(b_i=a_i\) for all \(i\), i.e.
\(a=b\), proving (3.6). \(\square\)

Here

\[
                         N=2^r\ell=2s,\qquad
                         G=rs,
\]

so \(G/N=r/2\), and every state misses fraction \(2^{-r}\).  For any
fixed desired slack \(\lambda\), choose \(r\ge2\lambda\).  Disjoint copies
give a linear missing count in every state and under every distribution.

The model satisfies the packet-level consequences one could hope to lift
from Proposition 7.1.  It is not claimed to be a literal rank-twisted
compiler realization; it disproves a deduction from one-point saturation
alone.

## 4. Smallest non-TU instance

For \(r=2\), use variables \(x,y\in\{0,1\}\) and targets
\(t_{00},t_{01},t_{10},t_{11}\), where \(t_{ab}\) is covered iff

\[
                         x\ne a\quad\text{or}\quad y\ne b.       \tag{4.1}
\]

With option variables \(x_0,x_1,y_0,y_1\), the cover system is

\[
 \begin{aligned}
 x_0+x_1&=1,& y_0+y_1&=1,\\
 x_1+y_1&\ge1,&x_1+y_0&\ge1,\\
 x_0+y_1&\ge1,&x_0+y_0&\ge1,\\
 x_0,x_1,y_0,y_1&\ge0.
 \end{aligned}                                     \tag{4.2}
\]

The point

\[
                         x_0=x_1=y_0=y_1={1\over2}  \tag{4.3}
\]

saturates all target inequalities.  Making all four tight uniquely gives
(4.3), so it is a fractional vertex.  No integral point covers all four:
assignment \((x,y)\) misses \(t_{xy}\).  The bundled cover matrix is
therefore not totally unimodular.

An ordinary bipartite matching formulation has silently split each
whole-option column into independently selectable incidences.

## 5. Why Birkhoff does not apply

Birkhoff--von Neumann applies when every matrix entry is an independently
selectable edge.  The moving-frame object has:

1. **whole-option bundling:** choosing \(\omega\) simultaneously fixes all
   \(s\) incidences in \(I_{P,\omega}\); and
2. **global legality:** allowed option tuples form \(\mathcal S\), possibly
   a proper subset of the Cartesian product.

Forgetting either condition permits a matching to mix incidences from
incompatible frames.  The fractional vertex (4.3) is the minimal example:
decomposition would require an integral assignment covering all four
targets, and none exists.

TU would apply under the much stronger hypothesis that one fixed frame
\(g\) supplies a genuine fractional matching in one bipartite graph,
respecting both source and target capacities.  Proposition 7.1 supplies
only an average over \(g\).  Even a fixed-frame matching can violate a
preassigned whole-packet chronology if it selects occurrence edges from
different packet options.

## 6. Exact missing-target continuation

For a distribution on legal states,

\[
 \mathbb E{\cal H}
 =\sum_T\Pr[L_\xi(T)=0].                            \tag{6.1}
\]

Thus \(\mathbb E{\cal H}=o(W)\) gives one integral state with \(o(W)\)
holes by averaging.  This is the correct configuration-level fractional
target.

For independent packet options, if

\[
                         p_P(T)=\Pr[T\in I_{P,\omega_P}],
\]

then

\[
                         \Pr[L(T)=0]
 =\prod_P(1-p_P(T)),\qquad
                         \mathbb E L(T)=\sum_Pp_P(T).             \tag{6.2}
\]

Section 3 has mean \(r/2\) but uncovered probability \(2^{-r}\), a
positive constant at fixed \(r\).

To force (6.1) to be \(o(W)\), one needs near-polarization, growing total
load, negative dependence excluding the all-miss event, or an explicit
integral theorem for bundled option columns.  At a fixed Gaussian depth,
the slack in Proposition 7.1 is a fixed constant, not a growing load.

## 7. Exact conclusion

Proposition 7.1 proves orbit flattening, legal normalized time sharing,
and annealed one-point slack.  It does not prove:

1. one fixed frame with pointwise fractional feasibility;
2. a matching in one fixed frame;
3. a distribution on legal packet states with small all-miss
   probabilities; or
4. one integral packet/compiler state with \(o(W)\) holes.

Neither bipartite TU nor Birkhoff bridges these gaps.  The exact remaining
theorem is

\[
 \boxed{
 \text{construct }\pi\text{ on globally legal states with }
 \sum_T\Pr_{\xi\sim\pi}[L_\xi(T)=0]=o(W).}          \tag{7.1}
\]

By averaging, (7.1) is already equivalent to one legal integral state with
\(o(W)\) holes.  Proposition 7.1 supplies only its first moments, and
Theorem 3.1 shows that no deterministic decomposition follows from those
moments alone.
