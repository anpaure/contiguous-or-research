# K17 common-basis/phase-DNF supplier separation

Date: 2026-08-02

Status: proof-safe structural theorem and generator-audit contract.  The
polynomial oracle below applies after a literal common-basis representation
and its two-phase state choices are fixed.  It does not turn the projected
common-basis/root-recourse problem into one min-cut.  No chronology,
residence, compiler, or word conclusion is claimed.

## 1. Parent and fixed-cut scope

The relevant compressed root layer is the common-basis representation

\[
 C\in {\cal B}(M_L)\cap
 {\cal B}\!left(M_7^*\oplus U_{16915,M}\right),
 \qquad B=R\setminus C_R,
 \tag{1.1}
\]

together with literal representing matchings
\(\mu_7\) (rank-seven targets into \(B\)) and \(\mu_L\) (low targets into
\(C\)).  Basis membership alone does not choose either matching.

On the fixed strict-\(bf5b\) representation, the authenticated supplier
relaxation has optimum deficiency 40.  Its decisive lifted Hall template is a
set \(P\) of 50 potential head requirements.  For a complete final state
\(\theta\), write

\[
 a_h(\theta)=1 \quad\Longleftrightarrow\quad
 h\text{ is an active hard-head occurrence},
 \tag{1.2}
\]

and let \(e_{hu}(\theta)\) be the literal incidence of active head \(h\) with
supplier identity \(u\).  Define the distinct-neighbor credit

\[
 b_{Q,u}(\theta)
 =\bigvee_{h\in Q}\bigl(a_h(\theta)\wedge e_{hu}(\theta)\bigr).
 \tag{1.3}
\]

The fixed-root mode face exposes at most ten credits for \(P\); a ten-mode
witness attains ten, while target deficiency 39 is DRAT-UNSAT.  Root
recoupling must therefore supply 40 net additional credits in the same
literal 50-head inequality.  This is a credit bound, not a count of basis
exchanges or root actions.

Every table, ticket-incidence value, supplier graph, phase DNF, and transfer
mode used below must be generated from one literal parent.  A row-footprint
filter across different parents is not a common-parent contract.

## 2. Complete lifted states

A complete lifted state is

\[
 \theta=(C,\mu_7,\mu_L,z,g,\omega),
 \tag{2.1}
\]

where:

1. \(C\) is the common basis in (1.1);
2. \(\mu_7,\mu_L\) are literal representing matchings of that same basis;
3. \(z\) is the row-disjoint transfer/mode choice on the same materialized
   parent;
4. \(g\) chooses one declared \((q,\alpha,\beta)\) state for every supported
   global short role; and
5. \(\omega\) chooses one compatible occurrence in each transported phase,
   with phase-specific predecessor/successor row capacity, protected-row
   exclusion, and all dynamic row-state prerequisites.

The declared state \(g\) is shared between the two phases.  The literal
predecessor and successor rows in \(\omega\) need not be shared.  A state
whose incidence menu is incomplete is not a complete lifted state until its
active-set pricing is finished.

Materializing \(\theta\) gives one bipartite supplier graph

\[
 G_\theta=(H_\theta,U;E_\theta).
 \tag{2.2}
\]

This placement of \(\mu_7,\mu_L,g,\omega\) inside \(\theta\) is essential:
they are not consequences of the set \(C\) alone.

## 3. Exact polynomial oracle after lifting

For \(Q\) in a fixed universe of labelled potential heads, put

\[
 \Delta_Q(\theta)
 =\sum_{h\in Q}a_h(\theta)
  -\sum_{u\in U}b_{Q,u}(\theta),
 \qquad
 \Delta(\theta)=\max_Q\Delta_Q(\theta).
 \tag{3.1}
\]

### Theorem 3.1 (integral lifted Hall separator)

For a complete integral state \(\theta\) and target supplier deficiency
\(d\), the following are equivalent:

\[
 \nu(G_\theta)\ge |H_\theta|-d,
 \tag{3.2}
\]

\[
 \Delta(\theta)\le d,
 \tag{3.3}
\]

and, for every labelled set \(Q\),

\[
 \boxed{
 \sum_{h\in Q}(1-a_h(\theta))
 +\sum_{u\in U}b_{Q,u}(\theta)
 \ge |Q|-d.}
 \tag{3.4}
\]

One maximum bipartite matching, equivalently one unit-capacity max-flow and
its residual minimum cut, either certifies (3.2) or returns a violated set
\(Q\).  Hence separation is polynomial in the explicitly materialized
supplier graph.  For a predeclared set such as the 50-head template \(P\),
evaluating (3.4) is linear in the explicit incidence/DNF size.

