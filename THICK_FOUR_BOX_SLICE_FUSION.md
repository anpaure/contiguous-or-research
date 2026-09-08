# Thick four-box slice fusion

## 1. Outcome and theorem ledger

Let

\[
 Q(h,a,b,c)=[0,h]\times[0,a]\times[0,b]\times[0,c],
 \qquad h\le a\le b\le c,
\]

with coordinatewise maximum.  The audited slice-and-hook construction gives

\[
 g_4(h,a,b,c)
 \le(h+1)(a+1)(b+c+1)-1.                          \tag{1.1}
\]

This note proves a real fusion improvement.  Define

\[
 d=(h+a-b)_+,
 \qquad
 \Psi(d)=\left\lceil{d\over2}\right\rceil
         \left(\left\lfloor{d\over2}\right\rfloor+1\right).
 \tag{1.2}
\]

### Theorem A (three-short-side chain fusion)

There is an explicit word satisfying

\[
 \boxed{
 g_4(h,a,b,c)
 \le(h+1)(a+1)(b+c+1)-1-c\Psi(d).}                 \tag{1.3}
\]

The saving is nonzero exactly when the three shorter sides satisfy the
strict triangle inequality `b<h+a`.  For an equal box of side `m`,

\[
 \Psi(m)={m^2\over4}+O(m),
\]

so (1.3) improves the leading coefficient from `2` to `7/4`:

\[
                         g_4(m,m,m,m)
 \le {7\over4}m^3+O(m^2).                          \tag{1.4}
\]

The construction is search-free and output-linear.  It fuses all levels of
the height-`h` coordinate inside the short chains of the `(a,b)` hook
decomposition; it is not merely a rearrangement of independent slices.

### Theorem B (sharp limit of the independent-chain connector)

Let `L_1,...,L_r` be the edge heights in the explicit symmetric-chain
decomposition of the three-short-side box.  The fused word has exact length

\[
                  |Q(h,a,b)|+cr-1.                 \tag{1.5}
\]

The full four-box width is

\[
                  w_4(h,a,b,c)
                  =\sum_{j=1}^r(\min(c,L_j)+1).    \tag{1.6}
\]

Consequently the excess of this independent-chain connector over width is
exactly

\[
                 \sum_{j=1}^r\max(c,L_j)-1.        \tag{1.7}
\]

For equal sides this is

\[
                         {13\over12}m^3+O(m^2).     \tag{1.8}
\]

Thus the fusion is substantial but remains critical-order in the thick
sector.  It cannot prove an `O(S^(3-delta))` error for any fixed
`delta>0`.  Further progress must share entries **between distinct small-box
symmetric chains**, not only between fourth-coordinate slices within one
chain.

### Additional proved fact: the bottom two-slice lift

For every nontrivial product box `P`,

\[
                         g(P\times[0,1])\le2g(P).   \tag{1.9}
\]

This saves one position over treating the positive slice independently, but
the saving occurs only at the global-zero boundary and does not iterate into
a subcritical construction.

No universal thick-sector theorem is claimed.

Taking the better of Theorem A and the bottom two-slice lift improves the
original slice bound (1.1) by `max(1,c*Psi(d))` when `h>=1`; see (2.3).
This changes no leading asymptotic below.

## 2. A generic two-slice fusion lemma

Let

\[
                         W=x_1,x_2,\ldots,x_n
\]

be a nonzero universal word for a nontrivial box `P`, and let `0_P` be its
zero.  Form

\[
 \begin{split}
 &(x_1,0),(x_2,0),\ldots,(x_n,0),\\
 &(0_P,1),\\
 &(x_1,1),(x_2,1),\ldots,(x_{n-1},1).
 \end{split}                                      \tag{2.1}
\]

This word has length `2n`.

### Lemma 1 (trimmed bottom lift)

The word (2.1) is universal for `P x [0,1]`.

#### Proof

Targets with last coordinate zero retain their witnesses in the first copy.
The target `(0_P,1)` is the central marker.  For a target `(x,1)` with
`x!=0_P`, choose a witness `W[i..j]` for `x`.

* If `j<n`, use the corresponding interval in the final height-one copy.
* If `j=n`, use the height-zero suffix `W[i..n]` followed by the central
  marker.

