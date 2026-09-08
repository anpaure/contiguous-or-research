# Bounded RunPod portfolio for the k=15 PBBS orbit-trade lane

Date: 2026-07-27

The canonical PBBS factor at `k=15` has all lower and upper sliding shadows,
but 73 components and 90 physical depth-three residence defects.  Full
`Z_15` symmetry forces load three on the two size-five rank-nine colour
orbits, so the exact search deliberately requires q1 coverage rather than
the false cap-two condition.

The current staged CNF

```text
k15_pbbs_z15_q2_d100.cnf
```

selects one `Z_15` orbit choice per lower necklace, preserves q1 and both q2
coverages, and changes at most 100 of the 429 PBBS choices.  It does not yet
certify one component, voltage coprime to 15, residence three, or deeper
shadows; those are imposed/audited in an exact lazy loop after a raw model.

Ten independent 1800-second Kissat runs were launched on the three CPU pods:

| pod label | seeds |
|---|---|
| amber | 1009, 1013, 1019, 1021 |
| rose | 1103, 1109 |
| purple | 1201, 1213, 1217, 1223 |

A raw SAT model is only a coherent q1/q2 2-factor.  It must be decoded,
subtour-cut to one quotient cycle, checked for voltage coprime to 15,
checked for forward (and, for the `15 -> 16` lift, dual) residence, and
audited at every shadow depth.  `UNKNOWN` has no mathematical force.

A second, cheaper staging wave uses the q1-only distance-100 formula
`k15_pbbs_z15_q1_d100.cnf`.  Ten 900-second runs (seeds 1301, 1303, 1307,
1319, 1409, 1423, 1451, 1453, 1459, and 1471) seek a low-component
chronology before both q2 sides are reintroduced.  Such a model is only a
seed: it does not by itself preserve the deeper PBBS tower.
