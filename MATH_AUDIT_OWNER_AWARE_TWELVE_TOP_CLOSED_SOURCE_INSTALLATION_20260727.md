# Independent audit of owner-aware twelve-top closed source installation

Date: 2026-07-27

Audited file:
`MATH_THEOREM_OWNER_AWARE_TWELVE_TOP_CLOSED_SOURCE_INSTALLATION_AND_PHYSICAL_LEAVE_20260727.md`

Method: independent coefficient and implication check.  No computation,
search, solver, web input, or probabilistic black box is used.

## 0. Verdict

The decisive claims pass, with the scope stated in the theorem.

* The set (Q_T(B)) is exactly, not just approximately, the additional
  deletion-only row leave.
* The condition

  \[
  O(B)\cap\operatorname{mid}\bigl(T\setminus T[U(B)]\bigr)
  =\varnothing
  \]

  is necessary and sufficient for zero-quarantine replacement on the
  bank tops.
* The closed binary system uses actual decorated packet words and is
  equivalent to a coefficient-one physical installation.
* The forced-owner Hall proof is correct, including the small-set/large-set
  split and its explicit hypothesis.
* The exact physical leave formula is correct in both directions.
* The nonmatroid counterexample follows directly from the independently
  proved interior one-window chronology theorem.
* Protected-trace preservation is not silently inferred from owner
  closure; it is correctly imposed as a separate equality.

The theorem does **not** claim an unconditional zero-quarantine bank for
every full table.  Its negative conclusion is the precise one supported
by the proof: ordinary owner Hall and matroid augmentation cannot supply
such a theorem, and a literal residual instance can force one row of
leave.

## 1. Audit of the fixed-bank coefficient ledger

Let

\[
 S=U(B),\qquad Z=O(B),\qquad |Z|=d|S|.
\]

Because the original table is coefficient one, every
(X\in\operatorname{mid}(T)) has a unique owner row.  Therefore the set

\[
 Q=\{\omega_T(X):X\in Z\cap\operatorname{mid}(T),
                         \omega_T(X)\notin S\}
\]

contains every and only nonbank old row which collides with the inserted
bank.

Delete (T[S\cup Q]).  If a surviving old row met (Z), its top would
belong to (Q), contradiction.  Thus the three possible collision
types are all excluded:

1. old--old collisions are excluded by coefficient one of (T);
2. bank--bank collisions are excluded by the packet-bank hypothesis;
3. old--bank collisions are excluded by the definition of (Q).

Hence the installed partial table has exactly

\[
                         N-|Q|
\]

rows and, because every row deck is squarefree of size (d), exactly

\[
                         d(N-|Q|)
\]

used owners.  Its hole count is therefore

\[
 W-d(N-|Q|)=(W-dN)+d|Q|.
\]

This checks the coefficient and row ledgers independently.

For minimality, each (V\in Q) has a witness
(X\in O(t_V)\cap Z).  A deletion-only installation which retained
(t_V) would have load two at (X).  Thus every (V\in Q) is forced,
and deleting exactly (Q) suffices.  The zero case is precisely
(Q=\varnothing), equivalent to the displayed condition above.

## 2. Audit of occurrence-to-row conversion

For (V\in Q), put

\[
                         q_V=|O(t_V)\cap Z|.
\]

Each (q_V) is between (1) and (d).  Distinct old rows have disjoint
owner decks, so the external owner collisions split without
multiplicity ambiguity:

\[
 e_T(B)=\sum_{V\in Q}q_V.
\]

It follows that

\[
 |Q|\le e_T(B)\le d|Q|,
\]

or

\[
 \left\lceil e_T(B)/d\right\rceil\le|Q|\le e_T(B).
\]

Since (e_T(B)\le|Z|=d|S|), the broad twelve-top bank with
(|S|=12n) has the claimed (12nd=O(m^2)) worst-case bound.  No step
mistakes owner occurrences for distinct conflicting rows.

## 3. Audit of the closed decorated-packet system

The variables in the theorem refer to fully decorated packet candidates,
not to top supports alone.  Thus selecting (z_P=1) selects the actual
twelve source words and their actual squarefree (12d)-owner set.

The four constraints have the following literal meanings.

1. The request equation selects one physical source candidate for every
   requested coordinate.
2. The top equation gives at most one selected source row at each top.
3. The owner inequality gives middle coefficient at most one inside the
   selected bank.
4. If a selected bank owner is currently used by (T), the implication
   forces its unique owner top into the selected top set.

After the old rows on the selected tops are removed, item 4 leaves no
old--bank collision.  Thus the selected binary solution itself is the
physical installation promised by the theorem.  Conversely every
zero-quarantine requested bank sets these variables and satisfies all
four constraints.  The equivalence is exact.

The trace equation also has the correct support.  Rows outside the
selected top set occur identically before and after installation and
cancel.  Hence preservation of the old additive ledger is exactly

