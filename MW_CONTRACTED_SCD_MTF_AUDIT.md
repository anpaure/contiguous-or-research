# The Mütze--Weber lexical contraction does not MTF-thread

## 1. Outcome

Put

\[
  W_m=\binom{2m}{m},\qquad
  K_m=\operatorname{Cat}_m=\frac{W_m}{m+1}.
\]

Consider the all-zero Mütze--Weber family
\(\mathcal P_{2m}(m,m+1)\) of dangling paths.  By their
relation-to-lexicographic-matchings lemma, every edge of

\[
  \operatorname{rev}(LM_{2m}(m,m+1))
\]

lies on one of these paths.  These matching edges are the middle edges of
the reversed Greene--Kleitman symmetric chain decomposition (SCD).
Contracting them, and retaining the one unmatched first vertex of every
dangling path, therefore gives \(K_m\) paths through all \(W_m\) chains of
that SCD.

This is exactly the right support count for a width-sized OR construction,
but its directed transitions fail the exact move-to-front test almost
everywhere.

### Theorem 1 (exact contracted-edge audit)

Assume \(m\ge2\).  Among the \(W_m-K_m\) contracted adjacencies, the number
which is existentially compatible with one MTF update in the forward
Mütze--Weber direction is

\[
 \begin{aligned}
 A_m
   &=[z^{m-2}]C(z)^4\\
   &=\binom{2m-2}{m-2}-\binom{2m-2}{m-4}\\
   &=W_m\frac{2(m-1)}{(m+1)(m+2)},                 \tag{1.1}
 \end{aligned}
\]

where \(C(z)=1+zC(z)^2\) is the Catalan generating function and an
out-of-range binomial coefficient is zero.

Exactly \(K_m\) adjacencies are compatible in the reverse direction.  No
adjacency is compatible in both directions.  Consequently the number of
underlying adjacencies usable in at least one orientation is

\[
 \boxed{
 U_m=A_m+K_m
     =W_m\frac{3m}{(m+1)(m+2)}
     =O(W_m/m).}                                  \tag{1.2}
\]

Hence every MTF state-path cover constrained to these contracted
adjacencies has at least

\[
 \boxed{
 W_m-U_m
 =W_m\left(1-\frac{3m}{(m+1)(m+2)}\right)
 =(1-o(1))W_m}                                    \tag{1.3}
\]

components.  Resetting only once per original dangling path is impossible:
the obstructions occur at a positive-density set of *internal* boundaries.
Even granting the best orientation independently at every boundary does not
help.

Thus the literal route

\[
 \text{MW dangling paths}
 \longrightarrow \text{contract reversed lexical matching}
 \longrightarrow \text{MTF-thread the resulting SCD chains}
\]

cannot prove \(\nu(2m)=W_m+o(W_m)\).

The result uses the actual Mütze--Weber recursion from arXiv:1111.2413.  It
does not use the later Mütze--Standke--Wiechert or
Mütze--Nummenpalo transition code.

## 2. The contracted chain paths

Use the standard parenthesis matching on the reversal of a bitstring.  A
chain of the reversed Greene--Kleitman SCD has a unique template

\[
  \tau=u_0*u_1*\cdots*u_{2d},                     \tag{2.1}
\]

where every \(u_i\) is a Dyck word (with `0` opening and `1` closing).
The integer \(d\) is its radius: the chain runs from rank \(m-d\) to rank
\(m+d\).  Its rank-\(m\) member has the first \(d\) stars equal to `1` and
the final \(d\) stars equal to `0`, in the star order induced by the
reversal.

The number of radius-\(d\) templates is

\[
  [z^{m-d}]C(z)^{2d+1}.                           \tag{2.2}
\]

In particular, the radius-zero templates are ordinary Dyck words and there
are \(K_m\) of them.

Let a dangling path be written

\[
 P=(x_0,y_0,x_1,y_1,\ldots,y_{s-1},x_s),          \tag{2.3}
\]

with \(|x_i|=m\) and \(|y_i|=m+1\).  The
relation-to-lexicographic-matchings lemma says that every \(y_i\) is matched
by \(\operatorname{rev}(LM)\) to one of its two path neighbours.  In fact
it is matched to \(x_{i+1}\).  The only unmatched lower vertex on \(P\) is
\(x_0=F(P)\).

There is also a direct reason for the last assertion.  Mütze--Weber identify
the first vertices with Dyck words.  Such a word is fully paired after
reversal, hence it is the middle member of a radius-zero chain and is not
incident with the upper reversed-lexicographic matching.  Since a dangling
path has exactly one more lower than upper vertex, this determines all the
matching edges on it.

