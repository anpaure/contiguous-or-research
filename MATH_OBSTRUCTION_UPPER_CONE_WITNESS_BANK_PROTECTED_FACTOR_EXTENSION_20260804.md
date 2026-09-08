# Upper-cone witness banks need not extend to a Middle-Levels two-factor

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical obstruction and exact cut
criterion.  It shows that one upper cone, `o(W)` protected incidence edges,
maximum degree two, and one literal avoiding path per target do not suffice
for extension to a spanning two-factor of `ML_m`.

## 0. Result

Let `ML_m` be the balanced `m`-regular containment graph between

\[
 \mathcal L={ [2m-1]\choose m-1},
 \qquad
 \mathcal U={ [2m-1]\choose m},
 \qquad
 W=|\mathcal L|=|\mathcal U|.
\]

For every `m>=4` there is an explicit subgraph `P subset ML_m` such that:

1. `P` is a vertex-disjoint union of owner paths and `Delta(P)<=2`;
2. every path avoids one fixed lower hinge `x`;
3. there is one path for each of `m-1` distinct upper targets, all lying in
   one Boolean cone above one rank-`m+1` base;
4. the union of each path is its assigned target;
5. `|E(P)|=6m-8=o(W)`; but
6. no spanning two-factor of `ML_m` contains `P`.

Thus no large protected-factor theorem can follow from upper-cone
localization, sublinear size, and maximum degree two alone.

## 1. Exact residual Ore--Ryser criterion

Let `P subset ML_m` have maximum degree at most two.  For
`A subseteq mathcal L` and `U in mathcal U`, put

\[
 a_U=d_{ML_m}(U,A),
 \qquad
 p_U=e_P(U,\mathcal L\setminus A).
\tag{1.1}
\]

### Theorem 1.1

The protected graph `P` extends to a spanning two-factor of `ML_m` if and
only if, for every `A subseteq mathcal L`,

\[
 \boxed{
 \sum_{U\in\mathcal U}\min\{2-p_U,a_U\}\ge2|A|.}
\tag{1.2}
\]

Equivalently, with

\[
 S_2(A)=\sum_U\min\{2,a_U\},
 \qquad
 \sigma(A)=S_2(A)-2|A|,
\tag{1.3}
\]

one must have

\[
 \boxed{
 \lambda_P(A):=
 \sum_U\left(\min\{2,a_U\}
 -\min\{2-p_U,a_U\}\right)
 \le\sigma(A).}
\tag{1.4}
\]

#### Proof

Delete the protected edges and prescribe residual degree

\[
                         b(v)=2-d_P(v).
\]

The total residual demand is equal on the two shores.  The bipartite
capacitated matching criterion says that a residual `b`-factor exists if
and only if, for every `A subseteq mathcal L`,

\[
 \sum_{L\in A}b(L)
 \le\sum_{U\in\mathcal U}
 \min\{b(U),d_{ML_m-P}(U,A)\}.
\tag{1.5}
\]

Let

\[
 q_U=e_P(U,A).
\]

Then

\[
 b(U)=2-p_U-q_U,
 \qquad
 d_{ML_m-P}(U,A)=a_U-q_U,
\]

and

\[
 \sum_{L\in A}b(L)=2|A|-\sum_Uq_U.
\]

For each owner,

\[
 \min\{2-p_U-q_U,a_U-q_U\}+q_U
 =\min\{2-p_U,a_U\}.
\]

Adding `sum_U q_U` to both sides of (1.5) gives exactly (1.2).
Subtracting (1.2) from the unprotected capacity `S_2(A)` gives (1.4).
\(\square\)

The protected loss has the explicit local form

\[
 \min\{2,a_U\}-\min\{2-p_U,a_U\}
 =
 \begin{cases}
 0,&a_U=0,\\
 1_{\{p_U=2\}},&a_U=1,\\
 p_U,&a_U\ge2.
 \end{cases}
\tag{1.6}
\]

Thus an owner with only one neighbour in `A` harms the cut precisely when
both of its protected incidences enter from the opposite shore.

## 2. The sharp singleton obstruction

Fix `x in mathcal L`.  It has exactly `m` neighbours in `mathcal U`.  For
`A={x}`, every neighbouring owner has `a_U=1`, so

\[
 S_2(A)=m,
 \qquad
 \sigma(A)=m-2.
\tag{2.1}
\]

Consequently (1.4) requires

