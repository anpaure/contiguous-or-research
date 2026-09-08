# Corrected positive-support certificate for the canonical \(K=11\) cyclic four-windows

Date: 2026-07-25

## 1. The theorem

Write \(A=10\).  For the canonical Chung--Feller/MSW exact wreath
factor on \([0,10]\), let \(\mathscr S_4\) be the family of sets which
occur as four consecutive coordinates in one of its forty-two cyclic
orders.  Then

\[
 \boxed{\mathscr S_4=\binom{[0,10]}4\setminus\mathcal H'},
 \qquad |\mathscr S_4|=330-32=298,
\]

where the corrected hole family is

\[
\begin{aligned}
\mathcal H'_0={}&
0147,0169,0237,0247,0256,0257,0258,025A,\\
&0347,0369,0469,0478,0479,047A,0489,0569,
\end{aligned}
\tag{1.1}
\]

and

\[
\begin{aligned}
\mathcal H'_+={}&
1269,1369,136A,1459,1469,1478,1479,158A,\\
&2369,247A,257A,2589,258A,259A,267A,347A.
\end{aligned}
\tag{1.2}
\]

Here, for example, `258A` means \(\{2,5,8,10\}\).  In particular,
the old entry \(127A\) is supported (in E8), while \(347A\) is absent.

This note supplies the previously missing **positive-support converse**.
It is a finite symbolic expansion of the displayed A--E recursion, not a
program output or an unsupported cardinality tally.

## 2. Exact source data and the two corrected E entries

For

\[
 \pi=(0,r_1,r_2,r_3,r_4,r_5,i_1,i_2,i_3,i_4,i_5),
\]

the eleven four-windows are the four sets

\[
0r_1r_2r_3,\qquad 0i_3i_4i_5,\qquad
0i_4i_5r_1,\qquad 0i_5r_1r_2
\tag{2.1}
\]

and the seven sets

\[
r_1r_2r_3r_4, r_2r_3r_4r_5, r_3r_4r_5i_1,
r_4r_5i_1i_2, r_5i_1i_2i_3, i_1i_2i_3i_4,
i_2i_3i_4i_5.
\tag{2.2}
\]

The complete \(T_3,T_4\) tables and the five A--E substitutions are in
`K11_CANONICAL_CYCLIC4_SUPPORT_CLASSIFICATION_20260725.md`, Sections 1--2.
The A and B orders are displayed in
`K11_CANONICAL_SUPPORT_CORRECTION_AB_AUDIT_20260725.md`, Sections 3--4;
the C and D orders and all their windows are displayed in
`K11_PORT_FOREST_HALL_ATTACK_20260725.md`, Section 6; and the E expansion
is displayed in
`K11_CANONICAL_CYCLIC4_SUPPORT_HAND_AUDIT_20260725.md`, Section 4.

There are two corrections to the printed E occurrence table.  They follow
immediately by reading the corresponding cyclic orders:

\[
\begin{array}{c|c|c|c}
\text{row}&\text{cyclic order}&\text{positions }2,3,4,5&
\text{correct set}\ \hline
E13&(0,2,6,4,3,1,A,8,7,5,9)&(6,4,3,1)&1346,\\
E14&(0,2,4,5,3,1,A,8,6,7,9)&(4,5,3,1)&1345.
\end{array}
\tag{2.3}
\]

Thus the printed `1236` and `1235` in those two cells are transcription
errors.  All other E cells follow from the uniform formula

\[
 (0,10-b_1,10-b_2,10-b_3,10-b_4,1,
       10,10-a_1,10-a_2,10-a_3,10-a_4)
\tag{2.4}
\]

for \(a_1a_2a_3a_4\mid b_1b_2b_3b_4\in T_4\).

## 3. Full A--B expansion (the formerly implicit part)

The following table is obtained by applying (2.1)--(2.2) to the nineteen
displayed A--B orders.  It is included so that the positive-support audit
does not hide 209 occurrences behind the phrase “direct substitution.”
Each row contains its eleven cyclic four-windows, in cyclic start order.

```text
A1  0135 1357 3579 2579 2479 2469 2468 468A 068A 018A 013A
A2  0135 1358 3578 2578 2478 2467 246A 469A 069A 019A 0139
A3  0136 1356 3569 2569 2459 2489 2478 478A 078A 017A 013A
A4  0138 1368 3568 2568 2456 245A 249A 479A 079A 0179 0137
A5  0136 1367 3567 2567 2457 245A 248A 489A 089A 0189 0139
A6  0134 1347 3479 2379 2679 2569 2568 568A 058A 018A 014A
A7  0134 1348 3478 2378 2678 2567 256A 569A 059A 019A 0149
A8  0146 1346 3469 2349 2389 2789 2578 578A 057A 015A 016A
A9  0145 1345 3459 2359 2389 2689 2678 678A 067A 017A 014A
A10 0168 1468 3468 2346 234A 239A 279A 579A 0579 0157 0158
A11 0148 1458 3458 2345 235A 239A 269A 679A 0679 0167 0178
A12 0167 1467 3467 2347 234A 238A 289A 589A 0589 0159 0156
A13 0145 1457 3457 2357 237A 236A 268A 689A 0689 0189 0149
A14 0146 1456 3456 2356 235A 238A 278A 789A 0789 0179 0149

B1  0125 1257 1579 4579 3479 3469 3468 368A 068A 028A 012A
B2  0125 1258 1578 4578 3478 3467 346A 369A 069A 029A 0129
B3  0126 1256 1569 4569 3459 3489 3478 378A 078A 027A 012A
B4  0128 1268 1568 4568 3456 345A 349A 379A 079A 0279 0127
B5  0126 1267 1567 4567 3457 345A 348A 389A 089A 0289 0129
```

Every entry can be checked by sliding a four-place window along its row;
for example A8 is
\((0,1,6,4,3,9,2,8,7,5,A)\), so its first three entries in the table
are \(0146,1346,3469\).

## 4. Lexicographic positive-support partition

For a zero-containing target, fix its least positive coordinate \(a\) and
write

\[
 U^0_a=\{0abc:a<b<c\le A\}.
\]

For a zero-avoiding target, fix its least coordinate \(a\) and write

\[
 U^+_a=\{abcd:a<b<c<d\le A\}.
\]

Substituting the A--B table above and the displayed C--D--E tables into
(2.1)--(2.2), and taking an ordinary set union within each disjoint
bucket, gives the following exact complement table.

### 4.1 Buckets containing zero

\[
\begin{array}{c|c|l|c}
a&|U^0_a|&U^0_a\setminus\mathscr S_4&
|U^0_a\cap\mathscr S_4|\\ \hline
1&36&0147,0169&34\\
2&28&0237,0247,0256,0257,0258,025A&22\\
3&21&0347,0369&19\\
4&15&0469,0478,0479,047A,0489&10\\
5&10&0569&9\\
6&6&--&6\\
7&3&--&3\\
8&1&--&1
\end{array}
\tag{4.1}
\]

This table is particularly easy to audit without any tallying software.
For instance, the entire \(a=2\) bucket is witnessed as follows:

\[
\begin{array}{c|l}
23&0234,0235,0236,0238,0239,023A\\
24&0245,0246,0248,0249,024A\\
25&0259\\
26&0267,0268,0269,026A\\
27&0278,0279,027A\\
28&0289,028A\\
29&029A.
\end{array}
\tag{4.2}
\]

Every entry in (4.2) occurs literally in the full row tables; the six
unwritten possibilities are precisely the six holes on the \(a=2\) line
of (4.1).  The other seven lines are checked in the identical triangular
way.  Their supported counts are

\[
34+22+19+10+9+6+3+1=104.
\tag{4.3}
\]

For completeness, here is the full zero-containing positive certificate,
grouped by the first two positive coordinates.  Thus no positive witness
is hidden in the counts of (4.1).

```text
01: 0123 0124 0125 0126 0127 0128 0129 012A
    0134 0135 0136 0137 0138 0139 013A
    0145 0146 0148 0149 014A
    0156 0157 0158 0159 015A
    0167 0168 016A
    0178 0179 017A
    0189 018A
    019A
02: 0234 0235 0236 0238 0239 023A
    0245 0246 0248 0249 024A
    0259
    0267 0268 0269 026A
    0278 0279 027A
    0289 028A
    029A
03: 0345 0346 0348 0349 034A
    0356 0357 0358 0359 035A
    0367 0368 036A
    0378 0379 037A
    0389 038A
    039A
04: 0456 0457 0458 0459 045A
    0467 0468 046A
    048A 049A
05: 0567 0568 056A 0578 0579 057A 0589 058A 059A
06: 0678 0679 067A 0689 068A 069A
07: 0789 078A 079A
08: 089A
```

This is certificate (4.4a).

### 4.2 Buckets avoiding zero

\[
\begin{array}{c|c|l|c}
a&|U^+_a|&U^+_a\setminus\mathscr S_4&
|U^+_a\cap\mathscr S_4|\\ \hline
1&84&1269,1369,136A,1459,1469,1478,1479,158A&76\\
2&56&2369,247A,257A,2589,258A,259A,267A&49\\
3&35&347A&34\\
4&20&--&20\\
5&10&--&10\\
6&4&--&4\\
7&1&--&1
\end{array}
\tag{4.4}
\]

For a compact positive witness audit, refine (4.4) by its first two
coordinates.  The number of supported suffix pairs in the successive
prefixes is

\[
\begin{array}{c|rrrrrrr|c}
\text{least }1&12&13&14&15&16&17&18&\text{sum}\\ \hline
\text{supported}&27&19&11&9&6&3&1&76
\end{array}
\tag{4.5}
\]

and

\[
\begin{array}{c|rrrrrr|c}
\text{least }2&23&24&25&26&27&28&\text{sum}\\ \hline
\text{supported}&20&14&6&5&3&1&49,
\end{array}
\tag{4.6}
\]

while the remaining prefix counts are

\[
\begin{array}{c|rrrrr|c}
\text{least }3&34&35&36&37&38&\text{sum}\\ \hline
\text{supported}&14&10&6&3&1&34,\\[1mm]
\text{least }4&45&46&47&48&&\\[-1mm]
\text{supported}&10&6&3&1&&20.
\end{array}
\tag{4.7}
\]

For least coordinates \(5,6,7\), all \(10,4,1\) possibilities occur.
The omitted suffixes in (4.5)--(4.7) are exactly those displayed in
(4.4): one omission in prefix 12, two in 13, four in 14, one in 15;
one in 23, one in 24, four in 25, one in 26; and one in 34.

Equations (4.5)--(4.7) are not merely aggregate counts: the complete A--B
list in Section 3 and the complete C--D--E lists cited in Section 2 give
an explicit row witness for each suffix pair.  For example, prefix 25 has

\[
 2567,2568,2569,256A,2578,2579
\tag{4.8}
\]

and no other supported member; prefix 34 has

\[
\begin{gathered}
3456,3457,3458,3459,345A,\\
3467,3468,3469,346A,\\
3478,3479,3489,348A,349A,
\end{gathered}
\tag{4.9}
\]

with \(347A\) the unique omission.  These are the two most collision-prone
lines; all other lines are literal complete triangular ranges with the
holes in (4.4) deleted.

Here is the full zero-avoiding positive certificate, again grouped by its
first two coordinates:

```text
12: 1234 1235 1236 1237 1238 1239 123A
    1245 1246 1247 1248 1249 124A
    1256 1257 1258 1259 125A
    1267 1268 126A
    1278 1279 127A
    1289 128A 129A
13: 1345 1346 1347 1348 1349 134A
    1356 1357 1358 1359 135A
    1367 1368
    1378 1379 137A
    1389 138A 139A
14: 1456 1457 1458 145A
    1467 1468 146A
    147A
    1489 148A 149A
15: 1567 1568 1569 156A
    1578 1579 157A
    1589 159A
16: 1678 1679 167A 1689 168A 169A
17: 1789 178A 179A
18: 189A
23: 2345 2346 2347 2348 2349 234A
    2356 2357 2358 2359 235A
    2367 2368 236A
    2378 2379 237A
    2389 238A 239A
24: 2456 2457 2458 2459 245A
    2467 2468 2469 246A
    2478 2479
    2489 248A 249A
25: 2567 2568 2569 256A 2578 2579
26: 2678 2679 2689 268A 269A
27: 2789 278A 279A
28: 289A
34: 3456 3457 3458 3459 345A
    3467 3468 3469 346A
    3478 3479 3489 348A 349A
35: 3567 3568 3569 356A
    3578 3579 357A
    3589 358A 359A
36: 3678 3679 367A 3689 368A 369A
37: 3789 378A 379A
38: 389A
45: 4567 4568 4569 456A
    4578 4579 457A
    4589 458A 459A
46: 4678 4679 467A 4689 468A 469A
47: 4789 478A 479A
48: 489A
56: 5678 5679 567A 5689 568A 569A
57: 5789 578A 579A
58: 589A
67: 6789 678A 679A
68: 689A
78: 789A
```

This is certificate (4.9a).

Therefore

\[
 76+49+34+20+10+4+1=194
\tag{4.10}
\]

zero-avoiding targets occur.

Combining (4.3) and (4.10) gives 298 positive targets.  The independently
audited A--E avoidance proof gives all 32 members of (1.1)--(1.2) zero
occurrences.  Since \(298+32=330\), the two inclusions meet and prove the
theorem.

## 5. Why the multiplicity ledger is not re-certified here

The old multiplicity note states

\[
 (m_0,m_1,m_2,m_3)=(32,149,134,15).
\]

That statement cannot be retained after the fresh row audit.  In addition
to the hole swap \(127A\leftrightarrow347A\), the two E transcription
errors (2.3) change the coefficient multiset.  More importantly, several
members of the old displayed “multiplicity-three” list have only two
literal witnesses in the corrected A--E rows (for example \(1234\) occurs
in E5 and D5).  Thus the old histogram was not a consequence of the
correct row table.

There is, however, a useful structural cap.  Every cyclic occurrence of a
four-set \(C\) is contained in the two adjacent cyclic five-windows
\(C\cup\{x\}\).  The canonical wreath factor owns every five-set exactly
once, so distinct occurrences of \(C\) consume disjoint pairs among its
seven five-supersets.  Hence

\[
 \boxed{\operatorname{mult}(C)\le\lfloor7/2\rfloor=3.}
\tag{5.1}
\]

A fresh coefficient-by-coefficient audit is still required to state the
correct values of \(m_1,m_2,m_3\).  Nothing in the support theorem above
uses the suspended histogram.

## 6. Exact status

Proved, by the explicit A--E expansion:

* \(\mathcal H'\) is the complete complement of the cyclic-four support;
* the support has exactly \(298\) members;
* the lower and complementary-upper cyclic-four ledgers therefore both
  start at support \(298\);
* the old multiplicity histogram is invalid and must not be used.

The physical port-forest construction remains separate: this certificate
does not choose cuts, heads, seams, or a 36-edge directed forest.
