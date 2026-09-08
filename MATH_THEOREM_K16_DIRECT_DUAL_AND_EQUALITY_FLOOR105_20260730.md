# K16 direct dual and equality theorem: the separated master needs at least 105 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete catalogue of 211,604
direction-coherent, positive-residence-safe seams, let

\[
 x\in\{0,1\}^{211604},\qquad
 \sum_{e\in\delta^+(v)}x_e=\sum_{e\in\delta^-(v)}x_e
 \quad(v\in V),
\]

and suppose every one of the 93 fixed q<=3 defects is serviced at least once.
Then

\[
                         C:=\sum_e x_e\ge105.          \tag{0}
\]

Consequently every physical separated-port repair in this catalogue needs at
least 105 nonold seams, hence at least 105 source cuts.

This statement omits the physical at-most-one port-capacity condition.  It is
therefore a lower bound for the stronger separated-port master.  It is
source-relative and does not constrain a different K16 carrier or a
non-separated transformation.

The Boolean hypothesis in (0) is material.  The scale-two dual below proves
the weaker floor 104 for arbitrary nonnegative real, rational, or integral
seam multiplicities.  The equality obstruction proving 105 is complete for
binary catalogue selections; it is not claimed for a relaxation allowing the
same directed seam to be used more than once.

## 1. Exact scale-2 direct dual: fractional floor 103.5

There are nonnegative integer target weights `b_t in {1,2,4}` and an integer
port potential `y_v in [-4,2]` such that every seam `e:u->v` satisfies

```text
sum_{t in H(e)} b_t <= 2 + y_v - y_u.                    (1)
```

The raw-binary checker verifies (1) on all 211,604 seams using exact integer
arithmetic.  The 93 target weights sum to

```text
sum_t b_t = 207.
```

For a balanced selected circulation of `C` seams, the potential telescopes.
Servicing every target therefore gives

```text
2 C >= 207,
```

so `C>=104`.

This continuous bound is tight.  An exact denominator-four primal supported
on 174 dual-tight seams has objective

```text
414/4 = 207/2 = 103.5.
```

An independent raw-binary replay verifies exact endpoint balance, service
numerator four for every target, and zero dual slack on every supported seam.
Thus no stronger *fractional* service+balance inequality exists; the next step
is genuinely integral.

## 2. The exhaustive equality-104 split

For a seam define its exact nonnegative dual slack

```text
s(e) = 2 + y_v - y_u - sum_{t in H(e)} b_t.
```

At `C=104`, telescoping gives

```text
208 = weighted_service + total_slack.
```

The minimum weighted service is 207.  All quantities are integers and every
target weight is positive.  Hence exactly two cases exist.

1. **No repeat:** every target is serviced once and total slack is one.
2. **One weight-one repeat:** total slack is zero, every target is serviced
   once except one additional occurrence of a weight-one target.

There is no third case.

Every selected arc of a balanced finite directed subgraph lies on a directed
cycle.  Accordingly, each case may first discard arcs outside cyclic SCCs of
its admissible slack layer without losing a solution:

```text
case                         admissible   cycle-eligible   providers
no repeat, slack total 1       74,879          15,340         3,399
weight-one repeat, slack 0     41,491           1,930         1,054
```

Exact CP-SAT replays find both models infeasible even when port capacity is
omitted.  More importantly, the all-tight case has a short solver-free parity
obstruction, and the remaining one-slack case has an independently checkable
CNF/DRAT certificate.

## 3. Solver-free obstruction to the all-tight repeat case

On the cycle-eligible tight-seam graph define

\[
\begin{aligned}
 T_1&=\{35044,36935,40066\},&P_1&=\{12545,12560,12575\},\\
 T_2&=\{33337,50976,58385\},&P_2&=\{12554,12569,12584\}.
\end{aligned}
\]

Direct raw replay proves, for each cycle-eligible tight seam \(e:u\to v\)
and for \(i=1,2\),

\[
 |H(e)\cap T_i|\equiv
  \mathbf 1_{\{u\in P_i\}}+\mathbf 1_{\{v\in P_i\}}\pmod2. \tag{5}
\]

If \(x\) is any nonnegative integral balanced selection of tight seams,
sum (5) with coefficient \(x_e\).  Endpoint balance makes the right side

\[
 \sum_{p\in P_i}\bigl(\deg_x^+(p)+\deg_x^-(p)\bigr)
 =2\sum_{p\in P_i}\deg_x^+(p)\equiv0\pmod2.             \tag{6}
\]

Thus the total service multiplicity on each \(T_i\) is even.  On the
all-tight equality face every target occurs once and one price-one target
\(r\) occurs once more.  The service sum on \(T_i\) is even exactly when
\(r\in T_i\).  Hence \(r\in T_1\cap T_2\), impossible because the displayed
triples are disjoint.

