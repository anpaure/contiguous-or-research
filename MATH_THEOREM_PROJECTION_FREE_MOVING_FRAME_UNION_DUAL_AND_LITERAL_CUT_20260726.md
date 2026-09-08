# Projection-free moving frames: the whole-union configuration dual, an exact overlay expansion formula, and a physical linear cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

The objective is the exact missing-shadow hinge

\[
 \mathfrak H
 =\sum_{q\le H,\epsilon,T}(1-L_q^\epsilon(T))_+,
\tag{0.1}
\]

not CPCR. Every option below is a complete moving-frame/compiler state
through all protected depths. Target multiplicity inside one option is
discarded; only its literal support matters.

At one fixed sign and depth, write \(N_q\) for the number of targets and
suppose the owner factor supplies exactly \(W\) raw occurrences. Then

\[
 \sum_T(1-L_q(T))_+
 =\sum_T(L_q(T)-1)_+-(W-N_q).
\tag{0.1a}
\]

Thus missing shadows are repeat excess *above the forced baseline*
\(W-N_q\). CPCR asks for control of a floor/covariance profile and is
strictly stronger: it may fail even when every target is hit. Conversely,
the scalar mean \(W/N_q>1\) may hold while a positive fraction of targets
is missing. The entire note concerns the left side of (0.1a).

There are three conclusions.

1. The home-bundle configuration LP has the exact dual

   \[
   \boxed{
   \operatorname{def}_{\rm cfg}
   =\max_{0\le w_t\le1}
      \left[
       \sum_tw_t
       -\sum_g\max_{\omega\in\Omega_g}
                    \sum_{t\in J_g^\omega}w_t
      \right].}
   \tag{0.2}
   \]

   This is the correct fractional whole-option Hall inequality. It is not
   an integral near-cover theorem.

2. For a two-frame overlay whose owner interaction splits into legal
   whole-component choice orbits \(K\), let \(J_K^0,J_K^1\) be the two
   typed target supports. For a target token \(t\), let

   \[
   c_t={\bf1}_{\{\exists K:t\in J_K^0\cap J_K^1\}},
   \qquad
   d_t=\#\{K:t\in J_K^0\triangle J_K^1\}.
   \tag{0.3}
   \]

   Independent fair whole-component choices have exact expected missing
   mass

   \[
   \boxed{
   \Psi(F_0,F_1)
   =\sum_{t:c_t=0}2^{-d_t}.}
   \tag{0.4}
   \]

   Hence \(\Psi=o(W)\) is a literal one-step augmenting theorem. It uses
   whole option unions and all overlap orders, not endpoint degree,
   pair codegrees, or floor covariance.

3. Coordinate projection-freeness alone does not imply (0.4). In the
   canonical pair-status moving-frame model, take a matching catalogue
   whose coordinate union graph is connected. There is no nontrivial
   coordinate projection fixed by the catalogue, but the exact owner
   overlap has one component, so every integral state chooses one global
   pair frame. At every fixed

   \[
                         q=A\sqrt m+O(1),\qquad A>0,
   \]

   every such state has

   \[
   \boxed{
   \mathfrak H_q^\pm
   \ge(\delta_A-o(1))W,\qquad
   \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.}
   \tag{0.5}
   \]

   This is a physical positive-density missing-shadow cut in a
   projection-free coordinate atlas. In fact it is already visible to
   (0.2): for the one global choice group, the constant weight on the
   rank-\((m\pm q)\) target layer gives configuration deficit at least
   \((\delta_A-o(1))W\).

   There is an important apparent contradiction which must be resolved
   at the level of definitions. The \(S_{2m}\)-average of complete frame
   states gives every target *raw occurrence multiplicity* \(W/N_q>1\).
   But (0.2) averages support indicators after duplicates inside an
   option have been discarded. Its average support load is strictly below
   one. Thus raw first-moment balance is not fractional feasibility for
   the whole-union configuration LP.

