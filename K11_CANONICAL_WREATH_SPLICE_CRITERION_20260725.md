# Exact physical splice criterion for canonical (K=11) wreath cycles

Date: 2026-07-25

## 1. Scope

This note concerns the canonical cyclic realization of an exact middle
wreath factor.  It gives a necessary and sufficient local criterion for
splicing two canonical eleven-cycles into one physical endpoint path.
It does not prove that the forty-two cycles admit the required global
six-path fusion.

Let a canonical cycle be written in a cyclic coordinate order

\[
 z_0,z_1,\ldots,z_{10}.
\]

At index (i\in\mathbb Z_{11}), put

\[
 S_i=\{z_{i-5},z_{i-4},z_{i-3},z_{i-2},z_{i-1}\},
\]

\[
 D_i=\{z_{i+1},z_{i+2},z_{i+3},z_{i+4},z_{i+5}\}.
\]

The missing and transition ports are

\[
 a_i=z_i,\qquad b_i=z_{i-5}.
\]

Thus (D_i) is disjoint from both (S_i) and (S_{i+1}), and the
canonical transition is

\[
 S_i,D_i,S_{i+1}.
\]

## 2. General seam criterion

Cut the transition after (D_i) in one physical path.  Let a second,
vertex-disjoint physical path begin at a source (S'_h), with its own port word

\[
 a'_h,b'_h,a'_{h+1},b'_{h+1},\ldots.
\]

Assume

\[
 S'_h\cap D_i=\varnothing.
\]

Vertex-disjointness in particular gives (S'_h\ne S_i) and
(D'_h\ne D_i).  These exclusions are essential: they rule out the two
degenerate equal-facet cases in which the apparent cross port equals an old
missing port and the exchange form below is not a genuine transition.

There is then a unique cross port

\[
 \beta=\Omega\setminus(S'_h\cup D_i).
\]

The cross transition is

\[
 S'_h=S_i-\beta+a_i,
 \qquad
 D'_h=D_i-a'_h+\beta.
\tag{2.1}
\]

### Theorem 2.1 (five seam inequalities)

The concatenation through the cross port \(\beta\) is physical if and only
if

\[
 \boxed{
 \begin{aligned}
 \beta&\ne a_{i-2},a_{i-1},\\
 b'_h&\ne a_{i-1},a_i,\\
 b'_{h+1}&\ne a_i.
 \end{aligned}}
\tag{2.2}
\]

All other no-lazy inequalities are inherited from the two old paths or
are automatic from the two incidence relations in (2.1).

#### Proof

Around the new seam the port word is

\[
 \ldots,a_{i-2},b_{i-2},a_{i-1},b_{i-1},a_i,
 \beta,a'_h,b'_h,a'_{h+1},b'_{h+1},\ldots.
\]

For every insertion (a_j), physicality is exactly the exclusion of that
symbol from the next two deletion ports.  The only such pairs changed by
the splice are

\[
 (a_{i-2};b_{i-1},\beta),
 \quad
 (a_{i-1};\beta,b'_h),
 \quad
 (a_i;b'_h,b'_{h+1}).
\]

The old inequalities involving (b_{i-1}) remain valid, leaving exactly
(2.2).  Starting with (a'_h), both future deletion ports are unchanged.
The automatic inequalities (a_i\ne\beta) and (a'_h\ne\beta) follow
from (2.1): equality would identify respectively the cross source with
(S_i), or the cross target with (D_i).  This proves necessity and
sufficiency. \(\square\)

## 3. Only two external facets survive at a canonical tail

Write

\[
 U_i=\Omega\setminus D_i
     =\{z_{i-5},z_{i-4},z_{i-3},z_{i-2},z_{i-1},z_i\}.
\]

Every possible cross source is a facet (U_i-\beta).  Two facets belong
to the old canonical cycle:

\[
 U_i-z_i=S_i,
 \qquad
 U_i-z_{i-5}=S_{i+1}.
\]

The four remaining facets are the off-cycle candidates.

### Corollary 3.1 (two-candidate theorem)

If (S'_h) belongs to a different canonical wreath cycle, then the first
line of (2.2) holds if and only if

\[
 \boxed{\beta\in\{z_{i-4},z_{i-3}\}.}
\tag{3.1}
\]

Consequently every canonical tail has exactly two off-cycle source facets
that pass all backward-looking physical tests.  Such a facet gives a full
physical splice precisely when its first two outgoing deletion ports also
satisfy

\[
 \boxed{
 b'_h\notin\{z_{i-1},z_i\},
 \qquad b'_{h+1}\ne z_i.}
\tag{3.2}
\]

#### Proof

For an off-cycle source, \(\beta\) is one of

\[
 z_{i-4},z_{i-3},z_{i-2},z_{i-1}.
\]

The first line of (2.2) excludes its last two members.  Substituting
(a_{i-1}=z_{i-1}) and (a_i=z_i) into the remaining two lines of
(2.2) gives (3.2). \(\square\)

## 4. The new shadow colors

The lower and complementary-upper colors created by the splice are

\[
 \boxed{B^*=S_i\cap S'_h=U_i\setminus\{z_i,\beta\},}
\tag{4.1}
\]

\[
 \boxed{Y^*=D_i\cap D'_h=D_i\setminus\{a'_h\}.}
\tag{4.2}
\]

In the two backward-eligible cases, (4.1) is respectively

\[
 \begin{array}{c|c}
 \beta& B^*\\ \hline
 z_{i-4}&\{z_{i-5},z_{i-3},z_{i-2},z_{i-1}\},\\
 z_{i-3}&\{z_{i-5},z_{i-4},z_{i-2},z_{i-1}\}.
 \end{array}
\tag{4.3}
\]

Thus the global fusion problem is now finite and sharply local:

* each of the \(462\) fixed-orientation canonical tails has only two
  backward-physical
  off-cycle facets;
* a candidate survives exactly the three forward tests (3.2);
* its two new shadow colors are given by (4.1)--(4.2);
* selecting cross arcs must turn the forty-two cycles into six paths while
  retaining support at least (319) in both shadow ledgers.

No weaker cycle-quotient connectivity statement is enough: the head-order
tests (3.2) and the two support ledgers must be carried by the same selected
cross arcs.
