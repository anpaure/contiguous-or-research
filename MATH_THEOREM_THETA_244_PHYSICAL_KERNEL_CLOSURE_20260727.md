# The physical theta core: independent closure and general row exploration

Date: 2026-07-27

Scope: static repaired promotion-ring mixed diagrams.  Literal diagram
columns are pairwise resource-disjoint.  Constants depending on the
fixed-density normalization are absorbed into $C^{|E|}$.

## 0. Verdict

The $\Theta_{2,4,4}$ core is closed.  The missing factor $\alpha$
is supplied by the already proved joint two-column path-mesh estimate,
not by multiplying marginal degrees.  If $d$ is the number of row
options through the protected owner, $L$ is the maximum one-witness
row incidence, and $A=d\alpha$ is the maximum one-witness column
incidence, then

\[
 Z_{\Theta_{2,4,4}}
 \le C d^4L^5\alpha^5={CL^5A^5\over d}.                        \tag{0.1}
\]

The same kernel argument proves every literal subdivided $K_{2,b}$
and every generalized theta bundle.  More strongly, the revised
row-exploration lemma in
`MATH_THEOREM_STATIC_MIXED_DIAGRAM_EXCESS_AND_DYNAMIC_OMEGA_BUFFER_20260727.md`
is valid: it proves every physical mixed core whose total old-row
witness order lies in the certified path-mesh range.  Row equalities are
harmless because they may simply be dropped.

Thus there is no next unresolved **static topology**.  The next actual
gate is dynamic: the first-moment/quarantine bound for the graded top
strip.  The only additional static scope condition is

\[
                         2\omega\le L_{\rm pm},                 \tag{0.2}
\]

where $L_{\rm pm}$ is the largest total witness order for which the
joint path-mesh maximum and internal census have been certified.

## 1. Literal weighted incidence kernel

Let $\mathcal R$ be the row-option set, $|\mathcal R|=d$, and let
$\mathcal E$ be the physical column-resource set.  Let $h(u,e)\ge0$
be the number of one-owner-witness incidences between row $u$ and
column $e$.  The one-witness ledgers give

\[
 \sum_eh(u,e)\le L,qquad
 \sum_uh(u,e)\le A=d\alpha.                                    \tag{1.1}
\]

For resource-disjoint columns $e\perp e'$, put

\[
 S(e,e'):=\sum_{w\in\mathcal R}h(w,e)h(w,e').                   \tag{1.2}
\]

