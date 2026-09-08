# The \(r-1,r,r+1\) MSW menu: literal cube, suffix audit, and the exact remaining cut

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let \(r\) be minimal with

\[
 C_r\ge4p,\qquad t={C_r\over p},
\tag{0.1}
\]

where \(C_j=\operatorname {Cat}_j\). Put

\[
 Z_r=H_{m,r}C_r,\qquad
 D_r=Z_r\left({1\over2}-{1\over t}\right).
\tag{0.2}
\]

All asymptotic capacity comparisons below use the phase-critical regime

\[
 r\to\infty,\qquad r=o(m),\qquad
 W-N_{r+1}=o(Z_r),
\tag{0.2a}
\]

the last condition being automatic when \(r=\Theta(\log p)\) in the
coefficient-one application.

Three conclusions are proved.

First, the proposed persistent-suffix audit is substantially correct.
For a scale-\(s\) rectangle and every serviced \(q\ge s\), its fixed
suffix arm has canonical endpoint loads at least \(C_s,C_{s-1}\).
The proof is an occurrence injection through the exact exterior parity
tail. The fixed-depth double-boundary count is also

\[
                         O(W/r^3)
\tag{0.3}
\]

for any bounded adjacent-scale menu. One displayed bridge equation in the
earlier proof was wrong: the bridge residual is
\(j=q-(s+1)+O(1)\), or symmetrically \(q-(u+1)+O(1)\), not
\(q-s-u+O(1)\). After this correction the generating-function estimate
and its \(W/r^3\) order remain valid.

Second, the blanket conclusion that (0.3) kills every bounded
adjacent-scale extension is false. It fixes the active bit budget at the
two-scale value \(D_r/4\). A third scale supplies enough compatible bits
to operate at the three-arm scale \(D_r/3\).

There is also a smaller correction at self-depth. The \(16/3\) threshold
for the previously pruned \(r,r+1\) cube is not the optimal literal
two-scale threshold. Since a scale-\(r\) conflict endpoint has weight two
and its scale-\(r+1\) mate has weight four, one should delete the former.
The maximum two-scale self-depth envelope is

\[
 2M_r+4M_{r+1}-2E_r
 =\left({11\over32}+o(1)\right)Z_r,
\tag{0.3a}
\]

so the corresponding raw threshold is \(t=32/5+o(1)\). The old
\(16/3\) theorem remains correct for its specified pruning, but not as a
maximum-capacity statement.

Third, the complete \(r-1,r,r+1\) physical conflict graph has only
isolated vertices, \(K_2\)'s, and \(P_3\)'s. Its maximum literal Boolean
subcube has exact dimension

\[
\boxed{
 L_3=M_-+M_0+M_+-E_--E_++T,}
\tag{0.4}
\]

where

\[
\begin{aligned}
 M_-&=H_{m,r}C_{r-2},&
 M_0&=H_{m,r+1}C_{r-1},&
 M_+&=H_{m,r+2}C_r,\\
 E_-&=H_{m,r+1}C_{r-2},&
 E_+&=H_{m,r+2}C_{r-1},&
 T&=H_{m,r+2}C_{r-2}.
\end{aligned}
\tag{0.5}
\]

Uniformly for \(r=o(m)\),

\[
 {L_3\over Z_r}={41\over256}
   +O\left({1\over r}+{r\over m}\right).
\tag{0.6}
\]

At depths \(q\ge r+2\), every selected bit has three nonhereditary arms.
The scale-\(r-1\) hereditary arm may contribute an additional unit; write
\(B_q\) for the number of those units which actually cross the canonical
overloaded-set cut. A maximum cube can be chosen to retain every
scale-\(r-1\) bit, and its optimistic cut capacity is exactly bounded by

\[
\boxed{
 {\cal V}_{\ge r+2}(q)=3L_3+B_q,\qquad 0\le B_q\le M_-.}
\tag{0.7}
\]

In particular, even with \(B_q=0\),

\[
 {{\cal V}_{\ge r+2}(q)\over Z_r}
 ={123\over256}+o(1)
 >{7\over16}
 \ge {D_r\over Z_r}.
\tag{0.8}
\]

