# Variable successor tags give a positive-resident clock dilation on nonbipartite rethreads

**Date:** 2026-08-13  
**Status:** unconditional local theorem under a finite common-successor tag
constraint and a finite support-domination test.  Unlike the cyclic
`p`-tag clock, it requires only positive residence, which is the exact
condition for the maximal flat antecedent.  It makes no zero-gap claim.

## 1. Joint rethread data

Let `F^-` and `F^+` be two oriented simple Johnson two-factors on the same
rank-`rho` owner occurrence bank

\[
                         v\longmapsto V_v\subseteq X. \tag{1.1}
\]

Write `s^-(v)` and `s^+(v)` for the two successors of occurrence `v`.
Assume the base owner and immediate palettes are simple.

Choose a finite tag set `P`, whose cardinality is part of the construction,
and a map

\[
                         t:V\longrightarrow P        \tag{1.2}
\]

such that

\[
                         \boxed{
 t(s^-(v))=t(s^+(v))=:t^+(v)\ne t(v)\quad(v\in V).} \tag{1.3}
\]

For an unchanged successor the equality is tautological.  At a changed
successor it is the exact compatibility constraint: the old and new heads
must enter through the same literal tag.

No additive voltage or cyclic ordering of `P` is assumed.  Condition
(1.3) automatically closes both states because tags live on vertices, not
on an independently integrated edge cocycle.

## 2. Variable-tag clock block

Fix `h>=2`, let

\[
                         U=\{u_0,\ldots,u_{2h-1}\},
 \qquad D_j=\{u_j,\ldots,u_{j+h-1}\},               \tag{2.1}
\]

with clock indices modulo `2h`, and choose a common core `C` disjoint from
`X,P,U`.  For owner rank `R`, require

\[
 |C|=R-\rho-h-1\ge0,
 \qquad |C\sqcup X\sqcup P\sqcup U|\le k.           \tag{2.2}
\]

Replace occurrence `v` by

\[
\begin{aligned}
 \Gamma(v)=(&C+V_v+t(v)+D_0,\ldots,C+V_v+t(v)+D_h,\\
             &C+V_v+t^+(v)+D_h,
              C+V_v+t^+(v)+D_{h+1},\ldots,
              C+V_v+t^+(v)+D_{2h}).                 \tag{2.3}
\end{aligned}
\]

At the middle, the tag changes at fixed `D_h`.  At the block end the owner
is `C+V_v+t^+(v)+D_0`.  In either state its successor `w=s^\pm(v)` starts
at `C+V_w+t(w)+D_0`; equality `t(w)=t^+(v)` from (1.3) makes the join the
literal base Johnson exchange.

Denote the two lifted states by `F^-[t,h]` and `F^+[t,h]`.

## 3. Graph, palettes, and positive residence

### Theorem 3.1

The two lifted states are simple rank-`R` Johnson two-factors.  Their
owner, immediate-lower, and immediate-upper palettes are simple.  Every
nonconstant coordinate has every positive run of length at least `h`.
They have the same component/socket actions as the base states and use
`2h+2` lifted owners per base occurrence.

#### Proof

Rank and Johnson adjacency follow exactly as in the cyclic tag clock:
clock edges exchange antipodal `U` labels; the middle edge exchanges the
two distinct tags in (1.3) at fixed `D_h`; the joining edge performs the
base exchange at fixed `(t^+(v),D_0)`.

The disjoint `(X,P,U)` profiles identify base owner, tag, and clock state.
Repeated anchors carry different tags or different base owners.  The three
edge types have ticket profiles

\[
\begin{array}{c|c|c}
 &\text{lower}&\text{upper}\\ \hline
\text{clock}&(\rho,1,h-1)&(\rho,1,h+1)\\
\text{tag}&(\rho,0,h)&(\rho,2,h)\\
\text{base}&(\rho-1,1,h)&(\rho+1,1,h),
\end{array}                                           \tag{3.1}
\]

so types cannot collide; base occurrence, literal tag, proper clock
interval, and base palette simplicity separate tickets within a type.

A base coordinate is constant through its `2h+2`-owner block, so every
base positive run only dilates.  Clock coordinates have positive runs at
least `h` in

\[
                         D_0,\ldots,D_h,D_h,\ldots,D_{2h}. \tag{3.2}
\]

Fix a tag `a`.  Whenever `t(v)=a`, the first half of `Gamma(v)` contains
`a`.  Every predecessor `u` of `v` in either state satisfies
`t^+(u)=t(v)=a`, so the second half of `Gamma(u)` also contains `a`.
These halves are consecutive and form a positive run of length `2h+2`.
If other adjacent blocks carry `a`, runs merge and become longer.  Thus
every positive tag run has length at least `2h+2`.  No assertion about the
intervening zero gaps is needed.

Substitution does not rename sockets or alter the base successor
permutation.  This proves the theorem.  \(\square\)

## 4. Finite support theorem

For a based cyclic base arc

\[
                         I=(v_1,\ldots,v_s),          \tag{4.1}
\]

define its full tag word

\[
 \tau(I)=\bigl((t(v_1),t^+(v_1)),\ldots,
                (t(v_s),t^+(v_s))\bigr),            \tag{4.2}
\]

and signature

\[
                         \sigma_t(I)=(T(I),s,\tau(I)),
 \qquad T(I)=\bigcup_{j=1}^sV_{v_j}.                \tag{4.3}
\]

Let `Sigma_t^-` and `Sigma_t^+` be the supports over all standard cyclic
arcs (at most one base turn) of `F^-` and `F^+`.

### Theorem 4.1

If

\[
                         \boxed{\Sigma_t^-\subseteq\Sigma_t^+,} \tag{4.4}
\]

