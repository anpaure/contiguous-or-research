# The lamp complement centers cannot be grouped into forward rectangles

**Date:** 2026-08-07  
**Input:** `MATH_THEOREM_NONABELIAN_LAMP_PHASE_FACTOR_AND_BINARY_CENTER_LIFT_20260807.md`  
**Status:** theorem.  The nonabelian lamp factor closes the equal-degree
phase and pairwise center-transplant gates, but its center lift is forced,
up to toggling coordinates globally, to be a code of minimum Johnson
distance three on each role shore.  Hence no two distinct centers on one
shore share an \((r-3)\)-core, and this phase factor cannot be partitioned
into nontrivial forward rectangles under any binary center realization of
the prescribed edge exchanges.

## 1. Coset coordinates

Retain the notation of the lamp construction.  Thus

\[
 V=\{v\in\mathbb F_2^{\mathbb Z_w}:\sum_i v_i=0\},
 \qquad
 \mathcal G=V\rtimes C_w,
\]

where \(w\ge5\) is odd, and

\[
 \mathcal H=\langle e_2+e_j:3\le j\le w-1\rangle.
\]

The subgroup has the concrete description

\[
 \mathcal H=\{v\in V:v_0=v_1=0\}.                 \tag{1.1}
\]

Consequently a left coset \(\mathcal H(v,j)\) is determined exactly by

\[
                         (v_0,v_1,j)
             \in\mathbb F_2^2\times\mathbb Z_w.    \tag{1.2}
\]

This identifies the active alphabet \(\Omega=\mathcal H\backslash
\mathcal G\) with \(\mathbb F_2^2\times\mathbb Z_w\).

## 2. The positive shore is an adjacent-pair code

Let \(g=(v,j)\).  The positive leaf set is

\[
 F_+(g)=\{\mathcal Ha^tg:t\in\mathbb Z_w\}.
\]

For \(\ell=j+t\), put

\[
                         z_\ell=v_{j-\ell}.          \tag{2.1}
\]

Because the cyclic shift convention gives
\((\tau^tv)_i=v_{i-t}\), equations (1.2) and (2.1) give

\[
 \boxed{
 F_+(g)=F_z:=
 \{(z_\ell,z_{\ell-1},\ell):\ell\in\mathbb Z_w\}.}
                                                               \tag{2.2}
\]

The word \(z\) has even parity.  Moreover, replacing \(g\) by another
element of the same positive role \(\langle a\rangle g\) leaves \(z\)
unchanged.  Conversely every even binary word occurs.  Hence positive roles
are in bijection with even binary words, through (2.2).

### Theorem 2.1 (minimum distance three)

