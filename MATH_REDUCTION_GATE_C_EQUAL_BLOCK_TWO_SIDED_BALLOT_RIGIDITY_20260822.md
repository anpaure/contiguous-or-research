# Gate C: equal-block shuffles reduce to almost-everywhere two-sided ballot cuts

**Status (2026-08-22).**  Every assertion below is proved.  For an exact
equal-block antipodal shuffle, the undeleted coherent row walk has a closed
block formula.  Each block cut induces a sign walk `W_i`; unless every
prefix lies between zero and its terminal height, at least `ell-2` interior
rows of that block contain no factor flag at all.

Consequently a phase with loss `O(bK)` can have only `O(K^2/b)` bad block
cuts.  At the entropy threshold `K=Theta(b/log b)`, all but
`O(b/log^2 b)` of the `K` cyclic cuts must pass the same two-sided ballot
test.  This is a strict reduction of the live block-order count, not yet
that count itself.

Throughout,
\[
 b=K\ell,\qquad K,\ell\ge3\text{ odd},\qquad q=b(b-1). \tag{0.1}
\]

## 1. Equal blocks and the signed antipodal lift

Partition the residue cycle `Z_b` into the consecutive blocks
\[
 B_i=\{i\ell,i\ell+1,\ldots,i\ell+\ell-1\},
 \qquad i\in\mathbb Z_K.                               \tag{1.1}
\]
For a cyclic block order `tau in S_K`, define
\[
 \alpha(i\ell+s)=\tau_i\ell+s
 \quad(0\le s<\ell).                                   \tag{1.2}
\]
Choose the unique sign word with corrected parity identically zero:
\[
 \epsilon_x=\alpha(x)+x\pmod2,
 \qquad
 \pi(x)=\alpha(x)+b\epsilon_x,
 \qquad \pi(x+b)=\pi(x)+b\pmod {2b}.                 \tag{1.3}
\]
Because `b` is odd, this indeed makes
`alpha(x)+epsilon_x+x=0 mod 2`.  On block `i`, (1.3) becomes
\[
 \pi(i\ell+s)=
 \bigl(\tau_i+K(\tau_i+i\bmod2)\bigr)\ell+s.          \tag{1.4}
\]
Thus an entire domain block maps increasingly onto one of the two lifts
of value block `tau_i`.

We use only the following exact property of the Catalan-switched central
factor `F*`.  If a central flag has predecessor arc `p->p-1`, then it lies
in `F*` exactly when its middle membership word, rotated to start at `p`,
is primitive Dyck.  Indeed the ordered Greene--Kleitman flag is obtained
by rotating at its leftmost unpaired one and returning first at its
rightmost unpaired zero.  The sole wrap arc `(2b-1)->0` is removed by the
Catalan diamond switches, and exactly the primitive wrap arc
`0->(2b-1)` is inserted.  These are precisely the cyclic predecessor
cases.

## 2. The block sign word

Fix a domain block `i`.  For `1<=u<K`, let
\[
 a_i(u)=
 \tau^{-1}(\tau_i+u)-i\pmod K,
 \qquad 1\le a_i(u)<K,                                 \tag{2.1}
\]
where every block subscript and every argument of `tau` is read modulo
`K`, and the second line chooses the displayed representative.
and define
\[
 w_i(u)=
 \begin{cases}
 +1,&a_i(u)\equiv u\pmod2,\\
 -1,&a_i(u)\not\equiv u\pmod2.
 \end{cases}                                           \tag{2.2}
\]
Put
\[
 W_i(m)=\sum_{u=1}^m w_i(u),\qquad
 A_i=W_i(K-1).                                         \tag{2.3}
\]

Consider an interior residue row
\[
 r=i\ell+s,\qquad1\le s<\ell.                          \tag{2.4}
\]
Its predecessor lies in the same block, so (1.2)--(1.3) give
`pi(r)=pi(r-1)+1`.  Let
\[
 S_r=\{\pi(r+v):0\le v\le b\}.                        \tag{2.5}
\]
Rotate coordinates at `pi(r)` and encode membership in `S_r` by `+` and
nonmembership by `-`.

### Lemma 2.1 (exact row word)

The length-`2b` rotated word is the following concatenation:
\[
 \boxed{
 +^{\ell-s},\quad
 w_i(1)^\ell,\ldots,w_i(K-1)^\ell,\quad
 +^{s+1},-^{\ell-s-1},\quad
 (-w_i(1))^\ell,\ldots,(-w_i(K-1))^\ell,\quad
 -^s.}                                                  \tag{2.6}
\]
Here `(+1)^ell` means `ell` plus signs and `(-1)^ell` means `ell`
minus signs.

#### Proof

The interval `r+[0,b]` first takes the suffix of domain block `i`, then
one full copy of every other domain block in cyclic order, and finally the
prefix through position `s` of the antipodal copy of block `i`.  Formula
(1.4) preserves the within-block coordinate `s`.

Relative to the image of block `i`, value block `tau_i+u` is encountered
in coordinate block `u` or its antipode `u+K`.  The selected lift is `u`
exactly when the cyclic domain distance `a_i(u)` and the cyclic value
distance `u` have the same parity, which is (2.2).  The other lift has the
opposite sign.  The two partial copies of the distinguished block give
the first, middle, and last runs in (2.6). \(\square\)

## 3. Exact positivity and a quantitative bad-cut loss