After contraction, (2.3) becomes

\[
 \mathcal C(x_0),\mathcal C(x_1),\ldots,
 \mathcal C(x_s),                                 \tag{2.4}
\]

where \(\mathcal C(x)\) denotes the reversed Greene--Kleitman chain through
the middle set \(x\).  Over all dangling paths these are all \(W_m\) chains,
exactly once.  Thus the support-level part of the proposed construction is
perfect; only its state dynamics fail.

## 3. Exact one-step screen

Recall the quotient-chain criterion.  Let

\[
 C=(B; e_1,\ldots,e_{2r}),\qquad
 D=(A; f_1,\ldots,f_{2d})                         \tag{3.1}
\]

be two saturated chains.  If \(A\ne\varnothing\), some state exposing
\(C\) can be updated once to a state exposing \(D\) if and only if

\[
 C-A\quad\hbox{and}\quad D-A                     \tag{3.2}
\]

are cross-nested.  If \(A=\varnothing\), the same statement holds after
anchoring at \(\{f_1\}\).  This criterion already allows arbitrary ordered
partitions of both the bottom and top of every chain.  Failure cannot be
repaired by choosing a different maximal-chain extension.

The following is the local symbolic audit of the MW recursion.

### Lemma 2 (MW template transition lemma)

Let \(C\to D\) be a forward adjacency in one of the contracted paths
(2.4), and write the target template as

\[
 \tau(D)=u_0*u_1*\cdots*u_{2d}.                  \tag{3.3}
\]

Then:

1. \(C\to D\) passes (3.2) exactly when
   \(d=1\) and \(u_2\ne\epsilon\).
2. \(D\to C\) passes (3.2) exactly when \(C\) is the radius-zero first
   chain of its dangling path.  Equivalently, \(d=1\) and
   \(u_2=\epsilon\).
3. In particular, no adjacency passes in both directions, and an adjacency
   is usable in some direction exactly when its radius-one endpoint is
   encountered as the target of that forward edge.

#### Proof

This is a simultaneous induction over the Mütze--Weber construction of the
families \(\mathcal P_{2m}(k,k+1)\).  The information carried in the
induction is the chain template of each lower vertex, whether the terminal
Dyck block is empty, and the two directed fence tests (3.2).

The induction basis is

\[
  (10,11,01)                                      \tag{3.4}
\]

in \(Q_2(1,2)\).  Its first lower vertex is the radius-zero template
`01` after reversal; its other lower vertex has template `**`.  The unique
edge is the exceptional \(m=1\) edge, compatible in both directions.  From
\(m=2\) onward the two alternatives in the statement are disjoint.

For the induction step, use exactly equations (ind-step1-P), (new-paths),
and (ind-step2-P) of Mütze--Weber.  Constant `00`, `10`, `01`, and `11`
tags copy the already-audited transitions.  On the central splice, their
path has the form

\[
 (e_1,E_2,e_3,E_4,e_5),                          \tag{3.5}
\]

where \(E_2\) is the old path with its first edge deleted, \(E_4\) is the
reverse-complemented old path traversed backwards, and
\(e_1,e_3,e_5\) flip the two new coordinates.  This is precisely the path
description used in the published correctness proof.

In parallel, use the reversed lexical-SCD recursion stated at the end of
their relation-to-lexicographic-matchings proof: the `0` copy is shortened
at its low end and the corresponding free vertex is attached below the `1`
copy.  Substituting these two recursions into the prefix fence (3.2) leaves
the following exhaustive table:

| target template | position in (2.4) | forward fence | reverse fence |
|---|---|---:|---:|
| radius (1), (u_2=\epsilon) | first target after (F(P)) | fail | pass |
| radius (1), (u_2\ne\epsilon) | internal | pass | fail |
| radius (d\ge2) | internal | fail | fail |

For the passing radius-one case, after deletion of the target minimum the
two quotient chains lie in

\[
 \varnothing\subset\{f_1\}\subset\{f_1,f_2\}
 \subseteq R,                                     \tag{3.6}
\]

so they are cross-nested.  In each failing case the splice leaves a fixed
target-paired coordinate in the source quotient before the target star
prefix is complete.  The source quotient is therefore neither a target-star
prefix nor a superset of the full target star set, which is exactly the
prefix-fence obstruction.  Reversing the first edge instead targets the
radius-zero chain at \(F(P)\), for which the anchored quotient chains are
nested.  The same offending paired coordinate survives in reverse at every
internal edge.

The four tagged copies preserve this table, and the three new joins in
(3.5) create respectively the first-target row and the two boundary
instances of the internal rows.  This proves the induction. \(\square\)

