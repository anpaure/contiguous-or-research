# K16 five-opt surplus transfer and upper-return obstruction

## 1. Scope and frozen inputs

This note concerns only the two authenticated state-2, five-opt target
chronologies

\[
 C_0:\quad
 \texttt{762a6361c571f4e182aa03340399d3a1c07f25755c689362da173f04bd1cc407},
\]

\[
 C_1:\quad
 \texttt{1e75cfb4c8e610a4ea2bf1095e44d3236f655aabc3efe65e8532912b7c0572a8}.
\]

They are respectively the files

```
scratch/k16_state2_hostseam_5opt_survivors_20260730/candidate_0.targets
scratch/k16_state2_hostseam_5opt_survivors_20260730/candidate_1.targets
```

Both have exact middle ownership, the required three-flat `G0` profile,
nonzero maximal envelope, exact target replay, sufficient scalar compiler
capacity, and complete upper support.  Their exact static rank-seven host
vectors have the unique holes

\[
 z_0=\texttt{0x1639},\qquad z_1=\texttt{0x1879}.
\]

The donor sets considered here are exactly

\[
 D_0=\{\texttt{0x9439}\},\qquad
 D_1=\{\texttt{0x8879},\texttt{0x9869},\texttt{0x9859}\}.
\]

This is a theorem about an occurrence-labelled segment-atom class.  It is
not a no-go for arbitrary target permutations or arbitrary value edits.

## 2. Seam signatures

Let `Q=(Q_0,...,Q_{N-1})` be a middle-target chronology.  If a segment
operation deletes the adjacent seams `E^-` and introduces the seams `E^+`,
define its adjacent rank-seven signature by

\[
 \sigma_7
 =\sum_{(i,j)\in E^+\atop |Q_i\cap Q_j|=7}
       e_{Q_i\cap Q_j}
  -\sum_{(i,i+1)\in E^-\atop |Q_i\cap Q_{i+1}|=7}
       e_{Q_i\cap Q_{i+1}}.                 \tag{2.1}
\]

Here a standard two-opt reverses one interval.  A standard genuine
three-opt cuts after `a<b<c` and uses one of the five nontrivial segment
patterns numbered 3--7 in the audit artifact.  Pattern 4 is

\[
 A\mid B\mid C\mid D\longmapsto A\mid C\mid B\mid D.       \tag{2.2}
\]

### Lemma 2.1 (exact seam ledger)

For every such segment operation, (2.1) is the exact change of the
adjacent rank-seven colour multiset.

#### Proof

Every adjacency internal to a retained segment survives, possibly with its
orientation reversed.  Intersection is symmetric, so its colour is
unchanged.  The only deleted adjacencies are the cut seams and the only new
adjacencies are the joining seams.  Summing their rank-seven colours gives
(2.1).  \(\square\)

The full static compiler host vector `h` is not, in complete generality,
identical to the adjacent colour vector: exceptional length-two and
length-three cells contribute a correction.  Consequently, every positive
host-vector claim below was replayed from the complete cell catalogue.  A
negative result stated only for `sigma_7` is explicitly labelled as such.

## 3. Exact donor occurrences

The relevant donor cells are all singleton rank-seven families.

For `C0`, `0x9439` occurs at

\[
 [2167,2169),\qquad [3929,3931).
\]

Their envelope pairs are respectively

\[
 (\texttt{0x9039},\texttt{0x9419}),\qquad
 (\texttt{0x9431},\texttt{0x9419}).
\]

For `C1`, the seven donor occurrences are

\[
\begin{array}{c|c}
\text{donor}&\text{cells}\\ \hline
\texttt{0x8879}&[2035,2037),[3751,3753)\\
\texttt{0x9869}&[3689,3691),[9502,9504)\\
\texttt{0x9859}&[4026,4028),[6775,6777),[7720,7722).
\end{array}                                                   \tag{3.1}
\]

Thus deleting one listed occurrence of a donor of multiplicity at least two
does not itself create a static hole.

## 4. Complete standard two/three-cut pure-signature census

### Theorem 4.1 (small pure atom obstruction)

Fix `Ci`, a hole `zi`, and a donor `d` from the corresponding set above.
Among all standard two-opt and genuine three-opt atoms satisfying

\[
 \sigma_7=e_{z_i}-e_d,                                      \tag{4.1}
\]

