# Product-phase rigidity for globally hash-twisted MSW collars

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

This note isolates a statewise obstruction to the most direct global
filling-dependent MSW braid.

Let a recursive child live on a coordinate block \(J\), and let its
exterior context live on a disjoint block \(E\). Suppose that at every
child phase \(t\) the physical middle states are still the complete
product

\[
 \{\,O_c\mathbin{\dot\cup}X_t(u):c\in\mathcal C,
       u\in\mathcal D_r\,\},
\]

where the \(O_c\)'s all have one fixed size and the \(X_t(u)\)'s form the
\(t\)-th Chung--Feller layer on \(J\). The row interleaving may depend on
the entire filling and context, with no bound on its hash alphabet.

The main theorem says that every Johnson-legal phasewise exact
interleaving preserves \(c\) along every row. After normalizing the first
phase, the factor is a disjoint sum of independent child factors in fixed
exterior contexts. In particular, no stationary exterior collar can
depend on the filling. This uses lower ownership and adjacency alone;
the upper ledger cannot repair the failure.

Thus a genuine global braid must leave this product-phase class. At some
cut it must stall or change the local rank/phase and use a cross-block
exchange. For a length-\(r\) geodesic with boundary braid

\[
 (c,u)\longmapsto(\rho(c,u),\tau(c,u)),
\]

the exact statewise equations are

\[
 (\rho,\tau)\in\operatorname {Sym}(\mathcal C\times\mathcal D_r),
\qquad
 d_J(O_c,O_{\rho(c,u)})
   =|P_u\setminus P_{\tau(c,u)}|.                 \tag{0.1}
\]

The swallowed local target is

\[
 (O_c\cap O_{\rho(c,u)})
       \mathbin{\dot\cup}(P_u\setminus P_{\tau(c,u)}). \tag{0.2}
\]

Consequently a nontrivial collar braid must pay at least the distance in
(0.1) in physical exterior-touching Johnson transitions. A stationary
filling-dependent collar has zero motion inside the excursion and must be
encoded by the exterior chronology before it and logically decoded on
the physically complementary shore after it.

There is also a sharp correction to the tempting
install--hold--erase picture. A complementary Johnson geodesic can never
leave an exterior collar and later return to the same physical collar:
coordinates common to two states on a geodesic persist between them.
Logical zero monodromy must instead mean that a left exterior port
\(A_c\) and its physically complementary right port \(E\setminus A_c\)
carry the same *label*. An intermediate collar \(Q\) is then merely a cut
in the chronology, and

\[
 d_J(A_c,Q)+d_J(Q,E\setminus A_c)=|A_c|             \tag{0.3}
\]

for every middle collar \(Q\). Thus there is no metric distance
obstruction to a global cut address.

Indeed, at the central child phases, exact lower ownership is equivalent
to one Latin condition:

\[
             c\longmapsto\gamma(c,u)\quad
             \hbox{is a permutation for every filling }u.      \tag{0.4}
\]

If the context labels form a group, the shear
\(\gamma(c,u)=c+h(u)\) satisfies (0.4). If \(h\) is balanced on a regular
orbit of size \(L\), then for every fixed input context its swallowed
collar fibre is at most

\[
                         \left\lceil{C_r\over L}\right\rceil.   \tag{0.5}
\]

Consequently there is no statewise middle-owner or metric obstruction to
a large global hash. The exact missing object is a literal exterior
module library whose prefix and suffix realize these seam permutations
while sharing the full phase-resolved \(X/Y\) palettes. Section 6 gives
the precise conditional composition theorem. It does not assert that a
large such library exists.

## 1. The context--filling Latin system

Let \(E,J\) be disjoint. Let

\[
  c\longmapsto O_c\in\binom Ee,\qquad c\in\mathcal C, \tag{1.1}
\]

be injective. Let \(\mathcal D\) be a finite filling set and, for
\(0\le t\le r\), let

\[
  \xi_t:\mathcal D\longrightarrow\mathcal L_t
       \subseteq\binom Jr                                  \tag{1.2}
\]

be bijective. Put

\[
 V_t(c,u)=O_c\mathbin{\dot\cup}\xi_t(u).                    \tag{1.3}
\]

A completely general context--filling interleaving is a sequence of
maps

\[
 F_t=(\alpha_t,\beta_t):
       \mathcal C\times\mathcal D\longrightarrow
       \mathcal C\times\mathcal D,                           \tag{1.4}
\]

and its row states are

