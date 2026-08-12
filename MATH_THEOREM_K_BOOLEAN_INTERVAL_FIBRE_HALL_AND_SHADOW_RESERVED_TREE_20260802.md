# Boolean leading-letter fibres: exact Hall cuts and a shadow-reserved tree theorem

**Date:** 2026-08-02  
**Status:** unconditional exact fibre reduction, exact tight-cut obstruction,
and an unconditional shadow-reserve theorem on complete uniform containment
fibres.  The result starts after an owner/target-exact static flag table has
been fixed.  It does not construct that table or its spanning tree in a
general sparse head bank.

## 0. Outcome

For a fixed owner/target-exact depth-`d` flag table, the freedom in the
leading source letter is a Boolean interval.  However, the balance graph
does **not** see the size of that interval in the full Boolean lattice.  It
sees only those letters which occur as first letters of fixed head states
with the same literal overlap spine.

This note proves four precise statements.

1. The role--tail Hall graph is the disjoint union, over literal spines, of
   weighted Boolean-interval incidence graphs.  All degrees, codegrees and
   Hall cuts have closed forms.
2. A reserved distinct-role tree is Hall-safe exactly when its tail-use
   vector fits every residual interval cut.  In particular, a tight Hall
   shore cannot export one unit of tail capacity without deleting a role on
   that same shore.
3. On a balanced complete uniform Boolean containment fibre, every dual
   Hall cut has an exact edge-boundary formula.  Proper cuts have at least
   one unit of integral charge, and a reserved tree is Hall-safe exactly
   when it does not overspend these charges.  Lovasz--Kruskal--Katona also
   gives the additive one-sided deletion reserve `n-a-1` before the two
   shores are balanced by multiplicities.
4. Raw leading-menu degree cannot prove the needed expansion.  A literal
   one-role fibre can have `2^q` admissible leading letters and realized
   degree zero; the recursive-SCD dead flag is the canonical sparse-table
   version of the same phenomenon.

Thus the weakest useful Boolean hypothesis is **realized interval
expansion after spine conditioning**, not a lower bound on the number of
leading letters.  Upper decks, residence and common-cap constraints are not
included.

## 1. Exact spine-fibre form

Use the notation of
`MATH_THEOREM_K_FIXED_HEAD_MARKED_FLAG_BMATCHING_AND_HALL_SAFE_SPANNING_TREE_20260802.md`.
For role `i`, write its fixed suffix word as

\[
        (A_{i,1},\ldots,A_{i,d}),\qquad
        U_i=\bigcup_{t=1}^d A_{i,t},\qquad
        K_i=T_i\setminus U_i,                                \tag{1.1}
\]

and put

\[
        s_i=(A_{i,1},\ldots,A_{i,d-1}).                       \tag{1.2}
\]

For a literal `(d-1)`-spine `s` and nonempty letter `C`, let

\[
 a_s(C)=\#\{j:h_j=(C,s)\}.                                   \tag{1.3}
\]

Thus `a_s(C)` is the multiplicity of the realized head state `(C,s)`.
Let

\[
 I_s=\{i:s_i=s\},\qquad
 P_s=\{C:a_s(C)>0\}.                                         \tag{1.4}
\]

### Theorem 1.1 (weighted Boolean-interval decomposition)

The possible tail states of role `i in I_s` are precisely

\[
 N_s(i)=\{(C,s):C\in P_s,\ K_i\subseteq C\subseteq T_i\}.     \tag{1.5}
\]

Consequently:

1. the ambient number of legal leading letters is

   \[
   \#\{C:\varnothing\ne C,\ K_i\subseteq C\subseteq T_i\}
   =
   \begin{cases}
      2^{|U_i|},&K_i\ne\varnothing,\\
      2^{|T_i|}-1,&K_i=\varnothing;
   \end{cases}                                               \tag{1.6}
   \]

2. its realized weighted degree is

   \[
             \deg_a(i)=
             \sum_{\substack{C\in P_s\\K_i\subseteq C\subseteq T_i}}
                     a_s(C);                                  \tag{1.7}
   \]

3. for roles `i_1,...,i_t in I_s`, their common realized neighbours are

   \[
   \left\{(C,s): C\in P_s,\
          \bigcup_{u=1}^tK_{i_u}\subseteq C
          \subseteq\bigcap_{u=1}^tT_{i_u}\right\};           \tag{1.8}
   \]

