# Catalan two-rail endpoint-complement braids

Date: 2026-07-31  
Status: exact lower-palette classification, exact protected conditional
compiler theorem, and authenticated K15/K16 calibration.  The uniform
endpoint-complement construction remains open.

## 0. Verdict

Let \(m\ge2\) and

\[
 M=\binom{2m}{m},\qquad
 N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m.
\tag{0.1}
\]

After adjoining a new coordinate \(z\), the child middle layer splits into
an unmarked rail of \(N\) rank-\((m+1)\) sets and a marked rail of \(M\)
copies of the rank-\(m\) sets.  Exact lower-\(q_1\) coverage forces, rather
than merely suggests,

\[
 \boxed{
 e_{UU}=N-K,\qquad e_{CC}=N,\qquad e_{UC}=2K.}
\tag{0.2}
\]

The correct constructive object is therefore a pair of \(K\)-path forests.
The marked forest has \(N\) internal edges carrying the entire tagged lower
palette.  The unmarked forest has \(N-K\) distinct internal colours.  Its
missing \(2K\) colours must be exactly the \(2K\) **marked endpoint
labels**.  A containment matching of the endpoint occurrences then restores
degree two and supplies those missing colours.  Connectivity is the
one-cycle condition on the contracted fragment graph.

This endpoint-complement identity is the exact general form of the proposed
ledger “cut \(K\) duplicate marked edges, cut \(K\) unmarked edges, and add
\(2K\) containment seams.”  In the duplicate-floor specialization it
becomes a finite system of colour rows, endpoint rows, containment Hall, and
subtour inequalities.  The hosted cap-two switch of
`MATH_THEOREM_CATALAN_TWO_RAIL_RAINBOW_SWITCH_REDUCTION_20260731.md` is one
sufficient local realization, not a normal form for every solution.

The result replaces arbitrary Catalan component packaging by a
Catalan-sized paired-forest problem.  It does not make the upper tower,
residence, boundary port, or common cap automatic.  Under the exact
protected conditions in Section 6 it gives a length-\(B(2m+1)\) word and
hence equality.

## 1. Rail colours

Let \(\Omega=[2m]\) and introduce \(z\notin\Omega\).  Write

\[
 \mathcal U=\binom{\Omega}{m+1},\qquad
 \mathcal C=z+\binom{\Omega}{m}.
\tag{1.1}
\]

Thus \(|\mathcal U|=N\) and \(|\mathcal C|=M\).  For Johnson-adjacent
vertices the lower and upper colours are as follows.

* An internal unmarked edge \(UV\) has lower colour
  \(U\cap V\in\binom\Omega m\) and upper colour
  \(U\cup V\in\binom\Omega{m+2}\).
* An internal marked edge \((z+C)(z+D)\) has lower colour
  \(z+(C\cap D)\), indexed by \(\binom\Omega{m-1}\), and upper colour
  \(z+(C\cup D)\), indexed by \(\binom\Omega{m+1}\).
* A cross edge is legal precisely in the form

  \[
                    U\;--\;(z+C),\qquad C\subset U.
  \tag{1.2}
  \]

  Its lower colour is \(C\), and its upper colour is \(z+U\).

The two lower signatures are disjoint.  There are \(M\) untagged lower
colours and \(N\) tagged lower colours.

## 2. The Catalan crossing count is forced

### Theorem 2.1 (forced crossing count)

Let \(H\) be a spanning Johnson degree-two factor on
\(\mathcal U\mathbin{\dot\cup}\mathcal C\).  If its lower colours cover the
complete child rank-\(m\) layer, then every lower colour occurs exactly once
and (0.2) holds.

#### Proof

Let \(c\) be the number of cross edges.  Degree sums on the two rails give

\[
 2e_{UU}+c=2N,\qquad 2e_{CC}+c=2M.
\tag{2.1}
\]

Hence \(c=2R\) is even and

\[
                  e_{UU}=N-R,\qquad e_{CC}=M-R.
\tag{2.2}
\]

Only marked internal edges supply the \(N\) tagged lower colours, so
\(M-R\ge N\), or \(R\le K\).  Untagged internal and cross edges together
supply the \(M\) untagged lower colours, so

\[
                 (N-R)+2R=N+R\ge M,
\]

or \(R\ge K\).  Thus \(R=K\), proving (0.2).  The factor has
\(M+N\) edges, exactly the number of lower colours.  Coverage therefore
forces multiplicity one for every colour. \(\square\)

