# Hostile audit: q4 seven-by-seven atom and k17 positive common reserve

**Date:** 2026-08-14
**Verdict:** **PASS at the named-owner/point-role level.**  The atom has an
exact one-owner named current.  The insertion/star macro has only the
claimed point current, and the two explicit recoupled rail states are
owner-simple with identical point roles.

## 1. Audited sources

```text
MATH_THEOREM_Q4_SEVEN_BY_SEVEN_NEAR_C_ATOM_ON_THIRTEEN_LABELS_20260814.md
SHA-256 9619e75f9efe620a61595dc40c47ce5bc3a6d5d161e170ac31a28a26aedd250d

MATH_THEOREM_Q4_K17_POSITIVE_ONE_OWNER_COMMON_RESERVE_20260814.md
SHA-256 cae68fd6542d1925c3663c901f981fee596dfa10560fc01b278d367960c7573d
```

Two malformed control bytes in the first draft of the reserve theorem's
point equations were repaired to literal `\bf1`.  No mathematical sign or
collision claim required weakening.

## 2. Seven-by-seven atom audit

The first five rails have signed current

```text
 e_H - e_(C1+2) + e_(C1+3) + e_(C2+2) - e_(C2+3).
```

For a word segment `L,2,3,R`, the theorem's convention is
`after-before`, where `after` swaps `2,3`.  Direct expansion gives

```text
 -e_(cL+2) + e_(cL+3) + e_(cR+2) - e_(cR+3),
```

so the sign in the adjacent-transposition lemma is correct.  Since the
positive extra rail is `before` and the negative extra rail is `after`,
the first pair contributes

```text
 e_(C1+2)-e_(C1+3)-e_(C*+2)+e_(C*+3),
```

and the second contributes

```text
 e_(C*+2)-e_(C*+3)-e_(C2+2)+e_(C2+3).
```

The `C*={5,6,7,8}` terms cancel literally, leaving the negative of the
five-rail rectangle.  Thus the complete current is exactly `e_H`.

The strengthened independent replay checks that all fourteen toggle words
are distinct-label words avoiding their centres, every cyclic wrap edge is
a Johnson edge, and each individual swap has the displayed intermediate
current.  It reconstructs 73 distinct positive owners and 72 distinct
negative owners; the negative set is exactly the positive set with `H`
deleted.  Hence the common-core lift is an exact occurrence identity, not
only a point projection.

```text
scratch/verify_q4_v13_seven_by_seven_atom_20260814.py
SHA-256 a5f1d9d1224457ce48ebd38e6489123185f894d5d5f310ef1951e3f6d0d5c69a

scratch/verify_q4_v13_seven_by_seven_atom_20260814.h100.out
SHA-256 400865dad6b0a2fef8da2b887f1ce2c62d015497126ffa8b40b48c242ec00bd2
```

## 3. Insertion and star algebra at k17

The old/new insertion words have periods 10 and 11 and differ only by
inserting label `1`.  Their point current is

```text
1_C + 4 e_1.
```

For a star core `S-u`, insertion of `z` changes the point vector by
`1_S-e_u+4e_z`.  Therefore

```text
(Phi1^(2)-Phi2)+(Phi1^(3)-Phi3)+(Phi1^(4)-Phi4)
```

has point current `e_2+e_3+e_4-3e_1`; adding the insertion current gives
exactly `1_H`.  The macro named-owner current is not asserted to equal
`e_H`, and the theorem correctly uses only this point projection.

The three repeated `Phi1` old decks are pairwise disjoint, as are their
new decks.  The other star cores are distinguished by their intersection
with `S`, because every toggle word avoids `S`.  Thus the seven macro
rails form simple shores of sizes 74 and 73.  Direct replay also confirms
that `H` occurs exactly once on the positive macro shore, in the insertion
rail, and never on the negative macro shore.

## 4. Complete finite collision audit

The zero-fresh-label boundary is genuinely covered.

1. The literal period-10/11 insertion pair has empty intersections with
   the opposite atom shores needed by the two recouplings.  The supporting
   census exhausts the normalized family of
   `8*3!*7!=241920` words; its first certificate is the theorem's word.
2. Every star old/new word is respectively a permutation of `E` and
   `E+z`, with the new word obtained by one insertion.  No word has `C0`
   as a cyclic four-window.
3. At `c=5`, an atom/star equality would have to contain the disjoint
   four-set `C0` and five-element star core.  Since these already fill the
   rank-nine owner, its star window would have to equal `C0`, excluded by
   item 2.
4. The insertion core `C` and every star core `S-u` are disjoint
   five-sets.  Their ten-element union cannot fit in a rank-nine owner.
5. Literal replay gives no remaining atom/macro cross collision in either
   recoupled state.

Both finite searches replay byte-for-byte on H100:

```text
scratch/search_q4_v13_atom_k17_insertion_collision_20260814.py
SHA-256 e26f931301bcd95d7a8725771114a3a2495178f095d4e5205175260ab8689dcb
output SHA-256 b1ea46abfa95570b97e59785c4d8f9085d93fb49cc35882a46588beb15f9c5ff

scratch/search_q4_k17_three_copy_star_pack_20260814.py
SHA-256 3a13e540e828ef608090c281f78b41070754850847af5c89a6860ef80a98c187
output SHA-256 78b084200f21515b0aa60400114dc534bd12032147f8d44fb3d3e88111d31920
```

## 5. Positive reserve and exact scope

With `B^+=Y^-`, `B^-=Y^+-e_H`, and `R_H=A^+`, both `B` shores are
simple 73-owner vectors with equal point degrees.  The atom identity gives

```text
B^+ + R_H = Y^- + A^+,
B^- + R_H = Y^+ + A^-.
```

The right sides are explicit unions of fourteen pairwise owner-disjoint
closed rails and contain 146 owners each.  The final independent replay
checks all literal star insertions and wrap edges, shore and cross
simplicity, the macro point current, the reserve algebra, and equality of
the two final point-role vectors:

```text
scratch/verify_q4_k17_positive_common_reserve_20260814.py
SHA-256 87b0d24d1bdeae35fdbd02fee7c4bdb9d3a0d83ef7deed45c7959cbdc839b3b9

scratch/verify_q4_k17_positive_common_reserve_20260814.h100.out
SHA-256 3d417e54b83a893bcfa15193370f9ddbde5cc98fceafa0ee5c90222ab7073f05
```

This closes the q4 `k=17` owner-only positive common-reserve gate.  It does
not establish immediate lower/upper colour simplicity, wider-window
resources, residence, chronology, or connected global factor topology.
The five-by-five atom minimum also remains open.
