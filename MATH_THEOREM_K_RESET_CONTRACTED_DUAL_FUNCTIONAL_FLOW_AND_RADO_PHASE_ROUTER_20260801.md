# Reset-contracted dual functional flow and the exact Rado phase-router criterion

**Date:** 2026-08-01  
**Status:** unconditional exact dual-flow theorem and an unconditional
Rado/gammoid repair theorem.  The latter is a sufficient prospective route:
it requires one reset-compatible functional filler and a literal
path-lifting phase-exchange network.  It does not assert that the current
`k=17` catalogue supplies either hypothesis.

## 0. Outcome

Contract the seven protected turns of the opened rolling reset, retaining
its incoming and outgoing socket resources.  On the residual instance the
three-matroid attachment problem has a useful exact dual form.

* Fix a bijection \(\phi\) from residual owners to residual **tail** roots.
  For a fixed flag table, the remaining head-owner choice is one ordinary
  bipartite perfect matching.  This is the tail-functional dual of the
  previously proved head-functional flow theorem.
* Starting from any functional filler obtained this way, let literal
  reset-avoiding phase trades form a directed exchange network.  Pair every
  still-required rank-\((m-2)\) target with a distinct containing
  rank-\((m-1)\) target, so the nested high-target obligations become one
  list per immediate target.  All obligations can be installed
  simultaneously if and only if their endpoint lists satisfy one Rado
  rank inequality in the strict gammoid of the exchange network.
* The gammoid rank is an ordinary vertex-capacitated max flow.  Therefore
  the exact criterion is

  \[
       \operatorname {maxflow}
       \left(S,\bigcup_{c\in I}L_c\right)\ge |I|
       \quad\hbox{for every obligation family }I.             \tag{0.1}
  \]

  The exact minimum number of uncovered obligations is

  \[
       \delta=max_I
       \left(|I|-r_{\mathcal G}\left(\bigcup_{c\in I}L_c\right)\right)_+.
                                                                    \tag{0.2}
  \]

Thus bounded or zero defect is a theorem once the literal exchange network
has the corresponding cut bound.  Fractional suffix marginals alone imply
neither (0.1) nor \(\delta=O(1)\).

## 1. Contracted reset resources

The statement is valid physically or in an aligned quotient.  In the
quotient, parallel phase-labelled incidences remain distinct.

Let

\[
                  R^-,\quad R^+,\quad O                       \tag{1.1}
\]

be the residual tail-root, head-root, and owner resources after deleting
the seven resources used on each shore by the opened reset path.  All three
sets have the same size \(N'\) (at `k=17`, \(N'=1423\)).  The two endpoint
flags of the opened path remain as the appropriate residual socket copies;
their flag states are fixed.

Fix a complete flag table \(F\), including those socket flags.  For an
aligned owner incidence \(p\subset o\supset q\), write

\[
                         p\xrightarrow[o]{F}q                  \tag{1.2}
\]

when the two selected flags pass the complete literal survivor test.  This
notation includes the physical phase; it is stronger than Johnson
adjacency.

## 2. The exact dual functional-flow theorem

Let

\[
                         \phi:O\longrightarrow R^-             \tag{2.1}
\]

be a bijection using aligned incidences \(\phi(o)\subset o\).  Define the
bipartite graph

\[
 J_{F,\phi}\subseteq R^+\times O,qquad
 qo\in J_{F,\phi}iff \phi(o)\xrightarrow[o]{F}q.             \tag{2.2}
\]

### Theorem 2.1 (tail-functional Hall)

For fixed \(F\) and \(\phi\), there is an owner-exact residual cycle cover
whose owner \(o\) has predecessor tail \(\phi(o)\) if and only if
\(J_{F,\phi}\) has a perfect matching.  Equivalently,

\[
                 |N_{J_{F,\phi}}(X)|\ge |X|
                 \qquad(X\subseteq R^+).                      \tag{2.3}
\]

The residual system is totally unimodular.

#### Proof

A perfect matching \(\theta:R^+\to O\) in \(J_{F,\phi}\) uses every head
and owner once.  Since \(\phi\) is bijective, the turns

\[
                     \phi(\theta(q))\longrightarrow q         \tag{2.4}
\]

