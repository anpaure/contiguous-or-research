# K16 H1 radius four: primitive H-triple plus one exterior cell

Date: 2026-07-30

Status: exact solver-free reduction and authenticated scope.  No K16
exterior-position census is claimed in this note.

## 1. The next literal family

Fix the reorganized H1 source

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
length 12,873; sole hole H=0x2c6d.
```

Let `C` be the frozen 7,099-move catalogue on its 288-position support `S_C`:

```text
scratch/k16_h1_radius4_mitm_catalogue_20260730.tsv
SHA-256 19a48659bdd50abf0a17d3baa3755b79fa88ab7c69a1361dd39a51eb9cd2d4a0
```

The family in this note is

\[
 \mathcal E_{3+1}=\{u^{q\leftarrow z}: u\text{ is a primitive catalogue
 H-triple},\ q\notin S_C,\ 0<z\ne w_q\le 0xffff\}.               \tag{1.1}
\]

Here *primitive* means that the three catalogue actions together install
`H`, while none of their three pairs installs `H`.  The authenticated packet
census gives exactly 16,420 prefixes on seven supports:

| triple support | primitive assignments |
|---|---:|
| `0,2,3` | 1,916 |
| `1,2,3` | 50 |
| `4498,4499,4500` | 138 |
| `4501,4502,4503` | 148 |
| `6434,6435,6436` | 3,100 |
| `6435,6436,6437` | 7,968 |
| `12867,12868,12869` | 3,100 |

There are `12,873-288=12,585` exterior positions.  Thus (1.1) is the
smallest literal position extension of item 1990's primitive-triple branch:
the first three actions and their exact H proof are unchanged, and only the
fourth action is allowed to leave the catalogue support.

Relative to the installer and all-catalogue radius-four census jobs, no word
in (1.1) is shared with either enumerated family.

* Root's remaining branch starts from an H-installing pair, whereas every
  prefix in (1.1) has no H-installing pair.  Root's all-catalogue decision
  also has its fourth site in `S_C`, whereas (1.1) requires `q notin S_C`.
* The current Thread-D H1 families all retain the p6440 gate.  Position 6440
  lies in `S_C`, none of the seven primitive supports contains it, and the
  exterior fourth site cannot equal it.  Therefore no word in (1.1) edits
  p6440.
* The current Thread-A reserve shells use the H2 source rather than this
  frozen H1 source.

The earlier catalogue triple-plus-one exclusion tested only catalogue values
at catalogue positions and hence does not decide (1.1).

### Relation to item 1999

There is **no set-theoretic disjointness claim from item 1999**.  Let

```text
S_13 = {0,1,4486,4487,4488,4489,6438,6439,6440,
        12869,12870,12871,12872}
