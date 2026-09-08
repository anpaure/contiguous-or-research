# Independent audit of the protected Catalan--pivot factor-first cycle-cover theorem

**Date:** 2026-08-02  
**Lane:** K, protected Catalan connector / factor-first audit  
**Verdict:** **conditional GO after the scope corrections below.**  The
owner-layer cycle-cover/switch/opening implication is correct.  The original
all-width telescoping formula and typed-opening wording require the
corrections below; source length, global physical addresses and owner-run
history remain separate exported rows.

## 1. Owner-layer cycle cover and fusion

Let `Q_0` be an upper-exact rooted Catalan forest relative to `M_0`.
It has `U=W-C` edges on `W` rooted vertices, hence `C` directed-path
components and exactly one unused outgoing and incoming port per component.

Hall in the split free-port graph is therefore necessary and sufficient for
a perfect connector matching `R` of size `C`.  The union `Q_0 dotunion R`
is a perfect incidence matching outside `M_0`; after contracting `Q_0`, `R`
is a directed permutation and hence a cycle cover.  Thus

\[
                         F=M_0\cup Q_0\cup R
\]

is a spanning alternating two-factor.  Since `Q_0` is untouched by the
connector switches, its complete immediate-upper palette is retained.

Theorem 3.1 is correct under its stated maximum-merger and compatibility
hypotheses.  Equations (3.2)--(3.3) are exactly the incidence-tree
inequalities for the original factor cycles.  Pairwise-disjoint complete
supports, or the stated hereditary applicability in a rooted incidence-tree
order, makes every merger literal after the preceding contractions.  The
component count falls by

\[
                         \sum_z(|e_z|-1)=c(F)-1,
\]

so one cycle remains.  Deleting one nonprotected connector edge then leaves
`U+C-1=W-1` short-shore edges and opens the unique cycle into the required
alternating Hamilton path.  Its decomposition is exactly `Q_0` plus the
remaining `C-1` connector edges.

This is an **alternative sufficient factorization**, not a logically
weaker theorem than direct Hamilton-path existence.  A direct Hamilton path
need not have a legal free-port edge closing its two endpoints, whereas the
factor-first route assumes a perfect connector cover, a switch basis, and a
safe opening.

The word **complete** in “complete supports” is load-bearing.  Once a
physical source layout `A` is fixed, define the global address closure of a
switch to contain

* every physical source position it changes;
* every depth-window/owner occurrence meeting one of those positions;
* every interval witness, run-boundary state, pin, cap row or private token
  whose value or physical address may change; and
* every nonadjacent component block which shares a physical address through
  a short intervening block.

Disjointness must hold for these global closures, not merely for local
component labels or adjacent port collars.  If hereditary applicability is
used instead, it must be rechecked in the current **global** chronology.
An uncharged isolate has one owner cell, so two blocks on its opposite sides
overlap in `d-1` source positions under full `d`-history gluing; this is the
smallest reason a pairwise connector atlas does not certify simultaneous
physical addresses.

## 2. Correct all-width ledger

The baseline definition

\[
             \Delta_z(S)=\mu_{A\triangle z}(S)-\mu_A(S)
\]

does not telescope for several interacting rethreads.  Even switches with
disjoint local supports can jointly change an interval which crosses both
supports.  Hereditary applicability at the owner/state level does not make
the baseline witness increments additive.

Fix a legal switch order `z_1,...,z_t` and put

\[
 A_0=A,
 \qquad A_j=A_{j-1}\triangle z_j,
 \qquad
 \Delta_j(S)=\mu_{A_j}(S)-\mu_{A_{j-1}}(S).           \tag{2.1}
\]

Let `e_*` be cut in the **final** chronology `A_t`, and let
`L_(e_*,A_t)(S)` count its witnesses crossing that final seam.  Then the
exact condition is

\[
 \boxed{
   \mu_{A_0}(S)+\sum_{j=1}^t\Delta_j(S)
       -L_{e_*,A_t}(S)\ge1
       \quad(S\text{ required}).}                    \tag{2.2}
\]

Equation (2.2) telescopes tautologically to the final linear witness count.
Equivalently one may use the single net increment
`mu_(A_t)(S)-mu_(A_0)(S)`.  The original baseline sum is valid only under a
separately proved additive-ledger theorem, such as full boundary-signature
transparency plus an internal occurrence decomposition.

With this correction, Theorem 4.1's all-width implication is exact.

## 3. Residence scope

The per-coordinate state consisting of endpoint bits, capped prefix/suffix
run lengths, an all-one flag, and an internal-good flag is an exact
concatenation monoid for the threshold `D=d+1`.  It detects whether a run
terminated at a new seam is shorter than `D`, and whether two boundary runs
merge to a legal run.

This state must be taken on coordinate traces in the **owner/depth row**.
The ordered `d` source-letter rails used to glue antecedents are a different
state.  Equality of source rails proves the depth-row factorization; it does
not by itself assert owner residence.  Conversely an accepted owner-run
state does not identify source positions or compiler addresses.

