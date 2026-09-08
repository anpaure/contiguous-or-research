# The frozen v5 k=17 post-socket bank is q1-impossible

## Scope

This theorem concerns only the frozen v5 bank obtained from
`scratch/k17_m9_endpoint_degree_combined30_socket_bank_v5_20260801.tsv`
and materialized as 6,252 resident pieces in
`scratch/k17_socket30_postbank_pieces_20260801.json`.
It is **not** a no-go theorem for k=17, the SCD parent, or the socket
architecture in general.

## Exact catalogue

There are 6,252 pieces and therefore 12,504 oriented endpoint states.  The
O3 catalogue enumerated every ordered seam between distinct pieces whose two
endpoint owners are Johnson-adjacent.  It found:

- 520,158 raw oriented seams;
- 129,942 context-extendable seams;
- 23,944 pairwise-robust seams;
- 1,458 rank-10 colours absent from the internal piece deck; and
- seven missing rank-10 colours with no raw seam provider:

\[
  20427,\ 69555,\ 70910,\ 72414,\ 72566,\ 73649,\ 83946.
\]

The compressed exact state and arc tables, summary, and resource record are
frozen under
`scratch/k17_socket30_postbank_arc_catalogue_20260801/`.

## Raw-seam necessity lemma

Let a word be formed by orienting and concatenating the frozen pieces, without
changing their internal owner sequences.  If a rank-10 target \(U\) is
represented by an interval that crosses a piece boundary, then \(U\) labels a
raw seam at one of the crossed boundaries.

### Proof

Choose any boundary crossed by the interval, and let \(A,B\) be the rank-9
owners immediately to its left and right.  All middle owners are distinct, so
\(A\ne B\).  Hence

\[
  |A\cup B|\ge 10.
\]

Both owners lie inside the representing interval, so

\[
  A\cup B\subseteq U.
\]

Since \(|U|=10\), equality is forced: \(A\cup B=U\).  Thus that boundary is a
raw seam provider for \(U\).  This argument applies even when the representing
interval crosses several boundaries. \(\square\)

## Consequence

Each of the seven colours is absent internally and has no raw seam provider.
By the lemma, no orientation or ordering of the 6,252 frozen pieces can
represent it.  Therefore the frozen v5 postbank admits no q1-complete braid and
no universal k=17 word.

The next selector must correlate minimum-residence cuts and socket choices with
raw q1 provider survival.  A Hamilton-path CNF over this fixed postbank is
theorem-redundant.

