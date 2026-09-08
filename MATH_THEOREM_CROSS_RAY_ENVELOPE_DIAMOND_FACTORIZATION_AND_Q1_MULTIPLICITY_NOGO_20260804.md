# Cross-ray envelope factorization and the q1 multiplicity obstruction

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional occurrence-level factorization and sharp
unit-capacity no-go for the explicit double-cross bridge and, more
generally, for a q1-exact diagonal.  One canonical cross-ray ticket does
factor through its exact union envelope and the native q1 diamond.  The
whole ray bank does not: all cuts on one rail use the same lower-turn and
upper-turn occurrences.  Under ordinary per-ticket Rado/gammoid semantics
the resulting rank is at most one per rail.  The theorem does not rule out
additional occurrence-distinct diamonds outside the selected q1 diagonal.

## 0. Outcome

Use the explicit double-cross bridge with

\[
 F=\{f_0,f_1,\ldots,f_d,f_{d+1}\},\qquad
 F^\circ=\{f_1,\ldots,f_d\},
\]

and put

\[
 C_1=K\cup\{z,a_1\}\cup F^\circ,
 \qquad
 C_3=K\cup\{z,a_3\}\cup F^\circ .                 \tag{0.1}
\]

For every `1<=j<d`, the left cross-ray ticket is

\[
 \bigl(P_1(j),S_0(j+1)\bigr)
 =\bigl(K\cup\{z,a_1\}\cup F[1,j],
        K\cup\{z,a_1\}\cup F[j+1,d]\bigr).          \tag{0.2}
\]

Thus, explicitly,

\[
 P_1(j)=K\cup\{z,a_1\}\cup F[1,j],\qquad
 S_0(j+1)=K\cup\{z,a_1\}\cup F[j+1,d].             \tag{0.3}
\]

The right cross-ray ticket is the analogous pair

\[
 P_0(j)=K\cup\{z,a_3\}\cup F[1,j],\qquad
 S_1(j+1)=K\cup\{z,a_3\}\cup F[j+1,d].             \tag{0.4}
\]

Each pair consists of two adjacent disjoint interval occurrences.  Their
interval union is exactly one full rail, and their Boolean union is exactly
`C_1` or `C_3`.  The full rail is not merely a convenient envelope: it is
the literal lower-turn occurrence of one of the bridge's two chord
diamonds.  Hence every individual ticket has a deterministic complete
factorization

\[
 \boxed{
   (\text{prefix witness},\text{suffix witness})
   \longrightarrow
   (\text{exact union-envelope lower turn})
   \longrightarrow
   (\text{native q1 upper turn}).}
                                                               \tag{0.5}
\]

However, the envelope occurrence and the q1 terminal occurrence in (0.5)
do not depend on `j`.  Consequently:

* one rail's `d-1` deterministic bundles have ordinary unit-capacity rank
  at most one;
* both rails together have rank at most two; and
* even if the two occurrence-coordinate roles of one ticket are allowed to
  coinstantiate its one q1 occurrence, the terminal deficiency of the
  `2(d-1)`-ticket bank is at least

\[
                              2(d-1)-2=2d-4.           \tag{0.6}
\]

The polarity bit from the nested-terminal coding theorem does not change
this bound: state labels distinguish meanings, not physical capacities.

Moreover, a q1-exact diagonal has exactly one lower-turn occurrence of each
rank-`(r-1)` value.  It therefore cannot contain `d-1` q1-diamond copies of
either `C_1` or `C_3`.  The minimal ordinary-Rado repair is an explicitly
materialized bank of `d-1` occurrence-distinct, correctly typed envelope
diamonds per rail (or, if the envelope occurrence is contracted as purely
semantic, at least `d-1` distinct accepted terminal occurrences per rail).
Those copies must lie outside the one-copy q1-exact lower-turn palette or
replace the present ticket factorization by a different injective one.

## 1. The full rails are the two chord lower turns

Index the bridge owners from zero:

\[
 G_1,\ldots,G_d,B,A,H_1,\ldots,H_d,D,E.              \tag{1.1}
\]

Thus

\[
 \operatorname{idx}(B)=d,\quad
 \operatorname{idx}(A)=d+1,\quad
 \operatorname{idx}(D)=2d+2,\quad
 \operatorname{idx}(E)=2d+3.                         \tag{1.2}
\]

Let the source word be `Q`, so owner and q1-turn addresses are

\[
 o_i=[i,i+d],\qquad
 p_i=[i+1,i+d],\qquad
 q_i=[i,i+d+1].                                      \tag{1.3}
\]

The bridge construction gives the two rail intervals

