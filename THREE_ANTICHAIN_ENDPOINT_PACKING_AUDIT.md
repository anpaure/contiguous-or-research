# Audit of `THREE_ANTICHAIN_ENDPOINT_PACKING.md`

## Verdict

Theorems 1 and 2 are valid as necessary endpoint bounds.  The six-cycle
example is a genuine OR realization and disproves global acyclicity for three
antichains.  The finite claims reproduced by the checker pass.

## Proof checks

1. **Endpoint blocks.**  Endpoint injectivity within each antichain makes
   every block rainbow.  Common-endpoint nesting makes its labels a chain.
   A target occurs once on each endpoint side, so the two block collections
   have the asserted vertex capacities.

2. **Bichromatic projections.**  Restricting the selected intervals to any
   two antichains gives exactly the setting of the audited endpoint-forest
   theorem.  A three-colour block projects to one edge for each colour pair;
   it causes no extra degree in a fixed two-colour projection.

3. **Overlap accounting.**  On either endpoint side, adjoining singleton
   blocks gives a partition of all `V` targets.  Its savings are exactly the
   sum of `|B|-1`.  Since at most `n` physical endpoint positions are used,
   the total two-sided saving is at least `2(V-n)`.

4. **Joint incidence identity.**  For size-two and size-three block counts
   `a_2,a_3`, direct expansion gives

   ```text
   3(a_2+2a_3)-(a_2+3a_3)=2a_2+3a_3.
   ```

   The right side is the number of nontrivial target/block incidences and is
   at most `2V`.  This validates the third cap in (2.1).

5. **Two-colour specialization.**  Alternating edge colours on each path
   realizes any linear forest as two matchings.  The matching number of a
   path forest is at least half its edges, validating the Dilworth comparison
   used to show `Lambda_hat_3=lambda`.

## Counterexample check

Direct OR evaluation gives the six labels listed in Section 4.  In each of
the three colour classes the two labels have equal rank and are distinct,
hence incomparable.  The left endpoint pairs are

```text
(A_1,B_1), (C_1,B_2), (C_2,A_2),
```

and the right endpoint pairs are

```text
(C_1,A_1), (B_1,C_2), (A_2,B_2).
```

They form one `C_6`.  Each two-colour restriction has two independent edges,
so there is no conflict with the pair theorem.

## Scope

`Lambda_3` is a relaxation, not a characterization of realizable endpoint
systems.  In particular, Theorem 1 does not claim that all trichromatic
cycles or all pairwise-forest block packings admit compatible global endpoint
orders.  Equation (5.1) evaluates only `Lambda_hat_3`, not the exact
`Lambda_3`.  No improvement to `B(11)` is claimed.

The executable audit is
`scratch/check_three_antichain_endpoint_packing.py`.

