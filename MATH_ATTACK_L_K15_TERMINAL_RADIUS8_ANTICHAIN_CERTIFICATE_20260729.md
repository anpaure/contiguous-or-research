# Exact radius-eight terminal-collar theorem for the verified `k=15` compiler

Date: 2026-07-29

## 1. Theorem and scope

Let `P` be the verified 6,438-letter exact common compiler prefix.  Replace
its final eight source letters at the same positions, require every new letter
to be nonzero, and preserve the exact middle carrier:

\[
 D^3P'=D^3P.                                           \tag{1.1}
\]

Then

\[
 \boxed{\operatorname{width}\mathcal R(P')\ge20}.     \tag{1.2}
\]

The original tail belongs to the fibre and has residual width 20, so the
minimum is exactly 20.  Hence every literal completion needs at least 20
appended letters, including completions using prefix/suffix-crossing
intervals.  No radius-eight terminal replacement yields a length-6,457 word.

The result is proved by a 124-slot envelope certificate.  The raw fibre has
18,606,981,120 states, but a full traversal is logically unnecessary and was
not run.  Radius nine, insertion/deletion, a shifted append boundary, and
separated multi-cell collars remain outside the theorem.  No global lower
bound `nu(15)>=6458` is claimed.

## 2. Exact radius-eight carrier fibre

Write

\[
 P=B(x_0,\ldots,x_7),
 \qquad |B|=6430.                                    \tag{2.1}
\]

The original tail is

\[
 (789,1557,17425,48,546,1603,2049,7682).             \tag{2.2}
\]

The eight affected four-window ORs and their fixed-head contributions are

\[
\begin{aligned}
T&=(8991,10013,18205,18229,17975,18035,3699,7779),\\
F&=(8975,8973,781,0,0,0,0,0).                        \tag{2.3}
\end{aligned}
\]

For coordinate `b`, let `epsilon_b(j)` record its occurrence at tail position
`j`.  Equation (1.1) is equivalent to the eight coordinate equations

\[
 {\mathbf 1}_{b\in T_i}
 = {\mathbf 1}_{b\in F_i}\ \vee\
   \bigvee_{j=\max(0,i-3)}^i\epsilon_b(j)
 \qquad(0\le i\le7).                                  \tag{2.4}
\]

The allowed eight-bit pattern counts for coordinates `0,...,14` are

\[
 (208,8,2,1,4,15,4,1,1,208,56,2,1,1,1),             \tag{2.5}
\]

whose product is

\[
 18{,}606{,}981{,}120.                                \tag{2.6}
\]

Their coordinatewise forced cell masks are

\[
 (272,1028,16384,48,2,64,2048,4096).                 \tag{2.7}
\]

All eight are nonzero, so the Cartesian product of the coordinate patterns
is exactly the nonzero `D^3` fibre; there is no additional cross-coordinate
condition.

The fixed head `B` misses the following 47 masks:

\[
\begin{aligned}
M_B=\{&685,797,960,1103,1635,1651,1813,1821,2420,2575,2676,3651,3683,\\
&3699,4469,5801,7267,7504,7682,7683,7779,7795,8250,8989,8991,9023,\\
&9524,10013,10015,12825,13119,13616,13620,17683,17738,17971,17973,\\
&17975,18035,18197,18205,18229,18231,19098,19568,21641,29776\}.   \tag{2.8}
\end{aligned}
\]

Its distinct suffix-OR states are

\[
 781,8973,8975,9007,13103,13231,15279,15295,16319,32703,32767. \tag{2.9}
\]

These lists determine every changed literal interval.

## 3. The 124-slot envelope relation

Let

\[
 A=\mathcal R(P)\setminus\{13620\}.                  \tag{3.1}
\]

As in the radius-seven theorem, `A` is the explicit old 20-antichain.  Any
residual of width at most 19 must gain some member of `A`.

There are 36 internal intervals `[l,r]` in the eight-cell tail and `8*11=88`
seam types obtained by adjoining a fixed suffix state from (2.9).  For each
of these 124 slots `I`, define `L_I` and `U_I` coordinatewise: a bit belongs
to `L_I` if every legal coordinate pattern places it in the slot, and belongs
to `U_I` if at least one pattern does.  Since the coordinates are independent
and (2.7) enforces nonempty cells,

\[
 g\text{ occurs at }I
 \quad\Longleftrightarrow\quad
 L_I\subseteq g\subseteq U_I.                        \tag{3.2}
\]

The complete `124*20` comparison has exactly three hits:

\[
\begin{array}{c|c|c|c|r}
g&I&L_I&U_I&\#\text{ legal tails realizing }g\text{ at }I\\ \hline
7267&[7,7]&4096&7779&160{,}358{,}400\\
7267&[6,7]&6144&7779&1{,}097{,}293{,}824\\
7267&[5,7]&6208&7779&944{,}186{,}880.
\end{array}                                           \tag{3.3}
\]

There is no seam hit and no hit for another member of `A`.  Therefore a
putative width-19 state must satisfy

\[
 x_j\vee\cdots\vee x_7=7267
 \quad\text{for some }j\in\{5,6,7\}.                 \tag{3.4}
\]

This envelope computation checks only `15*256` coordinate patterns and
`124*20` containments, rather than traversing (2.6).

## 4. The forced `7267/7682` exchange

### Lemma 4.1 (terminal suffix-exchange lemma)

Let `P=BX`, where `X` is a terminal tail whose exact carrier fibre factors
over coordinates and has a nonzero forced mask at every cell.  Let
`A subseteq R(P)` be a `w`-antichain.  Suppose:

1. the complete internal/seam envelope relation shows that the only member
   of `A` which any legal tail can gain is `g`, and every `g` witness is a
   terminal suffix OR `x_j OR ... OR x_(r-1)=g`;
2. `h` is missing from `B`, while every nonempty suffix OR of `B` contains
   a coordinate `alpha` absent from `h`;
3. some coordinate `gamma in h` has the unique legal tail occurrence
   `r-1`;
4. `alpha in g\h` and there is `beta in h\g`; and
5. `(A\{g}) union {h}` is a `w`-antichain.

Then every legal replacement tail has residual width at least `w`.

#### Proof

If `g` is not gained, the old antichain `A` remains.  Otherwise fix a suffix
`[j,r-1]` whose OR is `g`.  A witness for `h` cannot lie in `B` by Hypothesis
2, and cannot cross the seam because it would contain `alpha`.  By Hypothesis
3, an internal-tail witness must end at `r-1`.  If it starts at or after `j`,
its OR is contained in `g` and misses `beta`; if it starts before `j`, it
contains `g` and hence the forbidden coordinate `alpha`.  Thus `h` is lost,
and Hypothesis 5 supplies the replacement `w`-antichain.  ∎

Radius eight instantiates the lemma with

\[
 w=20,\quad g=7267,\quad h=7682,\quad
 \alpha=\text{bit }0,\quad\beta=\text{bit }9,\quad
 \gamma=\text{bit }12.                               \tag{4.1}
\]

The fixed head already misses `7682`, and its last letter is

\[
 B_{6429}=781.                                        \tag{4.2}
\]

Since `781` contains bit 0 and `7682` does not, every seam-crossing interval
is excluded as a `7682` witness.

Bit 12, of mask value 4096, has the unique legal tail pattern

\[
 \{2^7\};                                             \tag{4.3}
\]

thus an internal-tail `7682` witness must end at position 7.  Assume (3.4).
If an interval `[s,7]` starts at or after `j`, its OR is contained in `7267`
and lacks bit 9, which `7682` requires.  If `s<j`, its OR contains all of
`7267`, including bit 0, which `7682` forbids.  Hence

\[
 7267\text{ gained}\quad\Longrightarrow\quad7682\text{ lost}. \tag{4.4}
\]

The family

\[
\begin{aligned}
A'=(A\setminus\{7267\})\cup\{7682\}
=\{&685,960,1103,2420,2575,2676,4469,5801,7504,7682,8250,9524,\\
&12825,13616,17683,17738,19098,19568,21641,29776\}
                                                               \tag{4.5}
\end{aligned}
\]

is an explicit 20-antichain.  A state not gaining `7267` retains `A`; a state
gaining it has `A'` in its residual.  This proves the lower bound (1.2).
For the original tail, `A` gives width at least 20, while the containment
`9524 subset 13620` pairs two of the 21 residual masks into one chain and
gives a 20-chain cover.  Hence the original width is 20, proving equality.

## 5. Literal consequence and computation boundary

At each appended right endpoint, all contiguous OR values form one inclusion
chain.  Thus a `q`-letter completion of a fixed prefix requires

\[
 q\ge\operatorname{width}\mathcal R(P').             \tag{5.1}
\]

Equations (1.2) and (5.1) rule out a 19-letter suffix throughout the entire
radius-eight fibre.  No width-19 state exists, so there is no prospective
6,457 word requiring a further literal verifier.

A direct enumeration using the earlier full-fibre source would inspect all
18,606,981,120 states.  It was not run: the much smaller certificate in
Sections 2--4 is already necessary-and-sufficient at every envelope step and
proves the universal no-go.  All certificate generation and compilation were
performed on the H100 host's CPU; no GPU or exhaustive local-Mac job was used.

The first unclosed terminal radius is now nine.  The natural alternative is
an exact composition theorem for two separated small collars, where intervals
crossing both collars must be accounted for explicitly.

## 6. Exact composition of two separated small collars

The fallback move class also admits an exact reduction.

### Theorem 6.1 (two-collar deck composition)

Let `w` be a fixed word, and replace the two collars

\[
 I=[a,b],\qquad J=[c,d],\qquad c-b\ge4,              \tag{6.1}
\]

of lengths at most four.  Let `Sigma_I,Sigma_J` be their nonzero local
replacement fibres preserving every affected `D^3` window.  Then:

1. the global carrier fibre is exactly `Sigma_I times Sigma_J`;
2. if `B` is the fixed deck of intervals avoiding both collars,
   `E_I(x),E_J(y)` are the decks of intervals meeting only the indicated
   collar, and

   \[
   H=\bigvee_{t=b+1}^{c-1}w_t,                       \tag{6.2}
   \]

   then the intervals meeting both collars have deck

   \[
   X_{IJ}(x,y)=
   \{u\vee H\vee v:u\in S_I(x),\ v\in P_J(y)\},     \tag{6.3}
   \]

   where `S_I(x)` comprises ORs of segments ending at `b` and crossing `I`,
   and `P_J(y)` comprises ORs of segments starting at `c` and crossing `J`;
3. consequently

   \[
   \mathcal D(w^{x,y})
   =B\cup E_I(x)\cup E_J(y)\cup X_{IJ}(x,y).         \tag{6.4}
   \]

If `H=FULL`, all cross intervals equal `FULL`.  Put

\[
 B^*=B\cup\{FULL\},
 \qquad
 Z=\bigl(2^{[k]}\setminus\{\varnothing\}\bigr)\setminus B^*,
 \quad C_I(x)=E_I(x)\cap Z,
 \quad C_J(y)=E_J(y)\cap Z.                         \tag{6.5}
\]

Then the residual is exactly

\[
 \boxed{\mathcal R(w^{x,y})
 =Z\setminus\bigl(C_I(x)\cup C_J(y)\bigr).}         \tag{6.6}
\]

#### Proof

A four-cell window cannot meet both collars under (6.1), so its constraints
belong wholly to one local fibre; this proves the Cartesian factorization.
Every interval belongs to exactly one of the four classes: avoids both,
meets only `I`, meets only `J`, or meets both.  An interval meeting both
contains the whole fixed gap and factors uniquely into a segment ending at
`b`, the gap, and a segment starting at `c`, proving (6.3)--(6.4).  If the
gap OR is full, (6.3) contributes only `FULL`; absorbing it into `B^*` and
taking complements inside the remaining universe `Z` gives (6.6).  ∎

For a collar of length `r<=4`, each coordinate has at most `2^r<=16` local
patterns.  Its one-collar deck signature is determined by at most

\[
 \frac{r(r+1)}2+2r(k+1)+(k+1)^2\le394              \tag{6.7}
\]

interval types at `k=15`.  Thus a reusable certificate independently
enumerates and deduplicates the local signatures

\[
 \mathscr C_I=\{C_I(x):x\in\Sigma_I\},
 \qquad
 \mathscr C_J=\{C_J(y):y\in\Sigma_J\},              \tag{6.8}
\]

then checks the exact residuals (6.6) over signature pairs rather than raw
word pairs.  Gain/loss lists cannot merely be added: coverage of one lost
mask may be recycled by the other collar, which is why signature union is
the correct operation.

There is also a rigorous one-sided portal rejection screen for the verified
6,438-letter prefix.  Pair a separated nonterminal collar `I` with its final
eight-cell collar `J`, put `I` before `J`, and assume the fixed gap OR is
`FULL`.  Let `B` be the deck of intervals avoiding both collars and assume
(as holds for this verified prefix)

\[
 B\cap\bigl(A\cup\{7682\}\bigr)=\varnothing.       \tag{6.9}
\]

Intervals meeting only `J` start strictly after `I`, so their local seam data
are unchanged by the `I`-replacement.  The terminal calculation of Sections
3--4 therefore gives the following stronger dichotomy, not merely its width
conclusion: the only member of `A` that an interval meeting only `J` can gain
is `7267`, and gaining `7267` forces `7682` to remain missing.  Intervals
meeting both collars are `FULL`.  It follows that a width-at-most-19 pair must
make the nonterminal collar realize some mask in

\[
 \mathcal P=A\cup\{7682\}.                          \tag{6.10}
\]

Otherwise, if the terminal collar does not gain `7267`, the old antichain
`A` survives; if it gains `7267`, the exchange antichain
`(A\{7267}) union {7682}` survives.  Cross intervals are full and cannot
realize a portal.

For each of the at most 394 local interval types and each of the 21 portal
masks, the coordinate envelopes `L subseteq g subseteq U` are necessary for
literal realization.  Consequently, absence of all `394*21` envelope hits
rigorously rejects that fixed nonterminal collar before any signature-pair
enumeration.  A hit is not by itself sufficient in a general nonzero fibre:
cell nonemptiness couples otherwise coordinatewise pattern choices.  It
becomes sufficient only when every collar cell has a forced nonzero
coordinate (or when exact joint nonzero feasibility is checked separately).

Theorem 6.1 is a composition rule, not a no-go for all placements.  A collar
passing the one-sided screen must still pass exact nonzero feasibility, and a
passing signature pair would still need residual width at most 19 and then an
exact 19-column OR--Pascal/literal completion.

## 7. Artifacts and hashes

The parameterized compact verifier and radius-eight output are

```text
scratch/scan_k15_terminal_antichain_envelopes.cpp
scratch/k15_terminal_r8_antichain_certificate.json
```

with SHA-256 values

```text
a1f4767b5c5a56fbb58054b29ae6afc9d20ad5cbbcabc612352caf14a91c6de5
b54ac51bb3f780a36c8b13fbdc3ae4e47a6b86242db8f48cf9d57a9d1a081ff5
```

It is compiled with the explicit definition

```text
-DTAIL_R=8
```

and is bound to the verified input by

```text
scratch/k15_terminal_r8_audit_manifest.json
```

whose SHA-256 is

```text
3bb976580b2c505727489824b1b09b21ce844646a57082769999d88d7b44ad76
```

The executable checks the exact 6,438-prefix residual and all displayed
structural constants.  The cryptographic input identity is supplied by this
manifest rather than recomputed inside the C++ executable.

The input word and first-6,438-entry hashes are

```text
c4300f7d6ec4f618ead87bb15ca3b831803f0c3296e3c5274f4ecd91fb029598
224348c46f92592b722bdd29689567164968415f601c33957d8258681f2bfdea.
```
