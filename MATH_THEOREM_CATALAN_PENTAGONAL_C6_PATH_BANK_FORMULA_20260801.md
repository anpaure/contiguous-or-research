# The pentagonal `C6`: an all-`m` formula behind the `m=8` cycle finish

Date: 2026-08-01  
Status: exact dimension-uniform local identity and exact graphic criterion.
The frozen `m=8` winner is one instance.  No theorem is claimed that every
all-dimensional necklace factor contains a prepared instance.

## 0. Outcome

The sixteen successful `m=8` exchanges are one `C_16` rotation orbit of a
single algebraic packet.  The packet exists formally for every `m>=3` and,
through one oriented target edge, has exactly

\[
                         (m-1)^2(m-2)                 \tag{0.1}
\]

indexed completions.

It is weaker than the typed ternary Boolean hexagon: it preserves the lower
and upper palettes exactly and preserves cap two after its stated graphic
placement, but it changes two physical middle endpoints.  The resulting
graph is a linear forest and can therefore be oriented with injective tail
and head maps; it does not preserve a previously frozen typed tail/head
bank pointwise.

The exact remaining host theorem is now concrete:

> expose one packet whose target old edge is on a physical cycle, whose two
> other old edges lie on distinct paths, and whose two new-only middle
> vertices are available endpoints of two further path components.

That hypothesis is sufficient to remove the cycle.  Its existence in every
dimension is not proved.

## 1. The five-label packet

Let the ground set have size `2m`, where `m>=3`.  Choose an `(m-3)`-set `S`
and five distinct labels

\[
                         p,q,r,s,t\notin S.           \tag{1.1}
\]

Define three lower colours

\[
\begin{aligned}
 L_0&=S+p+q,\\
 L_1&=S+r+s,\\
 L_2&=S+s+t,
\end{aligned}                                        \tag{1.2}
\]

and three upper colours

\[
\begin{aligned}
 U_0&=S+p+q+s+t,\\
 U_1&=S+p+q+r+s,\\
 U_2&=S+q+r+s+t.
\end{aligned}                                        \tag{1.3}
\]

The containment graph induced by these six outer colours is the cycle

\[
 L_0-U_0-L_2-U_2-L_1-U_1-L_0.                       \tag{1.4}
\]

Let the old and new diamond phases be

\[
 O=\{(L_0,U_0),(L_1,U_1),(L_2,U_2)\},
 \qquad
 N=\{(L_0,U_1),(L_1,U_2),(L_2,U_0)\}.               \tag{1.5}
\]

### Theorem 1.1 (exact two-palette identity)

Every pair in (1.5) is a legal Boolean diamond.  Both phases use each of
the three lower colours and each of the three upper colours exactly once.
Their physical Johnson edges are as follows:

\[
\begin{array}{c|c}
O&
 (S+p+q+s)(S+p+q+t),\\
& (S+p+r+s)(S+q+r+s),\\
& (S+q+s+t)(S+r+s+t)\\ \hline
N&
 (S+p+q+r)(S+p+q+s),\\
& (S+q+r+s)(S+r+s+t),\\
& (S+p+s+t)(S+q+s+t).
\end{array}                                           \tag{1.6}
\]

Within either phase the six displayed physical endpoints are distinct.
The phases share four endpoints.  The two new-only endpoints are

\[
                 G=S+p+q+r,qquad H=S+p+s+t.          \tag{1.7}
\]

#### Proof

The containments in (1.4) are read directly from (1.2)--(1.3), and every
upper-minus-lower difference has size two.  Thus each pair is a legal
diamond and (1.5) is a cyclic reassignment of the same upper palette over
the same lower palette.  Expanding the two-element differences gives
(1.6).  Its physical endpoints are eight distinct three-subsets of
`{p,q,r,s,t}` adjoined to `S`; the two phases share the four stated rows and
have the new-only triples in (1.7).  \(\square\)

This is an alternating `C6` in the **outer matching**.  Its physical union
is two alternating paths, rather than the typed physical `C6` of the
four-resource Boolean hexagon.  Confusing those two statements would
incorrectly assert pointwise tail/head preservation.

## 2. Exact path-bank graphic criterion

Name the old physical edges, in the order of (1.6),

\[
                         AB,\qquad CD,\qquad EF,      \tag{2.1}
\]

so that the new edges are

\[
                         GA,\qquad DF,\qquad HE.      \tag{2.2}
\]

### Theorem 2.1 (cycle plus a four-path endpoint bank)

Let `R` be a graph of maximum degree two whose lower and upper diamond
palettes are exact.  Suppose `O subset R` and:

1. `CD` lies on a cycle component;
2. `AB` and `EF` lie on two distinct path components, both distinct from
   the cycle; and
3. `G` and `H` have degree at most one and lie on two further, distinct path
   components, all five named components being different.

Then

\[
                         R'=(R-O)\cup N               \tag{2.3}
\]

has maximum degree two, has the same exact lower and upper palettes, and
replaces the one cycle and four paths by four paths.  In
particular the cycle count falls by one and the total path count is
unchanged.

#### Proof

Deleting `CD` opens the cycle.  Deleting `AB` and `EF` splits each donor
path once.  The edge `GA` joins the path ending at `G` to one fragment of
the first donor; `HE` does the same with the path ending at `H` and one
fragment of the second; and `DF` joins one endpoint of the opened cycle to
the other fragment of the second donor.  All joined pieces came from
distinct components of the deleted graph, so no new cycle is created.
Every endpoint which loses and regains an edge keeps its degree; `B,C` lose
one and the available endpoints `G,H` gain one.  Thus
maximum degree remains at most two.  Theorem 1.1 gives the exact two outer
palettes.  Component counting gives four final paths.  \(\square\)

The five-distinct-components requirement may be weakened to the exact
graphic-matroid condition that the three added edges form a forest after
contracting the components of `R-O`, together with the literal degree-two
rows at `G,H`.  The displayed version is the clean prepared-host criterion
realized by the frozen `m=8` factor.

## 3. Exact menu through one oriented target

Take the middle old atom `(L_1,U_1)` as the target.  Its two physical
endpoints are `L_1+p` and `L_1+q`; an orientation fixes the ordered pair
`(p,q)`.

To recover a packet through it:

1. choose the ordered pair `(r,s)` of distinct elements of `L_1`; this
   fixes `S=L_1-r-s`;
2. choose `t` outside `U_1`.

There are therefore exactly

\[
           (m-1)(m-2)\,(2m-(m+1))
                    =(m-1)^2(m-2)                   \tag{3.1}
\]

indexed choices.  The parameters are recovered from the chosen packet, so
there is no overcount within this displayed family.

This `Theta(m^3)` count is raw algebraic supply.  A candidate is useful only
if its two companion old diamonds occur in the factor with the component
roles in Theorem 2.1 and its two new-only endpoints are available.  No positive
fraction estimate for those host conditions is currently proved.

## 4. Identification of the frozen `m=8` winner

For the first audited winner take

\[
\begin{aligned}
 S&=\{0,2,7,8,13\},\\
 (p,q,r,s,t)&=(5,6,3,11,15).
\end{aligned}                                        \tag{4.1}
\]

Then

\[
                   (L_0,L_1,L_2)=(8677,10637,43397), \tag{4.2}
\]

and (1.5) is exactly the frozen three-diamond exchange.  The target edge
`CD` is the unique-cycle edge; `AB` and `EF` lie on distinct path components
of sizes `11` and `62`; and `G,H` are endpoints of two further path
components of sizes `13` and `12`.  Thus Theorem 2.1 explains
the mechanical winner without search-specific language.

Coordinate rotation of (4.1) gives all sixteen audited winners.  Hence the
winner bank is one full `C_16` orbit of the dimension-free formula.

## 5. Honest all-dimensional target

The local algebra is no longer open.  A sufficient global statement is:

> **Pentagonal packet planting.**  Every exact necklace cap-two factor with
> a residual cycle can be reselected, without changing its two outer
> palettes, so some cycle edge has one of the `(m-1)^2(m-2)` completions in
> the prepared graphic state of Theorem 2.1.

Even this is only a central Catalan linearization theorem.  For an OR-word
recursion, residence, arbitrary-width upper witnesses, endpoint orientation,
and the common cap must still be guarded.  Because this packet changes the
typed middle banks, it cannot replace the typed Boolean hexagon inside a
proof which freezes tail/head identities across phases.

## 6. Mechanical replay

Run

```text
python3 scratch/audit_catalan_pentagonal_c6_path_bank_formula_20260801.py
```

It verifies the set identity and the prepared-host component change for
every `3<=m<=12`, and identifies (4.1) literally with the first frozen
`m=8` winner.  It writes

```text
scratch/catalan_pentagonal_c6_path_bank_formula_20260801.audit.json
```

with status `PASS_PENTAGONAL_C6_FORMULA` and payload SHA-256

```text
a8ccee7f8b7657370ca221013b6c06986a613e3e0e70832194bd9daa13f8bcb0
```