there is no atom that simultaneously has the exact `G0` profile, exact
maximal-envelope replay, sufficient capacity, and complete upper support.

More precisely:

1. For `C0`, there are 2 two-opt and 3,386 three-opt representations.
   The former both fail carrier replay.  Of the latter, 3,377 fail carrier
   replay, 7 fail `G0`, and 2 representations have exact carrier replay but
   one upper hole.  The two surviving representations are the same physical
   chronology.

2. For `C1`, there are 2 two-opt and 3,407 three-opt representations over
   all three donors.  The two-opt atoms fail carrier replay.  Among the
   three-opt atoms, 3,397 fail carrier replay, 9 fail `G0`, and exactly one
   has exact carrier replay but one upper hole.

#### Proof

Any atom satisfying (4.1) deletes an old occurrence of `d` and introduces a
new seam coloured `zi`.  The audit therefore fixes, successively, a donor
cut, a joining-seam slot, and an ordered pair of endpoints whose
intersection is `zi`.  In a two-opt this determines both cuts.  In a
three-opt it determines at least two of `a,b,c`, leaving at most one cut to
range over `0,...,N-2`.  This generates every representation satisfying
(4.1), without an unrestricted quadratic or cubic scan.

Each generated chronology is then rebuilt literally.  The verifier derives
its flats and depths, computes its maximal envelope, checks every replay
row, checks scalar capacity, and computes all upper masks by contiguous-OR
replay.  The counts above are the resulting exhaustive partition.  \(\square\)

### Remark 4.2 (exact scope)

Theorem 4.1 is complete for the adjacent-signature equation (4.1).  It does
not exclude a standard atom whose exceptional-cell correction changes and
whose full static host-vector change is nevertheless `e_zi-e_d`.  No such
atom is asserted to exist; it is simply outside the proved negative scope.

## 5. The two pure-signature service halves

The surviving physical chronology for `C0` is pattern 4 at cuts

\[
 (1057,1058,2166).                                           \tag{5.1}
\]

It moves the singleton row `Q_1058=0x1e39` across the block
`Q_1059,...,Q_2166`.  Its old and new seams are

\[
\begin{array}{c|c|c}
\text{old seam}&\cap&\cup\\ \hline
(1057,1058)&\texttt{0x1c39}&\texttt{0x1e3b}\\
(1058,1059)&\texttt{0x0639}&-\\
(2166,2167)&\texttt{0x9439}&\texttt{0x9e39}
\end{array}
\]

and

\[
\begin{array}{c|c|c}
\text{new seam}&\cap&\cup\\ \hline
(1057,1059)&\texttt{0x0439}&-\\
(2166,1058)&\texttt{0x1c39}&\texttt{0x9e39}\\
(1058,2167)&\texttt{0x1639}&\texttt{0x9e39}.
\end{array}                                                   \tag{5.2}
\]

The complete static-cell replay, not merely (2.1), gives

\[
 h'-h=e_{\texttt{0x1639}}-e_{\texttt{0x9439}}.              \tag{5.3}
\]

Every other rank-seven multiplicity is unchanged.  The chronology is
`G0`-exact, has capacity 26,844, and has no lower hole.  Its sole defect is
the lost upper target

\[
 U_0=\texttt{0x1e3b},                                       \tag{5.4}
\]

whose source had the unique provider `[1057,1059)`.

The analogous `C1` service is pattern 4 at

\[
 (4025,5315,12825).                                          \tag{5.5}
\]

The decisive donor/hole seam replacement is

\[
 (4025,4026):\texttt{0x9859}
 \quad\longmapsto\quad
 (4025,5316):\texttt{0x1879}.                                \tag{5.6}
\]

Full static replay gives exactly

\[
 h'-h=e_{\texttt{0x1879}}-e_{\texttt{0x9859}}.              \tag{5.7}
\]

It is `G0`-exact, has capacity 27,774, and is lower-zero-free.  Its sole
upper defect is

\[
 U_1=\texttt{0x6f79}.                                       \tag{5.8}
\]

The unique source provider was

\[
 [12823,12827)
 =(\texttt{0x6b61},\texttt{0x6a71},
   \texttt{0x6879},\texttt{0x4679}),                         \tag{5.9}
\]

and the cut after 12825 separates its last row from the first three.

Thus the pure transfer itself is physically real: in each carrier it fails
only because the unique pure insertion position spends one named upper
witness.

