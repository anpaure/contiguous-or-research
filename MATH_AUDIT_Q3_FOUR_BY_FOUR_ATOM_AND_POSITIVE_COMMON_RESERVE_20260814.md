# Hostile audit of the q3 four-by-four atom and positive common reserve

**Date:** 2026-08-14
**Verdict:** **PASS at the named-owner level, with the stated ambient
packing hypothesis.**

Audited sources and H100 SHA-256:

```text
MATH_THEOREM_Q3_FOUR_BY_FOUR_NEAR_C_ATOM_ON_ELEVEN_LABELS_20260814.md
baada59836c861cff33f56cf755f2f42b1c51d876a3122bfd02afea8d44b9826

MATH_THEOREM_Q3_ELEVEN_LABEL_ATOM_GIVES_POSITIVE_ONE_OWNER_COMMON_RESERVE_20260814.md
0fa1b1739c087fd4641b5482187cd420649b4d2ff066830d141c51406a28adc7
```

## 1. Literal atom replay

The eight cyclic words have the advertised periods, contain distinct
toggles, and avoid their centres.  Every consecutive three-window shift is
a Johnson edge, including wraparound.  Direct reconstruction gives 34
distinct positive owners and 33 distinct negative owners.  The negative
set is exactly the positive set minus `{0,1,2,3}`; the extra owner is the
first window of `p8a`.

The independent verifier imports no solver code:

```text
scratch/verify_q3_near_c_four_by_four_v11_atom_20260814.py
SHA-256 e975f97fc80bfb1ea424fd1bfe4b1559653cc22155e1e6c91313f17fa4b520d5

H100 output SHA-256
d9d53244fb68970b099c2897740db24d291d47e792a026c185dcf9f32c48970d
```

It returns `PASS` and also verifies the point difference
`(1,1,1,1,0,0,0,0,0,0,0)`, every support hole, and the auxiliary-label
histogram `0:1, 1:7, 2:16, 3:10`.

The earlier symbolic obstructions prove at least four rails per shore and
at least eleven reduced labels at four rails.  The certificate therefore
attains both minima.  The support audit also confirms that two positive
long rails cannot repeat at one exterior centre: `a=0,b=2` would require
`t=-6`, outside `|t|<=4`.

## 2. Insertion and star audit

The old insertion word has period eight and the new word period nine, the
minimum legal periods for `q=3`.  Their complete cyclic window lists show
that the new window `123` is `H` and every other old or new window contains
one of the three labels chosen outside the atom ground.  Thus the old
insertion deck misses `A^+`, while the new deck meets `A^+` only at `H`,
which is absent from `A^-`.

For a star core `S-u`, the small and large periods are respectively
`N=M-2` and `N+1=M-1`.  The point image

```text
P_R Phi_u = 1_S - e_u + 3 e_z
```

gives `(Phi_1-Phi_2)+(Phi_1-Phi_3)` the correction
`e_2+e_3-2e_1`.  Added to the insertion image `1_C+3e_1`, this is exactly
`1_H`.  Two copies of the centre potential are required, and the displayed
binomial inequality makes the standard small-deck/big-deck collision union
bound strictly less than one.

## 3. Collision audit

The collision separation is complete for the two final states.

1. Insertion versus atom is handled by the three fresh labels and the sole
   intended owner `H`.
2. Insertion versus star would require one owner to contain disjoint
   `c`-cores `C` and `S-u`; `2c>c+3` for every allowed `c>=4`.
3. Different star cores are signature-disjoint, while the two repeated
   centre decks are packed separately at periods `N` and `N+1`.
4. Atom versus star would require a rank-`(c+3)` owner to contain a union
   of size `2c-1`.  This is impossible for `c>=5`.  At `c=4`, equality
   forces the star toggle window to be exactly the three-set `C_0`; choosing
   those labels nonconsecutive excludes it.  The random packing remains
   available after adding the probability `N/binom(N,3)` of that forbidden
   window.

Hence `Y^-+A^+` and `Y^++A^-` are each unions of nine pairwise
owner-disjoint rails.  Their period sums both equal `4N+44`, and the reserve
algebra

```text
B^+ + R_H = Y^- + A^+,
B^- + R_H = Y^+ + A^-
```

is exact because `A^+=A^-+e_H` and `B^-=Y^+-e_H`.

## 4. External placement and inflation scope

For a fixed core/target and a random injection of the seven auxiliary
labels into an `L`-set, the source's union bound follows from the verified
auxiliary histogram.  Avoiding the positive 34-owner deck automatically
avoids the negative deck, which is its subset.  This protects owners only;
it does not protect q1/q2 resources.

Finally, common-core coning changes ambient rank but not toggle width.  A
toggle label occurs in exactly `q` windows of a legal rail and therefore
cannot serve as an everywhere-present suspension label.  Naive block
concatenation introduces uncancelled seam windows.  The source correctly
claims a q3 base/common reserve, not an all-q recurrence.

## 5. Scope boundary

No immediate-lower, immediate-upper, q2, residence, chronology, or global
component theorem follows from the owner identities.  Those typed and
topological compiler gates remain open.
