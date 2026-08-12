# Global endpoint-capacity Hall--Farkas theorem

Date: 2026-07-29  
Status: proved.  This sharpens the `6c98` endpoint-cover theorem to the exact
fractional Hall theorem for the endpoint-capacity relaxation.  It does not
prove integral seam recourse or either radius-99 branch feasible/infeasible.

## 1. Provider-capacity normal form

Let `V` be a finite endpoint set, `F_0` a frozen source seam set, `A` the
explicit catalogue of addable seams, and `C` a finite resource set.  A
resource may be a lower-q1 colour, an upper-q1 colour, or any other coverage
label carried by a seam.

Write

\[
 B_{va}=\iota_v(a),\qquad \bar B_{vh}=\iota_v(h),
 \qquad Q_{ca}=1[c\text{ is provided by }a].                 \tag{1.1}
\]

Endpoint incidence is counted with multiplicity.  Thus a loop at `v`, if
loops are admitted, has incidence two.  Parallel seam IDs remain distinct
columns of `B` and `Q`.

For a fractional source-cut vector `x in [0,1]^{F_0}`, define the freed
endpoint capacity

\[
 b_v(x)=\sum_{h\in F_0}\bar B_{vh}x_h.                       \tag{1.2}
\]

If `S_c subseteq F_0` is the source-provider set of resource `c`, then its
affine repair demand is

\[
 r_c(x)=1-\sum_{h\in S_c}(1-x_h)
       =\sum_{h\in S_c}x_h-|S_c|+1.                          \tag{1.3}
\]

The exact coverage row is `sum_a Q_ca y_a >= r_c(x)`.  Negative values of
`r_c(x)` simply make this row redundant.  In the source-unique case
`S_c={e(c)}`, one has `r_c(x)=x_e(c)`.

The **fractional endpoint-capacity Hall relaxation** is

\[
 y\ge0,\qquad By\le b(x),\qquad Qy\ge r(x).                  \tag{H_x}
\]

It deliberately relaxes exact degree restoration `By=b(x)`.  When every
resource demand is at most one, adding `y_a<=1` does not change feasibility
of `(H_x)`: replace every `y_a>1` by one.  Any resource using that column
still receives at least one unit, and every endpoint load only decreases.

## 2. Exact weighted Hall theorem

### Theorem 2.1 (global endpoint-capacity Hall--Farkas theorem)

For fixed `x`, system `(H_x)` is feasible if and only if

\[
 \boxed{\quad
   \sum_{c\in C}\lambda_c r_c(x)
   \le \sum_{v\in V}w_v b_v(x)
 \quad}                                                       \tag{2.1}
\]

for every pair of nonnegative weight vectors `lambda,w` satisfying

\[
 \sum_{c\in C}Q_{ca}\lambda_c
 \le \sum_{v\in V}B_{va}w_v
 \qquad(a\in A).                                             \tag{2.2}
\]

Once `lambda,w` are frozen, (2.1) is the globally valid affine Benders row

\[
 \sum_c\lambda_c
 \left(\sum_{h\in S_c}x_h-|S_c|+1\right)
 \le
 \sum_{h\in F_0}x_h\sum_v\bar B_{vh}w_v.                    \tag{2.3}
\]

#### Proof

Suppose `y` satisfies `(H_x)`.  Multiplying the resource rows by
`lambda_c`, summing, applying (2.2) column by column, and then applying the
endpoint capacities gives

\[
 \lambda^T r(x)
 \le\lambda^TQy
 \le w^TBy
 \le w^Tb(x).
\]

This proves necessity.  Conversely, the Farkas alternative for

`By<=b(x), -Qy<=-r(x), -y<=0`

says that infeasibility is equivalent to the existence of nonnegative
`w,lambda` satisfying (2.2) and
`lambda^T r(x)>w^Tb(x)`.  This is exactly a violation of (2.1).  Hence the
family is sufficient as well.  No integrality is used.  ∎

### Corollary 2.2 (bounded polynomial separator)

Let

\[
 R=\max_{a\in A}\sum_cQ_{ca}                                \tag{2.4}
\]

be the maximum resource rank of an addable seam.  A violated ray in Theorem
2.1 may be scaled so that `max_c lambda_c=1`.  After this normalization,
`0<=lambda_c<=1`, and every left side of (2.2) is at most `R`.  Any
`w_v>R` may be clipped to `R`: every seam incident with `v` then already has
right side at least `R`, while all other constraints are unchanged.

Consequently the explicit-catalogue LP

