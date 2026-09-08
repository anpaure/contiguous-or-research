# Raw optimal words and the negative-window compiler normal form

Date: 2026-07-28

## 1. Scope and verdict

This audit uses only the files `answers/k01.word` through
`answers/k14.word` and the proved monotone-deadline lower bound.  It does
not read carrier certificates, solver models, search histories, or hand-coded
ownership metadata.

The principal conclusion is an exact compiler normal form.  Once the
depth-`d` middle row is fixed, all upper OR rows are already fixed.  The
remaining lower compiler is an injective assignment of lower masks to short
physical intervals.  Given that assignment, the entry letters have a unique
entrywise-maximal realization obtained by deleting coordinates forbidden by
negative witness intervals.

This is a specialization of the existing full-witness realization theorem
in `MATH_OPTIMAL_NORMALIZATION_EXCHANGE_20260727.md`, not a replacement for
it.  What is new here is:

1. the fixed-middle specialization and its explicit compiler closure;
2. the raw empirical census across every optimum through `k=14`;
3. the discovery that the canonical closure stays optimal and universal in
   every stable case `k=6,...,14`; and
4. a sharp all-`k` missing lemma stated solely as an interval-assignment
   existence problem.

The strongest non-forced common pattern is that all raw optima from `k=9`
through `k=14` have an exactly flat maximal erosion in the interior and the
exact two-sided boundary ramp.  Their lower-mask assignments use only the
nominal rank row or one row deeper, apart from at most four boundary-ramp
exceptions.

## 2. Fixed-middle decomposition

For a word `A=(A_0,...,A_{W+d-1})`, let

\[
  (DA)_i=A_i\cup A_{i+1},\qquad T=D^dA.
\]

Fix a proposed middle row `T=(T_0,...,T_{W-1})`.  Its maximal linear
erosion is

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i,
 \qquad 0\le p<W+d.                                      \tag{2.1}
\]

Every source word with `D^dA=T` satisfies `A_p\subseteq P_p`.  Conversely,
an `A\subseteq P` has `D^dA=T` exactly when

\[
  [i,i+d]\cap\{p:x\in A_p\}\ne\varnothing
  \quad(i<W,\ x\in T_i).                                \tag{2.2}
\]

The upper side decouples completely:

\[
  D^{d+h}A=D^hT\qquad(h\ge0).                            \tag{2.3}
\]

Equivalently, for `j-i\ge d`,

\[
 \bigcup_{p=i}^jA_p=\bigcup_{t=i}^{j-d}T_t.              \tag{2.4}
\]

Thus shrinking or expanding the source inside `P`, while preserving `T`,
cannot change any upper witness.  This is the exact reason the compiler may
be analyzed independently of the upper carrier.

## 3. Exact phase-free compiler theorem

Let

\[
 \mathcal L_{<r}=\{X\subseteq[k]:1\le |X|<r\}
\]

and let `B_{W+d,d}` be the physical intervals of lengths `1,...,d`.
Suppose

\[
 \phi:\mathcal L_{<r}\hookrightarrow\mathcal B_{W+d,d}
\]

is injective.  For a coordinate `x`, define

\[
 Z_x(\phi)=
 \{p:x\in P_p\}\setminus
 \bigcup_{X:\,x\notin X}\phi(X).                        \tag{3.1}
\]

Define the maximal word reconstructed from the assignment by

\[
 A_p^\phi=\{x:p\in Z_x(\phi)\}.                          \tag{3.2}
\]

### Theorem 3.1 (fixed-middle interval-assignment realization)

The assignment `phi` is realized by a nonzero word with middle row `T` if
and only if

\[
 \phi(X)\cap Z_x(\phi)\ne\varnothing
 \quad(X\in\mathcal L_{<r},\ x\in X),                   \tag{3.3}
\]

\[
 [i,i+d]\cap Z_x(\phi)\ne\varnothing
 \quad(i<W,\ x\in T_i),                                 \tag{3.4}
\]

and

\[
 \bigcup_x Z_x(\phi)=[0,W+d-1].                         \tag{3.5}
\]