The physical cut applies when the independent integral variables are the
common pair-status components. A finer projection-free compiler could
escape if its exact cycle overlays split that giant component. For that
escape, (0.4), or its nonuniform/general-configuration analogue below, is
the precise literal expansion inequality still required.

## 1. Fused moving-frame choice groups

Let

\[
 \mathcal U
 =\{(q,\epsilon,T):
       1\le q\le H,\ \epsilon\in\{-,+\},\
       T\in\binom{[2m]}{m+\epsilon q}\}
\tag{1.1}
\]

be the typed target-token universe. Complementary signs are fused into
one group option, so the same state realizes all tokens paired by

\[
                         (q,-,T)
 \longleftrightarrow(q,+,[2m]\setminus T).
\tag{1.2}
\]

Let \(\mathfrak G\) be the maximal owner-disjoint fused choice groups.
All shared frame, rank-matching, slab, and compiler variables must be
inside one group; after this fusion, every tuple
\((\omega_g)_g\in\prod_g\Omega_g\) is globally legal. For
\(\omega\in\Omega_g\), let

\[
                         J_g^\omega\subseteq\mathcal U
\tag{1.3}
\]

be the support of its whole all-depth literal target column.

For a deterministic state,

\[
 F(\boldsymbol\omega)
 =\left|\bigcup_gJ_g^{\omega_g}\right|,
\qquad
 \mathfrak H(\boldsymbol\omega)
 =|\mathcal U|-F(\boldsymbol\omega).
\tag{1.4}
\]

As a function of an unrestricted collection of option elements,
\(F\) is monotone submodular. The legal domain, however, requires exactly
one option per fused group. On relative option changes, one removes an old
set and adds a new set, so neither the improvement function nor the hole
function has a fixed submodularity sign.

## 2. The home-bundle configuration LP and its dual

For every \(g,\omega\), and every bundle
\(B\subseteq J_g^\omega\), introduce a variable \(x_{g,\omega,B}\).
The fractional home-assignment LP is

\[
\begin{aligned}
 \operatorname{cov}_{\rm cfg}=\max\quad&
       \sum_{g,\omega,B}|B|x_{g,\omega,B},\\
 \sum_{\omega,B}x_{g,\omega,B}&=1
                         &&(g\in\mathfrak G),\\
 \sum_{g,\omega,B:t\in B}x_{g,\omega,B}&\le1
                         &&(t\in\mathcal U),\\
 x_{g,\omega,B}&\ge0.
\end{aligned}
\tag{2.1}
\]

The empty bundle is allowed. The group equality chooses one fractional
whole option/bundle state; the target inequality assigns at most one home
to each target. The LP does not forbid nonhome overlaps.

### Theorem 2.1 (exact configuration dual)

Put

\[
                         \operatorname{def}_{\rm cfg}
                         =|\mathcal U|-\operatorname{cov}_{\rm cfg}.
\tag{2.2}
\]

Then (0.2) holds.

#### Proof

Dualize the group equalities with free variables \(\alpha_g\) and the
target capacities with \(y_t\ge0\):

\[
\begin{aligned}
 \operatorname{cov}_{\rm cfg}=\min\quad&
       \sum_g\alpha_g+\sum_ty_t,\\
 \alpha_g+\sum_{t\in B}y_t&\ge |B|
       &&(g,\omega,\ B\subseteq J_g^\omega).
\end{aligned}
\tag{2.3}
\]

For fixed \(g,\omega\), the strongest bundle consists exactly of the
targets with \(y_t<1\). Hence the bundle family in (2.3) is equivalent to

\[
 \alpha_g\ge
 \max_{\omega\in\Omega_g}
       \sum_{t\in J_g^\omega}(1-y_t)_+.
\tag{2.4}
\]

