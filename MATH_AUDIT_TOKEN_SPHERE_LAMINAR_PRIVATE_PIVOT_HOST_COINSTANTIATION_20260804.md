# Independent audit: token-sphere laminar private pivot-host
# co-instantiation

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_TOKEN_SPHERE_LAMINAR_PRIVATE_PIVOT_HOST_COINSTANTIATION_20260804.md`  
**Frozen theorem SHA-256:**
`575a89720b723b6d5f3c42c147d4c808aae667bc9856b037e9a9db5eeba33e01`  
**Method:** independent symbolic proof and quantifier audit.  No finite
search, solver, random experiment, or computational candidate is used as
mathematical evidence.

## 0. Verdict

**PASS at the stated conditional scope.**

The theorem proves four exact statements.

1. It counts the outgoing one-aperture tokens which avoid a prescribed
   coordinate bank.
2. It combines this count with a complete `q1` seam palette and an exact
   running-intersection natural-join test.
3. It proves a degree-weighted two-stage private factor router which can
   service every claim even when the complete port bank is not suffix
   linkable.
4. It proves that a joined lower/upper/router tuple pastes into one
   one-pivot host without additional omission under explicit physical
   privacy, common-state, dual-role, and final-replay hypotheses.

The zero-omission row is a hypothesis about the complete module inventory
and replay.  The theorem proves that gluing preserves it; it does not derive
zero omission from balanced lower marginals, a separate rainbow forest, or
a marginal router.  No current result verifies the running-intersection,
bad-seam, private-lift, residence, second-coordinate, even-tap, or infinite-
spine hypotheses for the full Boolean construction.  Consequently the
theorem proves neither `PPC(1)` nor a new upper bound.

## 1. Restricted token-sphere audit

The exact aperture sphere consists of rank-`(R-1)` sets `J` satisfying

\[
                         |H\cap J|=R-D.                \tag{1.1}
\]

Since `|J|=R-1`, necessarily

\[
                         |J-H|=D-1.                    \tag{1.2}
\]

Let

\[
                         a=|F\cap H|,
 \qquad                    b=|F-H|.                   \tag{1.3}
\]

An output avoiding `F` chooses its intersection with `H` from `H-F` and
its exterior part from `H^c-F`.  The choices are independent and unique,
so their number is

\[
 {R-1-a\choose R-D}{R-b\choose D-1}.                 \tag{1.4}
\]

The first factor is positive exactly when `a<=D-1`; the second exactly
when `b<=R-D+1`.  These are the avoidance inequalities in the source
one-token theorem, now with the exact surviving multiplicity retained.

The scope warning is correct.  The relay uses all of the incoming token
`H`, so (1.4) only removes `F` from the exported `J`.  It does not make the
current pivot block disjoint from `F`, and it says nothing about occurrence
or cap footprints.

## 2. Seam-selection audit

On the assumed cyclic `q1`-exact carrier, the lower seam colours occur
once each on the complete rank-`(R-1)` shore.  Therefore every `J` counted
by (1.4) labels one and only one seam.  If the correlated host rejects a set
`mathcal B` of colours, an admissible seam exists exactly when

\[
 \mathcal S_D(H;F)-\mathcal B\ne\varnothing.          \tag{2.1}
\]

The sufficient cardinality inequality

\[
 |\mathcal B\cap\mathcal S_D(H;F)|
 <|\mathcal S_D(H;F)|                                 \tag{2.2}
\]

is immediate and sharp when only the rejected-set size is known.  Equality
can reject the whole eligible sphere.  The theorem does not infer a bound
on the actual Boolean bad set.

For a fixed-size coordinate bank along a schedule with both `D` and
`R-D` tending to infinity, write the two factors in (1.4) as

\[
 { (R-D)+(D-1-a) \choose R-D},
 \qquad
 { (D-1)+(R-D+1-b) \choose D-1}.                     \tag{2.3}
\]

Both lower arguments tend to infinity uniformly for bounded `a,b`.
Hence the product tends to infinity.  This verifies the bounded-bank and
bounded-bad-seam corollary.  Its recursive clause explicitly assumes that
the selected output is an accepted next state and that the next child is
rebuilt with one star.

## 3. Running-intersection audit

The relation variables retain literal equality of shared choices.  For an
edge `ij` of the scope tree, running intersection implies that
`S_i cap S_j` contains every variable shared between the two components of
`T-ij`.  Thus the message from one side is precisely the projection of the
assignments extendible over that entire side.

Leaf induction proves the displayed recursion.  At the root, a tuple
compatible with every incoming message selects one extension in each child
subtree.  Any two extensions agree on all variables they share, because
those variables occur in the corresponding separator.  They therefore
paste to a global tuple.  Restricting a global tuple proves the converse.

The theorem's parameterized bad set

\[
 \mathcal B_{\rm join}=
 \{J:\Join_i\mathcal R_i[z=J]=\varnothing\}           \tag{3.1}
\]

is consequently exact.  The union of certified local exception sets is a
one-way sufficient bound on (3.1), as stated.  A laminar scope family has
an inclusion forest and hence running intersection, but the theorem does
not assert that the actual lower, upper, and router scopes are laminar.

## 4. Degree-weighted factor-cascade audit

Let `d_p=deg_B(p)`.  For each incidence chain formed by a claim--port edge
and a port--sink edge, assign weight `1/(hq)`.  The loads are:

\[
\begin{array}{c|c}
\text{resource}&\text{load}\\ \hline
\text{claim }g&hq/(hq)=1,\\
\text{prefix edge-bundle interior}&q/(hq)=1/h,\\
\text{port }p&d_pq/(hq)=d_p/h\le1,\\
\text{suffix edge-bundle interior}&d_p/(hq)\le1/q,\\
\text{sink }s&(hq)^{-1}\sum_{f=ps}d_p\le1.
\end{array}                                           \tag{4.1}
\]

The last inequality is exactly the displayed weighted sink premise.
Private interiors and avoidance of nonincident displayed endpoints ensure
that (4.1) accounts for every finite capacity.  The flow has value `|G|`.
After node splitting, all physical capacities are integral, so integral
max flow gives one route from every claim to a distinct sink.  Because
every possible concatenation through a port is assumed type-legal,
integrality cannot create an illegal claim--sink pairing.

If `deg_K(s)<=q`, then

\[
 \sum_{f=ps}d_p\le h\deg_K(s)\le hq,                 \tag{4.2}
\]

so two ordinary bounded-degree factors are a valid specialization.

The theorem is genuinely weaker than full-port suffix linkage.  In its
one-claim example, two ports both reach one unit sink.  Their suffix rank is
one, while the claim needs only one representative.  With `h=2,q=1`, each
port has `d_p=1`, so the weighted sink load is

\[
                         (1+1)/(2\cdot1)=1.            \tag{4.3}
\]

The example is therefore valid and distinguishes the claim-level cascade
from the stronger full-port certificate.

At `h=q=2`, the conclusion applies to two physical factor lifts only under
the stated privacy and type premises.  The protected Middle-Levels factor
theorem supplies an abstract incidence factor, not its literal prefixes or
suffix bundles.  The diagonal theorem supplies its owner-bypassing bundles
only on the native accepted face and only if they survive compensation.
These qualifications are preserved.

## 5. Physical-pushout and charge audit

The gluing theorem separates semantic reuse from finite-capacity reuse.
Different interval addresses may overlap in source positions in the native
OR-word model.  Reusing the same immutable occurrence fact is also harmless
when both roles assert the same address, value, and type.  Neither fact
licenses two paths through one unit transit resource.

The physical-pushout condition handles the latter issue exactly.  Outside
the displayed interfaces, each unit resource belongs to one module.
Inside an interface, one complete bundle certifies every identified role
and consumes the unit only once.  In particular:

* compensation deletion precedes the suffix relation;
* prefix interiors avoid the suffix catalogue;
* upper connector work retains or redelivers every protected witness;
* dual use of `q_i` is permitted only for the identical accepted
  upper-turn fact and terminal type; and
* the opened-seam bundle is one occurrence, not three separately charged
  sockets.

Thus taking the union of the joined modules does not overuse a capacity or
invalidate an old witness.  Monotone pivot insertion preserves old interval
ORs.  The lower, upper, pivot, background, and router obligations are
assumed exhaustive and the final replay is assumed empty.  The conclusion

\[
                         \mathcal H=\varnothing        \tag{5.1}
\]

is therefore preservation of a complete zero-omission datum.  It is not an
unconditional coverage theorem.  Since the scaffold has exactly one pivot
position,

\[
                         \tau=1+R(\varnothing)=1.      \tag{5.2}
\]

One-star child reconstruction makes (5.2) a per-terminal charge rather
than a sum along the odd spine.  Existence of such a reconstructing spine
remains a hypothesis.

## 6. Correlation-obstruction audit

For the three binary relations in the theorem, the lower and upper
relations force

\[
                         x=y=z,                        \tag{6.1}
\]

while the router relation requires `z!=x`.  Their triple join is empty.
Each relation projects onto `{0,1}` on either variable, and every two of
the relations have a solution.  Thus individual feasibility, complete
one-variable separator projections, and pairwise co-instantiation all
hold.

A running-intersection tree would need the lower--router edge for variable
`x`, the lower--upper edge for `y`, and the upper--router edge for `z`.
A three-node tree has only two edges, so no such tree exists.  This proves
that the acyclicity hypothesis is substantive.  The resource interiors in
the example can be empty, showing that physical disjointness alone cannot
repair an inconsistent common cap/orientation state.

The independent common-terminal-cut warning is also correct.  A relational
join does not increase physical cut capacity; two marginal full ranks still
need an allocation, separated copies, or accepted coalescence.

## 7. Scope and nonpromotion ledger

| Row | Audited status |
|---|---|
| restricted token-sphere count | proved exactly |
| unique seam for every eligible token | conditional on a complete cyclic `q1` palette |
| running-intersection host test | proved exactly |
| actual Boolean scope laminarity | open |
| bounded joint bad-seam set | hypothesis, not proved |
| degree-weighted private factor cascade | proved |
| two abstract factors imply physical router | false as an inference |
| balanced lower bank passing all cuts | hypothesis/open |
| residual nonadjacency lower lift | hypothesis/open |
| rainbow all-width forest/Hamilton host | hypothesis/open |
| one-coordinate factor-diamond occurrence lift | conditional on survival and accepted type |
| second coordinate and product closure | open |
| private-footprint gluing | proved under the displayed interface hypotheses |
| zero omission after gluing | preserved from the exhaustive final-replay hypothesis |
| odd charge nonaccumulation | conditional on accepted one-star rebuilding |
| even taps / `PPC(1)` / all-dimensional bound | not proved |

## 8. SHA and file-scope check

The fourteen input hashes and the two added audit-input hashes in Section 7
of the theorem match the exact files read.  In particular, the theorem uses
the corrected exact-cut synthesis, the audited lower multisocket theorem,
the audited rainbow-forest CSP, the audited private Rado router, the
one-token overlay, and the audited diagonal router at their stated scopes.

No source theorem, source audit, index, or handoff file is modified.  The
only new files are this audit and its audited theorem.  Subject to the
frozen theorem hash above, no correction is required.