Thus the old persistent-one-arm dual does not close the three-scale menu.
It loses one unit per bit, but the literal cube has enough additional bits
to absorb that loss.

There is one sharp self-depth exception. At \(q=r+1\), the top scale is
at its own depth and has only two potentially useful arms. The exact
capacity envelope becomes

\[
\boxed{
 {\cal V}_{r+1}(q)
 =3M_-+3M_0+2M_+
  -3E_- -2E_+ +2T+B_{r+1}.}
\tag{0.9}
\]

Consequently

\[
 {{\cal V}_{r+1}\over Z_r}
 ={55\over128}+{B_{r+1}\over Z_r}+o(1).
\tag{0.10}
\]

For \(t\le128/9+o(1)\), no \(r-1\) bonus is needed at the count level.
For \(t>128/9+o(1)\), the exact necessary bonus fraction is

\[
\boxed{
 {B_{r+1}\over M_-}
 \ge {9\over8}-{16\over t}+o(1).}
\tag{0.11}
\]

The right side grows from zero to \(1/8\). Catalan arithmetic alone does
not prove (0.11), because different parent contexts can preload the same
suffix destination.

Let

\[
 \tau_r={C_r\over C_{r-2}}
 ={4(2r-1)(2r-3)\over r(r+1)}
 =16-{48\over r}+O(r^{-2}).
\tag{0.12}
\]

If \(t>\tau_r\), then \(C_{r-2}>p\), so every scale-\(r-1\) hereditary
destination is already over cap and \(B_q=0\). In this thin top strip,
(0.9), (0.3), and the canonical overloaded-set dual give a genuine
one-depth residual

\[
 K_{r+1,p}-(W-N_{r+1})
 \ge\left({1\over128}+o(1)\right)Z_r.
\tag{0.13}
\]

This is \(o(W)\), so it refutes exact self-depth saturation but not
coefficient one.

The uniform conclusion is therefore neither the proposed low/high
partition nor a complete positive theorem. The \(r-1\) layer destroys the
old high-\(t\) three-arm count obstruction as well as the low-\(t\) count
gap. What remains is directional:

1. prove the suffix-destination bonus (0.11) where it is needed;
2. orient the other three arms near their simultaneous maximum; and
3. do so under one common multidepth choice.

No marginal or scalar capacity estimate proves these statements.

## 1. Audit of hereditary suffix persistence

Fix a scale \(s\), one aligned parent context \(C\), and
\(R\in{\cal D}_{s-1}\). Rotate the omitted-label word at the parent block.
Its parity lists have the exact form

\[
\begin{aligned}
 {\mathsf E}_{C,R}
  &=(\iota_C{\mathsf A}(R),{\mathsf E}^{\rm ext}_C),\\
 {\mathsf O}_{C,R}
  &=(\iota_C{\mathsf B}(R),{\mathsf O}^{\rm ext}_C).
\end{aligned}
\tag{1.1}
\]

The internal prefix has length \(s-1\). At target depth \(q\), put

\[
                         \ell=m-q-1.
\tag{1.2}
\]

For \(s\le q\le m/2\),

\[
 s-1\le\ell\le m-s-1.
\tag{1.3}
\]

The two length-\(\ell\) suffixes in the exact four-arm formula therefore
lie wholly in the exterior parity tails and are independent of \(R\).
Write one of their cores as \(A_{C,q}\). Its two arm endpoints are

\[
 S_{C,q}=A_{C,q}\cup\{\beta_C\},\qquad
 T_{C,q}=A_{C,q}\cup\{\gamma_C\}.
\tag{1.4}
\]

At \(q=s\), the canonical boundary profile supplies \(C_s\) occurrences
at the first endpoint and \(C_{s-1}\) occurrences at the second.
Increasing \(q\) shortens the same fixed exterior suffix. It does not
inspect \(R\). Keeping the same pointed boundary in those rows therefore
gives injections