Clipping \(y_t\) to \([0,1]\) cannot increase the right side or the
objective. Put \(w_t=1-y_t\). Substitution in
\(|\mathcal U|-\operatorname{cov}_{\rm cfg}\) gives (0.2).
\(\square\)

Thus a fractional reserve of at most \(E\) uncovered tokens is possible
exactly when the right side of (0.2) is at most \(E\). At all depths
simultaneously, one weight vector on the typed universe is used; no
depthwise option maximum is legal.

### Integral gap

An integral solution of (2.1) is exactly a home-bundle matching and hence
one deterministic near-cover. Fractional feasibility need not round:
the alternating two-group catalogue

\[
 \{1,2\},\{3,4\}
 \qquad\text{and}\qquad
 \{1,3\},\{2,4\}
\tag{2.5}
\]

has zero value in (0.2), but every state misses one of the four targets.
Thus no proof of constant one can stop at Theorem 2.1.

## 3. The submodular concave-closure dual

Let \(\mathcal S\subseteq\prod_g\Omega_g\) be any globally legal state
catalogue and let \(\chi^\xi_{g,\omega}\) be the option indicator of
\(\xi\in\mathcal S\). Fix legal option marginals
\(\bar x=(\bar x_{g,\omega})\), for example the symmetric moving-frame
average.

The concave closure of the whole-union function at \(\bar x\) is

\[
\begin{aligned}
 F^+(\bar x)=\max\quad&
      \sum_{\xi\in\mathcal S}\pi_\xi F(\xi),\\
 \sum_\xi\pi_\xi&=1,\\
 \sum_\xi\pi_\xi\chi^\xi_{g,\omega}
      &=\bar x_{g,\omega},\\
 \pi_\xi&\ge0.
\end{aligned}
\tag{3.1}
\]

### Theorem 3.1 (exact affine-majorant dual)

\[
\boxed{
 F^+(\bar x)
 =\min_{\beta,\alpha}
 \left[
   \beta+\sum_{g,\omega}
              \alpha_{g,\omega}\bar x_{g,\omega}
 \right],}
\tag{3.2}
\]

where the minimum is over all affine majorants

\[
 \boxed{
 \beta+\sum_g\alpha_{g,\xi_g}
 \ge F(\xi)
 \qquad(\xi\in\mathcal S).}
\tag{3.3}
\]

#### Proof

This is the finite LP dual of (3.1): \(\beta\) dualizes total probability
and \(\alpha_{g,\omega}\) dualizes the option marginals. \(\square\)

The expected missing mass under the best correlated rounding with those
marginals is

\[
                         |\mathcal U|-F^+(\bar x).
\tag{3.4}
\]

Unlike (0.2), (3.2) sees every all-order intersection of the complete
state images. A constant majorant

\[
                         F(\xi)\le|\mathcal U|-D
                         \qquad(\xi\in\mathcal S)
\tag{3.5}
\]

is already a dual certificate of \(D\) unavoidable expected holes under
every distribution on \(\mathcal S\).

This is the relevant submodular/configuration dual for a prescribed
moving-frame fractional point. Pair moments and endpoint degrees are
projections of (3.1), not equivalent formulations.

## 4. Exact whole-union formula for a moving-frame overlay

First take arbitrary fused groups and independently choose
\(\omega\in\Omega_g\) with probabilities \(p_{g,\omega}\). Put

\[
 \rho_g(t)=\sum_{\omega:t\in J_g^\omega}p_{g,\omega}.
\tag{4.0}
\]

Because all shared legality variables were fused before the choices were
declared, the group choices are genuinely independent and every outcome
is a legal complete state. A target is missed exactly when every group
misses it. Hence the general whole-union identity is

\[
 \boxed{
 \mathbb E\mathfrak H
 =\sum_{t\in\mathcal U}\prod_{g\in\mathfrak G}
                         (1-\rho_g(t)).}
\tag{4.0a}
\]

Thus

