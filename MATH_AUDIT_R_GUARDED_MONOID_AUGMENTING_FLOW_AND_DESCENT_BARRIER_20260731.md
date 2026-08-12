# Adversarial audit: guarded monoid augmenting flow and descent barrier

Date: 2026-07-31  
Audited file:
MATH_THEOREM_R_GUARDED_MONOID_AUGMENTING_FLOW_AND_DESCENT_BARRIER_20260731.md  
Method: independent symbolic replay by three proof lanes; no finite search,
SAT, web use, or certificate data.

## 0. Overall verdict

**VALID WITH EXPLICIT HYPOTHESES.**

The main positive statement is not an automatic theorem about the complete
marked-preserving exchange catalogue.  It is an exact theorem once one
proves either:

* a serializable nonbranching unit-debt network; or
* a joint guard matroid, normally a strict gammoid, on already closed
  factor-feasible repair macros.

Under those hypotheses, the max-flow/min-cut and Rado formulas are correct,
and completed paths/batches strictly reduce the declared weighted terminal
defect.  Without them, strict local descent and ordinary Hall are false.

The counterexamples were independently reconstructed.  Their scope is
important: they refute deductions from finite monoid structure alone; they
do not prove that the actual PBBS catalogue contains the same obstruction.

The \(B(k)+O(1)\) corollary is valid only with literal-weighted leave,
protected deeper witnesses, a terminal common cap, and regeneration of the
carried sidecar state.  A bounded family of terminal middle masks may be
appended, but missing owners or palette data needed by the next Pascal step
cannot be paid this way.

## 1. Two-toggle table

For the two independent \(K_{2,2}\) blocks, the selected labels are:

\[
\begin{array}{c|c}
A_0&c,d\\
A_1&a,b\\
B_0&a,\varnothing\\
B_1&c,d .
\end{array}
\]

Taking unions gives:

\[
\begin{array}{c|c|c}
00&\{a,c,d\}&\text{hole }b\\
10&\{a,b\}&\text{holes }c,d\\
01&\{c,d\}&\text{holes }a,b\\
11&\{a,b,c,d\}&\text{no hole}.
\end{array}
\]

Every block state is a perfect matching, so both \(C_4\) toggles preserve
all resource degrees.  The run state is constant and clean.  Therefore:

* initial deficiency is one;
* both elementary moves have deficiency two; and
* the two-move compound has deficiency zero.

**Verdict: valid.**

The Boolean-union label is the support quotient of a provider-multiplicity
monoid.  It is not asserted to arise from the literal PBBS interval
geometry.  Accordingly, the result refutes a theorem based only on finite
run/shadow monoid axioms, not a stronger theorem using a proved special
PBBS expansion law.

## 2. Minimality and arbitrary radius

For two binary blocks write their contribution sets as \(A_i,B_j\).  If the
target universe has at most three elements and each single-toggle state has
deficiency at least two, then

\[
              |A_1\cup B_0|\le1,\qquad
              |A_0\cup B_1|\le1.
\]

Hence \(|A_1|\le1\), \(|B_1|\le1\), and their union cannot cover a
three-target universe.  Four labels in the displayed example suffice.

**Verdict: valid in the stated two-toggle, unweighted union-monoid class.**
No broader minimality is claimed.

For the radius-\(r\) construction, \(\alpha\) is absent exactly at the zero
state.  For every nonzero proper \(s\), each copy of \(\beta_s\) is absent
exactly when all coordinates equal \(s\): block \(i\) provides it precisely
when \(z_i\ne s_i\).  Thus zero has one hole, each nonzero proper state has
two, and the all-one state has none.  A support-\(r\) move cannot change all
\(r+1\) bits.

**Verdict: valid.**  This decisively rules out a dimension-uniform
bounded-support strict-descent theorem without another structural
hypothesis.

## 3. Literal Johnson balance check

All six displayed owner pairs are Johnson adjacent:

\[
\begin{array}{c|c}
AX,BX&12\\
BY,CY&14\\
CZ,AZ&13.
\end{array}
\]

