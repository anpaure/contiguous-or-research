# Thread D: K16 append-0200 one-debt portal and the global radius-two gate

**Date:** 2026-07-30  
**Status:** exact 16-portal return obstruction; global radius two remains open

## 1. Frozen source

Let \(A\) be

    scratch/k16_append0200_12874_onehole.word
    length 12874
    SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18

This is the authenticated length-12,873 three-hole word followed by the
literal entry \( \mathtt{0x0200} \).  Appending preserves every old witness.
Exact ending-OR replay gives the sole hole

\[
H(A)=\{h\},\qquad h=\mathtt{0x287d}=10365.
\tag{1.1}
\]

For a substitution set \(E\), define

\[
L(E)=\{T:c_A(T)>0=c_{A^E}(T)\},\qquad
G(E)=\{T:c_A(T)=0<c_{A^E}(T)\}.
\tag{1.2}
\]

The edited word is universal exactly when \(h\in G(E)\) and
\(L(E)=\varnothing\).  All claims below use exact interval multiplicities;
they do not add signed one-edit columns without replaying the mixed term.

## 2. Complete one-substitution frontier

Any one-substitution installer of \(h\) replaces its changed cell by a
nonzero submask of \(h\).  Exhausting all

\[
12874(2^8-1)=3,282,870
\]

position/submask assignments gives:

* 26,701 assignments install \(h\);
* none is universal;
* the minimum collateral debt is one;
* exactly 16 portals attain that minimum.

All 16 change position 6440 from \( \mathtt{0xa069} \).  Their new values are

    0x206d 0x206c 0x2065 0x2064
    0x204d 0x204c 0x2045 0x2044
    0x202d 0x202c 0x2025 0x2024
    0x200d 0x200c 0x2005 0x2004

Equivalently,

\[
V=\{\mathtt{0x2004}\vee s:s\subseteq\mathtt{0x0069}\}.
\tag{2.1}
\]

Every \(v\in V\) performs the exact one-hole transfer

\[
\{h\}\longmapsto\{d\},
\qquad d=\mathtt{0xa879}=43129.
\tag{2.2}
\]

The complete census is
*scratch/threadD_k16_append0200_onehole_census_20260730.audit.json*.
The native run used one H100 CPU, 12,288 KiB RSS, and 0.43 seconds wall
time.

## 3. Complete one-return census from every minimum portal

Fix \(v\in V\) and let \(A_v\) be the corresponding one-hole word with
hole \(d\).  Any second substitution that installs \(d\) has replacement
value in the 255 nonzero submasks of \(d\).  For each of the 16 portal
states, the exact census evaluates all 3,282,870 position/value pairs and
finds:

* exactly 27,840 substitutions install \(d\);
* no substitution completes the word;
* the minimum final debt is one, attained by 16 substitutions at position
  6440 itself; these merely toggle back to a state missing \(h\);
* among substitutions away from position 6440, the minimum final debt is
  two, attained 65 times.

The 65 best off-portal returns have two forms:

1. 64 replacements at position 0 leave
   \(\{43117,44141\}=\{\mathtt{0xa86d},\mathtt{0xac6d}\}\);
2. \(p12873:\mathtt{0x0200}\mapsto\mathtt{0xa879}\) leaves
   \(\{52833,52835\}=\{\mathtt{0xce61},\mathtt{0xce63}\}\).

These counts are identical for all \(v\in V\).  Therefore:

> **Theorem 3.1 (no two-substitution closure through the minimum portals).**
> No universal word at Hamming radius two from \(A\) uses
> \(A_{6440}\in V\).  Every return that restores \(d\) either restores the
> original hole \(h\), or creates at least two other holes.

The 16 per-portal outputs are
*scratch/threadD_k16_append0200_p..._offreturn_20260730.audit.json*; their
aggregate is
*scratch/k16_append0200_16portal_radius2_census_20260730.audit.json*.
An independent retained Python implementation, SHA-256
\(\mathtt{ca77a8ed469fa9e70311d6549f34ad31f15bc9ca13489906e4824474e6112e30}\),
also returns no universal two-substitution word.  Its H100 run used one CPU,
47,768 KiB RSS, no swap, and 17.14 seconds wall time.

