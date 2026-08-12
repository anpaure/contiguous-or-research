# Cross-audit and constructive continuation of Y6: untouched-row spill restitution

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver,
computer algebra, or long computation is used. Every move called literal
below replaces one positive middle packing by another packing of the same
middle union, so it remains inside one integral exact-factor fibre.

---

## 0. Outcome

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m,\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\) is sufficiently large that
\(1\le H\le m-1\).

For \(1\le q\le H\), put

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor.
\]

If \(F\) is an exact factor, \(\mu_q^F(S)\) is the number of its wreath
rows having \(S\) as a cyclic \((m-q)\)-interval, and

\[
Q_q(F)=
\sum_{|S|=m-q}
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1),
\qquad
\mathcal Q_H(F)=\sum_{q=1}^H\frac{Q_q(F)}{c_q}.
\]

Every unqualified depth sum in this report runs over \(1\le q\le H\).
Structural containment statements which explicitly include \(q=0\) also
cover the middle rank.

The three requested Y6 claims pass independent audit.

1. The two-owner active-pair rigidity theorem is exact for
   \(0\le q\le m-1\): a middle-disjoint pair's common lower targets are
   determined pointwise by its union of middle supports.
2. The depth-one star matching identity has the stated constants and no
   missing ordering factor.
3. The likelihood-ratio implication

   \[
   \frac{\mathbb E_{\pi_{\mathscr C}}Q_1}{W}
   =
   \frac{m-1}{m+1}\alpha_{\mathscr C}
   -\frac4{m+2}
   \]

   is exact. Thus an SCC-scale class must have
   \(\alpha_{\mathscr C}=O_A(m^{-1/2})\), and the same necessary statement
   holds for the whole-fibre law under GCC.

The untouched-row term in Y6.20a is also now controlled exactly. It is
literal spill restitution, not an unstructured error. For a two-row
fixed-union replacement, the complete quadratic change is

\[
\boxed{
\Delta Q_q
=-\frac2{q+1}
\left(
\sum_{S\in P_q}R_{q,S}
-\sum_{S\in N_q}R_{q,S}
\right),
}
\tag{0.1}
\]

where \(P_q\) are newly acquired singleton lower targets, \(N_q\) are
lost singleton targets, and

\[
R_{q,S}
=A_{q,S}(\mathcal U)+\rho^G_{q,S}
\]

is the active middle-containment plus untouched-row spill. At depth one,
the active term is constant on changed coordinates and

\[
\boxed{
\Delta Q_1
=-
\left(
\sum_{S\in P_1}\rho^G_{1,S}
-\sum_{S\in N_1}\rho^G_{1,S}
\right).
}
\tag{0.2}
\]

Thus a fixed-union replacement improves depth one exactly when it moves
singleton ownership toward larger untouched spill.

More generally, for every fixed \(k\)-row middle union \(\mathcal U\)
and untouched completion \(G\), this report constructs two exact
restitution functionals:

\[
\operatorname{Rest}_Q(\mathcal A),
\qquad
\operatorname{Rest}_C(\mathcal A).
\]

They satisfy

\[
\boxed{
\mathcal Q_H(G\mathbin{\dot\cup}\mathcal A)
=K_Q(\mathcal U,G)-2\operatorname{Rest}_Q(\mathcal A),
}
\tag{0.3}
\]

\[
\boxed{
\mathcal C_H(G\mathbin{\dot\cup}\mathcal A)
=K_C(\mathcal U,G)-\operatorname{Rest}_C(\mathcal A).
}
\tag{0.4}
\]

Consequently, replacing the active packing by a literal decomposition of
\(\mathcal U\) maximizing either restitution functional is a genuine
nonincreasing exact-factor move, strict whenever the present decomposition
is not a maximizer. This is the requested constructive clipped-restitution
move.

The largest literal neighborhood supplied by a fixed comparator is also
identified exactly. Its old/new ownership multigraph splits into balanced
connected components, and precisely those whole components may be switched
independently. An alternating Johnson cycle smaller than an ownership
component is not automatically legal. For three rows, every nontrivial
comparator reduces either to one connected two-for-two component plus a
common row, or to one connected three-for-three component.

This stronger neighborhood is sparse. In every exact factor the
cross-Johnson row graph has maximum degree at most

\[
D_m=n\bigl(m(m+1)-2\bigr),
\]

almost every fixed-size row union has a unique decomposition, and the old
supports of primitive three-for-three moves number at most
\(B\binom{D_m}{2}\). Thus a three-row theorem must target a polynomial
exceptional neighborhood around the colliding rows; generic buffer
abundance is irrelevant to literal realizability.

The scalar convexity side is complete: both restitution functionals are
\(M\)-concave on the ambient fixed-mass load lattice. The missing theorem is
literal exchange closure. Actual wreath-decomposition profiles preserve all
point margins and generally have no nontrivial unit \(M\)-exchange. A
high-energy factor is not proved to contain a non-maximal three-row or
bounded-row middle union.

Accordingly, SCC, GCC, MWB, and constant one are not proved here. Section 7
states a concrete three-row clipped-restitution condition which would imply
constant one without any full-Graver closure. Its hypothesis remains
unproved.

---

## 1. Cross-audit of the Y6 decisive claims

### 1.1 Active-pair rigidity

For a wreath \(R\), an \((m-q)\)-set \(S\), and
\(0\le q\le m-1\), let

\[
a_{q,S}(R)
=\#\{X\in\mathcal I_0(R):S\subseteq X\}.
\]

Complementing middle intervals gives

\[
\boxed{a_{q,S}(R)\le q+1,}
\tag{1.1}
\]

with equality exactly when \(S\in\mathcal I_q(R)\). Indeed, middle
supersets correspond to cyclic \((m+1)\)-intervals contained in \(S^c\),
whose size is \(m+q+1<2(m+1)\). At most one cyclic run contributes; it
contains at most \(q+1\) such intervals, with equality precisely when
\(S^c\) is one run.

