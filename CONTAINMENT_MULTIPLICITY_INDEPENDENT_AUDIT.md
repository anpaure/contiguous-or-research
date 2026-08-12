# Independent audit: containment multiplicity, simultaneous caps, and the k=11 encoding

## Verdict

**PASS with one local correction.**

The containment-multiplicity theorem is correct, its simultaneous
witness-length cap is correct, and the optional
`K11_FOREST_CONTAINMENT_CAPS` implementation in `k11_forest_sat.cpp` is a
sound necessary strengthening of the unrestricted length-465 formula.

The correction is to the domain of the nested interval-count inequality.  The
display

\[
  \sum_{c_s(n)\le t}\binom{k}{s}
    \le tn-\binom t2
\]

is valid as written for `1 <= t <= n`, not for every integer `t>=1`.  For a
completely unrestricted statement the right side must instead be

\[
  \sum_{\ell=1}^{\min(t,n)}(n-\ell+1).
\]

This correction does not affect any useful cap test, since every
`c_s(n)<=n`.

The new containment theorem is genuinely new relative to the current
`MATHEMATICAL_HANDOFF.md`: item 41l contains only the same-rank cap and the
higher-rank/lower-target cap.  The new `r<s` term sharply prunes upper-rank
witnesses.  By contrast, the MTF--SCD implication is not new: it is already
Theorem 1 of `GLOBAL_MTF_SCD_HANDOFF.md` and item 180 of
`MATHEMATICAL_HANDOFF.md`.

## 1. Audit of the containment-multiplicity theorem

Fix a rank `r`, write

\[
  M=\binom{k}{r},\qquad n=M+d,
\]

and choose one witness interval for each rank-`r` mask.  Order these intervals
by increasing left endpoint:

\[
  I_i=[a_i,b_i],\qquad 1\le i\le M.
\]

Equal-rank masks are incomparable.  Thus no two selected intervals nest, so
both endpoint sequences are strictly increasing.  Since each is an
`M`-element subset of `[n]`,

\[
  i\le a_i\le i+d,\qquad i\le b_i\le i+d,
\]

and hence

\[
  I_i\subseteq[i,i+d].                                      \tag{1}
\]

Let `J=[u,v]` have length `ell=v-u+1`.  If `ell>d`, then every index

\[
  u\le i\le v-d
\]

satisfies `I_i subseteq [i,i+d] subseteq J`.  The apparently delicate index
range is valid:

* `u>=1` trivially;
* `ell>d` and `v<=M+d` imply `u<=M`;
* `v-d<=M` follows directly from `v<=M+d`.

Therefore `J` contains at least

\[
  (v-d)-u+1=\ell-d                                    \tag{2}
\]

distinct selected rank-`r` witnesses.

If `OR(J)` has rank `s`, each such selected witness is a distinct rank-`r`
subset of that `s`-set.  There are at most `binom(s,r)` of them.  Consequently

\[
  \ell-d\le\binom{s}{r}
\]

when `s>=r`.  If `s<r`, even one contained rank-`r` witness is impossible, so
`ell>d` is impossible.  Thus every interval whose OR has rank `s` obeys

\[
  \boxed{
  \ell\le
  \begin{cases}
    d,&s<r,\\
    d+\binom{s}{r},&s\ge r.
  \end{cases}}
                                                               \tag{3}
\]

No fixed-row, chosen shortest witness, or compatibility assumption is hidden
in this proof.  The chosen rank-`r` witness family may be selected separately
for each `r`; (3) holds for every physical interval `J` after any such choice.

## 2. Simultaneous cap

For a proposed length `n`, (3) yields the correct cap

\[
 c_s(n)=\min\left(
 n,
 \min_{\substack{r>s\\\binom{k}{r}\le n}}
       \left(n-\binom{k}{r}\right),
 \min_{\substack{1\le r\le s\\\binom{k}{r}\le n}}
       \left(n-\binom{k}{r}+\binom{s}{r}\right)
 \right).                                                     \tag{4}
\]

This subsumes the previous cap:

* `r=s` gives `n-binom(k,s)+1`;
* `r>s` gives `n-binom(k,r)`;
* `r<s` is the new upper-target contribution.

For `1<=t<=n`, every rank with `c_s(n)<=t` must use one of the

\[
  \sum_{\ell=1}^{t}(n-\ell+1)=tn-\binom t2                 \tag{5}
\]

