# Complement-equivariant depth-one cores as constrained Kneser matchings

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Assume \(m\ge2\), and put

\[
 \Omega=[2m],\qquad
 \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal M=\binom{\Omega}{m},
\]

\[
 W=|\mathcal M|=\binom{2m}{m},\qquad
 N=|\mathcal L|=\binom{2m}{m-1},\qquad
 D=W-N={W\over m+1}=\operatorname {Cat}_m.
\]

There is an exact phase-free normal form for both the requested
near-spanning depth-one object and its strongest zero-excess version.

> A complement-equivariant Johnson cycle on \(G\) owners that covers
> every lower target is equivalent to an edge cover \(Q\) of
> \(KG(2m,m-1)\), with \(|E(Q)|=G/2\), whose canonical middle lift is one
> cycle. Its lower and upper loads are \(d_Q(R)\) and \(d_Q(U^c)\).

> A complement-equivariant Johnson cycle of length \(N\), with every
> lower \((m-1)\)-colour and every upper \((m+1)\)-colour used exactly
> once, is equivalent to a perfect matching \(M\) of
> \(KG(2m,m-1)\) whose canonical middle lift \(H(M)\) is one cycle.

The colour conditions and complement symmetry are automatic in the
Kneser formulation. The only remaining condition is the physical owner
condition

\[
 d_{H(M)}(X)\in\{0,2\}\qquad(X\in\mathcal M),                  \tag{0.1}
\]

with connected nonisolated support. Since \(H(M)\) has \(N\) edges,
(0.1) automatically gives exactly \(N\) used owners and \(D\) omitted
owners.

This yields four exact conclusions.

1. The Mersenne obstruction is built into the normal form: a perfect
   matching can exist only when \(N\) is even, equivalently when
   \(D=\operatorname {Cat}_m\) is even, equivalently when
   \(m\ne2^a-1\).
2. Every Kneser perfect matching already has the correct coordinate-swap
   degrees. Thus there is no further singleton-coordinate obstruction.
3. The completely symmetric LP relaxation satisfies every owner-degree
   equation exactly. The remaining gap is purely simultaneous
   integrality plus connectivity.
4. Alternating-cycle switches connect the entire perfect-matching space
   and preserve complement symmetry and exact two-sided rainbowness at
   every intermediate state. They are therefore the correct switch
   space; ordinary switches on one projected GMM cycle explore only a
   much smaller slice.

The theorem does not construct the required edge cover. It reduces the
open complement-coherent \(q=1\) theorem to one constrained edge-cover
problem with no residual colour bookkeeping; at zero excess it becomes a
constrained 1-factor.

## 1. From a complement-paired Johnson edge to a Kneser edge

Let \(e=\{X,Y\}\) be an edge of \(J(2m,m)\), and put

\[
 R=X\cap Y,\qquad U=X\cup Y.                                  \tag{1.1}
\]

Then \(|R|=m-1\), \(|U|=m+1\), and the complemented edge

\[
 e^c=\{X^c,Y^c\}                                               \tag{1.2}
\]

has lower colour \(U^c\) and upper colour \(R^c\). In particular,

\[
 R\cap U^c=\varnothing.                                       \tag{1.3}
\]

Conversely, let \(R,S\in\mathcal L\) be disjoint. Exactly two points
remain:

\[
 \Omega\setminus(R\cup S)=\{a,b\}.                            \tag{1.4}
\]

Define the two complementary Johnson edges

\[
 e_R(R,S)=\{R\cup\{a\},R\cup\{b\}\},                          \tag{1.5}
\]

\[
 e_S(R,S)=\{S\cup\{a\},S\cup\{b\}\}=e_R(R,S)^c.               \tag{1.6}
\]

Their lower colours are \(R,S\), respectively, and their upper colours
are \(S^c,R^c\), respectively.