\[
 \begin{array}{ll}
 \text{maximize}&\lambda^Tr(x)-w^Tb(x),\\
 \text{subject to}&Q^T\lambda\le B^Tw,\\
                  &0\le\lambda\le1,\quad0\le w\le R
 \end{array}                                                  \tag{2.5}
\]

has positive optimum if and only if `(H_x)` is infeasible.  A positive
optimum emits (2.3); a nonpositive optimum certifies every weighted Hall row.
The LP is polynomial in the explicitly listed provider catalogue.  No claim
is made that the catalogue itself is polynomial in a compressed parameter
such as `k`.

### Theorem 2.3 (finite provider capacities and aggregated parallels)

For arbitrary nonnegative repair demands, retain explicit provider
capacities `0<=y_a<=u_a`.  Then

\[
 By\le b,\qquad Qy\ge r,\qquad0\le y\le u                \tag{2.6}
\]

is feasible if and only if, for every `lambda,w>=0`,

\[
 \boxed{
 \lambda^Tr\le w^Tb+
 \sum_{a\in A}u_a[Q_a^T\lambda-B_a^Tw]_+ .}                 \tag{2.7}
\]

Indeed, for any feasible `y`, split each column price into its endpoint-paid
part and its positive excess:

\[
 \lambda^TQy
 \le w^TBy+
 \sum_a y_a[Q_a^T\lambda-B_a^Tw]_+
 \le w^Tb+
 \sum_a u_a[Q_a^T\lambda-B_a^Tw]_+.
\]

The converse is the bounded-variable Farkas alternative.  Equivalently,
linearize each positive part with a nonnegative slack `s_a` satisfying
`s_a>=Q_a^Tlambda-B_a^Tw` and minimize its coefficient `u_a`.

Theorem 2.1 is the infinite-capacity form: a finite inequality then requires
`Q_a^Tlambda<=B_a^Tw` on every column.  In the present q1 application the
unit bounds can instead be dropped without loss because every demand is at
most one, as proved in Section 1.  Parallel physical seam IDs may remain
separate unit-capacity columns.  If `m` columns have identical incidence and
resource signatures, they may equivalently be aggregated into one column of
capacity `u_a=m`; they must not be collapsed to capacity one.

## 3. Weighted one-palette endpoint rows form the exact fractional Hall system

Suppose each addable seam has exactly one relevant palette colour.  Then
`R=1`, and (2.2) is

\[
 \lambda_{c(a)}\le w_u+w_v\qquad(a=uv).                      \tag{3.1}
\]

For source-unique colours, (2.5) is precisely the prize-weighted LP in
Corollary 2.2 of
`MATH_THEOREM_L_K16_R99_6C98_ENDPOINT_COVER_BENDERS_20260729.md`.
The present theorem strengthens its interpretation:

> that LP has positive value exactly when the fractional one-palette
> provider packing under the freed endpoint capacities is infeasible.

It is therefore not merely a dominating heuristic for integral vertex-cover
rows.

An ordinary endpoint-cover row is the special integral choice

\[
 \lambda=1_T,qquad w=1_P,                                   \tag{3.2}
\]

where `P` meets every replacement provider of every colour in `T`.  The
26-node `6c98` cover and its row

\[
 \sum_h|\operatorname{ends}(h)\cap P|x_h
 \ge x_{4742}+x_{22511}+x_{23229}+x_{24034}                  \tag{3.3}
\]

are exactly such a Hall--Farkas vector.  Nothing here asserts that this
integral vector is optimal after all colours or both palettes are admitted;
its proved role is the explicit violation `3<4` and the certified 713-cut
exclusion family.

Integral endpoint covers alone are strictly weaker than the weighted family,
even for one colour.  Let its providers be the three edges of a triangle,
give every endpoint capacity `1/2`, and demand `4/5`.  Every integral vertex
cover has at least two vertices and hence capacity at least one, so every
ordinary cover row holds.  But total endpoint capacity is `3/2`, every unit
of provider mass consumes two endpoint units, and therefore at most `3/4`
colour mass can be packed.  The violated weighted row is
`lambda_c=1,w_v=1/2` at all three vertices, and reads `4/5<=3/4`.

For completeness, the LP dual of the one-palette separator at a fixed point,
with prizes `p_c` and endpoint capacities `d_v`, is

\[
\begin{array}{ll}
\text{minimize}&\displaystyle\sum_c\alpha_c,\\
\text{subject to}&\displaystyle
 \alpha_c+\sum_{a\in A(c)}q_a\ge p_c\quad(c\in C),\\
&\displaystyle\sum_aB_{va}q_a\le d_v\quad(v\in V),\\
&\alpha,q\ge0.
\end{array}                                                   \tag{3.4}
\]

