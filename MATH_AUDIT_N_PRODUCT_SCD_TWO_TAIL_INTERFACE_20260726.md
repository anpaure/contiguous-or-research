# Exact product-SCD two-tail word and uniform Stage-A interface

Date: 2026-07-26

## 0. Verdict

The product-SCD tail used in Lemma 7.3 and in equations (5.5)--(5.12) is
valid in the following exact form.

Let `X,Y` be disjoint sets of size `m`, let `0<=r<=m`, and put

\[
 A_m(a)=\binom ma-\binom m{a-1},
 \qquad
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0,
 \end{cases}
\]

and

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0.
 \end{cases}
\]

There is a literal word on `X dotcup Y` of exact constructed length

\[
 \boxed{L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
                  A_m(a)w_m(a)C_m(r-a)}                         \tag{0.1}
\]

covering every nonempty set of rank at most `r` and every set of rank at
least `2m-r`.  The single word covers both tails.  The factor `2` already
present in (0.1) comes from the two sides of each product gadget; it is not
an additional payment for the upper tail.

If `z` is one new coordinate, the ordinary trimmed lift has exactly
`2L_m(r)` entries and covers, in dimension `2m+1`, every nonempty rank at
most `r` and every rank at least `2m-r+1`.  In particular, with

\[
                         r=m-H-1,                                \tag{0.2}
\]

it covers every rank outside

\[
                         [m-H,m+H+1].                            \tag{0.3}
\]

Uniformly along every integer sequence satisfying

\[
             H/\sqrt m\longrightarrow\infty,
 \qquad      0\le H\le m/2,                                    \tag{0.4}
\]

one has

\[
 L_m(m-H-1)=o\!\binom{2m}{m},
 \qquad
 2L_m(m-H-1)=o\!\binom{2m+1}{m}.                               \tag{0.5}
\]

No MSW property, exact-factor property, common owner, port structure,
colouring, or compatibility with the central construction is used.  The
tail word may be concatenated to any literal Stage-A word.  The only missing
hypothesis after deleting a leave is control of the targets still missing
*inside* (0.3): the mere statement that the leave has `o(W)` rows or
occurrences does not itself imply that the number of central-band holes is
`o(W)`.

## 1. The half-cube chains and their literal increment words

Fix a symmetric chain decomposition of `2^X`.  Its chains have the form

\[
 C=(C_a\subset C_{a+1}\subset\cdots\subset C_{m-a}),            \tag{1.1}
\]

where `|C_j|=j` and each difference

\[
                         C_j\setminus C_{j-1}=\{e_j\}            \tag{1.2}
\]

is a singleton.  Symmetric chain decompositions exist for every `m`; for
completeness, the standard induction sends a chain (1.1) in `B_m` to the
two chains

\[
 (C_a,0)<\cdots<(C_{m-a},0)<(C_{m-a},1)
\]

and, when nonempty,

\[
 (C_a,1)<\cdots<(C_{m-a-1},1)
\]

in `B_(m+1)`.  These chains are saturated, symmetric, and partition the
product with the new coordinate.

Define the nonempty increment word

\[
 R(C)=
 \begin{cases}
  \{e_1\},\ldots,\{e_m\},&a=0,\\
  C_a,\{e_{a+1}\},\ldots,\{e_{m-a}\},&a>0,
 \end{cases}                                                    \tag{1.3}
\]

and put `L(C)=rev R(C)`.  Every entry is nonempty, and

\[
                         |R(C)|=|L(C)|=w_m(a).                   \tag{1.4}
\]

For every nonempty member `C_j` of the chain, a prefix of `R(C)` has union
`C_j`, and a suffix of `L(C)` has union `C_j`.  The empty member of the
unique rank-zero chain is deliberately omitted, because the universal-OR
problem asks for nonempty targets and nonempty word entries.

The number of chains of minimum rank exactly `a` is forced.  At rank `a`,
the number of chains whose minimum is at most `a` is `binom(m,a)`, since
each such symmetric chain contains exactly one rank-`a` member.  Hence

\[
                         \#\{C:\min C=a\}=A_m(a).                \tag{1.5}
\]

This count is independent of which symmetric chain decomposition was
chosen.

## 2. Exact even-dimensional construction

Choose independently any symmetric chain decomposition of `2^X` and any
one of `2^Y`.  For every ordered pair `(C,D)` of half-cube chains with
minimum ranks `a,b` satisfying

\[
                             a+b\le r,                            \tag{2.1}
\]

append the gadget

\[
                             L(C)\,\Vert\,R(D).                   \tag{2.2}
\]

Concatenate these gadgets in an arbitrary order.

