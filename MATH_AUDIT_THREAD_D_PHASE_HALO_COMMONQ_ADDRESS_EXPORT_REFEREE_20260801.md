# Referee audit of the phase-halo common-Q and address-export theorem

Date: 2026-08-01  
Lane: Thread D, independent audit  
Audited file:
`MATH_THEOREM_THREAD_D_PHASE_HALO_COMMONQ_ADDRESS_EXPORT_AND_CIRCUIT_GATE_20260801.md`  
Status: the fixed-row maximal-word theorem and the halo residence/census
claims are sound.  The initial two-phase Hall paragraph needed a
paired-left-shore correction and two scope statements needed weakening.
All three corrections are present in the current audited theorem.

## 0. Verdict

There is no flaw in the algebraic six-edge circuit or in its source no-go.
Independent replay confirms:

* raw minimum four edges with repeated owner `ht`;
* owner-disjoint minimum six edges, uniquely the displayed circuit in the
  literal six-label alphabet;
* exactly six phase-private maximal-erosion addresses;
* exactly four failed owner reconstructions in every `4<=d<=64`; and
* the dimension-uniform `d+2` edge lower bound per resident separated halo.

The general maximal-word criterion in Section 1 is also correct, provided
all of the following are fixed before it is invoked:

1. the physical source-address set and its common/private partition;
2. one complete cap state;
3. every target row, witness interval, and frozen exterior contribution; and
4. every equality incidence between rows and live source addresses.

It is an iff theorem for that fixed monotone equality system.  It does not
choose upper/compiler witness intervals, enforce injectivity, or encode
forbidden extra occurrences.

The material defect in the initial draft was in the two-phase extension of Section 3.  Pairing
only the right-hand physical addresses while retaining phase-labelled left
requirements is not ordinary Hall for a common allocation.  Both shores
must be paired (or the left shore must already consist of unphased common
tasks).  The current draft does this explicitly.

## 1. Fixed-row mixed maximal words

For common source positions `C` and phase-private positions `H`, the proposed
maximal letters are

\[
 K_p^C=P_p\cap\bigcap_{\epsilon,R:p\in J^C_{R,\epsilon}}
 S_R^\epsilon,
 \qquad
 K_p^\epsilon=P_p\cap\bigcap_{R:p\in J^H_{R,\epsilon}}
 S_R^\epsilon.                                      \tag{1.1}
\]

If a feasible word exists, every incident live letter is contained in its
corresponding `K`.  Hence replacing all live letters by the `K` rows can
only add coordinates which already lie in every incident target.  The
reconstruction equalities are therefore necessary and sufficient.  The
proof in the audited note is complete.

Three qualifications are load-bearing.

### 1.1 Witness addresses must already be selected

An assertion that a target is realized by *some* interval is a disjunction
over incidence sets.  It is not one row of (1.1).  To include an upper or
compiler witness, first select its physical interval, then insert the
corresponding equality row.  Variable witness selection remains an outer
SAT/matching problem.

### 1.2 Equality rows do not impose injectivity or negative constraints

The criterion can force the OR at a declared interval.  It cannot by itself
ensure that two targets use distinct physical cells, forbid an undeclared
duplicate colour, or prohibit an extra interval value.  Address injectivity
belongs to the corrected Hall theorem below.  Any forbidden-row condition
must be checked after constructing the maximal word or encoded separately.

### 1.3 Six private addresses are not a cap certificate

For the literal six-edge halo, the two maximal erosions differ at exactly

\[
                  0,1,d+2,d+4,2d+5,2d+6.             \tag{1.2}
\]

This proves that phase disagreement is localized to six source addresses.
It does not prove that the unions of the two phase letters lie in legal
rank/pin/owner caps at those addresses.  Thus “no diffuse source
disagreement” is proved; “no cap conflict” is not, until explicit `P_p` are
supplied and audited.  The four failed reconstructions show that caps cannot
rescue this particular circuit, but they do not establish cap legality.

## 2. Equal length versus safe addressed replacement

For `W` consecutive depth-`d` owner windows, the incident source span has
`W+d` positions.  The audited counting is correct: replacing two direct
edges by the six-edge circuit adds four owner rows and four source
positions, and a resident separated subdivision has charge at least
`2d+2`.

The terminology should nevertheless separate two statements.

* **Scalar equal length** means that old and new source words have the same
  number of positions.
* A **proof-safe addressed replacement** additionally needs a fixed support
  identification or address bijection, all crossing-row equalities, and the
  protected-occurrence allocation.

An equal-length word can fail every target row; absence of an address
bijection does not make its scalar lengths unequal.  Accordingly the phrase
“equal-length only when” in Section 2 should read “a safe zero-charge
replacement is certified only when.”

## 3. Correct Hall formulations

