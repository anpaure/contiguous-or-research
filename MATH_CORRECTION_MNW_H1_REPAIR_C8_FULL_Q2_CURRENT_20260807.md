# Correction: the positive-H1 repair C8 has three unit q2 negatives

**Date:** 2026-08-07  
**Method:** exact four-owner turn replay and inverse-pair exhaustion; no
computation or search  
**Status:** authoritative correction to Section 4 of
`MATH_THEOREM_MNW_POSITIVE_B8_H0_EXACT_AND_H1_SINGLE_OWNER_GATE_20260807.md`.
The incidence-phase and C8-uniqueness statements there remain valid.  The
claim that its q2 support loss is represented by only `L_0` is false.

## 1. The four lower owners

The unique alternating C8 has lower owners, in cyclic order,

```text
O  =1011000011
B1 =1001001011
B2 =1001010011
B3 =1101000011
```

and changes their selected pairs as follows:

\[
\begin{array}{c|c|c}
\text{owner}&\text{old pair}&\text{new pair}\\ \hline
O  &\{2,6\}&\{6,7\},\\
B1 &\{3,5\}&\{5,6\},\\
B2 &\{5,7\}&\{2,5\},\\
B3 &\{6,7\}&\{3,7\}.
\end{array}                                         \tag{1.1}
\]

Therefore the four turn changes are

\[
\begin{array}{c|c|c}
O  &1111010011&1011011011\\
B1 &1011101011&1001111011\\
B2 &1001111011&1101110011\\
B3 &1101011011&1111001011.
\end{array}                                         \tag{1.2}
\]

The intermediate target cancels.  The complete current is

\[
\boxed{
\begin{aligned}
\partial_2C_8={}&
 [1011011011]+[1101110011]+[1111001011]\\
&-[1111010011]-[1011101011]-[1101011011].
\end{aligned}}                                      \tag{1.3}
\]

## 2. All three negatives are unit providers

The exact inverse-pair lists are

\[
\begin{array}{c|c|c}
\text{target}&\text{inverse pairs}&\text{load}\\ \hline
1111010011&(2,6)&1,\\
1011101011&(3,5)&1,\\
1101011011&(6,7)&1.
\end{array}                                         \tag{2.1}
\]

The C8 removes precisely those three occurrences, at `O,B1,B3`.
The gamma--alpha pair, the closed endpoint packet, and positive `H0` do
not alter any target in (2.1).  Hence all three become absent immediately
after the C8.

## 3. Direct positive H1 does not restore the middle target

After the C8, positive H1 is literally alternating.  Its contextual
selected mates are not the naive prefixed base mates.  Its three owner
rows telescope to

\[
 \boxed{
 \partial_2H_1
 =[1111001011]+[1011010111]
  -[1111000111]-[1011011011].}                      \tag{3.1}
\]

In particular `1011101011` is absent from (3.1).  The support-safe face
`H_{L_0}` restores `1111010011`, but it does not restore either
`1011101011` or `1101011011`.

Thus, after the sequence

```text
closed endpoint packet -> positive H0 -> repair C8
-> safe L0 face -> positive H1,
```

the two named q2 holes still present are

\[
                         1011101011,qquad1101011011. \tag{3.2}
\]

No claim about later phase-repair faces is included here.

## 4. Scope

The correction concerns q2 multiplicity only.  The C8 remains the unique
literal phase repair at the bad H1 owner, and its vertex/status row remains
correct.  Any later theorem must use the full current (1.3), not only its
first negative term.