\[
 I_1=[d+1,2d],\qquad
 I_3=[2d+3,3d+2].                                    \tag{1.4}
\]

By (1.2)--(1.4),

\[
                         I_1=p_d,qquad I_3=p_{2d+2}. \tag{1.5}
\]

The two chord intersections are

\[
 B\cap A=C_1,qquad D\cap E=C_3,                     \tag{1.6}
\]

while their unions are

\[
 R_1:=B\cup A=K\cup\{z,a_1\}\cup F,
 \qquad
 R_3:=D\cup E=K\cup\{z,a_3\}\cup F.               \tag{1.7}
\]

Therefore

\[
 \operatorname{OR}_Q(p_d)=C_1,
 \quad \operatorname{OR}_Q(q_d)=R_1,
 \qquad
 \operatorname{OR}_Q(p_{2d+2})=C_3,
 \quad \operatorname{OR}_Q(q_{2d+2})=R_3.           \tag{1.8}
\]

Together with the two intermediate owner occurrences, these are the
literal interval diamonds

\[
 p_d\subset o_d,o_{d+1}\subset q_d,
 \qquad
 p_{2d+2}\subset o_{2d+2},o_{2d+3}\subset q_{2d+2}. \tag{1.9}
\]

Every inclusion changes the Boolean rank by one and the interval address
by one endpoint.  Hence (1.9) is exactly the native q1-diamond type, not
only a value-level containment.

## 2. Every cross cut factors through that diamond

For `1<=j<d`, define the literal left-rail addresses

\[
 x_{1,j}=[d+1,d+j],\qquad
 y_{1,j}=[d+j+1,2d],                                  \tag{2.1}
\]

and the right-rail addresses

\[
 x_{3,j}=[2d+3,2d+2+j],\qquad
 y_{3,j}=[2d+3+j,3d+2].                               \tag{2.2}
\]

They obey the exact address identities

\[
 x_{\epsilon,j}\cap y_{\epsilon,j}=\varnothing,
 \qquad
 x_{\epsilon,j}\cup y_{\epsilon,j}=p_{i_\epsilon},
 \qquad
 i_1=d,quad i_3=2d+2,                                \tag{2.3}
\]

where the union in (2.3) is union of adjacent interval-address sets.  The
source definition gives

\[
\begin{array}{c|cc}
 &x_{\epsilon,j}&y_{\epsilon,j}\\ \hline
 \epsilon=1&P_1(j)&S_0(j+1)\\
 \epsilon=3&P_0(j)&S_1(j+1).
\end{array}                                           \tag{2.4}
\]

Consequently

\[
 \operatorname{OR}(x_{\epsilon,j})
 \cup\operatorname{OR}(y_{\epsilon,j})=C_\epsilon
 =\operatorname{OR}(p_{i_\epsilon}).                 \tag{2.5}
\]

There are canonical literal Hasse chains from both ray cells to the
envelope.  With empty ranges suppressed, they are

\[
 \begin{aligned}
 x_{\epsilon,j}&\subset x_{\epsilon,j+1}\subset\cdots
   \subset x_{\epsilon,d-1}\subset p_{i_\epsilon},\\
 y_{\epsilon,j}&\subset y_{\epsilon,j-1}\subset\cdots
   \subset y_{\epsilon,1}\subset p_{i_\epsilon}.
 \end{aligned}                                      \tag{2.6}
\]

Every address step adds one rail position, and every value step adds the
corresponding unique filler coordinate.  Thus (2.6) is simultaneously an
interval-address cover chain and a Boolean Hasse chain.

### Theorem 2.1 (deterministic envelope-diamond bundle)

For each `epsilon in {1,3}` and `1<=j<d`, the record

\[
 \begin{aligned}
 \gamma_{\epsilon,j}=(&x_{\epsilon,j},y_{\epsilon,j};
 \text{the two chains (2.6)};
 p_{i_\epsilon},o_{i_\epsilon},o_{i_\epsilon+1},
 q_{i_\epsilon};\\
 &\text{the address identities (2.3), the OR identities (2.4)--(2.5),
 and the q1 identities (1.8)--(1.9)})                 \tag{2.7}
 \end{aligned}
\]

is a complete deterministic occurrence-labelled factorization of the
canonical cross-ray ticket through its exact union envelope and one native
q1 diamond.

#### Proof

The two upstream cells are the literal, exact ray-target witnesses by
(2.4).  Equation (2.3) says that they partition the full-rail occurrence,
and (2.5) says that its value is their exact Boolean union.  Equations
(2.6) give the complete literal incidence chains into that envelope, and
(1.8)--(1.9) give the subsequent literal q1 diamond (with the native
source-free owner-to-upper attachment).  Every address,
phase/ray role, cut label `j`, value, and incidence needed to replay the
composition is included in (2.7); no marginal representative is being
mistaken for a conjunction.  \(\square\)