Call block cut `i` *two-sided ballot* when
\[
                 0\le W_i(m)\le A_i
                 \qquad(1\le m<K).                    \tag{3.1}
\]

### Lemma 3.1 (positivity dichotomy)

For every `1<=s<ell`:

1. if (3.1) holds, the undeleted row word (2.6) has positive height at
   every proper nonempty prefix;
2. if `W_i(m)<0` for some `m`, the undeleted word is nonpositive at a
   proper prefix for every `s`;
3. if `W_i(m)>A_i` for some `m`, it is nonpositive at a proper prefix for
   every `1<=s<=ell-2`.

#### Proof

After the first partial run and the first `m` full blocks, the height is
\[
                         \ell-s+\ell W_i(m).             \tag{3.2}
\]
After the central block and the first `m` complementary blocks, it is
\[
                         \ell(A_i-W_i(m))+s+2.           \tag{3.3}
\]
Within a constant-sign block the minimum is at one of its endpoints.
The initial run is positive; the central block has endpoint heights
`ell-s+ell A_i` and `ell A_i+s+2`; and the final run descends from `s+2`
to the terminal height two.  Equations (3.2)--(3.3) therefore prove item
1.  If some `W_i(m)<=-1`, (3.2) is at most `-s`, proving item 2.  If some
`W_i(m)>=A_i+1`, (3.3) is at most `s+2-ell`, which is nonpositive for
`s<=ell-2`, proving item 3. \(\square\)

If the undeleted walk has a nonpositive proper prefix, deleting any one of
its plus steps cannot make it primitive: a deletion after that prefix
leaves the bad height unchanged, while an earlier deletion lowers it by
two.  Hence every row covered by items 2--3 contains zero factor flags.

### Theorem 3.2 (bad-cut loss)

Let `R(tau)` be the number of block cuts which fail (3.1), and let a
coherent phase of `pi(H*)` meet `F*` in `M` internal flags.  Then
\[
 \boxed{
 q-M\ge R(\tau)(\ell-2)(b-1).}                         \tag{3.4}
\]
Consequently, if `q-M<=C bK`,
\[
 R(\tau)\le
 {C bK\over(\ell-2)(b-1)}.                             \tag{3.5}
\]

#### Proof

Every failed cut supplies, by Lemma 3.1, at least `ell-2` distinct
interior residue rows whose undeleted walk is nonpositive.  Each such row
has all `b-1` columns absent from the factor.  Different block cuts have
disjoint interior rows.  Each phase visits every residue row once, and
antipodal translation preserves the relative word.  Summing these row
deficits proves (3.4), and (3.5) follows. \(\square\)

If `ell=b/K` tends to infinity, (3.5) is
\[
                         R(\tau)=O(K^2/b).               \tag{3.6}
\]
In particular, for `K=Theta(b/log b)`,
\[
                         R(\tau)=O(b/\log^2 b)=o(K).     \tag{3.7}
\]

The same block formula gives the converse estimate needed by the
construction.

### Theorem 3.3 (almost-everywhere ballot is sufficient)

If exactly `R` block cuts fail (3.1), then either coherent phase retains
at least
\[
                         (K-R)(\ell-3)(b-2)             \tag{3.8}
\]
factor flags.  Equivalently, its loss is at most
\[
 q-M\le b+(R\ell+3K-3R)(b-2).                          \tag{3.9}
\]
In particular, `R=O(K^2/b)` implies `q-M=O(bK)`.

#### Proof

Fix a two-sided-ballot cut and an interior offset
`1<=s<=ell-3`.  Lemma 3.1 makes its undeleted walk positive.  More
precisely, after prefix length two every height is at least three: this is
clear in the initial run of length `ell-s>=3`; (3.2) is at least
`ell-s`; (3.3) is at least `s+2`; and the final proper prefix has height
three.  Thus the last proper prefix of undeleted height at most two is
exactly time two.

The allowed deletion deck has size `b-1`.  It contains the unique selected
coordinate at relative offset one, while every other allowed deletion has
offset at least two.  The exact deletion criterion therefore accepts
exactly `b-2` columns in this row.  Keeping only these `ell-3` rows for
each of the `K-R` ballot cuts proves (3.8).  Since `b=Kell`, subtracting
(3.8) from `q=b(b-1)` gives the equality on the right of (3.9), and the
last claim follows. \(\square\)

## 4. The exact remaining block-order count

Let
\[
 \mathcal B_{K,R}=\{\tau\in S_K:
   \text{at most }R\text{ cyclic cuts fail (3.1)}\}.   \tag{4.1}
\]
The equal-block multiplicity route is now reduced, in both directions, to counting and
incidence-auditing `B_(K,R)` for
\[
 K=\Theta(b/\log b),\qquad R=O(b/\log^2 b).             \tag{4.2}
\]
An upper bound `log|B_(K,R)|=o(b)` would rule out this route.  A large,
macroscopically diverse subfamily of size at least `4^b/poly(b)`, together
with rankwise codegrees permitting a matching, would instead advance the
construction.  Neither conclusion is asserted here.

## 5. Finite audit

The companion checker
`scratch/verify_gate_c_equal_block_two_sided_ballot_rigidity_20260822.py`
exhausts small odd block orders, verifies (2.6) symbol by symbol against
the signed coordinate permutation, verifies the positivity trichotomy,
and checks (3.4) from exact deletion decks.  It is confirmatory; all
general proofs are above.
