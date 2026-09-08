# Protected rainbow-reset fragment packing

Date: 2026-07-31.

## 1. Scope

This note gives a proof-safe sufficient theorem for turning many cyclic
PBBS components into one protected linear chronology.  It simultaneously
tracks

* occurrence-labelled endpoint legality;
* exact recycling of deleted lower-\(q_1\) colours;
* internally protected and seam-served upper witnesses;
* acyclicity/connectivity; and
* the exact deadline-staircase charge of the resulting run trace.

The theorem is conditional on explicit cutwise inequalities in the guarded
port atlas.  It does **not** infer those inequalities from the number of
components or from scalar staircase slack.  This distinction is necessary:
component count and slack contain no endpoint, colour, reset, or cut-kernel
information.

The standard Aharoni--Haxell bound is recorded only as a formal comparison.
For the full component family it is numerically impossible once there are
three or more sources, so it is not the all-dimensional existence gate.

## 2. Protected fragment data

Let \(T\) be a cyclic lower-\(q_1\)-rainbow Johnson factor on \(W\)
rank-\(r\) states.  Cut at least one edge in each cyclic component.  If
\(b\) edges are cut in total, the result is a bank

\[
                     \mathcal P=\{P_1,\ldots,P_b\}
\tag{2.1}
\]

of occurrence-labelled path fragments.  Orient every fragment.  Since the
source factor is lower-rainbow, the cut colours

\[
 \Delta=\{\delta_1,\ldots,\delta_b\},\qquad
 \delta_h=U_h\cap V_h
\tag{2.2}
\]

are distinct.

Fix a proposed initial fragment \(a\), terminal fragment \(t\), and put

\[
 L=[b]\setminus\{t\},\qquad R=[b]\setminus\{a\}.
\tag{2.3}
\]

Thus \(|L|=|R|=b-1\).

For every required upper target, fix either

1. an interval witness lying wholly inside one retained fragment; or
2. a source label \(i\in L\), meaning that the selected outgoing seam from
   \(P_i\) must supply a displayed suffix--prefix witness for that target.

Write \(\mathcal U_i\) for the resulting seam-service bundle at source
\(i\).  The bundles need not be disjoint, but together with the internally
protected witnesses they must cover every required upper target.  Every
cross-seam witness carries its literal retained suffix and prefix spans.

Fix also an acyclic directed graph \(D\) on the fragments.  It is the
allowed order skeleton.  All physical seam candidates below are required to
be arcs of \(D\).

For \(i\in L\), \(j\in R\), and \(\delta\in\Delta\), call

\[
                         (i,j,\delta)
\tag{2.4}
\]

a **fully guarded port** when all of the following hold.

1. The terminal occurrence of \(P_i\) and initial occurrence of \(P_j\)
   are Johnson adjacent.
2. Their intersection colour is exactly \(\delta\).
3. The seam passes the chosen finite run-state/reset guard.
4. The seam supplies every target in \(\mathcal U_i\), with the displayed
   witness spans retained.
5. Any further protected pin or endpoint condition in the construction is
   satisfied literally.

Let

\[
 N_i(\delta)=\{j\in R:(i,j,\delta)\text{ is a fully guarded port}\}.
\tag{2.5}
\]

This is the joint object.  Separate endpoint Hall, colour Hall, service
Hall, and run-safety checks do not imply a theorem about (2.5).

## 3. Fixed-colour guarded Hall

Choose an injection

\[
                         \gamma:L\hookrightarrow\Delta.
\tag{3.1}
\]

Define the bipartite graph \(G_\gamma\) from \(L\) to \(R\) by

\[
                    i\sim j\quad\Longleftrightarrow\quad
                    j\in N_i(\gamma(i)).
\tag{3.2}
\]

### Theorem 3.1 (protected source-colour Hall theorem)

If

\[
             |N_{G_\gamma}(X)|\ge |X|
             \qquad\text{for every }X\subseteq L,
\tag{3.3}
\]

then the fragments admit one linear \(a\)-to-\(t\) chronology which

1. uses only fully guarded physical seams;
2. recycles \(b-1\) distinct members of the \(b\)-element cut-colour bank;
3. retains or supplies every protected upper target; and
4. has every selected seam separately satisfy its declared local run guard.

The resulting lower-\(q_1\) adjacency deck consists of \(W-1\) distinct
colours and omits exactly the one member of
\(\Delta\setminus\gamma(L)\).

#### Proof

