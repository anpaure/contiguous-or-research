# K16 H2 non-provider tokens and the exact remote-return circuit

Date: 2026-07-30

Status: exact source-relative reduction, one authenticated scoped UNSAT
face, and one open expanded port face.  No length-12,873 word is
constructed.  The global bracket remains

\[
                    12873\leq \nu(16)\leq12874.
\]

All positions are zero-based.  A *hole* is a nonzero 16-bit mask with no
contiguous-OR witness.

## 1. Frozen states and labels

Put

\[
\begin{aligned}
 E&=\mathtt{082a},\\
 P&=\mathtt{4879},&Q&=\mathtt{6879},\\
 L_0&=\mathtt{486b},&L_1&=\mathtt{686b},&L_2&=\mathtt{6c6b},\\
 P'&=\mathtt{494b},&Q'&=\mathtt{694b}.
\end{aligned}
\]

The exact states used below are

| state | file | SHA-256 | holes |
|---|---|---|---|
| `H2` | `scratch/k16_ejection_lns_h2_p110_20260730.word` | `5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7` | `P,Q` |
| reorganized `h1` | `scratch/k16_h2_to_h1_p0.h1.word` | `ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a` | `0x2c6d` |
| `H4` | `scratch/h2_provider_p5462_v24_h4b.word` | `db61678fe72754c918087fcb7c557518955bb335befac579219d0ca1e7695d8a` | `E,L_0,L_1,L_2` |
| `H3` | `scratch/h4b_provider_p573_v2090_h3b.word` | `2768264d1c6d4bf1af9b3a5c1eb2aa1f6483b18425e0397d247aafa34da7bba6` | `L_0,L_1,L_2` |

The reorganized `h1` state is only the edit

\[
             w_0:\mathtt{2c61}\longmapsto\mathtt{4879}.
\]

It must not be confused with the neutral-token states below.

## 2. Exact two-edit boundary

A separate hash-closed theorem exhausts the branch in which neither final
endpoint value, applied alone to H2, supplies `P` or `Q`.  Literal
containment reduces it to 335 position corridors; 330 admit values
non-provider at both endpoints.  Of those, 325 have an immediate
no-form target, while the five surviving supports have one explicit
exclusive-supply obstruction each.  An independent direct-interval replay
checks all 2,187 live value pairs and finds no universal word.

The complete H2 one-cell provider atlas has 44,421 distinct first edits
after duplicate removal.  Exactly 284 of them leave at most seven holes.
For every one of those 284 intermediate words, every arbitrary second
one-cell edit which provides a current hole was enumerated, allowing reuse
of the first position.  None is universal.

### Theorem 2.1 (provider orientation and excursion floor)

Every at-most-two-substitution completion of H2 has an endpoint whose final
value, applied alone to H2, supplies `P` or `Q`.  Consequently every
hypothetical two-substitution completion has an ordering in which the first
edit is a source-hole provider and the intermediate word has at least eight
holes.

#### Proof

The hash-closed non-provider corridor theorem gives the first sentence.  If
one endpoint is a source provider, orient it first.  Were the intermediate
hole count at most seven, this first edit would be one of the 284 retained
provider rows.  Any universal second edit must provide a current hole, so it
would occur in the exhaustive second enumeration, which has no completing
row.  \(\square\)

This does not bound provider-first paths which make a larger first
excursion.  The non-provider theorem is independently hash-closed.  A frozen
provider-first rerun manifest binds the source, included provider engine,
compiled binary, byte-identical audit and resource transcript.  The relevant
files are

```text
scratch/k16_h2_twostep_firsth7_debt7_to0.audit.json
  92c86bafea6e50630efa370e0cf048c69ecfcbb79178cda58bd1f343493d0225
scratch/k16_two_step_lowdebt_sweep_20260730.cpp
  2626bc0c68902817155c3b94e7bfc8248aec91f8f62a08b2d46c9fa43b33dfd8
scratch/k16_h2_provider_first_floor8_frozen_20260730/manifest.audit.json
  14015af20b855a9b10901b3793d9dd8c88fd2ceec60a6166794f35521ba50344
MATH_THEOREM_K16_H2_NONPROVIDER_EJECTION_CLOSURE_AND_EXCLUSIVE_SUPPLY_20260730.md
  79b9fe8e6926350536d71c44c5a119a83dc5fcbbe028cdf51b062f3fb7c0add7
scratch/k16_h2_nonprovider_joint_supports_independent_20260730.audit.json
  5d11ff16a66d638448a8e85b4a3ac1ea61134336a3f74bbfb748bf116a8482ef
  payload 5da33e78a916c57d5965cff53c8e97c07e8e56bbe6bafabe9faaf9cadc577865
```