4. balance decomposes independently over the spines.  In fibre `s` it is
   feasible if and only if

   \[
      |I_s|=\sum_C a_s(C)                                    \tag{1.9}
   \]

   and, for every `X subseteq I_s`,

   \[
      |X|\le
      \sum_{C\in\bigcup_{i\in X}[K_i,T_i]}a_s(C).             \tag{1.10}
   \]

Here `[K,T]={C:K subseteq C subseteq T}`, intersected implicitly with
`P_s`.

#### Proof

The tail of option `(B,A_{i,1},...,A_{i,d})` is `(B,s_i)`.  It can equal a
fixed head state only when the latter has the same spine.  The owner
condition is exactly

\[
 B\cup U_i=T_i
 \quad\Longleftrightarrow\quad
 K_i\subseteq B\subseteq T_i.                                \tag{1.11}
\]

This proves (1.5).  Since `T_i=K_i dotcup U_i`, counting the interval gives
(1.6), with the empty letter removed only when `K_i` is empty.  Equations
(1.7)--(1.8) follow by intersection of Boolean intervals.  No option changes
its spine, so the assignment graph is the disjoint union of the fibre
graphs.  Finally (1.9)--(1.10) are exactly total mass equality and
capacitated Hall in each fibre. \(\square\)

An equivalent dual cut form is useful.  For `Y subseteq P_s`, put

\[
 c_s(Y)=\#\{i\in I_s:[K_i,T_i]\cap P_s\subseteq Y\}.          \tag{1.12}
\]

Then (1.10) is equivalent to

\[
                         c_s(Y)\le\sum_{C\in Y}a_s(C)
                         \quad(Y\subseteq P_s).               \tag{1.13}
\]

Indeed, a violating role family may be enlarged to all roles whose entire
neighbourhood lies in its neighbour set.

## 2. Exact tree-reservation cuts

Let `R` be a set of reserved options with distinct roles, and let `b_s(C)`
be the number of those options whose tail is `(C,s)`.  Delete the reserved
roles and reduce the tail demand at `(C,s)` from `a_s(C)` to
`a_s(C)-b_s(C)`.

### Theorem 2.1 (cutwise Hall-safety)

The reservation `R` is Hall-safe if and only if, for every spine `s` and
every family `X` of unreserved roles in `I_s`,

\[
 \sum_{C\in\bigcup_{i\in X}[K_i,T_i]}b_s(C)
 \le
 \sum_{C\in\bigcup_{i\in X}[K_i,T_i]}a_s(C)-|X|.             \tag{2.1}
\]

In particular, if `X` is an unreserved role family whose pre-reservation
Hall inequality is tight, then no reserved tail unit may lie in its
neighbour set.

#### Proof

After the reservation, the capacity of the neighbour set of `X` is the
rightmost sum in (1.10) minus the left side of (2.1).  Residual Hall is
therefore exactly (2.1). \(\square\)

Define the additive fibre slack

\[
 \sigma_s=\min_{\varnothing\ne X\subseteq I_s}
 \left(
  \sum_{C\in\bigcup_{i\in X}[K_i,T_i]}a_s(C)-|X|
 \right).                                                    \tag{2.2}
\]

### Corollary 2.2 (uniform reserve)

If a certified number `q_s` satisfies `sigma_s>=q_s>=0`, then any
reservation satisfying

\[
                         \sum_C b_s(C)\le q_s                \tag{2.3}
\]

is Hall-safe in that fibre.

This criterion is intentionally one-sided: deleting reserved roles can
only help, whereas (2.3) bounds every possible loss of tail capacity.  The
cutwise form (2.1) is sharper whenever the tree tails avoid the small-slack
shores.

## 3. Boolean cut charge and upper-shadow reserve

The preceding statements use the **realized** head bank.  There is one
important face on which Boolean containment alone certifies a nonzero
slack.

### Lemma 3.1 (uniform-layer additive shadow)

Let `Q` be an `n`-set and let

\[
              0\le a<b\le\left\lfloor{n-1\over2}\right\rfloor.
                                                                    \tag{3.1}
\]

