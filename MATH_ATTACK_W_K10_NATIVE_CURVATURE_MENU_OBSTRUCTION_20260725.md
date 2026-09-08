# Lane W: K10 native curvature, type capacity, and the seam-menu obstruction

Date: 2026-07-25

## 0. Exact outcome

Put

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
t=\operatorname{Cat}_m=\frac Wn,
\qquad
H=\lceil A\sqrt m\rceil .
\]

Let

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor,
\qquad
S_A(m)=\sum_{q=1}^{H}\frac1{c_q}.
\]

All statements below are for fixed \(A>0\) and sufficiently large \(m\),
so \(H\le m-2\).  The doubled weighted floor collision is

\[
Q_A(F)=
\sum_{q=1}^{H}\frac1{c_q}
\sum_{S\in\binom{[n]}{m-q}}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
\tag{0.1}
\]

The requested K10 composition splits into one positive theorem and one
sharp obstruction.

### Proved positive theorem

Every persistent K10 packet component has exact weighted shadow norm

\[
\boxed{\|d_R\|_w^2=8S_A(m)-4}
\tag{0.2}
\]

and floor curvature

\[
\boxed{
\kappa_F(K_R)\le16S_A(m)-8,\qquad
\frac{\kappa_F(K_R)}{s_R}\le8S_A(m)-4,
}
\tag{0.3}
\]

where \(s_R=2\) wreaths per shore.  Pairing all
\(r_m=\operatorname{Cat}_{m-2}\) native components costs at most

\[
\boxed{
r_m(8S_A(m)-4)
=\left(\frac{\kappa_A}{2}+o_A(1)\right)t\sqrt m
=O_A(Ht),
}
\tag{0.4}
\]

where

\[
\kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
\]

Thus K10 really does supply a factor-scale curvature/type-capacity atlas.
If one of these native components also carries the Reynolds supporting
signal, it strictly decreases \(Q_A\) whenever

\[
Q_A(F)>(8S_A(m)-4)t.
\tag{0.5}
\]

### Proved obstruction

The native components are not shadow twins: their depth-one effects are
linearly independent, hence no two agree up to sign.

More decisively, every factor in their complete packet cube satisfies

\[
\boxed{
Q_A(F)\ge\left(\frac18-o(1)\right)W\gg Ht.
}
\tag{0.6}
\]

Choose a \(Q_A\)-minimizer inside this finite cube.  No nonempty union of
native packet components decreases its energy, despite (0.3), (0.4), and
(0.6).  Hence large energy does not force the Reynolds tangent into the
bounded-curvature K10 atlas, and iterating only those packets cannot prove
constant one.

K10's degree-three menu does not supply the missing fresh types:

* its seam count is pooled over \(m\) different transposition overlays;
* seams are ownership edges, not distinct components or lower-shadow
  occurrence pairs;
* a Boolean cube of fixed-base conformal components from different overlays
  requires pairwise-disjoint old supports and pairwise-disjoint new supports;
* the fixed join of the menu owner partitions is one block, so there is no
  nontrivial single row subset saturated for every menu colour; and
* sequential recomputation is the only escape, but K10 proves neither seam
  persistence nor multidepth type diameter after recomputation.

This is not merely a restatement of the curvature gate.  It is an exact
high-energy local-minimum obstruction for the proposed native iteration and
an exact fixed-base support-compatibility criterion for pooling seam-colour
trades.
No unconditional negative-energy trade on the prepared factor follows from
the currently proved K10 hypotheses.

## 1. K10's persistent native component atlas

Let \(F^{\mathrm{MSW}}_m\) be the canonical MSW factor and

\[
\tau=(2\ 3),\qquad M=m-2.
\]

For every Dyck word \(R\in\mathcal D_M\), the canonical
\(\tau\)-overlay has the genuine size-two component

\[
K_R=\{1100R,1010R\}.
\tag{1.1}
\]

The two shores of \(K_R\) each contain two physical wreaths and partition
the same \(2n\) middle roots.  Components for different \(R\) have disjoint
owner rows and invariant root unions.

K10 chooses a laminar half-signing

\[
x=(x_R)_{R\in\mathcal D_M}\in\{0,1\}^{\mathcal D_M}
\tag{1.2}
\]

