# J6 plus the native two-colour append: exact predecessor extension and the one-bit residence obstruction

Date: 2026-08-01  
Lane: A / compatible rooted state around the protected J6 boundary macro  
Status: **positive owner/`q1`/root-matching/graphic theorem; exact literal residence obstruction**

## 0. Verdict

Append the two owners `26750,27246` to the terminal owner `30782` of the
safe-open J6 path.  The resulting thirteen-owner sequence is

```text
30781 28797 20733 4605 511 959 1855
3647 7742 15422 30782 26750 27246.                 (0.1)
```

At the owner layer this is better than the generic small-matching theorem
can certify:

1. (0.1) is a simple rank-nine Johnson path;
2. all twelve lower and all twelve upper `q1` colours are distinct;
3. its twelve predecessor incidences extend to an explicit perfect
   matching of `ML_9`; and
4. relative to that matching, the twelve successor incidences contract to
   one directed rooted path.

Thus the prospective predecessor/graphic part of the compatible-rooted-state
gate is genuinely nonempty for this fused owner path.  The generic theorem
for a protected matching of size at most `m-1=8` does **not** apply here;
the extension at size twelve is a separate exact fact.

However, (0.1) is not a valid depth-three resident continuation of J6.
Coordinate `12` has trace

```text
1111000011100,
```

so owners `7742,15422,30782` form an internal positive run of length three.
Equivalently, the first appended owner `26750` omits the J6 terminal socket
coordinate `p=12`.  This violates the exact J6 outgoing condition before
any global Catalan connector is selected.  No later exterior continuation
can repair an already internal `0-111-0` pattern.

Consequently this append proves a positive **owner-layer rooted phase**, but
it does not itself belong to the fully protected state family used in the
ordered-Hall minimum.  The minimal explicit obstruction is the single
socket literal

\[
                         12\in Y_1,                   \tag{0.2}
\]

which fails for `Y_1=26750`.

## 1. Exact double-rainbow ledger

Let the owners in (0.1) be `V_0,...,V_12`, and put

\[
 L_i=V_i\cap V_{i+1},\qquad
 R_i=V_i\cup V_{i+1}\quad(0\le i<12).                \tag{1.1}
\]

Direct Boolean arithmetic gives

```text
lower L_i:
28733 20605 4349 509 447 831
1599 3646 7230 14398 26686 26734

upper R_i:
30845 28925 20989 4607 1023 1983
3903 7743 15934 31806 30846 27262.
```

Every `V_i` has rank nine, every `L_i` rank eight, every `R_i` rank ten,
and

\[
                         |V_i\triangle V_{i+1}|=2.    \tag{1.2}
\]

The three displayed lists have sizes `13,12,12`, respectively.  Hence
(0.1) is simple and both palettes are injective.

There is a small but important distinction from the isolated H2 column

```text
30844 -> 26750 -> 27246.
```

Replacing its first owner by the actual J6 terminal preserves its two upper
colours `30846,27262`, while its first lower colour changes from `26748` to
`26686`.  The latter is still new relative to the ten J6 lower colours.
Thus the literal two-colour fusion survives at owner/upper level, but its
isolated clipped-residence proof does not transport automatically.

## 2. The twelve-edge predecessor matching

Work in the regular bipartite inclusion graph

\[
 ML_9=\left({[17]\choose8},{[17]\choose9};\subset\right),
 \qquad W={17\choose8}=24310.                         \tag{2.1}
\]

Define the alternating shores of the owner path by

\[
 P_0=\{L_iV_i:0\le i<12\},\qquad
 P_1=\{L_iV_{i+1}:0\le i<12\}.                       \tag{2.2}
\]

Distinctness in Section 1 shows that both are matchings.

### Theorem 2.1 (exact `ML_9` predecessor extension)

There exists a perfect incidence matching `M_0` of `ML_9` such that

\[
                              P_0\subseteq M_0.        \tag{2.3}
\]

Equivalently, after deleting the twelve lower vertices `L_i` and the
twelve middle vertices `V_i` for `0<=i<12`, the residual inclusion graph
has a perfect matching of size `24298`.

#### Proof

Start from the standard Greene--Kleitman central perfect matching.  Force
the incidences in (2.2) in increasing path order, protecting the ones
already forced.  Three desired incidences (indices `2,3,6`) are already
present.  The other nine are installed by alternating exchanges whose
augmenting-path lengths are

```text
index:   0  1  4  5   7  8  9 10 11
length: 10  2  4  2  10  7  7  7  5.
```

Every exchange avoids all previously fixed lower and middle endpoints.
The resulting explicit matching has `24310` distinct rank-eight tails and
`24310` distinct rank-nine heads, every pair is an inclusion edge, and all
twelve pairs in `P_0` occur.

The full certificate is

```text
scratch/threadA_j6_j7_predecessor_extension_20260801.matching.tsv
SHA-256 67a9ab6a38187647bffd9a34e238115e4771a41a123dc60c3c1090f5e6f10f4e.
```

The independent verifier does not rerun the exchange algorithm.  It checks
all `24310` certificate rows directly, including both shore partitions,
literal containment, injectivity, surjectivity and (2.3):

