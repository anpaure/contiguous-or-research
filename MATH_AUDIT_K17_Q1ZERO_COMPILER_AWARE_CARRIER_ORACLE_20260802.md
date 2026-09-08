# Audit: K17 q1-zero compiler-aware carrier oracle

**Date:** 2026-08-02  
**Status:** exact finite two-phase projection oracle and a complete
32-endpoint calibration.  This is a transported lower-state projection, not
a depth-three source, state-balanced compiler, or universal word.

## 1. Frozen semantics

The lower object is the authenticated `round047` target table.  It partitions
all `65,535` nonempty targets of rank at most eight into `24,310` strict chains
with histogram

```text
length 1/2/3 = 0/7395/16915.
```

Before owner transport its exact four-flag short-reset projection has

```text
hard heads = 16898
matching   = 16898
deficiency = 0
zero heads = 0.
```

The authenticated inputs are

```text
target table SHA  95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735
projection SHA    2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a
universal y map   80980012d7b1449c8ce3932e77ee7e5e47f5d6eb6f18d219687358cbd024355a
```

For a decoded connected augmented-lollipop carrier, the oracle derives its
two canonical perfect root-to-owner phases.  It transports every frozen
chain without changing its ID, target list, length, or root, replacing only
its owner by the selected owner in that phase.  For each transported phase it
then independently rebuilds the complete hard-head graph and emits:

- maximum matching and exact deficiency;
- every zero-degree hard head;
- the exact alternating Hall shore;
- the total edge count and graph FNV hash;
- an independent target-table/factor replay.

The robust carrier score is

\[
  (D(F),Z(F))=
  \left(\max_{p\in\{0,1\}}d_p(F),
        \max_{p\in\{0,1\}}z_p(F)\right).             \tag{1.1}
\]

A compiler-aware descent from the current parent requires a strict carrier
potential decrease and componentwise nonincrease of `(D,Z)`.  Both literal
phases remain in the artifacts; taking only the better phase is invalid.

The runner is
`scratch/run_k17_q1zero_compiler_projection_oracle_h100_20260802.sh`
(SHA `82f907c6e0b73e8c6542932c3055d0646a1b061d0c2cbce74074eaf2664e4fbc`).
It verifies every input hash, uses a private staging directory, retains a
read-only failure bundle on any error, and publishes only after both phase
audits pass.  The legacy transport adapter accepts the first four metric rows
of the authenticated full projection report; that literal gate has SHA
`3e3edf236c5cca9e8beb70f2fb3eea3312554ed5caa348482f08b7cf3921e48e`.

## 2. First separation

For the two parents and their best carrier children, the exact results are:

```text
state     (R,H,Phi)       phase-0 (def,zero)   phase-1 (def,zero)   robust
P_A       1921,1694,5536       71,51                70,55            71,55
C2        1919,1686,5524       72,55                76,58            76,58

P_B       1922,1693,5537       65,47                75,58            75,58
C1        1920,1682,5522       64,48                63,51            64,51
```

`C1` repairs the robust projection while improving the carrier: worst
deficiency drops `75 -> 64` and worst zero heads drop `58 -> 51`.  `C2`
improves `Phi` but worsens both robust compiler coordinates and is rejected.

The more aggressive eight-circuit endpoint `C3=(1914,1670,5498)` is
upper-closed (zero old-target losses and twelve repairs in both openings),
but its transported phases are `(80,60)` and `(76,59)`.  It is therefore
also rejected.  This is a literal example where carrier-only optimization
moves away from the lower projection.

The first projection root is

```text
/home/amodo/or15/work/root_k17_q1zero_upper_closed_20260802/
  compiler_projection_phi5522_v2_20260802/
```

The `C1` manifest and score SHAs are respectively
`5fe2cddd896a9e7c0ab74a02add1ea4891860461fad8068c723063cd185b77e9`
and
`9d10178d84172c2349bbf63f3abcabcbf7fe2961322784c7f4f72943bc65d774`.

## 3. Complete 32-endpoint bank

The carrier-side bank contains 32 diverse endpoints of popcount one through
eight.  Every endpoint has:

- negative `Phi` relative to `C1`;
- connected passive replay;
- all frozen guards and q1 rows;
- exact two-opening upper containment with zero losses.

Its manifest, row table, and hard-result SHAs are

```text
d4be34cf78f1299c69ef3d5ccddce0c7d01f6ef8b7b94a80cd49c59ed30f100a
3039c70e414350df170b2e5d59b9b798052256daa67dc23e4437bed61be39170
d505dac857ad6082d0b521cbbe02535b60744df1d3d68e28961ccecd5b09b589
```

All 64 transported phase graphs were rebuilt exactly.  Only two of the 32
endpoints are compiler-nonworsening:

```text
mask   (R,H,Phi)       phase-0 (def,zero)   phase-1 (def,zero)   robust
8      1919,1681,5519       64,49                60,45            64,49
128    1919,1682,5520       63,49                61,46            63,49
```