and obtains the literal exact factor \(F_m^{\mathrm{lam}}\) by choosing the
\(x_R\)-shore of every \(K_R\).  Its selected packet count is

\[
\sum_Rx_R=\frac12\operatorname{Cat}_{m-2}+O(1).
\tag{1.3}
\]

Therefore it replaces

\[
\operatorname{Cat}_{m-2}+O(1)
=\left(\frac1{16}+o(1)\right)t
\tag{1.4}
\]

wreath rows and moves

\[
\left(\frac1{16}+o(1)\right)W
\tag{1.5}
\]

middle roots nontrivially.

### Lemma 1.1 (persistence after laminar preparation)

For every \(R\), the two shores of \(K_R\) remain one complete connected
component of

\[
\Gamma(F_m^{\mathrm{lam}},\tau F_m^{\mathrm{lam}}).
\tag{1.6}
\]

The same is true at every vertex of the full \(K_R\)-shore cube.

#### Proof

The invariant middle-root union of \(K_R\) is disjoint from all other
native packet root unions.  A cube vertex chooses one complete shore on
that union.  Applying \(\tau\) chooses the opposite shore.  Every middle
root in the union joins its current owner to its opposite-shore owner, and
no such edge leaves the union.  The original packet overlay was connected,
so it remains exactly one component. \(\square\)

Write \(z_R\) for the oriented move from one shore of \(K_R\) to the
other, and

\[
u_{R,q}=A_qz_R,\qquad
d_R=\left(c_q^{-1/2}u_{R,q}\right)_{q\le H}.
\tag{1.7}
\]

Changing the current shore only replaces \(z_R\) and \(d_R\) by their
negatives.

## 2. Exact all-depth native shadow norm

The exact four-arm formula may be written as follows.  In the omitted-label
order for \(R\), let \(E_R\) and \(O_R\) be the odd- and even-position
sublists of the common tail, of sizes \(m-1\) and \(m-2\).  For a set \(K\)
disjoint from \(2,3\), put

\[
\partial K=e_{K\cup\{3\}}-e_{K\cup\{2\}}.
\tag{2.1}
\]

For \(1\le q\le m-2\), set

\[
\ell=m-q-1.
\]

Then

\[
\boxed{
u_{R,q}
=
\partial\operatorname{suf}_{\ell}(O_R)
+\partial\operatorname{suf}_{\ell}(E_R)
-\partial\operatorname{pre}_{\ell}(E_R)
-\partial\operatorname{pre}_{\ell}(O_R).
}
\tag{2.2}
\]

### Lemma 2.1 (exact support norms)

\[
\boxed{
\|u_{R,1}\|_2^2=4,\qquad
\|u_{R,q}\|_2^2=8\quad(2\le q\le m-2).
}
\tag{2.3}
\]

Every nonzero coefficient is \(+1\) or \(-1\).

#### Proof

At \(q=1\), \(\ell=m-2=|O_R|\), so the two \(O_R\)-terms in
(2.2) cancel.  The proper prefix and suffix of the distinct-label list
\(E_R\) are different, leaving two disjoint dipoles and four unit cells.

For \(q\ge2\),

\[
1\le\ell\le m-3<|E_R|,|O_R|.
\]

The \(E_R\)-cores and \(O_R\)-cores are disjoint.  Within either list, a
proper prefix cannot equal an equal-length proper suffix.  Thus the four
cores in (2.2) are distinct, and their eight extensions by \(2\) or \(3\)
are distinct. \(\square\)

### Theorem 2.2 (native curvature and pairing capacity)

At every vertex of the native cube and for every \(R\),

\[
\|d_R\|_2^2
=4+\sum_{q=2}^{H}\frac8{c_q}
=8S_A(m)-4.
\tag{2.4}
\]

Let \(k_{q,S}=\mu_q(S)-c_q\), and define

\[
\sigma_F(q,S)=
\begin{cases}
-1,&k_{q,S}\le0,\\
+1,&k_{q,S}\ge1.
\end{cases}
\tag{2.5}
\]

The exact floor curvature of \(K_R\) is

\[
\kappa_F(K_R)
=\sum_{q,S}\frac1{c_q}
\left(u_{R,q}(S)^2+\sigma_F(q,S)u_{R,q}(S)\right).
\tag{2.6}
\]