When these conditions hold, `A^phi` is the entrywise-maximal realization;
it realizes every assigned lower target, has `D^dA^phi=T`, and has exactly
the upper rows `D^hT`.

#### Proof

If `p` belongs to an assigned interval labelled `X` and `x` is not in `X`,
then `x` is forbidden at `p`; this gives (3.1).  Hence the OR on `phi(X)` is
automatically contained in `X`.  Condition (3.3) gives the reverse
containment coordinate by coordinate.  Condition (3.4) is exactly (2.2),
and (3.5) makes all entries nonzero.  Conversely, any realization can use
only positions in `Z_x`; its positive lower witnesses, middle witnesses, and
nonzero entries force (3.3)--(3.5).  Equation (2.3) handles the upper rows.

This is precisely the full-witness criterion after the middle witnesses are
fixed and compressed into the erosion `P`.

## 4. Canonical negative-window closure

Given an already valid word `A`, choose for each lower mask its first short
OR occurrence, in row-major order; call this assignment `phi_A`.  Define

\[
 \mathcal C(A)=A^{\phi_A}.                               \tag{4.1}
\]

Then `A\subseteq C(A)`.  Indeed, if `x\in A_p`, no actual witness interval
containing `p` and labelled by a mask omitting `x` can exist.  Thus every bit
of `A` survives (3.1).  The closure preserves every selected lower witness,
the middle row, and all upper rows.

The operation need not be idempotent.  Newly added bits can create an
earlier occurrence of some lower target.  Re-selecting first occurrences may
therefore change `phi_A`, delete fewer coordinates, and add more bits.  Since
the process is monotone in the finite erosion box `P`, iteration terminates.

This distinction matters in the data.  `k=6` and `k=9` are already fixed;
`k=10` takes one proper expansion; `k=7,8,11,12` take two; `k=14` takes
three; and `k=13` takes four.  This is a genuinely iterative canonicalization,
not merely a one-shot rewriting of the raw word.

At the fixed point every omitted erosion incidence has an explicit reason:
it lies in at least one selected negative witness interval.  Thus the
source-word shrink dependencies are represented entirely by a bipartite
incidence relation

\[
  \{\text{owned lower targets}\}
  \longrightarrow
  \{(p,x):x\in P_p\setminus A_p\}.                       \tag{4.2}
\]

## 5. Raw census

Put `s=r-d`.  `flat/ramp` means that every interior erosion entry has rank
exactly `s`, while the two boundary ramps have ranks

\[
 r,r-1,\ldots,s+1
\]

once on each side.  `off-grade j` means that a rank-`t` target is owned at
row

\[
 \max(0,t-s)+j.
\]

| `k` | `d` | arithmetic slack | erosion-rank profile | flat/ramp | deadline deficit | chosen / erosion bits | pin / essential / nonessential chosen bits | lower duplicate excess | off-grade counts | proper closure rounds / added bits |
|---:|---:|---:|---|:---:|---:|---:|---:|---:|---|---:|
| 6 | 1 | 0 | `2^19 3^2` | yes | 0 | 36 / 44 | 30 / 34 / 2 | 0 | `0:21` | 0 / 0 |
| 7 | 2 | 10 | `2^33 3^2 4^2` | yes | 0 | 66 / 80 | 51 / 53 / 13 | 10 | `0:63` | 2 / 2 |
| 8 | 2 | 51 | `1^4 2^64 3^2 4^2` | no | 0 | 119 / 146 | 110 / 115 / 4 | 51 | `0:92` | 2 / 15 |
| 9 | 2 | 0 | `3^124 4^2 5^2` | yes | 0 | 330 / 390 | 210 / 223 / 107 | 0 | `0:254, +1:1` | 0 / 0 |
| 10 | 2 | 122 | `3^250 4^2 5^2` | yes | 2 | 644 / 768 | 412 / 443 / 201 | 120 | `-1:4, 0:381` | 1 / 57 |
| 11 | 3 | 369 | `3^459 4^2 5^2 6^2` | yes | 0 | 1318 / 1407 | 780 / 781 / 537 | 369 | `0:1023` | 2 / 4 |
| 12 | 2 | 266 | `4^922 5^2 6^2` | yes | 2 | 3108 / 3710 | 1672 / 1847 / 1261 | 264 | `0:1585` | 2 / 209 |
| 13 | 3 | 1059 | `4^1713 5^2 6^2 7^2` | yes | 2 | 5760 / 6888 | 3001 / 3049 / 2711 | 1057 | `-2:1, -1:3, 0:3986, +1:105` | 4 / 598 |
| 14 | 2 | 392 | `5^3430 6^2 7^2` | yes | 1 | 14687 / 17176 | 6434 / 7282 / 7405 | 391 | `-1:1, 0:6206, +1:268` | 3 / 346 |

