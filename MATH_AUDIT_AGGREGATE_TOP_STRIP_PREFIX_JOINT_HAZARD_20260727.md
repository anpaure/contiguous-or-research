# Audit of the aggregate top-strip prefix joint hazard

Date: 2026-07-27

Scope: compensated repaired-ring first moments and the proposed
top-strip quarantine.

## 0. Verdict

The quarantine arithmetic after the mixed-type comparison is valid, but
the comparison itself is not proved by the sign of the terminal term.
If the reference includes prefix survival, the negative prefix-death
term must be retained and paired with that reference derivative.

For an equality-resolved prefix resource union $P$ and the genuinely
new last-row resources $R(f)$, the exact shared-event correction is

\[
 \Xi_t(P,R(f))
 :=\nu_t\left|
       \mathcal E_t(P)\cap\mathcal E_t(R(f))
       \right|.                                                 \tag{0.1}
\]

The exact joint hazard is

\[
 \Lambda_t(P\cup R(f))
 =\Lambda_t(P)+\Lambda_t(R(f))-\Xi_t(P,R(f)).                   \tag{0.2}
\]

Consequently the proposed uniform integrated $o(1)$ error is
equivalent, after the already audited individual first-moment errors,
to an incidence-weighted $o(1)$ bound on (0.1).  It does not follow
from marginal compensation, from $\mathsf K_C\le0$, or from the
time-zero mixed-diagram estimate.

A regular compensated hypergraph example in Section 4 has normalized
cross hazard

\[
                         \int_0^T\Xi_t^{\rm FM}\,dt
                         =\log(1/z),                            \tag{0.3}
\]

which is $(1/20)\log m$ at $z=m^{-1/20}$.  Thus a uniform
statewise $o(1)$ theorem is false under the stated first-moment inputs.
No literal repaired-promotion-ring counterexample is asserted; ruling
out this concentration there is exactly the missing aggregate
cross-prefix hazard estimate.

## 1. Exact compensated set hazard

For an active vertex set $S$, write

\[
 \mathcal E_t(S)=\bigcup_{y\in S}\mathcal E_t(y),
\qquad
 J_t(S)=\sum_{y\in S}d_t(y)-|\mathcal E_t(S)|.                  \tag{1.1}
\]

Every active edge rings at rate $\nu_t=(r\Delta_t)^{-1}$, and an
active vertex $y$ has compensation rate

\[
                         \chi_t(y)={\Delta_t-d_t(y)\over r\Delta_t}.
                                                                    \tag{1.2}
\]

Therefore the rate of an event deleting at least one member of $S$ is

\[
\begin{aligned}
 \Lambda_t(S)
 &=\nu_t|\mathcal E_t(S)|+\sum_{y\in S}\chi_t(y)\\
 &={|S|\over r}-\nu_tJ_t(S).                                   \tag{1.3}
\end{aligned}
\]

For arbitrary active sets $A,B$, inclusion--exclusion on the event
sets gives

\[
\begin{aligned}
 \Lambda_t(A)+\Lambda_t(B)-\Lambda_t(A\cup B)
 &=\nu_t|\mathcal E_t(A)\cap\mathcal E_t(B)|\\
 &\quad+\sum_{y\in A\cap B}\chi_t(y).                          \tag{1.4}
\end{aligned}
\]

This is the exact joint-hazard identity; it contains both shared edge
events and shared compensation clocks.

More generally, let $S_1,\ldots,S_h$ be the equality-resolved
marginal resource factors used by a product reference, put
$U=\bigcup_iS_i$, and define

\[
 t_g=|\{i:g\cap S_i\ne\varnothing\}|,
 \qquad
 t_y=|\{i:y\in S_i\}|.                                        \tag{1.5}
\]

Then the exact union deficit is

\[
\boxed{
 \sum_{i=1}^h\Lambda_t(S_i)-\Lambda_t(U)
 =\nu_t\sum_g(t_g-1)_+
  +\sum_y\chi_t(y)(t_y-1)_+.}                                 \tag{1.6}
\]

Thus the pair domination
$(t-1)_+\le\binom t2$ is legitimate only after the terminal losses
and all marginal survival derivatives have first been assembled into
(1.6).  It is not a justification for deleting terminal terms before
normalization.

## 2. Equality-resolved prefix and last row

Fix one equality-resolved physical prefix.  Let $P_C$ be the union of
all active physical resources whose deletion terminates that prefix.
For a compatible last row $f$, assign every resource already in the
prefix to $P_C$ and put

\[
                         R_C(f)=V(f)\setminus P_C.              \tag{2.1}
\]

Thus $P_C\cap R_C(f)=\varnothing$.  Formula (1.4) becomes

\[
\boxed{
 \Lambda_t(P_C\cup R_C(f))
 =\Lambda_t(P_C)+\Lambda_t(R_C(f))
 -\nu_t|\mathcal E_t(P_C)\cap\mathcal E_t(R_C(f))|.}           \tag{2.2}
\]

Equivalently,

