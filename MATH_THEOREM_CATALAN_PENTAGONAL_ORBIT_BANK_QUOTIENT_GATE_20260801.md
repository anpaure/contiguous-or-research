# Pentagonal orbit banks: the exact quotient/graphic gate and the `m<=8` census

Date: 2026-08-01  
Status: exact central reduction and exact finite census.  The same
pentagonal orbit bank closes the frozen `m=6` and `m=8` factors.  No all-`m`
existence theorem for the required selector/bank pair is claimed.

## 0. Outcome

A full-rotation invariant cap-two factor does **not** necessarily contain
one locally prepared target-plus-two-donor packet.

* The frozen `m=3` factor has two physical cycles but none of its `96`
  formal target completions even has both companion old diamonds.
* The frozen `m=6` factor has twelve cycles.  It has companion phases and
  available new endpoints, but no single packet has the five-component
  role of the local prepared-host theorem.

Thus local packet occurrence is not a consequence of exact palettes and
rotation symmetry.

The correct invariant object is a **rotation-closed bank**.  This gives a
new unification:

* at `m=6`, the twelve endpoint-feasible pentagonal packets form one
  `C_12` orbit with pairwise disjoint old and new supports; toggling the
  whole orbit changes `36` edges and turns the `12 x C4` factor into a
  `Cat_6=132`-path forest;
* at `m=8`, the sixteen packets form one `C_16` orbit with disjoint old and
  new supports; toggling the whole orbit changes `48` edges and turns the
  unique `C32` factor into a `Cat_8=1430`-path forest.

At `m=8` one packet already suffices.  At `m=6` the bank succeeds even
though no member is individually in the five-component sufficient state.
This is a genuine collective topology effect.

## 1. Exact orbit-bank criterion

Use the notation of
`MATH_THEOREM_CATALAN_FULL_ROTATION_ORBIT_FACTOR_AND_M6_COLLAR_FINISH_20260801.md`.
Let `A_m` be the outer-simple diamond orbits under `C_(2m)`.  A selector
`x in {0,1}^{A_m}` develops to a physical edge set `F(x)`.

For one pentagonal packet `p`, let `O_p` and `N_p` be its old and new
three-diamond phases.  Let

\[
 \widehat O_p=\bigcup_{g\in C_{2m}}gO_p,
 \qquad
 \widehat N_p=\bigcup_{g\in C_{2m}}gN_p.             \tag{1.1}
\]

Call the bank **clean** when its distinct old phases have disjoint diamond
supports, its distinct new phases have disjoint diamond supports, and no
outer resource is repeated between different bank members.  In that case
the bank is a union of complete diamond orbits.

### Theorem 1.1 (rotation-bank equivalence)

Fix a clean packet bank and a selector `x` containing every orbit of
`widehat O_p`.  Replace those old orbits by the new orbits and call the
result `x^p`.  Then `x^p` has the same exact lower and upper necklace
margins as `x`.

It is an exact invariant Catalan linear forest if and only if

\[
 \sum_\alpha q_\alpha(X)x^p_\alpha\le2
                  \qquad(X\in\tbinom{[2m]}m),        \tag{1.2}
\]

and

\[
                         F(x^p)\in\mathcal I(M_{\rm gr}), \tag{1.3}
\]

where `M_gr` is the graphic matroid on the middle-layer Johnson graph.

#### Proof

Each packet cyclically permutes three upper colours over the same three
lower colours.  Cleanliness makes these identities disjoint, and rotation
closure makes them unions of orbit rows.  Thus the two exact quotient
margins are unchanged.  Equation (1.2) is exactly the literal middle
degree-two condition.  Equation (1.3) is exactly absence of a physical
cycle.  A graph satisfying both is a spanning linear forest; orienting its
paths gives injective tail and head maps.  Every implication is reversible.
\(\square\)

Equivalently, the simultaneous search is the exact integer system

\[
\begin{cases}
 x\in B(\mathcal P_L)\cap B(\mathcal P_U),\\
 Qx\le2,\\
 \widehat O_p\subseteq F(x),\\
 Qx^p\le2,\\
 F(x^p)\in\mathcal I(M_{\rm gr}).
\end{cases}                                           \tag{1.4}
\]

Here `P_L,P_U` are the two partition matroids encoding one orbit per lower
and upper necklace, and `Q` is the stabilizer-weighted literal load matrix.
This is not ordinary two-matroid intersection: it couples two partition
bases, weighted capacities, a prescribed exchange, and a graphic
independence row.

## 2. Exact fixed-support Hall form

There is a genuine Hall reduction once the physical support has already
paid cap and topology.

