# The q4 atom gives a genuine positive one-owner common reserve at k=17

**Date:** 2026-08-14
**Status:** exact positive owner theorem at the first unresolved parameter
`k=17,q=4,c=5`.  Both recoupled states are explicit unions of fourteen
pairwise owner-disjoint legal rails on the literal seventeen-label ground.
Typed q1/q2 resources, residence, and global factor topology are separate.

## 0. Outcome and setup

Use the ground `0,...,16` and put

\[
\begin{aligned}
 C_0&=\{13,14,15,16\},& C&=C_0\cup\{0\},\\
 P&=\{1,2,3,4\},& H&=C\cup P,\\
 S&=\{1,2,3,4,5,6\},& z&=7,\\
 E&=\{0,8,9,10,11,12,13,14,15,16\}.
\end{aligned}                                                   \tag{0.1}
\]

Thus `|C|=5`, `|H|=9`, `|S|=6`, and `|E|=10`.  Let
`A^+,A^-` be the q4 seven-by-seven atom from
`MATH_THEOREM_Q4_SEVEN_BY_SEVEN_NEAR_C_ATOM_ON_THIRTEEN_LABELS_20260814.md`,
lifted by `C0`.  It has 73 positive and 72 negative owners and

\[
          \sum_{Q\in\mathcal A^+}f(Q)
          =\sum_{Q\in\mathcal A^-}f(Q)+e_H.          \tag{0.2}
\]

This note constructs a conformal insertion/star macro with simple shores
`Y^+,Y^-`, where `H` occurs once in `Y^+` and not in `Y^-`, and

\[
                        P_9(Y^+-Y^-)={\bf1}_H.       \tag{0.3}
\]

After deleting that compulsory occurrence, put

\[
 B^+=Y^-,\qquad B^-=Y^+-e_H,\qquad
 \boxed{R_H=\sum_{Q\in\mathcal A^+}f(Q)}.           \tag{0.4}
\]

Then `B^+,B^-` are simple 73-owner matchings with identical point degrees,
and both `B^++R_H` and `B^-+R_H` are unions of fourteen pairwise
owner-disjoint closed rails with 146 owners.

## 1. Exact insertion without fresh labels

Take the period-10 old toggle word and its period-11 insertion

```text
sigma- = 2 3 4 6 7 8 10 12 9 11
sigma+ = 1 2 3 4 6 7 8 10 12 9 11.
```

Both use core `C`; call the rails `Q_Delta^-` and `Q_Delta^+`.  The cyclic
insertion identity gives

\[
 P_9\bigl(f(Q_\Delta^+)-f(Q_\Delta^-)\bigr)
                       ={\bf1}_C+4e_1.              \tag{1.1}
\]

The new first window is `1234`, so its owner is exactly `H`.

There are no labels outside `C0` and the thirteen-label atom at `k=17`, so
the fresh-marker argument used in the q3 theorem is unavailable.  The
collision claim here is literal:

\[
 \mathcal D(\mathcal A^+)\cap\mathcal D(Q_\Delta^-)=\varnothing,
 \qquad
 \mathcal D(\mathcal A^-)\cap\mathcal D(Q_\Delta^+)=\varnothing. \tag{1.2}
\]

An exhaustive H100 census checked all

\[
                         8\cdot3!\cdot7!=241920
\]

cyclic words obtained by omitting one auxiliary label, ordering the
consecutive target triple `2,3,4`, and permuting the other seven labels.
Exactly 88,964 old words satisfy the first condition in `(1.2)`, and
77,876 satisfy both.  The displayed word is the first certificate.  The
final theorem relies only on its direct replay, not on the census count.

## 2. Three-copy q4 star correction

For `u in {1,2,3,4}`, a star potential has core `S-u`, old toggle set `E`,
and new toggle set `E+z`.  If `tau_u^+` inserts `z` into `tau_u`, then

\[
 \Phi_u=f(S-u,E+z,\tau_u^+)-f(S-u,E,\tau_u),
 \qquad P_9\Phi_u={\bf1}_S-e_u+4e_z.                \tag{2.1}
\]

Use three copies of the `u=1` potential with the following old/new words:

```text
Phi1^(2)-: 10 8 13 14 16 11 9 0 15 12
Phi1^(2)+: 10 8 13 14 16 11 9 0 7 15 12

Phi1^(3)-: 12 8 16 0 11 13 14 10 15 9
Phi1^(3)+: 12 8 16 0 7 11 13 14 10 15 9

Phi1^(4)-: 14 12 11 13 0 10 15 8 9 16
Phi1^(4)+: 14 7 12 11 13 0 10 15 8 9 16.
```

For the three leaf potentials use

```text
Phi2-: 11 9 14 10 12 13 0 16 15 8
Phi2+: 11 9 14 10 7 12 13 0 16 15 8

Phi3-: 8 9 13 10 16 15 14 0 11 12
Phi3+: 8 7 9 13 10 16 15 14 0 11 12

Phi4-: 9 16 15 12 11 14 10 13 0 8
Phi4+: 9 16 7 15 12 11 14 10 13 0 8.
```

Put

\[
 K=(\Phi_1^{(2)}-\Phi_2)+(\Phi_1^{(3)}-\Phi_3)
                         +(\Phi_1^{(4)}-\Phi_4),
 \qquad Y_H=\Delta+K.                               \tag{2.2}
\]

Equations `(1.1)` and `(2.1)` give

