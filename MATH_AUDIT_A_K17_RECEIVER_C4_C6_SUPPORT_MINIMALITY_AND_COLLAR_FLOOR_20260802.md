# K17 receiver-bank C4/C6 minimality, the common-state support-four floor,
# and the internal five-role no-go

**Date:** 2026-08-02  
**Lane:** A, joint chain-slot escape from the fixed-root rank-seven SCC face  
**Status:** exact target/root/row-length theorem and independently replayed
finite audit.  The receiver circuits below do **not** by themselves certify
common-state sockets, the frozen private outer matching, suppliers,
chronology, residence, upper shadows, source closure, a compiler, or a word.

## 1. Scope correction and the relevant invariant

The fixed-root SCC theorem leaves two logically distinct escapes.

1. An unchanged bad P2 role may acquire a new socket because other roles
   change.  The SCC theorem does not rule this out.
2. A construction which repairs a bad role by moving its own rank-seven
   target must change its receiver incidence when that role is one of the
   162 singleton SCCs.

Write

\[
  \rho(\mathcal T)=
     \sum_{\substack{T\text{ rank }7\\T\text{ immediately below }R}}
       [T,R]
\tag{1.1}
\]

for the occurrence-labelled rank-seven-to-rank-eight receiver matching of a
chain table.  A permutation of complete role packets among physical sites
which keeps every internal pair `T<R` intact fixes `rho` exactly.  Therefore
the formal complete-packet site transposition from the fixed-suffix escape
theorem is still in the kernel of (1.1): by itself it cannot move any of the
162 labels.  The useful actuator must *cross-pair* at least one rank-seven
target with a different rank-eight root.

This distinction is load-bearing.  Moving the physical short site and
changing the receiver matching are not equivalent operations.

## 2. Complete support-two receiver exchange

Consider two exact length-two rows

\[
                (S,R),\qquad (L,Q),                 \tag{2.1}
\]

where `|S|=7` and `|L|<=6`.  The first root is a receiver and the second is
a nonreceiver.  A nonidentity replacement on these two rows which preserves
the two lower targets, the two roots and both row lengths is forced to be

\[
       (S,R)+(L,Q)\longmapsto(L,R)+(S,Q).            \tag{2.2}
\]

### Lemma 2.1 (exact C4 criterion)

The replacement (2.2) is a strict-chain target-table move if and only if

\[
                         L\subsetneq R,qquad S\subsetneq Q. \tag{2.3}
\]

It changes the receiver bank by replacing the receiver root `R` with `Q`.
Conversely, every exact two-row, length-two, target/root-preserving receiver
change has the form (2.2).

#### Proof

With the two roots and row lengths fixed, the two lower targets have only
the identity assignment and the transposition.  The latter produces exactly
(2.2), and its two strict-chain conditions are exactly (2.3).  Since `S` is
rank seven and `L` is not, the receiver status moves from `R` to `Q`.
\(\square\)

### Theorem 2.2 (exact K17 C4 census)

On the frozen round-47 target table, the 162 fixed-root singleton bad roles
and all 4,862 nonreceiver rank-eight roots have exactly

\[
                 304
\]

edges satisfying (2.3).  They cover 150 of the 162 bad roles, with maximum
degree five.  The exact uncovered chain IDs are

```text
23021 23042 23046 23070 23336 23340
23471 23850 23955 23987 24051 24055.
```

Hence these twelve roles require at least three changed chain slots in the
exact target/root/length-two class.  This is a structural statement on the
round-47 table.  In particular it is not evidence that any of the 304 C4s
preserves the separately frozen private outer matching or has a common
literal socket.

### Theorem 2.3 (complete support-two common-state no-go)

Every one of the 304 structural C4s was independently repriced by the exact
relaxed-nine five-cell oracle.  A C4 was retained only if **both** crossed
roles had a literal socket in phase zero and in phase one.  The exact result
is

\[
       304\text{ structural C4s},\qquad
       0\text{ common-phase socket-complete C4s}.      \tag{2.4}
\]

Thus support two is impossible for a receiver-changing packet which must
materialize both new length-two roles in both transported phases.  This
strengthens the structural support-three lower bound from twelve roles to
all 162 roles on the declared C4 face.  It is still only separate socket
existence in both phases; it does not assert one common selected occurrence,
which would be stronger.  In particular, the independently identified seven
private-aligned C4s are a subset of these 304 and all seven fail this socket
row as well; private alignment does not evade (2.4).

## 3. The support-three receiver cycle

For three length-two rows put

\[
  (A_i,R_i),\quad(A_j,R_j),\quad(A_k,R_k).            \tag{3.1}
\]

