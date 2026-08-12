# Adversarial audit of the octagon two-exterior-host reset

Date: 2026-08-01  
Lane: AD cross-audit of Thread D exterior OR interface  
Status: the two-host OR algebra is exact; this audit found the necessary
cross-phase matching hypothesis, now incorporated into the corrected reset
theorem.  Ambient owner, q1, residence, deadline and prescribed-cap legality
remain unproved.

## 1. Verdict

Let

\[
 X_L=\{a_0,a_1\},\qquad X_R=\{a_1,a_2\}.
\]

For both the maximal and sharp depth-\(d\) tensor inverses, the two exterior
binary splits in
`MATH_THEOREM_THREAD_D_OCTAGON_SPLIT_BOUNDARY_RESET_20260801.md` have the
following exact properties.

1. Their packet-near halves create precisely the opposite-phase typed masks
   \(\Pi_{1-\epsilon}\) and \(\Sigma_{1-\epsilon}\).
2. Relative to the already extended word \(X_L\mid Q^\epsilon\mid X_R\),
   they add exactly two positions.
3. Every old physical interval has an injective full-block lift of identical
   OR.  Thus the entire old OR deck of **that same phase** is preserved.
4. The free positionwise cap at the two left positions is \(X_L\), and at
   the two right positions is \(X_R\), in both orientations.

These conclusions do not construct the two exterior hosts, an owner word for
the added positions, prescribed caps, or fixed-width deadlines.  Relative to
the bare tensor, planting the two hosts costs four positions, not two.

The reset/nonaccumulation conclusion was not valid under the three hypotheses
originally listed in Theorem 4.1.  Contraction safety is a within-phase
statement.  Replacing \(Q^\epsilon\) by \(Q^{1-\epsilon}\) is a separate
operation, and the two source interval decks are not equal.  The corrected
theorem now also assumes a simultaneous matching after phase replacement for
the entire protected occurrence bank.  With this fourth hypothesis, the
reset proof is sound and gives \(\Phi'\le2\) for that transition.  A uniform
bound through a recursion requires the same certificate at every transition.

## 2. Exact ray identities

Write \(F\) for the filler bank and retain the fixed core \(K\).  Both source
phases have the literal boundary unions

\[
 R_L=K\cup F\cup\{z,a_2,a_3\},\qquad
 R_R=K\cup F\cup\{z,a_0,a_3\}.
\]

The oriented exterior blocks are

\[
\begin{array}{c|cc}
 &X_L\ ({\rm far},{\rm near})&X_R\ ({\rm near},{\rm far})\\ \hline
0&(a_0,a_1)&(a_2,a_1)\\
1&(a_1,a_0)&(a_1,a_2).
\end{array}
\]

Consequently their near-side cells are exactly

\[
 \{a_{1-\epsilon}\}\cup R_L=\Pi_{1-\epsilon},\qquad
 R_R\cup\{a_{2-\epsilon}\}=\Sigma_{1-\epsilon}.
\]

This proves the claimed two typed rays.  It also reconciles the result with
the AD polarity no-go: that no-go excludes **tensor-internal** refinements.
The successful letters are additional exterior hosts, so there is no
contradiction.

## 3. Full-block preservation and cap scope

For an old interval \([i,j]\), start at the first piece replacing the old
letter at \(i\) and stop at the last piece replacing the old letter at
\(j\).  The refined interval is distinct for every old endpoint pair and its
OR is unchanged.  This proves occurrence-level injection within one phase,
not merely equality of distinct mask sets.

At each of the two left split positions, the union of the phase-zero and
phase-one pieces is \(X_L\); analogously it is \(X_R\) at each right split
position.  Hence the theorem constructs a free common cap family.  It does
not prove that these repeated caps occur in a prescribed parent cap word, nor
that the added source positions dilate to legal Johnson owners.  Those are
correctly left as ambient hypotheses.

## 4. The missing reset quantifier

The two target pairs themselves do reset locally.  On changing phase, the
old side targets become the new native pair, and reversing the two split
orientations creates the newly missing pair.  Thus the four typed boundary
occurrences admit the intended bijection.

This does not transport an arbitrary protected bank through the change from
\(Q^\epsilon\) to \(Q^{1-\epsilon}\).  The failure is literal.  For the sharp
inverse at \(d=1\), put

\[
                         S=\{z,a_3,f_0\}.
\]

In the contracted phase-zero extended word, \(S\) is the singleton source
letter \(Q^0_{26}\) (extended-word position 27).  Its witness is unaffected
by either exterior split and is safe under simultaneous contraction.  Yet
\(S\) is absent from the complete interval deck of both the contracted and
expanded phase-one words.  Therefore within-phase full-block lifting plus
contraction Hall cannot imply that all inherited targets survive phase
replacement.

The corrected statement is the following.

### Corrected conditional reset theorem

Suppose, for one transition \(\epsilon\to1-\epsilon\), that:

1. both oriented exterior refinements obey all owner, q1, residence,
   deadline and prescribed-cap constraints;
2. simultaneous contraction of the two old blocks has a contraction-safe
   matching for the protected bank;
3. after replacing the contracted packet by the opposite phase, the entire
   protected occurrence bank together with the two old side tasks has one
   simultaneous matching to opposite-phase native/full-block cells, with the
   native \(\Pi_{1-\epsilon},\Sigma_{1-\epsilon}\) cells available; and
4. the reverse split cells are available for
   \(\Pi_\epsilon,\Sigma_\epsilon\).

Then contract, change phase, apply the matching in item 3, and reverse-split.
Every protected occurrence survives and exactly two split boundaries remain,
so \(\Phi'\le2\).  If this four-part certificate holds after every recursive
transition, the two boundaries do not accumulate.  Without item 3, the only
general estimate remains \(\Phi'\le\Phi+2\).

## 5. Rectangle and residence boundary

The tensor's local full-span rectangle is phase-identical because the total
union is common; it needs no ticket.  Every rectangle value already in the
old deck is transported by full-block lift.  Neither statement repairs the
separate donor-swap rectangle: the AD interior-poison lemma remains a valid
no-go for pure refinements in its frozen chronology.

Likewise OR preservation says nothing by itself about a flat fixed-width
compiler.  Splits lengthen crossing intervals.  The owner, deadline and
residence clauses in the corrected theorem are substantive hypotheses, not
consequences of the two ray identities.

## 6. Replay

Run

```text
python3 scratch/audit_ad_threadD_octagon_twohost_reset_scope_20260801.py --write
```

The replay checks depths \(1\le d\le12\), both maximal and sharp inverses,
both ray identities, every old-interval full-block lift, the free
positionwise caps, and the explicit cross-phase counterexample.  It is a
finite audit of the displayed constructions; the all-\(d\) identities remain
the symbolic proofs above.