The range matters. At \(q=m\), \(S=\varnothing\) and
\(a_{m,S}(R)=n>m+1\). Y6 uses only \(q\le H\le m-1\), so no stated
fixed-window theorem is affected.

If two middle-disjoint row pairs have the same middle union
\(\mathcal U\), then

\[
A_{q,S}(\mathcal U)
=\#\{X\in\mathcal U:S\subseteq X\}
\]

is the sum of their two containment counts. It reaches \(2(q+1)\) exactly
when both rows own \(S\) as a lower interval. Therefore the common
lower-target set, not merely its cardinality, is determined by
\(\mathcal U\). Y6.1 and its weighted consequence are valid.

The whole-fibre factorization is also exact. Every decomposition of
\(\mathcal U\) has exactly the same set of packings of the middle
complement. There is no ordered-pair factor. Class-restricted factorization
is not asserted and need not hold.

Finally, Y6.20a has the correct factor two. The floor-linear terms cancel
because every rank load has fixed total \(W\); the active-square term is
fixed because, writing \(h_q\) for the number of lower targets owned by
both active rows,

\[
\sum_S\ell_q(S)^2=2n+2h_q
\]

and \(h_q\) is union-rigid. Only cross-overlap with untouched rows remains.

### 1.2 Depth-one matching and likelihood ratio

For a fixed \((m-1)\)-set \(S\), the selected Johnson edges of color
\(S\) form a matching on the \(m+2\) vertices outside \(S\), and its size
is \(Z_S=\mu_1(S)\). Here \(\lambda_1=(m+2)/m\) and \(c_1=1\).
For an \(S_n\)-stable class,

\[
\mathbb E Z_S=\frac{m+2}{m}.
\]

With

\[
K=\binom{m+2}{2},\qquad L=\binom m2,
\]

let \(p_m\) be the probability that a prescribed color-\(S\) edge is
selected, and let \(r_{\mathscr C}\) be the conditional probability that
a prescribed disjoint edge is selected given the first edge. The fixed-edge
marginal and disjoint-edge conditional probability obey

\[
p_m=\frac{\mathbb EZ_S}{K}
=\frac2{m(m+1)},
\tag{1.2}
\]

\[
\mathbb E[Z_S(Z_S-1)]
=\frac{m+2}{m}Lr_{\mathscr C}.
\tag{1.3}
\]

Since

\[
\frac{\mathbb E Q_1}{N_1}
=\mathbb E[(Z_S-1)(Z_S-2)],
\qquad
N_1=\frac m{m+2}W,
\]

one obtains exactly

\[
\boxed{
r_{\mathscr C}
=
\frac{\displaystyle 4/(m+2)+\mathbb E Q_1/W}
{\binom m2},
}
\tag{1.4}
\]

\[
\boxed{
\frac{\mathbb E Q_1}{W}
=\frac{m-1}{m+1}\alpha_{\mathscr C}
-\frac4{m+2},
\qquad
\alpha_{\mathscr C}=\frac{r_{\mathscr C}}{p_m}.
}
\tag{1.5}
\]

If

\[
\mathbb E\mathcal Q_H\le C_AHB,
\]

then \(Q_1\le\mathcal Q_H\), \(HB/W=H/n\), and

\[
\alpha_{\mathscr C}
\le
\frac{m+1}{m-1}
\left(
\frac4{m+2}+\frac{C_AH}{n}
\right)
=O_A(m^{-1/2}).
\tag{1.6}
\]

All denominators and constants in Y6.2--Y6.5 are therefore valid.

Two wording qualifications are useful. The fixed-path homomesy theorem
controls fixed path-occurrence marginals, not arbitrary joint or multipath
laws. Its depth-two conditional probability concerns a prescribed
compatible continuation at the specified endpoint. Also, after deleting
the \(O(1/m)\) incompatible candidate row pairs, the average in Y6.49
acquires the harmless factor \((1-\varepsilon_m)^{-1}\), already absorbed
by its big-\(O\) notation.

---

## 2. Exact spill normal form for the untouched-row term

Let

\[
F=G\mathbin{\dot\cup}\{R,D\},
\qquad
F'=G\mathbin{\dot\cup}\{R',D'\}
\tag{2.1}
\]

be exact factors, where the two active pairs are middle-disjoint packings
of the same middle union \(\mathcal U\).

At depth \(q\), put

\[
u_q(E,S)=\mathbf1_{\{S\in\mathcal I_q(E)\}},
\]

\[
\ell_q(S)=u_q(R,S)+u_q(D,S),
\qquad
\ell'_q(S)=u_q(R',S)+u_q(D',S).
\tag{2.2}
\]