## 6. Upper-safe signed service shuttles

### 6.1 The `C0` shuttle

There is an exact upper-complete pattern-4 shuttle at cuts

\[
 (942,1058,2166).                                             \tag{6.1}
\]

It has flats `(986,12869,12871)`, capacity 26,729, exact maximal-envelope
replay and complete upper support.  Its complete all-ranks lower audit has
the sole hole `0x54b1`, and its exact full static family and degree changes
are

\[
 \Delta h=e_{\texttt{0x1639}}-e_{\texttt{0x9439}}
          -e_{\texttt{0x54b1}}.                              \tag{6.2}
\]

Its canonical word SHA-256 is

```
d2d621adfce3e5b3f980957b10f24285435ec1ca2db99dac69ac0db718b6d408
```

The seam ledger is

\[
\begin{array}{c|c|c}
\text{old seam}&\cap&\cup\\ \hline
(942,943)&\texttt{0x54b1}&\texttt{0x54bb}\\
(1058,1059)&\texttt{0x0639}&-\\
(2166,2167)&\texttt{0x9439}&\texttt{0x9e39}
\end{array}
\qquad
\begin{array}{c|c|c}
\text{new seam}&\cap&\cup\\ \hline
(942,1059)&\texttt{0x4431}&-\\
(2166,943)&\texttt{0x1439}&-\\
(1058,2167)&\texttt{0x1639}&\texttt{0x9e39}.
\end{array}                                                   \tag{6.3}
\]

The lost target has one occurrence-labelled source family: the length-three
cell `[943,946)` with envelopes

\[
 (\texttt{0x10b1},\texttt{0x14a1},\texttt{0x44a1}),
\]

joined mask `0x54b1` and mandatory mask `0x5411`.  Thus the residual demand
is literally `+e_0x54b1` at a named destroyed family.

This shuttle is unique in the following coded face: forward
`A|B|C|D -> A|C|B|D`, exterior blocks of length at least 21, interior
blocks of length at least 20, old cuts at distance at least 13 from a flat,
new seams at distance at least 14 from a moved flat, a cut in one of the
two authenticated donor collars, and a designated base-atlas `+/+` hole
seam independently revalidated on `C0`.  The census has 72,505 raw collar
descriptions, 61,775 phase-compatible descriptions, 372 exact local seam
triples, and 17 upper-complete exact carriers.  Exactly one of the 17 has
the one-extra-debt form (6.2).  This does not cover reversals, non-atlas
seams, short interacting collars, or four-cut atoms.

The smallest direct return is already closed in the adjacent-cofacet
two-opt class.  The nine `0x54b1` cofacets give 72 candidate two-opts:
66 fail the carrier and 4 retain an upper hole.  The two upper-complete
states do not close the lower ledger.  One moves the sole defect by

\[
 e_{54b1}-e_{64b1},                                        \tag{6.4}
\]

and the other replaces it by the pair `0x5471,0x54a9` while adding
`0x5469`.  Repeating the same complete 72-candidate audit at the one-hole
`0x64b1` state yields only the reverse one-hole move plus two states with two
holes.  Hence the one-hole-preserving adjacent-cofacet two-opt component
reachable from the shuttle is exactly

\[
 \texttt{0x54b1}\ \longleftrightarrow\ \texttt{0x64b1},     \tag{6.5}
\]

with no zero-hole sink.  An exact return therefore needs a three-or-more-cut
atom or an exceptional non-adjacent-cell host; neither is excluded here.

### 6.2 The `C1` shuttles

Keeping the fixed donor/hole endpoints `4025` and `5315`, move the block
`[4026,5316)` by a forward pattern-4 relocation.  Four exact upper-complete
carrier states have one additional singleton lower debt:

\[
\begin{array}{c|c|c}
\text{third cut}&\text{full static host-vector change}&
  \text{new sole rank-seven hole}\\ \hline
5985&e_{1879}-e_{9859}-e_{0d35}&\texttt{0x0d35}\\
6217&e_{1879}-e_{9859}-e_{4b38}&\texttt{0x4b38}\\
10242&e_{1879}-e_{9859}-e_{3871}&\texttt{0x3871}\\
11277&e_{1879}-e_{9859}-e_{0579}&\texttt{0x0579}.
\end{array}                                                   \tag{6.6}
\]

