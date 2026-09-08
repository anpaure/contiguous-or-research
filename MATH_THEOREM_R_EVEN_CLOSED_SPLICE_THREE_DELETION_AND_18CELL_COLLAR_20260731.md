# Even closed splices, three-deletion compression, and the exact collar gate

Date: 2026-07-31  
Lane: R, pure mathematics  
Status: unconditional splice recurrence; conditional equality-length collar
theorem; sharp fixed-anchor and fixed-fibre obstructions.  No new value of
`nu(k)` is claimed.

## 0. Result

Let `X=(x_0,...,x_(n-1))` be a nonempty-set word on a ground set `V`, and
let `z` be a fresh coordinate.  Define

\[
 S_z(X)=X\cdot[\{z\}]\cdot
       (\{z\}\cup x_0,\ldots,\{z\}\cup x_{n-2}).       \tag{0.1}
\]

The closed splice has an exact, parity-free characterization:

\[
 \boxed{S_z(X)\text{ is universal on }V\cup\{z\}
        \iff X\text{ is universal on }V.}             \tag{0.2}
\]

It follows that, for `k>=2`,

\[
                         \nu(k)\le2\nu(k-1).           \tag{0.3}
\]

Evenness enters only in the length comparison.  If `k=2r`, an optimal odd
parent has length `B(k-1)`, and `w(k)=binom(k,ceil(k/2))`, then

\[
 |S_z(X)|=B(k)+2d(k-1)-d(k).                          \tag{0.4}
\]

Thus on the local plateau

\[
                         d(k-1)=d(k)=3                \tag{0.5}
\]

the closed splice has length `B(k)+3=2|X|`; equality requires a genuine
three-unit compression.  Condition (0.5) is essential: `d(k)` is unbounded,
so the construction is not a constant-additive recurrence for all even `k`.

There are two mathematically different compression mechanisms.

1. **Literal deletion from the closed splice.**  For an optimal parent, all
   three deleted cells would have to lie in the uniformly tagged copy.
   A four-disjoint-witness tail condition is sufficient in abstract words.
   However, a sharp rank-antichain theorem shows that this architecture,
   when its old seam anchor has middle rank, cannot attain `B(16)`: it has
   length at least `B(16)+1`.  The authenticated canonical orientation has
   such an anchor.  An equality construction from that orientation must move
   or absorb the singleton, change the old shore, or use mixed-tag collar
   cells; rotations with a lower-rank anchor are not excluded.
2. **Twenty-one-out/eighteen-in collar replacement.**  Crop twenty-one cells
   from the two parent bodies and the bare-singleton seam, then insert
   eighteen arbitrary nonzero cells in three windows.  This has net saving
   three.  For any fixed seeds and crop, Theorem 5.2 below gives an exact
   necessary-and-sufficient seed condition: choose one physical host per
   fixed-body residual target so that every common cell core is nonempty and
   every demanded coordinate survives in at least one core.  The cores
   themselves are the constructive collar values.

Raw or marginal tail-witness counts and a repeat-free width-three deck are
useful screens, not substitutes for that condition.  The strong disjoint-
witness packing inequality (5.18) is genuinely sufficient.  By contrast,
the authenticated seed-5/self RF495 `4/9/5` fibre is a sharp fixed-fibre
counterexample to sufficiency of repeat-freeness plus the numerical deck
schedule: it has a repeat-free retained deck and the exact
`21`-missing/`23`-boundary schedule,
but its twenty-one residual rank-eight targets see only twenty nested
oriented anchors.  The solver-free inequality `21>20` excludes the entire
fixed fibre.  A second obstruction closes two superficially stronger fibres:
the V/V `4/9/5` one-hole control and delete-p1 `collar594` each retain two
immutable first-middle deliveries of `0xc279` at distinct deadlines.  Every
universal equality-length K16 word is ghost-free, so neither fixed fibre can
complete.  A successful collar must edit at least one carried-shadow
occurrence or use a different crop.

## 1. Notation

For a word `P=(p_0,...,p_(L-1))`, write

\[
 \operatorname{Cov}(P)
 =\left\{\bigcup_{i=a}^{b}p_i:0\le a\le b<L\right\}. \tag{1.1}
\]

All word letters are nonempty.  The OR symbol `|` in code is pointwise set
union.  Prefix and suffix OR families include the empty prefix and suffix,
whose OR is empty:

\[
 \operatorname{Pref}(P),\qquad \operatorname{Suff}(P). 
\]

For `q>=0`, the linear adjacent-OR derivative is

\[
 (D^qP)_i=\bigcup_{j=0}^{q}p_{i+j}.                  \tag{1.2}
\]

Put

\[
 w(k)=\binom{k}{\lceil k/2\rceil},
 \qquad B(k)=w(k)+d(k).                              \tag{1.3}
\]

Only the already-proved monotone-deadline lower bound `nu(k)>=B(k)` is used.

## 2. The exact closed-splice theorem

### Theorem 2.1 (one-parent closed splice)

Let `V` be nonempty and let `z` be fresh.  The word (0.1) is universal on
`V union {z}` if and only if `X` is universal on `V`.  Its length is `2n`.

#### Proof

Every interval of `S_z(X)` whose union omits `z` lies wholly in the initial
copy `X`.  Thus universality of the splice implies universality of `X`.

Conversely, let `M` be a nonempty old target and choose one `X`-witness
`[a,c]`.

- The same interval in the first block realizes `M`.
- If `c<n-1`, the corresponding interval in the tagged block realizes
  `M union {z}`.
- If `c=n-1`, the interval `x_a,...,x_(n-1),{z}` realizes
  `M union {z}`.
- The central singleton realizes `{z}`.

These are every nonempty target on `V union {z}`.  The length is
`n+1+(n-1)=2n`.  \(\square\)

The omission of `x_(n-1)` from the tagged copy is load-bearing: it is the
letter adjacent to the bare singleton.  An arbitrary internal omission is
not covered by this proof.

### Theorem 2.2 (arbitrary right-tail correction)

Let `C` be any (possibly empty) old-coordinate word and put

\[
 S_z(X;C)=X\cdot[\{z\}]\cdot(\{z\}\cup C).        \tag{2.1}
\]