Thus an unordered disjoint pair \(\{R,S\}\), namely an edge of
\(KG(2m,m-1)\), is exactly one complement orbit of Johnson edges together
with both of its colour labels.

## 2. Exact Kneser normal form

For any simple subgraph \(Q\subseteq KG(2m,m-1)\), define \(H(Q)\) on the
middle owners by adding the two edges (1.5)--(1.6) for every
\(\{R,S\}\in E(Q)\).

### Theorem 2.0 (general edge-cover normal form)

Let \(G\) be even. The following are equivalent.

1. There is a simple Johnson \(G\)-cycle whose successor commutes with
   complementation.
2. There is a simple subgraph \(Q\subseteq KG(2m,m-1)\) with
   \(|E(Q)|=G/2\) such that \(H(Q)\) is one cycle.

Under the correspondence, the physical depth-one loads are

\[
 \boxed{\mu^-(R)=d_Q(R),\qquad
        \mu^+(U)=d_Q(U^c).}                                   \tag{2.0a}
\]

Consequently the cycle covers every lower target if and only if
\(\delta(Q)\ge1\), and then it covers every upper target as well. Its
total repeat excess over the forced one-cover baseline is exactly

\[
 \boxed{
 \sum_{R\in\mathcal L}(d_Q(R)-1)
 =2|E(Q)|-N
 =G-N.}                                                       \tag{2.0b}
\]

In particular, a core of size \(G=W-\ell\), \(0\le\ell\le D\), is exactly
an edge cover with surplus

\[
                         G-N=D-\ell=O(W/m).                    \tag{2.0c}
\]

Because every lower degree is positive, this is also the exact one-sided
\(L^1\) overload:

\[
 \sum_{R\in\mathcal L}(d_Q(R)-1)_+=G-N.                        \tag{2.0d}
\]

Here \(G/N<2\), so the floor quota is one and the CPCR energy would be

\[
 \Phi_1(Q)=\sum_{R\in\mathcal L}(d_Q(R)-1)(d_Q(R)-2).           \tag{2.0e}
\]

Coverage requires only \(d_Q(R)\ge1\); it does not require
\(\Phi_1(Q)=0\). Thus already at \(q=1\), CPCR is a genuinely stronger
surrogate than the physical one-sided target, while the entire \(L^1\)
overload is automatically only \(O(W/m)\).

#### Proof

For 2, equations (1.5)--(1.6) make \(H(Q)\) complement-invariant. A
connected 2-regular lift is a cycle, and the same no-fixed-vertex/no-fixed-
edge argument used below shows that complementation acts as its half-turn.
Each edge of \(Q\) incident with \(R\) contributes exactly one Johnson edge
of lower colour \(R\); its complementary edge has upper colour \(R^c\).
This proves (2.0a), and summing the lower degrees proves (2.0b).

Conversely, partition the edges of the complement-equivariant cycle into
complement pairs. A Johnson edge and its complement have disjoint lower
colours \(R,U^c\), hence determine an edge of the Kneser graph by
Section 1. Distinct Johnson edge orbits determine distinct Kneser edges.
Their lift is the original cycle, which proves 2. \(\square\)

Thus the user's asymptotic complement-coherent \(q=1\) target is not a
perfect-matching problem but a **near-perfect edge-cover problem with a
2-regular middle lift**. The perfect-matching case below is its strongest
zero-excess specialization.

For arbitrary \(Q\), the owner degrees are exactly

\[
 d_{H(Q)}(X)=
 \#\Bigl\{(x,y)\in X\times X^c:
   \{X\setminus\{x\},X^c\setminus\{y\}\}\in E(Q)\Bigr\},        \tag{2.0f}
\]

and \(d_{H(Q)}(X)=d_{H(Q)}(X^c)\). Hence the entire physical condition is
that (2.0f) equal \(0\) or \(2\) at every owner, plus connectedness.

For a matching \(M\subseteq E(KG(2m,m-1))\), retain the notation \(H(M)\).

