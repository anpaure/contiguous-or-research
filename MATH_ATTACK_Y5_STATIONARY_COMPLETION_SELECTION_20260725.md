# Fifth-wave Y: stationary class selection as an exact completion-count theorem

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn.
\]

For fixed \(A>0\), let

\[
H=H_A=\lceil A\sqrt m\rceil
\]

and take \(m\) sufficiently large that \(H\le m-1\).  Let
\(K_{\rm tr}\) be the fair exact transposition-component heat kernel on the
finite fibre \(\mathfrak F_m\) of literal squarefree exact middle wreath
factors.

This attack does **not** prove that an original communicating class has
stationary mean \(O_A(HB)\).  It produces a new exact theorem which composes
quantitatively into coefficient one and isolates the missing positive
geometry in literal completion counts.

For a communicating class \(\mathscr C\), fix one wreath \(R\).  Conditional
on a uniform class factor containing \(R\), let \(\mathsf G_H(\mathscr C)\)
be the expected weighted number of lower intervals which \(R\) shares with
the other selected wreaths.  Then

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
=B\,\mathsf G_H(\mathscr C)-2\Lambda_H,
}
\tag{Y5.1}
\]

where \(\Lambda_H\) is the exact aggregate minimum integer pair-collision
floor.  In particular,

\[
\boxed{
\min_{\mathscr C}
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
\le C_AHB
\iff
\min_{\mathscr C}\mathsf G_H(\mathscr C)
\le\frac{2\Lambda_H}{B}+C_AH.
}
\tag{Y5.2}
\]

The baseline is explicit:

\[
\boxed{
\frac{2\Lambda_H}{B}
=n\sum_{q=1}^{H}
\frac{c_q+2\theta_q-1}{c_q+\theta_q}.
}
\tag{Y5.3}
\]

Thus the stationary theorem is exactly an additive-\(O_A(H)\)
conditional co-owner completion theorem around a baseline of order
\(nH\).  It requires relative \(O_A(1/n)\) accuracy.  At depth one the
baseline is

\[
\boxed{
\frac{2L_1}{B}
=\frac{4(2m+1)}{m+2}
=8-\frac{12}{m+2}.
}
\tag{Y5.4}
\]

There is also a deterministic literal form.  A bounded spill statistic
\(0\le\rho_{q,S}(D)\le q\), defined from the middle windows of \(D\) which
contain \(S\) without making it a lower interval, has a universal ceiling
\(\Sigma_q^{\max}\) such that every exact factor obeys

\[
\boxed{
(q+1)Q_q(F)=\Sigma_q^{\max}-\Sigma_q(F).
}
\tag{Y5.4a}
\]

Thus the stationary target is losslessly equivalent to finding a stationary
law whose expected literal spill is within weighted \(O_A(HB)\) of these
ceilings.  No fractional or signed state enters this identity.

The uniform law on the whole exact fibre is already stationary.  Hence a
single global completion-count inequality, involving the numbers of exact
factor completions of one wreath and one compatible wreath pair, is a
proved sufficient route to (Y5.2).

Two tempting shortcuts are closed exactly.

1. Any reversible short-permutation heat which includes all original
   transposition projections has stationary classes which are unions of
   original classes.  Its class means are size-weighted averages of original
   class means.  A low short class therefore selects a low original class,
   but class enlargement itself supplies no bound.

2. On a genuine transposition cell, midpoint-preserving Graver covariance
   routing chooses an optimal antipodal sign pair.  Stationarity instead
   forces all component signs to be independent fair bits.  The exact full
   energy lost by imposing stationarity is

   \[
   \boxed{
   \frac14\left(
   \sum_i\|V_i\|_H^2
   -\min_{\varepsilon_i=\pm1}
   \left\|\sum_i\varepsilon_iV_i\right\|_H^2
   \right)\ge0.
   }
   \tag{Y5.5}
   \]

   This stationary correlation tax is an additional necessary gate, not a
   covariance parametrization artifact.

Finally, a uniform \(B\)-subset of wreaths has conditional overlap exceeding
the floor baseline by \(\Theta_A(nH)\), and expected energy
\(\Theta_A(WH)\).  Thus maximum entropy without exact-cover
anti-correlation is wrong by a factor \(\Theta(n)\).  More sharply, only
\(O(W/m)\) of its depth-one collision mass comes from middle-incompatible
pairs.  Any successful stationary law must create a further
\(W/2-O_A(W/\sqrt m)\) covariance deficit among already compatible pairs.
The missing estimate must therefore use global literal exact-completion
geometry, not merely delete forbidden row pairs.

Everything below is integral whenever an exact factor or heat cell is used.
The independent-subset calculation is explicitly marked as an analytic
benchmark, not an exact-factor counterexample.

---

## 1. Exact factors, floor energy, and stationary classes

Let \(\mathscr W_m\) be the set of unoriented wreaths and put

\[
M=|\mathscr W_m|=\frac{(n-1)!}{2}.
\]

An exact factor \(F\in\mathfrak F_m\) is a set of \(B\) wreaths whose
middle interval families partition \(\binom{[n]}m\).

For \(1\le q\le H\), write

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\]

where \(c_q=\lfloor\lambda_q\rfloor\) and
\(0\le\theta_q<1\).  Put

\[
b_q=W-c_qN_q=N_q\theta_q\in\mathbb Z.
\tag{Y5.6}
\]

For a factor \(F\), let \(\mu_q^F(S)\) be the number of its wreaths in
which the rank-\(r_q\) set \(S\) is a cyclic interval.  The full
floor-corrected energy is

\[
Q_q(F)
=\sum_{S\in\binom{[n]}{r_q}}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1),
\tag{Y5.7}
\]

\[
\mathcal Q_H(F)=\sum_{q=1}^{H}\frac{Q_q(F)}{c_q}.
\tag{Y5.8}
\]

Define the minimum integer pair count

\[
L_q
=(N_q-b_q)\binom{c_q}{2}
+b_q\binom{c_q+1}{2},
\tag{Y5.9}
\]

