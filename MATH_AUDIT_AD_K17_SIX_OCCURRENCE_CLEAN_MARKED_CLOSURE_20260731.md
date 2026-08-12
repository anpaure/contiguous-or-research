# Independent audit of the six-occurrence clean `K17` marked closure

Date: 2026-07-31  
Status: **PASS**, exact source-relative witness; no marked-path, residual-flow,
upper-service, or compiler conclusion

## 1. Audited claim

Start with the first-occurrence rank-six transversal of the frozen
`6390+45` `K15` parent.  In six distinct repeated rank-six fibres, replace
the retained occurrence as follows.

| rank-six colour | old occurrence | new occurrence |
|---:|---:|---:|
| `0x250e` (`9486`) | `(0,4064)` | `(0,5826)` |
| `0x4076` (`16502`) | `(0,1781)` | `(0,6254)` |
| `0x068b` (`1675`) | `(0,1997)` | `(0,5349)` |
| `0x0b0d` (`2829`) | `(0,2849)` | `(0,6201)` |
| `0x5868` (`22632`) | `(0,1571)` | `(0,4923)` |
| `0x68b0` (`26800`) | `(0,2423)` | `(0,5775)` |

Here `(c,i)` means trace edge `i` of parent component `c`.  The independent
replay verifies directly that both addresses in every row have the displayed
rank-six colour and that the six fibres are distinct.

> **Audited finite theorem.**  The resulting `A/X/Y` macro forest has `1430`
> macro paths and `5005` port-forest components.  Every one of the `165`
> forced nonflat packets remains inside one macro.  The required bank still
> consists of `108` macros in `106` port-forest components, but its full
> component closure now has only `154` macros and `3815` distinct owners.
> Every closure component has no strict internal `D2` positive run below
> three and its adjacent-OR `D3` row has no strict internal positive run
> below four.

Thus the old `32`-run whole-component obstruction is removed by a changed
occurrence transversal.  The result is a clean component **bank**, not yet a
single component path.

## 2. Independent reconstruction

The verifier does not import the census producer.  From the parent cycles it
reconstructs

\[
 C_i=T_i\cap T_{i+1},\qquad Z_i=C_i\cap C_{i+1},
\]

and obtains the exact `Z`-fibre profile

\[
                  1^{3630}2^{1320}3^{55}.
\]

After applying the six substitutions, it rebuilds all child-node incidences:

* a retained trace edge joins consecutive `A` nodes;
* a deleted edge cuts the `A` rail and transfers the two flanks to the `X`
  and `Y` rails; and
* every resulting connected component is traversed from its `X` endpoint to
  its `Y` endpoint.

This gives `1430` literal Johnson paths partitioning all `19305` non-pure-`U`
rank-nine owners.  Their `17875` internal rank-eight intersections are
pairwise distinct.  The missing rank-eight colours are exactly the `6435`
old-coordinate ports.  Consequently the occurrence swaps preserve the
complete owner partition and the lower-`q1` port ledger; they do not silently
duplicate a lower colour.

The final port-degree profile is

\[
                   0^{4016}1^{1978}2^{441},
\]

and the port graph is still a linear forest with exactly `5005` components.
The `106` marked components have macro-size profile

\[
                       1^{77}2^{17}3^5 4^7,
\]

whose weighted sum is `154`.  Their `3815` owner tokens are distinct.

### Direct connector premaster

On this clean bank, the independently rebuilt one-pure-`U` connector
catalogue has

```text
geometric directed arcs       412
residence-clean directed arcs 312
distinct pure-U labels        140
zero-out oriented states       43
zero-in oriented states        43
```

One component is isolated even before all-different owner labels are
imposed:

```text
component index  6
macro             18
endpoint ports    16638, 22835
endpoint owners   82174, 55603
owner tokens      111
```

Consequently the six-swap bank cannot itself be joined into a Hamilton path
using only one direct old-coordinate pure-`U` connector between whole
components.  This is a scoped premaster obstruction, not a return of the
residence obstruction: all component interiors are clean.  A further
occurrence exchange, an optional unmarked-component bridge, or an
incidence-changing socket can still remove it.

### Exact optional-component escape

The same independent replay exhausts every intact internally clean unmarked
forest component as a bridge out of component `6`.  The unmarked bank is

```text
unmarked components                    4899
isolated rank-eight port components    4016
nontrivial macro components             883
internally D2/D3-clean nontrivial       801
nontrivial with D2 debt                   82
nontrivial with D3 debt                    0
```

Root the bridge at either orientation of component `6`, use an intact
unmarked component in either orientation, and end at an oriented different
marked component.  One pure-`U` owner connects each side.  Reversal-equivalent
bridges are counted once by always placing component `6` on the left.  The
complete ledger is

```text
direct one-U clean exits                   0
geometric two-U chains                   172
chains with U1=U2 (invalid)                9
geometric chains with distinct U1,U2     163
residence-clean distinct-U bridges       110
```

The `110` accepted alternatives use `100` distinct ordered `U` pairs and
`98` distinct `U` labels.  These are alternatives, not a simultaneously
selected family; the audit JSON records the complete label- and pair-load
profiles.  Of the accepted bridges, `76` use an isolated port component and
`34` use a nontrivial component.