The exchange divergences are

\[
                 -A+B,\quad -B+C,\quad -C+A.
\]

Their \(0\)-\(1\) sum is zero exactly when all three coefficients agree.
The nonempty balanced choice is the complete alternating cycle

\[
                         A-X-B-Y-C-Z-A.
\]

**Verdict: valid.**  This proves that raw same-colour exchange columns are
not a hereditary system and cannot automatically be the ground set of a
guard matroid.

## 4. Sublevel-cut theorem

By definition, a path has barrier at most \(h\) exactly when every vertex
lies in the induced subgraph

\[
             \Phi\le\Phi(x)+h.
\]

Reachability in that graph is therefore necessary and sufficient.  If no
accepting vertex is reachable, the reachable set and its outgoing boundary
are a literal directed cut.

For nonnegative arc cost, Bellman's equation gives a nonincreasing
cost-to-go \(J\).  Tying by minimum remaining hop count makes
\((J,\ell)\) strictly decreasing along an optimal path, including across a
zero-cost arc.  If \(J=\infty\), the full reachable set is forward-closed
and contains no accepting state.

**Verdict: valid.**  This is the unconditional potential-or-cut theorem.
Its potential is globally computed; it is not the raw replay/upper count.

## 5. Unit-debt flow theorem

The max-flow theorem uses four hypotheses that cannot be omitted:

1. one live token is transported to at most one successor token;
2. every source-to-sink path decodes to a closed factor-feasible compound;
3. every capacity-feasible path family commutes physically; and
4. all provider, deep-shadow, topology, and cap resources appear in the
   network state or as protected guards.

For the converse and the min-cut no-go, one further scope condition is
necessary: every simultaneous repair admitted by the declared atlas must
decompose into represented paths.  Resource vertices are vertex-split, and
the super-source has one capacity-one arc to each packet source.

With these hypotheses, integral max-flow gives a set of physical compounds,
and max-flow/min-cut is exact.  Integral min-cost flow gives the cheapest
full repair.  Allowing a drop arc of cost \(w(o)\) yields an integral
lexicographic optimum for weighted leave and then physical/cap cost.

The deficiency formula

\[
 \delta=\max_X\bigl(|X|-\lambda(X,t)\bigr)
\]

is the usual super-source cut formula: a super-source cut has capacity
\(m-|X|+\lambda(X,t)\), so \(m-\operatorname{maxflow}=\delta\).

**Verdict: valid after the theorem's explicit atlas-completeness clause.**
Without completeness, a full flow is still sufficient, but a min-cut
excludes only repairs represented by the network, not every physical
repair.

The two-toggle counterexample violates precisely the nonbranching
hypothesis: one toggle repairs one label while exposing two.  A path model
which silently drops one of those casualties would be unsound.

## 6. Rado and exact deficiency formula

For a matroid \(M\) on closed macros and candidate sets \(A_i\), Rado's
condition

\[
 r_M\left(\bigcup_{i\in X}A_i\right)\ge |X|
\]

is exactly the independent-transversal criterion.

For the partial formula, let

\[
 d=\max_X\left(
 |X|-r_M\left(\bigcup_{i\in X}A_i\right)
 \right).
\]

Adding \(d\) free dummy elements in direct sum with \(M\), and placing all
of them in every candidate set, raises every relevant rank by \(d\).
Rado gives a full extended transversal; at most \(d\) representatives can
be dummy.  This proves at least \(m-d\) genuine representatives.  The
maximizing set \(X\) gives the matching upper bound.

The rank increase statement is for nonempty \(X\); the empty-set Rado
inequality is \(0\ge0\) and is handled separately.

**Verdict: valid.**

The weighted problem is integral weighted matroid intersection on the pair
ground, using a partition matroid for packets and a parallel extension of
\(M\) for duplicate macro copies.