\[
                 Z_t(z)=V_t(F_tz).                            \tag{1.5}
\]

The functions in (1.4) may depend on the full context and full filling;
there is no locality or bounded-alphabet assumption.

### Proposition 1.1 (exact statewise ledger)

For a prescribed product phase family, lower ownership at phase \(t\) is
equivalent to

\[
                 F_t\in\operatorname {Sym}
                    (\mathcal C\times\mathcal D).             \tag{1.6}
\]

Johnson legality is exactly

\[
                 d_J(Z_t(z),Z_{t+1}(z))=1                     \tag{1.7}
\]

for every \(z,t\). If \(\mathcal Y\) is the prescribed upper-token
palette of the slab, exact upper ownership is exactly the multiset
identity

\[
 \mathop{\dot\bigcup}_{t,z}
   \{Z_t(z)\cup Z_{t+1}(z)\}=\mathcal Y.                       \tag{1.8}
\]

If the slab closes with the same rooted local ports, its relative
permutations

\[
                 S_t=F_{t+1}F_t^{-1}                           \tag{1.9}
\]

also obey the zero-monodromy equation

\[
                 S_{r-1}\cdots S_1S_0=F_rF_0^{-1}=1.          \tag{1.10}
\]

#### Proof

The map \(V_t\) is injective, and its image is the complete prescribed
phase family. Hence the states in (1.5) exhaust that family once exactly
when \(F_t\) is a permutation. Equation (1.7) is the definition of a
Johnson edge. Its upper token is the union of its endpoints, so (1.8) is
precisely the upper ownership ledger. Equation (1.10) telescopes. \(\square\)

The boundary equations (1.6)--(1.10), including (1.8), are simultaneous.
A Latin hash at every lower phase is not by itself an exact factor.

## 2. Product-phase rigidity

The following is the decisive statewise result.

### Theorem 2.1 (no exterior braid inside fixed-rank product phases)

Assume

\[
                 \mathcal L_t\cap\mathcal L_{t+1}=\varnothing
                 \qquad(0\le t<r).                             \tag{2.1}
\]

Let every \(F_t\) in (1.4) be a permutation, and assume every transition
in (1.7) is Johnson-legal. Then

\[
                 \boxed{\alpha_{t+1}(z)=\alpha_t(z)}           \tag{2.2}
\]

for every row \(z\) and every \(t\). After relabelling rows by \(F_0\),
one has

\[
       F_0=1,\qquad
       F_t(c,u)=(c,\beta_{t,c}(u)),\qquad
       \beta_{t,c}\in\operatorname {Sym}(\mathcal D).         \tag{2.3}
\]

Thus the factor is a disjoint union over fixed exterior contexts \(c\).
If the upper palette is the corresponding product palette, (1.8) holds
if and only if the local upper ledger holds separately in every context.

#### Proof

For equal-size subsets on disjoint coordinate blocks, Johnson distance
is additive. Hence

\[
\begin{aligned}
 d_J(Z_t(z),Z_{t+1}(z))
 &=d_J(O_{\alpha_t(z)},O_{\alpha_{t+1}(z)})\\
 &\quad+d_J(\xi_t(\beta_t(z)),
                   \xi_{t+1}(\beta_{t+1}(z))).                 \tag{2.4}
\end{aligned}
\]

The two local sets in the second term are unequal by (2.1), so that term
is at least one. The left side is one by Johnson legality. Therefore the
local term is exactly one and the exterior term is zero. Injectivity in
(1.1) proves (2.2).

Replace the row label \(z\) by \(F_0z\). This makes \(F_0=1\). Equation
(2.2) then gives \(\alpha_t(c,u)=c\) for all \(t\). Since \(F_t\) is a
permutation and preserves its first coordinate, its restriction to each
fibre \(\{c\}\times\mathcal D\) is a permutation, proving (2.3).

Every resulting upper token has the form

\[
 O_c\mathbin{\dot\cup}
 \bigl(\xi_t(\beta_{t,c}u)
       \cup\xi_{t+1}(\beta_{t+1,c}u)\bigr).                    \tag{2.5}
\]

Restriction to \(E\) recovers \(O_c\). Hence upper tokens belonging to
different contexts cannot coincide, and the global ledger factors into
the local ledgers. \(\square\)

### Corollary 2.2 (Chung--Feller hash obstruction)