For every nonempty family `X subseteq binom(Q,a)`, its rank-`b` upper
shadow obeys

\[
          |\partial_b^+X|\ge |X|+n-a-1.                       \tag{3.2}
\]

#### Proof

First take `b=a+1`.  Complement `X` to a family
`G subseteq binom(Q,n-a)`.  Complementation identifies
`partial^+X` with the one-step lower shadow of `G`.  Write

\[
                         |G|=\binom{x}{n-a}
\]

for real `x in [n-a,n]`.  The Lovasz form of
Kruskal--Katona gives

\[
             |\partial^-G|\ge\binom{x}{n-a-1}.                \tag{3.3}
\]

On this interval the difference

\[
 \binom{x}{n-a-1}-\binom{x}{n-a}
\]

is increasing.  Indeed, with `k=n-a`,

\[
 g(x)=\binom{x}{k-1}-\binom{x}{k}
     =\binom{x}{k-1}{2k-1-x\over k},
\]

and

\[
 {g'(x)\over g(x)}
 =\sum_{j=0}^{k-2}{1\over x-j}-{1\over2k-1-x}
 \ge {k-1\over x}-{1\over2k-1-x}\ge0.
\]

The last inequality holds for `x<=2k-3+1/k`; our whole domain has
`x<=n<=2k-3`, which follows from
`a+1<=floor((n-1)/2)`.  The value at `x=k=n-a` is `n-a-1`.
This proves (3.2) at the adjacent layer.

For larger `b`, normalized matching between consecutive lower-half ranks
gives

\[
 |\partial_b^+X|/\binom nb
 \ge |\partial_{a+1}^+X|/\binom n{a+1}.
\]

The binomial coefficients are nondecreasing through rank `b`, so
`|partial_b^+X|>=|partial_{a+1}^+X|`; use the adjacent bound. \(\square\)

The additive statement has a clean one-sided consequence: if there is one
role for every member of a family in `binom(Q,a)` and one available tail
capacity at every rank-`b` upper neighbour, then deleting any at most
`n-a-1` tail vertices still leaves a matching saturating all roles.  This
is the direct higher-rank analogue of the protected-root shadow lemma.  It
is not yet an exact-demand fibre, because unused tail capacities may
remain.

For an exact-demand fibre, balance the two uniform shores as follows.  Let

\[
 D=\binom{n-a}{b-a},\qquad E=\binom ba,\qquad
 g=\gcd(D,E),\qquad p={D\over g},\qquad q={E\over g}.         \tag{3.4}
\]

The rank-`a` to rank-`b` containment graph is `(D,E)`-biregular.  Give
every rank-`a` letter `p` role copies and every rank-`b` letter `q` units
of head capacity.  The two totals agree.

For `Y subseteq binom(Q,b)`, define

\[
 Z(Y)=\{K\in\tbinom Qa:N(K)\subseteq Y\}                     \tag{3.5}
\]

and the dual Hall charge

\[
                  \kappa(Y)=q|Y|-p|Z(Y)|.                    \tag{3.6}
\]

### Theorem 3.2 (exact uniform-fibre cut charge)

For every `Y subseteq binom(Q,b)`, writing `Z=Z(Y)`,

\[
 \boxed{
 \kappa(Y)
 =q|Y\setminus N(Z)|
  +{e(\binom Qa\setminus Z,N(Z))\over g}.}                   \tag{3.7}
\]

In particular the balanced uniform containment fibre satisfies Hall.  If
the containment graph is connected, then

\[
 \kappa(Y)=0
 \quad\Longleftrightarrow\quad
 Y=\varnothing\ \hbox{ or }\ Y=\binom Qb.                    \tag{3.8}
\]

Every nontrivial dual cut therefore has at least one unit of integral
charge.  Formula (3.7) is the exact parameter-specific lower bound;
without an additional boundary estimate its universal integer consequence
is only one.

#### Proof

All edges out of `Z` enter `N(Z)`, so

\[
 D|Z|=e(Z,N(Z)).                                             \tag{3.9}
\]

The total degree entering `N(Z)` is `E|N(Z)|`.  Hence

\[
 E|N(Z)|-D|Z|
   =e\left(\binom Qa\setminus Z,N(Z)\right).                 \tag{3.10}
\]

Using `q=E/g` and `p=D/g`, split `Y` into `N(Z)` and its
complement inside `Y`; equations (3.6) and (3.10) give (3.7).
Nonnegativity is immediate and is dual Hall.  Equality forces both terms
in (3.7) to vanish.  Then `Y=N(Z)` and there is no edge from the complement
of `Z` into `N(Z)`.  By the definition of `N(Z)`, there is also no edge
from `Z` to the complement of `N(Z)`.  Connectedness leaves only the empty
and full bipartitions, proving (3.8). \(\square\)

Now reserve a distinct-role option set `R`.  Let `u_R(Y)` be the number of
its tail units in `Y`, and let `r_R(Z)` be the number of its reserved role
copies whose rank-`a` index lies in `Z`.

### Corollary 3.3 (exact Boolean tree budget)

The reserved options are Hall-safe in the balanced uniform fibre if and
only if

\[
              u_R(Y)-r_R(Z(Y))\le\kappa(Y)
              \qquad\left(Y\subseteq\binom Qb\right).        \tag{3.11}
\]

Thus a reserved tail in `Y` is free when its role is forced into `Y`; it
spends one unit of cut charge otherwise.  In particular, any projected
tree skeleton satisfying

\[
       u_R(Y)-r_R(Z(Y))\le1
       \quad\hbox{for every nonempty proper }Y               \tag{3.12}
\]

is Hall-safe.

#### Proof

After the reservation, the capacity on `Y` is `q|Y|-u_R(Y)`, while the
number of remaining roles whose complete list lies in `Y` is
`p|Z(Y)|-r_R(Z(Y))`.  Dual Hall is exactly (3.11).  Equation (3.12) and
Theorem 3.2 imply it. \(\square\)

This is the exact Boolean contribution to the desired spanning-tree
argument.  Constructing a distinct-role projected tree which obeys
(3.11), or the clean one-charge condition (3.12), is a separate
graphic/partition problem.

## 4. Why raw Boolean degrees are insufficient

### Proposition 4.1 (arbitrarily large menus with realized degree zero)

For every `q>=1` there is a literal depth-two owner/target flag role whose
ambient leading menu has size `2^q` but whose realized tail degree is zero,
even though its spine head-mass equality holds.

#### Proof

Let `U` be a `q`-set, choose `z notin U`, and take

\[
                  T=U\cup\{z\},\qquad A_1=A_2=U.              \tag{4.1}
\]

The fixed head is `(U,U)`, and the role spine is also `U`, so there is one
unit of head capacity in the correct spine fibre.  Here

\[
                  K=T\setminus(A_1\cup A_2)=\{z\}.            \tag{4.2}
\]

The legal leading letters are all sets `B` with
`z in B subseteq T`, hence there are `2^q` of them.  But the only realized
head first letter in this fibre is `U`, which omits `z`; (1.5) gives no
edge.  The fixed suffix payload is unchanged throughout, so this is a
literal owner/payload obstruction, not a set-identity artefact. \(\square\)

The recursive-SCD dead root at `(k,m,d)=(7,3,3)` is a complete-table
version: target exactness holds, but the ordered spine and bottom-letter
requirements leave a role with no legal successor.  Therefore neither
ambient degree (1.6), average containment degree, nor rankwise target
coverage implies (1.10).

## 5. Exact remaining lower-side statement

For the canonical triangular owner/target table, define its fibre slacks
by (2.2).  A proof of the lower rotor-fusion gate may now be split into two
independently checkable claims:

1. **realized Boolean expansion:** prove the exact interval cuts
   `(1.10)`, preferably with quantitative slacks `sigma_s`; and
2. **slack-respecting tree:** choose a distinct-role projected spanning
   tree whose tail-use vector satisfies the cutwise inequalities (2.1), or
   the stronger but simpler budgets (2.3).

On any complete uniform containment fibre, Theorem 3.2 proves the first
claim and discharges the matching part of the second.  Sparse canonical
head banks are not complete uniform fibres, so their actual first-letter
occupancies must still be controlled; Boolean containment degrees alone
cannot do it.

No statement here concerns arbitrary-width upper unions, residence after
opening, or maximal common-cap/compiler feasibility.
