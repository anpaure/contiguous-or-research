# K17 P2--H two-row rethread classification and the rank-seven C6 gate

**Date:** 2026-08-02  
**Status:** exact target-table theorem on the frozen K17 three-level row
types.  It classifies the two possible two-row transpositions and proves
that neither gives a bank-preserving rank-seven escape.  The positive C6
statement is a sufficient payload/private-bank theorem, not a socket,
supplier, cycle-cover, residence, upper, source, compiler, or word
certificate.

## 1. Frozen objects and notation

Let a fixed old length-two row be

\[
             p:(S,R),\qquad S\subsetneq R,quad |R|=8,
\]

with its physical owner fixed.  Let a currently long eligible H row be

\[
             h:(B,M,U),\qquad B\subsetneq M\subsetneq U,
             \quad |M|=7,quad |U|=8,
\]

again with root and owner fixed.  The authenticated table has `3,899` old
length-two rows and `18,646` eligible H rows.  Every length-three middle is
rank seven.  The old P2-bottom rank census is

```text
rank 4   60
rank 5  703
rank 6 2351
rank 7  785
```

The exact short-bank certificate is the typed triple

\[
                     (S_H,\tau,\mu_B),                 \tag{1.1}
\]

not merely the cardinality `|S_H|=1748`: `tau` fixes one private ticket per
short H row and `mu_B` fixes the real-H-token outer matching required by
those tickets.  Its protected long endpoint shore is

\[
                     E_H=P_H\mathbin{\dot\cup}Q_H.      \tag{1.2}
\]

There are `3,495` dynamic H hosts in this shore and one fixed-soft host.

## 2. Complete classification of one-target two-row transpositions

Keep both roots and both owners fixed, keep row lengths two and three, and
exchange exactly one nonroot named target from each row.  There are exactly
two possibilities.

### Type B: bottom--bottom exchange

\[
 (S,R)+(B,M,U)\longmapsto(B,R)+(S,M,U).                \tag{2.1}
\]

It is a strict target-table rethread if and only if

\[
                         B\subsetneq R,
 \qquad                  S\subsetneq M.                \tag{2.2}
\]

The old containments give the other two chain inequalities.  Equation
(2.1) is a literal transposition of the named targets `S,B`, so it preserves
the target partition, both row lengths, every root, every owner, and the
set of short H rows.

It is **not** a circuit of the authenticated bottom matching `G_bot`.
That graph has only original H bottoms on its left shore and has the P2 rows
fixed outside its receiver shore.  After (2.1), original H token `B` lies
in a P2 row and old P2 label `S` lies in an H row.  Thus the typed outer
certificate `mu_B`, the `M_short` theorem, and the frozen dynamic
`p(token,H)` catalogue do not survive literally.  One can regard (2.1) as
a C4 only in a newly enlarged all-bottom/all-slot matching.  That enlarged
architecture needs a fresh exact outer, state, and supplier audit.

Moreover, if `|S|=7`, then (2.2) is impossible: two distinct rank-seven
sets cannot be in strict containment.  Type B can therefore move only P2
labels of rank at most six.

### Type M: bottom--middle exchange

\[
 (S,R)+(B,M,U)\longmapsto(M,R)+(B,S,U).                \tag{2.3}
\]

It is a strict target-table rethread if and only if

\[
       M\subsetneq R,\qquad B\subsetneq S,
       \qquad S\subsetneq U.                           \tag{2.4}
\]

To stay in the frozen row type, the new length-three middle `S` must have
rank seven.  For lower-rank `S`, (2.3) may be an abstract strict chain but
it leaves the authenticated H/state catalogue: the table parser and long
family theorem require every length-three middle to have rank seven.

For rank-seven `S`, a nontrivial Type-M move is impossible.  Indeed, the
old and new suffixes would be

\[
 S-R,\quad M-U,\quad M-R,\quad S-U,                    \tag{2.5}
\]

a C4 in the Boolean incidence graph between ranks seven and eight.  That
graph has no C4.  If distinct rank-seven sets `S,M` lie below both
rank-eight sets `R,U`, then `S union M` has size eight and must equal both
`R` and `U`; hence `R=U`, contradicting exact use of the root targets.

### Theorem 2.1 (sharp two-row no-go)

Within the frozen K17 row types, no two-row P2--H rethread both

1. moves a rank-seven P2 label out of its current suffix, and
2. preserves the typed H-bottom architecture.

Type B fails by rank, and Type M fails by the C4-free Boolean incidence
lemma.  Consequently the authenticated `226` rank-seven members of the
`230` singleton-P2-root obstruction remain isolated after adding every
Type-B P2--H donor edge.  This is a scoped deficiency lower bound of `226`
for that frozen-middle graph, conditional only on the authenticated
`226+4` rank split.  It is not a no-go for moving-middle circuits.

## 3. Smallest bank-preserving rank-seven escape

Let `X_0,X_1,X_2` be distinct rank-seven targets and `Y_0,Y_1,Y_2`
distinct rank-eight root slots.  Suppose the current suffix assignment is

\[
                         X_i\subset Y_i
                         \quad(i\in\mathbb Z/3),       \tag{3.1}
\]

and the alternate assignment satisfies

\[
                         X_{i+1}\subset Y_i
                         \quad(i\in\mathbb Z/3).       \tag{3.2}
\]

Then the six incidences (3.1)--(3.2) form an alternating C6.  Cycling the
three `X` labels among the three fixed root/owner slots preserves every
rank-seven target and root exactly once and changes no row length.

Every Boolean rank-seven/rank-eight C6 with three distinct roots has the
canonical form

