# Thread D: exact global exchange/CEGAR model for the K16 length-12,874 one-hole basin

**Date:** 2026-07-30  
**Status:** proof-safe model and exact reductions; no optimal length-12,874 word is claimed here

## 1. Frozen basin and objective

Let

```text
B = scratch/k16_ripple_insert12874_onehole.word
length 12874
SHA-256 5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db
```

Exact ending-OR replay gives the single missing nonzero mask

\[
 h=10365=\mathtt{0x287d}.
\]

The replay has 50,170 masks of multiplicity one and 8,188 of multiplicity
two.  Thus this is a one-hole basin, not a length-12,874 certificate.

The clean operation metric is substitution radius

\[
 \rho(B)=\min\bigl\{|\{i:C_i\ne B_i\}|:
            C\in(2^{[16]}\setminus\{\varnothing\})^{12874},\ C
            \text{ is interval-OR universal}\bigr\}.
\tag{1.1}
\]

Every macro operation must be materialized as a literal word and charged by
the number of changed positions in (1.1).  This avoids assigning an ambiguous
cost to a deletion-shift or a segment move.  Since \(B\) has a hole,
\(\rho(B)\ge1\).

The old length-12,873 fixed-support formulas and the one-bit portal catalogues
do not decide (1.1): arbitrary nonzero replacement masks, multi-edit witnesses
of \(h\), and the extra physical position must all be retained.

## 2. Exact exchange hypergraph

For a consistent finite substitution set \(E\), write \(B^E\) for the
literal edited word and \(c_E(T)\) for the number of intervals of \(B^E\)
whose OR is \(T\).  Define

\[
 L(E)=\{T:c_\varnothing(T)>0=c_E(T)\},\qquad
 G(E)=\{T:c_\varnothing(T)=0<c_E(T)\}.
\tag{2.1}
\]

An edit set is a successful balanced exchange precisely when

\[
 h\in G(E),\qquad L(E)=\varnothing.
\tag{2.2}
\]

This is the exact gain/loss hypergraph.  Atomic columns are not generally
additive.  If

\[
 \kappa_J(T)=\sum_{I\subseteq J}(-1)^{|J|-|I|}c_I(T),
\]

then \(c_E(T)=\sum_{J\subseteq E}\kappa_J(T)\); therefore a linear return
cycle is proof-safe only after all relevant higher interactions have been
shown to vanish.  The default implementation must instead evaluate the
simultaneous literal edit set by the exact interval-multiplicity delta
recurrence.

Two useful one-edit roots illustrate the current geometry:

* \(B_{6439}:\mathtt{0x2879}\mapsto\mathtt{0x287d}\) installs \(h\) and
  leaves exactly
  \(\{10361,26745,43129,59513\}\);
* \(B_{12873}:\mathtt{0xce41}\mapsto\mathtt{0x287d}\) installs \(h\) and
  leaves only \(\{52833,52835\}=\{\mathtt{0xce61},\mathtt{0xce63}\}\).

The second is the best immediate debt count, but debt count is only a search
score.  Closing its two debts by one more edit would rule in a radius-two
word; failure with that first edit fixed would not exclude a synergistic
radius-two witness of \(h\).

The complete arbitrary-substitution census has now been carried out using
the exact context-multiplicity identity, not a bit-flip restriction:

* exactly 26,889 position/value pairs install \(h\);
* none is lossless, so \(\rho(B)\ge2\);
* the minimum debt is two, attained exactly 169 times;
* those minimizers occur in four families:

| position | replacements | exact debt pair |
|---:|---:|---|
| 0 | 128 | \(\{43117,44141\}\) |
| 5921 | 8 | \(\{10553,10557\}\) |
| 6440 | 32 | \(\{43129,43133\}\) |
| 12873 | 1 | \(\{52833,52835\}\) |

For the last family, a complete second-substitution return census finds
2,285 substitutions capable of restoring both debts and no completion.
The 128 debt-one returns merely edit position 12873 again and lose \(h\).
Among the 2,157 off-terminal returns, the minimum new debt is four.  Hence
the radius-two master may soundly exclude the guarded branch
\(C_{12873}=\mathtt{0x287d}\), but this remains a fixed-root cut rather than
a global radius-two theorem.  The exact statement and literal insertion
provenance are recorded in
THREAD_D_K16_RIPPLE_ONEHOLE_SUBSTITUTION_RETURN_GATE_20260730.md.

## 3. Complete final-witness localization at fixed radius

The following lemma removes every arbitrary-width qualification.

### Lemma 3.1 (source-bad interval localization)

Fix a target \(T\ne0\) and a radius bound \(r\).  For an interval
\(I=[a,b]\), put

\[
 M_T(I)=\{i\in I:B_i\not\subseteq T\}.
\tag{3.1}
\]

If a word \(C\) at substitution distance at most \(r\) from \(B\) has
\(\bigvee_{i\in I}C_i=T), then

