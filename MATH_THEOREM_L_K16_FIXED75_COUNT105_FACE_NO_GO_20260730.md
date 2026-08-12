# K16 fixed-75 count-105 face: exact portal-permutation no-go

> **Subsequent authoritative update (2026-07-30).** The authenticated
> five-lock automaton now excludes count 105 in the full frozen
> source-relative balance/service relaxation, not merely on this face. This
> note remains useful as the structural portal/cycle explanation for the
> named `F75` face; any statement below that global count 105 was still open
> is superseded by handoff item 1934.

Date: 2026-07-30  
Lane: L, constructive count-105 rounding / exact fixed-face obstruction  
Status: **proved on the authenticated fixed-75 service+balance face; no global
count-105 conclusion**

## 1. Frozen data and scope

The authenticated raw seam ledger is

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

The scale-two direct certificate is

```text
scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json
SHA256 a89f9166a1f6eade1db20ea3b76d15aad2187eac48e23e0566b6968972b18bb2
```

The denominator-four primal and its exact cycle decomposition are

```text
scratch/k16_floor104_scaled_primal_D4_20260730.audit.json
SHA256 74a7c2a48355b9827b433385982bb42c118fb4d1506e975a53efa023d230f136

scratch/l_k16_d4_cycle_blocks_20260730.audit.json
SHA256 b9dca4325deac03fa8575ad755db2cf54b777f1dd8811009d2e35f25e5eaa7a8
```

It contains three integral directed `C15` blocks and one `C30` block.  Their
union, denoted `F75`, has exactly 75 seams on 75 ports and covers exactly 60
of the 93 service targets, once each: 45 targets of price two and 15 targets
of price four.  The 33 residual targets have price histogram

```text
1^15 2^15 4^3
```

and total price 57.

This note studies only selections containing exactly `F75`.  Capacity then
forces the other 30 seams to avoid its 75 ports.  We impose only the frozen
93-target service, directed balance, count 105 and, when stated, port capacity.
We do **not** impose q1, separation, reverse-edge, residence, survivor,
deeper-shadow or literal-compiler constraints.  Therefore an impossibility in
this note is a valid no-go for the fixed face, while it says nothing about a
count-105 selection not containing `F75`.

## 2. Restitution identity

For seam `e:u->v`, let `H(e)` be its frozen service-target set, let `b_t` be
the direct target price and let `y` be the integer vertex potential from the
direct certificate.  Define

\[
 s_e=2+y_v-y_u-\sum_{t\in H(e)}b_t.
\]

The certificate verifies `s_e>=0` for every one of the 211,604 seams.
For a balanced count-105 selection with target multiplicities `mu_t`, summing
over seams cancels the potential and gives

\[
 \sum_t b_t(\mu_t-1)+\sum_e s_e=2\cdot105-207=3.       \tag{2.1}
\]

Write

\[
 R=\sum_t b_t(\mu_t-1),\qquad S=\sum_e s_e.
\]

Thus `R,S` are nonnegative integers and

\[
 R+S=3.                                                \tag{2.2}
\]

Inside the fixed face, the remaining 30 seams must cover all 33 residual
targets.  Equation (2.2) is exact, not merely a lower bound.

## 3. The five target-group syndromes

Partition the fifteen price-one residual targets into

\[
\begin{aligned}
G_0&=\{35044,36935,40066\},\\
G_1&=\{37320,41102,47364\},\\
G_2&=\{33906,36417,51235\},\\
G_3&=\{33337,50976,58385\},\\
G_4&=\{41872,49436,61960\}.
\end{aligned}                                         \tag{3.1}
\]

For a seam `e`, define its five-bit target-group syndrome by

\[
 \chi_i(e)=|H(e)\cap G_i|\pmod2.                       \tag{3.2}
\]

For `S=2,R=1`, the unique repeat has price one, so the required total syndrome
is

\[
 \mathcal A_2=\{11111\oplus e_i:0\le i<5\}
              =\{15,23,27,29,30\}.                    \tag{3.3}
\]

For `S=3,R=0`, every residual target occurs once, so the required syndrome is

\[
 \mathcal A_3=\{11111\}=\{31\}.                       \tag{3.4}
\]

For both branches every seam hitting an `F75` target may be deleted from the
candidate graph.  Such a hit repeats a target of price at least two, exceeding
the repeat budget one in the `S=2` branch and the repeat budget zero in the
`S=3` branch.  This deletion is exact for these branches.

After deleting the fixed ports and all fixed-target hits, the clean pools are