\[
\begin{aligned}
 X_a&=C\cup\{a\},&X_b&=C\cup\{b\},&X_c&=C\cup\{c\},\\
 Y_{ab}&=C\cup\{a,b\},&Y_{bc}&=C\cup\{b,c\},
 &Y_{ca}&=C\cup\{c,a\},                              \tag{3.3}
\end{aligned}
\]

where `|C|=6` and `a,b,c` are distinct outside `C`.  Thus C6 is the
smallest nontrivial same-rank suffix circuit.

Some slots in the C6 may be P2 rows and some may be currently long H rows.
For an H slot `h` with unchanged real bottom `B_h`, require

\[
                 B_h\subsetneq X_{\rm new}(h).         \tag{3.4}
\]

In the canonical hex, an H bottom that survives a flip between two adjacent
rank-seven labels must lie in their intersection `C`.  Hence (3.4) is
equivalently `B_h subseteq C` for every changed H slot of a literal C6.

### Theorem 3.1 (protected C6 suffix rethread)

Assume an alternating C6 (3.1)--(3.2) contains at least one P2 slot and
uses only currently long H slots outside `E_H`.  Assume (3.4) at every H
slot.  Flipping the entire C6 then:

1. preserves the exact named-target partition and the length histogram;
2. preserves every physical root and owner, hence the frozen owner/root
   factor skeleton;
3. keeps every H bottom token on the same H host and keeps the hard-short
   set `S_H` pointwise fixed;
4. leaves every protected ticket and forced endpoint placement in `tau`
   untouched; and
5. leaves the explicit outer matching `mu_B` valid in the updated
   containment graph.

#### Proof

The C6 flip is a permutation of three rank-seven targets among three fixed
root slots, so target use, roots, owners, and row lengths are unchanged.
Condition (3.4) makes each changed H row a strict chain after the flip.
No H bottom moves, so all real-token placements in `mu_B` are the same.
No H row changes hard/short status.  Finally the changed long H hosts avoid
`E_H`, so no occurrence-labelled protected endpoint mode, token, flag, or
port in `tau` changes.  All components of the typed triple (1.1) therefore
remain literal certificates.  \(\square\)

This theorem is stronger, for bank preservation, than a Type-B donor swap:
it moves a rank-seven P2 role while keeping the authenticated real-H-token
matching rather than replacing it with an unproved enlarged matching.

## 4. What supplier and common-phase acceptance still require

Neither row-disjoint two-row swaps nor row-disjoint C6 flips preserve the
supplier perfect matching merely by counting.  Let `D` be the changed H
rows and `P` the changed P2 rows.  In the exact supplier bipartite graph,
only the following edge families can change:

\[
          ((P\cup D)\times H_{\rm long})
          \ \cup\
          (\mathcal A\times D),                       \tag{4.1}
\]

where `A` is the full source-row shore.  Every `d in D` is a demanded hard
head, so the old supplier matching contains an edge into `d`; that edge is
affected and must be replayed.  The old matching remains a certificate if
and only if all of its affected edges remain literal edges.  In general a
fresh maximum matching/Hall audit on the incrementally rebuilt graph is
necessary and sufficient for `16898/16898`.

Likewise, one common-phase socket witness per repaired P2 row is only an
edgewise projection.  Parallel rethreads require a simultaneous typed
selection which additionally enforces:

* predecessor and successor host capacities;
* endpoint bottom-token injectivity (including removal of a donated token
  for Type B);
* one common flag on every reused long host;
* avoidance, or exact reuse, of protected endpoint ports and flags;
* legal regenerated long modes for every changed H suffix;
* residual long--long Hall completion and supplier Hall completion; and
* the final state/reset boundary and connected chronology.

Pairwise row disjointness proves only target-table composability.  It does
not imply these endpoint rows.  In particular, a maximum matching from the
`1,641` union-zero P2 roles to donors would be an exact *parallel payload
rethread* theorem only after each edge is typed by the complete phase-zero
and phase-one ticket data and the shared endpoint rows are imposed.

## 5. Exact finite target and scope boundary

The smallest proof-safe rank-seven search object is therefore not the
two-row donor graph.  It is the directed suffix-assignment graph whose
vertices are movable rank-seven P2 slots and safe currently-long H slots.
The current rank-seven label of slot `i` may enter slot `j` when it is below
the fixed root of `j`, and, for an H slot, its unchanged bottom is below the
incoming label.  Nontrivial directed cycles are literal suffix rethreads;
the first possible cycles have length three and are the C6 modules above.

A finite actuator should enumerate those C6 modules, price every resulting
P2 role in both carrier phases, reject changed H hosts in `E_H`, and then
run the typed endpoint and supplier audits.  A failed C6 census is a no-go
only for this three-slot, fixed-root/owner, protected-bank face.  Longer
suffix cycles, root/owner changes, and enlarged all-bottom matching remain
outside its scope.

The locally frozen bank theorem is phase-zero and bound to
`original.res1972.tsv`.  Its private-ticket conclusion must not be carried
to a distinct `s7` owner phase without an explicit phase-aligned replay.
The C6 payload proof itself is phase-independent because it fixes roots and
owners; common-phase socket and supplier acceptance are not.

## 6. Frozen basis

```text
original.res1972.tsv
  db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185

potential socket-pricer source
  c24b5b76fa7e4b69c942e793e425bc8db0333f8370a61ca8287cebf0079ab27a

fixed-P2 global-union pricer source
  32deceace15b4a1ec51533fcc544f991c65c6d1b6ed0b3e57a0563de0e097966
```

The companion tiny audit independently checks the row/rank censuses and
exhausts the `680,680` lower-cover pairs of all `24,310` rank-eight Boolean
sets, finding no pair under two different roots and hence no C4.