#### Proof

For the active vertices in \(Q\), Hall deficiency is
\(|Q\cap H_\theta|-|N_\theta(Q\cap H_\theta)|\).  Equations (1.2)--(1.3)
write these two cardinalities as the two sums in (3.1).  The deficiency form
of Hall's theorem gives (3.2)--(3.3); rearranging gives (3.4).  The usual
alternating reachability set of a maximum matching supplies a maximizing
Hall shore. \(\square\)

For the exact 50-head cut and supplier perfection, (3.4) is

\[
 \boxed{
 \Gamma_P(\theta):=
 \sum_{h\in P}(1-a_h(\theta))
 +\sum_{u\in U}b_{P,u}(\theta)\ge50.}
 \tag{3.5}
\]

The best fixed-root state has \(\Gamma_P=10\), so any completion on that
reference must gain 40 net credits.  Lost old neighbors count negatively.

### Corollary 3.2 (exact Boolean compilation of one Hall row)

Suppose every atom in (3.5) is exposed by an exact Boolean circuit over the
same complete state \(\theta\).  Create:

- one term \(I_h\leftrightarrow\neg a_h\) for each labelled head \(h\in P\);
- one term
  \(B_u\leftrightarrow\bigvee_{h\in P}(a_h\wedge e_{hu})\) for each supplier
  identity \(u\) that can occur; and
- the cardinality row
  \(\sum_{h\in P}I_h+\sum_u B_u\ge50\).

Then the Boolean row is equivalent to (3.5).  Its size is polynomial in the
explicit phase-valid DNF catalogue.  Multiple DNF alternatives for the same
supplier belong inside one \(B_u\); they are not separate credits.

This is the strongest polynomial separator furnished by Hall: the input must
already be one complete integral representation/state, or the corresponding
semantic atoms must already be present in the master.

## 4. Projection obstruction at common-basis level

Let \(v\) retain only a compressed master choice, for example common-basis
membership and transfer modes, and let \({\cal R}(v)\) be its compatible
representing matchings, root completions, and phase occurrences.  The exact
projected deficiency is

\[
 \delta_\exists(v)
 =\min_{r\in{\cal R}(v)}\ \max_Q\Delta_Q(v,r).
 \tag{4.1}
\]

### Theorem 4.1 (representation-recourse obstruction)

If two completions \(r_1,r_2\in{\cal R}(v)\) of the same projected point
have different head activity or supplier incidence on some Hall shore, then:

1. \(\Gamma_P\) and the full supplier graph are not functions of \(v\);
2. a Hall failure of \((v,r_1)\) is not a valid no-good for \(v\); and
3. an exact separator in the projected variables must itself decide (4.1),
   rather than run a min-cut on one arbitrary completion.

#### Proof

The same projected point has two different values of a purported projected
Hall expression, proving item 1.  If \(r_2\) is supplier-feasible, excluding
\(v\) because \(r_1\) fails excludes a feasible lifted state, proving item 2.
By definition, membership of \(v\) in the supplier-feasible projection is
the existential question whether the minimum in (4.1) is at most the target
deficiency, proving item 3. \(\square\)

The hypothesis holds here.  A transversal-matroid basis can have several
representing matchings; changing an alternating representation can change
literal physical rows and supplier incidences without changing \(C\).  The
same issue occurs for a declared common phase state with several occurrence
tuples.

The quantifier order cannot be exchanged.  With two recourse completions and
two shores, the deficiency table can be

\[
\begin{array}{c|cc}
 &Q_1&Q_2\\\hline
r_1&1&0\\
r_2&0&1
\end{array}.
\tag{4.2}
\]

This is realized by two disjoint two-head components: in \(r_1\) only the
first pair shares one supplier, and in \(r_2\) only the second pair shares
one supplier.  Thus

\[
 \min_r\max_Q\Delta_Q(r)=1
 \quad\text{but}\quad
 \max_Q\min_r\Delta_Q(r)=0.
 \tag{4.3}
\]

Cut-by-cut repair with independently chosen recourse is therefore not exact.

### Consequence 4.2 (the proof-safe architecture)

There are exactly two proof-safe choices with the current abstractions:

1. **Lift the recourse.**  Put \(\mu_7,\mu_L\), shared-state groups, literal
   phase occurrences, and the semantic head/supplier incidence gates in the
   integer master.  Common-basis feasibility is handled by Edmonds
   two-matroid intersection or its representing matching flows; after every
   integral candidate, Theorem 3.1 supplies a polynomial Hall slave.
