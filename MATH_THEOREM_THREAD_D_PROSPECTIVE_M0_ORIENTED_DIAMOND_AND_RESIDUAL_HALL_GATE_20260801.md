# Fixed root matching: oriented diamonds and the second-phase residual Hall gate

Date: 2026-08-01  
Lane: Thread D / Catalan central forest  
Status: exact downstream fixed-fibre equivalence and obstruction; not the primary prospective-`M0` theorem

## Scope warning

This note fixes a complete root matching `M0` first.  Its Hall graph in
Section 2 extends the upper-exact partial matching `Q` to a **second**
perfect phase disjoint from `M0`.

It is not the primary joint-`M0` reduction.  That reduction is Theorem 2.1
and system (2.4) of
`MATH_THEOREM_THREAD_D_PROSPECTIVE_M0_ORIENTED_DIAMOND_AND_RESIDUAL_HALL_20260801.md`:
there an oriented-diamond choice specifies only the partial predecessor
assignment `L -> T`, and the residual `y`-matching completes **M0 itself**.
The upper matching `Q:L -> V` remains partial of size `P`.  The two Hall
rows are consecutive but logically different gates.

## 0. Result

Let \(\Omega=[2m-1]\), and let \(G_m\) be the middle-levels incidence
graph between

\[
 {\cal A}={\Omega\choose m-1},\qquad
 {\cal B}={\Omega\choose m}.
\]

Put

\[
 W=|{\cal A}|=|{\cal B}|,
 \qquad P={2m-1\choose m+1},
 \qquad C=W-P=\operatorname {Cat}_m.                 \tag{0.1}
\]

Choosing the root matching \(M_0\) prospectively does not remove the
integral correlation gate.  It gives the following exact normal form.

* A root matching \(M_0\) together with an upper-exact, tail/head-simple,
  rooted-acyclic matching \(Q\) of size \(P\) is exactly a family of \(P\)
  ordered Boolean diamonds whose middle-levels support is an alternating
  forest with exactly \(C\) path components.
* It extends to a spanning middle-levels two-factor exactly when one
  residual Boolean incidence graph has a perfect matching.  This is an
  ordinary Hall condition after \((M_0,Q)\) is fixed, but it is not
  automatic from the four marginal rows.
* To obtain the known decorated-two-factor certificate for Catalan Linear
  Matching, the resulting factor must additionally pass the exact
  lower-turn gap--Hall test and the componentwise linear-trace test.

Consequently a simultaneous positive theorem for the prospective
\(M_0\) system would be a genuine construction of the currently open
decorated-two-factor subclass.  It is not a disguised application of
ordinary two-matroid intersection.

There is an actual Boolean obstruction after freezing the fibre.  The
audited \(m=4\) rooted Catalan forest in
`MATH_THEOREM_CATALAN_PENTAGONAL_CONNECTOR_RANK_SEPARATION_AND_FOUR_PATH_ABSORBER_20260801.md`
has residual matching rank \(11/14\) and port-gap vector

\[
                       (4,2,2,3,3,1,-1).               \tag{0.2}
\]

Thus its residual Hall row fails.  Forest-preserving aligned pentagonal
pivots leave both the gap vector and the \(11/14\) rank unchanged.  This is
a literal Boolean fixed-\((M_0,Q)\) obstruction, not a no-go for choosing
\(M_0\), \(Q\), and the residual matching jointly.  In particular, known
decorable \(m=4\) factors show that no global \(m=4\) obstruction exists.

## 1. Rooted upper diamonds

Fix a perfect matching \(M_0:{\cal A}\to{\cal B}\).  For an incidence
edge \(e=AB\notin M_0\), define

\[
 \kappa_{M_0}(e)=M_0(A)\cup B\in{\Omega\choose m+1},  \tag{1.1}
\]

and define its rooted link by

\[
 \lambda_{M_0}(e):A\longrightarrow M_0^{-1}(B).       \tag{1.2}
\]

The two middle sets \(M_0(A)\) and \(B\) are distinct and both contain
\(A\), so their intersection is \(A\) and their union has rank \(m+1\).
Thus every such edge specifies the literal ordered diamond

\[
        D(e)=\bigl(A;\ M_0(A),B;\ M_0(A)\cup B\bigr). \tag{1.3}
\]