All four preserve `G0`, exact carrier replay, capacity 27,774, and every
upper target; an exact all-ranks lower replay proves that the displayed `x`
is the sole lower hole.  Their word hashes are respectively

```
d849dad57227a874631403c470a60e693c618a7e9435a376877d77aaea87d408
49a8ff60da7958b89da39940ed80afcfbbb7195428528b0d83a93a407e309d3d
5fc8f0cd1cb6bf5626012b544508dbd151804455d474bf61653373444a1f025c
7d5d80977d4af78088724d0b2ad5de73b520473453a4af6a907f5bd27aaee133
```

These are not solutions of the requested transfer equation: the third
negative term in every row of (6.6) is genuine and its source multiplicity
is one.  They are, however, exact service states for a meet-in-the-middle
construction.  The remaining return demand is now a named singleton
insertion `+e_x`, not an unspecified Hall defect.

The exact C1 census is scoped to the same block bounds and asymmetric flat
clearances as in Section 6.1, a donor causal collar, and one designated
`+/+` hole seam imported from the frozen full base-context atlas and then
independently revalidated on `C1`.  It has 79 revalidated hole seams
(61 at depth two and 18 at depth three), 79,677 phase-compatible
descriptions, and 448 exact carriers.  Exactly five are upper-complete; all
five were full-profiled through every lower rank, and none is a pure
`e_1879-e_d` transfer.  All moved-first-flat cases were also full-profiled,
so the pure transfer (5.7) is unique within this coded face.  Non-atlas or
phase-created internal hosts, reversals, short interacting seams and four-cut
atoms remain open.

## 7. Exact upper-return obstructions

### 7.1 The `C0` service

Let `S0` denote the service chronology (5.1), whose canonical decimal
encoding has SHA-256

```
ea1a7efdf75436fa6452bb53216ef92d59e49ac87b64fc65ce5f3c8560406084
```

Its nine rank-eight facets of `U0=0x1e3b` occur at positions

\[
 934,1057,2166,4630,4857,9776,10966,11594,12421.            \tag{7.1}
\]

They are all distinct.  Since `S0` has no `U0` provider, every restored
`U0` interval must cross a new seam joining two distinct facets of `U0`.

### Theorem 7.1 (short adjacent-neutral return no-go)

There is no standard two-opt or genuine three-opt return on `S0` which

1. restores `U0`,
2. has zero adjacent rank-seven signature, and
3. is an exact `G0` carrier with complete upper support.

The exact census contains no two-opt candidate and 136 three-opt
candidates.  Of the latter, 20 fail `G0` and 116 fail exact carrier replay.

#### Proof

There are 72 directed seams between distinct facets in (7.1).  Impose one
of them in each joining-seam slot of each standard pattern.  For a two-opt
this fixes both cuts.  For a three-opt it leaves at most one cut free.  Keep
exactly the atoms whose seam ledger (2.1) is zero, and replay every retained
chronology.  The exhaustive counts are those stated.  \(\square\)

The closest carrier failure is pattern 4 at cuts `(276,1057,10965)`: it has
only one replay failure, missing bit `0x2` at row 276, but its capacity is
26,063, below the required 26,332.

There is also no unrestricted two-opt return, even if its adjacent
rank-seven signature is nonzero.  Exhausting all 72 two-opt joins that can
create a new `U0` facet seam leaves 70 carrier failures and two exact
carriers; the two exact carriers remain upper-incomplete.  Therefore any
standard segment return completing the fixed service half needs at least
three additional cuts, and an adjacent-neutral standard return needs at
least four.

The last sentence is deliberately scoped to the fixed service chronology.
It does not exclude a different direct four-cut service atom.

There is nevertheless a literal closest return.  Applying pattern 4 at cuts

```
(942,1057,2165)
```

to `S0` restores `0x1e3b`, preserves `G0` and every upper target, and gives
exactly the shuttle of Section 6.1.  Its complete static change relative to
`S0` is

\[
 \Delta h=-e_{\texttt{0x54b1}}.                              \tag{7.2}
\]

Thus the upper debt can be repaid by one native three-cut atom, but the
known smallest repayment exports exactly one occurrence-labelled lower
token.  A deterministic all-pattern full-static three-cut generator has
been written for the remaining question.  Its interrupted capped run
emitted 21 independently authenticated upper-complete rows, none neutral;
because it had no completion footer, those rows give positive examples only
and no absence or total-count theorem.

