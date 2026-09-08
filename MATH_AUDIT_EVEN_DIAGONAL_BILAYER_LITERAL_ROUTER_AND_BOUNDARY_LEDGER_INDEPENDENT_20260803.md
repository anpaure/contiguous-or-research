# Independent audit: even diagonal bilayer literal router and boundary ledger

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_EVEN_DIAGONAL_BILAYER_LITERAL_ROUTER_AND_BOUNDARY_LEDGER_20260803.md`  
**Audited theorem SHA-256:**
`072daa9a76e4d2fccb9fa39f5bb59f3c90e0012147ea871d14ebde18d45cc9e6`  
**Verdict:** **GO after scope corrections.**  The occurrence/value
distinction, bilayer ledgers, two literal routing phases, physical boundary
detachment, compiler-slack obstruction, numerical calibrations, and typed
single-role cut are correct under the hypotheses now stated.  The result is
a theorem on a fixed cyclic diagonal row and its literal linearization; it
does not construct that row or a compatible terminal socket bank.

No finite search was used in this audit.

## 1. Corrections made during the audit

The original theorem had SHA-256
`6d7f705b6be91d14b59f4ef38914487bad27f55e3f44cf7fe7f0fd118f34cedb`.
Its algebra was correct, but five hypotheses were made explicit before the
GO verdict.

1. The dummy columns in the lower and upper tables require the
   corresponding q1 row to be surjective.  Without surjectivity the first
   two columns remain exact but the difference need not be a realizable
   real-plus-dummy decomposition.
2. The inequality `sigma >= C+1` is a necessary condition for the
   linearized row to admit an injective exact strict-lower compiler; it is
   not a condition forced by the owner row alone.
3. The `B+1` and fixed-`c` counts reserve `W` central-owner cells only on a
   face retaining the complete width-`d+1` diagonal owner band.  For
   `c>=2`, the subtraction of every displayed upper rank additionally
   requires the stated complete graded diagonal bands.
4. The terminal bank is a distinct, no-alias, single-role bank.  Likewise,
   the sockets in the literal router must be pairwise distinct and
   physically disjoint from its port/source resources.
5. In the typed cut, `sigma_B` is counted on resources disjoint from the
   surplus immediate-upper cells.  Otherwise the scalar sum could count an
   address twice.

These are scope corrections only.  They do not alter any formula or either
calibration.

## 2. Bilayer cardinalities

Let `K=2r`, fix `z`, and put

\[
 W={2r\choose r},\qquad M=W/2,\qquad C=W/(r+1).
\]

Pascal symmetry gives

\[
 {2r-1\choose r}={2r-1\choose r-1}=M,
\]

so the two middle-owner shores both have size `M`.  The two lower q1 target
shores have sizes

\[
 {2r-1\choose r-1}=M,
 \qquad
 {2r-1\choose r-2}
   ={r-1\over r+1}M=M-C.
\]

By complementing in the `(2r-1)`-set, the upper q1 target shores have the
opposite sizes `M-C` and `M`.  Thus the theorem correctly distinguishes the
equal middle-owner shores from the unequal lower/upper value shores.

## 3. Exact top-run ledger

The complete owner row contains `M` owners omitting `z` and `M` owners
containing `z`.  If its cyclic top trace has `h` one-runs, then it has

\[
 \#AA=M-h,\qquad \#BB=M-h,\qquad
 \#AB+\#BA=2h.
\]

For an `AA` edge, both intersection and union omit `z`; for a `BB` edge,
both contain `z`; for a cross edge, the intersection omits `z` and the union
contains `z`.  Hence the lower occurrence vector is

\[
 (M-h+2h,\ M-h)=(M+h,M-h),
\]

and the upper occurrence vector is `(M-h,M+h)`.  Subtracting the target
vectors `(M,M-C)` and `(M-C,M)` gives respectively

\[
 (h,C-h),\qquad(C-h,h).
\]

These are exact dummy vectors under the corresponding surjectivity
hypothesis.  Their nonnegativity gives `h<=C`; the presence of both zero and
one owners in the cyclic trace gives `h>=1`.  This proves (0.10)--(0.13).

The incidence check is also exact.  The `AA`, cross, and `BB` ports
contribute `2(M-h)`, `2h`, and `2(M-h)` incidences to the appropriate owner
shores.  Each middle shore therefore receives `2M` incidences, as required
by a degree-two occurrence factor.

## 4. Cyclic occurrence router and resource loads

With occurrence addresses retained, the graph

\[
 p_i o_i,\qquad p_i o_{i+1}
\]

is literally the alternating cycle

\[
 o_0,p_0,o_1,p_1,\ldots,o_{W-1},p_{W-1},o_0.
\]

Repeated values among the `P_i` do not identify vertices of this addressed
graph.  Under lower q1 surjectivity, choosing one occurrence of each of the
`W-C` lower targets leaves exactly `C` occurrence-labelled dummies, so the
real-plus-dummy port shore still has size `W`.

The literal equalities

\[
 P_i\cup A_i=T_i,
 \qquad
 P_i\cup A_{i+d+1}=T_{i+1}
\]

give the two routed phases.  In either phase the port indices are distinct,
the source indices are a cyclic permutation of all source occurrences, and
the assumed terminal sockets are distinct.  Thus each phase is an integral
unit-capacity linkage.  Across both phases every port, source occurrence,
and terminal socket has multiplicity two; uniform weight `1/2` gives load
one.  This verifies the claimed zero normalized overload.  It does not
export the sockets, and the theorem now says so explicitly.

## 5. The linear opening really has `W+1` physical ports

The linear source has length `W+d`.  Its width-`d` intervals are

\[
 p_j=[j,j+d-1],\qquad 0\le j\le W.
\]

They have `W+1` different start addresses and are therefore genuinely
different physical interval cells.  In particular, `p_0` and `p_W` are
different cells (indeed disjoint because `d<W`) even though periodicity
gives

\[
 \operatorname{OR}(p_0)=\operatorname{OR}(p_W)=P_{W-1}.
\]

The addressed incidence graph is consequently the alternating path

\[
 p_0,o_0,p_1,o_1,\ldots,p_{W-1},o_{W-1},p_W.
\]

The right-going phase uses `p_0,...,p_(W-1)` and source positions
`d,...,W+d-1`; the left-going phase uses `p_1,...,p_W` and source positions
`0,...,W-1`.  Each phase is integral and disjoint internally.  With weight
`1/2` on both phases, internal ports and overlapping source positions have
load one, boundary ports/source positions have load one-half, and every
owner receives load one.  Grouping `p_0,p_W` as the two physical
realizations of the closing logical port gives one unit for that logical
port as well.

This verifies both the `W+1`-port claim and the boundary-clone accounting.
For `d=1`, port cells and source cells alias, so the theorem correctly
withholds the separated-resource overload claim without coalescing.

## 6. Compiler injection and the `C+1` boundary cost

At exact length `W+d`, the number of interval addresses of widths at most
`d` is

\[
 \sum_{\ell=1}^{d}(W+d-\ell+1)
   =dW+{d(d+1)\over2}=dW+\tau_d.
\]

On the diagonal face every interval of width at least `d+1` contains a
rank-`r` owner cell, so every strict-lower target must be witnessed in this
short pool.  Different targets require different physical cells; an exact
injective compiler therefore consumes exactly

\[
 \Lambda=\sum_{s=1}^{r-1}{2r\choose s}
\]

short cells and leaves exactly

\[
 \sigma=dW+\tau_d-\Lambda
\]

unused.

All `W+1` detached port cells have rank `r-1`, while there are only

\[
 {2r\choose r-1}=W-C
\]

rank-`r-1` target values.  An injective compiler can use at most one port
occurrence per value.  Hence at least

\[
 (W+1)-(W-C)=C+1
\]

of these physical port cells are unused, proving `sigma>=C+1` whenever the
exact compiler exists.

This argument does **not** double-count the boundary clone.  Its forced
unused occurrence is one of the `C+1` port-row omissions, and all `C+1`
are already members of the global `sigma` unused short cells.  They cannot
be added to `sigma` again as a separate terminal bank.

## 7. Exact-length, `B+1`, and fixed-charge socket counts

At exact length, the width-`d+2` linear band has `W-1` cells.  If the cyclic
upper row is surjective and the omitted closing turn has another provider,
the remaining cells still cover all

\[
 {2r\choose r+1}=W-C
\]

upper targets.  Their surplus is exactly

\[
 (W-1)-(W-C)=C-1.
\]

This band is address-disjoint from the short pool.  The stipulated
single-role bank therefore has capacity at most `sigma+C-1`, and a linkage
of all `W` port tickets has deficiency at least

\[
 (W-\sigma-C+1)_+.
\]

At length `W+d+1`, on the stated complete width-`d+1` owner-band face, the
pool through width `d+1` has size

\[
 (d+1)W+\tau_{d+1}.
\]

After reserving `Lambda` lower cells and `W` owner cells, at most

\[
 (d+1)W+\tau_{d+1}-\Lambda-W=\sigma+d+1
\]

remain.  The full width-`d+2` q1 band has at most `C` surplus cells, so the
no-alias capacity and deficiency are

\[
 \sigma+d+1+C,
 \qquad
 (W-\sigma-d-1-C)_+.
\]

For fixed `c`, the theorem's formula follows by counting all intervals
through width `d+c` and subtracting `Lambda`, the `W` central owners, and
every target in the explicitly assumed complete rank-`r+j` bands.  For
`c=1`, the q1 band lies outside that pool and its `C` surplus is separately
granted.  For `c>=2`, q1 is already the `j=1` admitted band and must not be
added again.  The graded-band hypothesis inserted during this audit is
essential for that subtraction.

## 8. Type-refined opening and terminal cut

Duplicating the closing lower port increases the `z`-free surplus by one
for an `AA` or cross closing edge, and the `z`-containing surplus by one for
a `BB` edge.  This independently reproduces (5.1).

Removing a redundant closing upper occurrence decreases the `z`-free
upper surplus by one for `AA`, and the `z`-containing surplus by one for
`BB` or cross.  This reproduces (5.2) and the necessary safe-opening
inequalities.

Every terminal immediate-upper occurrence for a `B`-owner must contain
`z`.  After a safe opening the available surplus in that type is exactly

\[
 h'=h-1_{\{\text{a containing upper dummy was deleted}\}}.
\]

If the fixed semantics admit `sigma_B` additional, physically disjoint
short/common-cap units for those tickets, the full `B` shore of size `M`
has terminal deficiency at least

\[
 (M-h'-\sigma_B)_+.
\]

This is a cardinality cut only.  It neither proves that the `sigma_B`
units are typed-compatible nor rules out a dual-role or remote socket bank.

## 9. Numerical calibrations

For `K=14`,

\[
 r=7,\quad W=3432,\quad C=429,
\]

\[
 \Lambda=14+91+364+1001+2002+3003=6475.
\]

Since `W+1<Lambda` but `2W+3>=Lambda`, the deadline is `d=2`, and

\[
 \sigma=2(3432)+3-6475=392<430=C+1.
\]

Thus no exact-length word on this particular cyclic q1-surjective flat
diagonal face can possess an injective strict-lower compiler.  This does
not contradict the known nonflat/noncyclic optimum.

For `K=16`,

\[
 r=8,\quad W=12870,\quad M=6435,\quad C=1430,
\]

\[
 \Lambda=26332,\qquad d=3,
\]

and

\[
 \sigma=3(12870)+6-26332=12284.
\]

Here `sigma>=C+1`, and the exact-length scalar bank has upper bound

\[
 \sigma+C-1=13713>12870.
\]

So the total scalar cut vanishes, exactly as the theorem states; the live
question is the typed physical socket linkage.

## 10. Final scope

The corrected theorem proves the implication

\[
 \begin{array}{c}
 \text{cyclic q1-surjective even literal diagonal row}\\
 +\ \text{one real lower-target occurrence plus }C\text{ dummies}\\
 +\ \text{one pairwise-distinct compatible unused socket per owner}
 \end{array}
 \Longrightarrow
 \text{a zero-overload two-phase literal router}.
\]

It also proves exact compiler and terminal capacity obstructions on the
explicitly scoped diagonal/no-alias faces.  It does not prove existence of
the cyclic row, safe opening, lower compiler, terminal socket bank, or an
even all-dimensional construction.  Subject to those boundaries, the
audited theorem is proof-safe.