\[
\begin{aligned}
 \{\hbox{the }C_s\hbox{ source occurrences at depth }s\}
 &\hookrightarrow\mu_q^{-1}(S_{C,q}),\\
 \{\hbox{the }C_{s-1}\hbox{ mate occurrences at depth }s\}
 &\hookrightarrow\mu_q^{-1}(T_{C,q}).
\end{aligned}
\tag{1.5}
\]

Hence

\[
\boxed{
 \mu_q(S_{C,q})\ge C_s,\qquad
 \mu_q(T_{C,q})\ge C_{s-1}\qquad(q\ge s).}
\tag{1.6}
\]

This verifies persistence. The vague statement “projection can only
coalesce” is not sufficient by itself; (1.1)--(1.5) are the missing
rowwise occurrence map.

For \(s=r,r+1\), both bounds in (1.6) exceed \(p\). Their fixed arm is
therefore neutral on

\[
 \alpha_q=\mathbf1_{\{S:\mu_q(S)>p\}}.
\tag{1.7}
\]

For \(s=r-1\), the source bound \(C_{r-1}>p\) always holds, while the
mate bound is \(C_{r-2}\). Thus:

* if \(t>\tau_r\), the fixed arm is again forced neutral;
* if \(t\le\tau_r\), its destination may be below cap, but (1.6) alone
  does not prove this because exterior-context collisions may add load.

This is the exact point at which \(t\) ceases to determine the direction.

## 2. Audit and repair of the two-hole count

At one fixed depth, a nonlinear target can occur only when two selected
switch centres are the two boundary phases of one window. Interior
switches cancel from intersections by the local identity

\[
                         L\cap M\cap R=L\cap M'\cap R.
\tag{2.1}
\]

After deleting adjacent-scale critical pairs, two switches which can be
opposite boundaries at a depth \(q\ge r+1\) lie in disjoint recursion
nodes. For the three-scale menu, the only retained nested pair has scales
\(r-1,r+1\) and phase-centre separation two, so it cannot be an opposite
boundary pair at such a \(q\).

Collapse two disjoint marked nodes of scales \(s,u\). The one-hole context
series is

\[
 U(z)={1\over1-2zC(z)}={1\over\sqrt{1-4z}},
\qquad
 [z^j]U(z)^2=4^j.
\tag{2.2}
\]

For one boundary orientation, the bridge size is

\[
                         j=q-(s+1)+O(1),
\tag{2.3}
\]

and for the reversed orientation it is
\(j=q-(u+1)+O(1)\). The earlier expression
\(j=q-s-u+O(1)\) is false; it is already negative when
\(q=r+1\) and \(s=u=r\).

Since \(q\le m/2\), after (2.3) the outer residual size is still
\(\Omega(m)\). A finite sum over least-common-ancestor and boundary
orientations is therefore bounded by

\[
 O\left({4^{m-s-u}\over\sqrt m}\right).
\tag{2.4}
\]

Multiplying by the two local filling counts gives

\[
 J_q^{s,u}
 =O\left(
 {4^{m-s-u}\over\sqrt m}C_{s-1}C_{u-1}
 \right)
 =O\left({W\over(su)^{3/2}}\right).
\tag{2.5}
\]

Summing the nine ordered pairs in the \(r-1,r,r+1\) menu yields

\[
\boxed{J_q=O(W/r^3).}
\tag{2.6}
\]

Every mixed second difference has negative mass at most two, so the
complete nonlinear rescue against a fixed \(0\)-\(1\) target potential is
\(O(W/r^3)=o(Z_r)\).

The order (2.6) is therefore verified, but it does not imply a no-go once
the number of available bits is enlarged. For arbitrary activity
\(S_x=\sum_e x_e\), the correct dual inequality has the form

\[
 K_{q,p}(\bar\mu_q)-(W-N_q)
 \ge D_r-(W-N_q)-3S_x-O(W/r^3).
\tag{2.7}
\]

The two-scale proof inserted \(S_x\le D_r/4\), leaving \(D_r/4\).
A three-scale cube permits \(S_x\) near \(D_r/3\), and (2.7) then has no
positive main term. This refutes the claimed automatic extension to
bounded adjacent-scale menus.

## 3. Complete three-scale conflict classification

For a scale \(s\) parameter \(R\in{\cal D}_{s-1}\), write