### Theorem 2.1 (literal two-tail coverage)

The word (2.2), over all pairs (2.1), covers every nonempty
`S subseteq X dotcup Y` such that

\[
                             |S|\le r
 \quad\hbox{or}\quad          |S|\ge2m-r.                       \tag{2.3}
\]

#### Proof

Write `S=S_X dotcup S_Y`.  Let `C,D` be the unique half-chains containing
`S_X,S_Y`, with minimum ranks `a,b`.

If `|S|<=r`, then

\[
                         a+b\le |S_X|+|S_Y|=|S|\le r.             \tag{2.4}
\]

If `|S|>=2m-r`, symmetry of the two chains gives

\[
 a\le m-|S_X|,
 \qquad b\le m-|S_Y|,
\]

and therefore

\[
                         a+b\le2m-|S|\le r.                      \tag{2.5}
\]

Thus the relevant pair is scheduled in either case.  If both parts are
nonempty, take the suffix of `L(C)` whose union is `S_X` followed by the
prefix of `R(D)` whose union is `S_Y`.  This is one contiguous interval of
the gadget and its union is exactly `S`.  If one part is empty, use only the
appropriate one-sided suffix or prefix.  The case in which both parts are
empty is outside the problem.  Every witness lies inside one gadget, so the
order of concatenation and all inter-gadget seams are irrelevant.  This also
proves the upper-tail assertion directly; no complementation of an OR
witness has been used.  \(\square\)

### Theorem 2.2 (exact length and the origin of both factors)

The constructed word has length exactly (0.1).

#### Proof

Summing the two side lengths of (2.2) gives

\[
 \sum_{a+b\le r}A_m(a)A_m(b)\bigl(w_m(a)+w_m(b)\bigr).           \tag{2.6}
\]

The two summands are equal after interchanging the distinguished halves.
Moreover the telescoping identity

\[
 \sum_{b=0}^{\min(t,\lfloor m/2\rfloor)}A_m(b)
   =\binom m{\min(t,\lfloor m/2\rfloor)}                         \tag{2.7}
\]

holds for `t>=0`, while the sum is zero for `t<0`.  Thus (2.6) equals

\[
 2\sum_aA_m(a)w_m(a)C_m(r-a)=L_m(r).                             \tag{2.8}
\]

The factor `2` in (2.8) is therefore the equality of the total left-side
and right-side gadget lengths.  The same gadgets simultaneously give both
tails in Theorem 2.1; there is no second tail-copy factor.  \(\square\)

## 3. Exact trimmed lift from `2m` to `2m+1`

The odd lift is a second and logically separate factor `2`.

### Lemma 3.1 (trimmed lift for an arbitrary covered family)

Let

\[
                         Q=(Q_1,\ldots,Q_N)                       \tag{3.1}
\]

be any nonempty set-valued word on a ground set `V`, and let `F` be any
family of nonempty targets witnessed by intervals of `Q`.  For a new
coordinate `z`, the word

\[
 Q_1,\ldots,Q_N,\{z\},
 \{z\}\cup Q_1,\ldots,\{z\}\cup Q_{N-1}                         \tag{3.2}
\]

has exactly `2N` entries and covers

\[
                         F\ \cup\ \{\{z\}\}
                 \ \cup\ \{S\cup\{z\}:S\in F\}.              \tag{3.3}
\]

#### Proof

The first copy retains every witness for `S in F`, and the displayed
singleton covers `{z}`.  Choose an old witness `[i,j]` for `S`.  If `j<N`,
the corresponding interval in the transformed block witnesses
`S union {z}`.  If `j=N`, the seam interval

\[
                         Q_i,Q_{i+1},\ldots,Q_N,\{z\}             \tag{3.4}
\]

has union `S union {z}`.  This is why the final transformed entry may be
deleted without losing any lifted target.  No universality assumption on
`Q` is used.  \(\square\)

Apply Lemma 3.1 to the even tail family in Theorem 2.1.  Its length is
exactly `2L_m(r)`.  It certainly covers every nonempty odd-dimensional set
`T` with

\[
                         |T|\le r
 \quad\hbox{or}\quad          |T|\ge2m-r+1.                      \tag{3.5}
\]

Indeed, if `z notin T`, the even word covers `T` (with one harmless extra
upper layer available).  If `z in T`, write `T=S union {z}`.  The singleton
case is explicit; otherwise the inequalities in (3.5) imply respectively
`|S|<=r-1` or `|S|>=2m-r`, so (3.3) applies.

With `r=m-H-1`, (3.5) becomes

\[
                         |T|\le m-H-1
 \quad\hbox{or}\quad          |T|\ge m+H+2,                      \tag{3.6}
\]

