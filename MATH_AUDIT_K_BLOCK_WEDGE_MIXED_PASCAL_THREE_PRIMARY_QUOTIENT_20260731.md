# Independent audit of the block-wedge and three-primary Pascal quotient theorem

Date: 2026-07-31  
Verdict: **PASS after scope and ledger corrections**

## 1. Decisive checks

Two independent proof audits rederived the main statements in
MATH_THEOREM_K_BLOCK_WEDGE_MIXED_PASCAL_AND_THREE_PRIMARY_QUOTIENT_20260731.md.

The path-wedge theorem is exact for \(m\ge2\). The audit required three
qualifications now present in the theorem:

1. the smoothed colours \(d_i\) must be pairwise distinct in addition to
   \(\{d_i\}\cap\{\beta_i\}=\varnothing\);
2. suppression removes both the incoming \(\alpha_i\) and first-edge
   \(\beta_i\) ledgers before inserting \(d_i\); and
3. the converse assumes a simple Hamilton cycle, distinct hosted blocks and
   incoming occurrences, and the exact aggregate repair identity.

With those hypotheses, cutting the incoming edges gives a spanning
two-sided-rainbow \(K\)-path forest, and restoring them gives the stated
Hamilton closure. No connectivity, palette, or multiset step is implicit.

The gain-closed obstruction and mixed interval law were independently
recounted:

\[
|V|=2K,\qquad |E|=2K-t,\qquad
t=|X\setminus Y|=|Y\setminus X|.
\]

Because the selected subgraph is a proper subgraph of one cycle and has a
perfect matching, it is exactly \(t\) balanced alternating paths. The case
\(t=0\) is impossible. The gain and retained pivot formulas were checked
separately; they have different new-coordinate parities and cannot be
merged.

## 2. Quotient audit

The arithmetic

\[
h=\frac{2m-1}{3^{v_3(2m-1)}}\mid\operatorname{Cat}_m
\]

and freeness on ranks \(m-1,m,m+1\) were independently rederived. The
table for \(m=3,\ldots,8\) is exact.

The voltage statement is exact: a quotient path forest lifts pathwise, and
a quotient component cycle of voltage \(v\) has
\(\gcd(v,h)\) physical lifts. The theorem now explicitly requires simple
support, exact orbit palettes, injective \(\alpha,d,\beta\) ledgers, and the
untyped separation \(D\cap B=\varnothing\). A typed repair matching alone
would not imply the floor ledger.

The GMM count conclusion is deliberately conditional. The symmetry closure
of its printed atom supplies at most one quotient block. It supplies exactly
one, leaving deficit \(K/h-1\), only if all conjugate squares are mutually
compatible.

When \(3\mid(2m-1)\), the exact requirement is trivial stabilizer of the
full occurrence- and voltage-labelled quotient package under the residual
\(\mathbb Z_s\) action. Merely choosing nonidentical local sector data is
weaker and was not retained.

The multi-spiral extension was audited separately from the quotient-cycle
theorem. Deleting one wrap from each of \(r\) disjoint cycles and adding
\(r-1\) successive Johnson seams gives one Hamilton path, with exact
edge-local signed ledger

\[
-\sum_{j=1}^r \mathbf1_{\lambda(w_j)}
+\sum_{j=1}^{r-1}\mathbf1_{\lambda(s_j)}.
\]

This proves topology and the immediate lower/upper palette change only.
Exact-palette safety means zero signed change on both shores; coverage
safety means the final loads remain positive; a linear compiler may instead
consume an explicitly declared boundary deficit. The two path endpoints are
therefore additional physical resources. Every cut or seam touching a
protected cap-two block must also reverify its wedge and
\(\alpha,d,\beta\) ledgers. Neither the seam count nor co-orientation
determines the surviving number of repair ears. In particular, this path
branch is not a consequence of the quotient-cycle voltage theorem.

## 3. Period-three scope

The complete lower--upper diamond graph is balanced and
\(\binom{m+1}{2}\)-regular. Because the clean subgroup acts freely on both
shores, its quotient is a balanced regular bipartite multigraph. Hall gives
a quotient perfect matching, and freeness lifts it to an invariant physical
perfect matching. This removes the unconstrained residual-palette Hall gate
in every 3-primary valuation.