### 3.1 One fixed phase

For a fixed phase word, fixed cap/guard state, protected requirement multiset
`U`, and available physical cells `V`, the graph stated in the audited note
is exact.  An injective export exists iff

\[
                         |N(X)|\ge |X|\quad(X\subseteq U). \tag{3.1}
\]

### 3.2 Two phases with a fixed common allocation

Let `U_0,U_1` be the phase-specific requirement sets and let

\[
 \psi:U_0\longrightarrow U_1,qquad
 \phi:V_0\longrightarrow V_1                           \tag{3.2}
\]

be the fixed intended task and address alignments.  Form the paired graph
with left vertices

\[
                     \widehat U=\{(u,\psi(u)):u\in U_0\} \tag{3.3}
\]

and right vertices

\[
                     \widehat V=\{(v,\phi(v)):v\in V_0\}. \tag{3.4}
\]

Join the two pairs exactly when `u` is admitted at `v` in phase zero and
`psi(u)` is admitted at `phi(v)` in phase one.  A common allocation exists
iff this paired graph satisfies Hall.

Equivalently, if the target tasks are intrinsically phase-common, start with
one unphased left task for each target and use (3.4) on the right.  This is
the special case intended by the audited paragraph.

If `psi` or `phi` is variable, choosing it is an additional coupled
matching/hypergraph problem.  Hall for either marginal graph is not
sufficient.

### 3.3 Smallest counterexample to the current wording

Take one logical task `u`, one physical address in each phase, and suppose
both phase incidences are legal.  The common allocation plainly exists: use
that aligned address for `u` in both alternative words.

If the left shore is instead the phase-labelled multiset `{u_0,u_1}` while
the aligned address pair is collapsed to one right vertex, the displayed
Hall test fails on the two-element left set:

\[
                              1=|N(\{u_0,u_1\})|<2.    \tag{3.5}
\]

Thus pairing only the right shore gives a false negative.  Separate phase
vertices on both shores give two matchings but do not enforce common
allocation.  The paired-paired graph (3.3)--(3.4) is the exact object.

## 4. Residence and finite-census audit

The finite script is sound within its declared scope.  Paths of total size
at most six have at most five edges on either shore, so the per-shore cutoff
five exhausts the asserted minimum and uniqueness claims.  Cross-halo owner
disjointness is correctly imposed in each phase, and the involution carries
it to the other phase.

The maximal-erosion calculation is also exact.  A source letter incident to
an owner row is contained in that owner; hence it is contained in the
intersection of all incident owners.  Failure of the maximal erosion to
reconstruct a row rules out every smaller source word.  The two internal
positive runs `0,1,1,0` account precisely for the four mismatches.

The general parity proof correctly requires per-shore lower neutrality.
The separated alphabets make the left and right lower triple supports
disjoint, so global neutrality implies the two hypotheses separately.  No
claim is established for a nonlocal circuit which borrows labels across the
two shores.

## 5. Corrected surviving gate

After these scope corrections, the useful theorem is:

> Fix a complete common/private cap state, every row/witness incidence, a
> paired cross-phase task alignment, and a paired physical-address
> alignment.  The maximal-word reconstruction equalities and Hall in the
> paired-paired occurrence graph are necessary and sufficient for that
> fixed state.  The six-edge direct halo fails the reconstruction rows, and
> every resident separated direct halo has growing length.

The remaining positive route is therefore genuinely nonlocal: construct an
equal-length resident rethread, fix its phase task/address pairings, and then
apply the corrected two-stage test.  Signed telescoping alone supplies none
of those quantifiers.

## 6. Replay/provenance note

The supplied finite payload was originally reported as `e7dc2426...`.  The
script hashes the independent residence theorem as a dependency.  After
that dependency was frozen, a clean replay produced the same census and
owner rows but a new payload hash.  This is provenance drift, not a change
in the mathematical result.  The regenerated replay is byte-identical to
the current JSON:

```text
MATH_THEOREM_THREAD_D_PHASE_HALO_COMMONQ_ADDRESS_EXPORT_AND_CIRCUIT_GATE_20260801.md
  SHA-256 6e990a9e226b98a6d209162b23762e608d4a8b8005cddc04b8fbd20d489d972b
scratch/audit_threadD_c8_phase_halo_circuit_20260801.py
  SHA-256 0d50111c5af80b8fd92bece7f3e8eade1fc4ddb0e9d51828609761e6b5b431f2
scratch/threadD_c8_phase_halo_circuit_20260801.audit.json
  SHA-256 88f3ecec3cb94dc12b6084624965b5a39e7952d9aa9550f2e2bed640ff9a784d
  payload efc80c846cfb91747fb1d809a5a8a919a0508125e60a2727ce8ce9ade08999ad
```
