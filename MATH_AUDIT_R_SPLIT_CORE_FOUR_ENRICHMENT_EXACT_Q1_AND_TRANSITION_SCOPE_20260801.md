# Audit of the split-core four-enrichment repair

Date: 2026-08-01  
Verdict: `VALID AS A NEW PREPARED HOST; NOT TRANSPARENT FROM THE SPARSE HOST`  
Scope: local literal source, owner/q1/residence, monotone insertion, and
occurrence/common-cap semantics.

## 1. The exact four edits

Start from the sparse source in
`MATH_THEOREM_SPLIT_CORE_PIVOT_LITERAL_TWO_SIDED_COLLAR_20260801.md`.
Keep its two collar-heavy letters.  Make only the following replacements:

\[
\begin{aligned}
 (X_R-\{x_R\})\cup\{q^-\}&\longmapsto
 B^-=(B-\{x_R\})\cup\{q^-\},\\
 C\cup X_L\cup\{\lambda_h\}&\longmapsto
 (B-\{x_R\})\cup\{\lambda_h\},\\
 C\cup X_R\cup\{\rho_1\}&\longmapsto
 (B-\{x_L\})\cup\{\rho_1\},\\
 (X_L-\{x_L\})\cup\{q^+\}&\longmapsto
 B^+=(B-\{x_L\})\cup\{q^+\}.
\end{aligned}                                             \tag{1.1}
\]

In zero-based final-source coordinates these are positions

\[
                    h-1,quad2h-1,quad2h+1,quad3h+1,     \tag{1.2}
\]

and the pivot remains at `2h`.

### Theorem 1.1 (literal owner and q1 repair)

For every `h>=2`, the four-edit source has `4h+1` nonempty letters and its
length-`h+1` unions are exactly

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}.
                                                               \tag{1.3}
\]

Deleting `X` gives exactly

\[
 L_0,\ldots,L_{h-1},U_0,\ldots,U_{h-1},R_0,\ldots,R_{h-1}.
                                                               \tag{1.4}
\]

Every native shared length-`h` source cell equals the intersection of its
two adjacent owners, and every spanning length-`h+2` cell equals their
union.  Thus both immediate q1 palettes are literal and injective.  The
owner path, all owner-coordinate runs, and its `h+1` internal residence
floor are unchanged.

#### Proof

Every added coordinate lies in every owner window containing its edited
position.  The first and last edits insert `B^-` and `B^+` into the left and
right collar blocks.  The two pivot-adjacent edits retain `B-{x_R}` and
`B-{x_L}` across the seam exchanges.  Hence no owner union changes.

For a source `a_0,a_1,...`, put

\[
 O_t=\bigcup_{j=t}^{t+h}a_j,qquad
 C_t=\bigcup_{j=t+1}^{t+h}a_j.
\]

Then

\[
 O_t\cap O_{t+1}=C_t\cup(a_t\cap a_{t+h+1}).             \tag{1.5}
\]

The four additions are exactly the four missing sets in the sparse
source's deficit table.  Formula (1.5) is therefore tight at all `3h`
transitions.  A spanning cell is tautologically the union of its two owner
windows.  Since the owner sequence is unchanged, palette injectivity and
residence follow from the already audited owner ledger.  \(\square\)

## 2. Local caps and common source

The four enlarged letters are below their owner maximal envelopes.  In
particular, their envelopes contain respectively

\[
 B^-,\qquad (B-\{x_R\})\cup\{\lambda_h\},\qquad
 (B-\{x_L\})\cup\{\rho_1\},\qquad B^+.                  \tag{2.1}
\]

Consequently the displayed word is one common-source witness for all owner,
native lower-q1, and spanning upper-q1 rows.  With outside caps, lower bounds,
and fixed-exterior rows adjoined, the exact maximal-word test remains

\[
 K_p=C_p\cap\bigcap_{R:p\in J_R}S_R,quad
 L_p\subseteq K_p\ne\varnothing,quad
 S_R=B_R\cup\bigcup_{p\in J_R}K_p.                      \tag{2.2}
\]

Thus local legality does not imply ambient legality: every outside cap must
admit all four enlarged letters, and every outside row using an affected
address must reconstruct literally.