\[
 M_T(I)\subseteq\{i:C_i\ne B_i\},\qquad |M_T(I)|\le r.
\tag{3.2}
\]

Conversely, after the final values on \(I\) are specified, the conditions

\[
 C_i\subseteq T\quad(i\in I),\qquad
 \bigvee_{i\in I}C_i=T
\tag{3.3}
\]

are exactly the assertion that \(I\) witnesses \(T\).

**Proof.** Every source cell carrying a bit outside \(T\) must change, proving
(3.2).  Conditions (3.3) say respectively that the final OR has no outside
bit and has every bit of \(T\).  They are therefore necessary and sufficient.
\(\square\)

For each left endpoint, \(|M_T([a,b])|\) is monotone in \(b\).  Hence all
possible radius-\(r\) witness intervals are enumerated by extending \(b\)
only until the \((r+1)\)-st source-bad cell.  This is a global enumeration,
not a width cutoff.

For the frozen \(h=\mathtt{0x287d}\), a lightweight geometry replay gives

| radius \(r\) | possible source-bad intervals | distinct mandatory supports | maximum interval length |
|---:|---:|---:|---:|
| 1 | 13,584 | 12,556 | 5 |
| 2 | 26,782 | 25,110 | 6 |
| 3 | 39,981 | 37,663 | 7 |
| 4 | 53,175 | 50,215 | 8 |

Thus the eager missing-\(h\) row is small even though the word has 12,874
positions.

### Corollary 3.2 (complete radius-one census)

In any one-substitution completion, the changed cell belongs to the new
\(h\)-witness, so its replacement is a nonzero submask of \(h\).  Since
\(|h|=8\), the complete radius-one domain is

\[
 12874(2^8-1)=3,282,870
\tag{3.4}
\]

position/value pairs.  For each pair, exact suffix/prefix OR states compute
the entire multiplicity delta of intervals through the changed position.
The completed context-filtered census reduces these 3,282,870 necessary
position/submask pairs to 26,889 actual installers and proves that all of
them incur debt.  A census restricted to one-bit flips would not have proved
this radius-one theorem.

## 4. A global radius-\(r\) CEGAR, without a fixed support

There is a compact exact master that does not guess an editable collar.
For every physical position \(i\) and coordinate \(b\), introduce a final-bit
variable \(f_{i,b}\), and introduce

\[
 u_i=[(f_{i,0},\ldots,f_{i,15})\ne B_i].
\]

Encode this equivalence in both directions, require every final cell to be
nonzero, and impose

\[
 \sum_i u_i\le r
\tag{4.1}
\]

(or equality \(r\) when lower radii have already been excluded).  This uses
about \(17\cdot12874=218,858\) primary Boolean variables before the
cardinality counter.

For a separated target \(T\), enumerate

\[
 \mathcal I_r(T)=\{I:|M_T(I)|\le r\}.
\]

For every \(I\in\mathcal I_r(T)\), add a witness literal \(w_{T,I}\) and
the implications