Provider sets are disjoint as seam-ID sets within one palette.  Hence one
may assume `sum_(a in A(c))q_a<=p_c`, and (3.4) is equivalently total prize
minus the maximum fractional coloured-provider mass under the colour and
endpoint capacities.  This gives another direct proof that zero separator
value is equivalent to fractional capacity feasibility.

At `6c98`, restricted to the four colours in (3.3), the displayed violation
one is optimal under the normalization `0<=lambda<=1`.  A dual solution of
value one sets `q=1` on

\[
 18172=(490,617),\qquad21408=(576,638),\qquad
 22529=(611,663),                                           \tag{3.5}
\]

and sets `alpha_1883=1`, with every other dual variable zero.  The three
provider seams have six distinct endpoints, each of cut capacity one; they
pay the 1907, 3255 and 5939 prizes, while `alpha_1883` pays the fourth.
The primal 26-node row has value one, so strong duality proves equality.
This is only four-colour optimality: it does not prove optimality after all
upper colours or both palettes are admitted.

Optimizing only the binary endpoint-cover subfamily is weighted vertex cover
already for one colour and an arbitrary provider graph.  Thus there is no
general exact maximum-closure/min-cut oracle for arbitrary integral covers
unless `P=NP`; this abstract statement is not a complexity claim about the
single frozen K16 catalogue.  The fractional LP above is the exact
polynomial Hall oracle that is actually needed.

## 4. The simultaneous lower/upper Hall system

For simultaneous q1 repair, take the disjoint resource set
`C=C_L dotcup C_U`.  A loopless seam `a=uv` carries one lower colour
`ell(a)` and one upper colour `u(a)`.  The dual column condition becomes

\[
 \lambda_{\ell(a)}+\lambda_{u(a)}\le w_u+w_v.                \tag{4.1}
\]

Thus `R=2`.  The LP (2.5) is an exact polynomial separator for the
fractional **common-seam** lower/upper endpoint-capacity relaxation.  Setting
all weights of one palette to zero recovers the complete weighted
same-palette Hall family.  Unlike two independent palette tests, (4.1) sees
that the same seam variable, with the same two endpoint capacities, must
carry both labels.

For integral `lambda=1_T`, the correct combinatorial object is a
multiplicity endpoint cover: a seam carrying two selected labels must receive
two units of endpoint weight, not merely meet the selected endpoint set
once.  This is why simply taking an ordinary vertex cover of the union of
lower and upper provider graphs is not the general simultaneous Hall row.

### Theorem 4.1 (the audited joint-cover rows lie inside global Hall)

Assume the frozen source and addable seams are loopless.  Let `C_L,C_U` be
source-unique lower and upper colours, and put

\[
 L(x)=\sum_{c\in C_L}x_{e(c)},\qquad
 U(x)=\sum_{c\in C_U}x_{e(c)},\qquad
 \rho(x)=\sum_{h\in F_0}x_h.                                 \tag{4.2}
\]

Let nonnegative weights `a_c,b_c,gamma_v`, with
`a_c,b_c,gamma_v<=1`, satisfy

\[
 a_{\ell(s)}+b_{u(s)}+\gamma_i+\gamma_j\ge1                 \tag{4.3}
\]

for every addable seam `s=ij` whose lower and upper colours both belong to
`C_L,C_U`.  Then the joint hypergraph-cover row

\[
 \sum_{c\in C_L}a_cx_{e(c)}+
 \sum_{c\in C_U}b_cx_{e(c)}+
 \sum_v\gamma_vb_v(x)
 \ge L(x)+U(x)-\rho(x)                                      \tag{4.4}
\]

is a member of the global Hall--Farkas family.

These bounds are without loss for separation: replacing any cover weight
larger than one by one preserves every constraint containing that resource
and weakly decreases the cover cost.  Thus an unnormalized joint-cover row
with a larger coefficient is implied by its clipped global-Hall member.  The
audited integral `0/1` covers are literally members; after clipping,
`w_v=1/2+gamma_v<=3/2`, within the bounded rank-two LP (2.5).

#### Proof

Set

\[
 \lambda_c=1-a_c\ (c\in C_L),\qquad
 \lambda_c=1-b_c\ (c\in C_U),\qquad
 w_v=\tfrac12+\gamma_v.                                     \tag{4.5}
\]

If a seam carries two relevant unique colours, (4.3) gives (4.1).  If it
carries only one, the left side of (4.1) is at most one while its two
baseline endpoint halves already sum to one.  With no relevant label the
condition is automatic.  Hence these weights satisfy (2.2).

The loopless incidence identity is