Let `R^+` be a rotation-invariant middle-layer linear forest, and let
`Gamma(R^+)` be the bipartite occurrence graph whose shores are lower and
upper necklaces and whose edges are the outer-simple edge orbits contained
in `R^+`.  Fix a set `J` of pairwise shore-disjoint new packet orbits.

### Theorem 2.1 (rooted quotient Hall criterion)

There is an invariant exact outer matching inside `R^+` containing every
orbit in `J` if and only if

1. the forced orbits in `J` have distinct lower and upper shores; and
2. after deleting those shores, the residual occurrence graph satisfies

\[
              |N_{\Gamma(R^+)-J}(S)|\ge |S|
 \quad\text{for every residual lower-necklace set }S. \tag{2.1}
\]

#### Proof

The forced orbits consume their lower and upper necklace vertices.  Every
remaining selected orbit has unit margins because it is outer-simple, and
the physical cap and graphic row were already paid by `R^+`.  What remains
is exactly a perfect matching in the residual bipartite occurrence graph;
(2.1) is Hall's theorem.  \(\square\)

To obtain an actual old/new packet pair, the inverse replacement
`R^-=R^+-widehat N_p+widehat O_p` must also satisfy the old cap rows.  Thus
the exact support-first route is:

\[
 \boxed{
 R^+\text{ forest}
 +\text{ rooted residual Hall}
 + R^-\text{ cap two}.
 }                                                       \tag{2.2}
\]

This is the clean quotient condition requested by the finite evidence.
Without a fixed physical support, the weighted cap rows prevent a reduction
to Hall alone.

## 3. Exact finite census

The frozen factors give the following packet ledger.

| `m` | raw cycles | formal target options | companion old phase | available endpoints | single prepared role | clean rotation bank | bank result |
|---:|---:|---:|---:|---:|---:|:---|:---|
| 2 | 0 | 0 | 0 | 0 | 0 | none | already forest |
| 3 | 2 | 96 | 0 | 0 | 0 | none | this frozen factor remains cyclic |
| 4 | 0 | 0 | 0 | 0 | 0 | none | already forest |
| 5 | 0 | 0 | 0 | 0 | 0 | none | already forest |
| 6 | 12 | 9,600 | 48 | 12 | 0 | one `C_12` orbit | `132` paths, 0 cycles |
| 7 | 0 | 0 | 0 | 0 | 0 | none | already forest |
| 8 | 1 | 18,816 | 32 | 16 | 16 | one `C_16` orbit | `1,430` paths, 0 cycles |

The zero row at `m=3` is not an existence obstruction.  Exhausting all
six invariant cap-two selectors at `m=3` finds four invariant forests and
two selectors with two cycles.  Similarly:

\[
\begin{array}{c|c|c}
m&\text{all invariant cap-two selectors}&\text{forest selectors}\\\hline
2&2&1\\
3&6&4\\
4&5060&2728.
\end{array}                                             \tag{3.1}
\]

So the cyclic frozen `m=3` choice should simply be replaced.  At `m=6,8`,
the rotation-bank theorem repairs the displayed choices exactly.

### Why this does not prove the all-`m` theorem

The census proves neither of the following alternatives uniformly:

1. an invariant forest selector exists outright; or
2. a nonforest selector contains a clean pentagonal orbit bank satisfying
   (1.2)--(1.3).

It does show that those two alternatives cover every audited dimension
through eight.  The sharp next central conjecture is therefore:

> **Forest-or-pentagonal-bank dichotomy.**  For every `m`, the weighted
> necklace selector has either a graphic-independent solution, or a
> solution with one clean pentagonal orbit bank whose switched selector is
> graphic-independent.

This is strictly weaker than requiring every invariant factor to contain a
packet, which the `m=3` and `m=6` rows refute.

## 4. Mechanical replay

Run

```text
python3 scratch/audit_catalan_pentagonal_host_gate_m2_m8_20260801.py
```

It reconstructs the frozen factors, enumerates every formal packet through
every cycle edge, evaluates literal endpoint and component roles, groups
endpoint-feasible packets into rotation orbits, performs every clean
simultaneous bank toggle, and exhausts all invariant selectors at
`m=2,3,4`.  It writes

```text
scratch/catalan_pentagonal_host_gate_m2_m8_20260801.audit.json
```

with status `PASS_PENTAGONAL_HOST_CENSUS_M2_M8`.

Frozen identifiers:

```text
audit script SHA-256 5348604109f0000066ca775f5af9015e70ad636d897dfcc6ddccc22aec1f0334
audit JSON SHA-256   387dbd4ad1e4414f6b1a762dda40900893422b81f9f820f848ed58028be1e7ff
payload SHA-256      0cb5932125cf9b3618d1055a8049bd1f2f4d0d78a884418b383432c279dba271
```