\[
              P_9Y_H={\bf1}_C+4e_1-3e_1+e_2+e_3+e_4
                     ={\bf1}_H.                    \tag{2.3}
\]

The two macro shores are

\[
\begin{aligned}
 \mathcal Y^+=\{&Q_\Delta^+,
  (\Phi_1^{(2)})^+,(\Phi_1^{(3)})^+,(\Phi_1^{(4)})^+,
  (\Phi_2)^-,(\Phi_3)^-,(\Phi_4)^-\},\\
 \mathcal Y^-=\{&Q_\Delta^-,
  (\Phi_1^{(2)})^-,(\Phi_1^{(3)})^-,(\Phi_1^{(4)})^-,
  (\Phi_2)^+,(\Phi_3)^+,(\Phi_4)^+\}.
                                                               \tag{2.4}
\end{aligned}
\]

They contain respectively 74 and 73 owners.  `H` occurs exactly once in
`Y^+`, at the new insertion window, and does not occur in `Y^-`.

## 3. Complete collision audit

The displayed orders have the following literal properties.

1. The three old `Phi1` decks are pairwise disjoint, and the three new
   `Phi1` decks are pairwise disjoint.
2. Different star cores `S-u` are signature-disjoint: their toggle words
   use no label of `S`, so the omitted member of `S` is recoverable from an
   owner.
3. No displayed old or new star word has `C0` as a cyclic four-window.
   At the boundary `c=5`, this excludes the only possible atom/star
   equality.  Literal replay gives

   \[
   \mathcal D(\mathcal A^+)\cap\mathcal D(\mathcal Y^-_{\rm star})
   =\mathcal D(\mathcal A^-)\cap\mathcal D(\mathcal Y^+_{\rm star})
   =\varnothing.                                    \tag{3.1}
   \]

4. An insertion owner contains the five-core `C`, while a star owner
   contains the disjoint five-core `S-u`.  Their union has size ten, larger
   than the owner rank nine, so insertion/star equality is impossible.
5. The insertion/atom intersections are empty by `(1.2)`.

Consequently both macro shores are owner-simple and

\[
 \mathcal D(\mathcal A^+)\cap\mathcal D(\mathcal Y^-)=\varnothing,
 \qquad
 \mathcal D(\mathcal A^-)\cap\mathcal D(\mathcal Y^+)=\varnothing. \tag{3.2}
\]

## 4. Genuine positive reserve

Define `B^+,B^-` and `R_H` as in `(0.4)`.  Since `H` is the unique deleted
owner, both `B` shores have 73 owners.  Equation `(2.3)` shows that they
have identical point degrees.

The first augmented state has the rail decomposition

\[
              B^++R_H=\mathcal Y^-+\mathcal A^+,    \tag{4.1}
\]

and is simple by `(3.2)`.  For the second, the exact atom identity `(0.2)`
gives

\[
 \begin{aligned}
              B^-+R_H
       &=(\mathcal Y^+-e_H)+\mathcal A^+\\
       &=\mathcal Y^++\mathcal A^- .                \tag{4.2}
 \end{aligned}
\]

This is also simple by `(3.2)`.  Each right side contains fourteen legal
closed rails and 146 owners.  Therefore `R_H=A^+` is a genuine nonnegative
common reserve for the exact q4 k17 insertion/star macro, not a signed
lattice identity or an asymptotic packing statement.

### Corollary 4.1 (every named k17 owner)

The symmetric group on the seventeen coordinates is transitive on the
rank-nine owners.  Relabelling the complete certificate therefore supplies
the same positive common-reserve construction for every prescribed
`H' in binom([17],9)`.  This is an individual-owner theorem; it does not by
itself choose collision-free copies for many prescribed owners
simultaneously.

## 5. Independent H100 verification

The final verifier rebuilds all fourteen atom rails, the insertion pair,
the six star potentials, both macro shores, `B^+,B^-`, and both recoupled
states.  It checks every named owner, shore simplicity, cross collision,
point degree, reserve identity, and rail count without importing search
code.

```text
scratch/verify_q4_k17_positive_common_reserve_20260814.py
SHA-256 87b0d24d1bdeae35fdbd02fee7c4bdb9d3a0d83ef7deed45c7959cbdc839b3b9

H100 output
scratch/verify_q4_k17_positive_common_reserve_20260814.h100.out
SHA-256 3d417e54b83a893bcfa15193370f9ddbde5cc98fceafa0ee5c90222ab7073f05
```

The two supporting finite searches are

```text
scratch/search_q4_v13_atom_k17_insertion_collision_20260814.py
SHA-256 e26f931301bcd95d7a8725771114a3a2495178f095d4e5205175260ab8689dcb
output SHA-256 b1ea46abfa95570b97e59785c4d8f9085d93fb49cc35882a46588beb15f9c5ff

scratch/search_q4_k17_three_copy_star_pack_20260814.py
SHA-256 3a13e540e828ef608090c281f78b41070754850847af5c89a6860ef80a98c187
output SHA-256 78b084200f21515b0aa60400114dc534bd12032147f8d44fb3d3e88111d31920
```

All searches, verification, compilation, and hashing ran via SSH on H100.
The local Mac was used only for editing and Git.

## 6. Scope

This closes the special zero-point **owner-only** positive reserve gate at
the exact first unresolved parameter `k=17`.  It does not yet align the
literal lower flags or immediate/wider upper tickets, prove q-biresidence,
or place the fourteen-rail states inside one connected global factor.  Those
typed occurrence and chronology conditions remain necessary before an
optimal OR word is claimed.