If \(H\) is one cycle, its cyclic \(z\)-trace consequently has exactly
\(K\) positive marked runs and \(K\) zero unmarked runs.  A disconnected
factor can additionally have a pure-rail component, so the run assertion is
made only for a connected factor (or componentwise after excluding such a
component).

The arithmetic identities

\[
                         M=(m+1)K,\qquad N=mK
\tag{2.3}
\]

will also be useful.  In a \(K\)-path decomposition the mean marked and
unmarked fragment lengths are therefore \(m+1\) and \(m\), respectively.

## 3. The endpoint-complement theorem

Let \(F_C\) be a spanning path forest on the underlying
\(\binom\Omega m\) marked states, and let \(F_U\) be a spanning path forest
on \(\mathcal U\).  Endpoints below are **occurrences**.  We impose:

* **EC1.** \(F_C\) has exactly \(K\) nontrivial paths and its \(N\)
  internal intersection colours enumerate \(\binom\Omega{m-1}\) exactly
  once.
* **EC2.** \(F_U\) has exactly \(K\) paths and its \(N-K\) internal
  intersection colours form a set

  \[
                         L\subseteq\binom\Omega m.
  \tag{3.1}
  \]

* **EC3.** The \(2K\) endpoint labels of \(F_C\) are distinct and equal
  exactly

  \[
                      S=\binom\Omega m\setminus L.
  \tag{3.2}
  \]

Let \(P_C\) and \(P_U\) be the two \(2K\)-sets of endpoint occurrences.
Form the containment graph

\[
 p_C\sim p_U
 \quad\Longleftrightarrow\quad
 C(p_C)\subset U(p_U).
\tag{3.3}
\]

### Theorem 3.1 (Catalan endpoint-complement braid)

Under EC1--EC3, any perfect matching \(\mu:P_C\to P_U\) in (3.3) adds
\(2K\) legal containment seams and produces a spanning degree-two child
factor with every lower-\(q_1\) colour exactly once.  It is one Hamilton
cycle if and only if, after contracting the \(K\) paths on each rail, the
resulting two-regular bipartite multigraph is one alternating
\(2K\)-cycle.

#### Proof

Every path endpoint has internal degree one, and every other vertex has
internal degree two.  The perfect matching adds one edge at each endpoint,
so the union is degree two.  EC1 supplies every tagged lower colour once.
EC2 supplies exactly \(L\) internally on the unmarked side.  A cross seam
has lower colour equal to its marked endpoint label, and EC3 says that these
labels are exactly the complementary set \(S\), once each.  Hence the three
disjoint banks are

\[
 z+\binom\Omega{m-1},\qquad L,\qquad S,
\]

which form the entire child lower palette.

Contracting the rail paths preserves connected components and turns every
contracted vertex into degree two.  Such a bipartite graph is connected
exactly when it is one alternating cycle. \(\square\)

### Theorem 3.2 (exact converse inside the forest fibre)

Suppose a lower-rainbow spanning Johnson degree-two child factor has \(2K\) cross
edges and deleting them leaves path forests on both rails.  Then the two
forests satisfy EC1--EC3, and the cross edges are a containment matching as
in Theorem 3.1.

#### Proof

Theorem 2.1 gives \(N\) marked and \(N-K\) unmarked internal edges.
Deleting every cross edge leaves total endpoint degree \(2K\) on each rail,
so a forest on each spanning rail has exactly \(K\) path components.
Lower rainbowness forces the marked internal colours to be the entire tagged
palette and the unmarked internal colours to be a set \(L\) of size
\(N-K\).  The cross colours are their complement \(S\).  Each cross colour
is its marked endpoint label, so those \(2K\) labels are distinct and equal
\(S\).  In particular, no marked path can be an isolated vertex: its two
endpoint occurrences would have the same label and hence create the same
cross colour twice.  Thus EC1's paths are nontrivial.  Johnson legality gives
containment. \(\square\)

### Corollary 3.3 (linear form and the boundary colour)

Choose a marked endpoint of label \(\rho\in S\) and one unmarked endpoint
as the two word boundaries.  Match the remaining \(2K-1\) ports by
containment.  If the union with the fixed within-path endpoint pairings is
connected and acyclic, the result is one spanning path.  Its lower palette
is complete except for the single colour \(\rho\).

The edge count is

\[
             N+(N-K)+(2K-1)=M+N-1.
\tag{3.4}
\]

Thus \(\rho\) is not an abstract bookkeeping hole: it must have a literal
compatible boundary/compiler cell in any zero-defect word.

## 4. The duplicate-floor cycle ledger

The user's proposed cut construction is an exact specialization of
Theorem 3.1.  Let \(G_U\) and \(G_C\) be spanning simple 2-factors on the
two rails.  Assume:

* the \(N\) lower intersection colours of \(G_U\) are distinct, with unused
  facet set

  \[
      \mathcal E=\binom\Omega m\setminus\lambda_U(E(G_U)),
      \qquad |\mathcal E|=K;
  \tag{4.1}
  \]
* the lower intersection colours of \(G_C\) have the floor profile

  \[
                             1^{N-K}2^K.
  \tag{4.2}
  \]

Choose \(K\) cut edges \(D_U\subset E(G_U)\) and
\(D_C\subset E(G_C)\), and write \(\partial D_C\) for the multiset of their
\(2K\) endpoint labels.

### Corollary 4.1 (exact duplicate-cut criterion)

Deleting \(D_U,D_C\) and adding \(2K\) containment seams gives a
lower-rainbow Hamilton cycle if and only if all of the following hold.

1. \(D_C\) contains exactly one occurrence of every doubled marked
   intersection colour.
2. The endpoint/facet equation holds as multisets:

   \[
       \boxed{
       \partial D_C
        =\mathcal E\mathbin{\dot\cup}\lambda_U(D_U).}
   \tag{4.3}
   \]

3. Every source cycle of \(G_U\) and \(G_C\) is cut, so each deleted rail
   is a union of exactly \(K\) paths.
4. The marked port occurrences have a perfect containment matching into the
   unmarked port occurrences.
5. Its contracted fragment graph is one alternating cycle.

#### Proof

Condition 1 makes the retained marked edges carry every tagged colour once.
The retained unmarked colours are

\[
             \lambda_U(E(G_U))\setminus\lambda_U(D_U).
\]

Every new seam colour is its marked endpoint label, so (4.3) says exactly
that the seam colours are the disjoint union of the \(K\) lost unmarked
colours and the \(K\) previously unused facets.  Conditions 3--5 are
precisely the hypotheses which turn the two rail path families into one
cycle.  This proves sufficiency by Theorem 3.1.

Conversely, exact tagged coverage forces condition 1 under the floor
profile.  Exact untagged coverage forces (4.3), because the seam labels are
the marked cut endpoints independently of how the ports are paired.
Hamiltonicity forces 3--5. \(\square\)

Since the right side of (4.3) is a set, the selected marked cuts are
vertex-disjoint: \(D_C\) is a matching.  This is a genuine extra condition.
The floor profile controls cut **colours**, not their \(2K\) endpoint
facets.

Already \(m=2\) separates these conditions.  On \([4]\), take the
unmarked cycle

\[
 123,124,134,234,123,
\]

whose lower colours are \(12,14,34,23\) and whose unused facets are
\(\{13,24\}\).  Take the marked underlying cycle

\[
 12,13,23,24,34,14,12.
\]

Its intersection colours have the floor profile with duplicated colours
\(1,4\).  Cutting the edges \(14\!-\!12\) and \(34\!-\!14\) removes one occurrence
of each duplicate, but the endpoint multiset is
\(\{12,14,14,34\}\), so (4.3) fails for every unmarked cut bank.  Thus even
an exact one-per-duplicate choice need not be a usable braid cut.

The weakest general hypothesis is not (4.2), but simply that the retained
marked forest satisfies EC1.  In particular, the revised hosted split
switch can discard any lower-label multiplicities on its removed edges.
The cap-two construction supplies an upper-**union** floor profile; it does
not automatically supply (4.2).

### 4.2 Exact finite rows

Under the floor specialization, introduce cut variables \(x_e\) for marked
edges and \(y_a\) for unmarked edges.  For every doubled marked colour
\(c\), impose

\[
             \sum_{e:\lambda_C(e)=c}x_e=1,
\tag{4.4}
\]

and set \(x_e=0\) on singleton classes.  Put \(\sum_a y_a=K\).  Equation
(4.3) is exactly the family

\[
 \boxed{
 \sum_{e\ni X}x_e
   =\mathbf1_{\mathcal E}(X)
     +\sum_{a:\lambda_U(a)=X}y_a
 \quad\left(X\in\binom\Omega m\right).}
\tag{4.5}
\]

Because \(\lambda_U\) is injective, the right side is zero or one; these
rows also force the marked cuts to be a matching.  After the cuts are fixed,
containment is an ordinary Hall condition on **port occurrences**:

\[
                       |N_{\subseteq}(Q)|\ge |Q|
                       \qquad(Q\subseteq P_C).
\tag{4.6}
\]

Hall gives a degree-two factor, not one cycle.  Connectivity requires the
usual subtour cuts on the contracted fragments.  Thus neither equal port
counts nor ordinary containment Hall proves the braid.