This theorem is semantic until a complete cap state declares which
occurrences in (2.6) are finite capacities.  It preserves the literal ray
witnesses under either convention.  If the two occurrence-coordinate roles
must end at distinct capacities, one q1 terminal is insufficient even for
one ticket.  If the state accepts diagonal dual-role coinstantiation, one
ticket may end at `q_(i_epsilon)` with that occurrence charged once.  The
next section proves that this within-ticket permission does not solve the
cross-ticket capacity cut.

## 3. Sharp rank-one-per-rail no-go

Fix one complete cap/background state and use ordinary per-ticket
Rado/gammoid semantics: every finite occurrence has unit capacity, and two
different logical tickets may not consume the same finite occurrence.
Assume the strongest favorable within-ticket convention: the two
occurrence-coordinate roles of `gamma_(epsilon,j)` may coinstantiate the
same q1 terminal `q_(i_epsilon)`.

### Theorem 3.1 (envelope-diamond multiplicity cut)

For either rail `epsilon`, every simultaneous selection of the deterministic
bundle family

\[
             \{\gamma_{\epsilon,j}:1\le j<d\}         \tag{3.1}
\]

has size at most one.  Across both rails, every simultaneous selection has
size at most two.

#### Proof

Every member of (3.1) terminates at the same physical address
`q_(i_epsilon)`.  This is a unit-capacity cut of size one.  Hence two
distinct bundle representatives cannot coexist.  The two rails have at
most the two terminals `q_d,q_(2d+2)`, proving the total bound two.
\(\square\)

If the lower-turn occurrence `p_(i_epsilon)` is retained as a finite port,
the same rank-one cut already occurs one layer earlier.  Contracting that
lower turn as a purely declarative exact-envelope fact removes only the
earlier cut; it does not remove the terminal cut in Theorem 3.1.

### Corollary 3.2 (terminal deficiency)

Treat the `2(d-1)` cut-labelled cross-ray pairs as distinct logical tickets.
If their only admitted terminal representatives are (2.7), their common
terminal deficiency is at least

\[
                         2(d-1)-2=2d-4.               \tag{3.2}
\]

This remains true after adjoining arbitrary state labels, including the
one-bit polarized-chain label, unless those labels are accompanied by
new physical capacity.  A state refinement splits semantic types; it does
not duplicate the address `q_d` or `q_(2d+2)`.

The conclusion is also visible directly in the terminal Rado formula.  On
one rail, for the full ticket subset `J`, the union of every deterministic
terminal menu has gammoid rank at most one.  Hence

\[
                   |J|-r_N(A(J))\ge(d-1)-1=d-2.       \tag{3.3}
\]

Add the two disjoint rail subsets in the two-system/common-label min-max,
or simply use the two-address terminal cut, to obtain (3.2).

No unauthorized many-ticket coinstantiation is implicit here.  Such a rule
would replace ordinary per-ticket Rado semantics by a different
multi-obligation primitive and requires its own physical correctness
theorem.

## 4. A q1-exact diagonal cannot supply the missing copies

Let a cyclic q1-exact diagonal have owner row

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,qquad
 P_i=T_i\cap T_{i+1}=\bigcup_{h=i+1}^{i+d}A_h,
 \qquad i\in\mathbb Z_W,                              \tag{4.1}
\]

and suppose the lower-turn values `P_i` run once through the rank-`(r-1)`
shore.

### Theorem 4.1 (one-copy q1 multiplicity)

For every rank-`(r-1)` value `C`, there is exactly one q1 lower-turn
occurrence `p_i=[i+1,i+d]` with

\[
                         \operatorname{OR}(p_i)=C.     \tag{4.2}
\]

Consequently the selected q1 diagonal contains at most one native q1
diamond whose lower-turn value is `C`.

#### Proof

Q1 exactness says that the map `i -> P_i` is a bijection from the `W`
turn indices to the rank-`(r-1)` shore.  Equation (4.1) identifies the
value of `p_i` with `P_i`.  Thus (4.2) has exactly one solution.  A native
q1 diamond is indexed by its lower-turn seam, so there is at most one such
diamond above `C`. \(\square\)

A linear opening can only delete a wrap occurrence; it cannot create a
second copy.  Likewise, the active-wedge factor materialization theorem
protects one exact q1 turn at each selected lower-turn value.  Its
distinct-source hypothesis cannot manufacture repeated q1-exact copies of
one `C`.

