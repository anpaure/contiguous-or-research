# `k=17`: resource-saturation cores and the exact successor-cover separator

**Date:** 2026-08-02  
**Status:** pure q1 theorem.  The statement is exact relative to a complete
occurrence-labelled final-provider atlas and a specified successor-core
library.  It does not evaluate any of the residual banks and makes no
rank-ten, topology, residence, or compiler claim.

## 1. Frozen ledger and purpose

For the authenticated round-02 Hamming-two face, the frozen joint-clean
ledger is

\[
169426=164323+49+5054.
\]

The first term consists of banks already rejected by a retained
occurrence-labelled core; the second consists of dirty-central banks with
exact retained UNSAT proofs; and the final `5054` are the clean-anchor
survivors.  No q1 conclusion about those `5054` follows from this count.

The earlier guarded-minor theorem recognizes an old proof when its clauses,
or guarded consequences of those clauses, survive.  The result below is
strictly more semantic.  It recognizes the entire resource-support
obstruction even when every old provider identity has changed, and then
closes different escape choices by different successor cores.

## 2. The physical resource hypergraph

Fix a final bank `B`.  Let `V(B)` be its occurrence-labelled physical
sockets and let `C(B)` be its selected lower-q1 colours.  A legal physical
seam `e` has two sockets and one colour,

\[
             \partial e=\{u_e,v_e,\gamma(e)\}
             \subset V(B)\mathbin{\dot\cup}C(B)=:R(B).       \tag{2.1}
\]

All endpoint, Johnson, age, selected-colour, and protected-q1 predicates are
evaluated before `e` enters the atlas.  Parallel directed representations
of one physical seam are quotiented; distinct physical socket occurrences
are not identified merely because their owner masks agree.

Write `H(B)` for this resource hypergraph.  A set of seams is compatible
when its resource triples are pairwise disjoint.  The exact socket-quotient
theorem says that q1 feasibility is equivalent to a perfect matching of
`H(B)`.

The formulation extends verbatim if a q1 seam carries an additional genuine
unit-capacity protected resource: include that resource in \(\partial e\).
It must not be used to import rank-ten or other non-q1 requirements into the
statement.

## 3. Exact resource-support saturation

For a resource set `U subset R(B)`, define

\[
 \operatorname{cov}_B(U)=
 \max\bigl\{|U\cap\partial P|:
        P\text{ is a compatible seam set in }H(B)\bigr\},    \tag{3.1}
\]

where \(\partial P\) is the union of the resource triples of the seams in
\(P\), and put

\[
              \operatorname{def}_B(U)
                    =|U|-\operatorname{cov}_B(U).            \tag{3.2}
\]

Only seams meeting `U` need be retained in (3.1), but their complete outside
resource footprints remain load-bearing because two such seams can conflict
outside `U`.

### Theorem 3.1 (support-saturation min--max)

Let `F_B[U]` consist of

1. the positive exact-one row for every resource in `U`; and
2. every q1 at-most-one resource constraint.

Then

\[
 F_B[U]\text{ is satisfiable}
       \quad\Longleftrightarrow\quad
 \operatorname{def}_B(U)=0.                                \tag{3.3}
\]

Consequently `def_B(U)>0` is a proof-safe q1-UNSAT certificate.

#### Proof

If `F_B[U]` is satisfied, its true seam variables are resource-disjoint and
cover every positive row in `U`; they give a compatible set covering `U`.
Conversely, if a compatible seam set covers `U`, set precisely those seams
true and every other seam false.  All positive rows in `U` are satisfied,
and resource-disjointness satisfies every at-most-one row.  This proves
(3.3).  A global q1 solution satisfies `F_B[U]`, so positive deficiency is a
global obstruction.  \(\square\)

This is an exact semantic Hall test, not a degree test.  For a set of colour
resources it is the exact rainbow-matching condition on those colours.  For
two socket resources it automatically distinguishes a direct seam from two
arms and charges a repeated lower colour or outside socket only once.  Thus
the primal and dual fans are the two-resource special cases.

### Corollary 3.2 (semantic persistence of a core support)

For an authenticated pure-q1 core `K`, first transport the proof through the
exact physical socket quotient.  Let `U(K)` be the set of unconditional
physical resource rows whose positive clauses occur in that quotient proof.
An orientation-conditional directed tail/head clause is not, by itself, a
member of `U(K)`.  Reconstruct all final providers of the physical rows.  If