\[
 \boxed{
 \#\{U\supset x:p_U=2\}\le m-2.}
\tag{2.2}
\]

This is sharp at the singleton cut.  Saturating `m-1` owner-neighbours of
`x` using only protected incidences from `mathcal L\setminus\{x\}` leaves
residual capacity one for the residual demand two at `x`.

## 3. A one-cone avoiding-path counterexample

Assume `m>=4`.  Fix

\[
 x\in\mathcal L,
 \qquad
 Z=[2m-1]\setminus x,
 \qquad |Z|=m.
\]

Choose distinct

\[
                         z_*,w\in Z
\]

and distinct

\[
                         a,b,t\in x.
\]

Put

\[
                         U_0=x\cup\{z_*,w\},
 \qquad |U_0|=m+1.
\tag{3.1}
\]

For every `z in Z\setminus\{z_*\}`, define the central owner and two
lower facets

\[
 Y_z=x\cup\{z\},
 \qquad
 I_z=(x\setminus\{a\})\cup\{z\},
 \qquad
 K_z=(x\setminus\{b\})\cup\{z\},
\tag{3.2}
\]

and the two outer owners

\[
 L_z=I_z\cup\{z_*\},
 \qquad
 R_z=K_z\cup\{z_*\}.
\tag{3.3}
\]

For `z=w`, take the owner path

\[
                         L_w-I_w-Y_w-K_w-R_w.
\tag{3.4}
\]

Its union is `U_0`.  For `z notin {z_*,w}`, also put

\[
 M_z=(x\setminus\{a,t\})\cup\{z,z_*\},
 \qquad
 H_z=M_z\cup\{w\},
\tag{3.5}
\]

and take the extended owner path

\[
 H_z-M_z-L_z-I_z-Y_z-K_z-R_z.
\tag{3.6}
\]

Its union is

\[
                         T_z=U_0\cup\{z\}.
\tag{3.7}
\]

Assign target `T_w=U_0` to (3.4), and target `T_z` to (3.6).  Every target
lies in the single cone

\[
                         \{T:U_0\subseteq T\subseteq[2m-1]\}.
\]

### Lemma 3.1

The displayed objects form `m-1` pairwise vertex-disjoint literal Johnson
owner paths.  None uses the lower vertex `x`, their target unions are as
claimed, and their incidence union `P` satisfies

\[
                         \Delta(P)\le2,
 \qquad
                         |E(P)|=6m-8.
\tag{3.8}
\]

#### Proof

Every consecutive owner pair in (3.4)--(3.6) differs by one coordinate and
has the displayed rank-`m-1` intermediate intersection.  The lower vertices
`I_z,K_z,M_z` all omit at least one element of `x`, so none equals `x`.

For distinct parameters `z`, the vertices are distinguished by their
outside label `z`.  Within one parameter, the types are distinguished by
which of `a,b,t` are omitted and whether `z_*` and `w` are present.  Hence
different paths are vertex-disjoint.  Internal path vertices have degree
two and endpoints degree one.

Path (3.4) has four incidence edges.  Each of the other `m-2` paths has six,
so

\[
                         |E(P)|=4+6(m-2)=6m-8.
\]

The path unions follow directly from (3.2)--(3.7).  \(\square\)

Since `W=binom(2m-1,m)`, equation (3.8) is `o(W)`.

## 4. Failure of two-factor extension

Apply Theorem 1.1 to `A={x}`.  For every

\[
                         z\in Z\setminus\{z_*\},
\]

the owner `Y_z=x+z` has its two protected incidences `I_zY_z` and
`K_zY_z`, both entering from `mathcal L\setminus\{x\}`.  Thus

\[
                         p_{Y_z}=2
\]

for `m-1` neighbours of `x`.  The remaining neighbour

\[
                         Y_{z_*}=x\cup\{z_*\}
\]

has `p=0`.  Therefore the right side of (1.2) is exactly

\[
 (m-1)\min\{0,1\}+\min\{2,1\}=1,
\]

while its left side is `2|A|=2`.  The Ore--Ryser inequality fails by one.
No spanning two-factor of `ML_m` contains `P`.

Equivalently,

\[
                         \lambda_P(\{x\})=m-1
 >m-2=\sigma(\{x\}).
\]

## 5. Exact surviving gate

Cone localization does not control protected cut loss.  A valid tailored
extension theorem must impose, or prove from its path-selection rule, the
full family of inequalities

\[
 \lambda_P(A)\le S_2(A)-2|A|
 \qquad(A\subseteq\mathcal L).
\]

At minimum it must forbid the singleton-star concentration (2.2).  This
condition alone is not claimed sufficient for larger cuts; Theorem 1.1 is
the exact necessary-and-sufficient test.

The small protected-factor theorem remains valid because its global
`m-2` edge budget bounds every possible protected cut loss.  The present
counterexample has only `O(m)` edges but deliberately exceeds that local
cut budget while remaining `o(W)`.

## 6. Frozen dependency

The Middle-Levels setup and small protected-factor theorem are frozen in

`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`,
SHA256
`1deded37f83351f0750e633b8e771bc364159d7b979c21d21c5c306573b5f17f`.

The obstruction above uses only the standard exact bipartite capacitated
matching criterion and literal set identities.
