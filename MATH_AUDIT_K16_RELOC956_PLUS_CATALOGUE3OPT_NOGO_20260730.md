# K16 flat-relocation plus directed-3opt no-go (2026-07-30)

## Result

The smallest genuinely two-coordinate move in the atom-43389 basin is
rigorously dead:

1. relocate the interior flat from 2031 to 956;
2. apply one retained directed-3opt rethread from the atom-12 catalogue.

The relocated root has complete rank-8 support, complete upper support, and
Hall deficiency 98.  Its canonical alternating witness has 3,836 lower
targets and 3,738 neighbouring physical short cells.

Every one of the 61,317 distinct `(pattern,a,b,c)` tuples was applied to the
relocated chronology and audited from scratch.  This deliberately does not
assume that the old atom family remains closed after relocation.

- 10,739 chronologies pass generalized maximal-envelope replay;
- 10,738 also retain complete upper support;
- none makes the fixed witness non-deficient;
- the best fixed-witness deficiency is 96.

The two fixed-witness record states were then subjected to independent exact
maximum matching.  Both have actual Hall deficiency 102, worse than the
relocated root's 98.

Thus neither coordinate alone nor their smallest composition closes the
compiler:

- fixed-flat directed 3-opt: impossible by the 3,412/3,320 witness;
- single-flat relocation: minimum exact Hall deficiency 98;
- flat relocation to 956 plus one retained directed 3-opt: fixed-witness
  deficiency at least 96, actual record deficiencies 102.

## Scope

This is not a global K16 no-go.  It excludes only the exact composition above.
The next move must leave this basin in a genuinely nonlocal way: a component
hybrid, a newly generated witness-targeted rethread family, multiple flat
changes, or a different parent chronology.

The full audit package is under
`scratch/k16_reloc956_catalogue3opt_nogo_20260730/`; the census source is
`scratch/census_k16_relocated_catalogue_3opt_20260730.cpp`.
