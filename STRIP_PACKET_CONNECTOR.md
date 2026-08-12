# The terminal two-rail strip packet

## 1. Outcome

Let

\[
                 P_{s,c}=[0,1]\times[0,s]\times[0,c],
                 \qquad 1\le s\le c,
\]

with coordinatewise maximum, and let `g(1,s,c)` be the shortest word whose
nonempty contiguous maxima contain every nonzero point of `P_(s,c)`.

The independent symmetric-chain connectors for the two hooks in
`[0,1]x[0,s]` have nonzero length

\[
                              2s+2c+1.              \tag{1.1}
\]

The exact diamond result in `CROSS_CHAIN_PACKET_CONNECTOR.md` gives, for
`s=1`,

\[
                   g(1,1,c)=\left\lceil{3c\over2}\right\rceil+2. \tag{1.2}
\]

For every wider strip there is a simpler uniform fusion.

### Theorem A (shared strict-tail connector)

For every `2<=s<=c`,

\[
 \boxed{
                         g(1,s,c)\le2s+2c-1.}       \tag{1.3}
\]

Thus two adjacent terminal hook rectangles always save two entries over
their independent connectors.  The word is explicit, deterministic, and
output-linear.

The saving in (1.3) is additive, not a fixed fraction of `s`.  This pass
does **not** prove a bound of the form

\[
                  2s+2c+1-\epsilon s               \tag{1.4}
\]

for any absolute `epsilon>0`.  It instead proves a sharp obstruction inside
the natural one-flag/one-repair architecture: both pieces used in Theorem A
already have minimum possible length, and they share the only endpoint that
this architecture allows them to share.  A fractional saving requires a
genuine multi-seam braid in which entries simultaneously serve the two
target sheets.

The construction has been independently checked for every
`2<=s<=c<=100`; the verification is only a sanity check and is not used in
the proof.

## 2. Notation

Write

\[
 \begin{aligned}
 A_i&=(0,i,0),                 &&1\le i\le s,\\
 X  &=(1,0,0),\\
 Z_j&=(0,0,j),                 &&1\le j\le c,\\
 V_j&=(0,1,j),                 &&1\le j\le c-1,\\
 H_i&=(0,i,1),                 &&2\le i\le s.
 \end{aligned}                                    \tag{2.1}
\]

The letters `A_i`, `X`, and `Z_j` are forced pure-axis targets.  The `V_j`
and `H_i` form the two arms of the strict rectangle

\[
                         [1,s]\times[1,c]           \tag{2.2}
\]

in the last two coordinates.

## 3. The explicit word

Define

\[
 \begin{split}
 W_{s,c}={}&
 A_s,A_{s-1},\ldots,A_1,
 X,
 Z_1,Z_2,\ldots,Z_c,\\
 &V_{c-1},V_{c-2},\ldots,V_1,
 H_2,H_3,\ldots,H_s.
 \end{split}                                      \tag{3.1}
\]

Empty ranges are omitted.  For `s,c>=2`, its length is

\[
 s+1+c+(c-1)+(s-1)=2s+2c-1.                       \tag{3.2}
\]

The occurrence `Z_c` is doing two jobs.  It is the final member of the first
flag and the first member of the strict-rectangle connector

\[
 Z_c,V_{c-1},\ldots,V_1,H_2,\ldots,H_s.            \tag{3.3}
\]

That one shared occurrence is the second fusion beyond the ordinary
one-position bottom trim.

## 4. Coverage proof

### 4.1 The complete `x=1` sheet

Fix `0<=i<=s` and `0<=j<=c`.

* If `i=j=0`, the literal `X` represents `(1,0,0)`.
* If `i=0` and `j>0`, the interval from `X` through `Z_j` has maximum
  `(1,0,j)`.
* If `i>0` and `j=0`, the interval from `A_i` through `X` has maximum
  `(1,i,0)`.
