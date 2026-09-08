# The controlled-leave residual host has a Catalan coordinate-cocycle
# obstruction before topology

Date: 2026-08-01  
Lane: mixed-head controlled leave / induced odd owner-slot forest  
Status: exact solver-free no-go for the proposed balanced residual matching,
plus an exact Catalan-scale matching-deficiency lower bound.  The local
degree/codegree theorem remains valid.

## 0. Outcome

The controlled packet bank in
`MATH_THEOREM_CATALAN_CONTROLLED_LEAVE_PACKET_BANK_AND_BALANCED_RESIDUAL_FOREST_GATE_20260801.md`
does leave an asymptotically regular induced owner-slot host.  Its exact
residual counts are

\[
 |\mathcal U'|=U-2C=W-3C,
 \qquad |\mathcal L'|=W-2C,
 \qquad |\mathcal S'|=2(U-2C),                                  \tag{0.1}
\]

and every surviving degree is `2m^2-o(m^2)`, while the maximum codegree is
at most `2m`.

Nevertheless the proposed residual matching is impossible even without
the graphic row.  Any matching which saturated all residual uppers and all
residual owner slots would leave exactly `C` lower resources unused.  The
coordinate-incidence identity forces

\[
 \#\{K\text{ unused lower}:a\in K\}=2C-2c,                       \tag{0.2}
\]

where `c=Cat_(m-1)`.  But

\[
                         2C-2c>C                                \tag{0.3}
\]

for every `m>=3`.  Thus no such matching exists; physical forest
independence is moot.

More strongly, if a residual matching omits `d` upper colours, then

\[
                         d\ge\left\lceil{C-2c\over2}\right\rceil
                          =\left\lceil{I_m\over2}\right\rceil,    \tag{0.4}
\]

where `I_m=C-2c` is the internal Catalan convolution.  Hence the induced
host has an unavoidable `Theta(C)` matching defect.  This is consistent
with the `o(W)` Delcourt--Postle forest but rules out exact saturation in
the frozen one-stratum interface.

The obstruction is a lattice/cocycle row invisible to degrees and
codegrees.  A repaired controlled leave must alter the packet resource
signature, mix strata, or reserve additional outer resources so that the
forced lower-hole coordinate vector is realizable by `C` rank-`m-1` sets.

## 1. The general coordinate-cocycle identity

Let an induced odd owner-slot host retain upper resources `mathcal U'`,
lower resources `mathcal L'`, and owner-slot resources `mathcal S'`.
Let `F` be any owner-slot matching.  For a coordinate `t`, write

\[
\begin{aligned}
 U_t(F)&=\#\{e\in F:t\in\operatorname {upper}(e)\},\\
 L_t(F)&=\#\{e\in F:t\in\operatorname {lower}(e)\},\\
 S_t(F)&=\#\{\text{used owner slots }T^i:t\in T\}.
\end{aligned}                                                     \tag{1.1}
\]

### Lemma 1.1 (edgewise coordinate cocycle)

For every matching `F` and coordinate `t`,

\[
                              S_t(F)=U_t(F)+L_t(F).               \tag{1.2}
\]

#### Proof

One physical diamond has adjacent middle owners `T,H`, lower intersection
`K=T cap H`, and upper union `R=T union H`.  Coordinatewise,

\[
                  {\bf1}_{t\in T}+{\bf1}_{t\in H}
                 ={\bf1}_{t\in K}+{\bf1}_{t\in R}.               \tag{1.3}
\]

Sum (1.3) over the selected edges.  Slot labels do not change physical
coordinate membership. \(\square\)

Suppose now that `F` saturates every retained upper and owner-slot resource.
Let

\[
                 \mathcal H=\mathcal L'\setminus
                  \{\operatorname {lower}(e):e\in F\}            \tag{1.4}
\]

be its unused lower family.  Lemma 1.1 gives the exact forced degree vector

