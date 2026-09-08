# Final GO cross-audit: protected weighted boundary and common-core witness reservoir

**Date:** 2026-08-04  
**Verdict:** **GO for the two corrected local theorems.  NO-GO for any
inferred protected-factor completion or distinct-component planting.**

## 0. Audited objects

The audit started from:

- `MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md`,
  input SHA-256
  `2fad0407613763ff88cad8621d0d3e2124ae4ce71b0b3701bde6b4b67c03bdbc`;
- `MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md`,
  input SHA-256
  `82832c4a1754ed26e6d20ab5c909d7d65982f4acf6228bf27a5d89bcb53d08c9`.

The audited successors have SHA-256 values

- weighted-boundary theorem:
  `4bb0621bdac66579eefba12c8b270d6334c517468d7f0deba277943f0bfc8891`;
- common-core reservoir theorem:
  `3aaaf6388256954b2579581353f3c1e456198d6f7a4ebd0a9de951945695f983`.

The corrections are scope hardening, not a reversal of either local
result: the weighted statement now explicitly assumes `m>=2`; the
reservoir statement explicitly assumes `3<=c<=m`, proves the omitted
within-path owner/upper-colour distinctness row, and states the exact
setwise coinstantiation `P_c subseteq P_D` in the `c=m` specialization.

## 1. Weighted Ore boundary: line-by-line check

Let `a_U=|N(U) cap A|`.  Since every lower vertex has degree `m`,

\[
                         \sum_U a_U=m|A|.
\]

Hence

\[
 \sigma(A)=\sum_U\left(\min(2,a_U)-{2a_U\over m}\right).
\]

The summand is exactly

\[
 h_m(a)=
 \begin{cases}
 0,&a=0,m,\\
 (m-2)/m,&a=1,\\
 2(m-a)/m,&2\le a\le m-1.
 \end{cases}
\]

This proves both the unscaled and scaled identities.  In particular, the
endpoint `a=m` is sound: then `N(U) subseteq A`, so
`p_U=e_P(U,L setminus A)=0`; both boundary capacity and protected loss are
zero.  The original formula would fail only at the degenerate `m=1`
collision `a=1=m`, which is why the corrected theorem states `m>=2`.

For the protected loss, direct evaluation of

\[
 \min(2,a)-\min(2-p,a)
\]

gives zero for `a=0`, the indicator of `p=2` for `a=1`, and `p` for
`a>=2`.  Therefore

\[
 \lambda_P(A)=q_1^P(A)+q_{\ge2}^P(A)
\]

and the scaled inequality is exactly, not merely sufficiently,

\[
 m(q_1^P+q_{\ge2}^P)
 \le (m-2)n_1+2b_{\ge2}.
\]

The two separated rows are individually stronger than necessary but are
a valid sufficient certificate: adding them yields the exact row.  The
corrected text also formalizes the more general capacity split by requiring
nonnegative `c_1,c_2` whose sum is at most the total boundary capacity and
which separately dominate the two scaled losses.  No direction of an
inequality is reversed.

For `A={x}`, precisely the `m` owners above `x` have `a_U=1`, giving
`sigma(A)=m-2` and the stated sharp singleton row.  This agrees with the
explicit one-cone obstruction.

## 2. Common-core compression and target count

For a seam base `U_i=K union {a_(i-1),a_i}`, the condition `U_i subseteq Z`
is equivalent to `Z=K union T` with the displayed seam pair contained in
`T`.  Since `K` and `E` partition the ground set, the trace `T=Z setminus K`
is unique.  Removing the full ground set is exactly the restriction
`T ne E`.

Among the `c` distinguished external labels, a trace avoids every seam
pair exactly when its distinguished part is independent in `C_c`; the
other `m-c` coordinates are free.  Thus the optional count

\[
 2^{m-c}(2^c-I(C_c))-1
\]

is correct.  The corrected parameter row `3<=c<=m` matches the simple
cyclic hinge ring on which this count and the distinct seam bases rely.

## 3. Top-path collision, palette, and union check

For `1<=ell<=m-1`,

\[
 |O_{j,ell}|=(m-1)-(ell-1)+ell=m.
\]

Consecutive owners delete `k_ell` and insert `e_(j+ell+1)`, and their
intersection is the stated rank-`m-1` lower colour.  The external traces
of owners and lower colours are the cyclic intervals `T_(j,ell)`; fixed
length cyclic intervals of length below `m` are distinct, and different
lengths have different sizes.  The upper colour on adjacency `ell` has
external trace `T_(j,ell+1)`, so that palette is also globally simple.

The first owner contains all of `K`, and the external traces along the
first `ell` owners are nested with union `T_(j,ell)`.  Therefore every top
prefix has union exactly `K union T_(j,ell)`.  No owner, lower colour, or
upper colour is repeated across the `m` top paths.

## 4. Private paths, including the `q=2` truncation

If `T` is noninterval and belongs to the damage family, it contains a seam
pair, so `q=|T|>=2`; since every external co-singleton is cyclically
contiguous, `q<=m-2`.

For `q=2`, deleting two distinct coordinates `u_T,v_T` from `K` gives two
distinct rank-`m` owners.  They are Johnson adjacent, their lower colour is

