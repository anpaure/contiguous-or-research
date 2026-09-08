# Integral owner-chainization: a constant-factor theorem and the sharp barrier

Date: 2026-08-01  
Status: unconditional integral constant-factor theorem, exact reductions, and
scoped obstructions.  No `d+O(1)` owner-chain factor or OR chronology is
claimed.

## 0. Verdict

Put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,\qquad
 W=\binom{k}{r},\qquad
 \mathcal L_{<r}=\{S\subseteq[k]:1\le |S|<r\},
\]

\[
 \Lambda=|\mathcal L_{<r}|,qquad
 D=\left\lceil\frac{\Lambda}{W}\right\rceil,
\]

and let `d=d(k)` be the least integer satisfying

\[
 dW+\binom{d+1}{2}\ge \Lambda.
\]

The new fractional theorem in
`MATH_THEOREM_FRACTIONAL_OWNER_CHAINIZATION_EXACT_DEPTH_DPLUS1_20260801.md`
is correct: one chain of length at most `D` per rank-`r` owner covers the
strict lower ideal exactly **fractionally**, and `d<=D<=d+1`.

The integral state is now as follows.

1. There is an unconditional integral owner-chain factor of depth `O(d)`.
   This follows from Tomon's rank-symmetric minimum chain decomposition.
2. Depth `D` (hence `d+O(1)`) is not known.  Such a theorem would imply a
   minimum chain decomposition of the entire Boolean lattice whose largest
   chain is less than three above the average chain size.  This is a very
   strong one-sided uniform-chain statement, far beyond the currently proved
   `Theta(sqrt(k))` maximum.
3. A fixed symmetric-chain decomposition cannot be repaired by merely
   splitting its long lower parts: it needs `Theta(W)` extra chains, whereas
   the OR problem has only `O(d)` boundary chains.
4. Ordinary containment matching does not uncross owner by owner, and the
   owner-chain incidence matrix is not totally unimodular.  Thus neither a
   local lattice uncrossing nor a direct network-flow/TU argument bridges the
   fractional theorem to an integral factor.
5. Even an integral owner-chain factor is only the columnwise part of an OR
   word.  Endpoint serialization still requires the global arrival-clock law
   and the upper interval language.

## 1. Owner-chain factors

An **anchored `h`-chain factor** is a family

\[
 \{C_T:T\in\tbinom{[k]}r\}
\]

such that

* the `C_T` partition `mathcal L_<r`;
* every `C_T` is an inclusion chain;
* every member of `C_T` is contained in `T`; and
* `|C_T|<=h`.

Empty chains are allowed.  This is exactly the integral version of the new
fractional owner-chain theorem, before physical endpoint serialization.

## 2. Unconditional integral chainization at constant-factor depth

### Theorem 2.1 (Tomon gives an anchored `O(d)` factor)

There is an absolute constant `A` such that, for every sufficiently large
`k`, `mathcal L_<r` has an anchored `A d(k)`-chain factor.

Using the numerical form stated in Tomon's rank-symmetric decomposition
theorem, one may take

\[
 |C_T|\le \frac{13}{2}\sqrt{k}+1
       =\bigl(13\sqrt{2/\pi}+o(1)\bigr)d(k),          \tag{2.1}
\]

and therefore `|C_T|<=11d(k)` for all sufficiently large `k`.

#### Proof

Tomon proved that, for all sufficiently large `k`, the Boolean lattice has a
partition into exactly

\[
 W=\binom{k}{\lfloor k/2\rfloor}
\]

rank-symmetric chains, every one of size at most `13 sqrt(k)`.

Every such minimum chain partition has exactly one member of rank `r` in
each chain.  Indeed, the rank-`r` layer has `W` members, a chain meets it at
most once, and there are exactly `W` chains.  Name that member `T`.

Restrict the chain to its nonempty members of rank below `r`.  They form an
inclusion chain contained in `T`, and these restrictions partition
`mathcal L_<r`.

Rank symmetry puts at most half of the full chain strictly below `r` (with a
possible one-element rounding at the centre).  Hence (2.1) follows.  Finally,