Then `S_z(X;C)` is universal if and only if `X` is universal and, for every
nonempty old target `M`, at least one of the following holds:

\[
 M\in\operatorname{Cov}(C),                        \tag{2.2}
\]

or

\[
 M=s\cup p
 \quad\text{for some }s\in\operatorname{Suff}(X),\quad
 p\in\operatorname{Pref}(C).                       \tag{2.3}
\]

#### Proof

Unmarked targets can occur only in `X`.  A marked target other than `{z}`
is realized either wholly in the tagged block, giving (2.2), or by an
interval crossing the central singleton, whose old projection is exactly a
suffix OR of `X` joined to a prefix OR of `C`.  These two interval
classes are exhaustive and also prove sufficiency.  \(\square\)

Universality of both parents alone is not enough.  On the two-coordinate old
ground, take

```text
X=(1,2),   Y=(2,1),   z=4.
```

Both parents are universal, but taking `C=Y[:-1]=(2)` gives
`S_z(X;C)=(1,2,4,6)`, which misses `5`.  Therefore
every mixed K15 parent-pair splice requires an actual tail/seam compatibility
certificate; the self-splice is the unconditional case.

## 3. Exact derivative and length recurrences

### Theorem 3.1 (linear derivative recurrence)

For `0<=q<=n-1`,

\[
 D^qS_z(X)
 =D^qX\cdot\Gamma_q(X,z)\cdot
       \bigl(\{z\}\cup(D^qX)[:-1]\bigr),           \tag{3.1}
\]

where `Gamma_q` has `q+1` entries

\[
 \Gamma_q[h]
 =\{z\}\cup
   \bigcup X[n-q+h:n]\cup\bigcup X[0:h],
 \qquad 0\le h\le q.                               \tag{3.2}
\]

In particular, `|D^qS_z(X)|=2n-q`.

We use the convention that a derivative whose order is at least the length
of its input is the empty word.  This applies to the final block when
`q=n-1`.

#### Proof

A `(q+1)`-cell window lies wholly in the left copy, crosses the central
singleton, or lies wholly in the tagged copy.  The first class is `D^qX`.
The `q+1` crossing starts contain `q-h` final letters of `X`, the singleton,
and `h` initial tagged letters, giving (3.2).  Removing their common tag from
the final class gives `D^qX` with its last entry omitted.  These classes are
disjoint and exhaustive.  \(\square\)

For mixed parents, replace the initial prefix of `X` in (3.2) by the initial
prefix of `Y`, and replace the last block by
`{z} union (D^qY)[:-1]`.  This is a linear identity; cyclic differentiation
would require an additional wrap term.

### Corollary 3.2 (conditional even recurrence)

For every `k>=2`,

\[
                         \nu(k)\le2\nu(k-1).         \tag{3.3}
\]

If `k=2r` and an actual parent word of length `B(k-1)` exists, then

\[
 |S_z(X)|
 =B(k)+2d(k-1)-d(k).                                \tag{3.4}
\]

#### Proof

Theorem 2.1 gives (3.3).  For even `k`, Pascal's identity gives

\[
 w(k)=\binom{2r}{r}
     =2\binom{2r-1}{r}=2w(k-1).                    \tag{3.5}
\]

Substitution into `2B(k-1)` proves (3.4).  \(\square\)

Equation (3.4) requires the actual optimal parent.  It does not follow from
a conditional odd-carrier programme, and the claim `d(k)=3` for all even
`k>=16` is false.  On the plateau (0.5), (3.4) is `B(k)+3`; outside it the
additive term is exactly `2d(k-1)-d(k)`.

## 4. Direct deletion: a positive tail lemma and a sharp no-go

Let `X` be an optimal parent of length `n=nu(k-1)`.  Consider a subsequence
obtained by deleting three cells from `S_z(X)`.

### Lemma 4.1 (where three literal deletions must occur)

If the shortened word is universal, all `n` cells of the initial `X` and the
bare singleton `{z}` remain.  Hence all three deletions occur in the tagged
copy.

#### Proof

Every unmarked interval is wholly inside the surviving initial-copy cells.
Deleting one of them would produce a universal old word of length below
`nu(k-1)`, impossible.  Deleting the bare singleton loses `{z}`, because
every tagged-copy letter also contains a nonempty old letter.  \(\square\)

Let `D subseteq {0,...,n-2}` have size three and let `Y_D` be `X[:-1]` with
those positions deleted, in its inherited order.

### Theorem 4.2 (exact direct-deletion criterion)

The word

\[
 X\cdot[\{z\}]\cdot(\{z\}\cup Y_D)                 \tag{4.1}
\]

is universal if and only if every nonempty old target belongs to

\[
 \operatorname{Cov}(Y_D)\ \cup\
 \bigl(\operatorname{Suff}(X)\vee
       \operatorname{Pref}(Y_D)\bigr).             \tag{4.2}
\]

This is Theorem 2.2 specialized to a deleted self-splice.  It includes new
gap-fusion witnesses and is therefore sharper than merely asking that old
tagged witnesses survive.

For a target `M`, let `W_X^-(M)` be its interval-witness family in `X[:-1]`,
and let `tau_X^-(M)` be the minimum number of positions meeting every member
of that family.  For interval families on a line, greedy selection by the
earliest right endpoint proves

\[
 \tau_X^-(M)=\rho_X^-(M),                            \tag{4.3}
\]

where `rho` is the maximum number of pairwise position-disjoint witnesses.

### Corollary 4.3 (three-robust tail)

Suppose every nonempty target `M` which has no suffix witness ending at
`x_(n-1)` satisfies

\[
                         \rho_X^-(M)\ge4.            \tag{4.4}
\]

Then deleting any three tagged-copy positions leaves a universal word of
length `2n-3`.

#### Proof

Three deleted positions cannot meet all four disjoint witnesses, so one
tagged witness remains.  A target with a terminal suffix witness is realized
by that suffix followed by the bare singleton.  Theorem 4.2 finishes the
proof.  \(\square\)