Active-pair rigidity says that \(\ell_q(S)=2\) if and only if
\(\ell'_q(S)=2\). Since both profiles have total \(2n\), define

\[
P_q=\{S:\ell_q(S)=0,\ \ell'_q(S)=1\},
\]

\[
N_q=\{S:\ell_q(S)=1,\ \ell'_q(S)=0\}.
\tag{2.3}
\]

Then no other coordinate changes and

\[
\boxed{|P_q|=|N_q|=:t_q\le2n.}
\tag{2.4}
\]

For a row \(E\), define the literal spill

\[
\rho_{q,S}(E)
=a_{q,S}(E)
-(q+1)u_q(E,S),
\qquad
0\le\rho_{q,S}(E)\le q.
\tag{2.5}
\]

Let

\[
\rho^G_{q,S}=\sum_{E\in G}\rho_{q,S}(E),
\qquad
x_q(S)=\mu_q^G(S),
\tag{2.6}
\]

and

\[
T_q=\binom{m+q+1}{q},
\qquad
R_{q,S}=A_{q,S}(\mathcal U)+\rho^G_{q,S}.
\tag{2.7}
\]

### Lemma 2.1 -- exact-cover restitution

\[
\boxed{
T_q-A_{q,S}(\mathcal U)
=(q+1)x_q(S)+\rho^G_{q,S}.
}
\tag{2.8}
\]

#### Proof

There are exactly \(T_q\) middle \(m\)-sets containing \(S\). The active
union contains \(A_{q,S}(\mathcal U)\) of them, and the untouched rows
partition the rest. Every untouched lower owner consumes exactly \(q+1\)
such middle sets; every other containment is counted by \(\rho\).
\(\square\)

### Theorem 2.2 -- untouched-row spill transport

For the full quadratic floor energy at depth \(q\),

\[
\boxed{
Q_q(F')-Q_q(F)
=-\frac2{q+1}
\left(
\sum_{S\in P_q}R_{q,S}
-\sum_{S\in N_q}R_{q,S}
\right).
}
\tag{2.9}
\]

#### Proof

Put \(\phi_c(t)=(t-c)(t-c-1)\). Then

\[
\phi_c(x+1)-\phi_c(x)=2(x-c).
\]

The changed coordinates in \(P_q\) gain one active owner, while those in
\(N_q\) lose one. Since their cardinalities agree, the \(c_q\)-terms
cancel and

\[
Q_q(F')-Q_q(F)
=2\left(\sum_{P_q}x_q-\sum_{N_q}x_q\right).
\]

Substitute (2.8). The constant \(T_q\) cancels because
\(|P_q|=|N_q|\), proving (2.9). \(\square\)

### Corollary 2.3 -- pure spill transport at depth one

For every changed target at \(q=1\),

\[
\boxed{A_{1,S}(\mathcal U)=2.}
\tag{2.10}
\]

Consequently,

\[
\boxed{
m=2x_1(S)+\rho^G_{1,S},
}
\tag{2.11}
\]

and

\[
\boxed{
Q_1(F')-Q_1(F)
=-
\left(
\sum_{S\in P_1}\rho^G_{1,S}
-\sum_{S\in N_1}\rho^G_{1,S}
\right).
}
\tag{2.12}
\]

#### Proof

On the side with no lower owner, two nonlower rows contribute at most one
middle superset each, so \(A_{1,S}\le2\). On the side with one lower
owner, that row contributes exactly two, so \(A_{1,S}\ge2\). Equality of
the middle union forces (2.10). Now use \(T_1=m+2\) in (2.8), and cancel
the constant active term in (2.9). \(\square\)

Thus the Y6 cross term has a sign criterion: a two-row same-union switch
improves \(Q_1\) exactly when its newly acquired singleton targets have
larger total untouched spill than its lost singleton targets.

---

## 3. Exact clipped corridor restitution

Define the unweighted corridor

\[
C_q(F)=\sum_S\chi_{c_q}(\mu_q^F(S)),
\qquad
\mathcal C_H(F)=\sum_{q\le H}\frac{C_q(F)}{c_q},
\tag{3.1}
\]

where

\[
\chi_c(t)=(c-t)_+ +(t-c-1)_+.
\]

Put

\[
\Theta_q=T_q-(q+1)c_q.
\tag{3.2}
\]

Equation (2.8) gives

\[
x_q(S)-c_q
=\frac{\Theta_q-R_{q,S}}{q+1}.
\tag{3.3}
\]

Use \(\operatorname{sgn}(0)=0\).

### Theorem 3.1 -- exact clipped two-row transport

\[
\boxed{
C_q(F')-C_q(F)
=
\sum_{S\in P_q}\operatorname{sgn}(\Theta_q-R_{q,S})
-
\sum_{S\in N_q}\operatorname{sgn}(\Theta_q-R_{q,S}).
}
\tag{3.4}
\]

#### Proof

For every integer \(x\),

\[
\chi_c(x+1)-\chi_c(x)=\operatorname{sgn}(x-c).
\]

Apply this on \(P_q\), reverse it on \(N_q\), and use (3.3).
\(\square\)

Define

\[
\tau_{q,S}
=
\left(
\frac{|\Theta_q-R_{q,S}|}{q+1}-1
\right)_+
=(|x_q(S)-c_q|-1)_+.
\tag{3.5}
\]

Then

\[
\boxed{
\begin{aligned}
\Delta Q_q-2\Delta C_q
=2\bigg(&
\sum_{S\in P_q}
\operatorname{sgn}(\Theta_q-R_{q,S})\tau_{q,S}\\
&-
\sum_{S\in N_q}
\operatorname{sgn}(\Theta_q-R_{q,S})\tau_{q,S}
\bigg).
\end{aligned}
}
\tag{3.6}
\]

Moreover,

\[
\tau_{q,S}
=\min\{
\chi_{c_q}(x_q(S)),
\chi_{c_q}(x_q(S)+1)
\}.
\tag{3.7}
\]

Consequently,

\[
\boxed{
\sum_{q\le H}\frac{|\Delta Q_q-2\Delta C_q|}{c_q}
\le
2\min\{\mathcal C_H(F),\mathcal C_H(F')\}.
}
\tag{3.8}
\]

In particular,

\[
\left|
\Delta\mathcal Q_H-2\Delta\mathcal C_H
\right|
\le
2\min\{\mathcal C_H(F),\mathcal C_H(F')\}.
\tag{3.9}
\]

#### Proof of (3.6)--(3.9)

For the integer \(d=x_q(S)-c_q\),

\[
d=\operatorname{sgn}(d)
\left(1+(|d|-1)_+\right).
\]

On a gained coordinate the quadratic increment is \(2d\) and the clipped
increment is \(\operatorname{sgn}(d)\); on a lost coordinate both signs
reverse. This proves (3.6). A direct split into
\(d\le-1,d=0,d\ge1\) gives (3.7). On every affected coordinate, therefore,
\(\tau\) is bounded by the corridor contribution at both endpoints.
Summing first over affected coordinates and then over depths proves (3.8);
the triangle inequality proves (3.9). \(\square\)

The constant two is sharp for the scalar integer identity. The underlying
exact identity is

\[
\boxed{
(t-c)(t-c-1)=\chi_c(t)\bigl(\chi_c(t)+1\bigr).
}
\tag{3.10}
\]

Thus \(\mathcal Q_H=2\mathcal C_H+\mathcal T_H\), where

\[
\mathcal T_H
=\sum_{q,S}\frac{\chi_{c_q}(\mu_q(S))
(\chi_{c_q}(\mu_q(S))-1)}{c_q}\ge0,
\]

and (3.6) is exactly the one-step change in this tail energy.

---

## 4. The general \(k\)-row restitution optimizer

Let \(\mathcal U\) be a middle set union admitting one or more
decompositions into \(k\) pairwise middle-disjoint wreath rows. Let
\(\mathcal P_k(\mathcal U)\) be this finite set of active packings. Fix an
untouched packing \(G\) of the middle complement, so that

\[
G\mathbin{\dot\cup}\mathcal A
\]

is an exact factor for every
\(\mathcal A\in\mathcal P_k(\mathcal U)\).

For \(\mathcal A\in\mathcal P_k(\mathcal U)\), put

\[
\ell_{\mathcal A,q}(S)
=\#\{R\in\mathcal A:S\in\mathcal I_q(R)\}.
\tag{4.1}
\]

Every active profile has

\[
\sum_S\ell_{\mathcal A,q}(S)=kn.
\tag{4.2}
\]

The containment \(A_{q,S}(\mathcal U)\), untouched load \(x_q(S)\),
untouched spill \(\rho^G_{q,S}\), and restitution

\[
R_{q,S}=A_{q,S}(\mathcal U)+\rho^G_{q,S}
=T_q-(q+1)x_q(S)
\tag{4.3}
\]

are independent of the active decomposition.

### Theorem 4.1 -- exact quadratic restitution score

Define

\[
\boxed{
\operatorname{Rest}_Q(\mathcal A)
=
\sum_{q\le H}\frac1{c_q}
\left[
\frac{\langle R_q,\ell_{\mathcal A,q}\rangle}{q+1}
-\frac12\|\ell_{\mathcal A,q}\|_2^2
\right].
}
\tag{4.4}
\]

Then

\[
\boxed{
\mathcal Q_H(G\mathbin{\dot\cup}\mathcal A)
=K_Q(\mathcal U,G)-2\operatorname{Rest}_Q(\mathcal A),
}
\tag{4.5}
\]

where \(K_Q(\mathcal U,G)\) is independent of \(\mathcal A\). More
explicitly, its depth-\(q\) summand before division by \(c_q\) is

\[
K_{Q,q}
=
\sum_S\phi_{c_q}(x_q(S))
+kn\left(
\frac{2T_q}{q+1}-(2c_q+1)
\right).
\tag{4.6}
\]

#### Proof

For integers \(x,\ell\ge0\),

\[
\phi_c(x+\ell)
=\phi_c(x)+2x\ell+\ell^2-(2c+1)\ell.
\]

Sum in \(S\), use (4.2), substitute
\(x=(T_q-R_q)/(q+1)\), and then weight and sum in \(q\).
\(\square\)

### Corollary 4.2 -- literal quadratic restitution move

Choose

\[
\mathcal A_Q^*
\in
\operatorname*{arg\,max}_{\mathcal A\in\mathcal P_k(\mathcal U)}
\operatorname{Rest}_Q(\mathcal A).
\tag{4.7}
\]

Then

\[
\boxed{
\mathcal Q_H(G\mathbin{\dot\cup}\mathcal A_Q^*)
\le
\mathcal Q_H(G\mathbin{\dot\cup}\mathcal A),
}
\tag{4.8}
\]

with exact gain

\[
\boxed{
2\left(
\operatorname{Rest}_Q(\mathcal A_Q^*)
-\operatorname{Rest}_Q(\mathcal A)
\right).
}
\tag{4.9}
\]

Every endpoint is a literal positive exact factor. No signed intermediate
state or full-Graver closure is used.

For \(k=2\), two-owner rigidity gives

\[
\|\ell_{\mathcal A,q}\|_2^2=2n+2h_q(\mathcal U),
\]

so the quadratic term is constant and Theorem 4.1 reduces to the spill
transport formula in Section 2. For \(k\ge3\), the norm term records
collisions among the active rows. Three rows are the first size not ruled
out by two-owner rigidity from changing active collision multiplicity.
Existence of a useful alternate three-row decomposition is not asserted.

### Theorem 4.3 -- exact clipped restitution score

Define

\[
\boxed{
\operatorname{Rest}_C(\mathcal A)
=-
\sum_{q\le H}\frac1{c_q}
\sum_S\sum_{j=0}^{\ell_{\mathcal A,q}(S)-1}
\operatorname{sgn}\!\left(
\Theta_q-R_{q,S}+(q+1)j
\right).
}
\tag{4.10}
\]

Then

\[
\boxed{
\mathcal C_H(G\mathbin{\dot\cup}\mathcal A)
=K_C(\mathcal U,G)-\operatorname{Rest}_C(\mathcal A),
}
\tag{4.11}
\]

where

\[
K_C(\mathcal U,G)
=\sum_{q,S}\frac{\chi_{c_q}(x_q(S))}{c_q}.
\tag{4.12}
\]

Consequently, a literal maximizer
\(\mathcal A_C^*\) of \(\operatorname{Rest}_C\) is corridor-nonincreasing,
with exact corridor gain

\[
\operatorname{Rest}_C(\mathcal A_C^*)
-\operatorname{Rest}_C(\mathcal A).
\tag{4.13}
\]

#### Proof

Telescope

\[
\chi_c(x+\ell)-\chi_c(x)
=\sum_{j=0}^{\ell-1}\operatorname{sgn}(x+j-c)
\]

and use

\[
(q+1)(x_q(S)-c_q)
=\Theta_q-R_{q,S}.
\]

\(\square\)

Equations (4.9) and (4.13) are constructive in the exact mathematical
sense: within a specified finite family of literal decompositions, they
identify the exact steepest restitution endpoint. They do not assert that
the family is nontrivial or that the current endpoint is nonmaximal.

### Theorem 4.4 -- exact ownership-component neighborhood

Let \(\mathcal A,\mathcal A'\in\mathcal P_k(\mathcal U)\). First cancel
their common physical rows; each such row is forced in every exact hybrid
using rows from \(\mathcal A\cup\mathcal A'\), because no other row in
either packing contains any of its middle sets. On the residual middle
union, form a bipartite multigraph whose left vertices are the remaining
rows of \(\mathcal A\), whose right vertices are the remaining rows of
\(\mathcal A'\), and whose edge labelled by \(X\) joins the old and new
owners of \(X\). Every vertex has degree \(n\). Hence every connected
component contains the same number of old and new rows.

For each component \(K\), replacing all its old rows by all its new rows is
a literal exact-factor move. More strongly, a hybrid made only from rows of
\(\mathcal A\cup\mathcal A'\) covers \(\mathcal U\) exactly once if and
only if, on every component, it chooses all old rows or all new rows.

#### Proof

Degree counting in a component gives

\[
n|K\cap\mathcal A|=|E(K)|=n|K\cap\mathcal A'|.
\]

The edge labels of a component are therefore partitioned both by its old
rows and by its new rows, so switching the whole component preserves the
middle union exactly.

For the converse, the cancelled common rows are already forced. On the
disjoint residual row families, let \(s_R\in\{0,1\}\) record whether an
old row is used and \(t_D\in\{0,1\}\) whether a new row is used. Exact
coverage of the edge labelled \(X\), with owners \(R,D\), says

\[
s_R+t_D=1.
\]

Along every edge, therefore, \(s_R=1-t_D\). Connectivity makes all old
choices constant and all new choices their complement. This proves the
claim. \(\square\)

Thus Theorems 4.1 and 4.3 give an exact score for every legal
comparator-induced component switch. They give no license to switch a
proper alternating edge-cycle inside a component.

For \(k=3\), cancel common rows. A balanced component of side size one
would mean that one old and one new row have identical middle support,
hence are the same unoriented wreath. Consequently every nontrivial
three-row comparator is exactly one of:

1. a common row together with a connected two-by-two ownership component;
2. one connected three-by-three ownership component.

This is the complete genuine degree-three neighborhood. There is no
smaller alternating-cycle augmentation hidden inside it.

### Corollary 4.5 -- comparator-local clipped-restitution move

Let \(K_1,\ldots,K_r\) be the ownership components of a fixed comparator
\(\mathcal A'\). For \(J\subseteq[r]\), let \(\mathcal A^J\) be obtained
from \(\mathcal A\) by switching precisely the components indexed by
\(J\), and choose

\[
J^*\in\operatorname*{arg\,max}_{J\subseteq[r]}
\operatorname{Rest}_C(\mathcal A^J).
\]

Then \(G\mathbin{\dot\cup}\mathcal A^{J^*}\) is a positive exact factor
and

\[
\mathcal C_H(G\mathbin{\dot\cup}\mathcal A)
-\mathcal C_H(G\mathbin{\dot\cup}\mathcal A^{J^*})
=
\operatorname{Rest}_C(\mathcal A^{J^*})
-\operatorname{Rest}_C(\mathcal A)\ge0.
\]

The move is strict exactly when this comparator cube contains a hybrid of
higher clipped restitution. This enlarges single-component descent without
invoking the full factor-fibre Graver closure; it remains comparator-local.
Legality is Theorem 4.4 and the displayed gain is Theorem 4.3. \(\square\)

---

## 5. Ambient \(M\)-concavity and the literal exchange obstruction

Fix one depth and suppress \(q\). On the ambient fixed-sum integer lattice,
put

\[
\Phi_Q(\ell)
=\left\langle\frac R{q+1},\ell\right\rangle
-\frac12\|\ell\|_2^2.
\tag{5.1}
\]

### Theorem 5.1 -- the restitution objective is ambient \(M\)-concave

The function \(\Phi_Q\) is \(M\)-concave. If
\(x_i>y_i\) and \(x_j<y_j\), then, with

\[
x'=x-e_i+e_j,\qquad y'=y+e_i-e_j,
\]

\[
\boxed{
\Phi_Q(x')+\Phi_Q(y')
-\Phi_Q(x)-\Phi_Q(y)
=(x_i-y_i)+(y_j-x_j)-2\ge0.
}
\tag{5.2}
\]

The clipped functional in (4.10) is also ambient \(M\)-concave: its
coordinate marginal rewards are negatives of a nondecreasing sign
sequence.

#### Proof

The linear terms cancel between the two exchanged vectors. Expanding the
four affected squares gives the right side of (5.2), which is nonnegative
because both displayed coordinate gaps are positive integers. For the
clipped functional, the marginal reward for the \((j+1)\)-st unit in one
coordinate is

\[
-\operatorname{sgn}(\Theta-R+(q+1)j),
\]

a nonincreasing sequence in \(j\). A sum of such separable concave
coordinate functions on a fixed-total integer lattice obeys the same
two-vector exchange inequality. \(\square\)

Thus ordinary discrete convexity of the scalar cost is completely
available before literal wreath realizability is imposed.

For reference, a unit transfer from source \(N\) to destination \(P\)
changes the quadratic restitution by

\[
\frac{R_P-R_N}{q+1}
+\ell_N-\ell_P-1.
\tag{5.3}
\]

Using \(x=(T-R)/(q+1)\), this equals

\[
\mu(N)-\mu(P)-1.
\tag{5.4}
\]

Hence the ambient quadratic floor strictly decreases exactly when the
source load exceeds the destination load by at least two, the standard
\(M\)-convex exchange rule.

For the corridor, the exact unit-transfer change is

\[
\operatorname{sgn}(\mu(P)-c_q)
-\operatorname{sgn}(\mu(N)-c_q-1).
\tag{5.5}
\]

Moving one incidence from a source of load at least \(c_q+2\) to a
destination of load at most \(c_q-1\) lowers the corridor by exactly two
before the weight \(1/c_q\).

### Theorem 5.2 -- literal profiles have no unit exchange

For every active \(k\)-row packing and every coordinate \(v\in[n]\),

\[
\sum_{S\ni v}\ell_{\mathcal A,q}(S)=k(m-q).
\tag{5.6}
\]

Consequently, if two literal active profiles differ, no nontrivial
single-target transfer

\[
\ell\longmapsto\ell-e_S+e_T
\tag{5.7}
\]

can remain a literal \(k\)-row profile of the same middle union. Fixed
point margins would force \(\mathbf1_S=\mathbf1_T\), hence \(S=T\).

In the two-row case, delete the union-forced double-owner targets and let
\(\Sigma_q(\mathcal A)\) be the remaining singleton support. Its
cardinality and all point margins are fixed. If there are two distinct
supports, their indicator family fails \(M\)- and \(M^\natural\)-exchange:
the unpaired alternative changes cardinality, while every paired unit
exchange violates point margins. It also fails \(L^\natural\) midpoint
closure, since the intersection and union of two distinct equal-cardinality
binary supports have the wrong cardinalities.

#### Proof

In one wreath, a fixed point belongs to exactly \(m-q\) of the \(n\)
cyclic \((m-q)\)-intervals. Summing over the \(k\) rows proves (5.6).
The transfer (5.7) changes the point-margin vector by
\(\mathbf1_T-\mathbf1_S\), which vanishes only for \(S=T\). For two rows,
the double-owner set is fixed by Section 1, so subtracting it from (5.6)
leaves fixed margins and fixed size for every singleton support. The two
standard \(M^\natural\) alternatives are therefore excluded as stated.
Finally, for distinct equal-size binary vectors \(x,y\),

\[
\left\lfloor\frac{x+y}{2}\right\rfloor=x\wedge y,
\qquad
\left\lceil\frac{x+y}{2}\right\rceil=x\vee y,
\]

and both have the wrong fixed cardinality. \(\square\)

This is the decisive boundary. The objective admits exact ambient exchange
descent, but the genuine decomposition domain is not exchange-closed.
Replacing a literal profile by an ambient load vector would leave the exact
wreath fibre.

Every literal profile does satisfy the pointwise necessary box

\[
\boxed{
\max\{0,A_{q,S}(\mathcal U)-qk\}
\le\ell_{\mathcal A,q}(S)
\le
\min\left\{
k,
\left\lfloor\frac{A_{q,S}(\mathcal U)}{q+1}\right\rfloor
\right\},
}
\tag{5.8}
\]

together with \(\sum_S\ell=kn\). Indeed, if \(\ell\) active rows own
\(S\), then

\[
(q+1)\ell\le A_{q,S}(\mathcal U)\le(q+1)\ell+q(k-\ell)=qk+\ell,
\]

which gives both sides of (5.8). This ambient box/sum domain is
\(M\)-convex, but the inequalities are not sufficient for realization by
wreath rows, and the profiles at different depths are coupled.

---

## 6. Quantitative limits of bounded-row restitution

### Theorem 6.1 -- one bounded-row move is sub-Catalan

Put

\[
M_q
=\left\lfloor
\frac1{q+1}\binom{m+q+1}{q}
\right\rfloor.
\tag{6.1}
\]

Every exact-factor rank-\((m-q)\) load is at most \(M_q\). Therefore every
\(k\)-for-\(k\) same-union move satisfies

\[
\boxed{
|\Delta\mathcal Q_H|
\le
2kn\sum_{q\le H}\frac{M_q-1}{c_q}.
}
\tag{6.2}
\]

For a two-row fixed-union move, active-pair rigidity sharpens this to

\[
\boxed{
|\Delta\mathcal Q_H|
\le
4\sum_{q\le H}
\frac{(n-h_q(\mathcal U))(M_q-1)}{c_q}.
}
\tag{6.2a}
\]

For \(H=\lceil A\sqrt m\rceil\) and fixed \(k\),

\[
|\Delta\mathcal Q_H|
\le
4kn\sum_{q\le H}\frac{\binom mq}{q+1}
=\exp(O_A(\sqrt m\log m))
=o(B).
\tag{6.3}
\]

At depth one,

\[
|\Delta Q_1|
\le
2kn\left(
\left\lfloor\frac{m+2}{2}\right\rfloor-1
\right).
\tag{6.4}
\]

For \(k=2\), the parity-unified form of (6.4) is

\[
|\Delta Q_1|\le4n\left\lfloor\frac m2\right\rfloor.
\]

This also follows from (2.12): on changed coordinates
\(\rho^G_{1,S}=m-2x_1(S)\), and the common \(m\)-term cancels because
\(|P_1|=|N_1|\).

#### Proof

Every lower owner consumes \(q+1\) distinct middle supersets of its target,
giving the cap \(M_q\). A \(k\)-row replacement transports at most \(kn\)
units of lower incidence. One unit transfer between two coordinates whose
loads lie in \([0,M_q]\) changes the quadratic floor by at most
\(2(M_q-1)\), proving (6.2).

For two rows, the common double-owner set has size \(h_q\), so each
singleton support has size \(2(n-h_q)\). Hence at most \(2(n-h_q)\) units
are transported, proving (6.2a).

Since \(c_q\ge\lambda_q/2\) and

\[
\frac1{\lambda_q}\binom{m+q+1}{q}
=\binom mq,
\]

(6.3) follows. The fixed Gaussian-window binomial sum has logarithm
\(O_A(\sqrt m\log m)\), whereas \(\log B=\Theta(m)\).
\(\square\)

Thus no fixed-\(k\) move has a uniform macroscopic capture bound. Many
strict moves could still descend to the target; (6.2) is a speed limit, not
a local-minimum theorem.

### Theorem 6.2 -- bounded-row clipped moves have polynomial displacement

Every \(k\)-for-\(k\) same-union move satisfies

\[
\boxed{
|\Delta\mathcal C_H|
\le
2kn\sum_{q\le H}\frac1{c_q}
\le 2knH.
}
\tag{6.5}
\]

For a two-row fixed-union move, the sharper bound is

\[
|\Delta\mathcal C_H|
\le
4\sum_{q\le H}\frac{n-h_q(\mathcal U)}{c_q}
\le4nH.
\tag{6.6}
\]

#### Proof

The scalar corridor \(\chi_c\) is one-Lipschitz. At every depth the two
active profiles have total mass \(kn\), so their \(\ell^1\)-distance is at
most \(2kn\). This proves (6.5). In the two-row case, the double-owner
targets are fixed, each singleton support has size \(2(n-h_q)\), and hence
the symmetric difference has size at most \(4(n-h_q)\), proving (6.6).
\(\square\)

Two scale consequences are exact. A \(k\)-row move which lowers \(Q_1\)
by at least \(\varepsilon W\) must have

\[
k\ge
\frac{\varepsilon B}{2(M_1-1)}
=(\varepsilon+o(1))\frac Bm.
\tag{6.7}
\]

If \(\mathcal C_H(F)\ge\varepsilon W\), a \(k\)-row move lowering the
corridor by at least an \(\eta\)-fraction must have

\[
k\ge\frac{\eta\varepsilon B}{2H}
=\Omega_{\varepsilon,\eta}\!\left(\frac B{\sqrt m}\right).
\tag{6.8}
\]

Thus no fixed-row neighborhood can furnish a one-step proportional
restitution theorem. This does not preclude a long sequence of strict
fixed-row moves, which is exactly what the condition in Section 7 asks for.

### Theorem 6.3 -- almost every bounded row union is rigid

For an exact factor \(F\), form the row-conflict graph: two rows are adjacent
when some middle window of one is Johnson-adjacent to a middle window of the
other. Its maximum degree is at most

\[
D_m=n\bigl(m(m+1)-2\bigr).
\tag{6.9}
\]

It has an independent set of size at least

\[
\frac{B}{D_m+1}.
\tag{6.10}
\]

The middle union of any rows in this independent set has a unique wreath
decomposition.

#### Proof

One row has \(n\) middle windows. Each has \(m(m+1)\) Johnson neighbors,
of which exactly two are its cyclic neighbors in the same row, and every
other neighboring middle set has a unique owner in \(F\). This proves the
degree bound and the greedy independent-set estimate. Equivalently, the
number of cross-row Johnson edges is exactly

\[
W\left(\frac{m(m+1)}2-1\right)=\frac{BD_m}{2}.
\]

The middle support of one wreath induces exactly a cycle \(C_n\) in the
Johnson graph: two cyclic middle windows are Johnson-adjacent exactly when
their starting positions are consecutive. Indeed, if their cyclic starting
positions have distance \(d\in\{1,\ldots,m\}\), their intersection has
size \(m-d\), and hence has size \(m-1\) exactly for \(d=1\).
Independence removes all cross edges,
so the graph induced by the selected middle union is a disjoint union of
\(C_n\)'s.

The middle support of any alternative wreath is a connected \(n\)-vertex
Johnson cycle. It must therefore equal one whole component. That component
determines its unoriented cyclic order: after choosing one orientation of
the window cycle, the unique element added at each Johnson step lists the
underlying point cycle, and reversing the window cycle reverses that order.
Thus every row is one of the original rows. \(\square\)

More generally, for \(2\le k\le B\), the fraction of nonrigid \(k\)-row
subsets of \(F\) is at most

\[
\boxed{
\frac{D_mk(k-1)}{2(B-1)}.
}
\tag{6.11}
\]

Indeed, a nonrigid union must contain a conflict edge; count a conflict
edge and then the remaining \(k-2\) rows. For every fixed \(k\), (6.11)
tends to zero superpolynomially. Random bounded-\(k\) averaging therefore
cannot prove a macro restitution theorem. An adaptive argument must target
the sparse conflict tuples.

There is a sharper primitive-triple count. If three old rows support one
connected three-by-three ownership component, their induced conflict graph
must be connected. Otherwise the induced Johnson graph of their middle
union separates by conflict components; every new wreath support, being
connected, lies in one part, and the ownership overlay also separates.
Therefore the number of possible old supports of primitive three-row trades
is at most

\[
\boxed{
\sum_{R\in F}\binom{d_F(R)}2
\le B\binom{D_m}{2}.
}
\tag{6.12}
\]

This is an exponentially tiny fraction of all row triples. Connectedness
is only necessary: an arbitrary Johnson cycle need not be a sliding-window
wreath, so (6.12) is not an existence theorem.

Every pair of rows colliding at depth one is such a conflict pair: their
two disjoint color-\(S\) Johnson edges have cross-adjacent endpoints. Hence
Theorem 6.3 does not rule out targeted collision repair. But once such a
pair is fixed, at most \(2D_m\) third rows are even conflict-adjacent to
the pair, a necessary condition for a primitive three-row refactor. Thus
the abundance of depth-one zero-spill buffer rows does not furnish a legal
three-for-three move. Indeed, only the \(m+2\) middle supersets of a fixed
\((m-1)\)-set \(S\) can have owners meeting \(S\), so at least
\(B-(m+2)\) factor rows have \(a_{1,S}=0\). The required buffer must also
lie in the polynomial list of at most \(2D_m\) conflict-neighbors, and even
then wreath realizability remains unproved.

This sparsity gives no likelihood-ratio bound. Every active pair in the
four-middle likelihood event is already cross-Johnson-adjacent, so the
likelihood conditions on the exceptional conflict locus. Multiplying its
global row-pair density by a completion probability would double-count the
conditioning.

---

## 7. A concrete constant-one exchange target

Three rows are the first bounded size at which active collision
multiplicity is not frozen by two-owner rigidity. This motivates the
following non-Graver statement.

> **Three-row clipped restitution exchange
> \((\mathrm{TCRE}_A)\) — UNPROVED.**
> For every fixed \(A>0\), there are \(C_A<\infty\) and \(m_0(A)\) such
> that, whenever \(m\ge m_0(A)\) and an exact factor \(F\) satisfies
> \[
> \mathcal C_H(F)>C_AHB,
> \]
> some three selected rows form a middle union \(\mathcal U\) having an
> alternate literal three-row decomposition \(\mathcal A'\) with
> \[
> \operatorname{Rest}_C(\mathcal A')
> >
> \operatorname{Rest}_C(\mathcal A).
> \]
> Here the restitution scores are those of (4.10), evaluated with the
> untouched completion \(G=F\setminus\mathcal A\) and the common union
> \(\mathcal U\).

### Theorem 7.1 -- \(\mathrm{TCRE}_A\) implies constant one

If \(\mathrm{TCRE}_A\) holds for every fixed \(A>0\), then

\[
\boxed{\nu(k)\le(1+o(1))W(k).}
\tag{7.1}
\]

#### Proof

By Theorem 4.3, the replacement is a strict corridor-decreasing move
between literal exact factors. Iterate while
\(\mathcal C_H>C_AHB\). The exact fibre is finite, so strict descent
terminates at a factor with

\[
\mathcal C_H\le C_AHB.
\]

Since

\[
\frac{HB}{W}=\frac Hn=O_A(m^{-1/2}),
\]

this is \(o(W)\) on every fixed Gaussian window. The audited corridor-to-
overload comparison and frozen diagonalization then give (7.1).
\(\square\)

There is an analogous, stronger quadratic condition obtained by replacing
\(\mathcal C_H\), \(\operatorname{Rest}_C\) with
\(\mathcal Q_H\), \(\operatorname{Rest}_Q\). Since

\[
\mathcal C_H\le\frac12\mathcal Q_H
\]

by (3.10), it also implies constant one.

The theorem is genuinely bounded-row and does not invoke the full Graver
basis. Its hypothesis is not proved. Theorem 6.3 shows why it cannot be
replaced by a claim about every or a random three-row union. One must target
specific conflict triples carrying useful clipped restitution.

At depth one, the first collision-changing three-row local pattern is also
forced. If an active load changes from two owners to one, equality of the
middle union makes the active containment equal four: the two-owner side
has zero active spill, while the one-owner side has two units of active
spill. Indeed the two-owner side has containment at least four, whereas the
one-owner side has containment at most \(2+1+1=4\); equality of the middle
union forces both bounds to equality. This is exactly the literal buffer
pattern which a proof of
\(\mathrm{TCRE}_A\) must complete globally.

---

## 8. SCC/GCC scope and final boundary

The restitution maximizer is constructive for existence descent, but it
does not by itself prove SCC or GCC.

For the whole fibre and a fixed middle union \(\mathcal U\), factors with
a distinguished active packing factor exactly as

\[
\mathcal P_k(\mathcal U)
\times
\{\text{packings of the middle complement}\}.
\tag{8.1}
\]

Thus the active decomposition and untouched completion are conditionally
independent under the uniform distinguished-incidence law. A fair or
bijective rearrangement of decompositions has zero conditional trace.
Sending every decomposition to a restitution maximizer is many-to-one and
is not a completion-count injection. The remaining GCC term is the
deterministic alignment of the decomposition barycenter with the untouched
restitution barycenter; no upper bound at the \(O_A(HB)\) scale is proved.

There is an exact quadratic trace identity behind this obstruction. Given
\(\mathcal U\), let \(\mathcal A\) be uniform on
\(\mathcal P_k(\mathcal U)\), let \(G\) be uniform on the complement
packings, and write \(\ell_q,u_q\) for their load vectors and bars for
conditional means. Then independence and the monic quadratic leading term
of \(\phi_{c_q}\) give

\[
\boxed{
\begin{aligned}
\mathbb E[Q_q(G\mathbin{\dot\cup}\mathcal A)\mid\mathcal U]
={}&\sum_S\phi_{c_q}(\bar u_q(S)+\bar\ell_q(S))\\
&+\mathbb E\|u_q-\bar u_q\|_2^2
+\mathbb E\|\ell_q-\bar\ell_q\|_2^2.
\end{aligned}
}
\tag{8.2}
\]

The restitution argmax controls a minimum over decompositions; GCC asks for
this uniform mean, which pays both nonnegative variance traces. Under a
class-restricted law the Cartesian independence can fail and a covariance
term can appear, while the switch need not stay inside the class. This is
the exact fair-cell boundary, not a discarded error term.

The objective distinction is essential. The four-middle likelihood
identity and SCC/GCC are statements about \(\mathcal Q_H\). The clipped
functional \(\mathcal C_H\) is sufficient for the constant-one overload
route, but (3.10) gives only

\[
\mathcal Q_H=2\mathcal C_H+\mathcal T_H,
\]

with a nonnegative, potentially large tail. Thus clipped restitution alone
cannot be inserted into the likelihood-ratio argument without a new
anti-concentration or maximum-load estimate.

For SCC, a same-union redecomposition need not remain in the original heat
class, so even the Cartesian factorization need not be class-restricted.
When a two-row redecomposition is one genuine fair heat component, its
oriented cross-overlap term averages to zero between the two shores; any
corner improvement is paid back in the stationary cell mean.

The exact proved boundary is therefore:

1. Y6 active-pair rigidity, depth-one matching, and likelihood constants
   are valid.
2. The untouched-row term is exactly spill restitution, with the pure
   depth-one formula (2.12).
3. \(\operatorname{Rest}_Q\) and \(\operatorname{Rest}_C\) give literal
   steepest fixed-union moves and exact gain formulas.
4. Both objectives have complete ambient \(M\)-exchange convexity.
5. The exact comparator-induced neighborhood consists of whole balanced
   ownership components; arbitrary alternating cycles do not lift.
6. Literal wreath profiles are not exchange-closed; random bounded-row
   unions are overwhelmingly rigid, and fixed-row moves have only
   polynomial clipped displacement.
7. No exchange inequality forcing a useful three-row or bounded-row move
   from every high-energy factor is proved.
8. Consequently SCC, GCC, MWB, and constant one remain unproved.

The constructive remaining gate is no longer an uncontrolled
cross-overlap estimate. It is the literal lifting problem:

\[
\boxed{
\text{Does every high-corridor exact factor contain a conflict triple
whose alternate middle-union decomposition increases clipped restitution?}
}
\]

That bounded-row theorem would prove constant one by Theorem 7.1.