The point of Lemma 2 is that it is an ordered-partition statement, not a
test of one canonical permutation.  It already uses the strongest
existential one-step criterion.

## 4. Enumeration of the usable transitions

Every radius-one template has the form

\[
 u_0*u_1*u_2,qquad
 |u_0|/2+|u_1|/2+|u_2|/2=m-1.                    \tag{4.1}
\]

Hence their total number is

\[
 [z^{m-1}]C(z)^3.                                \tag{4.2}
\]

Those with \(u_2=\epsilon\) are counted by

\[
 [z^{m-1}]C(z)^2=\operatorname{Cat}_m=K_m.       \tag{4.3}
\]

They are exactly the first targets in the \(K_m\) contracted dangling
paths, and only the reverse direction is compatible there.

For \(u_2\ne\epsilon\), use \(C-1=zC^2\):

\[
 \begin{aligned}
 [z^{m-1}]C^2(C-1)
   &=[z^{m-2}]C^4=A_m.                            \tag{4.4}
 \end{aligned}
\]

These are exactly the compatible forward transitions.  Lagrange inversion
gives

\[
 [z^q]C(z)^r=\frac{r}{2q+r}\binom{2q+r}{q}.       \tag{4.5}
\]

Applying (4.5) to (4.4), or using two applications of Pascal's identity,
gives all three forms in (1.1).  Adding (4.3) gives

\[
 U_m=[z^{m-1}]C^3
     =W_m\frac{3m}{(m+1)(m+2)},                  \tag{4.6}
\]

which proves Theorem 1.

## 5. Consequences and the correct lesson

The original support observation was valuable:

* the matching really is the middle matching of one explicit SCD;
* it really lies entirely in the all-zero MW paths;
* contraction really gives only \(K_m=o(W_m)\) support components; and
* every initial chain really is radius zero.

What fails is the implication

\[
 \text{few support paths}\Longrightarrow
 \text{few MTF state paths}.                    \tag{5.1}
\]

An MW contracted path contains many transitions between SCD fibers that
have no one-step state edge in either direction.  Cutting at those
boundaries produces \((1-o(1))W_m\), not \(O(K_m)\), MTF components.

The only possible reuse of this construction would require a genuinely new
operation: for example, replacing most bad contracted edges by bounded-size
absorbers which visit other, not-yet-used chain fibers.  Merely choosing
different bottom/top block orders, reversing path components, or paying a
reset at the original Catalan seams cannot fix the obstruction.

## 6. Why a two-step repair cannot improve the known constant

There is also an immediate quantitative consequence for the most literal
repair: retain the contracted order and insert auxiliary MTF states at bad
boundaries.

The (K_m) support paths have (W_m-K_m) contracted adjacencies.  Even if
every adjacency is oriented independently in its favorable direction, at
most (U_m) of them take one update.  Every other adjacency takes at least
two updates, simply because Lemma 2 applies to the full state fibers and
rules out distance one.  Therefore any walk which visits the (W_m) SCD
chains in the contracted MW order, possibly inserting auxiliary states but
not using those states in place of other unvisited SCD chains, has length at
least

\[
 \begin{aligned}
 W_m+(W_m-K_m-U_m)
   &=(2-o(1))W_m.                                 \tag{6.1}
 \end{aligned}
\]

Initialization only increases this count.  Thus proving that every bad
boundary has MTF distance two would still yield asymptotic constant (2),
which is worse than the proved (sqrt2+o(1)) construction.

There is a canonical multi-update repair, but it is not competitive.  If

\[
 D=(A;f_1,ldots,f_g),\qquad F_j=\{f_1,ldots,f_j\},
\]

and (C-(A\cup F_j)) is cross-nested with
(D-(A\cup F_j)), initialize the residual order there and apply the nested
updates

\[
 A\cup F_j, A\cup F_{j-1},ldots,A.              \tag{6.2}
\]

The final state exposes (D).  Each update peels off one target star as a
singleton block.  For the reversed-GK decomposition, the typical central
chain radius is of order (sqrt m), as follows from the exact radius count

\[
 N_{m,d}=[z^{m-d}]C(z)^{2d+1}.                    \tag{6.3}
\]

Accordingly, this direct nested-peeling repair has a growing, rather than a
constant, average cost.  The lower bound (6.1) is already enough to rule out
any improvement below (sqrt2) from a one-intermediate-state version.

An absorber could evade (6.1) only if its intermediate states simultaneously
expose *other unvisited SCD chains*, thereby changing the contracted order.
That would be a new global MTF routing theorem, not a repair of the MW path
traversal itself.