Here a terminal suffix witness means an interval `[a,n-1]` in `X` whose OR
is `M`.  Raw witness count cannot replace (4.4).  In the word
`(a,a,a,a,b)`, the target `{a,b}` has four nested witnesses ending at the
last cell, all hit by that one position.  The relevant invariant is the
transversal/disjoint-packing number, not the number of intervals.

The robust-tail lemma is genuinely conditional.  In the authenticated
canonical K15 orientation it is blocked by the following antichain theorem;
the theorem itself states its seam-anchor hypothesis explicitly.

### Lemma 4.4 (rank-`r` interval saturation)

For a word `C=(c_1,...,c_m)` of arbitrary subsets of a `p`-point ground,

\[
 \left|\operatorname{Cov}(C)\cap\binom{[p]}r\right|\le m.             \tag{4.5}
\]

If equality holds, the letters `c_i` are pairwise distinct rank-`r` sets and
these singleton intervals are all rank-`r` interval unions.

#### Proof

For each fixed left endpoint, the interval unions form an inclusion chain,
so they contain at most one distinct rank-`r` set.  This proves the bound.
If equality holds, every start supplies a new rank-`r` set.  Working backward,
the last letter must itself have rank `r`.  If `c_(i+1)` is already a
rank-`r` singleton, an interval from `i` extending past it either repeats
that already-counted set or has rank above `r`; hence the new set at start
`i` must be the singleton `c_i`.  Backward induction proves the claim.
Distinct rank-`r` letters have union rank above `r`, so no longer interval
adds another rank-`r` value.  \(\square\)

### Theorem 4.5 (fixed-first-copy tagged-tail obstruction)

Let `A` be any old-coordinate word whose seam-anchor last letter has rank at
least `r>=2`, and let `C=(c_1,...,c_m)` be arbitrary, even allowing empty old
sets.  If

\[
 A\cdot[\{z\}]\cdot
   (\{z\}\cup c_1,\ldots,\{z\}\cup c_m)            \tag{4.6}
\]

is universal, then

\[
                         m\ge\binom{|V|}{r}.         \tag{4.7}
\]

#### Proof

Consider the tagged targets `{z} union R` with `|R|=r`.  Intervals wholly in
the tagged tail supply at most `m` distinct old projections by Lemma 4.4.
Every nonempty seam-crossing old projection contains the anchor.  If the
anchor has rank above `r`, no such projection has rank `r`, so already
`m>=binom(|V|,r)`.  If the anchor has rank `r`, a seam-crossing projection of
rank `r` equals that anchor.  Prefixes beginning at the bare singleton are
already tail intervals.  Thus `m=binom(|V|,r)-1` is the only possible value
below (4.7), and it forces equality in Lemma 4.4.  Every tail letter is then
a rank-`r` set.  No tail, prefix, or seam interval can realize
`{z} union R` with `1<=|R|<r`, contradicting universality.  \(\square\)

For the authenticated canonical K15 orientation, `|V|=15`, `r=7`, the first
copy has length `6438`, and its terminal letter `0x4671` has rank seven.
Therefore every word retaining that first copy, a bare singleton, and a
uniformly tagged tail has length at least

\[
 6438+1+\binom{15}{7}=12874=B(16)+1.                \tag{4.8}
\]

So this architecture can save at most two cells from the length-12876 closed
splice, never the three required for equality.  This does not obstruct a
collar which moves the singleton, changes cells of the old shore, or uses
mixed-tag values.

## 5. The twenty-one-out/eighteen-in collar theorem

Now let `k=2r`, let the old ground have size `k-1`, and assume (0.5).  Put

\[
 w=\binom{k-1}{r},\qquad n=w+3.                     \tag{5.1}
\]

Let `X,Y` be length-`n` parent words.  Choose nonnegative crop parameters
`alpha,beta,gamma,epsilon` with

\[
 \epsilon\ge1,\qquad
 \alpha+\beta\le n,qquad
 \gamma+\epsilon\le n,qquad
 \alpha+\beta+\gamma+\epsilon\ge3,                 \tag{5.1a}
\]

and set

\[
 A=X[\alpha:n-\beta],\qquad
 C=Y[\gamma:n-\epsilon].                            \tag{5.2}
\]

Let `Q_0,Q_1,Q_2` be three words of arbitrary nonempty child masks and put

\[
 \ell=|Q_0|+|Q_1|+|Q_2|
      =\alpha+\beta+\gamma+\epsilon-3.              \tag{5.3}
\]

Define

\[
 Z=Q_0\cdot A\cdot Q_1\cdot(\{z\}\cup C)\cdot Q_2. \tag{5.4}
\]

### Lemma 5.1 (exact compression arithmetic)

The word (5.4) has length

\[
 |Z|=2n-3=2w+3=\binom{k}{r}+3=B(k).                \tag{5.5}
\]

If `X=Y`, this replaces
`alpha+beta+gamma+epsilon` cells of the closed splice—including the removed
bare singleton and the unavailable end of the uniformly tagged copy—by
`ell` collar cells, a net deletion of three.  For `X!=Y`, (5.4) is a
two-parent generalized splice of the same length, not literally a deletion
from one closed word.

#### Proof

The two fixed bodies have total length

\[
 (n-\alpha-\beta)+(n-\gamma-\epsilon).
\]

Adding (5.3) gives `2n-3`.  Pascal's identity and (0.5) give the remaining
equalities.  \(\square\)

For the standard K16 crop,

\[
 (\alpha,\beta,\gamma,\epsilon)=(6,2,7,6),
 \qquad \ell=18.                                    \tag{5.6}
\]

Thus it removes `8` cells from the old copy, the bare singleton, and `12`
cells from the tagged `Y[:-1]` copy, then inserts eighteen cells:

\[
                         2n-21+18=2n-3.             \tag{5.7}
\]

Freeze the two bodies and the three collar locations.  Let `C_fix` be the
set of masks realized by physical intervals avoiding every collar cell, and
let

\[
 \mathcal R=(2^{[k]}\setminus\{\varnothing\})
             \setminus\mathcal C_{\rm fix}.         \tag{5.8}
\]

For `T in R`, a physical host is a pair `(F_T,I_T)`, where `I_T` is the
nonempty set of collar positions used by one literal interval, `F_T` is the
OR of its fixed cells, and `F_T subseteq T`.

