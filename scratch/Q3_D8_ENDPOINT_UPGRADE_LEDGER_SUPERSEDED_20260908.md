# Endpoint-upgrade ledgers, superseded by the affine fractional obstruction

2026-09-08. Pure partial analysis by cover-selectors. No computation.
The broader exact lower bound2856 in
Q3_D8_AGL_COUPLED_ENDPOINT_EXACT_FRACTIONAL_OBSTRUCTION_20260908.md
now excludes both proposals below, including configurations beyond
the restricted short-pool ledger recorded here.

Upgrading an A-containing self short orbit to full changes its
critical triple A+B+D to A+B+D+E_H. It adds one rank-seven target
orbit E_H and its reflected rank-nine orbit, costs16, and covers
one new rank-five witness W_H via C_5 times the zero shore.
The resulting bank has eight full and160 short physical rows,
charge2384, and128 rank-seven orbit occurrences for127 demands.

A mixed endpoint upgrade of a generic R/T bundle replaces the R
constituent's four short rows by lower-endpoint rows (ranks0..7),
and their reflected T partners by upper-endpoint rows (ranks1..8).
It also costs16 and adds exactly E_H at rank seven and its reflection
at rank nine. It covers W_H through the R constituent's C_5 times
zero. Choosing the opposite orientation gives no such witness bonus.

If all other short bundles remain in the original distinct-critical
pool, let delta denote the unique excess critical orbit, and use
p,q,r,t,z for the five generic types in the complete-family proof.
Both upgrades have even total incidence on Y union F. Thus delta
cannot belong to Y or F. Individual Y parity requires r+z even.
For either upgrade, charging the added endpoint orbit explicitly
gives

    number of XXX self triples = z-11-delta_C,
    total W_L capacity <=18-r-z.

Here delta_C is one if the excess lies in C, and zero otherwise.
Nonnegativity gives z>=11+delta_C. Since r+z is even, r+z>=12,
so at most six of the seven witnesses can be covered in this
restricted retained-pool setting.

This calculation did not classify newly admissible generic bundles
with one internal critical repetition. That dependent analysis was
stopped when the broader2856 dual arrived. No impossibility claim
about those bundles is inferred from this partial ledger; they are
instead covered directly by the independently audited affine-endpoint
fractional lower bound.