\[
 \sum_t\prod_g(1-\rho_g(t))=o(W)
\tag{4.0b}
\]

is already a literal augmenting theorem. It is a product of exact
whole-option miss probabilities, not a truncation to endpoint degrees or
pair intersections.

Take two complete legal states \(F_0,F_1\) on the same owner set. Suppose
their exact owner interaction decomposes into components
\(\mathcal C\), and every component can choose side \(0\) or side \(1\)
independently while retaining whole compiler cycles. Fuse complementary
components and every other shared variable into choice orbits
\(\mathcal K\). For \(K\in\mathcal K\), let

\[
                         J_K^0,J_K^1\subseteq\mathcal U
\tag{4.1}
\]

be the whole typed supports contributed by its two sides.

Choose independent fair bits \(\varepsilon_K\) and install
\(J_K^{\varepsilon_K}\). Define \(c_t,d_t\) by (0.3).

### Theorem 4.1 (exact fair-overlay missing formula)

\[
 \boxed{
 \mathbb E\mathfrak H
 =\sum_{t:c_t=0}2^{-d_t}.}
\tag{4.2}
\]

Consequently some legal complement-symmetric component recombination has
at most the right side of (4.2) holes.

#### Proof

If \(t\in J_K^0\cap J_K^1\) for some \(K\), that group covers \(t\)
under either bit and its miss probability is zero.

Otherwise, every group counted by \(d_t\) covers \(t\) under exactly one
of its two bits. To miss \(t\), all those bits must choose their unique
noncovering values. The bits are independent, so the probability is
\(2^{-d_t}\). Groups covering \(t\) under neither option are irrelevant.
Sum the targetwise miss probabilities. \(\square\)

### Nonuniform version

If group \(K\) chooses side \(1\) with probability \(p_K\), then

\[
 \Pr(t\text{ missed})
 =
 {\bf1}_{\{c_t=0\}}
 \prod_{K:t\in J_K^0\setminus J_K^1}p_K
 \prod_{K:t\in J_K^1\setminus J_K^0}(1-p_K).
\tag{4.3}
\]

This is the exact projection-free overlay functional. It is a whole-union
quantity; it cannot be reconstructed from fixed target loads or pair
covariances.

### Literal expansion gate

A sufficient one-step moving-frame augmenting theorem is

\[
 \boxed{
 \sum_{q,\epsilon,T:c_{q,\epsilon,T}=0}
       2^{-d_{q,\epsilon,T}}
 =o(W)}
\tag{4.4}
\]

for some exact two-state overlay of the current factor with a legal moving
frame, after all complement and shared-choice fusion. Conditional
expectation then selects one whole-component state with
\(\mathfrak H=o(W)\).

More generally, for a current zero set and unequal old/new options, the
common-background union formula in
MATH_THEOREM_H_MEMORY_COMPLEMENT_GROUPED_HALL_AND_SLAB_CUT_TEST_20260726.md
is the exact augmenting criterion. Equation (4.4) is its symmetric
one-step specialization.

## 5. Projection-free coordinate motion does not imply literal expansion

Call a perfect-matching atlas **coordinate-projection-free** when its
coordinate union graph

\[
                         G_{\mathcal A}
 =([2m],\bigcup_{M\in\mathcal A}M)
\tag{5.1}
\]

is connected. Then no nonempty proper coordinate union is preserved by
every matching in the atlas.

In the canonical pair-status recoupling model, the common owner supports
are the occupancy fibres of the connected components of
\(G_{\mathcal A}\). Hence coordinate projection-freeness leaves one owner
support, the entire middle layer. Every integral component selector must
choose one global matching \(M\in\mathcal A\).

Fix such an \(M\). Let \(V_f\) be the number of middle owners with \(f\)
full \(M\)-pairs and \(T_{f,q}\) the number of lower rank-\((m-q)\)
targets with \(f\) full pairs. Exact counting gives