* If `i,j>0`, the interval

  \[
                  A_i,A_{i-1},\ldots,A_1,
                  X,Z_1,\ldots,Z_j                 \tag{4.1}
  \]

  has maximum `(1,i,j)`.

Thus the prefix through `Z_c` covers every target with first coordinate one.
The same prefix contains every pure second- and third-axis target `A_i` and
`Z_j` literally.

### 4.2 The strict `x=0` rectangle

It remains to represent `(0,i,j)` with `i,j>=1`.

For `i=1`:

* if `j<c`, the target is the literal `V_j`;
* if `j=c`, the interval `Z_c,V_(c-1)` has maximum `(0,1,c)`.

The last interval is valid because `c>=2`.

For `i>=2`:

* if `j=1`, the target is the literal `H_i`;
* if `2<=j<c`, use

  \[
           V_j,V_{j-1},\ldots,V_1,H_2,H_3,\ldots,H_i; \tag{4.2}
  \]

* if `j=c`, begin (4.2) instead at `Z_c`.

Along (4.2), the third coordinate only decreases before the turn and the
second coordinate only increases after the turn.  Its componentwise maximum
is exactly `(0,i,j)`.  This covers the remaining sheet and proves Theorem A.

## 5. Exact length comparison for the hook packet

The standard hook decomposition of `[0,p]x[0,q]`, `p<=q`, has terminal
pair

\[
 H_{p-1}\sqcup H_p
      =\{p-1,p\}\times[0,q-p+1].                   \tag{5.1}
\]

Put

\[
                              s=q-p+1.              \tag{5.2}
\]

After translation and multiplication by `[0,c]`, this packet is precisely
`P_(s,c)`.  Its two independent chain connectors have edge heights `s+1`
and `s-1`, hence length

\[
 (s+1+c+1)+(s-1+c+1)=2s+2c+2                    \tag{5.3}
\]

when the packet's local minimum is included.

If the local minimum is the global zero, delete it: (5.3) becomes
`2s+2c+1`.  Theorem A gives `2s+2c-1`, a saving of two.

If the local minimum is nonzero, add it once to the word (3.1).  The fused
length is at most

\[
                              2s+2c,                \tag{5.4}
\]

again saving exactly two from (5.3).

For `s=1`, use the exact diamond word instead.  Including its local minimum,
its length is

\[
                 \left\lceil{3c\over2}\right\rceil+3, \tag{5.5}
\]

and its saving from the independent length `2c+4` is
`floor(c/2)+1`.

## 6. Why the two pieces cannot be shortened separately

The construction consists of a complete first-coordinate-one flag and a
strict first-coordinate-zero repair connector.  Each part is already tight
for its assigned job.

### Lemma 1 (forced flag mass)

Any word containing the pure targets

\[
 A_1,\ldots,A_s,quad X,quad Z_1,\ldots,Z_c        \tag{6.1}
\]

has at least `s+c+1` positions.

#### Proof

For a pure target on one coordinate axis, every entry of its witness is zero
on the other axes, and one entry must attain its exact positive coordinate
height.  Different heights and different axes force different entries.
The target `X` forces one further entry.  \(\square\)

The prefix in (3.1) has exactly this many entries and simultaneously covers
the whole `x=1` sheet.

### Lemma 2 (strict-tail mass)

Suppose a repair region is required to represent every point of
`[1,s]x[1,c]` in the last two coordinates and is allowed the boundary entry
`Z_c=(0,c)`.  Then the region together with `Z_c` contains at least

\[
                              s+c-1                \tag{6.2}
\]

positions.

#### Proof

For every `2<=i<=s`, the target `(i,1)` needs an entry whose second
coordinate is exactly `i` and whose third coordinate is at most one.  These
force `s-1` distinct positions.

For every `1<=j<=c-1`, the target `(1,j)` needs an entry whose third
coordinate is exactly `j` and whose second coordinate is at most one.  These
force `c-1` further positions, disjoint from the first family.  Finally the
provided boundary occurrence `Z_c` is a separate position.  The total is
`(s-1)+(c-1)+1=s+c-1`.  \(\square\)

