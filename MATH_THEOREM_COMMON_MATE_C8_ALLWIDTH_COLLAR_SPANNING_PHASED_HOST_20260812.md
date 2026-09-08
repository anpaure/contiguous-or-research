# The all-width odd `C8` collar has a spanning phased middle-levels host

**Date:** 2026-08-12
**Method:** explicit two-step phase closure, bounded exposure, protected-Ore
localization, and sharp partial shadows
**Status:** unconditional for every `m>=12`.  This proves the abstract
ordered-two-SDR host for the all-width collar.  It does not prove residence,
recursive MNW terminal identification, or the lower/common-cap compiler.

## 1. Input collar

Use the notation of Theorem 7.1 in
`MATH_THEOREM_COMMON_MATE_C8_ONE_STEP_COLLAR_Q2_Q3_ZERO_ODD_SOCKET_20260812.md`.
In particular, `C` has rank `m-3`,

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m},\qquad
 W=|\mathcal L|=|\mathcal U|,
 \tag{1.0}
\]

\[
 Q=\{q_0,q_1,q_2,q_3\},                             \tag{1.1}
\]

and the old path with index `i` runs from `R_i` through the complete
all-width outgoing collar to `F_i`.  Its incidence edges are properly
coloured `0,1,0,1,...`, beginning with the phase-zero edge `R_iL_i`.
For `m>=12`, the core and fresh bank both have enough labels for the four
distinct `t_i` and the four distinct `d_i` required there.

The local theorem proves that the phase-zero switch

\[
                         L_iR_i\longmapsto L_iR_{i-1}           \tag{1.2}
\]

has zero owner-window current at every width and acts on the four outgoing
sockets by the odd cycle `i -> i+1`.

## 2. An explicit two-transition phase closure

Define one more rank-`m` owner on path `i` by

\[
                         H_i=(C-t_i)\cup Q.                     \tag{2.1}
\]

Recall that

\[
 F_i=(C-t_i)\cup(Q-\{q_i\})\cup\{d_i\},             \tag{2.2}
\]

whereas

\[
 R_i=C\cup(Q-\{q_{i+3}\}).                          \tag{2.3}
\]

Consequently

\[
 F_i\longrightarrow H_i\longrightarrow R_i          \tag{2.4}
\]

is a two-transition Johnson path: the first transition replaces `d_i` by
`q_i`, and the second replaces `q_(i+3)` by `t_i`.  Its lower colours are

\[
\begin{aligned}
 J_i^0&=(C-t_i)\cup(Q-\{q_i\}),\\
 J_i^1&=(C-t_i)\cup(Q-\{q_{i+3}\}).
\end{aligned}                                       \tag{2.5}
\]

The private missing-core label `t_i` separates different indices.  Neither
colour in (2.5) is an old bridge colour, because every old bridge colour
contains one of the private `Z` labels.  The owners `H_i` are new and
pairwise distinct for the same reason.

Thus adjoining (2.4) closes the four old paths into four pairwise
vertex-disjoint incidence cycles.  The added incidence path has four edges,
so its alternating colours begin with phase zero at `F_i` and end with
phase one at `R_i`, exactly complementing the old endpoint colours.  Hence
the four cycles retain the prescribed phase of every old edge.

Let `P^circ` denote this four-cycle bank, and let
`mathcal Z(P^circ)` be its protected lower shore.  It has

\[
 |\mathcal Z(P^\circ)|=4m+12,\qquad
 |E(P^\circ)|=8m+24,                                \tag{2.6}
\]

and every protected lower and upper vertex has degree two.

The added closure does not alter all-width transparency.  The incoming arc
`H_i-R_i` is fixed, and the prefix proof of Theorem 7.1 allowed an arbitrary
unchanged suffix before `R_i`.  In the other direction, any crossing
interval which reaches `F_i` has already accumulated the full ground set,
so extending it through `H_i` and back to `R_i` leaves its union full in
both phases.

## 3. Exact exposure bound

For a degree-two protected bank put

\[
\begin{aligned}
 \mathcal Z(P)&=\{x\in\mathcal L:d_P(x)=2\},\\
 \alpha(P)&=\max_{x\notin\mathcal Z(P)}
 |\{U:x\subset U,\ d_P(U)>0\}|,\\
 \beta(P)&=\max_U|N(U)\cap\mathcal Z(P)|.
\end{aligned}                                       \tag{3.1}
\]

### Lemma 3.1

For the closed collar,

\[
                         \boxed{\alpha(P^\circ)\le4,
                         \qquad\beta(P^\circ)\le4.}            \tag{3.2}
\]

#### Proof

Put

\[
 D=[2m-1]\setminus C=Q\cup\{c\}\cup Z.             \tag{3.3}
\]

The protected lower colours containing the full core `C` are `C` plus an
edge of the graph on `D` consisting of

* the four cyclic edges on `Q`;
* the four edges `cq`, `q in Q`; and
* the edges `qz_j`, `q in Q`, `1<=j<H`.

Every three-set spans at most three edges of this graph.  The remaining
protected lower colours miss one private `t_i` and carry one of five
outside triples: the three triples in the bridge of Theorem 7.1 and the
two triples in (2.5).  The only repeated outside triples are the active
triples `Q-{q_j}`; each occurs twice.  Such a triple spans exactly two
cyclic edges on `Q`.  Every other outside triple occurs once.  Hence an
upper owner containing `C` contains at most `2+2=4` protected lower
colours.  An upper owner missing `t_i` contains no full-core colour and,
by direct inspection of the five consecutive outside triples, contains at
most two of them.  This proves `beta<=4`.

Now let `x` be an unprotected lower vertex.  If `C subset x`, then `x` is
`C` plus a pair in `D`.  The full-core protected owners correspond to the
triples

