# Directed Catalan defect transport

Date: 2026-07-31  
Status: proved exact reduction; the resulting labelled matching is not proved
to exist in every dimension

## 0. Purpose

The uniform version of the Catalan two-rail switch has a simpler exact
interpretation than the full one-of-two formulation.  It transports the
defect of the lower-colour word of the saturating cycle.  When that word has
the extremal profile

\[
                 0^K1^{N-2K}2^K,
\]

the repair is exactly a labelled three-partite perfect matching between

* the `K` omitted middle facets;
* the `K` duplicated lower colours; and
* the `K` missing lower colours.

This note proves that equivalence.  It also identifies the extra condition
which makes the cap-two middle cycle itself attain the lower integrality
floor.

## 1. Setup

Put

\[
 M={2m\choose m},\qquad N={2m\choose m+1},\qquad
 K=M-N=\operatorname{Cat}_m.
\]

Write a saturating cycle as

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0,
\]

where the `U_i` are all rank-`m+1` sets, the `C_i` are distinct rank-`m`
sets, and `C_i,C_{i+1}\subset U_i`.  Let

\[
 {cal E}={ [2m]\choose m}\setminus\{C_i:i<N\},\qquad |{cal E}|=K,
\]

and define the base lower colour of block `i` by

\[
                         b_i=C_i\cap C_{i+1}.             \tag{1.1}
\]

Choose an injective host map `phi` with `X\subset U_i` when
`phi(X)=U_i`.  Insert `X` into that block.  Define its two split colours

\[
 \alpha_X=X\cap C_i,\qquad \beta_X=X\cap C_{i+1}
       \quad(\phi(X)=U_i).                               \tag{1.2}
\]

We use the uniform outgoing convention: retain `X C_{i+1}` and cut
`C_i X`.  Equivalently, the two-rail switch cuts the incoming seam `C_i`
and retains the outgoing split colour `beta_X`.

## 2. Exact transport identity

Let `B` be the multiset `(b_i:i<N)`, and let `L` be the set of all
rank-`m-1` colours, each with multiplicity one.

### Theorem 2.1 (directed defect transport)

The uniform outgoing two-rail switches have an exact marked lower palette if
and only if

\[
 \boxed{
 B-\{b_i:\phi(X)=U_i\text{ for some }X\}
   +\{\beta_X:X\in{cal E}\}=L
 }                                                        \tag{2.1}
\]

as multisets.

Moreover, after inserting all omitted facets, the lower-colour multiset of
the cap-two middle Hamilton cycle is

\[
 L+\{\alpha_X:X\in{cal E}\}.                           \tag{2.2}
\]

Consequently that middle cycle has the exact integrality-floor profile
`1^(N-K) 2^K` if and only if the `alpha_X` are pairwise distinct.

#### Proof

An unmatched block contributes the marked lower colour `b_i`.  In a matched
block the incoming marked edge, of colour `alpha_X`, is cut, while the
outgoing edge, of colour `beta_X`, remains.  This is exactly the multiset on
the left of (2.1), proving the first assertion.

Before the two-rail switch, subdividing the base edge of a matched block
removes `b_i` and adds both `alpha_X` and `beta_X`.  If (2.1) holds, its full
lower multiset is therefore `L+{alpha_X}`, proving (2.2).  Since `L` already
contains every colour exactly once, adding `K` colours has the floor profile
precisely when those `K` added colours are distinct.  QED.

This identity is useful because it does not assume beforehand that the
cap-two middle cycle is lower-complete.  Exactness after switching is the
primary condition; lower-floor exactness of the intermediate cycle is the
separate rainbow condition on the cut colours `alpha_X`.

## 3. The zero-slack matching

Assume now that the base colour word has profile

\[
                       0^K1^{N-2K}2^K.                  \tag{3.1}
\]

Let `H` be its `K` missing colours and `D` its `K` duplicated colours.
Construct a labelled tripartite hypergraph on

\[
                       {cal E}\ \dot\cup\ D\ \dot\cup\ H.
\]

For `X in E`, `d in D`, and `h in H`, put a hyperedge `(X,d,h;i)` whenever

\[
 X\subset U_i,\qquad b_i=d,\qquad X\cap C_{i+1}=h.       \tag{3.2}
\]

The block index is retained as a label if several witnesses give the same
unlabelled triple.

### Theorem 3.1 (three-partite normal form)

Under (3.1), a uniform outgoing directed repair exists if and only if this
labelled hypergraph has a perfect matching.

If, in addition, the selected values `X cap C_i` are pairwise distinct, the
same matching simultaneously gives a cap-two middle Hamilton cycle with
lower profile `1^(N-K)2^K`.

#### Proof

To turn the base multiset into `L`, at least one occurrence of every colour
in `D` must be removed and every colour in `H` must be inserted.  There are
exactly `K` switches, `K` duplicated colours, and `K` holes.  Thus equality
forces every switch to remove exactly one duplicated occurrence and the
inserted `beta_X` values to enumerate `H`.  Each omitted facet is used once,
and distinct duplicate colours force distinct host blocks.  These are
exactly the three shores and hyperedges in (3.2).

Conversely a perfect matching chooses every omitted facet once, one
occurrence of every duplicate colour, and every hole once.  Its labelled
block witnesses are distinct, so they define an injective host map and make
(2.1) hold.  The final statement follows from Theorem 2.1.  QED.

## 4. Equivalent directed-diamond geometry

Every selected hyperedge is one Boolean diamond.  Put

\[
 d=b_i,\qquad h=\beta_X,\qquad R=d\cap h.
\]

Then `d` and `h` are Johnson-adjacent rank-`m-1` sets, and for unique
coordinates `p,q` one has

\[
 d=R+p,\quad h=R+q,\quad C_{i+1}=R+p+q,
\]

while `X=h+c` and `U_i=C_{i+1}+c` for the remaining block coordinate `c`.
Thus a repair transports one duplicate token along the directed Johnson edge

\[
                            d\longrightarrow h.          \tag{4.1}
\]

The omitted facet and its host certify that this colour move is physically
realizable inside the prescribed saturating block.  An arbitrary matching
between `D` and `H` in the Johnson graph is therefore insufficient; it must
lift through distinct omitted facets and host blocks.

## 5. Finite calibration and honest scope

The audit

```text
python3 scratch/audit_catalan_directed_repair_finite_m2_m3_20260731.py
```

contains two complete `m=3` fibres.

* One fixed saturating cycle has exactly one split-repair solution, but its
  orientation is mixed; it has no uniform directed solution.
* The cycle

  ```text
  60,53,23,15,29,30,54,46,43,45,39,51,58,27,57
  ```

  has base profile `0^5 1^5 2^5` and exactly one solution.  It is uniformly
  outgoing, its five `beta_X` values are the five base holes, and its five
  `alpha_X` values are distinct.  Hence it realizes Theorems 2.1 and 3.1
  with equality throughout.

At `m=2`, every rooted saturating cycle has general split-repair solutions
but no uniform one, so it is a genuine small base exception.

The theorem proved here is a reduction, not an all-dimensional existence
proof.  What remains is to construct, for every `m` (or recursively), a
saturating cycle whose labelled defect-transport hypergraph has the required
perfect matching, while also protecting connectivity, higher shadows,
residence, and the common-cap compiler.