### Theorem 5.2 (exact seed-level maximal-core criterion)

The fixed crop has a nonzero collar completion if and only if one can choose
one physical host `(F_T,I_T)` for every `T in R` such that, on defining

\[
 K_p=\bigcap_{T:\ p\in I_T}T                       \tag{5.9}
\]

with an empty-family intersection equal to the full child ground, one has

\[
 K_p\ne\varnothing\quad\text{for every collar cell }p,               \tag{5.10}
\]

and

\[
 F_T\cup\bigcup_{p\in I_T}K_p=T
 \quad\text{for every }T\in\mathcal R.             \tag{5.11}
\]

When these conditions hold, the literal assignment

\[
                         Q_p=K_p                    \tag{5.12}
\]

is a completing collar.

#### Proof

In any realizing collar, a cell used by target `T` is a nonempty subset of
`T`; hence it is a subset of `K_p`.  An unused cell has the full-ground core
by convention.  This proves (5.10) in both cases.  Every coordinate of
`T minus F_T` must occur in at least one used cell, which gives (5.11).

Conversely assign (5.12).  Every used core lies inside `T`, so the selected
interval OR is contained in `T`; its fixed part supplies `F_T`, and (5.11)
supplies every remaining coordinate.  Thus its OR equals `T`.  Unused cells
may take the full child mask and do not enter a selected host.  \(\square\)

This is literal contiguous-OR realizability inside one physical word.  It is
not an independent target-to-host matching and it does not select a different
source for each target.

### Corollary 5.3 (tail multiplicity description)

Assume `Q_1` is nonempty.  For a parent `P`, let

\[
 \mu_P^{u,v}(M)
 =\#\{[i,j]:u\le i\le j<n-v,
              \ \bigcup_{t=i}^{j}P_t=M\}.           \tag{5.13}
\]

Then the fixed-body residual family is exactly

\[
\begin{aligned}
 \mathcal R={}&
 \{M\ne\varnothing:\mu_X^{\alpha,\beta}(M)=0\}\\
 &\mathbin{\dot\cup}\{\{z\}\}\\
 &\mathbin{\dot\cup}
 \{\{z\}\cup M:M\ne\varnothing,
             \mu_Y^{\gamma,\epsilon}(M)=0\}.       \tag{5.14}
\end{aligned}
\]

#### Proof

The nonempty middle collar separates the two fixed bodies, so a collar-free
interval lies wholly in exactly one.  The first body realizes precisely the
old masks with positive first multiplicity.  The tagged body realizes
`{z} union M` precisely when the second multiplicity is positive.  No fixed
letter equals `{z}`.  \(\square\)

For an arbitrary layout, including `Q_1` empty, (5.8) remains authoritative;
fixed cross-body intervals may make (5.14) a strict overcount.

### Lemma 5.4 (disjoint-witness survival)

Let `rho_P(M)` be the maximum number of pairwise position-disjoint witnesses
of `M` in the full parent `P`.  Then

\[
 \rho_X(M)>\alpha+\beta
 \quad\Longrightarrow\quad
 \mu_X^{\alpha,\beta}(M)>0,                         \tag{5.15}
\]

and

\[
 \rho_Y(M)>\gamma+\epsilon
 \quad\Longrightarrow\quad
 \mu_Y^{\gamma,\epsilon}(M)>0.                     \tag{5.16}
\]

#### Proof

The crop deletes `alpha+beta` or `gamma+epsilon` parent positions.  Pairwise
disjoint intervals meeting the deleted set require distinct deleted
positions.  If there are more witnesses than deleted positions, one avoids
the deleted set and lies wholly in the crop.  \(\square\)

Measured relative to `Y[:-1]`, the second deleted set has size
`gamma+epsilon-1`.  For the standard K16 crop, nine disjoint `X`-witnesses
or fourteen disjoint full-`Y` witnesses force survival; within `Y[:-1]`,
thirteen suffice.  Raw occurrence multiplicity gives no such conclusion
because nested witnesses may share one deleted cell.

### Corollary 5.5 (a packing-based sufficient seed condition)

Let

\[
\begin{aligned}
 \mathcal L_X&=\{M\ne\varnothing:
                  \rho_X(M)\le\alpha+\beta\},\\
 \mathcal L_Y&=\{M\ne\varnothing:
                  \rho_Y(M)\le\gamma+\epsilon\}.
\end{aligned}                                        \tag{5.17}
\]

If

\[
                  |\mathcal L_X|+|\mathcal L_Y|+1\le\ell,            \tag{5.18}
\]

then (5.4) has a universal collar completion: assign every residual target
to a distinct collar cell and put that target itself in the cell.

#### Proof

Lemma 5.4 shows that the right side of (5.14) is an upper cover of the
residual family.  It is exact when `Q_1` is nonempty; fixed cross-body
intervals when `Q_1` is empty can only shrink the residual family.  Thus its
size is at most the left side of (5.18).  A singleton collar interval has
fixed OR empty, so one
distinct cell per residual target realizes all of them.  Fill unused cells
with any nonempty mask.  \(\square\)

Condition (5.18) is deliberately strong.  The exact criterion (5.9)--(5.11)
allows one cell to serve many targets through different fixed shores, which
is indispensable for the authenticated K15 crops.

## 6. What the repeat-free width-three deck supplies

Now specialize to `k=2r`, old ground size `2r-1`, and

\[
                         w=\binom{2r-1}{r}.           \tag{6.1}
\]

Assume in this section that `|A|>=4` and `|C|>=3`.  Assume the retained
`D^3X` values are distinct rank-`r` sets.  In the marked
crop `C`, call a retained three-letter start **clean** when its `D^2Y` value
has rank `r-1`.  The retained width-three deck is **repeat-free** when the
clean rank-`(r-1)` values are pairwise distinct.  This definition concerns
the declared cropped starts only; it is not uniqueness among arbitrary-width
witnesses.

