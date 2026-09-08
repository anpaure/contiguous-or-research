# Leaf plucking realizes every adjacent transfer between hook PBBS tori

**Date:** 2026-08-05  
**Method:** exact leaf-slot coordinates and forward/reverse parenthesis
cancellation; no search  
**Status:** unconditional for hook height `h>=3`.  One selected q2-neutral
clean C6 implements one adjacent unit transfer in the cyclic weak-composition
coordinate of the hook sector.  Hence every hook action torus lies in the
same common-pivot connector-hypergraph block as the concentrated all-hook
spine torus.  A physically disjoint loose spanning forest is not asserted.

## 1. Exact leaf-slot coordinates for `(h,1^b)`

Put

\[
 q=2h-1.
\tag{1.1}
\]

Let

\[
 x=(\ell_0,\ldots,\ell_{h-2},t,
       r_{h-2},\ldots,r_0)\in\mathbb Z_{\ge0}^{q},
 \qquad |x|=b.
\tag{1.2}
\]

Define the Dyck word

\[
\begin{aligned}
 D_h(x)={}&(10)^{\ell_0}1(10)^{\ell_1}1\cdots
        (10)^{\ell_{h-2}}1(10)^{t+1}\\
 &\quad 0(10)^{r_{h-2}}0\cdots
        0(10)^{r_1}0(10)^{r_0}.
\end{aligned}
\tag{1.3}
\]

Parallel peak deletion removes all displayed leaf factors and leaves the
mountain `1^(h-1)0^(h-1)`.  Conversely, if a Dyck word has soliton
partition `(h,1^b)`, deleting all leaves leaves that mountain.  In the
plane-tree picture the surviving path has `h-1` edges; every deleted leaf
is attached before or after one of its continuation edges, or at its final
vertex.  The final vertex has one compulsory leaf.  These are exactly the
`2h-1` slots in (1.2), so (1.3) is a bijection.

Let `phi` be the rooted PBBS shape map.  Direct first-maximum
complementation in (1.3) gives

\[
 \phi^2(D_h(x))=D_h(\operatorname{rot}x),
\tag{1.4}
\]

where

\[
 \operatorname{rot}(x_0,x_1,\ldots,x_{q-1})
   =(x_{q-1},x_0,\ldots,x_{q-2}).
\tag{1.5}
\]

Thus the rooted shape orbits of `g=f^2` are precisely cyclic necklaces of
weak compositions of `b` into `q` slots.  Under the standard exact PBBS
action-angle correspondence, each such necklace is one physical PBBS
component; this is the necklace form of the exact `L_gamma(b,q)` census.

The concentrated necklace

\[
                         [(b,0,\ldots,0)]
\tag{1.6}
\]

is the named all-hook spine component.  Its familiar phases include
`(10)^b1^h0^h` and `1^h0^h(10)^b`.

## 2. The leaf-plucking clean C6

Fix any Dyck word `F` with soliton partition

\[
                         (h,1^{b-1}),
 \qquad h\ge3,quad b\ge1.
\tag{2.1}
\]

Its semilength is `m-1`, where `m=h+b`.  Place `F` on cyclic coordinates
`3,4,...,2m`, and put

\[
 a_0=0,
 \qquad a_1=1,
 \qquad a_2=2.
\tag{2.2}
\]

Let `H` be the set of one-positions of this copy of `F`.  Then

\[
 0_{a_0}\,\varnothing\,
 0_{a_1}\,\varnothing\,
 0_{a_2}\,F
\tag{2.3}
\]

is its deficit-three decomposition.

Let `c` be the down-step immediately following the rightmost height-`h`
maximum of `F`.  After that step the path is at height `h-1`; let `d` be
the down-step immediately following the last subsequent visit to height
`h-1`, counting the endpoint of `c` as such a visit.  Then `c<d`, and both
are zero-positions of `F`.

Put

\[
 K=[0,2m]\setminus
       (H\mathbin{\dot\cup}\{a_0,a_1,a_2,c\}).
\tag{2.4}
\]

Then `|K|=m-2` and `d in K`.  Define

\[
 R_i=K+a_i,
 \quad P_i=K+a_i+a_{i+1},
 \quad Q_i=K+a_i+c,
 \quad L_i=P_i-d.
\tag{2.5}
\]

## 3. PBBS shore and common deletion

Let `Z_i=H+a_i`.  Their normalized Dyck shapes are

\[
                         F10,
 \qquad 10F,
 \qquad 1F0.
\tag{3.1}
\]

Their rightmost global maxima are followed by the same coordinate `c`.
The forward unmatched zeros cycle through `a_0,a_1,a_2`, while `c` is the
reverse unmatched zero in all three states.  Hence

\[
 f(Z_i)=Q_{i+1},
 \qquad
 f^{-1}(Z_i)=P_{i+1},
\tag{3.2}
\]

so all three old shores `P_i->Q_i` are PBBS factor edges.

