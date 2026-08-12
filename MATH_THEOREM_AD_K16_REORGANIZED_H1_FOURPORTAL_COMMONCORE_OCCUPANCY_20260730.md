# K16 reorganized H1: four-portal common-core occupancy theorem

Date: 2026-07-30  
Lane: AD  
Status: exact source-relative reduction and unsolved CNF; disposition UNKNOWN

## 1. Frozen H1 state and one-step portal atlas

The authenticated word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

has length 12,873 and sole missing mask

\[
                         H=11373=\mathtt{0x2c6d}.
\]

The exact provider atlas

```text
scratch/k16_reorganized_h1_exact_provider_atlas.audit.json
SHA-256 59cbc69665c5f21c8f9575e997765da478e947322d926669172cb71a04ddbbb7
```

evaluates all 28,805 distinct `(position,replacement-value)` one-cell
provider pairs capable of supplying \(H\).
Its minimum collateral debt is two, attained by exactly 153 substitutions in
four families:

\[
\begin{array}{c|c|c|c}
p&\text{replacement family}&\#&\text{debts}\\ \hline
0&\mathtt{0800}\vee s,\ s\subseteq\mathtt{246d}&128&
  \mathtt{4879},\mathtt{6879}\\
4489&\mathtt{0024}\vee s,\ s\subseteq\mathtt{2041}&8&
  \mathtt{2669},\mathtt{2e69}\\
6440&\mathtt{0440}\vee s,\ s\subseteq\mathtt{002d}&16&
  \mathtt{806d},\mathtt{a86d}\\
12872&\mathtt{2c6d}&1&
  \mathtt{ce61},\mathtt{ce63}.
\end{array}                                                    \tag{1.1}
\]

The displayed cubes are pairwise literal families; their counts sum to 153.
This is a complete minimum-debt one-substitution statement, not a claim that
an eventual completion must begin with one of them.

## 2. Exact private-witness hull

In the source word the eight debts have the following complete occurrence
ledger:

\[
\begin{array}{c|c}
\text{target}&\text{all source intervals}\\ \hline
\mathtt{4879}&[0,0]\\
\mathtt{6879}&[0,1]\\
\mathtt{2669}&[4487,4489]\\
\mathtt{2e69}&[4486,4489]\\
\mathtt{806d}&[6440,6440]\\
\mathtt{a86d}&[6438,6440]\\
\mathtt{ce61}&[12871,12872]\\
\mathtt{ce63}&[12869,12872],\ [12870,12872].
\end{array}                                                    \tag{2.1}
\]

The corresponding (H)-installing intervals are respectively

\[
[0,3],\quad[4486,4489],\quad[6438,6440],\quad[12872,12872].      \tag{2.2}
\]

In the first interval, positions 2 and 3 remain fixed context.  The minimal
support containing the four portals and every cell in every destroyed source
witness is therefore

\[
P=[0,2)\ \dot\cup\ [4486,4490)\ \dot\cup\ [6438,6441)
       \ \dot\cup\ [12869,12873),                                  \tag{2.3}
\]

of size 13 and block widths (2,4,3,4).  “Minimal” here is relative to the
source-witness-hull definition.  It is not a global WLOG theorem excluding a
remote donor cell or a different chronology.

## 3. Coverage-safe block decomposition

The fixed gaps before, between, and after the four blocks have ORs

\[
                 0,\ \mathtt{7fff},\ \mathtt{ffff},\
                 \mathtt{ffff},\ 0.                                \tag{3.1}
\]

Every supermask of each nonzero intervening gap OR already has a fixed-only
literal witness: the only supermasks of `0x7fff` are `0x7fff,0xffff`, and
the only supermask of `0xffff` is itself.  Hence no target left uncovered by
the fixed runs can have a witness crossing a gap.

Direct fixed-run replay covers exactly 65,480 nonzero masks.  Its complement
is a common repair family (R) of 55 targets.  Every (T\in R) has exactly
one undominated maximal-context term for every nonempty interval inside each
block.  Since

\[
 \binom{2+1}{2}+\binom{4+1}{2}+\binom{3+1}{2}
       +\binom{4+1}{2}=3+10+6+10=29,                                \tag{3.2}
\]

the exact raw term ledger has (55\cdot29=1595) forms and no cross-block
form.

The frozen dynamic-substitution emitter gives

```text
variables 1816
clauses   35208
literals  81990
```

for arbitrary nonzero values at all 13 positions, with every other position
fixed.  The raw instance is retained under

```text
scratch/k16_reorganized_h1_fourportal_joint13_20260730/model.{cnf,map}
```

with hashes `0fc8ab9880a5016cbc404810f74f1b04c54e93903f6b2b7e1ff47e7dc12f8cb7`
and `cefb607c2b16278aeafedc865fd74ec86f77bf5dc35b83a2a3fd347c8cdc47e9`.

## 4. Common-core canonicalization

The decisive special property of this joint support is

\[
                         \bigcap_{T\in R}T=\mathtt{0x0040}.            \tag{4.1}
\]

Choose one actual local form (I_T) for every (T\in R).  At each editable
position (p), define

\[
 C_p=\bigcap_{T:p\in I_T}T,                                         \tag{4.2}
\]

using `0xffff` when no selected form contains \(p\).

