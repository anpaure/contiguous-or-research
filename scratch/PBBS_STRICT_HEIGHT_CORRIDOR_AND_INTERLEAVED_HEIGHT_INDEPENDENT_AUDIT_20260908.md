# Strict-height corridors and the height of the interleaved PBBS cycle

2026-09-08. Independent pure-proof audit by `exact_b_induction` of the
user's strict-height argument. No mathematical program was run.

Verdict: the strict-height corridor and the interleaved-height assertion
both pass. The proof below uses the actual finite corridor of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, Lemma 21.1 and Theorem 21.2,
and the actual rooted one-step map in
`MATH_ATTACK_Y12_DIRECT_ALL_DEPTH_PBBS_DYCK_GATE_20260725.md`, Lemma 2.1.

## 1. Precise strict-height statement

Let n=2r+1, g=f^2, and let S be nonempty of rank r-q, where
1<=q<=r-1. There is a canonical oriented path

    B0, B1=gB0, ..., Bq=g^q B0

such that their intersection is S and the normalized Dyck height of
B0 is at least q+1. The same height is carried by every state of this
path and by the interleaved f-shifted cycle needed for lower targets.

For q=0 the one-state path B0=S has height at least one, so the same
strict inequality relative to q is immediate. The empty set is excluded:
at q=r, height at least r+1 would be impossible.

## 2. Reverse gaps and moving a global maximum backward

Let C_0,...,C_(d-1), d=2q+1, be the reverse-unmatched zeros of S in
forward cyclic order. Reverse matching cancels adjacent01 pairs. The
physical open gap between consecutive surviving C marks is a possibly
empty reverse-Dyck word: it is balanced and all one-minus-zero prefix
sums are nonpositive. One proof reverses the cancellation sequence:
inserting01 pairs preserves those nonpositive prefix sums. The surviving
C marks are barriers, so no matched pair crosses one of them.

Some reverse gap is nonempty because S is nonempty. Every such nonempty
gap has a negative prefix minimum, at most -1.

Form the expanded A/C word exactly as in the source, placing C_x,A_x
in that order at a coordinate carrying both marks. Let z_i count A marks
strictly between C_i and C_(i+1), and let the cyclic potential satisfy

    F(i+1)-F(i)=z_i-1.

Choose a C at a global maximum. Suppose its preceding PHYSICAL reverse
gap is empty. The two C marks are then adjacent original zero coordinates.
The expanded gap between them can contain at most one A mark, namely
the possible shared A at the first C coordinate. The possible A at the
second coordinate follows that C and is not in the expanded open gap.
Thus z_prev<=1.

Maximality gives z_prev-1=F(current)-F(previous)>=0. Hence z_prev=1,
and the preceding C is itself at the same global maximum. Move the choice
backward across this empty gap and repeat. Since at least one reverse
gap is nonempty, this finite backward traversal eventually finds a
global-maximum C0 with a nonempty preceding physical reverse gap.

Every global maximum satisfies the two-sided corridor inequalities of
Lemma 21.1. The source proof therefore applies unchanged at this chosen
maximum; this adjustment does not replace it by a merely local maximum.

## 3. A proper cyclic rise of at least q+1

Let G be the nonempty reverse-Dyck gap immediately preceding the selected
C0. Start at a vertex where its prefix sum has minimum -M, with M>=1.
The remaining suffix of G rises by exactly M to its ending height zero.

The actual corridor initial state is

    B0=S union {C0,...,C_(q-1)}.

Follow the physical cyclic interval from just after that minimum through
C_(q-1), inclusive. Its suffix of G contributes M; its q displayed
C coordinates have been changed from zeros to ones and contribute q;
the q-1 intervening reverse gaps are balanced. Its total one-minus-zero
increment in B0 is therefore M+q>=q+1.

This interval is proper. It begins inside the gap before C0 and ends at
C_(q-1), leaving the remaining d-q=q+1 unmatched marks outside. No
unproved multiple-winding increment is being used.

For any rank-r state on2r+1 coordinates normalized as0D, the maximum
increment of a proper cyclic interval is exactly ht(D). An interval
inside D has increment equal to a difference of prefix heights in[0,H],
hence at most H. One crossing the distinguished zero has increment
-h_start-1+h_end<=H-1. A prefix of D reaching its maximum attains H.
Thus the constructed interval proves ht(B0)>=q+1.

At the chosen global maximum, Theorem 21.2 supplies the actual states

    B_t=S union {C0,...,C_(q-t-1)} union {A0,...,A_(t-1)},

with gB_t=B_(t+1) and intersection S. Its collision exclusion and exact
predecessor/successor laws are retained. The height argument concerns
this actual corridor, rather than an arbitrary high completion of S.

## 4. One PBBS step preserves height exactly

Normalize a middle state as0D and let H=ht(D). Write D=P1Q at the first
up-step attaining H. The exact one-step map has normalized root

    phi(D)=complement(Q) 0 complement(P),

without reversing either word. Along complement(Q), the new height is
H minus the old height along Q, so it lies in[0,H] and ends at H.
The following zero lowers the height to H-1. Every prefix of P has
height in[0,H-1]; along complement(P) the new height is H-1 minus that
prefix height, so it stays in[0,H-1] and ends at zero.

Consequently ht(phi(D))=H, with equality attained at the end of
complement(Q). Physical rotation of the root does not change normalized
height. Therefore

    ht(fB)=ht(B),  ht(f^-1 B)=ht(B),  ht(gB)=ht(B).

The inverse equality follows because f is a bijection. This proves the
height statement for the interleaved component, not only for g-orbits.

## 5. Exact lower/upper witness transfer and the extra one

Let B_t=g^t B0 be the corridor. For an upper target S^c, the upper owners
B_t^c directly give a union of q+1 owners equal to S^c. Their underlying
middle cycle has height H>=q+1.

For the lower target S itself, define C_j=f^-1 g^j B0 for
0<=j<=q+1 and upper owners X_j=C_j^c. Then C_(j+1)=f^2 C_j, and the
exact PBBS identity gives

    X_j intersect X_(j+1)=fC_j=B_j.

For completeness, fC_j is disjoint from both C_j and f^2C_j. Those two
rank-r states are distinct Johnson neighbors, so their complement
intersection has rank r and is exactly fC_j. Taking all adjacent
intersections yields

    intersection_(j=0)^(q+1) X_j
       =intersection_(j=0)^q B_j=S.

This lower witness uses q+2 upper owners on the INTERLEAVED component.
Section4 shows that its height is still H, so the strict bound gives
q+2<=H+1. A non-strict H>=q bound alone would not supply this interface.

The case q=0 uses two upper owners on a component of height at least one.
The full ground set, corresponding to empty S on the upper side, is a
separate boundary target; once all singleton targets have literal
witnesses in a nonempty linear word, its full-word union realizes that
ground set automatically.

## 6. Scope

This note certifies the strict corridor-height theorem and the actual
height equality across interleaving. The height-dependent erosion,
cycle opening costs, component enumeration, and final all-dimensional
word-length estimate are separate construction steps being audited by
root. None of their numerical conclusions is assumed here.