Let `F^uparrow` be obtained from `F` by changing the step `c` from zero to
one, and let `F^uparrow_-` denote the same word with its first symbol
deleted.  Direct reverse cancellation gives

\[
 s(P_0)=a_2,
 \qquad
 s(P_1)=s(P_2)=3,
\tag{3.3}
\]

and the normalized predecessor shapes are

\[
 D(f^{-1}(P_0))=F^\uparrow00,
\]

\[
 D(f^{-1}(P_1))=F^\uparrow_-100,
 \qquad
 D(f^{-1}(P_2))=F^\uparrow_-010.
\tag{3.4}
\]

Before `c`, the height of `F^uparrow` is at most `h`.  From `c` onward it
is two above the height of `F`, which is at most `h-1` there.  Its
rightmost height-`h+1` maximum is therefore the last post-`c` visit of `F`
to height `h-1`, and the next step is exactly `d`.

Deleting the first up-step lowers all corresponding heights by one.  Thus
the two words involving `F^uparrow_-` have rightmost maximum `h` followed
by `d`.  Their appended tails reach height at most two; `h>=3` prevents a
new tie.  Consequently all three predecessor states have reverse survivor
`d`, and

\[
                         P_i\cap f^{-2}(P_i)=P_i-d=L_i.
\tag{3.5}
\]

This is the common-deletion condition.

## 4. Selection, q2 neutrality, and the exact angle move

Peak-pruning gives

\[
 \lambda(Z_0)=\lambda(Z_1)=(h,1^b),
 \qquad
 \lambda(Z_2)=(h+1,1^{b-1}).
\tag{4.1}
\]

Their largest-two-part gaps are `h-1` and `h`, respectively.  For `h>=3`
the soliton-gap theorem therefore puts every factor edge of these
components in the max-height q1 section.  In particular all six old and
companion occurrences required by the C6 are selected.

The clean switch

\[
                         P_iQ_i\longmapsto P_iQ_{i+1}
\tag{4.2}
\]

preserves upper q1 colours edgewise and lower q1 colours as a multiset.
Equation (3.5) invokes the common-deletion theorem, so the selected q2
multiset is also unchanged.

Now suppose the final leaf slot of `D_h(x)` is nonempty.  Removing one
terminal root leaf writes

\[
                         D_h(x)=F10
\tag{4.3}
\]

for a unique hook word `F` of type `(h,1^(b-1))`.  If `e_j` denotes the
`j`-th unit vector and the final slot is `q-1`, the other hook center is

\[
                         10F=D_h(x-e_{q-1}+e_0).
\tag{4.4}
\]

Therefore the C6 performs exactly one adjacent cyclic unit transfer.
Choosing another PBBS phase rotates the slot vector by (1.5), so every
move

\[
                         x\longmapsto x-e_j+e_{j+1}
 \qquad(x_j>0)
\tag{4.5}
\]

is realized by a literal selected q2-neutral common-pivot C6.

If the two necklaces in (4.5) are different, their old hook edges lie on
two distinct PBBS components, and the third old edge lies on the distinct
donor sector `(h+1,1^(b-1))`.  The C6 is then a genuine three-component
connector.  If the necklaces agree, the move is a loop in the quotient and
is unnecessary for connectivity.

## 5. Hook angle-level connectivity

The graph on weak compositions of `b` into `q` slots generated by adjacent
unit transfers is connected: move each unit step by step around the cyclic
slot graph until all units occupy slot zero.  Taking the quotient by cyclic
rotation preserves connectedness.  By Section 4, every nonloop edge of
this quotient graph is the hook pair of a literal q2-neutral connector.

Hence every physical PBBS component in the hook sector `(h,1^b)` lies in
the same connector-hypergraph block as the concentrated component (1.6).
The third vertex of each connector belongs to the lower-leaf hook sector
`(h+1,1^(b-1))`; iterating in `b` connects the angle-level hook atlas to the
named all-hook spine.

Thus

\[
 \boxed{\text{all hook action tori are connected at the literal
 common-pivot q2-neutral incidence level}.}
\tag{5.1}
\]

## 6. Remaining physical loose-forest gate

Incidence connectivity is not yet a serial switching theorem.  Many
adjacent-transfer connectors may reuse the same donor component, and a
loose-tree realization must select them so that each new hyperedge meets
the previous union in exactly one component.  Their literal supports must
also be made vertex-disjoint on every reused component.

A sufficient next statement is a recursive necklace-matching theorem:
at each leaf number `b`, pair all but at most one hook necklaces by adjacent
unit transfers, use their `(h+1,1^(b-1))` donors as parent vertices, and
choose the pairings over all `b` so that the resulting incidence graph is a
loose forest with `O(1)` roots and capacity-faithful physical placements.

The present theorem proves every required local hyperedge and removes the
angle-reachability obstruction.  It does not prove that global matching and
placement statement, nor any q3, residence, arbitrary-upper, or common-cap
interface.
