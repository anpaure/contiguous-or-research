# An all-hook family of selected three-component q2-neutral PBBS C6s

**Date:** 2026-08-05  
**Method:** exact forward/reverse cancellation and peak-pruning algebra; no
search  
**Status:** unconditional for `b>=1` and `h=m-1-b>=4`.  For every such
pair there is a literal max-height-selected clean C6 with one common q2
deletion.  As `b` varies, consecutive gadgets share the same physical hook
component, and cyclic rotations can be chosen so that all supports are
vertex-disjoint.  Hence the family is a genuine physically supported loose
chain, not only an action-profile chain.

## 1. Literal family

Work on the cyclic ground set `{0,1,...,2m}`.  Fix

\[
 b\ge1,
 \qquad
 h=m-1-b\ge4.
\tag{1.1}
\]

Put

\[
\begin{aligned}
 E&=\{2,4,\ldots,2b\},\\
 J&=\{2b+3,2b+4,\ldots,m+b+1\},\\
 H&=E\mathbin{\dot\cup}J,\\
 (a_0,a_1,a_2)&=(0,1,2b+2),\\
 c&=m+b+2,\\
 d&=m+b+3,\\
 K&=\{3,5,\ldots,2b+1\}
       \mathbin{\dot\cup}\{d,d+1,\ldots,2m\}.
\end{aligned}
\tag{1.2}
\]

Then `|H|=m-1`, `|K|=m-2`, and

\[
 [0,2m]=H\mathbin{\dot\cup}K\mathbin{\dot\cup}
           \{a_0,a_1,a_2,c\}.
\tag{1.3}
\]

Define, with subscripts modulo three,

\[
 R_i=K+a_i,
 \quad
 P_i=K+a_i+a_{i+1},
 \quad
 Q_i=K+a_i+c,
 \quad
 L_i=P_i-d.
\tag{1.4}
\]

## 2. The three old shores are PBBS edges

The forward-unmatched-zero decomposition of `H` is exactly

\[
 0_{a_0}\,D_0\,0_{a_1}\,D_1\,0_{a_2}\,D_2,
\tag{2.1}
\]

where

\[
 D_0=\varnothing,
 \qquad
 D_1=(10)^b,
 \qquad
 D_2=1^h0^h.
\tag{2.2}
\]

Let `Z_i=H+a_i`.  Flipping `a_i` consumes the unmatched zeros `a_i` and
`a_(i+1)`, leaving `a_(i-1)` as the unique forward-unmatched zero.  Direct
reverse cancellation in each of the three words leaves the common reverse
zero `c`.  Therefore

\[
\begin{aligned}
 f(Z_i)
  &=([0,2m]\setminus Z_i)-a_{i-1}
    =K+c+a_{i+1}=Q_{i+1},\\
 f^{-1}(Z_i)
  &=([0,2m]\setminus Z_i)-c
    =K+a_{i+1}+a_{i+2}=P_{i+1}.
\end{aligned}
\tag{2.3}
\]

Thus the centered factor contains all three directed old edges

\[
                         P_i\longrightarrow Q_i.
\tag{2.4}
\]

## 3. The companion deletion is common

Write `s(P)` for the reverse-unmatched zero of a rank-`m` state.  Reverse
cancellation gives

\[
 s(P_0)=2b+2=a_2,
 \qquad
 s(P_1)=s(P_2)=2b+3.
\tag{3.1}
\]

The three inverse states are consequently

\[
\begin{array}{c|c}
i&f^{-1}(P_i)\\ \hline
0&E\cup\{2b+3,\ldots,c\},\\
1&\{0\}\cup E\cup\{2b+4,\ldots,c\},\\
2&\{1\}\cup E\cup\{2b+4,\ldots,c\}.
\end{array}
\tag{3.2}
\]

In every row of (3.2), reverse cancellation leaves exactly the zero

\[
                         d=c+1.
\tag{3.3}
\]

The incoming centered-factor neighbour of `P_i` is therefore

\[
 f^{-2}(P_i)=P_i+s(P_i)-d,
\]

and the unchanged companion q1 row at `P_i` is exactly

\[
 P_i\cap f^{-2}(P_i)=P_i-d=L_i.
\tag{3.4}
\]

## 4. All six q1 occurrences are max-height selected

For each old row `R_i`, the forward-unmatched zeros are

\[
                         c-2,c-1,c.
\tag{4.1}
\]

Two intervening Dyck blocks are empty.  The remaining cyclic block has the
following literal forms (in the order `i=0,1,2`):

\[
\begin{aligned}
 W^R_0&=1^h0^2(10)^{b-1}1\,0^{h-1},\\
 W^R_1&=1^{h-1}010(10)^{b-1}1\,0^{h-1},\\
 W^R_2&=1^{h-1}0^3(10)^{b-1}1^2 0^{h-2}.
\end{aligned}
\tag{4.2}
\]

The assumption `h>=4` makes all three words Dyck.  Their height and
rightmost-max successor are

\[
\begin{array}{c|c|c}
i&\text{height}&\text{coordinate following its rightmost maximum}\\ \hline
0&h&a_1,\\
1&h-1&a_2,\\
2&h-1&a_0.
\end{array}
\tag{4.3}
\]

These are precisely the three occurrences `P_iQ_i` of the rows `R_i`.
The nonempty block is the unique maximum-height block.

For each companion row `L_i`, the forward-unmatched zeros are

\[
                         c-1,c,d.
\tag{4.4}
\]

Again two blocks are empty.  The remaining literal blocks are

\[
\begin{aligned}
 W^L_0&=1^h0(10)^{b-1}1\,0^h,\\
 W^L_1&=1^{h-2}010(10)^{b-1}1^2 0^{h-1},\\
 W^L_2&=1^{h-1}0^2(10)^{b-1}1^2 0^{h-1}.
\end{aligned}
\tag{4.5}
\]