### 7.2 The `C1` service

The C1 pure service has the unique upper debt `U1=0x6f79`.  A broad native
forward return face can be closed without any phase-labelled catalogue.
Take pattern-4 cuts

\[
 2040\le a<b<c\le12860,
 \qquad b-a\ge12,\quad c-b\ge12,                       \tag{7.3}
\]

with both blocks forward, and require one new seam whose endpoint union is
`0x6f79`.  In this constant-depth-two interior, the exact splice equations
use the eight physical boundary rows.  They reduce 3,604 directed service
arcs to 425 legal arcs and then to 12,011 distinct legal three-seam cycles.

For depth two, a seam changes only the first two envelopes on its right.
Since lower cells have length at most two and mandatory bits have
three-position carrier windows, every rank-seven family change lies in the
seven cell starts centered at that seam.  The block bounds (7.3) make the
three old collars and the three new collars separately disjoint, so their
signed occurrence-family counters give the exact full rank-seven change.
The resulting new-zero histogram is

\[
\begin{array}{c|r}
\text{new rank-seven zeros}&\text{cycles}\\ \hline
1&140\\
2&2975\\
3&8896.
\end{array}                                                   \tag{7.4}
\]

Thus this face has zero support-safe cycles and zero `h`-neutral cycles,
even before asking whether other upper witnesses survive.  The minimum
`L1` change is one, attained by 22 cycles; each deletes one unique lower
host.  Hence no separated forward direct-witness atom in (7.3) repays the
upper debt without reopening a lower blocker.

This theorem does not cover an indirect `0x6f79` witness of length at least
three, a reversal, a block shorter than 12, a phase-boundary cut, or four or
more cuts.

## 8. Exact MITM boundary

For a segment atom `A`, the proof-safe meet-in-the-middle key must retain

\[
 \mathcal K(A)=
 (\Delta h_A,\Delta u_A,\text{flat/phase boundary state},
  \text{capacity},\text{changed occurrence labels}).         \tag{8.1}
\]

Using only `sigma_7` is unsound unless invariance of the exceptional-cell
correction has separately been proved.  For the two service halves that
correction was checked directly and is unchanged; no universal correction
invariance theorem is claimed.

The smallest currently open exact faces are therefore:

1. a three-or-more-cut full-static return on `S0` with key
   `(0,+e_1e3b,...)`;
2. a return on the C0 shuttle (6.2) with key
   `(+e_54b1,0,...)`;
3. a return on one of the four C1 states (6.6) with key
   `(+e_x,0,...)`; or
4. one direct four-or-more-cut atom with final key
   `(e_z-e_d,0,...)`.

The first complete targeted generator for item 1 has at most 13,901,760
symbolic three-cut tuples before constant-radius seam/flat filtering: impose
one of 72 directed `U0` facet seams in one of the 15 pattern/seam slots and
range the one remaining cut.  Only exact `G0`/carrier/upper survivors need a
full static `h` replay.  This is the next finite theorem face; it is not
claimed decided here.

## 9. Conclusion

No complete surplus-to-hole chronology has been produced.  The strongest
proved advance is sharper:

* the desired full static token transfer is realized exactly on both frozen
  carriers by an explicit three-cut service half, unique within Theorem
  4.1's pure adjacent-signature class;
* each pure service half spends one explicitly identified unique upper
  witness;
* no pure-signature standard two/three-cut atom avoids that loss;
* the fixed `C0` service has no adjacent-neutral return through three cuts
  and no unrestricted return through two cuts; and
* the upper-safe C0 shuttle has no annihilating adjacent-cofacet two-opt,
  while its one-hole-preserving component is the two-cycle
  `0x54b1 <-> 0x64b1`;
* `C1` has four exact upper-safe signed service states, each with one named
  singleton return debt; and
* all 12,011 separated native forward direct-witness returns on the C1 pure
  service reopen one to three rank-seven holes.

Thus the obstruction is not parity or marginal capacity.  It is an exact
three-way chronology collision between the hole seam, the donor seam, and a
unique upper provider.  Any successful completion must use a wider
alternating circuit or a compound debt-return path.

## 10. Frozen artifacts

The primary targeted pure-atom census is