Call \((M_0,Q)\) a **prospective rooted upper system** when

1. \(Q\subseteq E(G_m)\setminus M_0\) is a matching of size \(P\);
2. \(\kappa_{M_0}:Q\to{\Omega\choose m+1}\) is bijective; and
3. the undirected graph underlying \(\lambda_{M_0}(Q)\) is a forest.

Because \(Q\) is a matching, every root has indegree and outdegree at most
one in (1.2).  Condition 3 therefore says that the rooted links are a
disjoint union of directed paths and isolated roots.

### Theorem 1.1 (three exact forms)

The following data are equivalent.

1. A prospective rooted upper system \((M_0,Q)\).
2. A perfect matching \(M_0\) and \(P\) ordered diamonds (1.3) having
   pairwise distinct lower entries, second middle corners, and upper
   entries, whose tail-to-head root graph is acyclic.
3. A spanning perfect matching \(M_0\) and a second partial matching \(Q\)
   such that \(M_0\cup Q\) is an alternating linear forest with exactly
   \(C\) components and its degree-two \({\cal A}\)-turns enumerate all
   rank-\((m+1)\) colours exactly once.

#### Proof

The lower entry and first middle corner of a diamond are \(A\) and
\(M_0(A)\).  Distinct \(Q\)-tails give distinct \(A\)'s and distinct first
corners; the matching condition on \(Q\) gives distinct second corners.
The remaining resource is exactly \(\kappa_{M_0}\), and contraction of the
\(M_0\)-edges turns \(M_0\cup Q\) into the rooted link graph (1.2).  This
proves the equivalence of 1 and 2 and identifies acyclicity in 3.

The graph \(M_0\cup Q\) has \(2W\) vertices and \(W+P\) edges.  If it is a
forest, its component count is

\[
                    2W-(W+P)=W-P=C.                   \tag{1.4}
\]

Conversely an alternating forest supported on a spanning phase \(M_0\)
contracts to the rooted forest, and its degree-two \({\cal A}\)-turn at
\(A\) has colour \(M_0(A)\cup Q(A)\).  Hence the exact-turn condition in 3
is precisely Condition 2 above. \(\square\)

This is a partial ordered four-transversal.  It has only \(P=W-C\)
diamonds; the \(C\) unused lower roots are exactly the path-component
defect.  It must not be called a completed Catalan Linear Matching.

## 2. Residual extension is exactly Hall

For a prospective rooted upper system put

\[
 X={\cal A}\setminus V_{\cal A}(Q),\qquad
 Y={\cal B}\setminus V_{\cal B}(Q).                   \tag{2.1}
\]

Both sets have size \(C\).  Let

\[
                   H_{M_0,Q}=(G_m-M_0)[X,Y].           \tag{2.2}
\]

### Theorem 2.1 (exact residual criterion)

The partial matching \(Q\) extends to a perfect matching \(M_1\) of
\(G_m-M_0\) if and only if

\[
 |N_{G_m-M_0}(S)\cap Y|\ge |S|
               \qquad\text{for every }S\subseteq X.  \tag{2.3}
\]

Equivalently, with

\[
 \delta(M_0,Q)=
   \max_{S\subseteq X}\bigl(|S|-|N_{G_m-M_0}(S)\cap Y|\bigr),          \tag{2.4}
\]

the largest extension has size \(W-\delta(M_0,Q)\), and a perfect
extension exists exactly when \(\delta(M_0,Q)=0\).

When (2.3) holds, every perfect matching \(R\) of (2.2) gives

\[
                         M_1=Q\mathbin{\dot\cup}R,      \tag{2.5}
\]

and \(M_0\cup M_1\) is a spanning middle-levels two-factor whose selected
upper turns are exactly the diamonds of \(Q\).

#### Proof

Every extension edge must join an unused \({\cal A}\)-endpoint to an
unused \({\cal B}\)-endpoint, and every perfect matching of (2.2) supplies
all missing edges.  Hall's theorem and its deficiency form prove
(2.3)--(2.4).  The graph (2.2) omits \(M_0\), so
\(M_0\cap M_1=\varnothing\).  The union of two disjoint perfect matchings
is therefore an ordinary spanning middle-levels two-factor.  Formula (1.1)
identifies the selected turns.
\(\square\)

