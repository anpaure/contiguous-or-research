# Exact Ore gate and independent algebra audit for the all-width odd `C8` collar

**Date:** 2026-08-12
**Method:** direct degree ledger, Ore--Ryser, and literal prefix-union replay
**Status:** unconditional reduction and independent self-audit.  The local
all-width collar passes.  Its direct extension is equivalent to one explicit
family of residual capacity inequalities below.  The separate theorem
`MATH_THEOREM_COMMON_MATE_C8_ALLWIDTH_COLLAR_SPANNING_PHASED_HOST_20260812.md`
closes the host gate by adjoining an explicit two-transition phase closure
and proving the stronger closed bank extendable for `m>=12`.

## 1. The protected bank

Use the notation and the four old paths of Theorem 7.1 in
`MATH_THEOREM_COMMON_MATE_C8_ONE_STEP_COLLAR_Q2_Q3_ZERO_ODD_SOCKET_20260812.md`.
Thus `H=m-3`, and each path has upper-owner sequence

\[
 R_i,U_i,W_{i,1},\ldots,W_{i,H},G_{i,1},G_{i,2},F_i.
 \tag{1.1}
\]

Let `P` be the union of the four alternating incidence paths, and let `X`
be its lower shore.  Let `I` be the internal upper-owner bank and `E` the
endpoint upper-owner bank.  Directly from (1.1),

\[
\begin{array}{c|c|c}
\text{bank}&\text{cardinality}&d_P\\ \hline
X&4(m+1)=4m+4&2\\
I&4m&2\\
E=\{R_i,F_i:i\in\mathbb Z_4\}&8&1.
\end{array}                                                   \tag{1.2}
\]

All other vertices have protected degree zero, and hence

\[
                         |E(P)|=8m+8.                         \tag{1.3}
\]

The four proposed switched incidences are

\[
                         N=\{L_iR_{i-1}:i\in\mathbb Z_4\}.    \tag{1.4}
\]

Every lower endpoint `L_i` in (1.4) belongs to `X` and is already saturated
by `P`.  Therefore **every** two-factor containing `P` automatically avoids
`N`; the forbidden bank costs no additional residual capacity.

## 2. Exact residual Ore--Ryser criterion

For `A subseteq mathcal L-X` and `U in mathcal U`, put

\[
                         a_U=|N(U)\cap A|.                     \tag{2.1}
\]

The residual demand on every lower vertex of `mathcal L-X` is two.  The
residual capacities on the upper shore are

\[
 b(U)=2-d_P(U)=
 \begin{cases}
 0,&U\in I,\\
 1,&U\in E,\\
 2,&U\notin I\cup E.
 \end{cases}                                                   \tag{2.2}
\]

No protected edge has a lower endpoint outside `X`, so deleting `P` does
not change the incidences from `A`.  Ore--Ryser consequently gives the
following exact criterion.

### Theorem 2.1 (large-collar host gate)

The all-width collar `P` extends to a spanning two-factor of `ML_m` if and
only if, for every `A subseteq mathcal L-X`,

\[
 \boxed{
  2|A|\le
  \sum_{U\notin I\cup E}\min\{2,a_U\}
  +\sum_{U\in E}\min\{1,a_U\}.}
 \tag{2.3}
\]

Equivalently, with

\[
 S_2(A)=\sum_U\min\{2,a_U\},                         \tag{2.4}
\]

the criterion is

\[
 \boxed{
 \Omega_P(A):=
 \sum_{U\in I}\min\{2,a_U\}
 +|\{U\in E:a_U\ge2\}|
 \le S_2(A)-2|A|.}
 \tag{2.5}
\]

#### Proof

After fixing `P`, a completion is a bipartite `b`-matching with demand two
on `mathcal L-X` and capacities (2.2) on the upper shore.  Its total demand
and capacity both equal

\[
                         2W-(8m+8).                          \tag{2.6}
\]

The capacitated Hall/Ore--Ryser inequalities are exactly (2.3).  Subtract
its right side from (2.4).  An internal owner loses
`min{2,a_U}` units.  An endpoint loses zero for `a_U=0,1` and one for
`a_U>=2`.  This gives (2.5).  The preceding observation about (1.4) proves
that no forbidden-edge term occurs. `square`

Thus the bank size `8m+8` is not itself the obstruction.  The only possible
obstruction is concentration of the ordinary middle-shadow slack on the
explicit `4m` internal owners and eight endpoints.

## 3. Immediate safe cuts and exact remaining inequality

The empty cut and the full residual cut `A=mathcal L-X` satisfy (2.3) with
equality.  Indeed, the latter uses every available upper capacity in
(2.2).  More generally, the standard protected-Ore identities imply that
any failed cut must satisfy

\[
 \Omega_P(A)>S_2(A)-2|A|,                            \tag{3.1}
\]

and hence is a near-tight middle-shadow cut.  In the notation of the exact
shadow-slack identity,

\[
 (m-1)\bigl(S_2(A)-2|A|\bigr)
 =(m-2)(|N(A)|-|A|)+b(A).                            \tag{3.2}
\]

Therefore any failed cut obeys the fully explicit inequality

\[
 \boxed{
 (m-2)(|N(A)|-|A|)+b(A)
 <(m-1)\Omega_P(A).}
 \tag{3.3}
\]