The first-coordinate join is `x` and the last-coordinate maximum is one.
\(\square\)

If `P` consists only of zero, then `g(P)=0` while
`g(P x [0,1])=1`; this is the sole excluded degenerate case.

The lift does not yield one saving at every adjacent positive pair.  At a
positive low level, `(0_P,s)` is itself a required target, so a universal
low-slice word already needs the zero marker.  Applying the same trim merely
trades one copied entry for the new high marker and has the same length as
two independent positive slices.  A polynomial saving therefore needs more
structure than repeated use of Lemma 1.

Using the audited three-box word of length

\[
 n=(a+1)(b+c+1)-1
\]

for the bottom pair of fourth-coordinate levels, and treating levels
`2,...,h` independently, gives for every `h>=1`

\[
 g_4(h,a,b,c)
 \le(h+1)(a+1)(b+c+1)-2.                          \tag{2.2}
\]

Combining (2.2) with Theorem A, the best exact bound proved by the two
fusion mechanisms is

\[
 g_4(h,a,b,c)
 \le(h+1)(a+1)(b+c+1)-1
   -\max\{1,c\Psi(d)\},                            \tag{2.3}
\]

for `h>=1`.  For `h=0`, use Theorem A with `Psi(d)=0` and no extra trim.
The one-position improvement in (2.2) is lower order; the chain fusion is
the substantive saving.

## 3. A chain-SCD connector lemma

The useful extra structure is a symmetric-chain decomposition of several
coordinates at once.

Let a ranked join-semilattice `P` have a symmetric-chain decomposition

\[
                         \mathcal C=\{C_1,\ldots,C_r\}.
\]

Pair each `C_j` with the full chain `[0,c]`.  The audited chain-rectangle word
uses

\[
                         c+|C_j|
\]

entries before zero deletion and represents every point of
`C_j x [0,c]`.

### Lemma 2 (SCD connector)

There is an explicit universal nonzero word for `P x [0,c]` of length

\[
                         |P|+cr-1.                 \tag{3.1}
\]

#### Proof

Concatenate the `r` chain-rectangle gadgets.  Their target rectangles
partition `P x [0,c]`, so every witness is internal to one gadget.  Summing
their lengths gives

\[
 \sum_j(c+|C_j|)=cr+|P|.
\]

Exactly one gadget contains the global zero, which may be deleted.  Every
other chain minimum is a nonzero target and is retained.  \(\square\)

This lemma fuses all `c+1` levels across each symmetric chain of `P`.  Its
quality is governed entirely by the number `r=w(P)` of chains.

## 4. An explicit SCD of the three shorter sides

We now construct and count the chains in

\[
                         P=[0,h]\times[0,a]\times[0,b].
\]

First decompose `[0,h] x [0,a]` by the audited hooks.  Since `h<=a`, the
hook indexed by `t=0,...,h` has edge height

\[
                         q_t=h+a-2t.                \tag{4.1}
\]

Pair that chain with `[0,b]` and decompose their rectangle into symmetric
hooks.  A product of chains of edge heights `q_t` and `b` has exactly

\[
                         \min(q_t,b)+1              \tag{4.2}
\]

symmetric chains.  Shifting by the minimum rank of the first hook preserves
symmetry relative to total rank `h+a+b`.  Thus the nested hooks give an
explicit SCD of the whole three-chain box.

The number of chains is

\[
 \begin{aligned}
 r
 &=\sum_{t=0}^h(\min(h+a-2t,b)+1)\\
 &=(h+1)(a+1)
   -\sum_{t\ge0}(h+a-b-2t)_+.                     \tag{4.3}
 \end{aligned}
\]

For an integer `d>=0`,

\[
 \sum_{t\ge0}(d-2t)_+
 =\left\lceil{d\over2}\right\rceil
  \left(\left\lfloor{d\over2}\right\rfloor+1\right)
 =\Psi(d).                                        \tag{4.4}
\]

Therefore

\[
 \boxed{
 w_3(h,a,b)=r=(h+1)(a+1)-\Psi((h+a-b)_+).}         \tag{4.5}
\]

The equality with `w_3` follows directly from the SCD: every symmetric chain
crosses the central rank once, so the number of chains equals the width.

Two useful parity forms are