Neither dominates the other in `(Phi,D,Z)`: mask 8 has lower `Phi`, while
mask 128 has lower robust deficiency.  Since the immediate search target is
`D<50`, mask 128 is the appropriate compiler-deficiency parent.

The mask-8 manifest/score SHAs are

```text
232a41d3227cd4e24480412a96ebcc918c62c50848cd6491ad4021c32ea4c880
8c8f22f768a248228a034b06da666b0938b81874eff7beede8b7c4dbff91e0ab
```

and the mask-128 SHAs are

```text
fe85546184d32977b2c3495fbdf2e81cc04ba9b3f17657221516288005d4c4ff
e0dfe22b80a0b5b9bfe6d83944583385b7831255b6f375778407189ad67d9047
```

The independent selector
`scratch/select_k17_q1zero_compiler_pareto_20260802.cpp`
(source SHA
`21248c5c7c20bdec7c0b62a361aa95a9a96f91dbde8297f249b70d268d2a860b`)
reports

```text
PASS_K17_Q1ZERO_COMPILER_PARETO candidates=32 admissible=2 pareto=2
```

The complete score table has SHA
`2bec53f4e3607162e681d65d31557260ec51ca08e38673e2cc644b33782a63ee`
at

```text
/home/amodo/or15/work/root_k17_q1zero_upper_closed_20260802/
  compiler_projection_bank32_20260802/compiler_pareto.tsv
```

Every per-candidate directory retains both Hall shores and both zero-head
lists in the same table schema used by the K17 global Benders compiler.

## 4. Second-generation descent

A 16-seed portfolio from the mask-128 and mask-8 parents deduplicates to
eleven literal endpoints.  Exact two-phase replay finds the new
compiler-deficiency record

```text
state          (R,H,Phi)       phase-0 (def,zero)   phase-1 (def,zero)   robust
mask-128       1919,1682,5520       63,49                61,46            63,49
M128_s7        1918,1681,5517       57,46                59,49            59,49
```

Thus one upper-closed singleton lowers `Phi` by three, preserves robust zero
heads, and lowers robust deficiency by four.  An independent literal
missing-set comparison gives zero losses and one repaired target in both
openings.  The authenticated identifiers are

```text
model SHA                 37a160f2b3f02839fcd9621dccb42cce43a0297016cdf050ded742baa6f84748
carrier audit SHA         6d9ad281b710a6ece767b7267982ee1d9acb1424b2e3c43851fa82b27bd18e6e
self comparison audit     4f8b37d00cef6948c902967d88677c163669aadc041a6cf464673207862eff03
missing-list SHA          940e0b38a1206b1e091bb2fd670b9b6d5b6b7bb0b74dd0881efcac9b94b91968
projection manifest SHA   7a00dca80329386277df665e96cecdd9302ff924ca513f8a0646f99aa66254bb
projection score SHA      fcfa3311c90cfee1eaeeca153bf9c92348ef40dba32c4fda5ffd54822190bffb
```

A sibling at the same `Phi`, `M128_s4`, has robust score `(62,48)` and is
retained as the zero-head Pareto endpoint.  From the first compiler-scored
parent `P_B`, robust deficiency has now fallen

```text
75 -> 64 -> 63 -> 59,
```

while every promoted step has negative `Phi` and exact upper containment.

## 5. Exact compound census from mask 128

All 1,023 subsets of a ten-circuit catalogue were materialized from the
mask-128 endpoint.  Of these, 583 are connected negative-`Phi` carrier
endpoints.  A popcount-stratified bank of 48 endpoints was then frozen and
authenticated.  Every bank member has zero literal upper-target losses in
both openings.  The bank manifest, hard comparison table, and bank table
have SHAs

```text
ee93646f89c659584e7806afbcb4498ac90e39f1b6977bba2ad56aceabd2348d
f870581a6b7b93e53d360bfad5f0a3c0e90aa37aee6f0e0575c49e362b3f5caa
1c725a16996098595eb5c06397251bc27596ddb8e5fe38c3798769691d56a102
```

All 96 transported phase graphs were rebuilt exactly.  The bank did not
cross the target `D<50`.  It did, however, find a compound endpoint which
strictly improves the carrier coordinates at the existing compiler record:

```text
state       (R,H,Phi)       phase-0 (def,zero)   phase-1 (def,zero)   robust
M128_s7     1918,1681,5517       57,46                59,49            59,49
mask 17     1917,1679,5513       57,46                59,49            59,49
```

The mask-17 model, passive carrier audit, projection manifest, and score
SHAs are

```text
c00386f2a3b0b06afab08b727261391f581beb89e27bfcfba2b2109ff5cb3286
f38da093d57e48d9a82d475f280c8d3ab0dc6b5255dca0f22b8091b6f2b42f4c
8edaca031df96adebd5dee310937c6f6303bb016c3f8b4bf3607f89f2095647c
b9bd0f61cad0ee68d184265165f2dcfc796262d18b0f3a04c8afdbaefe0328c5
```

An orthogonal endpoint, mask 113, has lower robust zero-head count at the
cost of two deficiency units:

```text
mask 113    1915,1677,5507       61,46                58,43            61,46
```

It is retained as a second parent because it exposes a distinct compiler
gradient.  The aggressive all-ten endpoint reaches carrier
`(1912,1667,5491)` but regresses to robust `(66,50)`.  This independently
confirms that compound carrier improvement is not monotone in compiler
quality.

The exact projection root is

```text
/home/amodo/or15/work/root_k17_q1zero_upper_closed_20260802/
  compiler_projection_bank48_m128_20260802/
```

The frozen 48-row aggregate and its 100-entry projection manifest have SHAs

```text
5932452e1514734cc8601c5cd0cb64d1347468a9c1e87971e8d0bab71dcf89c6
d3636119a8bbece7730eb79f760123d51187ff509f67fbdbb9d1d644a549a9da
```

## 6. Third-generation zero-head descent

A fresh sixteen-single portfolio was launched from mask 17 and mask 113.
Exact two-phase replay found a new compiler-aware record:

```text
state       (R,H,Phi)       phase-0 (def,zero)   phase-1 (def,zero)   robust
mask 17     1917,1679,5513       57,46                59,49            59,49
M17_s3      1916,1678,5510       56,42                59,45            59,45
```

Thus `M17_s3` preserves the record robust deficiency, lowers robust zero
heads by four, and lowers `Phi` by three.  It strictly dominates every
previous authenticated endpoint having robust deficiency 59.  It does not
dominate every point of the full three-coordinate frontier: for example,
mask 113 retains lower `Phi=5507` with the worse robust score `(61,46)`.

The model, search audit, packet, projection manifest, and projection score
SHAs are

```text
d9ec3d9b5f06670292edaa5da7e0f2e925215266ca941c6a7e5870fd217c98d6
ec5aa9cc846a9a65f68da08a242367bb87bfb1334e82700d3b488b53be7e790b
eba3558653689c2a7d4d718e364241c09f9d9f729ce8e1eb849cd9c56a0dc9c3
7821e7a117e149a1b6d999041b794a1faae78dda0849e312b4baa6bfd770e2c2
0734ae9ea14b0d49054b296ff6b62039d9a09ec4fb2e6ebefb6686c23fe0f7f4
```

An independent circuit reconstruction exhausts the unique nonempty subset
and its unique order, rebuilds the terminal model byte-for-byte, verifies
all guards, q1, connectivity, and both-opening containment, and reports

```text
PASS_INDEPENDENT_K17_PARETO_PROMOTABLE_COMPOSITION
strict_subsets=1 valid_orders=1 phi_delta=-3
```

The independent package manifest and audit SHAs are

```text
8ef2c6fc134e2044431def527e8d1da6c2f5f23dc026e81ae4fb2d0bc639209c
fec4788e3432fc2b3aa1215dfdf2cef5151bc300313f11972222231436c3aa1b
```

at

```text
/home/amodo/or15/work/root_k17_q1zero_upper_closed_20260802/
  audit_m17_s3_independent_v2_20260802/
```

The complete sixteen-single aggregate and its manifest have SHAs

```text
6b1e5d19ddf00cf115827390effbc5ca1d291b06155c4bf22845e57de02d054c
04e95b3495ffbec39b6c8756c8cf1d273fcff1744099b4fcf74be2a23b6ebb09
```

A separately hard-certified 23-member compound cross-bank from mask 17
contains no improvement: its best robust deficiency is 61 and its best
robust zero-head count is 48.  This is a frozen no-improvement census, not
an UNSAT statement outside the bank.  The carrier-bank manifest, hard table,
bank table, projection aggregate, and projection manifest SHAs are

```text
a6d77f11ef946b39cd62296b8726d17c32b3e1453e28cd9f265b2cc74c3ba1ce
dbba2f4b0c5c262aee48dd1ab75267f6bbec744b91a1c08526b6c79469b174e2
8e552f2d281a88e7d4c41a659f7f760dd561df946064d98a328bb7c9ea870ec5
dbd35350f27d320ada59493813c59af2403bb2c79d517678244f9955cd714202
751d5215c788c3ca793f5a088296c1714aaa63007f4fc2bb58744ebbdfb2f15f
```

## 7. Exact scope

Proved for this finite bank:

- literal carrier guards, q1, topology, and both-opening containment;
- exact transport of one defect-zero target partition onto both carrier
  owner phases;
- exact maximum matching, deficiency, zero heads, and Hall shore in every
  transported projection reported above, including all 96 graphs in the
  48-endpoint compound bank;
- the two-member robust compiler-aware Pareto frontier above.

Not proved:

- that the transported table is a literal depth-three source chronology;
- same-role flag/state balance or occurrence-labelled source consistency;
- residence zero or arbitrary-upper completion;
- DM/common-cap compilation or a length-`24,313` word;
- that repeated compiler-aware descent reaches zero.

The result changes the search objective rather than closing K17.  Future
packet banks must be separated by `(Phi,D,Z)` before promotion; a carrier-only
record is not a compiler-aware record.
