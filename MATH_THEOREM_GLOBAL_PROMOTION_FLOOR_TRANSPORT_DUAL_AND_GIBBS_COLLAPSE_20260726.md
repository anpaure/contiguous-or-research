# Global promotion-floor positivity: the exact transport dual, symmetric Gibbs gluing, and the nonlinear coefficient gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Inputs used without reproving them:

* `MATH_THEOREM_GIANT_PROMOTION_RING_STAR_RESOLUTION_AND_TRADE_LATTICE_20260726.md`;
* `MATH_THEOREM_W_GLOBAL_NECKLACE_ORBIT_CORRELATION_DICHOTOMY_20260726.md`;
* `MATH_THEOREM_GLOBAL_PROMOTION_MECHANICAL_ATLAS_AND_CLONE_HALL_20260726.md`;
* `MATH_THEOREM_PROMOTION_RING_R2_BLOCK_FLOOR_AND_GLOBAL_LATENT_OVERLAP_20260726.md`.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}m,\qquad N=\binom{2m}{m-H},
\tag{0.1}
\]

with calibrated covering-side depth

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 T:=MN=W+E,\qquad E=o(W).
\tag{0.2}
\]

For each root \(A\in\binom{[n]}{m-H}\), let \(\Omega_A\) be the directed
cyclic frames of \(A^c\), modulo rotation.  A full resolution is

\[
                         \omega=(\pi_A)_A
                         \in\Omega:=\prod_A\Omega_A.
\tag{0.3}
\]

Write \(L_D(\omega)\) for the number of selected root frames whose
middle deck contains \(D\in\binom{[n]}m\).  Then

\[
                         \sum_D L_D(\omega)=T=W+E.
\tag{0.4}
\]

The exact floor energy is

\[
\boxed{
 \Phi(\omega)
 :=\sum_D\frac{(L_D-1)(L_D-2)}2
 =\sum_D\binom{L_D}{2}-E.}
\tag{0.5}
\]

It is a nonnegative integer, it counts every hole at least once, and
\(\Phi=0\) exactly when every load is one or two.  Thus the middle
constant-one gate is \(\min_\omega\Phi(\omega)=o(W)\).

The individual target-star floor arrays and the signed trade-lattice
theorem are taken as established.  This note attacks their positive
global compatibility and proves the following exact reduction.

1. **Exact marginal transport polytope and dual.**  Let \(\Pi\) be the
   set of probability measures on \(\Omega\) for which every root frame
   is uniform.  Then

   \[
   \inf_{\gamma\in\Pi}\mathbb E_\gamma\Phi
   =\sup_{(\varphi_A)}
   \left\{
    \frac1F\sum_{A,\pi}\varphi_A(\pi):
    \sum_A\varphi_A(\pi_A)\le\Phi((\pi_A)_A)
    \right\},
   \tag{0.6}
   \]

   where \(F=(M-1)!\).

2. **Symmetric marginal collapse.**  In fact

   \[
      \boxed{
      \inf_{\gamma\in\Pi}\mathbb E_\gamma\Phi
      =\min_{\omega\in\Omega}\Phi(\omega).}
   \tag{0.7}
   \]

   The orbit measure of any deterministic minimizer has exactly uniform
   root-frame marginals.  In the dual (0.6), constant root potentials
   already attain the optimum.  Hence there is no extra positivity or
   transport obstruction caused by the common *one-root* marginals.
   This does not yet glue the higher joint laws of the overlapping star
   arrays.

3. **Exact star-extension dual.**  Let \(\mathcal K_D\) be the nonempty
   polytope of uniform-marginal, floor-supported laws on the full target
   star of \(D\).  There is a common global extension of some choice
   \(\mu_D\in\mathcal K_D\) if and only if no family of arbitrary local
   star functions \(f_D\) satisfies

   \[
    \sum_D\min_{\mu_D\in\mathcal K_D}
       \mathbb E_{\mu_D}f_D
    >\max_{\omega\in\Omega}\sum_D f_D(\rho_D\omega).
   \tag{0.8}
   \]

   This is the exact nonlinear compatibility dual.  Such a common
   extension exists if and only if a deterministic global floor
   resolution exists.  The canonical choice
   \(f_D=-\psi\circ\ell_D\) has separation margin exactly \(\Phi_*\).

4. **Exact Gibbs/IPF gluing of the one-root marginals.**  For every
   \(\beta\ge0\),

   \[
      \gamma_\beta(\omega)
      =\frac{e^{-\beta\Phi(\omega)}}
             {\sum_{\omega'}e^{-\beta\Phi(\omega')}}
   \tag{0.9}
   \]

   is a positive globally coupled one-frame-per-root law and belongs to
   \(\Pi\) automatically.  No marginal scaling factors are required:
   symmetry performs the iterative proportional fitting exactly.  As
   \(\beta\to\infty\), it converges to the uniform measure on the
   deterministic minimizers of \(\Phi\).

