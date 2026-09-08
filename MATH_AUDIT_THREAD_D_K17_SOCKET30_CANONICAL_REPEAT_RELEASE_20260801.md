# The k=17 socket30 canonical repeat release and its residual three-row endpoint obstruction

Date: 2026-08-01  
Status: exact solver-free audit; no Hamilton path or compiler claim

## 1. Scope

The input is the authenticated `6252`-piece v5 postbank in
`scratch/k17_socket30_postbank_pieces_20260801.json`.  This note asks for the
smallest release forced by its internal lower-q1 repetitions while retaining
as many of the thirty compact sockets as possible.  It then recomputes the
complete **internal** upper deck at ranks ten through fifteen and tests the
seven raw rank-ten endpoint-zero rows of the unrefined postbank.

No remaining-seam selector, Hamilton path, common cap, or generalized lower
compiler is asserted.

## 2. A general repeat-release identity

Let `N` owners be partitioned into `P` simple Johnson paths.  Their interiors
contain `N-P` edges.  If those edges use `D` distinct lower intersection
colours, put

\[
                       \delta=(N-P)-D.                 \tag{2.1}
\]

An intact-piece Hamilton path adds only `P-1` seams, so it has at most

\[
                       D+P-1=N-1-\delta                \tag{2.2}
\]

distinct lower colours.  Splitting an occurrence of a currently unique
colour decreases both `N-P` and `D` by one and leaves `delta` unchanged.
Splitting one occurrence of a repeated colour while another occurrence
survives decreases `delta` by one.  Therefore a colour-simple owner path
requires at least `delta` duplicate-occurrence releases.  When every repeat
has multiplicity two, one release from every repeated colour is also the
unique cardinality-minimal way to make the surviving internal colours
simple.

This is an owner-path statement.  A nonflat compiler could instead pay
additional lower targets with special cells.

## 3. Exact v5 lower ledger

The `6252` pieces contain

\[
  18058\text{ internal edges},\qquad
  18005\text{ distinct lower colours},\qquad
  \delta=53.                                           \tag{3.1}
\]

All `53` repeated colours have multiplicity two.  Their physical occurrence
types are

\[
       52\ (\text{residual},\text{socket}),\qquad
        1\ (\text{socket},\text{socket}).              \tag{3.2}
\]

The sole socket--socket colour is `31968`, occurring at

* socket target `31988`, edge `31984 -> 31972`; and
* socket target `97508`, edge `31969 -> 97504`.

Thus a release which always chooses the residual occurrence when available
has only two branches.  It cuts the `52` forced residual occurrences and one
of the two displayed socket occurrences.  Each branch has

\[
  6305\text{ pieces},\quad18005\text{ internal edges},\quad
  18005\text{ distinct internal lower colours}.        \tag{3.3}
\]

There are exactly `6305` missing lower colours and `6304` seams in a
Hamilton path of these pieces.  Hence lower-q1 completion is now tight: the
seams must use every missing colour except the single boundary colour,
without repetition.

The earlier position-row and the newer JSON piece artifacts give exactly the
same multiset of `6252` owner paths.

## 4. Exact upper-deck cost and branch dominance

The internal upper-hole counts after the two releases are:

| split socket occurrence | rank 10 | rank 11 | rank 12 | rank 13 | rank 14 | rank 15 |
|---|---:|---:|---:|---:|---:|---:|
| `31988` | 1509 | 2480 | 1612 | 564 | 104 | 11 |
| `97508` | 1509 | 2480 | 1612 | 563 | 104 | 11 |

The hole sets agree exactly at ranks `10,11,12,14,15`.  At rank thirteen,
cutting the `97508` occurrence additionally preserves the target `97527`
and loses nothing in return.  Thus the `97508` branch weakly dominates the
`31988` branch in the internal upper deck.

Relative to the unsplit postbank, the preferred branch creates respectively

\[
                         51,51,29,14,3,1               \tag{4.1}
\]

additional holes at ranks ten through fifteen.  These are exact joint
cut casualties, not a sum of independently charged edge debts.

## 5. Four old endpoint zeros open, three persist

The unrefined postbank has seven rank-ten targets with no raw seam:

\[
  20427,69555,70910,72414,72566,73649,83946.           \tag{5.1}
\]

In either canonical release branch, the exact raw directed provider counts
on the new endpoint states are

\[
\begin{array}{c|rrrrrrr}
U&20427&69555&70910&72414&72566&73649&83946\\ \hline
\#&2&0&2&0&2&2&0.
\end{array}                                             \tag{5.2}
\]

Each count two consists of the two orientations of one undirected seam; it
is not two resource-disjoint providers.  The persistent raw-zero bank is

\[
                         69555,72414,83946.              \tag{5.3}
\]

By the rank-ten seam reduction, no ordering or orientation of the canonical
`6305` released pieces can cover these three targets.  Their pairwise
intersections have ranks `6,7,6`, so no newly exposed rank-nine endpoint can
be a facet of two of them.  At least three new endpoint services, and hence
at least two further ordinary cuts, are necessary.  This bound does not
assert that two cuts suffice after residence, lower-colour, upper-ray, and
common-cap constraints are imposed.

Consequently the canonical 53-release is the exact lower-repeat reset but is
not yet the domain of a full upper-exact Hamilton selector.  The weakest
next relaxation is a further endpoint release/rethread whose exposed facets
hit all three rows in (5.3), followed by the joint lower-colour path and
rank-10--15 accumulated-union selector.

## 6. Artifacts

* `scratch/audit_threadD_k17_socket30_canonical_repeat_release_20260801.py`,
  SHA-256 `4435d74db8d1d22e759896ffa45ceb48b95b57e833833392c62fb12cf6ce94cc`;
* `scratch/threadD_k17_socket30_canonical_repeat_release_20260801.audit.json`,
  SHA-256 `29d829e670c101e1055c32d6e7429dec5ce43bba283c6ddd7fcddaad65a392cf`,
  status `PASS_EXACT_K17_SOCKET30_CANONICAL_53_REPEAT_RELEASE`.

The JSON retains all `53` selected cut occurrences in each branch, exact
rank-hole hashes, and the literal menus for the seven rows in (5.1).