also use every tail once, and (2.2) makes them literal.  Conversely, a cover
whose predecessor map is the prescribed \(\phi\) maps every head to its
incoming owner and hence gives a perfect matching in \(J_{F,\phi}\).  For
fixed \(\phi\), Hall and bipartite total unimodularity give the result.
\(\square\)

### Corollary 2.2 (exact two-functional form)

For a fixed flag table, the reset-conditioned three-matroid common base
exists if and only if there is an aligned owner-to-tail bijection \(\phi\)
for which (2.3) holds.

This is equivalent to the earlier head-functional theorem, but the two
orientations expose different constructive banks.  The rolling reset
prescribes both sides of seven owner columns.  They are forced edges of
\(\phi\) and \(\theta\) in the full extension and are deleted from the
residual maps after contraction.

The quantifier over \(F\) remains load-bearing.  The independently completed
`k=17` flag table with 406 universally dead tails admits no such \(\phi\).

## 3. Nested high-target obligations

Let \({\cal P}\) be the residual rank-\((m-1)\) targets not already marked
inside the reset bank, and let \({\cal T}\) be the corresponding residual
rank-\((m-2)\) targets.

Choose a containment matching

\[
                         \lambda:{\cal T}\hookrightarrow{\cal P},
                         \qquad T\subset\lambda(T).            \tag{3.1}
\]

which respects every already fixed reset chain.  Such a matching is the
ordinary lower-layer Hall row.  It converts the two target ranks into one
obligation for every \(P\in{\cal P}\):

\[
 c_P=
 \begin{cases}
  (T\subset P),&P=\lambda(T),\\
  (*\subset P),&P\notin\lambda({\cal T}).
 \end{cases}                                                  \tag{3.2}
\]

An endpoint flag satisfies \((T\subset P)\) when both displayed suffixes
occur and may be marked; it satisfies \((*\subset P)\) when its immediate
suffix is \(P\), while its deeper suffix remains unmarked.  Hence one
representative of every obligation marks every residual high target exactly
once.  Additional flag occurrences may remain unmarked.

## 4. Literal phase-exchange networks

Start with a reset-compatible functional filler

\[
                         (F_0,\phi_0,\theta_0).                 \tag{4.1}
\]

It is allowed to miss targets in (3.2), but Theorem 2.1 must hold: it is an
exact owner/tail/head factor containing the opened reset path.

A **literal phase-exchange network** is a directed graph \({\cal D}\) with
a source bank \(S\), together with a realization map for directed paths,
satisfying the following axioms.

1. A directed path from \(S\) to a terminal flag option is an alternating
   replacement of literal turn atoms in (4.1).  It preserves one use of
   every residual tail, head, and owner, and leaves a consistent single flag
   at every root.  Thus it may change \(F,\phi,\theta\) jointly, but its
   output is another functional factor.
2. Every internal exchange preserves all already protected high-target
   marks.  The terminal may additionally supply the obligation assigned to
   it.
3. The exchange avoids every contracted reset resource and preserves both
   reset socket states.
4. Vertex-disjoint directed paths have resource-disjoint realizations, so
   their alternating replacements commute.

These are physical hypotheses.  An arc is not certified merely by equality
of quotient sets: its aligned phases, both flags, and the literal survivor
law must be part of the realization.  Whole-orbit flag substitutions retain
depth-three positional rail balance, but that fact alone does not establish
axiom 1.

For an obligation \(c\), let \(L_c\) be the set of terminals whose realized
final flag supplies \(c\).  Delete the reset vertices from \({\cal D}\).
Let \({\cal G}={\cal G}({\cal D},S)\) be the strict gammoid on its terminal
vertices: a set is independent when it can be linked from distinct sources
in \(S\) by pairwise vertex-disjoint directed paths.

## 5. Exact Rado router theorem

### Theorem 5.1 (reset-contracted phase-router)

Under the hypotheses of Sections 3--4, there is a family of pairwise
vertex-disjoint paths in the phase-exchange network which installs all
residual high-target obligations while preserving an owner-exact functional
factor and the opened reset bank if and only if

\[
 r_{\cal G}\left(\bigcup_{c\in I}L_c\right)\ge |I|
 \qquad(I\subseteq\{c_P:P\in{\cal P}\}).                  \tag{5.1}
\]