Take \(\mathcal D=\mathcal D_r\) and let the \(\mathcal L_t\)'s be the
Chung--Feller flaw layers. They are pairwise disjoint. Therefore any
phase-respecting recursive MSW interleaving of the form (1.5), even one
whose \(F_t\)'s depend on a nonlocal full-word hash, preserves the
exterior context along every child row.

If the local endpoints are complementary and use the same rooted port,
then after the normalization in (2.3),

\[
                        \beta_{r,c}=\beta_{0,c}=1               \tag{2.6}
\]

for every context \(c\). Each context contains an independent exact
local factor; there is no cross-context collar braid.

#### Proof

Only (2.1) needs checking, and distinct flaw layers are disjoint. Theorem
2.1 applies. At the endpoints the canonical identity is
\(\xi_r(u)=J\setminus\xi_0(u)\). Complementary closure of the row and
injectivity of \(\xi_0\) give (2.6). \(\square\)

This rules out more than fixed-carrier hashes. It rules out every
filling-dependent context permutation while the construction retains the
synchronized fixed-rank product phase decomposition. An escape must make
the local projections at some physical cut fail the hypothesis of
(2.4): it must stall a local phase, change local rank, or perform a
cross-block exchange.

## 3. The boundary permutation of a genuine braid

We now drop the product-phase hypothesis in the interior and retain only
the two boundary products.

Let \(|J|=2r\), let

\[
                 u\longmapsto P_u\in\binom Jr                  \tag{3.1}
\]

be injective, and retain the exterior family (1.1). Normalize the left
boundary of a length-\(r\) segment as

\[
                 Z_0(c,u)=O_c\mathbin{\dot\cup}P_u.             \tag{3.2}
\]

Write its right boundary as

\[
 Z_r(c,u)=O_{\rho(c,u)}\mathbin{\dot\cup}
                    (J\setminus P_{\tau(c,u)}).                 \tag{3.3}
\]

### Theorem 3.1 (distance-balanced boundary Latin cocycle)

If both boundary product families are owned once and every displayed
segment is a Johnson geodesic of length \(r\), then

\[
 \Psi=(\rho,\tau)\in
      \operatorname {Sym}(\mathcal C\times\mathcal D_r),       \tag{3.4}
\]

and, pointwise,

\[
 \boxed{
 d_J(O_c,O_{\rho(c,u)})
       =|P_u\setminus P_{\tau(c,u)}|.}                          \tag{3.5}
\]

The full intersection of the segment is

\[
 \boxed{
 \bigcap_{t=0}^{r}Z_t(c,u)
   =(O_c\cap O_{\rho(c,u)})
       \mathbin{\dot\cup}(P_u\setminus P_{\tau(c,u)}).}        \tag{3.6}
\]

If the common value in (3.5) is \(d\), at least \(d\) of the \(r\)
physical Johnson transitions touch an exterior coordinate.

#### Proof

Right boundary ownership and injectivity of the two product
coordinatizations give (3.4). The endpoint distance is

\[
\begin{aligned}
 d_J(Z_0,Z_r)
 &=|O_c\setminus O_{\rho(c,u)}|
   +|P_u\cap P_{\tau(c,u)}|\\
 &=d_J(O_c,O_{\rho(c,u)})
   +r-|P_u\setminus P_{\tau(c,u)}|.                            \tag{3.7}
\end{aligned}
\]

It equals the geodesic length \(r\), proving (3.5).

Every coordinate common to the endpoints of a geodesic stays present
throughout: deleting it and later reinserting it would use two moves
which do not reduce endpoint distance. Conversely every element of the
full intersection belongs to both endpoints. Hence the full intersection
is the endpoint intersection, which is (3.6).

Finally, each element of \(O_c\setminus O_{\rho(c,u)}\) must be deleted
in a distinct Johnson transition. There are \(d\) such elements. \(\square\)

### Corollary 3.2 (stationary collars are installed outside)

If \(O_{\rho(c,u)}=O_c\), then \(\tau(c,u)=u\), and no transition inside
the length-\(r\) segment touches an exterior coordinate.

More generally, a proposed boundary shear

\[
                       \rho(c,u)=c+h(u),\qquad \tau(c,u)=u      \tag{3.8}
\]

in any context group is impossible unless \(h(u)=0\) at every row for
which \(c\mapsto O_c\) is injective.

#### Proof

Equation (3.5) gives \(P_u=P_{\tau(c,u)}\), hence \(\tau(c,u)=u\).
Every exterior coordinate in the common endpoint collar belongs to both
endpoints and therefore persists throughout the geodesic. Likewise, every
exterior coordinate outside the common collar is absent from both
endpoints and cannot be inserted and later deleted on a geodesic.
Therefore the exterior projection is constant throughout.
Equation (3.8) is the same statement in group notation. \(\square\)