\[
 \Xi_t(P_C,R_C(f))
 =\nu_t\bigl[
 J_t(P_C\cup R_C(f))-J_t(P_C)-J_t(R_C(f))
 \bigr].                                                       \tag{2.3}
\]

The equality resolution is essential only for assigning a shared
physical resource once.  It does not remove an edge event which meets
one prefix resource and one genuinely new last-row resource.

Let $I_C$ be the prefix-survival indicator.  Writing the link as a sum
of last-row indicators gives

\[
 I_CA_C=\sum_{f\in\mathcal F_C}
             I_{P_C\cup R_C(f)}.                               \tag{2.4}
\]

The exact first-moment generator is therefore

\[
\begin{aligned}
 \mathcal L_t(I_CA_C)
 &=-\Lambda_t(P_C)I_CA_C\\
 &\quad-I_C\sum_{f\in\mathcal F_C}
       I_f\Lambda_t(R_C(f))\\
 &\quad+I_C\sum_{f\in\mathcal F_C}
       I_f\Xi_t(P_C,R_C(f)).                                   \tag{2.5}
\end{aligned}
\]

The first line is the terminal prefix-death contribution.  It is
nonpositive, but it cannot be discarded when the reference derivative
contains the negative prefix-survival rate.  The first line cancels that
reference term; the third line is the remaining positive correlation.

## 3. Exact normalized error

Suppose the equality-resolved reference assigns rates
$\lambda_C^{\rm ref}$ to prefix survival and
$\lambda_f^{\rm ref}$ to the new last-row resources.  For one full
configuration $\eta=(C,f)$, (2.2) gives the exact normalized drift
error

\[
\begin{aligned}
 \varepsilon_\eta(t)
 &=\lambda_C^{\rm ref}-\Lambda_t(P_C)\\
 &\quad+\lambda_f^{\rm ref}-\Lambda_t(R_C(f))\\
 &\quad+\Xi_t(P_C,R_C(f)).                                    \tag{3.1}
\end{aligned}
\]

If the reference is the product vertex-survival reference, then
$\lambda_S^{\rm ref}=|S|/r$, and (1.3), (2.3) collapse (3.1) to

\[
                         \varepsilon_\eta(t)
                         =\nu_tJ_t(P_C\cup R_C(f)).             \tag{3.2}
\]

For a mixed type $\tau$, let $\mathcal Q_\tau(t)$ be its active
physical configurations and $b_\eta\ge0$ their equality-resolved
incidence weights.  After the known individual prefix and last-row
errors have been removed, the exact additional aggregate error is

\[
 \varepsilon_\tau^{\rm cross}(t)
 ={
   \sum_{\eta=(C,f)\in\mathcal Q_\tau(t)}
       b_\eta\Xi_t(P_C,R_C(f))
  \over
   \sum_{\eta\in\mathcal Q_\tau(t)}b_\eta}.                    \tag{3.3}
\]

Thus the missing theorem is precisely

\[
\boxed{
 \int_0^T\varepsilon_\tau^{\rm cross}(t)\,dt=o(1)
 \quad\text{in owner-incidence aggregate, uniformly over top types}.}
                                                                    \tag{XPH}
\]

The numerator in (3.3) is the count obtained by adjoining one new
column incident to both the prefix and the last row.  Hence XPH is the
$q=1$ cross-prefix column-link estimate.  Static row exploration
controls it at time zero, but monotonicity of raw counts does not control
its ratio to the shrinking dynamic reference.

## 4. Counterexample to a uniform first-moment conclusion

Fix the uniformity and clock denominator $r\ge2$.  Take one active
$r$-edge

\[
                         g=\{p,q\}\cup F,
                                                                    \tag{4.1}
\]

where $|F|=r-2$.  Until $g$ rings, every active vertex has degree one,
so $\Delta_t=1$ and every compensation rate is zero.  The unique edge
through $p$ is also the unique edge through $q$.  Consequently, on
the surviving state,

\[
 \nu_t|\mathcal E_t(p)\cap\mathcal E_t(q)|
 ={1\over r},                                                  \tag{4.2}
\]

and $\chi_t(p)=\chi_t(q)=0$.  Put $P=\{p\}$ and $R=\{q\}$.  Then

\[
 \Lambda_t(P)=\Lambda_t(R)={1\over r},qquad
 \Lambda_t(P\cup R)={1\over r}.                               \tag{4.3}
\]

The edge clock is exponential of rate $1/r$.  Therefore each marginal
survivor and the joint survivor decay at rate $1/r$, whereas their
product reference decays at rate $2/r$.  Hence, exactly,

\[
 {\Pr(P\cup R\text{ survives to }t)\over e^{-2t/r}}
 =e^{t/r}.                                                      \tag{4.4}
\]

For a disjoint union of copies, define the normalized first-moment
cross hazard by

\[
 \Xi_t^{\rm FM}
 ={\mathbb E\sum_i I_i(t)\Xi_t(P_i,R_i)
   \over\mathbb E\sum_i I_i(t)}.
\]

It is exactly $1/r$ at every time.  At the prescribed terminal time
$T=r\log(1/z)$,