Hall's theorem gives a matching saturating \(L\).  Since \(|L|=|R|\), it
also saturates \(R\).  Direct every matched edge from its source fragment to
its entry fragment.  Every fragment except \(t\) has outdegree one, every
fragment except \(a\) has indegree one, \(a\) has indegree zero, and \(t\)
has outdegree zero.  Such a degree cover is one \(a\)-to-\(t\) path plus
directed cycles.  Every selected arc belongs to the acyclic graph \(D\), so
there are no directed cycles.  Hence the cover is one spanning path.

The colours of its seams are \(\gamma(i)\), \(i\in L\), and are distinct.
The original factor had \(W\) distinct lower colours.  Cutting \(b\) edges
leaves \(W-b\) internal colours, while the path inserts \(b-1\) distinct
colours from the deleted bank \(\Delta\).  Thus all \(W-1\) final adjacency
colours are distinct and exactly one deleted colour remains absent.

Internally protected witnesses are unaffected by concatenation.  The
outgoing seam from each source \(i\) supplies its complete bundle
\(\mathcal U_i\), so all other protected targets are present.  Finally,
every selected seam was filtered by the exact run-state and pin guards.
\(\square\)

Item 4 is deliberately local.  Pairwise-safe joins need not compose to a
globally safe trace: `0|11|0` has two harmless-looking boundaries but forms
`0110`.  The composition-closed automaton hypotheses in Section 6 are what
upgrade the selected local guards to a global staircase statement.

Condition (3.3) is both necessary and sufficient after \(\gamma\), the
orientations, the fragments, and the acyclic skeleton have been fixed.  It
is a literal max-flow/min-cut condition, not a scalar palette count.

## 4. A genuine existence criterion for the colour injection

The next theorem turns existence of \(\gamma\) into a finite family of
cutwise pressure inequalities.

For \(i\in L\) and \(Y\subseteq R\), define the set of colours trapped in
\(Y\) by

\[
 B_i(Y)=\{\delta\in\Delta:N_i(\delta)\subseteq Y\}.
\tag{4.1}
\]

For \(X\subseteq L\), let

\[
 R(X,Y)=
 \#\{\phi:X\hookrightarrow\Delta:
             \phi(i)\in B_i(Y)\text{ for every }i\in X\}.
\tag{4.2}
\]

Write \((b)_s=b(b-1)\cdots(b-s+1)\).

### Theorem 4.1 (random-injection Hall-cut criterion)

If

\[
 \boxed{
 \sum_{s=1}^{b-1}
 \ \sum_{\substack{X\subseteq L\\ |X|=s}}
 \ \sum_{\substack{Y\subseteq R\\ |Y|=s-1}}
       \frac{R(X,Y)}{(b)_s}<1,}
\tag{4.3}
\]

then some injection \(\gamma:L\hookrightarrow\Delta\) satisfies (3.3),
and hence Theorem 3.1 applies.

A coarser but simpler sufficient inequality is obtained from

\[
                     R(X,Y)\le
                     \prod_{i\in X}|B_i(Y)|.
\tag{4.4}
\]

#### Proof

Choose \(\gamma:L\hookrightarrow\Delta\) uniformly.  For fixed \(X,Y\),
the restriction \(\gamma|_X\) is uniform among the \((b)_{|X|}\)
injections from \(X\) to \(\Delta\).  Therefore

\[
 \Pr\bigl(\gamma(i)\in B_i(Y)\text{ for all }i\in X\bigr)
       =\frac{R(X,Y)}{(b)_{|X|}}.
\tag{4.5}
\]

If Hall fails, some nonempty \(X\subseteq L\) has
\(|N_{G_\gamma}(X)|\le |X|-1\).  Extend this neighbour set, if necessary,
to a set \(Y\subseteq R\) of size exactly \(|X|-1\).  Then every colour
\(\gamma(i)\), \(i\in X\), is trapped in \(Y\), so the event in (4.5)
occurs.  The union bound and (4.3) show that Hall failure has probability
strictly less than one.  Inequality (4.4) simply forgets injectivity while
counting the admissible restrictions. \(\square\)

This is an honest probabilistic theorem.  It may be strengthened with exact
rook-polynomial counts in (4.2).  No useful bound on (4.3) follows from
\(b\), the Catalan number, or scalar slack alone.

## 5. Atomic port-pressure alternative

There is also a direct local-lemma route which does not preassign colours.
For source \(i\), let

\[
 \mathcal A_i=\{(j,\delta):j\in N_i(\delta)\}
\tag{5.1}
\]

be its fully guarded port domain.  Choose one member independently and
uniformly from each \(\mathcal A_i\).  A bad event specifies choices at two distinct
sources which use the same entry or the same colour.