Suppose, exhaustively, that every retained `D^2Y` start is either clean or is
one of exactly `j` starts of rank at most `r-2`.  Require every exceptional
start to have its following fourth parent letter retained and its `D^3Y`
value to have rank `r`.  Thus every exception is an interior fixed jump over
the child middle rank; in particular the final retained three-letter start
is clean.  Starts of rank at least `r` are excluded by this hypothesis.

### Proposition 6.1 (exact fixed-deck ledger)

Put

\[
 s=\alpha+\beta+\gamma+\epsilon.                   \tag{6.2}
\]

Under the hypotheses above, the two canonical internal start families
deliver

\[
                         2w+1-s-j                  \tag{6.3}
\]

distinct child middle targets.  Hence `s+j-1` middle targets remain for the
`s+2` source starts outside the two canonical internal families.  In
particular,

\[
                         j\le3                     \tag{6.4}
\]

is necessary for a universal equality-length completion.  If its
first-delivery inventory is ghost-free, exactly `3-j` of those boundary
starts are stalls, jumps, or same-deadline flat extras rather than first
occurrences of new middle targets.

#### Proof

The unmarked crop has `n-alpha-beta-3=w-alpha-beta` internal four-letter
starts, all distinct middle targets.  The marked crop has
`n-gamma-epsilon-2=w+1-gamma-epsilon` internal three-letter starts.  Removing
the `j` jumps leaves that many minus `j` distinct marked middle targets.
Their tag signatures are disjoint, proving (6.3).  The child has `2w` middle
targets, so the missing count is `s+j-1`.

The equality-length word has `2w+3` source starts, while the two internal
families contain `2w+1-s` starts.  Thus `s+2` starts remain.  Each fixed clean
start has already supplied its unique comparable middle value, while a jump
supplies none; every missing middle target needs a distinct remaining start.
This proves (6.4) and the final inventory statement.  \(\square\)

For the authenticated K15 crops,

\[
 (\alpha,\beta,\gamma,\epsilon)=(6,2,7,6),
 \qquad s=21,
 \qquad j=1.                                           \tag{6.5}
\]

The canonical internal families therefore leave exactly twenty-one middle labels to
twenty-three boundary starts, with two boundary waste units.  Seeds 1 and 5
are the two authenticated marked parents whose retained clean rank-seven
deck is repeat-free; each has one retained rank-six jump start.

This is a necessary middle-schedule screen, not a full compiler.  At K16 the
proved global first-delivery theorem excludes ghosts, so retained duplicate
rank-seven values at distinct earliest deadlines rule out the marked parent.
On a general `d=3` plateau, ghost exclusion requires its own numerical or
structural theorem and does not follow from `d=3` alone.

### Corollary 6.2 (combined seed certificate)

Under the collar hypotheses of Section 5, suppose both the exhaustive
clean/jump deck hypotheses of Proposition 6.1 and the packing inequality
(5.18) hold.  Then the seed admits a literal universal equality-length
collar, and its two canonical internal middle-delivery families have the
ledger (6.3).

For the standard K16 crop this concrete sufficient condition is

\[
 \left|\{M\ne\varnothing:\rho_X(M)\le8\}\right|
 +\left|\{M\ne\varnothing:\rho_Y(M)\le13\}\right|+1\le18. \tag{6.6}
\]

#### Proof

Corollary 5.5 constructs the literal collar cells.  Proposition 6.1
independently certifies the displayed fixed-deck ledger.  \(\square\)

The repeat-free hypothesis is deliberately separated from the implication
that creates the collar: (5.18) already suffices for universality, while
repeat-freeness certifies the intended first-delivery schedule.  Section 7
shows that replacing (5.18), or the exact common-core condition, by
repeat-freeness alone is invalid.

## 7. The sharp physical obstruction beyond repeat-freeness

### Lemma 7.1 (oriented-anchor Hall condition)

Let `A` be an equal-rank residual target family.  Assign every legal physical
host interval a key so that intervals sharing one key are nested.  If `K(T)`
is the key set available to target `T`, every collar completion satisfies

\[
 |\mathcal F|
 \le\left|\bigcup_{T\in\mathcal F}K(T)\right|
 \quad\text{for every }\mathcal F\subseteq\mathcal A.                \tag{7.1}
\]

#### Proof

Choose one realizing interval for each target.  Two distinct equal-rank
targets cannot use one key: nested intervals have comparable ORs, whereas
distinct equal-rank masks are incomparable.  The chosen keys are therefore
distinct, and Hall's inequality gives (7.1).  \(\square\)

The smallest abstract obstruction is two equal-rank targets with one common
nested key.  The authenticated physical obstruction is larger but equally
sharp.

### Theorem 7.2 (repeat-free seed-5/self RF495 no-go)

The fixed seed-5/self K16 crop with collar lengths `(4,9,5)` satisfies the
deck hypotheses of Proposition 6.1, yet no assignment of its eighteen
nonzero collar cells is universal.

#### Proof

The complete physical atlas has twenty-one residual rank-eight targets.  A
left-chain host is keyed by one of four physical left starts; middle and
right hosts are keyed by eleven and five physical right ends.  Same-key
intervals are nested, so only twenty oriented anchors exist.  Lemma 7.1
would require `21<=20`, a contradiction.  \(\square\)

This theorem is solver-free and closes the complete fixed seed-5/self RF495
fibre.  It is scoped to that parent, body crop, order, and `4/9/5` layout.
It does not exclude seed 1, a mixed parent pair, another crop, another collar
partition, or an interleaved even word.

Consequently:

- repeat-free `D^2` removes a fixed marked-middle ghost but does not imply
  oriented-anchor Hall;
- oriented-anchor Hall is necessary but not sufficient for collar values;
  the exact sufficient condition is the common-core system
  (5.9)--(5.11); and
- the twenty-one/three-deletion arithmetic is not a construction theorem.

### Proposition 7.3 (authenticated V/V near-completion calibration)

There is an independently replayed V/V `5/9/5` collar word of length
`12874` which realizes all `65535` nonempty K16 masks.  Deleting physical
position `1` gives a length-`12873` V/V `4/9/5` word whose sole missing mask
is

\[
                         H=\mathtt{0x2c6d}.           \tag{7.2}
\]

The shortened word has SHA-256