The theorem must require the **composed final state** after all rethreads
and the opening to be accepting.  Individual acceptance of every rethread
against the baseline is insufficient.  In particular, three locally
clipped-resident path components can be joined by legal Johnson connectors
and still create a middle-component run of length `d`; the explicit
all-`d` construction is recorded in
`MATH_THEOREM_K_PROTECTED_CATALAN_PIVOT_HISTORY_APERTURE_AND_RESIDENCE_GATE_20260802.md`.

Subject to final-state acceptance, the residence part of Theorem 4.1 is
correct.  Cutting a cyclic word can turn a cyclic run into clipped endpoint
runs, while the monoid records every internal run of the resulting linear
word.

## 4. Typed opening and source-length corrections

If `e_*=LV` is deleted from the short matching shore, its lower endpoint
`L` is the unique missing immediate-lower turn of the final Hamilton path.
It has rank `m-1`.  Therefore the opening is typed to the pivot compiler
only when

\[
                 L=R^-_{d-1}\quad\hbox{or}\quad L=R^+_{d-1},          \tag{4.1}
\]

for one of the two maximal rank-`m-1` pivot-ray cells (or when another
explicit rank-`m-1` compiler cell is supplied).  The pivot singleton and
shorter ray cells have smaller rank and cannot host this missing `q1`
target.  Equality in (4.1) is occurrence-level and must hold in the same
common cap as the transported background matching.

There is no additional omitted-root containment hypothesis on this
**rooted** factor-first face.  Put `H=M_0^{-1}(V)`.  After deleting the
rooted link `L->H`, the two owner endpoints are `M_0(L)` and
`V=M_0(H)`, so

\[
                         L\subset M_0(L),\qquad H\subset V             \tag{4.1a}
\]

hold automatically.  In an unrooted owner-path formulation, however, if
`o` is the omitted lower root and `s,t` the intended owner endpoints, one
must impose

\[
                         o\subset s\quad\hbox{or}\quad o\subset t.     \tag{4.1b}
\]

Indeed the `W-1` used roots are already matched to the nonterminal owners;
the perfect predecessor (or successor) phase extends exactly when `o` is
incident with the remaining endpoint.  Thus (4.1b) is necessary before an
unrooted cycle/path certificate may be imported into the rooted theorem.

Finally, Theorems 3.1--4.1 do not determine physical source length.  If
component `i` has `g_i` nonowner depth cells and adjacent literal source
fragments overlap in `o_i<=d` letters, the exact surplus is

\[
              \sum_i g_i+\sum_i(d-o_i).               \tag{4.2}
\]

A length-`B+1` claim requires (4.2) to equal one.  Thus the phrase “exact
local `B+1` composition” is conditional on the `SRC` row and (4.2), not a
consequence of the `W-1` owner-edge count.

For several fragments, the overlap ledger also needs a global address
quotient.  If fragment starts are `b_i`, every source position `u` receives
the global address `b_i+u`; all letters/caps assigned to the same address
must agree, and all named compiler pins must remain distinct at their
resulting global interval addresses.  Pairwise adjacent overlap equalities
do not enforce the latter condition when a short component makes
nonadjacent blocks overlap.  In the direct `B+1` face the one surplus cell
is the global boundary nonowner and every internal connector uses a full
`d` source overlap; any internal deficient overlap needs a separate
owner-preserving bypass.

## 5. Corrected theorem scope

After replacing the all-width condition by (2.2), requiring acceptance of
the composed residence state, imposing the literal rank-`m-1` typing
(4.1), and exporting the aperture equation (4.2) together with the global
address closure, the factor-first theorem is proof-correct:

\[
 \begin{gathered}
 Q_0\text{ upper exact}
 +R\text{ a connector cycle cover}
 +T\text{ a protected compatible switch incidence tree}\cr
 +e_*\text{ a final-state-safe typed opening}
 \Longrightarrow
 \text{one protected upper-exact resident Hamilton path.}
 \end{gathered}
\]

Every all-width target survives precisely under (2.2).  This theorem does
not prove existence of `Q_0`, connector Hall, the switch basis, the typed
opening, a length-`B+1` source scaffold, the global common cap, or Pascal
regeneration.  No finite search was used in this audit.

The proof-safe exact remaining factor-first lemma is therefore:

> **Globally addressed rooted cycle-cover lift.**  Jointly choose
> `M_0,Q_0,R`, one global source antecedent, a merger incidence tree and a
> connector opening `e_*=LV` so that (i) all switch supports are disjoint in
> global address closure or hereditarily valid in the evolving global word;
> (ii) the sequential witness ledger (2.2) and the composed final
> **owner-run** state accept; (iii) the final linear source has exactly one
> boundary nonowner and no internal overlap charge; and (iv) `L` is the
> literal maximal pivot-ray target in the same common cap.  Rooted endpoint
> containment is then automatic by (4.1a).  An unrooted substitute must add
> (4.1b).

Ordinary connector Hall, a pairwise history atlas, or a component switch
tree without these global-address conditions does not imply this lemma.
