# Audit of the `opusproblem/work` equivariant quotient construction

Date: 2026-07-28

Scope: read-only audit of

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/cpsat.py
/Users/amir.nuriyev/Downloads/opusproblem/work/equi2.py
/Users/amir.nuriyev/Downloads/opusproblem/work/cutcompile.py
/Users/amir.nuriyev/Downloads/opusproblem/work/gates.py
/Users/amir.nuriyev/Downloads/opusproblem/work/lib.py
```

No SAT or carrier search was run.  The only executions were syntax checks,
small orbit counts, graph reconstruction of an already stored selector, and
independent verification of two stored words.

The audited source SHA-256 values are

```text
aa4e56dbf7b8773fff65f6432857ec8d5123434de8ea0f207b828de55df7aeaf  cpsat.py
d939b89386a313ff306c659f18813c582e3f0cb822c731b44aab7f16776093ff  equi2.py
ae61b7a333a450a4dc13216349e0ab2ddbb2104e5685be3b698ce12816a58a13  cutcompile.py
7d237cc60748e786b84f0235b07b5b2e7b658990f6ca3c69132073aea16f7b63  gates.py
a744bfcedd5786b73a6cbc54d62e9b056f188084a768fbcaf3459726b6b72845  lib.py
```

## 1. Verdict

The cyclic quotient mathematics in `cpsat.py` is valid for composite
`k=15`: the rank-7 and rank-8 actions are free, `AddCircuit` constructs one
quotient Hamilton cycle, and a voltage coprime to 15 makes its lift one
physical 6,435-cycle.  Periodic orbits at upper ranks do not invalidate the
canonical coverage audits.

The current certificate pipeline is nevertheless broken at its file
interface:

> `cpsat.py` removes quotient self-loop choices, but `cutcompile.py` decodes
> the stored integer choice indices with `equi2.py`, which retains those
> choices.

For `k=15` the two enumerations differ after index 6.  Therefore an integer
selector written by `cpsat.py` is reconstructed as a different graph by
`cutcompile.py`.

Separately, a passing cyclic carrier is not an optimal word.  It still needs
a cut which preserves the linear upper gates, an exact lower compiler, and a
full interval-union verification.  If `cutcompile.py` actually emits a
length-`B(k)` nonzero word and `full_verify` reports no missing mask, that
word is a valid upper-bound certificate; together with the proved lower
bound it proves optimality.  No such `k=15` word is present in this directory.

## 2. Composite `k=15` is not the problem

### 2.1 Free action at the two quotient levels

The relevant levels are ranks 7 and 8.  If a subset of `[15]` is fixed by a
nontrivial rotation, its cardinality is a multiple of the length of a
nontrivial rotation orbit, hence has a nontrivial common divisor with 15.
But

\[
                         \gcd(15,7)=\gcd(15,8)=1.               \tag{2.1}
\]

Thus both actions are free.  The assertions at `cpsat.py:41-42` and
`equi2.py:48-49` are mathematically justified for `k=15`, and

\[
             \binom{15}{8}/15=6435/15=429                     \tag{2.2}
\]

is the correct number of quotient middle vertices.

Upper ranks can have shorter orbits; for example rank 9 is compatible with
period 5.  This causes no false coverage claim: `cpsat.py:313-330` and
`equi2.py:376-399` audit actual physical cyclic windows and compare canonical
representatives without assuming freeness at those ranks.

### 2.2 Voltage and connectivity

At `cpsat.py:118-139`, an oriented quotient arc from representative `u` to
representative `w` is labelled by the phase displacement

\[
                             t=s_w-s_u\pmod {15}.               \tag{2.3}
\]

The reverse arc has label `-t`; direct enumeration verifies this for all
11,998 non-loop `k=15` choices.  `AddCircuit` at `cpsat.py:148-152` uses all
429 quotient vertices because no optional self-loop arcs are supplied.  The
constraint at `cpsat.py:173-179` requires the total voltage to be a unit
modulo 15.  A quotient cycle of voltage `v` lifts to `gcd(15,v)` physical
cycles, so this is exactly the condition for one physical cycle.

The hard-coded factor `14` in the loose total-variable bound at
`cpsat.py:174` is valid for `k=15`.  It should be replaced by a bound derived
from `K`, the selected-arc count, and maximum shift for clarity if the code
is advertised for arbitrary `K`.

## 3. Critical implementation findings

### Finding 1 — P0: selector IDs are decoded with the wrong enumeration

`cpsat.py:90-92` skips every choice whose two middle endpoints lie in the
same rotation orbit.  `equi2.py:95-100` retains all such choices.
Nevertheless, `cutcompile.py:57-61` imports `equi2.Carrier` and interprets a
stored integer `sel` through its choice array.

The exact enumeration counts are

| `k` | `equi2` choices | `cpsat` choices | skipped | first ID divergence |
|---:|---:|---:|---:|---:|
| 9 | 140 | 135 | 5 | 3 |
| 11 | 630 | 625 | 5 | 4 |
| 15 | 12012 | 11998 | 14 | 6 |

This is not merely hypothetical.  Decoding
`cpsat_k11_rnd0.json` correctly gives a connected 462-vertex 2-regular
graph.  Decoding the same 42 indices as `cutcompile.py` does gives:

```text
418 vertices, 462 distinct edges;
degree histogram {1:143, 2:154, 3:33, 4:66, 5:22};
largest component 363 vertices;
all 42 selected choice tuples wrong.
```

**Required fix.**  Never serialize bare enumeration indices.  Store the
explicit choice tuples `(low_rep_mask,a,b)`, the selected directed arcs, the
enumerator version, and a SHA-256 digest of the complete ordered choice
table.  `cutcompile.py` must reconstruct from those tuples and reject a
digest mismatch.  Alternatively it may import `QModel`, but explicit tuples
make the certificate independent of OR-Tools and source ordering.

### Finding 2 — P0: cyclic `PASS` is not an optimal-word certificate

`cpsat.py:475-479` writes `{"k":K,"sel":sel}` and returns `PASS` once the
**cyclic** residence and shadow audits pass.  It does not choose a linear
cut, solve the lower compiler, or verify all nonempty masks.

A cyclic target may occur only in a window crossing a chosen cut.  Hence
cyclic all-depth coverage does not imply that any particular linearization
has complete upper coverage.  The required later gates occur only at
`cutcompile.py:65-83`:

1. select a cut;
2. recheck linear residence and upper coverage;
3. solve the lower compiler; and
4. call `full_verify` on the literal word.

The correct theorem statement is therefore conditional:

> A quotient `PASS` proves existence of the audited cyclic carrier only.  A
> saved word proves `nu(k)<=B(k)` only after an independent exact full-word
> verification and a length/nonemptiness check.

### Finding 3 — P1: the cut driver is incomplete and under-audited

`cutcompile.py:68-85` stops after the first eight cuts which pass its path
gates.  Consequently `no cut compiled` is not evidence that the cyclic
carrier has no compilable cut.  A theorem-grade negative result must inspect
all `W` cuts or prove a cut reduction theorem.

The reconstruction at `cutcompile.py:35-45` follows the first available
neighbor and checks only `len(cyc)==W` at line 63.  Before using a carrier it
should independently assert:

* exactly all `W` distinct rank-`r` masks occur;
* every physical vertex has degree two;
* every edge is a Johnson edge and has the claimed lower color;
* the graph is connected;
* all selected lower colors are distinct and complete; and
* the reconstructed directed voltage agrees with the stored certificate.

The final `full_verify` protects a successfully emitted word from these
carrier-level mistakes, but the missing checks can cause hangs, false
diagnostics, and invalid intermediate claims.

### Finding 4 — P1: restricted search and lazy clauses affect completeness

Excluding the 14 self-loop choices at `cpsat.py:90-92` is legitimate for a
construction search, but an `UNSAT` result then applies only to that
restricted quotient class.  It is not a no-go theorem for equivariant
carriers.

The lazy q2/q3 motif clauses at `cpsat.py:345-443` and
`equi2.py:414-512` are search accelerators, not certificate evidence.  They
encode selected *choice sets*, suppressing some phase/order information.
They may be incomplete or may fail to cut a physically missing motif.  This
cannot create a false final `PASS`, because every SAT endpoint is rebuilt
and audited at `cpsat.py:456-475` or `equi2.py:532-555`.  It can, however,
stall CEGAR or make a restricted `UNSAT`/exhaustion claim too strong.

### Finding 5 — P2: the compiler launches a local Homebrew solver

`gates.py:16` hard-codes

```text
/opt/homebrew/bin/kissat
```

and `gates.py:108-109` executes it directly.  This violates the current
remote-only heavy-search policy and makes the script nonportable.  Read the
solver path from an explicit command-line option/environment variable and
run production compilation on the `h100` CPU host.  The deterministic final
word verifier may remain local.

## 4. Constraint-by-constraint soundness

| Requirement | Where checked | Audit |
|---|---|---|
| all quotient middle vertices in one cycle | `cpsat.py:148-152` | sound for the non-loop quotient class |
| one q1 lower color orbit each | `cpsat.py:153-172` | sound; freeness lifts it to every rank-7 mask |
| one physical lifted cycle | `cpsat.py:173-179`, then `249-276` | sound for `k=15` |
| cyclic minimum residence | automaton `180-208`, exact audit `291-311` | endpoint audit prevents false `PASS` |
| cyclic upper coverage | `313-330` | exact physical audit |
| cyclic lower q2/q3 coverage | `332-343` | exact physical audit |
| linear minimum residence after cutting | `cutcompile.py:47-51` via `lib.py:46-54` | exact |
| linear upper coverage | `cutcompile.py:47-51` via `lib.py:73-102` | exact |
| literal middle windows | `gates.py:54-62` | exact given `A<=P` |
| every lower mask on a short window | `gates.py:63-94` | exact SAT encoding |
| nonempty letters | `gates.py:48-53` | exact |
| every nonzero mask is an interval union | `lib.py:164-176` | exact exhaustive verifier |

The residence variables in `cpsat.py` are intentionally one-way: insertion
forces ages `1,...,D`, then age information may disappear.  That suffices to
forbid deletion during the first `D` steps.  Even if the automaton were
misencoded, the exact reconstructed-cycle check at `cpsat.py:463-466` would
reject the endpoint rather than issue a false `PASS`.

## 5. Does a carrier plus compiler prove an optimal word?

Yes, but only at the literal-word endpoint.

Let `r,W,d=params(k)`.  The SAT word has length `W+d`.  Its constraints make
`D^d A=T`.  For any interval of `A` of length at least `d+1`,

\[
 \bigcup_{t=p}^{q}A_t
   =\bigcup_{i=p}^{q-d}T_i.                                    \tag{5.1}
\]

Thus carrier windows supply the middle and upper masks, while the SAT
selectors supply all lower masks on intervals of length at most `d`.
`full_verify` then checks the original problem directly, without relying on
this factorization proof.

Therefore the sufficient certificate is:

```text
len(word) == W+d
all(0 < word[i] < 2^k)
full_verify(word,k) == []
```

Together with the proved monotone-deadline lower bound `nu(k)>=W+d`, these
three facts prove `nu(k)=B(k)`.

A quotient selector, a connected physical carrier, complete cyclic shadows,
or SAT status alone does not prove the formula.

## 6. Existing artifacts

An independent brute-force interval-union pass gives:

```text
k=9:  len(k09_equi_new.word)=128=B(9),  missing=0, nonzero=True
k=11: len(k11_equi_new.word)=465=B(11), missing=0, nonzero=True
```

Hence those two stored word files are valid optimal upper certificates when
paired with the general lower bound, regardless of how their carriers were
found.

There is no `*_PASS.json` and no `k15` word in the audited directory.
`cpsat_k11_rnd*.json` are intermediate cyclic selectors (for example round
0 still has five lower-q2 orbit misses).  No current artifact here proves
`nu(15)=6438`.

## 7. Minimal repair sequence

1. Replace bare choice IDs by explicit, versioned choice tuples and a choice
   table digest.
2. Add a standalone selector verifier which reconstructs directed quotient
   arcs, voltage, the physical cycle, residence, and every cyclic shadow.
3. Make `cutcompile.py` validate the physical graph before traversal and, for
   completeness claims, inspect every admissible cut.
4. Move Kissat invocation behind an explicit remote solver configuration.
5. Save the final word together with `k,r,W,d`, its SHA-256 digest, and the
   exact missing-mask count from an independent verifier.

After these repairs, a successful `k=15` word would be theorem-grade.  They
do not make the search easier, but they prevent a quotient or serialization
success from being mistaken for the conjecture itself.