\[
 d(k)=\sqrt{\pi k/8}+O(1),
\]

so `(13/2)sqrt(k)+1 <= 11d(k)` eventually.  \(\square\)

Primary source: I. Tomon, *Decompositions of the Boolean lattice into
rank-symmetric chains*, Electron. J. Combin. 23(2) (2016), P2.53,
arXiv:1509.07346.

This theorem is genuinely integral and already includes distinct owner
anchors.  What it does not give is the sharp coefficient one in front of
`d`.

### Proposition 2.2 (in odd dimension anchoring is free)

Let `k=2m+1` and `r=m+1`.  A partition of `mathcal L_<r` into `W` chains of
maximum size `h` can always be turned into an anchored `h`-chain factor.

#### Proof

The lower ideal contains all `W=binom(k,m)` rank-`m` sets.  Since a chain
contains at most one of them, every one of the `W` chains contains exactly
one rank-`m` set, necessarily as its maximum.

The containment graph between rank `m` and rank `m+1` is
`(m+1)`-regular on both shores, and therefore has a perfect matching.  Match
the maximum of every chain to a distinct rank-`r` owner and label the chain
by that owner.  Every lower member of the chain is contained in its maximum,
hence in the matched owner.  \(\square\)

Thus, on the odd subsequence, distinct owner labels create no additional
integrality problem after the bounded chain partition has been found.  The
sharp gate is already the near-equitable chain partition of the truncated
Boolean lattice itself.

## 3. Why depth `D` is a strong uniform-chain theorem

The next result converts a hypothetical sharp owner factor into a chain
partition of the whole Boolean lattice.

For a family `C`, write

\[
 \overline C=\{[k]\setminus S:S\in C\}.
\]

### Theorem 3.1 (full-lattice completion)

Assume `mathcal L_<r` has an anchored `h`-chain factor.

* If `k=2m` is even, `2^[k]` has a partition into `W` chains, each of size at
  most `2h+2`.
* If `k=2m+1` is odd, `2^[k]` has a partition into `W` chains, each of size at
  most `2h+1`.

#### Proof: even case

Here `r=m`, and complementation permutes the middle owners.  For each middle
set `T`, put

\[
 F_T=C_T\ \cup\ \{T\}\ \cup\ \overline{C_{\overline T}}. \tag{3.1}
\]

Every lower member is contained in `T`.  If
`S in C_(overline T)`, then `S subset overline T`, so
`T subset overline S`.  Thus `F_T` is a chain.  The families `F_T` partition
all sets except `emptyset` and `[k]`, and `|F_T|<=2h+1`.

Attach `emptyset` to one chain and `[k]` to a different chain.  This gives
the asserted maximum `2h+2`.

#### Proof: odd case

Write `k=2m+1` and `r=m+1`.  Since there are `W` rank-`m` sets and `W`
owner chains, every `C_T` contains exactly one rank-`m` member; call it
`A_T`.  The map `T mapsto A_T` is a bijection.

Define the permutation `phi` of the owner layer by

\[
                         A_{\phi(T)}=\overline T.     \tag{3.2}
\]

Now put

\[
                         F_T=C_T\cup\overline{C_{\phi(T)}}. \tag{3.3}
\]

The least upper member in the second family is
`overline(A_(phi(T)))=T`, while the greatest lower member in `C_T` is
contained in `T`.  Hence `F_T` is a chain.  Since `phi` is a permutation,
the `F_T` partition every nonempty proper subset of `[k]`, and
`|F_T|<=2h`.  Attach the two extrema to two different chains.  \(\square\)

### Corollary 3.2 (sharp chainization gives maximum below average plus three)

Let

\[
                         s_k=\frac{2^k}{W}
\]

be the average chain size in a minimum `W`-chain decomposition.  If an
anchored `D`-chain factor exists, then `2^[k]` has a minimum chain
decomposition whose largest chain has size strictly less than

\[
                         s_k+3.                       \tag{3.4}
\]

#### Proof

For even `k`,