It is enough to check (5) on cycle-eligible tight seams: every positive edge
of a finite balanced directed multigraph lies on a directed cycle, hence its
endpoints lie in one strongly connected component of the full tight graph.
The raw verifier checks all 1,930 such seams and records the six nonzero
seams for each parity identity.  This rules out the repeat case even with
arbitrary integral seam multiplicities and without port capacity.

## 4. Exact no-repeat CNF and checked DRAT certificate

The deterministic emitter encodes, for each case:

- one Boolean variable per cycle-eligible physical seam;
- exact endpoint balance `sum(out)=sum(in)` at every port;
- exactly 104 selected seams;
- the corresponding exact service multiplicities and slack total;
- **no** at-most-one port-capacity constraints.

The encoding is an exact existential extension, not a short-window proxy.
For each port it first cancels seam variables common to the incoming and
outgoing rows, then encodes

\[
 \sum x_{\rm out}+\sum(1-x_{\rm in})=|E_{\rm in}|,
\]

which is identically \(\sum x_{\rm out}=\sum x_{\rm in}\).  PySAT's
sequential counters are used only as standard equisatisfiable encodings of
the displayed exact cardinalities.  SCC deletion is sound by the directed
cycle observation above.  In the no-repeat instance the 74,879 seams of
slack at most one reduce to 15,340 cycle-eligible Boolean seams; the formula
then imposes exactly 104 seams, service exactly one at every target, and
exactly one selected slack-one seam.  These are precisely the first equality
case and no additional physical condition.

The full deterministic CNFs have the following frozen hashes:

```text
case                 variables    clauses      SHA-256
no repeat            3,262,994    6,521,464    e1b89dd9da8a524baf1ed314eb6256d8cb0e9038e104043b94f68a9c4f7507d4
weight-one repeat      386,389      772,722    26ad302c30a9b537eb69f58348cb6f573ee6dee468f0bcc2ab42cf93d30feea8
```

`drat-trim` extracts small unsatisfiable cores and core proofs:

```text
case                 core clauses   core CNF   core DRAT
no repeat                  25,206      475 KB      427 KB
weight-one repeat             130        2 KB        3 KB
```

The bundle checker independently verifies two facts for each case:

1. every compact core clause occurs in the deterministic full CNF (literal
   order ignored, multiplicity respected);
2. `drat-trim` accepts the compact core proof with `s VERIFIED`.

The no-repeat core is a 25,206-clause submultiset of the deterministic full
formula, and its DRAT proof verifies.  Therefore the no-repeat equality case
is UNSAT.  The repeat CNF/DRAT pair in the table is a redundant independent
confirmation of the parity proof in Section 3.  Thus both exhaustive binary
equality cases are impossible.  Combined with the scale-2 lower bound,

```text
C >= 105.
```

QED (exact arithmetic plus a machine-checked finite no-repeat theorem).

## Scope

The theorem uses only binary seam selection, endpoint balance, and service of
the 93 frozen q<=3 defects in the source-relative
q<=3/upper-width-four seam catalogue.  It does not use port capacity,
separation, reverse-edge, q1, survivor, residence, or deeper-shadow rows.
The word "unrestricted" refers only to retaining all 211,604 seams in this
frozen catalogue.  It does not mean arbitrary K16 rethreads, and (0) does not
cover repeated use of one seam.

## Reproduction

The exact dual replay is:

```text
python3 scratch/audit_k16_direct_cut_dual_scale2_exact_20260730.py \
  --binary scratch/k16_len8_source_seam_ledger_20260730.bin \
  --exploration scratch/k16_direct_cut_dual_20260730.exploratory.json \
  --output NEW_SCALE2_AUDIT.json
```

The equality CNFs are regenerated by:

```text
python3 scratch/emit_k16_floor104_equality_cnf_20260730.py \
  --binary scratch/k16_len8_source_seam_ledger_20260730.bin \
  --certificate scratch/k16_direct_cycle_dual_exact_20260730.audit.json \
  --case CASE --output CASE.cnf --manifest CASE.manifest.json
```

where `CASE` is `no_repeat` or `repeat_weight1`.  The compact proofs are
checked with standard `drat-trim CORE.cnf CORE.drat`.

The frozen CNF manifests were originally emitted by driver SHA
`49a793ed...` using certificate SHA `a89f9166...`.  The retained emitter SHA
`c5997a40...` differs from that driver in exactly one provenance pin: it uses
the independently replayed certificate SHA `29b4aae4...`.  The two
certificates have exactly equal `target_weights` and `vertex_potential`
arrays, so the regenerated DIMACS CNFs have the frozen byte hashes above;
only newly generated manifest metadata records the newer driver and
certificate hashes.

## Frozen lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