and

\[
\Lambda_H=\sum_{q=1}^{H}\frac{L_q}{c_q}.
\tag{Y5.10}
\]

Since every load vector has total \(W\), direct expansion gives

\[
\boxed{
Q_q(F)
=2\left[
\sum_S\binom{\mu_q^F(S)}2-L_q
\right].
}
\tag{Y5.11}
\]

For each transposition \(\tau\), uniform resampling of the complete sides
of every ownership component is an orthogonal projection \(K_\tau\).  The
original heat is

\[
K_{\rm tr}=\binom n2^{-1}\sum_\tau K_\tau.
\tag{Y5.12}
\]

Every communicating class \(\mathscr C\) is a union of complete
\(\tau\)-cells, is \(S_n\)-stable, and has the uniform law
\(\pi_{\mathscr C}\) as its unique stationary law.  The all-opposite corner
of a \(\tau\)-cell is \(\tau F\), so transpositions generate the asserted
\(S_n\)-stability.

### 1.1 Projection and stationary-law proof

Here is the complete finite-state justification of those assertions.  Fix
\(F\) and \(\tau\), and form the bipartite ownership multigraph between the
wreaths of \(F\) and those of \(\tau F\), with one edge for every middle
set.  Every wreath \(R\) has a \(\tau\)-fixed middle interval: if the two
coordinates exchanged by \(\tau\) were separated by every one of the \(n\)
middle intervals of \(R\), their total incidence would be \(n\), whereas it
is \(2m=n-1\).  Thus some interval contains both coordinates or neither.
It follows that \(R\) is joined to \(\tau R\).

For \(m\ge2\), \(R\ne\tau R\) as an unoriented cyclic order.  Indeed, the
stabilizer of an odd unoriented cycle is dihedral; a nontrivial rotation is
not a transposition, and a reflection has cycle type \(1\,2^m\).  Moreover,
\(F\cap\tau F=\varnothing\), because otherwise \(R,\tau R\in F\) would
share the preceding fixed middle interval.

If an ownership component has left side \(L_i\), its right side is exactly
\(\tau L_i\).  The inclusion \(\tau L_i\) in that right side follows from
the fixed-interval edges.  Equality follows because the ownership multigraph is
\(n\)-regular, so the two sides of every finite connected component have
equal cardinality.  Consequently all

\[
F_\varepsilon
=\bigcup_i
\begin{cases}
L_i,&\varepsilon_i=+1,\\
\tau L_i,&\varepsilon_i=-1
\end{cases}
\qquad(\varepsilon\in\{\pm1\}^k)
\tag{Y5.12a}
\]

are distinct literal exact factors.  Recomputing the overlay from any
corner merely interchanges the two sides of the switched components.
Thus these \(2^k\) factors form an intrinsic partition cell, and \(K_\tau\)
is uniform averaging on that cell.  In particular,

\[
K_\tau^2=K_\tau=K_\tau^*,
\tag{Y5.12b}
\]

so \(K_\tau\) is an orthogonal partition projection.

Every positive \(K_{\rm tr}\)-edge lies inside a communicating class, and
from any state every corner of each of its \(\tau\)-cells has positive
transition probability.  Hence every class is a union of complete cells.
The all-opposite corner is \(\tau F\), proving \(S_n\)-stability.  Symmetry
and the positive self-loops make the uniform class law stationary and the
finite irreducible class aperiodic, so this law is unique.  More generally,
the complete stationary invariant algebra is

\[
\ker(I-K_{\rm tr})=\bigcap_\tau\operatorname{Ran}K_\tau,
\tag{Y5.12c}
\]

because

\[
\langle u,(I-K_{\rm tr})u\rangle
=\binom n2^{-1}\sum_\tau\|(I-K_\tau)u\|_2^2.
\tag{Y5.12d}
\]

This characterizes the communicating classes exactly as the atoms on which
all common fixed functions are constant, although it does not provide a
more explicit combinatorial classification.

Finally, for any fixed rank-\(r_q\) target \(S\), let
\(Z_q=\mu_q^F(S)\) under \(\pi_{\mathscr C}\).  Class stability and target
transitivity give

\[
\mathbb E Z_q=\lambda_q.
\tag{Y5.12e}
\]

Expanding (Y5.7) therefore gives the exact integer-variance identity

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}Q_q
=N_q\left(\operatorname{Var}_{\pi_{\mathscr C}}Z_q
-\theta_q(1-\theta_q)\right).
}
\tag{Y5.12f}
\]

Thus class selection is equivalently a near-minimal integer-variance
problem.  Stationarity fixes the first moment in (Y5.12e), but gives no
upper bound on the class-dependent variance.

---

## 2. The exact conditional completion theorem

For a wreath \(R\), let \(\mathcal I_q(R)\) be its family of \(n\) cyclic
rank-\(r_q\) intervals.  For distinct wreaths \(R,D\), put

\[
h_q(R,D)=|\mathcal I_q(R)\cap\mathcal I_q(D)|,
\qquad
g_H(R,D)=\sum_{q=1}^{H}\frac{h_q(R,D)}{c_q}.
\tag{Y5.13}
\]

For a communicating class \(\mathscr C\), define the literal completion
counts

\[
d_{\mathscr C}(R)
=|\{F\in\mathscr C:R\in F\}|,
\tag{Y5.14}
\]

\[
d_{\mathscr C}(R,D)
=|\{F\in\mathscr C:R,D\in F\}|.
\tag{Y5.15}
\]

If \(R,D\) share a middle interval, then
\(d_{\mathscr C}(R,D)=0\) by exact ownership.

Because \(\mathscr C\) is \(S_n\)-stable and \(S_n\) is transitive on
wreaths,

\[
d_{\mathscr C}(R)=\frac{|\mathscr C|B}{M}>0
\tag{Y5.16}
\]

for every \(R\).  Define

\[
\mathsf G_H(\mathscr C;R)
=\frac1{d_{\mathscr C}(R)}
\sum_{D\ne R}d_{\mathscr C}(R,D)g_H(R,D).
\tag{Y5.17}
\]

