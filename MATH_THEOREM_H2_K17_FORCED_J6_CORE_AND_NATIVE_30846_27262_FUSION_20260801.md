# Forced-J6 run8 core and a native two-colour fusion

Date: 2026-08-01  
Lane: H2 independent audit / finite `k=17` SCD socket selector  
Status: **verified scoped UNSAT core; verified local catalogue escape**

This note has two deliberately separate conclusions.

1. Forcing the safe-open pivot macro `J6` is UNSAT in the exact frozen
   run8 base global-q1 selector.
2. The three-owner path displayed in Section 4 removes that particular
   implication core at literal owner/q1 level.  It is a prospective new
   joint column, not a completed global selector or a `k=17` word.

No unrestricted `k=17` impossibility is claimed.

## 1. Authenticated computational scope

The H100 run directory is

```text
/dev/shm/k17_global_q1_master/run8_j6_safeopen_k64_socket512
```

The exact base model has

```text
2,203,040 variables
10,758,117 clauses
SHA-256 df56ead17b7fd245899a580b3193547d20e8abd6778dc57bcebcc7b7ef6131cb
```

The forced base differs by the single unit clause

```text
551076 0
```

and map variable `551076` is `macro J6`.  The larger eager model is the
byte-exact concatenation of the base with the static provider-chain,
one-seam actual-fragment, and multi-seam actual-fragment blocker CNFs.  Its
forced hash is

```text
b6fd1c27ad09ed557ec476c972d62fb1247f0541b5b18e782f1e733ff034575b.
```

The full forced eager DRAT has SHA-256

```text
c4dc3b23cd96dd4bc6537df8b2c2a8096f3095c5698fba5b0f31e2de6d87269e
```

and was verified.  More strongly, proof trimming leaves a `26`-clause
input core: `25` clauses already belong to the base model and the last is
the forced `J6` unit.  Thus the eager blocker appendices are not used in
the contradiction.

The local core and its tiny proof are

```text
scratch/h2_k17_forced_j6_core_20260801/
  eager_exact_force_j6.input_core.cnf
    SHA-256 20d2e8c6fb193f2cb9c5833628313d9aab3bc0e5b37a0246851ba39dd403556d
  eager_exact_force_j6.corelemmas.drat
    SHA-256 ee53a95aec1673668bda173c27d8fd86335fbede0f1ffa77b2dbc4835c69a376
```

Independent local `drat-trim` replay reports `s VERIFIED`.

The exact model scope is the run8 generalized global-q1 selector with the
published `193` socket target groups capped at `512`, the rank-ten provider
atlas capped at `64`, no shared guards, and the named joint macros.  The
builder binary is hashed upstream, but no byte-matching retained source for
the final J6-safe-open binary was found.  Therefore the CNF/core/proof is
authenticated while source-level rebuild provenance is incomplete.

## 2. Exact projected core

Use the following names.

| symbol | DIMACS variable | meaning |
|---|---:|---|
| `J` | 551076 | safe-open macro `J6` |
| `c1` | 2186801 | cut `634:6` |
| `S` | 81716 | socket row 81715, parent target 28926 |
| `B0,B1` | 157459,157460 | the two providers of target 30846 |
| `c2` | 2187074 | cut `686:4` |
| `D0,D1` | 143615,143616 | the two providers of target 27262 |

Existentially eliminating all twelve auxiliary variables from the
`25` non-unit core clauses gives exactly

\[
\begin{aligned}
J&\Longrightarrow c_1,\\
c_1&\Longrightarrow S\vee B_0\vee B_1,\\
S,B_0,B_1&\Longrightarrow c_2,\\
c_2&\Longrightarrow D_0\vee D_1,
\end{aligned}
\]

together with at-most-one on `D0,D1` and the complete conflict biclique

\[
             \{S,B_0,B_1\}\;\square\;\{D_0,D_1\}.       \tag{2.1}
\]

The independent audit checks this projection on all `256` assignments of
the eight named variables.  With `J=1`, the projected system has no
satisfying assignment.

### Human proof

`J6` extracts owner `30782` and therefore forces cut `634:6`.  The old edge
at that cut has rank-ten colour