This is exactly $B_X^{(1,1)}(e,e')$.  The proved two-column
path-mesh maximum says

\[
                         S(e,e')\le C_0d\alpha^2
                         \qquad(e\perp e').                    \tag{1.3}
\]

This is the joint estimate that degrees alone miss.  If $S_\perp$
denotes (1.2) with non-disjoint entries set to zero, then

\[
\begin{aligned}
 \sum_{e'}S_\perp(e,e')
 &\le\sum_wh(w,e)\sum_{e'}h(w,e')\\
 &\le LA=dL\alpha.                                              \tag{1.4}
\end{aligned}
\]

## 2. Fixed-endpoint paths

For $k\ge2$, let $P_k(u,v)$ count literal paths

\[
 u,e_1,x_1,e_2,\ldots,x_{k-1},e_k,v                            \tag{2.1}
\]

whose $k$ column resources are pairwise disjoint.  Dropping only the
nonconsecutive disjointness restrictions gives

\[
 P_k(u,v)
 \le\sum_{e_1,e_k}h(u,e_1)
       (S_\perp^{k-1})(e_1,e_k)h(v,e_k).                       \tag{2.2}
\]

For a nonnegative matrix $M$,

\[
 (M^q)_{ab}\le\|M\|_{\max}\|M\|_\infty^{q-1}.                 \tag{2.3}
\]

Using (1.1), (1.3), and (1.4) in (2.2) yields

\[
\boxed{
 P_k(u,v)\le C_kd^{k-1}L^k\alpha^k.}                          \tag{2.4}
\]

In particular,

\[
                         P_2(u,v)\le CdL^2\alpha^2.             \tag{2.5}
\]

Replacing (1.3) by the degree bound $S(e,e')\le A=d\alpha$
would lose exactly one factor $\alpha$.

## 3. The $\Theta_{2,4,4}$ calculation

Let

\[
                         C(u,v)=\sum_eh(u,e)h(v,e)              \tag{3.1}
\]

be the direct length-two branch kernel.  Its total mass is

\[
\begin{aligned}
 \sum_{u,v}C(u,v)
 &=\sum_e\left(\sum_uh(u,e)\right)^2\\
 &\le A\sum_{u,e}h(u,e)
 \le dLA=d^2L\alpha.                                           \tag{3.2}
\end{aligned}
\]

Fix the endpoint rows $u,v$.  Dropping disjointness constraints
between different branches, while retaining the disjoint pair inside
each length-four branch, enlarges the literal theta count to at most

\[
                         C(u,v)P_2(u,v)^2.                      \tag{3.3}
\]

Therefore

\[
\begin{aligned}
 Z_{\Theta_{2,4,4}}
 &\le\sum_{u,v}C(u,v)P_2(u,v)^2\\
 &\le(CdL^2\alpha^2)^2(d^2L\alpha)\\
 &\le Cd^4L^5\alpha^5,
\end{aligned}                                                   \tag{3.4}
\]

proving (0.1).  The sums allow $u=v$, equality of the two internal
rows, and every other row-equality pattern.  No equality partition is
being treated as an independent marginal event.

For $b$ internally row-disjoint length-four branches,

\[
 \sum_{u,v}P_2(u,v)^b
 \le C_bd^{b+2}L^{2b}\alpha^{2b}.                              \tag{3.5}
\]

At $b=3$, this is the literal subdivided-$K_{2,3}$ estimate

\[
 \operatorname{hom}_\perp(SK_{2,3})
 \le Cd^5L^6\alpha^6={CL^6A^6\over d}.                        \tag{3.6}
\]

Equation (2.4) similarly proves every generalized theta bundle with
longer internally row-disjoint branches; direct length-two branches are
handled by the existing rectangular $K_{2,q}$ estimate.

## 4. Independent audit of the general row exploration

First sum every private column with $q_j=1$ into its factor $L$, as
in the private-column elimination theorem.  Consider the remaining
physical core, with formal row set $R$, pairwise resource-disjoint
columns $e_j$, and multiplicities $q_{ij}$.  Put

\[
 q_j=\sum_iq_{ij},\qquad
 s=\sum_jq_j,\qquad
 \omega=s-c.                                                    \tag{4.1}
\]

First drop every prescribed equality or inequality between formal rows.
All summands are nonnegative, so this only enlarges the count.  It is
therefore enough to sum the $a=|R|$ formal rows independently; the
normalization is exactly $d^a$.  This avoids any unproved equality
credit.

In each connected component, order the rows so that, after the first,
each row meets an already introduced column.  When row $i$ is exposed,
let $O_i$ be its old incident columns and $N_i$ the columns first
introduced from it.  The old columns are fixed and pairwise
resource-disjoint, so the joint path-mesh maximum gives

\[
 \sum_{f_i\ni X}
 \prod_{j\in O_i}\binom{|f_i\cap e_j|}{q_{ij}}
 \le d\alpha_\omega^{\sum_{j\in O_i}q_{ij}}.                   \tag{4.2}
\]

Uniformly in the chosen row, the internal census gives

\[
 \sum_{(e_j:j\in N_i)}^*
 \prod_{j\in N_i}\binom{|f_i\cap e_j|}{q_{ij}}
 \le L^{|N_i|}
 \alpha_\omega^{\sum_{j\in N_i}(q_{ij}-1)}.                  \tag{4.3}
\]

The restriction that new columns also avoid all old columns may be
retained; dropping it in (4.3) only gives a uniform upper bound on the
valid branching weight.  Every later use of (4.2) is on an actual valid
prefix, whose introduced columns remain pairwise disjoint.

Multiplying the uniform conditional bounds along the exploration gives

\[
\begin{aligned}
 &\sum_i\sum_{j\in O_i}q_{ij}
 +\sum_i\sum_{j\in N_i}(q_{ij}-1)\\
 &=\sum_{i,j}q_{ij}-c=\omega.                                  \tag{4.4}
\end{aligned}
\]

Thus every physical mixed diagram satisfies

\[
 Z_\Gamma(X)
 \le C^\omega d^aL^c\alpha_\omega^\omega,                     \tag{4.5}
\]

provided the local estimates (4.2)--(4.3) are certified through the
largest total order encountered.  In the compressed core every
$q_j\ge2$, so $c\le\omega$ and
$s=c+\omega\le2\omega$, yielding the scope condition (0.2).

This proves the revised arbitrary-core lemma independently.  In
particular, a once-subdivided $K_4$ is not a new static obstruction:
row exploration charges its six columns by old-incidence counts
$0,1,2,3$, whose sum is six.

## 5. What the unrestricted homomorphism formulation does not say

The uncolored matrix expression

\[
                         \sum_{u,v}(C^2_{uv})^3                 \tag{5.1}
\]

allows equal and resource-overlapping column positions inside every
matrix product.  It is therefore stronger than the literal subdivided
$K_{2,3}$ count.  The component $K_{A,L}$ with $d-A$ isolated
rows shows that degrees plus a $C_4$ bound do not imply this
unrestricted inequality.  This does not contradict (3.6): the physical
kernel retains $e\perp e'$ inside every subdivided branch.

Consequently the exact next obstruction for the repaired-ring hierarchy
is not another static homomorphism inequality.  It is the stopped
incidence-weighted first-moment/quarantine estimate for the graded top
strip.  Static use beyond (0.2) would additionally require an extension
of the path-mesh maximum and internal census to the corresponding order.
