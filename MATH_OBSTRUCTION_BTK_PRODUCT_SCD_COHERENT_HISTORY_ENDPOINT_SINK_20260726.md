# BTK product-SCD endpoints are coherent-history sinks

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

The requested uniform forbidden-set endpoint degree is false for the
standard Greene--Kleitman/de Bruijn--Tengbergen--Kruyswijk symmetric-chain
decomposition.  The failure is stronger than an artificial choice of a
forbidden set.

Let a rank-`m` product path have length `h` and traverse it from its low
endpoint to its high endpoint.  Its `h` Johnson edges use two active
alphabets

\[
             I_A(P)\subset A,\qquad I_B(P)\subset B,
             \qquad |I_A(P)|=|I_B(P)|=h.              \tag{0.1}
\]

If `Q` is any other BTK product path having a Johnson-adjacent endpoint,
then, for `h\ge 4`,

\[
       (I_A(Q)\cup I_B(Q))\cap(I_A(P)\cup I_B(P))
       \ne\varnothing.                               \tag{0.2}
\]

For a cross-half endpoint edge one has the much stronger componentwise
nesting

\[
\begin{array}{c|c}
 \text{new level}&\text{active alphabets}\ \\ \hline
 r+1&I_A(Q)\subset I_A(P),\quad I_B(Q)\subset I_B(P),\\
 r-1&I_A(P)\subset I_A(Q),\quad I_B(P)\subset I_B(Q).
\end{array}                                         \tag{0.3}
\]

For a same-half edge, the untouched half has exactly the same active
alphabet.  Consequently

\[
                 Z_P:=I_A(P)\cup I_B(P),\qquad |Z_P|=2h,          \tag{0.4}
\]

is a zero-degree forbidden-coordinate cut at the exit of `P`.

This is precisely the forbidden set carried by the actual two-sided
`H`-memory history.  If

\[
                         2h+3\le H,                              \tag{0.5}
\]

then no endpoint seam out of `P`, followed by the adjacent product path,
is two-sided `H`-safe.  The assertion holds in either orientation.

At the scale

\[
                         H=\sqrt m\log\log m,                    \tag{0.6}
\]

the product paths with

\[
                         \sqrt m\le h\le2\sqrt m                \tag{0.7}
\]

are therefore coherent-history sinks.  Their exact asymptotic number is

\[
 \left[
   {2\over\sqrt\pi}(e^{-1}-e^{-4})+o(1)
 \right]{W\over\sqrt m},
 \qquad W=\binom{2m}{m}.                         \tag{0.8}
\]

Thus every endpoint-only, fixed-BTK product-path fusion has
`Omega(W/sqrt(m))` components, even after deleting `o(W/H)` atomic
paths.  This is larger than `W/H` by a factor of order `log log m`.

There is an important complement qualification.  A chainwise
complement-stable SCD does not exist for `m\ge2`.  The honest
complement-symmetric object is a pair of frames `B` and `B^c`.  The
obstruction above applies separately to each of these two product
frames.  It does not rule out a seam which changes from one frame to the
other, nor an internally cut/nonproduct path.  A successful endpoint
mixing theorem must use one of those mechanisms.

## 1. The BTK stack and active alphabets

Write subsets of `[m]` as zero-one words.  Read a word from left to
right.  At a `1`, push its position onto a stack.  At a `0`, pop the top
position and match the resulting `10` pair when the stack is nonempty;
otherwise leave the `0` unmatched.  At the end, the stack is the ordered
list

\[
                         R(w)=(u_1,\ldots,u_t)                   \tag{1.1}
\]

of unmatched `1` positions.

The matched pairs and unmatched positions define the usual BTK chain.
If its minimum rank is `a`, it has `m-2a` unmatched positions.  Along
the chain these positions carry a block of zeroes followed by a block of
ones.  At rank `s`, the last `s-a` unmatched positions are one.

Fix a product path at level `r`, so

\[
                         h=m-2r.                                 \tag{1.2}
\]