#### Proof

Rado's independent-transversal theorem applied to the matroid \({\cal G}\)
and the lists \(L_c\) says that (5.1) is equivalent to representatives

\[
                         v_c\in L_c                            \tag{5.2}
\]

whose set is independent in \({\cal G}\).  By definition, pairwise
vertex-disjoint paths link distinct sources to the terminals \(v_c\).
Apply their literal realizations simultaneously.  Axiom 4 makes the
exchanges commute; axioms 1 and 3 preserve the functional factor and reset;
axiom 2 preserves old marks and installs every obligation.  Equation (3.2)
then marks every residual target exactly once.

Conversely, a completion obtained through pairwise disjoint paths gives an
independent representative in every list, so Rado gives (5.1).  The converse
is scoped to this exchange-network architecture, not to arbitrary global
rethreadings. \(\square\)

### Theorem 5.2 (exact defect formula)

The largest number of obligations simultaneously installable by this
network is

\[
 \min_{I\subseteq\{c_P\}}
 \left(|\{c_P\}\setminus I|+
 r_{\cal G}\left(\bigcup_{c\in I}L_c\right)\right).           \tag{5.3}
\]

Consequently the minimum uncovered number is exactly

\[
 \delta=\max_I
 \left(|I|-r_{\cal G}\left(\bigcup_{c\in I}L_c\right)\right)_+.
                                                                    \tag{5.4}
\]

#### Proof

This is the deficiency form of Rado's theorem, equivalently the standard
matroid-intersection min--max formula after adjoining one partition part
for each obligation. \(\square\)

## 6. The rank inequalities are ordinary flows

Split every vertex subject to disjointness into an in-copy and an out-copy
joined by a capacity-one arc.  Give the supersource-to-source-bank and
terminal-to-supersink arcs unit capacity as well, retaining distinct
parallel terminal phases.  Directed Menger gives

\[
                   r_{\cal G}(Y)=\operatorname {maxflow}(S,Y). \tag{6.1}
\]

Thus (5.1) is precisely the all-subfamily flow condition (0.1), and (5.4)
is an exact max-flow/min-cut defect.  This is not a generic cardinality or
entropy heuristic.  It can be certified by integral path families or by
literal vertex cuts.

A convenient stronger sufficient condition is that every obligation family
\(I\) has \(|I|\) vertex-disjoint reset-avoiding routes into
\(\bigcup_{c\in I}L_c\).  A bounded defect follows only from the quantitative
cut bound

\[
             r_{\cal G}\left(\bigcup_{c\in I}L_c\right)
             \ge |I|-C\quad\hbox{for every }I,                \tag{6.2}
\]

which gives \(\delta\le C\).  Fractional suffix balance, large raw lists,
or extension of the reset's owner columns does not imply (6.2).

## 7. What the theorem advances and what remains

The construction divides the common integral gate into three exact rows.

1. **Functional filler flow.**  Find \(F_0,\phi_0\) satisfying the Hall
   cuts (2.3), with the opened reset fixed.  This may ignore high-target
   completeness.
2. **Nested target pairing.**  Find the lower containment matching
   \(\lambda\) in (3.1).
3. **Boolean phase-router cuts.**  Build literal exchange paths satisfying
   the four axioms and prove (5.1), or the bounded-defect form (6.2).

This is strictly more structured than the original three-matroid common
base: once the filler is fixed, the joint changes of flags and the
head-owner bijection are carried by one strict gammoid, so Rado and ordinary
max flow are exact.  It is also weaker than demanding a frozen SCD table be
completed; target providers are selected prospectively through exchanges.

No current theorem supplies the functional filler or the phase-router rank
cuts uniformly in \(m\).  The authenticated independent `k=17` table is not
a filler because it has 406 universally dead tails.  The exact reset owner
matching only proves that the forced bank itself has no incidence-supply
defect.

Even after Theorem 5.1, connectedness/nonzero voltage, residence outside the
reset, arbitrary-width upper witnesses, and the terminal compiler remain
separate later rows.  In particular, (5.4) is the exact one-copy gap for
this router architecture; it must not be replaced by an inference from the
uniform fractional circulation.
