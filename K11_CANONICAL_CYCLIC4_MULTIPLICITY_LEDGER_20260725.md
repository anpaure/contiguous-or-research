# Canonical K=11 cyclic-four multiplicity and fusion ledger

> **Retracted multiplicity data (2026-07-25).**  The histogram and triple
> list below are not valid for the corrected literal A--E rows.  In
> particular E13/E14 contain `1346,1345`, not `1236,1235`, and several
> listed triples have only two corrected occurrences.  The support value
> 298 is proved separately in
> `K11_CORRECTED_CYCLIC4_POSITIVE_SUPPORT_CERTIFICATE_20260725.md`; only
> the fusion identity `support = 298-L+G` survives from this note.

Using the symbolic A--E order table and the eleven window templates in
`K11_CANONICAL_CYCLIC4_SUPPORT_CLASSIFICATION_20260725.md`, the exact
multiplicity histogram is

\[
\boxed{m_0=32,\qquad m_1=149,\qquad m_2=134,\qquad m_3=15.}
\]

Indeed,

\[
149+134+15=298,
\]

and

\[
149+2(134)+3(15)=462.
\]

The fifteen multiplicity-three colours are

\[
\begin{gathered}
\{0,1,4,9\},
\{0,2,3,9\},
\{0,2,4,9\},
\{0,2,7,9\},
\{0,2,7,10\},
\{0,2,8,9\},\\
\{1,2,3,4\},
\{1,2,3,5\},
\{1,2,3,6\},
\{1,2,5,10\},
\{1,3,8,10\},\\
\{2,4,6,8\},
\{3,4,6,8\},
\{3,4,6,9\},
\{3,4,7,8\}.
\end{gathered}
\]

All other supported colours have multiplicity one or two.  The count is
obtained by sorting the 168 zero-containing occurrences and the 294
nonzero occurrences separately.  Their intermediate histograms are

\[
(m_0,m_1,m_2,m_3)=(16,46,52,6)
\]

and

\[
(16,103,82,9),
\]

respectively.

## Fusion ledger

Turning 42 cycles into six paths deletes 42 old edges and introduces 36
cross edges.  Let

- (L) be the number of old colours all of whose occurrences are among
  the 42 deleted edges;
- (G) be the number of distinct cross-edge colours absent from the
  surviving old support and from earlier cross edges.

Then the final support is exactly

\[
\boxed{298-L+G.}
\]

Consequently support at least 319 is equivalent to

\[
\boxed{G-L\ge21.}
\]

There are

\[
2(134)+3(15)=313
\]

old edge occurrences whose colours are repeated.  Thus the raw
multiplicity ledger does not force any loss: in principle 42 cuts could
all be chosen among repeated occurrences without exhausting a colour.
The remaining issue is the simultaneous one-per-cycle and physical
splice constraint.