\[
 \Lambda=\frac{2^k-W}{2}-1,
 \qquad s_k=2\frac{\Lambda}{W}+1+\frac2W.            \tag{3.5}
\]

Theorem 3.1 gives maximum `2D+2`, and

\[
 2D+2-s_k
 =2\left(D-\frac\Lambda W\right)+1-\frac2W<3.       \tag{3.6}
\]

For odd `k`,

\[
 \Lambda=2^{k-1}-1,
 \qquad s_k=2\frac\Lambda W+\frac2W,                \tag{3.7}
\]

and Theorem 3.1 gives maximum `2D+1`; the same calculation again gives a
difference below three.  \(\square\)

Furedi's still-open conjecture asks for every chain size to be either
`floor(s_k)` or `ceil(s_k)`.  Corollary 3.2 is weaker than that conjecture
because it only controls the maximum, but it is much stronger than the
known `Theta(sqrt(k))` maximum and the result that only `1-o(1)` of the
chains are asymptotically average.  Thus `D`-chainization is already a
serious uniform-chain problem; it is not an automatic refinement of Hall's
theorem.

Conversely, Tomon's rank-symmetric version of the Furedi programme would
imply an anchored `d+O(1)` factor simply by restricting each rank-symmetric
chain below its unique owner.  This locates sharp owner-chainization on the
same frontier, while not claiming logical equivalence to Furedi's full
conjecture.

## 4. A fixed SCD cannot be balanced by bounded splitting

Let `mathscr S` be any symmetric-chain decomposition.  If `ell(C)` is the
number of nonempty strict-lower members of one SCD chain, then the exact
overload above depth `h` is

\[
 E_{k,h}=\sum_{C\in\mathscr S}(\ell(C)-h)_+
        =\sum_{j=h+1}^{r-1}\binom{k}{r-j}.           \tag{4.1}
\]

This identity is independent of the chosen SCD.

Splitting a chain of lower length `ell` into pieces of length at most `h`
requires `ceil(ell/h)` pieces.  Therefore the number of extra pieces is at
least

\[
 \sum_C\left(\left\lceil\frac{\ell(C)}h\right\rceil-1\right)_+
 \ge \frac{E_{k,h}}h.                               \tag{4.2}
\]

At `h=D=d+O(1)`, the local central limit theorem gives

\[
 E_{k,D}=\Theta(W\sqrt{k}),\qquad D=\Theta(\sqrt{k}),
\]

and hence (4.2) is `Theta(W)`.  In odd dimension the lower restrictions of
the SCD already give `W` nonempty chains; in even dimension they give
`binom(k,r-1)=W-o(W)` nonempty chains.  Thus every fixed-SCD splitting route
uses

\[
                         W+\Theta(W)                 \tag{4.3}
\]

chains.  The `O(d)` boundary endpoints available in a near-optimal OR word
are negligible on this scale.

So the sharp construction must **rechain globally** across the native SCD
chains.  Splitting, even with optimally placed cuts, cannot prove the target.

## 5. Why ordinary uncrossing and ordinary flow do not round the factor

### Proposition 5.1 (ownerwise uncrossing is false)

There is a complete ideal containment SDR whose targets at one owner are not
nested.

#### Proof

Take `k=5`, `r=3`, `D=2`.  At owner `123`, assign the two incomparable
targets `12` and `13`.  Complete the assignment as follows:

\[
\begin{array}{c|c}
124&1,14\\
125&2,15\\
134&3,34\\
135&5,35\\
145&4,45\\
234&23,24\\
235&25.
\end{array}                                           \tag{5.1}
\]

Together with `123:12,13`, these are all five singletons and all ten pairs,
each in a distinct labelled owner slot and each contained in its owner.
No permutation of the two slots of owner `123` makes its targets a chain.
Thus any valid chainization has to exchange targets **between owners**; it
cannot be obtained by ownerwise sorting or uncrossing.

The usual distributive-lattice replacement also fails on the local pair:

\[
                         12\cap13=1,\qquad 12\cup13=123,
\]

