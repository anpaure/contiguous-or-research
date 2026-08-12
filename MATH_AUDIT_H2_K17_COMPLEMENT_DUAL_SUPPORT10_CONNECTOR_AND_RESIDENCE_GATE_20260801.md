# Corrected K17 complement-dual support-ten interface and residence gate

> **Correction (2026-08-01).**  The former two-boundary-tail argument and its
> claimed floor 219 are withdrawn.  Changing an internal `1->1` tail can also
> destroy a short run.  Section 6 now uses the proof-safe full set of
> `ell+1` spanning tails for each `0 1^ell 0` run and gives the corrected
> pairwise-disjoint-hyperedge floor 169.  The independent owner/rank-8 closure
> census is separately frozen in
> `MATH_THEOREM_H2_K17_COMPLEMENT_DUAL_INNER_J7_SUPPORT10_NOGO_20260801.md`.

Date: 2026-08-01  
Lane: H2 independent replay / non-dual connector interface  
Status: **exact factor/interface replay and corrected full-run-hyperedge
support-ten residence no-go; no global K17 claim.**

## 1. Frozen input and scope

The literal input is

```text
scratch/threadD_k17_complement_dual_splice_20260801/seed.best.tsv
SHA-256 a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3
```

The adjacent annealer summary has SHA-256
`28c0d90bf1c23b211d66289c40f93fb5e40cb610fa2655bd337484143ff432b2`
and explicitly says `CANDIDATE_ONLY_EXACT_REPLAY_REQUIRED`.  The independent
audit below does not trust that summary.  It reconstructs the 12,870-edge
rank-9/rank-8 incidence atlas, the complement involution, both perfect
matchings, every quotient shift, both turn palettes, and the physical
component traces directly from the TSV.

This note does not enumerate a connector and does not claim residence,
higher-shadow coverage, a source word, common cap, or a K17 construction.

## 2. Exact replay of the complement-dual seed

Let `D` be the selected incidence matching, `H=C D^{-1} C`, `A=CD`, and
`sigma=H^{-1}D=A^2`.  Independent replay gives

```text
D edges / H edges:              1430 / 1430
dual conflicts:                 0
A cycle lengths:                1429, 1
A cycle voltages:               2, 13  (mod 17)
sigma=A^2 cycle lengths:        1429, 1
sigma component voltages:       4, 9   (mod 17)
total factor voltage:           13     (mod 17)
rank-10 / rank-7 palette size:  1144 / 1144
repeat units on each shore:     286
load histogram on each shore:   1^878 2^247 3^18 4^1
```

Thus this is not the `715+715` parity factor produced by one even Hamilton
`A`.  It is the other exact two-component case: two odd `A` cycles, of
lengths `1429` and `1`.  Both quotient components have primitive physical
voltage.

The singleton component is particularly structured:

```text
owner id / representative:  425 / 7711
D incidence / shift:        3825 / 1
H incidence / shift:        3829 / 9
common facet id / rep:       295 / 3855
singleton step voltage:      9
```

It is exactly the first endpoint of the protected J7 path.

## 3. Exact fixed-`D` connector law

For a fixed `D`, let `R` be the owners whose `H` incidence changes and put
`F=H(R)`.  A legal replacement is a perfect incidence matching

\[
                         H':R\longrightarrow F                     \tag{3.1}
\]

equal to `H` outside `R`.  The corresponding changed successor tails are

\[
                         S=D^{-1}(F),                               \tag{3.2}
\]

and the new head map is

\[
                  g(x)=H'^{-1}(D(x)),\qquad x\in S.                \tag{3.3}
\]

Consequently `g:S->R` is a bijection and the old heads are
`sigma(S)=R`.  These are the exact tail/head balance rows for a fixed-`D`
enumerator.  Parallel quotient incidences must remain distinguished: the
edge ID and shift, not only the owner/facet pair, determine voltage and the
physical turn labels.

For the present `1429+1` factor, connectedness has a sharper necessary
form.  Writing `a=7711` for the singleton and `B` for the large component,
a connected successor permutation must have