There is a useful Boolean necessary row which is invisible to cardinality
alone.  For a family \({\cal Z}\) of subsets, write

\[
                         d_i({\cal Z})=|\{Z\in{\cal Z}:i\in Z\}|.
\]

Every residual incidence edge adds one coordinate.  Therefore a perfect
residual matching forces

\[
                 g_i=d_i(Y)-d_i(X)\ge0
                         \qquad(i\in\Omega).           \tag{2.6}
\]

Indeed \(g_i\) counts residual matching edges whose added coordinate is
\(i\).  This is necessary, not sufficient; the complete condition remains
(2.3).

### Proposition 2.2 (an actual fixed-fibre Boolean obstruction)

For the frozen upper-exact rooted \(m=4\) forest cited in Section 0,
\(|X|=|Y|=14\), the maximum matching of (2.2) has size \(11\), and the
coordinate gap vector is (0.2).  Hence (2.3) fails and no residual
completion exists.  Its one available rooted, forest-preserving pentagonal
pivot preserves the endpoint load vector and leaves the matching rank
\(11\).

This proposition is independently replayed by
`scratch/audit_catalan_pentagonal_connector_rank_separation_20260801.py`;
the frozen audit payload has SHA-256
`7d7522bc6b1ecc755efdcc234c7da4fca5457a98f50b4c32966bdf6118ce4338`.

The quantifier is essential:

\[
 \exists(M_0,Q)\ \forall R\;[R\text{ fails}]
 \quad\not\Longrightarrow\quad
 \forall(M_0,Q)\ \forall R\;[R\text{ fails}].        \tag{2.7}
\]

The obstruction proves that residual Hall cannot be postponed after an
arbitrary upper-forest choice.  It does not prove that prospective joint
selection is impossible.

## 3. Exact relation to decorated two-factors

Assume (2.3), choose \(R\), and write each component of
\(F=M_0\cup(Q\cup R)\) cyclically as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{s-1},B_{s-1},A_0.          \tag{3.1}
\]

The set \(Q\) marks an \({\cal A}\)-turn transversal: its selected turn
colours enumerate \({\Omega\choose m+1}\).  These marks do not by
themselves choose the required lower turns

\[
                         A_i\cap A_{i+1}
                   \in{\Omega\choose m-2}.            \tag{3.2}
\]

For the selected upper marks, form on all factor components the cyclic
gaps between consecutive upper marks.  Join a gap to a lower colour when
that colour occurs at a \({\cal B}\)-turn inside the gap.

### Theorem 3.1 (joint system versus the known sufficient subclass)

A prospective system \((M_0,Q)\), a residual matching \(R\), and a choice
of lower-turn occurrences induce a Catalan linear matching through the
decorated-middle-levels construction if and only if

1. the gap--lower-colour graph has a perfect matching; and
2. on every factor component the resulting binary mark trace is linear in
   the exact componentwise sense (unmarked components are allowed, wholly
   marked components are forbidden, and the unique binary cycle face is
   avoided).

Conversely every componentwise decorated linear middle-levels two-factor
admits a phase choice \(M_0\) for which its selected upper occurrences give
a prospective \(Q\), and the unselected edges of the other phase give the
residual matching \(R\).

#### Proof

For the forward direction, the gap matching is exactly the theorem that
the upper and lower selected turn types alternate componentwise and that
the lower colours are bijective.  The componentwise trace theorem then says
that the lifted perfect diamond matching is a linear forest precisely under
Condition 2.

For the converse, split every even factor cycle into its two alternating
perfect-matching phases, choosing one as \(M_0\).  At every selected upper
turn retain the incident edge of the other phase in \(Q\), and put all
remaining edges of that phase in \(R\).  Upper colours and matching
resources are exact by the decoration.  Every factor component contains an
unselected upper-shore occurrence: otherwise alternation would force the
component to be wholly marked.  Deleting the corresponding residual-phase
edge breaks that cycle, so \(M_0\cup Q\) is an alternating forest.  Thus
\((M_0,Q)\) is prospective and \(R\) is its residual extension. \(\square\)

The authoritative \({\rm ML}(7)\) counterexample in
`MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`
shows why the gap row cannot be deleted: both complete turn words are
surjective, yet all \(12{,}288\) upper transversals fail the induced
gap--Hall condition.  Thus separate palette marginals, even on a Hamilton
factor, do not imply a decorated factor.