If \(z\ne z'\) are even binary words, then

\[
                         |F_z-F_{z'}|
                       = |F_{z'}-F_z|\ge3.           \tag{2.3}
\]

#### Proof

Let

\[
                         D=\{i:z_i\ne z'_i\}.
\]

The two codewords choose one alphabet point in each fibre
\(\mathbb F_2^2\times\{\ell\}\).  Their chosen points in fibre \(\ell\)
differ exactly when

\[
                         \ell\in D\cup(D+1).         \tag{2.4}
\]

Since \(z,z'\) have the same parity, \(D\) has positive even size.  Thus
\(|D|\ge2\).  For \(w\ge5\), every nonempty even \(D\subset\mathbb Z_w\)
satisfies

\[
                         |D\cup(D+1)|\ge3;           \tag{2.5}
\]

equality occurs for two cyclically adjacent positions.  Each differing
fibre contributes one point to each one-sided set difference, proving
(2.3). \(\square\)

## 3. The negative shore has the same distance

Using

\[
                         cb^t=(e_2+e_t,t),           \tag{3.1}
\]

define, for \(\ell=j+t\),

\[
 z_\ell=v_{j-\ell}+\mathbf 1_{\{\ell=j\}}.          \tag{3.2}
\]

Then the negative leaf set has exactly the same form

\[
 \boxed{
 F_-(g)=\{\mathcal Hcb^tg:t\in\mathbb Z_w\}
       =\{(z_\ell,z_{\ell-1},\ell):\ell\in\mathbb Z_w\}.}
                                                               \tag{3.3}
\]

Here \(z\) has odd parity, and negative roles are in bijection with the odd
binary words.  The difference of two odd words again has positive even
weight, so Theorem 2.1 applies verbatim:

\[
 |F_-(R)-F_-(R')|=|F_-(R')-F_-(R)|\ge3              \tag{3.4}
\]

for distinct negative roles \(R,R'\).

## 4. Consequence for complement centers

The natural active centers in the lamp lift are

\[
                         C(R)=\Omega-F(R).           \tag{4.1}
\]

Complementation preserves Johnson distance.  Therefore distinct centers
on either role shore satisfy

\[
                         |C(R)-C(R')|
                       = |C(R')-C(R)|\ge3.           \tag{4.2}
\]

Adding the common filler \(K\) does not change this distance.

A shore of a forward rectangle with core \(S\) consists instead of centers

\[
                         S+x\qquad(x\in X),          \tag{4.3}
\]

so every two distinct centers on that shore have Johnson distance one.
Equations (4.2) and (4.3) are incompatible as soon as the shore has at least
two roles.

### Corollary 4.1 (no direct rectangle extraction)

No nontrivial forward \(K_{p,p+1}\) rectangle with \(p\ge2\) can be formed
from the complement centers of the lamp factor, on either shore.

At this point the conclusion rules out direct extraction from the natural
complement lift.  Section 5 strengthens it: on the full connected phase
factor, a different binary solution of the same center-exchange equations
cannot help either.

## 5. The obstruction holds for every binary center lift

The previous conclusion can be strengthened because the role graph is
connected.

### Lemma 5.1 (connected role graph)

The bipartite role graph formed by the right cosets of
\(A=\langle a\rangle\) and \(B=\langle b\rangle\) is connected.

#### Proof

The kernel element

\[
                         ba^{-1}=e_0+e_1
\]

lies in \(\langle a,b\rangle\).  Conjugating it by the powers of \(a\)
gives

\[
                         e_i+e_{i+1}
       \in\langle a,b\rangle\qquad(i\in\mathbb Z_w).              \tag{5.1}
\]

The edge vectors of a cyclic graph span the even-weight subspace \(V\).
Together with \(a\), they generate \(V\rtimes C_w=\mathcal G\).  Thus

\[
                         \langle A,B\rangle=\mathcal G.            \tag{5.2}
\]

Connected components of the \((A,B)\)-coset incidence graph are the right
cosets of \(\langle A,B\rangle\), so (5.2) proves connectedness.
\(\square\)

### Theorem 5.2 (center-voltage rigidity)

Let \(G_R\) be any binary center assigned to every positive and negative
role of the lamp factor, on an arbitrary larger coordinate alphabet.  Assume
that across every phase edge the two centers exchange exactly the two
prescribed first leaf pairs, so that the all-depth proper chains agree.
Then there is one fixed binary set \(Z\), independent of the role, such that

\[
                         G_R=C_R\mathbin\triangle Z                 \tag{5.3}
\]

for every role \(R\), where \(C_R\) is the complement-center solution of
Section 4 (extended by zeros on any extra coordinates).

Consequently, if all \(G_R\) have the same cardinality, then any two
distinct roles on one shore satisfy

\[
                         |G_R-G_{R'}|=|G_{R'}-G_R|\ge3.             \tag{5.4}
\]

#### Proof

Regard center indicators as vectors over \(\mathbb F_2\).  The prescribed
exchange on an edge \(RR'\) is an equation

\[
                         g_{R'}-g_R=\delta_{RR'}.                   \tag{5.5}
\]

The complement centers satisfy the same equations.  Subtracting the two
systems shows that \(g_R-c_R\) is constant across every edge.  Lemma 5.1
makes it one global vector \(\mathbf1_Z\), proving (5.3).

Symmetric difference with the same \(Z\) preserves the Hamming distance
between every pair of centers.  Sections 2--4 show that distinct same-shore
complement centers have Hamming distance at least six.  If \(G_R,G_{R'}\)
have equal cardinality, their two one-sided differences have equal size,
so each has size at least three.  This is (5.4). \(\square\)

### Corollary 5.3 (the lamp phase factor itself is nonrectangular)

No binary center lift of the full connected lamp phase factor, satisfying
the exact edge-transplant equations and equal center ranks, contains two
same-shore roles at Johnson distance one.  In particular, changing the
common filler or choosing a different solution of the center equations
cannot create a forward rectangle.

The surviving route must therefore alter the phase factor itself (for
example by using a disconnected or block-structured noncommuting factor),
or introduce extra actuators which change the edge-voltage equations before
rectangle grouping.  A mere reassignment of centers is not enough.