Let `C` be an `A`-chain of minimum rank `a\le r`.  At the high product
endpoint its `A`-word is `C_{m-r}`.  Put `p=r-a`.  Its unmatched word
has `p` zeroes followed by `h+p` ones.  Therefore its final stack has
length `h+p`, and

\[
 I_r(C)=\{\text{the first `h` entries of }R(C_{m-r})\}.          \tag{1.3}
\]

This is exactly

\[
                         C_{m-r}\setminus C_r.                  \tag{1.4}
\]

For a `B`-chain at the low product endpoint, the dual right-to-left
stack of unmatched zeroes gives the identical statement.  Its first
`h` persistent entries form `D_{m-r}\setminus D_r`.

## 2. The one-bit stack-nesting lemma

### Lemma 2.1 (stack deletion)

Let `w_i=1`, and let `w^\downarrow` be obtained by replacing that bit
by `0`.  Then `R(w^\downarrow)` is an ordered subsequence of `R(w)` and
at most two entries of `R(w)` are deleted.

Conversely, if `w_i=0` and `w^\uparrow` is obtained by replacing it by
`1`, then `R(w)` is an ordered subsequence of `R(w^\uparrow)`, with at
most two inserted entries.

#### Proof

Immediately before position `i`, let the stack be `S`.  In the word
`w`, the operation appends `i`, giving `Si`.  In
`w^\downarrow`, it deletes the last entry of `S` when one exists, and
otherwise leaves the stack empty.  Hence the latter stack is obtained
from the former by deleting one or two entries.

Apply the same remaining suffix to both stacks.  A common push appends
the same new entry to both lists.  A common pop deletes their last
entries; if one list is shorter, a pop made after it has emptied can
only reduce the discrepancy.  Inductively, the shorter list remains an
ordered subsequence of the longer one and the number of missing entries
never increases.  This proves the first assertion.  Interchanging the
two words proves the converse.  `square`

There is an exact endpoint consequence which does not require the two
chains to have the same minimum rank.

### Lemma 2.2 (active-tail nesting)

Suppose `x` is the high-half word of a level-`r` product endpoint, of
path length `h=m-2r`.

1. If `x^\downarrow` is the high-half word of a level-`r+1` product
   endpoint, then

   \[
                         I_{r+1}(x^\downarrow)\subset I_r(x).    \tag{2.1}
   \]

2. If `x^\uparrow` is the high-half word of a level-`r-1` product
   endpoint, then

   \[
                         I_r(x)\subset I_{r-1}(x^\uparrow).      \tag{2.2}
   \]

The dual statements hold for low-half words: changing `0` to `1` while
moving from `r` to `r+1` shrinks the active alphabet, and changing `1`
to `0` while moving to `r-1` enlarges it.

#### Proof

By (1.3), `I_r(x)` is the first `h` entries of `R(x)`.  At level
`r+1`, the path length is `h-2`, so the new active alphabet is the first
`h-2` entries of `R(x^\downarrow)`.  Lemma 2.1 says that the latter
list is obtained from `R(x)` by deleting at most two entries.  Its first
`h-2` entries therefore occur among the first `h` entries of `R(x)`.
This proves (2.1).

For (2.2), `R(x)` is obtained from `R(x^\uparrow)` by deleting at most
two entries.  Thus its first `h` entries occur among the first `h+2`
entries of the new stack, which are precisely the new active alphabet.

Reverse the coordinate order and complement all bits.  The low-half
zero stack becomes the high-half one stack, and the two asserted dual
statements follow.  `square`

## 3. Classification of every adjacent endpoint

Let

\[
                    X=C_{m-r}\cup D_r                             \tag{3.1}
\]

be the high endpoint of a positive-length product path `P`.  Assume
`h=m-2r\ge4`.  Then `|X\cap A|=m-r>m/2`.  A Johnson neighbor changes
this projection rank by `-1`, `0`, or `1`.  Hence any neighboring
positive-length product-path endpoint is again a high endpoint, at level
`r+1`, `r`, or `r-1`, respectively.