\[
                     \operatorname{def}_{B'}(U(K))>0,        \tag{3.4}
\]

then `B'` is q1-infeasible, even if no literal or clause of `K` has survived.
If the deficiency is zero, the subsystem using only those positive rows and
the q1 packing constraints is satisfiable.  Hence no proof confined to that
resource support can reject `B'`; a larger support or an additional
non-q1 premise is necessary.

The second sentence is the completeness boundary for the named semantic
support, not a feasibility statement about the whole bank.

### Theorem 3.3 (resource-cover transport)

Let `K` be a stored deficient resource system on `U`, and let `U'` be a
same-size occurrence-labelled resource set in a final bank.  Suppose there
are

1. a bijection \(f:U'\to U\); and
2. a map \(\pi\) from every effective final seam meeting \(U'\) to a stored
   seam meeting \(U\),

such that

* if \(u'\in\partial e\), then \(f(u')\in\partial\pi(e)\); and
* the images under \(\pi\) of every compatible final seam family form a
  compatible stored seam family with the same covered resources of `U`.

Then

\[
              \operatorname{def}_K(U)>0
       \quad\Longrightarrow\quad
              \operatorname{def}_{B}(U')>0.               \tag{3.5}
\]

#### Proof

If a compatible final family covered `U'`, its image would, by the two
displayed properties, be a compatible stored family covering `U`.  This
contradicts the stored positive deficiency.  \(\square\)

This transport recognizes a moved or relabelled semantic core even when no
old atom survives.  Provider clones may be folded onto an old provider only
when the second condition is proved for every compatible family; equality of
degrees or of pairwise masks is insufficient.  A practical sufficient
certificate records complete compatibility profiles, or uses the exact
boundary language of the companion final-provider theorem.

## 4. Complete escape signatures

Let `U_0` be a set of pivot resources.  Its exact signature family is

\[
 \Sigma_B(U_0)=\{P:
   P\text{ is compatible},\ U_0\subseteq\partial P,
   \text{ and every }e\in P\text{ meets }U_0\}.             \tag{4.1}
\]

Every perfect matching `M` induces exactly one member

\[
                  P=M\cap\{e:e\cap U_0\ne\varnothing\}.     \tag{4.2}
\]

For a signature `P`, contract its chosen seams: delete every resource in
`partial P` and every seam meeting such a resource.  Denote the residual
hypergraph by `H(B)/P`.

For the intact round-02 dual-fan sockets `s,t`, the family
`Sigma_B({s,t})` consists exactly of

* one legal direct `st` seam; or
* two resource-disjoint arms, one at `s` and one at `t`.

Thus this signature family includes different-colour arms, latent
geometry--supplier joins, dirty-single compensation, and genuinely
two-locked endpoint activation.  It does not infer any of them from a mask
or a provider degree.

If the central roles move, `{s,t}` is no longer the asserted pivot.  One must
reconstruct the new occurrence-labelled positive rows and apply the same
definition there.  The old socket masks alone do not define a signature
family.

### Lemma 4.1 (footprint quotient)

If two signatures `P,Q` have the same complete resource footprint,

\[
                         \partial P=\partial Q,              \tag{4.3}
\]

then `H(B)/P=H(B)/Q` for the q1 problem.  They may therefore be represented
by one footprint signature.

#### Proof

Contraction deletes exactly the consumed resources and all incident seams.
No other datum enters the physical q1 residual.  \(\square\)

This quotient is not valid for later topology or upper-shadow scoring, where
the identity of the chosen seam can matter.

## 5. Successor-core cover

Let `L` be a library of authenticated successor certificates.  An entry can
be

* a resource support `U(K)` as in Corollary 3.2;
* an occurrence-labelled guarded CNF minor; or
* an implication bicycle whose arcs are entailed after final provider
  reconstruction.

For a signature `P`, call a support entry `U(K)` **closed** when

\[
 \operatorname{def}_{H(B)/P}
       \bigl(U(K)\setminus\partial P\bigr)>0.                \tag{5.1}
\]

Rows in \(U(K)\cap\partial P\) are already satisfied by the signature and are
therefore removed, not demanded a second time.  A guarded minor or bicycle
closes `P` when it is entailed by the residual formula after the literals of
`P` are set true.

### Theorem 5.1 (complete one-interface successor separator)

If every exact signature is closed by at least one library entry,

\[
       \forall P\in\Sigma_B(U_0)\quad
       \exists K\in L\quad K\text{ closes }P,               \tag{5.2}
\]

then `B` is q1-infeasible.

#### Proof

Suppose a perfect q1 matching `M` exists.  Its restriction (4.2) is some
signature `P`.  The residual matching `M\setminus P` is a matching in
`H(B)/P` and saturates every resource not already consumed by `P`.
Therefore it saturates \(U(K)\setminus\partial P\) for every support entry
`K`, contradicting (5.1).  It also satisfies every residual entailed clause,
contradicting any guarded-minor or bicycle closure.  Hence no perfect
matching exists.  \(\square\)

The theorem permits different escape signatures to be killed by different
successor cores.  This is strictly stronger than asking one old core to
persist before the escape choice is made.

### Corollary 5.2 (safe overapproximation)

It is proof-safe to replace `Sigma_B(U_0)` by any certified superset and
prove (5.2) for every member of that superset.  Omitting even one realizable
signature is unsafe.  Similarly, enlarging a provider atlas is safe only for
a negative saturation verdict: if even the enlarged atlas has positive
deficiency, then the physical atlas does too.

### Theorem 5.3 (relative completeness)

For fixed `U_0` and library `L`, the separator is complete for refutations of
the following form:

1. split on the complete q1 footprint induced at `U_0`; and
2. at each leaf use one member of `L` as a resource-saturation, guarded-minor,
   or implication-bicycle contradiction.

If a signature remains open, no refutation of that specified form has been
established.  The bank may still be q1-infeasible because of a new core, a
larger Hall shore, or a correlation outside the library.

This is a proof-system completeness statement, not a claim that the
successor library contains every q1 obstruction.

## 6. A bounded semantic library

For an integer `k`, let `L_k` contain every occurrence-labelled resource set
of size at most `k` in a declared dependency cone.  The rule

\[
             \exists U\in L_k:\operatorname{def}_B(U)>0     \tag{6.1}
\]

is exact for the existence of a resource-saturation obstruction of support
at most `k` in that cone.  It discovers relocated or provider-changed cores;
it is not restricted to embeddings of previously stored clauses.

There is no ordinary degree or pairwise-Hall replacement for (6.1).  The
candidate seams form a coloured matching problem, and three-way resource
conflicts can survive every singleton and pair projection.  On a residual
face in which all effective choice rows are binary, implication-SCC closure
is an exact alternative representation; outside that face it is only a
library certificate.

## 7. Exact application to the `5054` survivor face

For each of the `5054` clean-anchor banks, a proof-safe next separator is:

1. use D's complete final-provider reconstruction, including all joint-only
   geometry--colour and two-endpoint seams;
2. form the exact direct-or-two-arm signatures at the two surviving central
   socket occurrences;
3. quotient signatures only by their complete resource footprints;
4. condition on each footprint and test the resource supports extracted
   from the authenticated successor cores (including the visible-pair core
   bank), followed by guarded-minor or binary implication closure; and
5. reject the bank only when every footprint is closed as in (5.2).

The coarse fast-filter reasons are handled semantically as follows.

* `reference_endpoint` invokes Theorem 3.3 on the rebuilt forced resource,
  rather than treating a mutable reference occurrence as destroyed.
* `new_out_atom`, `new_in_atom`, and `new_colour_tail` insert the new seam
  with its complete three-resource footprint into (3.1) and (4.1).  The atom
  breaks a core only through an open compatible signature.
* `palette_toggle` rebuilds the final colour resource and every provider of
  that resource.  A changed mask or multiplicity alone has no verdict.

These cases exhaust the reasons emitted by the present equality-based fast
filter, but the statements above do not assume their finite frequencies.

This procedure does not duplicate the full q1 solve.  It is a bounded local
matching and core-entailment separator driven by the already reconstructed
providers.  The theorem supplies no numerical verdict for the `5054` until
those exact footprint-to-core incidences are audited.

## 8. False-positive boundary

The following substitutions invalidate a rejection certificate:

* an incomplete final-provider atlas;
* owner masks in place of occurrence-labelled sockets;
* provider degree or colour multiplicity in place of resource footprints;
* separate endpoint arms in place of a direct seam covering both pivots;
* omission of an outside socket, colour, orientation, or protected q1
  resource from a footprint;
* singleton-child unions that omit joint-only seams;
* treating a role-relocated bank as though the old positive socket row still
  existed;
* retaining a binary implication after its positive row gains an unblocked
  third provider; or
* using a rank-ten or residence premise not present in the asserted q1
  residual.

With complete final resources, exact contraction, and an authenticated leaf
certificate, Theorems 3.1 and 5.1 have no false q1-UNSAT rejections.  Their
deliberate incompleteness is one-sided: an open signature is promoted to the
next exact stage rather than declared feasible.
