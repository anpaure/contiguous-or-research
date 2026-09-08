# Canonical K=11 support correction: recursion, symmetry, and the A--B audit

## 1. The detected transcription error

The previously recorded hole list cannot be literal.  The eighth
class-E row, obtained from

\[
R_4\mid I_4=4217\mid6538,
\]

is

\[
\pi_{E8}=(0,4,5,7,2,1,10,6,8,9,3).
\]

Its entries in positions (3,4,5,6) are

\[
(7,2,1,10),
\]

so the old claimed hole ({1,2,7,10}) is supported.

No row formula needs correction.  The corrected-hole candidate is

\[
\mathcal H'=
\bigl(\mathcal H_{\rm old}\setminus\{1,2,7,10\}\bigr)
\cup\{3,4,7,10\}.
\tag{1.1}
\]

The reason for the replacement is the exact reflection symmetry proved
in Section 5 below: ({1,4,7,8}) is paired with
({3,4,7,10}), while the supported set
({1,2,7,10}) is paired with the supported set
({1,4,9,10}).

## 2. Representative recursion checks

For a Dyck word (w=UpDq), with (h=|p|+2), the defining recursion is

\[
\Phi(w)=[h]\Vert[h-v:v\in\Phi(\operatorname{rc}(p))]
\Vert[1]\Vert[h+v:v\in\Phi(q)].
\]

Odd entries form (I), even entries form (R).  Hence

\[
I=[h]\Vert(h-R(\operatorname{rc}(p)))\Vert(h+I(q)),
\]

\[
R=(h-I(\operatorname{rc}(p)))\Vert[1]\Vert(h+R(q)).
\tag{2.1}
\]

The base row is (T_1=1\mid2).  The two (T_2) rows are

\[
13\mid24,qquad21\mid43.
\]

Equation (2.1) gives the first two (T_3) rows from the (r=0)
case,

\[
135\mid246,qquad143\mid265,
\]

the (r=1) row

\[
215\mid436,
\]

and the two (r=2) rows

\[
421\mid653,qquad231\mid645.
\]

As a representative nontrivial (T_4) check, take the (r=2)
case, the (T_2) row (13\mid24), and the unique (T_1) row.
Here (h=6), and (2.1) gives

\[
R=(6-(2,4),1,6+1)=4217,
\]

\[
I=(6,6-(1,3),6+2)=6538.
\]

Thus the row used in the correction is genuinely
(4217\mid6538).

## 3. Full class-A row and template audit

The fourteen class-A orders are

```text
A1   0 1 3 5 7 9 2 4 6 8 10
A2   0 1 3 5 8 7 2 4 6 10 9
A3   0 1 3 6 5 9 2 4 8 7 10
A4   0 1 3 8 6 5 2 4 10 9 7
A5   0 1 3 6 7 5 2 4 10 8 9
A6   0 1 4 3 7 9 2 6 5 8 10
A7   0 1 4 3 8 7 2 6 5 10 9
A8   0 1 6 4 3 9 2 8 7 5 10
A9   0 1 4 5 3 9 2 8 6 7 10
A10  0 1 8 6 4 3 2 10 9 7 5
A11  0 1 8 4 5 3 2 10 9 6 7
A12  0 1 6 7 4 3 2 10 8 9 5
A13  0 1 4 5 7 3 2 10 6 8 9
A14  0 1 4 6 5 3 2 10 8 7 9
```

Write a (T_4) row as

\[
(a_1,a_2,a_3,a_4)\mid(b_1,b_2,b_3,b_4).
\]

Substitution in the eleven cyclic-four templates gives the following
four zero-containing types:

\[
\begin{aligned}
Z_1&=\{0,1,2+a_1,2+a_2\},\\
Z_2&=\{0,2+b_2,2+b_3,2+b_4\},\\
Z_3&=\{0,1,2+b_3,2+b_4\},\\
Z_4&=\{0,1,2+a_1,2+b_4\},
\end{aligned}
\tag{3.1}
\]

and the seven nonzero types

\[
\begin{aligned}
N_1&=\{1,2+a_1,2+a_2,2+a_3\},\\
N_2&=\{2+a_1,2+a_2,2+a_3,2+a_4\},\\
N_3&=\{2,2+a_2,2+a_3,2+a_4\},\\
N_4&=\{2,2+a_3,2+a_4,2+b_1\},\\
N_5&=\{2,2+a_4,2+b_1,2+b_2\},\\
N_6&=\{2,2+b_1,2+b_2,2+b_3\},\\
N_7&=\{2+b_1,2+b_2,2+b_3,2+b_4\}.
\end{aligned}
\tag{3.2}
\]