Exact cross-instance conclusions from the raw files:

1. For every `k=6,...,14`, the depth-`d` row is a permutation of the full
   middle layer, except that the older `k=8` carrier is not flat under
   erosion.  (The small `k=4,5` representatives use genuinely non-flat
   middle schedules.)
2. For every `k=9,...,14`, the maximal erosion has the exact flat interior
   and exact boundary ramp.  This is the `d`-fresh/H-safe property, but here
   it is recomputed from the raw words rather than imported from a carrier
   certificate.
3. Every lower mask has a distinct actual short-cell occurrence, so the raw
   words themselves contain an explicit complete matching of the lower ideal.
4. Every raw assignment through `k=14` is within one row *below* nominal;
   the only larger deviations are earlier boundary-ramp witnesses.  In
   particular, no certificate uses a two-row downward spill.
5. Deadline loss is microscopic: `0,0,0,0,2,0,2,2,1` for `k=6,...,14`,
   despite arithmetic slack reaching 1059.
6. The compiler uses substantial non-pin freedom.  At `k=13`, 2711 of 5760
   chosen coordinate incidences are not individually essential to the
   middle row; at `k=14` the count is 7405 of 14687.  The lower solution is
   therefore not a disguised forced erosion.
7. Canonical closure produces another optimal universal word in every case
   `k=6,...,14`.  Once exactness of the raw middle row has been measured,
   preservation of universality is a theorem from (2.3) and Theorem 3.1;
   the empirical content is the concrete closure trajectory and fixed-point
   structure, not the preservation implication itself.

For every flat stable case `k=6,...,14`, the normalized words have the same
lengths and cover every nonempty mask.  The file emitted for the deliberately
non-flat `k=4` representative is diagnostic only: its reconstructed row is not
a valid fixed-middle normalization and the audit correctly reports one missing
mask.  No theorem or normalized-word claim is made for that file.

| `k` | fixed-point chosen bits | omitted erosion bits | SHA-256 |
|---:|---:|---:|---|
| 6 | 36 | 8 | `7d30e058f98e6c09d65515e3f3971ae8bd7637f711670fa06a8a1dc536852d6d` |
| 7 | 68 | 12 | `1addbe345db71ccce69baf46a2eeca8caf0a3fe24a5e1dfcf2db4a986a5aadb2` |
| 8 | 134 | 12 | `f5b63b6199d94a72e8ba58107dc3693bc82cd4ac482a787c18f2fb0b8b74da15` |
| 9 | 330 | 60 | `c7e8cbfbe1a3531ffae4c9a01bd4b3b51dad0856b38486bacc56dbcaa73e3221` |
| 10 | 701 | 67 | `775e00874892d1f51f966260eb2f47bb8acb0ca06d5bdc05c67c9ab1a7c66278` |
| 11 | 1322 | 85 | `3be742fade22d023241f947b9a25c823a80ede57d76b47630638ace2dda9303f` |
| 12 | 3317 | 393 | `4489ec0b80acdcf439ea38ad309cecbfd5b109623a0c6cd8903acee9f91be17c` |
| 13 | 6358 | 530 | `698fb173d05583da447ffe025c7f27cbb4ceb4b06ec0298827060ae6809debe0` |
| 14 | 15033 | 2143 | `689ad543e36896874540e3c8de4441eb3f95099b354ced7fe3fce20e87f0efd5` |