This is exactly

\[
\mathbb E_{F\sim\pi_{\mathscr C}}
\left[
\sum_{D\in F\setminus\{R\}}g_H(R,D)
\ \middle|\ R\in F
\right].
\tag{Y5.18}
\]

Equivariance of the completion counts and of \(g_H\) makes (Y5.17)
independent of \(R\); write it as \(\mathsf G_H(\mathscr C)\).

### Theorem 2.1: exact stationary completion identity

For every original heat class \(\mathscr C\),

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
=B\mathsf G_H(\mathscr C)-2\Lambda_H.
}
\tag{Y5.19}
\]

#### Proof

For a fixed factor and depth,

\[
\sum_S\binom{\mu_q^F(S)}2
=\sum_{\{R,D\}\subseteq F}h_q(R,D),
\]

because both sides count a target together with an unordered pair of its
wreath owners.  Weighting in \(q\) gives

\[
\mathcal Q_H(F)
=2\sum_{\{R,D\}\subseteq F}g_H(R,D)-2\Lambda_H
\tag{Y5.20}
\]

by (Y5.11).

Average the first term in (Y5.20) over \(F\in\mathscr C\), and count it by
an ordered distinguished first wreath:

\[
\begin{aligned}
\mathbb E_{\pi_{\mathscr C}}
\sum_{\{R,D\}\subseteq F}g_H(R,D)
&=\frac1{2|\mathscr C|}
\sum_R\sum_{D\ne R}
d_{\mathscr C}(R,D)g_H(R,D)\\
&=\frac1{2|\mathscr C|}
\sum_Rd_{\mathscr C}(R)\mathsf G_H(\mathscr C)\\
&=\frac B2\mathsf G_H(\mathscr C),
\end{aligned}
\]

where the last line uses
\(\sum_Rd_{\mathscr C}(R)=|\mathscr C|B\).  Substitute in (Y5.20).
\(\square\)

### Corollary 2.2: exact stationary-selection equivalence

Put

\[
\Theta_H
=\min_{\mathscr C}
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H.
\]

Every stationary law is a convex combination of the class-uniform laws,
so also

\[
\Theta_H
=\min_{\pi K_{\rm tr}=\pi}\mathbb E_\pi\mathcal Q_H.
\tag{Y5.20a}
\]

Then

\[
\boxed{
\Theta_H
=B\left(
\min_{\mathscr C}\mathsf G_H(\mathscr C)
-\frac{2\Lambda_H}{B}
\right).
}
\tag{Y5.21}
\]

Thus \(\Theta_H=O_A(HB)\) is equivalent, with the same constant, to an
additive \(O_A(H)\) bound above the conditional completion baseline.

### Theorem 2.3: deterministic literal spill-deficit identity

There is a pointwise exact-cover form of the preceding pair count.  Write
\(\mathcal I_0(D)\) for the middle intervals of a wreath \(D\).  For a
rank-\((m-q)\) set \(S\), define

\[
a_{q,S}(D)
=\#\{X\in\mathcal I_0(D):S\subseteq X\},
\tag{Y5.21a}
\]

\[
\rho_{q,S}(D)
=a_{q,S}(D)
-(q+1)\mathbf1_{\{S\in\mathcal I_q(D)\}}.
\tag{Y5.21b}
\]

For every \(D,S\),

\[
0\le\rho_{q,S}(D)\le q.
\tag{Y5.21c}
\]

Indeed, complementation identifies the middle intervals of \(D\) which
contain \(S\) with the cyclic \((m+1)\)-intervals of \(D\) contained in
\([n]\setminus S\).  The latter set has size \(m+q+1<2(m+1)\), so at most
one of its cyclic runs can have length at least \(m+1\), and it contributes
at most \(q+1\) such intervals.  Equality occurs exactly when the complement
is one run, equivalently when \(S\in\mathcal I_q(D)\); in that case the
subtraction in (Y5.21b) leaves zero.  Otherwise
\(\rho_{q,S}(D)=a_{q,S}(D)\le q\).

Now fix a literal exact factor \(F\), a row \(R\in F\), and
\(S\in\mathcal I_q(R)\).  There are exactly

\[
C_q^*=\binom{m+q+1}{q}
\tag{Y5.21d}
\]

middle sets containing \(S\), of which exactly \(q+1\) are owned by
\(R\).  Exact ownership of every remaining middle set, followed by
(Y5.21b), gives the deterministic identity

\[
\boxed{
\begin{aligned}
&(q+1)
\#\{D\in F\setminus\{R\}:S\in\mathcal I_q(D)\}\\
&\qquad+
\sum_{D\in F\setminus\{R\}}\rho_{q,S}(D)
=C_q^*-(q+1).
\end{aligned}
}
\tag{Y5.21e}
\]

Thus every middle window of another owner which contains \(S\) without
realizing \(S\) as that owner's own lower interval is recorded by a
nonnegative, bounded, literal spill.

Define the total directed spill

\[
\Sigma_q(F)
=\sum_{R\in F}\sum_{D\in F\setminus\{R\}}
\sum_{S\in\mathcal I_q(R)}\rho_{q,S}(D).
\tag{Y5.21f}
\]

Summing (Y5.21e) first over the \(n\) lower intervals of \(R\), then over
the \(B\) choices of \(R\), gives

\[
2(q+1)\sum_S\binom{\mu_q^F(S)}2+\Sigma_q(F)
=Bn\bigl(C_q^*-(q+1)\bigr).
\tag{Y5.21g}
\]

Set the universal floor-compatible spill ceiling

\[
\Sigma_q^{\max}
=Bn\bigl(C_q^*-(q+1)\bigr)-2(q+1)L_q.
\tag{Y5.21h}
\]

Combining (Y5.21g) with (Y5.11) proves the lossless integral formula

\[
\boxed{
(q+1)Q_q(F)=\Sigma_q^{\max}-\Sigma_q(F).
}
\tag{Y5.21i}
\]