\[
 V_f={m!\,2^{m-2f}\over f!^2(m-2f)!},
\tag{5.2}
\]

\[
 T_{f,q}
 ={m!\,2^{m-2f-q}\over
        f!(f+q)!(m-2f-q)!}.
\tag{5.3}
\]

Every lower \(q\)-window in an \(M\)-status cell empties \(q\) split
pairs and therefore preserves the number \(f\) of full pairs. Thus

\[
                         \mathfrak H_q^-
 \ge\sum_f(T_{f,q}-V_f)_+.
\tag{5.4}
\]

Complementation gives the same upper bound.

### Theorem 5.1 (physical projection-free pair-status cut)

If \(q=A\sqrt m+O(1)\), then every integral state of the connected
pair-status moving atlas satisfies (0.5).

#### Proof

The statewise inequality is (5.4). First,

\[
 {N_q\over W}
 =\prod_{i=1}^q{m-i+1\over m+i}
 =e^{-A^2+o(1)}.
\]

Moreover

\[
 {V_f\over T_{f,q}}
 =2^q{(f+1)\cdots(f+q)\over
          (m-2f-q+1)\cdots(m-2f)},
\]

which is strictly increasing in \(f\), so the two type counts have one
crossing. On the scale

\[
                         f={m\over4}+u\sqrt m+O(1)
\]

direct logarithmic expansion gives

\[
 \log{V_f\over T_{f,q}}=8Au+3A^2+o(1).
\]

The number of full pairs in a uniform rank-\(m\) set has variance
\(m/16+o(m)\). If

\[
 z={4(f-\mathbb EF_m)\over\sqrt m},
\]

uniform Stirling expansion on bounded \(z\)-intervals gives

\[
 {V_f\over W}={4\over\sqrt m}\phi(z)(1+o(1)),
 \qquad
 {T_{f,q}\over N_q}={4\over\sqrt m}\phi(z+2A)(1+o(1)).
\]

The likelihood-ratio crossing is therefore at
\(z=-3A/2+o(1)\), which is \(A/2+o(1)\) in target-layer standardized
units. The factorial formulas also give uniform Gaussian tails, so the
local limits may be summed. Consequently

\[
 {1\over W}\sum_f(T_{f,q}-V_f)_+
 \longrightarrow
 e^{-A^2}\Phi(A/2)-\Phi(-3A/2)=\delta_A>0.
\]

Indeed, in the middle coordinate the target-minus-middle limiting density
is \(e^{-A^2}\phi(z+2A)-\phi(z)\), whose log likelihood ratio is
\(-2Az-3A^2\); it is strictly positive exactly below the crossing. This
also proves \(\delta_A>0\). \(\square\)

The cut is physical: for the actually selected frame \(M\), the missing
family contains the excess of the deficient full-pair strata. Although
those strata depend on \(M\), their *total* deficit is uniform over the
internal compiler choice as well as over all frames. Write a global option
as \(\omega=(M,\eta)\), where \(\eta\) contains every legal within-frame
compiler, cross-parent slab, endpoint-memory, and path-cover choice that
remains subordinate to \(M\). Then the fixed all-ones weight on the lower
target layer gives

\[
 \sum_{T\in\binom{[2m]}{m-q}}1
 -\max_{\omega=(M,\eta)}|J_\omega^-|
 \ge(\delta_A-o(1))W.
\tag{5.5}
\]

Since connected pair-status recoupling has one global choice group,
(5.5) is exactly a positive configuration-dual value in (0.2). The same
argument applies to the upper layer, or to their fused sum.

The same obstruction is visible directly in the whole-union overlay
formula. For any two global options \(\omega_0,\omega_1\), connectedness
leaves one choice orbit. On one target layer, (4.2) reduces identically to