\[
\begin{aligned}
 w_{T,I}&\Longrightarrow \neg f_{i,b}
       &&(i\in I,\ b\notin T),\\
 w_{T,I}&\Longrightarrow \bigvee_{i\in I} f_{i,b}
       &&(b\in T).
\end{aligned}
\tag{4.2}

Finally add

\[
 \bigvee_{I\in\mathcal I_r(T)}w_{T,I}.
\tag{4.3}

By Lemma 3.1, (4.2)--(4.3) are equivalent to literal coverage of \(T\)
inside the global radius-\(r\) domain.  Only the forward implication for a
witness literal is needed: (4.3) forces at least one exact physical witness.

The CEGAR loop is then:

1. install (4.1) and the eager row for \(h\);
2. solve for a candidate final word;
3. replay all 65,535 masks using an independent ending-OR recurrence;
4. if the word is universal, run the independent literal verifier and stop;
5. otherwise add (4.2)--(4.3) for one or more replayed missing masks and
   repeat.

Every negative replay adds an exact row false at the current candidate, so
progress is strict.  There are only 65,535 target rows.  A final SAT candidate
is accepted only by literal replay.  A completed UNSAT solve of any CEGAR
relaxation is already a valid radius-\(r\) no-go, because every universal word
satisfies every installed row; omitted rows cannot invalidate UNSAT.  A time
or resource limit remains `UNKNOWN`.

For a proof-producing negative result, emit the accumulated master as CNF,
solve it with a proof-producing solver, and retain/check the proof.  CP-SAT is
appropriate for discovery, but an `INFEASIBLE` status without a proof log
should be described as exact solver evidence rather than a formal certificate.

### Permanent-provider compression

Let \(\mathcal W_B(T)\) be the old witness intervals for \(T\).  If it
contains \(r+1\) pairwise vertex-disjoint intervals, at most \(r\) edited
positions cannot meet all of them; one untouched witness survives.  Interval
scheduling by earliest right endpoint computes this packing number exactly.
Such a target can never be separated and needs no row.  This is especially
useful for high-rank targets whose raw set \(\mathcal I_r(T)\) can be large.

## 5. Final-witness branching and balanced return cycles

The exact alternative to the global Boolean master is a sparse
branch-and-price search.

1. Choose a final witness interval for \(h\) from
   \(\mathcal I_r(h)\), not merely an edit that happens to repair \(h\) in
   isolation.
2. Commit the literal constraint (3.3) on that interval.
3. Exact-replay the simultaneous partial assignment.  For a missing target
   \(T\), branch over its possible **final** witness intervals in
   \(\mathcal I_r(T)\), merging compatible value constraints.
4. Preserve all committed witness equations while extending the branch.
5. Prune once the forced edit support exceeds \(r\), or when a bit-domain or
   target-provider Hall test is empty.

Committing final witnesses is essential.  A naive Algorithm-X walk that
repairs a currently missing target and later permits its witness to be
destroyed is not a completeness proof; coverage is nonmonotone under edits.

The natural Benders cuts are therefore:

* **empty provider row:** no interval in \(\mathcal I_r(T)\) is compatible
  with the current guards;
* **support budget row:** every compatible \(T\)-interval forces a set of
  new edits whose union exceeds the remaining radius;
* **proper Hall row:** a set of committed targets has fewer compatible
  physical witness intervals than targets (physical intervals have capacity
  one, even when equal OR bases are compressed with multiplicity);
* **exact value no-good:** exclude a replayed final-bit assignment when no
  smaller guarded provider cut was extracted.

All of these cuts concern final physical witnesses.  Static signed gain/loss
columns are ordering data only unless their interaction terms have been
audited.

## 6. Immediate branch schedule

The proof-safe order is:

1. retain/replay the completed arbitrary-substitution radius-one no-go;
2. run the global CEGAR at \(r=2\), eagerly installing the
   \(h\)-row and using the tail portal
   \(12873:\mathtt{0xce41}\mapsto\mathtt{0x287d}\) as a hint;
3. install the completed fixed-tail return no-good, then prioritize the other
   168 minimum-debt portal branches and the joint-only \(h\)-witness branches;
4. if the global radius-two master is UNSAT, continue \(r=3,4,\ldots\),
   adding target rows lazily and retaining every proof/replay artifact.

The fixed-tail branch is valuable as a candidate generator, not as a
substitute for the global \(r=2\) formula: a two-edit solution may create
\(h\) only through the interaction of both edits.

## 7. Reusable implementation pieces and required corrections

The following code can be reused after explicit scope changes.

* `scratch/k16_noncontiguous_ruin_recreate_20260730.cpp` contains a
  word-length-generic exact multiplicity `Coverage`, `RangeOr`, and
  simultaneous-substitution `Evaluator`.  Extract these routines; do not use
  its hard-wired portal/search `main` for this basin.
* `scratch/k16_noncontiguous_balanced_exchange_exact_20260730.cpp` already
  performs simultaneous exact replay after merging rows.  Its row generator
  is restricted to width 48 and Hamming distance at most two, so exhaustion
  is only a scoped catalogue theorem.  Replace that generator by Lemma 3.1
  for a global radius claim.
* *scratch/k16_dynamic_fixed_substitution_cnf_20260730.cpp* now wraps the
  frozen fixed-run/block encoder with dynamic length and exact budgets 1--12.
  Together with
  *scratch/decode_verify_k16_dynamic_fixed_substitution_20260730.py* and
  *scratch/audit_k16_dynamic_fixed_substitution_encoding_logic_20260730.py*,
  it is the proof-safe finite-support implementation.  Fixed-support UNSAT
  is still not a global radius theorem.
* `scratch/audit_k16_trimmed_lift_exchange_portal_radius_20260730.py` contains
  the exact left-suffix/right-prefix reduction.  Its assertion that the
  common submask family has size 15 is specific to the old portals; here the
  radius-one envelope has size 255.  It also needs exact loss replay for every
  \(h\)-gaining candidate.
* `scratch/k16_12873_portal_prepayment_cpsat_20260730.py` carries exact
  multiplicity-weighted block bases and is useful for a two-state
  preserve-then-fire experiment.  The one-hole length-12,874 master itself is
  simpler: it needs only final coverage and the radius constraint.

Every derived artifact should use a new `threadD_k16_12874_onehole_*` prefix.
Old K16-12873 maps, CNFs, decoders, and UNSAT scopes must not be relabelled as
evidence for this basin.

## 8. Sharp remaining gate

The current mathematical gate is no longer an append-capacity question.  The
length-12,875 certificate shows that one extra literal cell trivially closes
the remaining mask.  Optimal length 12,874 asks whether the missing target
can be installed by a balanced same-length exchange.  The exact dichotomy is:

* a radius-one lossless substitution;
* a higher-radius interacting circuit satisfying (2.2), including the
  possibility that no proper sub-edit already witnesses \(h\).

Lemma 3.1 and the global target-row CEGAR cover both cases without a local
width assumption.