```
scratch/audit_a_k16_fiveopt_surplus_local_atoms_20260730.py
  SHA 8ddbd400982fd6f7f53274188c51c7b8cfd23539464621e9a0271992205a1cfc
scratch/a_k16_fiveopt_surplus_local_atoms_20260730.audit.json
  SHA 9bb834ef249204318cd51cd75b8b9fa6e8d72cae78c40fec3484825d6f2a507c
```

The C0 fixed-service return and signed-shuttle audits are

```
scratch/audit_a_k16_c0_service_upper_return_atoms_20260730.py
  SHA 7c9aa33656431b6f299299deef9ac52fc927643c663ba20d7e075b1563c59414
scratch/a_k16_c0_service_upper_return_atoms_20260730.audit.json
  SHA 2de81399310ed92ba7045337f38670c7b3e9c59908fb3f54ba0aa7ea4e1cf10a

scratch/audit_a_k16_c0_forward_relocation_single_debt_20260730.py
  SHA 8bdbd9e668f57e3ea7e59fffcf8a370405739d0ab76208709d584218972468fa
scratch/a_k16_c0_forward_relocation_single_debt_20260730.audit.json
  SHA 22fd98d8701ca1740ab5d83a1801cc79721c489ee83a80acb41bd9bc38fe0f1a
```

The adjacent-cofacet two-opt token graph is

```
scratch/audit_a_k16_c0_single_token_twoopt_return_graph_20260730.py
  SHA 8059ceec6e59fc106986358575c6bf928ddb2b5c2c5e3e7b834924db17e4bf33
scratch/a_k16_c0_single_token_twoopt_return_graph_20260730.audit.json
  SHA e722c4c2eede6c90c630a9181e2cdf8c0526a5fdb17d7b81f173315b73a9d772
  payload 37f59834b61bda3139580be49f2fe460066c4a72178615603f6165d02c2f7622
```

The complete C1 forward service and native direct-return audits are

```
scratch/audit_a_k16_c1_forward_threecut_surplus_transfer_20260730.py
  SHA 06e333db5a7ddc3448f7e094114b62d79cdeb2a5df78465bc14f73f7f55e3b97
scratch/a_k16_c1_forward_threecut_surplus_transfer_20260730.audit.json
  SHA 147e14496ac2367b9c8f6e864e006543ce9facf564bb913c88ea3f7374f0fb51

THREAD_A_K16_C1_NATIVE_FORWARD_UPPER_RETURN_OBSTRUCTION_20260730.md
  SHA 1bc72bc9bc9a0598212b6710423e21104cbb10b646c642556829955028a4049c
scratch/audit_a_k16_c1_native_forward_upper_return_20260730.py
  SHA 5aed284a0602daf6ae30dff9a4e8c249cef0544fce196744eceff1809e952a73
scratch/a_k16_c1_native_forward_upper_return_20260730.audit.json
  SHA 5fd07f0bee0ff6a124314ece47ca8398c22bc485073a942d2e2e67b13e1366c9
  payload 106b9bb79af82cbee5b2f0474933699817e4fc4573e0d2debe9fc97cb34a8aa5
```

The proof-safe but incomplete C0 full-static three-cut package is

```
THREAD_A_K16_C0_NATIVE_THREECUT_RETURN_GENERATOR_AND_PARTIAL_AUDIT_20260730.md
  SHA d9330b024833aa0678f69fa2aa20a7e7840e94f78166095a57197d1d041a76cf
scratch/threadA_k16_c0_fullstatic_threecut_return_20260730.cpp
  SHA 9f8ca2eead97e0dd1f88ee818a1fb56d27225a5e89d392fd6ffcb9285dcc899e
scratch/threadA_k16_c0_partial_threecut_returns_20260730.audit.json
  SHA 4e2e73900bd285a826ecede340be3f69de1861efeb9e5f18ed8c3b6c19b48204
```

The interrupted remote run is `UNKNOWN`; it is not a census artifact.

Finally, the filtered seam-parser defect and repair are frozen in

```
MATH_AUDIT_K16_FILTERED_SEAMCAT_PHASE_ARGUMENT_20260730.md
scratch/audit_a_k16_seamcat_argc7_phase_parser_20260730.py
scratch/a_k16_seamcat_argc7_phase_parser_20260730.audit.json
```

Every pre-patch `argc==7` phase-labelled stage-2 count is quarantined.  No
count or theorem in this note depends on it.