\[
 \frac12\sum_vb_v(x)=\sum_{h\in F_0}x_h=\rho(x).             \tag{4.6}
\]

Substituting (4.5) into (2.1) and rearranging gives exactly (4.4).  ∎

Thus the rank-two LP (2.5) simultaneously contains

1. every weighted or integral same-palette endpoint-cover row; and
2. every normalized fractional or integral joint lower/upper/endpoint-cover
   row of Theorem 5.4 in
   `MATH_THEOREM_L_K16_R99_PORTAL_CORE_AND_FEATURE_BENDERS_20260729.md`.

This is a logical containment of row families.  It does not say that a
previously displayed joint cover was minimum, nor that passing the global LP
implies integral seam completion.

### Proposition 4.2 (strictness beyond separate plus joint-cover closure)

Complete weighted Hall separation in each palette, even together with every
joint double-repair hypergraph-cover row, need not imply the global mixed
Hall system.

Take four unit-capacity endpoints.  Demand lower colours `l_1,l_2` and one
upper colour `u`, and let the relevant provider seams be

\[
\begin{array}{c|c}
12&(l_1,u),\\
13&(l_2,\text{undemanded upper label}),\\
24&(l_1,\text{undemanded upper label}),\\
34&(\text{undemanded filler labels}).
\end{array}                                                   \tag{4.7}
\]

Use total addition capacity `rho=2`.  The lower palette alone is feasible by
the disjoint seams `13,24`, and the upper palette alone is feasible by `12`
(with `34` as a disjoint filler if exact total mass is retained).  Hence all
separate-palette weighted Hall rows hold.  The joint overlap demand is
`2+1-rho=1`, and seam `12` itself supplies one feasible joint witness, so
every joint hypergraph-cover row also holds.

Simultaneous fractional repair is nevertheless impossible.  The unique
provider of `u` forces `y_12=1`, and the unique provider of `l_2` forces
`y_13=1`; endpoint 1 would have load two.  The global Hall certificate is

\[
 \lambda_u=\lambda_{l_2}=1,qquad w_1=1,
 \qquad\text{all other weights zero},                         \tag{4.8}
\]

which satisfies every column inequality and reads `2<=1`.  Thus the global
rank-two LP is a strict strengthening of the union of the two older row
families, already on four endpoints and before integrality is imposed.
Geometrically, joint-cover rows are exactly embedded with the uniform
baseline `w_v>=1/2` from (4.5); the sparse mixed certificate (4.8) has zero
prices away from one endpoint and cannot have that form.

## 5. Exact integral obstruction after all fractional Hall rows

Theorem 2.1 is sharp for `(H_x)` but cannot be upgraded to integral recourse
without an additional hypothesis.

### Proposition 5.1 (minimal alternating rectangle obstruction)

Let four endpoints `1,2,3,4` have unit capacities.  Give a red colour the
providers

\[
                    12,\ 34
\]

and a blue colour the providers

\[
                    13,\ 24.                                 \tag{5.1}
\]

Demand one unit of each colour.  There is no integral provider packing, but
the fractional assignment `y=1/2` on all four seams is feasible and saturates
every endpoint.  Consequently it satisfies every weighted Hall--Farkas row
of Theorem 2.1.

#### Proof

Every red provider intersects every blue provider, so two integral witnesses
cannot be chosen.  At weight one half, each colour receives total one and
each endpoint has load one.  The final assertion follows from Theorem 2.1.
∎

This is minimal for unit demands and unit endpoint capacities.  One colour
cannot obstruct integrality.  Two demanded edges consume four endpoint
units, so at least four unit-capacity endpoints are necessary.  If either
colour had only one provider, fractional feasibility would saturate its two
endpoints and force every positive provider of the other colour to avoid
them, yielding an integral disjoint pair.  Hence both colours need at least
two providers, and (5.1) attains the resulting lower bounds of two colours,
four endpoints and four provider seams.

The obstruction is already exact-degree: the displayed fractional point
saturates all endpoint capacities.  Therefore neither adding all weighted
endpoint-cover rows nor replacing `By<=b` by `By=b` removes the integer gate.

### Proposition 5.2 (an exact integral Hall-sufficient anchored-star class)

Assume `r_c in {0,1}` and all endpoint capacities are nonnegative integers.
Suppose every colour `c` has a private anchor `q_c`, all its providers are
loopless seams `q_cv` with `v!=q_c` in a set `N(c)`, the anchors are distinct
and occur in no other colour's provider, and `b(q_c)>=r_c`.  Then an integral
provider packing exists if and only if

\[
 \sum_{c\in T}r_c\le\sum_{v\in N(T)}b(v)
 \qquad\text{for every colour set }T.                         \tag{5.2}
\]