\[
                  28798\cup30782=30846.                 \tag{2.2}
\]

The frozen catalogue has three ways to repay it: the target-28926 socket
row, which internally contains a 30846 edge, or either of the two ordinary
30846 providers.  Every one of the three forces cut `686:4`.  That cut
deletes

\[
                  26750\cup27198=27262.                 \tag{2.3}

The only two 27262 providers use component-686 range `[0,4)` in the two
possible roles/orientations.  Each conflicts with each of the three 30846
repayment modes, giving (2.1).  Hence no repayment can be selected.  This
proves the scoped forced-J6 UNSAT theorem without referring to the eager
blocker clauses. \(\square\)

## 3. Minimum logical escape

At the projected Boolean level, one new column is enough and is necessary
to break this core.  It may be any of:

1. a new 30846 repayment mode compatible with one current 27262 mode;
2. a new 27262 repayment mode compatible with one current 30846 mode; or
3. one joint column which repays both 30846 and 27262.

Adding unrelated rank-ten providers cannot affect the core.

## 4. Literal native fusion

There is an explicit column of type 3:

\[
                 30844\longrightarrow26750\longrightarrow27246. \tag{4.1}
\]

Its physical occurrences are

```text
component 2002, position 0
component  686, position 3
component 1965, position 0
```

and its exact palettes are

\[
\begin{array}{c|cc}
 &\text{first edge}&\text{second edge}\\ \hline
\text{upper}&30846&27262\\
\text{lower}&26748&26734.
\end{array}                                           \tag{4.2}
\]

All three owners have rank nine, both edges are Johnson edges, and the two
upper and two lower colours are distinct.  The maximal depth-three source is

\[
       30844,26748,26732,26732,26734,27246,             \tag{4.3}

which is nonempty and replays (4.1) exactly.  There is no internally bounded
positive run of length below four.  The fusion is owner-disjoint and
q1-palette-disjoint from the opened J6 path.

The required extraction cuts are

```text
2002:1, 686:3, 686:4, 1965:1.
```

Their upper colours are respectively

```text
30972, 26878, 27262, 27502.
```

Colour `27262` is repaid internally by (4.2), so the exported child bank is

\[
                         \{26878,27502,30972\}.          \tag{4.4}

The frozen context-extendable atlas has raw provider counts `16,20,12` for
these three colours.  After excluding every J6/fusion owner position,
every forced internal cut, and the J6-forbidden cut `1484:6`, the counts are

\[
                         10,18,12.                       \tag{4.5}

There are `1,584` triples choosing one provider for each colour whose
physical owner ranges are pairwise disjoint and whose required cuts do not
split another chosen range.  Thus the fusion has no immediate exported
zero row.  Equation (4.5) is only a local control: it does not prove that
one of these triples survives all other sockets, macros, and global rows.

The literal macro is frozen at

```text
scratch/k17_j7_forced_j6_core_native_fusion_20260801.tsv
```

with SHA-256

```text
7a0fa8cf82cbf8ec022308cf2eda85c3ccdb8270af450ab52b123f23b82b39d4.
```

## 5. Audit artifact and exact remaining gate

The independent replay is

```text
scratch/audit_h2_k17_forced_j6_core_and_native_fusion_20260801.py
  SHA-256 07035725a79900b2e93d00ef01084ead502ce7df19f864a3f6a139704401aec9

scratch/h2_k17_forced_j6_core_and_native_fusion_20260801.audit.json
  SHA-256 20e139d5c53a231fe1eacf7d9cb623477affa2588c3e19b79f6f135b22f6c7cf
  payload 55466fbfa404c1df9c066d5ab4a4b6e296150ac496f12301a8045a6c075ef899
```

The next exact finite test is to add (4.1) as a joint column to the
prospective selector, credit it for both 30846 and 27262, impose its four
cuts and three owner resources, and recompute all boundary-child occurrence
clauses from the union of selected cuts.  The parent demand 28926 remains a
separate socket group: bypassing core row 81715 does not pay that demand, so
the expanded model must also select another compatible 28926 row.  Only
after that model is feasible may one proceed to directed chronology, ranks
11 and above, lower/common-cap matching, and the literal `k=17` word.