```text
e4a7ad4ed3041fd8e1fa7e6c1805a2315a2cf5dc811f5897e7b3a29e7c348676.
```

Its fixed bodies and free-window sizes are exactly

\[
 X[6:6436],\qquad z\cup X[7:6432],qquad (4,9,5).     \tag{7.3}
\]

Thus the maximal-core criterion of Theorem 5.2 reduces this fixed fibre to
the following literal question: can its eighteen cells be reassigned so
that some host realizes `H` while every one of the other `65534` masks
retains a host?  Proposition 7.3 alone does not answer that question;
Theorem 7.5 below answers it negatively from an independent deadline
invariant.

#### Audit and comparison

The deletion audit replays the shortened word from every start and obtains
exactly the hole (7.2).  Its top-bit run lengths are

```text
0^6436 1^1 0^3 1^6430 0^1 1^2.
```

The V/V fixed-body residual atlas has sixty targets and a 320-value maximal
closure domain.  The separately authenticated delete-position-1
`collar594` fibre also has sole incumbent hole `0x2c6d`, but has window sizes
`(5,9,4)`, sixty-one residual targets, and a 245-value closure domain.  An
independent invariant audit proves that the two words are not related by a
coordinate permutation, reversal, cyclic reindexing, or renaming of collar
windows.  They are therefore two distinct host geometries sharing one debt
label, not two presentations of one fibre.

This calibration sharpens the role of the seed conditions.  The repeat-free
width-three ledger controls first deliveries, while the disappearance of
`H` after deleting one free cell is a target-specific physical-host failure.
Neither fact determines the other.  In particular, repeat-freeness alone is
not the right positive compression criterion; the simultaneous common-core
condition (5.9)--(5.11), or a genuinely stronger structural implication of
it, remains necessary.

### Lemma 7.4 (architecture-free K16 equality words are ghost-free)

For a K16 word, scan from each left endpoint until its interval OR first has
rank at least eight.  A rank-eight outcome is a first-middle delivery.  If
one rank-eight target is first-delivered at two distinct right deadlines,
the later deadline group is a **ghost extra**.  Let `G` be the number of
ghost extras.

Every universal K16 word of length `L=12873` has

\[
                              G=0.                  \tag{7.4}
\]

#### Proof

Put `W=binom(16,8)=12870`, `e=L-W=3`, and

\[
 \Lambda=\sum_{a=1}^{7}\binom{16}{a}=26332.
\]

The first-delivery deadline inequality gives

\[
                  \Lambda\le(e-G)(L+G).             \tag{7.5}
\]

For completeness, delivery columns have lower-prefix depth at most `e-G`;
if `N` is the number of nondelivery columns, the exact waste inventory gives
`N<=e-G`.  Hence

\[
 \Lambda\le(L-N)(e-G)+Ne
          =L(e-G)+NG
          \le(e-G)(L+G),
\]

which is (7.5).  If `G>=1`, its right side is maximized at `G=1` and equals

\[
                         2(12874)=25748<26332.
\]

Thus `G=0`.  This proof uses no splice or collar architecture.  \(\square\)

### Theorem 7.5 (two complete one-hole collar fibres are impossible)

No reassignment of the eighteen free cells completes either of the following
fixed length-`12873` fibres:

1. the V/V TH495 `4/9/5` fibre of Proposition 7.3;
2. the delete-position-1 `collar594` fibre with word SHA-256
   `a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649`.

#### Proof

In the V/V fibre the immutable triples at zero-based positions
`[11726,11728]` and `[12826,12828]` are

```text
(0x8010,0xc261,0x8269),  cumulative ranks (2,7,8),
(0xc261,0x8231,0xc219),  cumulative ranks (6,7,8).
```

Both cumulative ORs first reach rank eight at their displayed last position,
and both equal `0xc279`.  They are therefore two first-middle deliveries of
one target at the distinct deadlines `11728` and `12828`.

The `collar594` fibre has the same second triple; its first triple is

```text
(0x8010,0x4001,0x8269),  cumulative ranks (2,4,8),
```

and again first-delivers `0xc279` at deadline `11728`.  Its second copy does
so at deadline `12828`.

The free positions are, respectively,

```text
V/V:       [0,4), [6434,6443), [12868,12873),
collar594: [0,5), [6435,6444), [12869,12873).
```

Thus neither triple intersects a free cell.  Every word in either fixed
fibre has `G>=1`, contradicting Lemma 7.4 if it is universal.  \(\square\)

For V/V, this proves that the exact sixty-target maximal-core system is
infeasible even though the displayed assignment satisfies the subsystem
with `0x2c6d` removed.  For `collar594`, it proves the sixty-one-target,
245-value normalized core infeasible.  The conclusion is confined to these
two frozen bodies and editable sets.  It does not prove
`nu(16)>12873`; an equality word may edit a ghost occurrence or use a
different architecture.

### Corollary 7.6 (necessary support enlargement)

Any universal length-`12873` collar extension which retains either fixed
body/order from Theorem 7.5 must make at least one position in

\[
 [11726,11728]\cup[12826,12828]                    \tag{7.6}
\]

editable, and must actually alter the first-delivery data of at least one of
the two triples.  Equivalently, no enlargement confined to positions outside
these six cells can complete either one-hole basin.

#### Proof

If all six positions stay fixed, the two distinct-deadline deliveries of
`0xc279` survive, so `G>=1`; Lemma 7.4 rules out universality.  Merely
declaring a cell editable but leaving its value unchanged does not remove the
same contradiction.  \(\square\)

### Lemma 7.7a (marked-shore ghost inheritance)

Let the retained marked body be `z union Y[gamma:n-epsilon]`.  Suppose two
old parent intervals wholly inside that crop first reach rank `r-1` at
distinct right deadlines and both have union `T`.  Then their marked copies
first reach child rank `r` at the correspondingly shifted distinct deadlines
and both have union `T union {z}`.  If the two copied intervals avoid the
editable support, every collar assignment has `G>=1`.

#### Proof

Every proper old prefix has rank below `r-1`; adjoining `z` raises all these
ranks by one and raises the terminal rank to `r`.  Thus first-delivery status
and the inequality of the two deadlines are preserved by the common physical
shift.  Fixed copied intervals are independent of all collar values.  \(\square\)