The compact radius-two Benders cut is especially simple.  Membership in
\(V\) means that bits in \( \mathtt{0x2004} \) are one, bits outside
\( \mathtt{0x206d} \) are zero, and the four bits in
\( \mathtt{0x0069} \) are free.  Hence the single clause

\[
\bigvee_{b\in\mathtt{0x2004}}\neg f_{6440,b}
\ \vee\
\bigvee_{b\notin\mathtt{0x206d}} f_{6440,b}
\tag{3.1}
\]

excludes all 16 branches at once inside a master with substitution budget
at most two.  The budget guard is essential; (3.1) is not valid for an
unbounded number of return edits.

## 4. Why this is not a global radius-two theorem

The result above removes only the 16 sharp direct portals.  Two exact classes
remain:

1. one of the other 26,685 direct installers of \(h\), followed by a second
   edit that repairs all of its debts;
2. a joint-only pair whose combined intervals witness \(h\), although neither
   one-edit prefix installs \(h\).

The second class is why a portal-prefix DFS is incomplete.  It must be
represented by final witness constraints.

For a target \(T\) and interval \(I\), put

\[
M_T(I)=\{i\in I:A_i\not\subseteq T\}.
\]

Every radius-\(r\) final witness interval satisfies \(|M_T(I)|\le r\).
Conversely, final cell bits on \(I\) witness \(T\) exactly when every cell is
a submask of \(T\) and their OR is \(T\).  Extending each left endpoint only
until the \((r+1)\)-st source-bad cell enumerates all such intervals with no
width cutoff.

For the source \(A\) and \(h\), the exact row sizes are:

| radius | witness intervals | mandatory support sets | maximum width |
|---:|---:|---:|---:|
| 1 | 13,579 | 12,558 | 5 |
| 2 | 26,775 | 25,114 | 6 |
| 3 | 39,972 | 37,669 | 7 |
| 4 | 53,165 | 50,223 | 8 |

Thus a global radius-two CEGAR is modest.  Give every position final-value
bits \(f_{i,b}\), channel \(u_i=[f_i\ne A_i]\), require nonzero cells and
\(\sum_i u_i\le2\), and install the exact disjunction over the 26,775 final
\(h\)-witness intervals.  Literal replay of a candidate supplies a missing
target \(T\); add the analogous exact interval row for \(T\).  A verified
SAT word is positive.  A completed UNSAT solve of any such relaxation is
already a sound global radius-two no-go.  Timeout or resource exhaustion is
UNKNOWN.

The general encoding and proof are in
*THREAD_D_K16_LENGTH12874_ONEHOLE_GLOBAL_EXCHANGE_CEGAR_20260730.md*.

## 5. Immediate exact schedule

1. Install clause (3.1).
2. Enumerate/score the remaining direct installers by exact debt count and
   add guarded one-return rows.
3. Keep the eager final-\(h\) interval row so joint-only pairs remain in the
   formula.
4. Separate every replayed hole with its exact final-witness row.
5. Accept a candidate only after independent 65,535-mask replay.

The two best off-portal continuations identify the first radius-three
exchange corridors, but they are not radius-two candidates: one moves the
debt to the boundary pair \(\{43117,44141\}\), and one moves it to the high
tail pair \(\{52833,52835\}\).  Any claimed balanced cycle must close those
new debts in the same simultaneous literal word.

## 6. Reproduction

The independently executed return audit is
*scratch/audit_threadA_k16_append0200_one_debt_return_20260730.py*.  Its
retained outputs are *scratch/threadD_append0200_return.stdout.txt* and
*scratch/threadD_append0200_return.resource.txt*.  The focused theorem note
*THREAD_D_K16_APPEND0200_ONE_DEBT_RETURN_GATE_20260730.md* records their
hashes and exact scope.
