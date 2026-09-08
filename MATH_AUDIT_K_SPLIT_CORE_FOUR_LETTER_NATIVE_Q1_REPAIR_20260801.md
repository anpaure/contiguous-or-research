# Independent audit of the split-core four-letter native-q1 repair

Date: 2026-08-01  
Corrected theorem SHA-256:
`b832d51713594f9c424ece34d1fe3a0962ab87fa8157842734979be53d354275`  
Verdict: **GO as a new four-enlargement source; NO transport from the sparse
source.**

## 1. Correct literal word

Retain `X=X_L dotunion X_R`, `x_L in X_L`, `x_R in X_R`, and retain the
two outer donor letters

\[
 (C\cup X_L)\cup\{d^-_{h-1}\},\qquad
 (C\cup X_R)\cup\{d^+_1\}.
\]

Enlarge only the four letters listed in (4.16a):

\[
 (X_R-x_R)+q^-\mapsto B^-,\quad
 (C+X_L)+\lambda_h\mapsto(B-x_R)+\lambda_h,
\]

\[
 (C+X_R)+\rho_1\mapsto(B-x_L)+\rho_1,\quad
 (X_L-x_L)+q^+\mapsto B^+.
\]

The previously displayed serialization with singleton outer `d` letters
was not equivalent: it additionally contracted two source positions.  The
theorem has been corrected to the genuine four-letter word.

## 2. Exact positive theorem

For every `h>=2`, the repaired word has the same depth-`h` owner row and,
after deleting `X`, the same pre-row as the sparse word:

\[
 D^hA^{\rm tight}=L_0,\ldots,L_{h-1},M_0,\ldots,M_h,
 R_0,\ldots,R_{h-1},
\]

\[
 D^hA^{\rm tight}_{\rm pre}
 =L_0,\ldots,L_{h-1},U_0,\ldots,U_{h-1},R_0,\ldots,R_{h-1},
\quad U_j=M_j\cup M_{j+1}.
\]

Each added coordinate is already present in every depth-`h` window meeting
its source position, which proves these identities without cancellation.
For adjacent owner windows `O_t,O_(t+1)` with shared `h`-letter cell `C_t`,

\[
 O_t\cap O_{t+1}=C_t\cup(a_t\cap a_{t+h+1}).
\]

The four enlargements put every endpoint intersection term into `C_t`.
Hence all `3h` lower colours occur at their native shared addresses; the
spanning `h+2`-letter intervals give all upper colours.  Both palettes are
literal and their set values are separately injective.

The two letters adjacent to the insertion have joint union

\[
 ((B-x_R)+\lambda_h)\cup((B-x_L)+\rho_1)
 =B\cup\{\lambda_h,\rho_1\}\supseteq X.
\]

Therefore every interval of the repaired pre-word transports injectively,
with the same OR, after reinserting `X`.  The only insertion-born cells of
source length at most `h` remain `[X]` and the two nested rays; the lost
length-`h` cells remain `M_1,...,M_(h-1)`.  No new insertion class is hidden
at `h=2`.

The extreme identities are stronger than value equality:

\[
 P_{h-1}=I_0,\qquad S_{h-1}=I_{h-1}
\]

are the same physical interval addresses.  A compiler ledger must share
each cell between its ray and q1 interpretation, not demand two capacities.

## 3. Sharp negative scope

There is no sparse-to-tight deck transport.  At `h=2`, take
`C={c}`, `X_L={x_L}`, `X_R={x_R}`.  The sparse singleton seam value
`{q^-}` becomes `{c,x_L,q^-}`.  Since `q^-` occurs nowhere else, the old
value `{q^-}` disappears completely.  Thus an incumbent target matching or
exact guard using it has no transported witness, although all owner and q1
rows of the repaired word are correct.

At every fixed source length `1<=q<=h`, generically four interval addresses
change value, one per enlargement; no interval of length at least `h+1`
changes.  Empty opposite-shore additions can reduce the short-row count.
Consequently every matching/equality/deadline/guard row meeting one of the
four enlarged positions must be replayed.  The exact transparency direction
is only

\[
 \operatorname{Deck}(A^{\rm tight}_{\rm pre})
 \subseteq \operatorname{Deck}(A^{\rm tight}_{\rm post}).
\]

Residence of the owner subpath is unchanged.  Under a literal source
embedding, endpoint runs are extended automatically by the crossing
depth-`h` windows; the remaining condition is that those exterior windows
are valid owners and pass their guards.  Abstract protected owner-path
containment alone does not retain the source antecedent.

## 4. Replay

The independent script
`scratch/audit_k_split_core_four_letter_q1_repair_20260801.py`, SHA-256
`67301baffc0cc15c6556706d9704290163c5683b776f9cee1439ff360c1e72e7`,
checks 297 symbolic cases with `2<=h<=12`, including empty/singleton shore
limits.  It reports:

```text
PASS_FOUR_LETTER_REPAIR
owners/pre-row/q1/insertion-transport/rays exact
sparse_to_repaired_deck_not_transparent
generic_changed_addresses_per_length_1_to_h=4; above_h=0
```

Thus the four native q1 deficits are genuinely repaired.  What is not
repaired is arbitrary sparse-source background admissibility; that is now
the exact exterior replay gate.
