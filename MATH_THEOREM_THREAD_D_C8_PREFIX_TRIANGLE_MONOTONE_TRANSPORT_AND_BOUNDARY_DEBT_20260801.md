# Folded C8 endpoint: monotone prefix-triangle transport and the exact three-colour boundary debt

Date: 2026-08-01  
Lane: Thread D, clean folded-C8 endpoint physicalization  
Status: dimension-free conditional prefix theorem; exhaustive replay of every
persisted endpoint certificate for `2<=d<=12`; exact boundary-service no-go
for the current raw component words.  The physical forest assertion is only
the authenticated **single suffix ray**; no simultaneous prefix/cross bank
is claimed, and no all-`d` seam-existence theorem is claimed.

## 0. Verdict

The clean endpoint rethread is monotone, but it is not a pure full-block
refinement of the maximal source.  Before splitting its first host letter,
it strictly shrinks source positions `0,...,d-1`.  Under the natural address
lift, precisely

\[
                    \{[i,j]:0\le i\le j<d\}             \tag{0.1}
\]

change core, a prefix triangle of size `binom(d+1,2)`.  Every changed core
is a strict subset of the old core and every duplicated old interval cap is
equal to the old cap.  Therefore **every individual old one-core graph edge
remains admissible**:

\[
 C_{new}(I^*)\subseteq C_{old}(I)\subseteq T
                \subseteq P_{old}(I)=P_{new}(I^*).       \tag{0.2}
\]

This corrects the stronger but false statement that any changed core destroys
an old matching edge.  What is not automatic is simultaneous literal
common-`Q`: all matched rows share source letters, so the maximal-word/cap
intersection equations still have to hold jointly.  Strict-core equality is
also not preserved on the triangle.

The factor palette has a separate exact debt.  If the fixed core `K` is
suppressed and `F[i,j]={f_i,...,f_j}`, the three removed lower colours are

\[
\begin{aligned}
 c_H&=\{z,a_1\}\cup F[1,d],\\
 c_R&=\{z,a_3\}\cup F[2,d+1],\\
 c_F&=\{z,a_0\}\cup F[0,d-1],                            \tag{0.3}
\end{aligned}
\]

and the inserted seam contributes the new colour

\[
                         c_S=\{z\}\cup F[1,d+1].         \tag{0.4}
\]

Thus an original `W=8d+24` rainbow cycle becomes a factor with `W-2`
distinct internal lower colours: it loses three old colours and gains one
new colour.  Neither one-sided ray serves any member of (0.3).  More
strongly, in every persisted certificate, no member of (0.3) occurs in
either raw component source deck or in any crossing interval under any of
the eight component order/orientation choices.  The present literal
boundary-service rank is therefore `0/3`.  Three external/pinned sidecar
occurrences are still required.

The source-length ledger is nonetheless favourable: the active host split
has `chi=1`, while contracting it back to the prospective unsplit word has
scalar reset charge `chi=0`.  This is a length statement, not a proof of the
joint common-cap equations.

## 1. Closed prefix algebra

Put

\[
 X=\{z,a_1,a_3\},\qquad N=\{z,a_3\}.                    \tag{1.1}
\]

The maximal source prefix of the authenticated short endpoint path is

\[
\begin{aligned}
 A_0&=X\cup F[1,d],\\
 A_i&=N\cup F[1,d+1-i] &&(1\le i<d),\\
 A_d&=N\cup\{f_1\}.                                    \tag{1.2}
\end{aligned}
\]

The prospective host word keeps `B_0=X` and has

\[
\begin{array}{c|cc}
 &\epsilon=0&\epsilon=1\\ \hline
 B_i&N\cup\{f_{d+1-i}\}&\{z,f_{d+1-i}\}
                 \quad(1\le i<d),\\
 B_d&A_d&A_d.
\end{array}                                             \tag{1.3}
\]

All later positions are unchanged.  Finally split `B_0` into the two
nonempty endpoint halves whose union is `X`.  The natural old-to-new address
map is

\[
 [i,j]\longmapsto
 \begin{cases}
 [0,j+1],&i=0,\\
 [i+1,j+1],&i>0.
 \end{cases}                                             \tag{1.4}
\]

Contracting the first two split positions reduces its core calculation to
the word `B` in (1.3).

### Theorem 1.1 (all-depth prefix-triangle formula)

Assume (1.2)--(1.3), with every position after `d` unchanged.  For every
`d>=2` and interval `[i,j]`, the lifted new core is contained in the old
core.  Equality fails exactly for (0.1).  For `0<=i<=j<d`, the precise lost
coordinate set is

\[
 C_A[i,j]\setminus C_B[i,j]=
 \begin{cases}
 F[1,d-j],&i=0,\\
 F[1,d-j],&i>0,\ \epsilon=0,\\
 \{a_3\}\cup F[1,d-j],&i>0,\ \epsilon=1.
 \end{cases}                                             \tag{1.5}
\]

