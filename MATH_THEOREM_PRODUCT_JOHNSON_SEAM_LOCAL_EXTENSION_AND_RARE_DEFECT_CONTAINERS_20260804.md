# Product-Johnson seam extension, rare-defect containers, and the exact
# boundary of local rejection arguments

**Date:** 2026-08-04  
**Status:** unconditional counting and extension theorems for the restricted
token sphere, plus sharp counterexamples to scope-only and naive local-lemma
arguments.  These results do not prove that the complete lower/upper/router
host relation has the required local form, and therefore do not prove
`PPC(1)` or a new bound on `nu(k)`.

## 0. Result

Fix the notation of
`MATH_THEOREM_TOKEN_SPHERE_LAMINAR_PRIVATE_PIVOT_HOST_COINSTANTIATION_20260804.md`.
Thus `H` is a rank-`(R-1)` incoming token on `[2R-1]`, the aperture depth is
`D`, and `F` is forbidden in the outgoing token.  Put

\[
 a=|F\cap H|,\qquad b=|F-H|,
\]

and assume

\[
 a\le D-1,\qquad b\le R-D+1.                        \tag{0.1}
\]

The eligible output sphere is exactly a product of two Johnson slices.  In
the natural sparse-defect coordinates it is

\[
 \Omega={A\choose h}\times{B\choose \ell},           \tag{0.2}
\]

where

\[
 \begin{aligned}
 A&=H-F,              &p:=|A|&=R-1-a,&h&=D-1-a,\\
 B&=H^c-F,            &q:=|B|&=R-b,  &\ell&=D-1.
 \end{aligned}                                        \tag{0.3}
\]

The first coordinate records the holes removed from `A`; the second records
the entrants selected from `B`.  Hence

\[
 N_F(H)=|\Omega|={p\choose h}{q\choose\ell}.          \tag{0.4}
\]

This coordinate system gives three exact seam-survival tools.

1. **Local projection.**  If the complete joined host relation depends on
   the output token only through coordinate footprints `U` in `A` and `V`
   in `B`, and `L` is its set of feasible local defect states, then
   the number of accepted seams is exactly

   \[
   \sum_{(S,T)\in L}
      {p-|U|\choose h-|S|}{q-|V|\choose\ell-|T|}.     \tag{0.5}
   \]

   In particular, a nonempty local join automatically extends to an
   eligible seam whenever

   \[
   |U|\le\min\{h,p-h\},\qquad
   |V|\le\min\{\ell,q-\ell\}.                        \tag{0.6}
   \]

   Thus a genuinely fixed total coordinate footprint cannot reject every
   seam on the triangular schedule.  The quantifier is **total footprint**,
   not bounded footprint per constraint.

2. **Coordinate core plus occurrence exceptions.**  If every token counted
   by (0.5) is accepted except possibly at a fixed set `E` of physical seam
   occurrences, then at least

   \[
                    A_{U,V}(L)-|E|                   \tag{0.7}
   \]

   seams survive, where `A_(U,V)(L)` denotes (0.5).  Consequently
   `|E|<A_(U,V)(L)` proves the exact missing strict inequality

   \[
       |\mathcal B_{\rm join}\cap\mathcal S_D(H;F)|<N_F(H).       \tag{0.8}
   \]

3. **Rare-defect certificates.**  An arbitrary bad relation may be covered
   by local cylinders which prescribe holes, retained old coordinates,
   entrants, and rejected entrants.  Every such cylinder has an exact
   hypergeometric weight.  If the sum of these weights is below one, a seam
   survives.  On the triangular schedule, a certificate with `s` required
   sparse defects has weight `O(R^(-s/2))` when its total footprint and `F`
   are fixed.

There is no valid local-lemma theorem based only on bounded coordinate or
occurrence scopes.  If `h>0`, the one-coordinate events

\[
                       \{x\text{ is a hole}\}\quad(x\in A)       \tag{0.9}
\]

