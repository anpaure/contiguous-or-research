# Trace Hall deficiency under alternating switches

Date: 2026-07-31  
Status: exact switch calculus; explicit smallest two-sided-surjective local
minimum for all Hamilton-safe \(C_6\)- and \(C_8\)-switches; no obstruction
to longer or compound switches

## 1. Scope

Fix \(m\geq2\), put \(\Omega=[2m-1]\), and let \(C\) be a Hamilton cycle
of the middle-levels graph with shores

\[
 {\cal A}=\binom{\Omega}{m-1},\qquad
 {\cal B}=\binom{\Omega}{m}.
\]

For \(A\in{\cal A}\), let its two neighbours on \(C\) be
\(B^-(A),B^+(A)\), and put

\[
 u_C(A)=B^-(A)\cup B^+(A)\in\binom{\Omega}{m+1}.
\]

For \(B\in{\cal B}\), with cycle neighbours \(A^-(B),A^+(B)\), put

\[
 \ell_C(B)=A^-(B)\cap A^+(B)\in\binom{\Omega}{m-2}.
\]

This note concerns the fixed-middle-levels-cycle sufficient subclass from
THREAD_A_CATALAN_TRACE_COMPONENT_HALL_AND_INTEGRAL_ROUNDING_20260731.md.
It does **not** assert that an arbitrary Catalan linear matching is
middle-levels-resolvable.

## 2. Coordinate-free component deficiency

For \(S\subseteq{\cal A}\), define

\[
 \Gamma_C(S)=N_C(S),\qquad U_C(S)=\{u_C(A):A\in S\},
\]

and, for every lower colour \(L\in\binom{\Omega}{m-2}\),

\[
 O_C(L)=\{B\in{\cal B}:\ell_C(B)=L\},\qquad
 \lambda_C(S)=\#\{L:O_C(L)\subseteq\Gamma_C(S)\}.
\]

The empty occurrence class is included, so \(S=\varnothing\) detects a
missing lower turn colour. Put

\[
 \kappa_C(S)=|\Gamma_C(S)|-|S|.
\]

For nonempty proper \(S\), \(\kappa_C(S)\) is exactly the number of cyclic
components of \(S\) in the induced \({\cal A}\)-cycle. At the two boundary
sets this formula is the correct Hall convention. Define

\[
 D_C(S)=\lambda_C(S)-|U_C(S)|-\kappa_C(S),\qquad
 \delta(C)=\max_{S\subseteq{\cal A}}D_C(S).             \tag{2.1}
\]

### Proposition 2.1 (deficiency is exact)

The maximum-matching deficiency of the augmented trace graph is
\(\delta(C)\). In particular, \(C\) admits alternating bijective upper and
lower turn representatives if and only if \(\delta(C)=0\).

#### Proof

The exact Hall compression in the source note is

\[
 |U_C(S)|+|\Gamma_C(S)|-\lambda_C(S)\geq |S|.
\]

Moving the right side to the left gives exactly \(D_C(S)\leq0\). The
standard deficiency form of Hall's theorem identifies the maximum violation
with the number of unmatched vertices in a maximum matching. Since the two
shores of the augmented graph have equal size, this is \(\delta(C)\).
\(\square\)

## 3. Exact alternating-switch derivative

Let \(Z\) be any simple even cycle which alternates between edges of \(C\)
and edges outside \(C\). Toggle it and assume

\[
                         C'=C\mathbin\triangle Z
\]

is again Hamilton. Put \(X=V(Z)\cap{\cal A}\) and
\(Y=V(Z)\cap{\cal B}\). At each vertex of \(Z\), denote its old internal
mate by \(p_0\), its new internal mate by \(p_1\), and its unchanged external
cycle neighbour by \(e\). Thus, for \(A\in X\) and \(B\in Y\),

\[
 u_0(A)=e(A)\cup p_0(A),\qquad u_1(A)=e(A)\cup p_1(A),
\]