It obeys

\[
\kappa_F(K_R)\le16S_A(m)-8,
\qquad
\frac{\kappa_F(K_R)}2\le8S_A(m)-4.
\tag{2.7}
\]

Moreover the native vectors admit a correlated pairing of cost at most

\[
\operatorname{Cat}_{m-2}(8S_A(m)-4).
\tag{2.8}
\]

#### Proof

Equation (2.4) is (2.3) with weights \(1/c_q\).  At a nonzero cell,
\(u=\pm1\), and therefore

\[
u^2+\sigma_Fu\in\{0,2\}.
\tag{2.9}
\]

The curvature is at most twice the weighted number of nonzero cells, which
proves (2.7).  The component has two old wreaths, so its side size is two.

Pair the \(r_m=\operatorname{Cat}_{m-2}\) vectors arbitrarily, adding one
zero vector if necessary.  For a pair \(d_R,d_{R'}\), choose the better
relative sign.  Then

\[
\min_{\varepsilon=\pm1}
\|d_R+\varepsilon d_{R'}\|^2
\le\|d_R\|^2+\|d_{R'}\|^2.
\tag{2.10}
\]

Independent fair signs between pairs kill all cross-pair inner products in
expectation.  Some common signing has cost at most the sum in (2.10),
namely (2.8). \(\square\)

The exact Catalan and Riemann-sum limits are

\[
\frac{\operatorname{Cat}_{m-2}}t\longrightarrow\frac1{16},
\qquad
\frac{S_A(m)}{\sqrt m}\longrightarrow\kappa_A.
\tag{2.11}
\]

Thus (2.8) is

\[
\left(\frac{\kappa_A}{2}+o_A(1)\right)t\sqrt m
=O_A(Ht).
\tag{2.12}
\]

### Corollary 2.3 (exact conditional descent threshold)

Define the clipped floor distance

\[
h(k)=
\begin{cases}
k,&k\le0,\\
k-1,&k\ge1.
\end{cases}
\tag{2.13}
\]

If a native packet at a factor \(F\) satisfies

\[
-\frac12\langle h_F,u_R\rangle_w
\ge\frac{Q_A(F)}{2t},
\tag{2.14}
\]

then switching it gives

\[
Q_A(F+z_R)-Q_A(F)
\le-\frac{2Q_A(F)}t+16S_A(m)-8.
\tag{2.15}
\]

It is therefore a strict exact-factor descent whenever

\[
Q_A(F)>(8S_A(m)-4)t.
\tag{2.16}
\]

#### Proof

The exact cell expansion is

\[
Q_A(F+z_R)-Q_A(F)
=2\langle h_F,u_R\rangle_w+\kappa_F(K_R).
\]

Use (2.7) and (2.14). \(\square\)

This proves the desired curvature scale.  It does not prove that a native
packet satisfies (2.14).

## 3. The packets are not shadow twins

The common K10 suffix-cylinder tag is only one marked dipole in (2.2).
The other three arms depend on the complete Dyck word \(R\).

### Lemma 3.0 (MSW flip-order identification)

For every nonempty Dyck word \(R\), the odd-index entries of its MSW flip
permutation are exactly \(\operatorname{Down}(R)\), the even-index entries
are exactly \(\operatorname{Up}(R)\), and its first entry is the
first-return down-step \(a_0(R)\).  Consequently the even arm used here has

\[
E_R=(4+\operatorname{Down}(R))\cup\{n\},
\qquad
\operatorname{first}(E_R)=4+a_0(R).
\tag{3.1}
\]

#### Proof

Strengthen the assertion inductively to both parities of the flip order.
Write the first-return decomposition as \(R=1u0v\), let \(|u|\) denote
ordinary word length, put \(a=|u|+2\), and let
\(\operatorname{rev}u\) denote reverse-complement.  The exact MSW recursion
is

\[
\rho(R)=
\bigl(a,\ a-\rho(\operatorname{rev}u),\ 1,\
       a+\rho(v)\bigr),
\tag{3.2}
\]

where the affine operations act entrywise.  The middle block has even
length.  Reversal and complementation exchange up- and down-step positions,
while the map \(j\mapsto a-j\) returns them, shifted by the initial step, to
their positions inside \(u\).  Thus the odd slots after the leading \(a\)
are precisely the shifted down-steps of \(u\); the tail contributes
\(a+\operatorname{Down}(v)\).  Together with \(a\), these are exactly all
down-steps of \(R\).  The same argument with the opposite parity gives all
up-steps.  Finally \(a=|u|+2\) is exactly the down-step closing the first
Dyck atom \(1u0\), hence \(a=a_0(R)\).  Shifting by four and appending \(n\)
gives (3.1). \(\square\)

### Theorem 3.1 (depth-one independence)

The vectors

\[
\{u_{R,1}:R\in\mathcal D_{m-2}\}
\tag{3.3}
\]

are linearly independent over every field.  In particular,

\[
u_{R,1}\ne\pm u_{R',1}\qquad(R\ne R').
\tag{3.4}
\]

#### Proof

Let \(D_R=\operatorname{Down}(R)\), and let \(a_0(R)\) be the first-return
down-step.  By Lemma 3.0, the proper suffix of \(E_R\) is
\(\{n\}\cup(4+(D_R\setminus\{a_0(R)\}))\).  Therefore, in the
four-target depth-one square for \(u_{R,1}\), the target

\[
S_R^*
=\{2,n\}\cup
\left(4+\bigl(D_R\setminus\{a_0(R)\}\bigr)\right)
\tag{3.5}
\]

has coefficient \(-1\).

The other two target forms that use the first even-list endpoint omit
\(n\); the target using \(3\) omits \(2\) and contains \(3\).  Hence only
the corresponding \(2,n\)-target of another word \(R'\) could equal
\(S_R^*\).

The map

\[
D_R\longmapsto D_R\setminus\{a_0(R)\}
\tag{3.6}
\]

is injective.  Given the displayed set, treat its positions as down-steps
and all other positions as up-steps, and let \(h'\) be the resulting
height.  The missing first-return position is

\[
a_0(R)=1+\max\{j:h'(j)=1\}.
\tag{3.7}
\]

Restoring it recovers \(R\).  Therefore \(S_R^*\) appears in no other
column \(u_{R',1}\).

In a nonzero linear relation, take any active \(R\).  Its
\(S_R^*\)-coordinate is the nonzero coefficient of \(u_{R,1}\), a
contradiction. \(\square\)

Thus K10 does not literally instantiate the exact-shadow-twin case.  The
factor-scale estimate (2.8) comes from correlated pairing with bounded
norm, not from equality of the full multidepth shadows.

## 4. What native pairing proves inside the full \(\tau\)-overlay

The full overlay

\[
\Gamma(F_m^{\mathrm{lam}},\tau F_m^{\mathrm{lam}})
\]

may contain components other than the native \(K_R\).  Let
\(D_{\mathrm{rest}}\) be the sum of their stacked weighted shadow vectors.

Keep every nonnative component on its all-positive side.  Pair the native
components as in Theorem 2.2 and use independent fair pair signs.  The
native signed sum has mean zero, so

\[
\mathbb E
\left\|
D_{\mathrm{rest}}+\sum_R\varepsilon_Rd_R
\right\|^2
=\|D_{\mathrm{rest}}\|^2
+\mathbb E\left\|\sum_R\varepsilon_Rd_R\right\|^2.
\]

Consequently the exact full-overlay signing optimum satisfies

\[
\boxed{
\beta_\tau
\le
\|D_{\mathrm{rest}}\|^2
+\operatorname{Cat}_{m-2}(8S_A(m)-4).
}
\tag{4.1}
\]

If

\[
\mathcal A_\tau
-\|D_{\mathrm{rest}}\|^2
>
\operatorname{Cat}_{m-2}(8S_A(m)-4),
\tag{4.2}
\]

the antipodal exact-factor identity gives a strict descent.

K10 proves no lower bound on the left side of (4.2).  Its laminar theorem
balances tagged cylinder dipoles, not the full component tangent, and its
seam theorem supplies no estimate on \(D_{\mathrm{rest}}\).

## 5. A high-energy local-minimum obstruction in the native cube

Let \(\mathscr X_m\) be the complete cube obtained by choosing either shore
of every native \(K_R\), while holding every other canonical
\(\tau\)-component at its canonical shore.  K10's laminar factor is one
vertex of \(\mathscr X_m\).

Let \(M_1(F)\) denote the number of depth-one holes.  The audited canonical
MSW marked-gap bound is

\[
M_1(F_m^{\mathrm{MSW}})
\ge J_m-\rho_1,
\tag{5.1}
\]

where

\[
J_m=(2m-3)\operatorname{Cat}_{m-2},
\qquad
\rho_1=\frac{2W}{m+2}.
\tag{5.2}
\]

Every native packet toggle has exactly two positive depth-one cells.
Therefore it can fill at most two current holes.

### Theorem 5.1 (uniform high energy on the native cube)

Every \(F\in\mathscr X_m\) satisfies

\[
\boxed{
M_1(F)
\ge J_m-\rho_1-2\operatorname{Cat}_{m-2}
=\left(\frac1{16}-o(1)\right)W.
}
\tag{5.3}
\]

Consequently

\[
\boxed{
Q_A(F)\ge2M_1(F)
\ge\left(\frac18-o(1)\right)W
\gg Ht.
}
\tag{5.4}
\]

#### Proof

Any cube vertex differs from the canonical corner in at most
\(\operatorname{Cat}_{m-2}\) packet signs.  Order those toggles
arbitrarily.  Each lowers the current hole count by at most two, proving
the first inequality.

The exact ratios are

\[
\frac{J_m}{W}
=\frac{m(m+1)}{4(2m-1)(2m+1)}
\longrightarrow\frac1{16},
\tag{5.5}
\]

\[
\rho_1=o(W),\qquad
\operatorname{Cat}_{m-2}=O(W/m).
\]

This proves (5.3).

For large \(m\),

\[
\lambda_1=\frac{m+2}{m}\in(1,2),\qquad c_1=1.
\]

Every hole has \(\mu_1=0\) and contributes exactly

\[
(0-1)(0-2)=2
\]

to the \(q=1\) summand of \(Q_A\).  Hence \(Q_A\ge2M_1\).
Finally,

\[
\frac{Ht}{W}=\frac Hn=O_A(m^{-1/2}),
\]

which proves the last comparison. \(\square\)

### Corollary 5.2 (native iteration cannot close)

There is an exact factor \(F_m^\square\in\mathscr X_m\) such that

\[
Q_A(F_m^\square)\ge\left(\frac18-o(1)\right)W
\tag{5.6}
\]

and no nonempty union of native packet components decreases \(Q_A\).

#### Proof

Choose a global minimizer of \(Q_A\) on the finite cube
\(\mathscr X_m\).  Every union of native component switches is another
cube vertex, so none has smaller value.  The lower bound is Theorem 5.1.
\(\square\)

At this minimizer every individual native packet obeys

\[
0\le
2\langle h_F,u_R\rangle_w+\kappa_F(K_R).
\]

Thus

\[
-\frac{\langle h_F,u_R\rangle_w}{2}
\le\frac{\kappa_F(K_R)}4
\le4S_A(m)-2.
\tag{5.7}
\]

On the other hand, Theorem 5.1 gives

\[
\frac{Q_A(F_m^\square)}{2t}
\ge\left(\frac{n}{16}-o(n)\right).
\tag{5.8}
\]

Since \(S_A(m)=O_A(\sqrt m)\) and \(n\sim2m\), no native component at
\(F_m^\square\) satisfies the Reynolds supporting bound (2.14).
The missing tangent has escaped the entire bounded-curvature atlas.

This proves more than failure of one greedy choice.  Starting from
\(F_m^{\mathrm{lam}}\), every iteration using arbitrary unions of the
persistent \(K_R\) remains in \(\mathscr X_m\), and every possible endpoint
still has the linear lower bound (5.4).

## 6. Normal form under transported packet toggles and menu relabelings

Let \(F_\varepsilon\) denote a native cube vertex.  Consider the class

\[
\mathscr N_m
=\{gF_\varepsilon:g\in S_n,\ 
\varepsilon\in\{0,1\}^{\mathcal D_{m-2}}\}.
\tag{6.1}
\]

### Theorem 6.1 (transported-atlas normal form)

The class \(\mathscr N_m\) is closed under:

1. arbitrary global coordinate relabelings; and
2. toggles of arbitrary transported native packets \(gK_R\).

Every finite word in these operations has endpoint \(gF_\varepsilon\).
Every endpoint satisfies

\[
Q_A(gF_\varepsilon)=Q_A(F_\varepsilon)
\ge\left(\frac18-o(1)\right)W.
\tag{6.2}
\]

#### Proof

A global relabeling \(\sigma\) sends \(gF_\varepsilon\) to
\((\sigma g)F_\varepsilon\).  A complete toggle of the transported packet
\(gK_R\) changes only the \(R\)-th bit of \(\varepsilon\).  Induction gives
the normal form.

The collision functional is invariant under global coordinate
permutations, so (6.2) follows from Theorem 5.1. \(\square\)

The K10 menu generates \(S_n\), but using its colours only as coherent
global relabelings therefore cannot escape the high-energy normal form.
Freshly recomputed partial ownership-component cuts are essential.

## 7. Why the seam reservoir is not a component-type reservoir

Let \(\mathcal R_m\) be K10's near-perfect matching of \(m\) coordinate
transpositions.  For \(\rho\in\mathcal R_m\), let \(L_\rho\) be the number
of certified genuine seams in the fresh overlay

\[
\Gamma(F_m^{\mathrm{lam}},\rho F_m^{\mathrm{lam}}).
\]

K10 proves

\[
\sum_{\rho\in\mathcal R_m}L_\rho
\ge\left(\frac{11}{128}-o(1)\right)W.
\tag{7.1}
\]

This is a sum over \(m\) different component cubes.

For some colour,

\[
L_\rho
\ge\left(\frac{11}{128}-o(1)\right)\frac Wm
=\left(\frac{11}{64}-o(1)\right)t.
\tag{7.2}
\]

If a component has \(s_C\) wreaths on its old shore, then it has exactly
\(ns_C\) middle ownership edges.  Therefore (7.2) implies only

\[
\sum_{C\text{ carrying a seam}}s_C
\ge\frac{L_\rho}{n}
=\Omega(t/m).
\tag{7.3}
\]

It gives no lower bound on the number of components, no upper bound on
their sizes, and no bound on their full multidepth shadow diameter.
K10's numerical seam hypotheses do not exclude concentration in one
component.  The obstruction to a generic seam-to-dispersion implication is
real: the canonical connected-overlay example carries

\[
\left(\frac1{24}+o(1)\right)t
\]

noncommuting seams in one component.

### Lemma 7.1 (cross-colour support compatibility)

Let \(F\) be an exact factor.  Suppose \(g_1,\ldots,g_r\) are squarefree
conformal trades from \(F\):

\[
A_0g_i=0,\qquad
\operatorname{supp}^-(g_i)\subseteq F,\qquad
\operatorname{supp}^+(g_i)\cap F=\varnothing,
\]

and \(F+g_i\) is exact for every \(i\).  Then

\[
F+\sum_{i\in I}g_i
\tag{7.4}
\]

is a \(0/1\) exact factor for every subset \(I\) if and only if the
negative supports are pairwise disjoint and the positive supports are
pairwise disjoint.

#### Proof

The ownership equation is automatic:

\[
A_0\left(F+\sum_{i\in I}g_i\right)=\mathbf1.
\]

On a wreath already in \(F\), the resulting coefficient is one minus the
number of selected negative supports containing it.  It belongs to
\(\{0,1\}\) for every \(I\) exactly when no two negative supports meet.
Outside \(F\), the coefficient is the number of selected positive supports
containing it, and the analogous condition is pairwise disjointness.
Positive and negative supports cannot meet because of conformality relative
to \(F\). \(\square\)

Disjoint coordinate transposition colours do not imply disjoint wreath
supports.  K10 proves neither support condition in Lemma 7.1 for components
chosen from different fresh overlays.  Therefore its matching colours
cannot be pooled as columns of one Reynolds signing merely because the
coordinate graph has degree at most three.

## 8. Static common-subset join collapse

Let \(\mathcal O_m\) be K10's union of its Hamilton path and seam-colour
matching.  Its coordinate graph is connected, so

\[
\langle\mathcal O_m\rangle=S_n.
\tag{8.1}
\]

For a menu transposition \(\sigma\), let \(\mathcal P_\sigma\) be the
owner-component partition of \(F\) in \(\Gamma(F,\sigma F)\), after
identifying a right row \(\sigma E\) with \(E\).

### Theorem 8.1 (one-block fixed join)

\[
\boxed{
\bigvee_{\sigma\in\mathcal O_m}\mathcal P_\sigma
\text{ has one block.}
}
\tag{8.2}
\]

Hence a row family which is simultaneously a union of complete component
blocks for every fixed menu colour is either empty or all of \(F\).  Thus
there is no nontrivial single common-row-subset cut.  For an individual
colour \(\sigma\), the two choices coming from these common subsets have
endpoints \(F\) and \(\sigma F\), which have equal \(Q_A\).

#### Proof

First, the identification of the right row with its pullback is
component-faithful.  Indeed, among the \(n\) middle windows of a wreath,
some window contains either both exchanged coordinates or neither: the
total number of incidences of those two coordinates among the windows is
\(2m<n\).  Such a window is fixed by the transposition, so its ownership
edge joins the row to its identified right copy.

For one transposition \(\sigma\), two owner rows are related in
\mathcal P_\sigma\) whenever their middle roots are connected by

\[
X\longleftrightarrow\sigma X.
\tag{8.3}
\]

Conversely, every overlay-component path alternates ownership edges, and
after the right-row identification each two-edge segment pulls back to a
relation \(o_F(X)\sim o_F(\sigma X)\), where \(o_F(X)\) is the unique row
of \(F\) owning \(X\).  Therefore joining the partitions over the menu
colours gives exactly the row image of the Schreier graph of
\(\langle\mathcal O_m\rangle\) on \(\binom{[n]}m\).  By (8.1), this group
is \(S_n\), which is transitive on the middle layer.  Since every row owns
middle roots, the row image is connected.  This proves (8.2).

A single row subset saturated for every component partition must be a union
of join blocks, so only the empty and full subsets remain. \(\square\)

The conclusion concerns one common saturated row subset.  It does not rule
out choosing different component unions for different colours subject to
additional support compatibility, nor does it rule out sequentially
recomputed cuts.

The adjective degree-three refers to the coordinate-colour graph, not to
the ownership-component constraint graph.  It supplies no subcubic
Max-Cut or type-pairing theorem on the component columns.

## 9. Exact proved and unproved boundary

### Proved

1. The persistent K10 packet atlas has the exact all-depth norm (2.4) and
   curvature (2.7).
2. Its complete correlated pairing cost is \(O_A(Ht)\), with leading
   constant \(\kappa_A/2\).
3. A Reynolds-favourable native packet would strictly descend above the
   exact threshold (2.16).
4. The native packet effects are linearly independent at depth one and are
   not shadow twins.
5. Every endpoint of the native cube has
   \(Q_A\ge(1/8-o(1))W\).
6. The cube contains a high-energy minimizer with no decreasing native
   packet subset, so bounded curvature does not force tangent capture.
7. Global menu relabelings plus transported native toggles have the closed
   normal form (6.1) and remain at linear energy.
8. Separate-colour component trades require the exact support compatibility
   of Lemma 7.1; K10 supplies no such compatibility.
9. The static join of all degree-three menu partitions is one block and
   yields no nontrivial single common-row-subset circuit.

### Not proved

1. This report does not prove that the particular laminar vertex
   \(F_m^{\mathrm{lam}}\) itself has no initial decreasing native packet.
   It proves that every native-only iteration remains linearly bad and that
   a high-energy native local minimum exists.
2. No theorem here rules out a useful freshly recomputed component cut
   after one K10 seam colour.
3. K10 proves no persistence, distinct-component dispersion, tangent
   dominance, small multidepth diameter, or cross-colour support
   compatibility for those fresh components.
4. Consequently no unconditional negative-energy exact trade whenever
   \(Q_A\gg Ht\), and no constant-one theorem, follows from the prepared
   factor plus the present seam menu.

The sole surviving K10 route is chronological recomputation of genuinely
fresh complete ownership components, with a new theorem controlling their
full multidepth effects.  That is additional mathematics not contained in
the laminar \(1/16\)-density theorem or the degree-three seam count.
