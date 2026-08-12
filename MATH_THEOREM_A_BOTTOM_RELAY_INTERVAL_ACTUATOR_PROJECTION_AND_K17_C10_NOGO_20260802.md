# Bottom-relay projection of Boolean interval actuators and the exact K17
# saturated-\(C_{10}\) socket no-go

**Date:** 2026-08-02  
**Lane:** A, central common-base/reset and bottom-relay recoupling  
**Status:** dimension-uniform exact projection theorem plus an exact audit of
the frozen K17 payload table.  No residence, state/socket, upper-shadow,
owner-topology, reset, source, compiler, or word conclusion is claimed.

## 0. Verdict

The bottom-token perfect-matching theorem does contain exact Boolean
interval circuits, but only after one extra colour is imposed on its matching
edges.

For a consecutive fixed suffix

\[
                  B\subset M\subset U,\qquad
       (|B|,|M|,|U|)=(q,q+1,q+2),                  \tag{0.1}
\]

decorate the legal bottom-to-slot edge by the other middle vertex

\[
                  \chi(B;M,U)=B\cup(U-M).           \tag{0.2}
\]

An alternating bottom-matching circuit is an exact four-resource interval
circuit if and only if its old and new \(\chi\)-decks agree.  The bottom,
upper, and fixed-middle rows then agree automatically.  The standard hub
\(C_6\), hub \(C_8\), and saturated \(B_5\) \(C_{10}\) all satisfy this
criterion.  Thus the correspondence is genuinely positive and
dimension-uniform.

It does not freeze both middle occurrences pointwise.  One middle \(M\) and
the upper \(U\) stay on their physical slots; the induced co-middle
\(\chi\) is transported between slots while its named palette is preserved.
Pointwise fixation of both middles would force the lower as their
intersection and leave no nonidentity actuator.

On the authenticated K17 table, this criterion gives many exact lower-band
circuits:

\[
\begin{array}{c|r|r}
 &\text{raw suffix sockets}&\text{native circuits}\\ \hline
C_6&96,619&246\\
C_8&287,269&16\\
C_{10}&0&0.
\end{array}                                         \tag{0.3}
\]

The zero in the last row is before any bottom perfect matching is chosen:
the fixed suffix geometry contains no saturated \(B_5\) \(C_{10}\) socket.
Consequently no sequence of bottom relays on this frozen table can realize
the combined \(C_{10}+C_6\) absorber.  The existing native \(C_6/C_8\)
circuits preserve the exact payload partition and suffixes, but they give no
owner-topology or common-state conclusion.

## 1. The coloured bottom matching

Let \(\mathcal B\) be a family of named rank-\(q\) bottoms.  Let
\(\mathcal V\) be physical slots with fixed consecutive suffixes

\[
                         M_v\subset U_v,\qquad
                 (|M_v|,|U_v|)=(q+1,q+2).           \tag{1.1}
\]

The bottom containment graph has edge \(Bv\) exactly when
\(B\subset M_v\).  Such an edge defines the Boolean interval

\[
                         [B,U_v]                     \tag{1.2}
\]

whose two middle vertices are

\[
                  M_v,\qquad \chi(B;v):=B\cup(U_v-M_v).        \tag{1.3}
\]

The strict containments in (0.1) imply that \(U_v-M_v\) is one point,
that \(\chi(B;v)\ne M_v\), and that (1.3) lists the two intermediates of
(1.2) exactly.

### Theorem 1.1 (exact co-middle deck criterion)

Let \(P_0,P_1\) be two bottom matchings using the same bottom-token palette
and the same physical slot palette.  Regard the fixed middle \(M_v\) as the
head of slot \(v\), and the induced co-middle \(\chi(B;v)\) as its tail.
Then the induced interval phases have identical lower, upper, tail, and head
resource palettes if and only if

\[
       \boxed{
       \{\!\{\chi(B;v):Bv\in P_0\}\!\}
       =
       \{\!\{\chi(B;v):Bv\in P_1\}\!\}.}           \tag{1.4}
\]

