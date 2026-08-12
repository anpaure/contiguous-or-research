# A factorable nineteen-switch prefix for the thirteen missing `k=11` masks

## 1. Outcome

The saturated `369+93` portal blueprint is false, but its weaker local idea
does survive.  There is an explicit nonzero 22-entry prefix whose first 19
triple windows are distinct rank-six masks, whose first 18 quadruple windows
are distinct rank-seven masks covering all twelve rank-seven omissions of the
current length-465 factor, and whose nineteenth quadruple window is the sole
rank-eight omission `958`.

The final three entries shared with a possible continuation have OR `550` of
rank four.  Hence there is no local rank obstruction to making the next
quadruple window a new rank-six central witness.

This is a certified prefix, not a length-465 solution.  The unresolved task is
to extend it by 443 further rank-six quadruple witnesses while covering all
lower and upper masks.

## 2. Why thirteen consecutive rank-seven portals cannot suffice

For shortened rank-six triples `P_i=R_3(i)`, consecutive portal colours are

\[
 U_i=R_4(i)=P_i\cup P_{i+1}.
\]

If `U_i` and `U_(i+1)` are distinct rank-seven masks, they share the rank-six
mask `P_(i+1)`.  Thus consecutive portal colours are adjacent in `J(11,7)`.
The twelve missing rank-seven masks do not form one path in their induced
Johnson graph; three are isolated and the graph is disconnected.

Using Johnson distance as the metric, the shortest walk visiting all twelve
required colours and ending at a colour capable of sharing a rank-six facet
with `958` has 16 edges.  No factorable rank-six lift exists among the
metric-optimal walks checked exhaustively by
`scratch/k11_portal_color_path.cpp`.  Allowing one additional Johnson edge
produces the certificate below: 18 ordinary rank-seven portals, hence 19
shortened rank-six triples, followed by the `958` seam.

## 3. Exact certificate

The rank-seven portal-colour sequence is

```text
493 941 956 892 1884 1878 1990 1735 1763
1267 251 127 607 671 1694 1946 1438 1468
```

It contains the twelve missing rank-seven masks and six bridge colours.  A
rank-six lift is

```text
489 429 940 828 860 1876 1862 1734 1731 1251
243 123 95 543 670 1690 1434 1436 444
```

Consecutive rank-six masks have exactly the displayed rank-seven unions.  Its
coordinate incidence words have no internal one-run shorter than three, so it
has a delay-two factor.  One sparse factor, chosen to leave a small right
boundary state, is

```text
489 425 424 300 780 788 836 1604 1602 1218 195
99 83 27 30 538 154 1176 408 4 32
```

Appending `514` gives

\[
 R_4(19)=408\cup4\cup32\cup514=958.
\]

The state retained for the next quadruple window is

\[
 4\cup32\cup514=550,
 \qquad |550|=4.
\]

Every entry above is nonzero.

## 4. Exact status

Proved and machine checked:

1. the 19 triple windows are distinct rank-six masks;
2. the first 18 quadruple windows are distinct rank-seven masks;
3. all twelve missing rank-seven targets occur;
4. the nineteenth quadruple window is `958`;
5. the sparse factor is exact and has no empty entry;
6. the continuation core has rank four.

Not proved:

1. a continuation through the other 443 rank-six masks;
2. preservation or reconstruction of all ranks one through five;
3. complete upper-shadow coverage after the continuation;
4. existence of a full length-465 universal array in this branch.

The certificate is `k11_partial_switch_prefix_q19.txt`; the independent-format
verifier is `k11_partial_switch_prefix_verify.cpp`.  The generator/search
record is `scratch/k11_portal_color_path.cpp`.