cover the whole sphere, even though their coordinate footprints are
pairwise disjoint and every coordinate occurs in only one event.  The
analogous entrant events cover when `\ell>0`.  Likewise, one singleton event
for every physical seam occurrence covers the sphere.  Therefore any valid
LLL, switching, or container proof must price the **total certificate mass**,
find a common defect transversal, or prove the hybrid structure in (0.7).

The fixed coordinate-avoidance and literal aperture algebra fit these
theorems.  A fixed finite bank of reserved physical seam occurrences fits
the exceptional set `E`.  The current all-subset lower path cuts, retained-
old upper selector/forest relation, component connector, and residual Rado
router do not yet fit: their dependence on the opened seam is global or
occurrence-labelled, and no bounded coordinate projection or small
exception set has been proved for them.

## 1. Product-Johnson coordinates

Every eligible output has the unique form

\[
 J=X\mathbin{\dot\cup}Y,
 \qquad X\in{A\choose R-D},
 \qquad Y\in{B\choose D-1}.                          \tag{1.1}
\]

Define its sparse defect pair

\[
                         P=A-X,\qquad Q=Y.            \tag{1.2}
\]

Then

\[
 |P|=p-(R-D)=D-1-a=h,
 \qquad |Q|=D-1=\ell.                                \tag{1.3}
\]

Conversely, every
`(P,Q) in binom(A,h) times binom(B,ell)` gives

\[
                         J=(A-P)\cup Q.               \tag{1.4}
\]

This proves the bijection (0.2) and the count (0.4).  A coordinate in `A`
is a rare defect when it is absent from `J`; a coordinate in `B` is a rare
defect when it is present in `J`.

The value of the reparametrization is that both selected defect sets have
size at most `D-1`, whereas `A` and `B` have order `R`.

## 2. Exact local-footprint extension

Let

\[
                         U\subseteq A,\qquad V\subseteq B,
 \qquad u=|U|,\quad v=|V|.                            \tag{2.1}
\]

The local defect state of `(P,Q)` is

\[
                         (P\cap U,Q\cap V).           \tag{2.2}
\]

Let `L` be any family of allowed local states in `2^U times 2^V`.  It
may be the direct specification of one host module, or the projection of a
natural join involving arbitrary finite internal variables.  Define

\[
 \Omega(L)=\{(P,Q)\in\Omega:(P\cap U,Q\cap V)\in L\}. \tag{2.3}
\]

Binomial coefficients outside their natural range are interpreted as zero.

### Theorem 2.1 (exact local projection count)

One has

\[
 \boxed{
 |\Omega(L)|=
 \sum_{(S,T)\in L}
 {p-u\choose h-|S|}{q-v\choose\ell-|T|}.}            \tag{2.4}
\]

In particular, the number of rejected eligible seams is

\[
                         N_F(H)-|\Omega(L)|.          \tag{2.5}
\]

#### Proof

Fix `(S,T) in L`.  A defect pair has this local state precisely when

\[
 P=S\mathbin{\dot\cup}P_0,
 \quad P_0\in{A-U\choose h-|S|},
 \qquad
 Q=T\mathbin{\dot\cup}Q_0,
 \quad Q_0\in{B-V\choose\ell-|T|}.                  \tag{2.6}
\]

This gives the corresponding summand in (2.4).  Distinct local states have
disjoint extension families, so summing proves the formula.  Equation
(2.5) follows from (0.4).  \(\square\)

### Corollary 2.2 (exact extension criterion)

A local state `(S,T)` extends to an eligible seam if and only if

\[
 \begin{aligned}
 0\le h-|S|\le p-u,\\
 0\le \ell-|T|\le q-v.
 \end{aligned}                                       \tag{2.7}
\]

Equivalently,

\[
 \begin{aligned}
 \max\{0,h-(p-u)\}\le |S|\le\min\{h,u\},\\
 \max\{0,\ell-(q-v)\}\le |T|\le\min\{\ell,v\}.
 \end{aligned}                                       \tag{2.8}
\]