In particular, \(\Sigma_q(F)\le\Sigma_q^{\max}\) for every literal exact
factor, with equality exactly when \(Q_q(F)=0\).  At all depths together,

\[
\boxed{
\mathcal Q_H(F)
=\sum_{q=1}^{H}
\frac{\Sigma_q^{\max}-\Sigma_q(F)}{c_q(q+1)}.
}
\tag{Y5.21j}
\]

This theorem converts any literal spill estimate directly and without loss
into the coefficient-one energy scale.  In particular, the stationary
target is exactly equivalent to finding a stationary law \(\pi\) satisfying

\[
\sum_{q=1}^{H_A}
\frac{\Sigma_q^{\max}-\mathbb E_\pi\Sigma_q(F)}{c_q(q+1)}
\le C_AH_AB.
\tag{Y5.21k}
\]

For a class, put

\[
\overline\Sigma_q(\mathscr C)
=\frac1B\mathbb E_{\pi_{\mathscr C}}\Sigma_q(F).
\tag{Y5.21l}
\]

The ordered-row version of (Y5.21g) gives the exact bridge to the
completion statistic:

\[
\boxed{
(q+1)\mathsf G_q(\mathscr C)
+\overline\Sigma_q(\mathscr C)
=n\bigl(C_q^*-(q+1)\bigr),
}
\tag{Y5.21m}
\]

where
\(\mathsf G_q(\mathscr C)=d_{\mathscr C}(R)^{-1}
\sum_{D\ne R}d_{\mathscr C}(R,D)h_q(R,D)\).
At depth one this reads

\[
2\mathsf G_1(\mathscr C)+\overline\Sigma_1(\mathscr C)=nm.
\tag{Y5.21n}
\]

Here the aggregate ceiling is exactly

\[
\Sigma_1^{\max}
=Wm-\frac{8W}{m+2}.
\tag{Y5.21o}
\]

Consequently a stationary law with
\(\mathbb E\mathcal Q_{H_A}\le C_AH_AB\) must already satisfy

\[
0\le\Sigma_1^{\max}-\mathbb E\Sigma_1(F)
=2\mathbb E Q_1
\le2C_AH_AB
=O_A(W/\sqrt m).
\tag{Y5.21p}
\]

Since \(\Sigma_1^{\max}=\Theta(Wm)\), this is relative
\(O_A(m^{-3/2})\) accuracy at depth one.

The identity itself supplies no lower bound placing the expected spill near
its ceiling; that is the remaining positive geometric input.

### 2.4 Exact baseline and first depth

Using \(b_q=N_q\theta_q\), equation (Y5.9) becomes

\[
L_q
=\frac{N_qc_q}{2}(c_q-1+2\theta_q).
\tag{Y5.22}
\]

Therefore

\[
\frac{2L_q}{Bc_q}
=n\frac{c_q+2\theta_q-1}{c_q+\theta_q},
\tag{Y5.23}
\]

which proves (Y5.3).

For fixed \(A>0\), the exact product for \(W/N_q\) gives, uniformly for
\(q\le A\sqrt m+1\),

\[
\log\lambda_q=\frac{q(q+1)}{m}+O_A(m^{-1/2}).
\]

This also gives a discontinuity-free quantitative bound.  For all
sufficiently large \(m=m(A)\) and all
\(\lceil H_A/2\rceil\le q\le H_A\),

\[
1+\eta_A\le\lambda_q\le T_A,
\qquad
\eta_A=e^{A^2/8}-1,
\qquad
T_A=e^{A^2+1}.
\tag{Y5.23a}
\]

If \(c_q=1\), the summand in (Y5.23) divided by \(n\) is at least
\(2\eta_A/T_A\); if \(c_q\ge2\), it is at least \(1/T_A\).  It is always
at most one.  Therefore, with

\[
\delta_A=\frac{\min\{2\eta_A,1\}}{T_A}>0,
\]

\[
\frac{\delta_A}{2}nH_A
\le\frac{2\Lambda_{H_A}}B
\le nH_A
\tag{Y5.23b}
\]

for all sufficiently large \(m\).  In particular,

\[
\frac{2\Lambda_{H_A}}B=\Theta_A(nH_A).
\tag{Y5.23c}
\]

At \(q=1\),

\[
N_1=\binom n{m-1},\qquad
\lambda_1=\frac{m+2}{m}=1+\frac2m,
\]

so \(c_1=1\), \(\theta_1=2/m\), and (Y5.23) gives (Y5.4).

Nonnegativity of \(\mathcal Q_H\) also recovers the universal lower bound

\[
\mathsf G_H(\mathscr C)\ge\frac{2\Lambda_H}{B}.
\tag{Y5.24}
\]

The target is to find one class within additive \(C_AH\) of equality.

---

## 3. A global exact-completion theorem would suffice

Let \(\mathfrak F_m\) itself replace \(\mathscr C\) in
(Y5.14)--(Y5.17), and write the resulting completion ratio as
\(\mathsf G_H^{\rm all}\).  The uniform law on the whole fibre is
stationary, because it is a size-weighted mixture of the uniform laws on
the communicating classes.  Equivalently, every \(K_\tau\) is doubly
stochastic.

### Corollary 3.1: global completion-count selection

If

\[
\boxed{
\mathsf G_{H_A}^{\rm all}
\le\frac{2\Lambda_{H_A}}B+C_AH_A,
}
\tag{GCC_A}
\]

then some original communicating class satisfies

\[
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_{H_A}
\le C_AH_AB.
\tag{Y5.25}
\]

#### Proof

Theorem 2.1 applied to the whole-fibre stationary law gives mean at most
\(C_AH_AB\).  This mean is a size-weighted average of the class means, so
one class is no larger. \(\square\)

Statement \((\mathrm{GCC}_A)\) is a literal counting theorem.  It asks for
the weighted average of \(g_H(R,D)\) under the exact conditional completion
probabilities

\[
\frac{d_{\mathfrak F_m}(R,D)}{d_{\mathfrak F_m}(R)}.
\]