The theorem concerns the selected q1 diagonal.  A word might contain other
intervals of value `C` outside that row.  They are useful here only if each
comes with an occurrence-distinct, correctly typed upper attachment in the
same complete cap state.  That is precisely an additional diamond bank,
not a consequence of q1 exactness.

## 5. Global uniqueness inside the explicit bridge source

The explicit bridge makes the multiplicity obstruction visible already in
its local source block.

### Lemma 5.1 (unique full-rail envelope in the bridge source)

In the complete explicit bridge source `Q`, whose positions are
`0,...,3d+3`, the only interval whose OR is `C_1` is `[d+1,2d]`, and the
only interval whose OR is `C_3` is `[2d+3,3d+2]`.

#### Proof

First consider `C_1`.  On the left rail, its `s`-th source letter contains
`f_s`, and no other left-rail letter contains `f_s`.  Therefore an interval
contained in the rail has union `C_1` only if it contains every one of its
`d` positions.  The owner identity

\[
 B=\operatorname{OR}[d,2d]=C_1\cup\{f_{d+1}\}
\]

forces the immediate left boundary letter to contain `f_(d+1)`, while

\[
 A=\operatorname{OR}[d+1,2d+1]=C_1\cup\{f_0\}
\]

forces the immediate right boundary letter to contain `f_0`.

In fact every source position outside the left rail is excluded.  For
`0<=p<d`, the unchanged maximal-envelope letter `Q_p` lies under only
`G`-owners and contains `a_3,f_(d+1)`; at `p=d` it still contains
`f_(d+1)`.  At `p=2d+1` it contains `f_0`, and at `p=2d+2` it contains
`a_3,f_0`.  The two endpoint letters of the right rail contain `a_3`, its
strict interior letters are filler singletons and cannot supply
`K union {z,a_1}`, and the terminal position `3d+3` contains
`a_3,f_(d+1)`.  Thus no interval meeting the exterior of the left rail has
OR exactly `C_1`, and no interval wholly in the strict interior of the
right rail has that OR.

For `C_3`, exchange the two active labels and the two rail roles.  The
boundary identities are

\[
 D=C_3\cup\{f_0\},\qquad E=C_3\cup\{f_{d+1}\}.
\]

Positions before the right rail contain either `a_1`, `f_0`, or
`f_(d+1)`; the strict interior of the left rail has only fillers and cannot
supply `K union {z,a_3}`; and position `3d+3` contains `f_(d+1)`.  Hence the
full right rail is the unique interval of value `C_3`. \(\square\)

This lemma concerns the complete explicit bridge source before it is
embedded into a larger ambient word.  It makes no assertion about remote
intervals lying wholly in that later exterior.  Theorem 4.1 is the global
statement for the selected q1-turn bank.

## 6. Exact minimal ordinary-capacity repair

Let `t_epsilon` be the number of occurrence-distinct, correctly typed
q1-diamond terminals in one complete state which accept the exact envelope
`C_epsilon` and are otherwise compatible with the retained ray witnesses.
Any deterministic bundle system factoring all `d-1` tickets on that rail
through those terminals has rank at most `t_epsilon`.  This is the terminal
cut bound

\[
                 r\le t_\epsilon.                     \tag{6.1}
\]

Therefore zero deficiency requires

\[
                 \boxed{t_1\ge d-1,\qquad t_3\ge d-1.}\tag{6.2}
\]

If the exact envelope occurrences themselves remain finite route ports,
the same inequalities are necessary for their occurrence multiplicities as
well.  Conversely, (6.2) is sufficient on this local face if one exhibits
`d-1` pairwise capacity-disjoint complete bundles per rail, preserves all
literal ray witnesses, supplies the required within-ticket product/phase
acceptance, and makes those bundles disjoint from the transported
background.

Thus the minimal missing state is not another scalar Hall inequality and
not another polarity label.  It is the following occurrence statement:

> **Replicated envelope-diamond bank.**  Materialize `d-1`
> occurrence-distinct accepted copies of the `C_1` envelope diamond and
> `d-1` occurrence-distinct accepted copies of the `C_3` envelope diamond,
> in one common phase/cap/background state, or construct a different
> injective factorization of the cut-labelled ray tickets.

The one-copy q1-exact diagonal cannot itself supply this bank by Theorem
4.1.  Any positive construction must use additional interval occurrences,
a different terminal type, or a different global organization of the
logical tickets.

### 6.1 A bounded-charge flat diagonal cannot hide the copies

There is also a scalar obstruction to manufacturing the required bank as
extra seams of the same flat diagonal.

