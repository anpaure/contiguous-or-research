# Equal-height leaf blocks give an exact PBBS angle-transfer C6

**Date:** 2026-08-05  
**Method:** rooted parenthesis algebra, the standard `A_1` KKR scan, and
cyclic rigging gaps; no computation or search  
**Status:** unconditional for `h>=4`, `u,v>=1`, and `u+v>=3`.  This closes
the first equal-profile boundary left by the arbitrary-tail descent theorem:
the two equal-action old shores lie on different PBBS angle tori.  Varying
`u,v` realizes an adjacent transfer in an explicit chain of unit-rigging
gap necklaces.  It does not yet span every rigging necklace in the sector.

## 1. A common-pivot C6 with two equal-height blocks

Put

\[
 s=u+v,\qquad m=h+s+1,\qquad n=2m+1,
\tag{1.1}
\]

where `h>=4` and `u,v>=1`.  Choose the cyclic deficit-three word

\[
 0_{a_0}(10)^u\;0_{a_1}(10)^v\;
 0_{a_2}(1^h0^h).
\tag{1.2}

Call its rank-`(m-1)` support `H`.  Let `c,d` be the first two down-steps
of the final mountain, let

\[
 [n]=H\mathbin{\dot\cup}K\mathbin{\dot\cup}
       \{a_0,a_1,a_2,c\},
\tag{1.3}

and define

\[
 R_i=K+a_i,\quad P_i=K+a_i+a_{i+1},\quad
 Q_i=K+a_i+c,\quad L_i=P_i-d.
\tag{1.4}

The three centers `Z_i=H+a_i` have normalized Dyck shapes

\[
\begin{aligned}
 A_{u,v}&=(1^h0^h)\,1(10)^u0\,(10)^v,\\
 B_{u,v}&=(10)^u\,1(10)^v0\,(1^h0^h),\\
 C_s&=(10)^v\,1(1^h0^h)0\,(10)^u.
\end{aligned}
\tag{1.5}

The final display is cyclically the hook shape

\[
                         C_s\sim (1^{h+1}0^{h+1})(10)^s.
\tag{1.6}

In all three words the dominant mountain supplies the rightmost global
maximum, and its first down-step is `c`.  The forward survivor is the one
remaining `a`-label.  Therefore

\[
 f(Z_i)=Q_{i+1},\qquad f^{-1}(Z_i)=P_{i+1},
\tag{1.7}

so `P_iQ_i` are three old centered-PBBS edges.

The predecessor words `X_i=f^{-1}(P_i)` are obtained from (1.5) by the
same first-maximum complement as in the arbitrary-tail theorem.  Their
dominant initial pieces have heights `h+1,h,h`; every later piece has
height at most three.  Since `h>=4`, their rightmost maxima are followed
by the second mountain down-step `d`.  Hence

\[
                         P_i\cap f^{-2}(P_i)=P_i-d=L_i.
\tag{1.8}

Thus the common-deletion theorem applies to the clean switch

\[
                         P_iQ_i\longmapsto P_iQ_{i+1}.
\tag{1.9}

It preserves every q1 row, every immediate upper colour, and the complete
selected q2 multiset.

## 2. The repeated action profile

Peak pruning gives

\[
 \lambda(A_{u,v})=\lambda(B_{u,v})
      =(h,2,1^{s-1}),
 \qquad
 \lambda(C_s)=(h+1,1^s).
\tag{2.1}

The top gaps are `h-2` and `h`, respectively.  Hence all six q1
occurrences needed by (1.9) are forced into every max-height section.

Action profile alone does not separate `A_(u,v)` from `B_(u,v)`.  The next
section does so at the exact angle level.

## 3. Unit riggings of the two equal-profile states

Use the standard highest-path `A_1` KKR scan, with `1` an empty letter and
`0` a ball.  At a ball, extend the longest singular string and reset its
rigging to the new vacancy number.  For the action in (2.1), the unit-string
vacancy is

\[
                         q=2h+1.
\tag{3.1}

The scan of a mountain `1^h0^h` creates one length-`h` string of rigging
zero.  The scan of

\[
                         W_r:=1(10)^r0
\tag{3.2}

creates one length-two string and `r-1` unit strings.

### Lemma 3.1 (literal unit-rigging rows)

The final unit-rigging multisets of the first two words in (1.5) are

\[
\begin{aligned}
 J(A_{u,v})&={(q-2)^{u-1},(q-1)^v\},\\
 J(B_{u,v})&={0^u,1^{v-1}\}.
\end{aligned}
\tag{3.3}

Here an exponent denotes multiplicity.

#### Proof

After scanning `1^h0^h`, the leading empty letter and the `r` internal
leaves of `W_r` create `r` singular unit strings of rigging `2h-1=q-2`.
The terminal ball extends one of them to length two.  Appending a balanced
ground leaf `10` thereafter creates a new unit string of rigging
`2h=q-1`.  This proves the first row.

Starting instead with `(10)^u` creates `u` unit strings of rigging zero.
Inside `W_v`, the `v` internal leaves create unit strings of rigging one;
the terminal ball extends one of those to length two.  Appending the final
mountain creates a new long string: its leading empty run makes all old
strings nonsingular, and its consecutive balls extend only the new string.
Thus the old unit riggings remain `0^u,1^(v-1)`, proving the second row.
`square`

## 4. Cyclic gap necklaces separate the angle tori

For sorted unit riggings

\[
                         J_1\le\cdots\le J_{s-1},
\]

form the cyclic gap word

\[
 (J_2-J_1,\ldots,J_{s-1}-J_{s-2},J_1+q-J_{s-1}),
\tag{4.1}

read up to cyclic rotation.  This is invariant under every action-angle
slide: a slide of a higher string translates all unit riggings equally,
while a unit slide only changes the chosen cyclic origin.  Hence (4.1) is
an invariant of the physical PBBS angle torus.

If `u,v>=2`, (3.3) gives the two gap necklaces

\[
\begin{aligned}
 G_A&=(0^{u-2},1,0^{v-1},q-1),\\
 G_B&=(0^{u-1},1,0^{v-2},q-1).
\end{aligned}
\tag{4.2}

The entries `1` and `q-1` are distinct and unique, so any cyclic equality
would have to align both; the intervening zero-run lengths would then have
to agree, which they do not.

If `u=1<v`, then

\[
 G_A=(0^{v-1},q),
 \qquad
 G_B=(1,0^{v-2},q-1),
\tag{4.3}

and if `v=1<u` the two roles are reversed.  Again they are unequal.  For
`u=v=1`, both consist of the one-entry necklace `(q)`.

We have proved:

### Theorem 4.1 (equal-height angle separation)

If `u+v>=3`, the equal-action centers `A_(u,v)` and `B_(u,v)` lie on
different periodic-BBS action tori, and hence on different PBBS factor
components.  Since `C_s` has a different action partition, the three old
edges in (1.9) lie on three distinct components.  The q2-neutral C6 merges
them into one.

The exceptional case `u=v=1` has only one unit string; its gap necklace
cannot distinguish the two centers, and no three-component conclusion is
claimed.

## 5. The induced angle-transfer chain

Fix `s>=3` and vary `u=1,...,s-1`, with `v=s-u`.  Apart from the collapsed
necklace

\[
                         G_*= (0^{s-2},q),
\tag{5.1}

the tori met by (4.2) have necklaces

\[
 G_r=(0^r,1,0^{s-3-r},q-1),
 \qquad 0\le r\le s-3.
\tag{5.2}

The connector with parameter `u` joins consecutive members:

\[
 G_*--G_0--G_1--\cdots--G_{s-3}--G_*.
\tag{5.3}

Every one of these hyperedges also contains the same hook action profile
`(h+1,1^s)`; the normalized hook word is cyclically
`M_(h+1)(10)^s`, independently of `u`.

Thus the equal-height boundary contains a literal adjacent-transfer
generator: one zero gap moves across the ordered pair of nonzero gaps
`1,q-1` at each step.  This is genuine angle-level motion, not merely a
profile shadow.

The family (5.3) is a hyperfan through a hook component, not yet a loose
forest spanning the whole action sector.  General unit-rigging necklaces
may have more than two nonzero gaps; proving that analogous local transfers
exist around every such gap is the remaining angle-expansion theorem.