These probabilities have an exact conditioning interpretation.  Let
\(U_B\) be the uniform law on all \(B\)-subsets of \(\mathscr W_m\), and
let \(\mathcal E_m\) be the event that their middle supports are pairwise
disjoint.  Each selected wreath owns \(n\) middle sets and \(Bn=W\), so

\[
\mathcal E_m
\iff \text{the selected wreaths form a literal exact factor}.
\tag{Y5.25a}
\]

Therefore the uniform whole-fibre law is exactly

\[
U_{\mathfrak F_m}=U_B(\,\cdot\mid\mathcal E_m).
\tag{Y5.25b}
\]

For every middle-compatible pair \(R,D\), Bayes' rule gives

\[
\boxed{
\frac{d_{\mathfrak F_m}(R,D)}{d_{\mathfrak F_m}(R)}
=\frac{B-1}{M-1}
\frac{\Pr_{U_B}(\mathcal E_m\mid R,D)}
{\Pr_{U_B}(\mathcal E_m\mid R)}.
}
\tag{Y5.25c}
\]

Thus \((\mathrm{GCC}_A)\) is precisely a weighted suppression theorem for
the literal completion ratios in (Y5.25c), not an appeal to an abstract
dependent distribution.

It is **unproved**.  Unlike a covariance ansatz, every number appearing in
it counts completed squarefree exact factors.

---

## 4. Maximum-entropy row sampling misses by a factor \(n\)

This section is an analytic no-go benchmark, not an exact-factor model.
Choose a uniform \(B\)-subset of the \(M\) wreaths, conditional on containing
a fixed wreath \(R\), and ignore middle collisions.

For fixed \(q\), double counting incidences of wreaths with rank-\(r_q\)
targets gives

\[
|\{D:S\in\mathcal I_q(D)\}|=\frac{Mn}{N_q}.
\]

Consequently,

\[
\sum_Dh_q(R,D)=\frac{Mn^2}{N_q},
\qquad h_q(R,R)=n.
\tag{Y5.26}
\]

The conditional expected overlap of the uniform subset is therefore

\[
\boxed{
\mathsf G_H^{\rm sub}
=\frac{B-1}{M-1}
\sum_{q=1}^{H}\frac1{c_q}
\left(\frac{Mn^2}{N_q}-n\right).
}
\tag{Y5.27}
\]

For fixed \(A\), uniformly on \(q\le H_A\), the numbers
\(c_q\) and \(\lambda_q\) are bounded above by constants depending only on
\(A\), while \(c_q\ge1\).  Since \(B/M\to0\) superexponentially relative
to the present scales, (Y5.27) gives

\[
\mathsf G_H^{\rm sub}
=n\sum_{q=1}^{H}\frac{c_q+\theta_q}{c_q}
+o_A(nH).
\tag{Y5.28}
\]

Subtracting (Y5.3), the contribution at depth \(q\) is

\[
n\left[
\frac{c_q+\theta_q}{c_q}
-\frac{c_q+2\theta_q-1}{c_q+\theta_q}
\right]
=n\frac{c_q+\theta_q^2}{c_q(c_q+\theta_q)}.
\tag{Y5.29}
\]

The last factor lies between two positive constants depending only on
\(A\).  Hence

\[
\boxed{
\mathsf G_{H_A}^{\rm sub}
-\frac{2\Lambda_{H_A}}B
=\Theta_A(nH_A),
}
\tag{Y5.30}
\]

and the corresponding expected energy is

\[
\boxed{
\mathbb E\mathcal Q_{H_A}^{\rm sub}
=\Theta_A(BnH_A)=\Theta_A(WH_A).
}
\tag{Y5.31}
\]

At depth one alone,

\[
\mathsf G_1^{\rm sub}=n+o(n),
\qquad
\mathbb E Q_1^{\rm sub}=(1+o(1))W.
\tag{Y5.32}
\]

Thus maximum-entropy row sampling is too large by a factor \(\Theta(n)\)
relative to \(H_AB\).  A successful entropy argument must prove that exact
middle completion suppresses the conditional lower-overlap excess from
\(\Theta_A(nH)\) to \(O_A(H)\); entropy or wreath transitivity alone does
not do so.

### 4.1 Pairwise middle exclusion removes only \(O(W/m)\)

The preceding benchmark can be sharpened: almost all of its depth-one
collision mass already lies on pairs of wreaths which are mutually
compatible at the middle rank.

Fix \(S\in\binom{[n]}{m-1}\), and let

\[
\mathscr O_S
=\{R\in\mathscr W_m:S\in\mathcal I_1(R)\}.
\]

For a middle set \(X\), put \(d=|S\setminus X|\).  There are

\[
M_d=\binom{m-1}{d}\binom{m+2}{d+1}
\tag{Y5.32a}
\]

such middle sets.  A wreath in \(\mathscr O_S\) contains exactly

\[
\nu_d=
\begin{cases}
2,&0\le d\le m-2,\\
3,&d=m-1
\end{cases}
\tag{Y5.32b}
\]

middle sets in the \(d\)-class.  Indeed, place \(S\) as one consecutive
block of length \(m-1\).  A middle window meeting that block in a prescribed
positive size crosses either its left or right boundary, while a middle
window disjoint from \(S\) lies in the complementary block of length
\(m+2\) and has three positions.

The stabilizer of \(S\) is transitive on each \(d\)-class.  Hence two
independent uniform wreaths in \(\mathscr O_S\) have expected number of
common middle intervals

\[
\chi_m
=\sum_{d=0}^{m-1}\frac{\nu_d^2}{M_d}.
\tag{Y5.32c}
\]

Their probability of being middle-incompatible is at most \(\chi_m\).
Now

\[
M_0=m+2,\qquad
M_d\ge\binom{m+2}{2}\quad(1\le d\le m-1),
\]

so

\[
\begin{aligned}
\chi_m
&\le\frac4{m+2}
+\frac{4m+1}{\binom{m+2}{2}}\\
&\le\frac{13}{m}.
\end{aligned}
\tag{Y5.32d}
\]