```text
tight s=0 arcs       38,935
slack-one portals    32,280
slack-two portals    73,713
slack-three portals  29,468
```

The tight graph has 12,816 strongly connected components.  Within each tight
SCC, the verifier constructs a phase `phi:V->F_2^5` satisfying

\[
 \chi(e)=\phi(\operatorname{tail}e)
          \oplus\phi(\operatorname{head}e)             \tag{3.5}
\]

on every internal tight arc.  Hence every all-tight directed closed walk has
syndrome zero.  For a cross-SCC tight arc, the reduced label is

\[
 \lambda(e)=\phi(\operatorname{tail}e)\oplus\chi(e)
             \oplus\phi(\operatorname{head}e).         \tag{3.6}
\]

The SCC condensation is a DAG.  Exact 32-state propagation on this labeled DAG
therefore gives precisely the set of syndromes of every tight path between any
queried pair of portal endpoints.

## 4. Portal-permutation lemma

**Lemma 4.1 (positive-seam permutation).**  Let `X` be a balanced
capacity-one directed selection, and suppose exactly `r` selected seams have
positive slack.  Then those `r` seams carry a permutation `pi` with the
following property: for every positive seam `e`, the selected graph contains
an all-tight directed path from `head(e)` to `tail(pi(e))`.  The cycles of `pi`
are exactly the cyclic orders of the positive seams on the directed-cycle
components of `X`.

**Proof.**  Balance and in/out capacity one decompose `X` into vertex-disjoint
directed simple cycles.  On each such cycle containing positive seams, map each
positive seam to the next positive seam in cyclic order.  Every intervening
seam is tight.  Taking the disjoint union of these cyclic maps gives `pi`.
\(\square\)

For `r<=3`, the possible permutation types are therefore:

```text
r=1: one cycle;
r=2: identity, or one transposition;
r=3: identity, transposition plus fixed point, or one genuine 3-cycle.
```

The verifier enumerates a relaxation of every type: it requires distinct
positive tails and distinct positive heads, but it does not require the
intervening tight paths to be internally port-disjoint, short enough, or
service-compatible.  Exclusion in this enlarged space is therefore sound.

## 5. Exact complete `S=2` and `S=3` census

The clean graph has the following numbers of individual positive portals with
a tight return path:

```text
slack 1: 15
slack 2: 47
slack 3: 25
```

Exact endpoint joins, SCC path-syndrome propagation, and XOR convolution give:

| total slack pattern | permutation type | endpoint-reachable candidates | allowed-syndrome candidates |
|---|---:|---:|---:|
| `2` | one cycle | 47 | 0 |
| `11` | identity | 105 | 0 |
| `11` | transposition | 118 | 0 |
| `3` | one cycle | 25 | 0 |
| `21` | identity | 678 | 0 |
| `21` | transposition | 399 | 0 |
| `111` | identity | 455 | 0 |
| `111` | transposition plus fixed point | 1,557 | 0 |
| `111` | genuine 3-cycle, modulo cyclic rotation | 952 | 0 |

The 952 oriented genuine 3-cycles represent 497 unordered portal triples;
455 of those triples admit both cyclic orientations.  Only four SCC-pair
syndrome queries occur in that last family.  Each is diagonal and has reduced
path-syndrome set `{0}`.  After restoring endpoint phases and portal labels,
the union of attainable total syndromes is

\[
\{1,2,4,7,8,11,13,14,16,19,21,22,25,26,28\},          \tag{5.1}
\]

which excludes 31.  Thus the genuine three-portal macro fails before length,
internal capacity or service recourse is imposed.

It follows that no fixed-face residual packet exists with `S=2` or `S=3`.

## 6. Tight-cycle/filler decomposition

The clean tight graph has exactly six nontrivial SCCs: five directed triangles
and one directed 45-cycle.  The triangles are:

```text
207242,207743,207494 : 36599,57059,56439
207292,207794,207544 : 47343,40430,48583
207343,207846,207593 : 64398,61918,48092
207393,207894,207641 : 63416,63261,58301
207445,207945,207693 : 51067,61297,60987
```

They are vertex-disjoint and partition the fifteen price-two residual targets.
The `C45` alternates the fifteen double-provider arcs with fifteen price-two and
fifteen price-one single-provider arcs, covering every residual price-one and
price-two target twice.  It is too long to be a separate filler in a 30-seam
no-repeat packet.

