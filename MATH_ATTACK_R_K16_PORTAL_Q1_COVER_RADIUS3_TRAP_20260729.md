# Lane R: the q1-cover-preserving portal has a radius-three mixed-Hall trap

Date: 2026-07-29

## 1. Result and scope

Let (Q) be the physical lift of the radius-five portal factor

```text
scratch/k16_q1_endpoint_resume1_static_portal_radius5_20260729.json
SHA-256 5ae4948c96a32b592871c84ba9fe34301a40992ec1592175edd2626249e01af8
```

and let (R) be the fully resident two-component PBBS endpoint

```text
scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
SHA-256 d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951
```

Both are simple spanning degree-two factors on the 12,870 rank-eight
subsets of `[16]`.  The factor (Q) contains every physical lower and upper
q1 colour; (R) has no positive residence run of length below four.

The original (Q/R) circulation is infeasible by an elementary upper-q1,
motif, and degree contradiction.  There is a unique minimum-radius physical
alternating (C_4) which preserves complete lower and upper q1 support and
changes a row of that certificate.  It destroys the displayed upper-only
core, but the resulting endpoint has a different mixed lower/upper Hall core.

For a second simple spanning degree-two factor \(Q'\) on the same fixed
12,870-vertex middle deck, cancel the common edges and put

\[
D=Q\setminus Q',\qquad A=Q'\setminus Q,\qquad
r=|D|=|A|.
\]

Call \(r\) the **replacement radius**.  More sharply:

> **Radius-three trap.**  For every simple spanning degree-two \(Q'\) on the
> same fixed middle deck with replacement radius \(r\leq 3\) and complete
> lower and upper q1 support, the fixed \((Q'/R)\) overlay fails the exact
> mixed-palette unit Hall test.

This theorem is finite and solver-free after the saved catalogues are
replayed.  It is not a no-go for replacement radius at least four, a
simultaneous change of (R), non-simple edge tokens, AA-enabled oriented-port
search outside (Q\cup R), deeper shadows, connectivity, `COMP3`, or a
literal k16 word.

## 2. The original six-row upper core

In the fixed overlay write a blue variable for removal of a (Q\setminus R)
edge and a red variable for addition of an (R\setminus Q) edge.  The
coordinate-zero length-two motif has closure

\[
b_1=(50531,51042),\quad
k=(50531,52547),\quad
b_3=(52547,56642),
\]

where (k) is common and therefore cannot be removed.  The relevant upper
provider rows are

\[
\begin{array}{c|c|c}
\text{colour}&Q\setminus R&R\setminus Q\\ \hline
51043&\{b_1\}&\varnothing\\
56643&\{b_3\}&\{r=(55619,56579)\}\\
55747&\{(55491,55619)\}&\varnothing\\
63811&\{(55619,63747)\}&\varnothing.
\end{array}
\]

Thus (b_1) cannot be removed.  The motif row forces removal of (b_3),
which forces addition of (r).  At vertex 55619 the two removable blue
incidences are exactly

\[
(55491,55619),\qquad(55619,63747),
\]

and the last two singleton upper rows forbid both removals.  Degree balance
therefore forbids (r), a contradiction.

This is the six-row certificate stored in

```text
scratch/k16_resume1_portalq1_upper_unit_hall_core_20260729.json
SHA-256 fa04c087d12731325446c977c18971bcd6c2b0ffe68d8eceb1284875b9870f5e
```

and is stronger than a CP-SAT `INFEASIBLE` transcript.

## 3. The unique minimum-radius cover-preserving pretrade

Delete

\[
D=\{(50283,50507),(50531,52547)\}
\]

and add

\[
A=\{(50283,50531),(50507,52547)\}.
\]

These four edges form a physical alternating (C_4), so incidence is
preserved at every vertex.  The affected q1 loads are

\[
\begin{array}{c|cc}
\text{lower colour}&\text{before}&\text{after}\\ \hline
50251&2&1\\
50275&1&2\\
50499&1&1
\end{array}
\qquad
\begin{array}{c|cc}
\text{upper colour}&\text{before}&\text{after}\\ \hline
50539&1&1\\
52555&1&2\\
52579&2&1.
\end{array}
\]

Therefore both q1 supports remain complete.  The exchange is **not**
strict-token or load-vector neutral: its nonzero signed load changes are

\[
-e_{50251}+e_{50275}
\quad\text{and}\quad
-e_{52579}+e_{52555}.
\]

The correct term is q1-cover-preserving.

Literal replay gives four components of lengths

\[
515,515,705,11135,
\]

zero lower/upper q1 holes, and 2,251 short positive runs with histogram

\[
1^{135}2^{915}3^{1201}.
\]

Thus the trade merges two portal components but worsens residence by one.
It deletes the common motif edge (k), so the Section 2 proof disappears.
There are no pointwise static Hall blockers against (R), and upper-only
unit propagation reaches a fixpoint.  Neither fact implies circulation
feasibility.

### Exact radius-two exhaustion

For a simple degree-preserving nonempty trade, cancellation of common edges
leaves alternating circuits.  Replacement radius one is impossible: one
deleted and one added edge with the same endpoint-incidence vector are the
same undirected edge.  At radius two the support must be one alternating
(C_4).

The complete physical (C_4) enumeration for (Q) contains 61,515 circuits,
of which 2,250 preserve both complete q1 supports.  A (C_4) changes the
Section 2 certificate exactly if it

1. deletes one of its five displayed Q/common edges; or
2. adds a provider of one of upper colours
   (51043,55747,56643,63811).

A change to the degree row at 55619 necessarily deletes one of the two
displayed Q incidences and is already covered by item 1.  Exactly one of the
2,250 cover-preserving (C_4)'s meets this complete predicate: the exchange
above.  Hence it is the unique minimum-radius exchange invalidating this
particular certificate.

The materialized factor and deterministic exhaustive-enumeration artifact are

```text
scratch/k16_portalq1_core_break_c4_pretrade_20260729.json
SHA-256 0d5fc8d2c1082b9be44f3b78b1a6d212908ee6f76fbfbcd9582006454ab3926a

scratch/k16_portalq1_core_break_c4_pretrade_20260729.audit.json
SHA-256 f15fc54708ad4dc6dc0344ea3afac95adee868805af9ec76f4da22d536f2aa46
```

## 4. The translated mixed-palette core

Let (Q_1=(Q\setminus D)\cup A).  In (Q_1/R), define

\[
e_1=(37531,37785),\quad
e_2=(37531,41627),\quad
e_3=(41627,41657),
\]

and

\[
f=(49819,53787),\quad
g=(49819,49881),\quad
\rho=(33467,49819).
\]

There is a coordinate-one length-two motif with closure

\[
\{e_1,e_2,e_3\}.
\]

The complete relevant provider rows are

\[
\begin{array}{c|c|c}
\text{colour}&Q_1\setminus R&R\setminus Q_1\\ \hline
L33435&\{e_2\}&\{\rho\}\\
L37529&\{e_1\}&\varnothing\\
L41625&\{e_3\}&\varnothing\\
L49691&\{f\}&\varnothing\\
U49883&\{g\}&\varnothing.
\end{array}
\]

The singleton rows lock (e_1,e_3,f,g).  The two selected (Q_1)-edges at
vertex 49819 are (f,g), so degree balance forbids every red addition there,
including \(\rho\).  The first row then locks (e_2).  No motif edge can be
removed, a contradiction.

This proof is recorded by the both-palette unit audit

```text
scratch/k16_portalq1_core_break_c4_both_unit_hall_20260729.audit.json
SHA-256 c8c15dbec89d835329d7c205f348caaa04c2f202ae3dc1137388497b3e0abfcd
```

The same socket-49819 obstruction previously appeared, under the old motif
index 148, in
`MATH_THEOREM_H_K16_STRICT_TOKEN_C6_PORTAL_CHAIN_AND_TRAP_20260729.md`.
The present (C_4) result shows that allowing q1 load drift does not remove
it.

## 5. One further square is still insufficient

At (Q_1), the complete physical census contains 61,511 alternating
(C_4)'s and 2,250 q1-cover-preserving ones.  Exactly three change a literal
or provider row in the translated core:

\[
\begin{aligned}
&\{(33467,37562),(33499,33530)\}
 \to\{(33467,33499),(33530,37562)\},\\
&\{(37533,38549),(38553,38577)\}
 \to\{(37533,38553),(38549,38577)\},\\
&\{(41689,41929),(45721,45769)\}
 \to\{(41689,45721),(41929,45769)\}.
\end{aligned}
\]

All three remain q1-complete and have zero pointwise static blockers.  Exact
mixed-palette propagation nevertheless proves each overlay infeasible.  The
first moves the obstruction to a five-row core at vertex 33707; the other two
retain variants of the socket-49819 core.  A non-touching (C_4) leaves the
displayed Section 4 proof verbatim.

The census is

```text
scratch/k16_portalq1_stage2_core_break_c4_20260729.audit.json
SHA-256 6d99bf8a09a7b3b0bdb53988a372610bfe92e6fefcb2b0f633a2b4e7fcd0145b
```

## 6. Complete replacement-radius-three exhaustion

A degree-balanced trade of total replacement radius three cannot have two
nonempty alternating components, because each component has replacement
radius at least two.  It is therefore one alternating (C_6).

To change the Section 2 certificate, such a (C_6) must either

1. delete one of its five displayed Q/common edges; or
2. add a non-Q Johnson provider for one of its four upper rows.

If neither event occurs, every literal and provider row in Section 2 is
unchanged, so that original contradiction proves infeasibility immediately.

There are 1,975 raw connected (C_6) descriptions summed over the five
deleted-edge targets.  Independently, the four upper colours have 140
non-Q Johnson provider edges; complete enumeration through them produces
1,758 raw descriptions.  After set deduplication and exact q1-support replay,
the union has precisely six cover-preserving (C_6)'s:

```text
D0 = (17771,25707) (50283,50507) (50531,52547)
A0 = (17771,50531) (25707,50283) (50507,52547)

D1 = (47395,55587) (47458,63810) (55619,63747)
A1 = (47395,47458) (55587,55619) (63747,63810)

D2 = (47395,55587) (47458,63810) (55619,63747)
A2 = (47395,47458) (55587,63747) (55619,63810)

D3 = (50283,50507) (50515,50522) (50531,52547)
A3 = (50283,50531) (50507,50522) (50515,52547)

D4 = (50475,50979) (50531,51042) (50538,50986)
A4 = (50475,50986) (50531,50979) (50538,51042)

D5 = (50531,51042) (51041,59232) (58722,58978)
A5 = (50531,58722) (51041,51042) (58978,59232)
```

All six materialized factors are degree two and q1 complete, with zero
pointwise static blockers against (R).  Every one has an independently
displayed mixed-palette unit contradiction.  In all six, the forcing chain
returns to the lower rows (L33435,L37529,L41625,L49691), upper row
(U49883), and the locked socket 49819, although the motif index changes.

The exhaustive C6 census and six factor hashes are in

```text
scratch/k16_portalq1_core_break_c6_20260729.audit.json
SHA-256 4d568d3e91b1628d3fa3bd158e3164bf07b3ae2f407d46446f11d4bf7fb0ae1c
```

The aggregate replay tying every candidate to its mixed-palette core is

```text
scratch/k16_portalq1_cover_preserving_radius3_trap_20260729.audit.json
SHA-256 d85d2d319d12214ea2df453963109b2b6f8c867333b348fc741e4bfe03f0b55b
```

This proves the radius-three trap.

## 7. Exact remaining gate

Within the fixed physical (Q/R) endpoint pair, the first unclosed pretrade
class has replacement radius at least four.  At replacement radius exactly
four, its support is either

1. one alternating (C_8); or
2. a union of two alternating (C_4)'s whose combined q1 support is valid
   even if neither component is separately support-preserving.

A successful trade must break both the local motif and the remote provider
socket; merely moving the displayed motif recreates the same obstruction.
The other principled escape is to change the resident factor simultaneously,
in particular in the broader AA-enabled oriented-port space.

No radius-four job was launched because H100 was under explicit severe
memory/swap pressure.  The model commands and all radius-at-most-three
artifacts are preserved locally.  No claim beyond the displayed fixed-pair,
fixed-deck, q1-cover-preserving theorem is made.

## 8. Reproducibility

Primary generators and aggregate checker:

```text
scratch/materialize_k16_portalq1_core_break_c4_20260729.py
SHA-256 49c0c33fa6cecc84d376438d6f364b0fed94c74e3313c8be981d8ffb76bb89d9

scratch/materialize_k16_portalq1_stage2_core_break_c4_20260729.py
SHA-256 1e89447449a8a2695ec2e7aaa84876f814cac51d37484281aef62dde879e2ef4

scratch/materialize_k16_portalq1_core_break_c6_20260729.py
SHA-256 650cb8345f661ed8fd6dcf9587f721478bbc790bad960ecb2ce5b37dcac80580

scratch/audit_k16_portalq1_cover_preserving_radius3_trap_20260729.py
SHA-256 570687b739f08513be33b6fc7945c51489a4571a00484f40390f2a77f2c7467e
```

The unit-Hall checker used for every displayed contradiction is

```text
scratch/audit_k16_overlay_upper_unit_hall_core_20260729.py
SHA-256 a0d9ce0d1547e8f5960be770e39051b85e3832d6a3b8a93a7f71cef5ee457b0f
```

and was run with `--palette-mode both` for every no-go claim after Section 3.
