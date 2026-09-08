# Fixed-factor rainbow completion: exact head-colour Hall min-max and the nonmatroid gate

**Date:** 2026-08-03  
**Status:** unconditional exact reduction and exact min-max formula.  The
result replaces the phrase “rainbow residual completion” by one integral
head-colour master followed by one all-subset Hall system.  It also proves
that functionality alone does not turn the selector into a Rado matroid.
No computation is used.  The Boolean all-parameter existence theorem
remains open.

## 0. Setup and outcome

Use the fixed-factor notation of
`MATH_THEOREM_FIXED_FACTOR_CAPTWO_LP_ENERGY_AND_C6_APPLICABILITY_20260803.md`.
Thus `H=G-F_0` is the residual bipartite graph between tail and head copies
of

\[
                    \mathcal M={ [2m-1]\choose m},
\]

its edges are partitioned into upper-colour classes `E_R`,
`R in mathcal U`, and

\[
 W=|\mathcal M|,qquad U=|\mathcal U|,qquad
 C=W-U=\operatorname{Cat}_m.                             \tag{0.1}
\]

Call `Q` a **rainbow base** when it is a matching and

\[
                              |Q\cap E_R|=1
                    \qquad(R\in\mathcal U).              \tag{0.2}
\]

It has size `U`.  Delete all tails and heads used by `Q`; denote the
residual shores by

\[
                         L_Q,qquad M_Q,qquad
                         |L_Q|=|M_Q|=C.                    \tag{0.3}
\]

For a residual head `T` and upper colour `R`, define the predecessor fibre

\[
 P_Q(T,R)=
 \{S\in L_Q: ST\in E(H),\ \kappa(ST)=R\}.               \tag{0.4}
\]

The exact residual completion theorem is

\[
 \boxed{
 C-\nu_{\rm rb}(H-V(Q))
 =\min_{J\in\mathfrak J_Q}
   \max_{X\subseteq L_Q}
   \bigl(|X|-|N_J(X)|\bigr),}                            \tag{0.5}
\]

where:

* `nu_rb` is maximum rainbow-matching size;
* `mathfrak J_Q` is the set of all partial matchings between residual heads
  and upper colours using only nonempty fibres `(T,R)`; and
* 

  \[
  N_J(X)=\{(T,R)\in J:P_Q(T,R)\cap X\ne\varnothing\}.
                                                                  \tag{0.6}
  \]

The inner maximum is nonnegative because `X=emptyset` is allowed.

Consequently `Q` admits a rainbow residual perfect matching if and only if
there is a head-colour matching `J` satisfying

\[
                     |N_J(X)|\ge |X|
                    \qquad(X\subseteq L_Q).              \tag{0.7}
\]

At `X=L_Q`, (0.7) forces `|J|=C`; hence such a `J` automatically uses every
residual head and `C` distinct upper colours.

Combining (0.5) with the rainbow-base decomposition gives the exact
fixed-factor criterion

\[
\boxed{
\begin{aligned}
&\text{a cap-two second perfect matching exists}\\
&\quad\Longleftrightarrow\quad
\exists\text{ rainbow base }Q\ \exists J\in\mathfrak J_Q
\ \forall X\subseteq L_Q:\ |N_J(X)|\ge|X|.
\end{aligned}}                                           \tag{0.8}
\]

This is the requested all-subset condition.  It is exact, but the choice
of `Q` and the integral head-colour master `J` remain correlated.

## 1. Exact characterization of the rainbow base itself

Before choosing `Q`, define the full predecessor fibres

\[
 P(T,R)=\{S\in\mathcal M:ST\in E(H),\ \kappa(ST)=R\},    \tag{1.1}
\]

and let

\[
 \mathcal A=\{(T,R):P(T,R)\ne\varnothing\}.             \tag{1.2}
\]

A set `D subseteq mathcal A` is a **head-colour base master** when it uses
every upper colour exactly once and every head at most once:

\[
 |D\cap(\mathcal M\times\{R\})|=1\quad(R\in\mathcal U),
 \qquad
 |D\cap(\{T\}\times\mathcal U)|\le1\quad(T\in\mathcal M).
                                                                  \tag{1.3}
\]

For `X subseteq mathcal M`, put

\[
 B_X=\{(T,R)\in\mathcal A:P(T,R)\subseteq X\}.          \tag{1.4}
\]

### Theorem 1.1 (exact base-master Hall criterion)

A head-colour base master `D` lifts to a rainbow base `Q` if and only if

\[
                              |D\cap B_X|\le |X|
                    \qquad(X\subseteq\mathcal M).        \tag{1.5}
\]

Equivalently, for every `D' subseteq D`,