### Theorem 2.1 (normal-form equivalence)

The following are equivalent.

1. There is a complement-invariant simple Johnson cycle factor \(P\)
   with \(N\) edges whose lower colours are all members of
   \(\mathcal L\), once each.
2. There is a perfect matching \(M\) of \(KG(2m,m-1)\) such that
   \(H(M)\) is 2-regular on its nonisolated support.

Under this correspondence:

* the upper colours also exhaust \(\binom{\Omega}{m+1}\) once each;
* the support is complement-closed and has exactly \(N\) owners;
* \(P\) is one cycle if and only if \(H(M)\) is connected after isolated
  vertices are deleted.
* in the connected case, complementation acts on that cycle as its
  half-turn, so either orientation has successor map satisfying

  \[
                         P(X^c)=P(X)^c.                         \tag{2.0}
  \]

#### Proof

Assume 1. Complementation permutes the edges of \(P\). For the unique
edge with lower colour \(R\), let its upper colour be \(U_R\), and set

\[
 \tau(R)=U_R^c.                                                \tag{2.1}
\]

By (1.3), \(R\cap\tau(R)=\varnothing\). Complementing that edge gives
the unique edge with lower colour \(\tau(R)\), and its upper colour is
\(R^c\). Hence

\[
 \tau^2(R)=R.                                                  \tag{2.2}
\]

There are no fixed points because two \((m-1)\)-sets paired by (2.1) are
disjoint and \(m>1\). Thus the pairs \(\{R,\tau(R)\}\) form a perfect
matching \(M\) of the Kneser graph. Equations (1.5)--(1.6) show that
\(H(M)=P\).

Conversely, let \(M\) be a perfect matching. Each \(R\in\mathcal L\)
occurs in exactly one matching edge and hence labels exactly one edge of
\(H(M)\). Equations (1.5)--(1.6) show simultaneously that every upper
colour occurs exactly once and that complementation preserves the edge
set. If the lift is 2-regular, its number of nonisolated vertices equals
its number \(N\) of edges.

If the lift is connected, complementation is a fixed-point-free
involutive automorphism of its abstract cycle. It cannot be a reflection:
a vertex-axis reflection would fix a middle owner, while an edge-axis
reflection would make the endpoints of one Johnson edge complementary,
although complementary \(m\)-sets have Johnson distance \(m>1\).
Therefore it is the half-turn, which commutes with either cyclic
successor. The remaining assertions follow.
\(\square\)

### Corollary 2.2 (degree formula)

For \(X\in\mathcal M\),

\[
 d_{H(M)}(X)=
 \#\Bigl\{(x,y)\in X\times X^c:
       M(X\setminus\{x\})=X^c\setminus\{y\}\Bigr\}.             \tag{2.3}
\]

In particular,

\[
 d_{H(M)}(X)=d_{H(M)}(X^c).                                   \tag{2.4}
\]

#### Proof

An edge of \(M\) contributes an incident edge at \(X\) exactly when it
has the form

\[
 \{X\setminus\{x\},\,X^c\setminus\{y\}\}
\]

for a unique \((x,y)\in X\times X^c\). Complementation exchanges \(X\)
and \(X^c\) and preserves the same matching edge. \(\square\)

Thus the exact unresolved constraint is

\[
 \boxed{
 \#\Bigl\{(x,y)\in X\times X^c:
       M(X-x)=X^c-y\Bigr\}\in\{0,2\}
 \quad\text{for every }X.}                                    \tag{2.5}
\]

No lower- or upper-colour condition remains outside (2.5).

## 3. Parity and the automatic coordinate ledger

### Proposition 3.1 (Mersenne parity in the normal form)

A perfect matching \(M\) as above requires \(N\) even. Moreover

\[
 N=m\operatorname {Cat}_m,                                    \tag{3.1}
\]

