# Independent audit of the exact common-cap defect/regeneration theorem

Date: 2026-07-31  
Audited note:
\[
\texttt{MATH\_THEOREM\_K\_EXACT\_COMMON\_CAP\_DEFECT\_AND\_REGENERATIVE\_LINKAGE\_20260731.md}.
\]

## 1. Audit verdict

The following implications are proof-safe.

1. \(V_*=\min_Q(|\mathcal T|-\nu(H_Q))\) is exactly the minimum number of
   target parts omitted by a literal partial common-cap compiler.
2. The fixed-guard cut update is an identity, not an estimate.
3. The alternating-linkage update \(V'=V+\ell-\kappa\) follows exactly from
   matching symmetric difference.
4. The boundary-pressure table is a regrouping of every Hall cut and is
   necessary and sufficient on the stated common-guard face.
5. Bounded cell support gives only an additive Lipschitz estimate; a fixed
   multiplicative contraction of unbounded defect requires an extensive
   repair bank.
6. The affine recurrence gives the advertised additive constant only after
   all physical gates have passed and all other terminal charges are either
   zero or separately bounded.

No unconditional Boolean/Pascal bulk-regeneration lemma is proved.

## 2. Quantifier audit

The order of quantifiers is essential:

\[
 \text{accepted physical }Z
 \;\longrightarrow\;
 \exists Q
 \;\longrightarrow\;
 \exists\text{ matching in }H_Q.
\tag{2.1}
\]

The theorem does not infer replay from a matching.  It does not choose a
matching in the marginal graph and then search for a cap.  It first fixes a
literal guard word; every edge of \(H_Q\) is already realized by that same
word.  This is why any matching in \(H_Q\) is safe and why ordinary Hall is
valid there.

The minimization over \(Q\) is existential and terminal.  Under recursive
composition one must export a guard transition and the boundary linkage
state; exporting only the numerical minimum \(V_*\) loses information.

## 3. Algebra audit

Let \(H=H_0\dot\cup K^-\) and \(H'=H_0\dot\cup K^+\) on the same target
set.  For every \(X\), disjointness of right banks gives

\[
 |N_H(X)|=|N_{H_0}(X)|+|N_{K^-}(X)|,
\]

and similarly for \(H'\).  Subtraction proves the cut identity.  Maximizing
over all \(X\), including the empty cut, gives Hall deficiency exactly.
There is no hidden assumption that the maximizing cut is preserved by the
switch.

For the linkage identity, the transported matching \(M_0\) is genuinely a
matching in the final graph.  Symmetric difference with a maximum final
matching decomposes into cycles, balanced paths, and exactly
\(\nu(H')-|M_0|\) vertex-disjoint augmenting paths.  Therefore the displayed
\(\kappa\) is exact.  Paths may leave the geometric halo; the note does not
claim bounded path length.

For the pressure table, grouping cuts by \(Y=N_L(X)\) loses no cuts and no
neighborhood multiplicity because right vertices, not incidences, are
counted.  The cap-safety/common-guard hypothesis is separate and necessary.

## 4. Counterexamples checked

### 4.1 Scalar defect is not a recursive state

Take targets \(a,b,c\) and old cells \(x,z\), with edges

\[
 a\sim x,\qquad b\sim x,\qquad c\sim z.
\]

The old deficiency is one.  Add one new cell \(y\).

* If \(y\sim a\), the final graph has the perfect matching
  \(ay,bx,cz\).
* If \(y\sim c\), targets \(a,b\) still share only \(x\), so deficiency
  remains one.

The old scalar defect and boundary-cell count are identical.  The target
neighborhood/linkage signature distinguishes the two transitions.

### 4.2 One changed cell may require a global reroute

For targets \(t_1,\ldots,t_n\) and cells \(c_0,\ldots,c_n\), put

\[
                         t_i\sim c_{i-1},c_i.
\]

The matching \(t_ic_{i-1}\) leaves \(c_n\) free.  Deleting \(c_0\) does not
destroy perfect matchability, but the unique repair shifts every target to
\(c_i\).  Thus bounded physical damage can require a globally long
augmenting path.  Bounded linkage width, not geometric locality, is the
correct conclusion.

### 4.3 Bounded blocker rank is not an LLL hypothesis

Events of size at most three can all share one target-choice variable, so
their dependency degree is unbounded.  Moreover three labels

\[
                         \{2,3\},\{1,3\},\{1,2\}
\]

have all pairwise intersections nonempty and empty triple intersection.
Pairwise cap tests therefore do not imply a common cap.  A matching-first
common guard or an explicit asymmetric pressure inequality is required.

## 5. Scope of the rank-three and robustness statements

Rank at most three applies only after all variable sockets and long cells
are fixed.  A variable socket cap together with three short-cell caps can
form a rank-four blocker.  New blockers created in the switch halo must be
enumerated before applying the robust margin in the theorem.

The estimate \(7s+b\) counts short right columns, not target incidences:
one isolated changed derivative row affects at most three envelope
positions, hence three singleton and four adjacent-pair columns.  Overlap
only reduces this union.  The coarse \(17t\) additionally charges newly
residual direct targets and uses \(s\le2t,b\le t\).  The exact exceptional
column count should be used in any finite application.

## 6. K17 scope

The authenticated OPTIMAL28 owner cycle closes ownership and immediate
lower colour, but its proposed zipper has 2392 short-run defects, 3568
failed replay rows, and upper holes 1900/911/128.  Therefore no guard
instance from that zipper is asserted and no value of \(V_*\) is reported.
The scalar cell surplus 3293 is upstream of, and logically unrelated to,
the exact common-cap cut test.

## 7. Independent boundary

The exact theorem proved here is the implication

\[
 \text{physical acceptance + guarded cut/linkage contraction}
 \Longrightarrow B(k)+O(1).
\]

The unproved part is construction of a dimension-uniform physically valid
packet bank satisfying the contraction cuts.  Neither switch locality,
positive slack, ordinary Hall, nor bounded conflict rank proves that bank.