\[
 \int_0^T\Xi_t^{\rm FM}\,dt
 ={T\over r}=\log(1/z).                                      \tag{4.5}
\]

This example has distinct prefix and last-row resources, exact marginal
compensation, and no equal-row diagonal.  It proves that the sign
$\mathsf K_C\le0$ and exact marginal hazards do not imply an integrated
$o(1)$ logarithmic comparison.  Taking a disjoint union of arbitrarily
many copies makes the same statement an owner-incidence aggregate:
every surviving copy contributes the same normalized cross hazard
$1/r$.

## 5. The weaker additive route and its exact gate

The failure above concerns a uniform **multiplicative** comparison.  It
does not rule out an absolute one-child estimate.  Let

\[
 \mathcal X_\tau(t)
 =\sum_{\eta=(C,f)\in\mathcal Q_\tau(t)}
   b_\eta I_\eta(t)
   |\mathcal E_t(P_C)\cap\mathcal E_t(R_C(f))|,                \tag{5.1}
\]

let $S_\tau(t)=\sum_\eta b_\eta I_\eta(t)$, and let
$Y_\tau(t)$ be the transported current-density reference.  The exact
aggregate first-moment inequality has the form

\[
 D^+\mathbb E{S_\tau(t)\over Y_\tau(t)}
 \le \epsilon_\tau(t)\mathbb E{S_\tau(t)\over Y_\tau(t)}
   +{\nu_t\mathbb E\mathcal X_\tau(t)\over Y_\tau(t)},         \tag{5.2}
\]

where the already audited marginal errors satisfy
$\int_0^T|\epsilon_\tau(t)|dt=o(1)$.  Thus the following current-residual
child estimate would suffice:

\[
\boxed{
 \nu_t\mathbb E\mathcal X_\tau(t)
 \le C L^{C_0}\alpha^{s+1}Y_\tau(t)
 \quad\text{uniformly in }t.}                                 \tag{ACH}
\]

Indeed, variation of constants would give

\[
 \mathbb E{S_\tau(t)\over Y_\tau(t)}
 \le e^{o(1)}\left[
 {S_\tau(0)\over Y_\tau(0)}+CTL^{C_0}\alpha^{s+1}
 \right].                                                     \tag{5.3}
\]

For $T=O(m\log m)$ and
$\alpha=m^{-19/10+o(1)}$, one has
$TL^{C_0}\alpha=m^{-9/10+o(1)}=o(1)$, so (ACH) propagates the
$O(\alpha^s)$ scale without any relative XPH estimate and without an
infinite ordered tower.

This is the strategy claimed in
`MATH_THEOREM_CROSS_PREFIX_Q1_ADDITIVE_CLOSURE_20260727.md`, but its
present proof does not establish (ACH).  The cited static mixed-diagram
theorem assumes that diagram columns are pairwise resource-disjoint.
Every summand in (5.1), however, contains an active event edge $g$
meeting a protected prefix column at $p\in P_C$ and the last row at
$s\in R_C(f)$.  Thus $g$ is resource-nondisjoint from an old protected
column.  The instruction to merge $g$ into a ``column-intersection
forest'' is not a lemma in the cited disjoint-column theorem, and it is
exactly where the additional endpoint factor $\alpha$ is needed.  A
time-zero static bound would not suffice: (ACH) is normalized by the
shrinking current reference $Y_\tau(t)$.

There is no separate compensation-child term in the two-set formula
after the definition $R_C(f)=V(f)\setminus P_C$: the sets are disjoint,
so a single compensation clock cannot belong to both.  If instead one
keeps overlapping marginal factors, its exact contribution is already
the second sum in (1.6) and must be equality-resolved there.

Consequently the smallest positive replacement for XPH is not a generic
one-row path-mesh maximum, but the rooted, resource-nondisjoint current
residual estimate (ACH), certified through child order $2L+2$.

## 6. Consequence for the quarantine theorem

The maximal-inequality and type-counting calculation in
`MATH_THEOREM_AGGREGATE_FIRST_MOMENT_TOP_STRIP_QUARANTINE_20260727.md`
remains valid **conditional on XPH**, or under the weaker additive route
conditional on ACH.  It is not an unconditional consequence of the
one-cluster identity.  The later file
`MATH_THEOREM_FIRST_MOMENT_GRADED_TOP_STRIP_ADDITIVE_CLOSURE_AND_ROOT_QUARANTINE_20260727.md`
correctly records ACH and its resource-nondisjoint stopped endpoint
extension as assumptions rather than proved inputs.

The exact surviving alternatives are:

1. prove XPH from hereditary repaired-ring endpoint geometry;
2. prove the weaker resource-nondisjoint absolute child estimate (ACH)
   and close by (5.3);
3. include the cross-prefix column as a stopped excess-$(s+1)$ variable
   and close its top boundary by another argument; or
4. quarantine prefix--last-row pairs by the incidence mass in the
   numerator of (3.3).

Until one of these is proved, the claimed uniform integrated $o(1)$
first-moment error is refuted at the level of the stated inputs, and the
constant-one trajectory remains conditional.