### Theorem 4.1 (exact common-core chart criterion)

The selected forms are simultaneously realizable if and only if, for every
(T) and every coordinate required by its maximal-context residual need,
that coordinate occurs in \(C_p\) at some \(p\in I_T\).  Nonzeroness needs no
separate condition: every active-target intersection contains `0x0040`, and
an unused cell has the explicit value `0xffff`.

When the condition holds, assigning the literal cell value (C_p) realizes
all selected forms.  Conversely every realizing assignment is contained
coordinatewise in the corresponding (C_p), so each required coordinate
must survive somewhere.

#### Proof

If a cell belongs to the selected (T)-form, its value must be a submask of
(T), and hence of (4.2).  Every residual required bit must be supplied by a
cell of that interval, proving necessity.  Conversely (C_p\subseteq T) on
each selected (T)-interval, so no forbidden bit enters.  The hypothesis
supplies every bit absent from the fixed context; the context supplies the
rest.  Equation (4.1) makes every active cell nonzero, while the empty-family
convention makes each unused cell `0xffff`.  Thus every form is a literal
contiguous-OR witness. \(\square\)

The intersection closure of the 55 targets has exactly 215 states, all
nonzero and all containing `0x0040`.  Adding the unused-cell value `0xffff`
gives a sufficient canonical closure alphabet of 216 masks.  The theorem
does not claim that every closure state is attained by a feasible global
assignment.  The number 216 is coincidental and unrelated to the earlier
216-family empty-intersection catalogue.

## 5. Exact 1,130-variable occupancy CNF

The common core permits removal of the coordinate-6 variables entirely.
Introduce:

* (55\cdot13=715) target-position occupancy bits (o_{T,p});
* (55\cdot4=220) target-block controls; and
* (13\cdot15=195) availability bits (a_{p,q}) for (q\ne6).

For every target, force its occupancy to be one nonempty consecutive run in
exactly one block.  Impose

\[
 o_{T,p}\Longrightarrow\neg a_{p,q}\qquad(q\notin T)                \tag{5.1}
\]

and the reverse canonical row

\[
 a_{p,q}\vee\bigvee_{T:q\notin T}o_{T,p}.                           \tag{5.2}
\]

Thus (a_{p,q}=1) exactly when every target active at (p) contains (q).
For every possible local interval, its endpoint/neighbor signature activates
one row per required noncommon coordinate, demanding that some availability
bit on the interval be true.  Coordinate 6 is automatically supplied at
every cell.

### Theorem 5.1 (CNF equivalence)

The occupancy CNF is satisfiable if and only if the frozen-complement
13-position support (2.3) contains a universal literal word.  From a model,
the exact cell is

\[
 z_p=\mathtt{0x0040}\vee
          \bigvee_{q\ne6:\ a_{p,q}=1}2^q.                            \tag{5.3}
\]

The proof is Theorem 4.1 plus the exact one-run and interval-signature
constraints.  Equation (5.2) supplies the reverse direction and makes (5.3)
the canonical active-target intersection.

The exact clause ledger is

\[
\begin{array}{c|r}
\text{family}&\#\\ \hline
\text{target occupancy ALO}&55\\
\text{occupancy-to-block}&715\\
\text{block-control AMO}&330\\
\text{run-start AMO}&385\\
\text{omission forward rows}&5577\\
\text{availability reverse rows}&195\\
\text{durable interval rows}&10301\\ \hline
\text{total}&17558.
\end{array}                                                     \tag{5.4}
\]

Thus the reduced instance has

```text
variables 1130
clauses   17558
```

and is frozen as

```text
scratch/k16_reorganized_h1_fourportal_joint13_20260730/model.occupancy.cnf
SHA-256 504677bee9bdf8a9eed475f284bcae489a2cf78db6dbc2a2b696c9bc7a632887

scratch/k16_reorganized_h1_fourportal_joint13_20260730/model.occupancy.map.json
SHA-256 486b5a2f3fa3fd05432190e62bba5fdf7594739b9cd71b058212e8e60a346330
payload SHA-256 7aa37cc02cff2f93fe38b2bfa284feb9af8becb00c248adcabfba970b7cb999d
```

The deterministic builder is

```text
scratch/build_ad_k16_reorganized_h1_fourportal_occupancy_cnf_20260730.py
SHA-256 1998ae4a1dd83e3309f88d809eb920c4d2affcba085ebdfa9771a23aa72d41eb
```

and a fail-closed SAT decoder/full literal replay is

```text
scratch/decode_verify_ad_k16_reorganized_h1_fourportal_occupancy_20260730.py
SHA-256 06e04a156473d76690809924182d3c2e1bec3c1e4379fac77fd66a28dc60e4e7
```

## 6. Exact boundary

No solver was launched for either joint13 formula.  Their disposition is
`UNKNOWN`.  The reduction permits assignments to precisely the 13 editable
positions (2.3), including their incumbents and hence zero through thirteen
actual changes; it is not restricted to the 153 portal values.  It does not cover a
remote donor, an edit outside this support, a moved cell/order, or an
unrelated length-12,873 word.  SAT is not a theorem until the frozen decoder
and an independent full replay pass; UNSAT is not a theorem without a
retained independently checked proof.