Thus `\Omega(L)` is nonempty exactly when `L` contains a state satisfying
(2.8).

#### Proof

The two binomial coefficients in its summand of (2.4) are positive exactly
under (2.7), which rearranges to (2.8).  \(\square\)

### Corollary 2.3 (small total footprint)

If

\[
 u\le\min\{h,p-h\},\qquad
 v\le\min\{\ell,q-\ell\},                            \tag{2.9}
\]

then **every** local state in `2^U times 2^V` extends.  Consequently any
nonempty joined local relation has an accepted eligible seam.

Along a regime in which

\[
 h,\ell,p-h,q-\ell\longrightarrow\infty,             \tag{2.10}
\]

every fixed total coordinate footprint satisfies (2.9) eventually.

#### Proof

For every `0<=s<=u`, the inequalities `s<=h` and `h-s<=p-u` follow from
`u<=h` and `u<=p-h`.  Apply the same argument on `B`, then Corollary 2.2.
\(\square\)

The word **total** is essential.  A family of many individually small
relations can have union footprint larger than either sparse budget.

### Corollary 2.4 (clean-default extension)

Suppose `(\varnothing,\varnothing) in L`.  If

\[
                         p-u\ge h,
 \qquad                    q-v\ge\ell,               \tag{2.11}
\]

then at least

\[
                         {p-u\choose h}{q-v\choose\ell}           \tag{2.12}
\]

eligible seams are accepted.

This is useful when every local module accepts the untouched state and a
running-intersection join proves that the untouched local choices coexist.

### Corollary 2.5 (running-intersection specialization)

Suppose finite host relations have a running-intersection tree after all
token dependence has been replaced by membership variables on `U union V`.
Let `L` be the projection of their natural join to those membership
variables.  The separator recursion determines `L` exactly.  If it returns
one state satisfying (2.8), then a common eligible seam exists.

In particular, under (2.9), nonemptiness of the finite local join alone is
enough.

#### Proof

Running intersection computes the exact natural join, hence its exact
projection `L`.  Apply Corollaries 2.2--2.3.  \(\square\)

This statement does not convert an occurrence address into a coordinate
membership variable.  Such a conversion is an additional structural
theorem about the host.

## 3. Coordinate core plus sparse occurrence exceptions

Let `sigma` send an eligible token to its unique physical opening seam in a
`q1`-exact carrier.  Thus `sigma` is injective on the eligible sphere.  Let
`E` be a set of physical seam occurrences.

### Theorem 3.1 (hybrid seam-survival bound)

Assume that every token in `\Omega(L)` is accepted by the complete host
unless its opening occurrence lies in `E`.  Then

\[
 \boxed{
 |\{\text{accepted eligible seams}\}|
 \ge |\Omega(L)|-|E|.}                               \tag{3.1}
\]

Consequently, if

\[
                         |E|<|\Omega(L)|,             \tag{3.2}
\]

then the joint bad-seam set is strictly smaller than `N_F(H)`.

More locally, one state `(S,T) in L` is enough whenever it satisfies (2.8)
and

\[
 |E|<
 {p-u\choose h-|S|}{q-v\choose\ell-|T|}.             \tag{3.3}
\]

#### Proof

At most `|E|` members of `\Omega(L)` can map into `E`, because `sigma` is
injective.  This proves (3.1).  Equations (3.2)--(3.3) follow from Theorem
2.1.  \(\square\)

The theorem isolates a particularly useful proof target:

> factor every genuinely coordinate-sensitive seam condition through one
> extendible local join, and prove that every remaining failure is attached
> to a fixed occurrence bank smaller than the extension multiplicity.

It is not enough that each rejected seam possess some short local
explanation whose physical address varies with the seam.

## 4. Rare-defect cylinder certificates

