# Independent audit of the corrected canonical cyclic-four support

Date: 2026-07-25

## Verdict

The theorem in
`K11_CORRECTED_CYCLIC4_POSITIVE_SUPPORT_CERTIFICATE_20260725.md` is
correct:

\[
 \mathscr S_4=\binom{[0,10]}4\setminus\mathcal H',
 \qquad |\mathscr S_4|=298.
\]

This audit used only the displayed recursive (T_3,T_4) data and direct
sliding of four-place windows along the forty-two canonical orders.  No
search, SAT instance, or computational enumeration was used.

## 1. Audit of all forty-two rows

The class sizes are

\[
 14+5+4+5+14=42.
\]

For every displayed order I independently slid a four-place cyclic window
through all eleven starting positions.

* All (14\cdot11=154) entries in the A table are correct.
* All (5\cdot11=55) entries in the B table are correct.
* All (4\cdot11=44) entries in the C table are correct.
* All (5\cdot11=55) entries in the D table are correct.
* All (14\cdot11=154) entries in the corrected E table are correct.

In particular, the literal E13 and E14 orders are

\[
 E13=(0,2,6,4,3,1,A,8,7,5,9),
 \qquad
 E14=(0,2,4,5,3,1,A,8,6,7,9).
\]

Their windows starting at the second nonzero position are respectively

\[
 \{6,4,3,1\}=1346,
 \qquad
 \{4,5,3,1\}=1345.
\]

Thus `1236` and `1235` were indeed transcription errors.  I found no
other error in the corrected forty-two-row cyclic-window expansion.

## 2. Lexicographic support audit

The zero-containing four-sets split by least positive coordinate into
buckets of sizes

\[
 36,28,21,15,10,6,3,1.
\]

Direct comparison with the row expansion gives supported counts

\[
 34,22,19,10,9,6,3,1,
\]

whose sum is (104).  The sixteen omitted members are exactly

```text
0147 0169
0237 0247 0256 0257 0258 025A
0347 0369
0469 0478 0479 047A 0489
0569
```

I checked every member of the full positive list (4.4a) against a literal
row occurrence.  For example, the relatively sparse prefixes are covered
by

```text
02: 22 supported members, with the six displayed omissions
04: 10 supported members, with the five displayed omissions
05:  9 supported members, with 0569 omitted
```

and the remaining prefixes agree term-for-term with the certificate.

The zero-avoiding four-sets split by least coordinate into buckets of sizes

\[
 84,56,35,20,10,4,1.
\]

The corrected row expansion gives supported counts

\[
 76,49,34,20,10,4,1,
\]

whose sum is (194).  Refining by the first two coordinates gives exactly

\[
\begin{array}{c|rrrrrrr}
1*&27&19&11&9&6&3&1\\
2*&20&14&6&5&3&1&\\
3*&14&10&6&3&1&&\\
4*&10&6&3&1&&&
\end{array}
\]

for prefixes (12,\ldots,18), (23,\ldots,28),
(34,\ldots,38), and (45,\ldots,48).  The least-(5,6,7)
buckets are complete.  The sixteen omitted members are exactly

```text
1269 1369 136A 1459 1469 1478 1479 158A
2369 247A 257A 2589 258A 259A 267A 347A
```

Every target in the full positive list (4.9a) has a literal occurrence in
one of the forty-two checked rows.  In particular, E8 supplies `127A`,
whereas no row supplies `347A`.

The two positive lists are disjoint by whether they contain zero, and each
is internally repetition-free by its lexicographic buckets.  Therefore

\[
 104+194=298
\]

distinct targets are supported.  Together with the direct absence of the
thirty-two displayed members of \(\mathcal H'\), this proves that
\(\mathcal H'\) is the complete complement, rather than merely a family
of certified holes.

One presentation-only defect was found and repaired during this audit:
the last lines of (4.9a) had compacted all least-(5) targets under the
label `56` and all least-(6) targets under `67`, despite saying the list
was grouped by its first two coordinates.  Splitting those labels into
`56,57,58` and `67,68` changes no target or count.

## 3. Multiplicity-histogram retraction

The retraction in Section 5 is necessary and correct.

* `1236` occurs literally only in D2 and E2 after the E13 correction.
* `1235` occurs literally only in D4 and E4 after the E14 correction.
* `1234`, although present in the old multiplicity-three list, occurs
  literally only in D5 and E5.

Thus the old triple list and hence the old histogram

\[
 (m_0,m_1,m_2,m_3)=(32,149,134,15)
\]

are not certified by the corrected occurrence table and must not be used.
The support theorem does not depend on that histogram.

The cap

\[
 \operatorname{mult}(C)\le3
\]

is valid independently: each occurrence of a four-set consumes the two
adjacent five-supersets, distinct occurrences consume disjoint pairs, and
there are exactly seven five-supersets of a fixed four-set.

## Final status

The corrected support (298), corrected hole family \(\mathcal H'\), and
the lower/upper four-colour support ledgers are independently certified.
Only the obsolete multiplicity refinement remains intentionally
unresolved.