## 3. Exact neutral-token atlas

In H2, `E` has multiplicity one, with sole witness `[5462,5462]`.  An
`E`-token is a one-cell edit which raises this multiplicity to at least two
while leaving both source holes `P,Q` absent.

The earlier external-reserve atlas had exactly two minimum-collateral novel
allele positions, 1210 and 5462.  The present theorem deliberately takes the
5462 branch: its incumbent is the unique `E` witness, so a non-provider edit
can pre-duplicate the precise resource consumed by the service move.  The
position-1210 ladder is a separate branch and is not covered here.

### Theorem 3.1 (complete zero-collateral token list)

Among all positions and all nonzero replacement values, exactly nine
`E`-tokens have no collateral hole:

\[
\begin{split}
 r\in\{&573,3044,3644,6090,6302,6725,\\
       &10082,10277,10881\},\qquad w_r\longmapsto E.
\end{split}                                            \tag{3.1}
\]

The complete atlas evaluates 13,120 admissible non-provider reserve
assignments on 12,872 positions and retains every accepted row and its debt
set.  Its accepted-row stream has SHA-256
`078baa9d1db01b68dfc5435428a3bfa52b8745e1e556f08de43ed0485e4988b3`.

Now let

\[
 \mathcal Y=\{\mathtt{0018},\mathtt{0038},\mathtt{0058},\mathtt{0078},
 \mathtt{0818},\mathtt{0838},\mathtt{0858},\mathtt{0878}\}.       \tag{3.2}
\]

For every token (3.1) and every `y` in (3.2), make the service edit

\[
                     w_{5462}\longmapsto y.             \tag{3.3}
\]

Then exact full replay gives

\[
 \bigl(\mu(E),\mu(P),\mu(Q),\mu(L_0),\mu(L_1),\mu(L_2)\bigr)
                       =(1,1,1,0,0,0),                  \tag{3.4}
\]

and the complete hole set is exactly

\[
                         \{L_0,L_1,L_2\}.               \tag{3.5}
\]

#### Proof

The token atlas enumerates every `E`-provider value from exact left/right OR
contexts and computes the full interval-multiplicity delta.  Filtering by
`E`-multiplicity at least two, zero `P,Q` multiplicity, and zero collateral
leaves precisely (3.1).  Direct full-ledger replay of all
\(9\cdot8=72\) token-service compositions gives (3.4)--(3.5); the separate
support-three audit cited in Section 5 recomputes all 72 base ledgers.
\(\square\)

The authenticated files are

```text
scratch/audit_threadA_k16_h2_nonprovider_e082a_reserve_atlas_20260730.py
  26682fb806bc5bc62a552416e8fc57da4196442646377a7ffb9a8132e792a649
scratch/threadA_k16_h2_e082a_reserve_atlas_20260730.audit.json
  b47b021155e2fe22c8c2f52175632b91bc768c341516a020d34df368d8c88e74
  payload 90429b8651af9dd466c265fe5633578a6de51df6411644074dabf40e31dd672c
```

Thus the neutral token is a genuinely non-provider first move: it preserves
the two-hole set and installs exactly the reserve consumed by (3.3).

## 4. The exact two-hole shuttle

Fix the first token `r=573` and service value `y=0x0018`; this is state H3.
Its complete one-cell provider atlas evaluates 90,748 distinct moves.

### Theorem 4.1 (one-return obstruction and two shuttle fibres)

No one-cell edit completes H3.  Among edits at positions `p != 0`, the
minimum final hole count is two, attained exactly sixteen times:

1. at position 5462, the eight values
   \[
   \{\mathtt{000a},\mathtt{002a},\mathtt{004a},\mathtt{006a},
     \mathtt{080a},\mathtt{082a},\mathtt{084a},\mathtt{086a}\}
   \]
   fill all three `L_i` and recreate the old pair `P,Q`;
2. at position 5971, the eight values
   \[
   \{\mathtt{0028},\mathtt{002a},\mathtt{0068},\mathtt{006a},
     \mathtt{0828},\mathtt{082a},\mathtt{0868},\mathtt{086a}\}
   \]
   fill all three `L_i` and create exactly the remote pair `P',Q'`.

#### Proof

For `p != 0`, any universal one-cell edit must provide a current hole, hence
occurs in the complete H3 provider atlas.  Its final-hole histogram starts
with `2:16`; there is no row at zero or one.  The sixteen minimizing rows
and their complete signed debt sets are exactly the two fibres displayed
above.  At position zero, every changed interval is a prefix.  The exact
prefix-provider sets for `L_0,L_1,L_2` have empty common intersection, so no
position-zero value supplies all three holes.  \(\square\)

