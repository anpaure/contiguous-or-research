# Odd APH collapses to one four-task anchored-catalyst staging lemma

**Date:** 2026-08-06  
**Method:** exact signed charge, zero-charge atom removal, a bounded staging
bank, and copy-before-erase of the collar order; no computation or search  
**Status:** unconditional algebraic reduction.  All scalar, task-count,
staging-capacity, collar-order, and final scheduling rows are proved.  One
literal occurrence-serialization statement, `ACT4` below, remains open.

## 1. Reserve a bounded staging bank

Continue to use

\[
 A=00,\quad B=20,\quad C=22,\quad H=02,\quad M=11.
\]

Besides the protected first connector and the two fixed collar blocks,
reserve four consecutive ordinary work blocks next to the collar.  They are
the **staging bank**.  Deleting these seven connector occurrences leaves a
linear word of length \(m-7\) and imbalance at most seven.

The proof of the reserved-collar one-atom theorem gives the general fact

\[
 \left.
 \begin{array}{c}
 |\#A-\#C|\le b,\\
 \text{no transition and no }BB
 \end{array}
 \right\}
 \quad\Longrightarrow\quad |w|\le2b+1.             \tag{1.1}
\]

Indeed, at most \(b\) extremes of one sign create at most \(b+1\) singleton
`B`-runs.  Consequently the remaining word contains an ordinary atom once

\[
                         m-7\ge16.                   \tag{1.2}
\]

Thus the reduction below is uniform for \(m\ge23\), equivalently
\(k=2m-1\ge45\).  A better staging theorem may lower this inessential
asymptotic threshold.

## 2. Choose the atom before the residual bank

Choose one ordinary atom in the word from Section 1 and remove its complete
support from the cancellation input.  It has zero signed extreme charge:
a transition atom contains one `A` and one `C`, while a `BB` atom contains no
extreme.

Now run the deterministic noncrossing cancellation on the remaining source
word.  Removing a zero-charge atom does not change the residual charge.
Therefore the residual extreme bank still contains

\[
                         t=|q|\le3                  \tag{2.1}
\]

labelled blocks, all of one sign.  They are automatically disjoint from the
atom.  Add the ordinary two-coordinate zipper record `(G_1,B_2)` as one
further labelled task.  There are at most

\[
                              t+1\le4               \tag{2.2}
\]

remote tasks, exactly the capacity of the staging bank.