Thus a stationary collar \(O(c,u)\) can distinguish fillings, but its
information must already be present when the child excursion begins and
must survive unchanged until that excursion ends. Logical zero monodromy
must be implemented on the physically complementary exterior shore; a
literal return to the same collar is impossible, as shown next.

Equations (3.4)--(3.6) are necessary, not sufficient. A positive braid
must also extend \(\Psi\) to intermediate phase permutations satisfying
all lower owner equations and the complete upper-token identity (1.8).

## 4. Logical zero monodromy is not physical return

A tempting picture installs a collar \(Q\), holds it during the child,
and then returns to the same physical exterior set. Geodesicity rules this
out.

### Lemma 4.1 (no physical collar return)

Let \(Z_0,Z_1,\ldots,Z_\ell\) be a Johnson geodesic and let \(E\) be any
coordinate block. If

\[
                         Z_s\cap E=Z_t\cap E=O                 \tag{4.1}
\]

for \(s<t\), then

\[
                         Z_j\cap E=O
                         \qquad(s\le j\le t).                   \tag{4.2}
\]

In particular, a nontrivial exterior address cannot be installed from
\(O\) and later erased back to \(O\) along one complementary geodesic.

#### Proof

Every coordinate present at both endpoints \(Z_s,Z_t\) of a geodesic
subpath stays present throughout that subpath. Deleting and reinserting it
would use two moves which do not reduce endpoint distance. Similarly, a
coordinate absent from both endpoints cannot be inserted and later
deleted. Apply these two statements to every coordinate of \(E\). \(\square\)

The correct meaning of zero monodromy is logical. Let \(|E|=2e\), let
\(A_c\in\binom Ee\) be a left exterior port, and let the right port with
the same context label be its physical complement \(E\setminus A_c\).
Then every \(Q\in\binom Ee\) obeys

\[
 \boxed{
 d_J(A_c,Q)+d_J(Q,E\setminus A_c)=e.}                         \tag{4.3}
\]

Indeed, if \(a=|A_c\cap Q|\), the two summands are \(e-a\) and \(a\).
Consequently every middle collar \(Q\) lies on some exterior geodesic
from \(A_c\) to its complement. A filling-dependent collar can be encoded
by deciding which exterior exchanges occur before the child and which
occur after it, with no extra metric length.

Thus Theorem 3.1 obstructs motion *during* the stationary child but gives
no distance obstruction to a chronology cut before it. Exact ownership of
those chronology cuts is the real gate.

## 5. The exact central Latin shear

Let

\[
               c\longmapsto Q_c\in\binom Ee,\qquad c\in\mathcal C,
                                                                    \tag{5.1}
\]

be injective. Let

\[
 X_0(u),X_1(u),\ldots,X_r(u),\qquad u\in\mathcal D_r,             \tag{5.2}
\]

be an exact local Chung--Feller factor on \(J\), with
\(X_0(u)=P_u\), \(X_r(u)=J\setminus P_u\). Thus each local phase is
owned once and

\[
 (t,u)\longmapsto U_t(u):=X_t(u)\cup X_{t+1}(u)                  \tag{5.3}
\]

is a bijection onto the local upper palette.

Let

\[
                    \gamma:\mathcal C\times\mathcal D_r
                              \longrightarrow\mathcal C          \tag{5.4}
\]

and put

\[
                    Z_t(c,u)=Q_{\gamma(c,u)}
                                  \mathbin{\dot\cup}X_t(u).       \tag{5.5}
\]

### Theorem 5.1 (central Latin shear criterion)

The states (5.5) own every central lower product state exactly once, at
every phase, if and only if

\[
 \boxed{\gamma_u:c\longmapsto\gamma(c,u)
        \text{ is a permutation of }\mathcal C
        \text{ for every }u.}                                   \tag{5.6}
\]

Under (5.6), all central upper product tokens are also owned exactly once.
Moreover, every window swallowing the full local child has target

\[
                         Q_{\gamma(c,u)},                        \tag{5.7}
\]

and, for a fixed input context \(c\), its fibre at \(Q_a\) is exactly

\[
                         |\{u:\gamma(c,u)=a\}|.                  \tag{5.8}
\]

#### Proof