5. **All nonnegative weighted Hall cuts pass.**  The fractional problem
   of choosing one frame per root and giving every target expected load
   at least one has the uniform solution.  Its exact dual is

   \[
     \sup_{y_D\ge0}\left[
       \sum_Dy_D-\sum_A\max_{\pi\in\Omega_A}
                  \sum_{D\in e(A,\pi)}y_D
     \right]=0.
   \tag{0.10}
   \]

   Thus no nonnegative target-weight, star-capacity, or ordinary Hall
   certificate separates the global problem.

6. **The exact nonlinear support gate is a coefficient problem.**  Put

   \[
      P_A(\mathbf z)=
        \sum_{\pi\in\Omega_A}\prod_{D\in e(A,\pi)}z_D,
      \qquad
      P(\mathbf z)=\prod_AP_A(\mathbf z).
   \tag{0.11}
   \]

   A monomial exponent vector of \(P\) is exactly the load vector of one
   deterministic resolution, and its coefficient counts its frame
   representations.  Therefore

   \[
      \boxed{
      \min_\omega\Phi(\omega)
      =\min_{\mathbf l\in\operatorname {supp}P}
       \left(\sum_D\binom{l_D}{2}-E\right).}
   \tag{0.12}
   \]

   A perfect floor resolution exists if and only if \(P\) has a monomial
   with every exponent in \(\{1,2\}\).

7. **What the global atlases prove, and what they do not.**  The fixed-
   coordinate two-orbit atlas puts \((1-o(1))R\) compatible roots of
   every target into one of two catalogue-scale orbits and has the exact
   required coordinate degrees.  The individual target-star arrays prove
   that every one-star floor projection is feasible.  The mechanical
   clone-Hall atlas proves that, after restricting to its balanced support
   and replacing every root factor by its phasewise product relaxation, a
   monomial with only \(o(W)\) target defect exists.  None of these
   assertions proves that the corresponding exponent occurs in the
   common cyclic-label polynomial; the missing equations are exactly the
   lag-\(H\) identities.

8. **Precise remaining obstruction.**  Any negative theorem must now be
   a genuinely nonlinear support statement, for example

   \[
                         \Phi(\omega)\ge cW
                         \qquad\text{for every }\omega,
   \tag{0.13}
   \]

   or an equivalent proof that the floor exponent set is disjoint from
   \(\operatorname {supp}P\).  It cannot be a one-root marginal
   transport dual, a nonnegative weighted Hall cut, an additive
   congruence, a bounded target-star circuit, or a balanced-half profile
   cut.  In the full-star dual it must obtain its gap from the shared
   cyclic-frame variables.

No estimate \(\min\Phi=o(W)\) or \(\min\Phi=\Omega(W)\) is proved here.
The advance is that one-root positivity is no longer conflated with
higher star compatibility: the former and its entropy gluing are exact,
while the latter is precisely the nonlinear support problem for the
cyclic frame product, with dual (0.8).

## 1. The exact floor energy

For \(l\in\mathbb Z_{\ge0}\), put

\[
                         \psi(l)=\frac{(l-1)(l-2)}2
                         =\binom l2-l+1.
\tag{1.1}
\]

Then

\[
 \psi(0)=1,\qquad \psi(1)=\psi(2)=0,
 \qquad \psi(l)>0\quad(l\ge3).
\tag{1.2}
\]

### Lemma 1.1 (floor identity)

For every full resolution,

\[
                         \Phi(\omega)=\sum_D\psi(L_D)
                         =\sum_D\binom{L_D}{2}-E.
\tag{1.3}
\]

In particular, if \(h(\omega)=|\{D:L_D=0\}|\), then

\[
                         h(\omega)\le\Phi(\omega),
\tag{1.4}
\]

and \(\Phi=0\) if and only if every target load is one or two.

#### Proof

Sum (1.1) over the \(W\) targets and use (0.4):

\[
 \sum_D\psi(L_D)
 =\sum_D\binom{L_D}{2}-(W+E)+W.
\]

This is (1.3).  Equations (1.2) prove the remaining assertions. \(\square\)

This choice of energy is essential.  Raw collision energy has unavoidable
floor \(E\); raw squared error gives a different weight to holes and
double loads.  Formula (1.3) is exactly zero on the desired integer floor.

## 2. The full multi-marginal transport polytope

Let