The directed cycle

\[
 \begin{aligned}
  (A_i,R_i)&\mapsto(A_k,R_i),\\
  (A_j,R_j)&\mapsto(A_i,R_j),\\
  (A_k,R_k)&\mapsto(A_j,R_k)
 \end{aligned}                                       \tag{3.2}
\]

is exact if and only if

\[
      A_k\subsetneq R_i,qquad
      A_i\subsetneq R_j,qquad
      A_j\subsetneq R_k.                             \tag{3.3}
\]

This is the alternating C6 of the lower-target/root matching.  When at
least one of `A_j,A_k` has rank at most six, it changes the receiver bank.

### Theorem 3.1 (support three is sharp for the twelve)

Exhausting every directed three-cycle (3.2) through the twelve C4-uncovered
roles over all 7,395 length-two rows gives 208 cycles.  The counts in the
chain-ID order displayed in Theorem 2.2 are

\[
  (19,19,13,16,16,10,10,15,14,25,28,23).            \tag{3.4}
\]

Every one of the 208 cycles uses **two** nonreceiver roles.  Thus every one
of the twelve has a receiver-bank exchange of support three, while none has
one of support two.  Support three is therefore exact and sharp in this
target/root/row-length-preserving class.

Exactly four of the 208 cycles use only original P2 rows:

```text
(23340,23365,10123)
(23340,23365,10837)
(23955,23980,10375)
(23955,23980,16810).
```

These four are the cleanest next common-state candidates because the frozen
protected H-ticket and H/F outer bank has no original-P2 row occurrence.
That observation proves only structural noninteraction with that H-ticket
bank.  The changed P2 source signatures and supplier incidences still need
literal replay, so this note does not call the four cycles protected-safe.

#### Proof

Equation (3.3) is precisely the strictness test for the three new rows, and
the move merely cycles their lower targets.  It therefore preserves every
named target, every root and every row length exactly.  The finite audit
enumerates all ordered choices of `j,k` satisfying (3.3), requires a
nonreceiver, and independently recovers the support-two uncovered set before
counting (3.4).  It additionally asserts that all 208 selected `j,k` are
nonreceivers and identifies membership in the frozen 3,899-row original-P2
bank.  \(\square\)

### Theorem 3.2 (complete support-three common-state no-go)

The four all-original-P2 cycles were repriced row by row.  None gives three
new roles which all have a socket in both phases:

* for the two cycles anchored at `23340`, new rows 0 and 1 are socket-zero;
* for the two cycles anchored at `23955`, new row 1 is socket-zero.

The other 204 cycles all move the anchor's rank-seven target onto an
original singleton/F root.  After duplicate roles are contracted, they use
exactly 72 distinct `(anchor,F-root)` rank-seven-on-F roles.  The same exact
five-cell oracle gives

\[
       72\text{ distinct rank-seven-on-F roles},\qquad
       0\text{ common-phase socket-positive roles}.   \tag{3.5}
\]

One zero role kills every containing cycle, so all 208 structural
support-three cycles fail common-state completion.  Combining Theorems 2.3
and 3.2 gives the exact scoped lower bound

\[
 \boxed{\text{common-state receiver-changing support}\ \ge 4}  \tag{3.6}
\]

for the twelve fixed-root/C4-uncovered roles, when every changed row remains
an exact length-two row and each new role must have a literal socket in both
transported phases.  No support-four existence is asserted.

A separate fail-closed readback checked all 304 C4 output/error pairs and
all 72 rank-seven-on-F output/error pairs: every output and every error file
is nonempty, every output has the expected materialized-role header, and
every error has the exact semantic no-socket prefix.  Thus no timeout,
resource exit, missing file, or empty output is being counted as a negative
certificate.

## 4. What the five-role target can now mean

For any of the twelve roles, a target-table receiver-changing actuator must
contain at least the three changed chain slots from Theorem 3.1.  The exact
common-state requirement raises that floor to four by Theorem 3.2.  If it is
required to be an **internal two-ended linear collar** with the same exterior
interface in both modes, it must also contain a retained role on each side
to expose and compare the two exterior ports.  Consequently

\[
           4\text{ changed roles}+2\text{ exterior guards}
              \ \ge\ 6\text{ chain roles}.           \tag{4.1}
\]

Hence a five-role internal collar cannot repair these twelve roles inside
the exact length-two/common-state architecture.  The earlier
direct-adjacency argument gave only a five-role floor for an abstract
reciprocal ticket; the receiver-bank and exact-socket audits raise the K17
floor by one.