At phase \(t\), the local state \(X_t(u)\) recovers \(u\), because
\(u\mapsto X_t(u)\) is injective. Therefore (5.5) owns the product phase
once precisely when, for every fixed \(u\), its exterior labels run
through \(\mathcal C\) once. This is (5.6).

For upper tokens, (5.3) recovers the pair \((t,u)\). At that fixed pair,
(5.6) makes \(c\mapsto Q_{\gamma(c,u)}\) a bijection. Hence

\[
 (c,t,u)\longmapsto
 Q_{\gamma(c,u)}\mathbin{\dot\cup}U_t(u)                         \tag{5.9}
\]

is a bijection onto the product of the exterior seam palette and the
local upper palette.

The child is a geodesic with the same exterior collar at both endpoints.
Its full intersection is therefore that collar, proving (5.7), and
(5.8) is immediate. \(\square\)

### Corollary 5.2 (group shear has balanced statewise fibres)

Suppose \(\mathcal C=G\) is a finite group acting regularly on its own
labels. For an arbitrary hash \(h:\mathcal D_r\to G\), put

\[
                         \gamma(c,u)=c\,h(u).                    \tag{5.10}
\]

Then (5.6) holds. If

\[
                         |h^{-1}(g)|
                           \le\left\lceil{C_r\over |G|}\right\rceil
                           \qquad(g\in G),                       \tag{5.11}
\]

then every fixed-context target fibre in (5.8) is at most

\[
                         \left\lceil{C_r\over |G|}\right\rceil. \tag{5.12}
\]

#### Proof

Right multiplication by \(h(u)\) is a permutation for every \(u\).
For fixed \(c\), the equation \(ch(u)=a\) is equivalent to
\(h(u)=c^{-1}a\), so (5.11) gives (5.12). \(\square\)

Thus an orbit of size

\[
                         |G|\ge C_r/b                            \tag{5.13}
\]

is enough to make the central swallowed fibre at most \(b\), when \(b\)
is integral. This is a
literal central \(X/Y\) statement. It proves that exact middle ownership
and the desired one-sided fibre bound are mutually compatible; the
difficulty lies in reaching the seam by an exact exterior factor.

Orbit size alone does not imply (5.12) for a nonregular action. One needs
a hash balanced on the actual image multiset \(u\mapsto\rho_{h(u)}c\)
simultaneously for all relevant \(c\).

## 6. Exact composition with an exterior seam-module library

The following theorem states the positive construction gate without
hiding any ownership condition.

Let \(|E|=2e\). For each option \(a\in\mathcal A\), suppose there is a
family of exterior paths

\[
 A^a_0(c),A^a_1(c),\ldots,A^a_e(c),
 \qquad c\in\mathcal C,                                      \tag{6.1}
\]

with these properties.

1. Every path in (6.1) is a Johnson geodesic and

   \[
   A^a_0(c)=A_c,\qquad A^a_e(c)=E\setminus A_c,                \tag{6.2}
   \]

   independently of \(a\).

2. For every exterior phase \(j\), the map
   \(c\mapsto A^a_j(c)\) bijects \(\mathcal C\) onto a physical phase
   palette \(\mathcal A_j\) independent of \(a\). The palettes
   \(\mathcal A_j\) are disjoint.

3. For every phase \(j\) and every \(a\), the map

   \[
   c\longmapsto A^a_j(c)\cup A^a_{j+1}(c)                     \tag{6.3}
   \]

   is a bijection onto one physical upper phase palette
   \(\mathcal B_j\), independent of \(a\). The palettes
   \(\mathcal B_j\) are disjoint.

4. At a fixed seam phase \(s\),

   \[
                         A^a_s(c)=Q_{\rho_a(c)},                \tag{6.4}
   \]

   where \(\rho_a\in\operatorname {Sym}(\mathcal C)\).

Call this a **port-fixed, palette-uniform exterior seam library**.
Conditions 2 and 3 are the complete exterior \(X/Y\) ledger; equality of
only the root and endpoint ports is insufficient.

Choose an arbitrary hash \(h:\mathcal D_r\to\mathcal A\). For every
\((c,u)\), form the concatenated row

\[
\begin{array}{ll}
 A^{h(u)}_0(c)\dot\cup P_u,\ldots,
 A^{h(u)}_s(c)\dot\cup P_u, &\text{(exterior prefix)},\\[2mm]
 Q_{\rho_{h(u)}(c)}\dot\cup X_0(u),\ldots,
 Q_{\rho_{h(u)}(c)}\dot\cup X_r(u), &\text{(local child)},\\[2mm]
 A^{h(u)}_s(c)\dot\cup(J\setminus P_u),\ldots,
 A^{h(u)}_e(c)\dot\cup(J\setminus P_u). &\text{(exterior suffix)}
\end{array}                                                     \tag{6.5}
\]