\[
                         F=|\Omega_A|=(M-1)!,
\]

independent of the root.  Define \(\Pi\) to be the set of arrays
\(\gamma=(\gamma_\omega)_{\omega\in\Omega}\) satisfying

\[
 \gamma_\omega\ge0,\qquad
 \sum_\omega\gamma_\omega=1,
\tag{2.1}
\]

and, for every root \(A\) and frame \(\pi\in\Omega_A\),

\[
                         \sum_{\omega:\omega_A=\pi}\gamma_\omega
                         =\frac1F.
\tag{2.2}
\]

This is the exact one-root common-marginal transport polytope induced by
the overlapping target-star arrays.  It is nonempty because it contains
the independent product of uniform root frames.  The stronger polytope
which retains each full star law is defined in Section 4.2.

For \(\varepsilon\ge0\), define its floor sublevel

\[
 \Pi(\varepsilon)=
 \left\{\gamma\in\Pi:
        \sum_\omega\gamma_\omega\Phi(\omega)\le\varepsilon W
 \right\}.
\tag{2.3}
\]

Since all sets are finite, \(\Pi(\varepsilon)\) is a rational polytope.
If it is nonempty, some deterministic configuration in its support has
\(\Phi\le\varepsilon W\).  The converse, including the exact marginals,
is stronger and follows from symmetry in Section 4.

## 3. Exact Kantorovich--Farkas dual

### Theorem 3.1 (multi-root transport dual)

One has

\[
\begin{aligned}
 \inf_{\gamma\in\Pi}\mathbb E_\gamma\Phi
 =\sup_{(\varphi_A)}\Biggl\{
   &\frac1F\sum_A\sum_{\pi\in\Omega_A}\varphi_A(\pi):\\
   &\sum_A\varphi_A(\pi_A)
      \le\Phi((\pi_A)_A)
      \quad\text{for every }(\pi_A)_A\in\Omega
 \Biggr\}.
\end{aligned}
\tag{3.1}
\]

The potentials \(\varphi_A\) are arbitrary real functions on root
frames.

#### Proof

This is finite linear-programming duality.  Put one primal variable
\(\gamma_\omega\) at every global configuration, use (2.2) as equality
constraints, and use \(\Phi(\omega)\) as the objective coefficient.
The dual variable at the equality for \((A,\pi)\) is
\(\varphi_A(\pi)\).  The dual inequality at a primal column \(\omega\)
is exactly the pointwise inequality in (3.1).  The redundant total-mass
constraint may be absorbed by adding constants to the root potentials.
The primal is feasible and bounded, so strong duality applies. \(\square\)

This theorem characterizes every incompatibility involving only the
prescribed one-root marginals.  The next theorem shows that symmetry
makes all such incompatibilities trivial.

## 4. Symmetric orbit gluing

The group \(G=S_{2m}\) acts on roots, frames, targets, and global
resolutions by relabelling coordinates.  The energy \(\Phi\) is invariant.

### Theorem 4.1 (marginal collapse)

Let

\[
                         \Phi_*:=\min_{\omega\in\Omega}\Phi(\omega).
\tag{4.1}
\]

Then

\[
                         \boxed{
                         \min_{\gamma\in\Pi}\mathbb E_\gamma\Phi
                         =\Phi_*.}
\tag{4.2}
\]

Moreover:

1. if \(\omega_*\) is any deterministic minimizer, the uniform measure
   on its \(G\)-orbit belongs to \(\Pi\) and is supported on minimizers;
2. in the dual (3.1), the constant choice
   \[
                         \varphi_A(\pi)=\frac{\Phi_*}{N}
   \tag{4.3}
   \]
   is feasible and optimal; and
3. for every \(\varepsilon\), \(\Pi(\varepsilon)\ne\varnothing\) if
   and only if some deterministic resolution has
   \(\Phi\le\varepsilon W\); and
4. more generally, every nonempty \(G\)-invariant subset
   \(\mathcal S\subseteq\Omega\) supports a measure in \(\Pi\).

#### Proof

Every probability measure has expected energy at least \(\Phi_*\).  Fix
a minimizer \(\omega_*\) and average its coordinate relabellings.  The
resulting orbit measure remains supported on minimizers.

It remains to check its marginals.  The action of \(S_{2m}\) is
transitive on all pairs \((A,\pi)\) consisting of a root and one of its
frames.  Every orbit configuration selects exactly one such pair above
each of the \(N\) roots.  Hence, after orbit averaging, all root-frame
pair inclusion probabilities are equal.  Their sum at a fixed root is
one, so every frame probability is \(1/F\).  Thus the orbit measure lies
in \(\Pi\), proving (4.2).