then for every `h>=2` and every standard cyclic lifted width `w`,

\[
                         \boxed{
 Deck_w(F^-[t,h])\subseteq Deck_w(F^+[t,h]).}         \tag{4.5}
\]

#### Proof

Project an old lifted interval to its base block arc `I` and record its
two endpoint offsets in `0,...,2h+1`.  Its base contribution is `T(I)`.
Its literal tag and clock contribution is determined by the full tag word
`tau(I)` and those offsets.  Condition (4.4) supplies a new base arc with
the same signature.  Use the same offsets.  The base, tag, and clock unions
and the physical width are identical, giving the required new witness.
\(\square\)

The full word (4.2) is conservative.  It may be quotiented by literal
tag-union equivalence of the endpoint pieces and complete intervening
blocks.  For a finite actuator it is usually simpler to test (4.4) or that
exact quotient directly.

## 5. An exact equality-quotient criterion

The tag-selection problem has a solver-free normal form once base support
witnesses have been chosen.

Let `mathcal A^-` be the finite set of based old cyclic arcs used in the
support test.  Choose, for every

\[
 I=(v_1,\ldots,v_s)\in\mathcal A^-,                 \tag{5.1}
\]

a new arc

\[
 \phi(I)=(w_1,\ldots,w_s)                           \tag{5.2}
\]

with

\[
                         T(\phi(I))=T(I).            \tag{5.3}
\]

No injectivity of `phi` is required.  On the occurrence set generate an
equivalence relation `sim_phi` by

\[
 s^-(v)\sim_\phi s^+(v)\quad(v\in V),               \tag{5.4}
\]

and, for every matched pair `(5.1)--(5.2)` and every `j`,

\[
 v_j\sim_\phi w_j,
 \qquad
 s^-(v_j)\sim_\phi s^+(w_j).                        \tag{5.5}
\]

The second equality in (5.5) matches the output tags of the two endpoint
blocks.  For internal `j` it often follows from the next input equality,
but retaining it gives one uniform statement including the final block.

### Theorem 5.1 (quotient-loop and fixed-alphabet criteria)

For the fixed witness map `phi`, the following are equivalent.

1. There are some finite tag alphabet `P` and a tag map `t` satisfying
   (1.3) for which
   `tau(I)=tau(phi(I))` for every old arc `I`.
2. No equivalence class of `sim_phi` contains both endpoints of a required
   tag-change edge:
   
   \[
                 [v]_{\sim_\phi}\ne[s^-(v)]_{\sim_\phi}
                 \quad(v\in V).                     \tag{5.6}
   \]

When (5.6) holds, one may take one private tag for every equivalence class.
The resulting clock lift satisfies all-width support inclusion for every
`h>=2`.

For a prescribed alphabet of size `p`, contract the classes of
`sim_phi` and form the conflict graph

\[
 G_\phi=\bigl(\{[v]_{\sim_\phi}:v\in V\},
       \{[v]_{\sim_\phi}[s^-(v)]_{\sim_\phi}:v\in V\}\bigr). \tag{5.7}
\]

Then a tag map into that prescribed alphabet exists if and only if
`G_phi` is loopless and `p`-colourable.  In particular, (5.6) plus
`p>=|V(G_phi)|` is sufficient.  This fixed-alphabet qualification is
load-bearing in the ambient-room inequality (2.2).

#### Proof

Any tag map in item 1 is constant on (5.4)--(5.5), hence on every
equivalence class.  Condition (1.3) makes the two classes in (5.6)
different.  This proves necessity.

Conversely, assume (5.6), and assign a distinct literal tag to every
equivalence class.  Relation (5.4) gives

\[
                         t(s^-(v))=t(s^+(v)),         \tag{5.8}
\]

while (5.6) makes that common tag different from `t(v)`.  Thus (1.3)
holds.  The two relations in (5.5) give, coordinate by coordinate,

\[
 (t(v_j),t^+(v_j))=(t(w_j),t^+(w_j)),               \tag{5.9}
\]

so the full tag words of each chosen old/new arc pair agree.  Together
with (5.3), this proves (4.4).  Apply Theorem 4.1.

For a prescribed alphabet, every valid tag map is constant on quotient
classes and must give different colours to the endpoints of every edge of
`G_phi`; hence it is a proper `p`-colouring.  Conversely, any proper
`p`-colouring of `G_phi` gives (1.3) and the equalities (5.8)--(5.9).
This proves the fixed-alphabet assertion.  \(\square\)

Thus, after selecting the finite base witness map, tag feasibility is
exactly the absence of a loop in an equality quotient.  It is not an
integer-rounding or graph-colouring problem when the tag alphabet may be
chosen freely.

## 6. Exact application gate for `T_2`

For the frozen two-hex `T_2` actuator, uniform `Z_13` tags leave two
tag-refined support exceptions in the internal relay.  The variable-tag
route replaces the uniform-voltage problem by the finite constraints

\[
 t(s^-(v))=t(s^+(v))\ne t(v)                       \tag{6.1}
\]

on the changed owner bank, together with the support test (4.4).  The
selection of support witnesses is a finite problem independent of `h`;
after those witnesses are selected, tag feasibility is the quotient-loop
test of Theorem 5.1.

By Theorem 5.1, it is enough to select one new mate for every old base
support arc and verify the finite no-loop condition (5.6).  A passing map
would give a positive-resident all-height actuator without the zero-gap
overhead of a cyclic tag alphabet.  A failed quotient identifies an exact
set of mutually incompatible support witnesses and hence the smallest
place where a further return collar is needed.

The theorem does not claim that such a witness map has been selected for
`T_2`; it identifies the current decisive finite calculation.  Host
completion and the terminal typed cap remain separate after a local
solution.