\[
 Q-\{q_i\},\quad \{c,q_i,q_{i+1}\},\quad
 \{q_i,z_{j-1},z_j\}.                                \tag{3.4}
\]

Every pair lies in at most four such triples; equality is possible only
for a consecutive pair `z_(j-1)z_j`, which lies under the four choices of
`q_i`.

If `x` contains `C-t_i` and three outside labels, it lies under at most two
of the four missing-core owners on path `i`, and under at most one full-core
owner.  If it misses two core labels, it lies under at most one owner on
each of the two corresponding paths; the only outside four-set repeated
between paths is `Q`, giving `H_i,H_j`.  No protected owner misses more than
one core label.  Therefore `alpha<=4`. `square`

## 4. No residual Ore cut

We use two already-proved consequences of the exact protected Ore--Ryser
criterion, from
`MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` and
`MATH_THEOREM_SUBLINEAR_EXPOSURE_PROTECTED_FACTOR_SMALL_CUT_AND_OPTIONAL_CORE_REDUCTION_20260805.md`.
Their proofs use only that every protected lower vertex has degree two and
every protected owner has degree at most two; therefore they apply verbatim
to the present disjoint cycle bank.

For completeness, the threshold reduction is unchanged as follows.  In an
inclusion-minimal failed shore, each selected lower vertex lies below at
most one loose residual owner.  At most `alpha(P)` of its `m` owner
neighbours are protected, leaving at least `m-alpha(P)-1` unprotected
owners having three or more neighbours in the failed shore; their family
has cardinality smaller than the shore.  The balanced partial-shadow
theorem gives (4.3).  Dually, a positive optional bank has a positive-owner
family strictly larger than itself, and every such owner contains at least
`m-beta(P)-1` optional members.  The strict-imbalance partial-shadow theorem
gives (4.4).  No acyclicity of the protected bank enters either argument.

First, if a protected bank `P` with `e` edges has a failed residual lower
shore `A`, then the small/co-small localization theorem gives

\[
 \min\{|A|,W-|A|\}
 <{m(m-1)\over2m-1}e.                               \tag{4.1}
\]

Second, the sharp partial-shadow theorem gives, with

\[
 K(D)={2D-1\choose D},                              \tag{4.2}
\]

the two bounds

\[
 |A|\ge K(m-\alpha(P)-1),                           \tag{4.3}
\]

and, for the optional complement

\[
 B=(\mathcal L\setminus\mathcal Z(P))\setminus A,
 \qquad |B|\ge K(m-\beta(P)-1)+1.                  \tag{4.4}
\]

Equation (4.4) applies because a failed residual shore is equivalent, by
the exact optional-complement identity, to a positive optional bank `B`.

For `P=P^circ`, Lemma 3.1 and (2.6) reduce both lower bounds to

\[
                         K(m-5)={2m-11\choose m-5}.              \tag{4.5}
\]

Put

\[
 T_m={m(m-1)\over2m-1}(8m+24).                      \tag{4.6}
\]

At `m=12`,

\[
 K(7)={13\choose7}=1716>T_{12}={15840\over23}.      \tag{4.7}
\]

The ratio `K(m-4)/K(m-5)` is

\[
 {(2m-9)(2m-10)\over(m-4)(m-5)}>3,                 \tag{4.8}
\]

whereas `T_(m+1)/T_m<2` for `m>=12`.  Hence

\[
                         K(m-5)>T_m\qquad(m>=12).    \tag{4.9}
\]

If (4.1) chooses the small alternative, then
`|A|<T_m<K(m-5)`, contradicting (4.3).  If it chooses the co-small
alternative, then

\[
 |B|=W-|\mathcal Z(P^\circ)|-|A|<W-|A|<T_m<K(m-5), \tag{4.10}
\]

contradicting (4.4).  Thus no failed residual shore exists.

### Theorem 4.1 (spanning phased host)

For every `m>=12`, `ML_m` has a spanning two-factor containing all four
closed collar cycles `P^circ`.

Each protected cycle may be alternately coloured in its already prescribed
phases, while all other factor cycles are coloured arbitrarily.  The two
colour classes are therefore ordered perfect matchings `(M_0,M_1)` which
contain the old all-width collar bank with every `L_iR_i` in `M_0`.

The proposed new edge `L_iR_(i-1)` is absent automatically: `L_i` is
already saturated in both phases.  Replacing the four old phase-zero edges
by the four new ones gives another ordered two-SDR.  Its complete
owner-window current is zero at every width, and its four-socket action is
the odd cycle `i -> i+1`.

#### Proof

The preceding cut argument proves the spanning two-factor.  Since each
component of `P^circ` is already a cycle, any containing two-factor retains
it as a whole component, so its prescribed alternating phase is independent
of every other component.  The remaining assertions are Theorem 7.1 and
Section 2. `square`

## 5. Consequence and scope

The formerly open large-bank planting row is closed:

\[
 \boxed{
 \text{all-width owner-deck zero}
 +\text{ odd connector-faithful socket action}
 +\text{ spanning ordered two-SDR host}.}            \tag{5.1}
\]

This is an abstract owner/immediate-lower theorem.  The containing factor
may have many other components and need not be upper-surjective.  No claim
is made here about coordinate residence, identification with the inherited
MNW recursive terminals, higher upper-palette assignment outside the
protected bank, or terminal lower/common-cap compilation.

The exact unclosed-bank Ore criterion and an independent replay of the
local collar algebra are frozen separately in
`MATH_REDUCTION_COMMON_MATE_C8_ALLWIDTH_COLLAR_EXACT_ORE_GATE_AND_SELF_AUDIT_20260812.md`.