\[
 \left|\mathcal U_q^-\setminus
          (J_{\omega_0}^-\cup J_{\omega_1}^-)\right|
 +{1\over2}|J_{\omega_0}^-\triangle J_{\omega_1}^-|
 =N_q-{ |J_{\omega_0}^-|+|J_{\omega_1}^-|\over2}
 \ge(\delta_A-o(1))W.
\tag{5.5a}
\]

Thus even the exact all-order union calculation has linear loss; no
endpoint-degree or pair-moment estimate is involved.

Now average any one exact frame factor over all
\(\sigma\in S_{2m}\). Owner transitivity gives owner load one, while
target transitivity gives every target **raw occurrence** load

\[
                         {W\over N_q}>1.
\tag{5.6}
\]

This does not contradict (5.5). Let \(m_\omega(T)\) denote the number of
raw occurrences of \(T\) in state \(\omega\). The raw average concerns
\(m_\omega(T)\), whereas the configuration LP concerns only
\({\bf1}_{\{m_\omega(T)>0\}}\). Relabelling a fixed state gives

\[
 \mathbb E_\sigma m_{\sigma\omega}(T)={W\over N_q}>1,
 \qquad
 \mathbb E_\sigma{\bf1}_{\{m_{\sigma\omega}(T)>0\}}
 ={ |J_\omega^-|\over N_q}
 \le1-(\delta_A-o(1)){W\over N_q}<1.
\tag{5.7}
\]

The difference is precisely repeat excess. Hence the obstruction is a
literal whole-option Hall cut, stronger than a mere integral-rounding
gap.

## 6. What a finer projection-free compiler must prove

Theorem 5.1 uses the exact common-support rigidity of pair-status
recoupling. It does not cover a compiler whose **cycle-level** interaction
components split the middle layer more finely and permit different frame
choices on those smaller owner supports.

For such a finer compiler, projection-freeness excludes the exterior
carrier cut from
MATH_THEOREM_FUSED_CONFIGURATION_HYPERGRAPH_AND_LINEAR_CARRIER_HALL_CUT_20260726.md,
but it supplies no lower bound on \(d_t\) in (0.3). The needed literal
statement is one of:

1. the overlay expansion inequality (4.4);
2. a nonuniform version using (4.3);
3. the full configuration expansion

   \[
   \sum_g\max_{\omega\in\Omega_g}
        \sum_{t\in J_g^\omega}w_t
   \ge\sum_tw_t-o(W)
   \qquad(0\le w_t\le1),
   \tag{6.1}
   \]

   together with an integral bundle decomposition theorem; or
4. a state-adaptive common-background augmenting-union theorem.

The raw moving-frame occurrence average does **not** prove (6.1). In the
canonical one-group atlas, Theorem 5.1 violates (6.1) with the constant
weight on a single protected target layer. The missing property is
literal fragmentation/homing: almost every target must be covered on
both sides of some component orbit or must see enough independently
choosable one-sided components that its miss probability in (4.2) is
summably small.

## 7. Certified boundary

Proved:

1. the exact home-bundle configuration LP dual (0.2);
2. the exact concave-closure/affine-majorant dual (3.2)--(3.3);
3. the exact whole-union overlay formula (4.2)--(4.3);
4. the literal sufficient expansion inequality (4.4);
5. a physical positive-density missing-shadow cut for the canonical
   coordinate-projection-free pair-status moving atlas; and
6. the exact failure of raw occurrence balance to imply fractional
   whole-support Hall feasibility.

Not proved:

1. (4.4) for the finer cycle-overlay moving compiler;
2. an integral decomposition of the bundle configuration LP;
3. a physical positive-density cut against every finer projection-free
   cycle overlay; or
4. constant one.

The answer is therefore a dichotomy. Projection-free coordinate motion
does not by itself beat the missing-shadow obstruction: the canonical
component model has a physical linear configuration cut. A finer compiler
can escape only by proving literal whole-union fragmentation at the level
of (4.2), not by invoking CPCR, endpoint degree, spectral gap, or fixed
moments.