## 3. Exact monotone insertion and short-band ledger

Delete the pivot `X`.  In the enriched preword its adjacent letters are

\[
 (B-\{x_R\})\cup\{\lambda_h\},qquad
 (B-\{x_L\})\cup\{\rho_1\},                             \tag{3.1}
\]

whose union contains `B` and therefore `X`.  The convex-hull insertion map
is injective on every old interval address and preserves its OR.  Crossing
intervals gain one source position, so exact-width, deadline, chronology,
and address guards still need explicit transport.

In the width-at-most-`h` band the complement remains exactly

\[
 X,quad B\cup\lambda[h-i+1,h],quad B\cup\rho[1,i],
                    \qquad1\le i<h,                     \tag{3.2}
\]

and exactly `h-1` old width-`h` crossing cells escape, with values
`M_1,...,M_{h-1}` of rank `r`.  Therefore the repair creates no additional
**insertion-born address class**.  A strict-lower matching on the enriched
preword transports after releasing every ray-served logical target and
replaying its non-value guards.

## 4. Sharp nontransparency from the sparse source

The edit (1.1) is not OR-transparent from the old sparse preword.  After
deleting `X`, the four edited positions are `h-1,2h-1,2h,3h`.  Using
zero-based inclusive addresses, the OR changes at exactly

\[
\begin{aligned}
 &[h-1,j],&&h-1\le j\le2h-2,\\
 &[i,2h-1],&&h\le i\le2h-1
       &&\text{if }X_R-\{x_R\}\ne\varnothing,\\
 &[2h,j],&&2h\le j\le3h-1
       &&\text{if }X_L-\{x_L\}\ne\varnothing,\\
 &[i,3h],&&2h+1\le i\le3h.
\end{aligned}                                             \tag{4.1}
\]

Every address in (4.1) has width at most `h`; all other sparse-preword
intervals keep their OR.  Hence “no new short cells” is true only for the
enriched-preword-to-inserted-word comparison.  Relative to the sparse host,
between `2h` and `4h` existing short cells change value.

The smallest obstruction is `h=2`, `C=empty`,
`X_L={ell},X_R={r}`.  The sparse seam singleton values `{q^-},{q^+}` become
`{ell,q^-},{r,q^+}`.  Since `q^-`,`q^+` are unique labels, both old singleton
targets disappear from the entire enriched deck.  Thus an incumbent sparse
matching or guard ledger cannot be transported without explicit rematching.

## 5. Occurrence identities, not duplicate witnesses

Two endpoint coincidences are literal address identities:

\[
 P_{h-1}=I_0=[h+1,2h],\qquad
 S_{h-1}=I_{h-1}=[2h,3h-1]                              \tag{5.1}
\]

in zero-based inclusive final coordinates.  One physical cell serves both
the ray-target and native lower-q1 row; there are not two occurrences.

Likewise each pre-insertion crossing owner `U_j` transports to exactly the
same length-`h+2` final cell which is the native upper-q1 occurrence for
`M_j,M_{j+1}`.  A ledger may attach two semantic row labels to that equality,
but it may not count two cells, two matching edges, or two protected
witnesses.

## 6. Correction to the earlier tight serialization

The source formerly displayed as (4.17) in
`MATH_THEOREM_A_SPLIT_PIVOT_PHYSICAL_COLLAR_AND_BPLUS1_TERMINAL_PATH_20260801.md`
was mathematically valid but was not a four-edit transformation: it also
shrunk the two collar-heavy letters to singletons.  The four-edit source in
(1.1) retains those letters and has the same owner, pre-row, q1, residence,
and insertion ledgers.  It is the correct realization of the claimed
four-replacement repair.

## 7. Independent replay

The dependency-free audit checks `540` symbolic parameter cases:
`2<=h<=16`, both split-shore sizes `1..3`, and `|C|=0..3`.  It enumerates
every interval address and verifies (1.3)--(5.1), the exact changed-address
families, owner caps, and residence.

```text
scratch/audit_r_split_core_four_enrichment_20260801.py
scratch/r_split_core_four_enrichment_20260801.audit.json
```

No global protected-factor embedding, exterior guard completion, background
rematching, or regenerative theorem follows.