### Theorem 6.2 (replication costs linear charge in `d`)

Let a linear word have length

\[
                              n=W+d+c,                 \tag{6.3}
\]

and consider its consecutive width-`d+1` diagonal band.  Suppose `b` of
the `W` required distinct q1 lower colours are supplied outside the
internal seams of this band.  If the internal seams contain those remaining
`W-b` distinct colours and additionally contain `t` repeated lower-turn
occurrences, then

\[
                              \boxed{c\ge t-b+1.}       \tag{6.4}
\]

In particular, replicating `C_1,C_3` from one copy each to `d-1` copies
each requires `t=2(d-2)`, and therefore

\[
                              c\ge2d-b-3.              \tag{6.5}
\]

For a bounded external boundary bank `b=O(1)`, this is `Omega(d)`, not
`O(1)`.

#### Proof

A word of length (6.3) has exactly

\[
                              n-d=W+c                  \tag{6.6}
\]

width-`d+1` intervals, hence at most `W+c-1` internal seams between
successive members of that band.  The assumed lower-turn ledger needs at
least

\[
                              W-b+t                    \tag{6.7}
\]

different seam occurrences.  Therefore

\[
 W-b+t\le W+c-1,
\]

which is (6.4).  Each envelope currently has one q1 copy, so reaching
`d-1` copies adds `d-2` repeated seams on each of the two rails.  This gives
(6.5). \(\square\)

The scope of Theorem 6.2 is important.  It rules out occurrence
replication **inside the same consecutive flat diagonal band** at bounded
charge.  It does not rule out a qualitatively different off-band socket
whose finite coordinates are not additional diagonal seams.  Such a socket
would be a different terminal construction and must carry its own exact
type, capacity, and regeneration proof.

### 6.2 Exact deterministic product criterion

The phase/product issue can be separated cleanly from envelope
multiplicity.  Fix one complete cap state and suppose all upstream
ray-to-envelope capacities and all background capacities have already been
made legal and disjoint.  Give cut `j` one deterministic complete terminal
bundle with ordered terminal coordinates

\[
                              (u_j^0,u_j^1).            \tag{6.8}
\]

If the state requires the two roles to use distinct capacities, the full
bank is feasible exactly when all `2(d-1)` displayed capacities on that
rail are pairwise distinct and every ordered pair has the required phase
type.  If the state accepts diagonal coinstantiation

\[
                              (u_j^0,u_j^1)=(q_j,q_j), \tag{6.9}
\]

with `q_j` charged once, the full bank is feasible exactly when the `q_j`
are pairwise distinct and every diagonal record has the required phase
normalization.

#### Proof

After fixing one deterministic bundle per ticket, there is no marginal
choice left and hence no hidden product-of-marginals inference.  Necessity
is the unit-capacity rule.  Conversely, the asserted distinctness makes the
complete deterministic records capacity-disjoint, while phase legality is
part of each record; selecting all records is therefore a valid joint
bank. \(\square\)

For the native bridge factorization, (6.9) has

\[
                              q_j=q_d
\]

for every left-rail cut and `q_j=q_(2d+2)` for every right-rail cut.  Thus
the exact deterministic criterion fails solely on cross-ticket
multiplicity even after the most favorable within-ticket product acceptance
is granted.  This is the promised sharp separation:

\[
 \boxed{
 \text{literal ray/envelope algebra: present};\quad
 \text{one-ticket phase diagonal: a state premise};\quad
 \text{bank-wide occurrence injection: absent}.}
                                                               \tag{6.10}
\]

## 7. Scope and dependencies

This theorem proves:

1. exact literal factorization of every canonical bridge ray ticket through
   its union-envelope lower turn and q1 diamond;
2. preservation of both exact ray witnesses in the complete record;
3. the sharp rank-one-per-rail cut under ordinary unit-capacity semantics;
4. the sharp lower bound `2d-4` for the two one-copy rails; and
5. impossibility of obtaining the needed repeated envelope diamonds from
   the q1-exact lower-turn palette itself.

It does not prove that no remote replicated envelope bank exists in a
larger word.  It does not construct product/phase acceptance for a single
diagonal bundle, transport the background, preserve all deeper upper rows,
or regenerate the bank in a Pascal child.

Dependencies:

* `MATH_THEOREM_C8_DOUBLE_CROSSRAIL_RESIDENT_BRIDGE_AND_PHASE_ENDPOINT_CORRECTION_20260801.md`;
* `MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md`;
* `MATH_THEOREM_ZERO_BLOCK_BIRAIL_COLLAPSE_AND_C8_CROSSMATCH_GATE_20260801.md`;
* `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`;
* `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`.
