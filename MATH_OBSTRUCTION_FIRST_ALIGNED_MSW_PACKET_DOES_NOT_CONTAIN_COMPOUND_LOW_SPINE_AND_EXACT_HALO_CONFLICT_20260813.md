# The first-aligned MSW portal packet does not already contain the compound low spine

**Date:** 2026-08-13  
**Status:** exact coexistence obstruction and exact selected-collar separation;
the relative incidence-trade problem remains open

## 1. Setup

Put

\[
 n=2m+1,\qquad R=m+1,
\tag{1.1}
\]

and assume the deadline regime

\[
 d\ge4,\qquad m\ge3d+2.
\tag{1.2}
\]

Use the height owners

\[
 U_h=\{0\}\mathbin{\dot\cup}[h+1,2h]
       \mathbin{\dot\cup}\{2h+2,2h+4,\ldots,2m\}.
\tag{1.3}
\]

The compound low-spine path contains the fixed seam

\[
                         C_4-U_5,                  \tag{1.4}
\]

where

\[
 C_4=\{0,5,6,7,8,9,12,14,\ldots,2m\},            \tag{1.5}
\]

\[
 U_5=\{0,6,7,8,9,10,12,14,\ldots,2m\}.           \tag{1.6}
\]

Let `F_m` be the exact wreath factor obtained from the canonical MSW
factor by applying the complete offset-zero first-aligned
`1100 <-> 1010` packet.  This is the target-independent factor used by
the internal-spine portal theorem.

## 2. An explicit two-row obstruction at the first compound seam

For every `m>=7`, put

\[
\begin{aligned}
 a_m&=101110011100(10)^{m-7}00,\\
 b_m&=101110011010(10)^{m-7}00,                    \tag{2.1}
\end{aligned}
\]

and

\[
\begin{aligned}
 c_m&=101111000110(10)^{m-7}00,\\
 e_m&=101110100110(10)^{m-7}00.                    \tag{2.2}
\end{aligned}
\]

All four words are Dyck words of semilength `m`.  In `(2.1)` the first
eligible aligned block is the block at positions `8,9,10,11`; in `(2.2)`
it is the block at positions `4,5,6,7`.  Consequently both pairs are
trades in the complete first-aligned packet.

### Theorem 2.1 (the packet separates the fixed seam endpoints)

The two positive rows replacing `(a_m,b_m)` contain the owners `C_4` and
`U_4`, one in each row.  A positive row replacing `(c_m,e_m)` contains
`U_5`.  In particular `C_4` and `U_5` belong to different rows of `F_m`,
and the edge `C_4-U_5` is absent from `F_m`.

#### Proof

Apply the literal inverse-triple row identity `(5.1)` of
`MATH_THEOREM_CLEAN_PACKAGE_CONFORMAL_WREATH_TRADE_PORTAL_AND_MATCHING_GATE_20260813.md`
to `(2.1)` and `(2.2)`.  The cyclic length-`m+1` windows beginning at the
displayed exceptional tails are respectively

\[
 \{0,5,6,7,8,9,12,14,\ldots,2m\}=C_4,            \tag{2.3}
\]

\[
 \{0,5,6,7,8,10,12,14,\ldots,2m\}=U_4,           \tag{2.4}
\]

and

\[
 \{0,6,7,8,9,10,12,14,\ldots,2m\}=U_5.           \tag{2.5}
\]

The positive middle supports of distinct conformal packet rows are
disjoint.  Hence `(2.3)` and `(2.5)` occur in different row components.
Edges of a wreath factor join consecutive owner windows in one row, so
they cannot form the seam `(1.4)`. \(\square\)

This is stronger than saying that a convenient embedding has not yet
been found.  The deterministic factor `F_m` literally does not contain
the first fixed edge of the compound replacement.

### Corollary 2.2 (no independent overlay)

The full first-aligned portal packet and the compound low-spine path do
not coexist by merely declaring the latter protected after the packet is
applied.  A further **relative incidence trade** must change the row
successors while preserving exact owner and immediate-lower incidence.

## 3. Exact separation of the selected portal collars from the compound seams

The obstruction in Section 2 is caused by other trades in the **whole**
packet.  It does not occur inside the explicitly selected internal-portal
rows themselves.

For a normalized portal `(A,q)`, its relevant positive row has zero-based
cyclic form

\[
                         P_{A,q}=(2,3,E,0,1,O),     \tag{3.1}
\]

where `|E|=m-1` and `|O|=m-2`.  The selected clean package and its four
literal halos are windows of this row.

Choose every free screen `z_h` in the compound path outside

\[
                         \{1,2,3,2m-1\}.           \tag{3.2}
\]

Only four labels are excluded, so the `Theta(m)` fresh-screen bank used
by the compound construction is unaffected.

### Lemma 3.1 (exceptional-marker separation)