### Theorem 3.1 (BTK endpoint inheritance)

Let `Y` be a Johnson neighbor of `X` which is an endpoint of another
path `Q` in the same BTK product decomposition.

1. If the Johnson edge moves a coordinate from `A` to `B`, then `Q` is
   at level `r+1` and

   \[
       I_A(Q)\subset I_A(P),\qquad I_B(Q)\subset I_B(P).          \tag{3.2}
   \]

2. If it moves a coordinate from `B` to `A`, then `Q` is at level
   `r-1` and

   \[
       I_A(P)\subset I_A(Q),\qquad I_B(P)\subset I_B(Q).          \tag{3.3}
   \]

3. If the exchange is wholly inside `A`, the `B`-word belongs to the
   same unique BTK chain at the same level, and

   \[
                         I_B(Q)=I_B(P).                           \tag{3.4}
   \]

   The same statement with `A,B` interchanged holds for an exchange
   wholly inside `B`.

In every case (0.2) follows.  In the two cross-half cases both active
alphabets overlap whenever the shorter path has positive length.

#### Proof

For an `A`-to-`B` exchange, the high-half word changes one `1` to `0`,
the low-half word changes one `0` to `1`, and the level is `r+1`.
Lemma 2.2 and its low-half dual give (3.2).  The reverse changes and
level `r-1` give (3.3).

For an exchange internal to `A`, the `B`-subset is unchanged.  Every
Boolean set lies in one unique BTK chain.  Its projection rank is still
`r`, so its level-`r` active segment is unchanged, proving (3.4).  The
other same-half case is symmetric.  `square`

The theorem also holds at low endpoints after reversing every product
path and interchanging the two halves.

## 4. The arbitrary forbidden-set statement fails

For the endpoint `X` of `P`, choose

\[
                         Z=I_A(P)\cup I_B(P).                     \tag{4.1}
\]

Then `|Z|=2h`.  Theorem 3.1 says that every Johnson-adjacent product-path
endpoint has an active alphabet meeting `Z`.  Therefore the robust
degree subject to active-direction avoidance of `Z` is exactly zero.

In particular, whenever `h=O(H)`, this is a legitimate forbidden set of
size `O(H)`.  No positive polynomial lower bound can hold uniformly over
all such `Z` for the BTK product SCD.

## 5. The cut is the actual coherent history

The preceding cut is not merely an adversarial test.  Traverse `P` from
low to high.  Every coordinate in `I_A(P)` is inserted once and every
coordinate in `I_B(P)` is removed once.  Thus all of `Z` occurs in the
last `h` physical Johnson directions.

After a seam to the high endpoint of `Q`, the only continuation through
`Q` traverses it from high to low.  A shared `A`-coordinate is then
removed, giving an insertion-then-removal residence.  A shared
`B`-coordinate is inserted, giving a removal-then-insertion residence.
By the exact two-sided residence criterion, either repeat destroys
two-sided safety.

The two occurrences are separated by at most

\[
                         h+1+h(Q).                               \tag{5.1}
\]

Theorem 3.1 gives `h(Q)\in\{h-2,h,h+2\}`.  Hence every repeat lies in a
window of at most

\[
                         2h+3                                   \tag{5.2}
\]

edges.  We have proved:

### Theorem 5.1 (coherent-history sink)

If `h\ge4` and `2h+3\le H`, no Johnson endpoint seam from a traversed
BTK product path `P` to another BTK product path can be followed by the
second path while preserving both lower and upper flags through depth
`H`.

The same is true after traversing `P` high to low.  Thus every such
atomic path must be terminal in an `H`-safe endpoint-only fusion
component.  `square`

The statement is genuinely stateful.  Testing only the seam labels does
not see the obstruction: the repeated label may occur deep inside `P`
and deep inside `Q`.  The live `H`-queue does see it.

## 6. A Gaussian band forces too many components