The repeated splice states in (6.5) are identified, not written twice in
the physical word.

### Theorem 6.1 (filling-dependent seam composition)

The rows (6.5) are an integral literal exact factor of the corresponding
product cylinder. They have complementary endpoints and are geodesics of
length \(e+r\). Their central swallowed target is

\[
                         Q_{\rho_{h(u)}(c)}.                     \tag{6.6}
\]

Consequently, if the permutations \(\rho_a\) and the hash \(h\) satisfy

\[
 \max_{c,d}|\{u:\rho_{h(u)}(c)=d\}|\le b,                        \tag{6.7}
\]

then the hereditary child fibre is at most \(b\), statewise.

#### Proof

Every prefix and suffix transition changes one exterior coordinate pair;
every central transition changes one local coordinate pair. The exterior
path changes every required exterior coordinate once, and the child
changes every required local coordinate once. Thus (6.5) is a Johnson
geodesic from

\[
                         A_c\dot\cup P_u
 \quad\hbox{to}\quad
                         (E\setminus A_c)\dot\cup(J\setminus P_u),
                                                                    \tag{6.8}
\]

which are complementary.

Fix \(u\). Its option \(h(u)\) is fixed across all \(c\). Conditions 2
and 3 therefore make the prefix lower and upper exterior palettes exact
over \(c\); adjoining the injective tag \(P_u\) preserves exactness.
Different \(u\)'s have different local tags. The suffix proof is
identical with the complementary tags \(J\setminus P_u\).

At the central phases, \(c\mapsto\rho_{h(u)}(c)\) is a permutation.
Theorem 5.1 gives both lower and upper ownership. Prefix, central, and
suffix upper tokens cannot collide across regions: their restrictions to
\(J\) have sizes \(r\), \(r+1\), and \(r\), respectively, while the two
size-\(r\) endpoint tag families \(P_u\) and \(J\setminus P_u\) are the
disjoint initial and terminal Chung--Feller layers. The same phase
separation handles lower states, with the two splice states identified.
Hence the complete \(X/Y\) ledger is exact.

Equation (6.6) follows from the full-child intersection, and (6.7) is
exactly its fibre bound. \(\square\)

The theorem is stable under arbitrary nonlocal hashes: the hash need not
be computable from a bounded collar, because a complete exterior module
is selected for each full local filling and all of its context rows are
used.

## 7. Proved boundary for coefficient one

The preceding results give a clean dichotomy.

### Rigorously closed

Any global hash which merely permutes context/filling rows while retaining
the synchronized fixed-rank product Chung--Feller layers is contextwise
and cannot move an exterior collar. This includes arbitrary full-word
hashes and unbounded hash alphabets. Theorem 2.1 uses only statewise
adjacency and exact lower ownership.

A proposed nontrivial boundary shear with unchanged local port is also
impossible inside the child, by (3.5). Physical install-and-return to the
same collar is impossible by Lemma 4.1.

### Rigorously feasible at the central ledger

A filling-dependent regular Latin shear (5.10) simultaneously preserves
every central \(X/Y\) owner and reduces the swallowed fibre to
\(\lceil C_r/|G|\rceil\). There is no statewise middle-owner or geodesic
metric invariant forcing a Catalan fibre once exterior chronology cuts are
allowed.

### Exact remaining gate

One must construct, at growing scale, a port-fixed palette-uniform
exterior seam library satisfying (6.1)--(6.4), together with a common hash
meeting (6.7) for

\[
                         b=2m+1,\qquad
                         r\le A\sqrt m.                          \tag{7.1}
\]

For the pure group model this asks for a regular seam orbit of size at
least \(C_r/(2m+1)\). A bounded local router library or a disjoint family
of two-row rectangles does not supply this: a fixed context lies in only
boundedly many images unless the routers compose through a
switch-stable, zero-holonomy exterior atlas.

Theorem 6.1 is conditional on that atlas. It does not prove that serial
alternating \(C_6\) or \(C_8\) routers retain the common phase-resolved
palettes, nor that their seam permutations have a growing regular orbit.
Those are exactly the two claims an actual global braid construction must
establish. No universal obstruction to such an atlas is proved here.
