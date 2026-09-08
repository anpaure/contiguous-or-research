# Thread A: native C1 forward upper-return obstruction (2026-07-30)

## 1. Frozen source and conclusion

Let `C1` denote

    scratch/k16_state2_hostseam_5opt_survivors_20260730/candidate_1.targets

with SHA-256

    1e75cfb4c8e610a4ea2bf1095e44d3236f655aabc3efe65e8532912b7c0572a8.

Apply the all-forward three-cut transposition with cuts

\[
 (4025,5315,12825).
\]

Call the resulting chronology \(Q\).  Exact reconstruction gives

\[
 h_Q-h_{C1}=e_{0x1879}-e_{0x9859}.                 \tag{1.1}
\]

Thus \(Q\) has no static lower hole, has the same three G0 flats
\((2031,12869,12871)\), and has exactly one upper hole,

\[
 U=0x6f79.                                          \tag{1.2}
\]

The unique old witness of \(U\) was

\[
 (0x6b61,0x6a71,0x6879,0x4679)                    \tag{1.3}
\]

on `[12823,12827)`.  In \(Q\), its first three rows occur at
`11533,11534,11535`, while the fourth occurs at `12826`.

The result below closes the smallest broad native forward-return face.
It uses no phase-labelled seam catalogue.

## 2. Exact seam equations

In a constant depth-two region, splice a left segment ending

\[
 L_{-3},L_{-2},L_{-1},L_0
\]

to a right segment beginning

\[
 R_0,R_1,R_2,R_3.
\]

Put

\[
 E_i=V_i\cap V_{i+1}\cap V_{i+2}\qquad(0\le i\le5),       \tag{2.1}
\]

where

\[
 (V_0,\ldots,V_7)=
 (L_{-3},L_{-2},L_{-1},L_0,R_0,R_1,R_2,R_3).
\]

### Lemma 2.1 (native depth-two splice test)

Assume the two input interiors are already G0-exact and \(L_0\ne R_0\).
The splice is G0-exact if and only if \(E_2,E_3\ne0\) and

\[
 \begin{aligned}
 E_0\cup E_1\cup E_2&=L_{-1},\\
 E_1\cup E_2\cup E_3&=L_0,\\
 E_2\cup E_3\cup E_4&=R_0,\\
 E_3\cup E_4\cup E_5&=R_1.
 \end{aligned}                                      \tag{2.2}
\]

#### Proof

At depth two, the maximal envelope at a position is the intersection of
the three target rows ending there.  Replacing a seam changes exactly the
first two envelope entries on the right.  Hence only the four rows in
(2.2) can change replay.  Their three-envelope unions are exactly the four
left sides displayed in (2.2).  Nonemptiness of the two changed envelope
entries is necessary and sufficient for G0.  The inequality
\(L_0\ne R_0\) prevents an unaccounted new flat.  This proves the claim.
\(\square\)

### Lemma 2.2 (rank-seven seam locality)

For a depth-two splice, the complete occurrence-labelled rank-seven family
change is supported on cell starts at distance at most three from the
seam.

#### Proof

Only the first two envelope entries on the right change.  A static cell has
length one or two, so its joined envelope can change only within one start
of those entries.  A row contributing a mandatory bit has a three-position
window.  Combining a two-position cell with a three-position row window
enlarges the affected start interval by at most two more positions.  Thus
all joined and mandatory changes lie in the seven starts centered at the
seam.  \(\square\)

Consequently, if every transported block has length at least 12, the three
old and three new collars are disjoint.  Their signed family counters add
exactly; this includes all mandatory-bit effects and is stronger than an
adjacent-intersection ledger.

## 3. Forward direct-return theorem

For cuts \(2040\le a<b<c\le12860\), define

\[
 \Phi_{a,b,c}(Q)=
 Q[0,a]\,Q[b+1,c]\,Q[a+1,b]\,Q[c+1,n-1],            \tag{3.1}
\]

with both transported blocks in forward orientation.  Require

\[
 b-a\ge12,\qquad c-b\ge12.                           \tag{3.2}
\]

Call the move *directly \(U\)-serving* if one of its three new seams has
endpoint union \(U=0x6f79\).

### Theorem 3.1 (no support-preserving direct forward return)

Among all moves (3.1)--(3.2) which are G0-exact and directly
\(U\)-serving:

1. none has zero full rank-seven host-vector change;
2. more strongly, every move creates at least one new rank-seven
   zero-host target.

Hence no move in this face can repay the upper debt while preserving the
lower support, and in particular none is an upper-complete, `h`-neutral
return atom.

#### Proof

A rank-eight endpoint contained in \(U\) occurs at 104 eligible positions
in the stated interior.  There are exactly 3,604 directed endpoint pairs
whose union is \(U\).  Applying Lemma 2.1 directly to their physical rows
leaves 425 legal service arcs.

The service arc can occupy any of the three new seam slots

\[
 (a,b+1),\qquad(c,a+1),\qquad(b,c+1).                \tag{3.3}
\]

For each slot, intersecting the two remaining exact seam-compatibility
lists, then imposing (3.2), gives exactly 12,011 distinct cut triples.
This construction is exhaustive: a directly serving move has a service
arc in one of (3.3), and its other two seams must pass Lemma 2.1.

For every triple, sum the three new seven-start family collars and subtract
the three old collars.  Lemma 2.2 and (3.2) make this the exact full
rank-seven occurrence-family delta.  The exact census has:

\[
 \begin{array}{c|r}
 \text{new rank-seven zeros}&\text{number of triples}\\ \hline
 1&140\\
 2&2975\\
 3&8896.
 \end{array}                                         \tag{3.4}
\]

Thus all 12,011 triples create a lower blocker, and none has zero host
delta.  Thirty-two evenly spaced triples were also reconstructed as full
words; in every case the global family vector agreed exactly with the
collar sum.  The complete triple and delta hashes below make the finite
enumeration reproducible.  \(\square\)

The minimum possible \(\ell^1\)-change is one.  It occurs for 22 triples,
and in every case the sole loss is an originally unique rank-seven host.
Thus the obstruction is sharp: the best forward direct return moves the
blocker rather than closing it.

## 4. Authentication and scope

Reproducer:

    scratch/audit_a_k16_c1_native_forward_upper_return_20260730.py
      SHA 5aed284a0602daf6ae30dff9a4e8c249cef0544fce196744eceff1809e952a73

Audit:

    scratch/a_k16_c1_native_forward_upper_return_20260730.audit.json
      SHA 5fd07f0bee0ff6a124314ece47ca8398c22bc485073a942d2e2e67b13e1366c9
      payload SHA
      106b9bb79af82cbee5b2f0474933699817e4fc4573e0d2debe9fc97cb34a8aa5

Internal enumeration hashes:

    triple SHA
      1ab8661129c40c51b65a9b5bea8b414576e25bbac467ee94cc112f5194b78b53
    delta-key SHA
      28edc6cdb25fb8961f76079b3a856bfda41435fe20076c9141b274fa23eb70d6

The audit reads no phase-labelled seam file; the `argc==6`/`argc==7`
wrapper issue is therefore quarantined from every count above.

The theorem does **not** exclude:

* an indirect \(0x6f79\) witness of length at least three whose adjacent
  endpoint union is smaller than \(U\);
* a reversed block;
* interacting transported blocks of length below 12;
* a cut in a phase-boundary collar;
* a four-cut or higher commutator.

The smallest surviving constructive class is therefore an indirect-witness
or four-seam return, not another separated forward direct-service atom.
