# MNW odd-graph joining flips: the exact local seam theorem

Date: 2026-07-28

Status: pure-mathematical local theorem.  The residence criterion below is
necessary and sufficient under the stated separation hypothesis.  It does
not assert that the MNW charts satisfy the resulting inequalities.

## 1. Odd-graph colours and residence

Let \(\Omega\) have size \(2m+1\), and let

\[
                         O_m=KG(\Omega,m).
\]

For an edge \(XY\) of \(O_m\), write

\[
                \chi(XY)=\text{the unique element of }
                         \Omega\setminus(X\cup Y).       \tag{1.1}
\]

If an oriented cycle has edge-colour word

\[
                         z=(z_j)_{j\in\mathbb Z/N\mathbb Z},
\]

then depth-three cyclic residence is

\[
 z_j\ne z_{j+1},\qquad z_j\ne z_{j+3},\qquad
 z_j\ne z_{j+5}\quad\text{for every }j.                 \tag{1.2}
\]

The distance-one clause is automatic in every simple two-factor.  Indeed,
for fixed \(X\) the neighbour on an edge of colour \(c\) is uniquely

\[
                         X^c\setminus\{c\}.              \tag{1.3}
\]

Thus two distinct edges incident with \(X\) have distinct colours.  The
distance-three and distance-five clauses are not consequences of ordinary
two-factor legality.

Condition (1.2) is invariant under reversing a cycle: equality at forward
distance \(d\) after reversal is equality at backward distance \(d\) before
reversal, and the starting index ranges cyclically over the entire word.

## 2. Alternating flips and oriented collars

Let \(F\) be a simple two-factor of \(O_m\).  Let \(Z\) be an
\(F\)-alternating even cycle, and put

\[
 E_-:=E(Z)\cap E(F),\qquad E_+:=E(Z)\setminus E(F),
 \qquad F':=F\mathbin\triangle Z.                       \tag{2.1}
\]