The local projection theorem is strongest when all coordinate dependence
has one fixed union footprint.  A complementary tool permits many local
certificates with different footprints.

Let

\[
 I_A,O_A\subseteq A,\qquad I_B,O_B\subseteq B,       \tag{4.1}
\]

where `I_A cap O_A=I_B cap O_B=emptyset`.  The associated cylinder is

\[
 \begin{aligned}
 C(I_A,O_A;I_B,O_B)=\{(P,Q)\in\Omega:
 &I_A\subseteq P,\ O_A\cap P=\varnothing,\\
 &I_B\subseteq Q,\ O_B\cap Q=\varnothing\}.
 \end{aligned}                                       \tag{4.2}
\]

Write

\[
 i=|I_A|,\quad o=|O_A|,
 \qquad j=|I_B|,\quad r=|O_B|.                       \tag{4.3}
\]

Here `i+j` is the number of required sparse defects.  The other literals
assert that old coordinates are retained or that complement coordinates
are not introduced.

### Lemma 4.1 (exact cylinder weight)

The cylinder has size

\[
 |C(I_A,O_A;I_B,O_B)|=
 {p-i-o\choose h-i}{q-j-r\choose\ell-j}.             \tag{4.4}
\]

Its density in `Omega` is

\[
 \boxed{
 w(I_A,O_A;I_B,O_B)=
 { (h)_i(p-h)_o\over(p)_{i+o}}
 { (\ell)_j(q-\ell)_r\over(q)_{j+r}},}               \tag{4.5}
\]

where `(x)_t=x(x-1)\cdots(x-t+1)`.

#### Proof

After installing the required holes and excluding the forbidden holes,
choose the remaining `h-i` holes from `p-i-o` coordinates.  The second
shore is identical.  Dividing (4.4) by (0.4) and cancelling factorials
gives (4.5).  \(\square\)

### Theorem 4.2 (weighted rare-defect DNF criterion)

Suppose every jointly bad eligible seam belongs to at least one cylinder in
a finite family `C`.  If

\[
 \boxed{
 \sum_{C\in\mathcal C} w(C)<1,}                      \tag{4.6}
\]

then an accepted eligible seam exists.  More precisely,

\[
 {|\mathcal B_{\rm join}\cap\mathcal S_D(H;F)|\over N_F(H)}
 \le\sum_{C\in\mathcal C}w(C).                       \tag{4.7}
\]

#### Proof

The assumed cylinders cover the bad set.  Apply the union bound using the
exact densities from Lemma 4.1.  \(\square\)

This is a certificate theorem rather than an independence assertion.  It
remains valid with arbitrary overlaps and arbitrary correlations between
the host modules.

### Corollary 4.3 (rare-degree asymptotics)

Assume every cylinder uses at most `t` coordinates on either shore.  Put

\[
 \eta_A={h\over p-t+1},\qquad
 \eta_B={\ell\over q-t+1},                            \tag{4.8}
\]

with positive denominators.  A cylinder with `i` required holes and `j`
required entrants has weight at most

\[
                         \eta_A^i\eta_B^j.            \tag{4.9}
\]

If `M_(i,j)` is the number of cylinders of rare bidegree `(i,j)`, the
sufficient condition becomes

\[
                         \sum_{i,j}M_{i,j}
                         \eta_A^i\eta_B^j<1.          \tag{4.10}
\]

On the triangular regime `D=Theta(sqrt R)`, with bounded `F,t`, one has

\[
                         \eta_A,\eta_B=O(R^{-1/2}).   \tag{4.11}
\]

Thus, if every certificate has at least `s` required sparse defects and
the total number of certificates is `o(R^(s/2))`, a seam survives for all
sufficiently large `R`.

#### Proof