\[
 \Psi(2m)=m(m+1),\qquad
 \Psi(2m+1)=(m+1)^2.                              \tag{4.6}
\]

When `b>=h+a`, the middle ranks have a full plateau and `Psi=0`; all
`(h+1)(a+1)` pairs in the two shorter coordinates occur at the middle.

## 5. Proof and accounting of Theorem A

Apply Lemma 2 to the three-short-side box and the remaining chain `[0,c]`.
Its volume is

\[
                         |P|=(h+1)(a+1)(b+1).
\]

Equations (3.1) and (4.5) give

\[
 \begin{aligned}
 g_4(h,a,b,c)
 &\le(h+1)(a+1)(b+1)\\
 &\quad+c\big((h+1)(a+1)-\Psi(d)\big)-1\\
 &=(h+1)(a+1)(b+c+1)-1-c\Psi(d),                 \tag{5.1}
 \end{aligned}

which is (1.3).

### Direct interpretation in the old slice-and-hook word

The same saving can be seen without invoking the full three-side SCD at
once.  Decompose the `(a,b)` rectangle into hooks.  Their edge heights are

\[
                         q_t=a+b-2t,qquad0\le t\le a.
\]

For one such hook, the old slice word spends

\[
                         (h+1)(c+q_t+1).            \tag{5.2}
\]

Before the one global zero deletion.  Instead cover the local three-chain
box of heights `(h,q_t,c)` by the best coordinate choice in the audited
three-box theorem:

\[
 K_t=
 \begin{cases}
 (h+1)(c+q_t+1),&q_t\ge h,\\
 (q_t+1)(c+h+1),&q_t<h.
 \end{cases}                                      \tag{5.3}
\]

For a short hook, the exact saving is

\[
 (h+1)(c+q_t+1)-(q_t+1)(c+h+1)=c(h-q_t).          \tag{5.4}
\]

The short hook heights are `q_t=b-a+2r`, and their total deficit below `h`
is exactly `Psi((h+a-b)_+)`.  Summing (5.4) reproduces (5.1).

Every local three-chain constructor omits its local origin.  For `t=0` this
is global zero and remains omitted.  For every `t>0` the local origin is a
nonzero full-box target and is restored once.  The `a` restorations cancel
all but the one legitimate global `-1`, so no hidden zero correction is
missing from (5.1).

### Exact adjacent two-slice corollary

Set `h=1`.  Since `a<=b` are integers,

\[
 (1+a-b)_+=
 \begin{cases}1,&a=b,\\0,&a<b.\end{cases}
\]

Thus the two adjacent fourth-coordinate slices fuse nontrivially exactly at
the zero-height terminal hook of a square `(a,b)` rectangle:

\[
 g_4(1,a,a,c)
 \le2(a+1)(a+c+1)-1-c.                            \tag{5.5}
\]

The saving `c` comes from replacing `2(c+1)` independent copies of that
terminal chain by the single chain-rectangle connector of length `c+2`.
When `a<b`, this particular hook decomposition has no height-zero terminal
chain and its adjacent-slice accounting gives no saving beyond the generic
one-time bottom trim of Lemma 1.

## 6. Exact architectural obstruction

Let `C_j` have edge height `L_j`, so `|C_j|=L_j+1`.  The SCD connector word
has length

\[
 \sum_j(c+L_j+1)-1=|P|+cr-1.                      \tag{6.1}
\]

The product rectangle `C_j x [0,c]` has width

\[
                         \min(c,L_j)+1.
\]

The local middle ranks align with the global middle rank because `C_j` is
symmetric.  Summing over the target partition gives the exact full-box width

\[
                         w_4(h,a,b,c)
 =\sum_j(\min(c,L_j)+1).                           \tag{6.2}
\]

Subtracting (6.2) from (6.1) proves

\[
 \begin{aligned}
 (|P|+cr-1)-w_4
 &=\sum_j\big(c+L_j-\min(c,L_j)\big)-1\\
 &=\sum_j\max(c,L_j)-1.                           \tag{6.3}
 \end{aligned}

This is not a lower bound on arbitrary four-box words.  It is a sharp
obstruction to the architecture in which each small-box symmetric chain is
given its own chain-rectangle connector.  The chain-rectangle gadget itself
is shortest for its assigned rectangle when the local minimum is required.
Indeed, for every positive first-chain level `i`, a witness for `(i,0)` must
contain an entry whose first coordinate is exactly `i` and whose second
coordinate is zero; these force `L_j` distinct entries.  The targets `(0,k)`
similarly force `c` further distinct entries, and the local-minimum target
forces one entry equal to `(0,0)`.  Hence `L_j+c+1` entries are necessary and
the connector attains the bound.

Hence an improvement within this architecture can come only from sharing
positions across different `C_j` rectangles, precisely the operation not
performed by slicing or by Lemma 2.

## 7. Equal-box calculation

Put `h=a=b=c=m`.  Then

\[
 \begin{aligned}
 |P|&=(m+1)^3=m^3+O(m^2),\\
 r&=(m+1)^2-\Psi(m)={3\over4}m^2+O(m).
 \end{aligned}
\]

Therefore the fused word has length

\[
                         |P|+mr-1
 ={7\over4}m^3+O(m^2).                             \tag{7.1}
\]

The four-box width is the central coefficient of
`(1+x+...+x^m)^4`:

\[
 w_4(m,m,m,m)
 =\binom{2m+3}{3}-4\binom{m+2}{3}
 ={2\over3}m^3+O(m^2).                             \tag{7.2}
\]

Thus the connector excess is

\[
                 \left({7\over4}-{2\over3}\right)m^3+O(m^2)
 ={13\over12}m^3+O(m^2),                           \tag{7.3}
\]

confirming (1.8).  The fusion improves a leading constant but not the
critical exponent.

## 8. Why the polynomial thin regime does not enlarge

Let

\[
                         P_2=(h+1)(a+1).
\]

Since `0<=d<=h`,

\[
 \Psi(d)\le{(d+1)^2\over4}
 \le{(h+1)^2\over4}
 \le{P_2\over4}.                                  \tag{8.1}
\]

Consequently

\[
                  {3\over4}P_2\le w_3(h,a,b)\le P_2. \tag{8.2}
\]

Also `S/4<=c<=S`, where `S=h+a+b+c`.  Hence

\[
                    c\,w_3(h,a,b)=\Theta(SP_2)     \tag{8.3}
\]

uniformly up to absolute constants.  The fused direct word is therefore
`O(S^(3-delta))` only in the same polynomial regime

\[
                         P_2=O(S^{2-\delta})        \tag{8.4}
\]

already isolated by the sorted slice theorem, apart from constant-factor
boundary choices.  The fusion does not enlarge the exponent-defined thin
sector.

This conclusion concerns the proved constructor, not the unknown optimum
`g_4`.  A different architecture may of course be subcritical in the thick
sector.

## 9. Precise next constructive target

The exact excess formula (6.3) identifies what must be fused next.  A useful
lemma cannot merely share fourth-coordinate levels along one small-box
chain; that sharing is already complete in Lemma 2.  It must take a family
of neighbouring symmetric chains `C_j` and replace their separately
concatenated rectangle words by one word whose excess is subadditive across
the family.

One concrete target is:

> **Cross-chain connector lemma.**  For the explicit nested-hook SCD of
> `[0,h]x[0,a]x[0,b]`, group chains in packets and cover the union of each
> packet times `[0,c]` with total excess
> `o(sum_(j in packet) max(c,L_j))`, while preserving witnesses internal to
> the packet word.

A uniform power saving in the sum over packets would give the missing
`O(S^(3-delta))` error.  The portal/endpoint conflict is that different
chains have different local minima: a connector marker usable for one chain
can contaminate targets in another.  Any successful fusion must organize
those minima into a monotone two-sided schedule rather than merely
concatenate them.

## 10. Final status

Proved:

* the generic bottom two-slice lift `g(P x [0,1])<=2g(P)`;
* the SCD connector length `|P|+c*w(P)-1`;
* the exact three-short-side width formula (4.5);
* the fused four-box bound (1.3), saving `c*Psi((h+a-b)_+)`;
* the exact independent-chain excess (1.7); and
* the equal-box leading constants `7/4` for length and `13/12` for excess.

Open:

* any cross-chain connector with a polynomial saving;
* the thick-sector local estimate `w_4+O(S^(3-delta))`; and
* the global constant-one theorem depending on it.