\[
 A_s(R)=1100R,\qquad B_s(R)=1010R.
\tag{3.1}
\]

Equal-scale nodes are disjoint. For adjacent scales \(s,s+1\), the unique
nested conflict is

\[
 110010R\longleftrightarrow101010R
             \longleftrightarrow101100R.
\tag{3.2}
\]

The two switches modify consecutive phases and cannot both be present.
Every switch has at most one such conflict above and at most one below.

For scales \(s,s+2\), a nested overlap occurs exactly when the larger
parameter is \(A_s(R)\) or \(B_s(R)\). The smaller node is the parameter
subtree of the larger row. Their starts are two pair-positions apart, so
their modified states are two phases apart. Their affected \(Y\)-edge
slots are disjoint, and the two local ownership permutations commute.
Thus there is no \(s,s+2\) conflict.

A switch can be incident with both adjacent matchings only in the nested
four-row pattern

\[
\begin{aligned}
 X&=11001010R,\\
 Y&=10101010R,\\
 Z&=10110010R,\\
 W&=10101100R,
\end{aligned}
\qquad R\in{\cal D}_{r-2}.
\tag{3.3}
\]

The scale-\(r+1\), scale-\(r\), and scale-\(r-1\) switches are respectively

\[
                         X\leftrightarrow Y,\qquad
 Y\leftrightarrow Z,\qquad
 Y\leftrightarrow W.
\tag{3.4}
\]

On the common row \(Y\), they modify phases \(1,2,3\). The first and third
commute; either adjacent pair is illegal. Hence (3.4) is one \(P_3\)
component of the conflict graph, not a triple hyperedge.

There are no other triple conflicts. Indeed, after all illegal adjacent
pairs are excluded, every row's modified phases have pairwise distance at
least two. Their affected state-and-colour slots are disjoint, so all
remaining local ownership permutations commute jointly.

It follows that the conflict graph is a disjoint union of isolated
vertices, \(K_2\)'s, and \(P_3\)'s. The two adjacent edge counts and the
number of \(P_3\)'s are exactly those in (0.5). Therefore:

* \(E_--T\) components are lower \(K_2\)'s;
* \(E_+-T\) components are upper \(K_2\)'s;
* \(T\) components are \(P_3\)'s.

A maximum independent set deletes one vertex from every \(K_2\) and the
middle vertex from every \(P_3\), proving (0.4). The selection can be made
to retain every scale-\(r-1\) vertex. Every subset of this selection is
an exact \(X/Y\)-ownership factor, so it is a literal Boolean cube.

## 4. Exact capacity envelopes

The maximum weighted independent set can be evaluated componentwise.
At \(q\ge r+2\), assign base weight three to every bit. Retaining the
lower endpoint of every lower \(K_2\), both endpoints of every \(P_3\),
and either endpoint of every upper \(K_2\) gives weight \(3L_3\). Every
scale-\(r-1\) fixed arm which crosses the overloaded-set cut adds one;
their total is \(B_q\). This proves (0.7).

At \(q=r+1\), scale \(r+1\) is at its own depth. Its two intrinsic marked
arms stay over cap, so its weight is at most two. The lower and middle
base weights are three. On a lower \(K_2\) one keeps the lower endpoint;
on an upper \(K_2\) one keeps the middle endpoint; on a \(P_3\) one keeps
both endpoints. The losses are respectively \(3,2,3\), proving (0.9).

At \(q=r\), the weights are \(3,2,4\) before the lower bonus. The same
component calculation gives

\[
\boxed{
 {\cal V}_{r}
 =3M_-+2M_0+4M_+
  -2E_- -2E_+ +2T+B_r.}
\tag{4.1}
\]

The Catalan and central-binomial quotients give

\[
\begin{aligned}
 {M_-\over Z_r}&={1\over16}+O(r^{-1}),&
 {M_0\over Z_r}&={1\over16}
     +O(r^{-1}+r/m),\\
 {M_+\over Z_r}&={1\over16}
     +O(r^{-1}+r/m),&
 {E_-\over Z_r}&={1\over64}
     +O(r^{-1}+r/m),\\
 {E_+\over Z_r}&={1\over64}
     +O(r^{-1}+r/m),&
 {T\over Z_r}&={1\over256}
     +O(r^{-1}+r/m).
\end{aligned}
\tag{4.2}
\]