independent standard-library raw replay / audit
  scratch/audit_ad_k16_direct_scale2_floor104_rawstream_20260730.py
  a6b434c787be1c0a842c95cc3dd8c2cff0918c910ba5719f7f3e36abe52c9830
  scratch/ad_k16_direct_scale2_floor104_rawstream_v3_20260730.audit.json
  1f5a78e4e6a97e3f2a52fb81d60962cdc0ee4effd5e92e7db3e2d37c81a37313

scale-2 exact checker
  scratch/audit_k16_direct_cut_dual_scale2_exact_20260730.py
  3b97379f2dbaa7f9ca64a8d40d316dfceff47c3acc327fb00fe24b5e98056ebd

scale-2 exact audit
  scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json
  a89f9166a1f6eade1db20ea3b76d15aad2187eac48e23e0566b6968972b18bb2

denominator-four primal
  scratch/k16_floor104_scaled_primal_D4_20260730.audit.json
  74a7c2a48355b9827b433385982bb42c118fb4d1506e975a53efa023d230f136

independent primal checker / audit
  scratch/audit_k16_floor104_scaled_primal_independent_20260730.py
  078665a907ed526be6ac50a9fac84e4be3365487c9513c6e5c3153b0b301a62b
  scratch/k16_floor104_scaled_primal_D4_independent_20260730.audit.json
  ce286af2cfc56732bc57a4621e808b49d83f3e3c9cb0959b8a6da19860d84ae0

equality-case CNF emitter
  scratch/emit_k16_floor104_equality_cnf_20260730.py
  c5997a40aa13cd274224a3884f9af5f87087b574a7fd9139d824ebc7d52582b6

DRAT bundle checker
  scratch/audit_k16_floor104_drat_bundle_20260730.py
  fd450ebec05643dd05a7beae4b181f53079c6f817e6569c58eea2f6d3e71d2bb

solver-free repeat parity verifier / audit
  scratch/threadA_verify_k16_floor104_repeat_parity_20260730.py
  8bbcba60ebd3e9d7a1e9b3fa6b6b55a46094aef5d287dcbc90fbc960bc8487b6
  scratch/threadA_k16_floor104_repeat_parity_v2_20260730.audit.json
  e6bfb1ce649b685980ab483920a7655ce03e236fc03d37dac2fe9b0d3ef7c9a9

no-repeat manifest / compact core / compact proof / bundle audit
  scratch/k16_floor104_no_repeat_cnf_20260730.manifest.json
  2ef0568d1e5b8f64f04e26b49504d536c1fb4669f26deb9c2eb40f8e60136b08
  scratch/k16_floor104_no_repeat_core_20260730.cnf
  c8be67536616d3bdd6fb9ed54e12e214b7abedc6c45860dfe52dd115a368d69c
  scratch/k16_floor104_no_repeat_core_20260730.drat
  80f00666ac026795fc1e1979b20efefee7ea1744ad55ce0f8180405579873da9
  scratch/k16_floor104_no_repeat_drat_bundle_20260730.audit.json
  c60888ce8123d09ca5c07563e105bbd3aecdc87efc6395e5a15267862deb3119

weight-one-repeat manifest / compact core / compact proof / bundle audit
  scratch/k16_floor104_repeat_weight1_cnf_20260730.manifest.json
  0cca10d4fa06f9d46dc8a2b1308d3da33d5789e3ccb01630ec19d489d358cff7
  scratch/k16_floor104_repeat_weight1_core_20260730.cnf
  b17e747773db8399c112434a8e947151bf7a5cd712dbc6341cc64b0f95c0e738
  scratch/k16_floor104_repeat_weight1_core_20260730.drat
  04c9fed6f8331b36b142c04254c94e8649ae1244f2e96a03186a550dadc006f8
  scratch/k16_floor104_repeat_weight1_drat_bundle_20260730.audit.json
  396b42079d0672fa89b13f0afd5341f7bcbfd7bd08807dff5ba0f647e200f15b

size-accounted proof-bundle builder / manifest
  scratch/build_k16_floor105_proof_bundle_manifest_20260730.py
  165fdaa115ca08877ee98d425e587e54c50ee60fd1d85ee96cbd4783e3e1c0a4
  scratch/k16_floor105_proof_bundle_20260730.manifest.json
  05aacd9f090cc5e09905bdd694bc195eacf2b01dec945fe67ff804e186509b37
```

The retained bundle has 47 artifacts totalling 11,527,203 bytes, including
the raw seam ledger.  The two deterministic full CNFs and superseded original
DRAT traces total 163,344,132 bytes and are intentionally omitted: the full
CNF byte streams regenerate to the frozen CNF hashes (with fresh manifest
metadata as explained above), while the much smaller retained core CNF/DRAT
pairs independently verify UNSAT.