Let `c_m=\binom m{\lfloor m/2\rfloor}`.  The exact number of rank-`m`
product paths of length at least `L` is

\[
                         P_{\ge L}
   =\binom m{\lfloor(m-L)/2\rfloor}^{\!2}.                       \tag{6.1}
\]

For fixed `0<alpha<beta`, adjusting the endpoints to the parity of `m`,
Stirling's formula gives

\[
 \#\{P:\alpha\sqrt m\le h(P)\le\beta\sqrt m\}
 =\bigl(e^{-\alpha^2}-e^{-\beta^2}+o(1)\bigr)c_m^2.             \tag{6.2}
\]

Indeed,

\[
 {\binom m{(m-\lambda\sqrt m)/2}\over
   \binom m{\lfloor m/2\rfloor}}
       =e^{-\lambda^2/2+o(1)}                                  \tag{6.3}
\]

uniformly for fixed `lambda`, and (6.2) is the difference of the two
squares in (6.1).  Also

\[
                         c_m^2
   =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.          \tag{6.4}
\]

Taking `alpha=1,beta=2` proves (0.8).

When `H=\sqrt m\log\log m`, every path in this band satisfies (0.5) for
all sufficiently large `m`.  By Theorem 5.1 each is terminal in its
fusion component, regardless of orientation.  Hence no two of them can
lie in the same component.  If `E_m` atomic paths are discarded, every
endpoint-only two-sided safe fusion has at least

\[
 \left[
   {2\over\sqrt\pi}(e^{-1}-e^{-4})+o(1)
 \right]{W\over\sqrt m}-E_m                                  \tag{6.5}
\]

components.  For `E_m=o(W/H)`, this is `Omega(W/sqrt(m))`, whereas the
coefficient-one endpoint ledger requires `o(W/H)`.

## 7. Complement symmetry: exact scope

There is no SCD of `B_m`, `m\ge2`, which is permuted chainwise by pure
set complementation.  The chain containing `emptyset` also contains
`[m]`, so complement stability would make it self-complementary.  If its
rank-one member is `{x}`, nestedness forces its rank-`m-1` member to
contain `x`, whereas self-complementarity would make that member
`[m]\setminus\{x\}`.  This is impossible.

Thus the phrase "complement-symmetric SCD" must mean a paired pair of
frames

\[
                         {\cal B},\qquad {\cal B}^{c},            \tag{7.1}
\]

where the second consists of the complements of the first chains,
reversed into increasing order.  The stack proof above applies to
`B`; after complementation its lower/upper dual applies to `B^c`.
Consequently each fixed frame separately has the sink obstruction and
the Gaussian component lower bound.

What has not been proved is that an endpoint in `B` cannot switch to a
path belonging to `B^c`, or to a third genuinely transverse SCD.  Such
a switch changes the record stack itself and need not preserve the
nesting (0.3).  Nor does the theorem cover cutting the atomic paths
internally.  These are the exact escapes left by the obstruction.

## 8. Proved boundary

Proved:

1. exact one-bit nesting of BTK endpoint active alphabets at adjacent
   product levels;
2. zero robust endpoint degree for the actual forbidden set of a
   traversed path;
3. failure of the full two-sided `H`-memory transition, not merely of a
   static endpoint test;
4. `Theta(W/sqrt(m))` coherent-history sinks at
   `H=sqrt(m) log log m`; and
5. the resulting component lower bound for every fixed-frame,
   endpoint-only BTK product fusion.

Not proved:

* a no-go for transitions between genuinely transverse SCD frames;
* a no-go after internal path cuts;
* a no-go for an SCD whose adjacent boundary chains have dispersed,
  nonnested active alphabets; or
* coefficient one.

The minimal positive successor is therefore a **transverse-frame
endpoint lemma**: construct at least polynomially many adjacent endpoints
whose active alphabets avoid the live queue, using a frame not sharing
the BTK record stack, and do so coherently under complement and through
successive histories.