The qualification **internal two-ended** is essential.  A global boundary
may supply or clip one guard, and a nonstandard source grammar may encode an
exterior port without retaining a chain role.  Equation (4.1) is not a
universal support-five no-go outside the declared collar architecture.

A candidate support-four/six-role collar must still replay, on one common
choice:

1. every changed role's literal source/state signature;
2. the supplier matching;
3. the selected private socket tickets and their complete outer matching;
4. owner, cap, history and guard rows; and
5. identical left and right exterior port signatures.

The support-three face is now closed by Theorem 3.2.  The next exact finite
object is a support-four chain-slot packet, or a source grammar which leaves
the declared length-two socket face.

## 5. Frozen audit bindings

Independent O3 replay root:

```text
/home/amodo/or15/work/a_k17_joint_chain_slot_receiver_c4_20260802
```

Local immutable copies:

```text
scratch/audit_a_k17_rank7_receiver_c4_20260802.cpp
  278bcac3a8ef14fb6189dabcee62b330d72fe3a3b3c618d2334d9f8ce1cfe4b9
scratch/a_k17_joint_chain_slot_receiver_c4_20260802/receiver_c4_edges.tsv
  5695c52b3c4b032d1772c8bbacaa7543ec8dd476927fc086d645368229832a06
scratch/a_k17_joint_chain_slot_receiver_c4_20260802/receiver_c4.audit.json
  9838f68468012d0657d21ad76a459f941a68d123be5965ddfdc539ce6a20d6df
scratch/a_k17_receiver_bank_c4_20260802/
  audit_a_k17_receiver_bank_c4_common_phase_socket_20260802.cpp
  d544c74f5f3bd89c744920f47c89590c9a46fd95ffc46b5029b96b4d95e92ca5
scratch/a_k17_receiver_bank_c4_20260802/socket_catalogue.audit.json
  1f3aee9947fa6cb51fc67da2338dd7ddd5f0b92483cc17eec583f046799352dd

scratch/audit_a_k17_rank7_receiver_c6_20260802.cpp
  9babf8dec24cbbd870fcc26c0fd4d44780131f3b5e758b4eb5266fe322955ad8
scratch/a_k17_joint_chain_slot_receiver_c4_20260802/receiver_c6_cycles.tsv
  32bfe2225282791cd050a2ed424b50576c61c3f927cc27cf327034d7aa07f1ce
scratch/a_k17_joint_chain_slot_receiver_c4_20260802/receiver_c6.audit.json
  51f8c537c88da4cd55bd7cb88ac207019f77c89c168ca8a39da460e3dc7f4ade
scratch/a_k17_receiver_bank_c4_20260802/
  audit_a_k17_receiver_bank_c6_common_phase_socket_20260802.cpp
  18c717f05976e82c6333408818cc5f6010dcca94eb55cb92c5179647d45c0af3
scratch/a_k17_receiver_bank_c4_20260802/
  receiver_c6_23340_23365_10123.socket.txt
  61d0b22ec44b10f28d5f45b217e26e4ed43ad00299c36818a08b2baad7be3ce3
scratch/a_k17_receiver_bank_c4_20260802/
  receiver_c6_23340_23365_10837.socket.txt
  a410615e8e6b85b61a73003e0fd7fc5dc2493765abc669bcc1cec6a2026fc781
scratch/a_k17_receiver_bank_c4_20260802/
  receiver_c6_23955_23980_10375.socket.txt
  f92bbd832ed2b615603b372d681bf33e742295071543b162c326f2b8a28578d6
scratch/a_k17_receiver_bank_c4_20260802/
  receiver_c6_23955_23980_16810.socket.txt
  186953622244ebfe7965e98327b9e9cf1215faea9340ac89a33dfb9a98eab0d5
scratch/a_k17_receiver_bank_c4_20260802/
  audit_a_k17_rank7_on_f_common_phase_socket_20260802.cpp
  cb33262df430c3f622aeb5356ad862745546e62741e6423936d5f0317c3e1f66
scratch/a_k17_receiver_bank_c4_20260802/rank7_on_f_socket.audit.json
  fe50282c80ad372f234bf09660792073f5ae80f50161e00291c60696405e734a
```

The C4 source consumes the full 19,448-row
`fixed_root_scc.tsv`; the assertion `size=19448` is therefore intentional.
The separate 623-row roles table used by another implementation is not an
input to this replay.

The common phase target skeleton is frozen by

```text
round047.s7.phase0.tsv
  ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207
```

Its target chains agree with phase one, but it is not the private
outer-matching materialization.  No private-preservation conclusion is
drawn from these counts.