Then \(E_-\) and \(E_+\) are matchings on the same set of ports and \(F'\)
is again a two-factor.  Delete \(E_-\) and orient every retained path in the
direction in which it occurs in \(F'\).  At a new edge \(f\in E_+\), write

\[
                         b=\chi(f).                      \tag{2.2}
\]

Let the last retained colours before \(f\), in reverse chronological order,
be

\[
                         L_1,L_2,L_3,L_4,L_5,            \tag{2.3}
\]

and let the first retained colours after \(f\) be

\[
                         R_1,R_2,R_3,R_4,R_5.            \tag{2.4}
\]

Thus the local colour word is

\[
 \cdots,L_5,L_4,L_3,L_2,L_1,b,R_1,R_2,R_3,R_4,R_5,\cdots .
                                                               \tag{2.5}
\]

We use the following exact separation hypothesis.

> **Five-edge seam separation.**  Every retained path component of
> \(F-E_-\) which occurs between two consecutive edges of \(E_+\) in
> \(F'\) has at least five edges.                              \(\tag{2.6}\)

Equivalently, in the edge-colour word of every cycle of \(F'\), two
consecutive occurrences of edges in \(E_+\) are at cyclic positional
distance at least six.  Hence a forward interval joining two edge positions
at distance at most five contains at most one new edge.

For an MNW joining step which cuts each participating current component
once, (2.6) is automatic for \(m\ge3\): a component has length at least
\(2m+1\), and deleting one edge leaves at least \(2m\ge6\) retained edges.
This observation proves separation only.  It proves none of the colour
inequalities below.

## 3. Necessary and sufficient residence criterion

### Theorem 3.1 (distance-three/five local seam theorem)

Assume that \(F\) satisfies (1.2) and that (2.6) holds.  Then \(F'\)
satisfies (1.2) if and only if, at every inserted edge with collar (2.5),
all ten of the following positional inequalities hold:

\[
\boxed{
\begin{array}{rclcrcl}
b&\ne&L_3,&&b&\ne&R_3,\\
L_1&\ne&R_2,&&L_2&\ne&R_1,                    \tag{3.1}\\[1mm]
b&\ne&L_5,&&b&\ne&R_5,\\
L_1&\ne&R_4,&&L_2&\ne&R_3,\\
L_3&\ne&R_2,&&L_4&\ne&R_1.                    \tag{3.2}
\end{array}}
\]

Here (3.1) is exactly distance-three avoidance and (3.2) is exactly
distance-five avoidance.  The entries are occurrences, not merely elements
of two unordered collar sets; in a degenerate short cyclic component some
displayed occurrences can coincide, and no cancellation of clauses is
permitted without checking those positions.

#### Proof

Fix \(d\in\{3,5\}\) and an ordered pair of edge occurrences of \(F'\) at
forward cyclic distance \(d\).  By (2.6), their forward interval contains at
most one edge of \(E_+\).

If it contains no edge of \(E_+\), both occurrences lie in one retained path
in their old consecutive order or its reverse.  Their colours were already
unequal in \(F\), by (1.2) and reversal invariance.

Suppose that the interval contains the new edge of colour \(b\) in (2.5).
There are exactly three possibilities.

1. The new edge is the second endpoint.  The pair is \((L_d,b)\).
2. The new edge is the first endpoint.  The pair is \((b,R_d)\).
3. The new edge is internal.  For a unique \(u\in\{1,\ldots,d-1\}\), the
   pair is

   \[
                             (L_u,R_{d-u}).              \tag{3.3}
   \]

Therefore distance-\(d\) avoidance is equivalent to

\[
 b\ne L_d,\quad b\ne R_d,\quad
 L_u\ne R_{d-u}\quad(1\le u\le d-1).                  \tag{3.4}
\]

For \(d=3\), formula (3.4) gives the four clauses (3.1).  For \(d=5\), it
gives the six clauses (3.2).  Every possible new equality has been listed,
and every listed equality is itself a forbidden return.  This proves both
necessity and sufficiency.  The distance-one clauses are automatic by
(1.3).  \(\square\)

### Corollary 3.2 (what the old edge colours do and do not prove)

Suppose, in the one-cut-per-component case, that the removed old edge of a
participating cycle has colour \(a\), and deleting it leaves the oriented
retained word \(P=(p_1,\ldots,p_\ell)\).  Around the old cut the word was

\[
          \cdots,p_{\ell-1},p_\ell,a,p_1,p_2,\cdots .  \tag{3.5}
\]

Old residence proves (3.4) with

\[
 b,L_u,R_v
 \quad\text{replaced by}\quad
 a,p_{\ell-u+1},p_v.                                  \tag{3.6}
\]

After joining, the right collar generally belongs to another retained path
and \(a\) is replaced by a new colour \(b\).  Consequently none of the ten
new clauses follows merely from the fact that every old component had a
permutation colour word.  Ordinary factor legality gives only

\[
                         b\ne L_1,qquad b\ne R_1,       \tag{3.7}
\]

which are the already-automatic adjacent-colour clauses.

### Corollary 3.3 (failure of separation)

If (2.6) fails, (3.1)--(3.2) at individual seams need not be sufficient: a
distance-three or distance-five interval can cross two inserted edges.  The
exact replacement is to inspect every pair \((z_j,z_{j+3})\) and
\((z_j,z_{j+5})\) whose forward interval contains at least one edge of
\(E_+\).  Pairs whose interval contains no new edge remain inherited and
safe.  Thus the obstruction stays local to the union of five-edge collars,
but it is no longer a product of independent one-seam tests.

## 4. Exact change of every turn colour

For a vertex \(X\) on a simple odd-graph cycle, let its two neighbours be
\(Y_-\) and \(Y_+\), and let the incident edge colours be

\[
                  c_-:=\chi(XY_-),\qquad c_+:=\chi(XY_+).
\]

The rank-\((m-1)\) turn colour at \(X\) is

\[
 \begin{aligned}
 \operatorname{Turn}(X)
   &=Y_-\cap Y_+\\
   &=\bigl(X^c\setminus\{c_-\}\bigr)
       \cap\bigl(X^c\setminus\{c_+\}\bigr)\\
   &=X^c\setminus\{c_-,c_+\}.                         \tag{4.1}
 \end{aligned}
\]

### Theorem 4.1 (endpoint one-swap law)

Let \(X\) be a port of the alternating flip.  Let

\[
 r_X=\text{the colour of the retained factor edge at }X,
\]

\[
 a_X=\text{the colour of the removed edge at }X,
 \qquad
 b_X=\text{the colour of the inserted edge at }X.       \tag{4.2}
\]

Then

\[
 \boxed{
 \begin{aligned}
 \operatorname{Turn}_F(X)&=X^c\setminus\{r_X,a_X\},\\
 \operatorname{Turn}_{F'}(X)&=X^c\setminus\{r_X,b_X\}\\
   &=\bigl(\operatorname{Turn}_F(X)\setminus\{b_X\}\bigr)
       \cup\{a_X\}.                                   \tag{4.3}
 \end{aligned}}
\]

Every vertex outside the ports has unchanged turn colour.

#### Proof

Equation (4.1) gives the first two lines of (4.3).  At a port, the retained,
removed, and inserted edges are three distinct edges incident with \(X\).
By (1.3), their colours \(r_X,a_X,b_X\) are pairwise distinct.  Hence
\(b_X\) belongs to \(X^c\setminus\{r_X,a_X\}\), whereas \(a_X\) belongs
to \(X^c\setminus\{r_X,b_X\}\), proving the one-out/one-in formula.  No
incident edge changes away from a port.  \(\square\)

If the alternating cycle removes \(t\) old factor edges, it has \(2t\)
ports.  Every nontrivial flip therefore changes exactly \(2t\) turn-colour
occurrences, each by one Johnson exchange.  As a signed multiset identity,

\[
 \boxed{
 \mathcal T(F')-\mathcal T(F)
   =\sum_{X\text{ a port}}
       \left(
       [X^c\setminus\{r_X,b_X\}]
       -[X^c\setminus\{r_X,a_X\}]
       \right).}                                      \tag{4.4}
\]

Different ports can contribute equal turn sets, so (4.4), rather than the
uncancelled count \(2t\), is the exact global support ledger.

In the path notation (2.5), at the tail of the new seam one has
\(r_X=L_1\), and at its head one has \(r_X=R_1\).  Thus (4.3) gives the
changed turn at both ends directly from the same collar used in Theorem
3.1.

## 5. Consequences for the MNW joining argument

The canonical MSW odd cycles have omitted-edge colour words which are
permutations of \(\Omega\).  They therefore satisfy (1.2) before joining.
For a flip which cuts each current component once, the separation needed in
Theorem 3.1 is automatic, as noted after (2.6).  The only remaining
residence issue at that step is the literal list (3.1)--(3.2).

This yields a sharp audit boundary.

1. Connectivity of the MNW flippability hypergraph does not imply any of
   (3.1)--(3.2).
2. Edge-disjointness of selected flipping cycles does not imply the collar
   inequalities either.
3. A proof that an MNW joining schedule preserves depth-three residence must
   verify all ten clauses at every dynamic seam, or prove a structural lemma
   which implies them.
4. Even a residence-safe flip changes the two endpoint turn colours of every
   inserted edge according to (4.3).  Hence turn-colour coverage must be
   transported with the signed ledger (4.4); it is not inherited from the
   seed factor.
5. If later joining operations can touch a current component more than once
   in one step, then five-edge separation must first be checked.  Without it,
   Corollary 3.3 is the correct audit, not independent seam tests.

## 6. Cyclic boundary audit

All indices in (1.2) are cyclic.  The proof of Theorem 3.1 uses directed
edge occurrences, so it remains valid when the left and right five-collars
overlap as sets of physical edges; the clauses must then be read
positionally.  For the shortest MSW components, \(N=2m+1\ge7\) when
\(m\ge3\), so offsets three and five are nonzero.  At \(N=7\), for example,
distance five is also backward distance two; this creates no exception,
because (1.2) and the proof use the specified forward offset modulo \(N\).

The genuinely exceptional case would be a cycle length dividing one of the
tested offsets, when a condition would compare an occurrence with itself.
Such a cycle cannot be depth-three resident in the first place and is
excluded by the hypothesis that \(F\) satisfies (1.2).  No linear end
correction is present: the last-to-first collar of every resulting cycle is
one of the cyclic seams already covered by Theorem 3.1.