\[
 \ell_0(B)=e(B)\cap p_0(B),\qquad
 \ell_1(B)=e(B)\cap p_1(B).                           \tag{3.1}
\]

Fix \(S\subseteq{\cal A}\). Write

\[
 g_t(B)={\bf1}_{\{e(B)\in S\ {\rm or}\ p_t(B)\in S\}}
 \quad(B\in Y),                                      \tag{3.2}
\]

\[
 n_V=\#\{A\in S:u_C(A)=V\},\qquad
 z_L=\#\{B\notin\Gamma_C(S):\ell_C(B)=L\}.
\]

Define

\[
 n'_V=n_V+\sum_{A\in X\cap S}
       \left({\bf1}_{u_1(A)=V}-{\bf1}_{u_0(A)=V}\right),           \tag{3.3}
\]

\[
 z'_L=z_L+\sum_{B\in Y}
 \left({\bf1}_{\ell_1(B)=L}{\bf1}_{g_1(B)=0}
      -{\bf1}_{\ell_0(B)=L}{\bf1}_{g_0(B)=0}\right).              \tag{3.4}
\]

### Theorem 3.1 (literal switch formula)

For every \(S\subseteq{\cal A}\),

\[
\boxed{
\begin{aligned}
 D_{C'}(S)-D_C(S)
  ={}&\sum_L\left({\bf1}_{z'_L=0}-{\bf1}_{z_L=0}\right)\\
    &-\sum_V\left({\bf1}_{n'_V>0}-{\bf1}_{n_V>0}\right)
      -\sum_{B\in Y}(g_1(B)-g_0(B)).
\end{aligned}}                                      \tag{3.5}
\]

Consequently

\[
 \boxed{\quad
 \delta(C')=\max_S\bigl(D_C(S)+\Delta_Z(S)\bigr),
 \quad}                                               \tag{3.6}
\]

where \(\Delta_Z(S)\) is the right side of (3.5).

#### Proof

Only vertices of \(X\) can change upper turn colour, so (3.3) gives the
exact change in
\(|U_C(S)|=\sum_V{\bf1}_{n_V>0}\). Only vertices of \(Y\) can change either
their lower turn colour or their membership in \(\Gamma_C(S)\), so (3.4)
gives the exact update of the number of occurrences of \(L\) outside the
collar. Since \(L\) is trapped precisely when this number is zero, the first
sum in (3.5) is the exact change in \(\lambda\). Finally,

\[
 |\Gamma_{C'}(S)|-|\Gamma_C(S)|
       =\sum_{B\in Y}(g_1(B)-g_0(B)),
\]

while \(|S|\) is fixed. Substitution in (2.1) proves (3.5), and maximizing
proves (3.6). \(\square\)

The formula exposes the obstruction to a naive gradient argument. A local
switch changes only \(X\cup Y\), but whether it creates or destroys a trapped
colour depends on the **global** zero/one status of \(z_L\), and whether it
creates or destroys an upper colour depends on the global support count
\(n_V\). Repairing one current maximum cut is not enough: (3.6) requires
simultaneously lowering every maximum cut without creating a new one.

## 4. Literal short switches

The middle-levels graph has no \(C_4\). Indeed, two distinct
\((m-1)\)-sets with two common \(m\)-supersets would have union of size at
most \(m\); their union then has size exactly \(m\) and is their unique
common \(m\)-superset, a contradiction.

Every \(C_6\) has the usual form, for \(|R|=m-2\) and distinct
\(a,b,c\notin R\),

\[
 R+a\subset R+a+b\supset R+b\subset R+b+c\supset
 R+c\subset R+c+a\supset R+a.                       \tag{4.1}
\]

It is switchable exactly when one of its two alternating perfect matchings
lies in \(C\), and it is Hamilton-safe exactly when the toggled two-factor
is connected. The same definitions apply to a literal \(C_8\), or to any
longer alternating circuit.

## 5. Smallest short-switch local minimum

Take \(m=4\), so \(\Omega=[7]\). In bitmask notation, the following cyclic
list is a Hamilton cycle of \({\rm ML}(7)\):

    7 23 19 51 49 57 56 60 52 53 21 29 13 15 11 43 41 105
    73 75 67 71 70 78 74 90 88 89 25 27 26 58 50 114 98 102
    38 54 22 86 82 83 81 85 84 116 100 108 44 45 37 101 69 77
    76 92 28 30 14 46 42 106 104 120 112 113 97 99 35 39

Both turn maps are surjective. The lower multiplicity histogram is
\(1^8 2^{12}3^1\); the upper histogram is \(1^{10}2^8 3^3\).
Nevertheless the augmented graph has maximum matching \(55/56\), so
\(\delta(C)=1\).

A literal component-Hall witness is the set of lower-shore indices

\[
 S=\{2,3,4,13,14,15,17,18,19\}.                     \tag{5.1}
\]

It has three cyclic components and only four upper colours,

\[
 U_C(S)=\{59,61,91,118\},
\]

while its collar traps eight lower colours,

\[
 \{6,17,18,20,24,34,48,72\}.
\]

Thus

\[
                 D_C(S)=8-4-3=1.                    \tag{5.2}
\]

### Theorem 5.1 (short-switch local minimum)

The cycle above has no Hamilton-safe \(C_6\)- or \(C_8\)-switch which lowers
\(\delta\). More precisely:

* among all \(210\) literal \(C_6\)'s, \(30\) alternate with \(C\), \(9\)
  are Hamilton-safe, and their new deficiencies are \(1^7 2^1 3^1\);
* among all \(630\) literal \(C_8\)'s, \(41\) alternate with \(C\), \(23\)
  are Hamilton-safe, and their new deficiencies are \(1^{14}2^8 3^1\).

Hence the assertion

> every positive component-Hall deficiency admits a Hamilton-safe short
> flip which strictly lowers it

is false, even after assuming both turn words are surjective.

The scope is sharp. The graph contains \(6048\) literal \(C_{10}\)'s; \(203\)
alternate with \(C\), \(94\) are Hamilton-safe, and eleven of those give
\(\delta=0\). Thus this is not an obstruction to longer or compound
symmetric-difference switches.

The example is smallest by \(m\). For \(m=2\) the single turn colours are
automatic. For \(m=3\), an exhaustive census has \(24\) Hamilton cycles of
\({\rm ML}(5)\) up to fixed start and reversal, and every one has
\(\delta=0\). The first short-switch local minimum therefore occurs at
\(m=4\).

## 6. Consequence for the all-\(m\) route

The fixed-cycle trace approach has an exact polynomial test (one augmented
bipartite matching), and (3.5) gives an exact update under every proposed
switch. What it does **not** have is a monotone \(C_6/C_8\) augmentation
theorem. Any recursive construction must instead do one of the following:

1. preserve the component-Hall cuts globally while constructing the cycle;
2. permit larger correlated switches (the first example already needs a
   \(C_{10}\)); or
3. bypass middle-levels support and construct the ordered four-transversal
   directly.

Allowing an arbitrary compound symmetric difference does not itself prove
anything: switching from a bad cycle to a good decorated cycle presupposes
the existence of the latter. The unrestricted compound-switch assertion is
therefore a reformulation of the remaining existence theorem, not a local
descent proof.

## 7. Reproducible audit

Run

    python3 scratch/audit_catalan_trace_switch_local_minimum_20260731.py

The audit independently verifies the Hamilton cycle, both turn
surjections, the \(55/56\) augmented matching, witness (5.1)--(5.2), all
simple \(C_6,C_8,C_{10}\) counts, every Hamilton-safe toggle and its exact
new matching deficiency, and the complete \(m=3\) minimality census.