The only old claimed zero-holes containing (1) are (0147) and
(0169).  Comparing the required pairs with the first-two-(R),
last-two-(I), and ((a_1,b_4)) projections in (3.1) rules out
(Z_1,Z_3,Z_4).  Every other old claimed zero-hole omits (1), so it
could only be (Z_2).  Across the fourteen rows, the nonzero triples
in (Z_2) are

```text
6810, 6910, 7810, 7910, 8910, 5810, 5910,
5710, 6710, 579, 679, 589, 689, 789.
```

None is an old claimed zero-hole.

For the old claimed nonzero holes, the sets containing both (1) and
(2) cannot occur in any A template.  A claimed set containing (1)
but not (2) could only be (N_1).  After subtracting two, the seven
required triples are

\[
147,148,237,247,256,257,368.
\]

The first-three-(R_4) sets are

\[
135,136,134,146,145,125,126,124,123,246,236,245,235,234,
\]

so none occurs.  A claimed set containing (2) but not (1) could
only be (N_3,N_4,N_5,N_6).  The seven required triples are

\[
147,258,358,367,368,378,458.
\]

The four relevant projection families are respectively

\[
\begin{aligned}
\{a_2a_3a_4\}:{}&357,356,347,346,345,157,156,127,137,124,123,125,135,134,\\
\{a_3a_4b_1\}:{}&257,256,237,234,235,457,456,167,167,128,138,128,158,138,\\
\{a_4b_1b_2\}:{}&247,245,267,238,238,347,345,567,467,178,178,168,148,168,\\
\{b_1b_2b_3\}:{}&246,248,256,278,268,346,348,356,456,578,478,678,468,568.
\end{aligned}
\tag{3.3}
\]

Again there is no match.  Finally, (347(10)) has neither (1) nor
(2), so only (N_2) or (N_7) is possible.  Subtracting two gives
the four-set (1258), which is neither an (R_4)-set nor an
(I_4)-set in the displayed (T_4) table.  Thus A supplies

\[
14\cdot11=154
\]

occurrences, but zero occurrences of any old claimed hole or of
(347(10)).

## 4. Full class-B row and template audit

The five class-B orders are

```text
B1  0 2 1 5 7 9 4 3 6 8 10
B2  0 2 1 5 8 7 4 3 6 10 9
B3  0 2 1 6 5 9 4 3 8 7 10
B4  0 2 1 8 6 5 4 3 10 9 7
B5  0 2 1 6 7 5 4 3 10 8 9
```

For a (T_3) row (a_1a_2a_3\mid b_1b_2b_3), the four
zero-containing templates are

\[
\begin{aligned}
Z_1&=\{0,1,2,4+a_1\},\\
Z_2&=\{0,4+b_1,4+b_2,4+b_3\},\\
Z_3&=\{0,2,4+b_2,4+b_3\},\\
Z_4&=\{0,1,2,4+b_3\},
\end{aligned}
\tag{4.1}
\]

and the nonzero templates are

\[
\begin{aligned}
N_1&=\{1,2,4+a_1,4+a_2\},\\
N_2&=\{1,4+a_1,4+a_2,4+a_3\},\\
N_3&=\{4,4+a_1,4+a_2,4+a_3\},\\
N_4&=\{3,4,4+a_2,4+a_3\},\\
N_5&=\{3,4,4+a_3,4+b_1\},\\
N_6&=\{3,4,4+b_1,4+b_2\},\\
N_7&=\{3,4+b_1,4+b_2,4+b_3\}.
\end{aligned}
\tag{4.2}
\]

Direct substitution of

\[
135\mid246, 143\mid265, 215\mid436,
421\mid653, 231\mid645
\]

shows that no template in (4.1) is an old claimed zero-hole.  Among
the nonzero candidates, (1269) and (127(10)) could only have type
(N_1); they would require the first-two-(R_3) sets (25) and
(36), whereas the actual sets are (13,14,12,24,23).  A claimed
set containing (1) but not (2) could only be (N_2), and direct
comparison with the five (R_3)-sets excludes all seven candidates.
Every remaining old claimed nonzero hole contains (2), while
(N_3,ldots,N_7) do not.  Thus no old claimed hole occurs.