where the union is no longer a strict-lower target and the meet is already
another globally assigned target.  \(\square\)

This proposition does not disprove global reassignment; indeed a different
chainized factor exists at `k=5`.  It proves that global alternating
exchanges are essential.

### Proposition 5.2 (the owner-chain matrix is not TU)

Let `mathfrak C_D(T)` be the chains of length at most `D` among the nonempty
strict subsets of `T`.  The set-partitioning matrix with columns `(T,C)` and
rows lower targets is not totally unimodular once `r>=4` and `D>=2`.

#### Proof

Choose

\[
                         X_1\subset X_2\subset X_3
\]

with all three ranks below `r`, and an owner `T` containing `X_3`.  Consider
the three legal chain columns

\[
                         \{X_1,X_2\},\quad
                         \{X_2,X_3\},\quad
                         \{X_1,X_3\}.
\]

On the three target rows their incidence matrix is

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},                                      \tag{5.2}
\]

whose determinant is `2`.  It is a square minor of the full matrix, even
after owner rows are added.  \(\square\)

Accordingly, the exact integral problem is the hypergraph factor

\[
\begin{aligned}
 &z_{T,C}\in\{0,1\},\\
 &\sum_{C\in\mathfrak C_D(T)}z_{T,C}=1
                    &&(T\in\tbinom{[k]}r),\\
 &\sum_{T,C:S\in C}z_{T,C}=1
                    &&(S\in\mathcal L_{<r}).         \tag{5.3}
\end{aligned}
\]

The fractional theorem gives a symmetric feasible point of (5.3) with
`z>=0`, but Proposition 5.2 blocks a direct bipartite-flow or total-
unimodularity rounding.  It does not prove an integrality gap for the full
Boolean instance; exact integral feasibility remains open.

This failure is consistent with the general complexity boundary.  The
cardinality-restricted chain-cover problem for an arbitrary finite poset is
NP-complete (H. Shum and L. E. Trotter, *Cardinality-restricted chains and
antichains in partially ordered sets*, Discrete Appl. Math. 65 (1996),
421--439).  Therefore any positive flow theorem here has to use the full
Boolean symmetry; it cannot be a generic bounded-chain version of
Dilworth's theorem.

## 6. Endpoint serialization is a separate gate

An integral solution of (5.3) gives one nested lower chain under each owner.
It still does not produce a word.

For a physical central chronology `(T_i)`, local arrival clocks must satisfy

\[
 x\in T_i\cap T_{i+1},\quad a_i(x)>0
       \quad\Longrightarrow\quad a_{i+1}(x)=a_i(x)-1. \tag{6.1}
\]

Independent owner chains impose no such compatibility.  Equivalently, a
word supplies two endpoint chain partitions, not one: fixed-left and
fixed-right witnesses must be orthogonal, their precedence digraphs must be
acyclic, their cells must fit the short diagonal band, and the coordinate
pin sets must survive.  These are the exact additional tests in
`MATH_THEOREM_ORDERED_ORTHOGONAL_CHAIN_BAND_EMBEDDING_20260731.md`.

Thus the honest implication chain is

\[
\boxed{
 \text{fractional owner chains (proved at }D)
 \longrightarrow
 \text{integral owner chains (proved only at }O(d))
 \longrightarrow
 \text{endpoint serialization (open).}}
\]

## 7. Shortest next target

The clean integral target is not another containment Hall inequality.  It is
one of the following genuinely stronger statements.

1. **Sharp factor theorem.**  Prove that (5.3) has an integral solution at
   `D` (or at `d+C`) for the Boolean lower ideal.
2. **Absorbing rounding theorem.**  Round the symmetric fractional factor
   while leaving only `O(1)` lower targets, then absorb them by a bounded
   number of global owner exchanges.
3. **Serialized theorem.**  Construct the factor together with a second
   orthogonal endpoint partition satisfying (6.1), rather than trying to
   serialize an arbitrary terminal factor afterward.

The first target alone would already be a strong new Boolean-lattice
uniform-chain theorem.  The third is what the OR problem ultimately needs.