```text
scratch/audit_threadA_j6_j7_predecessor_extension_20260801.py
SHA-256 741ba8e0e648737467d7cfc6625030b341a1ba0c02f08815373f67919fd2fde0

scratch/threadA_j6_j7_predecessor_extension_20260801.audit.json
SHA-256 7432ebe2d06a002b694268a452d420f0d30b632da733ff2aca4c349af3859582.
```

This is also a constructive Hall certificate.  Put

\[
 G'=ML_9\left[{[17]\choose8}\setminus\{L_i\},
               {[17]\choose9}\setminus\{V_i:0\le i<12\}\right].
\]

For any residual lower family `A`, the `M_0`-images of its members are
distinct residual middle neighbours.  Therefore

\[
                       |N_{G'}(A)|\ge |M_0(A)|=|A|,   \tag{2.4}
\]

which is exactly every residual Hall inequality.  Hence the residual graph
has a perfect matching and (2.3) follows.  \(\square\)

### Why the coarse shadow lemma is insufficient

For an arbitrary prescribed matching of size `t`, the standard central
shadow argument proves extension only for `t<=m-1`.  Here `t=12>8`, so its
uniform surplus can be smaller than the number of deleted middle vertices.
Theorem 2.1 uses the actual incidence geometry of (0.1), not an invalid
application of that coarse bound.

## 3. Rooted graphic consequence

Let `M_0` be the certified matching.  The verifier finds

\[
                         M_0^{-1}(V_{12})=27182.       \tag{3.1}
\]

For `0<=i<11`, (2.3) gives

\[
                         M_0^{-1}(V_{i+1})=L_{i+1}.   \tag{3.2}
\]

Therefore the rooted links of the successor shore are exactly

\[
 L_0\to L_1\to\cdots\to L_{11}\to27182.             \tag{3.3}
\]

All thirteen roots in (3.3) are distinct.  Thus `P_1` is tail-simple,
head-simple and graphic-independent; indeed it is one directed path.  Its
upper labels are precisely the twelve distinct sets `R_i` in Section 1.

This proves the predecessor-matching and protected-path part of a rooted
state without choosing an upper-exact Catalan forest on the remaining
colours.  It neither proves `Sigma(P)` nonempty under all source guards nor
proves the ordered Hall number `Delta(P)=1`.

## 4. Exact residence audit

The original eleven-owner J6 opening has no wholly internal positive run
shorter than four.  At its terminal end coordinate `12` occurs on exactly

```text
7742 15422 30782,
```

so it is the length-three clipped `p`-fragment in the exact J6 endpoint
record.  The first added owner satisfies

\[
                         12\notin26750.                \tag{4.1}
\]

Consequently the append changes that clipped fragment into the internal
trace

```text
0 | 111 | 0,
```

at owner positions `7..11`, with the positive block occupying positions
`8,9,10`.  This is the unique internal positive run of length below four
in the thirteen-owner concatenation.  The maximal depth-three source is

```text
30781 28733 20541 4157 125 189 317 63
574 1086 2110 2110 10286 26670 26734 27246,
```

so the failure is literal and not an artefact of an abstract palette
projection.

The repaired first-bridge singleton from the protected comparator theorem
changes a source letter while leaving its owner row, pre-row, palettes and
owner traces unchanged.  Therefore that repair is compatible with the
owner-layer matching calculation above wherever the comparator is used,
but no owner-trace-invariant source enrichment can repair (4.1).

### Corollary 4.1 (minimal continuation obstruction)

Any resident continuation of the displayed orientation of J6 must have its
first succeeding owner `Y_1` contain coordinate `12`.  In particular the
two-owner append `26750,27246` is impossible in a protected resident state,
independently of every later Catalan-forest, port-order or common-cap choice.

#### Proof

The clipped terminal `p`-run has current length three and depth-three
residence requires length at least four.  Thus `p=12` must persist through
the first successor.  If it does not, the two adjacent zeroes make the run
internal, after which no exterior owner can lengthen it.  Equation (4.1)
finishes the proof.  \(\square\)

## 5. Audited scope

The exact conclusions are:

* the H2 native fusion breaks the frozen two-colour logical core at the
  owner/upper level even when attached directly to the J6 terminal;
* its direct attachment has new lower colours `26686,26734`;
* the complete twelve-edge predecessor phase extends to a perfect `ML_9`
  matching;
* the successor shore is one protected rooted path; but
* the direct attachment is excluded from the fully protected boundary
  family by one explicit residence socket literal.

Thus the compatible-rooted-state gate does **not** fail at predecessor
Hall or graphic rank for this candidate.  It fails earlier, at the literal
boundary-state row (0.2).  A genuine J7 repair must change the first
succeeding owner or insert a different resident bridge while preserving the
two new upper colours and lower-palette injectivity; merely completing the
root matching cannot help.

Builder and compact exchange ledger:

```text
scratch/threadA_j6_j7_predecessor_extension_20260801.cpp
SHA-256 69444defc6f4c2ed7dd29c7d8375399fc29000ca0ff0d155fe17338bef38293c

scratch/threadA_j6_j7_predecessor_extension_20260801.audit.txt
SHA-256 f3921d0812f35264a47f19761b8f61039083c0747b6deceaf05e541b76d087dd.
```

The builder and verifier were run on the H100 CPU under explicit memory and
CPU limits.  No local exhaustive search was used.