The position-zero audit is

```text
scratch/audit_threadA_k16_h3_p0_return_20260730.py
  5623efaa9ac533ce60ccde42dc216e6b26c4c661b5ce52cc3080051eced2efd5
scratch/threadA_k16_h3_p0_return_20260730.audit.json
  25b0d47a956e44ff1ceb2d3326910f08d1981bfd9f495fdbd490e219699aa6af
  payload 21cab72d35ebc7165ef4e597bec69fd54b6dbc08258426607d6950df6f9ef069
```

Consequently

\[
 \{P,Q\}\xrightarrow{\text{neutral token}}\{P,Q\}
 \xrightarrow{\text{service}}\{L_0,L_1,L_2\}
 \xrightarrow{\text{remote return}}\{P',Q'\}           \tag{4.1}
\]

is an exact defect shuttle, not an absorber.  This is the first literal link
between the H2 portal graph and the remote return components.

## 5. A proved support-three no-go on all natural ports

Let the nineteen possible single-return cells be

\[
\begin{split}
\mathcal R=\{&576,577,578,3329,3330,3331,3494,3495,3496,\\
            &3838,3839,3840,5463,5464,5465,5466,
              5971,5972,5973\}.                       \tag{5.1}
\end{split}
\]

These are the six predecessor-controller collars selected by the six
one-bit-deficit components, with the service continuation through 5466.

### Theorem 5.1 (neutral token plus service needs two returns)

For every one of the 72 token-service states in Theorem 3.1, allow one
further arbitrary nonzero reassignment at a cell of (5.1), freezing every
other cell.  No resulting word is universal.  Among replacements capable of
supplying all three ladder holes, the minimum final hole count is two in
every base state.

#### Proof

For each base state and position, exact left-suffix/right-prefix OR contexts
enumerate every value capable of supplying all three ladder targets.  Any
universal return must lie in this set.  There are 624 candidate assignments
per base state and 44,928 altogether.  Exact full multiplicity deltas give
zero universal rows.  The ordered candidate summaries are identical over
all 72 cases, with minimum two holes.  \(\square\)

This proves a support floor of four for the precise architecture

\[
                 \text{one token} + \text{one service}
                   + \text{return cells in }\mathcal R.  \tag{5.2}
\]

It does not exclude a return outside (5.1), a different non-provider
precursor, more than one token, or a chronology change.

```text
scratch/audit_threadA_k16_h2_neutral_token_support3_20260730.py
  3a80f2a418734abef5cfa7cbf73673af4b9969d569947f5e3793590e504aca2e
scratch/threadA_k16_h2_neutral_token_support3_20260730.audit.json
  5c7f85b92e8dfb0d33409db15543aa9db20d6e0da0973ffbfff41206bb213ec5
  payload affaa785e7c4b1d907205df546479c130fcdcf76951486f838605da28eb03408
```

## 6. Exact two-return compatibility theorem

The relevant six three-cell blocks are

\[
\begin{aligned}
B_1&=[576,578],&B_2&=[3329,3331],&B_3&=[3494,3496],\\
B_4&=[3838,3840],&B_5&=[5462,5464],&B_6&=[5971,5973].   \tag{6.1}
\end{aligned}
\]

For all nine token choices, each of the five complete gaps strictly between
successive blocks has OR `0x7fff`.  Any interval meeting two blocks
therefore has OR `0x7fff` or `0xffff`.  Both colours retain fixed witnesses
outside the blocks.

Fix one token-service state `W`, and write `mu(t)` for its exact target
multiplicity.  For a one-cell edit `e` in block `B_i`, let

\[
 \Delta_e(t)=\#\{\text{new intervals of colour }t\text{ meeting }e\}
             -\#\{\text{old such intervals}\}.        \tag{6.2}
\]

### Theorem 6.1 (safe-gap compatibility graph)

For edits `e` in `B_i` and `f` in `B_j` with `i != j`, the twice-edited
word is universal if and only if

\[
                  \mu(t)+\Delta_e(t)+\Delta_f(t)\geq1 
 \quad(1\leq t\leq65535,\ 
       t\notin\{\mathtt{7fff},\mathtt{ffff}\}).       \tag{6.3}
\]

For edits at two distinct cells of one block, replace the sum in (6.3) by
their exact joint two-cell delta relative to `W`.  Hence existence of a
two-return completion in (6.1) is equivalent to an edge in the graph of
distinct-block signed profiles or a successful same-block joint profile.

#### Proof