For (4.3), the sum of the root potentials is \(\Phi_*\), which is at most
\(\Phi(\omega)\) for every configuration.  Its dual value is
\(\Phi_*\), so it is optimal by (4.2).  The third assertion follows by
orbit-averaging a deterministic sublevel configuration in one direction,
and by selecting a support point no worse than the expectation in the
other.  For the fourth, orbit-average any member of \(\mathcal S\); its
orbit remains inside \(\mathcal S\) by invariance and has uniform
marginals by the preceding count. \(\square\)

Thus the prescribed one-root marginals do not create a positivity gap.
The overlapping star arrays fail to tensor only because they attempt to
prescribe much more than these marginals: they prescribe incompatible
joint laws on their intersections.  Once only the common uniform
marginals and the global floor objective are retained, orbit gluing is
exact.

### 4.2 The full target-star marginal polytope

The preceding collapse must not be mistaken for a gluing of the
floor-optimal star arrays themselves.  We now formulate that stronger
problem exactly.

For a target \(D\), let

\[
 \mathcal R(D)=\{A\in\mathcal A:A\subset D\},
 \qquad
 X_D=\prod_{A\in\mathcal R(D)}\Omega_A,
\tag{4.4}
\]

and let \(\rho_D:\Omega\to X_D\) be restriction to the eligible roots.
For \(x\in X_D\), set

\[
 \ell_D(x)=
  \sum_{A\in\mathcal R(D)}
       \mathbf 1_{\{D\in e(A,x_A)\}},
 \qquad
 \mathcal F_D=\{x:\ell_D(x)\in\{1,2\}\}.
\tag{4.5}
\]

Let \(\mathcal K_D\subseteq\Delta(X_D)\) consist of the probability
measures supported on \(\mathcal F_D\) whose marginal on every
coordinate \(A\in\mathcal R(D)\) is uniform on \(\Omega_A\).  The
established exact star-resolution theorem says precisely that

\[
                         \mathcal K_D\ne\varnothing
                         \qquad(D\in\mathcal M).
\tag{4.6}
\]

For a prescribed family \(\boldsymbol\mu=(\mu_D)_D\), define the exact
extension polytope

\[
 \Gamma(\boldsymbol\mu)=
 \left\{\gamma\in\Delta(\Omega):
       (\rho_D)_\#\gamma=\mu_D
       \text{ for every }D\right\}.
\tag{4.7}
\]

Every root lies in at least one target star.  Consequently, if
\(\mu_D\in\mathcal K_D\) for all \(D\), every
\(\gamma\in\Gamma(\boldsymbol\mu)\) automatically belongs to \(\Pi\).

### Theorem 4.2 (exact star-extension dual)

Let \(\mu_D\in\mathcal K_D\) for every target.

1. The family \((\mu_D)_D\) has a common global extension if and only if,
   for every collection of real functions \(f_D:X_D\to\mathbb R\),

   \[
    \sum_D\mathbb E_{\mu_D}f_D
    \le
    \max_{\omega\in\Omega}
        \sum_D f_D(\rho_D\omega).
   \tag{4.8}
   \]

2. Some choice \(\mu_D\in\mathcal K_D\) has a common global extension
   if and only if no family \((f_D)_D\) satisfies

   \[
    \boxed{
    \sum_D\min_{\mu\in\mathcal K_D}\mathbb E_\mu f_D
    >
    \max_{\omega\in\Omega}\sum_D f_D(\rho_D\omega).}
   \tag{4.9}
   \]

3. Such a common extension exists if and only if the deterministic floor
   set

   \[
    \mathcal F=\bigcap_D\rho_D^{-1}(\mathcal F_D)
   \tag{4.10}
   \]

   is nonempty.

#### Proof

Let