For the uniform \(B\)-subset law, put

\[
p=\frac BM,\qquad
\alpha_m=\frac{M(B-1)}{B(M-1)}.
\]

Thus a fixed distinct pair has inclusion probability
\(\alpha_mp^2\).  Let \(I_{\rm comp}^{(B)}\) be its expected depth-one
collision count restricted to pairs with disjoint middle supports, counted
once for every shared \((m-1)\)-target.  Since
\(|\mathscr O_S|p=\lambda_1\), the total collision count is

\[
\frac{\alpha_mW}{2}(\lambda_1-p),
\]

while (Y5.32d) bounds the incompatible part by

\[
\frac{\alpha_mW\lambda_1\chi_m}{2}.
\]

Therefore

\[
\boxed{
I_{\rm comp}^{(B)}
\ge
\frac{\alpha_mW}{2}
(\lambda_1-p-\lambda_1\chi_m)
=\frac W2-O(W/m).
}
\tag{Y5.32e}
\]

The unrestricted collision count is \(W/2+O(W/m)\), so the matching
trivial upper bound also gives

\[
I_{\rm comp}^{(B)}=\frac W2+O(W/m).
\]

Now let \(\pi\) be any stationary law of the genuine heat chain.  It is a
mixture of class-uniform laws, hence is \(S_n\)-invariant and has wreath
marginal \(p\).  All of its selected pairs are middle-compatible.  Its
depth-one collision count is exactly

\[
J_\pi
=\mathbb E_\pi\sum_S\binom{\mu_1(S)}2
=\frac{2W}{m+2}+\frac12\mathbb E_\pi Q_1.
\tag{Y5.32f}
\]

Define the compatible covariance deficit relative to the uniform
fixed-cardinality law by

\[
\Delta_{\rm comp}(\pi)=I_{\rm comp}^{(B)}-J_\pi.
\]

Equations (Y5.32d)--(Y5.32f) give the explicit inequality

\[
\boxed{
\begin{aligned}
\Delta_{\rm comp}(\pi)
\ge{}&
\frac{\alpha_mW}{2}
\left(
\frac{m+2}{m}-p-\frac{13(m+2)}{m^2}
\right)\\
&-\frac{2W}{m+2}
-\frac12\mathbb E_\pi Q_1.
\end{aligned}
}
\tag{Y5.32g}
\]

Consequently, if

\[
\mathbb E_\pi\mathcal Q_{H_A}\le C_AH_AB,
\]

then

\[
\boxed{
\Delta_{\rm comp}(\pi)
\ge\frac W2-O_A(W/\sqrt m).
}
\tag{Y5.32h}
\]

Pairwise middle exclusion itself therefore removes only \(O(W/m)\) from
the maximum-entropy collision mass.  A successful stationary law must
create additional negative covariance of asymptotic size \(W/2\) among
pairs which are already fully compatible with exact middle ownership.  In
particular,

\[
\Delta_{\rm comp}(\pi_m)=o(W)
\quad\Longrightarrow\quad
\mathbb E_{\pi_m}Q_1=(1+o(1))W,
\tag{Y5.32i}
\]

which rules out any maximum-entropy or weak-conditioning proof that changes
only \(o(W)\) compatible collision mass.  This is not a no-go for global
exact completion: such completion is precisely the possible source of the
required order-\(W\) covariance deficit.

---

## 5. Exact transfer from augmented projection heat

Let \(\{K_\alpha\}_{\alpha\in I}\) be any finite family of orthogonal
partition projections on \(\mathfrak F_m\), containing every original
\(K_\tau\), and let

\[
K_{\rm aug}=\sum_{\alpha\in I}a_\alpha K_\alpha,
\qquad a_\alpha>0,\qquad\sum_\alpha a_\alpha=1.
\tag{Y5.33}
\]

This includes the intrinsic transposition/3-cycle/double-transposition
short heat.

### Theorem 5.1: projection-augmentation transfer

Every \(K_{\rm aug}\)-stationary law is stationary under every
\(K_\alpha\) separately, hence under \(K_{\rm tr}\).  Every augmented
communicating class \(\mathscr D\) is a disjoint union of original classes,
and

\[
\boxed{
\pi_{\mathscr D}
=\sum_{\mathscr C\subseteq\mathscr D}
\frac{|\mathscr C|}{|\mathscr D|}\pi_{\mathscr C}.
}
\tag{Y5.34}
\]

Consequently,

\[
\boxed{
\min_{\mathscr C}
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_H
\le
\min_{\mathscr D}
\mathbb E_{\pi_{\mathscr D}}\mathcal Q_H.
}
\tag{Y5.35}
\]

#### Proof

For a stationary density \(u\) relative to counting measure, symmetry gives
\(K_{\rm aug}u=u\).  Since each \(K_\alpha\) is an orthogonal projection,

\[
0
=\langle u,(I-K_{\rm aug})u\rangle
=\sum_\alpha a_\alpha\|(I-K_\alpha)u\|_2^2.
\]

Every summand vanishes, proving separate invariance.

Graphically, every original cell edge is an augmented edge, so every
original class lies inside one augmented class.  Uniform measure on the
larger class disintegrates by cardinality, proving (Y5.34).  Its energy is
the corresponding convex combination of original class means, which gives
(Y5.35). \(\square\)

This theorem proves that a Catalan-scale stationary estimate for the short
heat is a valid, stronger sufficient route to the original theorem.  It
does not create the estimate: augmented-class averaging cannot be smaller
than every old-class mean.

The inclusion of every \(K_\tau\) is essential.  A standalone even or
long-involution heat need not have stationary densities fixed by the
original projections merely because its coordinate permutations generate a
large group.

---

## 6. Exact stationary correlation tax on a transposition cell

Fix a transposition \(\tau\) and one intrinsic cell \(\mathscr D\).  Let
its ownership components have exact move vectors \(g_1,\ldots,g_k\), and
let

\(A_{r_q}\) denote wreath-to-rank-\(r_q\) cyclic-interval incidence.  Put

