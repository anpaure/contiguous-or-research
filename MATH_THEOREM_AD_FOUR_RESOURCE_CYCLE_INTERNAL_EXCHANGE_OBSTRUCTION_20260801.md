# Exact four-resource balance cannot absorb a directed cycle internally

Date: 2026-08-01  
Status: exact central-resource/topology theorem and a smallest literal
Boolean obstruction.  It proves that a directed cycle by itself never
supplies a resource-preserving ear into a forest.  It also gives arbitrarily
long induced rainbow Johnson cycles on which every proper-support exact
exchange is trivial.  It does **not** rule out an exchange which also uses
old atoms from path components, and it asserts nothing about OR-word,
residence, shadow, or compiler guards.

## 0. Outcome

An exact four-resource exchange preserves the tail and head degree of every
physical middle vertex separately.  Consequently, if its old support uses
only atoms from directed-cycle components, then after the exchange those
vertices still form a directed cycle cover.  In particular, one directed
cycle cannot be converted into paths using only resources carried by that
cycle, regardless of the support length or the exchange catalogue.

This obstruction is sharp and literal in the ordered Boolean-diamond host.
For every \(m\ge2\) and

\[
                         4\le \ell\le m+2,
\tag{0.1}
\]

there is an induced directed \(\ell\)-cycle whose lower colours, upper
colours, tails and heads are all repetition-free.  If an exact exchange
removes any proper subset of its clockwise atoms and uses precisely the same
four typed resource sets, it must put back the same atoms.  On the full
cycle, the only other phase reverses every edge; its physical graph is the
same cycle.

Thus every fixed bounded-support catalogue of **cycle-internal** exchanges
is avoided: choose \(\ell\) larger than its old-side support bound.  In fact,
even the unrestricted cycle-internal fibre contains no cycle-destroying
move.  Any successful absorber must import a nonzero endpoint boundary from
at least one path component (or relax one of the four resource equalities).
The ternary \(C_6\) actuator does exactly this by using two path components;
the present theorem explains why some exterior path bank is necessary.

## 1. Exact exchanges and their physical boundary

An ordered Boolean diamond is an atom

\[
             e=(L(e),U(e),T(e),H(e)),
\tag{1.1}
\]

where \(L\) has rank \(m-1\), \(U\) has rank \(m+1\), and the tail and
head are the two rank-\(m\) sets strictly between \(L\) and \(U\).  Tail
and head are different typed copies of the middle layer.

Let \(O,N\) be two finite atom sets.  Call \(O\rightsquigarrow N\) an
**exact four-resource exchange** if, as multisets,

\[
\begin{aligned}
 \{L(e):e\in O\}&=\{L(e):e\in N\},\\
 \{U(e):e\in O\}&=\{U(e):e\in N\},\\
 \{T(e):e\in O\}&=\{T(e):e\in N\},\\
 \{H(e):e\in O\}&=\{H(e):e\in N\}.
\end{aligned}
\tag{1.2}
\]

