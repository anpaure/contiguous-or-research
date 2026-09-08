# Pentagonal rotations at the protected Catalan connector gate: the first typed-head obstruction

Date: 2026-08-01  
Lane: protected Catalan connector / finite obstruction probe  
Status: complete finite census on the authenticated insured targets at
`(m,h)=(4,1),(5,1),(5,2)`.  No all-dimensional selector theorem is claimed.

## 0. Outcome

Fix the first incidence matching `M0`, every directed incidence of the
insured shortest collar, and one named upper-transparent residual closure.
Enumerate every root-aligned pentagonal `C6` whose three old lower rows occur
off the collar and off the closure.

The complete literal census is

| `(m,h)` | packets | correlated connector PASS | forced protected-head collision |
|---:|---:|---:|---:|
| `(4,1)` | 1 | 0 | 1 |
| `(5,1)` | 11 | 9 | 2 |
| `(5,2)` | 11 | 9 | 2 |

All `18` positive packets admit a reselected second matching which

1. contains the new pentagonal phase and every protected collar incidence;
2. contains the same named residual closure with upper load at least two;
3. is a directed q1-rainbow Hamilton cycle covering every adjacent-upper
   colour; and
4. decomposes after deleting the closure into an upper-exact rooted Catalan
   forest `Q0` and a contracted connector tree `Q1` of graphic rank
   `Cat_m-1`.

Every one of the `23` literal three-edge toggles with the complementary
matching frozen fails head bijectivity.  Correlated reselection is therefore
essential even in the positive rows.

The five negative packets need no SAT certificate.  A new packet incidence
and a protected collar incidence have different lower rows but demand the
same head of the second matching.  This is a typed paired-incidence
obstruction, not an upper-mask deficit.

## 1. Exact finite model

For every lower colour `q`, the authenticated directed Hamilton target gives

\[
                   M_0(q)=\text{tail}(q),\qquad
                   M_1(q)=\text{head}(q).                 \tag{1.1}
\]

The pentagonal formula has three lower rows `L_i`.  Root alignment means
that the endpoint common to the old and new physical edge on row `L_i` is
exactly `M0(L_i)`.  Hence the old-to-new pentagonal rotation is literally a
replacement of three values of `M1`, while preserving its three lower and
three adjacent-upper labels.

Let `P1` be the protected head incidences and let `e_*=(q_*,v_*)` be the
named closure.  The finite search fixes

\[
                 P_1\cup\{e_*\}\cup N_p                 \tag{1.2}
\]

and reselects the remaining values of `M1`.  It requires head bijectivity,
every adjacent-upper colour, and one owner-permutation cycle.  Proper
subtours are separated lazily.  Positive witnesses, rather than solver
claims, are frozen and independently replayed.

Deleting `e_*` from a positive cycle leaves a spanning directed path.  Pick
the three new packet rows first and then one retained occurrence of every
upper colour.  These rows form `Q0`; every subset of the path is acyclic, so

\[
 |Q_0|={2m-1\choose m+1},\qquad
 c(Q_0)=\operatorname{Cat}_m.                            \tag{1.3}
\]

The remaining `Cat_m-1` path edges form `Q1`.  After contracting `Q0`, they
are a tree.  The replay additionally enumerates the full residual connector
occurrence graph.  In every positive row that graph is connected and has
graphic rank `Cat_m-1`; the selected `Q1` is a literal matching-compatible
rank certificate.

## 2. The smallest obstruction

The unique packet on the insured `(m,h)=(4,1)` target has core mask `32`,
ordered labels

\[
                              (4,2,1,3,0),                \tag{2.1}
\]

and old/new second-matching rows

\[
\begin{aligned}
 O&=\{41\mapsto43,\ 42\mapsto58,\ 52\mapsto53\},\\
 N&=\{41\mapsto57,\ 42\mapsto43,\ 52\mapsto54\}.       \tag{2.2}
\end{aligned}
\]

The protected collar already contains

\[
                              50\mapsto54.                \tag{2.3}
\]

Thus (2.2)--(2.3) force two different lower rows to head `54`.  No
completion of the second matching exists.  Notice that the packet's upper
palette is still exactly preserved:

\[
                 \{47,61,62\}_{O}=\{47,61,62\}_{N}.       \tag{2.4}
\]

Therefore scalar palette preservation, old-row disjointness, and
protected-lower disjointness do not imply protected connector eligibility.
The first additional row is literal **head-resource disjointness**.

Owner rank three has no legal insured collar: there are not two distinct
exterior labels for the ternary exterior and rail exterior.  Hence (2.2) is
the smallest legal finite counterexample to the naive rule

> choose any root-aligned pentagonal rotation whose old lower rows avoid the
> protected bank and residual closure.

The other four negative packets have the same form.  Their colliding heads
are respectively `107,94,110,157`; each collision is between one new packet
row and one protected collar row.

## 3. What this says about an absorber

The census separates two notions which cannot be merged.

* A split-letter pivot can recreate a named OR-mask witness by block
  contraction.
* It cannot make two distinct lower incidence rows use the same head in one
  perfect matching.

Consequently a bounded source-letter absorber may pay upper-mask casualties
only after the connector state has passed the typed incidence rows.  For a
pentagonal bank, a proof-safe local eligibility predicate must include both
shore resources, not merely the lower/upper packet palettes:

\[
       \operatorname{head}(N_p)\cap
       \operatorname{head}(P_1\cup\{e_*\})=\varnothing,   \tag{3.1}
\]

apart from literal rows intentionally shared with the same lower colour.
Condition (3.1) is necessary, not asserted sufficient in all dimensions.
The `18` positive finite rows show that once it holds, a global correlated
reselection can repair all unprotected head collisions and recover the full
Catalan connector rank.  They do not give a uniform selector or absorber.

## 4. Reproducibility

Run

```text
python3 scratch/search_o1_pentagonal_rooted_connector_finite_20260801.py
python3 scratch/audit_o1_pentagonal_rooted_connector_finite_20260801.py
```

The search exhausts the displayed root-aligned packet formula on the three
authenticated targets.  The independent audit reconstructs the packet bank,
checks every forced collision directly, and replays every positive cycle,
palette, protected incidence, closure multiplicity, Catalan forest and
contracted connector rank.

Frozen identifiers:

```text
search script SHA-256  cd5244d221890ce440b6bdc541c22ad729063ebc5c5d7ac2b86164a5e9692446
search JSON SHA-256    d35f719f69484bc3907ffe2cce720a30f95a76244b787c5272424c2fa26a7b1d
search payload SHA-256 553546035dc90b564243de6b9850aa6ab3f97f44a9c275991601eb010ae59ba3
audit script SHA-256   aaf118c4b1bbd4402529b358f3cda5775204cb66b82216d6822773ad3f9cb8f5
audit JSON SHA-256     82324deb6f1e94947a9b1413c471d316e26446d9ab1dfe114e094406350eab2e
audit payload SHA-256  b6a034b305f53f56d8d99bff90641e675a65b850c8bbd050dd1192a42ba7535d
```

Replay status:

```text
PASS_PENTAGONAL_ROOTED_CONNECTOR_FINITE_REPLAY
```