\[
T_Hx
=\left(c_q^{-1/2}A_{r_q}x\right)_{q=1}^{H},
\qquad V_i=T_Hg_i.
\tag{Y5.36}
\]

Every cell corner is a literal exact factor

\[
x(s)=\bar x+\frac12\sum_{i=1}^ks_ig_i,
\qquad s\in\{\pm1\}^k.
\tag{Y5.37}
\]

The midpoint lower profile is \(\tau\)-invariant and every \(V_i\) is
\(\tau\)-anti-invariant.  Therefore, for one cell-dependent constant
\(C_{\mathscr D}\),

\[
\boxed{
\mathcal Q_H(x(s))
=C_{\mathscr D}
+\frac14\left\|\sum_i s_iV_i\right\|_2^2.
}
\tag{Y5.38}
\]

Put

\[
S_{\mathscr D}=\sum_i\|V_i\|_2^2,
\qquad
\Delta_{\mathscr D}
=\min_{\varepsilon\in\{\pm1\}^k}
\left\|\sum_i\varepsilon_iV_i\right\|_2^2.
\tag{Y5.39}
\]

### Theorem 6.1: stationary correlation tax

The unique \(K_\tau\)-stationary conditional law on \(\mathscr D\) is the
uniform law \(U_{\mathscr D}\), and

\[
\boxed{
\mathbb E_{U_{\mathscr D}}\mathcal Q_H
=C_{\mathscr D}+\frac14S_{\mathscr D}.
}
\tag{Y5.40}
\]

Among all probability laws on the cell which preserve the midpoint wreath
marginals, the optimum is uniform on one antipodal pair
\(\{x(\varepsilon),x(-\varepsilon)\}\), and its mean is

\[
\boxed{
C_{\mathscr D}+\frac14\Delta_{\mathscr D}.
}
\tag{Y5.41}
\]

Thus imposing stationarity costs exactly

\[
\boxed{
\mathsf T_{\mathscr D}
=\frac14(S_{\mathscr D}-\Delta_{\mathscr D})\ge0.
}
\tag{Y5.42}
\]

#### Proof

Equation (Y5.38) follows by orthogonality of the invariant midpoint and
anti-invariant effects.  The linear part of \(\mathcal Q_H\) is constant on
the cell because every corner has total rank-\(r_q\) incidence \(W\) at
each depth.  Under \(U_{\mathscr D}\), the signs are independent
fair bits, so all cross terms vanish and

\[
\mathbb E_s\left\|\sum_i s_iV_i\right\|^2
=\sum_i\|V_i\|^2.
\]

For an arbitrary midpoint-preserving sign law, symmetrize it under
\(s\mapsto-s\).  Its sign second-moment matrix is a convex combination of
the matrices \(\varepsilon\varepsilon^{\mathsf T}\).  The expected squared
norm is linear in that matrix, so an optimum is achieved by one antipodal
pair.  This proves (Y5.40)--(Y5.42). \(\square\)

There is an equivalent nonnegative three-term decomposition.  Let
\(t_{q,S}=2\bar\mu_q(S)\), the integer sum of the two loads at
\((q,S)\) in any antipodal pair of cell corners.  For integers \(a,t\ge0\),
put

\[
e_a(z)=\frac12(z-a)(z-a-1),
\qquad
b_a(t)=\min_{r+s=t}\bigl(e_a(r)+e_a(s)\bigr).
\tag{Y5.42a}
\]

The balanced split gives

\[
b_a(t)
=e_a(\lfloor t/2\rfloor)+e_a(\lceil t/2\rceil)
=\left\lfloor\frac{(t-2a-1)^2}{4}\right\rfloor.
\tag{Y5.42b}
\]

Define the immutable weighted pair-sum floor and weighted parity count by

\[
\mathfrak P_{\mathscr D}
=\frac12\sum_{q=1}^{H}\frac1{c_q}
\sum_{S}b_{c_q}(t_{q,S}),
\qquad
O_{\mathscr D}
=\sum_{q=1}^{H}\frac1{c_q}
\#\{S:t_{q,S}\text{ is odd}\}.
\tag{Y5.42c}
\]

If \(d=2z-t\), direct substitution gives

\[
e_a\left(\frac{t+d}{2}\right)
+e_a\left(\frac{t-d}{2}\right)
=b_a(t)+\frac14\bigl(d^2-\mathbf1_{\{t\text{ odd}\}}\bigr).
\tag{Y5.42d}
\]

Summing this scalar integer-variance identity gives

\[
\boxed{
\mathbb E_{U_{\mathscr D}}\mathcal Q_H
=2\mathfrak P_{\mathscr D}
+\frac14(\Delta_{\mathscr D}-O_{\mathscr D})
+\frac14(S_{\mathscr D}-\Delta_{\mathscr D}).
}
\tag{Y5.43}
\]

All three terms are nonnegative: \(b_a(t)\ge0\), parity forces
\(d^2\ge\mathbf1_{\{t\text{ odd}\}}\) at every target and hence
\(\Delta_{\mathscr D}\ge O_{\mathscr D}\), and averaging the squared norm
over independent fair signs gives
\(\Delta_{\mathscr D}\le S_{\mathscr D}\).  Conditional on every
\(\tau\)-cell, a
stationary class law is exactly \(U_{\mathscr D}\).  Hence (Y5.43), averaged
with weights \(|\mathscr D|/|\mathscr C|\), is an exact class ledger for
every fixed \(\tau\).

The first two terms are precisely what target-specific Graver covariance
routing optimizes.  Even a Catalan-scale bound on that antipodal optimum
leaves the independent necessary gate

\[
\mathbb E_{\mathscr D\subseteq\mathscr C}
(S_{\mathscr D}-\Delta_{\mathscr D})
=O_A(HB).
\tag{Y5.44}
\]

No such estimate follows from covariance routing.  Applying \(K_\tau\) to
the optimizing antipodal law makes it uniform on the cell in one step and
raises its expected full energy by exactly (Y5.42).