so \(N\) is odd exactly when \(m=2^a-1\). Hence the exact normal form is
impossible in precisely those dimensions.

#### Proof

The identity (3.1) follows from

\[
 \binom{2m}{m-1}={m\over m+1}\binom{2m}{m}.
\]

The Catalan number is odd exactly for \(m=2^a-1\). If \(m\) is even,
\(N\) is even; if \(m\) is odd, \(N\) has the parity of the Catalan
number. \(\square\)

For \(m\ne2^a-1\), the matching layer itself is nonempty. Indeed,
\(KG(2m,m-1)\) is connected and vertex-transitive, and the standard
vertex-transitive matching theorem says that every connected
vertex-transitive graph of even order has a perfect matching. Thus outside
the Mersenne dimensions, all of the unresolved content lies in the lifted
owner degrees (2.5), not in existence of a Kneser 1-factor.

Suppose now that \(M\) exists. For \(\{R,S\}\in M\), call the pair

\[
 L(R,S)=\Omega\setminus(R\cup S)                               \tag{3.2}
\]

its two-point leave. Both Johnson edges lifted from this matching edge
swap exactly the two coordinates in \(L(R,S)\).

### Theorem 3.2 (automatic leave regularity)

For every coordinate \(z\in\Omega\), exactly \(D/2\) edges of \(M\) have
\(z\in L(R,S)\). Consequently the coordinate-swap multigraph of \(H(M)\)
is \(D\)-regular: it is twice the leave multigraph of \(M\).

#### Proof

There are \(N/2\) edges of \(M\). A matching edge fails to leave \(z\)
exactly when one of its two lower-set endpoints contains \(z\); both
cannot contain \(z\), because the endpoints are disjoint. Since every
lower set occurs once, the number of such matching edges is

\[
 \binom{2m-1}{m-2}.                                           \tag{3.3}
\]

Therefore the number leaving \(z\) is

\[
 {N\over2}-\binom{2m-1}{m-2}
 ={1\over2}\,{W\over m+1}
 ={D\over2}.                                                   \tag{3.4}
\]

Each such matching edge gives two Johnson edges with the same swap pair,
so the swap degree at \(z\) is \(D\). \(\square\)

This recovers the Catalan parity obstruction, but also proves that once a
Kneser 1-factor exists, every first-coordinate moment is already exactly
right. The remaining owner-degree obstruction (2.5) is genuinely
higher-order.

## 4. The exact integer formulation and its symmetric fractional point

For the general \(G\)-edge-cover target, replace (4.1) below by

\[
 \sum_{S:S\cap R=\varnothing}z_{R,S}\ge1,                     \tag{4.0a}
\]

replace the right side of (4.3) by \(G\), and impose

\[
                         2\sum_{\{R,S\}}z_{R,S}=G.             \tag{4.0b}
\]

Its completely symmetric relaxation has

\[
 z_{R,S}={G\over N\Delta},\qquad a_X={G\over W}.               \tag{4.0c}
\]

Indeed, every lower degree is \(G/N\ge1\), while every owner degree is

\[
 m^2{G\over N\Delta}={2G\over W}=2a_X.                        \tag{4.0d}
\]

Thus even the near-spanning edge-cover form has an exact symmetric
fractional solution for every \(N\le G\le W\). The unresolved issue is
again integral simultaneous rounding of the lower-cover and owner-degree
constraints.

For each Kneser edge \(\{R,S\}\), introduce \(z_{R,S}\in\{0,1\}\), and
for each complementary owner pair introduce a common variable
\(a_X=a_{X^c}\in\{0,1\}\). The desired cycle factor is exactly the
integer system

\[
 \sum_{S:S\cap R=\varnothing}z_{R,S}=1
 \qquad(R\in\mathcal L),                                      \tag{4.1}
\]

\[
 \sum_{x\in X}\sum_{y\in X^c}
 z_{X-x,\,X^c-y}=2a_X
 \qquad(X\in\mathcal M),                                      \tag{4.2}
\]

