# Self-audit: upper-first named-collar layered trace flow

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Audited file:**
`MATH_THEOREM_UPPER_FIRST_NAMED_COLLAR_LAYERED_TRACE_FLOW_20260805.md`

## 1. Verdict

**GO in its fixed-order/fixed-completed-forest scope.**  The theorem is an
exact layered-path equivalence, not an existence theorem for the remaining
carrier-conditioned path.  It correctly rejects the attempted modular
quantifier reversal: the existing upper-carrier and MLD residual-forest
theorems prove nonempty marginals, not intersection with the trace-flow
relation.  Targets removed into a separately priced triangular
boundary/collar bank must first be adjoined as disjoint owner-rooted flags;
the theorem does not charge them to the MLD residual forest.

## 2. Window and length check

An order-`h` trace has `h+1` letters.  A path with `W` trace arcs spells its
initial `h` letters followed by one new terminal letter per arc, hence has
length `W+h`.  Arc `i` is exactly the source window `[i,i+h]`; adjacent arcs
share the state `(A_(i+1),...,A_(i+h))`.  Thus the layered graph has neither
an off-by-one error nor a missing endpoint window.

For the adjacent-depth application, `h=D+1`, so `W+h=W+D+1=B(k)+1` when
`D=d(k)`.

## 3. Named-cell injectivity

Inside owner `i`, strictly increasing suffix lengths give different
physical intervals.  Across owners `i!=j`, all selected suffix intervals
have respective right endpoints `i+h` and `j+h`, hence cannot be the same
cell.  Therefore pairwise distinct target labels need no second cell
matching after the trace path is selected.

The theorem does not claim that arbitrary, non-suffix lower pins share this
property.  Its exact domain is a completed owner-rooted flag system: the
named canonical residual output plus every separately priced
boundary/collar flag.

## 4. Upper transport and residence

If an upper target is `union_(i=a)^b T_i`, then the union of the overlapping
source windows is exactly the one source interval `[a,b+h]`.  No fixed-width
assumption is used, so arbitrary-width upper service of the fixed owner
order transports literally.

The path spells a nonempty source word with `D^h A=P`.  Hence it is itself
the exact residence antecedent.  The theorem does not infer path existence
from a scalar run lower bound.

## 5. Flow integrality

After `P` and the complete named forest are fixed, the only variables are
arcs of a layered directed graph.  Supersource--supersink unit flow has a
totally unimodular node--arc matrix.  Since the graph is layered, every
integral unit flow is one directed path with no residual directed cycle.

If the lower forest is not fixed, the target-once equalities are extra
colour rows.  The theorem explicitly does not assert total unimodularity of
that enlarged matrix.

## 6. Natural-pin subface

For a resident central order, the standard identity

\[
 \bigcap_{j=0}^{q}T_{i+j}=\bigcup_{p=i+q}^{i+h}E_p
\]

is exactly the corrected Shadow--Braid natural-pin formula with depth `h`.
Thus simultaneous natural interior flags are realized by the maximal
erosion word.  The note correctly leaves the final `h` owner positions and
all nonnatural opening/seam pins outside this automatic subface.

## 7. Counterexample check

For `h=2`, the unmarked word

\[
                    (\{4\},\{2\},\{1\},\{3\})
\]

has owner windows `{1,2,4}` and `{1,2,3}`.  The first declared full flag
forces its terminal trace letter to be `{1}`.  The second forces its
penultimate letter `B` to obey

\[
                         B\cup\{3\}=\{2,3\},
\]

so `2 in B subseteq {2,3}`.  Consecutive order-two traces identify these
two letters, an impossibility.  Each flag separately has a trace,
respectively `({4},{2},{1})` and `({1},{2},{3})`.  Hence the example proves
exactly the advertised local failure of marginal clockability.

It is not asserted to extend to a complete upper carrier; the theorem's
scope firewall states this explicitly.

## 8. Remaining theorem

The unresolved statement is the exact nonempty-intersection row

\[
 \exists P\in\mathcal U\ \exists\mathcal C\in\mathcal F_{\rm low}^{\rm comp}:
            s\leadsto t\text{ in }L(P,\mathcal C),
\]

including any required protected endpoint arcs.  The residual lower theorem
and the separately priced boundary construction must first give a nonempty
completed class `F_low^comp`; an upper theorem would give a nonempty class
`U`; neither proves the displayed relation.  No `B(k)+1`, `B(k)+O(1)`, or
exact all-`k` conclusion follows before this row, completion of the boundary
bank, and the all-price scalar gate are proved.
