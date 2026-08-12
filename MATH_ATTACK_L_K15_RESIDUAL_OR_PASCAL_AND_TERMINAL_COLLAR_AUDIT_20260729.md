# Residual OR--Pascal completion and the exact terminal-collar audit at `k=15`

Date: 2026-07-29

## 1. Scope and verdict

Let `P` be the certified 6,438-letter exact common compiler prefix underlying
the current length-6,458 word.  Its residual has 21 masks and inclusion width
20.  This note proves three things.

1. Append completion has an exact endpoint-chain/OR--Pascal formulation that
   includes every interval crossing the prefix/suffix seam.  In particular,
   every completion of this unchanged prefix needs at least 20 letters; the
   earlier last-letter seam exclusion is not needed for the lower bound.
2. A same-length compiler surgery followed by 19 letters is characterized by
   its exact gain/loss residual and a 19-column OR--Pascal atlas.  A simple
   sufficient absorber is to preserve all old masks while gaining one of the
   18 residual masks outside the unique union diamond.
3. The user's exhaustive 128-state final-cell audit is valid.  A second
   coordinate-factor audit exhausts every carrier-preserving replacement of
   the final `r` source cells for each `1 <= r <= 6`.  In all
   `361,395,136` tagged state evaluations across these six nested runs the
   residual width remains at least 20.  Thus no same-length replacement
   confined to the final six compiler cells can improve 6,458 to 6,457, even
   with arbitrary cross-boundary witnesses.

The first unresolved terminal collar has seven cells.  A bounded surgery at
nonterminal positions is also not excluded.  No lower bound
`nu(15) >= 6458` is claimed.

## 2. Exact endpoint-chain theorem

For a word `Z`, let

\[
 {\mathcal D}(Z)=\left\{\bigvee_{h=a}^{b}Z_h:1\le a\le b\le |Z|\right\}
\]

be its contiguous-OR deck, and put

\[
 {\mathcal R}(Z)=\bigl(2^{[k]}\setminus\{\varnothing\}\bigr)\setminus{\mathcal D}(Z).
\]

Fix a prefix

\[
 P=(p_1,\ldots,p_n)
\]

and append

\[
 X=(x_1,\ldots,x_q).
\]

Write

\[
 U_{ij}=\bigvee_{h=i}^{j}x_h\quad(1\le i\le j\le q),
 \qquad
 S_a=\bigvee_{h=a}^{n}p_h\quad(1\le a\le n).
\]

### Theorem 2.1 (endpoint atlas)

The masks newly available at appended right endpoint `n+j` are exactly

\[
 \Gamma_j(P,X)=
 \{U_{ij}:1\le i\le j\}
 \ \cup\
 \{S_a\vee U_{1j}:1\le a\le n\}.                 \tag{2.1}
\]

Every `Gamma_j` is an inclusion chain, and

\[
 PX\text{ is universal}
 \quad\Longleftrightarrow\quad
 {\mathcal R}(P)\subseteq\bigcup_{j=1}^{q}\Gamma_j(P,X). \tag{2.2}
\]

Consequently

\[
 \boxed{q\ge \operatorname{width}{\mathcal R}(P)}.       \tag{2.3}
\]

This bound already includes all seam-crossing intervals.

#### Proof

An interval ending at `n+j` either starts at suffix position `n+i`, giving
`U_ij`, or starts at prefix position `a`, giving `S_a OR U_1j`.  These are
all possibilities, proving (2.1).  Moving the left endpoint successively to
the left can only add coordinates, so all values at the fixed right endpoint
form one chain.

A mask missing from `P` can only acquire a witness whose right endpoint is
appended.  This proves (2.2).  Choosing one new witness for each residual
mask partitions the residual among at most `q` endpoint chains.  Dilworth's
theorem gives (2.3).  Notice that the proof never restricts the left
endpoint to the suffix.  ∎

### Theorem 2.2 (OR--Pascal compatibility)

A `q`-letter append exists if and only if there are nonzero diagonal masks
`U_11,...,U_qq` and a triangular table satisfying

\[
 U_{ij}=U_{i,j-1}\vee U_{i+1,j}\qquad(i<j),          \tag{2.4}
\]