The contraction estimate under
\(r(A(X))\ge\gamma|X|\) is also correct when packets partition the active
unit defects and each packet has size at most \(L\): there are at least
\(\Phi/L\) packets, at least a \(\gamma\) fraction are repaired, and each
removes at least one defect.

## 7. Joint-safety warning

If a protected target has two providers and two switches each withdraw a
different provider, each switch alone is safe.  Selecting both uncovers the
target even if their obligation-to-switch graph has a perfect matching.

**Verdict: valid.**  Individual monoid derivatives plus ordinary Hall do
not imply joint safety.  Withdrawal tickets, a joint guard matroid, or the
complete state graph are necessary.

This same issue applies to cap halos and topology transitions.  Pairwise
disjoint incidence supports alone do not prove that fragment permutations
serialize to one chronology.

## 8. Truncation and common-cap scope

A fixed \(\mathcal U_h\) controls only target ranks at most \(h\).  For an
all-\(k\) implication, one must either let \(h=h(k)\) include every
damageable rank, or protect every higher target by a support-avoiding
witness with enough batch withdrawal capacity.

Current absence of holes above \(h\) is not a protected-witness theorem.

The five-row common-cap transport lemma starts from an exact cap.  The
current OPTIMAL28 zipper has unhosted replay obligations, hence no exact
cap available for transport.  A prospective cap fibre may instead be
carried in the expanded state, or the final chronology may invoke a new
exact terminal cap recourse.

**Verdict: correctly scoped.**

## 9. Additive-constant implication

Once a physical word of length \(B(k)+c_k\) misses only a family of
distinct literal masks, appending one letter per missing mask proves the
stated upper bound.  The packet weight must bound that number of distinct
masks, not merely packet count.  Accordingly, every unresolved packet must
export an explicit casualty set \(T(o)\), \(|T(o)|\le w(o)\), and literal
replay must show that every target outside the union of these sets and the
declared terminal holes remains covered.  Replay exactness outside the
packet supports alone would not control cascaded loss of upper providers.

The added middle-hole term is valid: exact central ownership is not needed
for \(B(k)+O(1)\) if only \(O(1)\) terminal middle masks are missing.
However, if the missing owner/palette data is part of the sidecar used to
construct the next child, appending terminal letters does not regenerate
it.  That carried state must still satisfy the uniform invariant.

**Verdict: valid and consistent with Corollary 1.3 of the bounded-defect
regenerative-spine theorem.**

One unresolved run packet may correspond to \(d(k)\) missing literal
middle masks.  Therefore a constant unweighted Hall deficiency can yield
only \(B(k)+O(\sqrt k)\); the literal-weighted condition is essential.

## 10. \(K17\) interpretation

The frozen residual-pair skeleton has literal isolated obligations
(internal runs and 218 static rank-ten holes), so it fails even the first
post-guard expansion preflight.

The broader 545721-column marked-preserving catalogue gives individual
rank-ten support, but its raw columns are not closed degree-balanced
packets.  No serializable unit-debt network, joint guard matroid, weighted
cut, cap budget, or regenerative export has been proved for it.

The current counts

\[
3759,\quad 1900,\quad 911,\quad 128,\quad 3293
\]

are therefore calibration only.  In particular \(3293\) is not a joint
cap/upper-repair theorem, and the unweighted total \(6698\) is not a
terminal literal-hole bound.

**Verdict: no \(K17\) or all-\(k\) conclusion is overclaimed.**

## 11. Final proved/conditional boundary

Proved:

* finite exact monoid signatures for auditing switch effects;
* failure of strict atomic and all fixed-radius descent;
* exact state-sublevel repair/cut duality;
* exact flow/Rado repair and min-cost duality under declared
  serializability/joint-guard hypotheses;
* literal-weighted bounded-defect completion, including bounded terminal
  middle defects.

Still open:

* a PBBS/Pascal family satisfying serializable guarded expansion;
* a uniform literal-weighted cut bound and cap cost;
* protected all-depth witnesses under the selected batch; and
* regeneration of the exported central/palette/common-cap sidecar.
