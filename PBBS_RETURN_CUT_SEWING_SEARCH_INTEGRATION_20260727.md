# PBBS return-cut sewing: integrated search normal form

Date: 2026-07-27

## Outcome

The new mathematics is now represented by one literal search chain:

\[
\text{PBBS components}
\longrightarrow
\text{return-arc certificates}
\longrightarrow
\text{label-simple physical paths}
\longrightarrow
\text{endpoint-compatible wreath packets}
\longrightarrow
\text{exact owner cover}
\longrightarrow
\text{MWB/CPCR/PCap audit}.
\]

The arrows have deliberately different status.

1. Return arcs give a proved lower bound on the PBBS edges any wreath factor
   must delete.
2. Path sewing is a complete finite normal form for high-PBBS-overlap
   wreaths.
3. Exact cover is the unresolved integral compatibility gate.
4. MWB, CPCR, and PCap score a feasible terminal factor; they are not used to
   pretend that an infeasible catalogue is feasible.

## Why cuts and sewing are solved jointly

An optimal return-arc hitting set need not have compatible endpoints.  The
canonical optimal hitting sets at \(m=5\) produce 59 fragments, but only five
one-fragment wreath packets; 54 fragments occur in no sewn packet.  This does
not strengthen the distance lower bound.  It proves that the quantifiers

\[
\exists\text{ optimal cuts}\quad\text{and}\quad
\exists\text{ sewing}
\]

cannot be separated by fixing an arbitrary optimizer of the first problem.

The implemented path pool instead lists every PBBS run whose retained omitted
labels are distinct.  A candidate packet chooses disjoint runs, orientations,
and connector edges simultaneously.  It is emitted only if it is a simple
length-\(n\) Kneser cycle with \(n\) distinct omitted labels.  Hence it is an
actual wreath.

## Exact finite cross-check

For \(m=5,n=11\), path sewing gives

\[
\#\{C:h_{\rm PBBS}(C)=9,10,11\}=374,22,3
\]

with at most two paths, and adds exactly 2706 overlap-eight wreaths with at
most three paths.  These counts coincide with the independent exhaustive
enumerator over all \(10!/2=1,814,400\) geometric wreaths.

The overlap-at-least-nine and overlap-at-least-eight exact-cover instances
are respectively UNSAT with 399 and 3105 candidates.  No DRAT certificate is
claimed; these are solver-backed finite audits.  The structural generator and
the exhaustive generator are independent implementations and agree on the
complete catalogues.

## Search modes

`scratch/search_pbbs_wreath_bridge.py` has three modes.

* `target`: reproduce or route to a supplied exact wreath factor.
* `structural`: target-free search using unresolved owners, the exact
  return-cut lower bound, the constructive (n)-spaced lattice upper bound,
  component-count error, component-length error, and stopped trace loss.
* `hybrid`: use a target without discarding the structural diagnostics.

All modes retain physical alternating switches and point-balanced components
as hard constraints.  The score is an annealing potential, not a monotonicity
assertion.  The verified \(m=5\) path already proves that merges, neutral
reorders, splits, and temporary trace worsening are all necessary search
moves.

## Remaining mathematical gate

The integrated code does not prove the asymptotic theorem.  It isolates the
next target without a proxy:

> Find an exact owner cover by path-sewn wreath packets with total PBBS
> deletion cost \(O(C_m)\) and signed Gaussian-depth extraction loss
> \(o(W)\), then route it by physical merge--reorder--split switches.

The return-cut theorem supplies the lower bound and a Catalan-scale candidate
normal form.  The missing part is global endpoint/exact-cover compatibility,
not another occupancy estimate.

## Bounded verification commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scratch/test_math_aware_search_metrics.py
PYTHONDONTWRITEBYTECODE=1 python3 scratch/audit_pbbs_distinct_label_cuts.py \
  --m-min 2 --m-max 8
PYTHONDONTWRITEBYTECODE=1 python3 scratch/solve_pbbs_wreath_overlap_threshold.py \
  --m 5 --threshold 9 --generator paths
PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/verify_pbbs_path_catalogue_against_exhaustive.py \
  --m 5 --threshold 9
PYTHONDONTWRITEBYTECODE=1 python3 scratch/search_pbbs_wreath_bridge.py \
  --verify scratch/pbbs_m5_wreath_bridge_certificate.json
```

The threshold-eight path catalogue is also exact, but its generation takes
about 24 seconds on the current machine; it is not part of the default smoke
test.

## Support-matched trade layer

`scratch/search_pbbs_factor_trades.py` now sits between path generation and
global exact cover.  It searches the exact support identity

\[
\bigsqcup_{C\in R}\mathcal M(C)
=\bigsqcup_{C\in A}\mathcal M(C)
\]

around a known factor, then audits every terminal factor with the same
MWB/CPCR/PCap code.  This exposes the overlay components that a monolithic
SAT instance hides.

At \(m=5\), all closed trades of size at most six in the union of the five
known factors and the complete overlap-at-least-eight catalogue were
enumerated.  There are 46, none uses an overlap-at-least-eight path-catalogue
wreath, and none improves PBBS retention.  Nevertheless, the lower-overlap
trades form a real shadow-descent network.  Iteration produces a new exact
factor with weighted MWB \(547/8\), compared with the previous \(567/8\).

The full six-factor union has 114 distinct wreaths.  Exhaustive closed-trade
enumeration proves that the new factor is weighted-MWB-optimal within that
finite union.  Details and commands are in
`PBBS_SUPPORT_MATCHED_TRADE_SEARCH_20260727.md`.

The later entire-universe signature census removes this finite-catalogue
restriction for bounded trades.  Enumerating every geometric candidate that
touches at most four current base blocks and descending by exact closed trades
lowers the verified value further to \(391/8\).  The final factor is locally
optimal against all trades of size at most four in the full \(m=5\) wreath
universe.  The residual is dominated by depth two, which is now the relevant
finite model for the missing compatibility theorem.