## 5. The hosted local switch is a strict subfamily

The cap-two construction starts from a saturating cycle

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0
\]

and injects each unused facet \(X\in\mathcal E\) into a distinct host
\(U_i\), between \(C_i\) and \(C_{i+1}\).  It then retains one of
\(XC_i,XC_{i+1}\), cuts the other \(XJ_X\), cuts the unmarked edge of
colour \(J_X\), and installs the two sides of one alternating square.

In this class

\[
         \partial D_C=\mathcal E\mathbin{\dot\cup}\{J_X:X\in\mathcal E\},
\tag{5.1}
\]

so the endpoint equation is automatic once the \(J_X\)'s are distinct.
The remaining marked internal colours must form the exact tagged palette.
For fixed host injection \(\phi\), first reject if the \(N-K\) fixed
unmatched colours are not distinct, and let the residual palette be their
\(K\)-element complement.  The one-of-two choice is then exactly 2-SAT:
forbid an option whose retained colour lies outside that residual palette,
and forbid every pair of options which share either a retained colour or a
cut endpoint \(J_X\).  Distinct \(K\) retained colours inside a residual
\(K\)-set cover that set.

This local construction is strictly narrower than Theorem 3.1.  A general
marked completion cut may join two endpoints from \(\mathcal E\), or two
already-used endpoint labels, and need not be one of the two host-block
edges of an unused facet.

## 6. Upper shadows, residence, and the zero-defect theorem

The lower ledger is not the whole compiler.  In this section let
\(d=d(2m+1)\) be the child deadline depth.

### 6.1 Exact immediate-upper rows

If the forests arise by cuts \(D_U,D_C\), then no-\(z\) upper-\(q_1\)
coverage is exactly

\[
 \sum_{a:\,\upsilon_U(a)=Q}(1-y_a)\ge1
 \qquad\left(Q\in\binom\Omega{m+2}\right).
\tag{6.1}
\]

A cross seam always contains \(z\), so it can never repair a failure of
(6.1).  For a tagged target \(z+U\), the exact load is

\[
 \sum_{e:\,\upsilon_C(e)=U}(1-x_e)+\deg_{D_U}(U),
\tag{6.2}
\]

because every unmarked cut-port occurrence at \(U\) receives one cross
seam of upper colour \(z+U\).  Tagged upper-\(q_1\) coverage is equivalent
to (6.2) being at least one for every \(U\).

### 6.2 All-depth cut kernel

For a target avoiding \(z\), every witness must lie wholly inside one
retained unmarked fragment.  Equivalently, some old witness span avoids the
entire cut set \(D_U\).  Checking the cuts separately is insufficient.

For a target containing \(z\), a witness is either internal to a retained
marked fragment or is one of the literal suffix--whole-fragments--prefix
intervals of the final order.  This is the exact two-rail specialization of
the global protected cut-kernel theorem.

### 6.3 Residence

The positive \(z\)-runs are the marked fragments and the zero \(z\)-runs
are the unmarked fragments.  Thus depth-\(d\) lower residence of \(z\)
requires marked lengths at least \(d+1\), while the dual upper condition
requires the analogous unmarked bound.  Equation (2.3) shows that these
requirements have no mean-length obstruction when \(d+1\le m\), but mean
lengths do not supply the necessary spacing.

For all coordinates, a sufficient zero-loss condition is the reset product:
every fragment has length at least \(d+1\), no internal positive run has
length at most \(d\), and no bounded positive run meeting one allowed seam
inside any two-fragment product has length at most \(d\).  Then every run
crossing two or more seams contains a whole fragment, and

\[
                              \Psi_d=0.
\tag{6.3}
\]

Otherwise one must prove the exact positional inequality

\[
                    \Psi_d\le\operatorname{slack}(2m+1).
\tag{6.4}
\]

The number \(2K\) of seams is not a scalar cost.  Under (6.3) all of them
have collective staircase loss zero.  This is how the architecture can in
principle survive slack-zero or slack-below-\(K/3\) dimensions.

### Theorem 6.1 (protected endpoint-complement compiler)

Assume a connected endpoint-complement braid of Theorem 3.1.  Open one
cross seam of colour \(\rho\).  Suppose:

1. every upper target satisfies the all-depth cut kernel above;
2. the opened chronology is chain aligned and satisfies (6.4);
3. \(\rho\) has a literal compatible boundary/compiler port; and
4. after installing every protected pin, the residual lower atlas has one
   integral common-cap assignment.