For the V parent, the old intervals `[5290,5292]` and `[6390,6392]`
first-deliver `0x4279`.  With `gamma=7`, Lemma 7.7a gives the child ghost
`0xc279` in every standard-crop row whose marked parent is V.  This explains
simultaneously V/V TH495, V/V TH594, and XRF/YV, while their reverse
orientation XV/YRF is not affected.  The S4 row similarly inherits
`0x3cc2` as `0xbcc2`.

### Theorem 7.7 (complete configured-ledger immutable-ghost census)

Consider the twenty-five rows in the frozen raw-splice 18-cell scope ledger.
Twenty-four have either a literal local fixed complement or a fixed
complement determined by an authenticated K15 parent and the crop/window
semantics recorded in that ledger.  The scattered-puncture proposal is the
sole row without a frozen exact support.  For remote-only rows this theorem
audits the recorded configuration, not the provenance of an unavailable
historical solver manifest.

For each of the twenty-four rows, scan every fixed start only until its OR
first reaches rank at least eight or meets a free cell.  Group rank-eight
outcomes by target and physical deadline.  The following five rows have an
immutable target with at least two deadline groups and hence are
solver-free impossible by Lemma 7.4:

| fixed fibre | immutable target | deadlines |
|---|---:|---:|
| seed4/self S4 `4/9/5` | `0xbcc2` | `6483,7583` |
| V/V TH495 `4/9/5` | `0xc279` | `11728,12828` |
| V/V TH594 `5/9/4` | `0xc279` | `11729,12829` |
| two-parent XRF/YV `5/9/4` | `0xc279` | `11729,12829` |
| delete-p1 `collar594` | `0xc279` | `11728,12828` |

The seed5/self RF495 row survives this ghost test but is independently dead
by the `21>20` oriented-anchor theorem.  The other eighteen reconstructed
rows survive both of these particular tests.  “Survives” means only that no
immutable fixed-body ghost was found and no already-recorded anchor theorem
applies; it is not SAT, universality, or a compiler certificate.

All tri-window rows have exactly eighteen free cells, so support cardinality
does not break the tie.  Ordered by the number of targets absent from the two
fixed bodies, the smallest surviving row is

\[
 \boxed{\text{two-parent XV/YRF, crop }(6,2;7,6),
        \text{ windows }(5,9,4),\ |\mathcal R|=64.} \tag{7.7}
\]

The next rows are the four RF/RF optimal trims with `|R|=65`.  The reverse
orientation XRF/YV is dead: placing the repeating V parent on the marked
shore transports its two `0x4279` deliveries to the immutable child ghost
`0xc279`.  This orientation asymmetry is literal and explains why XV/YRF,
not merely an unlabeled RF/V pair, is the smallest surviving architecture.

#### Proof

The scan is the definition of a fixed first-middle delivery: stopping at a
free cell makes the test fail closed, whereas reaching rank eight first
gives an interval unaffected by every collar assignment.  Two deadline
groups for one target force `G>=1`, so Lemma 7.4 excludes the five displayed
rows.  Direct reconstruction checks the authenticated RF495 and S1495 fixed
layout tables cell by cell; the V/V TH495 reconstruction also agrees with
the fixed complement of the authenticated word `e4a7ad4e...`.  Fixed-body
interval replay gives the residual counts in (7.7).  The complete row and
literal occurrence data are frozen in the independent audit artifact named
in Section 9.  \(\square\)

### Proposition 7.8 (unique-bit supports and the canonical live augmentation)

For a fixed first-delivery interval `I=[a,b]` with target `T`, define the
unique contribution of cell `i` by

\[
 U_i(I)=w_i\setminus\bigcup_{j\in I\setminus\{i\}}w_j.              \tag{7.8}
\]

A target-contained edit can change the terminal OR only at a cell with
`U_i(I)` nonempty; an edit before `b` may instead preempt the old deadline.
For every immutable repeated witness in Theorem 7.7, each of its three cells
is either a unique-contribution cell or a proper-prefix cell.  The exact
unique masks are:

| ghost row/copy | unique masks in physical order |
|---|---|
| V/V TH495, first `c279` copy | `0010,4000,0008` |
| V/V TH495, second `c279` copy | `0040,0000,0008` |
| delete-p1, first `c279` copy | `0010,4000,0268` |
| delete-p1, second `c279` copy | `0040,0000,0008` |
| S4, first `bcc2` copy | `0400,0000,2040` |
| S4, second `bcc2` copy | `0480,1040,0800` |

TH594 and XRF/YV have the V/V supports shifted one position to the right.
Consequently the minimum *structural* support augmentation which can break
one of the two immutable deadline groups has cardinality one; its singleton
candidates are the six cells in the two displayed triples.  To erase both
fixed copies before rehosting the target requires one candidate from each
triple and hence cardinality two.  These are support statements, not claims
that every candidate value preserves the rest of the word.

For the authenticated delete-p1 `collar594` one-hole basin, complete literal
replay sharpens the six structural candidates.  Only positions

\[
        11726,\quad 11728,\quad 12826,\quad 12828                 \tag{7.9}
\]

have a value which removes the ghost while preserving every other middle
label.  Their best total hole counts are respectively `5,3,2,5`; positions
`11727,12827` have no such value.  Thus, in this basin, the unique strongest
augmentation is `p=12826`, whose old value `0xc261` uniquely contributes bit
`0x0040` to the second copy.  Exactly the following sixteen normalized values
leave the literal residual pair `{0x2c6d,0xc679}`.  A separate literal replay
of these same sixteen p12826 substitutions in the V/V basin gives the same
pair; no complete six-position ranking is asserted for V/V:

```text
4001 4021 4201 4221 4841 4861 4a41 4a61
c001 c021 c201 c221 c841 c861 ca41 ca61
```

Thus the canonical augmented delete-p1 support

```text
[0,5) union [6435,6444) union {12826} union [12869,12873)
```