physical intervals of length at most `t`.  Distinct masks cannot share a
physical interval, proving the corrected nested inequality.

Taking `n=binom(k,r)+d` and `t=d` recovers the original rank-slack inequality,
because every rank below `r` has cap at most `d`.  Thus the new family
subsumes the old family.  It should not be advertised as a new contradiction
to `nu(k)=B(k)`: the reported scan through `k=500` finds none, and that
empirical observation is not part of the theorem.

## 3. Exact k=11 caps

At `k=11,n=465`, the binomial row is

\[
  11,55,165,330,462,462,330,165,55,11,1.
\]

Applying (4) gives:

| target rank `s` | old `safe_bound(s)` | new `containment_bound(s)` | best new source |
|---:|---:|---:|---|
| 1 | 3 | 3 | a higher central rank |
| 2 | 3 | 3 | a higher central rank |
| 3 | 3 | 3 | a higher central rank |
| 4 | 3 | 3 | a higher central rank |
| 5 | 3 | 3 | rank 6 |
| 6 | 4 | 4 | rank 6 itself |
| 7 | 136 | 10 | `465-462+binom(7,6)` |
| 8 | 301 | 31 | `465-462+binom(8,6)` |
| 9 | 411 | 87 | `465-462+binom(9,6)` |
| 10 | 455 | 213 | `465-462+binom(10,6)` |
| 11 | 465 | 465 | no improvement |

Hence the supplied cap table `3,3,3,3,3,4,10,31,87,213,465` is exact.

These are useful search cuts even though the aggregate nested counts do not
rule out 465: they replace very long possible upper witnesses by local ones.

## 4. Source audit

Audited current source:

```text
78360d76011be1b6f600baf944e51e2949f059231595864233dd8dc8d0b3d7b8
    k11_forest_sat.cpp
```

Comparison source immediately before the containment option:

```text
a66bf34be18ae09c3b22252fe96c7dd96f9f780495ce0acd1fa7868d3f015247
    k11_forest_sat_density.cpp
```

The source change is confined to:

1. `containment_bound(rank)`;
2. the opt-in environment flag `K11_FOREST_CONTAINMENT_CAPS`;
3. substituting `witness_bound` for `safe_bound` on direct targets, generic
   exception slots, and crossed rank-seven witnesses;
4. reporting the flag in the diagnostic line.

The arithmetic in `containment_bound` implements (4) exactly.  The condition
`family<=N` is correct.  At `k=11,n=465` all rank families satisfy it.

The unary interval encoding enforces a cap `b` with clauses

```text
-Inside(p) -Inside(p+b)
```

for all `p+b<N`.  Since `Inside` is already constrained to be one nonempty
contiguous interval, these clauses are equivalent to length at most `b`.

For a nonexceptional rank-seven target, the crossed interval represents the
target when its `active` flag is true.  When it is inactive, tightening its
otherwise dummy interval remains harmless: a singleton dummy interval is
always available.  Generic exception intervals are actual target witnesses
and obey the same theorem.  Therefore there is no active/inactive soundness
gap.

The option allocates no variables.  It only adds binary length-cap clauses.
The exact additional-clause inventory in the fully enabled adjacent-shadow
formula is:

| encoded family | occurrences | old/new cap | extra clauses each | total |
|---|---:|---:|---:|---:|
| crossed rank-7 witnesses | 330 | 136 / 10 | 126 | 41,580 |
| generic rank-7 exception slots | 6 | 136 / 10 | 126 | 756 |
| direct rank-8 targets | 165 | 301 / 31 | 270 | 44,550 |
| direct rank-9 targets | 55 | 411 / 87 | 324 | 17,820 |
| direct rank-10 targets | 11 | 455 / 213 | 242 | 2,662 |
| **total** |  |  |  | **107,368** |

Each extra clause contributes three solver `add` calls including its terminal
zero, so the literal-stream call count rises by exactly `322,104`.

## 5. Independent remote build-only regression

All production-formula builds ran on the remote host with a hashing CaDiCaL
stub and `K11_FOREST_BUILD_ONLY=1`; no SAT solve was launched.  The enabled
stack was the current adjacent-shadow, rank-three-shadow, band, joint-band,
endpoint-alignment, canonical-rank6, singleton-pool, and rank6-boundary stack.