such that the columns in (2.1), with `x_j=U_jj`, cover the residual.

#### Proof

Every literal suffix gives (2.4).  Conversely, induction on `j-i` gives

\[
 U_{ij}=\bigvee_{h=i}^{j}U_{hh},
\]

so the diagonal is a literal appended word realizing the whole table.
Theorem 2.1 then gives exactness.  ∎

Thus an arbitrary Dilworth chain cover is only a necessary relaxation.  Its
chains must be simultaneous columns of one OR--Pascal triangle, with the
fixed seam chain attached to each column.  This is the exact shared-letter
chronology condition sought in the task.

## 3. The current residual and the exact fixed-prefix optimum

The canonical serialization of the first 6,438 entries as one
space-separated line followed by a newline has SHA-256

```text
224348c46f92592b722bdd29689567164968415f601c33957d8258681f2bfdea
```

and residual

\[
\begin{aligned}
R=\{&685,960,1103,2420,2575,2676,4469,5801,7267,7504,8250,\\
    &9524,12825,13616,13620,17683,17738,19098,19568,21641,29776\}.
                                                               \tag{3.1}
\end{aligned}
\]

Its rank histogram is

\[
 |R\cap\tbinom{[15]}4|=1,
 \quad |R\cap\tbinom{[15]}5|=1,
 \quad |R\cap\tbinom{[15]}6|=14,
 \quad |R\cap\tbinom{[15]}7|=5.                 \tag{3.2}
\]

Direct comparison of the 21 masks gives exactly two strict containments:

\[
 9524\subset13620,
 \qquad
 13616\subset13620,                               \tag{3.3}
\]

and

\[
 9524\vee13616=13620.                             \tag{3.4}
\]

Therefore

\[
 A=R\setminus\{13620\}                            \tag{3.5}
\]

is the unique maximum antichain and has size 20.  Theorem 2.1 proves that
every append to this fixed prefix has length at least 20, regardless of seam
witnesses.  The stored suffix uses the 18 other masks literally and ends in

```text
9524 13616
```

whose two singleton intervals and two-letter interval realize all three
masks in (3.3)--(3.4).  Hence 20 is exactly optimal for this prefix.

## 4. Exact surgery ledger and a clean 6,457 absorber

Consider any same-length surgery `P -> P'`.  Define its gains and losses by