## 6. What is forced and what is empirical

The following are theorem-level consequences of the existing machinery:

* the monotone-deadline lower bound `nu(k)>=B(k)`;
* the full-witness coordinate criterion;
* Theorem 3.1 as its fixed-middle specialization;
* the upper-row identity (2.3);
* monotonicity and finite termination of the canonical closure; and
* preservation of the witnesses chosen in each closure round, and therefore
  preservation of universality whenever the fixed middle/upper rows already
  cover every rank at least `r`.

The following are raw empirical invariants, not consequences of the lower
bound:

* existence of a flat depth-`d` middle row in these representatives;
* the exact `d`-fresh erosion ramp for every `k=9,...,14`;
* complete lower interval assignments with at most one-row downward spill;
* the tiny deadline deficits; and
* the number of proper closure rounds, added-bit counts, and resulting
  fixed-point rank profiles.

Central flattening is known not to follow from equality alone; `k=4,5` are
the visible small exceptions.  Likewise, a flat erosion alone does not force
the compiler assignment: the current `k=15` Hall-deficient carriers are
counterexamples to any such overstatement.

## 7. The minimal missing all-`k` compiler lemma

The compiler question can now be stated without source-letter variables.

### Missing Lemma CIA (compiler interval assignment)

For every `k`, put

\[
 r=\lceil k/2\rceil,
 \quad W=\binom kr,
 \quad d=\min\{e:\sum_{j<r}\binom kj\le eW+\binom{e+1}{2}\}.
\]

There exists a length-`W` middle carrier `T` whose entries enumerate
`binom([k],r)`, whose upper rows cover every mask of rank greater than `r`,
and an injection

\[
 \phi:\mathcal L_{<r}\hookrightarrow\mathcal B_{W+d,d}
\]

such that the sets `Z_x(phi)` of (3.1) satisfy (3.3)--(3.5).

The raw data support the sharper optional normal form:

* `T` may be chosen `d`-fresh, so its erosion has a flat rank-`r-d`
  interior and the exact boundary ramp; and
* each rank-`t` target may be assigned at row

\[
 \max(0,t-(r-d))
 \quad\text{or one row later},                           \tag{7.1}
\]

apart from `O(d)` boundary-ramp witnesses.

CIA immediately gives an optimal universal word by Theorem 3.1 and (2.3).
Conversely, every optimal word having a flat middle row supplies such a pair
`(T,phi)`.  It is therefore the exact compiler-layer statement, not a
relaxation disguised as a theorem.

The point of (7.1) is algorithmic: it turns the lower compiler from an
unstructured all-row matching into an adjacent-layer overflow problem.  The
`k=15` Hall frontier is then the first failed instance of this flow, rather
than evidence that the source letters need a new kind of SAT model.

## 8. Reproduction and immutable files

Run:

```bash
python3 scratch/analyze_raw_optimal_compiler_normal_form.py \
  --first-k 1 --last-k 14
```

Files:

* analyzer: `scratch/analyze_raw_optimal_compiler_normal_form.py`
* audit: `scratch/raw_optimal_k01_k14_compiler_normal_form_audit.json`
* console summary: `scratch/raw_optimal_k01_k14_compiler_normal_form_audit.stdout`
* normalized words: `scratch/raw_normalized_compiler_words/`

SHA-256:

```text
cda7291ef49cb575f5ea0a5b2c7115c8c1d804084490306aba4869aa77ea10299  scratch/analyze_raw_optimal_compiler_normal_form.py
ceceabe35889c1a972895a90ca50776aa647a2b09f0f4596fda2408971c8a0ca  scratch/raw_optimal_k01_k14_compiler_normal_form_audit.json
```

Individual raw-input hashes and every normalized-output hash are embedded in
the JSON audit.  The primary raw hashes for the recently solved cases agree
with the independent certificate records:

```text
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850  answers/k11.word
6d598c62f5925d1d2dfce8279eea82069318bd93ff66d0b204c639cf06297851  answers/k12.word
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0  answers/k13.word
7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17  answers/k14.word
```