Let

\[
 m=\min_i|\mathcal A_i|
\tag{5.2}
\]

and let \(\Gamma\) be the maximum number of other bad events sharing a
source variable with one bad event.  After deleting unary failures, the
symmetric local lemma gives the proof-safe criterion

\[
                         e(\Gamma+1)\le m^2.
\tag{5.3}
\]

Indeed, every bad event has probability at most \(m^{-2}\), and events on
disjoint source variables are independent.  Avoiding all bad events chooses
distinct entries and distinct colours.  Since there are \(b-1\) sources
and \(b-1\) entries, every entry is used, and acyclicity of \(D\) again
gives one spanning path.

The exact candidate-pressure criterion in
`MATH_THEOREM_K_COMMON_CAP_ATOMIC_PRESSURE_AND_CUT_DUAL_20260731.md`
applies verbatim and can be much sharper than (5.3).  Here its conflict
clutter has rank two: same-entry and same-colour pairs.  Neither (5.3) nor
the atomic pressure inequalities follow from the component count.

### Why the generic Aharoni--Haxell condition is not the gate

For comparison, make a graph \(\mathcal H_i\) on the vertex set
\(R\mathbin{\dot\cup}\Delta\), with edge \(\{j,\delta\}\) for every
fully guarded port at source \(i\).  The standard two-uniform
Aharoni--Haxell sufficient condition is

\[
 \nu\!\left(\bigcup_{i\in X}\mathcal H_i\right)
                >2(|X|-1)
 \qquad(\varnothing\ne X\subseteq L).
\tag{5.4}
\]

It is formally correct, but for \(X=L\) the matching number on
\(R\mathbin{\dot\cup}\Delta\) is at most \(|R|=b-1\).  Condition (5.4)
would require

\[
                       b-1>2(b-2),
\tag{5.5}
\]

which fails for every \(b\ge3\).  Thus (5.4) cannot certify a large full
fragment bank.  The fixed-colour Hall theorem, the injection cut criterion,
or a candidate-specific atomic-pressure proof is required instead.
The coefficient two is valid here because the source exit is the private
family index and the only shared matching resources are one entry and one
colour.  If a candidate consumes two globally shared physical ports as well
as a colour, its resource edge has rank three and the Aharoni--Haxell
coefficient is three.

## 6. Exact halo charge

Let \(d\) be the active staircase depth.  For one coordinate, a positive
run of length \(\ell\) is the forbidden word \(01^\ell0\).  The DFA which
forbids lengths \(1,\ldots,d-1\) has live states

\[
                 \epsilon,0,01,\ldots,01^{d-1}.
\tag{6.1}
\]

Reading \(1^d\) from any live state returns to \(\epsilon\).  Hence a
fragment whose first \(d\) states all contain every coordinate in the exit
danger set is a universal **incoming-boundary** reset port for all runs
shorter than \(d\).  The fragment's internal trace and its outgoing
transition must still be accepted by the same DFA.  The same statement with
\(d+1\) incoming ones resets the DFA which also forbids length \(d\), again
subject to internal and outgoing acceptance.  These are finite
occurrence-level guards, not a substitute for composition.

Fix an initial ideal \(B\) of the acyclic skeleton \(D\):

\[
                E_D([b]\setminus B,B)=\varnothing,
                \qquad a\in B,
\tag{6.2}
\]

and, unless \(B=[b]\), require \(t\notin B\).  Put

\[
                         M=\sum_{i\in B}|P_i|.
\tag{6.3}
\]

Assume the exact fragment and seam automata guarantee:

1. the full selected chronology has no internal positive run of length
   smaller than \(d\); and
2. after the path first leaves \(B\), its remaining suffix has no internal
   positive run of length at most \(d\).

The reset-core tests above are a strong finite sufficient way to impose
these conditions.  Exact partial transition maps may admit more arcs.

### Lemma 6.1 (halo debt lemma)

Every spanning path selected by Theorem 3.1 and satisfying (6.2) exhausts
all fragments of \(B\) before leaving it.  Its exact terminal-start
staircase debt satisfies

\[
                         \mathfrak D_d(T)\le M.
\tag{6.4}
\]

Consequently the chronology has a scalar-feasible depth-\(d\) deadline
staircase whenever

\[
                              M\le s(k).
\tag{6.5}
\]

#### Proof

The selected path starts in \(B\).  Once it leaves \(B\), (6.2) forbids a
return.  Since it is spanning, it must therefore visit every fragment of
\(B\) before its first exit.  Hence \(B\) occupies the first exactly \(M\)
physical middle positions.