Their block data are

\[
\begin{array}{c|c|c}
i&\text{height}&\text{coordinate following its rightmost maximum}\\ \hline
0&h&a_2,\\
1&h-1&2b+3,\\
2&h-1&2b+3.
\end{array}
\tag{4.6}
\]

The last column is exactly `s(P_i)` from (3.1), so these are the incoming
factor occurrences at `P_i`.  Since `h>=4`, every displayed long block is
strictly higher than the two empty blocks.  Hence all six required q1
occurrences belong to the max-height section.

## 5. q2 neutrality and component separation

Equation (3.4) gives the same deleted core coordinate `d in K` at all three
companion turns.  The common-deletion classification therefore applies:
replacing

\[
                         P_iQ_i\quad\hbox{by}\quad P_iQ_{i+1}
\tag{5.1}
\]

preserves the selected q1 and q2 multisets exactly.  The three affected q2
values merely cycle.

From (2.2), the base peak profile is

\[
 \beta(D_0)+\beta(D_1)+\beta(D_2)
   =(b+1,1^{h-1}).
\tag{5.2}
\]

Wrapping `D_i` adds one unit in pruning layer `height(D_i)+1`.  Thus the
three peak profiles, or equivalently their conjugate soliton partitions,
are

\[
\begin{array}{c|c|c}
i&\text{peak profile}&\text{soliton partition}\\ \hline
0&(b+2,1^{h-1})&(h,1^{b+1}),\\
1&(b+1,2,1^{h-2})&(h,2,1^{b-1}),\\
2&(b+1,1^h)&(h+1,1^b).
\end{array}
\tag{5.3}
\]

They are pairwise distinct.  Since the soliton partition is constant on a
PBBS factor component, the three old edges lie on three distinct cycles.
The clean C6 therefore merges those cycles into one while preserving q1
and q2 exactly.

## 6. The hook components agree across consecutive gadgets

Define the hook and near-hook partitions

\[
 H_b=(m-b,1^b),
 \qquad
 J_b=(m-1-b,2,1^{b-1}).
\tag{6.1}
\]

The connector with parameter `b` has action triple

\[
                         \boxed{\{H_b,H_{b+1},J_b\}}.
\tag{6.2}
\]

Consequently the triples for

\[
                         1\le b\le m-5
\tag{6.3}
\]

form a loose chain at the action-profile level: consecutive triples share
the one hook profile `H_(b+1)` and otherwise introduce two new profiles.

The shared profile is in fact the same physical PBBS component.  Put

\[
 s=b+1.
\]

The `H_(b+1)` state `Z_0` in the parameter-`b` gadget has normalized shape

\[
 A=1^h0^h(10)^s,
\tag{6.4}
\]

while the `H_(b+1)` state `Z_2` in the parameter-`b+1` gadget has shape

\[
 C=(10)^s1^h0^h.
\tag{6.5}
\]

For the rooted PBBS shape map `phi`, direct first-maximum complementation
gives

\[
 A\longmapsto 1^h(01)^s0^h\longmapsto C.
\tag{6.6}
\]

To check the lift, for `1<=j<=h-1` define

\[
 U_j=1^h0^j(10)^s0^{h-j},
 \qquad
 V_j=1^j(01)^s1^{h-j}0^h.
\tag{6.7}
\]

Then `U_1` is the middle word in (6.6), `V_1=C`, and

\[
 A\xrightarrow{h}U_1\xrightarrow{h}V_1
 \xrightarrow{h+2s}U_2\xrightarrow{h}V_2
 \xrightarrow{h+2s}\cdots
 \xrightarrow{h}V_{h-1}\xrightarrow{h+2s}A.
\tag{6.8}
\]

This shape cycle has odd period `2h-1` and voltage

\[
 h^2+(h-1)(h+2s)
   =(h-1)(2h+2s+1)+1.
\tag{6.9}
\]

The ground size is `2h+2s+1=2m+1`, so the voltage is one modulo the
ground size.  The quotient cycle therefore lifts to one physical
`f`-cycle; its length is odd, so it is also one `g=f^2` component.  Thus
the shared hook occurrences in consecutive gadgets lie on exactly the same
factor cycle.

The near-hook profiles `J_b` are pairwise distinct, and a near-hook profile
never equals a hook profile.  Therefore the projected component triples
themselves form a loose chain of `m-5` hyperedges on `2m-9` physical PBBS
components.

## 7. Cyclic rotations make the chain physically disjoint

Choose the connectors in increasing order of `b`.  Nonconsecutive
connectors use disjoint factor components, so their vertex supports are
automatically disjoint.  A connector and its predecessor share exactly one
hook component, and each uses exactly one old factor edge on that component.

Ground rotation gives `2m+1` distinct translates of the later edge: a
nonidentity rotation cannot fix either rank-`m` endpoint because
`gcd(m,2m+1)=1`.  A fixed edge of a cycle meets at most three cycle edges:
itself and its two neighbours.  Hence at most three rotations make the later
support meet the already chosen support on the shared component.  Since
`2m+1>3`, choose any other rotation.  Induction gives pairwise
vertex-disjoint literal supports for the entire chain.

The loose-tree realization theorem now applies.  Switching all `m-5`
connectors merges these `2m-9` initial PBBS cycles into one cycle while
preserving the selected q1 and q2 multisets exactly.

## 8. Scope

The theorem supplies a linear physically disjoint family of literal
three-component selected q2-neutral connectors.  It proves a genuine PBBS
component block of size `2m-9`, not merely a profile shadow.  It does not
show that all other PBBS components attach to this block, that the total
number of connector blocks is bounded, or that q3, residence, and common-cap
interfaces survive.