Every fixed compound seam owner, immediate-lower facet, and immediate-
upper union contains `0` and omits `1,2,3`.  Its owner and lower-facet
values also omit `2m-1`.

For the row `(3.1)`:

1. every length-`m+1` window containing `0` and omitting `1` contains
   `3`;
2. the unique length-`m` window containing `0` and omitting `1` is
   `E\cup\{0\}`, and it contains `2m-1`;
3. every length-`m+2` window containing `0` and omitting `1` contains
   both `2` and `3`.

#### Proof

The labels `0,1` are consecutive in `(3.1)`.  For cyclic windows of a
fixed length, the start sets containing the first but not the second of
two consecutive positions differ in exactly one start.

For length `m+1`, that window starts at the preceding exceptional label
`3`.  For length `m`, it starts at the first position of `E`, hence is
`E\cup\{0\}`.  The flip-list formula for `z_(A,q)` has first odd-shore
entry `2m-4`, so `E` contains `3+(2m-4)=2m-1`.  For length `m+2`, the
unique window begins with the exceptional pair `2,3`.  This proves all
three assertions. \(\square\)

### Corollary 3.2 (selected-collar middle and immediate-upper separation)

Under `(3.2)`, every owner, immediate-lower facet, and immediate-upper
union in a fixed compound seam is distinct from every resource of the
same rank in every selected internal-portal clean collar.

Thus the selected portal bank is compatible with the compound **named
seam resources**.  This statement does not install the seam edges in the
ambient factor; Theorem 2.1 shows why that stronger incidence assertion
still needs a relative trade.

## 4. An unavoidable linear family of nonmiddle upper collisions

Although selected portal collars avoid the compound seams, the selected
collars are not mutually disjoint in their rank-`m+2` upper values.

For `2<=q<=d-2` and `A\in\{q+1,q+2\}` with `A+1<=d`, define

\[
\begin{aligned}
 Q_{A,q}={}&\{0,1,2m,2A,2A+2\}\\
 &\cup\{5,7,\ldots,2m-2q+1\}\\
 &\cup\{2m-2q+4,2m-2q+6,\ldots,2m-2\}.
                                                        \tag{4.1}
\end{aligned}
\]

The three displayed parts have total rank `m+2`.

### Theorem 4.1 (adjacent-height upper collision)

For every allowed `(A,q)`, the upper value `Q_(A,q)` occurs in the left
clean halo of both portal collars `(A,q)` and `(A+1,q)`.  The same
collision persists after reversing either pointed portal orientation.

Consequently the canonical selected collar bank contains at least

\[
                         2d-7                         \tag{4.2}
\]

distinct repeated rank-`m+2` values.

#### Proof

Insert the exact flip lists of `z_(A,q)` and `z_(A+1,q)` into `(3.1)`.
In each row, take the length-`m+2` window whose owner-edge index is `-A`
relative to the pointed portal.  The two windows differ only in labels
outside that window; their common set is exactly `(4.1)`.  Since `A<=d`,
the index `-A` lies in the protected left block

\[
                         [-d,q+d+1].                 \tag{4.3}
\]

Reversal reflects this block and leaves the same cyclic window value.

For every `q=2,...,d-3`, the two choices `A=q+1,q+2` contribute two
values.  For `q=d-2`, only `A=d-1` has `A+1<=d`, contributing one more.
The labels in `(4.1)` recover `(A,q)`, so these values are distinct.  The
count is `2(d-4)+1=2d-7`. \(\square\)

This is an upper-ticket obstruction, not a middle-incidence obstruction.
If upper coverage is only an inequality, a repeated witness value may be
harmless.  If the four halos carry distinct exact upper tickets, the
literal canonical collars cannot all be protected simultaneously without
rerouting or allowing a linear correction bank.

## 5. Exact frontier

The coexistence calculation therefore has three sharply different parts.

1. **Selected portal collars versus fixed compound seams:** exact
   owner/lower/upper value separation holds by Corollary 3.2.
2. **Selected collars versus each other:** middle exactness holds, but the
   explicit `2d-7` family `(4.1)` prevents naive exact nonmiddle-upper
   disjointness.
3. **Whole target-independent packet versus compound incidence:** the
   required seam `C_4-U_5` is absent by Theorem 2.1.

Hence the next theorem cannot be a passive coexistence statement.  It
must construct a relative row trade which installs at least the seam
`C_4-U_5` (and then the remaining compound path), while fixing every
selected portal row and preserving the complete owner/lower signature.

## 6. Finite replay

The standard-library scripts

* `scratch/audit_pbbs_portal_compound_coexistence_20260813.py`, and
* `scratch/verify_pbbs_portal_compound_overlap_formulas_20260813.py`

reconstruct the MSW inverse trades and check the displayed identities.
All substantive runs were performed on `h100`; the local Mac was used
only for lightweight proof and file inspection.