exactly the ranks outside (0.3).  The lifted word additionally covers some
targets on the two boundary layers of the central band; this overlap is
harmless.

For reference, the exact parity ledger is therefore

\[
\begin{array}{c|c|c}
\text{dimension}&\text{central ranks left to Stage A}&\text{tail length}\\ \hline
2m&[m-H,m+H]&L_m(m-H-1)\\
2m+1&[m-H,m+H+1]&2L_m(m-H-1).
\end{array}                                                     \tag{3.7}
\]

Equivalently, in the usual odd-dimensional depth notation, the same word
simultaneously covers

\[
 \binom{[2m+1]}{m-q}
 \quad\hbox{and}\quad
 \binom{[2m+1]}{m+1+q}
 \qquad\hbox{for every }q\ge H+1.                               \tag{3.8}
\]

Thus there is no unhandled parity layer at the interface `q=H+1`.

## 4. Uniform `o(W)` estimate without a moderate-deviation upper range

Put

\[
 M=\lfloor m/2\rfloor,
 \qquad B_m=\binom mM,
 \qquad x=M-a.                                                    \tag{4.1}
\]

The increment words enumerate all nonempty members of all half-cube chains,
so the exact identity

\[
                         \sum_aA_m(a)w_m(a)=2^m-1                \tag{4.2}
\]

holds.  Thus

\[
 p_m(a)=\frac{A_m(a)w_m(a)}{2^m-1}                               \tag{4.3}
\]

is a probability distribution.

For `a>0`, direct subtraction in `A_m(a)` gives

\[
 A_m(a)w_m(a)
   =\binom ma\frac{(m-2a+1)^2}{m-a+1}.                           \tag{4.4}
\]

Write `m=2M+epsilon`, where `epsilon` is zero or one.  Successive binomial
ratios give the explicit estimate

\[
 \frac{\binom m{M-x}}{B_m}
 =\begin{cases}
 \displaystyle\prod_{j=1}^x\frac{M-j+1}{M+j},&\epsilon=0,\\[2mm]
 \displaystyle\prod_{j=1}^x\frac{M-j+1}{M+j+1},&\epsilon=1
 \end{cases}
 \le e^{-x^2/m}.                                                 \tag{4.5}
\]

Indeed `log(1-u)<=-u`; in the even case the sum of the resulting
`(2j-1)/m` terms is `x^2/m`, and in the odd case the sum of the `2j/m`
terms is at least `x^2/m`.  Since `m-2a+1<=2x+2` and
`m-a+1>=m/2`, equations (4.4)--(4.5) imply, for `a>0`,

\[
 A_m(M-x)w_m(M-x)
 \le 8\,\frac{(x+1)^2}{m}B_m e^{-x^2/m}.                         \tag{4.6}
\]

The omitted case `a=0` has weight exactly `m` and hence probability
`m/(2^m-1)`.  The elementary Wallis bound
`B_m/(2^m-1)<=2/sqrt(m)` for `m>=2`, comparison of the sum in (4.6) with
unit mesh on the scale `sqrt(m)`, and the separate rank-zero term give,
for an absolute constant `C`, the uniform tightness

\[
 \sup_m\sum_{x>K\sqrt m}p_m(M-x)
 \le C\int_{K/2}^\infty(1+u^2)e^{-u^2}\,du.                    \tag{4.7}
\]

Now set `r=m-H-1`.  If `a=M-x`, then

\[
 r-a=M-H-1-M+x.
\]

When `m=2M` its distance below the central rank is `H+1-x`, and when
`m=2M+1` it is `H-x`.  Consequently, for every fixed `K`, uniformly on
`x<=K sqrt(m)`, eventually `H>=2K sqrt(m)`, and either
`C_m(r-a)=0` or

\[
 \frac{C_m(r-a)}{B_m}
 \le \exp\!\left(-\frac{(H-x)^2}{m}\right)
 \le \exp\!\left(-\frac{H^2}{4m}\right)
 \longrightarrow0                                               \tag{4.8}
\]

whenever `H/sqrt(m)->infinity`.  Splitting (4.3) at `K sqrt(m)`, using
(4.7)--(4.8), first letting `m` tend to infinity and then `K` tend to
infinity, proves

\[
 \sum_ap_m(a)\frac{C_m(m-H-1-a)}{B_m}=o(1).                      \tag{4.9}
\]

Equations (0.1), (4.2), and (4.9) give

\[
 L_m(m-H-1)=o(2^mB_m).                                          \tag{4.10}
\]

Finally

\[
                         2^mB_m=\Theta\!\binom{2m}{m},           \tag{4.11}
\]

