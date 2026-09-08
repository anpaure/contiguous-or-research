# Exact five-type and rank-five-capacity read of the generic catalogue

2026-09-08. One authorized existing-matrix read on h100, under a
one-second outer cap, two-CPU affinity, and a 1 GiB address-space
limit. Runtime: 0.04969807108864188 seconds. No enumeration of new
candidates, optimization, search, or solver restart ran.

The input was the complete saved admissible relaxed catalogue in
`Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908.json`.
The read independently classified every critical target by the
canonical six-class Fano definitions, then inspected all 3024
generic bundles. It found exactly these five types:

| Type | Critical class multiset | Count | DR constituent words | Actual distinct rank-five witnesses covered |
| --- | --- | ---: | ---: | ---: |
| BB | C + 3D + 2B | 1344 | 1 | 1 |
| FF | C + 3D + 2F | 336 | 1 | 1 |
| BF | C + 3D + B + F | 336 | 0 | 0 |
| X | 2C + 4D | 336 | 2 | 2 |
| Y | 2C + 2D + B + F | 672 | 0 | 0 |

A DR word has two distinct first increments and a third increment
equal to one of them. The witness orbits are W_L: value two at zero,
value one on a Fano line L, and zero elsewhere. All seven W_L were
located in the saved full-target incidence list, so the final
column checks actual target coverage as well as the prefix formula.
There were zero unexpected class patterns or capacity violations.
In particular no admissible generic critical edge contains class A
or E.

For counts p,q,r,t,z of BB,FF,BF,X,Y, respectively, a hypothetical
one-full-orbit charge-2368 cover would obey

    p+q+r+2t+2z = 28,
    s+2(p+q+r+t+z) = 41.

The complete self-edge parity description forces

    YYX_self = (22-2p-r-z)/2,
    FFX_self = (26-2q-r-z)/2,
    XXX_self = z-11,

where here Y=A union B and X=D union E, rather than the generic
type names in the table. Nonnegativity gives z>=11. The seven W_L
could receive total coverage capacity at most

    p+q+2t+(z-11) = 17-r-z <= 6,

which is insufficient. The allowed full orbit covers none of the
W_L. This matrix classification verifies the finite input to that
global counting obstruction. Its complete pure classification and
counting proof is preserved in
`Q3_D8_COMPLETE_TRANSLATION_COMPLEMENT_FAMILY_OBSTRUCTION_20260908.md`.
Root, cover_selectors, and ternary_lift independently audited the
full argument, including its explicit critical-collision identities,
and reported PASS. The catalogue read here is corroboration, not a
required computational premise of that later pure proof.

The scope is one allowed full orbit plus 164 short physical rows,
with the exact critical-coverage budget at charge 2368. This ledger
does not apply to a different cost composition with slack on the
critical ranks.

Artifacts:

* `q3_d8_generic_five_type_capacity_read_20260908.py`;
* `Q3_D8_GENERIC_FIVE_TYPE_CAPACITY_READ_20260908.json`.

The JSON includes a literal representative of every type, each
bundle's two shore words, and the witness-orbit IDs that it covers.