For task \(i\), write its source and setup-target blocks as \(X_i,X_i'\).
For residual tasks, \(X_i\in\{A,C\}\) and \(X_i'=M\).  The remaining task
is `(G_1,B_2)->(G_1^*,B_2)`; omit it when the change is zero.

## 3. The complete scalar equation is one fixed-mass row

Let the ordered source collar be \(K=C(a)|C(b)\).  The zipper-split balance
theorem is exactly

\[
 \boxed{
   \operatorname{mass}(K)+\sum_i\operatorname{mass}(X_i)
      =4+\sum_i\operatorname{mass}(X_i').}
                                                        \tag{3.1}
\]

The number four on the right is the mass of `H|H`.

### Lemma 3.1 (bounded collar conversion has no connectivity obstruction)

After the task blocks have been placed in the four staging slots, there is
an unlabelled literal path on the collar plus staging support from

\[
                         K|X_1|\cdots|X_s
         \quad\hbox{to}\quad
                         HH|X_1'|\cdots|X_s',         \tag{3.2}
\]

where \(s\le4\).  The path may hold one external catalyst block fixed.

#### Proof

Equation (3.1) puts the two endpoint words in the same fixed-mass layer of
the capacity-two token graph on at most twelve coordinates.  This layer is
nonextreme.  If it had mass zero, the target `HH` could not occur; if it had
maximum mass, the same conclusion follows because `HH` is not all twos.
Every nonextreme fixed-mass layer on a path is connected: move one unit from
the first prefix excess to the next prefix deficit, decreasing the sum of
absolute prefix discrepancies.  Removing loops gives a simple path.  A
fixed external block is not part of this calculation.  \(\square\)

Likewise, there is no unlabelled obstruction to placing the tasks in the
staging bank.  Adjacent transpositions generate every permutation of block
positions.  If two adjacent blocks are unequal, their four-coordinate total
mass is nonextreme and the same token-graph argument interchanges them; if
they are equal, the transposition is a zero-length identity.

This proves that the remaining issue is serialization, not reachability.

## 4. The collar itself stores its order while the atom record is busy

The outside decoded source determines \(a+b\).  Within a fixed sum there are
at most three ordered collar types.  Use the three mass-four words

\[
                         R_0=H|H,\qquad
                         R_1=H|M,\qquad
                         R_2=M|H                         \tag{4.1}
\]

as order records, assigning them injectively within each fixed sum fibre.

Replace the endpoint `HH` in (3.2) by the appropriate `R_j`; the mass is
unchanged, so Lemma 3.1 still applies.  Keep `R_j` at the fixed collar berth
while the staged target blocks are scattered back to their labelled source
addresses and while the temporary source atom is restored **to its original
source value**.

At that checkpoint the source atom is literal again, so it labels a route
of the four-state register from its temporary atom code to the collar-order
class \(j\).  This is copy-before-erase: throughout the route both the
literal source atom and `R_j` are present.  Then hold the register endpoint
fixed and use a simple mass-four path

\[
                              R_j\leadsto H|H.          \tag{4.2}
\]

The fixed berth and register class label every strict state.  Thus the
permanent cart is created only after the temporary catalyst has been retired,
and no `HHHH` coexistence state is needed on this route.

### Lemma 4.1 (order-copy schedule is occurrence-safe)

Conditional only on an occurrence-labelled gather/scatter path, the schedule
in this section retains the atom type, collar order, source, and stage at
every checkpoint and strict collar state.

#### Proof

Before (3.2), the literal source collar labels its order.  During the bounded
conversion, the temporary atom register and the unchanged exterior source
label the chosen simple path.  Afterward `R_j` labels the collar order while
the atom register labels the temporary atom.  Once the atom is restored, its
literal source labels the register rewrite to class \(j\).  Finally the
register labels (4.2).  There is therefore no checkpoint at which both the
old and new copy of either datum are absent.  \(\square\)

## 5. The one exact remaining lemma

The algebra above motivates the following literal statement.

### Anchored-catalyst four-task staging lemma `ACT4`

Start with:

1. a raw decoded work word;
2. one zero-charge source atom carrying the four-state early record;
3. one head held at the atom origin and the other available as a mobile
   catalyst;
4. at most four labelled task occurrences disjoint from the atom; and
5. four named staging slots at the fixed collar side.

There are pairwise source-disjoint directed paths which:

1. gather the source task blocks, without changing their values, into the
   staging slots;
2. retain an occurrence decoder while the fixed-mass collar path of Lemma
   3.1 writes `R_j` and the task targets;
3. scatter every target task block back to its own labelled source address;
4. return both atom heads to their recorded source support and reverse the
   atom bootstrap; and
5. preserve the active first selected row and the protected boundary
   register throughout.

The task and staging count in `ACT4` is an absolute four.  No growing tape
compiler or mass reservoir is hidden in the statement.

### Theorem 5.1 (`ACT4` implies odd APH)

If `ACT4` holds, then the Anchored Pre-Head Bootstrap lemma holds for every
odd \(k\ge45\).  Consequently the already proved fixed-head marked/LIFO
recoder, connector beta, and monotone post-beta accumulator give the full
odd transition in every sufficiently large odd dimension.

#### Proof

Sections 1--2 supply the recorded atom and the at most four disjoint tasks.
Apply `ACT4`, using the endpoint `R_j` in the fixed collar path.  Lemma 4.1
then transfers the collar order to the protected register and writes the
source-independent permanent `H|H` at the fixed berth.  The temporary atom
has already returned to its raw source, so the entire ordinary tape is again
in the input alphabet expected by the bulk theorem.

Invoke the fixed-head marked/LIFO theorem to complement the ordinary tape,
then connector beta and the post-beta terminal accumulator.  Every theorem
now receives its stated literal input.  Finitely many odd dimensions below
45 may be absorbed into the base constant of an asymptotic same-parity
induction.  \(\square\)

## 6. Sharp proof boundary

`ACT4` cannot be replaced by the sentence "the relevant token layer is
connected."  Connectivity proves (3.2) and block permutations only as
unlabelled walks.  During a remote interchange the mobile `H` can disappear
at a strict fixed-mass state, and two different task addresses can then use
the same local word.  The old `ACB/BAC` and `ABCB/ACBB` examples demonstrate
exactly this distinction between reachability and occurrence serialization.

The early four-state atom theorem supplies a stationary origin and fixes the
old private/raw collision, so those examples are not counterexamples to
`ACT4`.  They show why a proof of `ACT4` must include a literal cursor/trail
decoder rather than appeal only to the symmetric group or token-graph
connectivity.

Thus the odd pre-head package has been reduced to one bounded, explicit
serialization lemma.  All other rows in its staging and collar ledger are
closed in this note.
