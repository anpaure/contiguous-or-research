# Gate C: unequal odd blocks and the exact weighted-excursion loss

**Status (2026-08-22).** Every assertion below is proved.  The equal-block
row formula extends exactly to arbitrary labelled odd block lengths.  The
unweighted ballot failure count is replaced by two weighted excursion
depths.  For a block of length `ell_i`, the exact number of interior rows
whose undeleted walk is nonpositive is

\[
 \boxed{B_i=\min\{\ell_i-1,\ \lambda_i+(\upsilon_i-2)_+\}.}       \tag{0.1}
\]

Every such row loses all `b-1` factor flags.  Conversely at least
`[ell_i-lambda_i-upsilon_i-3]_+` rows retain exactly `b-2` flags.  Hence

\[
 q-M\le b+(b-2)\sum_i(\lambda_i+\upsilon_i+3).          \tag{0.2}
\]

This identifies the genuine unequal-block escape from the equal-block
pivot no-go: long root blocks can buffer non-ballot weighted excursions.
It does not prove that the resulting high-overlap supports are sufficiently
diverse or packable.

## 1. Unequal block shuffle

Let

\[
 b\ge5\text{ be odd},\qquad K\ge3\text{ be odd},\qquad
 \ell_0,...,\ell_{K-1}\text{ be positive odd integers},
 \qquad\sum_i\ell_i=b.                                  \tag{1.1}
\]

Partition the domain circle `Z_b`, in label order, into consecutive blocks

\[
 D_i=\{d_i,...,d_i+\ell_i-1\},\qquad
 d_i=\sum_{j<i}\ell_j.                                  \tag{1.2}
\]

Let `rho` be a permutation of the block labels, interpreted as target rank:
block `i` occupies target rank `rho(i)`.  If

\[
 j_u=\rho^{-1}(u),\qquad
 t_{j_u}=\sum_{v<u}\ell_{j_v},                           \tag{1.3}
\]

define the increasing block map

\[
 \alpha(d_i+s)=t_i+s\pmod b,qquad0\le s<\ell_i.         \tag{1.4}
\]

Choose the corrected antipodal lift

\[
 \epsilon_x=\alpha(x)+x\pmod2,qquad
 \pi(x)=\alpha(x)+b\epsilon_x,qquad
 \pi(x+b)=\pi(x)+b\pmod {2b}.                           \tag{1.5}
\]

For a residue row `r`, its undeleted `(b+1)`-set is

\[
                         S_r=\{\pi(r),...,\pi(r+b)\}.    \tag{1.6}
\]

Rotate the coordinate membership word of `S_r` to start at `pi(r)`, writing
`+` for membership and `-` for nonmembership.  Deleting one of the `b-1`
internal selected coordinates gives a factor flag exactly when the
resulting balanced word is primitive Dyck, meaning that every proper
nonempty prefix has positive height.

## 2. Exact weighted row word

Fix block `i`.  In target order after it, write

\[
 i_u=\rho^{-1}(\rho(i)+u),\qquad1\le u<K,               \tag{2.1}
\]

with ranks reduced modulo `K`, and put

\[
 w_i(u)=(-1)^{u+((i_u-i)\bmod K)}.                       \tag{2.2}
\]

Thus `w_i(u)=+1` exactly when the target-rank distance and domain-label
distance have the same parity.

### Theorem 2.1 (unequal-block row word)

For the interior row

\[
                         r=d_i+s,qquad1\le s<\ell_i,    \tag{2.3}
\]

the rotated length-`2b` word is

\[
\boxed{
 +^{\ell_i-s},\quad
 w_i(1)^{\ell_{i_1}},...,w_i(K-1)^{\ell_{i_{K-1}}},\quad
 +^{s+1},-^{\ell_i-s-1},\quad
 (-w_i(1))^{\ell_{i_1}},...,(-w_i(K-1))^{\ell_{i_{K-1}}},\quad
 -^s.}                                                   \tag{2.4}
\]

#### Proof

Inside a domain block, both `alpha(x)` and `x` increase by one, so
`epsilon_x` is constant and `pi(r)=pi(r-1)+1`.  The domain interval
`r,...,r+b` takes the suffix of block `i`, every other domain block, and
the antipodal prefix of block `i`.  Under (1.4), a full domain block maps
increasingly to its target interval and therefore contributes a constant
membership sign repeated for its own length.

The clockwise distance between the starts of domain blocks `i` and `j`
has parity equal to `(j-i) mod K`, because every crossed block length is
odd.  The corresponding target-start distance has parity equal to the
number of crossed target blocks, again because all lengths are odd.  Hence
the selected lift of target block `i_u` agrees with the root lift exactly
when the two parities in (2.2) agree.  Its antipodal copy has the opposite
sign.  The two partial copies of the root block give the four displayed
root runs. \(\square\)

## 3. Exact killed-row formula

Define weighted prefixes

\[
 P_i(0)=0,\qquad
 P_i(m)=\sum_{u=1}^m\ell_{i_u}w_i(u),\qquad
 A_i=P_i(K-1),                                        \tag{3.1}
\]

and the two excursion depths

\[
 \lambda_i=-\min_{0\le m<K}P_i(m),\qquad
 \upsilon_i=\max_{0\le m<K}\{P_i(m)-A_i\}.            \tag{3.2}
\]

Both are nonnegative because `P_i(0)=0` and `P_i(K-1)=A_i`.

### Lemma 3.1 (two boundary minima)