The implication above is a sufficient middle-levels-resolvable route to
Catalan Linear Matching.  It is not an equivalence with arbitrary Catalan
linear matchings: an explicit \(m=3\) linear diamond matching has forced
middle-levels support of degree three.  Hence a failure of this prospective
route would not refute the unrestricted Catalan Linear Matching theorem.

## 4. Why prospective \(M_0\) is not ordinary matroid intersection

For a fixed \(M_0\), selecting \(Q\) asks for a common independent set of
four matroids on the candidate incidence edges:

1. the partition matroid of upper colours \(\kappa_{M_0}\);
2. the partition matroid of \({\cal A}\)-tails;
3. the partition matroid of \({\cal B}\)-heads; and
4. the graphic matroid of rooted links \(\lambda_{M_0}\).

The target size is \(P\), with every upper-colour class saturated.  Allowing
\(M_0\) to vary makes both \(\kappa_{M_0}\) and
\(\lambda_{M_0}\) depend on the inverse of the chosen perfect matching.
Thus the prospective problem is exactly

\[
 \boxed{\text{spanning perfect matching }M_0
   +\text{ upper-exact alternating partial two-factor}
   +\text{ residual Hall}.}                           \tag{4.1}
\]

It is not one fixed-ground-set two-matroid intersection.  The uniform
fractional point satisfying the known matching, cap-two, and graphic
inequalities does not resolve this integral correlation.

No generic maximum-degree estimate closes (4.1): all relevant partition
classes can be perfectly balanced while the selected rooted links contain
cycles, or while the residual graph violates (2.3).  The Boolean data which
can help are the actual incidence shadows, coordinate port gaps, and the
gap--Hall interlacing graph.

## 5. Exact cycle-breaking scope

The companion note
`MATH_THEOREM_THREAD_D_RAINBOW_MATCHING_CYCLE_BREAKING_AND_ROOTED_FOREST_GATE_20260801.md`
gives the exact fixed-\(M_0\) exchange statement.  Relative to a selected
rainbow matching \(F\) and protected set \(P_0\), choose a set \(D\) of
unprotected edges meeting every rooted cycle, put \(F_0=F-D\), and ask for
\(|D|\) replacement edges which are simultaneously independent in the four
contracted matroids above.  If \(\nu_F(D)\) is the largest such replacement
set, then the exact fixed-fibre obstruction is

\[
       \Delta_{P_0}(F)=
       \min_{D\text{ hits every cycle}}
                    \bigl(|D|-\nu_F(D)\bigr).          \tag{5.1}
\]

Cycle breaking while preserving all four resources is possible exactly
when \(\Delta_{P_0}(F)=0\).  A legal one-edge exchange is the special case
\(|D|=1\).

This theorem is exact but deliberately local.  It neither chooses the
prospective root matching nor proves residual Hall after the forest is
repaired.  A two-colour abstract example in that note already shows that
colour/tail/head marginal completion and graphic completion can demand
incompatible exchanges.  The \(m=4\) rank-\(11/14\) example above supplies
the separate literal Boolean warning that even a successfully repaired
rooted forest can lie in a residual-Hall-dead fibre.

## 6. Sharp surviving theorem target

The smallest noncircular all-dimension statement exposed by this reduction
is the following.

> **Prospective rooted decorated-factor theorem.**  There exist a perfect
> matching \(M_0\), a rooted upper system \(Q\), and a perfect residual
> matching \(R\) such that the induced factor admits a perfect matching in
> its gap--lower-colour graph and every decorated component has linear
> trace.

By Theorem 3.1 this is exactly an all-dimension componentwise decorated
middle-levels two-factor theorem and therefore implies Catalan Linear
Matching.  It is presently open.  The results audited here prove neither a
Boolean obstruction to this joint statement nor an automatic Boolean Hall
theorem.  What they do prove is sharp:

* residual Hall is exact once \((M_0,Q)\) is fixed;
* it can genuinely fail in a Boolean fibre;
* choosing \(M_0\), upper representatives, endpoints, rooted acyclicity,
  residual completion, and lower interlacing must be correlated; and
* cycle-breaking and residual completion are distinct gates.
