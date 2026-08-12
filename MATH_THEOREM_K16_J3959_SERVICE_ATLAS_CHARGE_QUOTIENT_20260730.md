# K16 j3959: the 5,166 service blocks quotient to three donor-charge states

Date: 2026-07-30  
Status: **exact finite theorem; scoped to the stable extraction and fixed donor descent**

## Statement

For every authenticated nested service block

\[
M=(V_0,V_1,V_2,4a79,4e39,4d39),
\]

remove the physical occurrences of (V_0,V_1,V_2) and the fixed service
packets from the `j=3959` chronology, preserve the order of all other
occurrences, and append the fixed post-flat service suffix.  There are 5,166
such internally depth-two-resident blocks.

The exact variable-depth deficit census has 5,110 signatures and no carrier.
Its bad-row histogram is

```text
12:3, 13:35, 14:61, 15:191, 16:304, 17:511, 18:665,
19:750, 20:777, 21:666, 22:560, 23:366, 24:194, 25:67, 26:16.
```

Apply to every state the three occurrence-conserving donor moves from the
`12 -> 6 -> 3 -> 2` descent.  Row by row, the number of deficits drops by
exactly ten, and the entire service-block-specific part of the signature is
unchanged.  Consequently the new histogram is the same histogram shifted
by ten:

```text
2:3, 3:35, 4:61, 5:191, 6:304, 7:511, 8:665,
9:750, 10:777, 11:666, 12:560, 13:366, 14:194, 15:67, 16:16.
```

Every one of the 5,166 states retains both residual equations

```text
5e38 -> 5e18, missing 0020,
6a71 -> 6a61, missing 0010.
```

Exactly three blocks attain the minimum:

```text
(ab61, ea61, ca71, 4a79, 4e39, 4d39)
(e361, ea61, ca71, 4a79, 4e39, 4d39)
(eb60, ea61, ca71, 4a79, 4e39, 4d39).
```

Thus the exact deficit-signature quotient reduces the outer search from
5,166 blocks to three.  Merely changing the nested service block cannot pay
either residual charge; the final absorber must internally rethread source
packets or change the service architecture.

## Proof

The C++ census reconstructs all 5,166 blocks from the raw set equations,
constructs the occurrence-labelled chronology for each block, and performs
the complete maximal-envelope replay.  It repeats the census after applying
the three donor moves.

The independent auditor reads the two 5,166-row tables and checks:

1. block labels and order agree row for row;
2. every empty-envelope count is zero;
3. every bad-row count falls by exactly ten;
4. replacing the fixed twelve-row core by the two-row core converts each
   raw signature exactly into its descended signature;
5. both residual equations occur in all 5,166 signatures;
6. the histograms and the three minimum blocks are exactly those above.

This proves the finite classification.  It does not show that every possible
K16 carrier can be put into this extraction order.

## Artifacts

```text
scratch/census_k16_j3959_service_atlas_donor_signatures_20260730.cpp
SHA256 465bd8be5221ed3c3aea677b0f05b4ce3cc6bdbe69bc39e7156fd93afe6377da

scratch/k16_j3959_service_atlas_donor_signatures_20260730/result.tsv
SHA256 24f5f41599df1e4e295dc553bc4103a6ed3cfc21293564523b97a137fa88b1c5

scratch/k16_j3959_service_atlas_donor_signatures_20260730/result2.tsv
SHA256 14aad251f0de792abe03552b5698e978a58d381e2058701a821a6cfe157e0124

scratch/audit_k16_j3959_service_atlas_charge_quotient_20260730.py
SHA256 3c3ccc216021ebe3084521f615caf3f7a4d1f715b03d9cbd7f90b8f79c2b08f4

scratch/k16_j3959_service_atlas_donor_signatures_20260730/charge_quotient.independent.audit.json
SHA256 f5ebf56586b819b1139bdc79e817915b8cb5923e5922c9fa3da4e82ed26b42c2
payload bb36cf41badeae806f251a3f0b2be894e8cda1190187fe88cb626116a58290cd
```