\[
 \mathfrak G=
 \left\{\bigl((\rho_D)_\#\gamma\bigr)_D:
              \gamma\in\Delta(\Omega)\right\}
 \subseteq\prod_D\Delta(X_D).
\tag{4.11}
\]

This is the convex hull of the finitely many vectors
\(\bigl(\delta_{\rho_D\omega}\bigr)_D\), \(\omega\in\Omega\).  Hence a
fixed \(\boldsymbol\mu\) belongs to \(\mathfrak G\) if and only if every
linear functional is at most its maximum on those vertices.  This is
exactly (4.8).

Now put \(\mathfrak K=\prod_D\mathcal K_D\).  The compact convex sets
\(\mathfrak G\) and \(\mathfrak K\) are disjoint if and only if they are
strictly separated by a linear functional \((f_D)_D\).  Its supremum on
\(\mathfrak G\) is the right side of (4.9), while its infimum on
\(\mathfrak K\) is the left side.  This proves assertion 2.

If \(\boldsymbol\mu\in\mathfrak G\cap\mathfrak K\), take an extension
\(\gamma\).  Since every star marginal is supported on
\(\mathcal F_D\), one has
\(\gamma(\rho_D^{-1}(\mathcal F_D))=1\) for every \(D\).  There are
finitely many targets, so \(\gamma(\mathcal F)=1\), and in particular
\(\mathcal F\ne\varnothing\).

Conversely, suppose \(\omega_*\in\mathcal F\).  Average \(\omega_*\)
over \(S_{2m}\).  The resulting measure is supported on \(\mathcal F\),
and Theorem 4.1 gives uniform one-root marginals.  Therefore each of its
star marginals lies in \(\mathcal K_D\), furnishing the required common
extension. \(\square\)

The exact near-floor version is the variational identity

\[
 \Phi_*
 =\min_{\boldsymbol\nu\in\mathfrak G}
     \sum_D
      \left\langle\psi\circ\ell_D,\nu_D\right\rangle.
\tag{4.12}
\]

The product relaxation \(\mathfrak K\) makes every summand zero, but it
need not meet \(\mathfrak G\).  Thus (4.9), rather than the constant
one-root dual of Theorem 3.1, is the exact location of a possible
positive global obstruction.  Pairwise agreement of star laws on every
overlap is necessary, but the cyclic star hypergraph is not a junction
tree, so such agreement alone is not a gluing theorem.

### Lemma 4.3 (no root-additive star separator)

No strict separator (4.9) can have the form

\[
 f_D(x)=c_D+
        \sum_{A\in\mathcal R(D)}g_{D,A}(x_A).
\tag{4.13}
\]

#### Proof

Every \(\mu\in\mathcal K_D\) has uniform one-root marginals, so the
expectation of (4.13) is independent of \(\mu\).  Summed over \(D\), it
equals the expectation of
\(\sum_D f_D(\rho_D\omega)\) under the independent uniform global law
\(\mathbb P_0\).  The maximum of that global score is at least its
expectation.  Hence the strict inequality in (4.9) is impossible.
\(\square\)

Thus any genuine incompatibility certificate has a nonzero interaction
part inside at least one star.  In the mechanical atlas it must, more
specifically, couple two or more phase labels belonging to the same root:
the clone relaxation makes those labels independent, while the genuine
frame forces them to arise from the single bijection (8.4) and the
lag-\(H\) equations (8.5).

### Proposition 4.4 (canonical nonlinear separator)

Define the same symmetric star potential at every target by

\[
                         f_D(x)=-\psi(\ell_D(x)).
\tag{4.14}
\]

Then the two sides of the flexible extension inequality (4.9) are

\[
 \sum_D\min_{\mu\in\mathcal K_D}\mathbb E_\mu f_D=0,
 \qquad
 \max_{\omega\in\Omega}\sum_Df_D(\rho_D\omega)=-\Phi_*.
\tag{4.15}
\]

Consequently this one explicit family strictly separates the local
floor-star product from the global marginal polytope if and only if
\(\Phi_*>0\), and its separation margin is exactly \(\Phi_*\).  In
particular, a quantitative no-go \(\Phi_*\ge cW\) is identical to an
order-\(W\) nonlinear star-dual gap.

#### Proof

Every law in \(\mathcal K_D\) is supported where \(\psi(\ell_D)=0\),
which gives the first equality.  The second follows from

\[
 \sum_D f_D(\rho_D\omega)
 =-\sum_D\psi(L_D(\omega))=-\Phi(\omega).
\]

Taking the maximum over \(\omega\) proves (4.15). \(\square\)

## 5. Symmetric Gibbs gluing and the entropy formula

Let \(\mathbb P_0\) be the independent uniform product measure on
\(\Omega\), and define

\[
 Z_\beta=\mathbb E_{\mathbb P_0}e^{-\beta\Phi},
 \qquad
 \gamma_\beta(\omega)
  =\frac{e^{-\beta\Phi(\omega)}}{Z_\beta}\mathbb P_0(\omega).
\tag{5.1}
\]

### Theorem 5.1 (automatic IPF)

For every \(\beta\ge0\):

1. \(\gamma_\beta\in\Pi\);
2. \(\gamma_\beta\) is strictly positive on every global resolution;
3. \[
      \mathbb E_{\gamma_\beta}\Phi
       =-\frac d{d\beta}\log Z_\beta,
      \qquad
      \operatorname {Var}_{\gamma_\beta}\Phi
       =\frac {d^2}{d\beta^2}\log Z_\beta;
   \tag{5.2}
   \]
4. \(\gamma_\beta\) converges as \(\beta\to\infty\) to the uniform
   measure on the set of deterministic minimizers; and
5. the exact entropy variational identity is
   \[
    -\log Z_\beta
     =\min_{\gamma}\left\{
       \beta\mathbb E_\gamma\Phi
       +D_{\rm KL}(\gamma\|\mathbb P_0)
      \right},
   \tag{5.3}
   \]
   and the minimizer in (5.3) automatically lies in \(\Pi\).

#### Proof

Both \(\mathbb P_0\) and \(\Phi\) are invariant under \(S_{2m}\), so
\(\gamma_\beta\) is invariant.  The same transitivity argument as in
Theorem 4.1 makes every root-frame marginal uniform.  Positivity is
immediate.  Differentiating the finite partition function proves (5.2).
As \(\beta\to\infty\), all nonminimum states are exponentially
suppressed, and all minimum states have equal weight.  Finally, (5.3) is
the elementary Gibbs variational formula, obtained by expanding
\(D_{\rm KL}(\gamma\|\gamma_\beta)\ge0\).  Its unique minimizer is
\(\gamma_\beta\), already shown to lie in \(\Pi\). \(\square\)

This is a genuine positive joint law on all root variables and therefore
induces mutually compatible star marginals at every finite temperature.
It does not assert that those induced marginals equal the separately
constructed floor-optimal star arrays.  The remaining quantitative
theorem is exactly a zero-temperature free-energy estimate:

\[
                         \Phi_*=o(W).
\tag{5.4}
\]

Equivalently, it is enough to prove

\[
                         -\frac1\beta\log Z_\beta=o(W)
\tag{5.5}
\]

along some \(\beta\to\infty\), since the left side decreases to
\(\Phi_*\).

## 6. Exact weighted Hall dual and its collapse

Before integrality, consider the root-frame cover LP

\[
 x_{A,\pi}\ge0,
 \qquad
 \sum_{\pi\in\Omega_A}x_{A,\pi}=1
 \quad(A\in\mathcal A),
\tag{6.1}
\]

\[
 \sum_{A,\pi:D\in e(A,\pi)}x_{A,\pi}\ge1
 \quad(D\in\mathcal M).
\tag{6.2}
\]

### Theorem 6.1 (all target-weight cuts pass)

The LP (6.1)--(6.2) is feasible.  Its Farkas dual obstruction value is

\[
 \sup_{y_D\ge0}\left[
  \sum_Dy_D-\sum_A\max_{\pi\in\Omega_A}
              \sum_{D\in e(A,\pi)}y_D
 \right]=0.
\tag{6.3}
\]

#### Proof

Set \(x_{A,\pi}=1/F\).  A fixed target has
\(R=\binom mH\) eligible roots and is selected by a uniform frame with
probability \(p=M/\binom MH\).  Its load is

\[
                         Rp=\theta=\frac{MN}{W}\ge1.
\]

Thus the primal is feasible.

For the dual directly, fix nonnegative \(y\).  The average frame score at
root \(A\) is no larger than its maximum.  Summing the averages over all
roots gives

\[
 \sum_A\max_\pi\sum_{D\in e(A,\pi)}y_D
 \ge\sum_A\frac1F\sum_\pi\sum_{D\in e(A,\pi)}y_D
 =\theta\sum_Dy_D
 \ge\sum_Dy_D.
\]

So every dual expression is nonpositive; \(y=0\) gives value zero.
\(\square\)

This includes arbitrary weighted stars and all ordinary set-capacity
cuts.  Any obstruction must use integrality or correlations between at
least two target loads.

## 7. Exact generating-polynomial support gate

For each root define its frame polynomial

\[
                         P_A(\mathbf z)
                         =\sum_{\pi\in\Omega_A}
                           \prod_{D\in e(A,\pi)}z_D,
\tag{7.1}
\]

and put

\[
                         P(\mathbf z)=\prod_AP_A(\mathbf z).
\tag{7.2}
\]

All coefficients are nonnegative integers.

### Theorem 7.1 (coefficient characterization)

For \(\mathbf l=(l_D)_D\in\mathbb Z_{\ge0}^{\mathcal M}\), the
coefficient \([\mathbf z^{\mathbf l}]P\) is positive if and only if some
full resolution has load vector \(\mathbf l\).  Consequently (0.12)
holds, and a zero-energy resolution exists exactly when

\[
 [\mathbf z^{\mathbf l}]P>0
 \quad\text{for some}\quad
 l_D\in\{1,2\},\quad
 |\{D:l_D=2\}|=E.
\tag{7.3}
\]

#### Proof

Choosing one monomial from every factor \(P_A\) is choosing one frame at
every root.  The exponent of \(z_D\) in the product is the number of
chosen decks containing \(D\), namely \(L_D\).  Conversely every
resolution contributes its load monomial.  Positivity of coefficients
prevents cancellation, proving the equivalence.  Formula (1.3) gives the
energy statement. \(\square\)

The theorem identifies the only possible nonlinear obstruction: a hole
in the integer support of a huge positive polynomial.  Convex first
moments cannot detect such a hole, because the uniform mean
\(\theta\mathbf1\) lies both in the configuration load polytope and in
the convex hull of the floor vectors.

## 8. The two-orbit, target-star, and mechanical clone-Hall atlases

The known atlases are now easy to place exactly.

### 8.1 The global two-orbit atlas

Fix a coordinate \(x\).  Its stabilizer
\(G_x=S_{[n]\setminus\{x\}}\) splits the full rooted-frame catalogue into
exactly two orbits, according as \(x\in A\) or \(x\notin A\).  If
\(x\notin D\), all \(R\) roots of \(D\) lie in the second class.  If
\(x\in D\), the exact split is

\[
 |\mathcal R(D)\cap\{A:x\in A\}|
  =\frac{m-H}{m}R,
 \qquad
 |\mathcal R(D)\cap\{A:x\notin A\}|
  =\frac HmR.
\tag{8.1}
\]

Thus one global catalogue orbit contains \((1-o(1))R\) compatible roots
for every target.  The two classes also have the exact forced coordinate-
degree totals.  This removes the orbit-size and point-margin obstructions
at the required root-star scale.

It does not provide the dominant seed supports.  Independent global
motion of the two classes has \(o(W)\) holes only if the selected frames
inside the dominant class already cover the corresponding half of the
middle layer up to \(o(W)\).  Orbit averaging preserves the floor energy
of each seed; it cannot manufacture a low-energy support point.

### 8.2 The individual target-star atlas

Fix a target \(D\).  At an eligible root, frames split into the two
classes

\[
                         D\in e(A,\pi),
                         \qquad
                         D\notin e(A,\pi).
\tag{8.2}
\]

The established giant star resolution couples all \(R\) eligible roots,
keeps the uniform frame marginal, and makes \(L_D\in\{1,2\}\).  Hence
every one-target projection of the floor marginal problem is exactly
feasible.

For two targets at distance at most \(H\), however, their stars overlap.
The two separately constructed laws prescribe different joint
distributions on the shared roots.  Equality of their one-root marginals
is only the first consistency condition.  A global extension would have
to satisfy all overlap marginals on the cyclic hypergraph of target
stars.  Theorem 4.1 shows that this extension issue creates no additional
cost once a deterministic floor configuration exists; it does not prove
that such a support point exists.

### 8.3 The mechanical clone-Hall atlas

Fix a balanced half \(Q\subset[n]\).  At each root, the mechanical word
specifies the \(Q/Q^c\) type of every phase simultaneously at all interval
lengths.  If phase labels are allowed to vary independently, the
mechanically restricted root factor is relaxed to a product

\[
 \widetilde P_A(\mathbf z)
 =\prod_{i\in\mathbb Z_M}
   \left(\sum_{D\in\mathcal N_{A,i}}z_D\right),
\tag{8.3}
\]

where \(\mathcal N_{A,i}\) is the literal target cell allowed by the
mechanical phase type.  The clone-Hall theorem proves that the product of
the \(\widetilde P_A\)'s has a monomial with only \(o(W)\) middle defect;
the analogous statement holds separately at the audited entrance rows.

The mechanically restricted genuine frame polynomial is not the full
product (8.3).  Its phase labels must come from one bijection

\[
                         \varphi_A:\mathbb Z_M\longrightarrow A^c,
\tag{8.4}
\]

and consecutive phase sets must obey the lag-\(H\) identities

\[
 J_{i+1}\setminus J_i
 =J_{i+H}\setminus J_{i+H+1}.
\tag{8.5}
\]

Thus the mechanically restricted part of \(P_A\) is a diagonal
common-permutation subpolynomial of the clone relaxation.  Clone Hall
proves that the relaxed coefficient is positive; the global gate is
whether a nearby coefficient survives the diagonal restriction at every
root simultaneously.

### Corollary 8.1 (dual classes already eliminated)

The following cannot furnish a linear-order obstruction:

1. orbit-size and point-margin cuts, by the global two-orbit atlas;
2. one-target or one-star marginal cuts, by the giant star arrays;
3. arbitrary nonnegative target weights, by Theorem 6.1;
4. balanced-half profile weights, by the mechanical profile census;
5. independent phase-cell Hall cuts, by clone Hall; and
6. additive integral congruences, by the full signed trade-lattice
   theorem.

A surviving obstruction must see at least two overlapping target stars
and the common label permutation (8.5).  Equivalently it must detect a
support hole of \(P\) which disappears in \(\prod_A\widetilde P_A\).

## 9. What iterative proportional fitting can and cannot do

The hard floor constraints define the set

\[
                         \mathcal F
 =\{\omega:L_D(\omega)\in\{1,2\}\text{ for every }D\}.
\tag{9.1}
\]

If \(\mathcal F\ne\varnothing\), uniform measure on \(\mathcal F\) is
already in \(\Pi\) by symmetry, and hard iterative proportional fitting
has a feasible limit.  If \(\mathcal F=\varnothing\), no sequence of
local star projections can create one; its limiting divergence yields a
statewise support certificate rather than a marginal one.

Soft IPF is always defined and is exactly the Gibbs family (5.1).  The
individual star-floor array is the maximum-entropy correction for one
isolated target star, but composing those corrections is not the same as
the global Gibbs law because their scopes overlap.  The exact quantity
which decides the outcome is the zero-temperature free energy

\[
                         \lim_{\beta\to\infty}
                         -\frac1\beta\log Z_\beta=\Phi_*.
\tag{9.2}
\]

The strengthened same-block triple theorem makes this distinction
quantitative.  A product of independent root blocks with \(o(W)\) holes
must have blocks of size at least \(R^{2-o(1)}\), not merely the
\(R\)-root size of one target star.  Thus a product of the individual
star arrays is ruled out even at its natural orbit scale.  The Gibbs law
in (5.1) is genuinely catalogue-wide and is not a forbidden block
product.

Thus an entropy proof must give a lower bound on \(Z_\beta\) strong enough
to make (9.2) \(o(W)\).  Merely knowing every one-star entropy projection,
or every clone-Hall coefficient, does not multiply because every root
lies in \(\Theta(M\binom mH)\) target stars.

## 10. Exact remaining theorem or obstruction

There are now two equivalent ways to finish the middle positivity gate.

### Positive form

Prove any one of

\[
                         \min_{\omega\in\Omega}\Phi(\omega)=o(W),
\tag{10.1}
\]

\[
                         \lim_{\beta\to\infty}
                         -\frac1\beta\log Z_\beta=o(W),
\tag{10.2}
\]

or that \(P\) has a monomial whose exponent vector has floor defect
\(o(W)\).  Orbit averaging then gives a positive uniform-marginal global
coupling automatically.

### Negative form

Exhibit a nonlinear statewise inequality

\[
                         \Phi(\omega)\ge cW
                         \qquad(\omega\in\Omega)
\tag{10.3}
\]

for some fixed \(c>0\), or an equivalent coefficient-support invariant
of \(P\).  By Corollary 8.1, it must use common-permutation holonomy across
overlapping target stars.  A nonnegative target weighting, a root-frame
transport potential, or a bounded harmonic score cannot suffice.

For the full constant-one theorem, a positive middle resolution must be
refined by one common tag word per root.  The same construction then needs
the shorter and longer interval polynomials at every controlled depth to
have aggregate floor defect \(o(W)\).  The transport symmetry remains
valid for that enlarged invariant cost; only the nonlinear support
problem becomes stronger.

## 11. Audited boundary

Proved:

1. the exact floor energy and its hole interpretation;
2. the complete multi-marginal transport polytope and Kantorovich dual;
3. symmetry collapse of the transport optimum to a deterministic minimum;
4. the exact full-star extension polytope and its nonlinear separation
   dual;
5. impossibility of a root-additive star separator;
6. the canonical nonlinear star separator with exact margin \(\Phi_*\);
7. exact positive Gibbs/IPF gluing with uniform root marginals;
8. collapse of every nonnegative weighted Hall dual;
9. the generating-polynomial coefficient characterization; and
10. the exact placement of the two-orbit, individual-star, and mechanical
   clone-Hall atlases as orbit-scale, one-star, and phasewise relaxations
   of the common support gate.

Not proved:

1. \(\Phi_*=o(W)\);
2. \(\Phi_*=\Omega(W)\);
3. positivity of a floor or near-floor coefficient of \(P\); or
4. simultaneous nested-rank floor control.

The strongest exact conclusion is that **one-root marginal compatibility
is not the remaining obstruction**.  Symmetry glues every deterministic
support point into the required uniform-marginal law and makes that
transport dual constant.  Full star-law compatibility is equivalent to
the nonlinear separator (4.9), or, identically, to the integral support
of the common cyclic-label polynomial.