Consequently, before the syndrome no-go, any genuine three-portal macro could
have been completed only by a subset of the five triangles.  If `j` triangles
were used, the macro would have had `30-3j` seams, including three positive
seams, and hence tight-path length

\[
 L=27-3j\in\{12,15,18,21,24,27\}.                     \tag{6.1}
\]

All three residual price-four targets are forced onto the macro: every one of
their tight or positive providers crosses singleton tight SCCs, so no pure
tight filler can service them.  This recourse ledger is exact but is not needed
for the final no-go, since Section 5 eliminates every macro syndrome already.

## 7. Completing the fixed-face no-go

The remaining restitution cases were frozen earlier:

1. `S=0,R=3`.  The exact cycle-lattice audit
   `scratch/threadB_k16_c105_cycle_lattice_modular_v2_20260730.audit.json`,
   SHA256
   `1d35ce7657becc2a9d49e5df280dbf5c34ea8312aafcbf331580b70816b910ae`,
   eliminates all 1,580 slack-zero repeat branches already in the larger
   global balanced-service lattice.

2. `S=1,R=2`.  The exact fixed-face syndrome-DAG audit
   `scratch/l_k16_fixed75_s1_syndrome_dag_v2_20260730.audit.json`, SHA256
   `41567cde5baed2208be1e8dcfea23e0a84f35b066b471cfa2c63b31d7f453f04`,
   payload
   `0c360fd5af1da0656a6647b86ce0d1f7b42177e0e18b3758328a66acb720be14`,
   eliminates the unique slack-one portal branch.  Its 107 return portals in
   the deliberately larger graph attain only the five unit syndromes, disjoint
   from every repeat-price-two requirement.

3. `S=2,R=1` and `S=3,R=0` are eliminated by Section 5.

These cases exhaust (2.2).  Therefore:

**Theorem 7.1 (fixed-75 face no-go).**  There is no balanced capacity-one
count-105 selection from the authenticated K16 seam bank which contains the
frozen block `F75` and services all 93 frozen targets.  Equivalently, `F75`
cannot be completed by a 30-seam packet on its unused ports.

This theorem is strictly face-local.  It neither proves that the unrestricted
service+balance optimum exceeds 105 nor excludes a different integralization
of the denominator-four primal.

## 8. New verifier and artifact

The complete `S=2/S=3` verifier is

```text
scratch/audit_l_k16_fixed75_pattern111_macro_20260730.py
SHA256 c35f7d3e51c33675015a6a76091b8d9ec13d249179a5f8af15a4b94cf12aa3c4
```

Its frozen output is

```text
scratch/k16_fixed75_s2_s3_positive_patterns_20260730.audit.json
SHA256 56b844ae5d7119cfcdef0e4768840754f08c240be67ee45e2158920b7760472f
payload 4ad77128ca0c7f13edaad68c681d1cf71d78a6e6264c60ad9ed35fcc9b9f95cb
```

The capped H100 CPU run used one process, a 2 GiB virtual-memory cap and a
600-second wall cap.  It finished in 2.36 seconds with maximum RSS 156,560 KiB.

```text
scratch/k16_fixed75_s2_s3_positive_patterns_20260730.resource.txt
SHA256 5cb28c01f9b9700584991d8b3fd0b9ece58060e5de3557cf3576ebeed357c453

scratch/k16_fixed75_s2_s3_positive_patterns_20260730.stdout.txt
SHA256 2fb5fdc75c3b4cd6ca0a927ff40bfc4153799eed4735edf948ab27e57ac2192f
```

The artifact freezes hashes of all three positive portal pools, the clean
tight rows, the SCC assignment and phase, the six literal tight SCC cycles,
all self-cycle masks, both swapped-pair mask catalogues, all 952 canonical
genuine-three-cycle rows, the four decisive component queries, and the complete
total-syndrome histogram.

## 9. Audit boundary

The genuine-three-cycle construction and syndrome propagation were
independently audited before the unified run.  That audit checked SCC phases,
cross-SCC labels, endpoint translation, cyclic-rotation canonicalization,
positive-endpoint capacity, XOR convolution, the `952/497/455` arithmetic and
the exclusion of syndrome 31.  It also identified and caused correction of a
field-label issue: the stored seam histograms are target-group syndromes, not
endpoint-balanced syndromes.

The unified `2,11,3,21,111` extension uses the same audited path-mask engine.
The exact one- and two-positive permutation loops and all zero-survivor counts
are frozen in the new artifact.  No positive witness exists, so there is no
literal all-depth factor replay to perform.