For row offset `s`, the minimum height through the first family of full
target-block runs is

\[
                         \ell_i-s-\lambda_i,            \tag{3.3}
\]

and the minimum from the central root block through the complementary full
runs is

\[
                         s+2-\upsilon_i.                \tag{3.4}
\]

All other proper prefixes have positive height whenever both displayed
quantities are positive.

#### Proof

After the initial root suffix and the first `m` full target blocks, (2.4)
has height

\[
                         \ell_i-s+P_i(m).               \tag{3.5}
\]

After the central two root runs and the first `m` complementary blocks,
its height is

\[
                         A_i-P_i(m)+s+2.                \tag{3.6}
\]

Inside a constant-sign run its minimum occurs at an endpoint.  The initial
run rises from one; the central positive run rises; the following negative
root run ends at the `m=0` value of (3.6); and the final run descends from
`s+2` to terminal height two, with final proper-prefix height three.
Taking the two extrema in (3.2) proves the claim. \(\square\)

### Theorem 3.2 (exact number of killed rows)

The undeleted word of row `s` is positive at every proper nonempty prefix
if and only if

\[
 \max\{1,\upsilon_i-1\}\le s\le\ell_i-\lambda_i-1.      \tag{3.7}
\]

Consequently the exact number of nonpositive interior rows of block `i` is

\[
 \boxed{
 B_i=(\ell_i-1)-
 [\ell_i-\lambda_i-\max\{1,\upsilon_i-1\}]_+
 =\min\{\ell_i-1,\lambda_i+(\upsilon_i-2)_+\}.}         \tag{3.8}
\]

Every one of these rows contains zero factor flags.

#### Proof

Strict positivity of (3.3) is equivalent to
`s<=ell_i-lambda_i-1`; strict positivity of (3.4) is equivalent to
`s>=upsilon_i-1`.  Intersecting with `1<=s<ell_i` proves (3.7) and the
first expression in (3.8).  The second is the same integer identity,
separating whether the interval in (3.7) is empty.

If an undeleted word has a nonpositive proper prefix, deleting a selected
step after that prefix leaves it unchanged, while deleting an earlier plus
lowers it by two.  No deletion can therefore produce a primitive Dyck word.
\(\square\)

## 4. Deep rows and the two-sided phase loss

Call an interior row *deep* when

\[
                 \upsilon_i+1\le s\le\ell_i-\lambda_i-3.           \tag{4.1}
\]

### Lemma 4.1 (deep rows retain `b-2` flags)

Every deep row has undeleted height at least three after prefix length two
and before the terminal two steps.  Its last proper prefix of height at most
two is exactly prefix length two, and precisely `b-2` of its `b-1`
internal deletions are primitive Dyck.

#### Proof

Condition (4.1) strengthens (3.3)--(3.4) to a lower bound of three.  It also
makes the initial positive run have length at least three.  The endpoint
argument of Lemma 3.1 then shows that every prefix after the first two and
before the terminal endpoint has height at least three.

Deleting a plus at a given step preserves earlier heights and lowers every
subsequent height by two.  Hence, for a positive height-two undeleted word,
an allowed deletion is primitive exactly when it occurs after the last
proper prefix of height at most two.  In the internal deletion deck, one
selected coordinate occurs before that cut and the other `b-2` occur after
it. \(\square\)

Let `M` be the number of internal flags of this coherent phase which lie in
the Catalan-switched factor, and put

\[
                              q=b(b-1).                 \tag{4.2}
\]

### Theorem 4.2 (two-sided loss ledgers)

One has the lower loss bound

\[
 \boxed{q-M\ge(b-1)\sum_i B_i.}                        \tag{4.3}
\]

and the constructive upper loss bound

\[
 \boxed{
 M\ge(b-2)\sum_i[\ell_i-\lambda_i-\upsilon_i-3]_+,
 \qquad
 q-M\le b+(b-2)\sum_i(\lambda_i+\upsilon_i+3).}        \tag{4.4}
\]

#### Proof

Each killed row has all `b-1` internal flags absent, proving (4.3).  The
number of deep rows in block `i` is exactly the positive part in (4.4), and
Lemma 4.1 proves the first lower bound on `M`.  Finally `[x]_+>=x` gives

\[
 \sum_i[\ell_i-\lambda_i-\upsilon_i-3]_+
 \ge b-\sum_i(\lambda_i+\upsilon_i+3).                 \tag{4.5}
\]

Subtract `(b-2)` times (4.5) from `q=b(b-1)` to obtain the second bound.
\(\square\)

Thus

\[
             K+\sum_i(\lambda_i+\upsilon_i)=o(b)       \tag{4.6}
\]

is a sufficient coefficient-one overlap criterion.  Conversely
`q-M=o(q)` forces

\[
 \sum_i\min\{\ell_i-1,\lambda_i+(\upsilon_i-2)_+\}=o(b).           \tag{4.7}
\]

Unlike equal blocks, (4.7) allows arbitrarily many badly ordered blocks if
their total row mass is `o(b)`.  Determining whether such buffered orders
can be macroscopically diverse and rankwise packed is the next Gate-C
question.

The companion checker
`scratch/verify_gate_c_unequal_odd_block_weighted_excursion_20260822.py`
constructs the signed coordinate lift directly, verifies (2.4) symbol by
symbol, exhausts every small odd composition/order in its stated range,
checks (3.8) against actual prefix heights, and verifies the exact deletion
decks and both loss ledgers.