\[
 \boxed{
 h_t:=\#\{K\in\mathcal H:t\in K\}
 =|\mathcal L'_t|+|\mathcal U'_t|-|\mathcal S'_t|.}               \tag{1.5}
\]

Consequently a necessary condition is

\[
 0\le h_t\le|\mathcal H|,
 \qquad \sum_{t\in\Omega}h_t=(m-1)|\mathcal H|.                 \tag{1.6}
\]

Condition (1.6) is only the singleton part of the lower-family degree-
sequence polytope, but it already closes the present residual gate.

## 2. Full-host baseline

Put

\[
 W={2m-1\choose m-1},\qquad
 U={2m-1\choose m+1},\qquad
 C=\operatorname {Cat}_m,qquad c=\operatorname {Cat}_{m-1}.     \tag{2.1}
\]

For every coordinate `t`, the full host has

\[
\begin{aligned}
 |\mathcal L_t|&={2m-2\choose m-2},\\
 |\mathcal U_t|&={2m-2\choose m},\\
 |\mathcal S_t|&=2{2m-2\choose m-1}.
\end{aligned}                                                     \tag{2.2}
\]

The first two binomial coefficients in (2.2) are equal, and

\[
 {2m-2\choose m-1}-{2m-2\choose m-2}=c.                          \tag{2.3}
\]

Therefore the full-host value of the right side of (1.5) is

\[
                  |\mathcal L_t|+|\mathcal U_t|-|\mathcal S_t|
                              =-2c.                              \tag{2.4}
\]

It is negative because the unpunctured host has `2C` more owner slots than
can be used by an upper-saturating matching.  The packet deletion is meant
to remove exactly this scalar slot excess; its coordinate distribution is
what fails.

## 3. The controlled packet contribution

For one packet use the notation from the controlled-leave theorem:

\[
 L=\sigma(S),\qquad V=\beta(S).                                  \tag{3.1}
\]

Its two reserved upper resources are

\[
                         azL,\qquad azV,                          \tag{3.2}
\]

its two reserved lower resources are

\[
                         aS,\qquad L,                             \tag{3.3}
\]

and its six reserved owner slots consist of

\[
 2[aL]+2[azS]+[aV]+[zL].                                         \tag{3.4}
\]

Here coefficients in (3.4) are slot multiplicities.  Deleting one lower
or upper resource subtracts its incidence vector from (1.5), while deleting
one owner slot adds its owner's incidence vector.  Hence one packet changes
the forced hole vector by

\[
\begin{aligned}
 \delta
 &=2\chi_{aL}+2\chi_{azS}+\chi_{aV}+\chi_{zL}
   -\chi_{aS}-\chi_L-\chi_{azL}-\chi_{azV}\\
 &=2\chi_{\{a\}}+\chi_{\{z\}}+\chi_S+\chi_L.                    \tag{3.5}
\end{aligned}
\]

The `beta` target `V` cancels completely.  Formula (3.5) is independent of
the derangement choice, the cycle-independent set, slot labels, and the
spread/concentration properties of the selected bank.

For a bank `P` of order `C`, combine (2.4) and (3.5):

\[
\boxed{
\begin{aligned}
 h_a&=2C-2c,\\
 h_z&=C-2c,\\
 h_t&=-2c+\#\{S\in P:t\in S\}
              +\#\{S\in P:t\in\sigma(S)\},\qquad t\in G.
\end{aligned}}                                                    \tag{3.6}
\]

As a consistency check, summing (3.6) over all `2m-1` coordinates gives

\[
                         \sum_t h_t=(m-1)C,                       \tag{3.7}
\]

using `(m+1)C=2(2m-1)c`, exactly the scalar degree sum of `C` unused
rank-`m-1` sets.

### Theorem 3.1 (exact residual matching no-go)

The induced residual host in the controlled-leave theorem has no matching
which saturates every residual upper and every residual owner slot.

#### Proof

Such a matching would have `U-2C` edges.  Since there are `W-2C` residual
lower resources, its unused lower family would have order exactly `C`.
Every coordinate can occur in at most all `C` members.  But (3.6) requires
`h_a=2C-2c`, and

\[
 2C-2c>C
 \quad\Longleftrightarrow\quad
 C>2c
 \quad\Longleftrightarrow\quad m>2.                              \tag{3.8}
\]

This contradicts (1.6). \(\square\)

The contradiction does not use acyclicity, local degrees, or the choice of
`sigma,beta,P`.  It invalidates the proposed balanced residual forest for
every parameter where the packet construction is defined.

## 4. Exact Catalan-scale deficiency floor

Let `A=U-2C` be the residual upper count, and let `F` be any residual
matching of order

\[
                              |F|=A-d.                            \tag{4.1}
\]

It leaves `d` residual uppers unmatched, `2d` residual owner slots unused,
and `C+d` residual lowers unused.  Let

\[
 u_a=\#\{\text{unmatched residual uppers containing }a\},
 \qquad
 s_a=\#\{\text{unused residual slots whose owner contains }a\}. \tag{4.2}
\]

The same cocycle calculation now gives

\[
                  h_a=(2C-2c)+s_a-u_a.                           \tag{4.3}
\]

Since `h_a<=C+d`, `u_a<=d`, and `s_a>=0`,

\[
 C-2c\le d+u_a-s_a\le2d.                                        \tag{4.4}
\]

### Theorem 4.1 (matching-rank obstruction)

Every matching in the residual host has upper coverage at most

\[
 (U-2C)-\left\lceil{C-2c\over2}\right\rceil.                    \tag{4.5}
\]

Equivalently its upper deficiency obeys (0.4).

This lower bound is `Theta(C)=Theta(W/m)`, but still `o(W)`.  It therefore
explains why the Delcourt--Postle theorem can return an asymptotically
complete residual forest while exact completion is impossible.

## 5. Degree and codegree audit after packet deletion

The failure above does **not** invalidate the local-load theorem.  For
reserved upper/lower sets `R_*`,`L_*` and reserved-slot multiplicity
`rho(T)`, the exact surviving degrees are

\[
\begin{aligned}
 d_*(R)
 &=\sum_{\{x,y\}\subset R}
   {\bf1}_{R-\{x,y\}\notin L_*}
   (2-\rho(R-x))(2-\rho(R-y)),\\
 d_*(K)
 &=\sum_{\{x,y\}\subset\Omega-K}
   {\bf1}_{K+\{x,y\}\notin R_*}
   (2-\rho(K+x))(2-\rho(K+y)),\\
 d_*(T^i)
 &=\sum_{x\in T,\ y\notin T}
   {\bf1}_{T-x\notin L_*}
   {\bf1}_{T+y\notin R_*}
   (2-\rho(T-x+y)).                                               \tag{5.1}
\end{aligned}
\]

For the spread derangement bank, the hypergeometric proof in the source
theorem gives uniformly over all surviving vertices

\[
\begin{aligned}
 d_*(R)&=2m(m+1)-O(m^2/\log m),\\
 d_*(K),d_*(T^i)&=2m(m-1)-O(m^2/\log m).                          \tag{5.2}
\end{aligned}
\]

Induced deletion cannot increase codegrees, so the exact original bounds
remain

\[
 d(U,L)\le4,qquad d(U,T^i)\le2m,qquad
 d(L,T^i)\le2(m-1),qquad d(T^i,H^j)\le1,                        \tag{5.3}
\]

and in particular

\[
                              \Delta_2\le2m=o(m^2).               \tag{5.4}
\]

Thus the induced host passes every advertised degree/codegree asymptotic
row.  Those rows imply only near-perfect conflict-free matchings; they do
not see the integral coordinate lattice (1.5).

## 6. Corrected architecture boundary

The exact necessary first check for any future controlled-leave interface
is:

> Compute `h_t=|L'_t|+|U'_t|-|S'_t|` for every coordinate before invoking
> expansion.  The vector `h` must be the coordinate-degree vector of the
> intended unused lower family.

For `C` unused rank-`m-1` resources this requires at least (1.6), and more
generally all degree-sequence/subset cuts of a `C`-set family.  The present
one-stratum packet signature fails already at `t=a` by exactly

\[
                              h_a-C=C-2c=I_m.                     \tag{6.1}
\]

Possible repairs must change this signature by at least `I_m` units.  They
include mixing a complementary stratum, altering which packet endpoint
slots are reserved for the residual forest, or reserving additional
`a`-containing upper/lower resources with a compensating scalar ledger.
Expansion, high girth and graphic independence become relevant only after
this coordinate cocycle is feasible.