\[
 G={\mathcal R}(P)\cap{\mathcal D}(P'),
 \qquad
 L={\mathcal D}(P)\setminus{\mathcal D}(P').                \tag{4.1}
\]

### Lemma 4.1 (gain/loss identity)

One has the disjoint identity

\[
 \boxed{{\mathcal R}(P')=({\mathcal R}(P)\setminus G)\ \dot\cup\ L}. \tag{4.2}
\]

In particular, a 19-letter completion requires

\[
 \operatorname{width}\bigl((R\setminus G)\cup L\bigr)\le19, \tag{4.3}
\]

and is equivalent to a 19-column OR--Pascal atlas for that new residual.

#### Proof

Partition the Boolean deck into masks covered and not covered by `P`, and
then compare membership in the deck of `P'`.  A formerly missing mask stays
missing exactly when it is not gained; a formerly covered mask becomes
missing exactly when it is lost.  The two classes are disjoint.  Equation
(4.3) follows from Theorem 2.1, while Theorem 2.2 gives the exact completion
criterion.  ∎

For the exact compiler, let `D` denote adjacent union and let the frozen
middle carrier be `T=D^3P`.  If a surgery has nonzero letters and satisfies

\[
 D^3P'=T,                                           \tag{4.4}
\]

then for every `h>=0`,

\[
 D^{3+h}P'=D^hT.                                   \tag{4.5}
\]

Thus the whole middle deck, residence data, and all upper shadows survive
automatically.  Only the lower-deck ledger (4.2) remains.

Put

\[
 Q=R\setminus\{9524,13616,13620\};\qquad |Q|=18.   \tag{4.6}
\]

### Corollary 4.2 (clean one-mask absorber)

Suppose a same-length nonzero surgery satisfies (4.4), loses no previously
covered mask, and gains one `g in Q`.  Then appending the 17 masks of
`Q\{g}` literally, followed by `9524,13616`, gives a universal word of
length

\[
 6438+19=6457.                                      \tag{4.7}
\]

This is sufficient, not necessary.  More generally, losses are allowed
precisely when (4.3) holds and a 19-column OR--Pascal atlas exists.

There are also seam-assisted sufficient variants.  For example, if the
surgery loses nothing, gains `9524`, and has a suffix OR `S` with

\[
 S\vee13616=13620,
\]

then appending `13616` first realizes both remaining diamond masks, after
which the 18 masks of `Q` may be appended literally.  The symmetric statement
holds with `9524` and `13616` interchanged.  Gaining only `13620` cannot
help: the 20-antichain (3.5) remains.

## 5. Incorporation of the user's final-cell audit

The last four source cells are

\[
 546,\ 1603,\ 2049,\ 7682,                          \tag{5.1}
\]

their union is `7779`, and the first three have union `3683`.  Holding the
first 6,437 cells fixed, a replacement `x` preserves the final `D^3` window
exactly when

\[
 \varnothing\ne x\subseteq7779,
 \qquad 3683\vee x=7779.                            \tag{5.2}
\]

Equivalently, `x` contains the forced bit `4096` and freely chooses the
seven remaining bits of `7779`.  Hence there are exactly `2^7=128` legal
replacements.

The source

```text
scratch/search_k15_tail_cell_replacements.cpp
```

has SHA-256

```text
d79c16a079ac634a62229c3b237fe155070105a73f4972ca41fc3981c46ccec3
```

and correctly does the following: it subtracts every old interval ending at
the last cell, inserts the new terminal suffix-OR chain, recomputes the exact
residual, and computes its inclusion width by strict-inclusion matching.
The exact distribution is

\[
\begin{array}{c|r}
(\operatorname{width},|R_x|)&\#x\\ \hline
(20,21)&1\\
(20,22)&4\\
(21,22)&3\\
(21,23)&120.
\end{array}                                         \tag{5.3}
\]

Only the original `x=7682` attains 21 missing masks.  The user's highlighted
replacement `x=7267` gains `7267` but loses `7682` and `7683`, so

\[
 R_{7267}=(R\setminus\{7267\})\cup\{7682,7683\}.    \tag{5.4}
\]

It has 22 masks and width 20.  Thus it does not reduce the append lower
bound.  This incorporates the supplied exhaustive result; it is not inferred
from a generic shore count.

## 6. Exact terminal-collar theorem through six cells

The preceding one-cell code was independently generalized by

```text
scratch/audit_k15_terminal_collar_width.cpp
```

with SHA-256

```text
39bc5cebf5ffbffe059742fbb22c700a27e95a3177999f11b7a6cd9d0d40dfc1
```

The executable is parameterized at compilation by `TAIL_R=r`.  Its finite
enumeration has a short exact proof.

Fix `r>=1`, put `s=6438-r`, and vary only the cells

\[
 A_s,\ldots,A_{6437}                                  \tag{6.1}
\]

in zero-based indexing.  The affected middle windows are

\[
 W_i=[s-3+i,s+i],\qquad 0\le i<r.                    \tag{6.2}
\]

Let `T_i` be the original OR on `W_i`, and let `F_i` be the OR of the fixed
positions of `W_i` lying before `s`.  For each coordinate `b`, a tail
occurrence pattern

\[
 \epsilon_b\in\{0,1\}^r
\]

is legal exactly when, for every `i`,

\[
 {\mathbf 1}_{b\in T_i}
 ={\mathbf 1}_{b\in F_i}\ \vee\
   \bigvee_{j=\max(0,i-3)}^i\epsilon_b(j).           \tag{6.3}
\]

The equations factor over coordinates.  Their Cartesian product, after
rejecting an empty source cell, enumerates every nonzero solution of
`D^3A'=T` once and only once.

For each candidate, intervals inside the fixed prefix are unchanged.  Every
other interval ends at one of the `r` tail positions and is either an
internal tail OR or

\[
 S_a\vee\bigvee_{j=0}^{i}A'_{s+j},                  \tag{6.4}
\]

where `S_a` is a fixed-prefix suffix OR.  Equations (6.3)--(6.4) therefore
reconstruct the exact residual.  The verifier then uses the strict-inclusion
bipartite graph and Dilworth's matching formula

\[
 \operatorname{width}(M)=|M|-\nu_{\subsetneq}(M)     \tag{6.5}
\]

to compute its width.

### Theorem 6.1 (six-cell terminal-collar no-go)

For every `1<=r<=6` and every nonzero replacement of the final `r` source
cells satisfying `D^3A'=T`,

\[
 \boxed{\operatorname{width}{\mathcal R}(A')\ge20}.      \tag{6.6}
\]

Indeed, the exact census is

\[
\begin{array}{c|r|r|r|r|r|r}
r&\text{legal states}&|{\mathcal R}(A_{<s})|&
\text{distinct residuals}&\min|{\mathcal R}(A')|&
\min\operatorname{width}&
\#\{(|R'|,\operatorname{width})=(21,20)\}\\ \hline
1&128&25&4&21&20&1\\
2&8{,}192&28&9&21&20&8\\
3&147{,}456&31&20&21&20&18\\
4&2{,}257{,}920&34&56&21&20&135\\
5&21{,}798{,}720&36&88&21&20&1{,}440\\
6&337{,}182{,}720&38&88&21&20&21{,}384.
\end{array}                                         \tag{6.7}
\]

The state counts sum to `361,395,136` tagged evaluations.  They are not that
many distinct six-cell words: the six scopes are nested, and an `r<6` state
also appears in the `r=6` fibre after the preceding original cells are
retained.  The union has the `337,182,720` distinct six-cell tails in the
last row.  In every audited scope the residual cardinality stays at least 21
and its width stays at least 20.  By Theorem 2.1, no suffix of length 19 can
complete any of them.  This conclusion includes every possible seam-crossing
witness and is stronger than checking a particular 20-letter suffix order.

The compact certificate is

```text
scratch/k15_terminal_collar_width_r1_r6.certificate.json
```

with SHA-256

```text
8d45bdef5e85ec2d8e6047d9647b95852ef9d6e5181ae06c576523946e06b60d
```

and the six raw stdout/stderr pairs are `scratch/r1.out`, `scratch/r1.err`,
..., `scratch/r6.out`, `scratch/r6.err`.  The `r=1` distribution independently
matches (5.3); `r=2` independently gives

\[
\begin{array}{c|r}
(20,21)&8\\
(20,22)&178\\
(21,22)&240\\
(21,23)&4010\\
(22,23)&64\\
(22,24)&3692,
\end{array}                                         \tag{6.8}
\]

totalling 8,192.

The `r=4,5,6` runs were compiled and executed on the H100 host's CPU.  No
GPU, SAT solver, or exhaustive local-Mac job was used.

## 7. Sharp remaining boundary

The exact length-6,457 gate is now:

1. make a same-length nonzero compiler surgery preserving `D^3A=T`;
2. achieve residual width at most 19; and
3. realize a 19-column OR--Pascal atlas for that residual.

Condition 2 is necessary but not sufficient; Condition 3 is the shared-letter
chronology omitted by a bare chain cover.  Corollary 4.2 is a convenient
strong sufficient condition paying both gates at once.

The terminal fibres `r<=6` fail already at Condition 2.  A subsequent exact
105-envelope certificate closes `r=7` without relying on its large raw state
count; see
`MATH_ATTACK_L_K15_TERMINAL_RADIUS7_ANTICHAIN_CERTIFICATE_20260729.md`.
A second 124-envelope certificate closes `r=8`; see
`MATH_ATTACK_L_K15_TERMINAL_RADIUS8_ANTICHAIN_CERTIFICATE_20260729.md`.
Thus the first untested terminal fibre is now `r=9`.  A nonterminal bounded
edit can have two separated collars and is not represented by these terminal
censuses.  Nor do they cover insertion/deletion or moving the prefix/suffix
boundary.

Therefore the rigorous boundary is:

\[
\boxed{
\begin{array}{l}
\text{unchanged prefix: suffix optimum exactly }20;\\
\text{last }r\le8\text{ source cells replaced: still at least }20;\\
\text{nine-cell or separated bounded absorber: open.}
\end{array}}
\]

No claim about the global optimum beyond

\[
 6438\le\nu(15)\le6458
\]

follows from this local audit.