\[
 \Theta(B^-)=\Theta(T[S]).
\]

The repaired twelve-top theorem then preserves both this trace vector
and the middle-owner vector packetwise through every later firing.

## 4. Independent check of robust Hall extension

In the top--owner containment graph, every top has degree

\[
                         a=\binom MH
\]

and every owner degree

\[
                         b=\binom mH.
\]

For a nonempty remaining top set (A), incidence counting gives

\[
                         |\Gamma(A)|\ge(a/b)|A|
                         =\lambda|A|.
\]

The neighbourhood also contains the complete (a)-set below any one
top, so (|\Gamma(A)|\ge a).  Deleting the (ds) forced owners loses at
most (ds) vertices, giving

\[
 |\Gamma(A)\setminus Z|
 \ge\max\{a,\lambda|A|\}-ds.
\]

There are two exhaustive cases.

* If (|A|\ge ds/(\lambda-d)), then
  (lambda|A|-ds\ge d|A|).
* If (|A|<ds/(\lambda-d)), the assumed inequality
  (a\ge ds\lambda/(\lambda-d)) gives

  \[
  a-ds\ge {d^2s\over\lambda-d}>d|A|.
  \]

Thus the (d)-clone Hall inequalities all hold.  The forced bank plus
the matching of the remaining clones is a full zero-repeat owner-atom
assignment.  Symmetric difference with the old clone matching does
decompose into alternating paths and cycles.

Nothing in this calculation orders the (d) owners at one top or
makes them consecutive windows.  The theorem correctly stops before
claiming a physical lift.

## 5. Audit of the exact physical rank formula

Fix (A\supseteq Q).  Before inserting replacement rows, the owners not
used by unchanged old rows are

\[
                  \mathcal H_T\ \dot\cup\ O_T(S\cup A).
\]

Every bank owner belongs to this union: a covered bank owner is owned
either on (S) or on a top of (Q\subseteq A).  Removing the bank set
(Z) therefore leaves exactly (F_B(A)), of size

\[
 h_0+d(|S|+|A|)-d|S|=h_0+d|A|.
\]

Any family counted by (r_B(A)) consists of literal rows, lies wholly
in this reservoir, and is owner-disjoint.  Inserting it leaves
(|A|-r_B(A)) tops empty, proving attainability.

For the reverse inequality, take an arbitrary final coefficient-one
partial table containing (B^-), and let (A) be exactly the nonbank
tops not retaining their old rows.  Every (Q)-top must occur in (A).
Every new row avoids the unchanged old rows and (Z), so all of its
owners lie in (F_B(A)).  The new rows are therefore one of the
families counted by (r_B(A)).  If the final leave is (ell), their
number is (|A|-\ell), whence

\[
                         \ell\ge|A|-r_B(A).
\]

Minimizing over (A) proves the formula.  This reverse construction is
the decisive step showing that the rank is not merely sufficient.

The trace-faithful refinement is also exact: outside (S\cup A) the
old rows cancel, leaving precisely the balance equation stated in the
theorem.

## 6. Independent audit of the nonmatroid obstruction

Take a legal deck

\[
 D=\{X_1,\ldots,X_d\}
\]

and an interior phase (i) with

\[
                         H+2\le i\le d-H-1.
\]

The one-window chronology theorem proves that if another legal deck has
symmetric difference two with (D), its unique removed member cannot
be (X_i).  Choose any legal deck (D') avoiding (X_i).  Such a deck
exists by arranging two labels of the deleted (H)-set for (X_i) at
distance at least (H), so that this (H)-set is not a retained
window.

If legal decks were matroid bases, basis exchange would provide
(Y\in D'\setminus D) such that (D-X_i+Y) is legal.  This contradicts
the chronology theorem.  Hence the nonmatroid conclusion is valid.

For any such (Y), the set

\[
                         F=D-X_i+Y
\]

has exactly (d) contained owners.  A legal row whose deck is contained
in (F) would have to use all of (F), again contradicting chronology.
Thus the one-top atom matching is saturated while the literal physical
rank is zero.  The unavoidable leave one is genuine.

Scope check: this local reservoir is not asserted to be forced in every
global table residual.  It is sufficient to refute the inference

\[
 \text{owner Hall}\quad\Longrightarrow\quad
 \text{literal zero-quarantine installation}.
\]

## 7. Final audited boundary

The strongest valid conclusion is:

\[
\boxed{
\begin{array}{c}
\text{owner atoms: polynomial forced banks have zero leave by Hall;}\\
\text{literal paths: zero leave iff the physical rank saturates;}\\
\text{fixed bank without rerouting: exact leave }|Q_T(B)|.
\end{array}}
\]

Accordingly the theorem sharpens the coarse quarantine count and gives
an exact physical installation criterion, but does not conceal the still
open consecutive-window augmentation theorem behind abstract matching
language.