The connector (3.3) attains (6.2).  Hence no compression that leaves the
flag and strict repair as separate witness regions can improve Theorem A.

This is an architectural lower bound, not a lower bound on unrestricted
strip words.  An unrestricted word may place mixed entries so that one
position participates in witnesses from both regions.

## 7. Relation to the exact diamond

When `s=1`, the strict repair consists only of the vertical targets `V_j`.
The exact diamond word interleaves these targets with positive `X`-pivots
and reduces the combined mass from about `2c` to `3c/2`.

For `s>=2`, the repair also has the horizontal arm

\[
                         H_2,H_3,\ldots,H_s.        \tag{7.1}
\]

Attaching this arm to the exact diamond as a conventional external tail
forces a complete vertical suffix port.  Attaching the pure-axis arm on the
other side forces the matching prefix port.  The two-sided record lemma from
`CROSS_CHAIN_PACKET_CONNECTOR.md` then requires at least `2c-1` scalar
height positions, erasing the diamond's linear saving.

This does not prove that the strip itself lacks a fractional fusion.  It
proves that the obvious operation

\[
       \text{optimal diamond core}+\text{two ordinary rail tails} \tag{7.2}
\]

cannot provide one.

## 8. What a fractional saving must do

Theorem A has only one overlap: `Z_c`.  Lemmas 1 and 2 show that a bound
with saving `Omega(s)` must create `Omega(s)` additional cross-role
positions.  More concretely, it must eliminate a positive fraction of the
strict-tail providers

\[
             V_1,\ldots,V_{c-1},H_2,\ldots,H_s      \tag{8.1}
\]

while still attaining their exact coordinate heights.  Those heights are
forced somewhere, so the replacement positions must also serve witnesses
in the first-coordinate-one flag.

This identifies the next object precisely.

> **Multi-seam strip braid (open).**  Order the forced axis entries and
> `O(s+c)` mixed entries so that at least `epsilon*s` exact-height providers
> simultaneously serve the `x=1` flag and the strict `x=0` rectangle, while
> every target retains a contiguous witness.

A rewrite confined entirely inside the strict tail cannot work, by Lemma 2.
A rewrite confined entirely inside the flag cannot work, by Lemma 1.  The
sharing must cross their present boundary and must use more than one scalar
prefix/suffix portal.

## 9. Aggregation consequence

Pairing adjacent chains throughout the nested three-box SCD and saving only
two entries per pair produces at most a constant times the number of chains.
For an equal box this is `O(m^2)`, whereas the independent-chain excess is
`Theta(m^3)`.  Thus Theorem A is a genuine packet fusion but does not alter
the `7/4` leading coefficient from `THICK_FOUR_BOX_SLICE_FUSION.md`.

The diamond packets can save `Theta(c)` each, but balanced terminal diamonds
occur too sparsely to change this conclusion.  A thick-sector improvement
still needs a uniform `Omega(min(c,L))` saving for a positive density of
long two-rail ribbons, or a larger packet which shares across many rails at
once.

## 10. Verification artifact and theorem ledger

`scratch/strip_packet_verify.cpp` constructs (3.1), exhaustively enumerates
all intervals, and verifies every box point for all `2<=s<=c<=100`.

Proved:

* the explicit strip word (3.1);
* the uniform bound `g(1,s,c)<=2s+2c-1` for `2<=s<=c`;
* exact local-zero accounting for terminal hook packets;
* minimum mass of the clean flag and strict repair pieces; and
* failure of the black-box diamond-plus-two-ports extension.

Open:

* any unrestricted bound with a fixed positive fraction saving in `s`;
* the exact value of `g(1,s,c)` beyond the already certified small cases;
* a multi-seam strip braid; and
* a uniform packet theorem for nonterminal turned ribbons.