There is a separate support issue.  For arbitrary exact factors \(F,G\),
their comparison cube is integral, but its hybrid corners need not lie in
the original heat class containing \(F,G\).  The identity

\[
x_F+x_G=x_{H_I}+x_{H_{I^c}}
\]

preserves wreath marginals, not nonlinear communicating-class indicators.
Thus arbitrary comparison-face covariance has both a heat-class support
gate and, on genuine transposition faces, the stationary tax (Y5.42).

---

## 7. Exact remaining theorem and implication to coefficient one

The stationary lane is now equivalent to the following literal completion
statement.

> **Stationary conditional completion selection \((\mathrm{SCC}_A)\) —
> UNPROVED.**  For every fixed \(A>0\), there is \(C_A<\infty\) such that,
> for all sufficiently large \(m\), some original heat class \(\mathscr C\)
> satisfies
> \[
> \boxed{
> \mathsf G_{H_A}(\mathscr C)
> \le
> n\sum_{q=1}^{H_A}
> \frac{c_q+2\theta_q-1}{c_q+\theta_q}
> +C_AH_A.
> }
> \tag{SCC_A}

By Theorem 2.1, \((\mathrm{SCC}_A)\) is exactly equivalent to

\[
\min_{\mathscr C}
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_{H_A}
=O_A(H_AB).
\tag{Y5.45}
\]

If it holds, averaging selects a literal exact factor \(F\) in that class
with

\[
\mathcal Q_{H_A}(F)=O_A(H_AB).
\]

Let \(\mathcal B_q\) be the balanced integer quota vectors having exactly
\(b_q\) coordinates \(c_q+1\) and all remaining coordinates \(c_q\), and
define the true unlabelled overload by

\[
O_q(F)=\frac12\min_{b\in\mathcal B_q}\|\mu_q^F-b\|_1,
\qquad
\mathcal O_H(F)=\sum_{q=1}^{H}\frac{O_q(F)}{c_q}.
\tag{Y5.45a}
\]

The exact overload inequality gives

\[
\mathcal O_{H_A}(F)
\le\frac12\mathcal Q_{H_A}(F)
=O_A(H_AB),
\tag{Y5.46}
\]

and

\[
\frac{H_AB}{W}=\frac{H_A}{n}=O_A(m^{-1/2})=o_A(1).
\tag{Y5.47}
\]

Thus \((\mathrm{SCC}_A)\) for every fixed \(A\), followed by the frozen
diagonalization, proves

\[
\boxed{
\nu(k)\le(1+o(1))W(k).
}
\tag{Y5.48}
\]

This implication is unlabelled and remains inside one completed exact factor
before the literal OR word is produced by the frozen reduction.  No labelled
common-owner synchronization is claimed.

---

## 8. Audit and exact status

The decisive double count was checked in both orientations:

* target first: \(\sum_S\binom{\mu_q(S)}2\);
* wreath pair first: \(\sum_{\{R,D\}\subset F}h_q(R,D)\).

The factor \(B/2\) in the class average and the factor two in the full
energy (Y5.11) are both essential.  They yield \(B\mathsf G_H\), not
\(2B\mathsf G_H\) or \(B\mathsf G_H/2\).

The following scope points are also essential.

1. The completion counts in Theorem 2.1 count literal squarefree exact
   factors.  They are not signed-lattice completion numbers.

2. The whole-fibre criterion \((\mathrm{GCC}_A)\) is sufficient, whereas
   the minimum-class criterion \((\mathrm{SCC}_A)\) is equivalent to the
   stationary target.

3. The uniform-subset calculation violates exact middle ownership.  It is
   a no-go for unconditioned entropy, not a counterexample to
   \((\mathrm{SCC}_A)\).

4. The compatible-pair refinement is stronger than merely observing that
   exact factors exclude middle collisions: (Y5.32h) proves that exclusion
   accounts for only \(O(W/m)\) of the required order-\(W\) covariance
   correction.  It remains a no-go for weak conditioning, not for global
   exact completion.

5. Short-permutation transfer requires the augmented projection family to
   include every original transposition projection with positive weight.

6. The antipodal Graver optimizer is literal and integral on its comparison
   face, but arbitrary comparison faces need not remain inside one original
   heat class.  On a genuine transposition cell, stationarity forces the
   uniform signs and pays (Y5.42).

7. No high-energy transposition-rigid exact family is constructed.  Such a
   family would obstruct an every-class theorem, but not by itself the
   existence of some other low class.

The proved advances are therefore:

* the exact completion-count identity (Y5.19) and equivalence (Y5.21);
* the deterministic integral spill-deficit identity
  (Y5.21e)--(Y5.21j);
* the explicit baseline (Y5.3), including the depth-one constant (Y5.4);
* the global exact-completion sufficient theorem \((\mathrm{GCC}_A)\);
* the factor-\(n\) maximum-entropy no-go (Y5.30)--(Y5.32);
* the compatible-pair \(13/m\) overlap bound and order-\(W\) covariance
  deficit gate (Y5.32d)--(Y5.32i);
* projection-augmentation transfer (Y5.34)--(Y5.35); and
* the exact stationary correlation tax (Y5.42)--(Y5.44).

The completion double count, baseline constants, entropy asymptotics,
projection transfer, and stationary-tax normalizations were independently
audited.  A separate completion audit independently derived
(Y5.21e)--(Y5.21j) directly from exact middle ownership and checked its
constants.  Another audit recomputed (Y5.32a)--(Y5.32h), including the
endpoint multiplicity \(\nu_{m-1}=3\), the constant \(13/m\), every factor
of \(1/2\), and the final \(W/2-O_A(W/\sqrt m)\) deficit; it found no
correction.

The existence of a stationary class with expected excess \(O_A(H_AB)\)
remains unproved.  It is neither a consequence of reversibility nor of the
short-permutation or long-involution coherent spectra.  The exact missing
positive statement is now the literal conditional completion estimate
\((\mathrm{SCC}_A)\), equivalently the near-ceiling spill estimate
(Y5.21k), or the stronger all-fibre count \((\mathrm{GCC}_A)\).