This is the exact unresolved row.  It is substantially narrower than a
generic protected-factor theorem: `A` avoids the named lower bank `X`, and
`Omega_P` is supported on only the named owner paths (1.1).  Conversely,
proving the reverse weak inequality in (3.3) for every such `A` proves the
spanning two-factor host.

There is an equivalent complement form which is sometimes sharper.  Write

\[
 A=\mathcal L\setminus(X\cup Y),\qquad
 Y\subseteq\mathcal L\setminus X,                  \tag{3.4}
\]

and put `r_U=|N(U) cap (X union Y)|`.  Relative to the full residual cut
`mathcal L-X`, the lost usable capacity is exactly

\[
\begin{aligned}
 D_X(Y)={}&
 \sum_{U\notin I\cup E}(r_U-(m-2))_+\\
 &+|\{U\in E:N(U)\subseteq X\cup Y\}|.             \tag{3.5}
\end{aligned}
\]

The cut (3.4) is safe if and only if

\[
                         \boxed{D_X(Y)\le2|Y|.}     \tag{3.6}
\]

Indeed an ordinary upper vertex has residual capacity two and loses
`2-min(2,m-r_U)=(r_U-(m-2))_+` units.  An endpoint has capacity one and
loses it exactly when all its facets lie in `X union Y`; an internal owner
has capacity zero and loses nothing.  The full residual cut has balanced
capacity and demand, and removing `Y` lowers demand by `2|Y|`, proving
(3.6).

Thus a counter-cut is equivalently a family `Y` whose union with the
explicit lower collar bank almost fills too many ordinary owner stars, or
completely fills too many endpoint stars.

No abstract matroid-intersection theorem removes (3.3).  Once a two-factor
exists, its two alternating colour classes are the required ordered two-SDR;
the issue is precisely existence of that factor through this linear-size
partial bank.

## 4. Independent replay of the all-width algebra

This section checks Theorem 7.1 without invoking its prose proof.

For an incoming socket `R_i`, put

\[
 T_i=C+c+q_i+q_{i+1}+q_{i+2}.                       \tag{4.1}
\]

The old output index is `i`, and the switched output index is `i+1`.
For every `0<=j<=H`, the cumulative unions through the neutral rail are

\[
\begin{aligned}
 R_i\cup U_i\cup W_{i,1}\cup\cdots\cup W_{i,j}
 &=T_i+\{z_1,\ldots,z_j\},\\
 R_i\cup U_{i+1}\cup W_{i+1,1}\cup\cdots\cup W_{i+1,j}
 &=T_i+\{z_1,\ldots,z_j\}.
\end{aligned}                                       \tag{4.2}
\]

After the complete neutral rail the common prefix contains `C`, `c`, all
of `Z`, and every active coordinate except `q_(i+3)`.  Passing to
`G_(i,1)` or `G_(i+1,1)` only exchanges a core tag for a label already in
`Z`, so the cumulative union remains equal.

The two bridge pairs are

\[
 \{q_{i+2},q_{i+3}\},\qquad
 \{q_{i+3},q_i\}.                                   \tag{4.3}
\]

Their unique coordinate missing from `T_i` is the same label `q_(i+3)`.
Because the `alpha/beta` order is determined by the global parity of the
label, this missing coordinate is introduced at the same one of the two
remaining bridge steps on both outputs.  Hence cumulative prefix unions
remain equal through `G_2` and `F`.

At `F` that cumulative union is

\[
 C\cup Z\cup\{q_0,q_1,q_2,q_3,c\}=[2m-1].          \tag{4.4}
\]

Thus every crossing owner interval ending inside the collar has identical
union in both phases, and every crossing interval continuing beyond it is
already the full ground set.  Noncrossing intervals are unchanged.  This
replays exact all-width transparency.

The bridge facets are

\[
\begin{aligned}
 &(C-t_i)+q_{i+1}+z_{H-1}+z_H,\\
 &(C-t_i)+q_{i+1}+z_H+d_i,\\
 &(C-t_i)+q_{i+1}+\alpha_i+d_i.
\end{aligned}                                       \tag{4.5}
\]

Distinct missing-core tags separate different `i`; missing a core tag
separates every bridge facet and owner from the neutral bank; and the three
outside triples in (4.5) are distinct.  This checks the simple lower
palette and the owner/path simplicity.  Four distinct `t_i` and four
distinct `d_i in Z-{z_(H-1),z_H}` exist for `m>=9`, which is the concrete
threshold hidden in “sufficiently large”.

Finally, the switched paths send `R_i` to `F_(i+1)`, so their socket action
is the odd four-cycle.  The local algebra, q1 simplicity, all-width deck,
and parity rows therefore pass independently.

## 5. Current verdict

The local all-width odd actuator is valid.  For the unclosed bank, the
direct Ore assertion is exactly

\[
 \boxed{
 \Omega_P(A)\le S_2(A)-2|A|
 \quad\text{for every }A\subseteq\mathcal L-X.}
 \tag{5.1}
\]

The companion spanning-host theorem proves a stronger statement: adjoining
one owner `H_i=(C-t_i) union {q_0,q_1,q_2,q_3}` closes each of the four
paths in two Johnson transitions, and the resulting larger bank extends to
a spanning two-factor for every `m>=12`.  Hence (5.1) follows a posteriori
in that range.  Residence and the recursive/common-cap interface remain
separate gates.