\[
                         \left|\bigcup_{a\in D'}P(a)\right|
                         \ge |D'|.                       \tag{1.6}
\]

### Proof

Make a bipartite graph between the selected columns `D` and the tail shore,
joining column `a=(T,R)` to every tail in `P(a)`.  A matching saturating
`D` selects one distinct tail for each column.  Together with its already
fixed distinct heads and colours, those selected occurrences form exactly a
rainbow base `Q`.  Thus (1.6) is Hall's theorem.

Condition (1.6) implies (1.5), because every column in `D cap B_X` has all
of its neighbours in `X`.  Conversely, if (1.6) fails for `D'`, put
`X=union_(a in D') P(a)`.  Then `D' subseteq D cap B_X`, so (1.5) fails.
Hence the two forms are equivalent. \(\square\)

Theorem 1.1 removes a second ambiguity: existence of `Q` is itself one
integral head-colour matching plus one exact fibre-Hall system.  The
separate colour-tail and colour-head SDRs prove the two marginals, not the
common master (1.3)--(1.5).

## 2. Fixed-`Q` residual min-max

Let

\[
 \mathcal A_Q=\{(T,R):T\in M_Q,\ P_Q(T,R)\ne\varnothing\}. \tag{2.1}
\]

A member `J of mathfrak J_Q` is any matching in the bipartite graph between
`M_Q` and `mathcal U` with edge set `mathcal A_Q`; it may be partial.

For fixed `J`, make the bipartite graph

\[
                         B_Q(J)=(L_Q,J;E_J),             \tag{2.2}
\]

where `S` is adjacent to `(T,R)` precisely when `S in P_Q(T,R)`.

### Lemma 2.1 (column lifting)

Matchings of `B_Q(J)` are in bijection with rainbow matchings in the
residual graph whose head-colour columns lie in `J`.

### Proof

An edge `S--(T,R)` of `B_Q(J)` is exactly the residual occurrence `ST` of
colour `R`.  Distinct matched tails are automatic.  Since `J` has distinct
heads and distinct colours, a matching of `B_Q(J)` also has distinct heads
and colours, hence is rainbow in `H-V(Q)`.

Conversely, a residual rainbow matching produces distinct pairs
`(T,kappa(ST))`; they form a head-colour matching `J`, and the original
tails match to those columns in `B_Q(J)`. \(\square\)

### Theorem 2.2 (exact residual deficiency)

Equation (0.5) holds.

### Proof

For fixed `J`, the defect form of Hall's theorem gives

\[
 \nu(B_Q(J))
 =|L_Q|-\max_{X\subseteq L_Q}
       \bigl(|X|-|N_J(X)|\bigr).                         \tag{2.3}
\]

Here `|L_Q|=C`.  By Lemma 2.1, maximizing the left side over all
head-colour matchings `J` gives the maximum residual rainbow-matching size.
Subtracting from `C` converts the outer maximum to the outer minimum and
proves (0.5). \(\square\)

Thus the exact selector deficiency may be frozen as

\[
 \delta_{\rm cap}(F_0)=
 \begin{cases}
 \displaystyle
 \min_{Q\in\mathfrak Q(F_0)}
 \min_{J\in\mathfrak J_Q}
 \max_{X\subseteq L_Q}
 \bigl(|X|-|N_J(X)|\bigr),&\mathfrak Q(F_0)\ne\varnothing,\\[4mm]
 +\infty,&\mathfrak Q(F_0)=\varnothing,
 \end{cases}                                             \tag{2.4}
\]

where `mathfrak Q(F_0)` is the family of rainbow bases.  The cap-two gate is
equivalent to

\[
                         \delta_{\rm cap}(F_0)=0.        \tag{2.5}
\]

## 3. Exact matroid content—and where it stops

On the column ground set `mathcal A_Q`, the predecessor fibres define a
transversal matroid `M_tail(Q)`.  Its rank is

\[
 r_{\rm tail}(Y)=
 \min_{Z\subseteq Y}
 \left(|Y\setminus Z|+left|\bigcup_{a\in Z}P_Q(a)\right|\right).
                                                                  \tag{3.1}
\]

Let `M_head(Q)` and `M_col(Q)` be the partition matroids imposing at most
one selected column per residual head and per upper colour.  Lemma 2.1 gives

\[
 \boxed{
 \nu_{\rm rb}(H-V(Q))
 =\max\{|J|:J\in
 I(M_{\rm tail}(Q))\cap I(M_{\rm head}(Q))
                  \cap I(M_{\rm col}(Q))\}.}            \tag{3.2}
\]

This is a common-independent-set problem for **three** matroids.  Rado's
theorem supplies (3.1), but ordinary Edmonds two-matroid intersection does
not combine the other two crossing partition rows.  Formula (0.5) is the
exact integral master-plus-Rado decomposition: choose `J` in the
head-colour matching system, then evaluate its transversal-matroid defect.

There are two genuine Rado faces.

1. If the head-colour matching `J` is fixed, (0.7) is ordinary Hall/Rado
   and is necessary and sufficient.
2. If a construction gives every admitted column a private tail, then
   `M_tail(Q)` is free on those columns, and only the ordinary head-colour
   bipartite matching remains.

Neither property follows from functional upper-colour classes alone.

## 4. Boolean functional specialization

For `R in mathcal U`, index its facets by

\[
                              S_b=R-\{b\}\qquad(b\in R),
\]

and recall the loopless functional map

\[
                              p_R(b)=a(S_b).
\]

The colour-`R` arc is

\[
                              S_b\longrightarrow S_{p_R(b)}.
                                                                  \tag{4.1}
\]

Therefore the predecessor fibre in (1.1) is exactly

\[
 P(S_c,R)=\{S_b:b\in R,\ p_R(b)=c\},                    \tag{4.2}
\]

and the residual fibre is its restriction to unused tails and heads.
Equations (1.5) and (0.7) are consequently explicit all-subset statements
about fibres of the Boolean maps `p_R`; no anonymous occurrence relation
remains.

If every `p_R` were a permutation, each nonempty fibre in (4.2) would be a
singleton.  Even then the task would be to choose head-colour columns whose
forced predecessor tails are distinct.  Thus local injectivity of every
functional class does not by itself synchronize the global columns.  The
Steiner parity theorem already shows that this permutation shortcut is
unavailable for even `m`; the next section shows that permutation
functionality would not be a generic three-coordinate integrality theorem
anyway.

## 5. Sharp abstract obstructions to a generic Rado collapse

These examples are abstract functional occurrence systems.  They are not
asserted to embed in one Boolean fixed factor.

### Proposition 5.1 (minimal colour-task nonmatroid)

Let the three colour classes consist of the single occurrences

\[
 e_a=(s_0,t_0),\qquad
 e_b=(s_0,t_1),\qquad
 e_c=(s_1,t_0),                                          \tag{5.1}
\]

with `s_0!=s_1` and `t_0!=t_1`.  Let a colour set be independent when it
has a rainbow matching.  Then

\[
                         A=\{a\},\qquad B=\{b,c\}       \tag{5.2}
\]

are independent, `|A|<|B|`, but neither `A+{b}` nor `A+{c}` is independent.
Hence the rainbow-matchable colour subsets do not form a matroid, a
gammoid, or a Rado matroid in general.

### Proof

The two occurrences of colours `b,c` are disjoint, so `B` is matchable.
The occurrence of `a` shares its tail with `b` and its head with `c`, so
neither augmentation is matchable.  This violates the matroid augmentation
axiom. \(\square\)

Full functional colour classes can be padded by occurrences incident with
vertices later removed by `Q`, leaving (5.1) in the residual graph.  This
shows why functionality of the pre-residual classes alone cannot prove a
Rado rank formula.  It does not prove that a Boolean rainbow base can create
this exact residual gadget.

### Proposition 5.2 (permutation-functional parity obstruction)

Let each of three shores be `{0,1}` and retain the four even-parity atoms

\[
                  000,\qquad011,\qquad101,\qquad110.    \tag{5.3}
\]

Every two-shore projection is `K_(2,2)`, each colour acts as a permutation
from tails to heads, and weight `1/2` on every atom gives unit load on all
six vertices.  Nevertheless there is no two-edge rainbow perfect matching.

### Proof

Two disjoint triples would have to be coordinatewise complements.  The
complement of an even-parity triple has odd parity and is absent.

Equivalently, the two head-colour perfect matchings are

\[
 \{(t_0,c_0),(t_1,c_1)\},\qquad
 \{(t_0,c_1),(t_1,c_0)\}.
\]

In the first choice both columns have sole predecessor `s_0`; in the second
both have sole predecessor `s_1`.  Each violates (0.7) on a singleton tail
cut. \(\square\)

This parity gadget is stronger than a marginal-Hall counterexample but is
still not a Boolean counterexample: it does not have the Boolean layer
sizes, colour-facet overlap pattern, or simultaneous root-map consistency,
and one of its two permutation classes has fixed points under the displayed
tail/head identification.

## 6. Exact surviving Boolean target

The cap-two selector problem for a fixed Boolean `F_0` is now exactly:

1. choose a head-colour base master `D` satisfying (1.3) and every fibre
   cut (1.5), then choose its tail lift `Q`;
2. in the residual Boolean fibres (4.2), choose a head-colour matching `J`
   satisfying every tail cut (0.7).

No separate marginal SDR, fractional cap point, or potential-C6 count
implies either correlated step.  Conversely, these two integral Hall
systems are sufficient and produce the cap-two second matching

\[
                              F=Q\mathbin{\dot\cup}P.
\]

The exact missing Boolean theorem can therefore be stated without vague
completion language:

> **Boolean functional two-stage Hall theorem.**  For some (or every)
> fixed first factor `F_0`, there is a base master `D` satisfying (1.5) and
> a tail lift `Q` such that the residual functional-fibre system admits a
> head-colour matching `J` satisfying (0.7).

Proving this theorem gives the cap-two second factor.  The examples in
Section 5 show that it cannot follow from abstract functionality or pairwise
Hall alone; a proof must use the global Boolean overlap among the maps
`p_R`, an absorber/exchange theorem within that host, or a private-fibre
support constructed before the two Hall stages.