When \(P_0\triangle P_1\) is one alternating \(C_{2r}\), condition (1.4)
therefore makes that matching circuit a literal \(r\leftrightarrow r\)
four-resource interval actuator.  On a complete bottom-relocated table,
flipping it retains every fixed suffix, physical root, owner, named payload,
and chain-length count.

#### Proof

The two matchings use the same bottom tokens, so their lower palettes agree.
They use the same slots, so their upper palettes \(\{U_v\}\) and fixed-head
palettes \(\{M_v\}\) agree occurrencewise.  Formula (1.3) shows that the
only remaining interval resource is the induced co-middle.  Hence equality
of all four rows is equivalent to (1.4).

If the matchings are part of two complete bottom-relocated tables, their
symmetric difference is a disjoint union of alternating circuits in the
bottom graph.  Flipping one circuit is again a perfect matching.  The
bottom-token theorem then retains every payload once and fixes the suffix,
root, owner, and histogram. \(\square\)

### Proposition 1.2 (why only one middle may be fixed occurrencewise)

There is no nonidentity interval actuator which fixes both physical middle
vertices occurrencewise.  Indeed, for any Boolean diamond with middle
vertices \(T,H\),

\[
                         L=T\cap H,\qquad U=T\cup H.            \tag{1.5}
\]

Thus fixing \((T,H)\) fixes its lower and upper endpoints and hence the
entire interval.  Theorem 1.1 is sharp in this sense: \(M_v,U_v\) stay on
their slots, while \(\chi\) is deck-preserved but generally moves address.

This distinction is important for later state compilation.  A named-palette
identity is not a fixed-address identity.

## 2. Exact realization of the three Boolean circuits

### Theorem 2.1 (hub \(C_{2r}\) as a bottom relay)

Fix a \((q-1)\)-set \(C\), a hub \(h\notin C\), and distinct rim points
\(a_0,\ldots,a_{r-1}\) outside \(C+h\).  Put

\[
\begin{aligned}
 B_i&=C+a_i,\\
 M_i&=C+a_i+a_{i+1},\\
 U_i&=C+h+a_i+a_{i+1},
\end{aligned}                                       \tag{2.1}
\]

with indices modulo \(r\).  The old and new bottom matchings are

\[
                     P_0=\{B_iv_i\},\qquad
                     P_1=\{B_{i+1}v_i\}.            \tag{2.2}
\]

They form one alternating \(C_{2r}\), and

\[
 \chi(B_i;v_i)=C+h+a_i,\qquad
 \chi(B_{i+1};v_i)=C+h+a_{i+1}.                    \tag{2.3}
\]

Hence (1.4) holds by a cyclic shift.  For \(r=3\) and \(r=4\), (2.2) is
respectively the exact Boolean \(C_6\) and parity-breaking \(C_8\).

#### Proof

Both \(B_i\) and \(B_{i+1}\) lie in the fixed middle \(M_i\), so every
edge in (2.2) is legal.  Equations (2.1)--(2.3) are direct set identities.
Theorem 1.1 completes the proof. \(\square\)

### Theorem 2.2 (saturated \(B_5\) \(C_{10}\) as a bottom relay)

Fix a \((q-1)\)-set \(C\) and cyclically ordered distinct points
\(a_0,\ldots,a_4\) outside \(C\).  Put

\[
\begin{aligned}
 B_i&=C+a_i,\\
 M_i&=C+a_i+a_{i+2},\\
 U_i&=C+a_i+a_{i+1}+a_{i+2}.                       \tag{2.4}
\end{aligned}
\]

Then

\[
                  P_0=\{B_iv_i\},\qquad
                  P_1=\{B_{i+2}v_i\}               \tag{2.5}
\]

is one alternating \(C_{10}\), and

\[
 \chi(B_i;v_i)=C+a_i+a_{i+1},\qquad
 \chi(B_{i+2};v_i)=C+a_{i+1}+a_{i+2}.              \tag{2.6}
\]

Thus its co-middle deck is also a cyclic shift, and the frozen-fibre
\(C_{10}\) is an exact bottom-relay interval actuator whenever the five
fixed suffix slots (2.4) exist.

