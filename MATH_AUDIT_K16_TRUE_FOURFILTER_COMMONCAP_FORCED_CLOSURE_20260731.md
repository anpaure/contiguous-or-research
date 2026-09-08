# True-four-filter K16 common-cap forced-closure audit

Date: 2026-07-31  
Scope: target SHA `c7beccc3...`, schedule
`X=(12870,12871,12872)`, `Y=(0,1,6388)`, with the singleton cell
`[6389,6389]` reserved for `0x8000`.

## 1. Exact compatibility condition after reserving `8000`

Let `E_p` be the maximal middle envelope, except that the certified singleton
reservation is installed first:

\[
\bar E_{6389}=\mathtt{0x8000},\qquad
\bar E_p=E_p\quad(p\ne6389).
\]

Let `C*=[6389,6389]` be unavailable to every residual target.  For an
injective residual assignment `M`, define

\[
A_p(M)=\bar E_p\cap
 \bigcap_{S:\,p\in M(S)}S.                              \tag{1.1}
\]

Then `M` has a simultaneous physical realization if and only if

1. `A_p(M)` is nonempty for every physical position;
2. the OR of `A(M)` on every middle interval is its middle target;
3. the OR of `A(M)` on every assigned residual cell is its assigned lower
   target.

The reserved singleton equation follows automatically: a nonempty subset of
`bar(E)_6389=0x8000` is `0x8000`.

For necessity, any realizing word is pointwise contained in (1.1), because
it is contained in every active middle and assigned lower target.  Enlarging
it to (1.1) cannot lose a required bit.  Conversely, (1.1) is contained in
every relevant target, and the three displayed conditions say exactly that
it is itself a realizing word.  Thus this is an exact maximal-cap criterion,
not merely a relaxation.

## 2. Solver-free universal-assignment lemma

Fix any bipartite graph with a matching `M` saturating its left side.  Make a
directed graph on left vertices: put `u -> v` when `u` can use the current
matched cell `M(v)`, and mark `u` when it can use a currently unmatched right
cell.

The edge `(u,M(u))` belongs to every left-perfect matching exactly when

- `u` does not reach a marked vertex; and
- `u` is not in a nontrivial strongly connected component.

Indeed, a path to an unmatched right cell gives an alternating-path switch,
and a directed cycle through `u` gives an alternating-cycle switch.  In the
other direction, the symmetric difference with any left-perfect matching
that omits `(u,M(u))` contains one of precisely those two structures.

Consequently one may soundly:

1. cap by all such universal assignments at once;
2. reject if that cap empties a position or breaks a middle/fixed lower row;
3. delete any remaining incidence whose additional cap would break a
   protected row; and
4. reject if the filtered residual graph fails Hall.

Iterating is a polynomial, matching-independent local obstruction test.  A
pass is not common-cap sufficiency because several nonessential choices may
still conflict jointly.

## 3. Exact audit

The pinned residual marginal graph has

```text
targets       26331
cells         32229
incidences   347677
matching      26331
```

An independently generated deterministic perfect matching has no empty
physical letter, but its maximal common cap fails 1,808 middle rows and 5,037
assigned lower cells.  This is matching-specific.

The universal-assignment closure is:

| round | new universal edges | ranks | incompatible edges deleted | residual graph |
|---:|---:|---|---:|---:|
| 0 | 14,059 | `5^195,6^3811,7^10053` | 997 | `12272 / 237475` |
| 1 | 1 | `6^1` | 996 | `12271 / 237467` |
| 2 | 0 | — | — | fixed point |

The sole second-round edge is

```text
target 0x12cc -> cell 15071 = [7152,7153].
```

At both nonempty rounds, the simultaneous cap by every universal assignment
has:

- zero empty positions;
- zero failed middle rows;
- zero failed fixed lower rows;
- zero residual no-host targets; and
- a perfect residual matching.

At the fixed point there are 14,060 universal assignments.  The remaining
12,271 targets have a perfect matching in the 237,467-edge filtered graph,
and no further matching edge is universal.  The final maximal fixed cap has
rank histogram

```text
1^1, 5^6480, 6^6388, 7^2, 8^2.
```

## 4. Verdict

No solver-free forced-cell or forced-row-bit obstruction was found.  More
strongly, the complete iterative closure under assignments common to all
current marginal perfect matchings reaches a nonempty exact fixed cap and a
perfect residual graph.

Therefore the deterministic matching failure cannot be promoted to a
common-cap no-go by any obstruction supported only on universally forced
assignments.  A higher-order disjunctive obstruction may still exist among
the 12,271 nonessential choices; resolving that requires the exact common-cap
CEGAR/SAT master or a stronger combinatorial lemma.  No K16 word is claimed.

## 5. Evidence

- `scratch/audit_k16_true_fourfilter_commoncap_forced_closure_20260731.py`
- `scratch/k16_true_fourfilter_commoncap_forced_closure_20260731.audit.json`