At \(v_3(2m-1)=1\), restriction of any such matching to the exceptional
banks gives exactly \(2\operatorname{Cat}_a\) clean-subgroup filter orbits.
The clean subgroup is transitive on each shortened full colour orbit, so
the restriction chooses exactly one of its three incident edge phases and
attains the sharp partial-full-orbit floor. At higher valuation the
restriction has \(2\operatorname{Cat}_a(s/3)\) clean-subgroup edge orbits,
one per exceptional quotient vertex; it need not use only
\(2\operatorname{Cat}_a\) full-rotation edge-orbit classes.

The exceptional filter diamonds have pairwise distinct middle endpoints:
same-shore exceptional colours differ by whole order-three cosets, and the
two shore types are separated by \(\infty\). This distinctness is internal
to the exceptional restriction. It does not prevent a nonexceptional
matching edge from using one of those middle vertices, and it gives no
degree-two, acyclicity, wedge or voltage conclusion for the full lift.

The filter-neutrality count is exact. Deleting the globally selected filter endpoints
changes the four Pascal shore sizes from

\[
(A,B;B,A)
\quad\text{to}\quad
(A-E,B-E;B-E,A-E),
\]

so the forced cross-shore difference remains \(A-B=K\). Thus the filters
do not cure the one-port GMM deficiency. A fixed independently prescribed
filter may still have a residual Kneser Hall obstruction; that constrained
question is no longer needed for the existential route.

The cycle-first reformulation is also exact. For a fixed spanning quotient
Johnson occurrence cycle \(\overline C\), a perfect matching of its typed
lower/upper colour-incidence graph is exactly an invariant common
transversal contained in \(\overline C\). It selects fewer than all cycle
edges, so its retained-vertex graph is a linear forest with \(K/h\)
components, allowing isolated vertices. Primitive total voltage is exactly
the condition for the physical cycle lift to be Hamiltonian. Isolates must
be separately excluded before invoking the stronger path-wedge/repair-ear
theorem.

## 4. Finite fixtures

The authenticated cyclic \(m=4\) replay verifies:

* two quotient paths of orders \(3\) and \(7\);
* two connector orbits;
* net voltage \(2\bmod7\);
* three repair-core edge orbits, with one forced orbit and one binary
  kernel choice.

The varied-size flag replay verifies:

* path orders \(21,7,7,6,5,5,4,3,2,2,2,2,2,2\);
* 13 distinct connector lower colours and 12 distinct connector upper
  colours;
* displayed-orientation wedge counts \(2\) and \(6\);
* 34 arcs in the full equal-union endpoint digraph; and
* indegree zero for both orientations of path \(0x95-0xc5\).

Hence its all-wedge closure is impossible for that fixed forest. No
statement about all \(m=4\) flag matchings is inferred.

The authenticated K16 replay supplies the distinct linear calibration:
four strict co-oriented \(\mathbb Z_{15}\)-spirals of base lengths
\(426,426,3,3\), all with sheet voltage \(+4\), interlace all three residual
sectors. Three Johnson seams make the physical path and the omitted wrap is
non-Johnson. The closed spiral bank and vertex parametrization are
\(\mathbb Z_5\)-covariant. The physical path has \(12869\) Johnson edges;
the four phase defects are the deficient orbits in the \(12870\)-entry
augmented cyclic audit support which also includes the absent wrap. The
common-cap compiler is asymmetric. This verifies the
multi-spiral topology and immediate-palette coverage, not a two-sided-
rainbow quotient common refinement or an all-dimension recursion.

## 5. Audited boundary

Proved:

* the dimension-free path-wedge equivalence;
* the gain-closed no-go and exact mixed \(t\)-interval law;
* the conditional mixed Pascal sufficient package;
* the clean-subgroup quotient/voltage lift;
* the co-oriented multi-spiral Hamilton-path and signed-palette ledger;
* the conditional quotient count deficit for the printed GMM atom;
* existence of a global clean-quotient diamond perfect matching and the
  automatically extendable exceptional restriction; and
* Pascal-imbalance neutrality of that restriction; and
* the coloured primitive-voltage cycle/common-transversal equivalence.

Open:

* a global quotient perfect matching whose entire physical diamond lift is
  a spanning degree-one/two acyclic forest;
* mixed retained/gain quotient parents in every dimension as one possible
  construction of such a matching; and
* generating-voltage closure with all pivot ledgers; or, on the separate
  linear branch, a palette-safe opening with certified boundary resources,
  protected-ear count, deeper collars and a compatible asymmetric compiler.

No all-\(m\), coefficient-one, or generic GMM completion claim survives.