Consequently, with \(\beta_q=B_q/Z_r\),

\[
\boxed{
\begin{aligned}
 {{\cal V}_{r}\over Z_r}
  &={130\over256}+\beta_r+o(1),\\
 {{\cal V}_{r+1}\over Z_r}
  &={110\over256}+\beta_{r+1}+o(1),\\
 {{\cal V}_{\ge r+2}\over Z_r}
  &={123\over256}+\beta_q+o(1).
\end{aligned}}
\tag{4.3}
\]

Since

\[
 {D_r\over Z_r}={1\over2}-{1\over t},
\tag{4.4}
\]

the first and third lines of (4.3) exceed \(D_r/Z_r\) uniformly for
\(4\le t<16+o(1)\), even at \(\beta=0\). The middle line gives the exact
necessary condition

\[
 \beta_{r+1}\ge
 \left({9\over128}-{1\over t}\right)_++o(1),
\tag{4.5}
\]

which is equivalent to (0.11) because \(M_-/Z_r=1/16+o(1)\).

## 5. Why \(t\) does not determine the lower bonus

For one scale-\(r-1\) parent, put

\[
 d=C_{r-1},\qquad e=C_{r-2}.
\tag{5.1}
\]

Its intrinsic marked profile under \(k\) selected switches is

\[
                         (d,e,e)\longmapsto(d-k,e,e+k).
\tag{5.2}
\]

If these were isolated physical targets with exact loads \(d,e,e\), the
maximum marked cap-tail reduction would be

\[
 u_r(t)=
 \begin{cases}
 \min\{e,d-p,p-e\},&e<p<d,\\
 0,&e\ge p.
 \end{cases}
\tag{5.3}
\]

Asymptotically,

\[
 {u_r(t)\over p}
 =
 \begin{cases}
 t/4-1,&4\le t\le16/3,\\
 t/16,&16/3\le t\le8,\\
 1-t/16,&8\le t\le16,
 \end{cases}
 \quad+o(1).
\tag{5.4}
\]

This explains the apparent attraction of the lower scale. It has useful
marked slack in the interior of the Catalan interval and loses it at both
ends.

But (5.3) is not a global theorem. Different parent contexts can have the
same physical suffix destination. Such collisions raise the actual
destination preload and can erase its slack; simultaneous source
collisions can also pool source excess. Therefore neither \(u_r(t)\) nor
\(t\) alone determines \(B_q\).

The exact fixed-cut quantity is

\[
 B_q
 =C_{r-2}\,
 \#\{C:\mu_q(T_{C,q})\le p
       \text{ and the retained lower packet at }C
       \text{ is credited}\},
\tag{5.5}
\]

with the obvious fractional version for a product mean. Formula (5.5)
must be evaluated jointly with the three variable arms. Marginal
Catalan preload and marginal destination counts may not be multiplied.

## 6. Uniform decision

The requested low/high dichotomy is false.

* The lower layer does remove the raw low-\(t\) capacity shortage.
* Once the maximum literal three-scale cube is used, it also removes the
  old high-\(t\) three-arm shortage: \(3L_3>D_r\) uniformly.
* At \(q=r+1\), a small suffix-destination bonus is needed only for
  \(t>128/9+o(1)\); its required fraction is (0.11).
* In the thin strip \(t>\tau_r\), that bonus is impossible and the
  one-depth residual (0.13) follows.
* Outside that thin strip, neither Catalan arithmetic nor the hereditary
  suffix dual decides the direction. The unresolved input is the joint
  target statement (0.11) together with simultaneous favourable action
  of the other arms.

Thus the \(r-1,r,r+1\) menu is a genuine surviving recursive-trade lane at
the scalar/full-ownership level, except for a harmless \(o(W)\) self-depth
residual near the very top Catalan ratio. It is not yet a coefficient-one
construction: the missing theorem is directional and correlation-sensitive,
not another conflict count.
