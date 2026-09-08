# Independent audit of the parameter-three joint donor collapse

Date: 2026-07-31  
Verdict: **GO in the stated fixed-parent, unlabelled-marginal scope.**

Audited theorem:

```text
MATH_THEOREM_CATALAN_COMPLEMENT_DONOR_FLOW_AND_BLOCK_OBSTRUCTION_20260731.md
SHA-256 6fcde7c7dc629d0696a0a0bb2406313e98ad416021ed46d5cda9e14ca3f53f91
```

The independent verifier neither imports nor reads the primary verifier or
its JSON.  It reconstructs the literal oriented child from the five paths in
the earlier source theorem, expands the complete two-shore LP symbolically,
treats the claimed 53 multipliers as untrusted certificate data, and checks
the integral witness in the full uncontracted attachment graph.

## 1. Reconstructed primal

The five oriented paths are

```text
34-15-07-0b
16-26-2a-29-19-13
2c-25-23
38-1c-0d
31-32-1a-0e.
```

Taking intersection and union on every oriented edge reconstructs exactly
15 records

```text
(lower rank-two colour, upper rank-four colour, tail, head),
```

whose two colour projections are the complete rank-two and rank-four
palettes.  The canonical index is increasing lower colour.  On the two
rank-three-to-rank-five normal forms, put

\[
 (\tau_i^+,\upsilon_i^+)=(t_i,t_i\cup h_i),\qquad
 (\tau_i^-,\upsilon_i^-)=(\bar h_i,\overline{t_i\cap h_i}).
\]

Both `tau` lists and both anchor lists have 15 distinct entries.  The
complete joint physical system has variables `p_i>=0`, `sum p_i=1`, and
the 120 legal atoms `w^s_(D,V)>=0`, with

\[
\sum_{V\supset D}w^s_{D,V}=
 \begin{cases}p_i,&D=\tau_i^s,\\1,&D\notin\tau^s(E),\end{cases}
\]

all six top-column sums equal to one, and owner loads bounded by
`1+p_i` at `upsilon_i^s` and by two at every ordinary owner.  An independent
matching replay also confirms that all 15 co-singletons are strict common
bases, so this simplex is the literal common-base polytope for the fixture.

## 2. The 53-multiplier identity

Let `R_(s,D)` and `C_(s,V)` be free equality multipliers, `K_(s,x)>=0`
owner-capacity multipliers, and `S` the free simplex multiplier.  Expanding

\[
 \sum R(\text{row load}-\text{row RHS})+
 \sum C(\text{column load}-1)+
 \sum K(\text{owner load}-\text{capacity})+
 S(\sum_i p_i-1)\le0
\]

gives the following exact independent checks:

```text
nonzero multipliers                 53
constant RHS                         0
p coefficients             1,...,1,0   (fourteen 1s)
legal physical atoms                120
minimum atom coefficient              0
maximum atom coefficient              2
shore-0 atom histogram       0:36, 1:19, 2:5
shore-1 atom histogram       0:48, 1:12
```

Thus every feasible point obeys

\[
 0\ge \sum_{s,D,V}\gamma^s_{D,V}w^s_{D,V}
        +\sum_{i=0}^{13}p_i
 \ge \sum_{i=0}^{13}p_i,
\]

where every `gamma` is nonnegative.  Since `p>=0` and `sum p=1`, this
forces `p_14=1`.  This is an exact integer identity, not a floating-point
dual report.

## 3. Literal integral witness

Index 14 is reconstructed, rather than assumed, as

```text
(lower, upper, tail, head) = (30,33,31,32).
```

The two displayed matchings are replayed literally:

```text
upper: 0b->1f, 23->2f, 13->37, 31->3b, 0d->3d, 0e->3e
lower: 04->16, 08->2c, 01->31, 02->32, 20->34, 10->38.
```

Each uses its six outer rows and six outer columns once.  Upstairs only
owner `33` has physical load two; downstairs only owner `30` has load two.
These are precisely the two ordinary, cap-two owners created by retaining
edge 14.  Every seam anchor has load at most one.

Rather than trusting the contracted partitions in the primary replay, the
independent verifier builds the entire tagged graph on

```text
15 lower owners + 20 central vertices + 15 upper owners.
```

It inserts the twelve physical edges, the retained central edge, and the
28 lower/upper attachments belonging to the other 14 child edges.  The
result is

```text
vertices              50
edges                 41
components             9
cycle rank             0
minimum degree         1
maximum degree         2
component sizes        3,3,4,4,5,5,6,8,12.
```

This proves a full uncontracted linear forest, which in particular proves
the theorem's contracted graphic assertion.  The same integral assignments
also prove feasibility at `p=e_14`; combined with the dual certificate, the
projection is exactly the singleton `{e_14}`.

## 4. Scope audit

No mathematical correction to Theorem 4.1 is required.  Its quantifiers
must remain as written:

* one fixed literal oriented parameter-three parent;
* the complete **unlabelled** upper/lower physical marginal systems;
* one shared retained-edge simplex and the resulting attachment forest.

The certificate does **not** prove an every-parent or all-parameter donor
theorem.  It does not include coherent SBE endpoint blocks,
occurrence-labelled representatives, residence, deeper witnesses, or a
maximal common cap.  Nor does it make independent-shore rounding or
rowwise complemented Farkas pairing valid.  The result is nevertheless a
genuine positive calibration: aggregate two-shore coupling can collapse a
fractional common-base simplex to one integral bank even though an
individual physical row straddles it.

## 5. Frozen independent artifacts

```text
scratch/independent_audit_catalan_n3_joint_donor_collapse_20260731.py
SHA-256 951f898f47c36a23070a9eb33c094cae997022eeaffc0fea6cf0062daa0611d3

scratch/catalan_n3_joint_donor_collapse_20260731.independent.audit.json
SHA-256 fd353a7b252e3490fc861bb2da29f53e247b95cc4ef82265cca25aa15d35d3d0
canonical payload SHA-256
d848e7d92682adeb663a284749bcb9e91026cedc901cab3ee3997b225949d7df
```

The reconstructed path sources were frozen at:

```text
MATH_THEOREM_R_TWO_COORDINATE_SIDE_TURN_FOREST_AND_CAPACITY_CUT_20260731.md
SHA-256 74dd8c45844e249f94d879469a78538dfee4b1b0b4582ea6d701c20e4cd6fe7a

MATH_THEOREM_R_CATALAN_BANK_FLEXIBLE_RHO_MINMAX_AND_DUPLEX_EXCHANGE_20260731.md
SHA-256 8f24927133e72ddc0dd5c5baf462f273740b73f677345e262c2f8414b70c3370
```