Theorems 2.1--2.2 are all-dimensional.  They assert an exact local
correspondence, not that a given suffix table contains the displayed slots
or that the selected local matching extends to a perfect matching of its
whole containment graph.

## 3. Exact K17 audit

Use the frozen table

```text
scratch/k17_exact_depth3_owner_payload_table_20260802/
  k17_depth3_owner_payload.tsv
```

with SHA

```text
029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1.
```

It has 18,646 eligible real bottom tokens.  Exactly 10,025 eligible hard
slots have consecutive rank pattern \(6<7<8\); these are the only rows on
which a rank-two Boolean interval can be changed by moving the theorem's
bottom while retaining its fixed suffix.

### Theorem 3.1 (literal socket census)

On this fixed table:

1. there are 96,619 hub-\(C_6\) suffix sockets whose three required bottom
   tokens all belong to the eligible token bank;
2. 246 of them are native circuits of the frozen bottom assignment;
3. there are 287,269 hub-\(C_8\) suffix sockets, 16 native;
4. there is no saturated \(B_5\) \(C_{10}\) suffix socket at all.

Flipping any of the 246 or 16 native circuits gives another exact static
bottom-relocated table.  Direct replay preserves the complete named target
multiset, every fixed \((M_v,U_v)\) suffix, every root and owner, the chain
histogram, and the induced co-middle deck.

#### Proof

For a hub socket, group slots by the common one-point difference
\(h=U_v-M_v\).  For every five-subset \(C\subset M_v\), record the rim edge
\(M_v-C\).  Triangles and four-cycles in this rim graph are exactly
(2.1) for \(r=3,4\).  Test the required bottoms \(C+a_i\) against the
18,646-token bank; a socket is native when its current bottoms follow one
cyclic orientation.

For \(C_{10}\), a slot (2.4) records the directed length-three word
\((a_i,a_{i+1},a_{i+2})\).  Five slots form the required socket exactly
when these words make one cyclic word of five distinct points and every
bottom \(C+a_i\) is eligible.  Exhaustive enumeration gives (0.3).  The
native representatives are independently materialized and replayed by the
auditor in Section 5. \(\square\)

### Corollary 3.2 (frozen-table combined-absorber no-go)

The exact \(C_{10}+C_6\) forest absorber cannot be realized while moving
only the bottom layer of this frozen K17 table.  This remains true after any
number of preliminary bottom relays: such relays change the matching but do
not change the suffix catalogue, and that catalogue contains zero candidate
\(C_{10}\) sockets.

This is a no-go for the specific frozen suffix table and the saturated
\(B_5\) \(C_{10}\) geometry.  It is not an all-K17 no-go after suffix
rethreading, and it is not an all-dimensional no-go.

## 4. Rank and topology scope

The positive K17 circuits above live in the lower consecutive band

\[
                         6<7<8.                      \tag{4.1}
\]

They can change the auxiliary interval matching on rank-seven co-middles
while the rank-seven fixed middles and rank-eight roots remain on their
slots.  They do **not** change the rank-eight-root/rank-nine-owner phase,
because every owner attachment is frozen by the bottom theorem.

If a proposed central absorber acts instead on ranks \(7<8<9\), it cannot
be represented by this bottom-TU face: rank-seven targets are suffix
resources, not movable bottoms.  Realizing that central actuator requires a
suffix/owner rethread first.  The all-dimensional correspondence in Section
2 still applies to a table whose movable layer actually occupies its lower
rank.

Even in the lower band, Theorem 1.1 preserves the induced co-middle only as
a named deck.  Its physical address changes.  Therefore the native
circuits give no automatic common-state, residence, reset, topology, or
compiler compatibility.  Those rows must be regenerated on the resulting
table.

## 5. Audit artifact

The exact scan and native replay are frozen at

```text
scratch/a_k17_bottom_interval_actuator_20260802/
  audit_a_k17_bottom_interval_actuator_20260802.py
  audit.json
```

The script parses all 24,310 rows, reconstructs the 18,646-token bank and
10,025 consecutive suffix slots, enumerates the three socket types directly
from masks, and replays one native \(C_6\) and one native \(C_8\) against
the complete target multiset and induced co-middle deck.