For (347(10)), only (N_4,N_5,N_6,N_7) could apply.  The required
pair (36) occurs in none of the last-two-(R_3),
((a_3,b_1)), or first-two-(I_3) projections, and (N_7) cannot
contain the literal (4).  Hence B supplies

\[
5\cdot11=55
\]

occurrences, but again zero occurrences of any old claimed hole or of
(347(10)).

## 5. Exact reflection invariance

Let (u,v) be Dyck words of semilengths (a,b).  The recursive
definition implies the concatenation identity

\[
\Phi(uv)=\Phi(u)\Vert(2a+\Phi(v)).
\tag{5.1}
\]

This follows by induction on the number of primitive factors of (u).
Using (5.1), a second induction gives

\[
\boxed{
\Phi(\operatorname{rc}(w))
=(2m+1)-\operatorname{rev}\Phi(w)
}
\tag{5.2}
\]

for every Dyck word (w) of semilength (m).  For a primitive word
(w=UpD), (5.2) is an immediate substitution in the defining
recursion and the induction hypothesis for (p).  For a concatenation
(w=uv), use
(operatorname{rc}(uv)=\operatorname{rc}(v)\operatorname{rc}(u)),
(5.1), and the two induction hypotheses.

Because (Phi(w)) has even length, reversal swaps odd and even
positions.  If (pi(w)=(0,R(w),I(w))) and

\[
\sigma(0)=0,qquad \sigma(x)=11-xquad(1\le x\le10),
\]

then (5.2) gives

\[
R(\operatorname{rc}(w))=\sigma(\operatorname{rev}I(w)),
\]

\[
I(\operatorname{rc}(w))=\sigma(\operatorname{rev}R(w)).
\]

Therefore

\[
\pi(\operatorname{rc}(w))
=\sigma\bigl(0,\operatorname{rev}I(w),
                 \operatorname{rev}R(w)\bigr),
\tag{5.3}
\]

which is (sigma) applied to the reversed cyclic order (pi(w)).
Reverse-complement permutes the 42 Dyck words.  Hence the canonical
factor, and in particular its cyclic-four support and multiplicities,
is invariant under (sigma).

For example, the supported E8 window (127(10)) is carried to the
supported E4 window (149(10)).  Conversely, the missing color
(1478), once independently certified, forces the missing color
(347(10)).

## 6. Corrected splice witness

The invalid (127(10)) row in the old backward-splice table is
replaced by (347(10)).  In B3,

\[
\pi=(0,2,1,6,5,9,4,3,8,7,10),
\]

take the five-window

\[
(4,3,8,7,10).
\]

Deleting (eta=8) in position two gives

\[
\{3,4,7,10\}.
\]

The entering coordinate is (t=0), so the candidate head is
(0347(10)).  Its unique canonical owner is the D3 window

\[
(7,3,10,0,4).
\]

Here the old tail coordinate (r=10) is in position two and (t=0)
is in position three.  The position-three head criterion requires
only that (r) not occupy position zero, so the forward test passes.

This is a complete local physical splice certificate.  It does not by
itself prove the global six-path fusion.

## 7. Scope of the audit

The A--B calculation above is complete: all (209=154+55) cyclic-four
occurrences from those classes have been accounted for symbolically,
and none belongs to the provisional corrected hole set
(mathcal H').  Reflection invariance is also exact.

This note alone does **not** certify that (mathcal H') is the complete
hole set.  That final assertion additionally requires the analogous
C--D--E template audit, including the explicit E8 correction.  Until
those ledgers are combined, the statements “32 holes” and “support
298” should be regarded as provisional rather than reused as inputs.

For the corrected internal-deletion graph, the complete class-B right
degrees (deletion positions (1,2,3) inside each cyclic five-window)
are:

| row | position 1 hits | position 2 hits | position 3 hits | degree |
|---|---|---|---|---:|
| B1 | (1479) | (0257,1459) | (025(10)) | 4 |
| B2 | (1478) | (0258,0369) | (347(10)) | 4 |
| B3 | (1459) | (0256,1469,347(10)) | (1269) | 5 |
| B4 | -- | -- | (347(10)) | 1 |
| B5 | (1269,347(10)) | (0169) | -- | 3 |

Thus the class-B maximum corrected right degree is exactly (5).