Ignoring the forbidden-defect literals can only enlarge a cylinder.  The
probability that `i` prescribed coordinates belong to a uniform `h`-subset
is `(h)_i/(p)_i`, at most `(h/(p-t+1))^i`; similarly on `B`.  This proves
(4.9)--(4.10).  Equation (4.11) follows from `p,q=Theta(R)` and
`h,ell=O(D)=O(sqrt R)`.  \(\square\)

Certificates with no required sparse defect are not discounted by this
argument.  This is correct: a default-bad local rule can reject almost the
entire sphere.

### Theorem 4.4 (defect-transversal container)

Let `C` be a cylinder cover of the bad set.  Suppose there are

\[
                         T_A\subseteq A,\qquad T_B\subseteq B          \tag{4.12}
\]

such that every cylinder's positive support `I_A cup I_B` meets
`T_A cup T_B`.  If

\[
                         p-|T_A|\ge h,
 \qquad                    q-|T_B|\ge\ell,            \tag{4.13}
\]

then an accepted seam exists.

#### Proof

Choose `P in binom(A-T_A,h)` and `Q in binom(B-T_B,ell)`.  Every cylinder
requires at least one defect coordinate from `T_A cup T_B`, so `(P,Q)` lies
in none of them.  Since the cylinders cover all bad states, this state is
accepted.  \(\square\)

Unlike (4.6), this may handle a very large certificate family.  It requires
a common avoidable transversal of the positive supports.

## 5. Sharp barriers to a scope-only LLL

The following examples show why the hypotheses above cannot be replaced by
`each rejection relation has bounded local scope`.

### Proposition 5.1 (disjoint one-coordinate cover)

If `h>0`, the family

\[
                         B_x=\{(P,Q):x\in P\},
 \qquad x\in A,                                      \tag{5.1}
\]

covers `Omega`.  Every event has one-coordinate scope; the scopes are
pairwise disjoint; and every coordinate belongs to exactly one scope.

If `ell>0`, the analogous family

\[
                         B_y=\{(P,Q):y\in Q\},
 \qquad y\in B,                                      \tag{5.2}
\]

also covers `Omega`.

#### Proof

Every `h`-set contains some `x` when `h>0`, and every `ell`-set contains
some `y` when `ell>0`.  \(\square\)

Thus the overlap graph of coordinate supports is not a valid dependency
graph for the uniform fixed-size slice.  Events on disjoint coordinates
remain globally coupled by the exact cardinality row.  In particular, a
naive symmetric LLL using only support overlap would give a false
conclusion in (5.1)--(5.2).

The union-bound weights are sharp on this example:

\[
                         \sum_{x\in A}{h\over p}=h\ge1.             \tag{5.3}
\]

### Proposition 5.2 (two proper unary rules can cover)

Assume `0<h<p` and fix `x in A`.  The two proper one-coordinate events

\[
                         \{x\in P\},
 \qquad                    \{x\notin P\}             \tag{5.4}
\]

cover `Omega`.

Hence individual nonemptiness, bounded scope, a constant number of
relations, and a running-intersection scope tree do not suffice.  Their
**accepted** local relations must have a common cardinality-compatible
tuple.

### Proposition 5.3 (locally feasible but slice-incompatible)

Let `U` be an `(h+1)`-subset of `A`, and let

\[
                         L=\{(U,\varnothing)\}.        \tag{5.5}
\]

The local relation `L` is nonempty, but `\Omega(L)` is empty because an
`h`-set cannot contain all `h+1` coordinates.  Thus local join nonemptiness
must be followed by the extension inequalities (2.8).

### Proposition 5.4 (singleton occurrence cover)

Let `sigma(Omega)` be the eligible physical seam occurrences.  For every
`e in sigma(Omega)`, let

\[
                         B_e=\{J:\sigma(J)=e\}.       \tag{5.6}
\]

Then the `B_e` have singleton occurrence footprints and cover all eligible
seams.  Each occurrence is used once.

Therefore `bounded occurrence footprint per rejection` has no counting
content.  What is useful is a **fixed union exception bank** `E` satisfying
Theorem 3.1.