#### Proof

Necessity is the endpoint-cover row with `P=N(T)`.  For sufficiency, make a
flow network with arcs `source -> c` of capacity `r_c`, arcs `c -> v` when
`q_cv` is an allowed provider, and arcs `v -> sink` of capacity `b(v)`.
Condition (5.2) is precisely every finite source-side min-cut inequality.
Integral capacities give an integral maximum flow, and the private-anchor
assumption converts each used `c -> v` arc back to the seam `q_cv` without
creating any further shared capacity.  ∎

More abstractly, any provider class whose resource/endpoint constraint
matrix is totally unimodular has the same fractional-to-integral conclusion
for integral right-hand sides.
The alternating rectangle shows that no such property is automatic for
general two-endpoint provider families, even within one palette.

## 6. Exact fractional degree equality has a larger dual

The actual seam recourse relaxation requires

\[
 By=b(x),\qquad Qy\ge r(x),\qquad0\le y\le1.                 \tag{E_x}
\]

Its complete Farkas family is the following.  For every

\[
 \lambda\ge0,\qquad \pi\in\mathbb R^V,\qquad s\ge0,
 \qquad Q^T\lambda\le B^T\pi+s,                             \tag{6.1}
\]

one must have

\[
             \lambda^Tr(x)\le\pi^Tb(x)+\sum_{a\in A}s_a.    \tag{6.2}
\]

Conversely, all inequalities (6.2) imply feasibility of `(E_x)`.

Indeed, necessity follows from

\[
 \lambda^Tr\le\lambda^TQy
 \le\pi^TBy+s^Ty
 \le\pi^Tb+\sum_as_a.
\]

Sufficiency is the Farkas alternative applied to `By=b`, `-Qy<=-r`,
`y<=1`, and `-y<=0`; eliminating the multiplier of `-y<=0` gives exactly
(6.1).  Here `pi` is free because degree is an equality, and `s` pays the
upper bounds `y_a<=1`.

The endpoint-capacity Hall family is the transparent subfamily
`pi=w>=0,s=0`, after relaxing `By=b` to `By<=b`.  Thus global Hall can prove
infeasibility before the exact seam oracle, but passing it does not certify
that all freed endpoint capacity can be filled.  Even passing the exact
fractional equality dual does not eliminate Proposition 5.1's integral
alternating rectangle.

## 7. Consequence and exact boundary for radius 99

The proved advance is the following hierarchy:

\[
\begin{array}{c}
\text{canonical portal-union incidence Hall rows}\\
\subseteq\text{integral endpoint-cover rows}\\
\subseteq\text{weighted one-palette Hall--Farkas rows}\\
\subseteq\text{global lower/upper Hall--Farkas rows},
\end{array}                                                   \tag{7.1}
\]

and the audited joint-cover rows also lie in the final family by Theorem
4.1.  The final family is exactly sufficient for the fractional
endpoint-capacity relaxation `(H_x)` and is separable by one bounded LP over
the explicit seam catalogue.

Here “incidence” is essential.  The 1,328 coefficient-one singleton portal
rows from the earlier portal audit Booleanize every positive source-edge
incidence to one.  They are valid binary-master strengthenings but need not
be valid for fractional `(H_x)` and are not literally members of (7.1).  If
an internal source edge has fractional cut value `1/2`, its two endpoint
incidences free one unit of capacity, while a coefficient-one support row
charges only `1/2`; two half-provider witnesses can use the full unit.
Accordingly those Boolean rows and the fractional Hall family must be kept as
separate branches of the hierarchy.

The four-colour `6c98` inequality remains a replayable integral member of
this global family and still proves that cut impossible.  What remains
unproved is any of:

- feasibility after all freed degrees are required to be filled;
- integrality of the common-seam provider packing;
- connectivity, voltage, residence, or deeper-shadow preservation; or
- feasibility/infeasibility of either complete radius-99 branch.

No computational search or solver transcript is used in this theorem.

## 8. Replay boundary

The only frozen-catalogue facts used beyond the earlier `6c98` theorem are
the endpoint identities in (3.5) and their unit cut capacities.  They are
already reconstructed from the quotient catalogue by

```text
scratch/audit_k16_r99_fixed_delete_6c98_upper4_hall_benders_20260729.py
scratch/k16_r99_fixed_delete_6c98_upper4_hall_benders_20260729.audit.json
```

All other claims in this note are finite-dimensional Farkas, LP duality,
max-flow integrality, or the displayed symbolic counterexamples.  No local
search, SAT solve, C++ enumeration, or sustained Python job was run.