The minimum optional size is therefore zero macros and zero non-`U` owners.
One concrete bridge is

\[
  55603\;--\;22843\;--\;6587\;--\;72107,              \tag{2.1}
\]

where the first owner is the orientation-zero exit of marked component `6`,
the last owner is the orientation-one entry of marked component `86`, and
the two middle owners are distinct pure-`U` owners.  Their three lower
intersection colours are respectively

\[
                         22835,quad6459,quad6571.       \tag{2.2}
\]

The middle colour `6459` is an isolated unmarked port component.  Direct
literal replay of (2.1) with the two adjacent component caps has no strict
`D2` run below three and no strict `D3` run below four.

If zero-macro port components are disallowed, the smallest nontrivial bridge
uses one macro and six non-`U` owners:

```text
isolated component orientation 1, exit owner/port 82174 / 16638
U owners                                      20734, 11509
optional macro                                941 (reversed)
optional endpoint ports                       20726, 11381
right marked component/orientation            94 / 0
right entry owner/port                         44273 / 11505
```

Thus the isolated vertex is not a genuine socket obstruction once intact
unmarked components are admitted.  Incorporating (2.1) changes the exact
neutral ledger: the marked bank temporarily contains `107` old forest
components (the `106` marked components plus isolated port `6459`) and needs
`106` pure-`U` connectors to become one path, leaving `4899` components and
`4899` pure-`U` owners for the complement.  Palette, connectivity, all other
connector choices, and common-cap compatibility remain to be solved jointly.

## 3. Prefix replay

Applying the six rows in the displayed order gives the following literal
ledger.

| swaps applied | marked closure macros | closure owners | bad components | `D2` bad | `D3` bad |
|---:|---:|---:|---:|---:|---:|
| 0 | 190 | 3970 | 6 | 32 | 0 |
| 1 | 178 | 3917 | 5 | 20 | 0 |
| 2 | 162 | 3843 | 4 | 8 | 0 |
| 3 | 160 | 3836 | 3 | 6 | 0 |
| 4 | 158 | 3829 | 2 | 4 | 0 |
| 5 | 156 | 3822 | 1 | 2 | 0 |
| 6 | 154 | 3815 | 0 | 0 | 0 |

Every row is reconstructed from the changed occurrence map, rather than
read back from the producer's objective fields.

## 4. What the result now reduces to

Because the marked closure is internally clean, it can be passed to the
component-path master without the earlier sixteen internal seam cuts.  The
direct whole-component/one-`U` face first needs the isolated component above
to acquire a legal socket.  A successful enlarged stage must then choose

1. orientations and an order for the `106` marked components;
2. `105` distinct pure-`U` connector owners, with their exact two rank-eight
   incidences and local `D2/D3` transition tests;
3. a residual completion on the other `4900` pure-`U` owners;
4. quotient connectivity, so the marked bank and its complement form the
   required two contiguous phases; and
5. upper/deep provider preservation and one common-cap compiler.

The component-neutral count is exact: joining `106` components consumes
`105` of the `5005` pure-`U` owners and leaves `4900` components and `4900`
owners for the residual completion.  This count is not an existence proof.

The previous frozen `5810`-owner three-path witness belongs to the original
first-occurrence forest.  Its atom numbers, endpoint ports, and two
non-Johnson trace interfaces are not a certificate for this six-swap forest.
The connector catalogue must be regenerated on the new `154`-macro bank.

## 5. Exact scope corrections

The six-row witness is existential.  It does **not** prove that six occurrence
swaps are necessary.  The producer exhausts all `1430` single swaps and all
pairs from its `50` strict-improving single-move alphabet.  Its triple layer
contains `1100` targeted extensions, and depths four through six form one
greedy exact-addition chain.  Hence neither full multi-swap optimality nor a
five-swap no-go follows.

The census JSON's final scope sentence says that no combinations of two or
more swaps are covered; that sentence is stale relative to the pair, triple,
and greedy fields now present.  Moreover its stored payload hash does not
match the current JSON body:

```text
stored payload    ebcdb6ee80c1b33f52bd3a3535c21709be9584eb45fc9e29330999f04e5e76a6
recomputed body   b0af46e4baef08fdfa5719f60008c9f1e0e3a7ef3f21f636bb78ef8376b3f9ef
```

The independent result therefore authenticates the six moves against the
raw parent and forced catalogue and relies on the census only to identify
the six addresses.  No claim is made about the changed upper-provider load,
upper/deep shadows, residual `b`-flow, connectivity, residence at future
component joins, common cap, or a length-`B(17)` word.

## 6. Frozen audit artifacts

```text
scratch/audit_ad_k17_six_occurrence_clean_closure_20260731.py
scratch/ad_k17_six_occurrence_clean_closure_20260731.audit.json
```

The JSON includes every prefix ledger, the final component profiles, and
hashes of all three inputs.  Its status is

```text
PASS_AD_INDEPENDENT_K17_SIX_OCCURRENCE_CLEAN_CLOSURE
```