By assumption there are no runs of lengths below \(d\).  A length-\(d\)
run can begin at zero-based index \(M\), because it is then a boundary run
of the suffix rather than an internal suffix run, but none can begin later.
In the exact latest-start notation this says

\[
                    \rho_j=0\ (j<d),\qquad \rho_d\le M.
\tag{6.6}
\]

Therefore \(\mathfrak D_d(T)=\sum_{j=1}^d\rho_j\le M\).  A
boundary-aware suffix guard excluding a start at \(M\) gives the sharper
\(M-1\), but that strengthening is not used.  The exact fixed-chronology
staircase theorem says that \(\mathfrak D_d(T)\le s(k)\) is necessary and
sufficient for scalar deadline feasibility with terminal omitted starts.
\(\square\)

This is stronger than charging every seam.  Arbitrarily many colours may be
recycled outside the halo at zero staircase charge, provided their exact
run-state transitions are clean.

## 7. Combined protected-fragment theorem

### Theorem 7.1 (protected rainbow-reset packing)

Assume the protected fragment data of Section 2 and the halo data of
Section 6.  Suppose at least one of the following selection certificates
holds:

1. an injection \(\gamma\) satisfying all Hall cuts (3.3);
2. the random-injection cut sum (4.3); or
3. the literal atomic port-pressure criterion, in particular the symmetric
   sufficient condition (5.3).

If \(M\le s(k)\), then there is one linear chronology on all \(W\) middle
states such that

* every seam is a literal Johnson seam in the protected atlas;
* its lower-\(q_1\) deck is rainbow with exactly the one forced boundary
  colour absent;
* every internally protected or seam-assigned upper target is present; and
* its exact minimum terminal-start staircase debt is at most \(M\).

If the resulting staircase additionally passes the integral common-cap
compiler, it gives the corresponding literal contiguous-OR word.  This last
condition is independent: endpoint routing and scalar deadline feasibility
do not imply common-cap integrality.

#### Proof

Certificate 1 gives Theorem 3.1 directly.  Certificate 2 supplies a
certificate-1 injection by Theorem 4.1.  Certificate 3 supplies a
collision-free choice of one fully guarded port at every source; distinct
entries and colours give the same degree-correct cover as in Theorem 3.1,
and the acyclic skeleton makes it one path.  The lower and upper conclusions
are Theorem 3.1, and the staircase conclusion is Lemma 6.1.  The common-cap
statement is exactly the terminal compiler theorem. \(\square\)

## 8. Catalan factor-three arithmetic

For PBBS on \(2m+1\) coordinates, write

\[
 C=\operatorname{Cat}_m,\qquad
 c=\#\{\text{PBBS components}\},qquad
 a=\#\{\text{minimum-period components}\}.
\tag{8.1}
\]

Odd normalized periods give

\[
                         C\ge a+3(c-a),
\tag{8.2}
\]

and hence

\[
 \boxed{
 c-a\le\left\lfloor\frac{C-a}{3}\right\rfloor,
 \qquad
 c\le a+\left\lfloor\frac{C-a}{3}\right\rfloor
       \le\frac{C+2a}{3}.}
\tag{8.3}
\]

Suppose a protected fragmentation has the following **closure-aware
unit-halo property**.  For each original PBBS component \(Q\), count every
fragment of \(Q\) which lies in the entire initial ideal \(B\), including
uncharged predecessors forced into its downward closure.  Require

\[
 \sum_{\substack{i\in B\\P_i\subset Q}}|P_i|
 \le
 \begin{cases}
 1,&Q\text{ nonminimum},\\
 \eta,&Q\text{ minimum-period}.
 \end{cases}
\tag{8.4}
\]

Then, summing over original components and using (8.3),

\[
 \boxed{
 M\le(c-a)+\eta a
   \le\frac{C-a}{3}+\eta a
   =\frac C3+\left(\eta-\frac13\right)a.}
\tag{8.5}
\]

Consequently:

1. If minimum-period components are reset-clean and have zero halo charge
   (\(\eta=0\)), then
   \[
                         M<\frac C3.
   \tag{8.6}
   \]
   Therefore the scalar inequality \(s(k)>C/3\) pays the complete halo.