\[
 \sum_{X\in\mathcal M}a_X=N.                                  \tag{4.3}
\]

Connectivity is the usual additional family of subtour inequalities.

Let

\[
 \Delta=\binom{m+1}{2}                                        \tag{4.4}
\]

be the degree of \(KG(2m,m-1)\).

### Theorem 4.1 (exact fractional barycentre)

The relaxation of (4.1)--(4.3) has the fully symmetric feasible point

\[
 z_{R,S}={1\over\Delta},\qquad a_X={m\over m+1}.                \tag{4.5}
\]

#### Proof

Equation (4.1) follows from Kneser regularity. For fixed \(X\), the
double sum in (4.2) has \(m^2\) terms, so at (4.5) it equals

\[
 {m^2\over\binom{m+1}{2}}={2m\over m+1}=2a_X.                 \tag{4.6}
\]

Finally

\[
 \sum_Xa_X={m\over m+1}W=N.                                   \tag{4.7}
\]

\(\square\)

Hence Hall capacity, all singleton owner degrees, both shadow shores, and
complement symmetry are simultaneously feasible with equality. The
missing theorem is an integral rounding theorem for (4.1)--(4.3), followed
by cycle joining. This is strictly more precise than asking for an
unspecified complement-symmetric switch.

## 5. The complete complement-preserving switch space

Let \(M,M'\) be perfect matchings of the Kneser graph. Their symmetric
difference is a vertex-disjoint union of even cycles alternating between
\(M\) and \(M'\). Flipping one such alternating cycle replaces its
\(M\)-edges by the other parity class and yields another perfect matching.

### Theorem 5.1 (alternating-cycle reconfiguration)

Every two Kneser perfect matchings are connected by alternating-cycle
flips. Under the lift \(M\mapsto H(M)\), every intermediate state has:

1. exact lower rainbowness;
2. exact upper rainbowness;
3. exact complement invariance of its Johnson edge set; and
4. the coordinate-swap degree \(D\) at every coordinate.

Only the owner degrees (2.3), and then connectedness, can fail during the
reconfiguration.

#### Proof

Flip the alternating components of \(M\triangle M'\) one at a time. The
four invariant assertions follow from Theorems 2.1 and 3.2 for every
perfect matching encountered. \(\square\)

This is the natural switch space beyond the explicit GMM lower-cycle
forest. It is complete for all exact complement-equivariant two-sided
colour systems: no such system lies outside it. A successful proof must
therefore establish one of the following equivalent-strength statements.

* There is a Kneser 1-factor satisfying (2.5).
* The integer system (4.1)--(4.3) is feasible.
* Some alternating-cycle-flip trajectory reaches owner degrees \(0/2\).

Connectivity of the resulting owner 2-factor is a final, separate cycle-
joining condition. No theorem in this note proves either integral gate.

## 6. Scope

The normal form concerns the strongest exact \(N\)-edge core on even
ground. For Mersenne \(m\), one omitted lower colour and its complementary
upper omission remove the scalar parity obstruction; this costs only one
colour and is asymptotically harmless. The corresponding near-perfect
Kneser formulation has exposed vertices and one repeated or omitted
colour, so it is not literally (4.1).

Accordingly, the theorem proves neither an asymptotic obstruction nor the
constant-one theorem. Its contribution is structural: it identifies a
complete, complement-preserving switch space in which both shadow shores
are solved exactly and only the physical owner-cycle condition remains.

As a calibration, when \(m=2\), take the Kneser matching

\[
 \{\{1\},\{2\}\},\qquad \{\{3\},\{4\}\}.
\]

Its lift is the complement-equivariant four-cycle

\[
 13,\ 14,\ 24,\ 23,\ 13,
\]

with all four singleton lower colours and all four triple upper colours
used exactly once. Thus the normal form contains the smallest positive
example.