An interval meeting both distinct edit blocks contains the complete fixed
gap between them.  Its OR is therefore `0x7fff` or `0xffff`; those two
targets retain fixed avoiding witnesses `[2,18]` and `[6425,6436]`,
respectively.  Every interval relevant to any other target meets at most one
edit, so its multiplicity delta is additive and (6.3) is necessary and
sufficient.  In one block, mixed intervals can meet both edits and must be
counted jointly; exact context enumeration gives the stated replacement.
\(\square\)

This is the compact, sound remote-return circuit model.  It keeps literal
interval chronology and every collateral target; it is not a marginal or
hole-count relaxation.

## 7. Authenticated endpoint-only no-go

There is one independently checked strict subface.  Starting from H2 make

\[
 w_0:=\mathtt{2c6d},\qquad w_{573}:=E,qquad
 w_{5462}:=\mathtt{0018},                              \tag{7.1}
\]

and allow arbitrary nonzero values only at

\[
 S_{12}=\{577,578,3330,3331,3495,3496,3839,3840,
           5463,5464,5972,5973\}.                     \tag{7.2}
\]

### Theorem 7.1 (restricted `S12` UNSAT)

No word in this frozen-complement face is universal.

#### Proof certificate

The exact dynamic interval CNF has 2,202 variables, 34,422 clauses, 74,608
literals, 111 repair targets, 451 changed-interval bases and 1,998 witness
terms.  Kissat returned UNSAT.  The 382,506,775-byte DRAT proof has SHA-256
`100f21b65b92da4290fb8000b9d65a51a0d0c865a9b99c54a44e0f24eeea18ee`;
`drat-trim` returned `s VERIFIED`.  The local compressed proof has SHA-256
`1a1e81405b8a794ed1624531ece0bd5d3107ed7080bc831858e742324933d6d5`.
\(\square\)

The file named `check.lrat` in the artifact directory is not LRAT: it is the
32,664-clause core CNF emitted by `drat-trim -c`.  The checked DRAT is the
proof certificate.

This theorem omits all five predecessor controllers in (6.1), freezes the
service cell and positions 5465--5466, and fixes one token, one service value
and the normalization (7.1).  It is not the full six-port theorem.

```text
scratch/threadA_k16_h2_neutral_token_remote_return_20260730/audit.json
  8b92a0dd2b00788b7f1b7b860653cc2c329fb23d2555a4cb2d1bd080d1c3c98b
scratch/threadA_k16_h2_neutral_token_remote_return_20260730/proof.drat.zst
```

## 8. Expanded predecessor-controller face

For the fixed H3 state, an exact unbounded CNF now allows arbitrary nonzero
values at all eighteen cells in the six blocks (6.1), freezing the
complement.  Its dimensions are

\[
 5094\text{ variables},\quad98001\text{ clauses},\quad220892\text{ literals},
\]

with 133 repair targets, 672 bases and 4,788 witness terms.  The exact model
hash is

```text
05812a55a294b008aa46721a9b801952bff0c5b9bd0574a822991ac30bac73a4
```

The first capped H100 run wrote a 997 MiB partial proof and then received
`SIGABRT` when `/dev/shm` reached 100 percent.  This is a resource exit, so
its disposition is exactly

\[
                              \boxed{\mathrm{UNKNOWN}}.
\]

The partial stream was not a certificate and was deleted from this lane's
named remote temporary directory.  No retry was launched.  The source,
model, map, statistics and abort log are preserved locally at

```text
scratch/threadA_k16_h2_neutral_token_sixport18_20260730/
```

Future proof-producing work must use a unique directory under
`/home/amodo/or15/work/`, not `/dev/shm`.

## 9. Sharp remaining gate

The proved boundary is now:

1. every hypothetical two-edit completion has a provider-first orientation,
   and every such orientation must excursion to at least eight holes;
2. exactly nine zero-collateral non-provider `E` tokens exist;
3. each token followed by any of the eight service alleles yields the same
   three-hole ladder;
4. one return cell in the complete nineteen-cell natural-port set never
   closes, and the best return is an exact two-hole shuttle;
5. the old endpoint-only twelve-cell face is certified UNSAT.

The smallest open constructive object *within this neutral-token/six-block
architecture* is therefore the two-return compatibility graph of Theorem
6.1, including same-block two-cell profiles.
A positive edge gives a literal H2 completion along the chronology token,
service, return, return, using at most four final changed cells (a return may
overwrite the service cell).  A complete negative certificate would prove
that this neutral-token architecture needs either a third return cell or a
cell outside the six port collars.  Neither outcome is currently proved.

Nothing in this report proves or refutes `nu(16)=12873`.