The definition permits arbitrary finite support.  When \(O\) is contained
in a four-resource matching \(M\), the replacement
\(M'=(M-O)\cup N\) is required separately to be a matching; the lemmas
below do not infer that condition from (1.2).

For a physical middle vertex \(X\), write

\[
 d_O^+(X)=|\{e\in O:T(e)=X\}|,
 \qquad
 d_O^-(X)=|\{e\in O:H(e)=X\}|,
\tag{1.3}
\]

and similarly for \(N\).

### Theorem 1.1 (pointwise boundary invariance)

Every exact four-resource exchange satisfies

\[
                  d_O^+(X)=d_N^+(X),\qquad
                  d_O^-(X)=d_N^-(X)
\tag{1.4}
\]

for every physical middle vertex \(X\).  Hence it preserves both the
directed boundary \(d^+-d^-\) and the two degree rows separately.

#### Proof

The third multiset equality in (1.2) gives the first equality of (1.4)
coordinate by coordinate.  The fourth gives the second.  No Boolean
incidence fact is needed. \(\square\)

### Theorem 1.2 (closed-cycle support cannot become a forest)

Let \(M\) be a four-resource matching, and suppose its physical graph has
maximum indegree and outdegree one.  Let \(O\subseteq M\), and suppose every
atom of \(O\) belongs to a directed-cycle component of \(M\).  If
\(O\rightsquigarrow N\) is exact and \(M'=(M-O)\cup N\) is again a
four-resource matching, then every physical vertex in those cycle
components still has indegree one and outdegree one in \(M'\).  The part of
\(M'\) on their vertex union is therefore a nonempty directed cycle cover.

In particular, if \(M\) has exactly one directed cycle and the exchange
uses no atom from a path component, then \(M'\) still has a directed cycle.

#### Proof

Every vertex on a directed-cycle component of \(M\) has global indegree and
outdegree one.  Replacing \(O\) by \(N\) changes its two degrees by

\[
        d_N^+(X)-d_O^+(X),\qquad d_N^-(X)-d_O^-(X),
\]

which are zero by Theorem 1.1.  Exact tail/head equality also prevents a
new edge from using a physical vertex outside the old tail/head resource
bank.  Thus the indicated vertex union remains closed and every one of its
vertices has one incoming and one outgoing edge.  A finite directed graph
with this degree vector is a disjoint union of directed cycles. \(\square\)

### Corollary 1.3 (the necessary exterior ticket)

A resource-preserving exchange which turns the last directed cycle of a
four-resource matching into a linear forest must remove at least one old
atom from a path component.  Equivalently, a true cycle absorber needs an
external tail/head boundary; the cycle's own resource bank has boundary
zero.

This is only a necessary topology condition.  Lower- and upper-colour
equalities can still obstruct every exchange after an exterior path is
supplied.

## 2. Induced rainbow cycles in the Boolean host

Fix an \((m-2)\)-set \(S\) and distinct coordinates

\[
                         x_0,x_1,\ldots,x_{\ell-1}
\tag{2.1}
\]

outside \(S\), where indices are cyclic modulo \(\ell\).  Condition (0.1)
is exactly what is needed to fit \(S\) and these coordinates inside a
\(2m\)-point ground set.  Put

\[
\begin{aligned}
 T_i&=S\cup\{x_i,x_{i+1}\},\\
 L_i&=S\cup\{x_{i+1}\},\\
 U_i&=S\cup\{x_i,x_{i+1},x_{i+2}\},\\
 e_i&=(L_i,U_i,T_i,T_{i+1}).
\end{aligned}
\tag{2.2}
\]

Let \(C_\ell=\{e_0,\ldots,e_{\ell-1}\}\).

### Lemma 2.1 (literal rainbow induced cycle)

The atoms in \(C_\ell\) are legal ordered Boolean diamonds.  Their lower
colours, upper colours, tails and heads are separately pairwise distinct,
so \(C_\ell\) is a four-resource matching.  Its physical graph is the
directed cycle

\[
                         T_0T_1\cdots T_{\ell-1}T_0.
\tag{2.3}
\]

Moreover the Johnson graph induced by \(\{T_i\}\) is precisely the
undirected cycle underlying (2.3).

#### Proof

Consecutive sets in (2.2) have intersection \(L_i\) and union \(U_i\), so
each atom is legal.  The cyclic one-coordinate windows \(L_i-S\),
two-coordinate windows \(T_i-S\), and three-coordinate windows \(U_i-S\)
are pairwise distinct for \(\ell\ge4\).  Thus all four typed rows are
injective.

After deleting the common core \(S\), the middle vertices are the edges of
the ordinary chordless cycle on \(x_0,\ldots,x_{\ell-1}\).  Two such
two-sets meet in one coordinate exactly when the ordinary edges are
consecutive.  Johnson adjacency is therefore exactly cyclic adjacency.
\(\square\)

### Lemma 2.2 (all atoms in the restricted resource box)

Suppose an ordered Boolean diamond \(f\) has

\[
 L(f)\in\{L_i\},\quad U(f)\in\{U_i\},\quad
 T(f),H(f)\in\{T_i\}.
\tag{2.4}
\]

Then for one unique \(i\), either

\[
                  f=(L_i,U_i,T_i,T_{i+1})=e_i
\tag{2.5}
\]

or

\[
                  f=(L_i,U_i,T_{i+1},T_i)=\overline e_i.
\tag{2.6}
\]

#### Proof

The two physical endpoints of a Boolean diamond are Johnson-adjacent.
Lemma 2.1 therefore makes them \(T_i,T_{i+1}\) for a unique cycle edge.
Their intersection and union are forced to be \(L_i,U_i\); only the two
orientations remain. \(\square\)

## 3. Complete exchange classification on the induced cycle

For \(I\subseteq\mathbb Z/\ell\mathbb Z\), put

\[
                         O_I=\{e_i:i\in I\}.
\tag{3.1}
\]

### Theorem 3.1 (rigid cycle fibre)

Let \(O_I\rightsquigarrow N\) be an exact four-resource exchange.  Then:

1. if \(I\ne\mathbb Z/\ell\mathbb Z\), necessarily \(N=O_I\);
2. if \(I=\mathbb Z/\ell\mathbb Z\), then either
   \(N=C_\ell\), or

   \[
                         N=\{\overline e_i:0\le i<\ell\}.
   \tag{3.2}
   \]

Both full phases have the same physical undirected cycle, so neither is a
linear forest.

#### Proof

Exact tail/head equality confines every atom of \(N\) to the middle bank
\(\{T_i\}\), and exact lower/upper equality confines it to
\(\{(L_i,U_i):i\in I\}\).  Lemma 2.2 shows that for each \(i\in I\),
exactly one of \(e_i,\overline e_i\) lies in \(N\).

Let \(r_i=1\) when \(i\in I\) and \(\overline e_i\) is selected, and put
\(r_i=0\) otherwise.  At vertex \(T_i\), equality of the old and new tail
indicators is

\[
 \mathbf1_{i\in I}
  =\mathbf1_{i\in I}(1-r_i)
   +\mathbf1_{i-1\in I}r_{i-1}.
\tag{3.3}
\]

Therefore

\[
                 \mathbf1_{i\in I}r_i
                  =\mathbf1_{i-1\in I}r_{i-1}
\tag{3.4}
\]

for every \(i\).  The quantities in (3.4) are constant around the cycle.
If \(I\) is proper, one is zero and hence all are zero; every selected edge
keeps its old orientation.  If \(I\) is the whole cycle, the common value
is zero or one, giving respectively the old phase or the full reversal.
Head equality gives the same equation.  This proves the classification.
\(\square\)

### Corollary 3.2 (every bounded cycle-internal catalogue is avoidable)

Fix \(s\).  For every \(m\ge\max\{2,s-1\}\), choose

\[
                        \ell=\max\{4,s+1\}\le m+2.
\]

Then the literal four-resource matching \(C_\ell\) has a directed cycle,
but admits no nontrivial exact cycle-internal exchange whose old phase has
at most \(s\) atoms.  Hence no fixed finite catalogue with bounded old-side
support can be a universal cycle-following absorber when its applicability
is required to come from the cycle alone.

The conclusion is stronger on this resource box: even allowing full
support and an unlimited catalogue yields only the full reversal, which
does not improve topology.

## 4. A nonlocal no-go on an asymptotically complete body

The preceding corollary concerns moves generated internally by the cycle.
One can also block exchanges which are allowed to draw arbitrarily many old
atoms from the rest of a near-perfect body.  The required device is a
one-step Johnson moat.

### Theorem 4.1 (moated one-cycle near-factor)

There is a sequence, for all sufficiently large \(m\), of four-resource
matchings \(M_m\) in the ordered Boolean-diamond host with size \(N-o(N)\),
where

\[
                         N={2m\choose m-1},
\tag{4.1}
\]

such that:

1. the physical graph of \(M_m\) is the disjoint union of the literal
   directed \(C_4\) from Section 2 and a linear forest; and
2. **no exact four-resource exchange of any finite support**, even one
   using arbitrary atoms of that forest, can eliminate the protected
   \(C_4\).

Thus every fixed finite catalogue is avoidable on an asymptotically
complete partial four-resource matching.  This statement is stronger than
hex-freeness but is still not an exact outer-perfect factor for \(m>2\).

#### Proof

Let \(V_C=\{T_0,T_1,T_2,T_3\}\), and let

\[
 \mathcal B=V_C\cup N_J(V_C)
\tag{4.2}
\]

be its closed neighbourhood in \(J(2m,m)\).  Since the Johnson degree is
\(m^2\), \(|\mathcal B|=O(m^2)\).  From the host delete

* both typed middle copies \(X_{\rm tail},X_{\rm head}\) for every
  \(X\in\mathcal B\); and
* the four lower and four upper resources of \(C_4\).

Keep the four protected cycle atoms separately.  At most \(O(m^2)\) typed
resources have been deleted.  The maximum host-resource degree is
\(D=m(m+1)\), so this removes at most \(O(m^2D)=O(D^2)\) atoms from the
\(ND\)-atom host.

Fix \(g\).  Apply the valid Delcourt--Postle conflict-free edge-colouring conclusion to
the residual host, together with the configurations for physical cycles of
length at most \(g\).  Deletion cannot increase any host degree, codegree,
configuration degree or mixed codegree.  Hence the residual edges have a
conflict-free colouring with at most

\[
                         D(1+D^{-\alpha_g})
\tag{4.3}
\]

colours.  Its largest colour class \(K\) has size

\[
 |K|\ge {ND-O(D^2)\over D(1+D^{-\alpha_g})}=N-o(N).
\tag{4.4}
\]

Its physical cycles all have length greater than \(g\).  Delete one atom
from each such cycle and take the usual slow diagonal \(g\to\infty\); the
result is a four-resource linear forest \(F\) of size \(N-o(N)\).  It is
resource-disjoint from \(C_4\), and every physical vertex used by \(F\) is
at Johnson distance at least two from \(V_C\).  Put \(M=C_4\cup F\).

Now let \(O\rightsquigarrow N'\) be any exact exchange with \(O\subseteq
M\), and suppose \((M-O)\cup N'\) is a four-resource matching.  Tail/head
equality says that every physical endpoint of \(N'\) is an old endpoint
from \(O\).  There is no Johnson edge between \(V_C\) and the physical
vertex bank of \(F\), by the moat.  Therefore \(N'\) splits into a cycle
part and a forest part.

This splitting also respects lower and upper resources.  If a rank-
\((m-1)\) set \(L_i\) of the protected cycle occurred in a forest-part new
atom, both of that atom's middle endpoints would contain \(L_i\), and hence
would be Johnson-neighbours of the protected endpoints of edge \(i\).  They
would lie in \(\mathcal B\), a contradiction.  The same argument applies to
an upper colour \(U_i\): all of its rank-\(m\) facets are pairwise
Johnson-adjacent and hence lie in \(\mathcal B\).  Thus the cycle part of
the exchange has, on each of the lower, upper, tail and head shores,
exactly the resource subbank contributed by \(O\cap C_4\); that subbank may
be proper.

Theorem 3.1 applies to that restricted phase.  It is either unchanged, or
the entire protected cycle is reversed.  In either case a physical
directed \(C_4\) remains.  This proves item 2. \(\square\)

### Scope of Theorem 4.1

The theorem gives a literal Boolean, nonlocal, catalogue-independent no-go
on an \(N-o(N)\) body.  It does **not** construct an exact outer-complete
four-resource factor with the moat.  Such a completion is a separate
integral problem; no exact-factor conclusion for general \(m\) is inferred
from the Delcourt--Postle colour class.

## 5. Minimality and the exact \(m=2\) factor

The four-cycle \(C_4\) is the smallest possible directed cycle in a
four-resource matching of ordered Boolean diamonds.

A directed two-cycle uses both orientations of one Johnson edge and repeats
its lower and upper colours.  A triangle in a Johnson graph is of one of
the following two forms:

* its three middle sets have one common rank-\((m-1)\) intersection; or
* its three middle sets lie in one common rank-\((m+1)\) union.

In the first case all three physical edges repeat one lower colour; in the
second they repeat one upper colour.  Neither is a four-resource matching.
Lemma 2.1 supplies \(C_4\), so the bound is sharp.

At \(m=2\), take \(S=\varnothing\) and use all four ground coordinates as
\(x_0,x_1,x_2,x_3\).  Then the four \(L_i\) are **all** rank-one sets and
the four \(U_i\) are **all** rank-three sets.  Hence \(C_4\) is an exact
outer-complete four-resource factor, not merely a partial matching.
Theorem 3.1 proves that this smallest full factor has no cycle-destroying
exact exchange of any support.  For \(m>2\), the isolated \(C_\ell\) of
Section 2 is only a partial matching unless a separate completion is
supplied.

Thus \(C_4\) is also the smallest literal certificate that directed-cycle
existence does not imply a cycle-destroying exact exchange.

## 6. Exact implication and remaining positive target

The implications established here are

\[
\begin{array}{c}
 \text{exact lower/upper/tail/head balance}\\
 \Downarrow\\
 \text{pointwise physical indegree and outdegree balance}\\
 \Downarrow\\
 \text{cycle-only old support remains a cycle cover}.
\end{array}
\tag{6.1}
\]

They refute the proposed statement that the directed cycle itself should
generate a bounded or \(O(\ell)\)-support resource-preserving ear.  The
correct positive object must be **endpoint-relative**:

> supply at least one old path component (or a path segment carrying a
> genuine exterior source/sink ticket), then find a balanced alternating
> circuit whose new phase merges the cycle into that endpoint-bearing bank.

The existing ternary \(C_6\) theorem is one sufficient realization, with
one cycle and two path components.  The exact lower bound proved here is
only one path component; whether a one-cycle/one-path Boolean packet exists
is a separate exchange-classification question.

Finally, all statements in this note are central.  They do not preserve or
even mention residence, deeper lower/upper shadows, prefix/suffix OR decks,
star-hidden fan traces, common cap, or literal chronology.  Any positive
endpoint-relative packet must pass those OR-word guards independently.

## 7. Finite replay

Run

```text
python3 scratch/audit_ad_four_resource_cycle_internal_obstruction_20260801.py
```

The dependency-free replay checks \(4\le\ell\le10\), every subset of the
clockwise phase and every orientation of its selected edges.  It finds
exactly \(2^\ell+1\) feasible states: the identity on each of the
\(2^\ell\) subsets, plus the full reversal.  It also checks that the
\(m=2,\ell=4\) lower and upper banks are their complete layers.  The replay
reports

```text
PASS_AD_FOUR_RESOURCE_CYCLE_INTERNAL_OBSTRUCTION
payload_sha256=dad12307db4a0b61d024bc463edf24c0c45d47e1889d17c8591749c53082798c
```

The byte-for-byte output is frozen at
`scratch/ad_four_resource_cycle_internal_obstruction_20260801.audit.json`.
An independent proof audit, including the restricted resource fibre, the
Delcourt--Postle count and both outer-shore moat rows, is in
`MATH_AUDIT_AD_FOUR_RESOURCE_CYCLE_INTERNAL_EXCHANGE_OBSTRUCTION_20260801.md`.