so the first assertion in (0.5) follows.  For the lifted word use the exact
identity

\[
 \binom{2m+1}{m}=\frac{2m+1}{m+1}\binom{2m}{m}:                  \tag{4.12}
\]

\[
 \frac{2L_m(m-H-1)}{\binom{2m+1}{m}}
 =\frac{2(m+1)}{2m+1}
   \frac{L_m(m-H-1)}{\binom{2m}{m}}
 \longrightarrow0.                                              \tag{4.13}
\]

This proof needs no condition `H=o(m^(2/3))`.  The convenient finite range
`H<=m/2` guarantees `r>=0` and is more than sufficient for every diagonal
application with `H=o(m)`.

## 5. Uniform composition with an arbitrary Stage A

### Theorem 5.1 (literal black-box tail interface)

Let `A_(m,H)` be any literal word on a `(2m+1)`-set.  Suppose it covers all
targets in the central ranks (0.3) except a family `E_(m,H)` of nonempty
targets.  Then there is a universal literal word of length

\[
 \boxed{
 |A_{m,H}|+|E_{m,H}|+2L_m(m-H-1).}                               \tag{5.1}
\]

#### Proof

Concatenate `A_(m,H)`, one set-letter equal to each target in `E_(m,H)`, and
the independently constructed odd tail word of Section 3.  Central targets
are covered by the first two blocks and all remaining ranks by the third.
Every witness used is internal to one block, so no seam condition is needed.
All letters and witnesses are literal and integral.  \(\square\)

In particular, if

\[
 |A_{m,H}|\le\binom{2m+1}{m}+o(W),
 \qquad |E_{m,H}|=o(W),                                         \tag{5.2}
\]

and (0.4) holds, (5.1) is `W+o(W)`.  The statement applies verbatim after
an arbitrary exact middle factor is switched, conjugated, or otherwise
modified, and also to a partial Stage-A word obtained by deleting a leave.
No relationship between that factor and either half-cube SCD is required.

What is not automatic is the second condition in (5.2).  An `o(W)` leave
measured in rows, middle occurrences, or factor components can be the sole
owner of many targets at many central depths.  The product-SCD word covers
only the outer ranks (3.6), and supplies no estimate on those central holes.
Thus the exact additional hypothesis needed after leave deletion is a
literal repair ledger

\[
                         |E_{m,H}|=o(W),                          \tag{5.3}
\]

or any stronger weighted-overload/owner theorem implying (5.3).  There is
no further tail-interface hypothesis.

There is a simple worst-case deletion ledger when the Stage-A object is
compiled from cyclic factor rows.  If `D` complete rows are removed, then at
each depth a removed row deletes at most `2(2m+1)` lower-plus-upper interval
occurrences.  Therefore

\[
 |E_{\rm after}|
 \le |E_{\rm before}|+2(2m+1)D(H+1).                            \tag{5.4}
\]

Consequently the purely cardinal sufficient condition is

\[
 D=o\!\left(\frac{W}{(2m+1)(H+1)}\right)
 \quad\left(\text{equivalently }(2m+1)D(H+1)=o(W)\right),       \tag{5.5}
\]

or, if the leave is measured by its `R=(2m+1)D` deleted middle
occurrences,

\[
                         R(H+1)=o(W).                            \tag{5.6}
\]

These are only worst-case sufficient bounds; owner multiplicity can make a
larger deletion harmless.  They explain why `R=o(W)` alone is not the
needed theorem.  If leave size is instead counted in complete rows, the
condition `D=o(W)` is vacuous: even the entire exact factor has only
`W/(2m+1)=o(W)` rows.

## 6. Scope and audit cautions

1. The universal-OR problem here excludes the empty target and requires
   nonempty set-letters.  If a different convention requires the empty set
   to have a nonempty witness, one extra zero letter is necessary; this is
   not the convention used by `nu(k)`.
2. `L_m(r)` in (0.1) is the exact length of the even word and already
   contains a factor `2`.  The odd word has length `2L_m(r)`, not `L_m(r)`
   and not `4L_m(r)` under a different tail convention.
3. The odd trimmed lift needs no endpoint hypothesis.  The seam (3.4)
   replaces precisely the omitted final transformed letter.
4. The upper tail is witnessed directly from symmetric upper endpoints.
   Complementation is never applied to an OR witness.
5. The asymptotic is uniform for every sequence satisfying (0.4), but fixed
   `H=A sqrt(m)` with fixed `A` gives only an `A`-dependent normalized tail,
   not `o_m(W)`.  The diagonal must have `A=A(m)->infinity`.
6. The tail theorem is independent of Stage A.  It proves no bound on
   central-band holes created by deleting a leave.