2. If every component has unit charge (\(\eta=1\)), only
   \[
                         M\le\frac C3+\frac{2a}{3}
   \tag{8.7}
   \]
   follows.  The hypothesis \(s(k)>C/3\) alone is insufficient for a
   conclusion from the factor-three estimate alone.  That estimate
   guarantees payment if the quantified extra gap
   \[
                         s(k)-\frac C3\ge\frac{2a}{3},
   \tag{8.8}
   \]
   holds; an actual smaller component/halo census or a zero-charge treatment
   of the minimum cycles may require less.

### Corollary 8.1 (global scalar discharge, with its exact hypothesis)

Assume \(s(k)>C/3\), the closure-aware unit-halo property with \(\eta=0\),
and any one of the three routing certificates in Theorem 7.1.  Then the
halo part of the
exact staircase gate is automatic: \(\mathfrak D_d(T)\le M<s(k)\).
Thus, under these hypotheses, arbitrarily many additional reset-clean
fragment seams cost no scalar staircase units.  Protected upper service and
the terminal common-cap compiler remain separate literal gates.

When \(\eta=0\), condition (8.4) also forces the initial fragment \(a\) to
come from a nonminimum component, because \(a\in B\).  This is part of the
literal hypothesis, not a consequence of the period census.

This exceptional term cannot be deleted by calling \(a\) small.  A uniform
upper bound strong enough for that step has not been proved, and known
minimum-period families are already superpolynomial on subsequences.

The component estimate controls only the possible halo length in (8.5).
It does not imply any of the guarded Hall cuts, colour-injection cuts,
upper-witness protections, or common-cap cuts in Theorem 7.1.

Nor is \(s(k)>C/3\) a uniform arithmetic fact.  The exact terminal-plateau
counterexamples \((m,d)=(225669,421)\) and \((691583,737)\), together with
the noncritical-plateau theorem, are proved in
`MATH_THEOREM_K_GLOBAL_PBBS_SLACK_COMPONENT_PACKAGING_20260731.md`.

## 9. Sharp abstract obstructions

### 9.1 Marginal endpoint and colour Hall do not combine

Take two source families, two entries \(u,v\), and two colours
\(\alpha,\beta\).  Let

\[
 \begin{aligned}
 \mathcal A_1&=\{(u,\alpha)\},\\
 \mathcal A_2&=\{(v,\alpha),(u,\beta)\}.
 \end{aligned}
\tag{9.1}
\]

The two source families jointly see both entries and both colours, and both
marginal source--resource graphs satisfy Hall.  Nevertheless every choice
of one pair from each family repeats an entry or repeats a colour.  Thus
there is no rainbow degree cover.  This is the smallest joint port
obstruction by numbers of sources and resource vertices.  It is certified
by checking that every colour injection fails the exact Hall condition
(3.3), or directly by the atomic conflict CSP.  The union-bound criterion
(4.3) is sufficient only; failure of its inequality is not an UNSAT
certificate.

### 9.2 Component count and slack do not create ports

For any \(c\) and any scalar budget, one can take \(c\) individually clean,
upper-complete fragments and declare that no pair of physical endpoints is
a legal Johnson-reset seam.  All component and staircase counts remain
unchanged, but the singleton Hall cut fails.  More subtly, the legal port
graph may split across a nontrivial component cut, or every legal seam may
carry one common colour.  These examples retain arbitrarily large scalar
slack and still admit no protected braid.

### 9.3 Minimum-period components are a real arithmetic interface

Even if every component requires only one charged owner, the extremal
factor-three count permits \((C+2a)/3\) charges.  A slack value just above
\(C/3\) need not pay the extra \(2a/3\).  Action--angle period data alone do
not imply that a minimum-period component has a reset-clean opening: cyclic
binary traces of the same length and coordinate occupancy can have entirely
different short-run profiles.

## 10. Exact remaining carrier invariant

The positive theorem isolates the required additional structure:

> **Protected reset-rainbow port expansion.**  Find occurrence-labelled
> cuts and fragment orientations for which all upper witnesses are internal
> or assigned to literal seam bundles, the fully guarded port atlas admits
> a colour injection satisfying every Hall cut (or passes the atomic
> pressure criterion), and all charged short-run starts can be detached into
> a closure-aware initial halo satisfying (8.4).

At the scalar level, whenever the additional inequality
\(s(k)>\operatorname{Cat}_m/3\) holds, the factor-three PBBS census pays the
nonminimum unit halo.  The two
unproved carrier assertions are precisely

1. reset-rainbow cutwise expansion of the occurrence-labelled port atlas;
2. zero-charge, or explicitly budgeted, handling of the minimum-period
   components.

No LLL, nibble, or scalar component estimate can replace these assertions
without additional literal degree/codegree and cut-kernel bounds.
