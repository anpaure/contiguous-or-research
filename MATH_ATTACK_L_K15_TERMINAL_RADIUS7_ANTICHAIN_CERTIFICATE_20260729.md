# Exact radius-seven terminal-collar theorem for the verified `k=15` compiler

Date: 2026-07-29

## 1. Verdict and scope

Let `P` be the verified 6,438-letter exact common compiler prefix underlying
the current length-6,458 word.  Replace, at the same seven positions, any or
all of its final seven nonzero source letters, subject only to preserving the
exact middle carrier

\[
 D^3P'=D^3P.                                           \tag{1.1}
\]

Then the residual inclusion width always satisfies

\[
 \boxed{\operatorname{width}\mathcal R(P')\ge20}.     \tag{1.2}
\]

The original tail belongs to this fibre and has width 20, so the minimum is
exactly 20.  By the endpoint-chain theorem, every completion suffix therefore
has length at least 20, including suffixes using arbitrary intervals crossing
the fixed-prefix boundary.  Consequently no radius-seven terminal-collar
replacement produces a length-6,457 word.

The decisive certificate is not the exhaustive traversal of 2.508 billion
tails.  It is a 105-envelope calculation followed by an explicit antichain
exchange.  A complete H100-CPU enumeration independently confirms the result.

This theorem concerns same-length replacements of the final seven source
cells.  It does not cover eight cells, insertion/deletion, moving the append
boundary, or separated nonterminal collars.  It proves no global lower bound
`nu(15)>=6458`.

## 2. Fixed residual and the necessary gain

The prefix residual is

\[
\begin{aligned}
R=\{&685,960,1103,2420,2575,2676,4469,5801,7267,7504,8250,\\
    &9524,12825,13616,13620,17683,17738,19098,19568,21641,29776\}.
                                                               \tag{2.1}
\end{aligned}
\]

Its only strict containments are

\[
 9524\subset13620,
 \qquad 13616\subset13620.                           \tag{2.2}
\]

Thus

\[
 A=R\setminus\{13620\}                               \tag{2.3}
\]

is a 20-antichain.  If a tail replacement gains no member of `A`, all 20
members remain missing; any newly lost masks can only enlarge the residual.
Therefore

\[
 \operatorname{width}\mathcal R(P')\le19
 \quad\Longrightarrow\quad
 \text{some member of }A\text{ is gained}.            \tag{2.4}
\]

This elementary implication is the entire pruning principle.

## 3. Exact coordinate-pattern fibre

Write

\[
 P=B X,
 \qquad |B|=6431,
 \qquad X=(x_0,\ldots,x_6).                           \tag{3.1}
\]

For `0<=i<=6`, let `W_i` be the affected four-cell window ending at tail
position `i`, let `T_i` be its original OR, and let `F_i` be the OR of its
fixed cells in `B`.  For coordinate `b`, write

\[
 \epsilon_b(j)={\mathbf 1}_{b\in x_j}.
\]

The carrier equation (1.1) is equivalent, coordinate by coordinate, to

\[
 {\mathbf 1}_{b\in T_i}
 = {\mathbf 1}_{b\in F_i}\ \vee\
   \bigvee_{j=\max(0,i-3)}^i\epsilon_b(j)
 \qquad(0\le i\le6).                                  \tag{3.2}
\]

Let `Pi_b` be the allowed set of seven-bit occurrence patterns satisfying
(3.2).  Their exact cardinalities for bits `0,...,14` are

\[
 (108,8,1,1,4,15,4,1,1,108,56,2,1,1,1).             \tag{3.3}
\]

The Cartesian product has

\[
 \prod_{b=0}^{14}|\Pi_b|=2{,}508{,}226{,}560          \tag{3.4}
\]

states.  The coordinatewise forced masks at the seven positions are

\[
 (1028,16384,48,2,64,2048,4096),                     \tag{3.5}
\]

so every Cartesian-product state is automatically nonzero.  Hence (3.2)
enumerates every legal radius-seven tail once and only once, with no hidden
cross-coordinate constraint.

The unchanged head `B` misses exactly the following 42 masks:

\[
\begin{aligned}
M_B=\{&685,960,1103,1635,1651,1813,1821,2420,2575,2676,3651,3683,3699,\\
&4469,5801,7267,7504,7682,7683,7779,7795,8250,9524,10013,10015,12825,\\
&13616,13620,17683,17738,17971,17973,17975,18035,18197,18205,18229,\\
&18231,19098,19568,21641,29776\}.                      \tag{3.6}
\end{aligned}
\]

Its 11 distinct suffix-OR states, from shortest to longest, are

\[
 789,797,8989,8991,9023,13119,13247,15295,16319,32703,32767. \tag{3.7}
\]

These two short lists determine every internal-tail and seam-crossing witness.

## 4. The 105-envelope certificate

There are 28 internal tail intervals `[l,r]`, with `0<=l<=r<=6`, and
`7*11=77` seam types, one for each tail endpoint and fixed suffix state in
(3.7).  Call this set of 105 slots `J`.

For a slot `I` and coordinate `b`, inspect the patterns in `Pi_b`.  Put bit
`b` in `L_I` if every allowed pattern makes the slot contain `b`, and put it
in `U_I` if at least one allowed pattern does.  Coordinate independence and
(3.5) give the exact equivalence

\[
 g\text{ is realizable at slot }I
 \quad\Longleftrightarrow\quad
 L_I\subseteq g\subseteq U_I.                        \tag{4.1}
\]

Indeed, necessity is immediate.  For sufficiency, choose independently for
each coordinate a pattern giving its prescribed slot bit; every resulting
source cell remains nonzero by (3.5), and (3.2) remains satisfied.

The complete `105*20` comparison against the old antichain has only three
hits:

\[
\begin{array}{c|c|c|c|r}
g&I&L_I&U_I&\#\text{ legal tails realizing }g\text{ at }I\\ \hline
7267&[6,6]&4096&7779&21{,}618{,}688\\
7267&[5,6]&6144&7779&148{,}642{,}560\\
7267&[4,6]&6208&7779&130{,}457{,}600.
\end{array}                                           \tag{4.2}
\]

There is no seam hit and no hit for any other member of `A`.  Thus (2.4)
sharpens to

\[
 \operatorname{width}\mathcal R(P')\le19
 \quad\Longrightarrow\quad
 x_j\vee\cdots\vee x_6=7267
 \text{ for some }j\in\{4,5,6\}.                    \tag{4.3}
\]

The envelope certificate requires only `15*128` coordinate-pattern checks
and `105*20` containment checks.  It is therefore a reusable proof object,
not a heuristic reduction of the large fibre.

## 5. Every gain of `7267` forces the loss of `7682`

The fixed head `B` misses `7682`, and its final letter is

\[
 B_{6430}=789.                                        \tag{5.1}
\]

Since `789` contains bit 0 whereas `7682` does not, no seam-crossing interval
can equal `7682`.

The unique allowed occurrence pattern for bit 12, whose mask value is 4096,
is

\[
 \Pi_{12}=\{2^6\}.                                    \tag{5.2}
\]

Therefore an internal-tail witness of `7682` must end at tail position 6.
Assume (4.3) and fix `j` with

\[
 x_j\vee\cdots\vee x_6=7267.                         \tag{5.3}
\]

An interval `[s,6]` with `s>=j` is contained in `7267`; it lacks bit 9,
which `7682` requires.  If `s<j`, the interval contains all of `7267`, hence
contains bit 0, which `7682` forbids.  Thus no internal-tail witness remains.
Together with (5.1),

\[
 7267\text{ gained}\quad\Longrightarrow\quad7682\text{ lost}. \tag{5.4}
\]

Finally, the family

\[
 A'=(A\setminus\{7267\})\cup\{7682\}                 \tag{5.5}
\]

is the explicit 20-antichain

\[
\begin{aligned}
\{&685,960,1103,2420,2575,2676,4469,5801,7504,7682,8250,9524,\\
&12825,13616,17683,17738,19098,19568,21641,29776\}.   \tag{5.6}
\end{aligned}
\]

Hence a tail that gains no `7267` retains `A`, while a tail that gains it
contains `A'` in its residual.  In both cases the residual width is at least
20.  This proves (1.2).

The original tail is legal and has residual width 20 by (2.1)--(2.2), so
the fibre minimum is exactly 20.

## 6. Independent full-fibre census

For independent corroboration, the earlier direct verifier was compiled with
`TAIL_R=7` and run on the H100 host's CPU.  It evaluated all
`2,508,226,560` states, found 171 distinct residual families, and returned

\[
 \min\operatorname{width}=20,
 \qquad
 \min\{|R'|:\operatorname{width}(R')=20\}=21.         \tag{6.1}
\]

The width-20 rows are

\[
\begin{array}{c|r}
|R'|&\#\text{ states}\\ \hline
21&142{,}560\\
22&2{,}753{,}240.
\end{array}                                           \tag{6.2}
\]

Every other state has width between 21 and 25.  The complete 20-row
`(width,residual size)` histogram sums exactly to the raw state count and is
stored in the manifest.  Runtime was 467.91 CPU seconds.  No GPU or local-Mac
exhaustive job was used.

The full enumeration is logically unnecessary for the theorem: Sections
2--5 already prove the no-go.  It is retained as an independent audit of the
carrier-pattern and residual-deck implementations.

## 7. Literal-compiler consequence and remaining boundary

For any fixed prefix, all new witnesses supplied by a `q`-letter append end
at one of its `q` appended positions; values sharing a right endpoint form an
inclusion chain.  Therefore

\[
 q\ge\operatorname{width}\mathcal R(P').             \tag{7.1}
\]

Combining (1.2) and (7.1), a 19-letter literal suffix is impossible throughout
the radius-seven fibre.  There is consequently no candidate 6,457 word to
verify in this class.  The exact `D^3` equations were preserved in (3.2), so
the middle carrier, residence chronology, and every upper row remain fixed;
the obstruction is entirely in the literal lower deck.

Radius eight is subsequently closed by the same suffix-exchange mechanism in
`MATH_ATTACK_L_K15_TERMINAL_RADIUS8_ANTICHAIN_CERTIFICATE_20260729.md`.
The first unclosed terminal radius is now nine.  A separated multi-cell collar
is a different move class because affected intervals need not all end after
one fixed split.

## 8. Artifacts and hashes

The compact mathematical verifier and its output are

```text
scratch/audit_k15_terminal_r7_antichain_certificate.cpp
scratch/k15_terminal_r7_antichain_certificate.json
```

with SHA-256 values

```text
a7b425c28c23e92a6177aa5130f9591a64477e0e687f21debec1006508d59bdc
633266d75e6077be49caf1d5c28076c14e04ef1e5af56fc8d7625d1b4d4b7571
```

The full-fibre source and logs are

```text
scratch/audit_k15_terminal_collar_width.cpp
scratch/k15_terminal_collar_r7.stdout.txt
scratch/k15_terminal_collar_r7.stderr.txt
```

with SHA-256 values

```text
39bc5cebf5ffbffe059742fbb22c700a27e95a3177999f11b7a6cd9d0d40dfc1
b0f2dc1b8850661f5f1c7a5d5c2dca70feabc1b76c1fb161acb6de513ec1c636
ba04fb65d8d2ff9c2076c47f99c505201b27f09cdd1ba36ea78ffe555f9411ad
```

The hash-bound manifest is

```text
scratch/k15_terminal_r7_audit_manifest.json
```

with SHA-256

```text
d53b4035a2fd15e142f37887a457862953951b990904c6ad3fc206dfe9a7d024
```

It binds both audits to the verified length-6,458 word

```text
scratch/k15_h19_exact_compiler_union_suffix_6458.word
c4300f7d6ec4f618ead87bb15ca3b831803f0c3296e3c5274f4ecd91fb029598
```

and to the canonical first-6,438-entry serialization hash

```text
224348c46f92592b722bdd29689567164968415f601c33957d8258681f2bfdea.
```