| portfolio | caps off: variables / clauses | caps on: variables / clauses | delta |
|---|---:|---:|---:|
| branch 0, no min-component restriction | 2,924,697 / 14,732,380 | 2,924,697 / 14,839,748 | 0 / +107,368 |
| `e0c1` | 2,924,697 / 14,772,036 | 2,924,697 / 14,879,404 | 0 / +107,368 |
| `e1c2` | 2,924,938 / 14,811,758 | 2,924,938 / 14,919,126 | 0 / +107,368 |

Disabled-mode preservation was checked against the pre-change source.  In all
three portfolios, the variable count, clause count, literal-call count, and
both 64-bit ordered literal-stream hashes agree exactly:

| portfolio | clauses | literal calls | hash1 | hash2 |
|---|---:|---:|---|---|
| branch 0 | 14,732,380 | 65,118,464 | `508f5b599ffa2587` | `ce4ebfb80b9d4243` |
| `e0c1` | 14,772,036 | 65,261,404 | `1ba2f6438525dabf` | `08e01def7963e234` |
| `e1c2` | 14,811,758 | 65,383,266 | `a90ec30698cb6056` | `b12d755236aaccbd` |

Thus “disabled mode unchanged” is true for the formula stream.  The stderr
diagnostic naturally gains the text `containment_caps=0`; that is not a CNF
change.

Remote audit directory:

```text
/root/k11_containment_independent_audit_20260723
```

Representative hash artifacts:

```text
70c5ad71c35e21e2bffdb393115d9c1392e0f8179e5f475272b8052e388f3ef4
    branch0_old.hash = branch0_newoff.hash
5ec21993585b36a2e3e4382adf9a83ed33a49c4af4e9854223704144f50c7fb3
    branch0_newon.hash
2941dd18d35e62231c7420e6ab7a7a286666a71e1ec005e62e4cba48067334e1
    e0c1_old.hash = e0c1_newoff.hash
ab49ccbd7a78f8b675b87b1e93af5cb667aae339c3644c7447abb7ebbeda6aab
    e0c1_newon.hash
fb2412ca9f11a3b738a35e4d1fae0dd978f3b78a5caf98c0f0e22e4a92d174f4
    e1c2_old.hash = e1c2_newoff.hash
656862f2d67c1f0d0054d3d3a59bf1b6a091947e4ef026b0ec7bd4f97839a128
    e1c2_newon.hash
```

The containment option composes independently with the local-density PB
option: it adds no PB variables and the same 107,368 clauses.

## 6. Audit of the MTF--SCD material

The theorem is correct after one wording repair: an ordered partition exposes
the **nonempty** members of its SCD chain.  It cannot expose the empty member
as a nonempty suffix OR.  This is already stated correctly in
`GLOBAL_MTF_SCD_HANDOFF.md`.

The displayed `k=5` tour is valid.  Its ten chains are disjoint symmetric
chains with total size 32.  The proposed states expose them, and the updates

```text
8, 16, 1, 2, 8, 18, 20, 5, 9
```

indeed perform the listed move-to-front transitions.  Initializing the first
state in reverse gives the explicit 14-entry word

```text
8,16,1,2,4,8,16,1,2,8,18,20,5,9.
```

At its ten designated endpoints, its suffix chains contain every nonempty
member of the ten SCD chains, so it is universal.

This is useful finite evidence for the missing state-transversal path lemma,
but it is not a new general construction and is not competitive at `k=5`:
the exact optimum is 12.  The additional assertion that explicit tours were
also found for `k=3,4,6` was not accompanied by state tables or certificate
files in the supplied result and should not be promoted on that text alone.

## 7. Integration advice

1. Add (3)--(5) immediately after handoff item 41l, with the restriction
   `1<=t<=n` stated explicitly.
2. Record the exact k=11 cap vector and the optional solver flag in
   `K11_INTEGRATED_SEARCH.md`.
3. Enable `K11_FOREST_CONTAINMENT_CAPS=1` for new exact k=11 portfolios.  It
   is a sound, variable-free localization cut and is materially stronger on
   ranks 7--10.
4. Do not relabel the MTF--SCD theorem as new.  Optionally add the valid k=5
   tour to `GLOBAL_MTF_SCD_HANDOFF.md` as finite evidence.
5. Do not copy stale numerical status from the supplied result.  The current
   repository already has the verified nonzero `k=11` upper bound 477, not
   478 (and certainly not the older lift bound 508).

The main mathematical advance in the supplied text is therefore the
containment-multiplicity theorem and its upper-rank localization, not a proof
of `nu(k)=B(k)` and not a new MTF construction theorem.