2. **Use full branch--Benders.**  Keep some representation/root choices in a
   slave, but accept a cut only when an authenticated oracle proves it valid
   for every residual completion of the master assignment.  Failure of one
   chosen completion is only a request for another completion, not a cut.

Weighted matroid intersection does not remove this distinction.  It handles
additive element weights on the common basis.  The credits in (3.5) are ORs
of representation- and phase-dependent incidences and are not additive
weights on \(C\).

This is a formulation theorem, not a general complexity lower bound.  The
known determinant-two socket minor and the known nonmatroid counterexample
rule out the current natural TU/matroid collapse; they do not prove that no
larger polynomial extended formulation can ever exist.

## 5. Why fractional marginal flow is not an exact substitute

If fractional head/edge activations are treated merely as capacities, one
can separate the resulting capacitated-flow relaxation by a min-cut.  More
precisely, give \(s\to h\) capacity \(b_h\), \(h\to u\) capacity
\(p_{hu}\), and \(u\to t\) capacity 1.  Flow deficiency at most \(d\) is
equivalent to

\[
 \boxed{
 \sum_{h\in Q}b_h
 \le d+|S|+
 \sum_{\substack{h\in Q\\u\notin S}}p_{hu}
 \quad\text{for all }Q\subseteq H,\ S\subseteq U.}
 \tag{5.1}
\]

Minimizing the right side over \(S\) gives

\[
 \sum_{h\in Q}b_h
 \le d+\sum_u\min\!\left\{1,\sum_{h\in Q}p_{hu}\right\}.
 \tag{5.2}
\]

One minimum cut separates (5.1).  For Boolean incidences, (5.2) is Hall's
inequality and agrees with Theorem 3.1.  For fractional phase-DNF marginals,
it is only a relaxation because it forgets common-state correlation.

For example, take two heads and two suppliers.  In state \(A\), both heads
see only supplier 1; in state \(B\), both see only supplier 2.  Each integral
state has deficiency one.  The half-mixture gives every head a half-edge to
each supplier, and a marginal capacitated flow sends one total unit through
each supplier and falsely saturates both heads.  Therefore a polynomial
min-cut on marginal phase incidences is not separation for the convex hull of
literal common-state configurations.

The exact integer DNF lift avoids this error.  Its row packing and shared
state gates remain branching variables; the supplier slave remains a
matching/min-cut.  Thus there is a polynomial fractional separator, but only
for (5.1), not for the convex hull of literal joint root/phase states.

## 6. Proof contract for a compiled 50-head cut

A compiled lifted cut is proof-safe only if all of the following hold.

1. **One parent.**  The table, common-basis/root data, mode catalogue,
   occurrence DNFs, protected rows, supplier graph, and cut witness bind the
   same parent SHA and parent-local identifiers.
2. **Unique semantic credits.**  Every cut term is keyed as either
   `INACTIVE_HEAD(h)` or `NEIGHBOR_SUPPLIER(u)`.  Keys are unique within the
   cut.  Alternative supports for one key are disjuncts of that one term.
3. **Exact activation.**  Each term is equivalent to its semantic credit on
   every represented completion.  A named root action is not itself a Hall
   credit unless it is proved equivalent to a particular head retirement or
   supplier adjacency.
4. **Complete recourse scope.**  A cut over compressed root-action variables
   carries a universal witness covering all residual common-basis
   completions.  A witness for one completion is insufficient.
5. **Canonical binding.**  The witness binds the shore/head list, supplier
   identities, target deficiency, right-hand side, canonical term/DNF file,
   and parent.  A self-declared scope string is not a semantic verification.
6. **No incomplete-menu promotion.**  A candidate with an active incomplete
   role/phase menu may be used as a relaxation or active-pricing request, but
   not as a fully phase-valid SAT witness.

Under these six conditions, Theorem 3.1 validates the cut and a DRAT proof of
the resulting frozen CNF validates only the explicitly authenticated
branch--Benders model.  It does not enlarge the root/occurrence scope of its
input cuts.

## 7. What remains

The remaining global work is not supplier separation itself.  It is to
either expose a complete common-basis representation and phase occurrence
state in the master, or build an independently checkable universal root
oracle that emits canonical cuts satisfying Section 6.  In particular, the
40-credit fixed-face obstruction gives no unconditional number of root
exchanges: a single alternating representation change can affect several
literal heads or suppliers, while the same basis can admit another
representation.

The first emitted root-aware generator and smoke CNF must be audited against
Section 6 before they can be used for a global UNSAT or supplier-perfection
claim.
