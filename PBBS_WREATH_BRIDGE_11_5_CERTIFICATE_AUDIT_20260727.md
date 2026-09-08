# An exact PBBS-to-wreath switch bridge in \(KG(11,5)\)

Date: 2026-07-27

## 1. Exact finite result

Let \(F_{\rm PBBS}\) be the canonical cyclic-parenthesis/PBBS spanning
2-factor of \(KG(11,5)\).  There is an explicitly recorded sequence of 303
factor-alternating simple 8-cycle switches with the following properties.

1. Every intermediate state is a spanning Kneser 2-factor.
2. Every component of every intermediate state is point-regular.
3. The final state consists of 42 cycles of length 11.
4. The final state is the explicit wreath factor in
   `m5_switch_vertical_wreath_factor_seed77.best.txt`.

Since every length-11 cycle of the odd graph \(KG(11,5)\) is a wreath, the
last state is an exact wreath factor.  Thus the nonmonotone
merge--reorder--split mechanism previously certified only at \(m=4\) also
exists at \(m=5\).

The replayable certificate is

```text
scratch/pbbs_m5_wreath_bridge_certificate.json
```

and its independent verifier is

```text
scratch/search_pbbs_wreath_bridge.py --verify
```

## 2. Independent replay checks

The verifier reconstructs the PBBS seed without reading a stored initial
factor.  At every step it checks:

* all eight toggled edges are physical Kneser edges;
* the toggled graph is one connected simple \(C_8\);
* exactly four edges are current factor edges and old/new edges alternate;
* toggling preserves degree two at every middle owner; and
* every resulting component is point-regular.

It then independently reconstructs the target from its 42 coordinate orders
and checks equality of all 462 factor edges.  The verified terminal data are

\[
\begin{array}{c|c}
\text{quantity}&\text{value}\\ \hline
\text{switches}&303\\
\text{terminal components}&42\text{ copies of }C_{11}\\
|E(F_{\rm PBBS})\setminus E(F_{\rm final})|&306\\
\text{changed centered owners}&446\\
\text{terminal two-sided stopped support loss}&42.
\end{array}
\]

Here the last quantity is 20 lower holes at depth one, one lower hole at
depth two, and their complementary upper copies.  The canonical PBBS tower
itself has zero live floor-correct excess at every depth, so in the exact
coupling

\[
 \mathfrak C^{\rm ord}
 =\mathfrak C^{\rm PBBS}_{\rm live}
  +\mathfrak R_{\rm mort}
  +\mathfrak B_{\rm ext},
\]

all 42 terminal units occur in the signed extraction term
\(\mathfrak B_{\rm ext}\); the live and mortality terms are zero.

## 3. The trajectory is necessarily nonmonotone

The starting PBBS factor has 12 components.  The certified search first
merges these into one point-regular 462-cycle, reorders that cycle, and then
splits it into the 42 target wreaths.  A representative sequence of exact
milestones is

\[
 (12,156)\to(1,195)\to(1,373)\to(3,398)
 \to(12,412)\to(29,447)\to(36,454)\to(42,462),
\]

where each pair is

\[
 (\#\text{components},\;\#\text{target factor edges already present}).
\]

The independently audited \(m=4\) path has the same qualitative behavior:
its component deficit initially worsens from 8 to 11, and its all-depth live
trace loss rises temporarily from 0 to 14 before returning to 0.  Therefore
the following search restrictions are rigorously invalid:

* never merge components;
* require component count to improve at each move;
* require shadow support loss to be nonincreasing; or
* search only for direct self-splits of long PBBS components.

## 4. What this proves—and what it does not

This is a finite exact construction, not an asymptotic rebundling theorem.
Writing \(B=C_5=42\), its numerical scales are

\[
 303=7.21\,B,
 \qquad
 306=7.29\,B.
\]

They are consistent with the desired \(O(B)\) dynamic-switch and edge-edit
statements, but two finite values \(m=4,5\) cannot establish a uniform
constant.  The remaining asymptotic theorem is still an availability/routing
statement: point-balanced bounded alternating switches must implement a
merge--reorder--split route using \(O(C_m)\) switches while keeping the
signed Gaussian-depth extraction loss \(o(W)\).

The certificate nevertheless changes the evidence in two ways.

1. Signature-primitive PBBS components do not block the dynamic route at the
   next dimension; global mixing really creates the required split cuts.
2. The exact FIFO/rebundling gate is now realized nontrivially at both
   \(m=4\) and \(m=5\), rather than only in the exceptional 126-owner case.

## 5. Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/search_pbbs_wreath_bridge.py \
  --verify scratch/pbbs_m5_wreath_bridge_certificate.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/audit_pbbs_to_ordinary_bridge.py \
  --m 5 \
  --ordinary-factor m5_switch_vertical_wreath_factor_seed77.best.txt
```

## 6. Static proximity census

The companion exhaustive census enumerates all

\[
 \frac{10!}{2}=1,814,400
\]

geometric wreaths on eleven coordinates and counts their common factor edges
with canonical PBBS.  Its overlap histogram has the following high end:

\[
\begin{array}{c|rrrrr}
h&7&8&9&10&11\\ \hline
\#\text{wreaths}&20449&2706&374&22&3.
\end{array}
\]

The three overlap-11 wreaths are precisely the three length-11 components
already present in the PBBS factor.  Two exact-cover threshold tests give:

* overlap at least 9: 399 candidates, but 66 middle owners occur in none;
* overlap at least 8: 3105 candidates, every owner occurs in 26--132
  candidates, but the exact-cover CNF is UNSAT.

The second item is a clean finite integrality phenomenon: local owner
coverage by high-overlap wreaths does not imply that they resolve into an
exact factor.  It does not determine the optimum *total* retained overlap,
because a nearest factor may mix a few lower-overlap wreaths with many higher
ones.

An exact-wreath local search produced the separately verifiable factor

```text
scratch/m5_nearest_pbbs_wreath_seed71.txt
```

which retains 195 PBBS edges, improving the retained count 156 of the
42-hole bridge endpoint to 195 and reducing edge distance to 267.  Its true
weighted MWB score is worse (\(683/8\), with 27 and 11 holes at the first two
lower depths).  This is direct finite evidence that PBBS proximity and shadow
balance form a Pareto problem rather than one interchangeable objective.

The census and threshold tests are reproduced by

```bash
clang++ -std=c++20 -O3 scratch/census_pbbs_wreath_overlap.cpp \
  -o /tmp/census_pbbs_wreath_overlap
/tmp/census_pbbs_wreath_overlap 5 10

PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/solve_pbbs_wreath_overlap_threshold.py --threshold 9
PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/solve_pbbs_wreath_overlap_threshold.py --threshold 8
```

The UNSAT statements above are solver-backed computational results; no DRAT
proof artifact is claimed in this note.