Every interval reaching position `d`, and every interval starting later,
has equal old and new cores.

#### Proof

For `j<d`, the old nested filler union contains `F[1,d+1-i]`, whereas the
new descending singleton union contains exactly
`F[d+1-j,d+1-i]`.  Their difference is `F[1,d-j]`.  In phase one and
`i>0`, (1.3) additionally deletes `a3`; when `i=0`, `B_0=X` restores it.
This proves (1.5), and every listed difference is nonempty.

If `j>=d` and `i<d`, the descending singleton positions supply
`f_2,...,f_{d+1-i}`, while the unchanged letter `B_d=A_d` supplies `f1`
and `a3`; hence their union is exactly the old nested union.  Positions
starting at or after `d` are unchanged term by term.  Splitting `B_0` does
not alter a full-block union, so (1.4) gives the same conclusion. \(\square\)

The proof is symbolic for all `d`.  It is conditional on the endpoint source
formulas; the existence of the surrounding seam/factor is authenticated only
for `2<=d<=12`.

## 2. Monotone matching transport

Give each split position the old cap of the position it refines.  Under
(1.4), the interval cap is unchanged.  Theorem 1.1 then gives (0.2).

### Corollary 2.1 (individual graph-edge preservation)

Every old edge in the Boolean interval graph

\[
                         C(I)\subseteq T\subseteq P(I)   \tag{2.1}
\]

maps injectively to a legal new edge.  The ray side cells, which use a proper
nonempty part of the split block, lie outside the address image and hence are
cell-disjoint from the transported matching.

This corollary is intentionally graph-local.  One source letter participates
in many assigned rows.  A single source word realizes all rows simultaneously
iff the complete maximal-word intersection/reconstruction equations hold.
Nor does (2.1) preserve the stronger condition `C(I)=T` on the changed
triangle.

## 3. Exact factor palette ledger

The endpoint forest removes the host edge, the repeated-upper edge, and the
final forest-opening edge.  Their intersections are exactly (0.3).  The one
inserted seam has intersection (0.4).  These four values are pairwise
distinct, and (0.4) was absent from the old lower palette.  Hence

\[
 |L_{new}|=|L_{old}|-3+1=W-2,                            \tag{3.1}
\]

with every retained/new value occurring once.  All sixteen upper values and
the audited residence conditions survive.

The only authenticated one-sided bank is the native suffix ray.  Its values
have the form

\[
                \{z,a_\epsilon\}\cup F[t,d],
                        \qquad 2\le t\le d,              \tag{3.2}
\]

with `a_epsilon` equal to `a3` or `a1` according to the endpoint.  Formula
(3.2) equals none of (0.3): `c_H` needs `f1`, `c_R` needs `f_(d+1)`, and
`c_F` needs both `a0` and `f0`.  Thus the advertised ray bank has boundary
service rank zero for the three lower debts, uniformly in `d`.

### Proposition 3.1 (current raw boundary no-service certificate)

For every persisted endpoint certificate `2<=d<=12`, in both phases:

1. neither component source deck contains any target in (0.3);
2. no interval crossing the join of the two component words contains one,
   for either component order and either orientation of each component.

Therefore simply ordering/reversing/concatenating the present two words
cannot recycle a lost colour.  A different endpoint pin, a lower sidecar, or
a nonlocal rethread must explicitly supply three distinct occurrences.

#### Proof

There are two component words.  Enumerate every internal interval and every
crossing interval in the `2*2^2=8` ordered/oriented concatenations and compare
its literal union with (0.3).  The exact replay finds no equality.  This is a
finite exhaustive statement for the frozen certificates, not an all-factor
no-go. \(\square\)

## 4. Exact remaining endpoint gate

The clean endpoint now has the following dependency order.

1. The monotone prefix map transports every old one-core matching edge and
   keeps the private ray cells disjoint.
2. A complete common-cap/maximal-word state must realize all transported
   rows simultaneously; core monotonicity alone does not do this.
3. Three distinct lower boundary services for (0.3) must be planted.  The
   current ray and raw component boundaries provide none.
4. A reflected second endpoint and a literal reset must share the same cap,
   owner, `q1`, residence, and guard state.

Only after these rows hold may the active `+1` split be called a zero-net
regenerative socket.  The contraction gives the correct scalar reset charge,
but not items 2--4.

## 5. Audit

Run

```text
python3 scratch/audit_threadD_c8_prefix_triangle_boundary_service_20260801.py --write
```

The light replay checks the exact factor, all interval addresses, the three
lost and one gained colours, both ray banks, both component decks, and all
eight raw concatenations for every persisted `2<=d<=12` certificate.  It
also stress-checks the closed prefix formulas through `d=64`.