\[
              \sigma'(a)\in B,qquad
              |\{x\in B:\sigma'(x)=a\}|=1.                        \tag{3.4}
\]

These two cross arcs are necessary but not sufficient: after deleting all
old arcs with tails in `S`, the induced pairing of path endpoints must form
one cycle.  The proof-safe implementation is a literal traversal of all
1,430 quotient owners.

For a two-edge `H` change, the singleton edge is forced.  If its old edge is
`aF`, choose an old big-component edge `qG` and require both cross incidences
`aG,qF`.  Then

\[
                 a\to a,\ y\to q
          \quad\rightsquigarrow\quad
                 a\to q,\ y\to a,
          \qquad y=D^{-1}(G),                                     \tag{3.5}
\]

which is the unique minimal rectangle merge.

## 4. Voltage and palette acceptance rows

For any final one-cycle pair `(D',H')`, the owner-step voltage is

\[
 \delta'(x)=s(D'(x))-s\!\left(H'^{-1}(D'(x))\to D'(x)\right)
            \pmod {17},                                           \tag{4.1}
\]

and the physical lift is one 24,310-cycle exactly when

\[
                         V'=\sum_x\delta'(x)\ne0\pmod {17}.        \tag{4.2}
\]

Relative to this seed, whose total voltage is `13`, a fixed-`D` change on
facet bank `F` has

\[
 V'=13+\sum_{f\in F}\bigl(s(H_f)-s(H'_f)\bigr)\pmod {17}.          \tag{4.3}
\]

For a joint `D/H` change, use the corresponding signed changes of both
global shift sums.  Recomputing (4.1) along the decoded cycle is the
fail-closed check.

The old lower rank-8 edge palette is exact because `D` is facet-perfect.
If `D` changes, facet-perfectness of `D'` is the exact lower-rank-8 row.
The other two immediate palettes are turn palettes:

```text
upper rank 10 at facet f:  U_f = upper(D'_f,H'_f)
lower rank 7 at owner o:   L_o = lower(D'_o,H'_o).
```

Let `mu_r` be the old load and let `loss_r,gain_r` be literal occurrence
counts over every changed facet/owner center.  The necessary and sufficient
surjection rows are

\[
             \mu_r(T)-\operatorname{loss}_r(T)
                      +\operatorname{gain}_r(T)\ge1,
             \qquad r\in\{7,10\}.                                \tag{4.4}
\]

On a fixed-`D` change only facets `F` can alter upper turns and only owners
`R` can alter lower turns.  On a joint change, the safe implementation
recomputes all centers incident with an old or new changed `D/H` edge.  The
scalar `286` repeat count is not a substitute for (4.4).

## 5. Literal J7 rows and the support-ten seed

The two protected owner paths require the following unique incidence rows.

```text
forward 7711 -> 8077:
  D=3831 shift0, H=4323 shift8, lower8=6687, upper10=8079, delta=9
forward 8077 -> 13623:
  D=4326 shift0, H=7979 shift10, lower8=7053, upper10=13631, delta=7

reverse 13623 -> 8077:
  D=7979 shift10, H=4326 shift0, lower8=7053, upper10=13631, delta=10
reverse 8077 -> 7711:
  D=4323 shift8, H=3831 shift0, lower8=6687, upper10=8079, delta=8
```

Only `D=4326` is selected in the incumbent, and none of the four required
`H` rows is selected.  In particular, fixed `D` cannot realize either J7
orientation: the forward first step and both reverse steps have no cross
incidence at their incumbent `D` facets.  A support-ten J7 enumerator must
therefore be genuinely non-dual and allow `D` as well as `H` to change.

At successor-arc level, forcing heads and lower-rank-8 labels closes the
initial support to five tails in either orientation:

```text
forward: {6943,7711,8077,8133,27253}
reverse: {6943,7711,8077,8133,13623}.
```

Here `8133,27253` are old predecessors of forced heads, and `6943` is the
old `D` owner of facet `6687`.  Thus exact support ten leaves five auxiliary
tails before matching closure.  At a completed leaf the enumerator must
check, with labelled incidences,