## 6. Which current host rows fit

The distinction is between dependence on the **value** of the output token
through a fixed coordinate projection, and dependence on the **physical
occurrence** at which that value appears.

### 6.1 Rows already covered

1. **Forbidden coordinate bank.**  The bank `F` is fully absorbed into
   `A,B,p,q,h,ell`; no additional union bound is required.
2. **One-aperture algebra.**  The relay theorem realizes every point of
   `Omega`.  Its active dropped/inserted labels are the sparse defect pair
   itself, so the aperture contributes no bad subset of `Omega`.
3. **Fixed coordinate-local collisions or terminal types.**  Once their
   combined dependence factors through one `U,V`, Theorem 2.1 applies.
   Running intersection may be used to compute the allowed local states,
   but it must be a join of the actual shared variables.
4. **A fixed reserved occurrence bank.**  If opening outside a named set
   `E` is the only remaining occurrence condition, Theorem 3.1 applies.
5. **Positive rare-defect explanations.**  If every failure has a bounded
   cylinder certificate with at least one required hole or entrant, the
   weighted or transversal criteria of Section 4 apply.

### 6.2 Rows not presently covered

1. **Balanced lower path and multisocket cuts.**  Their exact constraints
   quantify over all path subfamilies and named targets.  No theorem shows
   that changing the opened seam affects this system through a bounded
   coordinate projection or a fixed occurrence exception bank.  The local
   pivot rays fit; the background all-`Q` assignment does not yet fit.
2. **Retained-old upper selector and rooted forest.**  Whether a cut destroys
   every old witness of a target depends on the occurrence intervals of the
   whole factor.  The map from a lower colour `J` to its unique seam address
   may be arbitrary.  After a selector is fixed, a theorem bounding the
   union of unsafe cut addresses would create an `E`; no such uniform bound
   is currently proved.
3. **Component connectors and Hamilton opening.**  Prescribed endpoints,
   component Hall, and serial accessibility are global occurrence
   properties, not predicates of `J cap (U cup V)` on a fixed small bank.
4. **Residual typed router.**  A value-level boundary type or one displayed
   factor diamond may be coordinate-local.  The exact residual Rado rank
   after compensation deletion depends on all physical ports, sinks, and
   shared capacities.  A fixed compensation **occurrence** footprint can be
   put in `E`; the remaining all-cut router cannot presently be put there.
5. **Common cap and literal replay.**  These are global correlation and
   completeness tests.  Bounded arity of each clause does not imply a
   bounded union footprint, as Propositions 5.1--5.4 show.

Accordingly, the missing bad-seam theorem can now be stated in one of three
proof-safe forms.

### Product-slice seam certificate `PSSC`

For the complete joined host relation, prove at least one of:

1. **local-plus-exception:** it factors through `(U,V,L,E)` satisfying
   `|E|<A_(U,V)(L)`;
2. **rare DNF:** its bad set has a cylinder cover satisfying (4.6); or
3. **defect container:** its bad cylinders have a transversal satisfying
   (4.13).

Any one proves the strict bad-seam inequality needed by the private pivot-
host theorem.  None is currently established for the simultaneous lower,
upper, and router rows.

## 7. Scope relative to `PPC(1)`

Combining `PSSC` with the already stated private-footprint and
running-intersection hypotheses would remove the numerical bad-seam premise
from Theorem 4.1 of the source co-instantiation theorem.  The present result
does not prove `PSSC`; it gives exact, checkable sufficient criteria for it.

The principal mathematical gain is the quantifier correction:

\[
 \boxed{
 \text{bounded total coordinate projection + one compatible local state}
 \Longrightarrow \text{many seams},}
\]

whereas

\[
 \boxed{
 \text{bounded scope per relation}
 \not\Longrightarrow \text{any seam}.}
\]

No finite search, solver, random experiment, or computational candidate is
used as evidence in this theorem.