\[
 (K setminus\{u_T,v_T\}) union T,
\]

and their upper colour and path union are both `K union T`.  This is the
correct truncation; a longer cyclic-window construction is neither used
nor needed.

For `q>=3`, put `p=q-1` and `n=m-1`.  Then `2<=p<=n-2`.  The `n` cyclic
`p`-windows are distinct, so the owners `V_(T,j)` are distinct rank-`m`
sets.  Adjacent deletion windows have:

- union a cyclic `(p+1)`-window, producing distinct rank-`m-1` lower
  colours; and
- intersection a cyclic `(p-1)`-window, producing distinct rank-`m+1`
  upper colours.

All vertices and both palettes on one private path are therefore simple.
Different private targets have different exact external traces.  A private
trace is noninterval, whereas every top-bank trace is an interval, so
owners and both palettes are disjoint across all paths.  Finally the
intersection of all cyclic `p`-windows is empty because `p<n`; every
coordinate of `K` survives somewhere, and the full private-path union is
exactly `K union T`.

As an independent finite check, the set construction was enumerated for
every `4<=m<=9` (over all noninterval traces, a superset of the traces
actually needed for a fixed damage family).  In each case owners, lower
colours, and upper colours were globally collision-free; every adjacency
had Johnson distance one; and every claimed path union was exact.  This
finite check is corroborative only; the preceding argument is the proof.

## 5. Incidence degree and size

Subdividing a Johnson adjacency by its unique lower intersection gives two
Middle-Levels incidence edges.  Global owner and lower-colour simplicity
implies that the incidence paths are vertex-disjoint; internal owner and
lower vertices have degree two and endpoints degree one.  Hence
`Delta(P_D)<=2`.

There are `m` top paths.  Every long path has `m-1` owners and therefore
`2(m-2)` incidence edges; every `q=2` private path is shorter.  With at
most `|D|` private paths,

\[
 |E(P_D)|\le2(m-2)(m+|D|)<2(m-2)(m+2^m).
\]

Since

\[
 W={2m-1\choose m}\asymp {4^m\over\sqrt m},
\]

the ratio is `O(m^(3/2)/2^m)=o(1)`.  The stated `o(W)` size is correct.

## 6. Literal `c=m` coinstantiation and prefix transport

When `c=m`, orient `E` so that
`T_(i,ell)={a_i,a_(i-1),...,a_(i-ell+1)}` and put `k_1=b`.  Direct
substitution gives

\[
 O_{i,1}=K union\{a_i\}=L_i,
\]

\[
 O_{i,2}=(K setminus\{b\}) union\{a_i,a_(i-1)\}=R_i,
\]

and their lower intersection is `I_i=B union {a_i}`.  Consequently the
two incidence edges of every ring hinge are literally the first subdivided
adjacency of the corresponding top path:

\[
                         P_c\subseteq P_D.
\]

This is identification, not a merely collision-free second copy.  The
setwise joint protected bank is `P_D`; its size bound does not acquire an
extra `2m` hinge edges.

After the cyclic rethread, the top path beginning at `L_i` continues with
`R_(i+1),O_(i+1,3),...`.  The first two new owners have union
`K union {a_i,a_(i+1)}`, exactly the first-two-owner union of old path
`i+1`; every later owner is literally inherited from that old path.  Thus
every prefix of length at least two has the old `i+1` prefix union.  The
length-one prefix multiset is the unchanged set of owners `{L_i}`.  All
prefix widths are therefore transported exactly.

Private-path traces are noninterval, whereas ring owners/lower colours
have singleton or adjacent-pair traces.  No private edge is a ring hinge,
so every private witness is untouched.  Together with the damage-cone
localization, this proves the stated all-width **local upper-safety after
planting**.  The same identities were independently enumerated for
`4<=m<=9`.

## 7. Fail-closed global conclusion

Nothing in the path geometry or the `o(W)` count proves that `P_D` extends
to a spanning two-factor.  Such an extension exists exactly when the
weighted Ore inequality holds for **every** lower cut.  Even if it exists,
the theorem does not prove that the `m` ring hinges occupy distinct factor
components, which is required for the cyclic rethread to merge all of
them.  Residence and the common cap are also separate conditions.

Accordingly the audited result is:

- **GO:** exact weighted-boundary identity and exact protected-loss row;
- **GO:** separated cut-thinness rows as sufficient, not necessary;
- **GO:** collision-free common-core witness reservoir and `o(W)` size;
- **GO:** `c=m` literal hinge/top-edge identification and all-prefix
  witness transport;
- **NO-GO:** unconditional factor extension, distinct-component placement,
  or any full compiler conclusion.

## 8. Frozen dependencies

- `MATH_OBSTRUCTION_UPPER_CONE_WITNESS_BANK_PROTECTED_FACTOR_EXTENSION_20260804.md`,
  SHA-256
  `ff5c8eceb334ba7dc848352abd75cc7e701c69e5bc71570bf171c7734ce31ace`;
- `MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md`,
  SHA-256
  `96b9f8717c138dfac7df2a4d1c439392de1a3313c9e57114d2e1cd6f145b90ba`.