```

be its frozen joint13 support.  Item 1999's active-kernel theorem applies to
arbitrary values on `S_13` and every arbitrary outside edit set `E`.
Consequently it applies to every word in (1.1), as it does to every
fixed-source edit family.

The quantifiers are nevertheless different.  Item 1999 identifies the
source-fixed target kernel `K_(S_13)(E)` which still needs service, but does
not decide the coupled values on `S_13 union E`.  The theorem below fixes the
three-edit prefix `u`, forms the **post-prefix** all-target kernel `K_q(u)`,
and decides the last arbitrary value exactly by one maximum or the incumbent
coatoms.  It is therefore a strict decision refinement on this overlapping
family, not a duplicate source-kernel reduction.

The overlap audit also separates item 1999's highlighted next fibre.  Two
joint13 sites, 4486 and 4487, lie outside `S_C`; the other 12,583 choices of
`q notin S_C` lie outside joint13.  Among the 16,420 prefixes, 5,066 have two
sites outside joint13 and 11,354 have three.  Across all 206,645,700 raw
prefix/site rows, item 1999's outside-set sizes are therefore

```text
|E|=2:     10,132
|E|=3: 63,768,186
|E|=4:142,867,382.
```

Thus (1.1) does not overlap item 1999's specifically highlighted
`|E|=1` fibre (“arbitrary joint13 values plus one outside site”), although it
does lie under the general arbitrary-`E` active-kernel umbrella.  Rows covered
by item 1999's column-reset or face-halo folds may be removed first; the
maximum/coatom decision is needed only for the remaining unsafe rows.

## 2. The common-witness core

The following statement is independent of K16.  Let `u` be any nonzero-cell
word and let `W_u(T)` be the set of physical intervals whose OR is the
nonzero target `T`.  For a site `q`, define

\[
 K_q(u)=\{T:\text{there is no }T\text{-witness avoiding }q\}.       \tag{2.1}
\]

If `W_u(T)` is nonempty, put

\[
 \lambda_u(T)=\max_{[i,j]\in W_u(T)}i,\qquad
 \rho_u(T)=\min_{[i,j]\in W_u(T)}j.                                \tag{2.2}
\]

Define the common-witness core

\[
 J_u(T)=
 \begin{cases}
 [\lambda_u(T),\rho_u(T)],&\lambda_u(T)\le\rho_u(T),\\
 \varnothing,&\lambda_u(T)>\rho_u(T),\\
 [0,n-1],&W_u(T)=\varnothing.
 \end{cases}                                                       \tag{2.3}
\]

### Lemma 2.1 (interval-stabbing identity)

For every nonzero `T` and every site `q`,

\[
                         T\in K_q(u)\iff q\in J_u(T).               \tag{2.4}
\]

#### Proof

If `T` is absent, both sides hold for every `q`.  Otherwise, a witness avoids
`q` exactly when it ends before `q` or begins after `q`.  The former exists
iff `rho_u(T)<q`, and the latter exists iff `lambda_u(T)>q`.  Negating these
two alternatives gives (2.4).  QED.

Thus the targets threatened by changing `q` are not an arbitrary set: they
are exactly the target-labelled intervals `J_u(T)` which stab `q`.

## 3. Exact all-target last-cell interval

Remove the incumbent at `q`.  For `T in K_q(u)`, extend from `q` in both
directions through every consecutive fixed cell which is a submask of `T`,
and let `c_q^u(T)` be the OR of this maximal fixed collar.  Put

\[
 L_q(u)=\bigvee_{T\in K_q(u)}(T\setminus c_q^u(T)),\qquad
 U_q(u)=\bigcap_{T\in K_q(u)}T,                                    \tag{3.1}
\]

with empty union `0` and empty intersection `0xffff`.

### Theorem 3.1 (all-target last-cell theorem)

For a nonzero value `z`, the word `u^(q<-z)` is universal exactly when

\[
                         L_q(u)\subseteq z\subseteq U_q(u).          \tag{3.2}
\]

#### Proof

Every target outside `K_q(u)` has an unchanged witness avoiding `q`.  Fix
`T in K_q(u)`.  Every final `T` witness must contain `q`, so necessarily
`z subseteq T`.  All its other cells are consecutive `T`-submasks and hence
lie in the maximal collar.  Conversely, the whole maximal collar together
with `q` is itself one interval.  It has OR `T` exactly when

\[
       T\setminus c_q^u(T)\subseteq z\subseteq T.
\]

Intersect these Boolean intervals over all `T in K_q(u)`.  QED.

This strengthens item 1990's hole-only last-cell inverse.  Using every target
with no avoiding witness absorbs collateral exactly; no marginal gain or
representative profile is used, and no separate protection heuristic is
needed.

### Corollary 3.2 (maximum/coatom decision)

All feasible values are submasks of `U_q(u)`, and feasibility is upward
closed within that down-set.  Therefore an arbitrary genuine replacement at
an exterior site is decided as follows.

1. If `U_q=0`, reject.
2. If `U_q` differs from the incumbent, test only the literal value `U_q`.
3. If `U_q` equals the incumbent, test only its nonzero coatoms.

Equivalently, after `L_q` is materialized, the third case succeeds exactly
when some nonzero coatom of `U_q` contains `L_q`.  There are at most sixteen
literal tests.  An implementation should still run its exact four-edit delta
and a full 65,535-mask replay on every reported positive candidate.

## 4. Positive-cut sweep for all exterior sites

Lemma 2.1 turns `U_q` into sixteen interval cuts.  For each coordinate bit
`b`, define

\[
 d_b(q)=|\{T:q\in J_u(T),\ b\notin T\}|.                            \tag{4.1}
\]

Then

\[
                         b\in U_q(u)\iff d_b(q)=0.                  \tag{4.2}
\]

Every target contributes `+1` on one literal interval `J_u(T)` to each bit
it omits.  Sixteen difference arrays therefore recover all `U_q` values in
one sweep.  The witness endpoints in (2.2) are also cheap: for each right
endpoint, the ORs of intervals ending there form a compressed suffix chain
with at most seventeen distinct labels in dimension sixteen.  Recording the
latest start and earliest end of each label costs `O(17n+2^16)` operations
per prefix, before candidate replay.

This is a literal positive-cut formulation.  It retains the whole target
label on every active cut; replacing it by hole count, marginal gain, or an
independent-provider flag would be unsound.

## 5. Immediate K16 pruning and exact remaining kernel

The existing exact primitive-triple audit reports

```text
primitive H-triples with no installing pair       16,420
prefixes whose exact hole intersection is zero    11,068
remaining prefixes                                 5,352
```

Every hole of `u` is absent, so its common-witness core is the whole word and
it belongs to `K_q(u)` for every `q`.  Consequently

\[
 \bigcap_{T\in D(u)}T=0\quad\Longrightarrow\quad U_q(u)=0
 \quad\text{for every site }q.                                      \tag{5.1}
\]

Thus the 11,068 zero-intersection prefixes are already impossible for an
arbitrary fourth position and arbitrary nonzero value, not merely for a
catalogue action.  Only 5,352 prefixes require a sweep.  Before any further
cut, their exact exterior-position kernel has

```text
5,352 * 12,585 = 67,354,920 prefix/site rows,
```

with one maximum literal or at most sixteen coatoms per row, followed by
exact four-delta and full replay.  This removes the factor 65,535 from the
arbitrary-value quantifier without making a negative claim.

## 6. Light independent audit

The audit

```text
scratch/audit_l_k16_h1_radius4_primitive_triple_exterior_coatom_20260730.py
SHA-256 d77a3b13aaa1ab6f5594313c505a9673a3bc8f0917cea7e11a3bde96a65a11df
```

authenticates the word, catalogue, primitive packet file and prior no-pair
decision.  It now also authenticates item 1999 and the joint13 position file.
It checks the seven support counts, the `16,420=11,068+5,352` partition, all
12,585 catalogue-exterior positions, the two positions which remain inside
joint13, the exact `|E|=2,3,4` histogram, the absence of `|E|=1`, and the
p6440 disjointness claim.

Independently of the K16 derivation, it exhausts every one of the `7^4=2,401`
nonzero K3 words of length four and 256 deterministic random K4 words.  On
all 11,661 tested sites it compares literal witnesses with the core interval,
brute-forces every changed value, checks upward closure, and verifies that the
maximum/coatom tests preserve existence.  There are 375 positive site
instances, so the audit is not vacuously negative.

```text
scratch/k16_h1_radius4_primitive_triple_exterior_coatom_normal_form_20260730.audit.json
SHA-256 2312c62f9e23af5ebb72adf7306a0be5e615a2bc8cca7118495d27bcf7704d7e
payload a00ccf27ef621a83ee9f202a2766406da9c24a3c8d66f776795b2728e8e51be7
status PASS_SCOPE_AND_SMALL_EXHAUSTIVE_NORMAL_FORM.
```

## 7. Claim boundary

This report is a decision reduction, not a completed K16 census.  A negative
run of the 67,354,920-row kernel would close exactly the primitive-H-triple
plus one catalogue-exterior-cell family (1.1), after composing any rows
already normalized by item 1999.  Such a result would be a value-level
decision inside item 1999's general active-kernel scope; it must not be cited
as a set-theoretically disjoint outside-support theorem.  It would not close:

* an H-installing catalogue pair plus one catalogue and one exterior action;
* a direct four-site H witness with no installing triple;
* a novel value at a catalogue position;
* two or more noncatalogue actions;
* an unrelated length-12,873 source.

Those families remain separate and must not be inferred from this reduction.