\[
 \{\sigma'(x):x\in S\}=\{\sigma(x):x\in S\},\qquad
 \{D'(x):x\in S\}=\{D(x):x\in S\},\qquad |S|=10.                 \tag{5.1}
\]

The first equality is head balance; the second is the lower-rank-8 facet
balance.  They do not replace perfectness of `D'` and `H'`.

Because `7711` is the singleton, the forward J7 orientation supplies the
outgoing cross arc from the singleton, while the reverse orientation
supplies the incoming cross arc.  The opposite cross arc in (3.4) remains
mandatory in each case.

## 6. Corrected residence obstruction

The independent physical replay expands both primitive component lifts and
audits cyclic positive runs at floor four.  The 17-owner singleton lift is
clean.  The 24,293-owner large lift has

```text
length-2 positive runs:              1190
length-3 positive runs:              3128
distinct run-tail hyperedges:         254
pairwise-disjoint run hyperedges:      169
```

For a short physical run `0 1^ell 0`, record all `ell+1` quotient successor
tails of the arcs spanning the subword: the entering boundary arc, the
`ell-1` internal `1->1` arcs, and the leaving boundary arc.  If none changes,
the entire subpath remains inside one unchanged path fragment.  A new deck
phase can only rotate its coordinate name; it cannot alter its length.  Thus
every residence-producing successor exchange must hit every resulting
size-three or size-four run-tail hyperedge.

The audit greedily exhibits 169 pairwise vertex-disjoint run hyperedges.
Every hitting set therefore has size at least 169.  In particular:

> No exchange changing at most ten labelled successor tails can turn this
> frozen complement-dual seed into a floor-four resident owner cycle.

This corrects and supersedes an earlier unsound two-boundary-tail argument:
changing an internal `1->1` arc can destroy a run, so the full `ell+1`-arc
hyperedge is essential.  The corrected obstruction is independent of
topology, voltage, J7, and palette acceptance.  It is not a no-go for another
complement-dual seed or for a change with successor-tail support at least 169.

## 7. Residence state for a larger enumerator

After cutting every changed successor tail, each retained oriented fragment
should carry the following exact boundary state:

1. fragment owner count and net voltage;
2. an `internal_ok` bit;
3. for every coordinate, the endpoint bits, prefix and suffix positive-run
   lengths capped at four, and an `all_one` bit.

When a fragment is deck-rotated, rotate the coordinate-indexed state.  On a
join, the only newly bounded positive run is the old suffix plus the new
prefix; it must be zero or at least four.  Update capped prefix/suffix and
`all_one` in the usual concatenation rule.  Finally apply the same rule to
the closing seam.  Before this DP, reject any support whose changed tails do
not hit every full run-tail hyperedge from Section 6.

## 8. C++ enumerator checklist

A proof-safe support-ten non-dual enumerator must therefore:

1. bind the exact seed TSV by hash and reconstruct all incidence IDs/shifts;
2. select perfect incidence matchings `D'` and `H'`, edge-disjoint;
3. force one of the four-row J7 incidence pairs in Section 5;
4. define the labelled successor arc from `H'^{-1}D'` and require exactly ten
   changed tails, including the corresponding five-tail closure seed;
5. enforce exact head balance and rank-8 facet balance (5.1);
6. require the singleton/big cross pattern (3.4) and literally traverse one
   1,430-owner quotient cycle;
7. compute (4.1) and require nonzero voltage;
8. replay all affected rank-10 and rank-7 turn loads using (4.4);
9. apply the full run-tail-hyperedge screen, followed by exact physical replay
   or the fragment boundary automaton; and
10. report this support-ten face residence-UNSAT, while preserving `UNKNOWN`
    under every unrelated time, node, or resource cap.

## 9. Audit artifacts

```text
scratch/audit_h2_k17_complement_dual_support10_interface_20260801.py
scratch/h2_k17_complement_dual_support10_interface_20260801.audit.json
```

The JSON contains the first sixteen disjoint full-span run hyperedges, the
literal J7 incidence rows, incumbent owner states, closure seeds, topology,
voltage, and palette histograms.  No handoff or index is modified by this
lane.