Then the braid compiles to a universal word of length \(B(2m+1)\), and

\[
                         \boxed{\nu(2m+1)=B(2m+1).}
\tag{6.5}
\]

#### Proof

Theorem 3.1 and the opening give one spanning middle path with exactly one
missing lower-\(q_1\) colour \(\rho\).  The boundary port realizes that
colour.  The cut kernel gives all upper targets; chain alignment transfers
their owner windows to physical intervals.  Inequality (6.4) supplies a
legal length-\(B\) staircase, and the common cap realizes all residual
lower targets in the same physical letters.  Universality follows.  The
general lower bound gives equality. \(\square\)

The abstract common-cap hypothesis may be replaced by any proved sufficient
criterion, such as the trace-guarded convex interval-Hall condition or the
laminar-Rado criterion.  Ordinary marginal Hall is not sufficient.

## 7. Authenticated finite anatomy

### 7.1 K15

For \(m=7\),

\[
                    (M,N,K)=(3432,3003,429),
\tag{7.1}
\]

so (0.2) is

\[
             (e_{UU},e_{CC},e_{UC})=(2574,3003,858).
\tag{7.2}
\]

The authenticated resident all-depth-complete K15 factor with physical
cycle lengths \(6390,45\) has exactly (7.2) for every choice of \(z\).  On
deleting the cross edges it has \(429\) paths on each rail; the marked
internal palette is exact, the unmarked internal palette and marked endpoint
labels are complementary, and every cross edge is a literal containment.
Thus it realizes EC1--EC3 and the containment matching, together with
minimum run four and all-depth upper completeness.

It is not connected after fragment contraction: the two alternating cycles
have lengths \(852=2\cdot426\) and \(6=2\cdot3\), so the endpoint-pairing
product has cycle type \((426)(3)\).  Moreover its hosted-square compatibility
graph on the \(858\) cross seams has \(11\) isolated vertices for every
choice of \(z\).  Therefore this factor is a rigorous non-instance of the
narrow hosted local-switch theorem, even though it is an exact positive
instance of the broader endpoint-complement ledger short of one-cycle
monodromy.

### 7.2 K16 as a possible K17 source

For \(m=8\),

\[
                 (M,N,K)=(12870,11440,1430),
\tag{7.3}
\]

and the predicted K17 counts are

\[
             (e_{UU},e_{CC},e_{UC})=(10010,11440,2860).
\tag{7.4}
\]

The authenticated K16 endpoint-reroot carrier is a Johnson path, not the
needed cap-two cyclic marked rail.  Its adjacent load profiles are

\[
\begin{array}{c|c}
\text{rank-seven intersections}&1^{10066}2^{1319}3^{55},\\
\text{rank-nine unions}&1^{10111}2^{1229}3^{100}.
\end{array}
\tag{7.5}
\]

Its endpoints are not Johnson-adjacent.  In particular, a one-edge closure
cannot remove the rank-nine triple loads and cannot give the cap-two
upper-union floor.  The rank-seven triple loads are not themselves an
obstruction to the weaker retained-forest theorem; they only refute the
older lower-floor shortcut.  Thus the exact K16 certificate is not the
required K17 input, but it does not obstruct a different cap-two rail.

K16 also confirms that the final compiler clause is load-bearing: its exact
optimal word required endpoint rerooting, singleton retiming, and one
maximal-common-cap assignment.  None follows from (0.2).

The independent replay and full hashes are recorded in
`MATH_AUDIT_K_CATALAN_TWO_RAIL_K15_K16_ANATOMY_20260731.md`.

## 8. Exact remaining all-\(m\) gate

The specialized odd-lift theorem to prove is now the following.

> **Protected Catalan endpoint-complement braid.**  For every \(m\),
> construct the two \(K\)-path forests EC1--EC3 and a containment port
> matching with one-cycle (or one-path) monodromy, while preserving the
> complete upper cut kernel, satisfying the exact residence/staircase
> inequality, exposing the boundary colour at a compatible port, and
> retaining an integral common cap.

The duplicate-floor equations (4.4)--(4.6) are a sharp sufficient finite
form when simultaneous floor rails exist.  The hosted 2-SAT switch is a
smaller sufficient subfamily.  The K15 anatomy proves that the broader
endpoint-complement object is the correct scale and that the hosted
subfamily is too narrow.

This is not an arbitrary component-packaging theorem.  It is a
Catalan-sized two-rail seam matching with an exact endpoint-complement
equation.  Conversely it is not yet an all-\(m\) construction: containment
Hall, monodromy, protected upper witnesses, the run product, and the common
cap remain simultaneous conditions.