is the canonical **PAIR-EXPOSED** 19-cell row.  The V/V analog replaces its
three old windows by `[0,4)`, `[6434,6443)`, and `[12868,12873)` and has the
same sixteen p12826 pair-exposing values.  Neither row is yet PAIR-CLOSED.
For the canonical delete-p1 branch, with p12826 set to any one of these
sixteen values and every original collar cell left at its incumbent value,
the exact common-provider census proves that one further cell cannot close
both named debts: the only eight common assignments act at `p=6437` and all
create the same six new debts

```text
2879 287d a879 a87d c879 e879.
```

The emitted full distributed V/V 19-cell closure master has seventy-two
repair targets, 429 normalized cell values, and no structurally providerless
target, but its simultaneous common-core feasibility remains unproved.
Hence the exact
support classification is

```text
original 18-cell V/V and delete-p1 supports:        DEAD-H2;
add p12826 and use one of 16 values:                PAIR-EXPOSED;
one further edit on the fixed delete-p1 branch:     NO PASS;
distributed 19-cell pair closure:                   UNKNOWN.
```

This classification is independent of the separate smallest surviving
18-cell row XV/YRF from Theorem 7.7.

## 8. Exact proved and conditional boundary

The following statements are unconditional.

1. The self-splice equivalence (0.2), derivative recurrence (3.1), and
   recurrence `nu(k)<=2nu(k-1)` are exact for `k>=2`.
2. The even length formula (3.4) is conditional only on an actual parent of
   length `B(k-1)`.
3. For even `k`, given an actual parent `X` of length `B(k-1)`, if
   `d(k-1)=d(k)=3`, then `B(k)=2|X|-3`.
4. Direct deletion has the exact criterion (4.2); the robust-tail condition
   is sufficient but the fixed-anchor theorem excludes it as a route for the
   canonical K15 splice.
5. The crop arithmetic and maximal-core criterion are a constructive if and
   only if for every fixed three-window seed/layout.
6. Tail occurrence packing bounds the residual family, and (5.18) is a
   literal sufficient seed condition.
7. The fixed-deck ledger and the seed-5/self oriented-anchor obstruction are
   exact in their stated scopes.
8. The V/V `4/9/5` word in Proposition 7.3 is an authenticated one-hole
   equality-length control, not a universal word; its fibre is distinct from
   delete-p1 `collar594`.
9. Lemma 7.4 and the two immutable `0xc279` deliveries prove both complete
   fixed fibres UNSAT without a solver.
10. The complete configured-ledger scan closes three additional rows by an
    immutable ghost (TH594, XRF/YV, and the already-known S4 calibration) and
    selects XV/YRF as the smallest surviving residual atlas.
11. The unique-bit/prefix audit gives the exact six-cell H2 augmentation
    support.  In the delete-p1 basin, `p=12826` is the unique strongest
    one-cell choice; its sixteen best values expose residual
    `{0x2c6d,0xc679}` in both authenticated basins.  Distributed closure of
    that pair remains open.

The following are not proved.

1. A universal K16 word of length 12873.
2. Existence of a maximal-core host selection for seed 1, a mixed parent
   pair other than the excluded XRF/YV orientation, or another crop/partition
   not excluded by Theorems 7.2, 7.5, or 7.7.
3. A WLOG reduction of every even equality word to a doubled splice or an
   eighteen-cell collar.
4. Any implication from repeat-free width three alone to collar completion.
5. A constant-additive even recurrence outside dimensions satisfying the
   explicitly stated deadline plateau.

The verified K15 seed data are used in Proposition 6.1 and the scoped fibre
results in Section 7.  No stalled solver or empirical incumbent is promoted
to a general theorem; all immutable-ghost exclusions use only literal fixed
intervals plus the architecture-free deadline inequality.

## 9. Frozen authentication

```text
scratch/audit_r_k16_raw_splice_immutable_ghost_portfolio_20260731.py
  SHA-256 18f67ffdb54bd99993abdbce4604f8c2e5727e30e8b3a3b665be25ac3146a594
scratch/r_k16_raw_splice_immutable_ghost_portfolio_20260731.audit.json
  SHA-256 7364bb636b0f4f98092eb0a1b1739886f50ba241974723381ee6fe887a08e660
  payload 4adfdf8bb5da08a09663a1883e5514b7581f894f49189c575484f83dc0107315

scratch/k16_vv_th495_deletep1_onehole_20260731.word
  SHA-256 e4a7ad4ed3041fd8e1fa7e6c1805a2315a2cf5dc811f5897e7b3a29e7c348676
scratch/k16_vv_th495_deletep1_onehole_20260731.audit.json
  SHA-256 582d66801ed16884a77fa06a61680839c4eaa59248675f37dbde567ee0e42788
  payload 77ae626864cd5cdbf92c79a04f8a316ba4c7daa3c883be279160bfad104b1e12

scratch/k16_upper12874_best_delete.word
  SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
MATH_AUDIT_K16_MIDDLE_CHAIN_WASTE_PHASE_DUAL_20260730.md
  SHA-256 117c3dbb560c6331dfc09ef9a7bf4ce8cd3923eae5dfa116059a0bc24042ff34
MATH_THEOREM_K_K16_RF495_ORIENTED_ANCHOR_HALL_FIBRE_NOGO_20260730.md
  SHA-256 d1b23b644e484829af12b1e3fcb4b22503f33e9796978e8083f15c2cda460a77

MATH_AUDIT_K16_GHOST_SIX_POSITION_SURGERY_20260731.md
  SHA-256 7296cbbe6af005a6b70b47caf161ca824c31463f7a8151df2cca1affb838b2be
scratch/k16_ghost_six_position_surgery_20260731.audit.json
  SHA-256 ce045d5c55e3bdef782810bd1ef81d8dacbc7bb880e9eacbe7d048aa21e6b8a9
  payload a8f2462944e6d6957cafee2d7b412cecd5912cea7019510c05bb3284fe1c0baa
```

The portfolio checker reads no solver output.  It authenticates all four
parent hashes, reconstructs every ledger crop, cross-checks the complete
RF495 and S1495 fixed-layout tables and the V/V fixed complement, and then
performs the literal fail-closed delivery scan.  Three independent proof
audits checked the splice recurrence, collar/core theorem, ledger counts,
and fixed-ghost implication.
